#!/usr/bin/env python3
"""Validate the static Explorer candidate against its generated source manifest."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "viewer" / "explorer-manifest.json"
DATA = ROOT / "viewer" / "wiki-data.json"
HTML = ROOT / "viewer" / "index.html"


def ids(nodes: list[dict], kind: str) -> list[str]:
    return sorted(node["id"] for node in nodes if node["type"] == kind)


def digest(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def main() -> int:
    if not MANIFEST.exists():
        print("EXPLORER CANDIDATE VALIDATION FAILED\n- missing viewer/explorer-manifest.json; run build_explorer_manifest.py")
        return 1
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    raw = DATA.read_bytes()
    payload = json.loads(raw)
    nodes = payload["nodes"]
    actual_counts = {kind: len(ids(nodes, kind)) for kind in ("concept", "definition", "example", "guide")}
    actual_counts["total"] = len(nodes)
    errors: list[str] = []
    if hashlib.sha256(raw).hexdigest() != manifest["source_index_sha256"]:
        errors.append("wiki-data.json differs from manifest source index; rebuild manifest")
    if actual_counts != manifest["counts"]:
        errors.append(f"inventory count mismatch: expected {manifest['counts']}, got {actual_counts}")
    for kind, manifest_key in (("concept", "canonical_concept_ids"), ("example", "example_ids"), ("definition", "definition_ids"), ("guide", "guide_ids")):
        actual = ids(nodes, kind)
        if actual != manifest[manifest_key]:
            errors.append(f"{kind} ID inventory differs from manifest")
        if digest(actual) != manifest[manifest_key + "_sha256"]:
            errors.append(f"{kind} ID digest differs from manifest")
    html = HTML.read_text(encoding="utf-8")
    required_fragments = ("fetch('wiki-data.json')", "function nav()", "function go(id)", "go(location.hash.slice(1)||nodes[0]?.id)")
    for fragment in required_fragments:
        if fragment not in html:
            errors.append(f"static reader is missing required runtime fragment: {fragment}")
    if re.search(r"nodes\.slice\(|filter\([^)]*group", html):
        errors.append("static reader contains a detected subset-navigation pattern")
    if errors:
        print("EXPLORER CANDIDATE VALIDATION FAILED")
        for error in errors:
            print("- " + error)
        return 1
    print("explorer candidate validation passed")
    print(json.dumps(actual_counts, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
