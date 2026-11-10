#!/usr/bin/env python3
"""Build and validate the release-27 explorer candidate without publishing.

Starts with the current React artifact, preserving its reader code.  Replaces
/data.ts deterministically from all canonical concepts and definitions, with
concept bodies passed through the annotation transform.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import tempfile
from pathlib import Path

from annotation_transform import EXPLICIT_RE, parse_frontmatter, transform

ROOT = Path(__file__).resolve().parents[1]
LIVE = Path('/app/artifacts/instances/ReactComponent/quantum-time-wiki-explorer/current.json')
OUT = ROOT / '.agents/diffs/release-27-foundations-integration'
CANDIDATE = OUT / 'current.json'
REPORT = OUT / 'validation.json'
CONTENT_DIRS = ('mathematics', 'physics', 'page-wootters', 'philosophy')
GROUPS = {
    'mathematics': 'Mathematical Foundations',
    'physics': 'Canonical Gravity & Problem of Time',
    'page-wootters': 'Page–Wootters',
    'philosophy': 'Optional Philosophy',
}
TOKEN_RE = re.compile(r'\{\{def:([^|}]+)\|([^}]+)\}\}')
LINK_RE = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')


def sha(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def compile_candidate(candidate: dict) -> tuple[bool, str]:
    with tempfile.TemporaryDirectory(prefix='release-27-tsc-') as temp:
        work = Path(temp)
        (work / 'App.tsx').write_text(candidate['code'], encoding='utf-8')
        (work / 'data.ts').write_text(candidate['files']['/data.ts']['code'], encoding='utf-8')
        (work / 'stub.d.ts').write_text("""declare module '*';
