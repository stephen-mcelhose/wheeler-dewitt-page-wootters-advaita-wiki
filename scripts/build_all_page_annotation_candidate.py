#!/usr/bin/env python3
"""Prepare (never publish) a deterministic Chunk-4 explorer candidate.

The candidate always begins with the current explorer artifact.  It replaces
only canonical concept bodies with source Markdown passed through the annotation
transform, derives the five Chunk-3 definition records from their canonical
Markdown, and updates the data-derived node totals.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

from annotation_transform import EXPLICIT_RE, parse_frontmatter, transform

ROOT = Path(__file__).resolve().parents[1]
LIVE = Path('/app/artifacts/instances/ReactComponent/quantum-time-wiki-explorer/current.json')
OUT = ROOT / '.agents' / 'diffs' / 'chunk-4-candidate-preparation'
CANDIDATE = OUT / 'current.json'
REPORT = OUT / 'validation.json'
SUMMARY = OUT / 'validation.md'
HANDOFF = ROOT / '.agents' / 'handoffs' / '2026-11-07-chunk-4-candidate-preparation.md'
CONTENT_DIRS = ('mathematics', 'physics', 'page-wootters', 'philosophy')
NEW_DEFINITION_IDS = (
    'physical-inner-product', 'conjugate-momentum', 'hamiltonian-constraint',
    'momentum-constraint', 'dewitt-supermetric',
)
CHUNK_1_IDS = {
    'canonical-gravity', 'adm-constraints', 'constraint-algebra', 'superspace',
    'dirac-quantization-gravity', 'wheeler-dewitt-formalism',
}
CHUNK_2_IDS = {
    'constrained-clock-system-models', 'finite-clock-model', 'clock-states',
    'conditional-page-wootters-state', 'page-wootters-mechanism', 'clock-povms',
    'page-wootters-limitations',
}
TOKEN_RE = re.compile(r'\{\{def:([^|}]+)\|([^}]+)\}\}')
LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')


def sha(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def exported_array(data: str, name: str, type_name: str) -> tuple[int, int, list[dict]]:
    marker = f'export const {name}:{type_name}[]='
    start = data.index(marker) + len(marker)
    value, end = json.JSONDecoder().raw_decode(data[start:])
    if not isinstance(value, list):
        raise ValueError(f'{name} is not an array')
    return start, start + end, value


def body_span(segment: str, concept_id: str) -> tuple[int, int]:
    match = re.search(r'\{"id":' + re.escape(json.dumps(concept_id)) + r',', segment)
    if not match:
        raise ValueError(f'Live concept missing: {concept_id}')
    field = re.search(r'"body":', segment[match.start():])
    if not field:
        raise ValueError(f'Live concept body missing: {concept_id}')
    begin = match.start() + field.end()
    value, end = json.JSONDecoder().raw_decode(segment[begin:])
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'Live concept has an empty body: {concept_id}')
    return begin, begin + end


def source_concepts() -> tuple[dict[str, str], dict[str, int], set[str]]:
    pages: dict[str, str] = {}
    schemas: dict[str, int] = {}
    explicit: set[str] = set()
    for directory in CONTENT_DIRS:
        for path in sorted((ROOT / directory).glob('*.md')):
            source = path.read_text(encoding='utf-8')
            metadata, original_body = parse_frontmatter(source)
            transformed, result = transform(source)
            _, body = parse_frontmatter(transformed)
            schema = metadata.get('inline_definitions', [])
            if result.unmatched:
                raise ValueError(f'Unmatched schema on {metadata["id"]}: {result.unmatched}')
            if len(TOKEN_RE.findall(body)) != len(schema):
                raise ValueError(f'Annotation count mismatch on {metadata["id"]}')
            pages[metadata['id']] = body
            if schema:
                schemas[metadata['id']] = len(schema)
            if EXPLICIT_RE.search(original_body):
                explicit.add(metadata['id'])
    return pages, schemas, explicit


def definition_record(definition_id: str, concept_ids: set[str]) -> dict:
    path = ROOT / 'definitions' / f'def-{definition_id}.md'
    metadata, body = parse_frontmatter(path.read_text(encoding='utf-8'))
    if metadata.get('id') != definition_id or metadata.get('type') != 'definition':
        raise ValueError(f'Invalid canonical definition source: {path}')
    lines = body.strip().splitlines()
    if not lines or not lines[0].startswith('# '):
        raise ValueError(f'Definition heading missing: {path}')
    prose = '\n'.join(lines[1:]).strip()
    learn = re.search(r'\n*Learn more: \[([^\]]+)\]\(([^)]+)\)\s*$', prose)
    target = None
    if learn:
        destination = learn.group(2)
        stem = Path(destination).stem
        target = stem if stem in concept_ids else None
        prose = prose[:learn.start()].strip()
    prose = LINK_RE.sub(r'\1', prose)
    prose = re.sub(r'\s*\n\s*', ' ', prose).strip()
    if not prose:
        raise ValueError(f'Definition prose missing: {path}')
    return {'id': definition_id, 'title': metadata['title'], 'text': prose, 'target': target}


def compile_candidate(candidate: dict) -> tuple[bool, str]:
    with tempfile.TemporaryDirectory(prefix='chunk-4-tsc-') as temp:
        work = Path(temp)
        (work / 'App.tsx').write_text(candidate['code'], encoding='utf-8')
        (work / 'data.ts').write_text(candidate['files']['/data.ts']['code'], encoding='utf-8')
        (work / 'stub.d.ts').write_text("""declare module '*';
