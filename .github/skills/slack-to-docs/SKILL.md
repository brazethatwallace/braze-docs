---
name: slack-to-docs
description: >
  Mines SME or support Slack channels for documentation gaps, verifies behavior against
  source code, deduplicates against open and pending PRs, and opens manageable draft PRs
  with Slack thread citations. Use when pointed at a Slack channel (for example
  #whatsapp-sme-global), mining vertical SME threads for docs updates, or reproducing
  the WhatsApp Slack-to-PR workflow.
allowed-tools: Bash(git *), Bash(gh *), Read, Grep, CallMcpTool
---

# Slack channel → documentation PRs

Turn recurring SME or support Slack threads into **source-verified**, **public-safe** documentation updates. Each run starts from a **channel the user names**, produces an **overview plan**, then opens **one draft PR per vertical/theme** at a manageable size.

Inspired by the [#whatsapp-sme-global](https://braze.enterprise.slack.com/archives/C08CYL6KN1K) pilot ([internal thread](https://brazetechnology.slack.com/archives/G01LQQX3MGU/p1784158880961049)). Reference merged examples: [PR #14632](https://github.com/braze-inc/braze-docs/pull/14632), [PR #14641](https://github.com/braze-inc/braze-docs/pull/14641).

## Context

- Current branch: !`git branch --show-current`
- Open PRs to `develop`: !`gh pr list --state open --base develop --limit 15 --json number,title 2>/dev/null || echo "none"`

## Prerequisites

| Requirement | Why |
|-------------|-----|
| **Slack MCP** in your agent environment | Search channels and read threads. Tool names differ by host (for example Cursor MCP Bundle vs Claude Code Slack integration); use whichever Slack search/read tools your agent exposes. |
| **`gh` authenticated** for `braze-inc/braze-docs` | List open/merged PRs and open drafts |
| **Sibling `platform` (and SDK) repos** | **REQUIRED SUB-SKILL:** [reference-repos](../reference-repos/SKILL.md) (`braze-docs:reference-repos`) for every product-behavior theme before it appears in the overview |

If Slack MCP is unavailable, stop and ask the user to reconnect or enable it before mining threads.

---

## File scope

**Edit only:** `_docs/`, root `_includes/`

**Optional artifact:** `_data/slack_to_docs_overview_<channel>_<date>.md` when the user requests a saved overview (not committed unless they ask)

**Never edit:** `_lang/`, config, layouts, scripts, redirects (unless the user explicitly expands scope)

**Privacy:** Do not put customer names, company names, emails, or other PII from Slack into docs or PR bodies. Anonymize thread citations to role + month when needed.

---

## Step 1: Intake — channel and time window

Collect from the user (or infer from the prompt):

1. **Slack channel** — channel ID (`C…`), channel name (`#whatsapp-sme-global`), or archive URL
2. **Time window** — default **last 3–6 months** unless the user specifies otherwise; high-volume channels may use **last 4–8 weeks**
3. **Vertical / product area** — for example WhatsApp, Agents, Canvas (drives PR grouping and assignee routing)
4. **Optional cap** — max PRs to open this run (default **3–5**)

If only a channel name or URL is given, resolve the channel ID with your agent's Slack channel-search tool before mining.

---

## Step 2: Mine threads and build an overview

### Search strategy

Search Slack with paginated queries (public and private channels, as your Slack MCP allows). Examples:

```
in:<#CHANNEL_ID> after:YYYY-MM-DD
in:<#CHANNEL_ID> is:thread after:YYYY-MM-DD
```

Add targeted queries for high-signal patterns: `FAQ`, `error`, `credits`, `limit`, `how do`, `how to`, `does Braze`, `is it possible`.

For each promising hit, read the full thread (parent message + replies) using your agent's Slack thread-read tool (`channel_id` + `message_ts`).

### Triage each theme

| Bucket | Criteria | Action |
|--------|----------|--------|
| **Docs gap** | Recurring question; answer is stable product behavior | Candidate for docs |
| **Already documented** | Same answer exists on `develop` in `_docs/` | Skip |
| **Internal-only** | Unreleased feature, internal tooling, account-specific workaround, “ask your CSM” | Skip — do not publish |
| **Bug / product** | Defect or behavior that should be fixed in code | Skip — note for eng, not docs |
| **Unverified** | Cannot confirm in sibling source repos or existing public docs | Skip or flag for SME follow-up — do not put in a proposed PR |

### Source verification (required before the overview)

After triage, **before** writing the overview table, run **REQUIRED SUB-SKILL:** [reference-repos](../reference-repos/SKILL.md) (`braze-docs:reference-repos`) for every **Docs gap** theme.

Follow that skill in full: `git pull --ff-only` in the sibling repos you will search, search `shared_code/domains/` first for platform claims, flag flippers and rollout status, and do not guess.

| Claim type | Where to verify | If verification fails |
|------------|-----------------|------------------------|
| Braze product, API, or SDK behavior | Sibling `platform` or the relevant SDK repo | Do **not** propose a PR. Mark **Unverified** and skip or flag for SME. |
| Meta / carrier / third-party policy | Existing public docs plus the SME thread (not Braze code) | Propose only if public docs or the thread state a stable rule; say so in **Verified?**. |
| Already on `develop` | `_docs/` / root `_includes/` | Skip — do not re-document. |

### Internal-only filter (required)

**Do not document:**

- Unreleased or “coming soon” features unless already public on the docs site
- Internal-only tools, dashboards, or runbooks
- Customer-specific configurations, account names, or ticket details
- Ad-hoc Operator guidance that contradicts source code
- Workarounds for known bugs (escalate to product instead)

### Output: overview list

Write to chat (and optionally `_data/slack_to_docs_overview_<channel>_<date>.md` if the user wants a saved artifact).

**`Verified?` must include proof**, not `Yes` / `No` / `Docs skim`. Use one of:

| Status | Proof to put in the cell |
|--------|--------------------------|
| **Verified** | `Verified — <repo-relative path> (<what the code does>)` — for example `Verified — platform/shared_code/domains/channel_whats_app/…/messaging_service.rb (one subscription group per sending service)` |
| **Flipper** | `Flipper — <key>; rollout <global / limited / unknown>` |
| **Meta / policy** | `Policy — not Braze code; <public doc or SME conclusion>` |
| **Unverified** | `Unverified — <what you searched>; no matching source` — **Proposed PR** must be blank or **Skip** |

Example row:

```markdown
| Theme | Threads | Verified? | Target doc(s) | Canonical home | Dedup status | Proposed PR |
|-------|---------|-----------|---------------|----------------|--------------|-------------|
| Subscription is per sending number | 1 | Verified — `platform/shared_code/domains/chat_messaging_pipeline/…/messaging_service_base.rb` (`has_one :subscription_group`) | `opt_ins_and_opt_outs.md` | Main opt-in article | Clear | PR C |
```

Do not propose a product-behavior PR unless **Verified?** has a source path (or an explicit flipper/policy exception).

**Wait gate:** Present the overview and proposed PR batch. **Do not draft or open PRs** until the user approves the plan (or explicitly says to proceed with the full batch).

---

## Step 3: Confirm coverage before drafting

For each **approved** theme:

1. **Search `_docs/` and root `_includes/`** on `develop` for existing coverage (`Grep`, `Read`). Prefer updating over duplicating.
2. Reuse the **Verified?** proof from Step 2. Re-run **REQUIRED SUB-SKILL:** [reference-repos](../reference-repos/SKILL.md) (`braze-docs:reference-repos`) if the approved claim is narrower or different from the overview.
3. Carry the same proof into the PR **Approach** (repo-relative paths, no local filesystem paths), per [reference-repos](../reference-repos/SKILL.md).

---

## Step 4: Dedup against PRs and pending merges

**Before drafting**, run the [dedup check](workflows/dedup-check.md) for every target file and topic.

Summary rules:

1. **Open PRs** — `gh pr list --state open --base develop`. If another PR already edits the same file *or* the same topic, **merge into that PR’s scope**, defer the theme, or choose a different canonical home.
2. **Merged-not-deployed** — PRs merged to `develop` since the latest `v.*` tag (or in the last ~14 days) whose files overlap your targets. Read those files on `origin/develop`; **do not re-add** prose that is already merged.
3. **On-site duplication** — One canonical home per topic; other pages get **short cross-links** with anchors, not repeated tables or workflows.

### Content placement — main articles first

**Default:** Fit new information into the **main reference, workflow, or concept page** where an operator would naturally look for it. Extend an existing section before creating a parallel page.

**Last resorts only** — use FAQ or troubleshooting when they are **definitely** the ideal location:

| Placement | Use when | Avoid when |
|-------------|----------|------------|
| **Main article** (reference, workflow, processing, policy) | Behavior, limits, steps, tables, or diagrams belong with the feature | The answer is a one-off misc question with no natural section home |
| **`_includes/`** | Shared metrics or prose reused across multiple pages | Content belongs on a single page only |
| **FAQ** | Truly miscellaneous Q&A; stable anchor needed for cross-links from many satellites | The topic is core product behavior — put it on the main page instead |
| **Troubleshooting** | Multi-step diagnostic playbook (symptom → cause → fix) | A single limitation note or short answer — add to the main article or a note/alert there |

When choosing placement, ask: **“Where would a reader expect this while learning or using the feature?”** If the answer is the reference or workflow page, put it there — not in FAQ or troubleshooting by default.

### Canonical home patterns (from WhatsApp pilot)

| Content type | Canonical home | Satellite pages |
|--------------|----------------|-----------------|
| Product behavior, limits, workflows, diagrams | Main reference or processing page for that feature | FAQ or troubleshooting **link in** with one sentence + anchor |
| Shared metrics (campaign analytics) | `_includes/analytics/…` | Reporting pages point to include |
| Short Q&A that has no natural section home | `faq.md` with stable `####` + `{#anchor}` | Link from reference pages |
| Multi-step diagnostic playbooks | Dedicated troubleshooting page (only when playbook-length) | Main article + FAQ cross-link only |
| Meta / policy stubs | `meta_resources.md` or channel policy page | Link from formats or overview pages |

**Anti-pattern (WhatsApp lesson):** Adding full billing sections to `reporting.md`, `message_and_image_formats.md`, *and* `faq.md`. After merge, [#14641](https://github.com/braze-inc/braze-docs/pull/14641) moved credits guidance into `campaign_analytics` include and trimmed `reporting.md` to a pointer. [#14632](https://github.com/braze-inc/braze-docs/pull/14632) kept workflow detail on `messaging_users.md`; FAQ got only what had no better home.

**Anti-pattern (placement):** Creating a new FAQ entry or troubleshooting section when the same content fits an existing **How it works**, **Considerations**, or **Use cases** section on the main article.

---

## Step 5: Batch into PRs

### PR sizing and ownership

| Rule | Value |
|------|-------|
| **Max files per PR** | **5** `_docs/` or `_includes/` paths |
| **Min substance** | At least one meaningful edit; prefer **multiple sections on one page** over one sentence spread across many files |
| **One PR** | One **vertical / product theme** (for example “response messaging windows”, not “all of WhatsApp”) |
| **Branch name** | `docs/<vertical>-<short-topic-slug>` (example: `docs/whatsapp-response-messaging-billing`) |
| **Base branch** | `develop` |
| **PR type** | Draft |

If more than five files need changes for a theme, split into **2 PRs by sub-theme** (for example billing vs troubleshooting), not one large PR.

### Per-PR content checklist

- [ ] Every theme in the PR passed dedup check
- [ ] No internal-only content
- [ ] Source verified via [reference-repos](../reference-repos/SKILL.md); proof from **Verified?** is in **Approach**
- [ ] Canonical home chosen (main article first; FAQ/troubleshooting only if clearly best)
- [ ] Satellites cross-link only — no duplicate FAQ entries for the same question
- [ ] Slack thread URLs collected for **Source threads** section

---

## Step 6: Draft edits

**REQUIRED SUB-SKILL:** [braze-docs](../braze-docs/SKILL.md) (`braze-docs:braze-docs`) for voice, structure, Liquid, and links.

- English canonical only (`_docs/`, `_includes/`)
- Use `{{site.baseurl}}` internal links without trailing slashes
- **Prefer the main article:** extend **How it works**, **Considerations**, limits tables, or workflow steps on the feature’s reference page
- Add FAQ entries or troubleshooting sections **only** when no main-article section is the right home (see [Content placement](#content-placement-main-articles-first))
- When FAQ is justified, add stable anchors `{#kebab-case-question}` for cross-links from satellites
- Prefer extending an existing section over creating a parallel page

---

## Step 7: Open draft PRs

**REQUIRED SUB-SKILL:** [create-pr](../create-pr/SKILL.md) (`braze-docs:create-pr`) for Steps 0–1, 3–4, gates, and checklist.

### Step 2 override (slack-to-docs)

| Field | Value |
|-------|--------|
| **Title** | Imperative, specific (example: `Document WhatsApp response messaging windows and billing`). No ticket prefix unless the user supplies a Jira key. |
| **Label** | Optional: `slack-to-docs` if the label exists |

**Body** — use the create-pr template **plus** these sections:

```markdown
### Why are you making this change? (required)

<Reader outcome — what operators can do or understand after this merges.>

### Related PRs, issues, or features (optional)

- Complements / may overlap with #NNNN — <how you avoided duplication>
- Does **not** duplicate <topic> on `<page>` (cross-link only)

### Approach

<Canonical home choice, what was wrong before.>

Verified against Braze source code:

- `<repo-relative path>` — <what it proves>

### Source threads

- [<Short theme label>](<slack_thread_url>) — <Author first name> (<Month YYYY>)
- …

### Verification

<Preview URLs, anchor checks, spot-check against product UI where relevant.>

### Contributor checklist

<Copy from create-pr.>
```

In **Related PRs**, explicitly call out open PRs on the same files and merged PRs you reconciled against.

Set the **assignee** per [create-pr](../create-pr/SKILL.md) and the [PR template](../../../.github/PULL_REQUEST_TEMPLATE): add the [tech writer for the vertical](https://confluence.atl.braze.com/wiki/x/nAZuE) as assignee (`gh pr edit --add-assignee`), not as a reviewer. If the contributor is the vertical owner, they are already the default assignee. Optionally request review from SMEs cited in **Source threads**. Do not use platform `CODEOWNERS` for docs ownership — rely on the vertical tech writer assignee.

---

## Step 8: Handoff

After opening PRs, summarize in chat:

- PR links and one-line scope each
- Themes **deferred** (dedup, internal-only, unverified)
- Themes **skipped** because already on `develop`
- Recommended merge order if PRs depend on each other

---

## Example prompts

```
/slack-to-docs Mine #whatsapp-sme-global for the last 6 months and propose PRs.

Point slack-to-docs at #agent-console-support-and-feedback for the last 8 weeks.

Run slack-to-docs on C08CYL6KN1K — overview only, no PRs yet.
```

---

## Related skills

| Skill | Use when |
|-------|----------|
| [reference-repos](../reference-repos/SKILL.md) (`braze-docs:reference-repos`) | **Required** during Step 2 for each docs-gap theme; proof goes in **Verified?** |
| [braze-docs](../braze-docs/SKILL.md) | Writing and formatting edits |
| [create-pr](../create-pr/SKILL.md) | Pre-PR gates and opening drafts |
| [docs-discrepancies](../docs-discrepancies/SKILL.md) | Single-page source audit (not Slack-driven) |
| [support-analyzer](../support-analyzer/SKILL.md) | Support-case CSV triage instead of Slack |
