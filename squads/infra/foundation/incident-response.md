# Incident Response

---

## Severity Levels

| Level | Definition | Response Time | Example |
|-------|-----------|--------------|---------|
| **P0 — Critical** | Full outage or data loss. All users affected. | Immediate (< 15 min) | Site down, DB unreachable, data corruption |
| **P1 — Major** | Core feature broken for significant % of users | < 1 hour | Login failing, payments broken |
| **P2 — Minor** | Non-critical feature degraded; workaround exists | < 4 hours | Report export slow, minor UI bug affecting subset |
| **P3 — Low** | Cosmetic or edge-case issue; no business impact | Next business day | Wrong label, minor display glitch |

---

## Escalation Path

| Step | Who | Action |
|------|-----|--------|
| 1 | On-call engineer | Acknowledge, initial triage |
| 2 | Engineering Lead | Notified if P0/P1 within 15 min |
| 3 | CTO / Founder | Notified if P0 or P1 unresolved > 30 min |
| 4 | CS / Support Lead | Notify affected customers if P0/P1 > 30 min |

---

## Response Steps

1. **Acknowledge** — Post in #incidents: "I'm on this" + severity
2. **Diagnose** — Check logs, metrics, recent deploys
3. **Mitigate** — Fastest path to restore service (rollback, restart, flag off)
4. **Communicate** — Update #incidents every 15–30 min; notify CS if customers affected
5. **Resolve** — Confirm service restored; mark incident closed
6. **Postmortem** — Required for P0/P1 within 48h of resolution

---

## Postmortem Template

```
## Incident: [title]
Date: ___
Duration: ___
Severity: P_
Affected: [service / users]

### Timeline
- HH:MM — [what happened]
- HH:MM — [detection]
- HH:MM — [mitigation started]
- HH:MM — [resolved]

### Root Cause
[1–3 sentences]

### Contributing Factors
- [factor 1]
- [factor 2]

### What Went Well
- [item]

### Action Items
| Item | Owner | Due |
|------|-------|-----|
| [fix] | @name | [date] |
```

---

## On-Call Rotation
- Schedule: _e.g. weekly rotation_
- Tool: _e.g. PagerDuty / manual Slack rotation_
- Current on-call: ___
