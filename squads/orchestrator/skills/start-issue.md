# /start-issue

Start working on a Linear issue: checkout the correct branch and mark it In Progress.

## Usage

- `/start-issue` — list assigned issues and let you pick
- `/start-issue PDL-47` — go directly to a specific issue

## Prerequisites

- Linear API token: set `LINEAR_API_TOKEN` in `.env` or environment
- Git repo cloned locally

## Steps

1. **Load open issues** assigned to you via Linear API (filter: not completed/cancelled)
2. **Present list** sorted by priority:
   ```
   #  | ID     | Pri    | Title                        | Due
   ---|--------|--------|------------------------------|------
   1  | PDL-47 | URGENT | Fix scheduling duplication   | 18/06
   2  | PDL-11 | HIGH   | Implement qualification flow | 20/06
   ```
3. **User picks** an issue (number or ID)
4. **Check for `repo:` label** on the issue — if missing, block: "Issue not planned yet. Define the target repo before starting."
5. **Checkout branch** (use `issue.branchName` from Linear API):
   ```bash
   git fetch origin
   git checkout <branchName> || git checkout -b <branchName> origin/main
   ```
6. **Mark In Progress** via Linear API mutation
7. **Post comment** on the issue: started timestamp, branch, executor
8. **Confirm** to user:
   ```
   Ready — [ID]: [title]
   Branch: [branchName]
   Status: In Progress
   ```

## Rules

- NEVER create a new branch if it already exists on remote
- NEVER start if repo label is `repo:pending`
- Branch name comes from Linear (`issue.branchName`) — don't invent it

## Linear API

```python
import subprocess, json, os

TOKEN = os.environ.get("LINEAR_API_TOKEN")

def linear_query(query):
    r = subprocess.run(
        ["curl", "-s", "-X", "POST", "https://api.linear.app/graphql",
         "-H", f"Authorization: {TOKEN}",
         "-H", "Content-Type: application/json",
         "-d", json.dumps({"query": query})],
        capture_output=True
    )
    return json.loads(r.stdout)
```
