# /competitive-analysis

Structured competitor research using Porter's Five Forces and Jobs-to-be-Done. Produces a 1-page brief with actionable positioning insights.

## When to use

Before entering a new market, when a competitor launches a significant new product or campaign, when pricing needs recalibration, when the sales team is losing deals to a specific competitor consistently.

## Inputs

- `competitor_name`: name of the competitor to analyze
- `analysis_depth`: `surface` / `standard` / `deep`

| Depth | What it covers | Time |
|---|---|---|
| Surface | Positioning + ICP + pricing model | ~15 min |
| Standard | All 7 dimensions below | ~45 min |
| Deep | Standard + customer review mining + 3 actionable insights | ~90 min |

## Framework (Porter's Five + Jobs-to-be-Done)

### 1. Positioning
- How do they describe themselves? What headline or tagline do they lead with?
- What promise are they making? Is it functional, emotional, or both?
- What category are they placing themselves in?

### 2. ICP
- Who are they visibly targeting? (industries, company size, job titles)
- What specific pains do they address in their messaging?
- What customer language appears on their site, ads, and case studies?

### 3. Product / Service
- Core features and capabilities
- Pricing model (per seat, flat, usage-based, enterprise)
- Delivery model (self-serve, white-glove, hybrid)
- Notable missing features or gaps

### 4. Go-to-market
- Primary channels (SEO, paid, content, events, partnerships, community)
- Sales motion (PLG, sales-led, channel)
- Content strategy: what do they publish and to whom?
- Where are they visibly spending? (check job postings — they reveal strategy)

### 5. Strengths
What do they do genuinely well? Be honest. Underestimating competitors is more dangerous than overestimating them.

### 6. Vulnerabilities
- What do their G2/Capterra/Trustpilot reviews complain about?
- What do churned customers say?
- What's missing from their offering?
- What market they serve poorly?

### 7. Positioning opportunity
Where can your brand differentiate? This must be specific:
- Not "better customer support" — that's table stakes
- "They don't serve [segment] because [reason] — we can own that segment by [method]"

---

## Output format

```
COMPETITIVE ANALYSIS — [competitor] — [date]
Depth: [surface / standard / deep]

POSITIONING
  [2–3 sentences]

ICP
  Target: [who]
  Pain addressed: [2–3 bullet points]

PRODUCT / SERVICE
  Core: [brief description]
  Pricing: [model]
  Notable gaps: [list]

GO-TO-MARKET
  Primary channels: [list]
  Sales motion: [description]

STRENGTHS
  1. [specific strength]
  2. [specific strength]

VULNERABILITIES
  1. [specific gap or complaint]
  2. [specific gap or complaint]

POSITIONING OPPORTUNITY
  1. [specific differentiation angle]
  2. [specific differentiation angle]
  3. [specific differentiation angle]
```

## Rules

- No vanity analysis. If they're genuinely strong in an area, say so.
- Sources must be cited (URLs, review platforms, job postings). Unverified claims must be marked `[unverified]`.
- Positioning opportunities must be specific and actionable — not "be better" or "focus on quality."
- For `deep` depth: review mining is mandatory. Read at least 10 recent reviews before writing the Vulnerabilities section.
