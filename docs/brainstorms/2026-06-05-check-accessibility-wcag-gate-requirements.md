# check-accessibility: WCAG 2.2 AA Gate — Requirements

**Date:** 2026-06-05
**Status:** Draft
**Replaces:** existing `check-accessibility` skill built from BD-6188 audit findings

---

## Problem

The `check-accessibility` skill (`/Users/breanna.fitzgerald/braze-docs/.github/skills/check-accessibility/`) currently acts as a regression checker for known BD-6188 audit incidents and a table accessibility linter. It is not a WCAG 2.2 AA gate.

Gaps identified:
- No check for image alt text (WCAG 1.1.1 — the most common documentation accessibility violation)
- No check for non-descriptive link text ("here", "click here") (WCAG 2.4.4)
- No check for heading hierarchy skips (WCAG 1.3.1, 2.4.6)
- No check for `lang` attribute on architecture changes (WCAG 3.1.1)
- Reference material organized by audit incident IDs, not WCAG criteria — makes it hard to verify coverage

---

## Goal

Rebuild `check-accessibility` so it accurately encodes WCAG 2.2 Level AA compliance requirements for a Jekyll markdown documentation site. When a contributor runs the skill before opening a PR, they can trust that passing the skill means no WCAG 2.2 AA violations in their changed files.

---

## Users

- **Docs contributors** — writers, PMs, engineers editing `_docs/` or `_includes/`. May have no accessibility background. The skill must tell them what's wrong and how to fix it, not just cite criterion IDs.
- **Docs reviewers / TL** — running the skill before approving a PR to confirm the branch is clean.

---

## Outcomes

1. A contributor running the skill on a branch with accessibility violations receives: the criterion violated (with plain-English explanation), the exact file and line, and a fix recommendation or auto-fix for high-confidence mechanical issues.
2. A contributor running the skill on a clean branch receives a clear all-clear, not silence.
3. The reference material is organized by WCAG 2.2 AA criterion, making it auditable: given a criterion number, anyone can verify what the skill checks and confirm coverage.
4. The skill covers the documentation-relevant WCAG 2.2 AA subset — not criteria that don't apply to a static Jekyll docs site (animations, video captions, timing).

---

## Non-Goals

- Hard blocking / CI enforcement — this is pre-PR advisory only
- Full-site audit tooling (Axe, Lighthouse) — out of scope
- WCAG AAA criteria
- Locale files (`_lang/`) — already excluded; no change
- Automated heading-level rewrites — heading hierarchy is reported, not auto-fixed (changing heading levels risks altering document structure in ways only the author can judge)

---

## Scope

### File routing (unchanged)

| Pattern | Path |
|---|---|
| `_layouts/**`, `_includes/**/*.html`, `assets/js/**`, `assets/css/**`, `assets/scss/**`, `_config*.yml`, `*.html` at root, `Gemfile`, `package.json`, `.github/workflows/**` | Architecture audit |
| `_docs/**/*.md`, `_includes/**/*.md`, `_includes/**/*.html` | Content (markdown) audit |
| `_lang/**` | Skip |
| `_includes/**/*.html` | Both paths |

### WCAG 2.2 AA documentation-site criterion subset

These are the criteria applicable to a Jekyll markdown documentation site, organized by where they fire.

#### Content path (markdown / HTML include files)

| Criterion | What | Check mechanism | Auto-fixable |
|---|---|---|---|
| **1.1.1 Non-text Content** | Missing alt text on images; empty alt on non-decorative images | New script (`check_content_accessibility.py`) + LLM judgment for quality | High confidence: add `alt=""` to decorative images; ask for others |
| **2.4.4 Link Purpose** | Non-descriptive link text ("here", "click here", "this link", "learn more", "read more") | New script — pattern match on link text | Ask (suggest replacement from surrounding context or link target) |
| **1.3.1 Info and Relationships** | Table accessible names | Existing `check_table_accessibility.py` | Existing confidence-gated auto-fix |
| **2.4.6 Headings and Labels** | Heading hierarchy skips (e.g., h2 → h4 without h3) | New script — parse heading levels per file | Report only (author must resolve) |
| **4.1.2 Name, Role, Value** | Missing `title` on iframes embedded in markdown | New script — pattern match | Ask |

#### Architecture path (layout, CSS, JS files)

