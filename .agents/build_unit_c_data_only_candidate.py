#!/usr/bin/env python3
"""Generate only /data.ts from canonical source; preserve live App bytes exactly."""
from __future__ import annotations
import json
import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / '.agents/diffs/unit-c-complete-recovery-candidate/current.json'
OUT = ROOT / '.agents/diffs/unit-c-data-only-preview/current.json'
sys.path.insert(0, str(ROOT / 'scripts'))
sys.path.insert(0, str(ROOT / '.agents'))
from annotation_transform import parse_frontmatter, transform
from generate_learning_order import parse_learning_order

GROUPS = {'mathematics': 'Mathematical Foundations', 'physics': 'Canonical Gravity & Problem of Time', 'page-wootters': 'Page–Wootters', 'philosophy': 'Optional Philosophy'}
LINK = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

def definition(path: Path, ids: set[str]) -> dict:
    meta, body = parse_frontmatter(path.read_text(encoding='utf-8'))
    text = '\n'.join(body.strip().splitlines()[1:]).strip()
    learn = re.search(r'\n*Learn more: \[([^\]]+)\]\(([^)]+)\)\s*$', text)
    target = None
    if learn:
        candidate = Path(learn.group(2)).stem
        target = candidate if candidate in ids else None
        text = text[:learn.start()].strip()
    text = LINK.sub(r'\1', text)
    text = re.sub(r'\s*\n\s*', ' ', text).strip()
    result = {'id': meta['id'].removeprefix('def-'), 'title': meta['title'], 'text': text}
    if target:
        result['target'] = target
    return result

def record(node: dict, group: str, kind: str | None = None) -> dict:
    result = {'id': node['id'], 'title': node['title'], 'summary': node['summary'], 'status': node.get('review_status', 'draft'), 'path': node['path'], 'group': group, 'philosophy': node['path'].startswith('philosophy/'), 'body': node['body'], 'parents': node.get('parents', []), 'relationships': node.get('relationships', []), 'sources': node.get('sources', [])}
    if kind:
        result['kind'] = kind
        result['metadata'] = {key: value for key, value in node.items() if key != 'body'}
    return result

def main() -> None:
    template = json.loads(TEMPLATE.read_text(encoding='utf-8'))
    nodes = json.loads((ROOT / 'viewer/wiki-data.json').read_text(encoding='utf-8'))['nodes']
    index = {node['id']: node for node in nodes}
    concepts = []
    for directory, group in GROUPS.items():
        for path in sorted((ROOT / directory).glob('*.md')):
            meta, _ = parse_frontmatter(path.read_text(encoding='utf-8'))
            if meta.get('type') != 'concept':
                continue
            transformed, result = transform(path.read_text(encoding='utf-8'))
            if result.unmatched:
                raise ValueError(f'unmatched annotations: {meta["id"]}: {result.unmatched}')
            _, body = parse_frontmatter(transformed)
            source = dict(index[meta['id']])
            source['body'] = body
            concepts.append(record(source, group))
    ids = {item['id'] for item in concepts}
    definitions = [definition(path, ids) for path in sorted((ROOT / 'definitions').glob('def-*.md'))]
    examples = [record(node, 'Worked examples', 'example') for node in nodes if node.get('type') == 'example']
    guides = [record(node, 'Global references', 'guide') for node in nodes if node.get('type') == 'guide']
    order = parse_learning_order()
    if set(order) != ids or len(order) != len(ids):
        raise ValueError('learning order does not exactly cover concepts')
    counts = (len(concepts), len(definitions), len(examples), len(guides), len(nodes))
    if counts != (39, 83, 17, 1, 140):
        raise ValueError(f'unexpected canonical counts: {counts}')
    data = (
        "export type Definition={id:string;title:string;text:string;target?:string};export type Relationship={type:string;target:string};export type Source={title:string;url:string;persistent_id?:string};export type Concept={id:string;title:string;summary:string;status:string;path:string;group:string;philosophy:boolean;body:string;parents:string[];relationships:Relationship[];sources:Source[];kind?:'concept'|'example'|'guide';metadata?:Record<string,unknown>};"
        + f"export const totalNodes={len(nodes)};"
        + "export const definitions:Definition[]=" + json.dumps(definitions, ensure_ascii=False, separators=(',', ':')) + ';'
        + "export const examples:Concept[]=" + json.dumps(examples, ensure_ascii=False, separators=(',', ':')) + ';'
        + "export const globalReferences:Concept[]=" + json.dumps(guides, ensure_ascii=False, separators=(',', ':')) + ';'
        + "export const learningOrder:string[]=" + json.dumps(order, ensure_ascii=False, separators=(',', ':')) + ';'
        + "export const concepts:Concept[]=" + json.dumps(concepts, ensure_ascii=False, separators=(',', ':')) + ';'
    )
    candidate = dict(template)
    candidate['files'] = dict(template['files'])
    candidate['files']['/data.ts'] = dict(template['files']['/data.ts'])
    candidate['files']['/data.ts']['code'] = data
    if candidate['code'].encode() != template['code'].encode():
        raise ValueError('App template changed')
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(candidate, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'wrote {OUT}: concepts={len(concepts)} definitions={len(definitions)} examples={len(examples)} guides={len(guides)} total={len(nodes)}')

if __name__ == '__main__':
    main()
