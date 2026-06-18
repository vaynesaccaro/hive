# /document

Generate or update technical documentation after a feature ships. Prevents the gap between what was built and what is recorded.

## When to use

At the end of any non-trivial feature — before merging to main. Also use when existing documentation is found to be out of date.

## Inputs

- Feature description or diff to document
- List of files changed (or the git diff)
- Any known edge cases or operational quirks

## Steps / Framework

### Step 1 — Read the diff or feature description
Understand what was actually built — not what was planned. Documentation must reflect what the code does, not what it was supposed to do.

### Step 2 — Generate or update three documentation artifacts

**Artifact 1 — Inline docs (component-level)**
Markdown file in the repository co-located with the code. Covers:
- What this component does
- Inputs and outputs (with types)
- Non-obvious decisions and why they were made
- Known limitations

**Artifact 2 — Wiki entry**
An HTML or Markdown page for the project wiki summarizing:
- Feature name and purpose
- How it works (user-facing and technical view)
- Dependencies and configuration
- Screenshots or diagrams if applicable

**Artifact 3 — Playbook entry (operational runbook)**
How to operate this in production. Covers:
- How to verify it's working (health check)
- How to debug the most common failure modes
- How to roll back if it needs to be reverted
- Who to contact if it breaks at 2am

### Step 3 — Verify alignment between documentation and code
Cross-check each claim in the documentation against the actual code. Flag any statement that describes intended behavior rather than actual behavior.

### Step 4 — Flag undocumented edge cases
List any edge case or failure path that exists in the code but is not covered in the documentation. These are documentation debt.

---

## Output

```
DOCUMENTATION REPORT — [feature] — [date]

Files created/updated:
- [path]: [inline docs / wiki / playbook]
- [path]: [inline docs / wiki / playbook]

Verification: [all claims match code / N discrepancies found]

Undocumented edge cases:
- [edge case 1]
- [edge case 2]
```

## Rules

> "Documentation that describes what the code *should* do, not what it *does*, is worse than no documentation."

- Never document intended behavior. Only document actual behavior.
- Playbook must include a rollback procedure. A runbook without rollback is incomplete.
- If you cannot verify a claim against the code, mark it as `[UNVERIFIED — needs review]`.
- Documentation is not done until all three artifacts exist.