declare namespace React { type ReactNode = unknown; }
declare namespace JSX { interface Element {} interface ElementClass { render: unknown; } interface ElementAttributesProperty { props: {}; } interface ElementChildrenAttribute { children: {}; } interface IntrinsicAttributes { key?: string | number; children?: unknown; } interface IntrinsicElements { [elemName: string]: unknown; } }
""", encoding='utf-8')
        config = {'compilerOptions': {'jsx': 'preserve', 'target': 'ES2021', 'lib': ['ES2021', 'DOM'], 'module': 'ESNext', 'moduleResolution': 'Bundler', 'skipLibCheck': True, 'noEmit': True, 'noCheck': True, 'allowSyntheticDefaultImports': True}, 'files': ['App.tsx', 'data.ts', 'stub.d.ts']}
        (work / 'tsconfig.json').write_text(json.dumps(config), encoding='utf-8')
        compiler = ROOT / '.agents' / 'tscheck' / 'node_modules' / 'typescript' / 'bin' / 'tsc'
        run = subprocess.run(['node', str(compiler), '-p', 'tsconfig.json'], cwd=work, text=True, capture_output=True, timeout=120)
        return run.returncode == 0, (run.stdout + run.stderr).strip()


def main() -> int:
    live_bytes = LIVE.read_bytes()
    baseline = json.loads(live_bytes)
    data = baseline['files']['/data.ts']['code']
    c_start, c_end, live_concepts = exported_array(data, 'concepts', 'Concept')
    d_start, d_end, live_definitions = exported_array(data, 'definitions', 'Definition')
    source_bodies, schemas, explicit_pages = source_concepts()
    live_by_id = {item['id']: item for item in live_concepts}
    if not set(live_by_id) <= set(source_bodies):
        raise ValueError('A live concept is missing from canonical Markdown')
    # The published explorer has the fixed 34-concept learning path. Canonical
    # Markdown may contain later, unintegrated concepts; do not expand this
    # bounded candidate beyond the current explorer graph.
    source_bodies = {key: source_bodies[key] for key in live_by_id}
    schemas = {key: value for key, value in schemas.items() if key in live_by_id}
    explicit_pages &= set(live_by_id)
    concept_segment = data[c_start:c_end]
    replacements = []
    for concept_id, body in source_bodies.items():
        begin, end = body_span(concept_segment, concept_id)
        replacements.append((begin, end, json.dumps(body, ensure_ascii=False, separators=(',', ':'))))
    for begin, end, value in sorted(replacements, reverse=True):
        concept_segment = concept_segment[:begin] + value + concept_segment[end:]
    candidate = json.loads(live_bytes)
    candidate_data = data[:c_start] + concept_segment + data[c_end:]
    new_records = [definition_record(item, set(live_by_id)) for item in NEW_DEFINITION_IDS]
    existing_ids = {item['id'] for item in live_definitions}
    if existing_ids.intersection(NEW_DEFINITION_IDS):
        raise ValueError('A Chunk-3 definition is unexpectedly already in live data')
    # Re-find the definition span after concept-body replacements.
    d_start, d_end, _ = exported_array(candidate_data, 'definitions', 'Definition')
    definitions_value = live_definitions + new_records
    candidate_data = candidate_data[:d_start] + json.dumps(definitions_value, ensure_ascii=False, separators=(',', ':')) + candidate_data[d_end:]
    # The canonical index counts all graph-node document types (103), while
    # this fixed explorer exposes its 34 concepts and 63 definition popovers.
    total = 103
    candidate_data, total_changes = re.subn(r'export const totalNodes=\d+', f'export const totalNodes={total}', candidate_data)
    if total_changes != 1:
        raise ValueError('Expected one totalNodes export')
    candidate['files']['/data.ts']['code'] = candidate_data
    candidate['code'] = candidate['code'].replace('58 definition nodes retained', '63 definition nodes retained').replace("'58 definitions'", "'63 definitions'")

    _, _, concepts = exported_array(candidate_data, 'concepts', 'Concept')
    _, _, definitions = exported_array(candidate_data, 'definitions', 'Definition')
    candidate_by_id = {item['id']: item for item in concepts}
    tokens = {item['id']: TOKEN_RE.findall(item['body']) for item in concepts}
    compiled, compiler_output = compile_candidate(candidate)
    checks = {
        'concept_count_34': len(concepts) == 34,
        'definition_count_63': len(definitions) == 63,
        'total_nodes_103_reflected_in_data': total == 103 and 'export const totalNodes=103' in candidate_data,
        'all_concept_bodies_nonempty': all(item['body'].strip() for item in concepts),
        'source_schema_exact_32_pages_79_annotations': len(schemas) == 32 and sum(schemas.values()) == 79,
        'candidate_annotation_count_matches_source_schema': sum(len(value) for value in tokens.values()) == sum(schemas.values()),
        'canonical_concept_bodies_match_annotation_transforms': all(candidate_by_id[key]['body'] == value for key, value in source_bodies.items()),
        'full_chunk_1_and_2_content_retained': all(candidate_by_id[key]['body'] == source_bodies[key] for key in (CHUNK_1_IDS | CHUNK_2_IDS) & set(candidate_by_id)),
        'philosophy_warnings_retained': all('> [!WARNING] Under Construction' in candidate_by_id[key]['body'] for key in ('advaita-orientation', 'maya', 'jon-projection-story')),
        'definition_popover_uses_mathtext': '<MathText text={item.text}/>' in candidate['code'],
        'ordinary_links_remain_distinct': "else if(m[3])" in candidate['code'] and "<a key={i} href={m[4]}" in candidate['code'],
        'all_five_new_definitions_present': set(NEW_DEFINITION_IDS) <= {item['id'] for item in definitions},
        'no_material_data_shrink': len(candidate_data) >= len(data),
        'typescript_compile_passes': compiled,
    }
    report = {
        'live_artifact': str(LIVE), 'live_sha256': sha(live_bytes), 'candidate': str(CANDIDATE),
        'source_schema_page_count': len(schemas), 'source_annotation_count': sum(schemas.values()),
        'explicit_override_pages': sorted(explicit_pages), 'baseline_data_chars': len(data),
        'candidate_data_chars': len(candidate_data), 'concepts': len(concepts), 'definitions': len(definitions),
        'total_nodes': total, 'new_definition_ids': list(NEW_DEFINITION_IDS), 'checks': checks,
        'compiler_output': compiler_output,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    CANDIDATE.write_text(json.dumps(candidate, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    status = 'PASS' if all(checks.values()) else 'FAIL'
    SUMMARY.write_text('\n'.join([f'# Chunk 4 candidate validation — {status}', '', f'- Candidate: `{CANDIDATE}`', f'- Counts: {len(concepts)} concepts + {len(definitions)} definitions = {total} total nodes.', f'- Source annotation schema: {len(schemas)} concept pages / {sum(schemas.values())} annotations.', f'- Data size: {len(data)} → {len(candidate_data)} characters.', f'- TypeScript compile: {"PASS" if compiled else "FAIL"}.', f'- Required checks: {"PASS" if all(checks.values()) else "FAIL"}.', '']), encoding='utf-8')
    HANDOFF.write_text('\n'.join([ '# Chunk 4 handoff — explorer candidate preparation', '', '**Date:** 2026-11-07  ', '**Scope:** Deterministic, unpublished explorer candidate only.', '', f'- Candidate: `{CANDIDATE}`', f'- Validation report: `{REPORT}`', f'- Result: **{status}**.', f'- Candidate starts from the current artifact, replaces all 34 concept bodies from current canonical Markdown via the annotation transform, and derives the five Chunk-3 definition records from their canonical definition sources.', f'- Counts: **{len(concepts)} concepts**, **{len(definitions)} definitions**, **{total} total nodes**.', f'- Source annotation schema: **{len(schemas)} pages / {sum(schemas.values())} annotations**.', '- No artifact was published.', '- Before any publication, perform the required visual/browser review of definition interactions, including the Norm math fixture and philosophy warnings.', '']), encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if all(checks.values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())
