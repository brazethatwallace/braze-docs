#!/usr/bin/env bash
# Dispatch Auto-translate for several batch files one after another (same repo
# concurrency group). After each `gh workflow run`, waits for that run to
# finish before starting the next — avoids GitHub cancelling queued dispatches
# when multiple `workflow_dispatch` events are submitted back-to-back.
#
# Usage (from repo root):
#   ./scripts/translation_catchup/dispatch_batches_sequential.sh \
#     scripts/translation_catchup/generated/batches/phase_a_includes_batch_002.txt \
#     scripts/translation_catchup/generated/batches/phase_b_user_guide__root_batch_003.txt
#
# Env: REPO (default braze-inc/braze-docs), REF (default develop), SKIP_ORPHAN
#      (default true, forwarded to dispatch_batch.sh).

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

REPO="${REPO:-braze-inc/braze-docs}"

if [[ $# -lt 1 ]]; then
  echo "usage: $0 <batch.txt> [batch.txt ...]" >&2
  exit 1
fi

for BATCH_FILE in "$@"; do
  echo ""
  echo "======== $(date -u +%Y-%m-%dT%H:%M:%SZ) dispatch: $BATCH_FILE ========"
  BEFORE="$(gh run list --workflow=auto-translate.yml --repo "$REPO" --limit 1 --json databaseId --jq '.[0].databaseId')"

  SKIP_ORPHAN="${SKIP_ORPHAN:-true}" ./scripts/translation_catchup/dispatch_batch.sh "$BATCH_FILE"

  AFTER="$(gh run list --workflow=auto-translate.yml --repo "$REPO" --limit 1 --json databaseId --jq '.[0].databaseId')"
  RUN_ID="$AFTER"
  if [[ -n "${BEFORE:-}" && "$BEFORE" == "$AFTER" ]]; then
    echo "warning: run id unchanged; waiting 5s and re-polling" >&2
    sleep 5
    RUN_ID="$(gh run list --workflow=auto-translate.yml --repo "$REPO" --limit 1 --json databaseId --jq '.[0].databaseId')"
  fi

  echo "Watching run $RUN_ID …"
  gh run watch "$RUN_ID" --repo "$REPO" --exit-status
  echo "Run $RUN_ID finished."
done

echo ""
echo "All $# batch file(s) completed."
