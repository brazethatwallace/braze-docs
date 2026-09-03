---
nav_title: Home
article_title: What's new in Braze
description: "Braze release notes are published monthly so you can stay up-to-date on major product releases, ongoing product improvements, Braze partnerships,."
page_order: 0
search_rank: 1
page_type: reference
---

# What's new in Braze

{% alert tip %}
For more information on any of the updates listed on this page, contact your account manager or [open a support ticket]({{site.baseurl}}/user_guide/administer/personal/braze_support/). Check out our [SDK Changelogs]({{site.baseurl}}/developer_guide/changelogs) for more information about our monthly SDK releases, improvements, and breaking changes.
{% endalert %}

{% details August 20, 2026 %}

## August 20, 2026 release

### Data & Reporting

#### Cloud Data Ingestion SQL editor

{% multi_lang_include release_type.md release="General availability" %}

The [SQL editor]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sql_editor) lets you create and edit Cloud Data Ingestion (CDI) syncs by writing a SQL query against any table or view in your data warehouse, rather than building and maintaining a dedicated Braze-specific table. It's available for all sync data types across all CDI data warehouse sources: Snowflake, Redshift, BigQuery, Databricks, and Fabric.

#### Cloud Data Ingestion visual mapper

{% multi_lang_include release_type.md release="Beta" %}

The [visual mapper]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/visual_mapper) lets you create a Cloud Data Ingestion (CDI) sync by mapping an existing data warehouse table's columns to Braze fields directly in the dashboard, with no SQL or dedicated table required. This beta release supports User Attributes syncs across all CDI data warehouse sources. The visual mapper and the SQL editor are complementary: use the visual mapper for direct column-to-field mapping, and the SQL editor for advanced cases like transformations, joins, and conditional logic.

#### Cloud Data Ingestion for Google Cloud Storage and Azure Blob Storage

{% multi_lang_include release_type.md release="General availability" %}

Cloud Data Ingestion (CDI) supports two new file storage sources: Google Cloud Storage, generally available now, and Azure Blob Storage, coming the week of August 31, 2026. Both sources work like the existing Amazon S3 source—Braze ingests files as soon as they're written to the bucket or container—so customers on Google Cloud or Azure get the same speed and reliability without replicating files into S3 or building a custom integration.

#### Cloud Data Ingestion to BrazeAI Decisioning Studio

{% multi_lang_include release_type.md release="Early access" %}

Cloud Data Ingestion (CDI) can now sync data warehouse data directly to BrazeAI Decisioning Studio for customers using both products, so you can bring in data beyond your Braze workspace for reinforcement learning and AI decisioning without building custom ETL jobs. This early access release supports Snowflake sources, with additional data warehouse sources coming soon.

### BrazeAI<sup>TM</sup>

#### Operator can navigate the dashboard for you

{% multi_lang_include release_type.md release="General availability" %}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#navigate-the-dashboard) can navigate to a different dashboard page to complete your request. When a prompt needs a different part of the dashboard, Operator identifies the destination, proposes the navigation, and takes you there before continuing its work.

This lets Operator chain multi-step work from a single prompt. For example, if you ask Operator from the home page to set up your drag-and-drop editor settings to match your brand guidelines, it navigates you to the relevant email settings and continues helping you from there.

By default, Operator asks you to approve a proposed navigation before it moves you to a new page. To let Operator navigate without waiting for your approval each time, turn on [Auto-approve actions]({{site.baseurl}}/user_guide/brazeai/operator/reviewing_actions#auto-approve-actions).

#### Operator can act on more dashboard pages

{% multi_lang_include release_type.md release="General availability" %}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities) can complete work from additional dashboard pages when you describe the outcome in natural language. Examples include building reports and dashboards, working from email template and Content Block list pages, importing or managing users, creating predictions, and updating more admin and settings surfaces.

For example, on the Report Builder page, ask Operator to build a report that shows workspace SMS engagement over the last 30 days.

For representative coverage, see [What you can do with Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities). Ask Operator on the page you're on for the most current answer.

#### Operator can create and edit Canvases

{% multi_lang_include release_type.md release="General availability" %}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities) can create a draft Canvas from a natural-language description, and edit an existing Canvas the same way. Describe the journey you want—entry criteria, delays, and messages—and Operator assembles a draft you review and refine before you launch it.

For example, ask Operator to build an abandoned cart journey that waits one hour after cart abandonment, sends an email reminder, then a push after 24 hours if the user still hasn't purchased.

For supported steps and limitations, see [What you can do with Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities).

#### Content Optimizer step updates

{% multi_lang_include release_type.md release="Beta" %}

The [Content Optimizer]({{site.baseurl}}/user_guide/brazeai/content_optimizer) step includes the following updates:

- **Step states:** Content Optimizer steps show whether they're in **Learning**, **Optimizing**, or **Action Recommended**, so you can see where each step stands.
- **Pre-launch setup checks:** Content Optimizer checks for key misconfigurations while you draft, so you can catch issues before you launch.
- **Track which combination each user received:** A new Liquid tag and user profile visibility let you track which variant combination each user received, end to end.
- **New Currents data:** Three new event types let you pull Content Optimizer data into your warehouse: `users.canvas.costep.Send`, `users.canvas.costep.Conversion`, and `contentoptimizer.ComponentStore`.

For setup details, see [Content Optimizer step]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step).

### Orchestration

#### Workspace quiet hours

{% multi_lang_include release_type.md release="Early access" %}

[Workspace quiet hours]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours/workspace_quiet_hours) let you set a default quiet hours window for a messaging channel across your entire workspace. Every campaign and Canvas on that channel respects the window in each recipient's local time zone. You can keep the workspace default, or opt out and apply a campaign or Canvas-specific window instead.

Messages that would send during the window are held for later delivery or aborted, depending on the campaign type. Workspace quiet hours never modify message content.

#### Canvas threshold alerts

{% multi_lang_include release_type.md release="Early access" %}

[Canvas threshold alerts]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/canvas_threshold_alerts) notify you when user entries or messages sent fall outside the volume you expect. Set a threshold, choose how often Braze checks it (every 3 to 12 hours, or every 24 hours), and get notified by email, webhook, or both when a rule is met. You can create multiple alerts for the same Canvas, including on drafts—the alert starts checking after the Canvas launches.

#### Automatic Team assignment

{% multi_lang_include release_type.md release="General availability" %}

For users with Team-level permissions only, Braze can assign a [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams#automatic-team-assignment) automatically during object creation.

### Channels & Touchpoints

#### Connected Content debugger

{% multi_lang_include release_type.md release="Early access" %}

The [Connected Content debugger]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/debugger) shows the live request and response for each Connected Content call in **Preview & Test**, so you can verify your endpoint, headers, and Liquid tags before you launch a campaign or Canvas. Open **View details** to inspect the URL, method, status code, request and response headers, payload, duration, and whether the response was served from cache.

During early access, the debugger is available for Content Cards, email, in-app messages, push, SMS/MMS/RCS, webhooks, and WhatsApp.

#### In-app message and landing page surveys

{% multi_lang_include release_type.md release="General availability" %}

Braze surveys collect feedback in [in-app messages]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys/) and [landing pages]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys/) that you can analyze and use in follow-up messaging.

#### KakaoTalk carousel message

{% multi_lang_include release_type.md release="General availability" %}

A [KakaoTalk carousel message]({{site.baseurl}}/user_guide/channels/kakaotalk/create_kakaotalk_message#step-2-compose-your-kakaotalk-message) includes up to six scrollable cards. Each card has an image, header, message, optional Website URL, and at least one button.

#### WhatsApp Template Builder improvements

{% multi_lang_include release_type.md release="General availability" %}

[WhatsApp Template Builder]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/template_builder/) supports more creation paths and template options:

