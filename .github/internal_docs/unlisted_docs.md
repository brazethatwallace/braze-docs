
# Unlisted docs

> The `unlisted_docs` collection holds pages that need a working public URL but should stay out of the navigation, search index, sitemap, and search-engine results. Use it for private betas, internal references, pricing handbooks, and other content you want to share by direct link only.

This collection replaces the standalone `braze-docs-hidden` repository. All pages, conventions, and assets that used to live there now live in `braze-docs` under the `_docs/_unlisted_docs/` directory.

## When to use unlisted docs

Use `unlisted_docs` when **all** of the following are true:

- The page must be reachable by anyone with the URL (no login required).
- The page should not appear in the left-hand navigation.
- The page should not appear in Algolia search results.
- The page should not appear in the sitemap or be indexed by search engines (`noindex`).

Common use cases:

- Private beta documentation shared by an account manager
- Pricing handbooks and entitlements documents linked from order forms
- Archived pages kept alive only as redirects
- One-off references that don't fit the public information architecture

If you need ordinary, discoverable documentation, add the page to the appropriate public collection (`_user_guide`, `_developer_guide`, `_api`, `_partners`) instead.

## Where unlisted docs live

| Path | Purpose |
| --- | --- |
| `_docs/_unlisted_docs/` | Source markdown for the collection |
| `_docs/_unlisted_docs/archive/` | Archived pages kept as redirects to current public docs |
| `_docs/_unlisted_docs/other/` | Catch-all for unlisted references that don't fit a category |
| `_docs/_unlisted_docs/pricing/` | Pricing handbooks and entitlements docs |
| `_docs/_unlisted_docs/private_betas/` | Private beta documentation |
| `assets/unlisted_docs/img/` | Images referenced by unlisted pages |
| `assets/unlisted_docs/img_archive/` | Archived images referenced by unlisted pages |
| `assets/unlisted_docs/download_file/` | PDFs, CSVs, and other downloadable assets referenced by unlisted pages |

Assets for `unlisted_docs` live in their own namespace (`assets/unlisted_docs/`) so they can never collide with or accidentally overwrite assets used by the public docs.

## How URLs work

The canonical URL for any page in this collection is `https://www.braze.com/docs/<permalink>/`. The legacy `https://www.braze.com/unlisted_docs/<permalink>/` URL is kept alive via a permanent (HTTP 308) redirect so that any links already shared externally before the migration continue to resolve to the new home.

| URL form | Behavior |
| --- | --- |
| `https://www.braze.com/docs/<permalink>/` | Canonical — served directly by the docs Vercel project. |
| `https://www.braze.com/unlisted_docs/<permalink>/` | Legacy — 308 Permanent Redirect to the canonical URL above. |
| `https://www.braze.com/unlisted_docs/assets/...` | Legacy asset path — 308 Permanent Redirect to `/docs/assets/unlisted_docs/...` (assets were namespaced during migration). |

