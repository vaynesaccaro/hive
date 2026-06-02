---
name: second-opinion
description: "Ask any OpenRouter model a question and get the raw response — copy-paste, zero editing. Use when you want a second perspective from Kimi, GPT-5, Grok, Gemini, etc."
---

# /second-opinion

Single-model query via OpenRouter MCP. **The model's response is delivered 100% raw, no rewriting, no agent commentary mixed in.** Agent commentary, if any, comes AFTER, clearly separated.

## Arguments

- `[model]` — optional. Friendly alias (`kimi`, `gpt5.5`, `grok`, `gemini-pro`, etc.) OR raw OpenRouter ID (`moonshotai/kimi-k2.6`). Catalog: `_core/MODELS-MAP.md`.
- `[prompt]` — optional. The question. If missing, ask the user.

## Flow

1. **Resolve model:**
   - If passed as argument → resolve alias from `_core/MODELS-MAP.md` → OpenRouter ID
   - If not → `AskUserQuestion` with top 4 general + "Other":
     1. `kimi` (Kimi K2.6 — top coding open)
     2. `gpt5.5` (GPT-5.5 — flagship reasoning)
     3. `grok` (Grok 4.20 — 2M ctx, low cost)
     4. `gemini-pro` (Gemini latest — multimodal/long)

2. **Resolve prompt:**
   - If passed → use it
   - If not → ask: "What's your question?"

3. **Calculate `max_tokens`** (see `_core/MODELS-MAP.md` reasoning gotcha):
   - Reasoning models (Kimi K2.6, GPT-5.x, kimi-thinking, qwen-thinking, deepseek-r1): `4000`
   - Non-reasoning: `2000`
   - User passed `--max-tokens N` → use N

4. **Call MCP tool `mcp__multi__chat`** with `{model: "<id>", prompt: "<question>", max_tokens: <calculated>}`.
   - If response returns `finish_reason: "length"` + `content: null` → retry with `max_tokens * 2` (cap 8000). Notify user.

5. **Render response in REQUIRED format:**
   ```
   🤖 <openrouter-id> responded:
   ───────────────────────────────────────────────
   <LITERAL RESPONSE, ZERO EDITING, INCLUDING ORIGINAL FORMATTING>
   ───────────────────────────────────────────────
   ```

6. **Ask user:** "Want my analysis/commentary? (yes/no)"
   - If yes → add analysis AFTER the block
   - If no → done

## Absolute rules

1. **NEVER edit, paraphrase, summarize or "improve" the model's response.** Exact copy-paste.
2. **NEVER mix agent commentary inside the response block.** Commentary comes outside, clearly separated.
3. **Always show the full OpenRouter ID** in the header (not the alias).
4. **No markdown headers (##) inside the block** — may break visual delimitation.

## Prerequisites

- MCP `multi` active (`.mcp.json` in cwd, `OPENROUTER_API_KEY` in env)
- `_core/MODELS-MAP.md` readable to resolve aliases

## Examples

```
/second-opinion
→ asks for model and prompt

/second-opinion kimi "what Python pattern for circuit breaker?"
→ goes directly to Kimi K2.6

/second-opinion gpt5.5 "refute this argument: <long text>"
→ alias + inline prompt
```

## Refs

- `_core/MODELS-MAP.md` — aliases and OpenRouter IDs
- `_core/mcp/README.md` — MCP setup guide
- `mcp__multi__chat` — MCP tool used
- Complementary skill: `/consensus` — ask N models the same question
