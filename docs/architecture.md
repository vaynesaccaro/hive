# HIVE Architecture

## Overview

HIVE is a folder structure + conventions that makes Claude Code behave like a team of specialists. No framework lock-in — just markdown files, Python scripts, and git.

```
hive/
  CLAUDE.md              ← Root context: Stamper persona + squad table + rules
  .claude/
    settings.json        ← Hook event wiring
    hooks/               ← 9 automation hooks (Python)
  _core/                 ← Framework engine
  squads/                ← 11 specialized agents
  skills/                ← Global reusable commands
  memory/                ← Global orchestrator memory
  workers/               ← Deterministic cron scripts
  incidents/             ← Incident log hub
  sessions-log/          ← Session history
  docs/                  ← This folder
```

---

## How Claude Code loads context

Claude Code reads `CLAUDE.md` files in cascade — starting from the current working directory up to the repo root. HIVE exploits this:

- Open `hive/` → loads root `CLAUDE.md` (Stamper)
- Open `hive/squads/commercial/` → loads both root + `squads/commercial/CLAUDE.md` (Stamper + Victor)
- Open `hive/squads/dev/` → loads both root + `squads/dev/CLAUDE.md` (Stamper + Ethan)

Each squad's `CLAUDE.md` defines:
- **Persona** — name, role, operating principles
- **Scope** — what this squad owns vs. what it defers
- **Foundation table** — which files to read before working
- **Memory schema** — what L1/L2/L3 contains for this squad
- **Absolute rules** — non-negotiable behaviors

---

## Memory system

### 3-layer STATE.md

Every squad maintains `memory/STATE.md` with three layers:

```
[L1]
Current status — what's happening right now. 1-3 lines.
Stamper reads this when aggregating /status.

[L2]
In progress — active tasks, current work, pending reviews.

[L3]
Backlog — queued items, not started, low urgency.
```

L1 is designed to be machine-readable for aggregation. Keep it factual, not narrative.

### Memory files

Each squad's `memory/` folder contains:

| File | Purpose |
|---|---|
| `STATE.md` | Live operational state (L1/L2/L3) |
| `decisions.md` | Architectural and operational decisions log |
| `gotchas.md` | Known pitfalls, lessons learned, edge cases |
| `MEMORY.md` | Index of all saved memory files |

Additional memory files can be added as needed — project context, reference data, historical records.

### Global vs. squad memory

- **Global memory** (`memory/` at root) — Stamper's cross-squad context, company-level decisions
- **Squad memory** (`squads/<name>/memory/`) — isolated per squad, only loaded when that squad is open

---

## Hooks

9 hooks automate operational housekeeping. All are Python scripts in `.claude/hooks/`.

### PreToolUse — session branch

```python
# Fires before any tool call that writes files
# Creates session/YYYY-MM-DD-HHMM branch on first edit
# Prevents direct commits to main during a session
```

### PostToolUse — state dirty flag

```python
# Fires after tool calls that modify squad files
# Marks STATE.md as dirty when squad context changes
# Used by stop hook to decide what to commit
```

### Stop — session merge

```python
# Fires when Claude Code session ends
# Auto-commits modified files on the session branch
# Merges session/* back to main
# Cleans up the session branch
```

### UserPromptSubmit — squad routing

```python
# Fires on every user message
# Detects squad keywords (commercial, dev, infra...)
# Loads squad context if not already loaded
# Prevents context loss across long sessions
```

### UserPromptSubmit — knowledge lookup

```python
# Fires before sensitive operations (deploy, DNS, drop, migration)
# Runs _core/lookup.py against incidents + sessions + memory
# Surfaces relevant past incidents before action
```

### UserPromptSubmit — session recovery

```python
# Fires on session start
# Checks if previous session ended mid-work
# Recovers unfinished session context if found
```

---

## _core/ scripts

### lookup.py

Knowledge search across all memory sources:

```bash
python _core/lookup.py "deploy vercel"
python _core/lookup.py "ghl webhook" --source incidents
python _core/lookup.py "auth" --source sessions --since 2026-01-01
python _core/lookup.py "supabase" --json --top 5
```

Covers: `incidents/`, `sessions-log/`, `memory/`, squad `memory/` files.

### state-aggregator.py

Reads L1 from all squad STATE.md files and returns an aggregate:

```bash
python _core/state-aggregator.py squads/
# Output: timestamped L1 snapshot per squad
```

Used by `/status` skill.

### harness.sh

Worker runner. Executes Python scripts in `workers/` on a schedule:

```bash
# Add workers to harness.sh:
# run_worker "workers/daily-report.py" "09:00"
# run_worker "workers/health-check.py" "every:1h"
```

Designed to run as a cron job on a server. No AI in the loop — workers are deterministic.

### memory-schema.md

Documents the STATE.md format, naming conventions, and aggregation rules. The source of truth for how memory works.

---

## Skills

Skills are markdown files that define reusable behaviors. Invoked with `/skill-name` in Claude Code.

### Global skills (`skills/`)

Available to all squads:

| Skill | File | What it does |
|---|---|---|
| `/hive-setup` | `skills/hive-setup.md` | First-time company onboarding |
| `/open-squad` | `skills/open-squad.md` | Load squad context + STATE |
| `/close-squad` | `skills/close-squad.md` | Update STATE + propagate L1 |
| `/status` | `skills/status.md` | Aggregate L1 from all squads |

### Squad-specific skills (`squads/<name>/skills/`)

Only available when that squad is open. Add your own here.

---

## Workers

Workers are Python scripts that run on a schedule, independent of the AI.

Design rules:
1. **Deterministic** — same input, same output. No LLM calls.
2. **Write to STATE.md** — workers update squad state, never CLAUDE.md or skills.
3. **Idempotent** — safe to run multiple times.
4. **Fail loudly** — log errors, don't swallow exceptions silently.

Example workers:
- Daily revenue summary → Finance STATE.md L1
- Weekly competitor mentions scan → Intelligence STATE.md L2
- Health score recalculation → CS STATE.md L1

---

## Context files

Each squad has `context/squad-context.md` — company-specific data filled during `/hive-setup`. This is what makes HIVE feel personalized vs. generic.

The root `squads/orchestrator/context/user-profile.md` tells Stamper who you are — your role, working style, preferences, and anti-patterns.

---

## Security model

1. **Credentials never in files** — use a secrets manager (1Password, Vault, AWS Secrets Manager). `.env` only for non-sensitive config.
2. **Workers are read-only for everything except STATE.md** — no workers modify CLAUDE.md, skills, or foundation docs.
3. **Destructive operations require explicit confirmation** — hardcoded in absolute rules, enforced in hooks.
4. **Session branches** — main is never written to directly during a session.
