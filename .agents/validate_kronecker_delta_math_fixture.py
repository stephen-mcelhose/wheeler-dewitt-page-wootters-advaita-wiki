#!/usr/bin/env python3
"""Validate the exact Explorer Kronecker-delta display-math fixture."""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KATEX = ROOT / '.agents' / 'tscheck' / 'node_modules' / 'katex'
FIXTURE_ID = 'example-dirac-notation-basis-and-adjoint'
CANONICAL_NE_TEX = r'0,&n\ne m.'
CANONICAL_NEQ_TEX = r'0,&n\neq m.'
SOURCE_FORMS = (r'n\ne m', r'n\neq m')
SAFE_RELATION_TEX = r'n\text{ not equal to } m'
PRIVATE_USE = re.compile(r'[\ue000-\uf8ff]')


def fail(message: str) -> int:
    print(f'Kronecker-delta math fixture failed: {message}', file=sys.stderr)
    return 1


def payload_after(source: str, marker: str) -> list[dict]:
    start = source.find(marker)
    if start < 0:
        raise ValueError(f'missing {marker}')
    value, _ = json.JSONDecoder().raw_decode(source[start + len(marker):])
    if not isinstance(value, list):
        raise ValueError(f'{marker} is not an array')
    return value


def render(tex: str) -> str:
    program = """const katex=require(process.argv[1]);
const tex=process.argv[2];
process.stdout.write(katex.renderToString(tex,{displayMode:true,throwOnError:false,strict:'ignore'}));
"""
    result = subprocess.run(['node', '-e', program, str(KATEX), tex], text=True, capture_output=True, timeout=30)
    if result.returncode:
        raise ValueError(result.stderr.strip() or 'KaTeX rendering failed')
    return result.stdout


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('artifact', type=Path, help='exact candidate or live artifact JSON')
    args = parser.parse_args()
    try:
        artifact = json.loads(args.artifact.read_text(encoding='utf-8'))
        code = artifact['code']
        data = artifact['files']['/data.ts']['code']
        examples = payload_after(data, 'export const examples:Concept[]=')
        fixture = next(item for item in examples if item.get('id') == FIXTURE_ID)
        body = fixture['body']
    except (OSError, KeyError, StopIteration, TypeError, ValueError, json.JSONDecodeError) as error:
        return fail(f'cannot load actual artifact fixture: {error}')
    if CANONICAL_NE_TEX not in body:
        return fail('actual emitted Kronecker fixture does not preserve the canonical n\\ne m condition')
    guides = payload_after(data, 'export const globalReferences:Concept[]=')
    notation = next(item for item in guides if item.get('id') == 'mathematical-notation-reference')
    if CANONICAL_NEQ_TEX not in notation.get('body', ''):
        return fail('actual emitted notation fixture does not preserve the canonical n\\neq m condition')
    if '\\begin{cases}' not in body or '\\end{cases}' not in body:
        return fail('actual emitted fixture has malformed cases markup')
    if body.count('\\begin{cases}') != 1 or body.count('\\end{cases}') != 1:
        return fail('actual emitted fixture has unbalanced cases markup')
    expected_renderer = "const rendered=clean.replace(/\\\\(?:neq|ne)(?![A-Za-z])/g,'\\\\text{ not equal to }');"
    if expected_renderer not in code:
        return fail('MathBlock does not contain the approved general \ne/\neq safe relation-token normalization')
    for source_form in SOURCE_FORMS:
        rendered = re.sub(r'\\(?:neq|ne)(?![A-Za-z])', lambda _: r'\text{ not equal to }', source_form)
        if rendered != SAFE_RELATION_TEX:
            return fail(f'MathBlock normalization does not convert {source_form!r} to clear text math')
        try:
            html = render(rendered)
        except ValueError as error:
            return fail(str(error))
        if 'katex-error' in html or PRIVATE_USE.search(html):
            return fail(f'safe rendering for {source_form!r} contains KaTeX error or private-use glyph output')
        if 'not equal to' not in html:
            return fail(f'safe rendering for {source_form!r} does not expose a clear not-equal condition')
    print('Kronecker-delta math fixture passed: exact artifact preserves canonical n\\ne m and n\\neq m source forms; MathBlock renders both as clear "n not equal to m" without private-use glyphs')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
