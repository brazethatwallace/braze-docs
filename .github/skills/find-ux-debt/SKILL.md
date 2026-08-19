---
name: find-ux-debt
description: >
  Scans one or more Braze platform UI files or directories for deterministically
  verifiable copy problems: name/value mismatches, deprecated terms, avoid-list
  violations, case violations, spatial language, i18n key/value mismatches,
  inconsistent terminology, and button antipatterns. Use after reference-repos
  surfaces a UI component file, or any time you want to audit platform copy
  before filing UX Debt tickets. Outputs a structured findings report grouped by
  severity tier: Tier 1 (factual issues the writer can log directly) and Tier 2
  (style/judgment calls routed to the UX writer). Two checks (avoid-list,
  deprecated-term) require the braze-ux-writing plugin (skill: writing-ux-copy);
  the remaining six run without it.
argument-hint: "[platform/path/to/Component.tsx or directory/]"
---

# Find UX debt in platform UI files

> **Workflow context:** `reference-repos → find-ux-debt → log-ux-debt`
> Run this skill after `reference-repos` surfaces a UI component file, or any
> time you want to audit platform copy before filing tickets.

Scan Braze platform UI source files for copy problems that are **deterministically
verifiable from source code**. Findings are grouped into two tiers so a writer
never has to decide whether something is "bad enough to report."

**Composes:** braze-ux-writing:writing-ux-copy (optional — required for avoid-list and deprecated-term checks only)
**Composes:** braze-atlassian:creating-jira-tickets (only when Tier 2 findings exist and the writer confirms a UXW ticket)

---

## Two-tier severity model

| Tier | Checks | Why | Writer's next step |
|---|---|---|---|
| **1 — Factual** | `name-mismatch`, `deprecated-term`, `i18n-mismatch` | Verifiable right answer from source code alone. No judgment required. | Log each finding as a UX Debt ticket with `/log-ux-debt` |
| **2 — Style/judgment** | `avoid-list`, `case-violation`, `spatial-language`, `inconsistent-terminology`, `button-antipattern` | Requires Braze writing standards knowledge or broader context the writer doesn't have. | Skill offers to log one consolidated UXW story to the "UXW support for UX debt" epic |

The skill never asks the writer to evaluate a Tier 2 finding — it surfaces it, explains it briefly, and handles escalation.

---

## Gotchas

- **Don't flag proper nouns as case violations** — "Feature Flags", "Push Notifications", "Braze Canvas" look like title case but are correct. Cross-reference `braze-ux-writing:writing-ux-copy → reference/feature_terms.md` before flagging a case hit. If the plugin is unavailable, skip case-violation for strings that match known product names.
- **Don't match "left" / "right" as bare words in spatial-language** — "left-align", "right-click", "left-to-right" are not positional UI copy. Match full phrases only: "to the left of", "above the", "see the table below", "below the".
- **Don't treat "Cancel" and "Close" as inconsistent terminology** — they describe different affordances. The inconsistent-terminology check targets the *same semantic operation* named differently, not any two action verbs in the same file.
- **Don't present Tier 2 findings as things the writer needs to decide on** — the two-tier model exists so writers never evaluate whether a style finding is "bad enough." Surface it, route it to UXW, and move on.
- **Don't scan compiled or minified files** — `dist/`, `build/`, `*.min.js` contain transformed strings. Flag and skip if the path indicates a build artifact.
- **Don't claim a clean scan when template literals or computed strings were present** — `t(\`key.${dynamic}\`)` and `label={getLabel()}` are outside extraction scope. The findings report footer must always note this.
- **Don't flag `title=` in non-UI contexts** — SVG `<title>`, HTML page titles, and React metadata `title` props are not UI labels. Scope `title=` matching to component prop contexts.

---

## Step 0 — Plugin detection

Run before any file scanning.

1. **Detect** — Check the agent's available-skills list for `Skill Name: writing-ux-copy`. If not listed, check filesystem paths: `~/.agents/skills/writing-ux-copy/`, `~/.claude/skills/writing-ux-copy/`, `~/.cursor/skills/writing-ux-copy/`. Do not treat a missing filesystem path as proof the skill is absent if it appears in the available-skills list.

2. **If available** — Proceed with all 8 checks. Load `braze-ux-writing:writing-ux-copy → reference/avoid_list.md` and `braze-ux-writing:writing-ux-copy → reference/feature_terms.md` before starting.

3. **If not available** — Proceed with the 6 non-plugin checks. Skip `avoid-list` and `deprecated-term`. Append to the findings report footer:

```
⚠ 2 checks skipped (braze-ux-writing plugin not found):
  - avoid-list     — install braze-ux-writing to enable
  - deprecated-term — install braze-ux-writing to enable

Install: braze-agent-plugins → plugins/teams/braze-ux-writing
https://github.com/braze-inc/braze-agent-plugins/tree/main/plugins/teams/braze-ux-writing
```

---

## Step 1 — Resolve scope

Accepts a file path or directory via `$ARGUMENTS`. If no argument, ask.

- **Single file** (`.tsx`, `.jsx`, `.vue`, `.erb`, `.js`) → scan that file, continue to Step 2.
- **Directory** → scan all UI component files one level deep, then ask:

  If AskUserQuestion is available:
  - "This level only" — stop after the current directory
  - "Go deeper" — recurse into subdirectories

  Otherwise ask: "Scan subdirectories too? (y/n)"

**Error handling:**

