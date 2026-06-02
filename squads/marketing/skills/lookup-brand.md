# /lookup-brand

Retrieve brand guidelines and ICP context before creating any piece of content. Prevents off-brand output from the start.

## When to use

Before any content creation skill (`/content-ideas`, `/linkedin-post`, `/write-caption`, `/write-thread`, `/youtube-script`, etc.). This skill loads the brand context so everything produced afterward is on-brand and ICP-aligned.

It takes 30 seconds. Skipping it costs hours of revision.

## Steps / Framework

### Step 1 — Read brand voice
Read `foundation/brand-voice.md`.

Extract:
- Tone of voice (adjectives that describe how the brand sounds)
- Vocabulary to use (words and phrases that are on-brand)
- Vocabulary to avoid (words and phrases that feel off or inauthentic)
- Content pillars (the recurring themes the brand covers)

### Step 2 — Read ICP profile
Read `foundation/icp-audience.md`.

Extract:
- Primary audience segment(s)
- Core pain points (what keeps them up at night)
- Core beliefs and worldview (what they already believe that the brand builds on)
- Language they use to describe their situation (their words, not marketing words)
- What they're skeptical of (what triggers their distrust)

### Step 3 — Synthesize into a content brief

Present the summary as a quick brief to carry into the next content task:

```
BRAND BRIEF — [date]

Tone: [3-5 adjectives]
Use: [key vocabulary]
Avoid: [off-brand vocabulary]
Content pillars: [list]

ICP: [primary segment name]
Their pain: [2-3 bullet points]
Their language: [key phrases they use]
Their skepticism: [what triggers distrust]

Ready for: [content task name]
```

## Rules

- Do not summarize from memory. Always read the actual files.
- If `foundation/brand-voice.md` does not exist, stop and flag: "Brand voice not configured. Create `foundation/brand-voice.md` before producing content."
- If `foundation/icp-audience.md` does not exist, stop and flag: "ICP profile not configured. Create `foundation/icp-audience.md` before producing content."
- The brief is meant to be carried into the next skill call — not saved as a separate file.
