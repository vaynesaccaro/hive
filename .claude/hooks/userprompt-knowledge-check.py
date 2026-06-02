#!/usr/bin/env python3
"""UserPromptSubmit — Knowledge Check: runs lookup before sensitive operations."""
import json, os, subprocess, sys

SENSITIVE = ["deploy","dns","ssl","drop ","delete ","rm -rf","migration","force push","truncate","production","webhook","database","schema change","stripe","payment"]

def is_sensitive(p): return any(k in p.lower() for k in SENSITIVE)

def lookup(keywords):
    script=os.path.join("_core","lookup.py")
    if not os.path.exists(script): return ""
    try:
        r=subprocess.run(["python",script,keywords,"--top","5"],capture_output=True,text=True,timeout=10)
        return r.stdout.strip()
    except: return ""

def main():
    try: data=json.loads(sys.stdin.read())
    except: sys.exit(0)
    prompt=data.get("prompt","")
    if not prompt or not is_sensitive(prompt): sys.exit(0)
    found=[k for k in SENSITIVE if k in prompt.lower()]
    extra=[w for w in prompt.split() if len(w)>4][:3]
    kw=" ".join(found[:3]+extra).strip()
    results=lookup(kw)
    if results and "No results" not in results:
        print("[hive/knowledge-check] Relevant past context found:")
        print(results)
        print("— Review before proceeding. —")
    sys.exit(0)

if __name__=="__main__": main()
