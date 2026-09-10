---
nav_title: GPI
article_title: Globalization Partners International
date_published: "2026-09-09"
description: "This reference article outlines the partnership between Braze and Globalization Partners International (GPI), a translation services provider. The GPI Translation Services Connector extracts Braze content for translation and imports completed translations back through Braze's Translation API."
alias: /partners/gpi/
page_type: partner
search_tag: Partner
---

# Globalization Partners International

> [Globalization Partners International](https://www.globalizationpartners.com/) (GPI) provides the GPI Translation Services Connector for Braze. The connector extracts content from campaigns, Canvases, email templates, and Content Blocks for translation, then imports completed translations back into Braze through the Translation API. GPI supports human translation, AI-powered translation, and AI translation with expert post-editing across more than 200 languages.

_This integration is maintained by Globalization Partners International._

## About the integration

The GPI Translation Services Connector integrates with Braze's native multi-language model and Translation API. You extract translatable content from the GPI Translation Portal, send it to GPI for translation, and import finished translations back into Braze without manual copy-paste. GPI preserves Liquid tags and personalization throughout the workflow.

## Use cases

### Global campaign launch

Select campaigns, Canvases, or email templates in Braze, set source and target languages, and submit the content to GPI for professional human translation. GPI handles localization and quality assurance in draft previews before launch.

### Time-sensitive or high-volume localization

Route flash sales, urgent lifecycle messages, or large batches of Content Blocks through the connector to receive translations imported back into Braze automatically. Turnaround time depends on the workflow you choose and can range from weeks to minutes.

### Internationalization support

GPI provides guidance on formatting and best practices for Braze localization, including right-to-left (RTL) languages such as Arabic, Hebrew, and Persian.

### Ongoing localization at scale

GPI uses Translation Memory to reuse previous translations for terminology and style consistency and to reduce cost on exact, repeat, and fuzzy matches. Update source-language campaigns in Braze and send the revised content to GPI to refresh the corresponding translations.

## Prerequisites

Before you start, you need the following:

| Prerequisite | Description |
| --- | --- |
| A Globalization Partners International account | A GPI account is required to use this integration. |
| A Braze REST API key | A Braze REST API key with the following permissions:<br>- `campaigns.list`<br>- `campaigns.details`<br>- `campaigns.translations.get`<br>- `campaigns.translations.update`<br>- `canvas.list`<br>- `canvas.details`<br>- `canvas.translations.get`<br>- `canvas.translations.update`<br>- `content_blocks.list`<br>- `content_blocks.info`<br>- `content_blocks.translations.get`<br>- `content_blocks.translations.update`<br>- `templates.email.list`<br>- `templates.email.info`<br>- `templates.email.translations.get`<br>- `templates.email.translations.update`<br><br>Create this key in the Braze dashboard from **Settings** > **APIs and Identifiers** > **API Keys**. For more information, see [Creating REST API keys]({{site.baseurl}}/api/basics#creating-rest-api-keys). |
| A Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/api/basics#endpoints). Your endpoint depends on the Braze URL for your instance. |
| Braze multi-language settings | Target locales must be configured in Braze under **Settings** > **Localization Settings**. For more information, see [Multi-language settings]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Integration

### Step 1: Create a Braze REST API key

1. In Braze, go to **Settings** > **APIs and Identifiers** > **API Keys**.
2. Create a REST API key with the permissions listed in [Prerequisites](#prerequisites).
3. Copy the API key and note your instance REST endpoint.

### Step 2: Send settings to GPI

1. Send your API key and REST endpoint to your GPI account manager.
2. Send the list of users who need access to the connector so GPI can enable it for them.
3. GPI configures the connector with your credentials and validates the connection.

### Step 3: Configure localization settings in Braze

1. In Braze, go to **Settings** > **Localization Settings** and confirm your target locales are enabled.
2. Confirm the content you send for translation has the required locales enabled. Content without enabled locales cannot receive imported translations.
3. Add [translation Liquid tags]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) around the content that needs translation.
4. For RTL languages, add Liquid tags to support content direction based on language. Avoid alignment styling directives unless you confirm they do not affect RTL rendering.

## Use GPI with Braze

Only content in draft or post-launch draft status can be translated in Braze.

### Step 1: Export content for translation

1. In the [GPI Translation Portal](https://www.translationportal.com), open the **Braze** connector and select **New Request**.
2. Complete the **Information** tab, then open the **Content** tab. From **Categories**, select **Campaign**, **Canvas**, **Email Template**, or **Content Block**, then select the items to export.
3. Select **Submit** to send a quote request to GPI. Your GPI account manager contacts you when the quote is ready for review and approval.

### Step 2: Import translations into Braze

1. In the **Braze** connector, locate the project you want to import.
2. Select the **Import** icon in the **Actions** column.
3. Wait for the import confirmation message. Check import job status on the **Jobs** page.

### Step 3: Check translation request status

1. Go to the [GPI Translation Portal](https://www.translationportal.com).
2. Select **Sign In** and enter your credentials.
3. In the GPI Translation Portal navigation, select **Braze** to open the connector dashboard. Review the **Quotes** and **Projects** tables for request and project status.

### Step 4: Preview translations in Braze

After you import translations, preview them in Braze:

1. Open the **Edit** screen for the campaign or message you translated.
2. In the **Message Composer**, go to the **Preview and Test** or **Test** tab.
3. Under **Preview message as user**, select **Multi-language user**, then select the locale you want to view.
4. Confirm the preview in the target language. To share with external reviewers, generate a preview link.

## Considerations

- The GPI Translation Services Connector for Braze is distributed at no cost.

## Troubleshooting

For assistance with the GPI Translation Services Connector for Braze or any GPI translation project, contact your GPI project manager, call +1-866-272-5874, or email [support@globalizationpartners.com](mailto:support@globalizationpartners.com).
