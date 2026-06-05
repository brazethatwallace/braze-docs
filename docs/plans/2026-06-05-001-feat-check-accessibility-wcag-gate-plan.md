---
title: "feat: Rebuild check-accessibility skill as WCAG 2.2 AA gate"
date: 2026-06-05
status: active
origin: docs/brainstorms/2026-06-05-check-accessibility-wcag-gate-requirements.md
---

# feat: Rebuild check-accessibility skill as WCAG 2.2 AA gate

**Origin:** `docs/brainstorms/2026-06-05-check-accessibility-wcag-gate-requirements.md`

---

## Problem Frame

The `check-accessibility` skill currently acts as a regression checker for BD-6188 audit incidents and a table accessibility linter. Its reference material (`references/ada-issues-priority.md`) is organized by audit incident IDs, not WCAG criteria — making it impossible to verify coverage, and leaving major WCAG 2.2 AA criteria entirely unchecked (image alt text, non-descriptive link text, heading hierarchy, `lang` attribute, WCAG 2.2-new focus criteria).

This plan replaces the skill's knowledge base with a criterion-organized catalog and adds a content linting script to close the most impactful documentation-specific coverage gaps.

---

## Scope Boundaries

### In scope
- New `wcag-aa-docs-criteria.md` criterion catalog (replaces `ada-issues-priority.md`)
- New `scripts/check_content_accessibility.py` for content checks (alt text, link text, heading hierarchy, inline iframes)
- Updated `workflows/markdown-audit.md` to invoke both scripts
- Updated `workflows/architecture-audit.md` to reference WCAG criterion IDs and add three missing checks
- Updated `SKILL.md` entry point (description, allowed-tools, reference pointer)

### Deferred to Follow-Up Work
- CI workflow for `check_content_accessibility.py` (skill-only for now; consistent with pre-PR advisory mandate)
- Programmatic contrast ratio calculation for architecture checks (color contrast remains LLM judgment)
- Link destination title lookup for 2.4.4 fix suggestions
- Alt text quality assessment beyond presence/absence detection

### Non-goals
- Blocking CI gate — skill remains pre-PR advisory only
- Full-site audit tooling (Axe, Lighthouse integration)
- WCAG AAA criteria
- `_lang/` locale files

---

## Requirements

From the requirements document:

- **R1** — A contributor running the skill on a branch with violations receives: the WCAG criterion violated (with plain-English explanation), file and line, and a fix recommendation or auto-fix for high-confidence mechanical issues
- **R2** — A contributor running the skill on a clean branch receives an explicit all-clear
- **R3** — Reference material is organized by WCAG 2.2 AA criterion so coverage is auditable
- **R4** — `check_content_accessibility.py` outputs the same JSON schema as `check_table_accessibility.py`
- **R5** — Heading hierarchy violations are always low confidence (author judgment required)
- **R6** — BD-6188 audit history is preserved as `Historical context` footnotes within each relevant criterion entry

---

## Key Technical Decisions

**KTD1: Two-script sequential invocation in the markdown workflow.**
The markdown workflow invokes `check_table_accessibility.py` first, then `check_content_accessibility.py`. Both write to `/tmp/` with HEAD-SHA-suffixed filenames. After both complete, the workflow reads both output files and builds a merged findings list. Classification (confidence tier) runs once across the merged list. This avoids a combined script (fragile), a wrapper script (unnecessary abstraction), and separate classification passes (redundant logic). (see origin: `docs/brainstorms/2026-06-05-check-accessibility-wcag-gate-requirements.md`)

**KTD2: Decorative image detection is filename-heuristic only in the script.**
The script classifies images as likely-decorative based on filename patterns (`divider`, `spacer`, `bg-`, `icon-` prefix/suffix). Likely-decorative images auto-fix to `alt=""` at high confidence. All other images without alt text surface as medium confidence with an "add descriptive alt text" ask. The LLM can use surrounding context to suggest alt text during the ask step, but the script itself does not invoke the LLM.

**KTD3: `wcag-aa-docs-criteria.md` replaces `ada-issues-priority.md` — not supplements it.**
After the rebuild, `ada-issues-priority.md` is deleted. The architecture workflow's "Required Reading" directive is updated to point at the new catalog. BD-6188 history moves into `Historical context` footnotes in the new catalog, not a parallel file.

---

## High-Level Technical Design

### Markdown audit data flow (after this plan)

