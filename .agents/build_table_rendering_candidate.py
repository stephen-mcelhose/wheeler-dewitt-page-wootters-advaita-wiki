#!/usr/bin/env python3
"""Build the bounded Markdown-table rendering candidate from the live artifact."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / '.agents' / 'current-artifact.json'
OUT = ROOT / '.agents' / 'diffs' / 'notation-reference-table-rendering' / 'current.json'

HELPERS = """function parseTableRow(line:string){return line.trim().replace(/^\\|/,'').replace(/\\|$/,'').split('|').map(cell=>cell.trim())}
function isTableSeparator(line:string){const cells=parseTableRow(line);return cells.length>0&&cells.every(cell=>/^:?-{3,}:?$/.test(cell))}
"""
BRANCH = """if(l.includes('|')&&i+1<lines.length&&isTableSeparator(lines[i+1])){const headers=parseTableRow(l);const rows:string[][]=[];i+=2;while(i<lines.length&&lines[i].trim()&&lines[i].includes('|'))rows.push(parseTableRow(lines[i++]));out.push(<div key={i} className='my-6 overflow-x-auto rounded-xl border border-slate-200 bg-white shadow-sm'><table className='min-w-full border-collapse text-left text-sm leading-6'><thead className='bg-indigo-50 text-slate-900'><tr>{headers.map((cell,column)=><th key={column} scope='col' className='border-b border-slate-200 px-4 py-3 font-bold'><Inline text={cell} defs={defs} onNavigate={onNavigate}/></th>)}</tr></thead><tbody className='divide-y divide-slate-200'>{rows.map((row,rowIndex)=><tr key={rowIndex} className='align-top text-slate-700'>{headers.map((_,column)=><td key={column} className='px-4 py-3'><Inline text={row[column]||''} defs={defs} onNavigate={onNavigate}/></td>)}</tr>)}</tbody></table></div>);continue}"""


def main() -> None:
    artifact = json.loads(BASE.read_text(encoding='utf-8'))
    code = artifact['code']
    inline_end = "return <>{nodes}</>}\nfunction Reader"
    if inline_end not in code:
        raise SystemExit('Inline/Reader insertion point absent')
    code = code.replace(inline_end, "return <>{nodes}</>}\n" + HELPERS + "function Reader", 1)
    branch_point = "if(/^```/.test(l)){const language=l.slice(3).trim();let source='';i++;while(i<lines.length&&!/^```/.test(lines[i]))source+=lines[i++]+'\\n';i++;out.push(<pre key={i} className='my-6 overflow-x-auto rounded-xl bg-slate-950 p-5 text-sm leading-6 text-slate-100 shadow-sm'><code data-language={language}>{source.replace(/\\n$/,'')}</code></pre>);continue}const h="
    if branch_point not in code:
        raise SystemExit('Reader table insertion point absent')
    code = code.replace(branch_point, branch_point[:-len('const h=')] + BRANCH + "const h=", 1)
    artifact['code'] = code
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(artifact, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(OUT)


if __name__ == '__main__':
    main()
