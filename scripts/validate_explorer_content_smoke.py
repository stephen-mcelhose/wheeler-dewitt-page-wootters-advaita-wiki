#!/usr/bin/env python3
"""Content smoke checks for the non-published static Explorer candidate.

These checks prove that the current source index contains the pages and exact
reader-facing anchors required for the current Foundations/Page–Wootters review.
They do not replace interactive definition-popover verification.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "viewer" / "wiki-data.json"

REQUIRED = {
    "hilbert-spaces": ["# Hilbert Spaces"],
    "dirac-quantization": ["# Dirac Quantization and Physical States", "\\hat C_I", "physical inner product"],
    "formal-and-physical-state-spaces": ["# Formal and Physical State Spaces", "\\mathcal H_{\\mathrm{kin}}", "\\mathcal H_{\\mathrm{phys}}"],
    "example-dirac-quantization-c3-formal-and-physical-spaces": ["# Finite C³ Constraint", "physicalInnerProductOnToyKernel3D", "7\\alpha^*\\beta"],
    "constrained-clock-system-models": ["{{def:clock-system-factorization|clock-system factorization}}", "{{def:constrained-history-state|constrained history state}}"],
    "clock-states": ["{{def:ideal-clock-state-family|idealized clock representation}}", "{{def:covariant-time-povm|covariant POVMs}}"],
    "clock-povms": ["{{def:clock-reading-and-external-time|clock outcome}}", "{{def:covariant-time-povm|covariant time POVM}}"],
    "finite-clock-model": ["{{def:clock-quality|finite readout resolution}}"],
    "page-wootters-limitations": ["{{def:multiple-choice-problem|multiple-choice problem}}"],
    "mathematical-notation-reference": ["\\mathcal H_{\\mathrm{kin}}", "\\mathcal H_{\\mathrm{phys}}", "\\ker\\hat C"],
}


def main() -> int:
    nodes = {node["id"]: node for node in json.loads(DATA.read_text(encoding="utf-8"))["nodes"]}
    errors: list[str] = []
    for node_id, fragments in REQUIRED.items():
        node = nodes.get(node_id)
        if not node:
            errors.append(f"missing required reader node: {node_id}")
            continue
        body = node.get("body", "")
        for fragment in fragments:
            if fragment not in body:
                errors.append(f"{node_id}: missing required canonical fragment: {fragment}")
    if errors:
        print("EXPLORER CONTENT SMOKE FAILED")
        for error in errors:
            print("- " + error)
        return 1
    print(f"explorer content smoke passed: {len(REQUIRED)} inspection targets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
