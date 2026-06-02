# OpenRouter MCP — Setup Guide

HIVE ships with 7 multi-model skills that let you query any model on OpenRouter (Kimi, GPT-5, Grok, Gemini, Qwen, DeepSeek, and more) without leaving Claude Code.

---

## How it works

The MCP server (`religa/multi_mcp`) runs locally and exposes 5 tools to Claude Code:

| Tool | What it does |
|---|---|
| `mcp__multi__chat` | Single model query |
| `mcp__multi__codereview` | Code review with chosen model |
| `mcp__multi__compare` | Same prompt to N models in parallel |
| `mcp__multi__debate` | Multi-model consensus with cross-critique |
| `mcp__multi__models` | List available aliases and IDs |

The `.mcp.json` file at the HIVE root wires everything up — Claude Code loads it automatically when you open any HIVE directory.

---

## Setup (5 minutes)

### Step 1 — Get an OpenRouter API key

1. Create a free account at [openrouter.ai](https://openrouter.ai)
2. Go to [Settings → Keys](https://openrouter.ai/settings/keys)
3. Create a key — copy it (`sk-or-...`)
4. Add credits if you want to use paid models (free tier models are available, see `_core/MODELS-MAP.md`)

### Step 2 — Set the env variable

**Mac / Linux — add to `~/.bashrc` or `~/.zshrc`:**
```bash
export OPENROUTER_API_KEY="sk-or-your-key-here"
```
Then reload: `source ~/.bashrc`

**Windows — add to PowerShell profile (`$PROFILE`):**
```powershell
$env:OPENROUTER_API_KEY = "sk-or-your-key-here"
```
Or set it permanently via System → Environment Variables.

### Step 3 — Run the install script

```bash
# Mac / Linux
export OPENROUTER_API_KEY="sk-or-..."
bash _core/mcp/install.sh

# Windows (Git Bash or WSL)
export OPENROUTER_API_KEY="sk-or-..."
bash _core/mcp/install.sh
```

The script:
1. Validates Python 3.11+ and git
2. Clones `religa/multi_mcp` into `~/.local/share/hive/multi_mcp`
3. Creates a virtualenv and installs dependencies
4. Runs a smoke test with Kimi K2.6 (~$0.001)

### Step 4 — Test it

Open Claude Code in your HIVE directory:
```
claude
/second-opinion kimi "what is the capital of France?"
```

You should see Kimi's raw response inside a delimited block.

---

## The 7 multi-model skills

All skills are global — available in every squad context.

| Skill | Invocation | Use when |
|---|---|---|
| Second opinion | `/second-opinion` | You want one model's perspective on a question |
| Consensus | `/consensus` | You want N models on the same question + synthesis |
| Anti-bubble | `/anti-bubble` | You want an outsider to read an asset (no company context) |
| ICP check | `/icp-check` | You want to simulate your ICP reading a piece of copy |
| DoD check | `/dod-check` | You want a cheap model to validate a PR against acceptance criteria |
| Cost compare | `/cost-compare` | You want to find the cheapest model that does the job for a worker |
| Code review model | `/code-review-model` | You want a code review from any OpenRouter model |

All skills:
- Ask which model to use if not passed as argument
- Accept friendly aliases (`kimi`, `gpt5.5`, `grok`) or raw OpenRouter IDs
- Deliver model responses raw (copy-paste, zero editing)
- Apply the reasoning model max_tokens rule automatically (see MODELS-MAP)

---

## Model selection

Skills ask which model to use. Zero defaults — you always choose.

Quick reference for common use cases:

| Use case | Suggested models |
|---|---|
| Code review | `kimi`, `gpt5codex`, `qwencoder` |
| Reasoning / analysis | `gpt5.5`, `grok`, `kimi-think` |
| Marketing / copy feedback | `gemini-pro`, `gpt5.5`, `kimi` |
| Anti-bubble (diverse corpus) | `gemini-pro`, `kimi`, `glm5.1` |
| Cheap workers | `dsflash`, `qwenflash`, `granite` |
| Free tier | `kimi-free`, `dsflash-free`, `qwencoder-free` |

Full catalog with prices, context windows, and benchmarks: `_core/MODELS-MAP.md`

---

## Troubleshooting

**MCP "multi" not showing in Claude Code:**
- Check that `.mcp.json` exists in the HIVE root
- Verify `OPENROUTER_API_KEY` is set: `echo $OPENROUTER_API_KEY`
- Restart Claude Code

**`mcp__multi__chat` returns an error:**
- Check OpenRouter credits: [openrouter.ai/settings/credits](https://openrouter.ai/settings/credits)
- Verify the model ID is valid: `curl -s https://openrouter.ai/api/v1/models | python3 -c "import json,sys; [print(m['id']) for m in json.load(sys.stdin)['data']]" | grep kimi`

**Reasoning model returns empty response:**
- This is the `max_tokens` gotcha — skills handle this automatically with retry
- If it persists, pass `--max-tokens 6000` explicitly

**Re-run install after update:**
```bash
bash _core/mcp/install.sh
```
The script is idempotent — safe to run multiple times.
