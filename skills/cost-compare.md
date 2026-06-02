---
name: cost-compare
description: "Cost/quality matrix — run the same task across N models at different price tiers, show response + cost + tokens, help choose the 'cheap enough' model for recurring workers."
---

# /cost-compare

Sends the same task to a range of models (cheapest to top tier) and shows response + cost side by side. Use to:
- **Before embedding a model in a recurring worker** — confirms that the cheap tier is sufficient
- **Before creating a new skill** — choose the suggested default model
- **Cost/quality trade-off analysis** — see the trade-off clearly

## Arguments

- `[models]` — optional. List of aliases. Default suggestion (asked): `[granite, dsflash, qwenflash, codestral, kimi]` — sweep from cheapest to top, 5 models.
- `[prompt]` — optional. The task to test. If missing, ask.

## Flow

1. **Resolve models:**
   - If passed → resolve aliases via `_core/MODELS-MAP.md`
   - If not → `AskUserQuestion` multiSelect with suggested range + "Other":
     1. `granite` ($0.05/$0.10 — IBM tiny)
     2. `dsflash` ($0.10/$0.20 — DeepSeek)
     3. `qwenflash` ($0.19/$1.13 — Qwen)
     4. `codestral` ($0.30/$0.90 — Mistral)
     5. `kimi` ($0.68/$3.42 — Kimi K2.6)
     6. `gpt5.4` ($2.50/$15 — top tier reference)
   - Validate: 3 ≤ N ≤ 6 (need ≥3 for matrix to make sense)

2. **Resolve prompt:**
   - If passed → use it
   - If not → ask user (prefer a REPRESENTATIVE prompt of recurring use, not an isolated test)

3. **Calculate `max_tokens` per model**: Reasoning 4000 · Non-reasoning 2000. Compare fairly — all with enough tokens to deliver complete response, otherwise the matrix is biased.

4. **Call `mcp__multi__compare`** with N models + prompt.

5. **Calculate cost per call:** read prices from `_core/MODELS-MAP.md`, multiply by tokens reported by MCP (`usage.prompt_tokens`, `usage.completion_tokens`).

6. **Render matrix:**
   ```
   💰 Cost-Compare Matrix — <N> models × 1 task
   ───────────────────────────────────────────────

   ### 🤖 <model-id-1> · $<real-cost-this-call>
   <raw response>

   ### 🤖 <model-id-2> · $<cost>
   <raw response>

   ...

   ───────────────────────────────────────────────

   ### Summary matrix

   | Model | Cost this call | Tokens in/out | $/M in | $/M out |
   |---|---|---|---|---|
   | <model-1> | $<x.xxxxx> | <in>/<out> | $<a> | $<b> |
   | <model-2> | $<x.xxxxx> | <in>/<out> | $<a> | $<b> |

   **Total cost this run:** $<sum>

   ### Analysis

   **Perceived quality** (subjective, agent analyzes):
   - <model-X>: <very good | OK | weak | failed> — <observation>

   **Recommendation by use case:**
   - High-volume workers (>1000 calls/day): <cheapest sufficient model>
   - Occasional skill with quality requirements: <mid tier>
   - Single critical task: <top model>
   ```

## Absolute rules

1. **Model responses always raw** — copy-paste without editing
2. **Cost calculated from REAL tokens reported by MCP** — don't estimate via length()
3. **Quality analysis is the AGENT'S** — visually separated, marked as subjective
4. **NEVER recommend a model without seeing output quality** — cheap and broken is expensive
5. **Prompt must be REPRESENTATIVE of real use** — testing with "what is 2+2" says nothing about a worker that generates carousels

## Recommended usage pattern

1. Before creating a new skill or worker, run `/cost-compare` with a representative prompt
2. Note result in the relevant squad's `memory/decisions.md`: "Worker X uses model Y, validated on $/cost-compare YYYY-MM-DD, avg cost $0.0XX/call"
3. Revisit quarterly — new models may have appeared with better cost/quality

## Examples

```
/cost-compare
→ asks for models and prompt

/cost-compare [granite,dsflash,kimi,gpt5.4] "extract 3 main tags from this post: <text>"
→ 4-model matrix for tagging task

/cost-compare dsflash,qwenflash,codestral "explain in 2 sentences the difference between debounce and throttle"
→ 3 cheap models for short explanation task
```

## Refs

- `_core/MODELS-MAP.md` — "Fast / cheap" tier + flagship for comparison
- `mcp__multi__compare` — MCP tool
