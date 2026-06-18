# /status

Aggregates L1 from all active squads and prints a company-wide snapshot.

## Usage

```
/status
/status --brief
```

## When to activate

- "what's the status", "company overview", "where are we", "weekly status"
- `/status` explicit invocation

---

## Steps

### 1 — Run state aggregator

```bash
python _core/state-aggregator.py
```

Reads L1 from every `squads/*/memory/STATE.md`.

### 2 — If _core/state-aggregator.py unavailable

Read manually (in order):
1. `squads/orchestrator/memory/STATE.md`
2. `squads/commercial/memory/STATE.md`
3. `squads/cs/memory/STATE.md`
4. `squads/marketing/memory/STATE.md`
5. `squads/product/memory/STATE.md`
6. `squads/finance/memory/STATE.md`
7. `squads/dev/memory/STATE.md`
8. `squads/infra/memory/STATE.md`
9. `squads/operations/memory/STATE.md`
10. `squads/quality/memory/STATE.md`
11. `squads/intelligence/memory/STATE.md`

### 3 — Format output

```
HIVE Status — YYYY-MM-DD HH:MM
════════════════════════════════════════

  COMMERCIAL (Victor)
    <L1 content>

  CS (Leah)
    <L1 content>

  MARKETING (Maya)
    <L1 content>

  PRODUCT (Owen)
    <L1 content>

  FINANCE (Clara)
    <L1 content>

  DEV (Ethan)
    <L1 content>

  INFRA (Dean)
    <L1 content>

  OPERATIONS (Harper)
    <L1 content>

  QUALITY (Nora)
    <L1 content>

  INTELLIGENCE (Rex)
    <L1 content>

════════════════════════════════════════
Blockers: <list any squad with "BLOCKED" in L1, or "none">
```

### 4 — Flag blockers

Any squad whose L1 contains "BLOCKED", "blocked", or "urgent" should be called out explicitly in a "Blockers" section at the bottom.

---

## Rules

1. **Show all active squads** — don't skip squads that say "not configured".
2. **Inactive squads** — skip squads whose L1 is "Squad inactive".
3. **Surface blockers** — never bury a BLOCKED status in the list.
4. **--brief flag** — show only squad name + first line of L1, no L2/L3.
