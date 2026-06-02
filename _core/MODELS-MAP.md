# MODELS-MAP — OpenRouter Model Catalog

> Source of truth for skills that call models via the OpenRouter MCP.
> **Zero defaults, zero prescription.** Skills always ask which model to use.
> Last updated: 2026-05-31

## How to use

**In skills:** always ask the model via `AskUserQuestion` if not passed as argument. Accepts 3 formats:

1. **Friendly alias** (e.g. `kimi`, `gpt5.5`, `grok`) — resolved against the table below
2. **Raw OpenRouter ID** (e.g. `moonshotai/kimi-k2.6`, `openai/gpt-5.4-pro`)
3. **OpenRouter auto-update aliases** (e.g. `~google/gemini-pro-latest`) — always points to latest version

**Example invocations:**
```
/second-opinion                          # asks for model
/second-opinion kimi "my question"       # alias
/second-opinion moonshotai/kimi-k2.6 "..." # raw ID
/consensus [kimi,gpt5.5,grok] "..."      # list
```

---

## 💻 Coding (ranked by LiveCodeBench v6 / SWE-Bench Pro — May 2026)

| Alias | OpenRouter ID | Ctx | $/M in | $/M out | Benchmark |
|---|---|---|---|---|---|
| `kimi` | `moonshotai/kimi-k2.6` | 256k | $0.68 | $3.42 | **#1 LiveCodeBench v6: 89.6%** · SWE-Pro leader |
| `kimi-think` | `moonshotai/kimi-k2-thinking` | 256k | $0.60 | $2.50 | Reasoning + coding combined |
| `gpt5codex` | `openai/gpt-5.3-codex` | 400k | $1.75 | $14.00 | OpenAI dedicated coding model |
| `gpt5codex-max` | `openai/gpt-5.1-codex-max` | 400k | $1.25 | $10.00 | Codex large variant |
| `qwencoder` | `qwen/qwen3-coder-plus` | 1M | $0.65 | $3.25 | 87.1% LiveCodeBench v6 |
| `qwencoder-next` | `qwen/qwen3-coder-next` | 256k | $0.11 | $0.80 | Efficient per active param |
| `glm5.1` | `z-ai/glm-5.1` | 200k | $0.98 | $3.08 | **#1 web dev open** (1534 Elo) |
| `codestral` | `mistralai/codestral-2508` | 256k | $0.30 | $0.90 | European coding, low cost |

## 🧠 Reasoning / Flagship

| Alias | OpenRouter ID | Ctx | $/M in | $/M out | Benchmark |
|---|---|---|---|---|---|
| `gpt5.5` | `openai/gpt-5.5` | 1M | $5.00 | $30.00 | **82.7% Terminal-Bench 2.0** (top agentic) |
| `gpt5.4` | `openai/gpt-5.4` | 1M | $2.50 | $15.00 | **#1 BenchLM weighted: 73.9** |
| `grok` | `x-ai/grok-4.20` | **2M** | $1.25 | $2.50 | Largest viable ctx + low cost |
| `minimax` | `minimax/minimax-m2.7` | 200k | $0.26 | $1.20 | MiniMax reasoning tier |
| `qwen-max` | `qwen/qwen3.7-max` | 1M | $1.25 | $3.75 | Top Qwen flagship |
| `qwen-think` | `qwen/qwen3-max-thinking` | 256k | $0.78 | $3.90 | Qwen with chain-of-thought |

## ⚡ Fast / cheap (recurring workers, atomic tasks)

| Alias | OpenRouter ID | Ctx | $/M in | $/M out |
|---|---|---|---|---|
| `dsflash` | `deepseek/deepseek-v4-flash` | 1M | $0.10 | $0.20 |
| `qwenflash` | `qwen/qwen3.6-flash` | 1M | $0.19 | $1.13 |
| `flashlite` | `google/gemini-3.1-flash-lite` | 1M | $0.25 | $1.50 |
| `glm-flash` | `z-ai/glm-4.7-flash` | 200k | $0.06 | $0.40 |
| `granite` | `ibm-granite/granite-4.1-8b` | 128k | $0.05 | $0.10 |
| `gpt5.4-nano` | `openai/gpt-5.4-nano` | 400k | $0.20 | $1.25 |

## 🌍 Long context / multimodal

| Alias | OpenRouter ID | Ctx | $/M in | $/M out |
|---|---|---|---|---|
| `gemini-pro` | `~google/gemini-pro-latest` | 1M | $2.00 | $12.00 |
| `gemini-flash` | `~google/gemini-flash-latest` | 1M | $1.50 | $9.00 |
| `gpt5image` | `openai/gpt-5.4-image-2` | 272k | $8.00 | $15.00 |

## 🆓 Free tier (rate-limited)

| Alias | OpenRouter ID | Ctx |
|---|---|---|
| `kimi-free` | `moonshotai/kimi-k2.6:free` | 256k |
| `qwencoder-free` | `qwen/qwen3-coder:free` | 1M |
| `dsflash-free` | `deepseek/deepseek-v4-flash:free` | 1M |

---

## ⚠️ Gotcha — Reasoning models and `max_tokens`

**Reasoning models spend many tokens on internal "thinking" before responding.** If `max_tokens` is too low, the model finishes with `finish: length` and NO visible answer (all tokens consumed by chain-of-thought).

**Rule for skills:**
- **General default:** `max_tokens: 2000`
- **Reasoning models:** `max_tokens: 4000`
- **Always allow user override**

**How to detect reasoning model** (heuristic for skills):
- Name contains `thinking`, `reasoning`, `-r1`, `-o3`, `-o4`
- Family `gpt-5.*` (all 5.1+ variants are reasoning)
- `moonshotai/kimi-k2.6` (no suffix — reasoning by default)
- `moonshotai/kimi-k2-thinking` (explicit)
- `qwen/qwen3-max-thinking` (explicit)
- `deepseek/deepseek-r1*`

**Non-reasoning models (max_tokens 1000 is enough):**
- Family `google/gemini-*-flash*`
- `qwen/qwen3.6-flash`, `qwen/qwen3-coder-plus`
- `deepseek/deepseek-v4-flash`
- `mistralai/codestral-*`
- `ibm-granite/granite-*`
- `z-ai/glm-4.*-flash`

---

## Updating prices / benchmarks

Prices on OpenRouter change. Verify via API before assuming:
```bash
curl -s https://openrouter.ai/api/v1/models | python3 -c "
import json, sys
data = json.load(sys.stdin)
for m in data['data']:
    if m['id'] == 'moonshotai/kimi-k2.6':
        print(m['pricing'])
"
```

To add a new model:
1. Confirm ID via `curl -s https://openrouter.ai/api/v1/models | python3 -c "import json,sys; [print(m['id']) for m in json.load(sys.stdin)['data']]"`
2. Define a short unique alias
3. Add a row in the correct tier with ctx/price/benchmark
4. Commit

---

## Refs

- OpenRouter models: `https://openrouter.ai/api/v1/models`
- LiveCodeBench v6: https://llm-stats.com/benchmarks/livecodebench-v6
- BenchLM ranking: https://benchlm.ai/blog/posts/best-llm-coding
- SWE-Bench: https://www.swebench.com/
