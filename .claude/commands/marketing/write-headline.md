# /write-headline

Generate 5 headline variants for a piece of content. Each variant uses a different psychological mechanism.

## When to use

When writing an article, email, ad, or post and the headline needs to be tested before committing. Also use before publishing any long-form content to ensure the headline earns the click.

## Inputs

- `topic`: the subject of the content
- `content_summary`: 2–3 sentences on what the content actually delivers
- `target_audience`: who this is written for (ICP segment or persona)
- `platform`: `article` / `post` / `email` / `ad`

## Steps / Framework

### Step 1 — Understand what the content delivers
Before writing headlines, confirm: what specific, concrete value does this content give the reader? Vague content produces vague headlines.

### Step 2 — Generate 5 variants

One headline per type:

| Type | Mechanism | Example pattern |
|---|---|---|
| **Curiosity gap** | Creates an information gap the reader needs to close | "The [X] most people skip that changes everything" |
| **How-to** | Promises a specific skill or outcome | "How to [result] without [common pain]" |
| **Number list** | Sets clear expectations and implies thoroughness | "[N] ways to [outcome] in [timeframe]" |
| **Challenge** | Confronts a common belief or assumption | "You don't need [popular thing]. You need [better thing]." |
| **Proof-based** | Anchors on a result, case, or data point | "[Specific result]: what [example] did that others don't" |

### Step 3 — Evaluate each variant

For each headline:
- Character count
- Why it works for this specific ICP
- The ICP scroll-stop test: "Would my ICP stop scrolling for this, or keep going?"

---

## Output format

```
HEADLINE VARIANTS — [topic] — [platform]

1. [Curiosity gap]
   Headline: [text]
   Characters: [N]
   Why it works: [one sentence for this ICP]
   Scroll-stop test: [yes / borderline / no]

2. [How-to]
   ...

3. [Number list]
   ...

4. [Challenge]
   ...

5. [Proof-based]
   ...

RECOMMENDED: [headline number] — [one sentence rationale]
```

## Rules

- **No clickbait without substance.** The headline must be deliverable by the content. If the content doesn't deliver what the headline promises, rewrite the content — not just the headline.
- **The scroll-stop test is mandatory.** If the honest answer is "no," revise the headline.
- **Never produce a headline with "game-changer," "secret," or "hack."** These are noise.
- Provide a recommended pick with rationale — do not leave the choice entirely to the user.
