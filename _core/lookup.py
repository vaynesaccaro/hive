#!/usr/bin/env python3
"""
HIVE Knowledge Lookup
Searches incidents, sessions-log, and memory files for relevant context.
Run before sensitive operations: deploy, DNS, database changes, integrations.

Usage:
  python _core/lookup.py "deploy vercel"
  python _core/lookup.py "auth" --source incidents
  python _core/lookup.py "database" --source sessions --since 2026-01-01
  python _core/lookup.py "webhook" --json --top 5
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent


def search_files(directories: list[Path], keywords: list[str], since: str | None = None) -> list[dict]:
    results = []
    since_dt = None
    if since:
        try:
            since_dt = datetime.fromisoformat(since).replace(tzinfo=timezone.utc)
        except ValueError:
            print(f"Warning: invalid --since date '{since}', ignoring", file=sys.stderr)

    for directory in directories:
        if not directory.exists():
            continue
        for path in directory.rglob("*.md"):
            try:
                content = path.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue

            if since_dt:
                mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
                if mtime < since_dt:
                    continue

            content_lower = content.lower()
            matched_keywords = [kw for kw in keywords if kw.lower() in content_lower]
            if not matched_keywords:
                continue

            # Extract first meaningful excerpt (up to 300 chars around first match)
            first_kw = matched_keywords[0].lower()
            idx = content_lower.find(first_kw)
            start = max(0, idx - 100)
            end = min(len(content), idx + 200)
            excerpt = content[start:end].strip().replace("\n", " ")

            results.append({
                "file": str(path.relative_to(REPO_ROOT)),
                "matched": matched_keywords,
                "excerpt": excerpt,
                "modified": datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d"),
            })

    # Sort by modification date descending
    results.sort(key=lambda x: x["modified"], reverse=True)
    return results


def get_directories(source: str | None) -> list[Path]:
    all_sources = {
        "incidents": [REPO_ROOT / "incidents"],
        "sessions": [REPO_ROOT / "sessions-log"],
        "memory": (
            [REPO_ROOT / "memory"]
            + [REPO_ROOT / "squads" / sq / "memory" for sq in os.listdir(REPO_ROOT / "squads")
               if (REPO_ROOT / "squads" / sq / "memory").exists()]
        ),
    }
    if source and source in all_sources:
        return all_sources[source]
    # All sources
    dirs = []
    for d_list in all_sources.values():
        dirs.extend(d_list)
    return dirs


def main():
    parser = argparse.ArgumentParser(description="HIVE Knowledge Lookup")
    parser.add_argument("query", help="Search keywords (space-separated)")
    parser.add_argument("--source", choices=["incidents", "sessions", "memory"],
                        help="Limit search to one source")
    parser.add_argument("--since", help="Only files modified after this date (YYYY-MM-DD)")
    parser.add_argument("--top", type=int, default=10, help="Max results to show (default: 10)")
    parser.add_argument("--json", action="store_true", dest="json_out", help="Output as JSON")
    args = parser.parse_args()

    keywords = args.query.split()
    directories = get_directories(args.source)
    results = search_files(directories, keywords, args.since)
    results = results[: args.top]

    if args.json_out:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return

    if not results:
        print(f"No results for: {args.query}")
        return

    print(f"\nResults for '{args.query}' ({len(results)} found):\n")
    for r in results:
        print(f"  [{r['modified']}] {r['file']}")
        print(f"  Matched: {', '.join(r['matched'])}")
        print(f"  ...{r['excerpt']}...")
        print()


if __name__ == "__main__":
    main()
