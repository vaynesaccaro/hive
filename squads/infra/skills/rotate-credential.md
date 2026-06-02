# /rotate-credential

Safely rotate an API key, secret, or password. Test the new credential before revoking the old one.

## When to use

- Scheduled rotation (every 90 days for sensitive keys)
- After a suspected or confirmed credential leak
- When an employee who had access departs
- After a security audit finding
- Before decommissioning an environment that has active credentials

## Inputs

- `credential_name`: human-readable name of the credential (e.g., "Stripe API Key — production")
- `service`: the service or platform where this credential lives
- `reason`: why rotation is being triggered

## Steps / Framework

### Step 1 — Identify all consumers
Before touching anything: find every place this credential is used.

Search for:
- Environment variables referencing this service
- Config files (`.env`, `config.yaml`, `secrets.yaml`)
- CI/CD pipeline variables
- Other services that call the service using this credential
- Deployed workers or cron jobs

Document the complete list. Do not proceed if you cannot identify all consumers — a partial rotation is worse than no rotation.

### Step 2 — Generate new credential
In the target service (platform dashboard or API), generate a new key/secret/password.

Do not replace the old one yet. Both must coexist temporarily.

### Step 3 — Store new credential in secrets manager
Save the new credential in your secrets manager (e.g., 1Password, AWS Secrets Manager, Vault) **before** deploying it anywhere.

Format: same naming convention as the old credential, with rotation date noted.

### Step 4 — Update all identified consumers
For each consumer identified in Step 1:
- Update the environment variable or config to use the new credential
- Restart or redeploy the consumer if required for the change to take effect

### Step 5 — Test new credential in production
Verify the new credential works in every consumer before revoking the old one:
- Trigger a real request or operation that uses the credential
- Confirm success in logs

Do not skip this step. Revoking before testing creates an outage.

### Step 6 — Revoke old credential
Once all consumers are confirmed working with the new credential:
- Revoke or delete the old credential in the target service
- Remove it from secrets manager
- Confirm revocation (attempt a request with the old credential — it should fail with 401/403)

### Step 7 — Log the rotation

```
CREDENTIAL ROTATION LOG — [date]

Credential type: [e.g., "API key for payment service"]  ← NEVER the actual value
Service: [service name]
Reason: [reason]
Consumers updated: [list]
Rotated by: [agent / person]
Old credential: revoked ✅
New credential: active ✅
```

Append this entry to `memory/decisions.md`.

## Rules

- **NEVER log the actual credential value anywhere.** Not in memory, not in decisions.md, not in a commit, not in a log file.
- **Never revoke the old credential before testing the new one.** In that order, always.
- **Never rotate without completing Step 1.** A partial rotation that misses one consumer creates a hidden failure.
- If you cannot access the target service to generate a new credential, stop and ask for help — do not improvise.
