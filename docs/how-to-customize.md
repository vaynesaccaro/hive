# How to Customize HIVE

HIVE is designed to be forked and adapted. This guide covers the most common customizations.

---

## Rename personas

The default personas (Victor, Leah, Maya...) are generic names. Replace them with whatever fits your company culture.

In `squads/<name>/CLAUDE.md`, edit the persona section:
```markdown
## Persona

**Your Name Here** — Head of Sales.
[Edit the personality description to match your culture]
```

No other changes needed — the persona name is only in the CLAUDE.md.

---

## Add or remove squads

### Removing a squad

If you don't need a squad (e.g., no Dev squad because you're non-technical):

1. Remove it from the squads table in root `CLAUDE.md`
2. Update `squads/<name>/memory/STATE.md` L1 to: `Squad inactive — not used in this installation.`
3. Optionally delete the folder entirely

### Adding a squad

Create the folder structure:
```bash
mkdir -p squads/my-squad/{context,memory,foundation,skills,workers,data}
```

Create `squads/my-squad/CLAUDE.md` following the pattern of existing squads:
- Persona section
- Scope (what it covers + what it doesn't)
- Foundation table
- Memory schema
- Absolute rules
- Skills list

Add it to the root `CLAUDE.md` squads table.

---

## Add sub-squads

For squads that need specialization (e.g., multiple products under Product, multiple regions under CS):

```
squads/product/
  CLAUDE.md              ← Owen — Head of Product (parent context)
  saas/
    CLAUDE.md            ← Owen-SaaS — focused on SaaS product
    memory/STATE.md
  services/
    CLAUDE.md            ← Owen-Services — focused on services
    memory/STATE.md
```

The parent CLAUDE.md acts as a router — it describes the sub-squads and when to use each.

---

## Switch project management tools

HIVE ships with **Linear** as default. Here's how to switch.

### Why Linear is the default

Linear's MCP integration with Claude Code is the deepest available — issues, cycles, projects, and comments all become native context for the agent. For teams using AI heavily, this integration pays off.

### Switching to GitHub Issues

1. In root `CLAUDE.md`, replace the PM section:
```markdown
## Project management
HIVE uses **GitHub Issues**. Reference issues as `#123`.
Use labels for squad routing: `commercial`, `cs`, `dev`, etc.
```

2. Remove Linear-specific skills if any
3. Add a skill that creates GitHub issues via `gh` CLI if needed

### Switching to Jira

1. Update the PM section in root `CLAUDE.md` with your Jira project key and workflow
2. Wire Jira MCP if available, or use the Jira REST API via a custom skill

### No PM tool

If you prefer to track work in STATE.md directly (pure harness, no external tool):

1. Remove the PM section from root `CLAUDE.md`
2. Use L2 in STATE.md as your task list
3. Use `memory/decisions.md` for decision logs

---

## Add custom skills

Skills are markdown files. Drop them in:
- `skills/` — available globally
- `squads/<name>/skills/` — available only in that squad

Skill format:
```markdown
# /my-skill-name

Brief description of what it does.

## When to activate
[Trigger conditions]

## Steps
[Numbered steps the agent follows]

## Rules
[Guardrails]
```

---

## Add workers

Workers are Python scripts in `workers/`. Register them in `_core/harness.sh`:

```bash
run_worker "workers/my-worker.py" "09:00"          # runs daily at 9am
run_worker "workers/my-worker.py" "every:1h"       # runs every hour
```

Workers must:
- Be deterministic (no randomness, no LLM calls)
- Write output to `squads/<name>/memory/STATE.md` only
- Exit 0 on success, non-zero on failure

---

## Customize the memory schema

The default L1/L2/L3 schema works for most squads. To change what a squad tracks in each layer, edit the `## Memory schema` section in `squads/<name>/CLAUDE.md`.

Example — CS squad with customer count in L1:
```markdown
## Memory schema
`memory/STATE.md`:
- **L1:** Active customers (N), churn risk (N), open onboardings
- **L2:** In-flight onboardings, at-risk accounts being worked
- **L3:** Expansion opportunities, churn post-mortems pending
```

---

## Use a different LLM

HIVE is built on Claude Code, but the architecture is LLM-agnostic. The CLAUDE.md files are instructions — any instruction-following model can use them.

To adapt for another tool:
- **Cursor / Windsurf**: rename `CLAUDE.md` to `.cursorrules` or the equivalent
- **Custom agent**: pass `CLAUDE.md` content as system prompt
- **OpenAI Assistants**: use `CLAUDE.md` as the assistant instructions file

Hook scripts (`.claude/hooks/`) are Claude Code-specific and would need reimplementation for other environments.

### Writing custom stop hooks

If you add a stop hook that warns the user about something (e.g., missing session log, uncommitted state), use a **sentinel file** to avoid repeating the warning every session:

```python
from datetime import date
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent  # adjust to your repo root
TODAY = date.today().isoformat()

def get_sentinel_path():
    # Per-day sentinel: warn at most once per day
    return ROOT / ".git" / f"stop-warned-{TODAY}"

def sentinel_exists():
    return get_sentinel_path().exists()

def write_sentinel():
    try:
        get_sentinel_path().write_text(TODAY, encoding="utf-8")
    except Exception:
        pass

def main():
    if sentinel_exists():
        sys.exit(0)  # already warned today

    # ... your checks ...

    if warnings:
        write_sentinel()
        print("\n".join(warnings), file=sys.stderr)
        sys.exit(2)  # non-blocking: shows warning but doesn't stop Claude

    sys.exit(0)
```

**Common mistake:** keying the sentinel to the session branch name instead of the date. Each Claude Code session creates a new branch (`session/YYYY-MM-DD-HHMM`), so a per-branch sentinel never suppresses — the warning fires on every session. See `squads/dev/memory/gotchas.md` → G001.

---

## Keep upstream changes

If you forked HIVE and want to pull in framework updates:

```bash
git remote add upstream https://github.com/felipeluissalgueiro/hive.git
git fetch upstream
git merge upstream/main --no-ff
```

Conflicts will appear in `squads/<name>/context/` and `memory/` files — these are your customizations. Always resolve in your favor for those files; accept upstream changes for `_core/`, `skills/`, and framework CLAUDE.md files.
