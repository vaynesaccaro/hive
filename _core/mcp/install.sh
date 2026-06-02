#!/usr/bin/env bash
# install.sh — Set up the OpenRouter MCP for HIVE
# Idempotent: safe to run multiple times.
#
# Does:
#   1. Validates deps (python 3.11+, git)
#   2. Clones/updates religa/multi_mcp into ~/.local/share/hive/multi_mcp
#   3. Creates virtualenv and installs deps via uv (pip fallback)
#   4. Verifies OPENROUTER_API_KEY is set in env
#   5. Smoke test: calls Kimi K2.6 via API (~$0.001)
#
# Usage: bash _core/mcp/install.sh
#
# Before running, set OPENROUTER_API_KEY in your environment:
#   export OPENROUTER_API_KEY="sk-or-..."
#
# Get a key at: https://openrouter.ai/settings/keys
# After running, open Claude Code in any HIVE directory and the "multi" MCP
# loads automatically via .mcp.json in the root.

set -euo pipefail

MCP_DIR="${HOME}/.local/share/hive/multi_mcp"
# Pinned commit of religa/multi_mcp — bump deliberately after auditing upstream changes.
# Do not change without reviewing the diff at:
#   https://github.com/religa/multi_mcp/compare/<old>...<new>
MCP_PIN="6a69e55f3ede0d6505d09e5d3b64873076c7c05c"

ok()   { echo -e "\033[32m✓\033[0m $*"; }
warn() { echo -e "\033[33m⚠\033[0m $*"; }
err()  { echo -e "\033[31m✗\033[0m $*" >&2; }
step() { echo -e "\n\033[1;36m▸\033[0m \033[1m$*\033[0m"; }

# ── 1. Deps ──
step "1/5 — Checking dependencies"
for cmd in python3 git curl; do
  if command -v "$cmd" >/dev/null 2>&1; then
    ok "$cmd found: $(command -v $cmd)"
  else
    err "$cmd not found — install it first"
    exit 1
  fi
done
PYVER=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
if python3 -c 'import sys; sys.exit(0 if sys.version_info >= (3,11) else 1)'; then
  ok "Python $PYVER (>=3.11 OK)"
else
  err "Python $PYVER — multi_mcp requires >=3.11"
  exit 1
fi

# ── 2. Check API key ──
step "2/5 — Checking OPENROUTER_API_KEY"
if [[ -z "${OPENROUTER_API_KEY:-}" ]]; then
  err "OPENROUTER_API_KEY is not set"
  err ""
  err "Set it before running this script:"
  err "  export OPENROUTER_API_KEY=\"sk-or-...\""
  err ""
  err "Get a key at: https://openrouter.ai/settings/keys"
  err ""
  err "To persist across sessions, add it to your shell profile:"
  err "  echo 'export OPENROUTER_API_KEY=\"sk-or-...\"' >> ~/.bashrc"
  exit 1
fi
ok "OPENROUTER_API_KEY is set (len=${#OPENROUTER_API_KEY})"

# ── 3. Clone/update multi_mcp ──
step "3/5 — multi_mcp in $MCP_DIR"
mkdir -p "$(dirname "$MCP_DIR")"
if [[ -d "$MCP_DIR/.git" ]]; then
  ok "Already cloned, fetching pinned commit"
  git -C "$MCP_DIR" fetch --quiet origin
else
  ok "Cloning religa/multi_mcp"
  git clone --quiet https://github.com/religa/multi_mcp.git "$MCP_DIR"
fi
ok "Checking out pinned commit $MCP_PIN"
git -C "$MCP_DIR" checkout --quiet "$MCP_PIN" || {
  err "Pinned commit $MCP_PIN not found in religa/multi_mcp"
  err "Upstream may have force-pushed. Audit before bumping MCP_PIN in this script."
  exit 1
}

# ── 4. Venv + deps ──
step "4/5 — Virtualenv + Python deps"
cd "$MCP_DIR"
if command -v uv >/dev/null 2>&1; then
  ok "Using uv (fast)"
  uv venv --quiet 2>/dev/null || true
  uv pip install -q --upgrade pip
  uv pip install -q -e .
else
  warn "uv not found, using python -m venv (slower)"
  python3 -m venv .venv
  ./.venv/bin/pip install -q --upgrade pip
  ./.venv/bin/pip install -q -e .
fi
[[ -x "$MCP_DIR/.venv/bin/python" ]] || { err "venv was not created"; exit 1; }
ok "Venv ready: $MCP_DIR/.venv/bin/python"

# ── 5. Smoke test ──
step "5/5 — Smoke test (Kimi K2.6, ~\$0.001)"
# Pass the API key via stdin config so it never appears in `ps` output
RESP=$(curl -s -K - https://openrouter.ai/api/v1/chat/completions <<EOF
header = "Authorization: Bearer $OPENROUTER_API_KEY"
header = "Content-Type: application/json"
data = "{\"model\":\"moonshotai/kimi-k2.6\",\"messages\":[{\"role\":\"user\",\"content\":\"Reply only the word: pong\"}],\"max_tokens\":10}"
EOF
)
ANSWER=$(echo "$RESP" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('choices',[{}])[0].get('message',{}).get('content') or d.get('error',{}).get('message','null'))")
if [[ "$ANSWER" =~ pong ]]; then
  ok "Smoke test PASSED — Kimi replied: $ANSWER"
elif [[ "$ANSWER" == *"Insufficient credits"* ]]; then
  warn "No OpenRouter credits — add at https://openrouter.ai/settings/credits"
  warn "Setup is otherwise complete."
else
  warn "Unexpected response: $ANSWER"
  warn "Raw: $RESP"
  warn "Setup may still work — check your API key and credits."
fi

step "✅ Setup complete"
cat <<EOF

Next steps:
  1. Open a NEW shell (so OPENROUTER_API_KEY is loaded if you added it to .bashrc)
  2. Open Claude Code inside your HIVE directory
  3. The "multi" MCP loads automatically via .mcp.json
  4. Test: /second-opinion kimi "what is the capital of France?"

Available MCP tools:
  - chat        (single model query)
  - codereview  (code review with chosen model)
  - compare     (same prompt to N models in parallel)
  - debate      (multi-model consensus with cross-critique)
  - models      (list aliases and IDs)

HIVE multi-model skills:
  /second-opinion  /code-review-model  /consensus
  /icp-check       /dod-check          /cost-compare  /anti-bubble

Model catalog: _core/MODELS-MAP.md
Full guide:    _core/mcp/README.md
EOF
