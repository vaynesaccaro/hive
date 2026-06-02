---
name: dod-check
description: "Automated Definition of Done validation — a cheap model reads the current diff + Linear issue acceptance criteria and returns a pass/partial/fail verdict with justification."
---

# /dod-check

A cheap model (default suggestion: `dsflash`, `qwenflash`, or `flashlite`) compares the current diff with the acceptance criteria and returns a structured verdict. Costs cents per PR. Doesn't replace human validation on critical PRs, but filters 80% of routine cases.

## Arguments

- `[model]` — optional. Cheap alias (`dsflash`, `qwenflash`, `flashlite`, `glm-flash`, `granite`). Default suggestion (asked): `dsflash` ($0.10/$0.20 — near-free, 1M ctx).
- `[issue]` — optional. Linear issue ID (e.g. `PROJ-42`). Default: tries to extract from current branch name (`feat/proj-42-...`).
- `[base-branch]` — optional. Default `main`.

## Flow

1. **Resolve model:**
   - If passed → resolve alias
   - If not → `AskUserQuestion` with top 4 cheap + "Other":
     1. `dsflash` (DeepSeek V4 Flash — near-free, 1M ctx)
     2. `qwenflash` (Qwen 3.6 Flash — 1M ctx)
     3. `flashlite` (Gemini 3.1 Flash Lite)
     4. `glm-flash` (GLM 4.7 Flash)

2. **Resolve Linear issue:**
   - If passed → use it
   - If not → extract from `$(git branch --show-current)` (pattern `feat/proj-XX-...`)
   - Failed → ask user

3. **Fetch acceptance criteria from Linear:**
   - Via `mcp__claude_ai_Linear__get_issue` with resolved ID
   - Extract "Acceptance Criteria:" or "Definition of Done:" or "DoD:" section from description
   - No criteria in issue → notify user and stop (can't validate without explicit criteria)

4. **Collect diff:**
   ```bash
   git diff <base-branch>...HEAD
   git log <base-branch>..HEAD --oneline
   ```

5. **Build prompt:**
   ```
   You are validating whether a code delivery meets the defined acceptance criteria.
   Original acceptance criteria for the issue:
   <CRITERIA>

   Delivery diff:
   <DIFF>

   For EACH item in the criteria, respond in the format:
   - [✅ meets | ⚠️ partial | ❌ does not meet] <criteria item> — <evidence in diff or absence>

   At the end:
   VERDICT: <READY TO MERGE | MINOR ADJUSTMENTS | REDO>
   SUGGESTED ACTIONS (if not ready): <short list>
   ```

6. **Call `mcp__multi__chat`** with chosen model.

7. **Render response:**
   ```
   🎯 DoD Check — <model-id>
   Issue: <ID> — <title>
   Branch: <current> vs <base-branch>
   Estimated cost: ~$<X>
   ───────────────────────────────────────────────

   <raw model response, copy-paste>
   ───────────────────────────────────────────────

   ### Summary

   **Model verdict:** <READY/ADJUSTMENTS/REDO>
   **Confidence:** <high/medium/low> (based on how many criteria were met)
   **Suggested next step:**
   - Ready → merge to main (after senior/lead approval)
   - Adjustments → comment on PR + fix
   - Redo → reopen issue, review scope
   ```

## Absolute rules

1. **Model response always raw** — copy-paste without editing
2. **NEVER auto-approve** — model only recommends, human decides
3. **No acceptance criteria in issue → SKILL FAILS** (can't validate without explicit criteria; tell user to refine the issue first)
4. **Cost always shown** — user sees how much each DoD check costs
5. **Does NOT modify Linear issue or merge code** — report only

## Prerequisites

- Inside a git repo
- MCP `multi` active
- MCP Linear (`mcp__claude_ai_Linear__*`) active
- Linear issue with defined acceptance criteria

## Examples

```
/dod-check
→ asks for model + extracts issue from branch

/dod-check dsflash
→ DeepSeek Flash + extracts issue

/dod-check qwenflash PROJ-123
→ Qwen Flash, specific issue

/dod-check granite PROJ-123 develop
→ Granite, specific issue, base branch develop
```

## Refs

- `_core/MODELS-MAP.md` — "Fast / cheap" tier
- `mcp__multi__chat` — MCP tool
- `mcp__claude_ai_Linear__get_issue` — fetch issue
