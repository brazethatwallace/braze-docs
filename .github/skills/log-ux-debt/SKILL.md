---
name: log-ux-debt
description: >
  Use when reference-repos or docs-discrepancies surfaces a copy inconsistency
  in Braze platform source that is deterministically verifiable: name/value
  mismatches (permission identifier vs. display name, renamed features), avoid-list
  violations ("successfully", "e.g.", "Please"), case violations (title case where
  sentence case is required), spatial language ("above", "below"), i18n key/value
  mismatches, inconsistent terminology across components, or button antipatterns
  ("OK", "Submit"). Handles CODEOWNERS lookup, duplicate detection, and ticket
  creation with acceptance criteria.
disable-model-invocation: true
argument-hint: "[platform/path/to/file.tsx]"
---

# Log a UX debt ticket for a copy inconsistency

Use this skill when platform source code contains a copy problem that is
**deterministically verifiable** — you can point to the file and line, state
what it says, and state what it should say, without needing subjective UX
judgment. File a UX Debt ticket with the owning team.

> **Side effects:** This skill creates a Jira ticket. Only invoke it when the
> user has explicitly asked to log a UX debt ticket.

**Composes:** braze-atlassian:searching-jira, braze-atlassian:creating-jira-tickets

---

## Detectable copy problem types

