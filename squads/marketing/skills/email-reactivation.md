# /email-reactivation

Write a 3-email reactivation sequence for inactive leads using the SOAP framework. Low friction, no pressure, one CTA per email.

## When to use

When a lead segment has gone cold (30, 60, or 90+ days without engagement) and needs a structured attempt to re-open the conversation before being moved to passive nurture.

## Inputs

- `lead_segment`: `inactive_30d` / `inactive_60d` / `inactive_90d`
- `product_or_service`: what you're offering (brief description)
- `last_touchpoint`: what the last interaction was (e.g., "attended a webinar", "downloaded a guide", "had a discovery call")

## SOAP Framework

Each email is built on four elements:

**Story** — A brief personal or customer story that mirrors the lead's situation. Not a pitch — a reflection. They should recognize themselves.

**Obstacle** — Name the specific thing holding them back. Not "I know you're busy." Something real: "Most people at this stage are still trying to [X] manually, which means [Y is happening]."

**Action** — One concrete, low-friction step. Not "schedule a call." Something smaller: "Reply to this email with one word", "Click here for the guide", "Tell me if this is still on your radar."

**Prize** — What changes when they take that step. Not a feature list. A before/after. Specific.

---

## Sequence

### Email 1 — D+0 (Re-engagement)
- Subject: plain, no emoji, no clickbait (e.g., "Quick question about [their situation]")
- Lead with the Story — make it personal and recognizable
- Name the Obstacle — the specific thing that probably stalled them
- Low-friction Action: one easy step, not a call booking link
- Prize: the specific change that step unlocks
- Length: max 150 words

### Email 2 — D+7 (Social proof)
- Subject: different framing, reference a result
- Lead with a brief case study or result from someone in their situation
- Obstacle: the specific fear or doubt your proof addresses
- Action: still low-friction — "curious if this changes how you're thinking about it"
- Prize: what that clarity produces
- Length: max 150 words

### Email 3 — D+14 (Breakup)
- Subject: something like "Closing this out" or "Before I close your file"
- Breakup frame: "I'm going to stop reaching out after this — I don't want to send emails that aren't useful to you."
- No pressure. No guilt. No "last chance to get X% off."
- Action: one door left open — "If the timing is ever right, you know where to find me."
- Length: max 100 words

---

## Output format

```
EMAIL REACTIVATION SEQUENCE — [segment] — [product/service]

--- EMAIL 1 (D+0) ---
Subject: [subject line]
Body:
[SOAP email — max 150 words]

--- EMAIL 2 (D+7) ---
Subject: [subject line]
Body:
[SOAP email — max 150 words]

--- EMAIL 3 (D+14 — Breakup) ---
Subject: [subject line]
Body:
[Breakup email — max 100 words]
```

## Rules

- **Each email has ONE CTA.** Never stack multiple asks.
- **No emojis in subject lines.** They filter as promotional in many clients.
- **No discounts as the lever.** Reactivation via discount trains leads to wait for discounts.
- **Max 200 words per email** (including the breakup email at 100 max). Long reactivation emails are not read.
- **After D+14 with no response:** move to long-term nurture. Do not extend the sequence. More emails after this signal = harassment.