```
markdown-audit.md (workflow)
  ↓
Step 1: Collect changed files (md + html includes)
  ↓
Step 2a: python3 scripts/check_table_accessibility.py --json /tmp/table-$(sha).json [files]
Step 2b: python3 scripts/check_content_accessibility.py --json /tmp/content-$(sha).json [files]
  ↓
Step 3: Merge findings from both JSON files
         Apply confidence tier classification to each finding
         (Table findings: existing logic unchanged)
         (Content findings: use new type field to route classification)
  ↓
Step 4: Apply high-confidence auto-fixes
  ↓
Step 5: Present medium/low findings one at a time
  ↓
Step 6: Final summary
```

### `check_content_accessibility.py` violation types

| Violation type | WCAG | High confidence? | Auto-fix candidate |
|---|---|---|---|
| `image_missing_alt` | 1.1.1 | Conditional (decorative heuristic) | `alt=""` for decorative; ask for others |
| `nondescriptive_link` | 2.4.4 | No — always ask | Suggest replacement from context |
| `heading_skip` | 2.4.6 | No — always low confidence | Report only |
| `iframe_missing_title` | 4.1.2 | No — always ask | Add `title=""` |

### Architecture workflow criterion mapping (after this plan)

Old: P1-A, P1-B, P1-C, P2-A, P2-B, P2-C, P3-A, P3-B, P3-C, P4-A
New: WCAG 2.4.7, 2.4.1, 4.1.2, 1.4.3, 4.1.3, 2.4.3(new-tab), 4.1.2(iframes), 4.1.2(inputs), 1.3.1, + **added: 3.1.1, 2.4.11, 2.5.8**, P4-A retained as non-WCAG cleanup

---

## Implementation Units

### U1. Write `wcag-aa-docs-criteria.md` and retire `ada-issues-priority.md`

**Goal:** Replace the audit-incident reference with a WCAG 2.2 AA criterion catalog covering the documentation-specific subset.

**Requirements:** R3, R6

**Dependencies:** None

**Files:**
- `.github/skills/check-accessibility/references/wcag-aa-docs-criteria.md` — create
- `.github/skills/check-accessibility/references/ada-issues-priority.md` — delete (git rm)

**Approach:**
Each criterion entry uses the structure defined in the requirements doc:
- Criterion ID + name (WCAG shorthand)
- Plain English explanation for a docs contributor
- What to check (file types, patterns, specific things to look for)
- Check mechanism: `script: check_table_accessibility.py`, `script: check_content_accessibility.py`, `LLM judgment`, or `both`
- Auto-fixable: `yes (high confidence)`, `ask (medium)`, `ask (low)`, `no`
- Historical context: links to PRs where this was found/fixed on the Braze docs site (sourced from existing entries in `ada-issues-priority.md`)

Criteria to include (from the requirements WCAG criterion table):
- Content path: 1.1.1, 2.4.4, 1.3.1, 2.4.6, 4.1.2 (iframes in markdown)
- Architecture path: 2.4.7, 2.4.1, 1.4.3, 4.1.2 (full), 4.1.3, 2.4.3 (new-tab context), 3.1.1, 2.4.3 (focus order), 1.4.11, 2.4.11, 2.5.8
- Non-WCAG: P4-A (obsolete meta tags) — retained as cleanup opportunity with note that it is not a WCAG requirement

**Test scenarios:**
- Verify each criterion in the WCAG table from the requirements doc has a corresponding entry
- Verify every entry has all required fields (Plain English, What to check, Check mechanism, Auto-fixable, Historical context where applicable)
- Verify BD-6188 historical context from `ada-issues-priority.md` is preserved under the relevant entries (not dropped)
- Verify P4-A is clearly labeled as non-WCAG

**Verification:** `ada-issues-priority.md` no longer exists; `wcag-aa-docs-criteria.md` exists and has entries for all 15+ criteria in scope.

---

### U2. Write `scripts/check_content_accessibility.py`

**Goal:** New script for content accessibility checks: alt text presence, non-descriptive link text, heading hierarchy skips, inline iframe titles.

**Requirements:** R1, R2, R4, R5

**Dependencies:** None

**Files:**
- `scripts/check_content_accessibility.py` — create
- `scripts/tests/test_check_content_accessibility.py` — create (optional but strongly recommended)

**Approach:**
CLI signature mirrors `check_table_accessibility.py`:
```
python3 scripts/check_content_accessibility.py [file1.md] [file2.md ...] [--json output.json]
```

Exit codes: `0` = no violations, `1` = violations found, `2` = script error.

