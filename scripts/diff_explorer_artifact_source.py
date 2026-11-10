#!/usr/bin/env python3
"""Compare a React Explorer artifact data module with the canonical source index.

Usage:
  python3 scripts/diff_explorer_artifact_source.py <artifact-json> [output-md]

The report is intentionally inventory-focused: a renderer shell can open while
its data module is empty, stale, or only a subset of canonical source.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "viewer" / "wiki-data.json"


def extract_ids(code: str, symbol: str) -> set[str]:
    # Supports ordinary object literals in a generated data module. Empty arrays
    # correctly yield the empty set, which is the important regression signal.
    match = re.search(rf"export const {re.escape(symbol)}[^=]*=\s*\[(.*?)\];", code, re.S)
    if not match:
        return set()
    return set(re.findall(r"\bid\s*:\s*['\"]([^'\"]+)['\"]", match.group(1)))


def main() -> int:
    if len(sys.argv) not in (2, 3):
        print("usage: diff_explorer_artifact_source.py <artifact-json> [output-md]")
        return 2
    artifact_path = Path(sys.argv[1])
    output = Path(sys.argv[2]) if len(sys.argv) == 3 else ROOT / ".agents" / "issues" / "explorer-artifact-source-diff.md"
    source_nodes = json.loads(SOURCE.read_text(encoding="utf-8"))["nodes"]
    source_by_kind = {kind: {n["id"] for n in source_nodes if n["type"] == kind} for kind in ("concept", "definition", "example", "guide")}
    artifact = json.loads(artifact_path.read_text(encoding="utf-8"))
    files = artifact.get("state", {}).get("content", {}).get("files", {})
    data_code = files.get("/data.ts", {}).get("code", "")
    artifact_by_kind = {
        "concept": extract_ids(data_code, "concepts"),
        "definition": extract_ids(data_code, "definitions"),
        "example": extract_ids(data_code, "examples"),
        "guide": extract_ids(data_code, "globalReferences"),
    }
    rows = []
    for kind in ("concept", "definition", "example", "guide"):
        missing = sorted(source_by_kind[kind] - artifact_by_kind[kind])
        extra = sorted(artifact_by_kind[kind] - source_by_kind[kind])
        rows.append((kind, len(source_by_kind[kind]), len(artifact_by_kind[kind]), missing, extra))
    total_source = len(source_nodes)
    total_artifact = sum(len(ids) for ids in artifact_by_kind.values())
    lines = [
        "# Explorer artifact versus canonical-source diff",
        "",
        f"- Source index: `{SOURCE.relative_to(ROOT)}`",
        f"- Artifact inspected: `{artifact_path}`",
        f"- Source nodes: **{total_source}**",
        f"- Extracted artifact data nodes: **{total_artifact}**",
        "",
        "| Kind | Source | Artifact data | Missing from artifact | Extra in artifact |",
        "|---|---:|---:|---:|---:|",
    ]
    for kind, source_count, artifact_count, missing, extra in rows:
        lines.append(f"| {kind} | {source_count} | {artifact_count} | {len(missing)} | {len(extra)} |")
    for kind, _, _, missing, extra in rows:
        if missing:
            lines += ["", f"## Missing {kind} IDs ({len(missing)})", "", "```text", *missing, "```"]
        if extra:
            lines += ["", f"## Extra {kind} IDs ({len(extra)})", "", "```text", *extra, "```"]
    lines += ["", "## Verdict", "", "**FAIL** — artifact data is not source-equivalent." if total_source != total_artifact or any(missing or extra for _,_,_,missing,extra in rows) else "**PASS** — artifact data inventory matches canonical source."]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
