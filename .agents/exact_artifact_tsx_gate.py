#!/usr/bin/env python3
"""Compile the exact ReactComponent candidate App.tsx and /data.ts payload."""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".agents"))
from validate_explorer_data_payload import artifact_data, validate_data_source  # noqa: E402

TSC = ROOT / ".agents" / "tscheck" / "node_modules" / "typescript" / "bin" / "tsc"
TSCONFIG = ROOT / ".agents" / "tscheck" / "tsconfig.json"
GLOBALS = ROOT / ".agents" / "tscheck" / "globals.d.ts"


def fail(message: str) -> int:
    print(f"exact-artifact TSX gate failed: {message}", file=sys.stderr)
    return 1


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("artifact", type=Path, help="Exact ReactComponent JSON to materialize and compile")
    parser.add_argument("--label", default="artifact", help="Evidence label, for example candidate or live")
    args = parser.parse_args()
    try:
        artifact_bytes = args.artifact.read_bytes()
        artifact = json.loads(artifact_bytes)
        code = artifact["code"]
        data = artifact_data(artifact, args.label)
        if artifact.get("language") != "tsx" or not isinstance(code, str):
            return fail("artifact must provide TSX code and /data.ts code")
        validate_data_source(data, args.label)
    except (OSError, KeyError, TypeError, json.JSONDecodeError, ValueError) as error:
        return fail(f"cannot load exact artifact: {error}")
    if not TSC.exists() or not TSCONFIG.exists() or not GLOBALS.exists():
        return fail("local TypeScript compiler fixture is incomplete")

    with tempfile.TemporaryDirectory(prefix="exact-artifact-tsx-") as temporary:
        work = Path(temporary)
        # These are byte-for-byte the candidate payloads, not a stale fixture.
        (work / "App.tsx").write_text(code, encoding="utf-8")
        (work / "data.ts").write_text(data, encoding="utf-8")
        shutil.copy2(TSCONFIG, work / "tsconfig.json")
        shutil.copy2(GLOBALS, work / "globals.d.ts")
        # TypeScript resolves package declarations by walking node_modules from
        # the exact temporary candidate directory.
        os.symlink(ROOT / ".agents" / "tscheck" / "node_modules", work / "node_modules", target_is_directory=True)
        result = subprocess.run(
            ["node", str(TSC), "-p", str(work / "tsconfig.json")],
            cwd=work,
            text=True,
            capture_output=True,
            timeout=180,
        )
    output = (result.stdout + result.stderr).strip()
    if result.returncode:
        return fail(output or f"tsc exited {result.returncode}")
    print(
        "exact-artifact TSX gate passed: "
        f"{args.label}={args.artifact} App.tsx={len(code.encode())} bytes /data.ts={len(data.encode())} bytes; "
        "command=node .agents/tscheck/node_modules/typescript/bin/tsc -p <temporary exact-payload tsconfig>"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
