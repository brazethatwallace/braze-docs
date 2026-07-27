# How the Support analyzer (Looker) workflow operates

**Audience:** Docs and adjacent teams (internal).  
**Workflow file:** [`.github/workflows/export-support-cases-from-looker.yml`](workflows/export-support-cases-from-looker.yml)  
**Cursor skill (manual triage):** `.github/skills/support-analyzer/SKILL.md`

On a fixed cadence (and on demand), a GitHub Actions workflow exports recent **Braze Support** cases from **Looker** into this repo, builds an **internal digest** (themes and counts only), then may open **draft** pull requests that propose small, **allowlisted** edits to English customer docs in `_docs`. Case bodies stay off GitHub’s public PR pages where we can avoid it; PRs link to **Salesforce** case views instead.

The Looker saved report behind the export is scoped to a **rolling ~3-day** window of cases, so the schedule is **twice weekly** rather than nightly.

---

## The sequence

**~7:00 AM Eastern, Tuesday and Friday:** The **Support analyzer (Looker)** workflow runs (two `cron` entries with `timezone: America/New_York`).

1. **`export`** — Checks out **`support-analyzer-data`**, runs `scripts/export_support_cases_from_looker.py` with Looker API credentials, writes **`_data/support_cases_latest.csv`** (redacts common credential patterns in case text before write), and pushes to **`origin/support-analyzer-data`**. If the CSV is unchanged from the last commit, this job does not create a new commit.

2. **`digest_and_pr`** — Checks out the default branch checkout for that job, fetches the CSV from **`support-analyzer-data`**, runs `scripts/support_analyzer_weekly_digest.py`, uploads the digest markdown as workflow artifact **`support-analyzer-weekly-digest`**, and opens a **draft** digest PR to **`develop`** (branch pattern `support-analyzer/weekly-digest-<run_id>`, title like **`[SA] Weekly support cases digest — YYYY-MM-DD`**, label **`support analyzer`**). The digest PR body includes a short **stakeholder blurb** explaining automation. **This PR does not change customer-facing docs**—only `.github/support_analyzer_weekly_digest.md`.

3. **`phase2_doc_prs`** — Unless **`workflow_dispatch`** was started with **Skip Phase 2** checked, checks out **`github.ref`** (scheduled runs: repo default branch, usually **`develop`**; manual runs: the branch you selected so the Phase 2 script exists), fetches the same CSV, runs **`scripts/support_analyzer_phase2.py`** with **`--strict-anchors`** against [`.github/support_analyzer_phase2_rules.yml`](support_analyzer_phase2_rules.yml). For each **enabled** rule that matches enough cases and has real edits to apply, it pushes a branch `support-analyzer/phase2-<rule_id>-<YYYY-MM-DD>-<run_id>` (Eastern date + run id) and opens a **draft** PR to **`develop`**, unless an **open** draft for that rule already exists (same branch prefix) or every edit is skipped on **`develop`** (`fingerprint`, `skip_if_contains`, or `skip_if_contains_in_files`). PR bodies start with the same kind of **stakeholder blurb**, then rule metadata, Salesforce case links (up to 50), optional rule notes, and verification guidance. **Assignees** are resolved from [`.github/support_analyzer_doc_assignees.csv`](support_analyzer_doc_assignees.csv) (longest matching **Page Path** prefix → **GitHub Username**). A verification markdown file is uploaded when present as artifact **`support-analyzer-phase2-verification`**.

4. **`close_digest_pr`** — If a digest PR was opened **and** Phase 2 **succeeded**, closes that digest PR with **`gh pr close --delete-branch`** and leaves a short comment pointing readers at the **digest artifact** on the workflow run. The digest markdown remains in Actions artifacts even after the PR is closed.

5. **`notify`** — Posts to **#docs_request** in Slack (Docs PR Bot) when `SLACK_BOT_TOKEN` and `SLACK_DOCS_REQUEST_CHANNEL` are set. Failures include the failed job name(s) and a link to the workflow run. When Phase 2 opens draft PRs, the message lists each PR and pings assignees (GitHub usernames from the assignees map, resolved to Slack `<@U…>` when possible).

**Typical writer flow:** You do **not** need to merge the digest PR for the pipeline to finish—it auto-closes after Phase 2. You **do** review and merge (or close) each **Phase 2** draft doc PR on its merits after validating product behavior and style.

