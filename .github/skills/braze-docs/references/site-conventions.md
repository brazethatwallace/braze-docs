# Site Conventions

Procedures for broken link resolution, redirect configuration, Liquid syntax,
and page anatomy in the braze-docs Jekyll site.

## Broken link detection and fixing

To fix a broken or suspect link:

1. Identify the link target path (strip `{{site.baseurl}}` prefix).
2. Check if a file exists at `_docs/_<collection>/<path>.md`. Verify canonical targets against English source under `_docs/` (and root `_includes/` when the link points to included content), not `_lang/`, unless you are explicitly fixing localized pages.
3. If not, search `assets/js/broken_redirect_list.js` for the path.
4. Follow any redirect chain to the final destination.
5. Verify the final destination file exists.
6. If the link has an anchor (`#slug`), verify the heading exists in the target.
7. Update the link to the current canonical path.
8. If the old path has no redirect entry, add one to `broken_redirect_list.js`.

Heading anchors are auto-generated from heading text: lowercased, spaces become
hyphens, special characters stripped. Example: `## Custom event analytics`
generates `#custom-event-analytics`.

## Redirect configuration

Redirects live in `assets/js/broken_redirect_list.js`:

```javascript
validurls['/docs/user_guide/old_section/old_page'] = '/docs/user_guide/new_section/new_page';
```

- One entry per moved path.
- Paths include the `/docs/` prefix and must be lowercase.
- `REDIRECT_FROM` must match the broken URL path exactly, including any trailing slash, `#anchor`, or other link artifacts when present.
- `REDIRECT_TO` should be the canonical destination path.
- Prefer no trailing slash for both paths unless an anchor or another link artifact requires it.
- Never include locale prefixes in redirect paths. Strip `/docs/en/`, `/docs/es/`, `/docs/ko/`, and any other language tag down to `/docs/`. Redirects only map canonical English paths.
- Collapse redirect chains (old to new directly, not old to intermediate to new).
- Other mechanisms: `layout: redirect` in frontmatter, `local_redirect` for heading-level redirects.

## Links in YAML frontmatter values

Some pages use YAML fields like `guide_top_text` that contain inline links. These fields are rendered by layouts using `| markdownify` but **not** `| liquify`, so Liquid tags like `{{site.baseurl}}` are not evaluated. Standard Markdown links `[text]({{site.baseurl}}/path/)` will render the Liquid tag literally and break the href.

**Use a plain HTML anchor instead:**

```yaml
guide_top_text: "See our article for <a href='/docs/user_guide/path/to/page'>page title</a>."
```

- Use an absolute `/docs/`-prefixed path (not `{{site.baseurl}}`).
- Production URLs omit trailing slashes (`vercel.json` `trailingSlash: false`). Use `/docs/user_guide/path/to/page`, not `/docs/user_guide/path/to/page/`, in static HTML anchors and redirect targets.
- Bulk cleanup for `_user_guide/`, `_developer_guide/`, and `_api/`: `python3 scripts/strip_internal_doc_link_trailing_slashes.py --dry-run` then `--apply`.
- The link checker (`scripts/find_broken_links.ts`) scans for Markdown-style links only, so HTML anchors are not checked — verify the target path exists manually.
- Reference example: `_docs/_api/endpoints/catalogs.md`.

## Liquid syntax

### Alerts

```liquid
{% alert important %}
Must-know caveats, billing impacts, deprecated features, beta status.
{% endalert %}
```

Types: `important`, `note`, `tip`, `warning`. Use sparingly. Do not stack two in a row.

### Tabs

```liquid
{% tabs %}
{% tab Tab Name %}
Content for this tab.
{% endtab %}
{% endtabs %}
```

Use `{% tabs local %}` for tabs that do not sync across the page. Subtabs: `{% subtabs %}` / `{% subtab Name %}`.

### Images

```markdown
![Alt text describing the image.]({% image_buster /assets/img/directory/filename.png %})
```

Optional styling: `{: style="max-width:60%"}`

Alt text: plain language, complete sentence, sentence case. Do not use "image of" or "picture of". Use "and" not "&".

## Page anatomy

### Introduction

Place 1-5 sentences immediately after the H1 heading. Two patterns:

1. **Lead-in paragraph:** Opens the topic with context.
2. **Content statement:** "This reference article covers..."

Use block quotes (`>`) for intro text.

### Prerequisites

Place a `## Prerequisites` section as the **first** `##` on the page (after the H1 and optional blockquote). Use it only for what the user must have or do before completing the article's task. Format as bullets, a numbered list, or a table.

When using a table, the first column header must be **Requirements** (not "Prerequisite" or "Prerequisites"):

```markdown
## Prerequisites

| Requirements | Description |
|---|---|
| Braze REST API key | A key with the `users.track` permission. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
```

Use a **Requirements** section (not Prerequisites) for constraints or specs from Braze or a third party (e.g., file format rules, API permissions). That section may appear anywhere on the page.
