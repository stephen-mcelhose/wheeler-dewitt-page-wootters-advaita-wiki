#!/usr/bin/env python3
"""Build a source-preserving Explorer candidate with canonical worked examples."""
from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# Never seed a recovery candidate from the failed live artifact. This known-good,
# source-preserving navigation candidate retains the approved reader behavior.
BASE = ROOT / '.agents' / 'diffs' / 'learning-navigation-hotfix' / 'current.json'
OUT = ROOT / '.agents' / 'diffs' / 'worked-examples-explorer-surface' / 'current.json'
GATE = ROOT / '.agents' / 'exact_artifact_tsx_gate.py'
DATA_GATE = ROOT / '.agents' / 'validate_explorer_data_payload.py'
MATH_GATE = ROOT / '.agents' / 'validate_kronecker_delta_math_fixture.py'
GUIDE_GATE = ROOT / '.agents' / 'validate_global_reference_surface.py'


def run_gate(command: list[str]) -> None:
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, timeout=180)
    if result.returncode:
        raise SystemExit((result.stdout + result.stderr).strip())
    print(result.stdout.strip())


def main() -> None:
    if not BASE.exists():
        raise SystemExit(f'required known-good base candidate is missing: {BASE}')
    artifact = json.loads(BASE.read_text(encoding='utf-8'))
    nodes = json.loads((ROOT / 'viewer' / 'wiki-data.json').read_text(encoding='utf-8'))['nodes']
    source_examples = [node for node in nodes if node.get('type') == 'example']
    source_guide = next((node for node in nodes if node.get('id') == 'mathematical-notation-reference' and node.get('type') == 'guide'), None)
    source_total = len(nodes)
    if not source_examples:
        raise SystemExit('canonical index has no examples')
    if source_guide is None:
        raise SystemExit('canonical notation-reference guide is missing')

    data = artifact['files']['/data.ts']['code']
    old_type = "export type Concept={id:string;title:string;summary:string;status:string;path:string;group:string;philosophy:boolean;body:string;parents:string[];relationships:Relationship[];sources:Source[]};"
    new_type = "export type Concept={id:string;title:string;summary:string;status:string;path:string;group:string;philosophy:boolean;body:string;parents:string[];relationships:Relationship[];sources:Source[];kind?:'concept'|'example';metadata?:Record<string,unknown>};"
    if old_type not in data:
        raise SystemExit('expected Concept type declaration is absent')
    data = data.replace(old_type, new_type, 1)
    marker = 'export const concepts:Concept[]='
    if marker not in data or 'export const examples:Concept[]=' in data:
        raise SystemExit('unexpected existing reader example payload state')
    records = []
    for node in source_examples:
        records.append({
            'id': node['id'], 'title': node['title'], 'summary': node['summary'],
            'status': node.get('review_status', 'draft'), 'path': node['path'],
            'group': 'Worked examples', 'philosophy': node['path'].startswith('philosophy/'),
            'body': node['body'], 'parents': node.get('parents', []),
            'relationships': [{'type': r['type'], 'target': r['target']} for r in node.get('relationships', [])],
            'sources': node.get('sources', []), 'kind': 'example',
            'metadata': {key: value for key, value in node.items() if key not in {'body'}},
        })
    payload = json.dumps(records, ensure_ascii=False, separators=(',', ':'))
    data = data.replace(marker, f'export const examples:Concept[]={payload};' + marker, 1)
    guide_record = {
        'id': source_guide['id'], 'title': source_guide['title'], 'summary': source_guide['summary'],
        'status': source_guide.get('review_status', 'draft'), 'path': source_guide['path'],
        'group': 'Global references', 'philosophy': False, 'body': source_guide['body'],
        'parents': source_guide.get('parents', []),
        'relationships': [{'type': relation['type'], 'target': relation['target']} for relation in source_guide.get('relationships', [])],
        'sources': source_guide.get('sources', []), 'kind': 'guide',
        'metadata': {key: value for key, value in source_guide.items() if key != 'body'},
    }
    guide_payload = json.dumps([guide_record], ensure_ascii=False, separators=(',', ':'))
    data = data.replace(marker, f'export const globalReferences:Concept[]={guide_payload};' + marker, 1)
    data = data.replace("kind?:'concept'|'example'", "kind?:'concept'|'example'|'guide'")
    data, changed = re.subn(r'export const totalNodes=\d+;', f'export const totalNodes={source_total};', data, count=1)
    if changed != 1:
        raise SystemExit('totalNodes insertion point is absent')
    artifact['files']['/data.ts']['code'] = data

    code = artifact['code']
    # KaTeX's default not-equal construction uses a private-use overlay glyph in
    # this deployed renderer. Keep canonical TeX in the payload; normalize only
    # the known display fixture to clear textual mathematics before rendering.
    old_math_block = "function MathBlock({latex}:{latex:string}){const clean=latex.trim();let html=clean;try{html=katex.renderToString(clean,{displayMode:true,throwOnError:false,strict:'ignore'})}catch{}"
    new_math_block = "function MathBlock({latex}:{latex:string}){const clean=latex.trim();const rendered=clean.replace(/n\\\\ne m/g,'n\\\\text{ not equal to }m');let html=rendered;try{html=katex.renderToString(rendered,{displayMode:true,throwOnError:false,strict:'ignore'})}catch{}"
    if old_math_block not in code:
        raise SystemExit('expected MathBlock rendering insertion point is absent')
    code = code.replace(old_math_block, new_math_block, 1)
    old_import = "import {concepts,definitions,learningOrder,totalNodes,type Concept,type Definition} from './data';"
    new_import = "import {concepts,examples,globalReferences,definitions,learningOrder,totalNodes,type Concept,type Definition} from './data';"
    if old_import not in code:
        raise SystemExit('expected data import is absent')
    code = code.replace(old_import, new_import, 1)
    code = code.replace("const target=concepts.find(c=>m[4].endsWith(c.path.split('/').pop()||''));", "const target=[...concepts,...examples,...globalReferences].find(c=>m[4].endsWith(c.path.split('/').pop()||''));", 1)

    old_reader = "if(/^\\\\\\[$/.test(l)){let eq='';i++;while(i<lines.length&&!/^\\\\\\]$/.test(lines[i]))eq+=lines[i++]+'\\n';i++;out.push(<MathBlock key={i} latex={eq.trim()}/>);continue}const h="
    new_reader = "if(/^\\\\\\[$/.test(l)){let eq='';i++;while(i<lines.length&&!/^\\\\\\]$/.test(lines[i]))eq+=lines[i++]+'\\n';i++;out.push(<MathBlock key={i} latex={eq.trim()}/>);continue}if(/^```/.test(l)){const language=l.slice(3).trim();let source='';i++;while(i<lines.length&&!/^```/.test(lines[i]))source+=lines[i++]+'\\n';i++;out.push(<pre key={i} className='my-6 overflow-x-auto rounded-xl bg-slate-950 p-5 text-sm leading-6 text-slate-100 shadow-sm'><code data-language={language}>{source.replace(/\\n$/,'')}</code></pre>);continue}const h="
    if old_reader not in code:
        raise SystemExit('reader display-math insertion point is absent')
    code = code.replace(old_reader, new_reader, 1)
    code = code.replace("!/^(#|>|[-*]\\s|\\\\\\[)/.test(lines[i])", "!/^(#|>|[-*]\\s|\\\\\\[|```)/.test(lines[i])", 1)

    old_selection = "export default function App(){const [selectedId,setSelectedId]=useState('hilbert-spaces');const [query,setQuery]=useState('');const selected=concepts.find(x=>x.id===selectedId)||concepts[0];"
    new_selection = "export default function App(){const [selectedId,setSelectedId]=useState('hilbert-spaces');const [query,setQuery]=useState('');const allPages=useMemo(()=>[...concepts,...examples,...globalReferences],[]);const selected=allPages.find(x=>x.id===selectedId)||concepts[0];"
    if old_selection not in code:
        raise SystemExit('reader selection insertion point is absent')
    code = code.replace(old_selection, new_selection, 1)
    old_nav = "const nav=(id:string)=>{if(concepts.some(c=>c.id===id)){setSelectedId(id);window.scrollTo({top:0,behavior:'smooth'})}};"
    new_nav = "const workedExamples=selected.kind==='example'?[]:examples.filter(example=>example.relationships.some(relation=>relation.type==='illustrates'&&relation.target===selected.id)||selected.relationships.some(relation=>relation.type==='illustrates'&&relation.target===example.id));const illustratedConcepts=selected.kind==='example'?concepts.filter(concept=>selected.relationships.some(relation=>relation.type==='illustrates'&&relation.target===concept.id)||concept.relationships.some(relation=>relation.type==='illustrates'&&relation.target===selected.id)):[];const nav=(id:string)=>{if(allPages.some(page=>page.id===id)){setSelectedId(id);window.scrollTo({top:0,behavior:'smooth'})}};"
    if old_nav not in code:
        raise SystemExit('reader navigation insertion point is absent')
    code = code.replace(old_nav, new_nav, 1)

    old_global_header = "<div className='mx-auto flex max-w-7xl items-center gap-3 px-4 py-3 sm:px-6'><div className='flex h-9 w-9 items-center justify-center rounded-lg bg-indigo-600 text-white'><BookOpen size={19}/></div><div><p className='text-xs font-semibold uppercase tracking-[.16em] text-indigo-600'>Annotation reader experiment</p><h1 className='text-base font-bold'>Time, Quantum Cosmology, and Advaita</h1></div><div className='ml-auto hidden w-72 items-center gap-2 rounded-lg border border-slate-200 bg-slate-50 px-3 py-2 md:flex'><Search size={16}/><input className='w-full bg-transparent text-sm outline-none' value={query} onChange={e=>setQuery(e.target.value)} placeholder={`Search ${totalNodes} graph nodes`}/></div></div>"
    new_global_header = "<div className='mx-auto flex max-w-7xl items-center gap-3 px-4 py-3 sm:px-6'><div className='flex h-9 w-9 items-center justify-center rounded-lg bg-indigo-600 text-white'><BookOpen size={19}/></div><div><p className='text-xs font-semibold uppercase tracking-[.16em] text-indigo-600'>Annotation reader experiment</p><h1 className='text-base font-bold'>Time, Quantum Cosmology, and Advaita</h1></div><button type='button' onClick={()=>nav('mathematical-notation-reference')} className='ml-auto whitespace-nowrap text-xs font-medium text-slate-500 underline decoration-slate-300 underline-offset-4 transition hover:text-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-400 focus:ring-offset-2'>Notation reference</button><div className='hidden w-72 items-center gap-2 rounded-lg border border-slate-200 bg-slate-50 px-3 py-2 md:flex'><Search size={16}/><input className='w-full bg-transparent text-sm outline-none' value={query} onChange={e=>setQuery(e.target.value)} placeholder={`Search ${totalNodes} graph nodes`}/></div></div>"
    if old_global_header not in code:
        raise SystemExit('global header insertion point is absent')
    code = code.replace(old_global_header, new_global_header, 1)

    old_header = "<div className='mb-6 flex flex-wrap gap-2'><Badge>Canonical body retained</Badge><Badge tone={selected.status==='draft'?'draft':'indigo'}>{selected.status.replace('_',' ')}</Badge><Badge tone='amber'>58 definitions</Badge></div>"
    new_header = "<div className='mb-6 flex flex-wrap gap-2'><Badge>Canonical body retained</Badge><Badge tone={selected.status==='draft'?'draft':'indigo'}>{selected.status.replace('_',' ')}</Badge><Badge tone='amber'>58 definitions</Badge>{selected.kind==='example'&&<Badge>WORKED EXAMPLE</Badge>}</div>"
    if old_header not in code:
        raise SystemExit('reader status-area insertion point is absent')
    code = code.replace(old_header, new_header, 1)

    old_sections = "<section className='mt-10 border-t border-slate-200 pt-6'><h3 className='font-bold'>Sources & relationships</h3>"
    new_sections = "{workedExamples.length>0&&<section className='mt-10 border-t border-slate-200 pt-6'><h3 className='text-xl font-bold text-slate-900'>Worked examples</h3><p className='mt-2 text-sm leading-6 text-slate-600'>Canonical worked examples linked by the illustrates relationship.</p><div className='mt-4 grid gap-3'>{workedExamples.map(example=><button key={example.id} onClick={()=>nav(example.id)} className='rounded-xl border border-indigo-200 bg-indigo-50 p-4 text-left transition hover:border-indigo-400 hover:bg-indigo-100'><Badge>WORKED EXAMPLE</Badge><span className='mt-2 block text-sm font-bold text-indigo-800'>{example.title}</span><span className='mt-1 block text-sm text-slate-600'>{example.summary}</span><span className='mt-3 inline-flex items-center gap-1 text-sm font-semibold text-indigo-700'>Open worked example <ChevronRight size={16}/></span></button>)}</div></section>}{illustratedConcepts.length>0&&<section className='mt-10 border-t border-slate-200 pt-6'><h3 className='text-xl font-bold text-slate-900'>Illustrated concepts</h3><p className='mt-2 text-sm leading-6 text-slate-600'>This worked example is an exploration route, not a learning-path step.</p><div className='mt-4 flex flex-wrap gap-3'>{illustratedConcepts.map(concept=><button key={concept.id} onClick={()=>nav(concept.id)} className='inline-flex items-center gap-1 rounded-lg border border-indigo-200 bg-white px-4 py-2.5 text-sm font-semibold text-indigo-700 hover:bg-indigo-50'><ChevronLeft size={16}/>Back to {concept.title}</button>)}</div></section>}<section className='mt-10 border-t border-slate-200 pt-6'><h3 className='font-bold'>Sources & relationships</h3>"
    if old_sections not in code:
        raise SystemExit('worked-example section insertion point is absent')
    code = code.replace(old_sections, new_sections, 1)
    artifact['code'] = code
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(artifact, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    # Mandatory final generation gates operate on the just-written exact candidate.
    # Reject unresolved sentinels and incomplete payloads before compiling or publishing.
    run_gate(['python3', str(DATA_GATE), str(OUT), '--label', 'candidate'])
    run_gate(['python3', str(GATE), str(OUT)])
    run_gate(['python3', str(MATH_GATE), str(OUT)])
    run_gate(['python3', str(GUIDE_GATE), str(OUT), '--source-root', str(ROOT)])
    print(f'wrote {OUT} with {len(records)} canonical example records and one global reference guide')

if __name__ == '__main__':
    main()
