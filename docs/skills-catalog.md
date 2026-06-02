# HIVE Skills Catalog

Complete reference for all 43 skills across HIVE. Invoke any skill with `/skill-name` inside Claude Code.

---

## Global Skills

Available in every squad context.

| Skill | Invocation | What it does |
|---|---|---|
| HIVE onboarding | `/hive-setup` | First-time company setup — fills all squad contexts with your company data |
| Open squad | `/open-squad <name>` | git pull + load CLAUDE.md + STATE.md; aggregates L1 if squad has children |
| Close squad | `/close-squad <name>` | Update STATE.md + decisions log + propagate L1 to parent |
| Company status | `/status` | Aggregate L1 from all active squads in one view |
| Log incident | `/log-incident` | Create incident record in `incidents/` hub + update INDEX.md |

---

## Orchestrator Skills

> **Stamper — Chief of Staff.** Issue and project lifecycle management.

| Skill | Invocation | What it does |
|---|---|---|
| Create issue | `/create-issue` | Guided issue creation: title, description, acceptance criteria, squad, priority |
| Plan issue | `/plan-issue` | Break issue into technical plan with file list + approval gate before coding starts |
| Start issue | `/start-issue` | Checkout branch from Linear branchName + mark issue In Progress |
| Close issue | `/close-issue` | Quality cycle (review → build → test) + merge + mark Done in Linear |

**Workflow order:** `/create-issue` → `/plan-issue` → `/start-issue` → (implement) → `/close-issue`

---

## Commercial Skills

> **Victor — Head of Sales.** Lead pipeline, qualification, and deal closing.

| Skill | Invocation | What it does |
|---|---|---|
| Sales call | `/sales-call` | 7-part Challenger Sale framework: Warm-up → Reframing → Urgency → Emotional → New Path → Solution → Closing |
| Handle objection | `/handle-objection` | Surface-to-real objection mapping, diagnostic flow, non-fit signal detection |
| Follow up | `/follow-up` | D+0/D+2/D+7/D+14 sequence + breakup email template |
| Commercial debate | `/commercial-debate` | Multi-perspective roundtable: Sales vs CS vs Finance vs Devil's Advocate |

---

## CS Skills

> **Leah — Head of CS.** Onboarding, retention, and success metrics.

| Skill | Invocation | What it does |
|---|---|---|
| CS debate | `/cs-debate` | Roundtable on customer success decisions with multiple perspectives |
| Log KPI | `/log-kpi` | Record customer KPI snapshot in `data/kpis.md` with timestamp |

---

## Dev Skills

> **Ethan — Tech Lead.** Architecture, code review, debugging, and documentation.

### Code Review Pipeline

Run cheapest → most expensive. Stop when issues are found and fixed.

| Skill | Invocation | Cost | What it does |
|---|---|---|---|
| Gemini review | `/gemini-review` | Free | Gemini 2.5 Flash via OAuth CLI — structural review, P1/P2/P3 |
| Codex review | `/codex-review` | ~$0.40 | OpenAI Codex CLI — security, logic, performance classification |
| Claude review | `/claude-review` | Subscription | Claude Opus headless — deep architectural review, final gate |

**Classification used across all reviews:**
- **P1** — blocks merge (security hole, broken logic, data loss risk)
- **P2** — must fix before next deploy (performance, error handling, test gap)
- **P3** — fix in follow-up (naming, style, minor edge case)

**When to use which:**
| Change type | Reviews |
|---|---|
| Trivial (copy, isolated CSS) | None required |
| New feature code | `/codex-review` |
| Logic/functional change | `/codex-review` + `/claude-review` |
| Critical (auth, billing, migration, deploy) | All three + senior approval |

### Development

| Skill | Invocation | What it does |
|---|---|---|
| Dev debate | `/dev-debate` | Architecture roundtable with multiple tech personas |
| Quick dev | `/quick-dev` | Rapid throwaway prototype mode — builds fast, documents nothing |
| Challenge | `/challenge` | Independent second opinion on a technical decision |
| Document | `/document` | Generate documentation after a feature ships (updates code docs + wiki) |

