#!/usr/bin/env python3
"""Pure Markdown annotation transformer for source-level definition schemas.

This tool intentionally does not read, write, or publish the React explorer.
It converts eligible first prose occurrences into explicit definition annotations:
    {{def:definition-id|Visible term}}

The output is a review artifact for later renderer wiring.  Existing Markdown,
math, links, headings, code, citations, and warning/caveat blocks are preserved.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

EXPLICIT_RE = re.compile(r"\{\{def:([^|}]+)\|([^}]+)\}\}")
INLINE_MATH_RE = re.compile(r"\\\([\s\S]*?\\\)")
INLINE_CODE_RE = re.compile(r"`[^`]*`")
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]*)\)")
REFERENCE_LINK_RE = re.compile(r"\[[^\]]+\]")


@dataclass(frozen=True)
class InlineDefinition:
    definition_id: str
    term: str


@dataclass(frozen=True)
class TransformReport:
    page_id: str
    applied: tuple[InlineDefinition, ...]
    unmatched: tuple[InlineDefinition, ...]
    explicit_annotations: int


def parse_frontmatter(markdown: str) -> tuple[dict, str]:
    if not markdown.startswith("---\n"):
        raise ValueError("Expected JSON frontmatter beginning with '---'.")
    end = markdown.find("\n---\n", 4)
    if end < 0:
        raise ValueError("Could not locate closing frontmatter delimiter.")
    metadata = json.loads(markdown[4:end])
    return metadata, markdown[end + 5 :]


def render_frontmatter(metadata: dict, body: str) -> str:
    return "---\n" + json.dumps(metadata, indent=2, ensure_ascii=False) + "\n---\n" + body


def with_schema(markdown: str, schema: Iterable[InlineDefinition]) -> str:
    """Return source with a schema added, preserving the body byte-for-byte."""
    metadata, body = parse_frontmatter(markdown)
    metadata["inline_definitions"] = [
        {"definition_id": item.definition_id, "term": item.term, "occurrence": "first"}
        for item in schema
    ]
    return render_frontmatter(metadata, body)


def schema_from_frontmatter(markdown: str) -> tuple[dict, str, tuple[InlineDefinition, ...]]:
    metadata, body = parse_frontmatter(markdown)
    raw_schema = metadata.get("inline_definitions", [])
    schema: list[InlineDefinition] = []
    for item in raw_schema:
        if item.get("occurrence", "first") != "first":
            raise ValueError(f"Unsupported occurrence policy: {item!r}")
        definition_id = item.get("definition_id")
        term = item.get("term")
        if not isinstance(definition_id, str) or not definition_id:
            raise ValueError(f"Missing definition_id: {item!r}")
        if not isinstance(term, str) or not term.strip():
            raise ValueError(f"Missing term: {item!r}")
        schema.append(InlineDefinition(definition_id, term))
    return metadata, body, tuple(schema)


def split_protected(text: str) -> list[tuple[bool, str]]:
    """Split one prose line into annotatable and protected segments.

    This deliberately uses finditer instead of re.split: the protective patterns
    contain internal capture groups, and re.split would leak those groups into
    the returned sequence.
    """
    explicit_pattern = r"\{\{def:[^|}]+\|[^}]+\}\}"
    combined = re.compile(
        "|".join(
            [
                INLINE_MATH_RE.pattern,
                INLINE_CODE_RE.pattern,
                MARKDOWN_LINK_RE.pattern,
                REFERENCE_LINK_RE.pattern,
                explicit_pattern,
            ]
        )
    )
    segments: list[tuple[bool, str]] = []
    cursor = 0
    for match in combined.finditer(text):
        if cursor < match.start():
            segments.append((True, text[cursor : match.start()]))
        segments.append((False, match.group(0)))
        cursor = match.end()
    if cursor < len(text):
        segments.append((True, text[cursor:]))
    return segments


def annotate_eligible_text(text: str, pending: list[InlineDefinition]) -> tuple[str, list[InlineDefinition]]:
    remaining = list(pending)
    result = text
    for item in tuple(remaining):
        pattern = re.compile(r"(?<![\w-])" + re.escape(item.term) + r"(?![\w-])", re.IGNORECASE)
        match = pattern.search(result)
        if match is None:
            continue
        visible = match.group(0)
        annotation = "{{def:" + item.definition_id + "|" + visible + "}}"
        result = result[: match.start()] + annotation + result[match.end() :]
        remaining.remove(item)
    return result, remaining


def convert_definition_links(text: str, pending: list[InlineDefinition]) -> tuple[str, list[InlineDefinition], list[InlineDefinition]]:
    """Convert only schema-declared links into definitions.

    A source link to ../definitions/def-*.md is a legacy definition link, not an
    ordinary navigation link. It is deliberately converted to an inline
    definition annotation when its visible label matches the page schema. All
    other Markdown links remain untouched and link-styled.
    """
    remaining = list(pending)
    converted: list[InlineDefinition] = []

    def replace(match: re.Match[str]) -> str:
        nonlocal remaining
        label, destination = match.group(1), match.group(2)
        if "/definitions/def-" not in destination:
            return match.group(0)
        for item in tuple(remaining):
            if label.casefold() == item.term.casefold():
                remaining.remove(item)
                converted.append(item)
                return "{{def:" + item.definition_id + "|" + label + "}}"
        return match.group(0)

    return MARKDOWN_LINK_RE.sub(replace, text), remaining, converted


def transform(markdown: str) -> tuple[str, TransformReport]:
    metadata, body, schema = schema_from_frontmatter(markdown)
    explicit_ids = {definition_id for definition_id, _ in EXPLICIT_RE.findall(body)}
    pending = [item for item in schema if item.definition_id not in explicit_ids]
    applied: list[InlineDefinition] = []
    explicit_annotations = len(EXPLICIT_RE.findall(body))
    output: list[str] = []
    in_fence = False
    in_display_math = False

    for line in body.splitlines(keepends=True):
        raw = line.rstrip("\n")
        newline = "\n" if line.endswith("\n") else ""

        if raw.startswith("```"):
            in_fence = not in_fence
            output.append(raw + newline)
            continue
        if raw == "\\[":
            in_display_math = True
            output.append(raw + newline)
            continue
        if raw == "\\]":
            in_display_math = False
            output.append(raw + newline)
            continue
        if (
            in_fence
            or in_display_math
            or raw.startswith("#")
            or raw.startswith(">")
            or raw.startswith("[^" )
            or raw.startswith("    ")
        ):
            output.append(raw + newline)
            continue

        raw, pending, converted = convert_definition_links(raw, pending)
        applied.extend(converted)
        rebuilt: list[str] = []
        for eligible, segment in split_protected(raw):
            if not eligible or not pending:
                rebuilt.append(segment)
                continue
            annotated, remaining = annotate_eligible_text(segment, pending)
            newly_applied = [item for item in pending if item not in remaining]
            applied.extend(newly_applied)
            pending = remaining
            rebuilt.append(annotated)
        output.append("".join(rebuilt) + newline)

    transformed = render_frontmatter(metadata, "".join(output))
    report = TransformReport(
        page_id=metadata["id"],
        applied=tuple(applied),
        unmatched=tuple(pending),
        explicit_annotations=explicit_annotations,
    )
    return transformed, report


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate schema-annotation Markdown output without wiring the explorer.")
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()

    source = args.source.read_text(encoding="utf-8")
    transformed, report = transform(source)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(transformed, encoding="utf-8")
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(
        json.dumps(
            {
                "page_id": report.page_id,
                "applied": [item.__dict__ for item in report.applied],
                "unmatched": [item.__dict__ for item in report.unmatched],
                "explicit_annotations": report.explicit_annotations,
            },
            indent=2,
        ) + "\n",
        encoding="utf-8",
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
