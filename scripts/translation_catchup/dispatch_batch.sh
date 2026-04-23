#!/usr/bin/env bash
# Dispatch Auto-translate for one batch file (one path per line).
# Usage: ./scripts/translation_catchup/dispatch_batch.sh path/to/batch.txt
# Env: REPO (default braze-inc/braze-docs), REF (default develop),
#      SKIP_ORPHAN (default true → pass skip_orphan_cleanup=true)

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

BATCH_FILE="${1:?usage: $0 <batch.txt>}"
if [[ ! -f "$BATCH_FILE" ]]; then
  echo "error: not a file: $BATCH_FILE" >&2
  exit 1
fi

REPO="${REPO:-braze-inc/braze-docs}"
REF="${REF:-develop}"
SKIP_ORPHAN="${SKIP_ORPHAN:-true}"

lines=()
while IFS= read -r raw || [[ -n "${raw}" ]]; do
  line=$(printf '%s\n' "$raw" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
  [[ -z "$line" || "$line" == \#* ]] && continue
  lines+=("$line")
done < "$BATCH_FILE"

if [[ ${#lines[@]} -eq 0 ]]; then
  echo "error: no usable paths in $BATCH_FILE (empty, whitespace-only, or comment-only)" >&2
  exit 1
fi

files=$(printf '%s ' "${lines[@]}")
files="${files%% }"

echo "Dispatching ${#lines[@]} file(s) to workflow on $REPO@$REF (skip_orphan_cleanup=$SKIP_ORPHAN)"

gh workflow run auto-translate.yml \
  --repo "$REPO" \
  --ref "$REF" \
  -f "files=$files" \
  -f "skip_orphan_cleanup=$SKIP_ORPHAN"

echo "Queued. Recent runs:"
gh run list --workflow=auto-translate.yml --repo "$REPO" --limit 3
