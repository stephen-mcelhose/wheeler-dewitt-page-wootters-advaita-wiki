#!/usr/bin/env python3
"""Build the navigation hotfix candidate from canonical wiki sources."""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

from generate_learning_order import parse_learning_order

ROOT = Path(__file__).resolve().parents[1]
LIVE = Path("/app/artifacts/instances/ReactComponent/quantum-time-wiki-explorer/current.json")
BASE = ROOT / ".agents" / "diffs" / "release-27-foundations-integration" / "current.json"
OUT = ROOT / ".agents" / "diffs" / "learning-navigation-hotfix"
CANDIDATE = OUT / "current.json"
REPORT = OUT / "validation.json"


def run(command: list[str]) -> tuple[bool, str]:
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, timeout=180)
    return result.returncode == 0, (result.stdout + result.stderr).strip()


def main() -> int:
    if not BASE.exists():
        raise SystemExit(f"required source-preserving base candidate is missing: {BASE}")
    order = parse_learning_order()
    base = json.loads(BASE.read_text(encoding="utf-8"))
    candidate = json.loads(json.dumps(base))
    data = candidate["files"]["/data.ts"]["code"]
    import_old = "export const concepts:Concept[]="
    if import_old not in data:
        raise SystemExit("candidate data does not expose concepts")
    data = data.replace(import_old, "export const learningOrder:string[]=" + json.dumps(order, ensure_ascii=False, separators=(",", ":")) + ";" + import_old, 1)
    candidate["files"]["/data.ts"]["code"] = data
    code = candidate["code"]
    code = code.replace("import {concepts,definitions,totalNodes,type Concept,type Definition} from './data';", "import {concepts,definitions,learningOrder,totalNodes,type Concept,type Definition} from './data';", 1)
    old_at = "const at=concepts.findIndex(c=>c.id===selected.id);const grouped="
    new_at = "const learningAt=learningOrder.indexOf(selected.id);const previousId=learningAt>0?learningOrder[learningAt-1]:undefined;const nextId=learningAt>=0&&learningAt<learningOrder.length-1?learningOrder[learningAt+1]:undefined;const grouped="
    if old_at not in code:
        raise SystemExit("reader navigation insertion point is missing")
    code = code.replace(old_at, new_at, 1)
    old_nav = "{at>0?<button onClick={()=>nav(concepts[at-1].id)} className='inline-flex items-center gap-1 font-semibold text-indigo-700'><ChevronLeft size={17}/>Previous</button>:<span/>}{at<concepts.length-1&&<button onClick={()=>nav(concepts[at+1].id)} className='inline-flex items-center gap-1 font-semibold text-indigo-700'>Next<ChevronRight size={17}/></button>}"
    new_nav = "{previousId?<button onClick={()=>nav(previousId)} className='inline-flex items-center gap-1 font-semibold text-indigo-700'><ChevronLeft size={17}/>Previous</button>:<span/>}{nextId&&<button onClick={()=>nav(nextId)} className='inline-flex items-center gap-1 font-semibold text-indigo-700'>Next<ChevronRight size={17}/></button>}"
    if old_nav not in code:
        raise SystemExit("reader positional navigation expression is missing")
    candidate["code"] = code.replace(old_nav, new_nav, 1)
    OUT.mkdir(parents=True, exist_ok=True)
    CANDIDATE.write_text(json.dumps(candidate, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    checks: dict[str, bool] = {}
    outputs: dict[str, str] = {}
    commands = {
        "annotation_tests": ["python3", "scripts/test_annotation_transform.py"],
        "index_graph_validation": ["sh", "-c", "python3 .agents/skills/doc-manager/scripts/build_index.py . && python3 .agents/skills/doc-manager/scripts/validate.py ."],
        "typescript_compile": ["node", ".agents/tscheck/node_modules/typescript/bin/tsc", "-p", ".agents/tscheck/tsconfig.json"],
        "optional_domain_smoke": ["python3", ".agents/release_smoke_check.py", str(CANDIDATE)],
        "learning_order_parser": ["python3", ".agents/generate_learning_order.py", "--check"],
        "learning_order_validator": ["python3", ".agents/validate_learning_navigation.py", str(CANDIDATE)],
    }
    # Compile the exact candidate, not the stale tscheck fixture.
    (ROOT / ".agents" / "tscheck" / "App.tsx").write_text(candidate["code"], encoding="utf-8")
    (ROOT / ".agents" / "tscheck" / "data.ts").write_text(candidate["files"]["/data.ts"]["code"], encoding="utf-8")
    for name, command in commands.items():
        checks[name], outputs[name] = run(command)
    live = json.loads(LIVE.read_text(encoding="utf-8"))
    checks["candidate_completeness_preservation"] = (
        len(order) == 38
        and len(candidate["files"]["/data.ts"]["code"]) >= len(base["files"]["/data.ts"]["code"])
        and "<MathText text={item.text}/>" in candidate["code"]
        and "(grouped[g]??[])" in candidate["code"]
        and all(token in candidate["code"] for token in ("DefinitionTerm", "WARNING — Under Construction", "Draft / Under Construction / Not reviewed"))
        and live["type"] == candidate["type"] == "ReactComponent"
    )
    checks["canonical_source_count"] = len(order) == 38
    report = {
        "release": "version 29",
        "candidate": str(CANDIDATE),
        "base": str(BASE),
        "learning_order_count": len(order),
        "checks": checks,
        "outputs": outputs,
        "candidate_sha256": hashlib.sha256(CANDIDATE.read_bytes()).hexdigest(),
    }
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
