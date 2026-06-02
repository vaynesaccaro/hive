# Dev — Gotchas & Patterns

> Lessons learned, edge cases, things that burned us. Format: date, what happened, what to do instead.

<!-- Add entries as patterns emerge -->

---

## G001 — Stop hook sentinel must be per-day, not per-branch

**Date:** 2026-06-02
**Symptom:** A stop hook warning (e.g., "session has no log") fires on every Claude Code session, even after the user has already seen it multiple times that day.
**Root cause:** The sentinel file that suppresses repeated warnings was keyed to the session branch name (`stop-warned-session-YYYY-MM-DD-HHMM`). Each new Claude Code session creates a new branch, so the sentinel never exists → warning fires again.

**Wrong:**
```python
def get_sentinel_path():
    branch = run_git(["rev-parse", "--abbrev-ref", "HEAD"])
    branch_slug = branch.replace("/", "-")
    return ROOT / ".git" / f"stop-warned-{branch_slug}"
```

**Correct:**
```python
TODAY = date.today().isoformat()

def get_sentinel_path():
    # Fires at most once per day — matches the warning cadence
    return ROOT / ".git" / f"stop-warned-{TODAY}"
```

**Rule:** Match sentinel granularity to the intended warning cadence. Per-day warning → per-day sentinel. Per-session warning (e.g., different message each session) → per-branch sentinel.
