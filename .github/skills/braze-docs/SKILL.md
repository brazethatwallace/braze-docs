---
name: braze-docs
description: >
  Use when drafting, editing, or reviewing markdown under `_docs/` or root
  `_includes/` in the braze-docs repo — including fixing broken links, updating
  cross-references, adding Liquid formatting (alerts, tabs, images), or resolving
  merge conflicts in documentation branches. English canonical source only;
  `_lang/` is out of scope unless the user explicitly requests locale work.
---

# Braze Docs

## Context
- Current branch: !`git branch --show-current`
- Modified files: !`git diff --name-only HEAD`

## Mode detection

Detect mode from $ARGUMENTS first, then modified files, then ask.

| Signal | Mode | Load |
|--------|------|------|
| $ARGUMENTS: "conflict", "merge", "resolve" | **Conflict** | *(workflow is in this file)* |
| $ARGUMENTS: "redirect", "mredirects", "ulinks", "broken_redirect" | **Redirects** | **REQUIRED SUB-SKILL:** [redirect-management](../redirect-management/SKILL.md) |
| $ARGUMENTS: "link", "broken" | **Links** | [site-conventions.md](references/site-conventions.md) |
| $ARGUMENTS: "write", "draft", "create", "new" | **Write** | [writing-style.md](references/writing-style.md) |
| $ARGUMENTS: "review", "audit", "style", "check", "style qa", "qa style" | **Review** | [writing-style.md](references/writing-style.md), [glossary.md](references/glossary.md); for pre-PR diff checks use [style-qa-changed-files.md](workflows/style-qa-changed-files.md) |
| $ARGUMENTS: "css", "layout", "component", "include", "i18n", "custom" | **Custom** | *(workflow is in this file — see Custom components and CSS)* |
| Modified files include `broken_redirect_list.js` | **Redirects** | **REQUIRED SUB-SKILL:** [redirect-management](../redirect-management/SKILL.md) |
| Modified files show conflict markers or branch matches `merge/*` | **Conflict** | *(workflow is in this file)* |
| Modified files are under `_docs/` with no link/conflict signals | **Write** | [writing-style.md](references/writing-style.md) |

If mode is still ambiguous, ask: "What are you working on?"

Treat bare `qa` by itself as ambiguous. Ask a follow-up instead of auto-routing
to Review mode.

If AskUserQuestion is available:
- **Writing or editing content** — Drafting new articles or updating existing ones → **Write**
- **Fixing broken links** — Broken cross-references or internal links in Markdown (not `broken_redirect_list.js`) → **Links**
- **Managing redirects** — Adding, updating, or validating entries in `broken_redirect_list.js` → **Redirects** (**REQUIRED SUB-SKILL:** [redirect-management](../redirect-management/SKILL.md))
- **Resolving merge conflicts** — Conflicts between branches → **Conflict**
- **Reviewing for style** — Checking existing content against style standards → **Review**

Otherwise ask: "What are you working on? (1) Writing/editing content, (2) Fixing broken links, (3) Managing redirects (`broken_redirect_list.js`), (4) Resolving merge conflicts, (5) Reviewing for style"

## Overview

Writing, structuring, and linking Braze documentation. References load by mode
(see above). For the canonical source of truth on any topic, consult the style
guide files listed below.

## Gotchas

- **Don't resolve merge conflicts in bulk without an approved written plan**, because conflict resolution must match the PR's intent and the user must stay in control. Do the full **Merge conflicts** workflow below instead of guessing.
- **Don't draft new content before searching `_docs/` (and root `_includes/`) for existing coverage**, because duplicate or rephrased prose drifts, bloats the site, and hides the single source of truth. When coverage exists, tighten or correct that content or add a short cross-link instead.
- **Don't write comprehensive speculative copy to fill gaps you haven't verified**, because confident-sounding filler drives hallucinations. Prefer the smallest accurate edit; when you draw on another article, style guide section, or product/SDK behavior, cite the source inline — for example: `[_docs/_user_guide/path/to/page.md]` or article title in brackets — so the author can confirm. Omit internal paths from public PR descriptions.
- **Don't treat `_lang/` as the place to fix English canonical issues**, because the translation pipeline owns localized files. See **Locale and English source** for the exception.