- **Create templates while building campaigns and Canvases:** Create a new WhatsApp template directly in the composer instead of only selecting existing templates from Content.
- **Carousel response messages:** Build carousel layouts as response messages, not only as outbound templates.
- **New template types: Utility and Flow:** Template Builder supports Utility templates and Flow templates, including when you create templates from campaigns, Canvases, or the standalone Content Templates experience.

#### Custom form blocks and JavaScript bridge for landing pages

{% multi_lang_include release_type.md release="General availability" %}

Landing pages now support [custom form blocks]({{site.baseurl}}/user_guide/messaging/landing_pages/custom_form_blocks) and a [JavaScript bridge]({{site.baseurl}}/user_guide/messaging/landing_pages/javascript_bridge), so you can capture custom form input and sync client-side events and attributes through your landing page experience.

#### Multi-step landing page forms

{% multi_lang_include release_type.md release="General availability" %}

[Multi-step landing page forms]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/multi_step_forms) let you split a long form across multiple steps in a single **Form** row, with a built-in confirmation step after submission. 

#### Manage Subscriptions block for landing pages

{% multi_lang_include release_type.md release="General availability" %}

The [Manage Subscriptions]({{site.baseurl}}/user_guide/messaging/landing_pages/manage_subscriptions) block lets users view, opt in to, and update email subscription groups on a landing page.

### Partnerships

#### Audience Sync: Google Data Manager API

{% multi_lang_include release_type.md release="Early access" %}

[Audience Sync to Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync) supports Google Data Manager API in early access.

#### Amazon Bedrock - AI Model Provider

