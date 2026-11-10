#!/usr/bin/env python3
import argparse, json, re, sys
from pathlib import Path
TYPES={"concept","definition","guide","redirect","example","meditation"}
STATUSES={"draft","ai_reviewed","approved"}
REL_TYPES={"prerequisite-for","formalizes","addresses","derives-from","limitation","contrasts-with","analogical-comparison","historical-context","uses","illustrates","related-to"}
REQ={"schema_version","id","type","title","summary","review_status","relationships","sources"}
CHARTER_HEADINGS=("Purpose and audience","Scope and non-goals","Source and research policy","Canonical document types","Concept and relationship policy","Definition and content-quality policy","Source and provenance policy","Examples policy","Explorer and package workflow","Change, redirect, and version policy","Definition of done")
CONTROL=re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]")
def node(p):
 s=p.read_text(encoding="utf-8")
 m=re.match(r"^---\s*\n(.*?)\n---\s*\n",s,re.S)
 if not m: raise ValueError("missing JSON frontmatter")
 try: d=json.loads(m.group(1))
 except Exception as e: raise ValueError("frontmatter must be JSON: "+str(e))
 return d,s[m.end():]
def math_errors(body):
 out=[]
 if CONTROL.search(body): out.append("contains forbidden control character")
 if body.count(r"\(")!=body.count(r"\)"): out.append("unbalanced inline math delimiters")
 if body.count(r"\[")!=body.count(r"\]"): out.append("unbalanced display math delimiters")
 if "#0" in body or "#$#" in body: out.append("contains obsolete formula delimiter")
 return out
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("root",nargs="?",default="."); a=ap.parse_args(); root=Path(a.root).resolve(); errors=[]; nodes={}; bodies={}; data={}
 skip={"README.md","WIKI_CHARTER.md","concept-index.md","example-index.md","glossary.md","overview-learning-path.md","references.md","CONTRIBUTING.md"}
 charter=root/"WIKI_CHARTER.md"
 if not charter.exists(): errors.append("missing required WIKI_CHARTER.md")
 else:
  ct=charter.read_text(encoding="utf-8")
  for h in CHARTER_HEADINGS:
   if not re.search(r"^##\s+"+re.escape(h)+r"\s*$",ct,re.M): errors.append(f"WIKI_CHARTER.md: missing heading {h!r}")
 for p in root.rglob("*.md"):
  if any(x in p.parts for x in (".agents","viewer","__pycache__",".github","web")) or p.name in skip: continue
  try: d,b=node(p)
  except ValueError as e: errors.append(f"{p.relative_to(root)}: {e}"); continue
  missing=REQ-set(d)
  if missing: errors.append(f"{p.relative_to(root)}: missing {sorted(missing)}")
  if d.get("schema_version")!="2.0": errors.append(f"{p.relative_to(root)}: schema_version must be 2.0")
  if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*",str(d.get("id",""))): errors.append(f"{p.relative_to(root)}: invalid id")
  if d.get("type") not in TYPES: errors.append(f"{p.relative_to(root)}: invalid type")
  if d.get("review_status") not in STATUSES: errors.append(f"{p.relative_to(root)}: review_status must be one of {sorted(STATUSES)}")
  if d.get("id") in nodes: errors.append(f"duplicate id: {d.get('id')}")
  nodes[d.get("id")]=p; bodies[p]=b; data[p]=d
  if d.get("type")=="concept" and "parents" not in d: errors.append(f"{p.relative_to(root)}: concept requires parents")
  if d.get("type")=="redirect" and not d.get("redirect_to"): errors.append(f"{p.relative_to(root)}: redirect requires redirect_to")
  if d.get("type")=="example":
   for k in ("status","patterns","modality","topics","teaches","prerequisites","action","non_conclusion"):
    if k not in d: errors.append(f"{p.relative_to(root)}: example missing {k}")
   if "examples" not in p.parts: errors.append(f"{p.relative_to(root)}: examples must live under examples/")
  for e in math_errors(b): errors.append(f"{p.relative_to(root)}: {e}")
  for x in d.get("sources",[]):
   if not isinstance(x,dict) or not all(x.get(k) for k in ("title","url","persistent_id")): errors.append(f"{p.relative_to(root)}: each source needs title,url,persistent_id")
 for ident,p in nodes.items():
  d=data[p]
  for rel in d.get("relationships",[]):
   if not isinstance(rel,dict) or rel.get("type") not in REL_TYPES or rel.get("target") not in nodes: errors.append(f"{p.relative_to(root)}: invalid/dangling relationship {rel}")
  if d.get("type")=="redirect" and d.get("redirect_to") not in nodes: errors.append(f"{p.relative_to(root)}: dangling redirect")
  for link in re.findall(r"\[[^]]+\]\(([^)#]+)(?:#[^)]+)?\)",bodies[p]):
   if "://" not in link and not (p.parent/link).resolve().exists(): errors.append(f"{p.relative_to(root)}: broken internal link {link}")
 for f in ("README.md","concept-index.md","example-index.md","glossary.md","overview-learning-path.md","references.md","viewer/index.html","start-wiki.py","Makefile"):
  if not (root/f).exists(): errors.append("missing required "+f)
 if errors:
  print("VALIDATION FAILED",file=sys.stderr); print("\n".join("- "+x for x in errors),file=sys.stderr); return 1
 print(f"Validation passed: {len(nodes)} graph nodes."); return 0
if __name__=="__main__": raise SystemExit(main())