JSON output schema matches `check_table_accessibility.py`'s schema, with these additions per violation object:
- `violation_type`: one of `image_missing_alt`, `nondescriptive_link`, `heading_skip`, `iframe_missing_title`
- `wcag_criterion`: e.g., `"1.1.1"`, `"2.4.4"`, `"2.4.6"`, `"4.1.2"`

Parsing approach per violation type:
- **`image_missing_alt`** — regex match on markdown image syntax `!\[([^\]]*)\]\(([^)]+)\)`. Flag when alt text group is empty. Classify as likely-decorative when the image path contains: `divider`, `spacer`, `separator`, `bg-`, `background`, `icon-` as filename components. `suggestion_content` for decorative: `![](original_src)`. For informational (non-empty path, no decorative signal): `suggestion_content` is `"Add descriptive alt text describing what this image shows"` with `fix_hint` showing the correct syntax.
- **`nondescriptive_link`** — regex match on `\[([^\]]+)\]\(([^)]+)\)`. Non-descriptive text list: `here`, `click here`, `this`, `this link`, `this page`, `learn more`, `read more`, `more`, `link`, `click`, `see more`, `details`. Match case-insensitively, strip punctuation. `suggestion_content` is the raw link text + surrounding sentence for context.
- **`heading_skip`** — parse all heading lines (`^#{1,6}\s`) in order. Flag when level increases by more than 1 (e.g., h2 → h4). `suggestion_content` describes the skip with the line range.
- **`iframe_missing_title`** — regex for `<iframe` in markdown (inline HTML). Flag if no `title="..."` attribute present. `suggestion_content` is the iframe tag with a `title=""` placeholder.

Scope guard: process only changed files passed as arguments. Do not walk the full repo.

**Test scenarios:**
- `![](image.png)` in a markdown file → `image_missing_alt` violation with decorative suggestion (empty path signals decorative)
- `![Description](image.png)` → no violation
- `![](divider.svg)` → `image_missing_alt` with `suggestion_content` = `![](divider.svg)` (decorative heuristic: "divider" in filename)
- `[click here](https://example.com)` → `nondescriptive_link` violation
- `[View documentation](https://example.com)` → no violation
- h2 followed immediately by h4 in same file → `heading_skip` violation
- h2 → h3 → h4 → no violation
- `<iframe src="...">` (no title) → `iframe_missing_title` violation
- `<iframe src="..." title="Embedded form">` → no violation
- Empty file → exit code 0, empty violations array
- File with no markdown images/links/headings/iframes → exit code 0
- `--json` flag writes to the specified path; without `--json`, prints violations as human-readable text to stdout

**Verification:** `python3 scripts/check_content_accessibility.py` on a test file with known violations produces correct JSON output matching the schema; exit codes are correct.

---

### U3. Update `workflows/markdown-audit.md` to invoke both scripts

**Goal:** Extend the markdown audit workflow to run `check_content_accessibility.py` alongside the existing table script and merge findings before classification.

**Requirements:** R1, R4

**Dependencies:** U2

**Files:**
- `.github/skills/check-accessibility/workflows/markdown-audit.md` — modify

**Approach:**
Step 2 becomes two sub-steps:

**Step 2a** — Run table script (unchanged):
```bash
python3 scripts/check_table_accessibility.py --json /tmp/a11y-table-$(git rev-parse --short HEAD).json [files]
```

**Step 2b** — Run content script:
```bash
python3 scripts/check_content_accessibility.py --json /tmp/a11y-content-$(git rev-parse --short HEAD).json [files]
```

If either script errors (exit code 2): surface the error and stop (no partial fixes).

After both scripts complete, read both JSON files. Merge into a single findings list ordered by: file, then line number ascending. Violations from both scripts enter the same confidence tier classification pass in Step 3.

**Confidence tier additions for content violations:**
- `image_missing_alt` + decorative heuristic match → high confidence
- `image_missing_alt` + no decorative signal → medium confidence
- `nondescriptive_link` → medium confidence (always ask — surrounding context needed)
- `heading_skip` → low confidence (always — author must judge intent)
- `iframe_missing_title` → medium confidence (always ask)

**Step 4 auto-fix additions:**
When applying auto-fixes for `image_missing_alt` (decorative), use StrReplace to replace `![](src)` with `![](src)` — the alt attribute is already empty, so the fix is confirming it is correct by adding an explicit empty string. Actually, empty markdown alt is written as `![ ](src)` or `![](src)` which is already valid empty alt. The "fix" here is a verification pass, not a textual change. In the auto-fix step, report these as verified rather than modified.