The redirect rules live in [`vercel.json`](../../vercel.json) and are described in detail in [Legacy URL redirects](#legacy-url-redirects).

## Adding a new unlisted page

1. Pick the right subdirectory under `_docs/_unlisted_docs/` (`private_betas/`, `pricing/`, `other/`, or `archive/`). Create a new one if no existing folder fits.
2. Create your `.md` file with the following front matter:

   ```yaml
   ---
   nav_title: Short page title
   article_title: Full page title
   permalink: "/your-unique-slug/"
   description: "One-sentence description used by previews."
   hidden: true
   noindex: true
   ---
   ```

3. Write the page content like any other Braze Docs page. Use the same Liquid tags, alerts, and tables as the public docs.
4. Reference assets through the unlisted-docs namespace:

   ```liquid
   ![Description of the image]({% image_buster /assets/unlisted_docs/img/your_folder/your_image.png %})
   [Download the handbook]({{site.baseurl}}/assets/unlisted_docs/download_file/Your_File.pdf)
   ```

5. To preview locally, find your permalink in the front matter and append it to either:

   ```text
   http://127.0.0.1:5006/docs/<permalink>/
   http://127.0.0.1:5006/unlisted_docs/<permalink>/
   ```

### Required and recommended front matter

| Key | Required? | Why |
| --- | --- | --- |
| `permalink` | Required | Defines the public URL slug for the page. Must be unique across the entire `_docs/` tree. |
| `hidden: true` | Recommended | Keeps the page out of the sitemap and ensures it's not indexed by Algolia. The collection sets this by default, but setting it explicitly is good practice. |
| `noindex: true` | Recommended | Adds `<meta name="robots" content="noindex, nofollow">` to the rendered page. The collection sets this by default. |
| `nav_title` | Recommended | Used as the browser tab title. |
| `article_title` | Optional | Used in some metadata. Falls back to the H1 if omitted. |
| `description` | Optional | Used by some preview cards and tooling. |
| `hide_toc: true` | Optional | Hide the right-hand table of contents on a per-page basis. |

The `unlisted_docs` collection sets these defaults in `_config.yml`, so you do not need to repeat them in each page:

```yaml
layout: documents
hidden: true
noindex: true
hide_feedback: true
hide_nav: true
hide_breadcrumb: true
```

### Permalink uniqueness

Permalinks must be unique across the entire `_docs/` tree, not just within `_docs/_unlisted_docs/`. Before merging, check for collisions:

```bash
grep -rh '^permalink:' _docs/ | sort | uniq -c | sort -rn | head -20
```

Any line with a count greater than `1` is a collision and will cause Jekyll to behave non-deterministically.

Permalinks must also not collide with any `alias:` declared on a page elsewhere in the repo. The `_plugins/alias_generator.rb` plugin generates a meta-refresh stub at every alias path, so an alias on a public page produces an output file at the same destination as a same-slug permalink. Before adding a new unlisted page, search for the slug across all `alias:` entries:

```bash
grep -rn "^alias:.*your-unique-slug" _docs/
```

If a public page already declares that alias, the public page is the legitimate owner of the URL — pick a different slug for the new unlisted page.

## Promoting an unlisted page to a public collection

When a private beta becomes generally available (or any unlisted page is ready for public consumption), you usually want a different URL on the public site, but you also want the old `unlisted_docs` URL to keep working for anyone who already has it.

1. **Move the file** from `_docs/_unlisted_docs/<subdir>/<page>.md` to its destination in the public collection (for example `_docs/_user_guide/.../<page>.md`).
2. **Update the front matter:**
   - Remove `hidden: true` and `noindex: true` (unless you still want the page hidden from search).
   - Update `permalink` to the new public-friendly slug.
   - Add the page-meta fields the public collection expects (`page_order`, `page_type`, `description`, etc.).
3. **Move and rename referenced assets** out of `assets/unlisted_docs/` into the appropriate public asset folder (typically `assets/img/<feature_name>/`), and update the `image_buster` references in the page accordingly.
4. **Add a redirect stub** in `_docs/_docs_pages/redirects/` so the original unlisted permalink keeps working:

   ```yaml
   ---
   permalink: "/<old-unlisted-slug>/"
   layout: redirect
   redirect_to: "https://www.braze.com/docs/<new-public-permalink>/"
   ---
   ```

   This stub captures `https://www.braze.com/docs/<old-slug>/` and forwards visitors to the new public URL. Anyone who lands on the legacy `https://www.braze.com/unlisted_docs/<old-slug>/` URL will first hit the Vercel 308 redirect (see [Legacy URL redirects](#legacy-url-redirects)) which sends them to `/docs/<old-slug>/`, and then the redirect stub forwards them to the new public URL — so the same one stub handles both URL forms.

## Why pages don't show up in nav, search, or sitemap

Several pieces of the build pipeline cooperate to keep `unlisted_docs` content out of public surfaces:

| Surface | Mechanism | Configured in |
| --- | --- | --- |
| Sitemap (`sitemap.xml`) | Skips any page whose collection has `hidden: true` or whose front matter has `hidden: true`/`noindex: true` | `_docs/_docs_pages/sitemap.xml` |
| Algolia search index | Excludes the entire `_docs/_unlisted_docs/` tree | `_config.yml` (`algolia.files_to_exclude`) |
| Algolia indexing safety net | Drops any record where `hidden`, `noindex`, or `config_only` is true before indexing | `_plugins/algolia_hooks.rb` |
| `<meta robots>` tag | Adds `noindex, nofollow` for pages whose path starts with `_unlisted_docs` or whose front matter has `hidden: true`/`noindex: true` | `_plugins/noindex.rb` |
| Left-hand navigation | Collection has `hidden: true` and pages default to `hide_nav: true` | `_config.yml` (collection definition + defaults block) |
| Feedback widget | Collection defaults to `hide_feedback: true` | `_config.yml` (defaults block) |

If you change any of these surfaces in the future, double-check that `unlisted_docs` is still excluded.

## Legacy URL redirects

To keep legacy `https://www.braze.com/unlisted_docs/<slug>/` URLs working after the `braze-docs-hidden` deployment is retired, `vercel.json` contains two permanent (HTTP 308) redirects:

```json
"redirects": [
  {
    "source": "/unlisted_docs/assets/:path*",
    "destination": "/docs/assets/unlisted_docs/:path*",
    "permanent": true
  },
  {
    "source": "/unlisted_docs/:path*",
    "destination": "/docs/:path*",
    "permanent": true
  }
]
```

Vercel evaluates redirects in order, so the more specific assets rule must come first.

| Incoming request | Redirects to |
| --- | --- |
| `/unlisted_docs/foo/` | `/docs/foo/` |
| `/unlisted_docs/assets/img/foo.png` | `/docs/assets/unlisted_docs/img/foo.png` |
| `/unlisted_docs/assets/download_file/Handbook.pdf` | `/docs/assets/unlisted_docs/download_file/Handbook.pdf` |

Why a redirect instead of a transparent rewrite:

- Each page ends up with a single canonical URL going forward (`/docs/<slug>/`), which avoids duplicate-URL surface area for analytics and bookmarks.
- The HTTP 308 response explicitly tells browsers, CDNs, and any search engines (if a page were ever indexed) that the URL has permanently moved.
- The rule is simple to remove later, when sharing of legacy URLs has fully stopped.

### What still needs to happen at the infrastructure layer

These redirects only fire for requests that actually reach the docs Vercel project. As of this writing, traffic to `/unlisted_docs/*` on `www.braze.com` is routed to the separate `braze-docs-hidden` Vercel project. To activate the redirects, infra needs to:

1. Stop routing `www.braze.com/unlisted_docs/*` to the `braze-docs-hidden` Vercel project.
2. Route `www.braze.com/unlisted_docs/*` to the `braze-docs` Vercel project.
3. Then retire the `braze-docs-hidden` Vercel project (and, optionally, the source repo).

After step 2, the redirects above start firing automatically — every legacy `/unlisted_docs/<slug>/` URL begins 308-redirecting to its new `/docs/<slug>/` home.

> [!IMPORTANT]
> Do **not** retire `braze-docs-hidden` (steps 1 and 3 above) until the routing change in step 2 is in place. Otherwise every legacy `/unlisted_docs/<slug>/` URL will 404 in the gap.

### Testing the redirects before cutover

You can validate the redirect rules end-to-end before infra repoints the legacy traffic.

**Option 1 — Vercel preview deployment (recommended).** Open this branch as a PR; Vercel automatically builds a preview deployment at a `*.vercel.app` URL. The preview owns its own root, so you can hit the redirects directly:

```bash
# Replace <preview> with the preview deployment URL Vercel comments on the PR.
curl -sI https://<preview>.vercel.app/unlisted_docs/whatsapp_pricing_updates/ | head -5
# Expected: HTTP/2 308 with `location: /docs/whatsapp_pricing_updates/`

curl -sI https://<preview>.vercel.app/unlisted_docs/assets/img/ai_step1.png | head -5
# Expected: HTTP/2 308 with `location: /docs/assets/unlisted_docs/img/ai_step1.png`
```

**Option 2 — Vercel CLI locally.** Install `vercel` CLI (`npm i -g vercel`), authenticate, then run `vercel dev` from the repo root to run a local server that honors `vercel.json`:

```bash
vercel dev --listen 3000
# In another terminal:
curl -sI http://localhost:3000/unlisted_docs/handbooks/ | head -5
curl -sI http://localhost:3000/unlisted_docs/assets/download_file/Braze_Entitlements_Handbook_27.pdf | head -5
```

**Option 3 — bulk-test every legacy URL.** Once you have either a preview deployment or `vercel dev` running, generate the full list of expected redirect pairs from the migrated pages and verify each one:

```bash
# From the repo root, list every (legacy URL, new URL) pair the migration created:
ruby -ryaml -e '
  require "find"
  Find.find("_docs/_unlisted_docs") do |p|
    next unless p.end_with?(".md")
    fm = File.read(p).match(/\A---\n(.*?)\n---/m) and meta = YAML.safe_load(fm[1])
    permalink = meta && meta["permalink"] or next
    puts "#{permalink.sub(%r{^/}, "/unlisted_docs/")}\t#{permalink.sub(%r{^/}, "/docs/")}"
  end
' | sort

# Then loop through them:
HOST="https://<preview>.vercel.app"   # or http://localhost:3000
while IFS=$'\t' read -r legacy expected; do
  actual=$(curl -sI "$HOST$legacy" | awk 'tolower($1) == "location:" { print $2 }' | tr -d '\r')
  if [ "$actual" = "$expected" ]; then
    echo "OK   $legacy -> $expected"
  else
    echo "FAIL $legacy -> got '$actual' expected '$expected'"
  fi
done < /tmp/expected_redirects.tsv
```

Sign off the migration only when every legacy URL returns 308 with the expected `Location`.

## Unlisted docs vs. the `_hidden` collection

Braze Docs has two collections that produce pages excluded from navigation, search, and the sitemap: `unlisted_docs` (this collection) and `hidden` (under `_docs/_hidden/`). Their build mechanics overlap heavily, but they serve different purposes. Use the table below to pick the right one.

| | `unlisted_docs` (`_docs/_unlisted_docs/`) | `hidden` (`_docs/_hidden/`) |
| --- | --- | --- |
| Primary audience | Customers (via a direct link from an account manager, solutions engineer, sales motion, etc.) | Internal — the docs team, contributors, and tooling |
| Typical content | Private beta documentation, pricing handbooks, archived customer-facing features kept as redirects | Archived legacy SDK docs, deprecated layout templates, internal forms (feedback, documentation request), compliance and regex references, styling test pages, internal SDK redirect stubs |
| Subdirectories today | `archive/`, `other/`, `pricing/`, `private_betas/` | `archive_docs/`, `archived_layouts/`, `compliance/`, `misc_reference/`, `other/`, `redirects/`, plus loose pages like `styling_examples.md` |
| URL pattern | `https://www.braze.com/docs/<permalink>/` (plus the legacy `/unlisted_docs/<permalink>/` redirect described above) | `https://www.braze.com/docs/<permalink>/` |
| Excluded from nav, search, sitemap, search-engine indexing | Yes | Yes |
| Origin | Migrated from the standalone `braze-docs-hidden` repository | Always lived in `braze-docs` |

If the new page is something an external user might receive a link to (private beta, pricing reference, link in a customer email), put it in `_docs/_unlisted_docs/`.

If the new page exists for the docs team or for archival/internal reasons (a styling example, an archived SDK doc, an internal redirect for a renamed page, a compliance reference for the docs team), put it in `_docs/_hidden/`.

When in doubt, ask in the docs team channel before creating a new page in either collection.

## Migration history

This collection was created by migrating the contents of the `braze-docs-hidden` repository into `braze-docs`. During the migration:

- 86 markdown files moved from `braze-docs-hidden:_docs/_hidden/` to `braze-docs:_docs/_unlisted_docs/`, preserving the `archive/`, `other/`, `pricing/`, and `private_betas/` directory structure.
- 101 referenced assets (images, PDFs, CSVs) moved from `braze-docs-hidden:assets/img/` and `braze-docs-hidden:assets/download_file/` to `braze-docs:assets/unlisted_docs/img/` and `braze-docs:assets/unlisted_docs/download_file/`. Assets were namespaced under `assets/unlisted_docs/` rather than merged into `assets/img/` and `assets/download_file/` because the hidden repo's image folder contained 1,396 same-name-different-content collisions with assets already in `braze-docs`.
- Two `multi_lang_include` partials referenced by the migrated content (`_includes/shopify_alerts.md` and `_includes/whatsapp/about_credits.md`) were copied from `braze-docs-hidden:_includes/` to `braze-docs:_includes/`.
- All `image_buster` and `{{site.baseurl}}/assets/...` references in the migrated markdown were rewritten to the new `assets/unlisted_docs/` namespace.
- 30 obsolete redirect stubs in `_docs/_docs_pages/redirects/` were removed. Each one had previously redirected `/docs/<slug>/` to `https://braze.com/unlisted_docs/<slug>/`. Once the content lives natively in `_docs/_unlisted_docs/` with the same permalinks, those stubs cause Jekyll permalink collisions and become redundant.
- 20 archived redirect-only pages from `archive/` were removed because each one's `permalink:` collided with an `alias:` already declared on the canonical public page (the `_plugins/alias_generator.rb` plugin produces a meta-refresh redirect at every alias path). Examples: `archive/operator.md` (collided with `_user_guide/brazeai/operator.md`'s `alias: /operator/`), `archive/dashboard_builder.md`, `archive/kakaotalk.md`, `archive/messaging_interaction_data.md`. The legacy URL forwarding still works end-to-end: `https://www.braze.com/unlisted_docs/<slug>/` → 308 to `/docs/<slug>/` → meta-refresh from the public page's alias to the canonical public URL. The alias on the public page is also more durable because it auto-tracks any future move of that public page.
- One legacy alias was removed from `_docs/_unlisted_docs/private_betas/shopify_beta.md`: the migrated file declared `alias: /partners/shopify/`, which never collided in the hidden repo (it generated `/unlisted_docs/partners/shopify/index.html`) but does collide with the public Shopify partner page's alias once it's rebased under the `/docs/` baseurl. The public partner page is the legitimate owner of `/docs/partners/shopify/`.
- Two permanent (HTTP 308) redirects were added to `vercel.json` so that legacy `/unlisted_docs/<slug>/` and `/unlisted_docs/assets/...` URLs forward to their new homes once `/unlisted_docs/*` traffic is repointed to the docs Vercel project.
- Net result: 66 unlisted pages live under `_docs/_unlisted_docs/` (86 migrated minus the 20 archive redirects whose job is already done by aliases on canonical public pages).

If you need to confirm a page's provenance, see the migration commit history.
