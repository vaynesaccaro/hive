# /dev-debate

Architecture roundtable for technical decisions. Forces every major technical choice through multiple critical lenses before the team commits.

## When to use

- Before making a significant architectural decision (new service, major refactor, data model change)
- When two valid implementation approaches exist and the team is split
- Before migrating to a new stack, framework, or infrastructure layer
- Before introducing a new external dependency
- When a technical spike reveals tradeoffs that need structured evaluation

## Format

Three rounds. Total time: ~25 minutes.

---

### Round 1 — Perspectives (10 min)
Each perspective presents its view on the technical decision without interruption.

**Tech Lead**
Focus: system coherence, long-term architecture fitness, technical debt introduced or reduced.

**Senior Dev**
Focus: implementation feasibility, estimated effort, hidden complexity, what "done" actually looks like.

**QA**
Focus: testability of the proposed approach, edge cases that will be hard to test, what breaks first.

**Product**
Focus: user impact, whether the technical choice enables or constrains the product roadmap.

**DevOps / Infra**
Focus: operational complexity, deployment model, monitoring, rollback, infrastructure cost.

**Security**
Focus: attack surface introduced, data exposure risk, auth/authz implications, compliance.

---

### Round 2 — Cross-examination (10 min)
Each perspective challenges the others directly. No politeness.

- Tech Lead challenges Senior Dev: "Is your effort estimate realistic or optimistic?"
- Senior Dev challenges Tech Lead: "Is this architecture clean in theory but hell to implement?"
- QA challenges everyone: "How do we test the failure path?"
- DevOps challenges Tech Lead: "What does this look like at 3am when it breaks?"
- Security challenges everyone: "What data can be exfiltrated if this is compromised?"
- Product challenges Tech Lead: "Does this decision lock us out of any roadmap item in the next 6 months?"

---

### Round 3 — Synthesis (5 min)
Tech Lead synthesizes the recommendation:
- Decision: proceed / revise / reject
- Key tradeoffs accepted
- Outstanding risks (with owners)
- The next action: who does what, by when

---

## Output

```
DEV DEBATE — [topic] — [date]

Decision: [proceed / revise / reject]

Rationale:
- Tech Lead: [one sentence]
- Implementation: [one sentence]
- QA: [one sentence]
- Product: [one sentence]
- DevOps: [one sentence]
- Security: [one sentence]

Tradeoffs accepted: [list]
Outstanding risks: [list with owners]
Next action: [what, who, by when]
```

## Rules

- The Tech Lead's role in Round 3 is synthesis, not override. If Security raises an unresolved critical risk, it cannot be steamrolled by the synthesis.
- "We'll figure it out later" is not an acceptable answer in Round 2.
- Log the outcome in `memory/decisions.md` with the ADR reference if one is created.
