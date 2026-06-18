# /gemini-review

Run a code review using the Google Gemini CLI. Free tier available via personal Google account OAuth.

## Usage

- `/gemini-review` — reviews last 3 commits
- `/gemini-review 5` — reviews last N commits
- `/gemini-review abc1234` — specific commit
- `/gemini-review abc1234..def5678` — commit range

## Prerequisites

- Gemini CLI installed: `npm install -g @google/gemini-cli`
- Authenticated: run `gemini` once to log in via Google OAuth

## Steps

1. **Collect diff** — `git diff HEAD~N..HEAD` + `git log --oneline`
2. **Detect stack** — same as `/claude-review`
3. **Send to Gemini CLI:**
   ```bash
   git diff HEAD~N..HEAD | gemini -m gemini-2.5-flash -p "<review prompt>"
   ```
4. **Apply chunking if needed** — free tier: 250K tokens/min
   - Diff < 30KB: single call
   - Diff 30–100KB: split by file, ~30KB per call
   - Diff > 100KB: one file at a time, 15s between batches (max 5 calls/min)
5. **Classify findings** into P1/P2/P3 × LOGIC/SYNTAX/STYLE/SECURITY/PERFORMANCE/DEAD_CODE
6. **Save report** to `docs/gemini-reviews/gemini-review-YYYY-MM-DD.md`

## Default Model

`gemini-2.5-flash` — 1M context window, available on free tier via OAuth.

## Priority Levels

Same as `/codex-review`: P1 Critical / P2 Important / P3 Suggestion.

## Fallback

If CLI unavailable: offer to do the review inline using current Claude instance.

## Cost

$0 with personal Google account (free tier). No API key required.
