# /hardening-check

Periodic server hardening audit based on CIS Benchmarks (Ubuntu 24.04). Identifies security gaps and optionally applies fixes.

## Syntax

```
/hardening-check              # dry-run (report only, no changes)
/hardening-check --apply      # apply fixes (confirms each item before applying)
```

## Inputs

- `host`: target server hostname or IP (use `<VPS_HOST>` placeholder in documentation)
- `user`: SSH user with sudo access (use `<VPS_USER>` placeholder in documentation)

## Checklist

### SSH Configuration
- [ ] `PermitRootLogin = no`
- [ ] `PasswordAuthentication = no`
- [ ] `PubkeyAuthentication = yes`
- [ ] `MaxAuthTries ≤ 3`
- [ ] `AllowUsers` = only explicitly authorized users listed

### UFW Firewall
- [ ] Status = active
- [ ] Default incoming = deny
- [ ] Default outgoing = allow
- [ ] Port 22 = allow only from whitelisted IPs (not from ANY)
- [ ] Port 80/443 = allow (reverse proxy)
- [ ] No other ports open to ANY

### User Accounts
- [ ] Only expected users have a bash shell
- [ ] sudo group contains only authorized admin users
- [ ] No accounts without a password
- [ ] Root has never logged in directly (check `last root`)

### Exposed Services
- [ ] Database ports (5432 / 6379 / 27017) = listening on localhost only
- [ ] Docker daemon (2375/2376) = NOT exposed externally
- [ ] Only expected ports appear in `ss -tlnp` output

### System Updates
- [ ] `unattended-upgrades` service is active and running
- [ ] Fewer than 5 security updates pending (`apt list --upgradable`)
- [ ] No reboot required for a pending kernel update

### Logs and Disk
- [ ] `logrotate` configuration is valid
- [ ] Fewer than 50 failed SSH attempts in the last 24 hours (`journalctl -u ssh`)
- [ ] `/var/log` directory is under 2GB
- [ ] No repeated CRITICAL or ERROR entries in `dmesg` output

---

## Scoring

| Result | Threshold | Meaning |
|---|---|---|
| ✅ PASS | ≥ 90% of checks pass | Approved baseline |
| ⚠️ WARN | Up to 5 warnings, 0 failures | Monitor — plan remediation |
| ❌ FAIL | Any FAIL check | Block — remediate before proceeding |

---

## Output format (dry-run)

```
HARDENING CHECK — [host] — [date]

SSH
  ✅ PermitRootLogin = no
  ✅ PasswordAuthentication = no
  ❌ MaxAuthTries = 6 (should be ≤ 3)
  ...

FIREWALL
  ✅ UFW active
  ⚠️  Port 22 open to ANY (should be restricted to known IPs)
  ...

[...all sections...]

SCORE: XX / YY checks passed ([X]%)
STATUS: [PASS / WARN / FAIL]

RECOMMENDED FIXES:
1. Set MaxAuthTries 3 in /etc/ssh/sshd_config → sudo systemctl restart ssh
2. Restrict port 22: ufw delete allow 22; ufw allow from <your-ip> to any port 22
```

## Rules

- Dry-run mode makes no changes to the server. It only reads and reports.
- `--apply` mode confirms each fix individually before applying. Never batch-applies without confirmation.
- NEVER restart the SSH daemon (`sshd`) as a fix — this would lock you out. Flag the issue and provide manual instructions.
- After any `--apply` run, re-run dry-run to verify the fixes were applied correctly.
