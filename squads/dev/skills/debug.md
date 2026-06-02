# /debug

Structured debugging framework based on Pólya's "How to Solve It" — 4 mandatory phases. Forces methodical thinking before touching code.

**Absolute rule: Never jump straight to fixing. Complete understanding first.**

## Activation

Invoke when: a bug is reported, something isn't working, investigating unexpected behavior, "why is this breaking", "what's causing this".

## Phase 0 — Triage (automatic)

Before anything else, assess severity and recommend a mode:

```
TRIAGE

[1-2 line problem summary]

Recommended severity: [TRIVIAL / MEDIUM / CRITICAL]
Reason: [why this classification]

→ TRIVIAL: run all 4 phases in one block, resolve immediately
→ MEDIUM: show understanding + hypotheses, you validate, then resolve
→ CRITICAL: stop at each phase for your validation before proceeding

Proceed with [recommendation] or prefer different mode?
```

| Severity | When | Examples |
|---|---|---|
| TRIVIAL | Obvious cause, low impact, reversible | typo, missing import, undefined variable |
| MEDIUM | Multiple possible causes, moderate impact | logic bug, integration breaking, unexpected behavior |
| CRITICAL | Production affected, data at risk, unknown cause | prod down, silent cron failure, regression after deploy |

## Phase 1 — Understanding

Answer ALL of these before touching code:

- **Unknown**: What is the expected behavior? What is the observed behavior? What is the delta?
- **Data**: Exact error message (verbatim, not paraphrased). Environment (local/staging/prod). Is it reproducible? When did it start?
- **Constraints**: Which systems are involved? Any external dependencies that may have changed?

Output format:
```
PHASE 1 — UNDERSTANDING
Expected: [X]
Observed: [Y]
Error: [exact message]
Environment: [where]
Since: [when / unknown]
Reproduces: [always / intermittent / condition]
Systems involved: [list]
Missing data: [what to ask user, if anything]
```

## Phase 2 — Investigation Plan

NOT the fix plan. The **diagnosis** plan.

1. Check `incidents/` for related past incidents
2. List all hypotheses in order of probability
3. For each hypothesis: define the test that confirms or discards it
4. Order by cost: fast/cheap tests first
5. Identify what NOT to change during investigation

Output format:
```
PHASE 2 — INVESTIGATION PLAN

Related incidents: [none / link]

Hypotheses (by probability):
H1: [description] → Test: [what to verify]
H2: [description] → Test: [what to verify]

Execution order: H1 → H2
Constraint: no code changes until root cause confirmed
```

## Phase 3 — Diagnosis Execution

Run the Phase 2 plan, one test at a time.

Rules:
- One test at a time — no parallel experiments
- Record concrete evidence from each test (log output, value, response)
- No fixing during diagnosis
- If H1 fails, move to H2 — don't insist

Anti-patterns (forbidden):
- Changing code "to see if it fixes it" without understanding the cause
- Applying Stack Overflow fixes without validating the context matches
- Changing multiple things simultaneously
- Ignoring the error message and going straight to code
- Theorizing without reading logs first

Output format:
```
PHASE 3 — DIAGNOSIS

Test H1: [what I did] → Result: [confirmed/discarded]
  Evidence: [concrete output/log/value]

ROOT CAUSE IDENTIFIED:
[precise description — file:line, exact flow, why it breaks]

Causal chain: [A] → [B] → [C] → [observed error]
```

## Phase 4 — Fix + Retrospective

Only now fix. Then review.

**Fix rules:**
1. Propose the minimum change that resolves the root cause
2. Do NOT refactor adjacent code opportunistically
3. Verify the fix doesn't introduce regressions
4. Confirm expected behavior (Phase 1) is restored

**Mandatory retrospective:**
- Was the fix verified?
- Was there a faster diagnostic path?
- Is this fix reusable elsewhere?
- What would prevent this bug from happening again?
- Should this be logged as an incident? (if >30min or production impact → `/log-incident`)

Output format:
```
PHASE 4 — FIX + RETROSPECTIVE

Fix applied:
  File: [path:line]
  Change: [concise description]

Verification:
  [ ] Expected behavior restored
  [ ] No regressions identified
  [ ] Tested in [environment]

Retrospective:
  Time spent: [estimate]
  Faster diagnostic path: [insight]
  Reusable in: [where / not applicable]
  Prevention: [what to do to avoid recurrence]
  Log as incident: [yes/no — reason]
```

## Behavior by Mode

**TRIVIAL**: Phases 1→2→3→4 in a single block. Condensed output. Resolve and present result.

**MEDIUM**: Phase 1+2 → STOP → present to user → user validates → Phase 3+4.

**CRITICAL**: Phase 1 → STOP → user validates understanding → Phase 2 → STOP → user validates plan → Phase 3 → STOP → user validates root cause → Phase 4.
