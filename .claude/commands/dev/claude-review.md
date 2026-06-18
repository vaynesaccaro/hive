# /claude-review

Run a code review using a separate Claude Code CLI instance (Opus model) for an independent second opinion.

## Usage

- `/claude-review` — reviews last 3 commits
- `/claude-review 5` — reviews last N commits
- `/claude-review abc1234` — specific commit
- `/claude-review abc1234..def5678` — commit range

## Prerequisites

- Claude Code CLI installed: `npm install -g @anthropic-ai/claude-code`
- Active login session (`claude` to authenticate)

## Steps

1. **Collect diff** — `git diff HEAD~N..HEAD` + `git log --oneline`
2. **Detect stack** — check `package.json` (Node/TS), `requirements.txt` (Python), `go.mod` (Go), etc.
3. **Send to Claude CLI headless:**
   ```bash
   git diff HEAD~N..HEAD | claude -p "<review prompt>" --model opus --max-turns 1
   ```
4. **Classify findings** into P1/P2/P3 × LOGIC/SYNTAX/STYLE/SECURITY/PERFORMANCE/DEAD_CODE
5. **Save report** to `docs/claude-reviews/claude-review-YYYY-MM-DD.md`
6. **Ask if user wants P1s auto-fixed**

## CLI Flags (mandatory)

| Flag | Value | Why |
|---|---|---|
| `-p` | prompt | Headless, non-interactive mode |
| `--model` | `opus` | Forces Opus (best on SWE-bench Pro: 64.3%) |
| `--max-turns` | `1` | Analysis only — no agentic loop |

## Large Diffs

If diff > 100KB, split by file and send each group separately with a 5s delay between batches.

## Priority Levels

Same as `/codex-review`: P1 Critical / P2 Important / P3 Suggestion.

## Isolation

This skill spawns a **separate** Claude Code CLI instance — independent process, independent context, independent token consumption.

## Fallback

If CLI unavailable: offer to do the review inline (already running Opus), same classification structure.

## Multi-Model Review Pipeline

For critical changes, run all three reviews in order (cheapest first):
1. `/gemini-review` — free (Google OAuth)
2. `/codex-review` — ~$0.40 (OpenAI API key)
3. `/claude-review` — ~$1.00 (Claude subscription)
