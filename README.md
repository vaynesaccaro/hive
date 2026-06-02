# 🐝 HIVE

**Harness for Intelligent Virtual Enterprises**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Built for Claude Code](https://img.shields.io/badge/Built%20for-Claude%20Code-orange)](https://claude.ai/code)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/felipeluissalgueiro/hive/pulls)

> Run your entire company with specialized AI squads — each with its own persona, memory, and skills — orchestrated by an AI Chief of Staff.

---

## The Problem

Most AI adoption looks like this:

| Stage | What it looks like |
|---|---|
| **1 — Using AI** | ChatGPT, prompts, personal productivity |
| **2 — Building with AI** | APIs, automations, one-off workflows |
| **3 — Operating with AI** | Systems with context, memory, and specialized agents |

Stage 3 is where the real leverage is — but building it from scratch takes months. HIVE is the architecture, ready to clone.

---

## What HIVE Is

HIVE is an open-source harness for running a full company with AI agents inside **Claude Code**.

You get 11 specialized squads — each a domain expert AI with its own persona, memory, and decision log — plus an orchestrator (Stamper) that routes, delegates, and tracks everything.

```
You → Stamper → Victor (Sales)
              → Leah (CS)
              → Maya (Marketing)
              → Owen (Product)
              → Clara (Finance)
              → Ethan (Dev)
              → Dean (Infra)
              → Harper (Operations)
              → Nora (Quality)
              → Rex (Intelligence)
```

Every squad has **context** (what it knows), **memory** (what it remembers), and **skills** (what it can do). Nothing is re-explained each session.

---

## Quick Start

```bash
# 1. Clone
git clone https://github.com/felipeluissalgueiro/hive.git my-company
cd my-company

# 2. Install Claude Code (if you haven't)
# Mac / Linux:
curl -fsSL https://claude.ai/install.sh | sh
# Windows:
irm https://claude.ai/install.ps1 | iex

# 3. Open Claude Code and run onboarding
claude
/hive-setup
```

`/hive-setup` asks ~5 minutes of questions and personalizes every squad for your company.

---

## Architecture

```
hive/
  CLAUDE.md                  ← Root orchestrator (Stamper)
  .claude/
    settings.json            ← Hook wiring
    hooks/                   ← 9 automation hooks
  _core/                     ← Framework engine
    lookup.py                ← Knowledge search (incidents + sessions + memory)
    state-aggregator.py      ← L1 aggregation across squads
    harness.sh               ← Worker runner
    memory-schema.md         ← L1/L2/L3 format spec
  squads/
    orchestrator/            ← Stamper (Chief of Staff)
    commercial/              ← Victor (Head of Sales)
    cs/                      ← Leah (Head of CS)
    marketing/               ← Maya (Head of Marketing)
    product/                 ← Owen (Head of Product)
    finance/                 ← Clara (CFO)
    dev/                     ← Ethan (Tech Lead)
    infra/                   ← Dean (Head of Infra)
    operations/              ← Harper (COO)
    quality/                 ← Nora (Head of Quality)
    intelligence/            ← Rex (Head of Intelligence)
  skills/                    ← Global skills (all squads)
  memory/                    ← Global memory
  workers/                   ← Deterministic cron scripts
  incidents/                 ← Incident hub
  sessions-log/              ← Session history
  docs/                      ← Guides and references
```

### Each squad contains

```
squads/commercial/
  CLAUDE.md                  ← Persona, scope, rules, absolute rules
  context/
    squad-context.md         ← Company-specific context (filled via /hive-setup)
  memory/
    STATE.md                 ← Live state: L1 (now) / L2 (in progress) / L3 (backlog)
    decisions.md             ← Architectural decisions log
    gotchas.md               ← Known pitfalls and lessons learned
    MEMORY.md                ← Memory index
  foundation/                ← Reference docs (playbooks, templates, SOPs)
  skills/                    ← Squad-specific skills
  workers/                   ← Background automation scripts
  data/                      ← Squad data files
```

---

## The 11 Squads

| Squad | Persona | Core responsibility |
|---|---|---|
| **Orchestrator** | Stamper — Chief of Staff | Routes, delegates, tracks, aggregates |
| **Commercial** | Victor — Head of Sales | Lead gen, qualification, proposals, pipeline |
| **CS** | Leah — Head of CS | Onboarding, health score, churn prevention |
| **Marketing** | Maya — Head of Marketing | Content, brand, campaigns, ICP alignment |
| **Product** | Owen — Head of Product | Roadmap, stories, sprint, prioritization |
| **Finance** | Clara — CFO | DRE, invoicing, cash flow, budget |
| **Dev** | Ethan — Tech Lead | Architecture, code review, testing, standards |
| **Infra** | Dean — Head of Infra | Servers, monitoring, CI/CD, security |
| **Operations** | Harper — COO | HR, culture, OKRs, SOPs |
| **Quality** | Nora — Head of Quality | Process audits, stranger test, standards |
| **Intelligence** | Rex — Head of Intelligence | Competitive intel, bias audit, war games |

---

## How It Works

### 1. Context loads automatically

When you open any squad folder in Claude Code, `CLAUDE.md` loads its persona, scope, and rules. The squad knows what it's responsible for and what it's not.

### 2. Memory persists across sessions

`STATE.md` follows the L1/L2/L3 schema:
- **L1** — current status (what's happening now)
- **L2** — in progress (active tasks)
- **L3** — backlog (queued, not started)

The orchestrator can aggregate L1 from all squads with `/status`.

### 3. Hooks automate the housekeeping

Five hooks handle the operational plumbing without manual intervention:

| Hook | What it does |
|---|---|
| `PreToolUse` | Creates a `session/YYYY-MM-DD-HHMM` branch on first edit |
| `PostToolUse` | Marks the session dirty when a write tool runs |
| `Stop` | Auto-commits and merges the session branch to `main` (skips files with obvious secrets) |
| `UserPromptSubmit` | Detects squad keywords in the prompt and hints which squad context to load |
| `UserPromptSubmit` | Runs the knowledge lookup before sensitive operations (deploy, DNS, migration…) |

You never manage branches or session state manually.

### 4. Skills are reusable commands

HIVE ships with **50 skills** across all squads. Invoke with `/skill-name`:

```
/hive-setup              ← first-time company onboarding
/open-squad dev          ← load Dev squad context
/close-squad dev         ← update STATE + propagate L1
/status                  ← aggregate L1 from all squads
/log-incident            ← log an incident to the hub
/create-issue            ← guided Linear issue creation
/plan-issue              ← technical plan + approval gate
/start-issue             ← checkout branch + mark In Progress
/close-issue             ← quality cycle + merge + mark Done
/sales-call              ← 7-part Challenger Sale framework
/debug                   ← Pólya 4-phase debug framework
/codex-review            ← P1/P2/P3 code review via Codex CLI
/competitive-analysis    ← research competitor and map threats
```

→ **[Full skills catalog](docs/skills-catalog.md)** — all 50 skills with descriptions, usage guidance, and instructions for adding custom ones.

### 5. Workers run independent of AI

Scripts in `workers/` are plain Python — they write to `STATE.md` and `memory/` with deterministic outputs, no AI in the loop.

`_core/harness.sh` is a **stateless runner**: it executes every registered worker once per invocation. The `schedule` argument in `register_worker` is metadata (used in logs) — actual scheduling is delegated to the OS:

```cron
# Run all HIVE workers every day at 09:00
0 9 * * * bash /path/to/hive/_core/harness.sh

# Or run a single worker on its own schedule
*/30 * * * * bash /path/to/hive/_core/harness.sh workers/health-check.py
```

This keeps the harness simple and lets you use the scheduler you already trust (cron, systemd timers, Windows Task Scheduler).

---

## Usage Examples

**Open a squad and start working:**
```
/open-squad commercial

Victor, I have 3 leads from last week I haven't followed up on.
```

**Get the aggregate company status:**
```
/status
```

**Log an incident:**
```
/log-incident production API down since 14:00
```

**Run the knowledge lookup before a risky operation:**
```python
python _core/lookup.py "deploy vercel production"
```

---

## Project Management

HIVE ships with **Linear** as the default PM tool. Linear is purpose-built for AI-assisted development — issues, cycles, and projects all become part of the agent's context.

Reasons we ship Linear as default:
- Native Claude Code MCP integration
- Issues carry full context (description, acceptance criteria, comments)
- Cycles give squads a temporal frame
- Free tier covers small teams

**Using a different tool?** See [docs/how-to-customize.md](docs/how-to-customize.md) for a switching guide to GitHub Issues, Jira, or no PM tool at all.

---

## Customization

HIVE is designed to be forked and personalized:

- **Rename personas** — Victor, Leah, Maya... are defaults. Rename to whatever fits your culture.
- **Add sub-squads** — got multiple products? Add `squads/product/saas/` and `squads/product/services/`.
- **Write your own foundation docs** — each squad has a `foundation/` folder for your playbooks, templates, and SOPs.
- **Add workers** — drop scripts in `workers/` and add them to `_core/harness.sh` for cron execution.
- **Extend skills** — add squad-specific skills in `squads/<name>/skills/` or global skills in `skills/`.

See [docs/how-to-customize.md](docs/how-to-customize.md) for the full guide.

---

## Multi-Model via OpenRouter (optional)

HIVE ships with 7 skills that let you query **any model** (Kimi, GPT-5, Grok, Gemini, Qwen, DeepSeek, and more) without leaving Claude Code — for second opinions, consensus panels, ICP simulation, anti-bubble checks, and cost/quality comparisons.

**Setup in 3 steps:**

```bash
# 1. Get a key at https://openrouter.ai/settings/keys
export OPENROUTER_API_KEY="sk-or-your-key-here"

# 2. Run the install script (clones multi_mcp, creates venv, smoke test)
bash _core/mcp/install.sh

# 3. Test
claude
/second-opinion kimi "what do you think about this architecture decision?"
```

The `.mcp.json` in the root wires everything up — Claude Code loads the MCP automatically when you open any HIVE directory.

**The 7 multi-model skills:**

| Skill | Use when |
|---|---|
| `/second-opinion` | One model's raw perspective on a question |
| `/consensus` | N models on the same question + overlap/divergence synthesis |
| `/anti-bubble` | Outsider reads an asset without company context |
| `/icp-check` | Simulate your ICP reading a piece of copy |
| `/dod-check` | Cheap model validates a PR against Linear acceptance criteria |
| `/cost-compare` | Find the cheapest model that works for a recurring worker |
| `/code-review-model` | Code review from any OpenRouter model |

All skills ask which model to use — zero defaults. See `_core/MODELS-MAP.md` for the full catalog with prices and benchmarks, and `_core/mcp/README.md` for the full setup guide.

---

## Requirements

- [Claude Code](https://claude.ai/code) — CLI or desktop app
- Git
- Python 3.8+ (for `_core/` scripts)
- **Optional:** Python 3.11+ + OpenRouter API key (for multi-model skills)

No framework dependencies. No npm. No Docker. It's markdown files and Python scripts.

---

## Contributing

1. Fork the repo
2. Create a branch: `git checkout -b feat/your-feature`
3. Make your changes
4. Open a PR — describe what you changed and why

Areas where contributions are most useful:
- Foundation doc templates (SOPs, playbooks, checklists)
- Additional squad skills
- Worker examples for common use cases
- Documentation improvements

---

## License

MIT — free to use, modify, and distribute.

---

Built by [@felipeluissalgueiro](https://github.com/felipeluissalgueiro) · Powered by [Claude Code](https://claude.ai/code)
