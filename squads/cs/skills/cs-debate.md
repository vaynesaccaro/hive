# /cs-debate

Structured multi-perspective roundtable for Customer Success decisions. Prevents retention and expansion decisions from being made from a single vantage point.

## When to use

- When a client is showing churn risk and the response isn't clear
- Before proposing an expansion or upsell to an existing customer
- When redesigning the onboarding process
- When debating whether to change health score thresholds
- When a client escalation has no obvious resolution

## Format

Three rounds. Total time: ~25 minutes.

---

### Round 1 — Perspectives (10 min)
Each perspective presents its view on the CS challenge.

**CS Lead**
Focus: retention, relationship health, client satisfaction. Asks: "What does this client actually need right now?"

**Sales voice**
Focus: expansion revenue, upsell timing, account growth. Asks: "Is there an expansion opportunity here or are we misreading the signal?"

**Product voice**
Focus: roadmap alignment, feature gaps, whether the client's pain is solvable with current or upcoming capabilities.

**Finance voice**
Focus: LTV, churn math, cost of intervention vs cost of loss. Asks: "What does keeping vs losing this account mean in numbers?"

**Operations voice**
Focus: delivery capacity. Asks: "Can we actually deliver the solution being proposed, given current team load?"

---

### Round 2 — Cross-examination (10 min)
Each perspective challenges the others directly.

- CS challenges Sales: "Is this expansion genuinely in the client's interest right now, or too soon?"
- Sales challenges CS: "Are we being too cautious and missing a real window?"
- Product challenges CS: "Is this pain actually solvable, or are we over-promising?"
- Finance challenges everyone: "What's the cost of being wrong in either direction?"
- Operations challenges all: "Who's delivering this and when?"

---

### Round 3 — Synthesis (5 min)
One concrete recommendation:
- What action to take (or not take)
- Primary rationale from each voice (one sentence each)
- The next action: owner + deadline

---

## Output

```
CS DEBATE — [topic] — [date]

Recommendation: [one clear action]

Rationale:
- CS Lead: [one sentence]
- Sales: [one sentence]
- Product: [one sentence]
- Finance: [one sentence]
- Operations: [one sentence]

Next action: [what, who, by when]
```

## Rules

- Client's best interest is the tiebreaker — not revenue, not convenience.
- If no clear recommendation emerges after Round 3, escalate to leadership with the tension documented.
- Log the outcome in `memory/decisions.md`.
