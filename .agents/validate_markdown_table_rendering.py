#!/usr/bin/env python3
"""Validate the bounded Markdown-table Reader branch against the notation guide."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

GUIDE_ID = 'mathematical-notation-reference'
HEADER = '| Rendered | Read aloud | Usual local role | Focused example |'
PHI_ROW = r'| \(\phi\) | “phi” | A vector/state label, often paired with \(\psi\). | \(\langle\phi|\psi\rangle\) |'


def fail(message: str) -> int:
    print(f'markdown-table rendering validation failed: {message}', file=sys.stderr)
    return 1


def array_after(source: str, marker: str) -> list[dict]:
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
    args = parser.parse_args()
    try:
        artifact = json.loads(args.artifact.read_text(encoding='utf-8'))
        code = artifact['code']
        data = artifact['files']['/data.ts']['code']
        guides = array_after(data, 'export const globalReferences:Concept[]=')
        guide = next(item for item in guides if item.get('id') == GUIDE_ID)
        body = guide['body']
    except (OSError, KeyError, StopIteration, TypeError, ValueError, json.JSONDecodeError) as error:
        return fail(f'cannot load exact artifact: {error}')

    required_reader_tokens = (
        'function parseTableRow(',
        'function isTableSeparator(',
        "if(l.includes('|')&&i+1<lines.length&&isTableSeparator(lines[i+1]))",
        "<table className='min-w-full border-collapse text-left text-sm leading-6'>",
        '<thead className=',
        '<tbody className=',
        "<th key={column} scope='col' className=",
        "<td key={column} className=",
        '<Inline text={cell} defs={defs} onNavigate={onNavigate}/>',
        "overflow-x-auto rounded-xl border border-slate-200 bg-white",
    )
    missing = [token for token in required_reader_tokens if token not in code]
    if missing:
        return fail('Reader lacks required table rendering tokens: ' + ', '.join(repr(token) for token in missing))
    if 'headers.map((cell,column)=><th' not in code or 'rows.map((row,rowIndex)=><tr' not in code or "<Inline text={row[column]||''} defs={defs} onNavigate={onNavigate}/>" not in code:
        return fail('Reader does not render both header and body cells through Inline')
    for token in ("if(/^\\\\\\[$/.test(l))", "if(/^```/.test(l))", "|```)/.test(lines[i])"):
        if token not in code:
            return fail(f'existing display-math/code-block branch guard is missing: {token!r}')
    if HEADER not in body or PHI_ROW not in body:
        return fail('canonical Greek-letters table header or phi row is absent from exact artifact data')
    if r'\(|\psi\rangle\)' not in body or r'\(\langle\phi|\psi\rangle\)' not in body:
        return fail('canonical inline-math table-cell fixtures are absent')
    print('markdown-table rendering validation passed: Reader has bounded accessible table branch; Greek-letters header/phi row and inline-math cells retained; display-math/code branches guarded')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
