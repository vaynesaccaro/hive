# /log-incident

Log an incident or technical learning to the framework's incident hub. Prevents recurrence by making knowledge searchable.

## When to use

- A bug caused production impact
- A debugging session took > 30 minutes
- Something silently failed (cron, webhook, integration)
- You discovered a non-obvious gotcha
- A deploy caused a regression

## Steps

1. **Collect information** (ask user if not available):
   - Title, date of incident (not log date), severity (Low/Medium/High/Critical)
   - Project/service affected, duration
   - What happened, root cause (file:line if applicable)
   - Why it wasn't caught earlier
   - How it was fixed (with commit hashes if available)
   - Prevention: specific, verifiable checklist items

2. **Generate slug**: `YYYY-MM-DD_short-title-in-kebab-case.md`

3. **Write to `incidents/` in the repo root**

4. **Write copy to `docs/incidents/` in the affected project** (create folder if needed)

5. **Update `incidents/INDEX.md`** — append row to current month's table

6. **Report**: confirm all files written and provide paths

## Incident File Format

```markdown
---
date: YYYY-MM-DD
severity: Low | Medium | High | Critical
project: [project name]
duration: [how long the incident lasted]
tags: [2-5 tags]
---

# [Title]

## What Happened
[Clear description of the incident]

## Root Cause
[Precise cause — file:line if applicable]

## Why It Wasn't Caught
[Testing gap, monitoring gap, assumption, etc.]

## How It Was Fixed
[Steps taken + commit hashes]

## Prevention
- [ ] [Specific verifiable action]
- [ ] [Specific verifiable action]

## Related
[Links to related incidents, PRs, or docs]
```

## Rules

- NEVER invent details — ask the user if something is unknown
- Severity is set by the user, not inferred
- Commit hashes: only real ones, never invented
- Prevention items must be verifiable (command, pattern, checklist) — never generic ("be more careful")
- Date of incident ≠ date of logging

## Incidents Index Format

`incidents/INDEX.md` maintains a table:

```markdown
## YYYY-MM

| Date | Severity | Project | Title |
|---|---|---|---|
| YYYY-MM-DD | High | [project] | [Title](./YYYY-MM-DD_slug.md) |
```
