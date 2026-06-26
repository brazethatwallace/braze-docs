---
nav_title: Log analytics
article_title: Log Analytics 
page_order: 1
description: "This article covers how to manually log impressions, clicks, dismissals, and handle on-click behavior for your customized Content Cards."
toc_headers: "h2"

---

# Log analytics

{% multi_lang_include developer_guide/_shared/logging_analytics/content_cards.md %}

## Unique dismissals higher than unique impressions

If *Unique Dismissals* exceeds *Unique Impressions*, your custom Content Card integration logged dismissals without logging impressions for those same cards. Braze's default Content Card UI logs both automatically, so this mismatch appears only when you use a custom UI.

Log an impression each time you display a card, and log a dismissal when the user dismisses it. For method names and examples, see the platform sections below.

## Missing Content Cards analytics

If Content Cards appear correctly in your app but you consistently do not receive any analytics (impressions, clicks, and so on), it is likely an SDK integration issue.

- **Custom Content Card views (Android, iOS, Web):** The default Braze UI logs impressions and clicks automatically on all platforms. If you are using a custom Content Card view or implementation, you must call the appropriate logging methods explicitly within your application. See [Log analytics]({{site.baseurl}}/developer_guide/content_cards/logging_analytics) for your platform. For custom Web implementations specifically, ensure the Braze Web SDK is loaded, check the browser console for errors, and verify that card data is being received.
- **SDK initialization and user identification:** Ensure the SDK is fully initialized before displaying cards. Events are silently dropped (not queued) if the SDK is uninitialized, in delayed initialization mode, or GDPR-disabled. The SDK does log analytics for anonymous users, but dashboard metrics like "unique daily impressions" require a resolved user identity, so call `changeUser` before cards are displayed where possible.

## Content Card ID

Each campaign send to a recipient generates a new Content Card ID. If the same user receives the campaign again on a later send, Braze assigns a new ID. Reference the card `id` when logging impressions, clicks, and dismissals in custom implementations.
