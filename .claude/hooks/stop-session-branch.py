#!/usr/bin/env python3
"""Stop — Session Branch: auto-commit and merge session/* to main."""
import json, os, re, subprocess, sys
from pathlib import Path

# Regex patterns covering common secret formats. Tighten/extend as new providers appear.
SECRET_PATTERNS = [
    re.compile(r"sk-[A-Za-z0-9_\-]{20,}"),
    re.compile(r"sk_live_[A-Za-z0-9]{20,}"),
    re.compile(r"sk_test_[A-Za-z0-9]{20,}"),
    re.compile(r"sbp_[A-Za-z0-9]{20,}"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bASIA[0-9A-Z]{16}\b"),
    re.compile(r"xox[baprs]-[A-Za-z0-9-]{10,}"),
    re.compile(r"AIza[0-9A-Za-z_\-]{35}"),
    re.compile(r"Bearer\s+[A-Za-z0-9._\-]{20,}"),
    re.compile(r"-----BEGIN\s+[A-Z\s]*PRIVATE KEY-----"),
    re.compile(r"""(?ix)\b(api[_-]?key|secret|password|passwd|access[_-]?token|auth[_-]?token|private[_-]?key)\b\s*[:=]\s*['"]?[A-Za-z0-9_\-./+=]{12,}"""),
]

SKIP = [".env", ".vercel/", ".claude/session/"]
MAX_SCAN_BYTES = 2 * 1024 * 1024

def run(cmd): return subprocess.run(cmd, capture_output=True, text=True, cwd=".")
def branch(): return run(["git", "rev-parse", "--abbrev-ref", "HEAD"]).stdout.strip()
def has_changes(): return bool(run(["git", "status", "--porcelain"]).stdout.strip())

def is_sensitive(fp):
    try:
        if os.path.getsize(fp) > MAX_SCAN_BYTES:
            return False
        content = Path(fp).read_text(encoding="utf-8", errors="replace")
        return any(p.search(content) for p in SECRET_PATTERNS)
    except Exception:
        return False

def safe_add():
    to_add = []
    for line in run(["git", "status", "--porcelain"]).stdout.splitlines():
        fp = line[3:].strip()
        if any(s in fp for s in SKIP): continue
        if os.path.isfile(fp) and is_sensitive(fp):
            print(f"[hive] skip sensitive: {fp}", file=sys.stderr)
            continue
        to_add.append(fp)
    if to_add: run(["git", "add", "--"] + to_add)

def main():
    try: json.loads(sys.stdin.read())
    except: pass
    b = branch()
    if not b.startswith("session/"):
        flag = os.path.join(".claude", "session", ".dirty")
        if os.path.exists(flag): os.remove(flag)
        sys.exit(0)
    if not has_changes():
        run(["git", "checkout", "main"]); run(["git", "branch", "-d", b])
        print(f"[hive] empty session removed: {b}", file=sys.stderr); sys.exit(0)
    safe_add()
    if not run(["git", "diff", "--cached", "--name-only"]).stdout.strip():
        run(["git", "checkout", "main"]); run(["git", "branch", "-d", b]); sys.exit(0)
    run(["git", "commit", "-m", f"chore(session): {b}"])
    run(["git", "checkout", "main"])
    m = run(["git", "merge", b, "--no-ff", "-m", f"merge: {b}"])
    if m.returncode != 0:
        print(f"[hive] merge conflict on {b}", file=sys.stderr)
        run(["git", "checkout", b]); sys.exit(1)
    run(["git", "branch", "-d", b])
    flag = os.path.join(".claude", "session", ".dirty")
    if os.path.exists(flag): os.remove(flag)
    print(f"[hive] {b} merged to main", file=sys.stderr)
    sys.exit(0)

if __name__ == "__main__": main()
