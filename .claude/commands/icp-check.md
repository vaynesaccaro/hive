---
name: icp-check
description: "Simulate your ICP reading an asset (copy, pitch, email, landing page, post) and responding as if they were the target customer. Uses 2-3 models for cross-cultural triangulation."
---

# /icp-check

An OpenRouter model assumes the role of your ICP (Ideal Customer Profile) and responds as they would read the asset. By default uses 2-3 models to triangulate reactions (diverse cultural bias = more robust signal).

## Arguments

- `[models]` — optional. List of aliases. Default suggestion (asked if not passed): `[gemini-pro, gpt5.5, kimi]` (3 different families for cultural bias variation).
- `[icp]` — optional. Path to ICP file or inline description.
  - Default: tries to read `squads/marketing/foundation/icp-audience.md`
  - Inline: `--icp "B2B SaaS CEO, 20-50 employees, pain: cold pipeline"`
- `[asset]` — optional. File path or inline text.

## Flow

1. **Resolve ICP:**
   - `--icp` inline argument → use it
   - Path to file → Read
   - No argument → try `squads/marketing/foundation/icp-audience.md`; if not found, ask user to describe

2. **Resolve asset:**
   - Path argument → Read
   - Text argument → use
   - No argument → ask user (paste text or path)

3. **Resolve models:**
   - If passed → resolve aliases via `_core/MODELS-MAP.md`
   - If not → `AskUserQuestion` multiSelect with 4 + "Other":
     1. `gemini-pro` (Google/global bias)
     2. `gpt5.5` (OpenAI/Western bias)
     3. `kimi` (Asian bias)
     4. `glm5.1` (open Chinese bias)
   - Validate: 2 ≤ N ≤ 4

4. **Build ICP prompt (same string for all models):**
   ```
   You are the following customer:
   <FULL ICP>

   You just received/read the following material from a company:
   <ASSET>

   Respond ONLY as this customer, first person, thinking out loud.
   Include: visceral first reaction (1-2 sentences), what caught your attention (positive),
   what bothered you (negative, if any), and whether you would take the next step
   (reply to email, click button, schedule meeting) — yes/no/maybe + why.
   Do NOT break character. Do NOT offer marketing advice.
   ```

5. **Calculate `max_tokens`**: Reasoning 4000 · Non-reasoning 2000. ICP simulation can be long — don't cut short.

6. **Call `mcp__multi__compare`** with N models.

7. **Render:**
   ```
   🎯 ICP Check — <N> cross-model simulations
   ICP: <title/summary>
   Asset: <title/path>
   ───────────────────────────────────────────────

   ### 🤖 <model-id-1> responding as ICP
   <raw response>

   ### 🤖 <model-id-2> responding as ICP
   <raw response>

   ...
   ───────────────────────────────────────────────

   ### Synthesis

   **Dominant reaction:** <consensus across models>
   **Would take next step?** <N yes / N no / N maybe>
   **Consensus positives:** <list>
   **Consensus negatives:** <list>
   **Divergences (review):** <points where models disagreed>

   **Recommendation:** <publish, adjust point X, redo>
   ```

## Absolute rules

1. **Model stays in character** — if it "breaks the fourth wall" (gives marketing advice), note it in the block
2. **Model responses always raw** — copy-paste, no editing
3. **Synthesis is the AGENT'S OPINION** — visually separated
4. **Does NOT replace real customer interviews** — proxy/shortcut; validate with real users when possible
5. **Minimum 2 models.** ICP from 1 model doesn't capture bias

## Examples

```
/icp-check
→ asks for everything: models, ICP, asset

/icp-check kimi,gpt5.5 --icp "B2B SaaS CEO" "<paste copy here>"
→ 2 models, inline ICP, inline asset

/icp-check gemini-pro,kimi,glm5.1 --icp foundation/icp-audience.md ./drafts/launch.md
→ 3 models, ICP from file, asset from file
```

## Refs

- `squads/marketing/foundation/icp-audience.md` — fill via `/hive-setup`
- `_core/MODELS-MAP.md` — aliases
- `mcp__multi__compare` — MCP tool
