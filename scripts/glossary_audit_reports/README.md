# Glossary drift reports

Weekly CI writes `latest.json` and `latest.md` here when
`audit-glossaries` finds mismatches between Phrase-synced glossaries and
platform/SDK locale files. Local audit runs can still use root-level
`glossary_audit_report.*` (gitignored).

**Missing terms** in the report count only bold UI labels (`**Term**`) in
English `_docs/` body text, so Jekyll front matter (`image:`, `layout:`)
and generic prose do not inflate the list.

**Exact mismatches** may include an *untranslated source* note when a
product locale file still ships English for that string.
