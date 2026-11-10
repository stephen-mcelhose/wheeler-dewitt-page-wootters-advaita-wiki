#!/usr/bin/env python3
"""Generate the normal-reader TypeScript data module from canonical wiki data.

Usage from the repository root:
    python3 scripts/generate_web_data.py

Input:
    viewer/wiki-data.json
    .agents/generated/learning-order.json (when present)

Output:
    web/src/data.ts

The reader template imports this module. Canonical bodies, metadata, sources,
relationships, and annotations remain data; this generator never changes App.tsx.

Body pre-processing
-------------------
If a node has a ``body_markdown`` field (produced by a future annotation pipeline),
that is used as-is. Otherwise the raw ``body`` is used after converting legacy
definition links of the form ``[label](../definitions/def-id.md)`` to the inline
annotation format ``{{def:id|label}}`` that the reader understands.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "viewer" / "wiki-data.json"
DEFAULT_OUTPUT = ROOT / "web" / "src" / "data.ts"
DEFAULT_ORDER = ROOT / ".agents" / "generated" / "learning-order.json"

# Matches [label](any/path/def-some-id.md)
_DEF_LINK_RE = re.compile(r"\[([^\]]+)\]\([^)]*\/def-([^).]+)\.md\)")


def convert_def_links(body: str) -> str:
    """Convert legacy definition markdown links to inline annotation syntax.

    [ket](../definitions/def-ket.md)  →  {{def:ket|ket}}
    """
    return _DEF_LINK_RE.sub(
        lambda m: "{{def:" + m.group(2) + "|" + m.group(1) + "}}", body
    )


def load_learning_order(path: Path, concept_ids: set[str]) -> list[str]:
    if path.exists():
        value = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(value, dict):
            for key in ("learningOrder", "learning_order", "order", "ids"):
                if isinstance(value.get(key), list):
                    value = value[key]
                    break

        if not isinstance(value, list) or not all(
            isinstance(item, str) for item in value
        ):
            raise ValueError(f"Unsupported learning-order payload: {path}")

        missing = sorted(set(value) - concept_ids)
        if missing:
            raise ValueError(
                f"Learning order references missing concepts: {missing}"
            )

        return value

    return sorted(concept_ids)


def group_for(path: str, node_type: str) -> tuple[str, bool]:
    if node_type == "guide":
        return "Global References", False
    if path.startswith("mathematics/"):
        return "Mathematical Foundations", False
    if path.startswith("physics/"):
        return "Canonical Gravity & Problem of Time", False
    if path.startswith("page-wootters/"):
        return "Page\u2013Wootters", False
    if path.startswith("philosophy/"):
        return "Optional Philosophy", True
    if node_type == "example":
        return "Worked Examples", False
    return "Definitions", False


def ts(value: object) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--learning-order", type=Path, default=DEFAULT_ORDER)
    args = parser.parse_args()

    payload = json.loads(args.input.read_text(encoding="utf-8"))
    nodes = payload.get("nodes")
    if not isinstance(nodes, list):
        raise ValueError("Expected a nodes array in wiki-data.json")

    concepts: list[dict] = []
    examples: list[dict] = []
    references: list[dict] = []
    definitions: list[dict] = []

    for raw in nodes:
        if not isinstance(raw, dict):
            raise ValueError("Every node must be an object")

        node = dict(raw)
        kind = node.get("type")
        path = node.get("path", "")
        group, philosophy = group_for(path, kind)

        if kind == "definition":
            # Definitions are inline popup text — convert def links in body too
            body = node.get("body_markdown", node.get("body", ""))
            body = convert_def_links(body)
            definitions.append({
                "id": str(node["id"]).removeprefix("def-"),
                "title": node["title"],
                "text": body,
                "target": next(
                    (
                        r.get("target")
                        for r in node.get("relationships", [])
                        if r.get("type") == "related-to"
                    ),
                    None,
                ),
            })
            continue

        if kind not in {"concept", "example", "guide"}:
            continue

        # body_markdown is the reader-facing transformed body.
        # Fall back to body, then convert any legacy definition links.
        body = node.get("body_markdown", node.get("body", ""))
        body = convert_def_links(body)

        node["body"] = body
        node["status"] = node.get("review_status", "draft")
        node["kind"] = kind
        node["group"] = group
        node["philosophy"] = philosophy
        node.setdefault("parents", [])
        node.setdefault("relationships", [])
        node.setdefault("sources", [])

        if kind == "concept":
            concepts.append(node)
        elif kind == "example":
            examples.append(node)
        else:
            references.append(node)

    concepts.sort(key=lambda n: n["title"])
    examples.sort(key=lambda n: n["title"])
    references.sort(key=lambda n: n["title"])
    definitions.sort(key=lambda n: n["title"])

    learning_order = load_learning_order(
        args.learning_order,
        {n["id"] for n in concepts},
    )

    total = len(concepts) + len(examples) + len(references) + len(definitions)

    source = """\
// GENERATED FILE — do not edit by hand.
// Source: viewer/wiki-data.json via scripts/generate_web_data.py

export type Definition = {
  id: string;
  title: string;
  text: string;
  target?: string;
};

export type Relationship = {
  type: string;
  target: string;
  note?: string;
};

export type Source = {
  title: string;
  url: string;
  persistent_id?: string;
};

export type Concept = {
  id: string;
  title: string;
  summary: string;
  status: string;
  path: string;
  group: string;
  philosophy: boolean;
  body: string;
  parents: string[];
  relationships: Relationship[];
  sources: Source[];
  kind?: "concept" | "example" | "guide";
  metadata?: Record<string, unknown>;
  [key: string]: unknown;
};

"""

    source += f"export const totalNodes = {total};\n"
    source += f"export const definitions: Definition[] = {ts(definitions)};\n"
    source += f"export const concepts: Concept[] = {ts(concepts)};\n"
    source += f"export const examples: Concept[] = {ts(examples)};\n"
    source += f"export const globalReferences: Concept[] = {ts(references)};\n"
    source += f"export const learningOrder: string[] = {ts(learning_order)};\n"

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(source, encoding="utf-8")

    print(f"Generated {args.output.relative_to(ROOT)}")
    print(
        f"concepts={len(concepts)} definitions={len(definitions)} "
        f"examples={len(examples)} guides={len(references)} total={total}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