| Scenario | Response |
|---|---|
| File path not found | "File not found: `<path>`. Confirm the path is relative to the platform repo root." |
| File is not a UI component (binary, CSS, JSON, test file) | "Skipped: `<path>` — pass a `.tsx`, `.jsx`, `.vue`, or `.erb` file." |
| No extractable UI strings found | "No extractable UI strings found in `<path>`. The file may use patterns outside this skill's extraction scope (template literals, dynamic labels)." |
| Plugin detection throws unexpectedly | "Could not determine braze-ux-writing status. Proceeding with 6 non-plugin checks." |

---

## Step 2 — Extract UI strings

The skill cannot parse a full AST, so it targets high-yield patterns.

**Constraint:** Template literals, computed strings, and strings assembled at runtime are outside extraction scope — a clean report does not guarantee a clean file.

| Pattern | What to search for |
|---|---|
| JSX text / prop strings | `label=`, `tooltip=`, `title=` (component prop contexts only), `aria-label=`, `placeholder=`, `description=`, `helperText=` |
| i18n calls | `I18n.t(`, `t('`, `translationKey` |
| String constants | `const *LABEL`, `const *TITLE`, `const *TOOLTIP`, `const *MESSAGE` |
| Error/success messages | `errorMessage`, `successMessage`, `toastMessage` prop values |

---

## Step 3 — Run checks

### Tier 1 — Factual (file as UX Debt)

1. **name-mismatch** — Compare nearby code identifiers (permission keys, prop names) to adjacent display strings. Flag when the identifier and the string describe different things.

2. **deprecated-term** — Requires plugin. Load `braze-ux-writing:writing-ux-copy → reference/feature_terms.md`. Check extracted strings against the renamed-terms list. Flag any match.

3. **i18n-mismatch** — Compare the i18n key name to its default string argument. Flag when they describe different concepts (e.g. key `manage_media_assets` with default "Edit Media Assets").

### Tier 2 — Style/judgment (route to UXW)

4. **avoid-list** — Requires plugin. Load `braze-ux-writing:writing-ux-copy → reference/avoid_list.md`. Flag any extracted string that contains a listed term.

5. **case-violation** — Check button and label strings for title case (word count ≥ 3 with multiple capitalized words). Cross-reference feature_terms.md before flagging — proper nouns like "Feature Flags" are correct and must not be flagged.

6. **spatial-language** — Scan for full positional phrases: "to the left of", "to the right of", "above the", "below the", "see the table above", "see the table below". Do not match bare "left", "right", "above", or "below" as standalone words.

7. **inconsistent-terminology** — Collect action verbs from the file. Flag when the *same semantic operation* is named differently across components (e.g. "Remove" and "Delete" both present for the same delete action). "Cancel" and "Close" are intentionally distinct — do not flag them.

8. **button-antipattern** — Flag "OK", "Submit", "Click here", "Yes", "No" as standalone button labels.

---

## Step 4 — Report findings

Group findings by tier, not by check type. Tier 1 first, then Tier 2. If scanning a directory, group all findings by file before showing post-scan guidance.

```
COPY SCAN: path/to/Component.tsx

── Tier 1: Factual issues ──────────────────────────────────
These have a clear, verifiable fix. You can log each one as a UX Debt ticket.

[name-mismatch] Line 50
  Current: "Manage Media Library Assets"
  Issue: tooltip copy doesn't match permission key `editMediaLibraryAssets`
  Suggested: "Edit Media Library Assets"
  → Run /log-ux-debt to file

── Tier 2: Style and judgment calls ────────────────────────
These require UX writing expertise. The skill will offer to log a UXW ticket below.

[avoid-list] Line 32
  Current: "Changes saved successfully"
  Issue: "successfully" is on the Braze avoid list (redundant in success states)
  Suggested: "Changes saved"

---
Note: Template literals and computed strings are outside this skill's extraction scope — a clean report doesn't guarantee a clean file.
```

---

## Step 5 — Post-scan guidance

After printing the report, guide the writer to the right next step.

**If Tier 1 findings exist:**

If AskUserQuestion is available:
- "Log first finding now" — invoke `/log-ux-debt` with the first Tier 1 finding passed as `$ARGUMENTS` (JSON with `file`, `current`, `expected`, `context` keys)
- "I'll log them manually" — print the guidance below and stop

Otherwise ask: "Want me to log the first Tier 1 finding now? (y/n)"

If no: print the guidance below and stop.
If yes: invoke `/log-ux-debt` with the first finding as structured `$ARGUMENTS`.

> To log the remaining Tier 1 findings, run `/log-ux-debt` for each one and pass the finding details.

**If Tier 2 findings exist:**
> The Tier 2 findings above are style and judgment calls — they're best reviewed by the UX writer rather than filed directly as UX Debt. I can log a single consolidated UXW ticket in the "UXW support for UX debt" epic ([UXW-341](https://jira.atl.braze.com/browse/UXW-341)) covering all of them. Bre is expecting these types of tickets.
>
> Want me to log it?

If AskUserQuestion is available:
- "Yes, log UXW ticket" — invoke `braze-atlassian:creating-jira-tickets` with the fields below
- "No thanks" — stop

Otherwise ask: "Log a UXW ticket for these findings? (y/n)"

**If yes**, invoke `braze-atlassian:creating-jira-tickets` with:

- **Project:** `UXW`
- **Issue type:** Story
- **Summary:** `[UX Copy] Style findings in <ComponentName> from automated copy scan`
- **Parent epic:** `UXW-341`
- **Assignee:** Bre Fitzgerald
- **Description:** bullet list of all Tier 2 findings (file, line, current copy, issue, suggested)

If scope was a directory, group all Tier 2 findings from all files into the single ticket.

**If no findings in either tier:**
> No issues found. Template literals and computed strings weren't scanned — check those manually if needed.
