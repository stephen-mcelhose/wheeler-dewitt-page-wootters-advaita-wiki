#!/usr/bin/env python3
"""Build a deterministic source-equivalence manifest for the static Explorer.

The manifest records the exact canonical inventory that a reader candidate must
show. It is deliberately independent of any published React artifact.
"""
from __future__ import annotations

import hashlib
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "viewer" / "wiki-data.json"
LEARNING_PATH = ROOT / "overview-learning-path.md"
OUT = ROOT / "viewer" / "explorer-manifest.json"


def digest(value: object) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(encoded).hexdigest()


def main() -> int:
    raw = DATA.read_bytes()
    payload = json.loads(raw)
    nodes = payload["nodes"]
    by_type = Counter(node["type"] for node in nodes)
    canonical = sorted(node["id"] for node in nodes if node["type"] == "concept")
    examples = sorted(node["id"] for node in nodes if node["type"] == "example")
    definitions = sorted(node["id"] for node in nodes if node["type"] == "definition")
    guides = sorted(node["id"] for node in nodes if node["type"] == "guide")
    manifest = {
        "schema_version": "1.0",
        "purpose": "Exact source inventory required for an Explorer candidate.",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_index_sha256": hashlib.sha256(raw).hexdigest(),
        "learning_path_sha256": hashlib.sha256(LEARNING_PATH.read_bytes()).hexdigest(),
        "counts": {"concept": by_type["concept"], "definition": by_type["definition"], "example": by_type["example"], "guide": by_type["guide"], "total": len(nodes)},
        "canonical_concept_ids": canonical,
        "example_ids": examples,
        "definition_ids": definitions,
        "guide_ids": guides,
        "canonical_concept_ids_sha256": digest(canonical),
        "example_ids_sha256": digest(examples),
        "definition_ids_sha256": digest(definitions),
        "guide_ids_sha256": digest(guides),
    }
    OUT.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
    print(json.dumps(manifest["counts"], sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
