#!/usr/bin/env bash
# Load Jira REST credentials for local SF KB scripts.
# Usage from repo root:
#   source scripts/jira_env.sh
if [[ -n "${BASH_VERSION:-}" ]]; then
  _SELF="${BASH_SOURCE[0]}"
else
  _SELF="$0"
fi
ROOT="$(cd "$(dirname "$_SELF")/.." && pwd)" || return 1 2>/dev/null || exit 1
ENV_FILE="$ROOT/.jira.env"
if [[ ! -f "$ENV_FILE" ]]; then
  echo "Missing $ENV_FILE — copy .jira.env.example to .jira.env and add JIRA_API_TOKEN." >&2
  return 1 2>/dev/null || exit 1
fi
# shellcheck source=/dev/null
set -a
# shellcheck source=/dev/null
source "$ENV_FILE" || {
  set +a
  return 1 2>/dev/null || exit 1
}
set +a
if [[ -z "${JIRA_USER_EMAIL:-}" || -z "${JIRA_API_TOKEN:-}" ]]; then
  echo "Set JIRA_USER_EMAIL and JIRA_API_TOKEN in $ENV_FILE." >&2
  return 1 2>/dev/null || exit 1
fi
unset _SELF
