# Workflow: Content Accessibility Audit (Markdown and HTML Includes)

## Overview

Runs two accessibility scripts against changed markdown and HTML include files:

1. `scripts/check_table_accessibility.py` — checks table accessible names (WCAG 1.3.1)
2. `scripts/check_content_accessibility.py` — checks image alt text (1.1.1), non-descriptive link text (2.4.4), heading hierarchy (2.4.6), and inline iframes (4.1.2)

Findings from both scripts are merged and processed together with the same confidence-tier system. High-confidence fixes are applied automatically. Medium and low confidence issues pause and ask the author what to do.

---

## Step 1: Identify the changed files to check

Collect the following changed files from the context in SKILL.md:
- `_docs/**/*.md`
- `_includes/**/*.md`
- `_includes/**/*.html` — include these; both scripts check HTML content

Exclude anything under `_lang/`.

If the file list is empty after exclusions, report:
> No changed files found for content accessibility checks (excluding `_lang/`). Nothing to check.

**Note on HTML files from `_includes/`:** HTML table violations are always classified as low confidence (see Step 3). They will never be auto-fixed — they are always presented to the author with options.

---

## Step 2: Run both accessibility scripts

Run the scripts against the changed files. Run both even if the first finds no violations.

**Step 2a — Table accessibility:**
```bash
python3 scripts/check_table_accessibility.py --json /tmp/a11y-table-$(git rev-parse --short HEAD).json [file1.md] [file2.md ...]
```

**Step 2b — Content accessibility:**
```bash
python3 scripts/check_content_accessibility.py --json /tmp/a11y-content-$(git rev-parse --short HEAD).json [file1.md] [file2.md ...]
```

For each script, capture:
- **Exit code** — `0` = no violations, `1` = violations found
- **JSON output** — structured list of findings

**If either script exits with code 2 or produces unexpected output:** report the raw error and stop. Do not apply any fixes.

After both scripts complete, read both JSON files and merge the findings into a single list ordered by file path, then by line number ascending. Violations from both scripts enter the same classification pass in Step 3.

If both scripts exit 0 and both JSON files are empty arrays:
> Content accessibility audit complete — no violations found in the [N] changed file(s).

Stop here.

---

## Step 3: Classify each violation by confidence tier

**Tiers are ordered by priority: low > medium > high. If any low- or medium-confidence condition is met for a violation, that tier wins — even if all high-confidence conditions are also satisfied.**

### High confidence — auto-fix

#### Table violations (from `check_table_accessibility.py`)