## Merge conflicts

When the user is in a merge conflict (or asks for help with one):

1. **Gather context** — Use the feature branch name, changed files, and the PR title/description or the user's stated goal so you know what the change is trying to achieve.
2. **Summarize conflicts** — For each conflicted file (or region), state what each side is doing (for example "main added X; our branch moved Y") in plain language, not only conflict markers.
3. **Propose a resolution plan** — Tie recommendations to the end goal: what to keep, what to merge, what to drop, and any follow-up edits (links, redirects, style). Call out risky spots (redirect lists, shared `_includes/`, generated or high-churn files).

**Wait gate:** Do not proceed to step 4 until the user responds with explicit approval of the plan.

4. **Apply all resolutions** — Resolve every conflict agreed in the plan in one comprehensive pass. Do not stop mid-conflict or ask for re-confirmation; the approval above covers the full plan. Run a consistency pass (links, frontmatter, style) and report what changed file-by-file.

If the user wants only analysis, stop after step 3.

## Style guide source files

| Path | Use for |
|------|---------|
| `docs/contributing/style_guide.md` | Parent index — start here |
| `docs/contributing/style_guide/writing_style_guide.md` | Writing style, voice, tone, grammar, punctuation, formatting |
| `docs/contributing/style_guide/image_style_guide.md` | Image styling, cropping, alt text, screenshots |
| `docs/contributing/style_guide/alerts.md` | Important, Note, Tip, Warning alerts — when and how to use |
| `docs/contributing/style_guide/product_feedback_ctas.md` | In-article product feedback include (`product_feedback_cta.md`) — contexts, placement, reviewer checklist |
| `docs/contributing/style_guide/api_endpoint_guidelines.md` | API endpoint article structure and formatting |

When the full style guide has specific guidance on a topic, defer to the source file over this summary.

## Writing style summary

The Braze voice is **straightforward**, **empowering**, and **human**. Key rules:

