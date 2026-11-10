#!/usr/bin/env python3
"""Reconcile canonical source counts against the approved expected-count snapshot.

Exit 0 when equal. Exit 3 for any mismatch so the caller must ask the user
before updating expected-source-counts.json or generating a content preview.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


NODE_TYPES = ("concept", "definition", "example", "guide")


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"count reconciliation failed: cannot read {path}: {error}", file=sys.stderr)
        raise SystemExit(2)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-index", type=Path, required=True)
    parser.add_argument("--expected", type=Path, required=True)
    args = parser.parse_args()

    index = load_json(args.source_index)
    expected_document = load_json(args.expected)
    nodes = index.get("nodes")
    expected = expected_document.get("counts")
    if not isinstance(nodes, list) or not isinstance(expected, dict):
        print("count reconciliation failed: invalid source index or expected-count schema", file=sys.stderr)
        return 2

    actual = {kind: sum(1 for node in nodes if node.get("type") == kind) for kind in NODE_TYPES}
    actual["total"] = len(nodes)
    expected_counts = {kind: expected.get(kind) for kind in (*NODE_TYPES, "total")}
    if any(not isinstance(value, int) for value in expected_counts.values()):
        print("count reconciliation failed: expected counts must be integers", file=sys.stderr)
        return 2

    deltas = {kind: actual[kind] - expected_counts[kind] for kind in actual}
    if all(delta == 0 for delta in deltas.values()):
        print("count reconciliation passed: source counts equal approved expected counts")
        print(json.dumps({"expected": expected_counts, "actual": actual}, sort_keys=True))
        print("PROCESS CHECK: before generating a preview, confirm whether this work intentionally added or removed a concept, definition, example, or guide. If yes, investigate why the count is unchanged and record the reconciliation decision.")
        return 0

    direction = "more" if actual["total"] > expected_counts["total"] else "less"
    prompt = (
        "SOURCE COUNT MISMATCH — user decision required before continuing.\n"
        f"Expected: {expected_counts}\n"
        f"Actual:   {actual}\n"
        f"Direction: {direction}\n\n"
    )
    if direction == "more":
        prompt += "Ask the user: 'Did I intentionally add a concept, definition, example, or guide? Should I update expected counts?' If no, fail hard and investigate. If yes, update expected-source-counts.json after confirming the additions."
    else:
        prompt += "Ask the user: 'Did I intentionally remove a concept, definition, example, or guide? Should I update expected counts?' If no, fail hard and investigate. If yes, update expected-source-counts.json after confirming the removals."
    print(prompt, file=sys.stderr)
    return 3


if __name__ == "__main__":
    raise SystemExit(main())
