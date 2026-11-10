#!/usr/bin/env python3
import os, subprocess, sys, zipfile
from pathlib import Path
root=Path('.').resolve(); name=root.name; target=root.parent/(name+'.zip')
if subprocess.run([sys.executable,'.agents/skills/doc-manager/scripts/validate.py','.'],check=False).returncode: raise SystemExit('Package aborted: validation failed.')
files=[]
for p in root.rglob('*'):
 if p.is_file() and '__pycache__' not in p.parts and p.resolve()!=target.resolve() and not p.name.endswith('.zip'): files.append(p)
files.sort(key=lambda x:str(x.relative_to(root)))
with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
 for p in files:
  info=zipfile.ZipInfo(name+'/'+str(p.relative_to(root)).replace(os.sep,'/'));info.date_time=(1980,1,1,0,0,0);info.compress_type=zipfile.ZIP_DEFLATED;info.external_attr=0o644<<16
  z.writestr(info,p.read_bytes())
print(target)
