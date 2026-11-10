#!/usr/bin/env python3
"""Build a source-preserving Spectra preview candidate from the integrity-validated live reader."""
from __future__ import annotations
import json, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
sys.path.insert(0,str(ROOT/'.agents'))
from annotation_transform import parse_frontmatter, transform
from generate_learning_order import parse_learning_order

ROOT=Path(__file__).resolve().parents[1]
# Recovery invariant: never rebuild from a malformed or partial live artifact.
# This exact candidate is the last known-good complete reader baseline.
BASE=ROOT/'.agents/diffs/not-equal-relation-token-hotfix/current.json'
OUT=ROOT/'.agents/diffs/unit-c-complete-recovery-candidate/current.json'
GROUPS={'mathematics':'Mathematical Foundations','physics':'Canonical Gravity & Problem of Time','page-wootters':'Page–Wootters','philosophy':'Optional Philosophy'}
CONTENT=('mathematics','physics','page-wootters','philosophy')
LINK=re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

def definition(path:Path, ids:set[str])->dict:
    meta, body=parse_frontmatter(path.read_text(encoding='utf-8'))
    text='\n'.join(body.strip().splitlines()[1:]).strip()
    learn=re.search(r'\n*Learn more: \[([^\]]+)\]\(([^)]+)\)\s*$',text)
    target=None
    if learn:
        candidate=Path(learn.group(2)).stem
        target=candidate if candidate in ids else None
        text=text[:learn.start()].strip()
    text=LINK.sub(r'\1',text)
    text=re.sub(r'\s*\n\s*',' ',text).strip()
    record={'id':meta['id'].removeprefix('def-'),'title':meta['title'],'text':text}
    if target: record['target']=target
    return record

def record(node:dict, group:str, kind:str|None=None)->dict:
    out={'id':node['id'],'title':node['title'],'summary':node['summary'],'status':node.get('review_status','draft'),'path':node['path'],'group':group,'philosophy':node['path'].startswith('philosophy/'),'body':node['body'],'parents':node.get('parents',[]),'relationships':node.get('relationships',[]),'sources':node.get('sources',[])}
    if kind:
        out['kind']=kind
        out['metadata']={key:value for key,value in node.items() if key!='body'}
    return out

def main():
    if not BASE.exists(): raise ValueError(f'known-good reader baseline is missing: {BASE}')
    live=json.loads(BASE.read_text(encoding='utf-8'))
    nodes=json.loads((ROOT/'viewer/wiki-data.json').read_text(encoding='utf-8'))['nodes']
    index={n['id']:n for n in nodes}
    concepts=[]
    for directory in CONTENT:
        for path in sorted((ROOT/directory).glob('*.md')):
            meta, _=parse_frontmatter(path.read_text(encoding='utf-8'))
            if meta.get('type')!='concept': continue
            transformed, result=transform(path.read_text(encoding='utf-8'))
            if result.unmatched: raise ValueError(f'unmatched annotations: {meta["id"]}: {result.unmatched}')
            _, body=parse_frontmatter(transformed)
            node=dict(index[meta['id']]); node['body']=body
            concepts.append(record(node,GROUPS[directory]))
    ids={c['id'] for c in concepts}
    definitions=[definition(p,ids) for p in sorted((ROOT/'definitions').glob('def-*.md'))]
    examples=[record(n,'Worked examples','example') for n in nodes if n.get('type')=='example']
    guides=[record(n,'Global references','guide') for n in nodes if n.get('type')=='guide']
    order=parse_learning_order()
    if set(order)!=ids or len(order)!=len(ids): raise ValueError('learning order does not exactly cover concepts')
    if len(guides)!=1 or guides[0]['id']!='mathematical-notation-reference': raise ValueError('notation guide invariant failed')
    data=("export type Definition={id:string;title:string;text:string;target?:string};export type Relationship={type:string;target:string};export type Source={title:string;url:string;persistent_id?:string};export type Concept={id:string;title:string;summary:string;status:string;path:string;group:string;philosophy:boolean;body:string;parents:string[];relationships:Relationship[];sources:Source[];kind?:'concept'|'example'|'guide';metadata?:Record<string,unknown>};"+f"export const totalNodes={len(nodes)};"+"export const definitions:Definition[]="+json.dumps(definitions,ensure_ascii=False,separators=(',',':'))+";export const examples:Concept[]="+json.dumps(examples,ensure_ascii=False,separators=(',',':'))+";export const globalReferences:Concept[]="+json.dumps(guides,ensure_ascii=False,separators=(',',':'))+";export const learningOrder:string[]="+json.dumps(order,ensure_ascii=False,separators=(',',':'))+";export const concepts:Concept[]="+json.dumps(concepts,ensure_ascii=False,separators=(',',':'))+";")
    code=live['code']
    required_table_tokens=('function parseTableRow(', 'function isTableSeparator(', "if(l.includes('|')&&i+1<lines.length&&isTableSeparator(lines[i+1]))")
    if any(token not in code for token in required_table_tokens): raise ValueError('integrity-validated table reader baseline is missing')
    code=code.replace("<p>67 definition nodes retained</p>",f"<p>{len(definitions)} definition nodes retained</p>",1)
    code=code.replace("<Badge tone='amber'>58 definitions</Badge>",f"<Badge tone='amber'>{len(definitions)} definitions</Badge>",1)
    artifact=dict(live); artifact['code']=code; artifact['files']=dict(live['files']); artifact['files']['/data.ts']=dict(live['files']['/data.ts']); artifact['files']['/data.ts']['code']=data
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(artifact,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'wrote {OUT}: concepts={len(concepts)} definitions={len(definitions)} examples={len(examples)} guides={len(guides)} total={len(nodes)} from known-good baseline {BASE}')
if __name__=='__main__': main()
