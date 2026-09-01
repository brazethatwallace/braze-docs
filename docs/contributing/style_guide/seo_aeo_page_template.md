# SEO and AEO page template

Use this template when creating or optimizing Braze Docs pages for search engines and answer engines (AI overviews, LLM retrieval). It extends the [page anatomy](../../.github/skills/braze-docs/references/site-conventions.md) rules in the braze-docs skill and the [writing style guide](writing_style_guide.md).

**Scope:** English canonical pages under `_docs/` and root `_includes/`. This guide does not cover Sanity CMS integration or bulk migration of existing pages.

## Quick checklist

| Element | Requirement |
|---------|-------------|
| `article_title` | Matches H1 intent; primary keyword in first ~60 characters |
| `description` | Required; ≤150 characters; answers what the reader will learn |
| Opening answer block | First ~120 words directly answer the page's primary question |
| Heading hierarchy | One H1; no skipped levels; FAQs use `####` with `{#kebab-case}` anchors |
| Internal links | 2–4 contextual links on reference pages; link text matches destination |
| FAQ block | Real search-style questions; highest-priority first; answer first, then detail |
| `page_type` | Set `FAQ` on FAQ hub pages; use `reference`, `tutorial`, or `landing` elsewhere |
| `search_rank` | Optional hub boost (lower number = higher in-site search priority) |

## Title and meta description

### `article_title`

- Sets the browser tab title and search result title via [`html_include.html`](../../../_includes/html_include.html).
- Align with the H1 heading intent. They may differ in length but must describe the same topic.
- Put the primary keyword near the start (first ~60 characters when possible).

```yaml
---
article_title: Create SMS campaigns in Braze
nav_title: Create SMS
description: "Learn how to create and send SMS campaigns, including audience selection, message composition, and launch settings."
---
```

### `description`

- Required for optimized pages. Maximum **150 characters** (including spaces), wrapped in double quotes.
- Write as a complete sentence that answers: *What will I learn on this page?*
- Do not duplicate the H1 verbatim.

See [metadata.md](../yaml_front_matter/metadata.md) for all frontmatter keys.

## Opening answer block

Place a direct answer **immediately after the H1** (before `## Prerequisites` or the first `##` section).

**Target:** ~80–120 words that answer the page's primary question without requiring the reader to scroll.

**Patterns:**

1. **Lead-in paragraph** — Context plus the direct answer in the first sentence.
2. **Content statement** — "This article explains how to…" followed by the core answer.
3. **Blockquote intro** — Use `>` for the opening block when it matches existing site conventions.

**Example:**

```markdown
# Create SMS campaigns

> SMS campaigns let you send one-time messages to a targeted audience. This article covers audience selection, message composition, subscription compliance, and launch settings.

After you complete this guide, you can create and launch a basic SMS campaign from the Braze dashboard.
```

**Avoid:**

- Burying the answer below prerequisites or a long background section
- Opening with history or feature marketing copy before stating what the page covers

## Heading hierarchy

- One `#` H1 per page (usually matches `article_title` topic).
- Use `##` for major sections; `###` for subsections; `####` for FAQ questions.
- Do not skip levels (for example, `##` directly to `####`).
- Task headings use imperatives ("Create a segment", not "Creating a segment").

FAQ pages use `####` questions with stable anchors:

```markdown
#### How do I reset my API key? {#how-do-i-reset-my-api-key}
```

See [writing style guide — FAQs](writing_style_guide.md#frequently-asked-questions-faqs).

## FAQ blocks

**When to use a dedicated FAQ page (`page_type: FAQ`):**

- Multiple recurring questions on one topic
- Questions that do not fit cleanly into a task article

**When to add FAQs to an existing article:**

- One or two edge-case questions → add a `## Frequently asked questions` section at the end
- More than three unrelated questions → consider a separate FAQ hub and cross-link

**FAQ writing rules:**

1. Order by user priority (most common question first).
2. Start each answer with a direct response, then add detail.
3. Phrase questions as real search queries ("How do I…", "What is…", "When should I…").
4. Link to deeper articles instead of duplicating long procedures.

## Internal linking

**Minimum:** 2–4 contextual internal links on reference and hub pages.

**Rules** (from braze-docs skill):

- Use `{{site.baseurl}}/path` without trailing slashes.
- Link text must describe the destination (never "click here", "learn more", or "here").
- Prefer "For more information, see …" or "To learn more, refer to …"
- Link to parent channel hubs and related task articles (hub-and-spoke).

**YAML `guide_top_text` and HTML anchors:** Use `/docs/...` paths without `{{site.baseurl}}` in static HTML anchors. See [site conventions — Links in YAML frontmatter values](../../.github/skills/braze-docs/references/site-conventions.md#links-in-yaml-frontmatter-values).

## Schema and structured data

**Today (automatic):**

- `<title>` from `article_title` / `nav_title` / `title`
- `<meta name="description">` from `description` (fallback: truncated body)
- `<link rel="canonical">` on every page
- Site-wide `WebSite` + `SearchAction` JSON-LD in `html_include.html`
- `llms.txt` / Copy for LLM for supported collections

**Not yet implemented (future site change):**

- Per-page `FAQPage` JSON-LD
- Per-page `TechArticle` / `Article` JSON-LD
- Open Graph (`og:`) and Twitter card meta tags

Do not add inline JSON-LD in markdown files until a sitewide layout pattern is approved.

## `page_type` and `search_rank`

### `page_type`

| Value | Use for |
|-------|---------|
| `FAQ` | FAQ hub pages with multiple Q&A entries |
| `reference` | API docs, glossary entries, field definitions |
| `tutorial` | Step-by-step how-to guides |
| `landing` | Section index pages |
| `partner` | Partner integration articles |
| `solution` | Example library / solution articles |
| `glossary` | Glossary term pages |
| `update` | Release notes entries |

### `search_rank`

Optional numeric frontmatter field (lower = higher priority in Braze Docs search). Use on high-traffic hub pages (for example, `search_rank: 1` on channel landing pages).

## Pilot audit workflow

For page-level SEO/AEO recommendations, use the in-repo pilot tooling:

```bash
# Rank pilot candidates
python3 scripts/seo_pilot/page_scorecard.py --out scripts/temp/seo-pilot-scorecard.csv

# Verified link fix tables with section context
python3 scripts/seo_pilot/link_fix_table.py --out scripts/temp/link-fix-table.csv

# Per-page meta, intro, and FAQ audit
python3 scripts/seo_pilot/page_audit.py --pages-file scripts/temp/pilot-pages.txt --out-dir docs/seo_pilot/recommendations
```

See [`scripts/seo_pilot/README.md`](../../../scripts/seo_pilot/README.md) for input file formats (GSC, Algolia, support CSV).

## Recommendation tiers

When delivering page recommendations, split changes into two layers:

**No-approval** (ship in a PR without copy review):

- `article_title` / `description` within limits
- Broken or stale internal link fixes (from verified link fix table)
- Heading level corrections
- `page_type: FAQ` on FAQ hubs
- `search_rank` tuning

**Approval-needed** (editorial or product sign-off):

- Opening answer block rewrites
- New FAQ Q&A content
- Section reorganization
- Product limits, SKUs, or third-party claims (verify with reference-repos first)

## Related resources

- [Writing style guide](writing_style_guide.md)
- [YAML metadata](../yaml_front_matter/metadata.md)
- [Redirecting URLs](../content_management/redirecting_urls.md)
- [braze-docs skill — site conventions](../../.github/skills/braze-docs/references/site-conventions.md)
