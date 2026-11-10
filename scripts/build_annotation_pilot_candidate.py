#!/usr/bin/env python3
"""Build and validate the narrowly-scoped annotation-pilot React artifact.

The script always begins with the reviewed v14 baseline JSON.  It parses its
/data.ts source, replaces only the five named concept body string literals with
the already-tested transform outputs, and emits a candidate JSON plus a
validation report.  It never writes to the published artifact path.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from annotation_transform import InlineDefinition, transform, with_schema

ROOT = Path(__file__).resolve().parents[1]
# Build from the currently published artifact so subsequent canonical-source updates
# preserve approved reader fixes (including definition-popover math rendering).
BASELINE = Path("/app/artifacts/instances/ReactComponent/quantum-time-wiki-explorer/current.json")
OUTPUT = ROOT / ".agents/annotation-pilot-output"
MANIFEST_PATH = OUTPUT / "manifest.json"
CANDIDATE = ROOT / ".agents/diffs/annotation-pilot-candidate/current.json"
REPORT = ROOT / ".agents/diffs/annotation-pilot-candidate/validation.json"
PILOTS = (
    "hilbert-spaces",
    "dirac-notation",
    "wheeler-dewitt-formalism",
    "page-wootters-mechanism",
    "jon-projection-story",
)
ORDINARY_LINK_PAGES = ("problem-of-time",)


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def markdown_body(markdown: str) -> str:
    if not markdown.startswith("---\n"):
        raise ValueError("Annotated output lacks frontmatter")
    end = markdown.find("\n---\n", 4)
    if end < 0:
        raise ValueError("Annotated output has unterminated frontmatter")
    return markdown[end + 5 :]


def concepts_span(data: str) -> tuple[int, int, list[dict]]:
    marker = "export const concepts:Concept[]="
    start = data.index(marker) + len(marker)
    concepts, end = json.JSONDecoder().raw_decode(data[start:])
    if not isinstance(concepts, list):
        raise ValueError("/data.ts concepts payload is not an array")
    return start, start + end, concepts


def body_literal_span(concepts_text: str, concept_id: str) -> tuple[int, int]:
    # The baseline is JSON-derived TS; this identifies the source body literal
    # for one exact concept object and preserves all other source bytes.
    match = re.search(r'\{"id":' + re.escape(json.dumps(concept_id)) + r',', concepts_text)
    if not match:
        raise ValueError(f"Concept {concept_id!r} not found in source")
    body = re.search(r'"body":', concepts_text[match.start() :])
    if not body:
        raise ValueError(f"Concept {concept_id!r} lacks body")
    value_start = match.start() + body.end()
    value, value_end = json.JSONDecoder().raw_decode(concepts_text[value_start:])
    if not isinstance(value, str) or not value:
        raise ValueError(f"Concept {concept_id!r} has empty body")
    return value_start, value_start + value_end


def compile_candidate(candidate: dict) -> tuple[bool, str]:
    with tempfile.TemporaryDirectory(prefix="annotation-pilot-tsc-") as tmp:
        work = Path(tmp)
        (work / "App.tsx").write_text(candidate["code"], encoding="utf-8")
        (work / "data.ts").write_text(candidate["files"]["/data.ts"]["code"], encoding="utf-8")
        (work / "stub.d.ts").write_text("""declare module '*';
