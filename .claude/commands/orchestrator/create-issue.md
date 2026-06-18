# /create-issue

Create a new Linear issue with a complete, actionable description.

## Usage

- `/create-issue` — guided creation
- `/create-issue "Fix login redirect bug"` — start with a title

## Inputs

- `title` — clear, specific (not "Fix bug", but "Fix redirect loop on OAuth callback")
- `description` — what needs to be done and why
- `acceptance_criteria` — verifiable conditions for Done
- `priority` — Urgent / High / Medium / Low
- `assignee` — who does this (optional)
- `labels` — repo:name, area:commercial, etc.

## Steps

1. **Collect all inputs** (ask for missing ones)
2. **Check for duplicates** — search Linear for similar open issues
3. **Create issue via Linear API** with full description
4. **Add labels** (repo:X if target repo is known)
5. **Confirm** with issue ID and link

## Description Template

```markdown
## Context
[Why this issue exists — what problem it solves]

## What needs to be done
[Clear description of the work]

## Acceptance Criteria
- [ ] [Verifiable condition 1]
- [ ] [Verifiable condition 2]

## Notes
[Any technical context, links, references]
```

## Rules

- Title must be specific and actionable
- Acceptance criteria must be verifiable — no "works correctly"
- If scope is unclear, add a `/plan-issue` step before starting
- repo:pending label = issue created but not planned yet