**Step 5 additions:**
For `image_missing_alt` (informational), add an option: **Generate alt text suggestion** — I'll describe what this image shows based on surrounding context. Apply when the user accepts.

For `nondescriptive_link`, show: the offending link text, the URL, and 1-2 sentences of surrounding context. Options: **Accept suggestion** (if the LLM can generate one), **Provide custom text**, **Skip**.

For `heading_skip`, show: the heading levels involved, the lines. Options: **Acknowledge** (I'll fix manually), **Skip**.

**Step 6 summary** — retain existing table format; add rows for content violation types.

The title of the audit section changes from "Table accessibility audit complete" to "Content accessibility audit complete" to reflect the broader scope.

**Test scenarios:**
- Workflow invoked on a file with table violations only → Step 2b produces empty JSON; Step 3 processes only table findings; outcome matches existing behavior
- Workflow invoked on a file with content violations only → Step 2a produces exit 0 (no tables flagged); Step 3 processes content findings; auto-fixes applied where appropriate
- Workflow invoked on a file with both types → findings merged, ordered by line number, processed in a single pass
- Step 2b errors (exit code 2) → error reported, workflow stops, no fixes applied
- Non-interactive mode (`ci` or `headless` in `$ARGUMENTS`) → content violations follow same skip-all-asks behavior as table violations

**Verification:** Running the skill on a file with a missing-alt image produces a violation with the correct WCAG criterion, confidence tier, and fix option.

---

### U4. Update `workflows/architecture-audit.md` for WCAG criterion IDs and new checks

**Goal:** Replace BD-6188 incident IDs (P1-A etc.) with WCAG criterion references, and add three checks missing from the current workflow: language of page (3.1.1), focus not obscured (2.4.11), target size minimum (2.5.8).

**Requirements:** R1, R3

**Dependencies:** U1

**Files:**
- `.github/skills/check-accessibility/workflows/architecture-audit.md` — modify

**Approach:**
In the Required Reading directive at the top, change reference from `ada-issues-priority.md` to `wcag-aa-docs-criteria.md`.

In Step 1 (file-type to checks mapping), replace the `P1-A` style IDs with WCAG criterion references. Example:

| File type | Checks to run |
|---|---|
| CSS/SCSS | 2.4.7 (focus visible), 1.4.3 (contrast), **2.4.11 (focus not obscured)**, **2.5.8 (target size)** |
| Layouts, root HTML | 2.4.1 (skip nav), 4.1.2 (ARIA), 4.1.2 (iframes), 1.3.1 (heading semantics), **3.1.1 (lang attribute)**, P4-A (meta tags) |
| `_includes/*.html` | 4.1.2 (ARIA), 4.1.3 (live regions), 2.4.3 (new-tab), 4.1.2 (iframes), 4.1.2 (input labels), 1.3.1 (heading) |
| JS | 4.1.3 (live regions), 4.1.2 (dynamic ARIA) |

For each check in Step 2, prepend the criterion ID to the heading. Example: "**WCAG 2.4.7 — Focus Visible**" rather than "**P1-A — Focus rings**". Keep the check logic itself unchanged.

**Add three new checks to Step 2:**

**3.1.1 — Language of page** (layout files only):
- Grep changed `_layouts/` and root `.html` files for `<html` tag
- Verify `lang="[two-letter-code]"` attribute is present and non-empty
- Flag if `lang` is missing or set to an empty string

**2.4.11 — Focus Not Obscured** (CSS/SCSS files):
- Look for `position: sticky`, `position: fixed`, or `z-index` changes in CSS/SCSS
- Flag when sticky/fixed elements are introduced or modified without a corresponding note about keyboard focus behavior
- Guidance: sticky headers that cover focused elements are a WCAG 2.2 new violation. Flag any new or modified sticky/fixed positioning for manual verification.
- Do not compute overlap — flag the pattern and ask the author to verify

**2.5.8 — Target Size Minimum** (CSS/SCSS files):
- Look for new button, link, or interactive element size definitions in changed CSS
- Flag when `width` or `height` is set to a value below 24px (CSS px) on an element that appears to be interactive (`.btn`, `button`, `a`, `.nav-link`, `.tab`, `.icon-btn`, or similar class patterns)
- Note: WCAG 2.5.8 requires 24×24 CSS px minimum; flag candidates below this threshold for author verification

**Step 3 / Step 4** — update criterion IDs in finding format:
```
[WCAG criterion ID] [Criterion name]
File: path/to/file.html (line N)
Found: [quoted pattern]
Why it matters: [one sentence]
Fix: [what the author should do]
```

**Test scenarios:**
- A changed layout file missing `lang="en"` on `<html>` → 3.1.1 finding
- A CSS file adding `position: sticky` to a header → 2.4.11 finding flagging for manual verification
- A CSS file setting `.icon-btn { width: 16px; height: 16px }` → 2.5.8 finding
- A clean CSS file with no new color values, no outline removal, no small targets → no findings; architecture audit complete message
- Findings report uses WCAG IDs (e.g., "WCAG 2.4.7") not BD-6188 IDs (e.g., "P1-A") in output

**Verification:** Architecture audit on a test HTML file with a missing `lang` attribute produces a 3.1.1 finding. Architecture audit on a clean CSS file produces no findings.

---

### U5. Update `SKILL.md` entry point

**Goal:** Update the skill's name, description, allowed-tools, and internal reference pointer to match the rebuilt skill.

**Requirements:** R1, R3

**Dependencies:** U1, U2, U3, U4

**Files:**
- `.github/skills/check-accessibility/SKILL.md` — modify

**Approach:**
- Update `description` to reflect WCAG 2.2 AA scope: "Pre-PR WCAG 2.2 AA gate for Braze Docs contributors. Runs before opening a PR to check documentation and architecture changes against the documentation-relevant subset of WCAG 2.2 Level AA. Detects changed file types and routes automatically: architecture changes (layouts, JS, CSS, templates) are audited against WCAG 2.2 AA criteria; markdown changes run two accessibility scripts (table + content) with confidence-gated auto-fixing."
- Update `allowed-tools` to include `Bash(python3 scripts/check_content_accessibility.py*)` alongside the existing tools
- Update Core Principle 3 (`Priority × impact ordering`) to reference `wcag-aa-docs-criteria.md` instead of `ada-issues-priority.md`
- Update the all-clear example output from:
  > No table accessibility violations found in the 2 changed markdown file(s).
  to:
  > Content accessibility audit complete — no violations found in the 2 changed markdown file(s).
- The examples section may need minor updates to match the new all-clear output format

**Test scenarios:**
- `name:` field in frontmatter remains `check-accessibility`
- `allowed-tools:` includes both script invocations
- Core Principle 3 points to `wcag-aa-docs-criteria.md`
- Description accurately describes WCAG 2.2 AA scope (not ADA/ABA audit scope)

**Verification:** `SKILL.md` frontmatter is valid; `allowed-tools` includes both scripts; description no longer references ADA audit findings.

---

## Risks & Dependencies

| Risk | Likelihood | Mitigation |
|---|---|---|
| `check_content_accessibility.py` decorative image heuristic produces false positives | Medium | Heuristic fires medium-confidence "ask" for informational images; only confirmed decorative filenames auto-fix. Authors can override. |
| Heading skip detection breaks on YAML frontmatter or code blocks containing `#` | Low | Script should ignore content inside code fences (` ``` ` delimiters) and YAML frontmatter (`---` block at file start) when parsing heading levels |
| Merged findings list ordering causes confusion if table and content violations interleave | Low | Merge by line number; clearly label each finding's type and WCAG criterion so interleaving is self-explanatory |
| Architecture workflow becomes verbose with WCAG IDs that contributors don't recognize | Low | Each criterion entry in `wcag-aa-docs-criteria.md` has a plain-English explanation; the architecture workflow output should include a one-sentence plain-English note, not just the criterion number |

---

## Deferred Implementation Notes

- The exact regex patterns for non-descriptive link text will benefit from testing against real `_docs/` files before finalizing the pattern list
- "Decorative image" filename heuristics should be expanded as false positives are discovered in real use
- Heading skip detection needs to decide how to handle ATX headings inside blockquotes or nested list items — conservative approach: skip those lines

---

## Sources & Research

- Requirements doc: `docs/brainstorms/2026-06-05-check-accessibility-wcag-gate-requirements.md`
- Existing skill entry point: `.github/skills/check-accessibility/SKILL.md`
- Existing table script: `scripts/check_table_accessibility.py`
- Existing markdown audit workflow: `.github/skills/check-accessibility/workflows/markdown-audit.md`
- Existing architecture audit workflow: `.github/skills/check-accessibility/workflows/architecture-audit.md`
- Existing ADA issues reference: `.github/skills/check-accessibility/references/ada-issues-priority.md`
- WCAG 2.2 specification: https://www.w3.org/TR/WCAG22/
