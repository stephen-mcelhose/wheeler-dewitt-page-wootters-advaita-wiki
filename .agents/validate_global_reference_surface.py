#!/usr/bin/env python3
"""Verify source-preserved global Notation Reference reader exposure."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

GUIDE_ID = 'mathematical-notation-reference'
GUIDE_TITLE = 'Mathematical Notation Reference and Reading Cheat Sheet'
CONTROL_LABEL = 'Notation reference'


def fail(message: str) -> int:
    print(f'global-reference surface validation failed: {message}', file=sys.stderr)
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
        guides = array_after(data, 'export const globalReferences:Concept[]=')
        learning_order = array_after(data, 'export const learningOrder:string[]=')
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
        return fail(str(error))
    source = next((node for node in source_nodes if node.get('id') == GUIDE_ID), None)
    if source is None or source.get('type') != 'guide':
        return fail('canonical notation-reference guide is missing from the source index')
    if len(guides) != 1:
        return fail('global reference payload must contain exactly one bounded guide record')
    guide = guides[0]
    required = ('id', 'title', 'summary', 'status', 'path', 'body', 'relationships', 'sources', 'metadata', 'kind')
    if any(key not in guide for key in required):
        return fail('guide record is incomplete')
    for key in ('id', 'title', 'summary', 'path', 'body', 'relationships', 'sources'):
        if guide[key] != source[key]:
            return fail(f'guide does not preserve canonical {key}')
    if guide['kind'] != 'guide' or guide['id'] != GUIDE_ID or guide['title'] != GUIDE_TITLE:
        return fail('guide identity or title is not canonical')
    if GUIDE_ID in learning_order:
        return fail('notation reference must not be added to learningOrder')
    if "const groups=['Mathematical Foundations','Canonical Gravity & Problem of Time','Page–Wootters','Optional Philosophy'];" not in code:
        return fail('sidebar/domain grouping changed')
    required_code = (
        'globalReferences',
        "[...concepts,...examples,...globalReferences]",
        "onClick={()=>nav('mathematical-notation-reference')}",
        f'>{CONTROL_LABEL}</button>',
    )
    if any(token not in code for token in required_code):
        return fail('global header control or same-reader route is missing')
    if code.count(CONTROL_LABEL) != 1:
        return fail('global control label must occur exactly once')
    print('global-reference surface validation passed: canonical guide preserved, globally reachable in the same reader, and excluded from learning/sidebar grouping')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
