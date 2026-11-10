#!/usr/bin/env python3
"""Generate the canonical learning-order artifact from overview-learning-path.md."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "overview-learning-path.md"
OUTPUT = ROOT / ".agents" / "generated" / "learning-order.json"
CONTENT_DIRS = ("mathematics", "physics", "page-wootters", "philosophy")
LIST_ITEM = re.compile(r"^\s*\d+\.\s+\[[^\]]+\]\(([^)]+)\)\s*$")
FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)


def metadata(path: Path) -> dict:
    match = FRONTMATTER.match(path.read_text(encoding="utf-8"))
    if not match:
        raise ValueError(f"{path.relative_to(ROOT)}: missing JSON frontmatter")
    try:
        return json.loads(match.group(1))
    except json.JSONDecodeError as error:
        raise ValueError(f"{path.relative_to(ROOT)}: invalid JSON frontmatter: {error}") from error


def canonical_concepts() -> dict[str, Path]:
    concepts: dict[str, Path] = {}
    for directory in CONTENT_DIRS:
        for path in sorted((ROOT / directory).glob("*.md")):
            data = metadata(path)
            if data.get("type") != "concept":
                continue
            concept_id = data.get("id")
            if not isinstance(concept_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", concept_id):
                raise ValueError(f"{path.relative_to(ROOT)}: invalid canonical concept ID")
            if concept_id in concepts:
                raise ValueError(f"duplicate canonical concept ID: {concept_id}")
            concepts[concept_id] = path
    return concepts


def parse_learning_order() -> list[str]:
    concepts = canonical_concepts()
    order: list[str] = []
    seen_ids: set[str] = set()
    seen_paths: set[Path] = set()
    for line_number, line in enumerate(SOURCE.read_text(encoding="utf-8").splitlines(), 1):
        match = LIST_ITEM.match(line)
        if not match:
            continue
        target = match.group(1)
        if "://" in target or target.startswith("#"):
            raise ValueError(f"overview-learning-path.md:{line_number}: learning links must be local concept links")
        path = (SOURCE.parent / target).resolve()
        if path.suffix != ".md" or not path.exists():
            raise ValueError(f"overview-learning-path.md:{line_number}: unresolved learning link: {target}")
        data = metadata(path)
        if data.get("type") != "concept":
            raise ValueError(f"overview-learning-path.md:{line_number}: link does not target a canonical concept: {target}")
        concept_id = data.get("id")
        if concept_id not in concepts or concepts[concept_id].resolve() != path:
            raise ValueError(f"overview-learning-path.md:{line_number}: unresolved canonical concept ID: {concept_id}")
        if concept_id in seen_ids or path in seen_paths:
            raise ValueError(f"overview-learning-path.md:{line_number}: duplicate listed concept: {concept_id}")
        seen_ids.add(concept_id)
        seen_paths.add(path)
        order.append(concept_id)
    if not order:
        raise ValueError("overview-learning-path.md: malformed or empty learning sequence")
    missing = sorted(set(concepts) - seen_ids)
    extra = sorted(seen_ids - set(concepts))
    if missing or extra:
        raise ValueError(f"learning sequence must include every canonical concept exactly once; missing={missing}, extra={extra}")
    positions = {concept_id: index for index, concept_id in enumerate(order)}
    for concept_id, path in concepts.items():
        for parent in metadata(path).get("parents", []):
            if parent not in positions:
                raise ValueError(f"{concept_id}: declared prerequisite is missing from learning sequence: {parent}")
            if positions[parent] >= positions[concept_id]:
                raise ValueError(f"{concept_id}: prerequisite appears after concept in learning sequence: {parent}")
    return order


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--check", action="store_true", help="fail if the generated artifact differs")
    args = parser.parse_args()
    try:
        order = parse_learning_order()
        payload = {"pathId": "learning", "source": "overview-learning-path.md", "learningOrder": order}
        rendered = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
        if args.check:
            if not args.output.exists() or args.output.read_text(encoding="utf-8") != rendered:
                raise ValueError(f"generated learning-order artifact is absent or stale: {args.output}")
        else:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(rendered, encoding="utf-8")
        print(f"learning-order passed: {len(order)} canonical concepts")
        return 0
    except ValueError as error:
        print(f"learning-order failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
