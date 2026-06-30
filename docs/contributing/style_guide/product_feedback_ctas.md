# Product feedback CTAs in articles

Use this pattern when article text should invite readers to submit **product feedback** about Braze features — missing capabilities, enhancements to existing features, early feedback on new GA features, or dashboard UX friction.

This pattern is for **in-article prose only**. It does not replace:

- **Documentation feedback** — site widgets (`feedback.html`, `binary_feedback.html`) and the `/feedback/` page
- **Docs-format pilots** — `_includes/developer_guide/_shared/tutorial_feedback.md` (Google Form)
- **Early access and private beta** — contact your account manager or CSM in an Important or Note alert per [Alerts](alerts.md#when-to-use-an-alert)
- **Accessibility feedback** — `_includes/accessibility/feedback.md` (Support > Share feedback for accessibility of Braze or messages)

After this pattern ships, **new** product-feedback CTAs in `_docs/` and root `_includes/` must use the include below — not ad hoc portal links.

## Include

File: `_includes/product_feedback_cta.md`

Invocation:

```liquid
{% multi_lang_include product_feedback_cta.md context="gap" feature="per-domain sending for email templates" %}
{% multi_lang_include product_feedback_cta.md context="new_feature" feature="Canvas Audience Sync" %}
{% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="additional Data Transformation templates and destinations" %}
{% multi_lang_include product_feedback_cta.md context="pain_point" channel="ux" feature="navigation to workspace email settings" %}
```

The include outputs one or two sentences only. You choose placement:

- **Inline** — immediately after the sentence that states the limitation or friction, on the **same line** (space before `{% multi_lang_include ... %}`) so the CTA stays in one Markdown paragraph. The include file uses `{%-` / `-%}` on Liquid tags so output does not start with blank lines.
- **Note alert** — wrap the include (or limitation + include) in `{% alert note %}` when the CTA should stand out without using Important

Do not wrap the include in Important unless the surrounding content already meets Important alert criteria in [Alerts](alerts.md).

## When to use each context

| Context | Use when | Destination |
| --- | --- | --- |
| `gap` | The docs state a feature is **not supported**, **not planned**, or **only available elsewhere** (for example, only in Currents or Snowflake) | Product portal article (`_docs/_user_guide/administer/personal/product_portal.md`) → **Community** > **Product roadmap** in the dashboard |
| `new_feature` | A **new GA feature** article where product wants adoption feedback (coordinate with PM before adding) | Product portal |
| `pain_point` + `channel: feature` | An **existing GA feature** has a known enhancement gap or partial support | Product portal |
| `pain_point` + `channel: ux` | **Dashboard usability**, navigation, or visual design friction (not a missing product capability) | **Support** > **Share feedback** in the global header (no docs URL) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="When to use each context" }

### `pain_point` channel decision

| Reader friction | Channel |
| --- | --- |
| "We need capability X in the product" | `feature` |
| "This screen is confusing" / "Hard to find this setting" | `ux` |
| Accessibility of Braze or messages | Use `_includes/accessibility/feedback.md`, not this include |
{: .reset-td-br-1 .reset-td-br-2 aria-label="pain_point channel decision" }

## Parameters

| Parameter | Required | Values | Notes |
| --- | --- | --- | --- |
| `context` | Yes | `gap`, `new_feature`, `pain_point` | |
| `channel` | When `context` is `pain_point` | `feature`, `ux` | Omit for `gap` and `new_feature` |
| `feature` | Recommended | Free text | Short phrase inserted into the sentence (for example, `web push for the Shopify integration`). Use correct capitalization for product names (for example, `Canvas Audience Sync`). Omit only when generic wording is intentional. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parameters" }

Link text is always **product feedback** for portal-bound variants. Do not use "Braze product portal", bare `portal.braze.com`, or legacy `access_braze/portal` in new copy.

## Examples

### Gap — inline (FAQ)

```liquid
{% details Is the one-click unsubscribe setting available for email templates? %}
No, we currently do not have plans to add this for email templates, as these templates aren't assigned to a sending domain. {% multi_lang_include product_feedback_cta.md context="gap" feature="per-domain sending for email templates" %}
{% enddetails %}
```

### Pain point — feature channel (Note alert)

```liquid
{% alert note %}
Braze Data Transformation may not yet support external platforms that require special verification or authentication for webhooks. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="feature" feature="webhook authentication for external platforms" %}
{% endalert %}
```

### New GA feature — Note alert (style guide example; coordinate with PM before publishing)

```liquid
{% alert note %}
{% multi_lang_include product_feedback_cta.md context="new_feature" feature="Canvas Audience Sync" %}
{% endalert %}
```

Rendered shape: *Canvas Audience Sync is generally available. Share how it's working for your team through [product feedback](...).*

Pass `feature` with the capitalization you want in the sentence. The include does not alter casing.

## Reviewer checklist

- Correct `context` and `channel` for the friction type
- Inline CTAs are on the same line as the limitation sentence (no blank line before the include)
- `feature` param names the specific ask where possible
- Portal link targets `user_guide/administer/personal/product_portal` via the include (not ad hoc URLs)
- EAP/beta content still uses contact AM/CSM pattern, not this include
- Not confused with docs-format or page feedback widgets

## Bulk migration

Existing ad hoc CTAs (~22 reader-facing pages) should migrate to this include in follow-up PRs after this pattern is approved.
