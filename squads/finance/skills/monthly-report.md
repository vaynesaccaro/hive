# /monthly-report

Generate a structured monthly financial report. Combines P&L analysis, variance flagging, and executive summary in one pass.

## When to use

At the end of each month, after all transactions for the period are confirmed. Also use when leadership needs a financial snapshot outside of the regular cadence.

## Inputs

- `month`: period being reported (e.g., "May 2026")
- `revenue_data`: revenue by stream for the month
- `expense_data`: expenses by category for the month
- `previous_month_data`: same structure for the prior month
- `same_month_last_year` (optional): same period prior year for YoY comparison

## Steps / Framework

### Step 1 — Calculate P&L for the month
```
gross_revenue = sum of all revenue streams
total_expenses = sum of all expense categories
net_result = gross_revenue - total_expenses
net_margin = net_result / gross_revenue × 100
```

### Step 2 — Month-over-month comparison
For each revenue stream and expense category:
- Calculate delta: `current - previous`
- Calculate delta %: `(current - previous) / previous × 100`

### Step 3 — Year-over-year comparison (if data available)
Same calculation against the same month in the prior year.

### Step 4 — Identify top drivers
- **Top 3 revenue drivers**: highest revenue streams this month
- **Top 3 expense drivers**: highest expense categories this month

### Step 5 — Flag variances
Flag any revenue stream or expense category with a **>20% change vs previous month**. For each flag, note whether it is expected (seasonal, one-time) or unexplained.

### Step 6 — Executive summary
5 bullet points maximum. Cover: overall result, biggest positive, biggest risk, one trend to watch, one recommended action.

### Step 7 — Update STATE.md and memory
- Append key numbers to L1 in squad STATE.md
- If any threshold was crossed (runway alert, margin drop, etc.), also log in `memory/decisions.md`

---

## Output format

```
MONTHLY FINANCIAL REPORT — [MONTH]
Generated: [date]

P&L SUMMARY
  Revenue:  [X]
  Expenses: [X]
  Net:      [X] ([X]% margin)

MoM: [+/-X] ([+/-X]%)
YoY: [+/-X] ([+/-X]%) [if available]

TOP REVENUE DRIVERS
  1. [stream]: [X] ([+/-X]% vs prev month)
  2. [stream]: [X] ([+/-X]% vs prev month)
  3. [stream]: [X] ([+/-X]% vs prev month)

TOP EXPENSE DRIVERS
  1. [category]: [X] ([+/-X]% vs prev month)
  2. [category]: [X] ([+/-X]% vs prev month)
  3. [category]: [X] ([+/-X]% vs prev month)

VARIANCE FLAGS (>20% change)
  ⚠️  [category]: [X]% change — [explanation or "unexplained"]

EXECUTIVE SUMMARY
  • [overall result]
  • [biggest positive]
  • [biggest risk]
  • [trend to watch]
  • [recommended action]
```

## Rules

- Revenue = cash received. No accrual.
- If a variance is flagged as "unexplained," it must be investigated before the report is finalized.
- The executive summary must have a recommended action — a report without an action is just data.
- Never omit MoM comparison. Context is the point of a report.