### Debugging

| Skill | Invocation | What it does |
|---|---|---|
| Debug | `/debug` | Pólya 4-phase framework: Understanding → Investigation Plan → Diagnosis → Fix + Retrospective |

**Triage levels:**
- **TRIVIAL** — fix immediately, minimal validation
- **MEDIUM** — full Pólya cycle, user validates fix
- **CRITICAL** — mandatory retrospective + root cause + prevention

---

## Finance Skills

> **Clara — CFO.** Runway, reporting, and financial health.

| Skill | Invocation | What it does |
|---|---|---|
| Finance debate | `/finance-debate` | CFO roundtable on financial decisions |
| Runway | `/runway` | Calculate burn rate + months of runway from current data |
| Monthly report | `/monthly-report` | Generate monthly P&L summary from squad data |

---

## Infra Skills

> **Dean — Head of Infra.** Servers, monitoring, security, and credential rotation.

| Skill | Invocation | What it does |
|---|---|---|
| Infra debate | `/infra-debate` | Infrastructure decision roundtable |
| Hardening check | `/hardening-check` | Security checklist: ports, SSH keys, firewall, TLS, env vars |
| Restart service | `/restart-service` | Safe service restart with health check before and after |
| Rotate credential | `/rotate-credential` | Guided credential rotation: generate → update services → verify → archive old |

---

## Intelligence Skills

> **Rex — Head of Intelligence.** Competitive analysis, bias audit, war games.

| Skill | Invocation | What it does |
|---|---|---|
| Competitive analysis | `/competitive-analysis` | Research competitor, map positioning, identify gaps and threats |
| War game | `/war-game` | Simulate competitor moves and your counter-moves |

---

## Marketing Skills

> **Maya — Head of Marketing.** Content, brand, campaigns, and distribution.

### Brand & Strategy

| Skill | Invocation | What it does |
|---|---|---|
| Marketing debate | `/marketing-debate` | Multi-persona roundtable on marketing decisions |
| Lookup brand | `/lookup-brand` | Answer brand questions: colors, tone, archetypes, anti-patterns |
| Content ideas | `/content-ideas` | Generate content ideas aligned with ICP, brand voice, and trends |

### Content Creation

| Skill | Invocation | What it does |
|---|---|---|
| Write headline | `/write-headline` | Generate headline + subheadline + hook (4 patterns) |
| Write caption | `/write-caption` | Short caption for Instagram/TikTok + LinkedIn variant |
| LinkedIn post | `/linkedin-post` | Executive LinkedIn format: hook → bullets → data point → CTA |
| Write thread | `/write-thread` | Twitter/Threads thread with reply map |
| YouTube script | `/youtube-script` | Full YouTube script with hook, retention cliffhangers, CTA |
| Email reactivation | `/email-reactivation` | SOAP-format reactivation sequence for cold leads |

### Analysis & Improvement

| Skill | Invocation | What it does |
|---|---|---|
| Analyze post | `/analyze-post` | Diagnose post performance with composite score |
| Improve post | `/improve-post` | Critical revision with ready-to-use copy suggestions |

---

## Skill Count Summary

| Squad | Skills |
|---|---|
| Global | 5 |
| Orchestrator | 4 |
| Commercial | 4 |
| CS | 2 |
| Dev | 8 |
| Finance | 3 |
| Infra | 4 |
| Intelligence | 2 |
| Marketing | 11 |
| **Total** | **43** |

---

## Adding Custom Skills

Place new skill files in the appropriate squad's `skills/` folder:

```bash
squads/<squad-name>/skills/<skill-name>.md
```

Or in `skills/` for global skills available everywhere.

Skill file structure:

```markdown
---
name: my-skill
description: One-line description of what this skill does
---

# /my-skill

## When to use
...

## Inputs
...

## Process
...

## Output format
...
```

After adding, register the skill in the squad's `CLAUDE.md` under `## Skills`.

See [how-to-customize.md](how-to-customize.md) for the full guide.
