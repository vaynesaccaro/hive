---
name: anti-bubble
description: "A neutral model (no company context) reads an asset and answers 'what does this communicate to an outsider?' — captures external reading without internal bias."
---

# /anti-bubble

An OpenRouter model reads your asset with ZERO company context and responds as an external reader. Detects:
- Internal jargon that seems obvious but isn't
- Undeclared assumptions
- Messages that communicate X internally but Y externally
- Missing hook/context for people who don't know your brand

Default suggestion: `gemini-pro` (Google corpus = linguistically diverse) or `kimi` (Chinese corpus = completely outside the typical English/marketing bubble).

## Arguments

- `[model]` — optional. Default suggestion (asked if not passed): `gemini-pro`.
- `[asset]` — optional. File path or inline text.

## Flow

1. **Resolve model:**
   - If passed → resolve alias
   - If not → `AskUserQuestion` with 4 + "Other":
     1. `gemini-pro` (Google — most linguistically diverse corpus)
     2. `kimi` (Moonshot — Asian bias, completely outside English bubble)
     3. `gpt5.5` (OpenAI — Western bias, conservative)
     4. `glm5.1` (Z-AI — open Chinese, alternative)

2. **Resolve asset:**
   - Path → Read
   - Inline text → use
   - No argument → ask the user

3. **Build prompt WITH NO COMPANY CONTEXT:**
   ```
   You are reading the following material for the first time. You know NOTHING about
   the company that produced it, the target audience, or the business context. Act as
   a generic, intelligent reader who came across this by chance (ad in a feed, forwarded
   email, LinkedIn post).

   <ASSET>

   Answer objectively:
   1. What is this message communicating? (1-2 sentences, in your reading)
   2. Who do you think the target audience is? (in your reading)
   3. What did you UNDERSTAND clearly?
   4. What was CONFUSING or ambiguous?
   5. Did you feel curious to know more? (yes/no + why)
   6. Are there any words/expressions you don't recognize or that seem like jargon?

   Do NOT offer marketing advice. Do NOT assume context beyond the text.
   ```

4. **Calculate `max_tokens`**: Reasoning 4000 · Non-reasoning 2000.

5. **Call `mcp__multi__chat`** with chosen model.

6. **Render:**
   ```
   🌐 Anti-Bubble Check — <model-id> (no company context)
   Asset: <title/path>
   ───────────────────────────────────────────────

   <raw model response>
   ───────────────────────────────────────────────

   ### Synthesis

   **Intended by company:** <space for user to declare>
   **Read by outsider:** <synthesis of response>
   **Communication GAP:**
   - <point where intent ≠ reading>
   - <flagged jargon>
   - <undeclared assumption>

   **Verdict:**
   - 🟢 Communicates as intended
   - 🟡 Partial — adjust X
   - 🔴 Doesn't communicate — rewrite
   ```

## Absolute rules

1. **Prompt NEVER includes company context** — the whole point is the model reading "clean."
2. **Model response always raw** — copy-paste without editing.
3. **Synthesis is the AGENT'S** — visually separated.
4. **GAP is the key metric** — difference between intended vs. read. No declared GAP = incomplete analysis.

## When NOT to use

- Very technical material where "outsider" doesn't give useful reading (e.g. API doc for devs) → `/second-opinion` with coding model
- Very long material (>5000 words) → break into sections
- Multimodal material (image + text critique) → ensure use of `gemini-pro` (native multimodal)

## Examples

```
/anti-bubble
→ asks for model and asset

/anti-bubble gemini-pro ./drafts/linkedin-post.md
→ Gemini reads file

/anti-bubble kimi "We are AI-First. Our method applies VSM to B2B SaaS to scale without operational noise."
→ Kimi reads inline — will catch all the jargon
```

## Refs

- `squads/marketing/foundation/brand-voice.md` — adjust when verdict is red
- `squads/marketing/foundation/icp-audience.md` — use `/icp-check` for ICP reading (not outsider)
- `_core/MODELS-MAP.md` — models with diverse corpus (Gemini, Kimi, GLM)
- `mcp__multi__chat` — MCP tool
