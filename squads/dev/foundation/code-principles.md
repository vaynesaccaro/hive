# Code Principles

Core rules that govern how we write and review code. Short list — if everything is a principle, nothing is.

---

## 1. Clarity Over Cleverness
Write code that the next engineer can read and understand without asking you. If it needs a comment to explain _what_ it does (not _why_), simplify it.

## 2. No Premature Abstraction
Don't abstract until you have the third use case. Duplication is cheaper than wrong abstraction. When the pattern is clear, refactor.

## 3. Test at Boundaries
Test the contract between systems, not implementation details. Unit tests for pure logic; integration tests for I/O and APIs; avoid mocking what you don't own.

## 4. Fail Loudly and Early
Validate inputs at the entry point. Throw/return errors immediately — don't let bad data travel deep into the stack. Avoid silent failures.

## 5. Small, Focused Functions
Each function does one thing. If you need "and" to describe it, split it. Max function length: _e.g. 40 lines_ (guideline, not hard rule).

## 6. Data In, Data Out
Prefer pure functions. Isolate side effects (DB writes, external calls, mutations) to the edges. Core business logic should be testable without I/O.

## 7. Leave It Better Than You Found It
If you touch a file, fix one piece of nearby tech debt (a missing type, a misleading name, a dead import). Don't refactor the entire module — just leave it incrementally better.

## 8. Configuration Over Hardcoding
Strings, thresholds, and flags that change per environment belong in config, not in code. No magic numbers without a named constant.

---

## What These Are Not
- Style rules → enforced by linter/formatter (see `.eslintrc`, `pyproject.toml`)
- PR process → see review-checklist.md
- Branch rules → see branch-convention.md