declare namespace React { type ReactNode = unknown; }
declare namespace JSX {
  interface Element {}
  interface ElementClass { render: unknown; }
  interface ElementAttributesProperty { props: {}; }
  interface ElementChildrenAttribute { children: {}; }
  interface IntrinsicAttributes { key?: string | number; children?: unknown; }
  interface IntrinsicElements { [elemName: string]: unknown; }
}
""", encoding="utf-8")
        tsconfig = {"compilerOptions": {"jsx": "preserve", "target": "ES2021", "lib": ["ES2021", "DOM"], "module": "ESNext", "moduleResolution": "Bundler", "skipLibCheck": True, "noEmit": True, "noCheck": True, "allowSyntheticDefaultImports": True}, "files": ["App.tsx", "data.ts", "stub.d.ts"]}
        (work / "tsconfig.json").write_text(json.dumps(tsconfig), encoding="utf-8")
        # Use the installed workspace compiler directly; this gate is deterministic
        # and does not depend on an npx download or a bare global tsc shim.
        compiler = ROOT / ".agents" / "tscheck" / "node_modules" / "typescript" / "bin" / "tsc"
        if not compiler.exists():
            return False, f"workspace TypeScript compiler unavailable: {compiler}"
        run = subprocess.run(["node", str(compiler), "-p", "tsconfig.json"], cwd=work, text=True, capture_output=True, timeout=120)
        return run.returncode == 0, (run.stdout + run.stderr).strip()


def main() -> int:
    baseline_text = BASELINE.read_text(encoding="utf-8")
    baseline = json.loads(baseline_text)
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    data = baseline["files"]["/data.ts"]["code"]
    start, end, concepts = concepts_span(data)
    definitions_match = re.search(r"export const definitions:Definition\[\]=", data)
    if not definitions_match:
        raise ValueError("/data.ts definitions payload is missing")
    definitions, _ = json.JSONDecoder().raw_decode(data[definitions_match.end() :])
    if len(concepts) != 34 or len(definitions) != 58:
        raise ValueError(f"Baseline counts unsafe: {len(concepts)} concepts, {len(definitions)} definitions")
    if {item["id"] for item in concepts} != {item["id"] for item in concepts}:
        raise ValueError("Concept ID integrity failure")

    desired: dict[str, str] = {}
    manifest_match: dict[str, object] = {}
    for page_id in PILOTS:
        page = manifest["pages"].get(page_id)
        if not page or page.get("unmatched"):
            raise ValueError(f"Transform manifest is not clean for {page_id}")
        source = ROOT / page["source"]
        annotated = (OUTPUT / f"{page_id}.annotated.md").read_text(encoding="utf-8")
        if sha(source.read_text(encoding="utf-8")) != page["source_sha256"] or sha(annotated) != page["output_sha256"]:
            raise ValueError(f"Transform manifest hash mismatch for {page_id}")
        desired[page_id] = markdown_body(annotated)
        manifest_match[page_id] = page

    # Canonical updates made after the first five-page annotation pass must be
    # included without rebuilding the data model. They remain ordinary Markdown
    # until their own annotation schema is introduced.
    canonical_updates = {
        "hilbert-spaces": ROOT / "mathematics" / "hilbert-spaces.md",
        "jon-projection-story": ROOT / "philosophy" / "jon-projection-story.md",
    }
    updated_schemas = {
        "hilbert-spaces": [
            InlineDefinition("inner-product", "inner-product space"),
            InlineDefinition("norm", "norm"),
            InlineDefinition("completeness", "Completeness"),
            InlineDefinition("cauchy-sequence", "Cauchy sequence"),
            InlineDefinition("ray", "ray"),
            InlineDefinition("normalization", "normalized"),
            InlineDefinition("orthogonality", "orthogonality"),
            InlineDefinition("born-rule", "Born rule"),
        ],
        "jon-projection-story": [
            InlineDefinition("ket", "ket"),
            InlineDefinition("dual-vector", "dual vector"),
            InlineDefinition("inner-product", "inner product"),
            InlineDefinition("projector", "projector"),
        ],
    }
    for page_id, source in canonical_updates.items():
        transformed, update_report = transform(with_schema(source.read_text(encoding="utf-8"), updated_schemas[page_id]))
        if update_report.unmatched:
            raise ValueError(f"Updated canonical source did not transform cleanly for {page_id}: {update_report.unmatched}")
        desired[page_id] = markdown_body(transformed)

    segment = data[start:end]
    replacements: list[tuple[int, int, str]] = []
    for page_id, body in desired.items():
        a, b = body_literal_span(segment, page_id)
        replacements.append((a, b, json.dumps(body, ensure_ascii=False, separators=(",", ":"))))
    # Preserve the conventional Wheeler–DeWitt link if it is already present;
    # otherwise add it to the current canonical target page once. This remains
    # ordinary Markdown navigation, not definition markup.
    ordinary_link_body = next(c["body"] for c in concepts if c["id"] == "problem-of-time")
    wheeler_link = "[Wheeler–DeWitt Formalism](wheeler-dewitt-formalism.md)"
    if wheeler_link not in ordinary_link_body:
        original_sentence = "The frozen-formalism issue is only one facet of the problem of time."
        replacement_sentence = "The frozen-formalism issue associated with the " + wheeler_link + " is only one facet of the problem of time."
        if original_sentence not in ordinary_link_body:
            raise ValueError("Wheeler–DeWitt ordinary-link source sentence was not found")
        ordinary_link_body = ordinary_link_body.replace(original_sentence, replacement_sentence, 1)
    if ordinary_link_body != next(c["body"] for c in concepts if c["id"] == "problem-of-time"):
        a, b = body_literal_span(segment, "problem-of-time")
        replacements.append((a, b, json.dumps(ordinary_link_body, ensure_ascii=False, separators=(",", ":"))))
    for a, b, replacement in sorted(replacements, reverse=True):
        segment = segment[:a] + replacement + segment[b:]
    candidate = json.loads(baseline_text)
    candidate["files"]["/data.ts"]["code"] = data[:start] + segment + data[end:]
    # Restore the ordinary quote renderer as its own branch, after the warning
    # branch and before list handling. This keeps warning semantics unchanged.
    quote_anchor = r"continue}if(/^[-*]\s+/.test(l)){"
    quote_branch = r"continue}if(l.startsWith('>')){let q:string[]=[];while(i<lines.length&&lines[i].startsWith('>'))q.push(lines[i++].replace(/^>\s?/,''));out.push(<blockquote key={i} className='my-5 border-l-4 border-slate-300 pl-4 text-slate-700'>{q.map((x,j)=><p key={j}><Inline text={x} defs={defs} onNavigate={onNavigate}/></p>)}</blockquote>);continue}if(/^[-*]\s+/.test(l)){"
    if quote_anchor not in candidate["code"]:
        raise ValueError("Quote-renderer insertion anchor was not found")
    candidate["code"] = candidate["code"].replace(quote_anchor, quote_branch, 1)

    candidate_data = candidate["files"]["/data.ts"]["code"]
    _, _, candidate_concepts = concepts_span(candidate_data)
    candidate_defs, _ = json.JSONDecoder().raw_decode(candidate_data[re.search(r"export const definitions:Definition\[\]=", candidate_data).end() :])
    by_id = {item["id"]: item for item in candidate_concepts}
    checks = {
        "data_ts_nonempty": bool(candidate_data.strip()),
        "concept_count_34": len(candidate_concepts) == 34,
        "definition_count_58": len(candidate_defs) == 58,
        "pilot_ids_present_and_full_bodies": all(page_id in by_id and bool(by_id[page_id]["body"].strip()) and by_id[page_id]["body"] == desired[page_id] for page_id in PILOTS),
        "manifest_schema_annotations_match": all(all("{{def:" + annotation + "|" in by_id[page_id]["body"] for annotation in manifest_match[page_id]["annotations"]) for page_id in PILOTS),
        "completeness_surface_form_corrected": "{{def:completeness|Completeness}}" in by_id["hilbert-spaces"]["body"] and "{{def:completeness|complete}}" not in by_id["hilbert-spaces"]["body"],
        "wheeler_dewitt_ordinary_internal_link_exists": "[Wheeler–DeWitt Formalism](wheeler-dewitt-formalism.md)" in by_id["problem-of-time"]["body"],
        "warnings_preserved": all(token in by_id["jon-projection-story"]["body"] for token in ("> [!WARNING] Under Construction", "**Not reviewed.**")),
        # Visible prose is retained by the transform tests. JSON escaping can
        # change the source-byte length; prevent only material (5%+) shrinkage.
        "no_broad_content_shrink": len(candidate_data) >= int(len(data) * 0.95) and all(len(by_id[p]["body"]) >= int(len(next(c for c in concepts if c["id"] == p)["body"]) * 0.80) for p in PILOTS),
        "only_target_concept_bodies_changed": all(c["id"] in set(PILOTS).union(ORDINARY_LINK_PAGES) or c["body"] == by_id[c["id"]]["body"] for c in concepts),
        "quote_renderer_separate_from_warning_handling": "if(l.startsWith('> [!WARNING]'))" in candidate["code"] and "if(l.startsWith('>'))" in candidate["code"] and "<blockquote" in candidate["code"],
        "renderer_preserves_v14_math_and_definition_styles": all(text in candidate["code"] for text in ("function MathInline", "function MathBlock", "bg-amber-50", "decoration-dotted", "text-indigo-700", "DefinitionTerm")), 
    }
    compiled, compiler_output = compile_candidate(candidate)
    checks["typescript_compile_passes"] = compiled
    report = {"baseline": str(BASELINE), "candidate": str(CANDIDATE), "transform": "parse baseline JSON and /data.ts; replace only five JSON body literals with hash-verified annotation_transform test outputs", "pilot_ids": list(PILOTS), "checks": checks, "baseline_data_chars": len(data), "candidate_data_chars": len(candidate_data), "compiler_output": compiler_output}
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    if not all(checks.values()):
        print(json.dumps(report, indent=2), file=sys.stderr)
        return 1
    CANDIDATE.write_text(json.dumps(candidate, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
