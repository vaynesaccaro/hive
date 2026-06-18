#!/usr/bin/env python3
"""
sync-commands.py — Mirror HIVE skills into Claude Code slash commands.

Single source of truth: the *.md files in `skills/` and `squads/*/skills/`.
This script mirrors them into `.claude/commands/` so they show up in the `/` menu:

  skills/<name>.md            -> .claude/commands/<name>.md          (flat)
  squads/<sq>/skills/<name>.md -> .claude/commands/<sq>/<name>.md     (namespaced -> /<sq>:<name>)

It is idempotent: copies new/changed files and removes orphan command files
whose source no longer exists. Files in .claude/commands/ that are NOT managed
by this mirror are left untouched.

Usage:  python _core/sync-commands.py [--check]
        --check : report drift and exit non-zero, write nothing (for CI/hooks).
"""
import sys, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CMD_DIR = ROOT / ".claude" / "commands"


def desired_map():
    """Return {dest_path: src_path} for every skill that should become a command."""
    m = {}
    # Root skills -> flat
    skills_dir = ROOT / "skills"
    if skills_dir.is_dir():
        for src in skills_dir.glob("*.md"):
            m[CMD_DIR / src.name] = src
    # Squad skills -> namespaced subfolder
    for sk in ROOT.glob("squads/*/skills"):
        if not sk.is_dir():
            continue
        squad = sk.parent.name
        for src in sk.glob("*.md"):
            m[CMD_DIR / squad / src.name] = src
    return m


def managed_existing():
    """All .md currently under a managed location (root level + squad subdirs)."""
    if not CMD_DIR.is_dir():
        return set()
    out = set()
    out.update(CMD_DIR.glob("*.md"))            # flat (root skills)
    for sub in CMD_DIR.iterdir():               # one level of squad namespaces
        if sub.is_dir():
            out.update(sub.glob("*.md"))
    return out


def main():
    check = "--check" in sys.argv
    desired = desired_map()
    desired_dests = set(desired)
    existing = managed_existing()

    to_write, to_remove = [], []
    for dest, src in desired.items():
        if not dest.exists() or dest.read_bytes() != src.read_bytes():
            to_write.append((dest, src))
    # Orphans: managed command files with no corresponding source.
    # Only treat squad-subdir files and root files that look skill-derived as managed.
    for dest in existing - desired_dests:
        to_remove.append(dest)

    if check:
        drift = to_write or to_remove
        for d, _ in to_write:
            print(f"[drift] would update: {d.relative_to(ROOT)}")
        for d in to_remove:
            print(f"[drift] would remove: {d.relative_to(ROOT)}")
        if drift:
            print(f"[sync-commands] OUT OF SYNC: {len(to_write)} update(s), {len(to_remove)} removal(s)")
            sys.exit(1)
        print("[sync-commands] in sync")
        sys.exit(0)

    for dest, src in to_write:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)
    for dest in to_remove:
        dest.unlink()
        # prune empty squad dirs
        if dest.parent != CMD_DIR and not any(dest.parent.iterdir()):
            dest.parent.rmdir()

    print(f"[sync-commands] {len(desired)} command(s) mirrored "
          f"({len(to_write)} updated, {len(to_remove)} removed)")


if __name__ == "__main__":
    main()
