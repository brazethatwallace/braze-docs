#!/usr/bin/env bash
# Exchange PHRASE_TMS_TOKEN (Platform API token) for a short-lived TMS Bearer JWT.
# Usage from repo root:
#   eval "$(scripts/phrase_tms_auth.sh)"
# To sync glossaries from Phrase into scripts/glossaries/*.json, use:
#   python scripts/sync_glossaries_from_phrase.py
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
# shellcheck source=/dev/null
source "$ROOT/.phrase-tms.env"
platform="${PHRASE_PLATFORM_BASE_URL:-https://eu.phrase.com}"
jwt="$(
  curl -fsS -X POST "${platform}/idm/oauth/token" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    --data-urlencode "grant_type=urn:ietf:params:oauth:grant-type:token-exchange" \
    --data-urlencode "subject_token=${PHRASE_TMS_TOKEN}" \
  | python3 -c "import sys, json; print(json.load(sys.stdin)['access_token'])"
)"
printf "export PHRASE_TMS_BEARER=%q\n" "$jwt"
printf "export PHRASE_TMS_BASE_URL=%q\n" "${PHRASE_TMS_BASE_URL:-https://cloud.memsource.com}"
