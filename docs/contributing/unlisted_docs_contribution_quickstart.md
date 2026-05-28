# Unlisted docs contribution quickstart

Use this page as a practical checklist for contributing to `_docs/_unlisted_docs/`.

## Unlisted docs versus hidden docs

Use `_docs/_unlisted_docs/` for customer facing content that should be reachable by direct URL but excluded from navigation and indexing.

Use `_docs/_hidden/` for internal docs team content, tooling pages, and internal references that are not intended as customer facing docs.

| Collection | Use case | Audience |
| --- | --- | --- |
| `_docs/_unlisted_docs/` | Private betas, pricing handbooks, archived customer pages | External readers with direct links |
| `_docs/_hidden/` | Internal tooling docs, internal reference pages, styling tests | Internal contributors |

## Where to add unlisted docs content

- Markdown pages: `_docs/_unlisted_docs/{private_betas,pricing,other,archive}/`
- Images and media: `assets/unlisted_docs/img/`
- Archived images: `assets/unlisted_docs/img_archive/`
- Downloadable files (PDF, CSV, XLSX): `assets/unlisted_docs/download_file/`

Keep unlisted assets in `assets/unlisted_docs/` so they never collide with public docs assets.

## Required page setup

1. Create a Markdown file in the correct `_docs/_unlisted_docs/` subfolder.
2. Add front matter with a unique permalink:

```yaml
---
nav_title: Short page title
article_title: Full page title
permalink: "/your-unique-slug/"
description: "One sentence summary."
hidden: true
noindex: true
---
```

3. Use unlisted asset paths in content:

```liquid
![Image alt text]({% image_buster /assets/unlisted_docs/img/your_folder/your_image.png %})
[Download file]({{site.baseurl}}/assets/unlisted_docs/download_file/your_file.pdf)
```

4. Preview locally:

```text
http://127.0.0.1:5006/docs/<permalink>/
```

## Plugin and routing behavior you should know

These repo plugins and settings affect unlisted docs behavior:

- `noindex` plugin (`_plugins/noindex.rb`): Adds `noindex, nofollow` robots metadata for unlisted docs pages.
- `alias_generator` plugin (`_plugins/alias_generator.rb`): Generates redirect stubs for `alias:` paths. Check for collisions with existing aliases before choosing a permalink.
- `multi_lang_include` plugin (`_plugins/multi_lang_include.rb`): Available for reusable include partials used by unlisted docs.
- `_config.yml` defaults for `unlisted_docs`: Applies hidden/noindex and nav suppression defaults.
- `vercel.json` redirects: Keeps legacy `/unlisted_docs/*` URLs forwarding to `/docs/*` after routing cutover.

## Pre-merge checklist

- Permalink is unique across `_docs/` and does not collide with existing `alias:` values.
- Page renders with no Liquid errors.
- Images and downloads load from `assets/unlisted_docs/` paths.
- Page does not appear in left navigation.
- Page uses second person, present tense, and style guide compliant copy.

## Related docs

- `docs/contributing/unlisted_docs.md`
- `docs/contributing/unlisted_docs_qa.md`
