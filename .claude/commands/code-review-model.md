---
name: code-review-model
description: "Run a code review of the current branch using any OpenRouter model (Kimi, GPT-5 Codex, Qwen Coder, etc). Same P1/P2/P3 output format as /codex-review and /claude-review."
---

# /code-review-model

Code review of the current branch using a model of your choice via OpenRouter MCP. Output format identical to `/codex-review`, `/claude-review`, `/gemini-review` — easy side-by-side comparison if you run multiple.

## Arguments

- `[model]` — optional. Coding alias (`kimi`, `gpt5codex`, `qwencoder`, `glm5.1`, `codestral`, etc.) or raw OpenRouter ID.
- `[base-branch]` — optional. Default: `main`.

## Flow

1. **Resolve model:**
   - If passed → resolve alias via `_core/MODELS-MAP.md`
   - If not → `AskUserQuestion` with top 4 CODING + "Other":
     1. `kimi` (Kimi K2.6 — #1 LiveCodeBench v6 89.6%)
     2. `gpt5codex` (GPT-5.3 Codex — OpenAI dedicated coding)
     3. `qwencoder` (Qwen3-Coder Plus — 1M ctx, top open)
     4. `glm5.1` (GLM-5.1 — #1 web dev open)

2. **Resolve base-branch** (default `main`).

3. **Collect diff:**
   ```bash
   git diff <base-branch>...HEAD
   git log <base-branch>..HEAD --oneline
   ```
   If diff is empty → warn "no changes vs <base-branch>" + stop.

4. **Calculate `max_tokens`**: Reasoning models (kimi, gpt5codex) 4000 · Non-reasoning 2000 · Long diff (>500 lines) 6000-8000 regardless.

5. **Call `mcp__multi__codereview`** with:
   ```
   {
     model: "<openrouter-id>",
     diff: "<git diff content>",
     context: "Branch <current> vs <base-branch>. Commits: <log>"
   }
   ```

6. **Classify findings** into:
   - **P1** — critical (prod-breaking bug, security, wrong logic)
   - **P2** — important (code smell, performance, unhandled edge case)
   - **P3** — style/nit (cosmetic, naming)
   By category: logic · security · syntax · style

7. **Render response:**
   ```
   🤖 Code Review by <openrouter-id>
   ───────────────────────────────────────────────
   Branch: <current> → <base-branch>
   Files changed: <N>
   Lines: +<add>/-<del>

   ### P1 — Critical
   - [logic] <file:line> — <description>
   - [security] <file:line> — <description>

   ### P2 — Important
   - [logic] <file:line> — <description>

   ### P3 — Style/nit
   - [style] <file:line> — <description>

   ### Raw model response (reference)
   <block with full output, copy-paste without editing>
   ───────────────────────────────────────────────
   ```

## Absolute rules

1. **Raw model response always present as appendix** — user can validate if P1/P2/P3 classification is correct.
2. **NEVER invent a finding** — only report what the model found.
3. **Finding ALWAYS with path + line when possible** — if model didn't provide, mark `<no line>`.
4. **Do NOT suggest a fix** unless user asks — review is diagnosis, not execution.
5. **Do NOT commit or edit files** — report only.

## Related skills

- `/codex-review` — Codex CLI direct (not via OpenRouter)
- `/claude-review` — Claude Code direct
- `/gemini-review` — Gemini CLI direct
- `/code-review-model` — **this one**, any model via OpenRouter

Output format is IDENTICAL across all 4 — easy to compare side-by-side.

## Examples

```
/code-review-model
→ asks for model + runs on current branch vs main

/code-review-model kimi
→ Kimi K2.6 review vs main

/code-review-model gpt5codex develop
→ GPT-5.3 Codex review of current branch vs develop
```

## Refs

- `_core/MODELS-MAP.md` — coding aliases
- `_core/mcp/README.md` — MCP setup
- `mcp__multi__codereview` — MCP tool
- Similar skills: `/codex-review`, `/claude-review`, `/gemini-review`
