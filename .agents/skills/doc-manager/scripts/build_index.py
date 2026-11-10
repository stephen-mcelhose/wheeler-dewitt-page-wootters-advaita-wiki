#!/usr/bin/env python3
import argparse,json,re
from pathlib import Path
def main():
 ap=argparse.ArgumentParser();ap.add_argument("root",nargs="?",default=".");a=ap.parse_args();root=Path(a.root).resolve(); out=[]; skip={"README.md","WIKI_CHARTER.md","concept-index.md","example-index.md","glossary.md","overview-learning-path.md","references.md"}
 for p in sorted(root.rglob("*.md")):
  if any(x in p.parts for x in (".agents","viewer","__pycache__")) or p.name in skip: continue
  s=p.read_text(encoding="utf-8");m=re.match(r"^---\s*\n(.*?)\n---\s*\n",s,re.S)
  if not m: continue
  try: d=json.loads(m.group(1))
  except Exception: continue
  d["path"]=str(p.relative_to(root)).replace("\\","/");d["body"]=s[m.end():].strip();out.append(d)
 out.sort(key=lambda x:x.get("title","")); (root/"viewer"/"wiki-data.json").write_text(json.dumps({"schema_version":"2.0","nodes":out},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 def rows(kind): return [x for x in out if x.get("type")==kind]
 def index(name, items):
  lines=["# "+name,"","Generated; run `make index` after content changes.",""]+[f"- [{x['title']}]({x['path']}) — {x.get('summary','')}" for x in items]
  (root/(name.lower().replace(" ","-")+".md")).write_text("\n".join(lines)+"\n",encoding="utf-8")
 index("Concept Index",rows("concept"));index("Example Index",rows("example"));print(f"Indexed {len(out)} nodes.")
if __name__=="__main__":main()
