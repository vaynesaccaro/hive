#!/usr/bin/env python3
"""PostToolUse — marks session dirty when writes happen."""
import json, os, sys

WRITE_TOOLS = {"Write","Edit","NotebookEdit"}

def main():
    try: data = json.loads(sys.stdin.read())
    except: sys.exit(0)
    if data.get("tool_name","") not in WRITE_TOOLS: sys.exit(0)
    flag_dir = os.path.join(".claude","session")
    os.makedirs(flag_dir, exist_ok=True)
    open(os.path.join(flag_dir,".dirty"),"w").write("1")
    sys.exit(0)

if __name__=="__main__": main()
