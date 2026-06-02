# Memory Schema

## STATE.md format

Every squad's `memory/STATE.md` follows the bracketed L1/L2/L3 format:

```markdown
# <Squad Name> STATE

[L1]
<Current status — 1-3 lines. What's happening right now.>
<Stamper reads this when running /status aggregation.>

[L2]
- [ ] <Active task 1>
- [ ] <Active task 2>
- [x] <Completed task>

[L3]
- <Backlog item 1>
- <Backlog item 2>
```

## L1/L2/L3 definitions

| Layer | Contains | Who reads it |
|---|---|---|
| **L1** | Current status, key metrics, blockers | Stamper (aggregation), human (quick scan) |
| **L2** | Active tasks, in-progress work, pending reviews | Squad agent (session start), human |
| **L3** | Backlog, queued items, not started | Squad agent (planning), human |

## L1 guidelines

L1 is designed for machine-readable aggregation. Keep it:
- **Factual** — "3 active deals, 1 proposal sent" not "things are going well"
- **Short** — 1-3 lines max
- **Current** — update every session, not every week
- **Signaling** — include blockers if any: "BLOCKED: waiting on legal review"

## Update cadence

| Layer | When to update |
|---|---|
| L1 | Every session close (`/close-squad`) |
| L2 | When tasks start, complete, or change |
| L3 | When new items are identified or priorities shift |

## Aggregation (how /status works)

`_core/state-aggregator.py` reads L1 from all squad STATE.md files and formats them into a company-wide snapshot. Output includes:
- Squad name
- L1 content
- Timestamp of last update

## Memory files

Beyond STATE.md, each squad's `memory/` folder can contain:

| File | Format | Purpose |
|---|---|---|
| `decisions.md` | `## YYYY-MM-DD — Title\nContent` | Architectural/operational decisions log |
| `gotchas.md` | `## YYYY-MM-DD — Title\nContent` | Known pitfalls and lessons learned |
| `MEMORY.md` | Index of other memory files | Navigation index |
| `project_*.md` | Free-form | Active project context |
| `reference_*.md` | Free-form | Reference data (configs, mappings) |
| `feedback_*.md` | Free-form | Behavior feedback for the agent |

## Global vs. squad memory

- **Global** (`memory/` at root) — Stamper's context, company-wide decisions
- **Squad** (`squads/<name>/memory/`) — isolated per squad

Claude Code loads squad memory only when that squad's folder is open.

## Retention policy

Memory files are append-only by default. Don't delete historical entries — add superseding entries instead.

Exception: `STATE.md` is always current state. Overwrite, don't append.
