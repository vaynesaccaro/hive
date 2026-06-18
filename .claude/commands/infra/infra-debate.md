# /infra-debate

Infrastructure decision roundtable. Prevents unilateral technical choices from creating operational or security debt.

## When to use

- Before choosing a new infrastructure component (database, queue, cache, CDN)
- Before scaling decisions (vertical vs horizontal, managed vs self-hosted)
- Before migrating hosting providers or regions
- Before changing CI/CD pipeline or deployment model
- When evaluating build vs buy for an infrastructure layer

## Format

Three rounds. Total time: ~25 minutes.

---

### Round 1 — Perspectives (10 min)
Each perspective presents its view on the infrastructure decision.

**Infra Lead**
Focus: reliability, uptime, operational simplicity, long-term cost. Asks: "Will this still make sense at 10x current load?"

**Dev voice**
Focus: developer experience, local development compatibility, debugging tooling, deployment friction.

**Security voice**
Focus: attack surface introduced, network exposure, encryption at rest/in transit, compliance implications.

**Finance voice**
Focus: monthly cost, cost trajectory at scale, lock-in risk, egress fees hidden in the pricing model.

**Operations voice**
Focus: operational complexity, team knowledge required, runbook availability, incident response burden.

---

### Round 2 — Cross-examination (10 min)
Each perspective challenges the others directly.

- Infra challenges Dev: "Are you optimizing for dev experience at the cost of operational sanity?"
- Dev challenges Infra: "Is this operationally reliable but a nightmare to develop against?"
- Security challenges Infra: "What's the blast radius if this component is compromised?"
- Finance challenges Infra: "What does this cost at 100k users? Did you price the egress?"
- Operations challenges everyone: "Who's on-call for this at 3am and do they understand it?"

---

### Round 3 — Synthesis (5 min)
One concrete recommendation:
- Proceed / Proceed with conditions / Revisit / Reject
- Key tradeoffs accepted
- Outstanding risks (with owners)
- Next action: owner + deadline

---

## Output

```
INFRA DEBATE — [topic] — [date]

Decision: [Proceed / Proceed with conditions / Revisit / Reject]

Rationale:
- Infra Lead: [one sentence]
- Dev: [one sentence]
- Security: [one sentence]
- Finance: [one sentence]
- Operations: [one sentence]

Tradeoffs accepted: [list]
Outstanding risks: [list with owners]
Next action: [what, who, by when]
```

## Rules

- Security risks flagged in Round 2 cannot be dismissed — they require a mitigation plan or the decision must be revisited.
- "We'll optimize costs later" is acceptable only if cost trajectory is documented and has an owner.
- Log the outcome in `memory/decisions.md` and create an ADR if the decision is significant.