[Amazon Bedrock](https://aws.amazon.com/bedrock/) is a fully managed AWS service that provides access to foundation models from leading AI companies through a unified API, so brands can build and scale generative AI applications on AWS.

For more information, see [Amazon Bedrock]({{site.baseurl}}/partners/amazon_bedrock).

#### Bynder - Message Orchestration - CMS and DAM

[Bynder](https://www.bynder.com) is a digital asset management (DAM) platform that helps customers create, manage, find, and distribute approved digital assets (images, videos, and other creative) from a single source of truth. When integrated with Braze, Bynder's Universal Compact View (UCV) Google Chrome extension lets marketers search for and select Bynder assets without leaving the Braze dashboard. Insert links to those assets directly into campaigns and Canvases.

For more information, see [Bynder]({{site.baseurl}}/partners/bynder).

#### Multiplied Media - Message Personalization - Visual and Interactive Content

[Multiplied Media](https://multiplied.media) is a creative and automation studio that uses your CRM data to create personalized images, GIFs, and video—a unique asset for each customer. The Multiplied Media and Braze integration lets you send this media through email, push notifications, in-app messages, Content Cards, and WhatsApp.

For more information, see [Multiplied Media]({{site.baseurl}}/partners/multiplied_media).

### SDK

The following SDK updates have been released. For more details, see [SDK Changelogs]({{site.baseurl}}/developer_guide/changelogs).

#### SDK breaking updates

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- Unity SDK 12.0.0
    - Updated the native iOS bridge [from Braze Swift SDK 14.1.0 to 18.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/14.1.0...18.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Updated the native Android bridge [from Braze Android SDK 42.2.0 to 43.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v42.2.0...v43.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- Flutter SDK 22.0.0
    - Updates the native Android bridge [from Braze Android SDK 42.3.1 to 43.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v42.3.1...v43.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Updates the native iOS bridge [from Braze Swift SDK 17.0.0 to 18.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/17.0.0...18.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- Swift SDK 18.0.0-18.1.0
    - Renames `Braze.Ecommerce.ProductViewedEvent.typeIdentifiers` to `type` on Swift and Objective-C API surfaces.
    Renames Live Activities push-to-start update events on `Braze.LiveActivities.UpdateEvent.ActivityType`, which are emitted when using Braze.`LiveActivities.subscribeToStateUpdates(_:)`:
        - `pushToStartOptedOut` to `pushToStartUnregistered`
        - `pushToStartOptOutFlushed` to `pushToStartUnregisterFlushed`

#### Summary of recent SDK features and fixes

- **Swift SDK v18.1.0:** Adds push token logout methods, in addition to the existing push logout method, to support additional logout use cases. Also updates the eCommerce event type.
- **Flutter SDK v22.0.0:** Updates the native bridge to inherit functionality from the Android and Swift SDKs.
- **Unity SDK v12.0.0:** Updates the native bridge to inherit functionality from the Android and Swift SDKs.

For more details, see the [SDK Changelogs]({{site.baseurl}}/developer_guide/changelogs).
{% enddetails %}
{% details July 23, 2026 %}

## July 23, 2026 release

### Data & Reporting

#### Messaging Diagnostics dashboard

{% multi_lang_include release_type.md release="General availability" %}

The [Messaging Diagnostics dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) provides a high-level breakdown of message sending outcomes, allowing you to spot trends and diagnose potential issues in your messaging setup. This dashboard can help you understand why messages from your campaigns or Canvases may not have been sent as expected. Contact your customer success manager for access to the feature.

#### CSV Custom Events mapper

{% multi_lang_include release_type.md release="General availability" %}

The [CSV import flow]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import#about-csv-import) for custom events now includes a mapper that lets you map event names and event property headers to Braze fields before import. This update brings the custom events experience in line with the custom attributes flow and reduces the need to reformat files before upload. The flow includes uploading a CSV, mapping required fields and events, mapping event properties, and then selecting targeting preferences before import. If your file already matches the expected format, you can continue through the flow without making mapping changes.

#### Catalogs free storage now supports up to 500 MB

{% multi_lang_include release_type.md release="General availability" %}

The free version of [catalogs]({{site.baseurl}}/user_guide/data/activation/catalogs/create#tiers) now supports up to 500 MB of storage across all CSV files.

### BrazeAI<sup>TM</sup>

#### Operator can now update Settings pages for you

{% multi_lang_include release_type.md release="General availability" %}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator/capabilities) can now make changes directly on more Settings pages, so you can describe a change in natural language instead of clicking through configuration screens. Supported pages include:

- Quiet hours
- Push settings
- Messaging rate limits
- Messaging rules and always-on approval workflows
- Other identifiers and API limits
- Contact information

For example, on the Quiet hours page, ask Operator to set quiet hours from 9 PM to 8 AM for SMS.

#### Remote Braze MCP server

{% multi_lang_include release_type.md release="Early access" %}

The [Braze MCP server]({{site.baseurl}}/user_guide/brazeai/mcp_server) is a remote-hosted connection that lets you connect AI agents such as Claude, ChatGPT, Cursor, VSCode, Codex, Google Antigravity, and Claude Code directly to Braze. Through natural language, agents can read campaign, Canvas, and segment analytics, custom attributes, events, KPIs, and catalogs, and create or update email templates, Content Blocks, and media library assets. No user-profile PII is exposed.

To connect, paste a single endpoint URL into your MCP client—`https://mcp.braze.com/mcp` for US or `https://mcp.braze.eu/mcp` for EU—then sign in with OAuth, including SSO. The server launches with the available tools.

### Orchestration

#### Teams audience scoping

{% multi_lang_include release_type.md release="General availability" %}

The [Teams]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) audience configuration now supports multiple filters.

### Channels & Touchpoints

#### Survey rating scale for in-app messages and landing pages

{% multi_lang_include release_type.md release="Early access" %}

Add a numeric rating scale to a form block in both [landing page surveys]({{site.baseurl}}/user_guide/messaging/landing_pages/create_landing_pages/surveys#rating-scale) and [in-app message surveys]({{site.baseurl}}/user_guide/channels/in_app_messages/drag_and_drop/surveys#rating-scale) to capture sentiment, satisfaction, and likelihood-to-recommend without any custom code. Three ranges are supported: 1–10, 1–5, and 0–10 (the standard NPS range).

#### WhatsApp limited time offer templates

{% multi_lang_include release_type.md release="General availability" %}

[WhatsApp limited time offer templates]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/message_and_image_formats#limited-time-offer-templates) display a time-sensitive promotional offer with an optional countdown as the offer nears expiration. Use this layout for time-boxed promotions, such as seasonal sales or offers personalized to a user attribute.

#### Shopify self-serve SDK version upgrade

{% multi_lang_include release_type.md release="General availability" %}

New [Shopify]({{site.baseurl}}/partners/ecommerce/shopify/) customers are provisioned on the latest Braze Web SDK and JavaScript SDK versions during setup. Existing customers can view their current SDK version in integration settings, get notified when a newer version is available, and self-serve upgrades from integration settings.

#### HTML editor for Banners

{% multi_lang_include release_type.md release="General availability" %}

When you compose a Banner, you can now build it [using the HTML editor]({{site.baseurl}}/user_guide/channels/banners/create_a_banner#compose-a-banner). The HTML editor is best for teams that already maintain their own HTML templates or want full control over markup and styling for Banners. You can write or paste custom HTML directly into the editor.

#### Replace a file in the media library

{% multi_lang_include release_type.md release="General availability" %}

You can now [replace the file of an existing media library asset]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library#replace-a-file) while keeping its URL and asset ID stable. Because the URL doesn't change, any campaign, Canvas, Content Block, or template that references that asset automatically reflects the updated file, so you don't have to manually re-upload or re-link it everywhere it's used.

#### Grid view for the media library

{% multi_lang_include release_type.md release="General availability" %}

The media library and select template libraries now offer a grid view alongside the existing list view. Grid view displays assets as thumbnails with key metadata (name, type, last modified), making it faster to find images and creative by sight instead of by filename. Filtering and search work the same in both views.

#### Shareable Preview support for more channels

{% multi_lang_include release_type.md release="General availability" %}

[Shareable Preview]({{site.baseurl}}/user_guide/channels/email/html_editor#step-3b-preview-and-test-your-message) now supports the following additional channels:

- SMS, MMS, and RCS
- WhatsApp
- Push
- Content Cards
- LINE

From a campaign or message, generate a link and share it with reviewers who don't have Braze dashboard access—brand, legal, or an outside agency, for example. Recipients open the link in any browser to see the message rendered as a customer would, including any test personalization.

#### Push credentials update API

{% multi_lang_include release_type.md release="General availability" %}

You can now update push credentials programmatically with the [Update push credentials endpoint]({{site.baseurl}}/api/endpoints/apps/post_update_push_credential). Each request updates one app and one platform (`apple`, `firebase`, `huawei`, or `kindle`) and accepts credential payloads as Base64-encoded values. This helps teams manage large app portfolios and credential rotation policies without relying on manual dashboard uploads.

### Partnerships

#### Refiner - Surveys

[Refiner](https://refiner.io) is an in-app survey platform for SaaS and mobile apps. It enables product and voice-of-customer teams to launch targeted in-app surveys and continuously collect NPS, CSAT, CES, product feedback, and zero-party user data.

#### Stayfilm - Visual and Interactive Content

[Stayfilm](https://www.stayfilm.com/) is a REST API for automated, personalized video production at scale. The platform integrates data, images, text, soundtracks, narration, and visual effects to generate customized video content for eCommerce, marketplaces, CRM workflows, and marketing campaigns.

#### Validity - Data and Analytics

[Validity Everest](https://www.validity.com/everest/) is an email deliverability platform that helps you measure inbox placement and protect your sending reputation. The Braze and Validity integration syncs your Everest seed list to Braze, automatically seeds qualifying campaigns and Canvases, and pulls engagement metrics back into Validity Inbox so you can compare seed-based placement with real subscriber engagement.

### SDK

The following SDK updates have been released. For more details, see [SDK Changelogs]({{site.baseurl}}/developer_guide/changelogs).

#### SDK breaking updates

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

- [Android SDK 43.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v43.0.0)
    - Adds `unregisterPush` and logout methods.
    - Adds additional fields to eCommerce events.
    - Adds exponential backoff for push notification image loading.
- [Swift SDK 17.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Adds additional fields to eCommerce events.
    - Makes data states predictable after initialization.
    - Adds non-blocking accessors for device and user identifiers.
    - Removes the deprecated push-to-start update API on `Braze.LiveActivities`.
- [Web SDK 6.10.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
    - Adds `unregisterPush` and logout methods.
    - Adds additional fields to eCommerce events.
    - Fixes a Banner and Content Card issue related to redundant refreshes on startup.
    - Adds a public method for Banner dismissal.
- [Flutter SDK 21.0.0](https://github.com/braze-inc/braze-flutter-sdk/releases/tag/v21.0.0)
    - Updates the native iOS bridge.
    - Removes deprecated methods.
    - Updates `changeUser`, `enableSDK`, and `disableSDK` handlers to return completion results.
- [Expo SDK 5.2.0](https://github.com/braze-inc/braze-expo-plugin/releases/tag/v5.2.0)
    - Updates the sample app to Expo SDK 56.
- [React Native SDK 22.0.0](https://www.npmjs.com/package/@braze/react-native-sdk/v/22.0.0)
    - Adds support for Banner dismissals.
    - Includes binding updates.

{% enddetails %}
{% details June 25, 2026 %}

## June 25, 2026 release

### Data & Reporting

#### Metric name update for Content Cards and Banners

The _Unique Recipients_ metric has been renamed to _Unique Daily Impressions_ for Content Cards and Banners. _Unique Daily Impressions_ refer to the number received from Braze and is based on the `user_id`. Unique daily impressions are counted at the campaign or Canvas step level. For more details, refer to the [Metrics glossary]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

#### User deletion

{% multi_lang_include release_type.md release="General availability" %}

[User deletion]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users/) lets you manage your database by removing profiles that are no longer needed, created in error, or required to be deleted for compliance (such as GDPR or CCPA).

#### Data point exclusions

{% multi_lang_include release_type.md release="General availability" %}

[eCommerce recommended events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events/) no longer count toward billable data points. You can adopt Braze eCommerce events (`ecommerce.product_viewed`, `ecommerce.cart_updated`, `ecommerce.checkout_started`, `ecommerce.order_placed`, `ecommerce.order_cancelled`, `ecommerce.order_refunded`) without data point consumption.

#### Event History tab

{% multi_lang_include release_type.md release="General availability" %}

The **Event History** tab on [user profiles]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/) lists the user's custom events and purchases from the past 30 days (up to 100 most recent). Use it to confirm an SDK or API integration is sending events as expected, debug why a user did (or didn't) enter an event-triggered campaign or Canvas, or investigate a support escalation about a specific user.

#### Deliverability Center surfaces Microsoft SNDS data for Amazon SES customers

For workspaces that send email through Amazon SES, the [Deliverability Center]({{site.baseurl}}/deliverability_center/) displays Microsoft SNDS metrics for your dedicated sending IPs. Braze backfills up to 90 days of historical SNDS data when this feature is turned on for your workspace.

### BrazeAI<sup>TM</sup>

#### Unified BrazeAI assistants in Operator

The standalone BrazeAI assistants found throughout the dashboard are unified into [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/), establishing Operator as the single AI assistant for marketer-facing generative AI assistance across the dashboard. The following assistants now route through Operator:

{% multi_lang_include releases/brazeai_operator_legacy_assistants.md %}

The existing entry points remain where each legacy assistant button used to live. Instead of opening a standalone assistant, these entry points now open the Operator pane with dynamic prompts that are pre-scoped to your task. These entry points provide a direct route into Operator so you can use these capabilities without adjusting your existing workflows.

#### Operator support for campaign creation and editing

[Operator]({{site.baseurl}}/user_guide/brazeai/operator/) can now create and edit entire campaigns, not just compose messages. From a single natural-language prompt or campaign brief, Operator builds a ready-to-review campaign end to end—composing the message, scheduling delivery, targeting an audience, and assigning conversion events—then recaps what it built in the review step. Previously, Operator could compose the message (one of the five campaign creation steps); it now has visibility and control over the remaining Schedule, Target, Assign, and Review steps.

This functionality is available from the **Campaigns** page or from within any existing campaign. As a result, Operator can:

{% multi_lang_include releases/brazeai_operator_campaign_creation_prompts.md %}

#### Operator support for Content Blocks

[Operator]({{site.baseurl}}/user_guide/brazeai/operator/) can now create and edit [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/)—the reusable snippets you build once and reference across multiple messages—directly from a natural-language prompt. From the **Content Blocks** page, ask Operator to create a new Content Block from scratch or edit an existing one, and Operator generates or updates the content for you to review.

#### Agent Console templates built with Operator

When building an agent in **Agent Console**, you can choose to create a custom agent or select an option in **Create an agent with Operator** to use BrazeAI Operator to apply a starting template. Operator can pre-configure instructions, output fields, and context for the following Agent Console starting templates.

For more details, see [Create custom agents]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#agent-templates-built-with-operator).

#### Agent Console enhancements

You can do the following in the [Agent Console]({{site.baseurl}}/user_guide/brazeai/agents/):

{% multi_lang_include releases/brazeai_agent_console_enhancements.md %}

#### Edit a launched Content Optimizer step

{% multi_lang_include release_type.md release="Beta" %}

After your Canvas is launched, you can now [update a Content Optimizer step]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/content_optimizer_step/#edit-a-launched-step) to:

{% multi_lang_include messaging/canvas/content_optimizer_launched_step_actions.md %}

### Channels & Touchpoints

#### User dismissals for Banners

{% multi_lang_include release_type.md release="General availability" %}

You can allow users to manually dismiss a Banner by selecting **Banner can be dismissed** when configuring dismissal behavior. This option is beneficial in scenarios where you want to promote a limited-time sale for all app users, but allow them to dismiss the message if they aren't interested.

See [Configure dismissal behavior]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#dismiss-behavior) for details on enabling dismissal and customizing the dismiss button.

#### Custom click tracking for Banners

{% multi_lang_include release_type.md release="General availability" %}

For more granular click tracking for Banners, you can [assign a custom identifier]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#step-32-define-on-click-behavior-optional) to each interactive element using the **Identifier for Reporting** field in its properties panel.

#### Re-eligibility for Banners

When re-eligibility is enabled for Banner campaigns, users who dismiss a Banner can become eligible again after a configurable cooldown window that starts at dismissal. If re-eligibility isn't turned on, dismissed users remain ineligible. To configure re-eligibility, see [Configure re-eligibility]({{site.baseurl}}/user_guide/channels/banners/create_a_banner/#re-eligibility). Note that Canvas Banner steps use Canvas re-entry settings instead.

#### Quick Push A/B Testing

{% multi_lang_include release_type.md release="General availability" %}

Quick Push A/B Testing now supports multi-platform push campaigns and Canvas steps through variant groups, so you can test aligned iOS and Android message variations in one workflow. For more information, refer to [Multiple platform push messages]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/multiple_platform_push/#use-cases).

#### Optimize with BrazeAI™

{% multi_lang_include release_type.md release="Early access" %}

**Optimize with BrazeAI™** automatically turns on when you add multiple push variants, applies recommended experiment defaults, and optimizes toward the highest-performing variant. You can turn it off if you need to send immediately. For more information, see [Optimizing A/B tests with BrazeAI]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection).

#### WhatsApp test send results

After sending a test WhatsApp message, you can view a [detailed delivery report]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/#step-4-view-test-send-results) directly in the message composer. This helps you confirm your message reached the intended recipient and troubleshoot failures before launch.

### Partnerships

#### Convercus - Data and Analytics - Loyalty

[Convercus]({{site.baseurl}}/partners/data_and_analytics/loyalty/convercus/) is a SaaS loyalty and coupon platform that helps brands and retailers grow customer frequency, basket value, and repurchase rates through omnichannel loyalty programs and personalized coupon campaigns.

#### Copy Pastd - Message Orchestration - Templates

[Copy Pastd]({{site.baseurl}}/partners/copy_pastd/) Building Blocks is a drag-and-drop email builder that pushes Liquid-powered Content Blocks and full templates directly into your Braze workspace. Design once, sync to Braze, and reuse the same components across campaigns, Canvases, and triggered flows without rebuilding HTML each time.

#### Databricks Mosaic - AI Model Providers

[Databricks Mosaic]({{site.baseurl}}/partners/ai_model_providers/databricks_mosaic) is Databricks' unified platform for building, deploying, and managing AI and machine learning models at scale on the Databricks Data Intelligence Platform.

#### DinMo - Data and Analytics - Reverse ETL

[DinMo]({{site.baseurl}}/partners/dinmo/) is a composable customer data platform (CDP) that connects your cloud data warehouse to Braze through reverse Extract, Transform, Load (ETL). Marketing teams can build audience segments from warehouse data, sync user attributes and events into Braze, and keep subscription statuses up to date without CSV uploads or engineering support.

#### EmailShepherd - Message Orchestration - Templates

[EmailShepherd]({{site.baseurl}}/partners/emailshepherd/) is an agentic email creation platform built on your Email Design System that allows your whole marketing team—and AI agents—to produce on-brand, production-ready emails without bottlenecks. The Braze integration publishes approved emails directly to your Braze workspace, so marketers can scale email production in Braze without sacrificing brand consistency.

#### Talkable - Message Personalization - Referrals

[Talkable]({{site.baseurl}}/partners/talkable/) helps consumer brands turn happy customers into a scalable referral channel. With the Braze integration, marketing email opt-ins captured in Talkable referral campaigns flow into Braze in real time, giving your team the consent, context, and campaign data you need to welcome, segment, and engage every new advocate and friend.

### SDK

#### SDK breaking updates

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

{% multi_lang_include releases/sdk/2026_6_25_26_updates.md %}

{% enddetails %}

{% details May 28, 2026 %}

## May 28, 2026 release

### Data & Reporting

#### Push Performance dashboard

The [Push Performance dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance?tab=push%20performance#push-performance-dashboard) gives you a single, channel-level view of push engagement, including sends, bounces, deliveries, and direct, influenced, and total open rates over a configurable time window. Use it to understand the overall health of your push channel without rolling up data from individual campaigns or Canvases.

#### Geolocation fields in catalog selections

{% multi_lang_include release_type.md release="General availability" %}

Catalogs now support distance-based filtering with the new geolocation field type and Catalog Selection operators. This helps you create more relevant location-aware experiences, such as showing each user their nearest restaurant, filtering open properties within 50 km for a real estate campaign, or targeting stores near a specific event. Instead of approximating geographic targeting with city or region codes, you can filter catalog items by proximity to a center point, including a Liquid user attribute such as a user's most recent location. For more information, see [Selections]({{site.baseurl}}/user_guide/data/activation/catalogs/selections).

#### Banner and RCS for Report Builder

[Report Builder]({{site.baseurl}}/report_builder/) supports Banner as a channel and RCS as a sub-category under SMS, so you can measure performance for both directly in your custom reports alongside every other Braze channel.

#### `ecommerce.cart_updated` event actions

The [`ecommerce.cart_updated` event]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/?tab=ecommerce.cart_updated#code-examples) supports `add` and `remove` actions alongside `replace`, allowing you to send incremental cart changes instead of a full cart snapshot on every update. 

### BrazeAI<sup>TM</sup>

#### Content Optimizer for SMS, MMS, and RCS messages

{% multi_lang_include release_type.md release="Beta" %}

You can use [Content Optimizer]({{site.baseurl}}/user_guide/brazeai/content_optimizer) to optimize hooks, bodies, and CTAs for SMS, MMS, and RCS messages. Content Optimizer helps you test and optimize message content at scale, using AI to generate and evaluate high volumes of content variants automatically.

### Orchestration

#### Workspace time zones

{% multi_lang_include release_type.md release="General availability" %}

Use [workspace time zones]({{site.baseurl}}/user_guide/administer/global/admin_settings/workspace_time_zone) to define specific time zones for individual workspaces. This makes scheduled campaigns and Canvases (that don’t use local time or Intelligent Timing) send according to the workspace's designated time zone, rather than the overarching company time zone.

Workspace time zones for message sending are rolling out gradually, so you may not see these settings in your dashboard yet.

### Channels & Touchpoints

#### WhatsApp `inbound_profile_name`

You can automatically capture a user's WhatsApp display name from Meta's inbound messaging webhook and write it to the user's Braze profile. When an inbound WhatsApp message is received, Braze exposes the profile name as a new WhatsApp Liquid attribute, [{% raw %}`{{whats_app.${inbound_profile_name}}}`{% endraw %}]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/), which you can reference in a Canvas User Update step to save to a profile field.

#### Orphaned SMS subscription states

Braze [automatically manages orphaned subscription state records]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/#how-braze-handles-orphaned-subscription-states) (subscription data stored for a phone number or email address not tied to any user profile) to prevent unintended subscription state inheritance. This protects users from scenarios where a newly created user profile incorrectly inherits subscription state from a previously deleted or unrelated user.

### Partnerships

#### Chord - Customer Data Platform

[Chord](https://www.chord.co/) provides a customer data platform that captures and standardizes events from your eCommerce storefront. When you connect Chord to Braze, purchase activity, behavioral events, and identity updates flow into Braze so you can trigger campaigns and keep profiles current without building those pipelines yourself.

For more information, see [Chord]({{site.baseurl}}/partners/chord/).

#### Better Email - Templates

[Better Email](https://www.betteremail.dev) is a collaborative email creation platform built around an Email Design System. Teams can design, manage, and export production-ready emails from a shared system of blocks and styles, ensuring brand consistency at scale without relying on developers or agencies.

For more information, see [Better Email]({{site.baseurl}}/partners/better_email/).

#### DailyPlay - Dynamic Content

[DailyPlay](https://dailyplay.ai/) is a gamification platform. Use it to launch personalized, branded games and built-in reward systems that deepen engagement and improve retention.

For more information, see [DailyPlay]({{site.baseurl}}/partners/dailyplay/).

### SDK

#### SDK breaking updates

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

{% multi_lang_include releases/sdk/2026_5_28_26_updates.md %}

{% enddetails %}
{% details April 30, 2026 %}

## April 30, 2026 release

### Data & Reporting

#### Quick User Add for individual profile creation

{% multi_lang_include release_type.md release="General availability" %}

You can now create an individual user profile from **Import Users** by selecting **Quick User Add** and entering an email or external ID.

Previously, creating users from this workflow required CSV upload or an automated ingestion method.

For more information, see [CSV import]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import/).

#### Zero-copy CDI syncs for Canvas triggers

{% multi_lang_include release_type.md release="General availability" %}

CDI now supports the `Canvas triggers` data type for zero-copy personalization. You can trigger Canvases from warehouse or S3 data and pass context fields without persisting those fields on Braze user profiles.

Previously, CDI syncs required data to be written to Braze profiles for this type of personalization workflow.

For more information, see [Zero-copy personalization using CDI]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync/).

#### eCommerce recommended events

{% multi_lang_include release_type.md release="General availability" %}

[eCommerce recommended events]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/) cover six steps in the purchase journey: `product_viewed`, `cart_updated`, `checkout_started`, `order_placed`, `order_cancelled`, and `order_refunded`. When you successfully send these events, Braze validates the data and makes it available to a growing set of platform features.

### Currents and Datashare

#### New Banner and WhatsApp Currents updates

{% multi_lang_include release_type.md release="General availability" %}

Currents and Datashare now include a new `Banner.Dismiss` event and additional fields for existing WhatsApp events.

Previously, these Banner dismissal events and WhatsApp fields were not available in export data.

For more information, see [Currents changelog]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs).

### Orchestration

#### Multi-language translations

{% multi_lang_include release_type.md release="General availability" %}

Compose [multi-language messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) with quick, one-time locale setup that doesn’t require complex code and enables you send to all of your markets with confidence.

#### Granular permissions migration

{% multi_lang_include release_type.md release="General availability" %}

Managing who can access your account and perform specific actions is critical for both security and operational efficiency. To give you more control, Braze is introducing [granular permissions]({{site.baseurl}}/user_guide/administer/global/user_management/permissions), a more flexible and precise way to manage user access across your account.

#### Send to Destination Canvas component

{% multi_lang_include release_type.md release="General availability" %}

The [Send to Destination step]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/send_to_destination) allows you to send users from one Canvas to another. For example, if you have two Canvases that share messaging for promotional offers, you can use Send to Destination to connect these Canvases.

#### Canvas Context enhancements

{% multi_lang_include release_type.md release="General availability" %}

In Canvas, you can now reference context variables to set:

- A removal event for Content Cards
- The expiration of Content Cards

For more details, see [Card creation]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card/card_creation/?tab=canvas).

#### Delivery validation advancement behavior for Message steps

{% multi_lang_include release_type.md release="General availability" %}

[Delivery validations]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step/#delivery-validations) provide an additional check to confirm your audience meets the delivery criteria at message send. If a user doesn’t meet the set delivery validations for a Message step, you can use the **Delivery validations advancement behavior** setting to determine if the user should advance to the next step or exit the Canvas.

#### Workspace messaging rate limits

{% multi_lang_include release_type.md release="General availability" %}

Use [workspace messaging rate limits]({{site.baseurl}}/user_guide/administer/global/workspace_settings/messaging_rate_limits) to regulate the delivery rate of your outgoing messages from your platform to make sure your users are receiving the messages they need to. Workspace messaging rate limits are rolling out gradually, so you may not see these settings in your dashboard yet.

### Channels & Touchpoints

#### WhatsApp Template Builder

{% multi_lang_include release_type.md release="Early access" %}

The [WhatsApp Template Builder]({{site.baseurl}}/user_guide/channels/whatsapp/message_features_and_optimization/) lets you create and submit WhatsApp message templates directly in Braze—no need to switch between Braze and the Meta Business Manager. After Meta approves your template, use it in as many campaigns and Canvases as you’d like.

#### Shopify product tags, metafields, and collections

{% multi_lang_include release_type.md release="General availability" %}

You can now [sync Shopify product tags, collections, and metafields]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/) from your Shopify store into your Braze catalog. This provides richer product data for personalization, segmentation, and catalog-based messaging without custom workarounds.

### Partnerships

#### GRAVITY - Data and Analytics - Loyalty

{% multi_lang_include release_type.md release="General availability" %}

[GRAVTY®](https://www.lji.io/) is an enterprise-grade loyalty platform from Loyalty Juggernaut Inc. (LJI) that enables brands across retail, travel, restaurants (including quick-service restaurants), and financial services to design, manage, and scale next-generation programs—driving measurable growth in engagement, retention, and customer lifetime value through personalized, data-led experiences.

<!-- Use this section to list any new SDKs or SDK updates that are already released. -->
### SDK

The following SDK updates have been released. For more details, see [SDK changelogs]({{site.baseurl}}/releases/sdk_changelogs/).

#### SDK breaking updates

{% multi_lang_include release_type.md release="General availability" %}

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

{% multi_lang_include releases/sdk/2026_4_30_26_updates.md %}

{% enddetails %}
{% details April 2, 2026 %}

## April 2, 2026 release

### Data & Reporting

#### New Banner channel fields in Currents and Datashare events

Braze added fields for existing Banner channel events in Currents and Datashare exports. For a list of these event and field updates, see [Changes in Version 7]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-for-storage).

#### Mixpanel EU and India data center support for Currents

The Currents Mixpanel integration now supports Mixpanel's EU and India data centers. When you configure a Mixpanel integration, you can choose which Mixpanel region Braze sends your data to. This update supports Mixpanel's growing international footprint for mutual customers. For more information, see [Mixpanel]({{site.baseurl}}/partners/data_and_analytics/analytics/mixpanel).

#### Reusable Cloud Data Ingestion (CDI) sources and syncs

{% multi_lang_include release_type.md release="Early access" %}

Cloud Data Ingestion (CDI) has a new design that separates sources and syncs, so you can reuse one source across multiple syncs. Existing syncs migrate automatically to the new sources and syncs model with no downtime. Go to **Cloud Data Ingestion** > **Sources** to view, edit, or create sources, then select a source from the dropdown when creating a sync. This change reduces repetitive setup, and creates a foundation for future enhancements. For more information, see [Setting up data warehouse integrations]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#setting-up-data-warehouse-integrations).

### BrazeAI<sup>TM</sup>

#### File support tickets from BrazeAI Operator<sup>TM</sup>

{% multi_lang_include release_type.md release="General availability" %}

[BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/) now includes a flow to file Braze support tickets without leaving the dashboard. For steps, auto-included context, and tips for faster resolution, see [File support tickets with BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/support_tickets/).

### Orchestration

#### Multi-language translations

{% multi_lang_include release_type.md release="General availability" %}

After adding locales to your workspace, use [multi-language translations]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) to target users in different languages all within a single push, email, Banner, in-app message, or Content Block.

![Locale previews]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %}){: style="max-width:70%;"}

#### Canvas Context enhancements

{% multi_lang_include release_type.md release="General availability" %}

In Canvas, you can now reference context variables to set:

- An [expiration]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) for Banners and in-app messages in a Message step
- A [personalized delays]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables) for Action Paths steps

In the Context variable name field, you can also enter the context variable name or select it from the dropdown in the step editor. For more details, see [Context]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) and [Context variables]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables).

### Channels & Touchpoints

#### KakaoTalk

{% multi_lang_include release_type.md release="General availability" %}

[KakaoTalk]({{site.baseurl}}/kakaotalk) is a messaging channel that enables broadcast messaging and 1:1 chat with users. Create a personalized user experience by using Liquid and other dynamic content to build an environment that fosters and enhances a rich user experience with your brand.

![A KakaoTalk list item message.]({% image_buster /assets/img/kakaotalk/wide_image.png %}){: style="max-width:70%;"}

#### Banners in Canvas

{% multi_lang_include release_type.md release="General availability" %}

You can use [Banners]({{site.baseurl}}/user_guide/channels/banners) as a messaging channel in Canvas [Message steps]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step). Banners allow you to personalize app or website content dynamically, reflecting real-time user eligibility and behavior.

### Partnerships

#### CataBoom - Message Personalization - Visual and Interactive Content

[CataBoom]({{site.baseurl}}/partners/cataboom) is a gamification platform. Brands use it to build and launch interactive digital experiences, including spin-to-win games, quizzes, and instant-win games. Those experiences deepen engagement and collect first-party data.

#### Denada - Message Orchestration - Templates

[Denada]({{site.baseurl}}/partners/denada) is an AI-powered marketing creative platform that lets subject matter experts create on-brand marketing materials through natural conversation. With Denada, teams can go from ideation to finished email content without needing design expertise.

#### Poq - eCommerce - Mobile app platform

[Poq]({{site.baseurl}}/partners/poq) enables enterprise businesses to rapidly launch, manage, and scale fully native iOS and Android apps—delivering high-performance mobile experiences that drive commerce and bring your brand promise to life.

#### The Trade Desk – Canvas Audience Sync

Using the [Braze Audience Sync to The Trade Desk]({{site.baseurl}}/partners/canvas_audience_sync/trade_desk_audience_sync/), you can dynamically sync your first-party user data from Braze directly into The Trade Desk for ad retargeting, lookalike modeling, and suppression.

### SDK

#### Connect your Integrated Development Environment (IDE) to the Docs MCP

Use AI coding assistants to accelerate your Braze integration workflow by connecting your Integrated Development Environment (IDE) to the Braze Docs MCP through Context7. This gives your assistant direct access to current Braze documentation, so it can generate more accurate SDK guidance, code examples, and troubleshooting help in your development environment. For setup steps in Cursor, Claude Desktop, and VS Code, see [Building with an LLM]({{site.baseurl}}/developer_guide/getting_started/build_with_llm/#connecting-to-the-braze-docs-mcp).

#### SDK breaking updates

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

{% multi_lang_include releases/sdk/2026_4_2_26_updates.md %}

{% enddetails %}

{% details March 5, 2026 %}

## March 5, 2026 release

### Data & Reporting

#### New data center

{% multi_lang_include release_type.md release="General availability" %}

Braze has launched a new [data center]({{site.baseurl}}/user_guide/data/infrastructure/data_centers/): JP-01. You can sign up for region-specific data centers when setting up your Braze account.

#### Context variables

{% multi_lang_include release_type.md release="General availability" %}

[Context variables]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) are temporary pieces of data you can create and use within a user’s journey through a specific Canvas. Each time a user enters the Canvas—even if they have entered it before—the context variables will be redefined based on the latest entry data and Canvas setup. This approach allows each Canvas entry to maintain its own independent context, allowing users to have multiple active states within the same journey while retaining the specific context for each state.

#### Cloud Data Ingestion sources

{% multi_lang_include release_type.md release="Early access" %}

[Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/#setting-up-cloud-data-ingestion-in-braze) has a new UI that separates sources from syncs, letting you reuse a single source across any number of syncs. This reduces duplicate configuration and simplifies setup when you have multiple syncs. If you have existing syncs, they're automatically migrated to the new sources-and-syncs structure with no downtime. To get started, go to **Cloud Data Ingestion** > **Sources** to view, edit, or create sources, then select a source from the dropdown when creating a sync.

#### Additional fields for Currents and Data Share events

{% multi_lang_include release_type.md release="General availability" %}

[Currents and Data Share events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04) now include the following new fields to deepen the data available for analytics and downstream systems:

{% multi_lang_include releases/currents/2026_3_5_26_field_changes.md %}

#### Campaign and Canvas fields for Snowflake Data Share

{% multi_lang_include release_type.md release="General availability" %}

[Snowflake Data Share]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) now includes additional fields reflecting Campaign and Canvas information across 66 existing tables, including:

- `campaign_name`
- `canvas_name`
- `canvas_step_name`
- `canvas_variation_name`
- `message_variation_name`
- `conversion_behavior`
- `experiment_split_name`

#### CSV pre-import validation and error reporting

{% multi_lang_include release_type.md release="General availability" %}

[CSV user imports]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/) now support pre-import validation and detailed error reporting. Before importing, select **Validate file before importing** on the **Import Users** page—Braze will scan your file and generate a report identifying rows that will fail entirely (errors) and rows that will succeed with some values skipped (warnings). You can download the report, fix your CSV, and re-upload, or proceed as-is. After the import completes, a downloadable report of any rows that failed is also available, with the exact reason for each issue.

#### Messaging diagnostics dashboard

{% multi_lang_include release_type.md release="Early access" %}

The [Messaging Diagnostics dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard/) provides a high-level breakdown of message sending outcomes, allowing you to spot trends and diagnose potential issues in your messaging setup. This dashboard can help you understand why messages from your campaigns or Canvases may not have been sent as expected.

### BrazeAI<sup>TM</sup>

#### Braze Agents in Agent Console

{% multi_lang_include release_type.md release="General availability" %}

[Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/) are AI-powered helpers you can create inside Braze. Agents can generate content, make intelligent decisions, and enrich your data so you can deliver more personalized customer experiences. When you create an agent, you define its purpose and set guardrails for how it should behave. After it’s live, the agent can be [deployed]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents) in Braze to generate personalized copy, make real-time decisions, or update catalog fields.