All three conditions must be true:
1. `violation_type` is absent (table script doesn't set this field) AND `message` is `"Markdown table is missing an accessible name."` (no IAL at all)
2. The `suggestion_content` contains an `aria-label` derived from a heading that is **specific** — not one of: `Table`, `Overview`, `Details`, `Notes`, `Summary`, `Introduction`, `Background`, `Results`, `Example`, `Examples`, `Reference`, `References`
3. The table is in a file with **3 or fewer total violations** across both scripts combined

*Each violation is classified independently — condition 3 applies across the merged findings count for the file.*

#### Content violations (from `check_content_accessibility.py`)

- `violation_type: image_missing_alt` where the original image had empty alt — **none are auto-fixed**. All image alt violations are medium confidence (see below). The fix requires author judgment about the image's meaning.

### Medium confidence — stop and ask

#### Table violations
Any of these conditions:
- `message` is `"Markdown table IAL is missing aria-label="` (modifying an existing IAL)
- The `aria-label` in the suggestion is a generic heading (from the exclusion list above)
- The nearest heading is **strictly more than 20 lines** above the table start line

#### Content violations
- `violation_type: image_missing_alt` — author must decide whether to add alt text or confirm decorative intent
- `violation_type: nondescriptive_link` — fix requires knowing the destination
- `violation_type: iframe_missing_title` — title wording is contextual

### Low confidence — stop and ask

#### Table violations
Any of these conditions:
- Violation is on an **HTML table** (`<table>` tag)
- The file has **4 or more total violations** across both scripts combined
- The suggestion would result in `aria-label="Table"`

#### Content violations
- `violation_type: heading_skip` — always low confidence; heading level changes affect document structure and require author judgment

---

## Step 4: Apply high-confidence fixes

For each high-confidence violation, apply the fix using StrReplace:
- `current_content` = the `current_content` field from the violation
- `new_content` = the `suggestion_content` field from the violation
- File = the `file` field

After applying each fix, confirm: `✓ Fixed: [file]:[line] — [brief description]`

If multiple high-confidence fixes apply to the same file, apply them all before moving to the next file. Apply fixes from bottom to top (highest line number first) to avoid line-number drift.

---

## Step 5: Present medium and low confidence issues

After applying all high-confidence fixes, collect the remaining violations and present them grouped by file. For each issue:

---

**[file path]:[issue line]**

```
[The affected line(s) — for tables, the first 4 rows; for images/links, the full line]
```

**WCAG criterion:** [e.g., 2.4.4 Link Purpose]
**Issue:** [violation message]
**Suggested fix:**
```
[fix_hint from the violation]
```

**What would you like to do?**

*For table violations:*
- **Accept the suggestion** — Apply the generated aria-label as-is
- **Provide a custom label** — I'll describe what this table contains
- **Mark as layout table** — This is a decorative/layout table; apply `role="presentation"`
- **Skip for now** — Leave this table unchanged (will be flagged in CI)

*For `image_missing_alt` violations:*
- **Add alt text** — Tell me what the image shows; I'll apply it
- **Confirm decorative** — This image is purely decorative; the empty alt is intentional
- **Skip for now** — Leave this image unchanged

*For `nondescriptive_link` violations:*
- **Replace link text** — Tell me a better description; I'll apply it
- **Accept context suggestion** — Use the surrounding text to suggest a replacement
- **Skip for now** — Leave this link unchanged

*For `heading_skip` violations:*
- **I'll fix manually** — Acknowledged; I'll adjust heading levels myself
- **Skip for now** — Leave this unchanged

*For `iframe_missing_title` violations:*
- **Add title** — Tell me what this iframe contains; I'll add the title attribute
- **Skip for now** — Leave this iframe unchanged

---

**Non-interactive mode** (`$ARGUMENTS` contains "ci" or "headless"): Skip all prompts. Record every medium- and low-confidence violation as "skipped (non-interactive mode)" and include them in the final summary under "Skipped issues." Apply no fixes for these violations.

Wait for a response before moving to the next medium/low confidence issue. Handle one at a time.

---

## Step 6: Final summary

After all issues are resolved or skipped, present a summary:

---

### Content accessibility audit complete

**Changed files checked:** [N]
**Violations found:** [N] (table: [N], content: [N])

| WCAG | Type | Count | Resolution |
|---|---|---|---|
| 1.3.1 | Table accessible names | N | [auto-fixed / fixed with input / skipped] |
| 1.1.1 | Image alt text | N | [fixed with input / skipped] |
| 2.4.4 | Non-descriptive link text | N | [fixed with input / skipped] |
| 2.4.6 | Heading hierarchy | N | [acknowledged / skipped] |
| 4.1.2 | Inline iframes | N | [fixed with input / skipped] |

**Skipped issues (action needed before merging):**
- `[file path]:[line]` — [WCAG criterion] [violation message]

---

## Gotchas

- **Apply fixes bottom-to-top within a file.** If you apply fixes top-to-bottom, earlier insertions shift subsequent line numbers.
- **Don't run a full scan with no arguments.** This scans all 3,000+ files. Always pass the specific changed files as arguments.
- **For table IAL fixes, read the existing IAL first.** The existing IAL may have `.reset-td-br-N` classes. Verify they are preserved in the suggestion.
- **Image alt text fixes require author input** — the script flags presence/absence; only the author knows what the image shows.
- **Heading skips are always low confidence.** Never auto-fix heading levels — the change could alter how readers understand document structure.
- **`check_content_accessibility.py` skips code fences but not inline backticks.** A `![](url)` inside a backtick-wrapped inline code span will still be flagged. This is a known limitation.

---

## Success Criteria

- [ ] Both scripts run against changed files only (not a full scan)
- [ ] Findings from both scripts are merged and classified in a single pass
- [ ] High-confidence table fixes applied automatically (bottom-to-top per file)
- [ ] Each medium/low confidence issue presented one at a time with type-appropriate options
- [ ] Summary presented at the end showing violation counts by WCAG criterion
- [ ] If either script exits with code 2 or unexpected output, the raw error is surfaced and the workflow stops (no partial fixes applied)
