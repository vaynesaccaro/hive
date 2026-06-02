# /restart-service

Safely restart a service on a remote server, with pre/post health verification.

## When to use

When a service needs to be restarted due to a crash, configuration change, memory leak, or deployment. Not for initial starts or first deployments.

## Inputs

- `service_name`: name of the systemd service to restart
- `host`: target server (SSH address)
- `reason`: why the restart is being triggered (for audit log)

## Steps / Framework

### Step 1 — Check against the ALLOWLIST

Before proceeding, verify `service_name` is in the appropriate category:

**Safe to restart without extra confirmation (ALLOWLIST):**
- `nginx`
- `caddy`
- Application services (non-database workers, API servers, background jobs)

**Requires explicit confirmation before restarting (data services):**
- `postgresql` / `postgres`
- `redis` / `redis-server`
- `kafka`
- `elasticsearch`
- Any service with "db" or "data" in the name

**NEVER restart under any circumstances:**
- `sshd` / `ssh` — restarting the SSH daemon on a remote server risks locking yourself out permanently

If the service is not on the ALLOWLIST, ask for explicit confirmation before proceeding.

### Step 2 — Check service status before restart
```bash
ssh <VPS_USER>@<VPS_HOST> "systemctl status <service_name>"
```
Record: was it running? Any recent errors in the status output?

### Step 3 — Restart the service
```bash
ssh <VPS_USER>@<VPS_HOST> "systemctl restart <service_name>"
```

### Step 4 — Verify service came back up
Check status with 3 retries × 5 seconds between each:
```bash
ssh <VPS_USER>@<VPS_HOST> "systemctl is-active <service_name>"
```
If not active after 3 retries: escalate — do not attempt a second restart without investigation.

### Step 5 — Check application logs for errors
```bash
ssh <VPS_USER>@<VPS_HOST> "journalctl -u <service_name> -n 50 --no-pager"
```
Flag any ERROR, CRITICAL, or traceback lines.

### Step 6 — Report

```
RESTART REPORT — [service_name] — [date]

Host: [host]
Reason: [reason]

Before: [running / stopped / failed]
After: [running / stopped / failed]

Log errors found: [yes / no]
[if yes: paste relevant lines]

Status: [OK / NEEDS ATTENTION]
```

## Rules

- Log every restart in `memory/decisions.md` with service, host, reason, and outcome.
- Never restart a data service (postgres, redis) without first checking that there is no active write operation (look for long-running queries or pending transactions).
- If the service does not come back up after 3 retries, stop and escalate. Do not loop.
- If the restart was triggered by a deployment: always run the health check for the application after verifying the service is active.