declare namespace React { type ReactNode = unknown; }
declare namespace JSX { interface Element {} interface ElementClass { render: unknown; } interface ElementAttributesProperty { props: {}; } interface ElementChildrenAttribute { children: {}; } interface IntrinsicAttributes { key?: string | number; children?: unknown; } interface IntrinsicElements { [elemName: string]: unknown; } }
""", encoding='utf-8')
        config = {'compilerOptions': {'jsx': 'preserve', 'target': 'ES2021', 'lib': ['ES2021', 'DOM'], 'module': 'ESNext', 'moduleResolution': 'Bundler', 'skipLibCheck': True, 'noEmit': True, 'noCheck': True, 'allowSyntheticDefaultImports': True}, 'files': ['App.tsx', 'data.ts', 'stub.d.ts']}
        (work / 'tsconfig.json').write_text(json.dumps(config), encoding='utf-8')
        compiler = ROOT / '.agents/tscheck/node_modules/typescript/bin/tsc'
        run = subprocess.run(['node', str(compiler), '-p', 'tsconfig.json'], cwd=work, text=True, capture_output=True, timeout=120)
        return run.returncode == 0, (run.stdout + run.stderr).strip()


def definition_record(path: Path, concept_ids: set[str]) -> dict:
    metadata, body = parse_frontmatter(path.read_text(encoding='utf-8'))
    definition_id = metadata['id'].removeprefix('def-')
    lines = body.strip().splitlines()
    if metadata.get('type') != 'definition' or not lines or not lines[0].startswith('# '):
        raise ValueError(f'Invalid definition source: {path}')
    prose = '\n'.join(lines[1:]).strip()
    learn = re.search(r'\n*Learn more: \[([^\]]+)\]\(([^)]+)\)\s*$', prose)
    target = None
    if learn:
        stem = Path(learn.group(2)).stem
        target = stem if stem in concept_ids else None
        prose = prose[:learn.start()].strip()
    prose = LINK_RE.sub(r'\1', prose)
    prose = re.sub(r'\s*\n\s*', ' ', prose).strip()
    if not prose:
        raise ValueError(f'Empty definition prose: {path}')
    return {'id': definition_id, 'title': metadata['title'], 'text': prose, **({'target': target} if target else {})}


def main() -> int:
    live_bytes = LIVE.read_bytes()
    live = json.loads(live_bytes)
    old_data = live['files']['/data.ts']['code']
    pages: list[dict] = []
    source_bodies: dict[str, str] = {}
    schemas: dict[str, int] = {}
    for directory in CONTENT_DIRS:
        for path in sorted((ROOT / directory).glob('*.md')):
            source = path.read_text(encoding='utf-8')
            metadata, _ = parse_frontmatter(source)
            transformed, result = transform(source)
            _, body = parse_frontmatter(transformed)
            if result.unmatched:
                raise ValueError(f'Unmatched annotations on {metadata["id"]}: {result.unmatched}')
            schema = metadata.get('inline_definitions', [])
            if len(TOKEN_RE.findall(body)) != len(schema):
                raise ValueError(f'Annotation count mismatch on {metadata["id"]}')
            pages.append({'id': metadata['id'], 'title': metadata['title'], 'summary': metadata['summary'], 'status': metadata['review_status'], 'path': str(path.relative_to(ROOT)), 'group': GROUPS[directory], 'philosophy': directory == 'philosophy', 'body': body, 'parents': metadata.get('parents', []), 'relationships': metadata.get('relationships', []), 'sources': metadata.get('sources', [])})
            source_bodies[metadata['id']] = body
            if schema:
                schemas[metadata['id']] = len(schema)
    concept_ids = {item['id'] for item in pages}
    definitions = [definition_record(path, concept_ids) for path in sorted((ROOT / 'definitions').glob('def-*.md'))]
    definition_ids = {item['id'] for item in definitions}
    if len(definition_ids) != len(definitions):
        raise ValueError('Duplicate definition IDs')
    if not all(set(TOKEN_RE.findall(item['body'])) <= set() for item in []):
        raise ValueError('Unreachable')
    token_ids = {definition_id for item in pages for definition_id, _ in TOKEN_RE.findall(item['body'])}
    if not token_ids <= definition_ids:
        raise ValueError(f'Unknown definition annotation targets: {sorted(token_ids - definition_ids)}')
    total = len(pages) + len(definitions) + len(list((ROOT / 'examples').glob('*.md')))
    prefix = "export type Definition={id:string;title:string;text:string;target?:string};export type Relationship={type:string;target:string};export type Source={title:string;url:string;persistent_id?:string};export type Concept={id:string;title:string;summary:string;status:string;path:string;group:string;philosophy:boolean;body:string;parents:string[];relationships:Relationship[];sources:Source[]};"
    data = prefix + f'export const totalNodes={total};' + 'export const definitions:Definition[]=' + json.dumps(definitions, ensure_ascii=False, separators=(',', ':')) + ';export const concepts:Concept[]=' + json.dumps(pages, ensure_ascii=False, separators=(',', ':')) + ';'
    candidate = json.loads(live_bytes)
    candidate['files']['/data.ts']['code'] = data
    candidate['code'] = candidate['code'].replace('63 definition nodes retained', f'{len(definitions)} definition nodes retained').replace("'58 definitions'", f"'{len(definitions)} definitions'")
    # Keep the rendered sidebar behavior, but make every domain bucket optional.
    # This is intentionally a source-level patch so release validation can inspect it.
    sidebar_old = "const at=concepts.findIndex(c=>c.id===selected.id);const nav="
    sidebar_new = "const at=concepts.findIndex(c=>c.id===selected.id);const grouped=useMemo(()=>concepts.reduce<Record<string,Concept[]>>((all,concept)=>{(all[concept.group]??=[]).push(concept);return all},{}),[]);const groups=['Mathematical Foundations','Canonical Gravity & Problem of Time','Page–Wootters','Optional Philosophy'];const nav="
    if sidebar_old not in candidate['code']:
        raise ValueError('Expected sidebar insertion point missing from App source')
    candidate['code'] = candidate['code'].replace(sidebar_old, sidebar_new, 1)
    render_old = "{['Mathematical Foundations','Canonical Gravity & Problem of Time','Page–Wootters','Optional Philosophy'].map(g=><section key={g} className='mb-4'><p className='mb-1 text-xs font-bold uppercase tracking-wider text-slate-500'>{g}</p>{list.filter(c=>c.group===g).map(c=>"
    render_new = "{groups.map(g=><section key={g} className='mb-4'><p className='mb-1 text-xs font-bold uppercase tracking-wider text-slate-500'>{g}</p>{(grouped[g]??[]).filter(c=>list.includes(c)).map(c=>"
    if render_old not in candidate['code']:
        raise ValueError('Expected sidebar rendering expression missing from App source')
    candidate['code'] = candidate['code'].replace(render_old, render_new, 1)
    compiled, compiler_output = compile_candidate(candidate)
    OUT.mkdir(parents=True, exist_ok=True)
    CANDIDATE.write_text(json.dumps(candidate, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    smoke = subprocess.run(['python3', str(ROOT / '.agents/release_smoke_check.py'), str(CANDIDATE)], text=True, capture_output=True, timeout=30)
    smoke_passes = smoke.returncode == 0
    smoke_output = (smoke.stdout + smoke.stderr).strip()
    by_id = {item['id']: item for item in pages}
    required_examples = {'example-inner-product-conjugate-linearity-and-orthogonality', 'example-norms-distance-cauchy-completeness', 'example-integrated-hilbert-space-basics', 'example-quantum-states-rays-and-normalization', 'example-dirac-notation-basis-and-adjoint', 'example-bases-coordinates-and-orthonormality'}
    example_ids = {parse_frontmatter(path.read_text(encoding='utf-8'))[0]['id'] for path in (ROOT / 'examples').glob('*.md')}
    example_refs = {rel['target'] for item in pages for rel in item['relationships'] if rel['type'] == 'illustrates'}
    new_defs = {'span', 'linear-independence', 'basis', 'coordinates'}
    checks = {
        'candidate_arrays_nonempty': bool(pages and definitions),
        'all_source_concept_bodies_reflected': all(by_id[key]['body'] == value for key, value in source_bodies.items()),
        'all_current_source_graph_counts': len(pages) == 38 and len(definitions) == 67 and total == 114,
        'all_schema_annotations_generated': sum(len(TOKEN_RE.findall(item['body'])) for item in pages) == sum(schemas.values()) == 84,
        'new_bases_concept_and_definitions_present': 'bases-and-coordinates' in by_id and new_defs <= definition_ids,
        'new_examples_present': required_examples <= example_ids and 'example-bases-coordinates-and-orthonormality' in example_refs,
        'no_material_shrink': len(data) >= len(old_data),
        'popover_math_renderer_retained': '<MathText text={item.text}/>' in candidate['code'],
        'definition_and_link_styling_retained': all(s in candidate['code'] for s in ('bg-amber-50', 'decoration-dotted', 'text-indigo-700', 'DefinitionTerm')),
        'quote_and_warning_behavior_retained': all(s in candidate['code'] for s in ("if(l.startsWith('> [!WARNING]'))", "if(l.startsWith('>'))", '<blockquote')),
        'philosophy_warnings_retained': all('> [!WARNING] Under Construction' in by_id[key]['body'] for key in ('advaita-orientation', 'maya', 'jon-projection-story', 'physics-method-boundary')),
        'optional_bucket_fallback_present': '(grouped[g]??[])' in candidate['code'],
        'typescript_compile_passes': compiled,
        'release_smoke_check_passes': smoke_passes,
    }
    report = {'release': 'version 28', 'live': str(LIVE), 'live_sha256': sha(live_bytes), 'candidate': str(CANDIDATE), 'counts': {'concepts': len(pages), 'definitions': len(definitions), 'examples': len(list((ROOT / 'examples').glob('*.md'))), 'total_nodes': total, 'annotation_pages': len(schemas), 'annotations': sum(schemas.values())}, 'data_chars': {'live': len(old_data), 'candidate': len(data)}, 'checks': checks, 'compiler_output': compiler_output, 'smoke_output': smoke_output}
    REPORT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if all(checks.values()) else 1

if __name__ == '__main__':
    raise SystemExit(main())
