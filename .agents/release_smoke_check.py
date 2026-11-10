#!/usr/bin/env python3
"""Deterministic release check for optional explorer domain buckets.

Rejects direct property access on grouped/domain bucket maps. Such maps may omit
an optional category, so render code must use a bracket lookup with an explicit
array fallback (for example, ``grouped[group] ?? []``).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

MAP_NAMES = r"(?:grouped|buckets|categories|domains)"
# A direct property lookup cannot provide a missing-bucket array fallback.
UNSAFE_DOT_ACCESS = re.compile(rf"\b{MAP_NAMES}\s*\.\s*[A-Za-z_$][\w$]*")
# Known optional categories accessed through a literal key must contain an
# explicit fallback in the same expression. This catches the bracket variant
# while allowing safe forms such as ``grouped['philosophy'] ?? []``.
OPTIONAL_LITERAL = re.compile(
    rf"\b{MAP_NAMES}\s*\[\s*['\"](?:philosophy|mathematics|physics|page-wootters|pageWootters)['\"]\s*\](?!\s*(?:\?\?|\|\|)\s*\[)"
)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("artifact", type=Path, help="ReactComponent artifact JSON to inspect")
    args = parser.parse_args()
    try:
        artifact = json.loads(args.artifact.read_text(encoding="utf-8"))
        source = artifact["code"]
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as error:
        print(f"release smoke-check: cannot read App source: {error}", file=sys.stderr)
        return 2

    violations = []
    for pattern, reason in ((UNSAFE_DOT_ACCESS, "direct optional bucket access"), (OPTIONAL_LITERAL, "literal optional bucket access without [] fallback")):
        for match in pattern.finditer(source):
            line = source.count("\n", 0, match.start()) + 1
            violations.append(f"line {line}: {reason}: {match.group(0)}")
    if violations:
        print("release smoke-check failed:", file=sys.stderr)
        print("\n".join(violations), file=sys.stderr)
        return 1
    print("release smoke-check passed: optional domain buckets have no unsafe direct access")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