- Active voice. Present tense. Second person ("you"). Imperative for instructions.
- Standard contractions (you're, can't). No noun+verb contractions (Braze'll).
- Oxford comma required. Sentence case for headings.
- Never use "simple", "simply", "just", "easy" in instructions.
- Avoid "not X, but Y" antithesis. State the positive directly; use before/after framing for contrast.
- Use "customers" for brands, "consumers" for their end users, "company users" for platform users. Never "clients".
- Descriptive link text. Never "Learn more", "here", "click here".
- Use gender-neutral pronouns. Avoid ableist language.

For the complete writing rules, load [references/writing-style.md](references/writing-style.md) (loaded automatically in Write and Review modes).

## Site structure

Jekyll site. Collections dir: `_docs/`. Base URL: `/docs`.

| Collection | Folder | Content |
|---|---|---|
| user_guide | `_user_guide/` | Product docs for dashboard users |
| developer_guide | `_developer_guide/` | SDK integration and developer docs |
| api | `_api/` | REST API endpoint docs |
| partners | `_partners/` | Technology partner integrations |
| releases | `_releases/` | Release notes |
| help | `_help/` | Troubleshooting and support |

Contributor handbook (not a Jekyll collection): `docs/contributing/` in this repository.

Permalink pattern: `./:collection/:path/` (Jekyll build paths). Production URLs omit trailing slashes (`vercel.json` `trailingSlash: false`); use no-slash paths in links, redirects, and canonical targets.

## Locale and English source

- **Routine work:** Edit markdown under `_docs/` (all collections) and root `_includes/` for shared snippets. Do not create, edit, move, rename, or delete files under `_lang/` during normal article updates, link fixes, redirects follow-up, or style edits.
- **Why:** Localized pages are updated by Braze's separate translation process; editing `_lang/` in the same PR as English changes risks drift or conflicts with that pipeline.
- **Broken links and verification:** When resolving links for English pages, treat canonical targets as `_docs/...` and root `_includes/...` as appropriate. Reading `_lang/` for comparison or existence checks is fine; **writes** to `_lang/` stay off limits unless the user asked for that scope.
- **Exception:** If the user clearly asks to update a specific locale, fix a translation bug, or work only in `_lang/`, follow that instruction for that task.

## YAML frontmatter

Every doc file requires YAML frontmatter. Required fields:

```yaml
---
nav_title: Permissions
article_title: Company user permissions
page_order: 1
page_type: reference
description: "This reference article covers how user permissions work at Braze."
---
```

| Field | Purpose | Notes |
|---|---|---|
| `nav_title` | Sidebar navigation label | Short, scannable |
| `article_title` | Page title (H1) | Descriptive, sentence case |
| `page_order` | Sort position in nav | Integer, lower = higher |
| `page_type` | Content type | `reference`, `glossary`, `landing`, `solution` |
| `description` | SEO meta description | Wrap in quotes |

Optional fields: `tool`, `noindex`, `hidden`, `layout`, `local_redirect`, `search_rank`.

## Internal linking

```markdown
[Link text]({{site.baseurl}}/user_guide/path/to/page)
```

- Always use `{{site.baseurl}}` (resolves to `/docs`). Do not add a trailing slash on internal links.
- Anchor links: `{{site.baseurl}}/user_guide/path/to/page#heading-slug`
- Same-page anchors: `[heading text](#heading-slug)`
- Never use "Learn more", "here", or "click here" as link text.
- Standard cross-reference phrase: "To learn more, refer to [Topic](...)." or "For more information, see [Topic](...)."

For broken link detection, redirect rules, Liquid syntax, and page anatomy, load [references/site-conventions.md](references/site-conventions.md) (loaded automatically in Links mode).

## Feedback includes

Three parameterized includes cover in-article feedback. Do not mix them:

| Include | Use for |
|---------|---------|
| `_includes/product_feedback_cta.md` | Product capability gaps, enhancement asks, GA feature adoption feedback, dashboard UX friction |
| `_includes/developer_guide/_shared/tutorial_feedback.md` | Developer tutorial format pilots (Google Form) |
| `_includes/accessibility/feedback.md` | Accessibility of Braze or messages |

**Product feedback CTAs** — new CTAs in `_docs/` and root `_includes/` must use `product_feedback_cta.md`, not ad hoc portal links. Full guidance: `docs/contributing/style_guide/product_feedback_ctas.md`.

Invocation:

```liquid
{% multi_lang_include product_feedback_cta.md context="gap" feature="per-domain sending for email templates" %}
```

- `context`: `gap`, `new_feature`, or `pain_point` (with `channel: feature` or `ux` when `context` is `pain_point`)
- **Inline placement:** same line as the limitation sentence, with a space before `{% multi_lang_include ... %}` so the CTA stays in the same Markdown paragraph

## Custom components and CSS

Use this section when adding new `_includes/` components, custom CSS in `assets/css/_content.scss`, or page-specific layouts.

### CSS specificity hierarchy

Rules in `_tabs.scss` and `_content.scss` are nested inside `#main_content #article-main { ... }`, giving them effective specificity ~(2,1,x). New rules added at file root have specificity ~(0,1,0) and will silently lose to the global rules. Resolve with `!important` on the override — do not restructure the nesting.

### Known global bleeds into custom components

Any new HTML inside `#main_content` inherits these rules — plan for explicit overrides:

| Rule | Effect | Override |
|------|--------|----------|
| `#main_content p { margin-bottom: 25px }` | Adds large bottom margin to every `<p>` inside your component | `margin-bottom: 0 !important` on the element |
| `#main_content img { border: 1px solid ... }` | Adds a border to every `<img>` inside your component | `border: none !important` on the element |

### Margin collapsing in SDK tab panes

`.sdk-tab-content` and `.sdk-ab-sub_tab-content` both have `padding: 0` and no border, so `margin-top` on their first child collapses through both parents and produces no visible gap. Use `padding-top` on a scoped wrapper div instead — padding does not collapse.

### Page-scoping CSS without `page_class`

The site has no `page_class` frontmatter support. To scope styles to a single page:

1. Wrap the relevant content in a `<div class="semantic-page-name">` directly in the markdown file.
2. Add the CSS rule targeting that wrapper in `assets/css/_content.scss`.
3. Add `!important` — the global high-specificity rules will otherwise win.

Example: a prompt library page wraps its tab block in `<div class="prompt-library-tabs">` and the CSS targets `.prompt-library-tabs .sdk-tab-content { padding-top: 16px !important }`.

### i18n for user-facing strings in includes

All user-visible text added to `_includes/` files must be localized:

1. Add the key to **all 7 language blocks** in `_data/i18n.yml`: `en`, `fr`, `ja`, `ko`, `pt-br`, `es`, `de`.
2. Access in Liquid: `{{ site.data.i18n[site.language].key | default: "English fallback" }}`.
3. Use `site.language` — **not** `site.lang` (that variable is always nil).
4. Access in JavaScript via the `site_i18n` global (injected by `_includes/html_include.html`). Always guard: `(typeof site_i18n !== 'undefined' && site_i18n['key']) ? site_i18n['key'] : 'English fallback'`.

## Key glossary

- **Canvas** — Always capitalized. Plural: Canvases.
- **workspace** — Not "app group" (deprecated term).
- **capacity** — Use instead of "limit" for custom data constraints.
- **eCommerce** — Not "ecommerce" or "e-commerce".
- Avoid: "via" (use "through"), "e.g." (use "for example"), "i.e." (use "that is").
- Avoid: "out-of-the-box" (use "default"), "whitelist" (use "allowlist"), "blacklist" (use "blocklist").

For the full glossary, load [references/glossary.md](references/glossary.md) (loaded automatically in Review mode).

## Pre-PR Style QA

When finishing prose edits and opening a PR (including via
[create-pr](../create-pr/SKILL.md) or the feedback-handler agent), run the
non-interactive checklist in
[workflows/style-qa-changed-files.md](workflows/style-qa-changed-files.md)
on the changed `_docs/` / root `_includes/` lines before opening the draft.

## Related skills

When chaining another skill, use **REQUIRED SUB-SKILL:** `braze-docs:skill-name` in instructions — do not use `@` or `/` syntax inside skill text. Prefer relative links to sibling `SKILL.md` files for discovery.

| Skill | Use for |
|-------|---------|
| [reference-repos](../reference-repos/SKILL.md) (`braze-docs:reference-repos`) | Verify product, API, or SDK behavior against sibling repos |
| [docs-discrepancies](../docs-discrepancies/SKILL.md) (`braze-docs:docs-discrepancies`) | Audit `_docs` pages against platform source and open discrepancy PRs |
| [support-analyzer](../support-analyzer/SKILL.md) (`braze-docs:support-analyzer`) | Triage support case CSVs and draft docs updates |
| [salesforce-migration](../salesforce-migration/SKILL.md) (`braze-docs:salesforce-migration`) | SF Knowledge Base migration tickets (Phase 1/2) |
| [check-accessibility](../check-accessibility/SKILL.md) (`braze-docs:check-accessibility`) | Pre-PR accessibility gate — run before any PR touching `_docs/`, `_includes/`, layouts, JS, or CSS |
| [create-pr](../create-pr/SKILL.md) (`braze-docs:create-pr`) | Open a draft PR to `develop` with repo-aligned description, pre-PR gates (including Style QA on changed prose), and manual verification checklist |
