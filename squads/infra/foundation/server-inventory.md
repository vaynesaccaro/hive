# Server Inventory

_Last updated: ___  |  Owner: ____

---

## Servers

| Name | IP / Host | Role | OS | Services Running | SSH Key | Backup | Status |
|------|----------|------|----|-----------------|---------|--------|--------|
| _prod-master_ | _x.x.x.x_ | _Production workers + orchestrator_ | _Ubuntu 22.04_ | _Docker, workers, Coolify_ | _~/.ssh/prod_master_ | ✅ Daily | 🟢 |
| _prod-app_ | _x.x.x.x_ | _App server (API + web)_ | _Ubuntu 22.04_ | _Nginx, Node.js / Python_ | _~/.ssh/prod_app_ | ✅ Daily | 🟢 |
| _dev_ | _x.x.x.x_ | _Development / staging_ | _Ubuntu 22.04_ | _Docker, test services_ | _~/.ssh/dev_ | ⚠️ Manual | 🟡 |
| _db-primary_ | _x.x.x.x_ | _Primary database_ | _Ubuntu 22.04_ | _PostgreSQL 15_ | _~/.ssh/db_ | ✅ Hourly | 🟢 |

---

## Managed Services (Non-VPS)

| Service | Provider | Region | Purpose | Dashboard |
|---------|----------|--------|---------|-----------|
| _e.g. PostgreSQL_ | _Supabase_ | _us-east-1_ | _Main app DB_ | _[link]_ |
| _e.g. Redis cache_ | _Upstash_ | _us-east-1_ | _Job queue + cache_ | _[link]_ |
| _e.g. Object storage_ | _Cloudflare R2_ | _Global_ | _File uploads_ | _[link]_ |
| _e.g. CDN + DNS_ | _Cloudflare_ | _Global_ | _Edge + protection_ | _[link]_ |

---

## Backup Policy

| Asset | Frequency | Retention | Method | Last Verified |
|-------|-----------|-----------|--------|--------------|
| _PostgreSQL DB_ | _Daily_ | _30 days_ | _Supabase PITR_ | _[date]_ |
| _App server config_ | _Weekly_ | _4 versions_ | _Git + rsync_ | _[date]_ |
| _User uploads_ | _Daily_ | _90 days_ | _R2 versioning_ | _[date]_ |

---

## Notes
- Credentials stored in 1Password — vault: `infrastructure`
- SSH config file: `~/.ssh/config`
- Alert if any server offline > 5 min: _[monitoring tool / URL]_
