# /hive-setup

First-time onboarding for HIVE. Guides the user through personalizing the orchestrator and activating squads for their company.

Run once after cloning. Can be re-run to update context at any time.

---

## When to activate

- `/hive-setup` — first time after cloning
- `/hive-setup --reset` — wipe and restart personalization
- "set up my company", "configure HIVE", "personalize the squads"

---

## Step 0 — Welcome

Print exactly:

```
HIVE Setup — let's configure your company.

I'll ask you a few questions. Every field is optional — skip with Enter.
This takes ~5 minutes. You can re-run /hive-setup anytime to update.

Press Enter to begin.
```

---

## Step 1 — Company basics

Ask in sequence (one at a time, not a wall of questions):

1. **Company name** — "What's your company name?"
2. **Industry** — "What industry are you in? (e.g. SaaS, consulting, e-commerce, agency)"
3. **Stage** — "What stage? (pre-revenue / early / growing / scaling)"
4. **Mission** — "One sentence: what does your company do?"

---

## Step 2 — User profile

Ask in sequence:

1. **Your name** — "What's your name?"
2. **Your role** — "What's your role? (Founder, CEO, Solo operator, etc)"
3. **Peak hours** — "When do you do your best work? (e.g. mornings, late night)"
4. **Off limits** — "Any time you never work? (family time, evenings, weekends)"
5. **Preferred style** — "How do you like info delivered? (bullet points, detailed, terse)"

---

## Step 3 — Squad activation

Show the full squad list and ask which to activate:

```
Available squads — which ones apply to your company?
Type the numbers separated by commas, or "all" to activate everything.

 1  Commercial (Victor) — lead gen, proposals, CRM, pipeline
 2  CS / Customer Success (Leah) — onboarding, client health, churn
 3  Marketing (Maya) — content, brand, campaigns, social
 4  Product (Owen) — roadmap, stories, prioritization
 5  Finance (Clara) — invoicing, cash flow, DRE, budget
 6  Dev (Ethan) — code, review, architecture
 7  Infra (Dean) — servers, monitoring, CI/CD, security
 8  Operations (Harper) — HR, culture, OKRs, processes
 9  Quality (Nora) — SOPs, audits, standards
10  Intelligence (Rex) — competitive intel, market research
```

Save the selection as `ACTIVE_SQUADS`.

**Squads NOT selected:** update their `memory/STATE.md` L1 line to:
```
Squad inactive — not selected during /hive-setup. Activate via /hive-setup.
```

---

## Step 4 — Squad context (active squads only)

For each active squad, ask a mini-questionnaire. Keep it tight — 2-3 questions max per squad. Skip squads the user says "skip" to.

### Commercial
- What's your current stage: no pipeline / building pipeline / active pipeline?
- What's your ICP in one sentence?

### CS
- How many active customers do you have?
- What does "successful onboarding" look like for your product?

### Marketing
- What channels are you active on?
- How would you describe your brand voice in 3 words?

### Product
- What's the core problem your product solves?
- What's your north star metric?

### Finance
- What's your revenue model? (subscription / project / retainer / product)
- What's your current monthly burn rate? (approximate is fine)

### Dev
- What's your main tech stack?
- Monorepo or multi-repo?

### Infra
- Where are you hosted? (cloud provider / VPS / serverless)
- Do you have monitoring set up?

### Operations
- How many people on your team (humans)?
- Do you use OKRs or another goal framework?

### Quality
- Do you have any documented SOPs right now?
- What's the highest-risk process in your company?

### Intelligence
- Who are your top 2-3 competitors?
- How often do you do competitive research?

---

## Step 5 — Write files

After collecting all answers, write everything in one batch:

### 5a — Update `CLAUDE.md` root (company section)

Replace the `## The company (personalize this)` block with:
```markdown
## The company

- **Company:** [name]
- **Industry:** [industry]
- **Stage:** [stage]
- **Mission:** [mission]
- **Team:** [user name] + AI squads
```

### 5b — Write `squads/orchestrator/context/user-profile.md`

Fill every answered field. Leave unanswered fields blank (not `[placeholder]`).

### 5c — Write each active squad's `context/squad-context.md`

Fill with answers from Step 4. Leave unanswered fields blank.

### 5d — Update Orchestrator `memory/STATE.md`

Replace L1 with:
```
[L1]
HIVE configured. Company: [name] | Industry: [industry] | Stage: [stage]
Active squads: [comma-separated list]
Last setup: [YYYY-MM-DD]

[L2]
- [ ] Populate foundation/ docs for active squads
- [ ] Configure PM tool (default: Linear — see docs/how-to-customize.md)

[L3]
- Set up workers for recurring tasks
- Run first /status after populating foundation/
```

---

## Step 6 — Confirm

Print:

```
HIVE configured.

Company:        [name] — [industry] ([stage])
Active squads:  [list]
User profile:   [name], [role]

Files updated:
  ✅ CLAUDE.md — company section
  ✅ squads/orchestrator/context/user-profile.md
  ✅ squads/orchestrator/memory/STATE.md
  ✅ squads/[each active squad]/context/squad-context.md

Next steps:
  1. Open a squad to start working:
     /open-squad commercial
  2. Populate foundation/ docs for deeper context:
     squads/commercial/foundation/icp-profile.md
     squads/dev/foundation/tech-stack.md
     (see each squad's CLAUDE.md for the full list)
  3. Check aggregate status anytime:
     /status
```

---

## Rules

1. **Never write placeholder text** (`[Your name]`, `[TBD]`) — blank field is better than fake data.
2. **Never invent answers** — only write what the user actually said.
3. **Inactive squads get a clear STATE.md note** — not just empty files.
4. **Re-run is safe** — always overwrite, never append.
5. **Commit after writing** — `git add -A && git commit -m "chore(setup): hive-setup — [company name]"`.
