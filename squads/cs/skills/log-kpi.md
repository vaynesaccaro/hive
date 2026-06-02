# /log-kpi

Log a CS metric to STATE.md and check whether it crosses an alert threshold.

## When to use

After collecting any CS metric — weekly, monthly, or on-demand. Also use when a metric update comes in from an external source (survey response, platform export, manual check).

## Inputs

- `metric_name`: name of the metric (see supported list below)
- `value`: the measured value
- `period`: time period (e.g., "May 2026", "W22 2026")
- `notes` (optional): context that explains the number

## Steps / Framework

### Step 1 — Collect inputs
If `metric_name`, `value`, or `period` were not provided, ask for them before proceeding.

### Step 2 — Write to STATE.md
- If the metric is operational (weekly cadence): append to **L2** (squad operational state)
- If the metric is strategic (monthly, crosses threshold, or represents a trend): append to **L1** (leadership-visible state)

Format for STATE.md entry:
```
[METRIC] metric_name: value | period: X | logged: YYYY-MM-DD | notes: ...
```

### Step 3 — Check alert thresholds
Compare the logged value against thresholds defined in `foundation/health-score.md`.

If a threshold is crossed:
- Flag the entry in L1 with `[ALERT]`
- Suggest one concrete action (e.g., "NPS below 7 → trigger proactive check-in sequence")

### Step 4 — Check for trend shifts
If this metric was logged previously:
- Compare to last 2 readings
- If direction changed (improving → declining or vice versa): append an entry to `memory/decisions.md` noting the trend shift

---

## Supported Metrics

| Metric | Typical cadence | Alert direction |
|---|---|---|
| NPS | Monthly | Below 7 = flag |
| Churn rate | Monthly | Above baseline = flag |
| Onboarding completion rate | Weekly | Below 80% = flag |
| Health score (per account) | Weekly | Below threshold in `health-score.md` |
| CSAT | Per interaction or monthly | Below 4/5 = flag |
| Response time (support) | Weekly | Above SLA = flag |
| Expansion MRR | Monthly | Decline = flag |

## Rules

- Do not fabricate values. Only log what was explicitly provided or retrieved from a source.
- If `foundation/health-score.md` does not exist, log the metric without threshold check and note: "No thresholds configured — create `foundation/health-score.md` to enable alerts."
- Every log entry must have a period. A metric without a period is not a metric, it's a number.