| Criterion | What | Check mechanism | Auto-fixable |
|---|---|---|---|
| **2.4.7 Focus Visible** | CSS that removes or suppresses focus rings | LLM reading changed CSS/SCSS files | No — CSS scope judgment required |
| **2.4.1 Bypass Blocks** | Missing skip navigation link in layout templates | LLM reading changed layout files | No |
| **1.4.3 Contrast (Minimum)** | Color definitions below 4.5:1 (text) / 3:1 (large text) | LLM reading changed CSS/SCSS | No |
| **4.1.2 Name, Role, Value** | Missing/incorrect ARIA attributes in templates | LLM reading changed HTML/layout files | No |
| **4.1.3 Status Messages** | Live regions in JS/templates | LLM reading changed JS | No |
| **3.1.1 Language of Page** | Missing or incorrect `lang` attribute on `<html>` | Script — grep for `lang=` in changed layout files | Ask |
| **2.4.3 Focus Order** | Tab order issues in templates | LLM | No |
| **1.4.11 Non-text Contrast** | UI component border/icon contrast (3:1) | LLM reading CSS | No |
| **2.4.11 Focus Not Obscured (2.2 new)** | Sticky/fixed headers covering keyboard focus | LLM reading CSS/JS | No |
| **2.5.8 Target Size Minimum (2.2 new)** | Interactive element below 24×24 CSS px | LLM reading CSS | No |
| **P4-A (non-WCAG)** | Obsolete meta tags | Existing check — retained as cleanup opportunity | May auto-remove on explicit user request |

---

## New artifact: `wcag-aa-docs-criteria.md`

Replaces `ada-issues-priority.md` as the primary reference for the skill. Structure per entry:

```
## [Criterion ID] [Criterion Name]
**Plain English:** What this means for a docs contributor.
**What to check:** Specific patterns, file types, things to look for.
**Check mechanism:** Script name / LLM / both.
**Auto-fixable:** Yes (high confidence) / Ask (medium) / No.
**Historical context:** Links to PRs where this was found/fixed in the Braze docs site.
```

The BD-6188 audit history is preserved as `Historical context` footnotes within each applicable criterion entry. It is no longer the primary organizing structure.

---

## New script: `check_content_accessibility.py`

A companion to `check_table_accessibility.py`. Handles the content-path structural checks:
- **1.1.1** — Detect images with empty alt and classify as likely decorative vs. likely informational (based on filename heuristics: `divider`, `spacer`, `bg-`, `icon-` → likely decorative; anything else → informational, ask)
- **2.4.4** — Detect links where visible text matches a non-descriptive pattern list
- **2.4.6** — Parse heading hierarchy per file, flag skips
- **4.1.2 (iframes)** — Detect `<iframe>` without `title` attribute

Output: same JSON schema as `check_table_accessibility.py` so the markdown workflow can consume both with a single classification pass.

---

## Confidence tier changes

The existing confidence tier system applies unchanged to the new checks. Additional rule:
- All heading hierarchy violations are **low confidence** — changing heading levels requires author judgment about document structure

---

## Skill structure changes

| File | Change |
|---|---|
| `.github/skills/check-accessibility/SKILL.md` | Update name + description to reflect WCAG 2.2 AA scope; update allowed-tools to include new script |
| `.github/skills/check-accessibility/references/ada-issues-priority.md` | Replace with `wcag-aa-docs-criteria.md` |
| `.github/skills/check-accessibility/workflows/architecture-audit.md` | Update to reference WCAG criterion IDs; check list gains `lang` attribute and 2.2-new criteria |
| `.github/skills/check-accessibility/workflows/markdown-audit.md` | Step 1 runs both scripts; Step 3 classification unchanged in mechanism, now covers new violation types |
| `scripts/check_content_accessibility.py` | New file |

---

## Success criteria

- [ ] Contributor running the skill on a branch that adds `![](image.png)` (no alt) receives a 1.1.1 violation with a fix recommendation
- [ ] Contributor running the skill on a branch with `[click here](url)` receives a 2.4.4 violation
- [ ] Contributor running the skill on a branch that skips h2→h4 receives a 2.4.6 report
- [ ] Architecture changes to CSS that remove `outline` receive a 2.4.7 finding
- [ ] All findings cite the WCAG criterion ID and plain-English explanation
- [ ] `wcag-aa-docs-criteria.md` covers all criteria in the table above; each entry has a complete "what to check" section
- [ ] A clean branch produces an explicit all-clear message, not silence
- [ ] `check_content_accessibility.py` outputs the same JSON schema as `check_table_accessibility.py`

---

## Assumptions

- The BD-6188 audit findings all map to WCAG criteria (verified: they do, with P4-A being the only exception — it's a cleanup item, not a WCAG requirement)
- `check_table_accessibility.py` continues to own table checks; the new script does not duplicate them
- Heading hierarchy analysis can be done reliably by parsing heading tokens in markdown (confirmed by inspection of existing docs format)
- The decorative/informational image heuristic (filename-based) will have false positives; these surface as medium-confidence "ask" items, not auto-fixes

---

## Out of scope for this implementation

- **Automated color contrast calculation** — contrast checks in the architecture path remain LLM judgment (reading CSS values), not programmatic computation. A follow-up could add a proper contrast calculation library.
- **Link destination title lookup** — 2.4.4 fix suggestions for link text could be enhanced by fetching the destination page title. Deferred.
- **Alt text quality assessment** — the script detects presence/absence. LLM judgment during the "ask" step can evaluate quality. A future enhancement could add a structured LLM quality check to the high-confidence alt text auto-fix candidates.