All eight categories below are verifiable from source code alone. If the problem
requires design context, user research, or subjective tone judgment, it is out of
scope for a UX Debt ticket — file a UXW story instead: project `UXW`, parent
epic [UXW-341](https://jira.atl.braze.com/browse/UXW-341), assigned to Bre
Fitzgerald. Use `braze-atlassian:creating-jira-tickets` for that as well.

| Type | What to look for in source | Example |
|---|---|---|
| **name-mismatch** | Code identifier (permission key, prop name) differs from the displayed string | `editMediaLibraryAssets` → tooltip says "Manage Media Library Assets" |
| **deprecated-term** | UI string uses an old product or feature name after a rename | Button says "AI Image Generator" — product is now "Generate with Operator" |
| **avoid-list** | UI string contains a term on the Braze avoid list (`braze-ux-writing:ux-writing` → `reference/avoid_list.md`) | "successfully saved", "e.g.", "Please confirm", "OK", "Click here" |
| **case-violation** | UI string uses title case where Braze standard requires sentence case | Button reads "Create New Campaign" — should be "Create new campaign" |
| **spatial-language** | UI string uses "above", "below", "left", or "right" as a positional reference | "See the table above" — breaks in RTL and responsive layouts |
| **i18n-mismatch** | i18n key name or its default string doesn't match the displayed copy | Key `manage_media_assets` — default value "Edit Media Assets" — displayed string "Manage Media Library Assets" |
| **inconsistent-terminology** | Same action or concept named differently across two or more components | "Remove" in one modal, "Delete" in another for the same operation |
| **button-antipattern** | CTA label is vague or imperative-less | Button reads "Submit" or "OK" instead of `[Verb] [object]` |

---

## Gotchas

- **Don't grep for the full file path in CODEOWNERS** — CODEOWNERS uses glob
  patterns (`dashboard/app/**`), not literal file paths. Grep for the deepest
  specific directory segment instead, then manually confirm the pattern covers
  the full path. A grep that returns no results does not mean no owner exists.
- **Don't treat the first JQL result as a definitive duplicate** — `summary ~`
  is fuzzy and returns partial matches. Present all results to the user and ask
  for explicit confirmation before stopping.
- **Don't bypass `braze-atlassian:creating-jira-tickets`** — that skill enforces
  a HARD-GATE for agent eligibility assessment and appends the required Agent
  Info expand block. Calling the Atlassian MCP or CLI directly skips both.
- **Don't file subjective or tone-only issues as UX Debt** — "This feels too
  formal" or "the copy could be warmer" have no verifiable ground truth. File
  those as a UXW story instead: project `UXW`, parent epic
  [UXW-341](https://jira.atl.braze.com/browse/UXW-341), assigned to Bre
  Fitzgerald.
- **Don't confuse inconsistent-terminology with avoid-list** — "successfully" is
  on the avoid list (file as `avoid-list`); "Remove" vs "Delete" for the same
  action is inconsistent terminology (file as `inconsistent-terminology`). The
  distinction matters for acceptance criteria.

---

## Inputs

Collect the following before proceeding.

### Shortcut: $ARGUMENTS parsing

If `$ARGUMENTS` is present, check for a structured call from a parent skill
(docs-discrepancies, reference-repos). These pass a JSON object with keys:
`file`, `current`, `expected`, `context`. Parse and prefill all four inputs.

If `$ARGUMENTS` is a plain string, treat it as the **platform file path** only
and ask for the remaining three inputs.

If no `$ARGUMENTS`, ask for all inputs. **Copy type** can usually be inferred
from the other inputs — only ask if genuinely ambiguous.

| Input | Description | Example |
|---|---|---|
| **Platform file path** | Repo-relative path in `platform/` to the file | `dashboard/app/javascript/src/components/MediaLibrary/GenerateImageWithOperatorButton/GenerateImageWithOperatorButton.tsx` |
| **Current copy** | What the file currently says | `"Manage Media Library Assets"` |
| **Expected copy** | What it should say | `"Edit Media Library Assets"` |
| **Context** | One sentence explaining where the discrepancy matters | Found while verifying the media library FAQ permission name against platform source |
| **Copy type** *(inferred if possible)* | Category from the table above | `name-mismatch` |

---

## Step 1 — CODEOWNERS lookup

Search `../platform/.github/CODEOWNERS` for lines whose glob pattern matches
the platform file path. Work from most specific to least specific — the last
matching pattern in the file wins (CODEOWNERS precedence rules).

Grep for the deepest specific directory segment of the file path (for example,
for `.../MediaLibrary/Foo.tsx`, search for `MediaLibrary`), then evaluate which
patterns cover the full path.

- Extract the `@Appboy/<team-name>` owner from the best-matching line.
- If multiple patterns match, prefer the most specific (longest matching prefix).
- If no owner is found, prompt the user to specify the team manually.

---

## Step 2 — Team → Jira project key

Load [`references/team-jira-map.md`](references/team-jira-map.md) and find the
row for the `@Appboy/<team>` handle from Step 1.

If the team is not in the table, prompt the user for the Jira project key
before continuing.

---

## Step 3 — Duplicate check

Delegate to `braze-atlassian:searching-jira` with this JQL:

```
project = <KEY> AND issuetype = "UX Debt" AND summary ~ "<key term from discrepancy>" ORDER BY created DESC
```

Present all results to the user (URL + summary for each). Ask:
- **Potential duplicate found:** Is one of these the same issue? Proceed with a new ticket, or stop?
- **No results:** Continue to Step 4.

---

## Step 4 — Prepare ticket fields

Compose the following before invoking `braze-atlassian:creating-jira-tickets`.

**Project:** key resolved in Step 2  
**Issue type:** `UX Debt`  
**Summary:**

```
[UX Copy] <ComponentName>: "<current copy>" should be "<expected copy>"
```

**Description** (pass as a single `--description` body including ACs):

```markdown
## Background

A copy inconsistency ([copy type]) was found in [ComponentName] while verifying Braze documentation against platform source code.

- File: [GitHub permalink — https://github.com/Appboy/platform/blob/develop/<path>#L<line>]
- Current copy: "[current copy]"
- Expected copy: "[expected copy]"

[One sentence from the Context input]

*Suggested revision:* Replace "[current copy]" with "[expected copy]" in [file and line reference].

## Acceptance Criteria

[Select the ACs that apply to the copy type — include all that are relevant:]

- [ ] The [element type] in [ComponentName] reads "[expected copy]".        ← all types
- [ ] The updated copy is consistent with the code identifier or permission key (for example, `editMediaLibraryAssets`).   ← name-mismatch, i18n-mismatch
- [ ] The old term "[deprecated term]" does not appear in any visible string in this component.   ← deprecated-term
- [ ] The string is sentence case throughout this component.   ← case-violation
- [ ] No spatial references ("above", "below", "left", "right") remain in this component's strings.   ← spatial-language
- [ ] The i18n key value and default string match the displayed copy.   ← i18n-mismatch
- [ ] "[Term A]" and "[Term B]" are unified to "[canonical term]" across [ComponentA] and [ComponentB].   ← inconsistent-terminology
- [ ] If the string is i18n'd, the translation key is updated to match.   ← all types where i18n applies
```

---

## Step 5 — Delegate to creating-jira-tickets

Invoke `braze-atlassian:creating-jira-tickets` with the fields prepared in
Step 4. That skill handles:
- Loading Jira conventions (including `braze-jira-acceptance-criteria` and `braze-jira-team-field`)
- Agent eligibility assessment (HARD-GATE — required before preview)
- Agent Info expand block appended to the description
- Preview gate — user must confirm before creation
- Creation and fetch-back verification

Do not call the Atlassian MCP or CLI directly for creation.

---

## Step 6 — Report

After `braze-atlassian:creating-jira-tickets` completes, print the ticket URL
and a one-line summary to the chat console:

```
Logged UX Debt: [KEY-1234](https://jira.atl.braze.com/browse/KEY-1234)
Summary: [UX Copy] ComponentName: "current copy" should be "expected copy"
```

---

## Reference files

- [`references/team-jira-map.md`](references/team-jira-map.md) — `@Appboy/<team>` → Jira project key mapping table
