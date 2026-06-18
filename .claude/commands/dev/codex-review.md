# /codex-review

Run an automated code review using the OpenAI Codex CLI. Classifies findings by priority (P1/P2/P3) and category.

## Usage

- `/codex-review` — reviews last 3 commits on current branch
- `/codex-review 5` — reviews last N commits
- `/codex-review abc1234` — reviews a specific commit
- `/codex-review abc1234..def5678` — reviews a commit range

## Prerequisites

- Codex CLI installed: `npm install -g @openai/codex`
- `OPENAI_API_KEY` set as environment variable

## Steps

1. **Detect API key** — check env var, then `.env.local`, then `.env`
2. **Map arguments to CLI commands:**
   - no args → `codex review --base HEAD~3`
   - N → `codex review --base HEAD~N`
   - SHA → `codex review --commit <SHA>`
   - range → `codex review --base <SHA1>` (HEAD implicit)
3. **Run Codex CLI** with appropriate flags
4. **Classify findings** into P1/P2/P3 × LOGIC/SYNTAX/STYLE/SECURITY/PERFORMANCE/DEAD_CODE
5. **Save report** to `docs/codex-reviews/codex-review-YYYY-MM-DD.md`
6. **Ask if user wants P1s auto-fixed**

## Priority Levels

**P1 — Critical (fix before deploy):** bugs breaking production, security vulnerabilities, data loss race conditions, logic errors producing wrong results, regressions.

**P2 — Important (fix this session):** dead code, missing error handling on critical paths, incorrect typing, maintenance-confusing inconsistencies.

**P3 — Suggestion (backlog):** readability improvements, optional refactors, non-critical performance, naming conventions.

## Categories

LOGIC | SYNTAX | STYLE | SECURITY | PERFORMANCE | DEAD_CODE

## Report Format

Save to `docs/codex-reviews/codex-review-YYYY-MM-DD.md`:

```markdown
# Codex Review — YYYY-MM-DD

## Summary
- Branch: [branch]
- Commits reviewed: N (hash1..hashN)
- Findings: X P1 | Y P2 | Z P3

## P1 — Critical
### [CATEGORY] Short title
- File: path/to/file.ts:42
- Problem: clear description
- Impact: what happens if not fixed
- Suggested fix: code or instruction

## P2 — Important
...

## P3 — Suggestions
...
```

## Fallback

If Codex CLI is unavailable, offer to run the review inline using the current Claude instance with the same P1/P2/P3 classification structure.

## CLI Rules

- NEVER use `--quiet` (flag doesn't exist)
- NEVER combine `--commit` with `--base`
- NEVER pass `--commit` more than once
- NEVER pass a prompt alongside `--base`
- Timeout: 5 minutes max