### Orchestration

#### Granular user permissions

{% multi_lang_include release_type.md release="Early access" %}

Braze is introducing [granular permissions]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/), a more flexible way to manage user access. Refer to [Migrating to granular permissions]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) to learn about the migration process, including how legacy permissions map to granular permissions.

#### Channel-based rate limiting

{% multi_lang_include release_type.md release="General availability" %}

When setting a delivery speed rate limit for a multi-channel campaign or Canvas, you can choose to set either a shared rate limit or a [channel-based limit]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/#multichannel-campaigns-and-canvases). When a multichannel campaign or Canvas uses channel-based rate limiting, the rate limit applies to each of the selected channels. For example, you can set your campaign or Canvas to send a maximum of 5,000 webhooks and 2,500 SMS messages per minute across the campaign or Canvas.

#### Canvas Context step

{% multi_lang_include release_type.md release="General availability" %}

[Canvas Context steps]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context) let you create and update one or more variables for a user as they move through a Canvas. For example, if you have a Canvas that manages seasonal discounts, you can use a context variable to store a different discount code each time a user enters the Canvas.

### Channels & Touchpoints

#### Translate locales in Content Blocks

{% multi_lang_include release_type.md release="Early access" %}

After adding locales to your workspace, you can [target users in different languages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) all within a Content Block.

