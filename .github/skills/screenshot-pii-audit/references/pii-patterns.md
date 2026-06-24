# Screenshot PII patterns (Braze Docs)

## Always flag (high signal)

| Pattern | Example | Why |
|---------|---------|-----|
| External ID headers | `external_id`, `Ext_Id` | Identifies user identifier columns |
| Numeric user IDs in previews | `42004428`, `42004430` | Production-style external_id values |
| Alphanumeric external IDs | `a82415`, `a71902` | Common Braze CSV identifier format |
| Customer custom attributes | `OptIn_Email_Art_News`, `Marketing_Transactor_Flag` | Customer-specific schema |
| Production CSV filenames | `user_updates_03_04.csv` | Suggests real export file names |
| Real email addresses | `name@company.com` | Direct PII (not `@example.com`) |
| Person names | `Jordan Miller`, `Casey Higgins` | May be customer or employee data |
| Single names in Name columns | `Jordan`, `Miller` (when `Name` / `Name_Last` headers present) | Separate first/last columns in CSV previews |

## Person names (review required)

The scanner flags:

1. **First Last pairs** (e.g. `Jordan Miller`)
2. **Single tokens** in screenshots that show `Name` or `Name_Last` column headers (common when first and last names are in separate CSV columns)

This includes many style-guide example names so authors confirm they are fictional.

**If the name is fictional / from dashboard-06:** add a sidecar with the violation `dismiss_ids` and a reason such as "Example names from dashboard-06 fixture per style guide".

**If the name is a real employee or customer:** blur or replace before merging — do not dismiss.

A small set of documented example pairs (`Alex Smith`, `Yuri Kim`, etc.) are auto-allowed.

## Usually safe (FakeBrandz / style guide)

- Screenshots from [dashboard-06](https://dashboard-06.braze.com/)
- Placeholder emails: `alex@example.com`, `name@example.com`
- Generic attribute names shown in Braze UI defaults
- UI copy numbers: file size limits (`500`, `50`), years in footers

## Common false positives

| Finding | Mitigation |
|---------|------------|
| Version/build numbers mistaken for IDs | Sidecar with `dismiss_ids` |
| FakeBrandz IDs that match numeric pattern | Sidecar explaining dashboard-06 fixture |
| Generic Braze UI labels containing "ID" | Sidecar or crop screenshot |
| Fictional example names in CSV previews | Sidecar with reason (e.g. dashboard-06 fixture) |

## Sidecar format

File: `assets/img/path/to/image.png.pii-audit-dismiss.json`

```json
{
  "reason": "Required explanation for security audit trail",
  "dismiss_all": false,
  "dismiss_ids": ["abc12345"]
}
```

Set `"dismiss_all": true` only when the entire image is confirmed safe.

## Maintainer override

Add the **`pii-audit-dismissed`** label on the PR after reviewing sidecars or confirming findings are safe. CI allows merge but posts an audit comment listing unresolved detections.
