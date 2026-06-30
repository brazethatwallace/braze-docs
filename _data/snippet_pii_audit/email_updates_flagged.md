# Snippet email PII — updates and flagged items

- **Updated:** 2026-06-25 (UTC)
- **Scope:** English canonical fenced code blocks flagged as `email_address` in the snippet PII audit (`_docs/`, `_includes/`).
- **Change applied:** Replaced placeholder domains (`@braze.com`, `@email.com`, `@test.com`, `@gmail.com`, `@yourbrand.com`, and similar) with `@example.com` where the address is illustrative only. Local parts were preserved unless they contained a real person's name (for example `braze+nadav@dots.eco` → `braze+user@example.com`).

## Summary

| Metric | Before | After |
|--------|-------:|------:|
| Total snippet PII findings | 197 | 117 |
| Email address findings | 87 | 7 |
| Files with email findings | 46 | 4 |

**42 files** were updated. See git diff for the full list.

## Flagged — not updated

These remaining **7 email findings** were left unchanged because replacing the address would alter the meaning of the example or misrepresent vendor/API behavior.

### `_docs/_partners/data_and_analytics/analytics/kickbox.md` (updated)

Previously flagged; now uses `@example.com` with aligned `user` and `domain` fields. The undeliverable sample uses `example2@exampl.com` with `did_you_mean: example2@example.com` to preserve the typo-correction example.

### `_docs/_user_guide/channels/webhooks/create_a_webhook.md` (1 finding)

| Match | Lines | Reason |
|-------|-------|--------|
| `support@lob.com` | ~159 | Verbatim Lob API **404 error JSON** (`message` field). Changing the address would misquote Lob's API response. |

**Recommendation:** Sidecar dismiss with reason "Vendor API error payload".

### `_docs/_releases/deprecations/eclipse_setup_deprecated.md` (1 finding)

| Match | Lines | Reason |
|-------|-------|--------|
| `git@github.com` | — | Git SSH clone URL (`git@github.com:braze-inc/...`), not an email placeholder. Scanner false positive on `user@host` pattern. |

**Recommendation:** Sidecar dismiss or extend scanner to skip `git@` SSH URLs.

### `_includes/developer_guide/unity/sdk_integration.md` (2 findings)

| Match | Lines | Reason |
|-------|-------|--------|
| `git@github.com` | — | Same as Eclipse doc — Git SSH clone URLs for Unity SDK dependency setup. |

**Recommendation:** Sidecar dismiss or extend scanner to skip `git@` SSH URLs.

## Related prose (out of snippet scope)

The following were **not** flagged by the fenced-block scanner but still use non-`example.com` placeholder domains in tables or inline examples. Update separately if desired:

- `_docs/_user_guide/audience/manage_audience/import_users/csv_import.md` — `smith@user.com`, `nguyen@user.com` (markdown table, not a code fence); `jane.doe@braze.com` in column description prose.
- `_docs/_api/endpoints/scim/delete_existing_dashboard_user.md` — `user@test.com` in parameter description (prose, not fenced).
