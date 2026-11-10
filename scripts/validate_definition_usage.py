#!/usr/bin/env python3
"""Validate required first-use consumers for reusable definition nodes.

This source-only gate prevents a definition from being counted as added while it
is absent from the intended reader-facing concept pages. The governed set lives
in .agents/required-definition-usage.json. Definitions outside that manifest
may be intentionally glossary-only or legacy terms; adding them to the manifest
turns their declared consumers into release requirements.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from annotation_transform import EXPLICIT_RE, parse_frontmatter, transform  # noqa: E402

MANIFEST = ROOT / ".agents" / "required-definition-usage.json"
CONTENT_DIRS = ("mathematics", "physics", "page-wootters", "philosophy")


def concept_sources() -> dict[str, tuple[Path, dict, str]]:
    sources: dict[str, tuple[Path, dict, str]] = {}
    for directory in CONTENT_DIRS:
        for path in sorted((ROOT / directory).glob("*.md")):
            metadata, body = parse_frontmatter(path.read_text(encoding="utf-8"))
            sources[metadata["id"]] = (path, metadata, body)
    return sources


def definition_ids() -> set[str]:
    ids: set[str] = set()
    for path in (ROOT / "definitions").glob("def-*.md"):
        metadata, _ = parse_frontmatter(path.read_text(encoding="utf-8"))
        ids.add(metadata["id"])
    return ids


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    required: dict[str, list[str]] = manifest["definitions"]
    concepts = concept_sources()
    definitions = definition_ids()
    errors: list[str] = []

    for definition_id, consumer_ids in required.items():
        if definition_id not in definitions:
            errors.append(f"required definition is missing: {definition_id}")
            continue
        if not consumer_ids:
            errors.append(f"required definition has no declared consumers: {definition_id}")
        for concept_id in consumer_ids:
            if concept_id not in concepts:
                errors.append(f"{definition_id}: declared consumer concept is missing: {concept_id}")
                continue
            path, metadata, body = concepts[concept_id]
            schema = metadata.get("inline_definitions", [])
            schema_ids = [item.get("definition_id") for item in schema]
            if definition_id not in schema_ids:
                errors.append(f"{definition_id}: {path.relative_to(ROOT)} lacks inline_definitions schema consumer")
                continue
            transformed, report = transform(path.read_text(encoding="utf-8"))
            if report.unmatched:
                errors.append(f"{definition_id}: {path.relative_to(ROOT)} has unmatched schema entries: {report.unmatched}")
                continue
            explicit_ids = [item[0] for item in EXPLICIT_RE.findall(body)]
            transformed_body = parse_frontmatter(transformed)[1]
            token_count = transformed_body.count("{{def:" + definition_id + "|")
            if token_count != 1:
                errors.append(f"{definition_id}: {path.relative_to(ROOT)} must resolve exactly one first-use annotation; found {token_count}")
            if definition_id in explicit_ids and token_count != 1:
                errors.append(f"{definition_id}: explicit annotation resolution failure in {path.relative_to(ROOT)}")

    if errors:
        print("DEFINITION USAGE VALIDATION FAILED")
        for error in errors:
            print("- " + error)
        return 1
    print(f"definition usage validation passed: {len(required)} governed definitions")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
