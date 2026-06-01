# 🐝 HIVE

**Harness for Intelligent Virtual Enterprises**

> Run your company with AI agents.

HIVE is an open-source framework for operating a full company with specialized AI squads — each with its own persona, memory, and skills — orchestrated by a central AI Chief of Staff.

Built on top of [Claude Code](https://claude.ai/code).

---

## What is HIVE?

Most people are still in Phase 1 or 2 of AI adoption:

| Phase | What it looks like |
|---|---|
| 1 — Use AI at work | ChatGPT, prompts, personal productivity |
| 2 — Build with AI | APIs, no-code tools, one-off automations |
| **3 — Operate with AI** | **Systems with context, memory, and specialized agents that work like a team** |

HIVE is Phase 3. It gives you the architecture to run Commercial, CS, Marketing, Product, Finance, Dev, Infra, Operations, Quality, and Intelligence squads — each as a specialized AI agent with its own context and memory.

---

## Architecture

```
hive/
  CLAUDE.md              ← Orchestrator (your AI Chief of Staff)
  .claude/hooks/         ← automation: session branches, squad routing, memory
  _core/                 ← framework engine: schemas, scripts, conventions
  squads/                ← 11 specialized squads
    orchestrator/
    commercial/
    cs/
    marketing/
    product/
    finance/
    dev/
    infra/
    operations/
    quality/
    intelligence/
  skills/                ← global skills (available to all squads)
  memory/                ← global orchestrator memory
  workers/               ← deterministic cron scripts
  incidents/             ← incident hub
  sessions-log/          ← session history
  docs/                  ← architecture, getting started, how to customize
```

Each squad has:
- `CLAUDE.md` — persona, scope, rules
- `memory/STATE.md` — live operational state (L1/L2/L3)
- `memory/decisions.md` — architectural decisions log
- `memory/gotchas.md` — known pitfalls
- `foundation/` — reference docs for the squad
- `skills/` — squad-specific skills
- `workers/` — background automation scripts

---

## Quick Start

```bash
# 1. Clone
git clone https://github.com/felipeluissalgueiro/hive.git
cd hive

# 2. Install Claude Code
# Mac/Linux:
curl -fsSL https://claude.ai/install.sh | sh
# Windows:
irm https://claude.ai/install.ps1 | iex

# 3. Run onboarding
claude
/hive-setup
```

The `/hive-setup` skill guides you through personalizing HIVE for your company in under 10 minutes.

---

## Squads

| Squad | What it does |
|---|---|
| **Orchestrator** | Chief of Staff — routes, delegates, tracks, remembers |
| **Commercial** | Lead generation, proposals, CRM |
| **CS** | Onboarding, client success, support |
| **Marketing** | Content, campaigns, brand |
| **Product** | Roadmap, stories, development |
| **Finance** | DRE, invoicing, cash flow |
| **Dev** | Code, review, deploy |
| **Infra** | VPS, monitoring, CI/CD |
| **Operations** | HR, culture, goals, processes |
| **Quality** | SOPs, audit, stranger test |
| **Intelligence** | Competitive intel, bias audit, war game |

---

## Project Management

HIVE ships with **Linear** as the default project management tool. Linear is purpose-built for engineering teams and integrates natively with Claude Code — issues, cycles, projects, and comments all become part of the agent's context.

If you prefer another tool (GitHub Issues, Jira, Notion), see `docs/how-to-customize.md`.

---

## How It Works

1. **Context** — each squad has a `CLAUDE.md` that defines its persona, scope, and rules
2. **Memory** — `STATE.md` keeps live operational state; individual memory files persist across sessions
3. **Hooks** — 9 hooks automate session branches, squad routing, and state updates
4. **Skills** — reusable behaviors invoked with `/skill-name`
5. **Workers** — deterministic scripts that run on cron, independent of the AI

---

## Docs

- [Architecture](docs/architecture.md)
- [Getting Started](docs/getting-started.md)
- [How to Customize](docs/how-to-customize.md)

---

## License

MIT — free to use, modify, and distribute.

---

Built by [@felipeluissalgueiro](https://github.com/felipeluissalgueiro) · Powered by Claude Code
