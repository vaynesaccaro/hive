# Health Score

## Review Cadence
- **Green accounts:** Monthly review
- **Yellow accounts:** Bi-weekly review
- **Red accounts:** Weekly + escalation

---

## Metrics & Weights

| Metric | Weight | How Measured |
|--------|--------|-------------|
| Product usage (DAU/WAU) | **30%** | _e.g. login frequency, feature adoption_ |
| Onboarding completion | **20%** | _% of onboarding checklist done_ |
| Support ticket volume / severity | **15%** | _open P1/P2 tickets_ |
| NPS / CSAT score | **15%** | _last survey result_ |
| Contract renewal date | **10%** | _days until renewal_ |
| Stakeholder engagement | **10%** | _last CS touchpoint < 30d_ |

---

## Thresholds

| Score | Status | Color | Action |
|-------|--------|-------|--------|
| 80–100 | Healthy | 🟢 Green | Routine check-in; look for expansion |
| 60–79 | At Risk | 🟡 Yellow | Proactive outreach; identify blockers |
| 0–59 | Critical | 🔴 Red | Escalate; churn protocol (see churn-protocol.md) |

---

## Scoring Formula
```
Score = (Usage × 0.30) + (Onboarding × 0.20) + (Support × 0.15)
      + (NPS × 0.15) + (Renewal × 0.10) + (Engagement × 0.10)
```
Each sub-metric normalized to 0–100 before weighting.

---

## Notes
- Scores updated: _weekly / bi-weekly_
- Tool tracking scores: _e.g. CRM, Gainsight, manual spreadsheet_
- Score overrides allowed by CS Manager with written justification
