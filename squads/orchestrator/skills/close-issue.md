# /close-issue

Close a Linear issue: merge branch, mark Done, post completion comment.

## Usage

- `/close-issue PDL-47` — close a specific issue

## Prerequisites

- Linear API token: `LINEAR_API_TOKEN` in environment
- On the feature branch for the issue

## Steps

1. **Run quality cycle** (unless user says "skip"):
   - `/codex-review` on current branch
   - Fix any P1/P2 findings
   - Build check: `npm run build` / `go build` / `python -m py_compile` (auto-detect stack)
2. **Commit + push** any remaining changes
3. **Merge branch** to integration branch (or main if no integration branch):
   ```bash
   git checkout main
   git merge feat/<branch> --no-ff -m "feat: [description] — Closes [ID]"
   git push origin main
   git branch -d feat/<branch>
   ```
4. **Mark Done** via Linear API mutation
5. **Post completion comment** on the issue:
   ```
   Completed — YYYY-MM-DD HH:MM
   Branch: [branch]
   Merged into: [target branch]
   Files changed: [list]
   ```
6. **Confirm** to user

## Quality Skip

User can say "skip quality cycle" or "close without review" to bypass step 1. Acknowledge the skip in the completion comment.

## Merge Strategy

```
feat/issue-XX  →  feature/[feature]  →  main
```

NEVER merge directly to main without validation. Each branch goes to the feature integration branch first, then to main when the full feature is validated end-to-end.
