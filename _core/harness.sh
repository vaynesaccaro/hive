#!/usr/bin/env bash
# HIVE Worker Harness
# Runs deterministic worker scripts on a schedule.
# No AI in the loop — workers are pure Python, predictable outputs.
#
# Usage:
#   bash _core/harness.sh                  # run all registered workers
#   bash _core/harness.sh workers/my.py    # run specific worker
#   crontab -e  →  0 9 * * * bash /path/to/hive/_core/harness.sh
#
# Worker contract:
#   - Exit 0 on success, non-zero on failure
#   - Write state updates to squads/<name>/memory/STATE.md only
#   - Never modify CLAUDE.md, skills/, foundation/, or _core/
#   - Log to stdout/stderr — harness captures and routes

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LOG_DIR="$REPO_ROOT/sessions-log/workers"
PYTHON="${PYTHON:-python3}"

mkdir -p "$LOG_DIR"

# ─── Worker registry ──────────────────────────────────────────────
# Format: run_worker <script> <schedule>
# Schedules: "always" | "daily:HH:MM" | "every:Nh" | "every:Nm"
#
# Add your workers here:
# run_worker "workers/daily-summary.py"       "daily:09:00"
# run_worker "workers/health-check.py"        "every:1h"
# run_worker "workers/competitor-scan.py"     "daily:08:00"

REGISTERED_WORKERS=()

register_worker() {
    REGISTERED_WORKERS+=("$1|$2")
}

# Register workers below. The schedule string is metadata for logs — actual
# scheduling is delegated to cron / systemd / Task Scheduler (see README §5).
register_worker "workers/example.py" "daily:09:00"

# ─── Harness logic ────────────────────────────────────────────────

run_worker() {
    local script="$1"
    local schedule="$2"
    local script_path="$REPO_ROOT/$script"
    local log_file="$LOG_DIR/$(basename "$script" .py)-$(date +%Y%m%d).log"

    if [[ ! -f "$script_path" ]]; then
        echo "[harness] SKIP $script — file not found" >&2
        return 0
    fi

    echo "[harness] RUN $script (schedule: $schedule)"
    if "$PYTHON" "$script_path" >> "$log_file" 2>&1; then
        echo "[harness] OK  $script"
    else
        echo "[harness] ERR $script — check $log_file" >&2
    fi
}

# Run specific worker if passed as argument
if [[ $# -gt 0 ]]; then
    run_worker "$1" "manual"
    exit 0
fi

# Run all registered workers
if [[ ${#REGISTERED_WORKERS[@]} -eq 0 ]]; then
    echo "[harness] No workers registered. Add them to _core/harness.sh."
    exit 0
fi

for entry in "${REGISTERED_WORKERS[@]}"; do
    script="${entry%%|*}"
    schedule="${entry##*|}"
    run_worker "$script" "$schedule"
done

echo "[harness] Done — $(date)"
