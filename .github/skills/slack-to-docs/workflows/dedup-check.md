# Dedup check — open PRs, merged-not-deployed, and on-site overlap

Run this workflow in **Step 4** of [slack-to-docs](../SKILL.md) for **every** target file and theme before drafting.

---

## 1. Fetch PR and branch state

```bash
git fetch origin develop main --tags

# Open PRs targeting develop
gh pr list --state open --base develop --limit 100 \
  --json number,title,headRefName,files,body

# Recently merged PRs (overlap + merge-order context)
gh pr list --state merged --base develop --limit 50 \
  --json number,title,mergedAt,files,body
```

For each candidate open or recently merged PR, inspect overlapping paths:

```bash
gh pr diff <NUMBER> --name-only
```

Flag any PR that touches the **same file** or discusses the **same topic** in the title/body (for example both mention “response messaging”, “131049”, “credits vs sends”).

---

## 2. Merged-not-deployed on `develop`

Content merged to `develop` may not be live on production yet, but it **still counts as documented** for dedup purposes.

**Window:** PRs merged to `develop` after the latest `v.*` release tag, or within the **last 14 days** — whichever captures more overlap.

```bash
# Latest release tag (deploy anchor)
git tag -l 'v.*' --sort=-v:refname | head -1

# Files that differ between main and develop (pending deploy)
git diff origin/main..origin/develop --name-only -- _docs/ _includes/
```

For each target path:

```bash
git show origin/develop:_docs/path/to/file.md   # what is already merged
```

Search `_docs/` and root `_includes/` on the current branch or `develop` for keyword or FAQ overlap using the **Grep** tool (for example `keyword or FAQ question`).

**Rule:** If the topic is already answered on `origin/develop`, do **not** add it again. At most add a cross-link if the canonical home is elsewhere.

---

## 3. Topic-level dedup (not just file paths)

Two PRs can conflict without touching the same file:

| Conflict type | Example (WhatsApp pilot) | Resolution |
|---------------|--------------------------|------------|
| Same FAQ question | “Are response messages free?” in two PRs | One entry only — prefer **main article** if that is the better home; otherwise one FAQ entry |
| Same table in multiple pages | Billing table on FAQ + formats + reporting | **Main article or include** is canonical; FAQ/troubleshooting link in |
| Include vs page | Credits on `reporting.md` vs `campaign_analytics` include | Put shared metrics in **include**; reporting gets one pointer |
| Troubleshooting vs main article | Error 131049 playbook vs FAQ bullet | Playbook on reference or troubleshooting page only if multi-step; short limits/behavior notes stay on main article |
| New page vs expand existing | New `send_failures.md` vs long FAQ | Prefer expanding the main article; dedicated troubleshooting page only for playbook-length content |

Before adding prose, ask: **“Where is the canonical home?”** If unsure, pick one and link from everywhere else.

---

## 4. Search open PR bodies for topic keywords

```bash
gh pr list --state open --base develop --search "whatsapp faq" --json number,title,body
```

Search terms: product name, error code, feature name, UI label, thread author theme.

If an open PR already covers the theme:

- **Defer** your edit until that PR merges, or
- **Coordinate** with the user to add to that branch, or
- **Narrow** your PR to a non-overlapping sub-theme

---

## 5. Record dedup status in the overview

For each theme, mark one of:

| Status | Meaning |
|--------|---------|
| **Clear** | No open or merged overlap |
| **Cross-link only** | Topic exists on develop; add link/anchor only |
| **Deferred** | Open PR #NNNN covers this — wait |
| **Merged** | Already on develop — skip |
| **Split** | Moved to a different PR to avoid file conflict |

---

## 6. Pre-merge reconciliation (when updating open slack-to-docs PRs)

If a related PR merged while yours was open:

1. `git fetch origin develop && git merge origin/develop` (or rebase per team preference)
2. Re-read conflicting files on `develop`
3. **Remove duplicated sections** from your branch; replace with cross-links
4. Update **Related PRs** in the PR body to note reconciliation

This is what kept [#14632](https://github.com/braze-inc/braze-docs/pull/14632) and [#14641](https://github.com/braze-inc/braze-docs/pull/14641) from shipping duplicate credits guidance on `reporting.md`.
