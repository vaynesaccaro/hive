# /linkedin-post

Adapt content to LinkedIn executive format. Practitioner tone — not expert-from-above, but someone who built something and is sharing what broke.

## When to use

When turning a content idea, article, or insight into a LinkedIn post. Run `/lookup-brand` first unless brand context is already loaded in this session.

## Inputs

- `content`: base text, article draft, or key insight to adapt
- `headline`: the core claim or argument
- `hook_type`: one of — `impactful_demonstration` / `controversial_statement` / `problem_solution` / `direct_question` / `curiosity_gap`
- `article_url` (optional): full article URL if this post promotes a longer piece
- `pillar`: content pillar this belongs to

## Tone

Practitioner in the trenches. The implied voice is: "I built this and here's what broke."

Before writing, identify the **implied villain** — the belief, assumption, or status quo being challenged. Name it internally, even if it doesn't appear explicitly in the post.

## Required Format

**Line 1: Hook (≤ 15 words)**
Must activate doubt or antagonism in the reader. Must work when truncated before "see more" in the feed. Test: does it create an itch the reader needs to scratch?

[blank line]

**Lines 2–6: Body (3–5 bullet points)**
One business insight per bullet. Each bullet should be able to stand alone as a tweet. No fluff. No transitions like "and furthermore" or "in addition."

[blank line]

**Standout data point**
One number, percentage, or concrete cost. Make it specific — "saves 3 hours per week" beats "saves time."

[blank line]

**Closing question**
One specific question that invites a real reply. Not "What do you think?" — something that requires the reader to apply the insight to their own situation.

[blank line]

**3–5 hashtags**
Mix of broad reach and niche relevance.

[blank line]

**MANDATORY CTA (never omit)**
If `article_url` provided: `Read the full article: <article_url>`
If no article: `Follow for more on [topic].`

---

## Length

800–1,300 characters excluding the CTA block. Under 800 feels thin. Over 1,300 loses the feed.

---

## Quality checklist (validate before output)

- [ ] First line activates doubt or antagonism in ≤ 15 words?
- [ ] Tone is practitioner who discovered, not expert who teaches?
- [ ] Villain/challenged belief identified (even if implicit)?
- [ ] Body has at least one specific data point or concrete example?
- [ ] CTA present?
- [ ] Within 800–1,300 character limit?

If any box is unchecked: rewrite before delivering.

## Rules

- Never open with "I" as the first word (LinkedIn algorithm suppresses it).
- Never use hollow phrases: "game-changer," "paradigm shift," "excited to share."
- The CTA is mandatory. Omitting it is a mistake, not a stylistic choice.
- If `article_url` is not provided and there is no meaningful follow action, suggest the author create one before publishing.
