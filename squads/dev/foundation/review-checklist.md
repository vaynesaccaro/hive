# Code Review Checklist

Use during PR review. Check each item before approving.

---

## Logic & Correctness
- [ ] Does the code do what the story/ticket says it should do?
- [ ] Are edge cases handled (null, empty, concurrent, large inputs)?
- [ ] Are error paths explicit — no silent failures?
- [ ] Does it introduce or fix any race conditions?

## Security
- [ ] No secrets, tokens, or credentials in code or logs
- [ ] Inputs are validated before use (especially user-controlled data)
- [ ] No SQL injection, XSS, or SSRF vectors introduced
- [ ] Authorization checks present — not just authentication
- [ ] Third-party deps added? Any known vulnerabilities? (`npm audit` / `pip-audit`)

## Tests
- [ ] New behavior has test coverage
- [ ] Tests test behavior, not implementation details
- [ ] Tests pass locally and in CI
- [ ] No tests deleted without explanation

## Performance
- [ ] No N+1 queries introduced
- [ ] No unnecessary blocking calls in hot paths
- [ ] Large data sets handled with pagination or streaming

## Code Quality
- [ ] Follows code-principles.md (clarity, no premature abstraction, etc.)
- [ ] No dead code left behind
- [ ] Names are clear — functions, variables, files
- [ ] No commented-out code committed

## Documentation & Observability
- [ ] Public APIs and complex logic have comments explaining _why_
- [ ] Relevant docs updated (README, ADR, API reference)
- [ ] New errors are loggable and diagnosable
- [ ] Analytics / tracking events added if required by story

---

## Reviewer Etiquette
- Distinguish blockers from suggestions: prefix with `[blocking]` or `[nit]`
- Approve if you'd be comfortable maintaining this code
- If uncertain, ask — don't guess intent from code
