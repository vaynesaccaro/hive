#!/usr/bin/env python3
"""Stop — Session Branch: auto-commit and merge session/* to main."""
import json, os, subprocess, sys
from pathlib import Path

SENSITIVE = ["sk-","Bearer ","password=","api_key=","token=","secret=","PRIVATE KEY"]
SKIP = [".env",".vercel/",".claude/session/"]

def run(cmd): return subprocess.run(cmd,capture_output=True,text=True,cwd=".")
def branch(): return run(["git","rev-parse","--abbrev-ref","HEAD"]).stdout.strip()
def has_changes(): return bool(run(["git","status","--porcelain"]).stdout.strip())

def is_sensitive(fp):
    try: return any(p in Path(fp).read_text(encoding="utf-8",errors="replace") for p in SENSITIVE)
    except: return False

def safe_add():
    to_add=[]
    for line in run(["git","status","--porcelain"]).stdout.splitlines():
        fp=line[3:].strip()
        if any(s in fp for s in SKIP): continue
        if os.path.isfile(fp) and is_sensitive(fp): print(f"[hive] skip sensitive: {fp}",file=sys.stderr); continue
        to_add.append(fp)
    if to_add: run(["git","add","--"]+to_add)

def main():
    try: json.loads(sys.stdin.read())
    except: pass
    b=branch()
    if not b.startswith("session/"):
        flag=os.path.join(".claude","session",".dirty")
        if os.path.exists(flag): os.remove(flag)
        sys.exit(0)
    if not has_changes():
        run(["git","checkout","main"]); run(["git","branch","-d",b])
        print(f"[hive] empty session removed: {b}",file=sys.stderr); sys.exit(0)
    safe_add()
    if not run(["git","diff","--cached","--name-only"]).stdout.strip():
        run(["git","checkout","main"]); run(["git","branch","-d",b]); sys.exit(0)
    run(["git","commit","-m",f"chore(session): {b}"])
    run(["git","checkout","main"])
    m=run(["git","merge",b,"--no-ff","-m",f"merge: {b}"])
    if m.returncode!=0:
        print(f"[hive] merge conflict on {b}",file=sys.stderr)
        run(["git","checkout",b]); sys.exit(1)
    run(["git","branch","-d",b])
    flag=os.path.join(".claude","session",".dirty")
    if os.path.exists(flag): os.remove(flag)
    print(f"[hive] {b} merged to main",file=sys.stderr)
    sys.exit(0)

if __name__=="__main__": main()
