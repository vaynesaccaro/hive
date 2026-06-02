# Deploy Checklist

---

## Pre-Deploy Gates
- [ ] All CI checks passing (tests, lint, build)
- [ ] PR reviewed and approved
- [ ] No open blocking issues related to this deploy
- [ ] Migrations reviewed — reversible or have rollback plan
- [ ] Feature flags configured (if applicable)
- [ ] Staging deploy completed and smoke-tested
- [ ] Notify team in #deployments channel: what, when, who

---

## Deploy Steps

### Backend / Workers
1. [ ] SSH to VPS or trigger deploy pipeline
2. [ ] Pull latest: `git pull origin main`
3. [ ] Install/update deps: _e.g. `pip install -r requirements.txt`_
4. [ ] Run migrations (if any): _e.g. `python manage.py migrate`_
5. [ ] Restart service: _e.g. `systemctl restart <service>` or `pm2 reload all`_
6. [ ] Verify process is running: `systemctl status <service>`

### Frontend
1. [ ] Trigger Vercel / CDN deploy (auto on push to main, or manual)
2. [ ] Confirm build succeeds in CI/CD dashboard
3. [ ] Preview URL spot-checked

---

## Post-Deploy Validation
- [ ] Core user flows working (manual or automated smoke test)
- [ ] No spike in error rate (check logs / APM)
- [ ] No spike in latency (check metrics)
- [ ] New feature / fix confirmed working in production
- [ ] Migrations applied correctly (spot-check data)
- [ ] Announce deploy complete in #deployments

---

## Rollback Trigger
Initiate rollback if ANY of the following:
- Error rate > **_X%_** baseline within 15 minutes
- P0 bug reported by user or monitoring
- Data integrity issue detected
- Service health check failing

### Rollback Steps
1. Revert via `git revert` + re-deploy, OR redeploy previous release tag
2. Roll back migration if applied: _e.g. `python manage.py migrate <app> <prev>`_
3. Notify team and open incident (see incident-response.md)

---

## Owner: ___  |  Last reviewed: ___
