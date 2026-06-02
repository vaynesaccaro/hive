# /challenge

Independent second opinion on a technical decision. Surfaces blind spots before they become incidents.

## When to use

- When a decision feels settled and the team is about to commit
- When everyone agrees — unanimous agreement in a technical discussion is often a warning sign
- Before merging a significant architectural change
- When a senior engineer wasn't part of the original discussion
- As a pre-mortem step before shipping something non-trivial

## How it works

The challenger assumes the role of a skeptical senior engineer who was **not part of the original discussion**. This is important: the challenger has no emotional investment in the decision being correct.

### Step 1 — State the decision
Describe the decision that was made (or is about to be made) clearly:
- What was decided
- What alternatives were considered
- Why this option won

### Step 2 — The challenger probes with four questions

**1. What assumptions were made?**
List every assumption baked into this decision. Mark each as: verified / unverified / untestable.

**2. What is the failure mode?**
How does this break? Under what load, edge case, or input does it fail? What's the blast radius when it does?

**3. What is the maintenance cost in 2 years?**
Who will be on-call for this? Will they understand it? What will onboarding a new engineer to this component look like?

**4. Who disagrees and why?**
Name the people who might have a legitimate objection to this decision. Steelman their position.

### Step 3 — Output three challenges

Three specific, concrete challenges to the decision. Not vague skepticism — actual objections a senior engineer would raise.

### Step 4 — Recommendation

One of three outcomes:
- **Keep**: challenges raised, but decision holds. Document the tradeoffs accepted.
- **Revisit**: one or more challenges require further investigation before proceeding.
- **Reverse**: a challenge reveals a fundamental problem. Stop and re-evaluate.

---

## Output format

```
CHALLENGE — [decision topic] — [date]

Decision under review: [brief description]

Assumptions made:
- [assumption 1]: [verified / unverified]
- [assumption 2]: [verified / unverified]

Failure mode: [description]
Maintenance cost: [2-year projection]
Who disagrees: [name the perspective and why]

Challenges:
1. [specific challenge]
2. [specific challenge]
3. [specific challenge]

Recommendation: [Keep / Revisit / Reverse]
Rationale: [one sentence]
```

## Rules

- The goal is not to block work — it is to surface blind spots before they become incidents.
- The challenger must steelman every challenge. Weak objections waste everyone's time.
- If the recommendation is "Keep," document the challenges accepted so future engineers understand the tradeoffs.
- Log the output in `memory/decisions.md` if the recommendation is Revisit or Reverse.
