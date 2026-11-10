#!/usr/bin/env python3
"""Verify canonical worked examples are emitted and safely surfaced in the reader."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def fail(message: str) -> int:
    print(f'example-surface validation failed: {message}', file=sys.stderr)
    return 1


def array_after(source: str, marker: str) -> list:
    start = source.find(marker)
    if start < 0:
        raise ValueError(f'missing {marker}')
    value, _ = json.JSONDecoder().raw_decode(source[start + len(marker):])
    if not isinstance(value, list):
        raise ValueError(f'{marker} is not an array')
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('artifact', type=Path)
    parser.add_argument('--source-root', type=Path, required=True)
    args = parser.parse_args()
    try:
        artifact = json.loads(args.artifact.read_text(encoding='utf-8'))
        code = artifact['code']
        data = artifact['files']['/data.ts']['code']
        source_nodes = json.loads((args.source_root / 'viewer' / 'wiki-data.json').read_text(encoding='utf-8'))['nodes']
        examples = array_after(data, 'export const examples:Concept[]=')
        concepts = array_after(data, 'export const concepts:Concept[]=')
        learning_order = array_after(data, 'export const learningOrder:string[]=')
    except (OSError, KeyError, TypeError, json.JSONDecodeError, ValueError) as error:
        return fail(str(error))
    source_examples = [node for node in source_nodes if node.get('type') == 'example']
    source_concepts = {node['id'] for node in source_nodes if node.get('type') == 'concept'}
    emitted = {node.get('id'): node for node in examples}
    if len(emitted) != len(examples) or set(emitted) != {node['id'] for node in source_examples}:
        return fail('emitted example IDs do not exactly match canonical /examples records')
    for source in source_examples:
        record = emitted[source['id']]
        for key in ('title', 'summary', 'status', 'path', 'relationships', 'sources', 'body', 'metadata'):
            if key not in record or not record[key]:
                return fail(f"{source['id']} is missing preserved {key}")
        if record['body'] != source['body'] or record['relationships'] != source['relationships'] or record['sources'] != source['sources']:
            return fail(f"{source['id']} does not preserve canonical body, relationships, or sources")
        targets = [relation.get('target') for relation in record['relationships'] if relation.get('type') == 'illustrates']
        if not targets or any(target not in source_concepts for target in targets):
            return fail(f"{source['id']} lacks a valid illustrated-concept relation")
    for concept in concepts:
        for relation in concept.get('relationships', []):
            if relation.get('type') == 'illustrates' and relation.get('target') not in emitted and relation.get('target') not in source_concepts:
                return fail(f"{concept['id']} illustrates target resolves to neither an emitted example nor a canonical concept")
    if set(learning_order) & set(emitted):
        return fail('examples must be absent from learningOrder')
    required = ('Worked examples', 'workedExamples', 'illustratedConcepts', 'Back to {concept.title}', "selected.kind==='example'?[]", 'examples.filter', 'WORKED EXAMPLE', "selected.kind==='example'&&<Badge>WORKED EXAMPLE</Badge>", "<Badge>WORKED EXAMPLE</Badge><span className='mt-2 block text-sm font-bold text-indigo-800'>{example.title}</span>")
    if any(token not in code for token in required):
        return fail('reader lacks required labeled worked-example/back navigation')
    if not re.search(r"const previousId=learningAt>0", code) or not re.search(r"const nextId=learningAt>=0", code):
        return fail('concept Previous/Next is not learningOrder-only')
    print(f'example-surface validation passed: {len(examples)} canonical examples; {len(concepts)} concepts; examples excluded from {len(learning_order)}-item learningOrder')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
