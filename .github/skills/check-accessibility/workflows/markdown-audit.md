# Workflow: Markdown Table Accessibility Audit

## Overview

Runs `scripts/check_table_accessibility.py` on changed markdown files, interprets the output,
and applies fixes at three confidence tiers. High-confidence fixes are applied automatically.
Medium and low confidence issues pause and ask the author what to do.

---

## Step 1: Identify the changed markdown files

From the context in SKILL.md, collect the list of changed `_docs/**/*.md` and `_includes/**/*.md`
files. Exclude anything under `_lang/`.

If the file list is empty after exclusions, report:
> No changed markdown files found (excluding `_lang/`). Nothing to check.

---

## Step 2: Run the table accessibility script

Run the script against the changed files only (not a full scan):

```bash
python3 scripts/check_table_accessibility.py --json /tmp/a11y-violations-$(git rev-parse --short HEAD).json [file1.md] [file2.md ...]
```

Capture:
- **Exit code** — `0` means no violations, `1` means violations found
- **violations.json** — structured list of findings

If exit code is `0`: report "No table accessibility violations found in the changed markdown files." and stop.

If the script errors (exit code 2 or unexpected output): report the error, show the raw output, and stop.

---

## Step 3: Classify each violation by confidence tier

Read the violations JSON file written in Step 2 (`/tmp/a11y-violations-$(git rev-parse --short HEAD).json`). For each violation, apply the following classification.

**Tiers are ordered by priority: low > medium > high. If any low- or medium-confidence condition is met for a violation, that tier wins — even if all high-confidence conditions are also satisfied.**

### High confidence — auto-fix

All three conditions must be true:
1. Violation message is `"Markdown table is missing an accessible name."` (no IAL exists at all — not a modification case)
2. The `suggestion_content` contains an `aria-label` derived from a heading that is **specific** — the label is not one of: `Table`, `Overview`, `Details`, `Notes`, `Summary`, `Introduction`, `Background`, `Results`, `Example`, `Examples`, `Reference`, `References`
3. The table is in a file with **3 or fewer total violations** (bulk-violation files may have systematic issues needing human review)

*Each violation is classified independently. A file with 3 violations can contain both high- and low-confidence violations simultaneously — condition 3 is necessary but not sufficient for high confidence.*

### Medium confidence — stop and ask

Any of these conditions:
- Violation message is `"Markdown table IAL is missing aria-label="` — an existing IAL is present that needs to be modified (risk of breaking other classes/attributes)
- The `aria-label` in the suggestion is a generic heading (from the list above)
- The nearest heading is **strictly more than 20 lines** above the table start line (a heading exactly 20 lines above is high-confidence; the threshold is >20, not ≥20)

### Low confidence — stop and ask

Any of these conditions:
- The violation is on an **HTML table** (`<table>` tag), not a markdown GFM table
- The file has **4 or more violations** total
- The suggestion would result in a label like `"Table"` — the script's fallback when no heading is found

---

## Step 4: Apply high-confidence fixes

For each high-confidence violation, apply the fix using StrReplace:

- `current_content` = the `current_content` field from the violation
- `new_content` = the `suggestion_content` field from the violation
- File = the `file` field

After applying each fix, briefly confirm: `✓ Fixed: [file]:[line] — added aria-label="[label]"`

If multiple high-confidence fixes apply to the same file, apply them all before moving to the next file. Apply fixes from bottom to top (highest line number first) to avoid line-number drift.

---

## Step 5: Present medium and low confidence issues

After applying all high-confidence fixes, collect the remaining violations and present them
grouped by file. For each issue, show:

---

**[file path]:[table start line]**

```markdown
[First 4 rows of the table, or the full table if under 4 rows]
```

**Issue:** [violation message]
**Suggested fix:**
```
[suggestion_content from the violation]
```

**What would you like to do?**

If AskUserQuestion is available:
- **Accept the suggestion** — Apply the generated aria-label as-is
- **Provide a custom label** — I'll describe what this table contains
- **Mark as layout table** — This is a decorative/layout table; apply `role="presentation"`
- **Skip for now** — Leave this table unchanged (will be flagged in CI)

Otherwise ask:
> What would you like to do? (1) Accept the suggestion, (2) Provide a custom label, (3) Mark as layout table with role="presentation", (4) Skip for now

---

