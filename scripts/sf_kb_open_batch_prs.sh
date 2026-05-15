#!/usr/bin/env bash
# Open Salesforce KB multi-article batch PRs from stashes (run from repo root).
# Each PR body includes **product vertical ownership** for reviewer routing; see
# `_data/kb_articles_actioned.md` → *Product vertical ownership (multi-article batches)* to
# fill in or correct owners when TBD.
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

git fetch origin develop
git checkout develop
git pull origin develop

STASH_GTM="stash@{0}"
STASH_REST="stash@{1}"

# Product vertical strings: align with `product_vertical_hint()` in `scripts/generate_kb_phase1_outputs.py`
# and the ownership table in `_data/kb_articles_actioned.md` (section 1).

# Markdown fragment: product vertical for batched PRs (align with kb_articles_actioned.md table).
pr_ownership_block() {
  local vertical="$1"
  printf '%s\n' \
    "### Product vertical ownership" \
    "" \
    "**${vertical}**" \
    "" \
    "Route this batched PR for review under that product vertical. If the suggestion is wrong or unknown, set **Product owner** for this primary doc in [\`_data/kb_articles_actioned.md\`](_data/kb_articles_actioned.md#product-vertical-ownership-multi-article-batches) (table *Product vertical ownership*)." \
    ""
}

make_pr() {
  local branch="$1" relpath="$2" stashref="$3" summary="$4" pr_title="$5" product_vertical="$6" body="$7"

  git checkout develop
  git pull origin develop
  if git show-ref --verify --quiet "refs/heads/$branch"; then
    git branch -D "$branch"
  fi
  git checkout -b "$branch"
  git checkout "$stashref" -- "$relpath"
  {
    pr_ownership_block "$product_vertical"
    printf '%s\n' "$body"
  } > /tmp/sf_kb_pr_body.md
  git add "$relpath"
  git commit -m "$summary"
  git push -u origin "$branch"
  gh pr create --base develop --title "$pr_title" --label "salesforce migration" --body-file /tmp/sf_kb_pr_body.md
}

MAKE_JIRA="${MAKE_JIRA:-1}"

# 1 GTM
make_pr "sf-cursor-kb-batch-gtm" "_docs/_developer_guide/sdk_integration/google_tag_manager.md" "$STASH_GTM" \
  "Add GTM troubleshooting for SF KB batch" \
  "Salesforce KB: Google Tag Manager initialization and logging" \
  "SDK & developer integrations" \
"### Why are you making this change? (required)

Adds troubleshooting for Google Tag Manager with the Braze SDK (initialization and verbose logging guidance) from Salesforce Knowledge migration articles.

### Salesforce Knowledge articles

- \`ka0VP000000O4iPYAS\` — Google Tag Manager (GTM) Braze Initialisation Failed
- \`ka0VP000000OmhpYAC\` — How to Enable Verbose Logging in Google Tag Manager (GTM)

### Related PRs, issues, or features (optional)

- Phase 2 multi-article batch: \`_docs/_developer_guide/sdk_integration/google_tag_manager.md\`

### Contributor checklist

- [x] Style and links reviewed."

# 2 Partners home
make_pr "sf-cursor-kb-batch-partners-home" "_docs/_partners/home.md" "$STASH_REST" \
  "Document Technology Partners credential and status troubleshooting" \
  "Salesforce KB: Technology Partners invalid credentials and dashboard status" \
  "Partners & integrations" \
"### Why are you making this change? (required)

Clarifies reconnect steps when Braze shows invalid credentials and how Braze Technology Partners status relates to external dashboards.

### Salesforce Knowledge articles

- \`ka0VP000000HmxtYAC\` — Why is it showing Invalid credentials from mParticle Current integration?
- \`ka0VP000000QhvlYAC\` — Deliverability Dashboard shows Google Postmaster as Connected, Technology Partners records it as Pending

### Contributor checklist

- [x] Style and links reviewed."

# 3 Segment analytics
make_pr "sf-cursor-kb-batch-segment-analytics" "_docs/_user_guide/analytics/tracking/segment_analytics_tracking.md" "$STASH_REST" \
  "Add segment analytics tracking FAQs for SF KB" \
  "Salesforce KB: Segment analytics tracking historical data and troubleshooting" \
  "Analytics" \
"### Why are you making this change? (required)

Documents that segment analytics revenue charts are not historical before tracking was enabled and common checks when data looks wrong.

### Salesforce Knowledge articles

- \`ka0VP000000BT0HYAW\` — Does Segment Analytics Tracking Display Historical Data on Revenue Dashboard?
- \`ka0VP000000JUQbYAO\` — Segment Analytics Tracking Not Working

### Contributor checklist

- [x] Style and links reviewed."

# 4 Action paths
make_pr "sf-cursor-kb-batch-action-paths" "_docs/_user_guide/messaging/canvas/canvas_components/action_paths.md" "$STASH_REST" \
  "Document Add an email address trigger for Action Paths" \
  "Salesforce KB: Action Paths Add an email address trigger" \
  "Canvas (Email channel triggers — confirm Email vs Canvas PM if needed)" \
"### Why are you making this change? (required)

Explains how the Add an email address action group trigger behaves during the evaluation window.

### Salesforce Knowledge articles

- \`ka0VP000000JVo5YAG\` — Action Paths when Ranking is off - what is the expected behaviour?
- \`ka0VP000000JtonYAC\` — How does the Add an Email Address trigger work?

### Contributor checklist

- [x] Style and links reviewed."

# 5 Experiment paths
make_pr "sf-cursor-kb-batch-experiment-paths" "_docs/_user_guide/messaging/canvas/canvas_components/experiment_step.md" "$STASH_REST" \
  "Add Experiment Path FAQ for sends and conversion window" \
  "Salesforce KB: Experiment Path sends vs split and conversion window" \
  "Canvas" \
"### Why are you making this change? (required)

Clarifies why downstream sends can differ across paths and how the experiment conversion window is measured.

### Salesforce Knowledge articles

- \`ka0VP000000HF7VYAW\` — My Experiment Path is entering users into Content Card steps equally, why is there a discrepancy in Sends?
- \`ka0VP000000TG1NYAW\` — Experiment Path Canvas Step Window

### Contributor checklist

- [x] Style and links reviewed."

# 6 Canvas troubleshooting
make_pr "sf-cursor-kb-batch-canvas-action-triggers" "_docs/_user_guide/messaging/canvas/troubleshooting.md" "$STASH_REST" \
  "Add Canvas troubleshooting for action-based custom events" \
  "Salesforce KB: Canvas action-based triggers and custom event properties" \
  "Canvas" \
"### Why are you making this change? (required)

Adds guidance for action-based steps when custom event properties or timestamps do not match trigger filters.

### Salesforce Knowledge articles

- \`ka0VP000000So3VYAS\` — Action Based Campaigns/Canvases Using Custom Event Properties as Trigger Not Sending
- \`ka0VP000000TYzBYAW\` — Action-Based Delivery Campaign Not Sending (Check Custom Event Timestamp)

### Contributor checklist

- [x] Style and links reviewed."

git checkout develop
echo "Done. Return to develop."
