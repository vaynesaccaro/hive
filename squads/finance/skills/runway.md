# /runway

Cash runway projection with 3 scenarios. The pessimistic scenario drives decisions.

## When to use

Monthly, or any time a significant change in revenue or expenses occurs. Also use before approving a structural expense or evaluating a hiring decision.

## Inputs

- `current_balance`: current cash on hand
- `last_3m_revenue`: revenue by stream for the last 3 months (cash received, not invoiced)
- `last_3m_expenses`: expenses by category for the last 3 months (committed, not just paid)
- `committed_future_expenses`: known upcoming expenses not yet reflected in the 3-month average
- `sales_pipeline`: deals expected to close in the next 90 days (with probability)

## Steps / Framework

### Step 1 — Calculate baseline burn
```
avg_monthly_revenue = sum(last_3m_revenue) / 3
avg_monthly_expenses = sum(last_3m_expenses) / 3
monthly_burn = avg_monthly_expenses - avg_monthly_revenue
```

If `monthly_burn` is negative, the business is cash-flow positive. Still run all 3 scenarios.

### Step 2 — Project 12 months for 3 scenarios

**Base scenario**: current trend continues, no change in revenue or expenses.

**Optimistic scenario**: revenue +30%, expenses flat. Use this to understand the upside ceiling — not for planning.

**Pessimistic scenario**: revenue -30%, expenses flat. This is the scenario that drives decisions.

For each scenario: find the month where `cumulative_balance` drops below 0.

### Step 3 — Factor in pipeline and committed expenses
- Add pipeline revenue weighted by close probability to the base and optimistic scenarios
- Add committed future expenses to all 3 scenarios

### Step 4 — Output

```
RUNWAY PROJECTION — [DATE]

Current balance: [X]
Monthly burn (avg 3m): [X]

BASE SCENARIO
  Revenue: [X]/mo | Expenses: [X]/mo | Burn: [X]
  Runway: N months (until MM/YYYY)

OPTIMISTIC (+30% revenue)
  Runway: N months (until MM/YYYY)

PESSIMISTIC (-30% revenue)  ← THIS IS THE METRIC THAT MATTERS
  Runway: N months (until MM/YYYY)

TRAFFIC LIGHT (pessimistic scenario):
  ✅ > 12 months → operate confidently
  ⚠️  6–12 months → caution, no new structural expenses
  🚨 3–6 months → defensive mode, cut costs + focus on revenue
  🔥 < 3 months → emergency, act immediately

TOP EXPENSE CATEGORIES:
  1. [category]: [X]/mo ([X]% of total)
  2. [category]: [X]/mo ([X]% of total)
  3. [category]: [X]/mo ([X]% of total)
```

## Rules

- **Revenue = cash received**, not contracted or invoiced. Accrual basis is lying to yourself.
- **Expenses = committed**, not just paid. Unpaid invoices and upcoming payroll count.
- **Always 3 scenarios.** A single scenario projection is fiction.
- **The pessimistic scenario is the one that drives decisions.** The optimistic scenario is for morale, not planning.
- Never present runway without a traffic light classification.
- If runway is in the warning zone (⚠️ or worse), flag in L1 STATE.md and log in `memory/decisions.md`.
