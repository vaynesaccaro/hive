# Branch Convention

## Base Branch
- **Main branch:** `main`
- Direct commits to `main`: **not allowed** (protected)
- All changes go via PR

---

## Naming Rules

### Format
```
<type>/<short-description>
```
Use lowercase, hyphens, no spaces.

### Types

| Prefix | Use For |
|--------|---------|
| `feat/` | New feature or user-facing capability |
| `fix/` | Bug fix |
| `chore/` | Tooling, config, deps, CI, non-functional changes |
| `refactor/` | Code restructure with no behavior change |
| `docs/` | Documentation only |
| `test/` | Adding or fixing tests |
| `hotfix/` | Urgent production fix (branches from `main`) |

### Examples
```
feat/user-onboarding-flow
fix/auth-token-expiry-loop
chore/upgrade-typescript-5
refactor/move-utils-to-shared
hotfix/payment-timeout-crash
```

### Ticket reference (optional but recommended)
```
feat/pdl-42-user-onboarding-flow
fix/pdl-87-auth-token-expiry
```

---

## Merge Strategy
- **Default:** Squash merge into `main` — keeps history linear
- **Exception:** Merge commit for releases or long-lived feature branches (keep all commits)
- Delete branch after merge: **yes**

---

## Long-Lived Branches
| Branch | Purpose |
|--------|---------|
| `main` | Production-ready code |
| `develop` _(if used)_ | Integration branch for pre-release |

Avoid long-lived feature branches. If a branch lives > 5 days, split the work.

---

## Stale Branches
- Branches with no activity > 30 days: reviewed and deleted
- Owner: Engineering Lead
