# /close-squad

Updates the squad's STATE.md with current work status and propagates L1 to the orchestrator.

## Usage

```
/close-squad commercial
/close-squad dev
```

## When to activate

- "close [squad]", "done with [squad]", "switching squads", "wrap up [area]"
- `/close-squad <name>` explicit invocation
- End of a focused work session on a squad

---

## Steps

### 1 — Summarize session work

Ask (or infer from context):
- What was completed this session? (→ L1 update)
- What's still in progress? (→ L2 update)
- Anything new for backlog? (→ L3 update)
- Any decisions made? (→ decisions.md)
- Any gotchas discovered? (→ gotchas.md)

### 2 — Update STATE.md

Rewrite the squad's `squads/<name>/memory/STATE.md`:

```markdown
# <Squad> STATE

[L1]
<1-3 lines: what's the current status after this session>
Last updated: YYYY-MM-DD

[L2]
- [ ] <still in progress>
- [x] <completed this session>

[L3]
- <new backlog items>
```

### 3 — Update decisions.md (if any decisions were made)

Append to `squads/<name>/memory/decisions.md`:
```markdown
## YYYY-MM-DD — <Decision title>
<What was decided and why>
```

### 4 — Update gotchas.md (if any lessons learned)

Append to `squads/<name>/memory/gotchas.md`:
```markdown
## YYYY-MM-DD — <What happened>
<What to do differently next time>
```

### 5 — Propagate L1 to orchestrator

Update `squads/orchestrator/memory/STATE.md` — find the line for this squad and update it with the new L1. If not present, add it.

### 6 — Confirm

```
Squad closed: <Name>

STATE.md updated:
  L1: <new L1>
  L2: <count> items in progress, <count> completed
  L3: <count> backlog items

Propagated to orchestrator STATE.md.
```

---

## Rules

1. **Always update L1** — even if nothing changed, note "no change since last session".
2. **L1 must be factual** — "3 leads in pipeline" not "things going well".
3. **Propagate to orchestrator** — always, without exception.
4. **If decisions were made, log them** — unlogged decisions disappear.
