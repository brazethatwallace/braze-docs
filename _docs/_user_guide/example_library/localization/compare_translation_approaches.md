---
nav_title: Compare translation approaches
article_title: Compare approaches for managing multi-language translations
page_order: 1
page_type: reference
description: "Compare manual Liquid, Content Blocks, catalogs, multi-language messages, translation partners, and Connected Content to choose how Kitchenerie manages localized copy."
tool:
  - Campaigns
  - Canvas
---

# Compare approaches for managing multi-language translations

> Evaluate how localized copy is stored, updated, previewed, and sent so you can choose a localization approach that fits your QA workflow, channel mix, and update frequency.

## About this example

Kitchenerie, a fictional kitchenware retailer, sends email, push, and in-app messages in English, French, and German. Marketing and engineering need a repeatable, scalable way to manage translations across campaigns.

Braze supports several localization patterns:

- **Manual conditional Liquid:** Copy entered per language in the message body
- **Content Blocks:** Reusable blocks (with or without multi-language translation tags)
- **Catalogs:** Structured translation rows keyed by locale
- **Multi-language messages:** Translation tags, CSV uploads, and the translation API (early access)
- **Translation partners:** Smartling, Phrase, Lokalise, and others
- **Connected Content:** Localized strings fetched from your CMS or API at send time

This example compares tradeoffs so you can match an approach to your QA workflow, channel mix, update frequency, and team resources. It doesn't replace step-by-step setup for any single method. For feature walkthroughs, start with [Localization]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/) and [Multi-language messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/).

## Considerations

- Decide whether you need dashboard preview and QA, professional translation workflows, high-frequency content updates, or real-time CMS-driven copy before you pick a pattern.
- [Multi-language messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) support email, push, banners, in-app messages, and Content Blocks. Note that SMS and WhatsApp use other localization patterns. Manual Liquid, Content Blocks, catalogs, partners, and Connected Content can apply across channels where those features are supported.
- Braze does not generate translations. You supply copy through the dashboard, CSV, API, catalog import, partner workflow, or external CMS.
- Manual Liquid and Content Blocks with embedded conditionals need naming conventions and review processes as languages grow, and multi-language and partner workflows centralize updates but may require CSV or API maintenance.
- Connected Content and some partner flows depend on external systems. If an API or CMS is unavailable at send time, localized content may fail to load.
- Overlap is common. For example, you may use multi-language tags for email bodies, Content Blocks for shared footers, and catalogs for product copy in the same program.

## Setup

### Step 1: Capture your localization requirements

| Requirement | Questions to answer |
| --- | --- |
| Preview and QA | Do marketers need to preview each locale in the Braze composer before send? |
| Scale | How many languages and how often does copy change? |
| Workflow | Do you need translator review, revisions, and approvals? |
| Data shape | Is copy free-form marketing text, or structured product fields (names, prices, URLs)? |
| Automation | Should translations update automatically when your CMS changes? |
| Team skills | Can your team maintain Liquid, CSV uploads, APIs, or partner integrations? |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Capture your localization requirements" }

### Step 2: Compare approaches at a glance

| Dimension | Manual Liquid | Content Blocks | Catalogs | Multi-language messages | Translation partners | Connected Content |
| --- | --- | --- | --- | --- | --- | --- |
| Dashboard preview / QA | Yes | Yes | Yes | Yes | Varies by partner | Limited—harder to preview fetched content |
| Default (no integration) | Yes | Yes | Partial—catalog setup required | Yes | No—vendor setup | No—API or CMS required |
| Channel coverage | All supported channels | All supported channels | All supported channels | Email, push, banners, in-app messages, Content Blocks | Varies by partner | All supported channels |
| Implementation effort | Low | Low–medium | Medium | Low | High (partner-dependent) | Medium |
| Ongoing (BAU) effort | High—per-message edits | Medium—block maintenance | Medium—CSV or API updates | Medium—CSV uploads | Medium—managed in platform | Low—fetched at send time |
| High-frequency updates | No | Partial | No | Partial | Yes | Yes |
| Professional translation workflow | No | No | No | No | Yes | No |
| Structured / product data | Limited | Limited | Yes—ideal for keyed copy | Limited | Varies | Yes—through external source |
| External dependency risk | None | None | None | None | Medium | Medium—send fails if source is down |
| Best suited for | Few languages, infrequent updates | Shared components across messages | Many locales of structured strings | Many languages with lower copy-paste effort | Enterprise translation with approvals | Dynamic CMS-driven localization |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 .reset-td-br-7 aria-label="Compare approaches at a glance" }

### Step 3: Match Kitchenerie-style scenarios to an approach

| Kitchenerie scenario | Recommended starting point |
| --- | --- |
| Three languages, few campaigns per month, small marketing team | Manual conditional Liquid or Content Blocks with Liquid |
| Shared header, footer, and legal blocks across email and IAM | Content Blocks—with [multi-language translations saved on the block]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/#save-translations-in-content-blocks) when locales scale |
| Product names, promo lines, and image URLs keyed by locale | [Catalogs]({{site.baseurl}}/user_guide/data/activation/catalogs/) |
| Email and push in eight or more locales with composer preview | [Multi-language messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) |
| Central TMS with translator workflow and approvals | [Localization partners]({{site.baseurl}}/partners/message_personalization/localization/) (for example Smartling or Phrase) |
| Copy owned in a CMS that updates daily | [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Match Kitchenerie-style scenarios to an approach" }

### Step 4: Implement the approach you selected

1. **Manual conditional Liquid:** Use profile `language` or locale attributes with `if` / `elsif` / `else` Liquid. See [Alternative approaches]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/#alternative-approaches) and [Conditional logic]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic/).
2. **Content Blocks:** Create reusable blocks; optionally hide conditional Liquid inside blocks. See [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/) and the Content Blocks tab under [Sending translated messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/#sending-translated-messages).
3. **Catalogs:** Import translation rows (for example `id`, `context`, `language`, `body`) and reference them with Liquid `catalog_items`. See the Catalogs tab under [Sending translated messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/#sending-translated-messages).
4. **Multi-language messages:** [Add locales]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings/), wrap copy in translation tags, then upload a CSV. If you have early access to the [translation endpoints]({{site.baseurl}}/api/endpoints/translations/), you can update translations by API instead. Preview with **Multi-language user** in the composer.
5. **Translation partners:** Configure workspace locales, then follow your partner integration (for example [Smartling]({{site.baseurl}}/partners/message_personalization/localization/smartling/) or [Phrase]({{site.baseurl}}/partners/message_personalization/localization/phrase/)).
6. **Connected Content:** Call your CMS or translation API at send time. Test thoroughly; preview may not reflect live API responses. See [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/).

For Canvas and campaign orchestration across regions (one journey versus one journey per country), see [Translation management]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/#translation-management) on the Localization page.

## Related articles

- [Localization]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/)
- [Multi-language messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/)
- [Localization settings]({{site.baseurl}}/user_guide/administer/global/workspace_settings/multi_language_settings/)
- [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/)
- [Catalogs]({{site.baseurl}}/user_guide/data/activation/catalogs/)
- [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)
- [Localization partners]({{site.baseurl}}/partners/message_personalization/localization/)
- [Accessibility language for localized messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/#language-settings-and-accessibility)
