#!/usr/bin/env python3
"""
Example HIVE worker — appends a daily heartbeat to the orchestrator's STATE.md.

Use this as a template for your own deterministic jobs:
  - Pure Python, no AI calls
  - Idempotent when possible
  - Writes only to squads/<name>/memory/ or sessions-log/
  - Exit 0 on success, non-zero on failure

Wire it into the harness by adding a line to _core/harness.sh:
  register_worker "workers/example.py" "daily:09:00"

Then schedule the harness itself with cron / systemd / Task Scheduler.
"""
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
STATE = REPO_ROOT / "squads" / "orchestrator" / "memory" / "STATE.md"


def main() -> int:
    if not STATE.exists():
        print(f"[example] orchestrator STATE.md not found at {STATE}", file=sys.stderr)
        return 1
    stamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    line = f"\n<!-- worker:example heartbeat {stamp} -->\n"
    with STATE.open("a", encoding="utf-8") as f:
        f.write(line)
    print(f"[example] heartbeat written to {STATE.relative_to(REPO_ROOT)} at {stamp}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
