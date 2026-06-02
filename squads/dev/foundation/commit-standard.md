# Commit Standard

We follow [Conventional Commits](https://www.conventionalcommits.org/).

---

## Format
```
<type>(<scope>): <short summary>

[optional body]

[optional footer: BREAKING CHANGE, closes #issue]
```

- **Summary:** imperative mood, lowercase, no period, max 72 chars
- **Body:** explain _why_, not _what_; wrap at 72 chars
- **Footer:** reference issues (`Closes #42`) or breaking changes

---

## Types

| Type | Use For |
|------|---------|
| `feat` | New feature (triggers minor version bump) |
| `fix` | Bug fix (triggers patch version bump) |
| `chore` | Tooling, deps, CI, non-functional |
| `refactor` | Code change — no new behavior, no bug fix |
| `docs` | Documentation only |
| `test` | Add or fix tests |
| `perf` | Performance improvement |
| `style` | Formatting — no logic change |
| `revert` | Reverts a previous commit |
| `ci` | CI/CD pipeline changes |

---

## Scopes (Examples)
Define scopes relevant to your project:
- `auth`, `api`, `db`, `ui`, `infra`, `billing`, `notifications`

---

## Examples

### Simple
```
feat(auth): add magic link login

fix(api): return 404 instead of 500 on missing resource

chore(deps): upgrade zod to 3.22
```

### With body
```
refactor(db): extract query helpers to shared module

Queries were duplicated across 3 services. Centralized in
db/helpers.ts to reduce drift and make testing easier.
```

### Breaking change
```
feat(api)!: remove deprecated v1 endpoints

BREAKING CHANGE: /api/v1/* routes removed. Migrate to /api/v2/*.
Closes #134
```

---

## Rules
- One logical change per commit — don't batch unrelated changes
- Don't commit commented-out code
- Don't commit debug logs or console.log left from development
- CI will lint commit messages on PR — fix before merging