### Partnerships

#### Algolia - Search Recommendations

[Algolia]({{site.baseurl}}/partners/ecommerce/product_search_recommendations/algolia) is a search and discovery platform that helps developers build fast, relevant, and scalable search experiences. With a powerful API-first approach, Algolia combines advanced ranking algorithms with AI-driven insights for seamless site search, navigation, and personalized content discovery.

#### Anthropic - AI Model Provider

[Anthropic]({{site.baseurl}}/partners/ai_model_providers/anthropic) is an AI safety and research company developing Claude, a next-generation AI assistant built to be helpful, honest, and safe for a wide range of language tasks.

#### Canva - Message Personalization - Creative Studio

[Canva]({{site.baseurl}}/partners/canva) syncs your images in Canva directly to the Braze Media library, streamlining your creative workflow and keeping your visual assets up to date across all your messaging channels.

#### DOTS.ECO - Rewards

[DOTS.ECO]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/rewards/dots_eco) lets you reward users with real-world environmental impact through trackable digital certificates. Each certificate can include metadata like a shareable certificate URL and image URL, so users can view (and revisit) their proof of impact.

#### Figma - Message Personalization - Creative Studio

[Figma]({{site.baseurl}}/partners/figma) is a collaborative design platform that allows you to build, design, and prototype products. Use this integration to send images and visual assets from Figma directly into the Braze media library.