**Non-interactive mode** (`$ARGUMENTS` contains "ci" or "headless"): Skip all prompts. Record every medium- and low-confidence violation as "skipped (non-interactive mode)" and include them in the final summary under "Skipped issues." Apply no fixes for these violations.

Wait for a response before moving to the next medium/low confidence issue. Handle one at a time.

### Handling responses

**Accept the suggestion:** Apply `suggestion_content` as the fix (same StrReplace approach as high-confidence). Confirm the fix.

**Provide a custom label:** Ask: "What label should this table have? Write a short, descriptive phrase (for example: 'Supported SDK versions by platform')." Apply the fix with the custom label substituted into the IAL pattern.

**Mark as layout table:** Apply `{: role="presentation" }` on the line immediately after the last table row (for markdown tables) or add `role="presentation"` to the `<table>` tag (for HTML tables). Confirm the fix.

**Skip for now:** Note it in the final summary. The CI check will flag it when the PR is opened.

---

## Step 6: Final summary

After all issues are resolved or skipped, present a summary:

---

### Table accessibility audit complete

**Changed files checked:** [N]
**Violations found:** [N]

| Resolution | Count |
|---|---|
| Auto-fixed (high confidence) | N |
| Fixed with your input (medium/low) | N |
| Skipped (will be flagged in CI) | N |

**Auto-fixed files:**
- `[file path]` — [N] fix(es) applied

**Skipped issues (action needed before merging):**
- `[file path]:[line]` — [violation message]

---

## Gotchas

- **Apply fixes bottom-to-top within a file.** The script reports `suggestion_line` as a 1-indexed line number. If you apply fixes top-to-bottom, earlier insertions shift subsequent line numbers and the remaining fixes land on the wrong lines.
- **Don't replace the entire IAL line for a bare-IAL violation without reading the full existing IAL first.** The existing IAL may have `.reset-td-br-N` classes. The suggested fix from the script already includes these classes — verify the existing classes match before applying.
- **For HTML table fixes, read the surrounding context first.** Is this a complex data table with multiple `<thead>` rows? A `<caption>` is semantically richer. Is it a simple inline reference table? `aria-label` is fine. Don't blindly apply the script's `aria-label` suggestion for HTML tables without reading the table structure.
- **Don't run a full scan (`python3 scripts/check_table_accessibility.py` with no args).** This scans all 3,000+ markdown files and will be slow and produce noise. Always pass the specific changed files as arguments.
- **The script's "nearest heading" fallback is `"Table"`.** If you see `aria-label="Table"` in a suggestion, that means no heading was found — this is a low-confidence case. Don't auto-apply it.
- **Files under `_docs/_hidden/` are skipped by the script automatically.** If a changed file is under `_hidden/`, don't manually add it to the run list.

---

## Success Criteria

- [ ] Script run against changed markdown files only (not a full scan)
- [ ] All violations classified by confidence tier
- [ ] All high-confidence fixes applied automatically (bottom-to-top per file)
- [ ] Each medium/low confidence issue presented one at a time with options
- [ ] Summary presented at the end showing counts and any skipped issues
- [ ] If the script exits with code 2 or unexpected output, the raw error is surfaced and the workflow stops (no partial fixes applied)

---

## Example

**Input:** One changed file `_docs/_user_guide/messaging/push/android/push_primer.md` with 2 violations.

**violations.json (abbreviated):**
```json
[
  {
    "file": "_docs/_user_guide/messaging/push/android/push_primer.md",
    "table_start_line": 45,
    "suggestion_line": 50,
    "suggestion_content": "| Push permission | Granted | Denied |\n{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label=\"Push primer permission outcomes\" }",
    "current_content": "| Push permission | Granted | Denied |",
    "message": "Markdown table is missing an accessible name.",
    "fix_hint": "Add after the last row: {: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label=\"Push primer permission outcomes\" }"
  }
]
```

**Classification:** Violation message matches high-confidence type. `aria-label` is "Push primer permission outcomes" — specific, not on the generic exclusion list. File has 2 violations (≤3). No low- or medium-confidence conditions met. → **High confidence.**

**Auto-fix applied:** `✓ Fixed: _docs/...push_primer.md:50 — added aria-label="Push primer permission outcomes"`

**Final summary:**
```
### Table accessibility audit complete
Changed files checked: 1 | Violations found: 2
Auto-fixed (high confidence): 2 | Fixed with your input: 0 | Skipped: 0
Auto-fixed files:
- `_docs/_user_guide/messaging/push/android/push_primer.md` — 2 fix(es) applied
```
