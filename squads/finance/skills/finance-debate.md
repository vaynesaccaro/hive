# /finance-debate

Financial decision roundtable. Forces major money decisions through multiple perspectives before committing.

## When to use

- Before approving a structural expense (new hire, annual tool contract, office space)
- Before changing pricing or introducing discounts
- Before offering a large or precedent-setting discount to close a deal
- When runway drops below a safety threshold
- When a significant investment is being evaluated

## Format

Three rounds. Total time: ~25 minutes.

---

### Round 1 — Perspectives (10 min)
Each perspective presents its view on the financial decision.

**CFO voice**
Focus: cash flow, survival, burn rate, runway impact. Asks: "Can we afford this if revenue drops 30% next month?"

**CEO / Growth voice**
Focus: strategic opportunity, what this enables, opportunity cost of not doing it.

**CS voice**
Focus: customer impact, whether this decision affects delivery quality or client relationships.

**Operations voice**
Focus: execution cost, team capacity required, hidden implementation costs.

**Devil's Advocate**
Focus: the downside scenario everyone is glossing over. What's the worst plausible case?

---

### Round 2 — Cross-examination (10 min)
Each perspective challenges the others.

- CFO challenges CEO: "What's the evidence this investment returns within 6 months?"
- CEO challenges CFO: "What's the cost of not doing this? Is caution actually the riskier move?"
- CS challenges Finance: "Does this cut affect client delivery in ways we haven't priced in?"
- Operations challenges everyone: "Who executes this and what does it actually cost in hours?"
- Devil's Advocate challenges everyone: "What does this look like if the revenue assumption is wrong?"

---

### Round 3 — Synthesis (5 min)
One concrete recommendation:
- Approve / Approve with conditions / Reject
- Primary rationale from each voice
- If approved with conditions: list the conditions explicitly
- Next action: owner + deadline

---

## Output

```
FINANCE DEBATE — [topic] — [date]

Decision: [Approve / Approve with conditions / Reject]

Rationale:
- CFO: [one sentence]
- Growth: [one sentence]
- CS: [one sentence]
- Operations: [one sentence]
- Risk flagged by Devil's Advocate: [one sentence]

Conditions (if applicable): [list]
Next action: [what, who, by when]
```

## Rules

- The CFO voice has veto power on survival decisions (runway < 3 months). Not on growth decisions.
- "We'll make it work" is not a financial plan. Every approval needs a named budget source.
- Log the outcome in `memory/decisions.md`.
- If the decision involves pricing changes, also run the change through the commercial squad.
