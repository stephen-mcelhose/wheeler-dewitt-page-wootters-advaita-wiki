#!/usr/bin/env python3
"""Reject sentinel data modules and require complete parseable Explorer payloads."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

# Keep this list explicit and version-controlled. Add any build-system sentinel here.
INVALID_PLACEHOLDER_SENTINELS = (
    "PLACEHOLDER",
    "__PLACEHOLDER__",
    "{{PLACEHOLDER}}",
    "TODO_DATA",
    "__DATA_PENDING__",
)
REQUIRED_ARRAY_EXPORTS = (
    "concepts:Concept[]",
    "definitions:Definition[]",
    "examples:Concept[]",
    "globalReferences:Concept[]",
    "learningOrder:string[]",
)


def fail(message: str) -> None:
    raise ValueError(message)


def artifact_data(artifact: dict[str, Any], label: str) -> str:
    try:
        data = artifact["files"]["/data.ts"]["code"]
    except (KeyError, TypeError) as error:
        fail(f"{label} is missing files['/data.ts']['code']: {error}")
    if not isinstance(data, str):
        fail(f"{label} /data.ts code must be a string")
    return data


def array_after(source: str, marker: str) -> list[Any]:
    start = source.find(marker)
    if start < 0:
        fail(f"/data.ts is missing required export {marker}")
    try:
        value, _ = json.JSONDecoder().raw_decode(source[start + len(marker):])
    except json.JSONDecodeError as error:
        fail(f"cannot parse {marker} payload: {error}")
    if not isinstance(value, list) or not value:
        fail(f"{marker} must be a nonempty array")
    return value


def validate_data_source(data: str, label: str) -> dict[str, int]:
    for sentinel in INVALID_PLACEHOLDER_SENTINELS:
        if sentinel in data:
            fail(f"{label} /data.ts contains forbidden placeholder sentinel {sentinel!r}")
    if not data.strip():
        fail(f"{label} /data.ts is empty")
    arrays = {name: array_after(data, f"export const {name}=") for name in REQUIRED_ARRAY_EXPORTS}
    total = re.search(r"export const totalNodes=(\d+);", data)
    if not total:
        fail(f"{label} /data.ts is missing numeric totalNodes")
    if any(not isinstance(item, dict) or not str(item.get("body", "")).strip() for item in arrays["concepts:Concept[]"]):
        fail(f"{label} concepts payload has an empty canonical body")
    if any(not isinstance(item, dict) or not str(item.get("body", "")).strip() for item in arrays["examples:Concept[]"]):
        fail(f"{label} examples payload has an empty canonical body")
    if any(not isinstance(item, dict) or not str(item.get("body", "")).strip() for item in arrays["globalReferences:Concept[]"]):
        fail(f"{label} global references payload has an empty canonical body")
    return {
        "concepts": len(arrays["concepts:Concept[]"]),
        "definitions": len(arrays["definitions:Definition[]"]),
        "examples": len(arrays["examples:Concept[]"]),
        "globalReferences": len(arrays["globalReferences:Concept[]"]),
        "learningOrder": len(arrays["learningOrder:string[]"]),
        "totalNodes": int(total.group(1)),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifact", type=Path)
    parser.add_argument("--label", default="candidate")
    args = parser.parse_args()
    try:
        artifact = json.loads(args.artifact.read_text(encoding="utf-8"))
        counts = validate_data_source(artifact_data(artifact, args.label), args.label)
    except (OSError, TypeError, json.JSONDecodeError, ValueError) as error:
        print(f"Explorer data payload gate failed: {error}", file=sys.stderr)
        return 1
    print("Explorer data payload gate passed: " + ", ".join(f"{key}={value}" for key, value in counts.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