#### Flybuy - Message Personalization - Location

[Flybuy]({{site.baseurl}}/partners/message_personalization/location/flybuy) by Radius Networks is the leading omnichannel location platform leveraging AI-powered technology to optimize speed of service across pickup, delivery, drive-thru, and dine-in. Through its integrated Marketing Suite, Flybuy also enables brands to deliver hyper-targeted, moment-based messages, helping to drive engagement, increase check size, and support broader loyalty initiatives.

#### Google Gemini - AI Model Provider

[Google Gemini]({{site.baseurl}}/partners/ai_model_providers/google_gemini) is Google’s family of AI models that combines advanced reasoning across text, code, and images to help brands deliver smarter, more personalized experiences.

#### Limbik - Message Personalization - Personalization Engines

[Limbik]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalization_engines/limbik) is your AI resonance layer—predicting how real audiences interpret and respond to messages, concepts, and AI outputs before they reach the market. Powered by continuous primary research across 60+ countries and 25+ languages, Limbik delivers human-validated synthetic audiences—digital populations that simulate real audience response at machine speed and with research-grade accuracy (95% confidence, 1.5% to 3% margin of error). Limbik gives you the ability to immediately ensure your messaging resonates with what your target audience believes and feels.

#### Linkrunner - Message Orchestration - Attribution

