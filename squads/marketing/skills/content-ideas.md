# /content-ideas

Generate N content ideas aligned with your ICP and brand. No generic output — every idea needs a specific angle.

## When to use

When building an editorial calendar, planning a content sprint, or when the team has run out of ideas that feel original. Run `/lookup-brand` first.

## Inputs

- `quantity`: number of ideas to generate (default: 4)
- `channel`: `Instagram` / `LinkedIn` / `YouTube` / `TikTok` / `Threads`
- `focus_pillar` (optional): restrict to a specific content pillar

## Steps / Framework

### Step 1 — Load brand and ICP context
Read `foundation/brand-voice.md` and `foundation/icp-audience.md`. If `/lookup-brand` was already run in this session, use that output instead.

### Step 2 — Research recent trends
Search for recent discussions, news, and viral content in your industry. What is your ICP talking about right now? What questions are they asking? What frustrations are they venting?

### Step 3 — Generate candidate ideas
For each candidate idea, ask before including it:
- Does it name an enemy, villain, or antagonist? (A belief, system, or status quo that holds your ICP back.)
- Is it specific enough to not be generic? The test: could this idea be published by 100 different brands without changing more than the name?

Discard any idea that fails both checks.

### Step 4 — Score and filter
Score each surviving idea on four dimensions (1–10 each):
- **Trend relevance**: is this timely? Does it connect to something happening now?
- **ICP alignment**: does it speak to a real, documented ICP pain point?
- **Originality**: could only your brand publish this angle?
- **Actionability**: can this be produced and published this week?

Include only ideas with total score ≥ 20 (out of 40), or individual dimension score ≥ 5.

---

## Output format (per idea)

```
---
Idea: [specific title with a clear angle — not a topic, an angle]
Pillar: [education / challenge / story / proof]
ICP: [which audience segment this targets]
Score: [X/40] (trend: X | ICP: X | originality: X | actionability: X)
Villain: [the belief, system, or status quo being challenged]
Angle: [2–3 sentences on the unique take]
Keywords: [3–5 SEO or discovery keywords]
Best channels: [where this format and angle performs best]
Why now: [what trend or context makes this timely]
---
```

## Rules

- **Never produce generic ideas.** "Post about AI trends" or "share a productivity tip" are not ideas — they are categories. Every output must have a specific angle.
- **The villain must be named.** An idea without an antagonist has no tension. No tension = no engagement.
- **Verify against recent posts** before finalizing — if the brand published something similar in the last 30 days, find a new angle.
- If fewer than the requested quantity of ideas pass the quality filter, return only the passing ideas and explain why the rest were cut.
