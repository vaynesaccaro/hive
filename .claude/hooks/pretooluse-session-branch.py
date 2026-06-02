#!/usr/bin/env python3
"""
PreToolUse — Session Branch
Creates a session/YYYY-MM-DD-HHMM branch on the first write operation of a session.
"""
import json, subprocess, sys
from datetime import datetime

WRITE_TOOLS = {"Write","Edit","Bash","NotebookEdit"}

def get_branch():
    r = subprocess.run(["git","rev-parse","--abbrev-ref","HEAD"],capture_output=True,text=True)
    return r.stdout.strip()

def main():
    try: data = json.loads(sys.stdin.read())
    except: sys.exit(0)
    tool = data.get("tool_name","")
    if tool not in WRITE_TOOLS: sys.exit(0)
    if tool == "Bash":
        cmd = data.get("tool_input",{}).get("command","")
        WRITE_PATTERNS = [">","tee ","git add","git commit","git merge","cp ","mv ","rm ","mkdir ","touch ","sed -i","chmod ","chown "]
        if not any(w in cmd for w in WRITE_PATTERNS): sys.exit(0)
    branch = get_branch()
    if branch in ("main","HEAD"):
        nb = f"session/{datetime.now().strftime('%Y-%m-%d-%H%M')}"
        subprocess.run(["git","checkout","-b",nb],capture_output=True)
        print(f"[hive] session branch: {nb}",file=sys.stderr)
    sys.exit(0)

if __name__=="__main__": main()
