# /improve-post

Rewrite a post to improve its performance. Diagnose first, then fix the top weaknesses. Show your work.

## When to use

When a post needs to be improved before publishing, or when a published post should be revised for a future republish. Differs from `/analyze-post` in that the primary output is the improved version, not the diagnostic report.

## Inputs

- `original_post`: the full text of the post to improve
- `platform`: `Instagram` / `LinkedIn` / `Twitter/X` / `Threads`
- `main_weakness` (optional): a hint about what to focus on (e.g., "hook is weak", "no CTA", "too generic")

## Steps / Framework

### Step 1 — Run the diagnosis
Apply the same analysis as `/analyze-post` internally. Identify:
- Hook strength
- ICP alignment
- Villain presence
- CTA quality
- Tone consistency

### Step 2 — Identify the top 2 weaknesses
From the diagnosis, select the 2 factors with the lowest scores. These are the only things being fixed. Do not try to fix everything at once — focused rewrites outperform total overhauls.

If `main_weakness` was provided as input, verify it against the diagnosis. If the hint disagrees with the diagnosis, prioritize the diagnosis and note the discrepancy.

### Step 3 — Rewrite
Produce the improved version. Constraints:
- Keep the core idea. The rewrite is not a new post — it is the same post, better expressed.
- Only change the structure, hook, or CTA unless the angle itself is the root problem.
- If the angle is the root problem, flag it explicitly and rewrite with the new angle — but confirm with the user before doing so.

### Step 4 — Show the reasoning

---

## Output format

```
IMPROVE POST — [platform]

TOP 2 WEAKNESSES IDENTIFIED:
1. [weakness + evidence from the original post]
2. [weakness + evidence from the original post]

ORIGINAL:
[original post text]

REWRITE:
[improved post text]

WHAT CHANGED:
1. [specific change and why it addresses weakness 1]
2. [specific change and why it addresses weakness 2]
3. [any other notable change]
```

## Rules

- Always show what changed and why. A rewrite without an explanation is just a different post — it doesn't teach anything.
- Never change the core idea without flagging it. Changing the angle without consent is overstepping.
- If `main_weakness` contradicts the diagnosis, say so explicitly. Don't silently override the user's input without acknowledgment.
- If the original post is fundamentally strong and the changes are minor, say so. Not everything needs a major rewrite.
