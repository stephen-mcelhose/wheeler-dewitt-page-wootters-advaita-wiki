#!/usr/bin/env python3
"""Verify an explorer candidate uses the generated canonical learning path."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".agents"))
from generate_learning_order import parse_learning_order  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact", type=Path)
    args = parser.parse_args()
    try:
        expected = parse_learning_order()
        artifact = json.loads(args.artifact.read_text(encoding="utf-8"))
        code = artifact["code"]
        data = artifact["files"]["/data.ts"]["code"]
    except (OSError, KeyError, TypeError, json.JSONDecodeError, ValueError) as error:
        print(f"learning-navigation validation failed: {error}", file=sys.stderr)
        return 2
    match = re.search(r"export const learningOrder:string\[\]=(\[[^;]*\]);", data)
    if not match:
        print("learning-navigation validation failed: artifact lacks typed learningOrder", file=sys.stderr)
        return 1
    try:
        actual = json.loads(match.group(1))
    except json.JSONDecodeError as error:
        print(f"learning-navigation validation failed: malformed artifact learningOrder: {error}", file=sys.stderr)
        return 1
    errors = []
    if actual != expected:
        errors.append("artifact learningOrder does not exactly match parsed overview-learning-path.md")
    required = (
        "learningOrder.indexOf(selected.id)",
        "learningOrder[learningAt-1]",
        "learningOrder[learningAt+1]",
    )
    for token in required:
        if token not in code:
            errors.append(f"reader does not use generated learning navigation token: {token}")
    forbidden = (
        "concepts[at-1]",
        "concepts[at+1]",
        "concepts[at - 1]",
        "concepts[at + 1]",
    )
    for token in forbidden:
        if token in code:
            errors.append(f"reader retains artifact-array positional navigation: {token}")
    if errors:
        print("learning-navigation validation failed:\n- " + "\n- ".join(errors), file=sys.stderr)
        return 1
    print(f"learning-navigation validation passed: {len(actual)} ordered concepts; unlabeled controls use learningOrder only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
