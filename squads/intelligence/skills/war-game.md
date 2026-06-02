# /war-game

Simulate a competitive scenario before committing to a market decision. Find the failure mode before the market does.

## When to use

Before any significant market-facing decision:
- Launching at a new price point
- Entering a new market segment
- Announcing a product feature publicly
- Making a significant partnership or exclusivity move
- Repositioning brand messaging

## Inputs

- `decision`: the specific decision under evaluation (be precise — "launch at [price X]" not "change pricing")
- `timeframe`: horizon for the simulation (e.g., "next 90 days", "next 12 months")

## Steps / Framework

### Step 1 — Identify key stakeholders
For this specific decision, identify 3–5 parties who will react:

Typical stakeholders (select the most relevant for the decision):
- **Main competitor**: what do they do in response?
- **Target customer (ICP)**: how do they perceive and react to this?
- **Channel partner or distributor**: does this affect their incentives?
- **Investor or board**: how does this read against stated strategy?
- **Skeptical internal team member**: who internally would object and why?

### Step 2 — Simulate each stakeholder's reaction
For each stakeholder:
- First reaction: immediate instinct (within 48 hours)
- Best response: if they're playing to win, what do they do?
- Worst case for you: the move that most threatens your decision's success

### Step 3 — Find the fast failure scenario
Combine 2–3 stakeholder reactions to construct the scenario where your decision fails fastest. Be specific: what happens in month 1, month 3, month 6?

### Step 4 — Find the high-upside scenario
Combine 2–3 stakeholder reactions to construct the scenario where your decision succeeds beyond expectations. What conditions need to be true?

### Step 5 — Output recommendation and contingencies

---

## Output format

```
WAR GAME — [decision] — [date]
Timeframe: [timeframe]

STAKEHOLDER REACTIONS

[Stakeholder 1: e.g., Main Competitor]
  First reaction: [description]
  Best response: [description]
  Worst case for us: [description]

[Stakeholder 2: e.g., Target Customer]
  First reaction: [description]
  Best response: [description]
  Worst case for us: [description]

[...continue for all stakeholders...]

FAST FAILURE SCENARIO
  Month 1: [what happens]
  Month 3: [what happens]
  Month 6: [outcome]
  Trigger conditions: [what makes this scenario activate]

HIGH-UPSIDE SCENARIO
  Month 1: [what happens]
  Month 3: [what happens]
  Month 6: [outcome]
  Conditions required: [what needs to be true]

RECOMMENDATION: [Go / Go with conditions / No-go]
Rationale: [2–3 sentences]

CONTINGENCY PLAN A (if fast failure begins)
  Trigger: [early warning signal]
  Response: [what to do]

CONTINGENCY PLAN B (if different failure mode)
  Trigger: [early warning signal]
  Response: [what to do]
```

## Rules

- The fast failure scenario must be plausible, not catastrophic fiction. Ground it in what competitors have actually done before.
- Every contingency plan must have a named trigger (an observable signal that activates it) — not just a response.
- A "Go" recommendation does not mean the risks don't exist. It means the expected value is positive given the contingencies are prepared.
- Log the output in `memory/decisions.md` before the decision is executed.
