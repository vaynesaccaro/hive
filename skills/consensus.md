---
name: consensus
description: "Send the same question to N OpenRouter models in parallel and show raw responses side by side + overlap/divergence synthesis. Use when one model's bias isn't enough."
---

# /consensus

Multi-model parallel query on the same question. Shows raw responses + synthesis of overlap and divergence. Optional `--deep` mode (`mcp__multi__debate`) has each model critique the others' answers.

## Arguments

- `[models]` — optional. Comma-separated list of aliases (`kimi,gpt5.5,grok`) or brackets (`[kimi,gpt5.5,grok]`). Min 2, max 5.
- `[prompt]` — optional. The question.
- `--deep` — optional. Uses `mcp__multi__debate` (models respond + critique each other). Slower and costlier, but more robust output.

## Flow

1. **Resolve models:**
   - If passed → parse list, resolve aliases via `_core/MODELS-MAP.md`
   - If not → `AskUserQuestion` multiSelect with top 8 + "Other":
     1. `kimi` · 2. `gpt5.5` · 3. `grok` · 4. `gemini-pro` · 5. `qwen-max` · 6. `glm5.1` · 7. `kimi-think` · 8. `dsflash`
   - Validate: 2 ≤ N ≤ 5

2. **Resolve prompt:**
   - If passed → use it
   - If not → ask the user

3. **Calculate `max_tokens` per model** (see `_core/MODELS-MAP.md`): Reasoning 4000 · Non-reasoning 2000.
   If a model returns `finish: length` + `content: null` → retry ONLY that one with doubled cap.

4. **Decide mode:**
   - Without `--deep` → `mcp__multi__compare` (fast, parallel, 1 response per model)
   - With `--deep` → `mcp__multi__debate` (cross-critique, ~3x more tokens)

5. **Render raw responses:**
   ```
   🤖 Consensus — <N> models
   ───────────────────────────────────────────────

   ### 🤖 <model-id-1>
   <literal response, copy-paste, no editing>

   ### 🤖 <model-id-2>
   <literal response>

   ...

   ───────────────────────────────────────────────
   ```

6. **Synthesis (separate from response block):**
   ```
   ### Synthesis — overlap and divergence

   **Points of consensus (≥ N-1 models agree):**
   - <point> (N/N)
   - <point> (N-1/N — divergent: <model>)

   **Points of divergence:**
   - <point>: <model A> says X, <model B> says Y

   **Recommendation:** <objective conclusion>
   ```

## Absolute rules

1. **Model responses always raw** — copy-paste without editing (same as `/second-opinion`).
2. **Synthesis is the AGENT'S** — visually separated, identified as non-canonical analysis.
3. **Minimum 2 models.** "Consensus" from 1 model is just `/second-opinion`.
4. **Maximum 5 models.** More than that = noise + disproportionate cost.
5. **Always show estimated total cost** after (sum tokens × prices from MODELS-MAP).

## When to use `--deep`

| Scenario | Mode |
|---|---|
| Critical decision (architecture, billing, security) | `--deep` |
| Technical hypothesis validation | `--deep` |
| Exploratory research | without `--deep` |
| Style/tone comparison (marketing) | without `--deep` |
| Quick anti-bubble check | without `--deep` |

## Prerequisites

- MCP `multi` active
- `_core/MODELS-MAP.md` readable
- OpenRouter with credits (`--deep` costs 3-5x more)

## Examples

```
/consensus
→ asks for models and prompt

/consensus [kimi,gpt5.5,grok] "Is X a good approach for Y?"
→ 3 models in parallel

/consensus kimi,gemini-pro "which Python lib for rate limiting?" --deep
→ cross-critique, ~3x cost
```

## Refs

- `_core/MODELS-MAP.md` — aliases by category
- `mcp__multi__compare` — normal mode (parallel)
- `mcp__multi__debate` — `--deep` mode (critique)
- Skill `/second-opinion` — single model
