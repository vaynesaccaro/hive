# /analyze-post

Analyze a published post for performance and improvement. Produces a structured diagnosis with scores, a specific rewrite, and actionable fixes.

## When to use

When reviewing a post that underperformed. When auditing a content backlog. When coaching a team member on content quality. Before deciding whether to boost a post with paid spend.

## Inputs

- `post_content`: full text of the published post
- `platform`: `Instagram` / `LinkedIn` / `Twitter/X` / `Threads` / `YouTube` (description)
- `metrics` (optional): views, reach, engagement rate, comments, saves, shares

## Analysis Framework

### 1. Hook strength
- Does it stop the scroll?
- Does it work when truncated (before "see more" / "read more")?
- Is the first line asking for attention or earning it?
- Score: 1–10 with one sentence explanation

### 2. ICP alignment
- Does this speak to a real, documented pain point?
- Is the language the audience actually uses, or marketing language?
- Would the right person see themselves in this post?
- Score: 1–10 with one sentence explanation

### 3. Villain
- Is there an explicit or implicit antagonist — a belief, system, or status quo being challenged?
- Content without a villain is content without tension. Content without tension is content that gets scrolled past.
- Score: present / weak / absent

### 4. CTA
- Is there one?
- Is it specific and low-friction?
- Does it appear before the reader loses momentum?
- Score: strong / present / weak / missing

### 5. Tone consistency
- Does it match the brand voice in `foundation/brand-voice.md`?
- Does it sound like a real human or a marketing department?
- Note any vocabulary that feels off-brand.

### 6. What to keep
List 2–3 elements that worked — even in a weak post, something usually lands. Name them specifically.

### 7. What to change
List 2–3 specific improvements with concrete examples. "Improve the hook" is not useful. "Replace the first line with a specific result from the content" is useful.

---

## Output format

```
POST ANALYSIS — [platform] — [date]

OVERALL SCORE: [X/10]

Hook: [X/10] — [one sentence]
ICP alignment: [X/10] — [one sentence]
Villain: [present / weak / absent] — [one sentence]
CTA: [strong / present / weak / missing] — [one sentence]
Tone: [on-brand / off-brand / mixed] — [one sentence]

What worked:
1. [specific element]
2. [specific element]

What to change:
1. [specific change + example]
2. [specific change + example]

REWRITTEN VERSION:
[full rewrite applying the improvements]

What changed: [3 bullet points explaining the specific edits made]
```

## Rules

- Always produce the rewritten version — analysis without a rewrite is incomplete.
- Score each dimension independently. A post can have a 9/10 hook and 3/10 ICP alignment.
- If `foundation/brand-voice.md` is not available, skip the tone check and note it.
- The rewrite keeps the core idea. It does not change what the post is about, only how it is expressed.