[Linkrunner]({{site.baseurl}}/partners/message_orchestration/attribution/linkrunner) is a mobile attribution and analytics platform that helps you track and analyze your user acquisition campaigns.

#### Mailizio - Message Orchestration - Templates

[Mailizio]({{site.baseurl}}/partners/message_orchestration/templates/Mailizio) is an email creation and management platform that makes it easy to design reusable, brand-safe content using an intuitive visual editor. With Mailizio's integration to Braze, you can export your content blocks and email templates, then automatically generate in-app messages from those same assets, enabling fast and fully controlled campaign deployment.

#### Open Loyalty - Data and Analytics - Loyalty

[Open Loyalty]({{site.baseurl}}/partners/data_and_analytics/loyalty/openloyalty) is a cloud-based loyalty program platform that lets you build and manage customer loyalty and rewards programs. The Braze and Open Loyalty integration syncs loyalty data—such as points balance, tier changes, and expiry warnings—directly into Braze in real-time. This lets you trigger personalized messages (Email, Push, SMS) when a user's loyalty status changes.

#### OpenAI - AI Model Provider

[OpenAI]({{site.baseurl}}/partners/ai_model_providers/openai) creates advanced AI models, like GPT, that enable natural language understanding and generation, empowering brands to build and scale meaningful customer interactions.

#### Shopgate - Channels

[Shopgate]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/shopgate) is a mobile commerce and omnichannel platform that helps merchants create shopping apps and improve the efficiency of brick-and-mortar stores through fulfillment tools and clienteling, meaning personalized in-store customer support based on customer data.

#### Splio - Data and Analytics - Cohort Import

[Splio]({{site.baseurl}}/partners/data_and_analytics/cohort_import/splio) is an audience-building tool that lets you increase the number of campaigns and revenue without harming customer experience, and provides analytics to track the performance of CRM campaigns both online and offline.

### SDK

#### SDK breaking updates

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

{% multi_lang_include releases/sdk/2026_3_5_26_updates.md %}

{% enddetails %}

{% details February 5, 2026 %}

## February 5, 2026 release

