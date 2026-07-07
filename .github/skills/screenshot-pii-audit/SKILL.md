---
name: screenshot-pii-audit
description: >
  Pre-PR security gate for Braze Docs screenshots.   OCR-scans changed images under
  assets/img/ for likely PII (external_id values, person names, customer attribute names, production
  CSV previews, real emails). Use before opening a PR with new or updated screenshots,
  when asked to "audit screenshots", "check screenshot PII", or after a CI PII failure.
allowed-tools: Bash(git *), Bash(python3 scripts/check_screenshot_pii.py*), Read, Write, StrReplace, Grep
---

# Screenshot PII Audit

## Context

- Branch: !`git branch --show-current`
- Changed images: !`git diff --name-only origin/develop...HEAD 2>/dev/null | grep -E '^assets/img/.*\.(png|jpg|jpeg)$' || true`

## When to run

- Before opening a PR that adds or updates screenshots under `assets/img/`
- When CI **Check screenshot PII** fails
- When reviewing another author's image changes

## Workflow

Load and follow [workflows/audit-changed-images.md](workflows/audit-changed-images.md).

## Enforcement

| Layer | Behavior |
|---|---|
| **CI** (`check-screenshot-pii.yml`) | **Blocking** on PRs that change images. Upserts a PR comment on failure; deletes bot comments on a clean pass. Partial fixes show struck-through cleared items. On `synchronize`, if the push does not touch images, dismiss sidecars, or scanner/workflow files, and the previous head already passed this check, CI skips Tesseract/OCR and leaves PR comments unchanged. |
| **Maintainer label** | `pii-audit-dismissed` allows merge but leaves an audit comment. |
| **Sidecar file** | `<image>.pii-audit-dismiss.json` documents false positives in-repo. |

Style guide: [docs/contributing/style_guide/image_style_guide.md](../../../docs/contributing/style_guide/image_style_guide.md)

## Code snippets (fenced blocks)

English markdown under `_docs/` and root `_includes/` can be scanned without OCR:

```bash
python3 scripts/check_snippet_pii.py _docs/path/to/page.md
```

- Shared patterns live in `scripts/pii_text_scan.py` (snippet rules skip alphanumeric `external_id` values and relax numeric IDs when placeholders like `YOUR_REST_API_KEY` appear).
- CI: **Check snippet PII (advisory)** — warning-only, does not block merge.
- Dismissals: `_docs/path/to/page.md.pii-audit-dismiss.json` (same JSON as screenshot sidecars).