---

## Writer and maintainer responsibilities

**When you’re tagged on a Phase 2 PR**

- Read the **stakeholder blurb** at the top: the change is **automated** from Support themes, not a human-authored spec.
- Use **Salesforce** links in the PR to inspect cases if needed; **do not** paste consumer PII into GitHub comments.
- Confirm wording against **product behavior** before merge. For **public**-facing PR descriptions, use **Verified against Braze source code.** and do **not** paste internal `platform` or SDK file paths (see `.github/skills/reference-repos/SKILL.md`).
- If the assignee is wrong, fix the row in **`.github/support_analyzer_doc_assignees.csv`** (or the upstream spreadsheet export) in a follow-up PR.

**When you’re tagged on the digest PR**

- Use it as a **triage aid** (keyword themes). It will usually **auto-close** after Phase 2; the canonical copy for that run is the **artifact** if you need it after close.

**Keeping the ownership map current**

- **`.github/support_analyzer_doc_assignees.csv`** should stay aligned with the team’s **Docs – Page Paths / ownership** spreadsheet.
- **Monthly sync:** GitHub Actions workflow **Doc ownership sync (monthly)** (`.github/workflows/sync-doc-ownership.yml`) runs on the **first weekday** of each month at **9:00 America/New_York** (and on demand). It scans eligible `_docs/` paths on `develop`, updates the spreadsheet **Page Paths** tab, regenerates the CSV, and opens a draft PR when the CSV changes. Path rules live in `scripts/doc_ownership_sync_config.yml`.
- **Manual override:** You can still re-export CSV from the sheet and replace the file in a PR if needed.
- **Two assignees for one path:** put **comma-separated GitHub logins** in the **GitHub Username** cell (quoted in CSV if needed), for example `"lydia-xie,zairro"`. Multiple spreadsheet rows for the same path also combine when they share the longest matching prefix length.

---

## Possible tasks

### Triggering a manual run

1. In **braze-docs**, go to **Actions** → **Support analyzer (Looker)**.
2. Click **Run workflow**.
3. Choose the branch (usually **`develop`** for production-like behavior; use a **feature branch** only when testing workflow or script changes not yet on `develop`).
4. Optionally set **Skip Phase 2** to `true` if you only want **export + digest** (no draft doc PRs).

Scheduled runs use the repo **default branch** for Phase 2 checkout; manual runs use the **selected branch** so `scripts/support_analyzer_phase2.py` does not need to exist on `develop` before your PR merges.

### Running pieces locally (optional)

**Export** (requires Looker credentials in the environment—do not commit secrets):

```bash
pip install requests pyyaml ripgrep
export LOOKER_CLIENT_ID=...
export LOOKER_CLIENT_SECRET=...
# optional: export LOOKER_SUPPORT_CASES_QUERY_ID=...
export SUPPORT_ANALYZER_OUTPUT=_data/support_cases_latest.csv
export SUPPORT_ANALYZER_EXPORT_ACKNOWLEDGE_SENSITIVE_DATA=1
python scripts/export_support_cases_from_looker.py
```

**Digest** (path to CSV can be a local copy):

```bash
python scripts/support_analyzer_weekly_digest.py /path/to/support_cases_latest.csv .github/support_analyzer_weekly_digest.md
```

**Phase 2** (dry run—no branch/PR):

```bash
python scripts/support_analyzer_phase2.py /path/to/support_cases_latest.csv \
  --rules .github/support_analyzer_phase2_rules.yml \
  --assignees-map .github/support_analyzer_doc_assignees.csv \
  --root . \
  --dry-run
```

Omit **`--dry-run`** only when you intend to create branches and PRs (`GH_TOKEN` / `gh` auth required).

---

## Key paths and branches

| Item | Location |
|------|----------|
| Workflow | `.github/workflows/export-support-cases-from-looker.yml` |
| Phase 2 rules | `.github/support_analyzer_phase2_rules.yml` |
| Doc → assignee map | `.github/support_analyzer_doc_assignees.csv` |
| Exported CSV on branch | `support-analyzer-data` → `_data/support_cases_latest.csv` |
| Digest output (in PR / artifact) | `.github/support_analyzer_weekly_digest.md` |
| Phase 2 script | `scripts/support_analyzer_phase2.py` |
| Export script | `scripts/export_support_cases_from_looker.py` |
| Digest script | `scripts/support_analyzer_weekly_digest.py` |

