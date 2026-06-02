# Getting Started with HIVE

## Prerequisites

- [Claude Code](https://claude.ai/code) installed (CLI or desktop app)
- Git
- Python 3.8+

---

## Step 1 — Clone

```bash
git clone https://github.com/felipeluissalgueiro/hive.git my-company
cd my-company
```

Replace `my-company` with your actual company or project name. This is your private instance — fork it if you want to track changes to the upstream framework.

---

## Step 2 — Open in Claude Code

```bash
claude
```

Or open the `my-company/` folder in the Claude Code desktop app.

Claude Code will automatically read `CLAUDE.md` and load the Stamper persona.

---

## Step 3 — Run setup

```bash
/hive-setup
```

This guided session (~5-10 minutes) will:
- Ask for your company name, industry, and stage
- Ask about your working style and preferences
- Let you pick which squads to activate
- Ask 2-3 questions per active squad
- Write everything to the right files

After setup, every squad has context about your company. Sessions start with relevant state instead of a blank slate.

---

## Step 4 — Open your first squad

```bash
/open-squad commercial
```

Or navigate to the squad folder:

```bash
cd squads/commercial
claude
```

Victor (Head of Sales) loads with your company context. Start working.

---

## Step 5 — Check status anytime

```bash
/status
```

Aggregates L1 from all active squads. Shows what's happening now across the company.

---

## Core workflows

### Working with a squad

```
/open-squad <name>      ← load squad + STATE
[do work]
/close-squad <name>     ← update STATE + propagate L1 to orchestrator
```

### Logging a decision

Tell the squad agent to log a decision — it will write to `squads/<name>/memory/decisions.md`.

Or write directly:
```markdown
## 2026-06-01 — Chose Stripe over Paddle
Reason: better API docs and existing team knowledge.
```

### Logging a gotcha

When something goes wrong or you learn something non-obvious:
```markdown
## 2026-06-01 — GHL webhook delays
GHL webhooks can be delayed up to 30s under load. Don't assume real-time.
Always add a polling fallback for time-sensitive flows.
```

### Running the knowledge lookup

Before any sensitive operation (deploy, DNS change, integration):
```bash
python _core/lookup.py "<keywords>"
```

---

## Populating foundation docs

Each squad has a `foundation/` folder for reference documents. These are what the squad reads before any work session.

Populate them progressively — you don't need everything upfront:

| Squad | First doc to write |
|---|---|
| Commercial | `foundation/icp-profile.md` |
| CS | `foundation/onboarding-playbook.md` |
| Marketing | `foundation/brand-voice.md` |
| Product | `foundation/roadmap.md` |
| Finance | `foundation/chart-of-accounts.md` |
| Dev | `foundation/tech-stack.md` |
| Infra | `foundation/server-inventory.md` |
| Operations | `foundation/okr-framework.md` |
| Quality | `foundation/sop-template.md` |
| Intelligence | `foundation/competitive-framework.md` |

---

## Committing your work

HIVE's hooks handle session branches automatically. When you end a session, changes are committed and merged to `main`.

If you want to commit manually:
```bash
git add squads/ memory/ skills/
git commit -m "chore(session): update state after [what you worked on]"
```

Never force-push to `main` — the session hooks depend on clean branch history.

---

## Syncing across machines

Standard git workflow:
```bash
git pull --rebase origin main   ← before starting
git push origin main            ← after session ends (hooks do this automatically)
```

---

## What to do when the agent doesn't know something

1. Check `context/squad-context.md` — is the relevant field blank?
2. Add the information directly to the context file
3. Re-run `/hive-setup` for that squad if needed

The agent is only as good as the context you give it. Blank fields = generic answers.