### BrazeAI<sup>TM</sup>

#### Content Optimizer

{% multi_lang_include release_type.md release="Beta" %}

[Content Optimizer]({{site.baseurl}}/user_guide/brazeai/content_optimizer) is a continuous, high-variant content testing Canvas step that delivers automated engagement optimization. Using a drag-and-droppable interface similar to the message step, define the components to test, generate variants using AI (or enter them manually), and use Liquid tags to map these components to your message content.

Built on a non-contextual multi-armed bandit optimizer, Content Optimizer sends a single message per user, determining which combination of component variants to deliver based on predictive recommendations. As the step gathers data over time, high-performing variants naturally increase in send allocation while poor-performing variants decrease. Content Optimizer works best with repeated-send Canvases that have consistent daily user volume (at least a few thousand users per day) to enable continuous optimization.

### Data & Reporting

#### eCommerce recommended events

{% multi_lang_include release_type.md release="Early access" %}

To match eCommerce recommended events with the existing purchase event, we added the ["Places Order" conversion event]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/ecommerce_use_cases#conversions-dashboard), which is similar to “Makes Purchase".

### Channels & Touchpoints

#### Translate locales in banners

{% multi_lang_include release_type.md release="Early access" %}

After adding locales to your workspace, [target users in different languages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#use-locales) all within a single banner.

#### Configure width for drag-and-drop Content Blocks

[Adjust the width of your Content Block]({{site.baseurl}}/user_guide/messaging/design_and_edit/editor_blocks?sdktab=email) by selecting the button in the navigation menu. The default width is 100% when not specified in your email global style settings; otherwise, the global settings will be honored.

![A double-sided arrow with an option to edit the width.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }

#### Use automated IP warming

{% multi_lang_include release_type.md release="Early access" %}

Use [automated IP warming]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/#automated-ip-warming) to gradually increase your daily send volume, allowing inbox providers to learn and trust your sending patterns. Braze sends to your most engaged subscribers first, which allows daily volume to grow at a pace that matches best practices.

### Partnerships

#### LinkedIn – Canvas Audience Sync

Using the [Braze Audience Sync to LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync/), add user data from your Braze integration to LinkedIn customer lists to deliver advertisements based on behavioral triggers, segmentation, and more. Any criteria normally used to trigger a message (such as push, email, SMS, and webhook) in a Braze Canvas based on user data can now trigger an ad to that user in your LinkedIn customer lists.

#### Oracle Crowdtwist - Data & analytics

[Oracle Crowdtwist]({{site.baseurl}}/partners/crowdtwist) is a leading cloud-native customer loyalty solution to empower brands to offer personalized customer experiences. Their solution offers over 100 out-of-the-box engagement paths, providing rapid time-to-value for marketers to develop a more complete view of the customer.

#### Fullstory - Dynamic Content

[Fullstory’s]({{site.baseurl}}/partners/fullstory/) behavioral data platform helps technology leaders make better, more informed decisions. By injecting digital behavioral data into their analytics stack, Fullstory's patented technology unlocks the power of quality behavioral data at scale–transforming every digital visit into actionable insights. 

#### Open Loyalty - Data & analytics

[Open Loyalty]({{site.baseurl}}/partners/openloyalty) is a cloud-based loyalty program platform that lets you build and manage customer loyalty and rewards programs. The Braze and Open Loyalty integration syncs loyalty data—such as points balance, tier changes, and expiry warnings—directly into Braze in real-time. This lets you trigger personalized messages (Email, Push, SMS) when a user's loyalty status changes.

#### DOTS.ECO - Extensions

[DOTS.ECO]({{site.baseurl}}/partners/dots.eco) lets you reward users with real-world environmental impact through trackable digital certificates. Each certificate can include metadata like a shareable certificate URL and image URL, so users can view (and revisit) their proof of impact.

#### Mailizio - Message orchestration

[Mailizio]({{site.baseurl}}/partners/mailizio/) is an email creation and management platform that makes it easy to design reusable, brand-safe content using an intuitive visual editor. With Mailizio's integration to Braze, export your content blocks and email templates, then automatically generate in-app messages from those same assets, enabling fast and fully controlled campaign deployment.

### APIs

#### Media Library POST APIs

{% multi_lang_include release_type.md release="General availability" %}

Media Library assets can now be added via API, enabling customers, partners, and agencies to automate more of their message creation workflows. Use the [API]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) to upload an asset file directly or copy a file from an existing URL. This feature unlocks integration and automation capabilities.

### Currents and Datashare

#### Agent Console Events for Storage destinations and Datashare

{% multi_lang_include release_type.md release="General availability" %}

Two new [events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) are now available for Storage destinations (AWS S3, GCS, and Azure Blob Storage) and Snowflake Datashare: `agentconsole.AgentExecuted` and `agentconsole.ToolInvocation`. These events enable you to analyze Agent Console usage and details in your downstream systems, helping you understand and get the most out of your agent usage. Agents allow you to create and deploy intelligent agents that can perform specific tasks across Braze, including generating content in canvases or catalogs and routing users down different paths based on intelligent decisioning. For more information, see the [Currents changelog]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### New 'Retry' events for individual channels

{% multi_lang_include release_type.md release="General availability" %}

New [retry events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) are now available for email, LINE, push notifications, SMS, webhooks, and WhatsApp channels. These events provide visibility into when frequency capping results in a scheduled message being delayed rather than aborted. When a message is deprioritized or frequency capped, it can now be retried within a configured retry window, giving you better insight into message delivery patterns and frequency capping impacts. For more information, see the [Currents changelog]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Add new 'time_ms' field to TokenStateChange event

{% multi_lang_include release_type.md release="General availability" %}

A new `time_ms` field has been added to the [`users.behaviors.pushnotification.TokenStateChange`]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) event, providing millisecond-level granularity for tracking push token state changes. This enhanced precision helps you understand the latest status of a push token when multiple changes occur within the same second, giving you confidence in downstream systems that you have the correct subscription status. For more information, see the [Currents changelog]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Send Anonymous user to Tealium Destinations

{% multi_lang_include release_type.md release="General availability" %}

Events that do not have an external user ID defined can now be streamed to [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents?redirected=1) destinations. When you select the "Include events from anonymous users" checkbox on your Currents integration, events without an external user ID will be sent to the destination instead of being suppressed. This capability is critical for downstream analytics and use cases involving non-identified and anonymous users.

##### Send Anonymous user to CustomHTTP Destinations

{% multi_lang_include release_type.md release="Beta" %}

Events that do not have an external user ID defined can now be streamed to CustomHTTP destinations. When you select the "Include events from anonymous users" checkbox on your Currents integration, events without an external user ID will be sent to the destination instead of being suppressed. This capability is critical for downstream analytics and use cases involving non-identified and anonymous users.

#### Email Open event — "machine_open" field

The [Email Open event]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-open-events) now generates the "machine_open" field value to report on the [_Machine Open_]({{site.baseurl}}/user_guide/analytics/metrics_glossary) metric. 

### SDK

The following SDK updates have been released. Swift SDK v14.0.1 fixes an issue with the handling of universal links. Android SDK v40.2.0 fixes a potential memory leak and resolves an issue with multiple sessions being opened when transparent activities are present. Expo SDK v3.2.0 adds the `forwardUniversalLinks` option (default: false) to configure the native Swift SDK handling of universal links.

#### SDK breaking updates

The latest SDK updates have been released. Breaking updates are listed in the SDK updates section; all other updates can be found in the corresponding SDK changelogs.

{% multi_lang_include releases/sdk/2026_2_5_26_updates.md %}

{% enddetails %}