---

## Secrets and variables

| Name | Type | Purpose |
|------|------|---------|
| `LOOKER_CLIENT_ID` | Secret | Looker API |
| `LOOKER_CLIENT_SECRET` | Secret | Looker API |
| `LOOKER_SUPPORT_CASES_QUERY_ID` | Variable (optional) | Saved Look / query id override |

Export fails closed without **`SUPPORT_ANALYZER_EXPORT_ACKNOWLEDGE_SENSITIVE_DATA=1`** in the workflow env (acknowledges CSV may contain PII).

---

## Quick reference

| Task | Where / command |
|------|-------------------|
| Manual workflow run | Actions → **Support analyzer (Looker)** → **Run workflow** |
| Export + digest only | Manual run with **Skip Phase 2** = `true` |
| Download digest without opening merged PR | Workflow run → **support-analyzer-weekly-digest** artifact |
| Download Phase 2 verification log | Workflow run → **support-analyzer-phase2-verification** artifact |
| Change schedule or copy | Edit workflow `on.schedule` / PR `body` in `.github/workflows/export-support-cases-from-looker.yml` |
| Add or change automated doc proposals | Edit `.github/support_analyzer_phase2_rules.yml` |
| Change who gets assigned | Edit `.github/support_analyzer_doc_assignees.csv` |

---

## Troubleshooting

| Symptom | What to check |
|---------|----------------|
| **Export** fails | Looker secrets, query id variable, network; Actions log for `export_support_cases_from_looker.py`. |
| **Export** push rejected (GH013) | Case text contained a credential GitHub push protection blocked. The export job runs `scripts/export_support_cases_from_looker.py` from the **workflow ref** (`develop` on schedule), not from `support-analyzer-data` (that branch is CSV-only). Redaction covers AWS keys, SendGrid `SG.…` keys, Twilio `AC…`/`SK…` SIDs, GitHub/Slack/Stripe tokens—re-run after merging script/workflow fixes. Check the log for `Redacted N embedded credential-like value(s)`; do not unblock secrets in GitHub unless you intend to store them on the data branch. |
| **Digest** fails with empty CSV | Branch **`support-analyzer-data`** missing or empty file; ensure `export` succeeded. |
| **Phase 2** fails “script not found” | For scheduled runs, `support_analyzer_phase2.py` must exist on **default branch**; merge the script before relying on schedule-only. |
| **Phase 2** fails strict anchors | Target `_docs` file missing anchor text on `develop`; fix anchor or rule in a PR, or adjust rule. |
| **No Phase 2 PRs** opened | Normal if no rule matches enough cases or edits are already present (fingerprints / `skip_if_contains` / anchors). |
| **Duplicate-looking Phase 2 PR** | Earlier PR merged equivalent prose without `<!-- support-analyzer-phase2:... -->` fingerprint; automation re-proposes. Close the duplicate, merge only missing files, or add `skip_if_contains` to the rule (see #13773 / #13823, #13772 / #13914). For `data_series_currents`, merged include `api/export_data_series_analytics_dashboard_note.md` satisfies the rule. |
| **`gh pr create` assignee errors** | Script retries **without** assignees; fix invalid **GitHub Username** values in the CSV (e.g. team placeholders that are not user logins). |
| **Digest PR not auto-closed** | `close_digest_pr` only runs if digest PR was created **and** Phase 2 job **succeeded**; check Phase 2 job and permissions. |
| **Close digest failed with 403** | Job needs **`contents: write`** and **`pull-requests: write`** for `gh pr close --delete-branch` (already set in workflow). |

---

## Data and privacy

- Treat the Support CSV and case narratives as **sensitive**. Limit who can read **`support-analyzer-data`** and the Looker query scope.
- Automated PR bodies should use **Salesforce case links**, not pasted email bodies or PII.

For product verification in Cursor, follow the **reference-repos** skill (`.github/skills/reference-repos/SKILL.md`) layout and policies; the Looker workflow **does not** clone `Appboy/platform` in CI—optional `verification` blocks in rules run **ripgrep** only when a local checkout exists.
