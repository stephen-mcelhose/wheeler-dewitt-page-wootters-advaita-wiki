#!/usr/bin/env python3
"""Verify publication integrity for a React explorer candidate and live artifact."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".agents"))
from validate_explorer_data_payload import artifact_data, validate_data_source  # noqa: E402

MATH_GATE = ROOT / '.agents' / 'validate_kronecker_delta_math_fixture.py'
EXACT_TSX_GATE = ROOT / '.agents' / 'exact_artifact_tsx_gate.py'
GUIDE_GATE = ROOT / '.agents' / 'validate_global_reference_surface.py'


def fail(message: str) -> None:
    print(f"published-artifact integrity failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def load(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        fail(f"cannot parse {path}: {error}")
    if not isinstance(value, dict):
        fail(f"{path} must contain an object")
    return value


def artifact_parts(value: dict, label: str) -> tuple[str, str]:
    code = value.get("code")
    files = value.get("files")
    if not isinstance(code, str) or not isinstance(files, dict):
        fail(f"{label} is missing code or files")
    data = files.get("/data.ts")
    if not isinstance(data, dict) or not isinstance(data.get("code"), str):
        fail(f"{label} is missing /data.ts code")
    return code, data["code"]


def array_after(source: str, marker: str) -> list:
    start = source.find(marker)
    if start < 0:
        fail(f"/data.ts is missing {marker}")
    start += len(marker)
    decoder = json.JSONDecoder()
    try:
        value, _ = decoder.raw_decode(source[start:])
    except json.JSONDecodeError as error:
        fail(f"cannot parse {marker} payload: {error}")
    if not isinstance(value, list):
        fail(f"{marker} must be an array")
    return value


def count_examples(concepts: list) -> int:
    return sum(1 for item in concepts if isinstance(item, dict) and str(item.get("path", "")).startswith("examples/"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate", type=Path)
    parser.add_argument("live", type=Path)
    parser.add_argument("--source-root", type=Path, required=True, help="Canonical wiki root used to verify source node counts")
    args = parser.parse_args()

    try:
        source_index = json.loads((args.source_root / "viewer" / "wiki-data.json").read_text(encoding="utf-8"))
        source_nodes = source_index["nodes"]
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as error:
        fail(f"cannot read canonical source index: {error}")
    source_concepts = sum(1 for item in source_nodes if item.get("type") == "concept")
    source_definitions = sum(1 for item in source_nodes if item.get("type") == "definition")
    source_examples = sum(1 for item in source_nodes if item.get("type") == "example")
    source_guides = sum(1 for item in source_nodes if item.get("id") == "mathematical-notation-reference" and item.get("type") == "guide")
    source_total = len(source_nodes)

    candidate_bytes = args.candidate.read_bytes()
    live_bytes = args.live.read_bytes()
    candidate_hash = hashlib.sha256(candidate_bytes).hexdigest()
    live_hash = hashlib.sha256(live_bytes).hexdigest()
    if candidate_hash != live_hash:
        fail(f"candidate/live SHA-256 differ: candidate={candidate_hash}, live={live_hash}")

    candidate = load(args.candidate)
    live = load(args.live)
    for label, artifact in (("candidate", candidate), ("live", live)):
        code, data = artifact_parts(artifact, label)
        try:
            payload_counts = validate_data_source(artifact_data(artifact, label), label)
        except ValueError as error:
            fail(str(error))
        if "learningOrder" not in data or "totalNodes" not in data:
            fail(f"{label} /data.ts lacks learningOrder or totalNodes")
        concepts = array_after(data, "export const concepts:Concept[]=")
        definitions = array_after(data, "export const definitions:Definition[]=")
        learning_order = array_after(data, "export const learningOrder:string[]=")
        total_match = re.search(r"export const totalNodes=(\d+);", data)
        if not total_match:
            fail(f"{label} /data.ts lacks numeric totalNodes")
        total_nodes = int(total_match.group(1))
        if not concepts or not definitions or not learning_order:
            fail(f"{label} contains an empty required payload")
        if any(not isinstance(item, dict) or not str(item.get("body", "")).strip() for item in concepts):
            fail(f"{label} contains missing concept bodies")
        examples = array_after(data, "export const examples:Concept[]=")
        global_references = array_after(data, "export const globalReferences:Concept[]=")
        concept_paths = count_examples(concepts)
        if len(concepts) != source_concepts:
            fail(f"{label} concept count mismatch: {len(concepts)} vs source {source_concepts}")
        if len(definitions) != source_definitions:
            fail(f"{label} definition count mismatch: {len(definitions)} vs source {source_definitions}")
        if concept_paths != 0:
            fail(f"{label} incorrectly mixes examples into concepts payload")
        if len(examples) != source_examples:
            fail(f"{label} example count mismatch: {len(examples)} vs source {source_examples}")
        if any(not isinstance(item, dict) or not str(item.get("body", "")).strip() for item in examples):
            fail(f"{label} contains missing example bodies")
        if len(global_references) != source_guides:
            fail(f"{label} global reference count mismatch: {len(global_references)} vs source {source_guides}")
        if any(not isinstance(item, dict) or not str(item.get("body", "")).strip() for item in global_references):
            fail(f"{label} contains missing global reference bodies")
        if total_nodes != source_total:
            fail(f"{label} totalNodes mismatch: {total_nodes} vs source {source_total}")
        if source_examples <= 0:
            fail("canonical source unexpectedly has no examples")
        required_tokens = ("learningOrder", "learningAt", "learningOrder[learningAt+1]", "learningOrder[learningAt-1]")
        if any(token not in code for token in required_tokens):
            fail(f"{label} App source lacks required learning navigation token")
        if "concepts[at+1]" in code or "concepts[at-1]" in code:
            fail(f"{label} App source uses forbidden positional concept navigation")
        artifact_path = args.candidate if label == 'candidate' else args.live
        math_result = __import__('subprocess').run(['python3', str(MATH_GATE), str(artifact_path)], cwd=ROOT, text=True, capture_output=True, timeout=60)
        if math_result.returncode:
            fail(f"{label} Kronecker-delta math fixture failed: {(math_result.stdout + math_result.stderr).strip()}")
        compile_result = __import__('subprocess').run(['python3', str(EXACT_TSX_GATE), str(artifact_path), '--label', label], cwd=ROOT, text=True, capture_output=True, timeout=180)
        if compile_result.returncode:
            fail(f"{label} exact artifact parser/compiler gate failed: {(compile_result.stdout + compile_result.stderr).strip()}")
        guide_result = __import__('subprocess').run(['python3', str(GUIDE_GATE), str(artifact_path), '--source-root', str(args.source_root)], cwd=ROOT, text=True, capture_output=True, timeout=60)
        if guide_result.returncode:
            fail(f"{label} global-reference surface gate failed: {(guide_result.stdout + guide_result.stderr).strip()}")
        print(f"{label}: concepts={len(concepts)}, definitions={len(definitions)}, examples={len(examples)}, globalReferences={len(global_references)}, totalNodes={total_nodes}, app_bytes={len(code.encode())}, data_bytes={len(data.encode())}, sentinel/payload_gate={payload_counts}, math_fixture=passed, exact_parser_compiler=passed, global_reference_surface=passed")
    print(f"published-artifact integrity passed: sha256={candidate_hash}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
