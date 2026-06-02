# /plan-issue

Break a Linear issue into a concrete technical plan before execution starts.

## Usage

- `/plan-issue PDL-47`

## Steps

1. **Read the issue** in full (title, description, acceptance criteria)
2. **Read foundation context** relevant to the task (tech stack, code principles, branch conventions)
3. **Produce a technical plan:**
   - Summary of what needs to be done (2-3 sentences)
   - File list: every file to create or modify
   - Implementation steps: numbered, concrete, each step = one atomic change
   - Acceptance criteria checklist (derived from issue)
   - Risks or unknowns to resolve before starting
4. **Estimate**: rough time and complexity (S/M/L/XL)
5. **Ask for approval** before execution begins

## Output Format

```
PLAN — [ID]: [title]

Summary:
[What needs to be done, why, what changes]

Files:
- CREATE: path/to/new-file.ts — [purpose]
- MODIFY: path/to/existing.ts — [what changes]

Steps:
1. [Atomic change 1]
2. [Atomic change 2]
...

Acceptance Criteria:
- [ ] [Criteria 1]
- [ ] [Criteria 2]

Risks:
- [Unknown or dependency that could block]

Estimate: [S/M/L/XL] — [rough time]

Proceed with this plan? (yes / adjust / break into sub-issues)
```

## Rules

- Plan is for THIS issue only — do not scope-creep
- File list must be exhaustive — no "and other files as needed"
- Steps must be concrete enough that any agent can execute them
- Risks must be resolved before execution starts (investigate if needed)
