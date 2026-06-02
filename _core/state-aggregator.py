#!/usr/bin/env python3
"""
HIVE State Aggregator
Reads L1 from all squad STATE.md files and outputs a company-wide snapshot.
Used by /status skill.

Usage:
  python _core/state-aggregator.py
  python _core/state-aggregator.py squads/
  python _core/state-aggregator.py --json
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent


def extract_l1(state_path: Path) -> str | None:
    try:
        content = state_path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return None

    match = re.search(r"\[L1\]\s*\n(.*?)(?:\[L2\]|\Z)", content, re.DOTALL)
    if not match:
        return None

    l1 = match.group(1).strip()
    return l1 if l1 else None


def get_squads(squads_dir: Path) -> list[dict]:
    squads = []
    if not squads_dir.exists():
        return squads

    for squad_name in sorted(os.listdir(squads_dir)):
        squad_path = squads_dir / squad_name
        state_path = squad_path / "memory" / "STATE.md"

        if not state_path.exists():
            continue

        l1 = extract_l1(state_path)
        mtime = datetime.fromtimestamp(state_path.stat().st_mtime).strftime("%Y-%m-%d %H:%M")

        squads.append({
            "squad": squad_name,
            "l1": l1 or "(no L1 content)",
            "updated": mtime,
            "state_path": str(state_path.relative_to(REPO_ROOT)),
        })

    return squads


def main():
    parser = argparse.ArgumentParser(description="HIVE State Aggregator")
    parser.add_argument("squads_dir", nargs="?", default="squads",
                        help="Path to squads directory (default: squads/)")
    parser.add_argument("--json", action="store_true", dest="json_out",
                        help="Output as JSON")
    args = parser.parse_args()

    squads_dir = REPO_ROOT / args.squads_dir
    squads = get_squads(squads_dir)

    if not squads:
        print("No squads found with STATE.md.")
        return

    if args.json_out:
        print(json.dumps(squads, indent=2, ensure_ascii=False))
        return

    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print(f"\n{'='*60}")
    print(f"  HIVE Status — {now}")
    print(f"{'='*60}\n")

    for s in squads:
        print(f"  [{s['squad']}]  (updated {s['updated']})")
        for line in s["l1"].splitlines():
            print(f"    {line}")
        print()

    print(f"{'='*60}")
    print(f"  {len(squads)} squads reporting\n")


if __name__ == "__main__":
    main()
