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

If dashboard analytics show *Unique Dismissals* higher than *Unique Impressions* for Content Cards, review your logging integration:

- Confirm whether you use Braze's default Content Card UI or a fully custom UI. Custom UI requires you to log impressions and dismissals explicitly.
- Verify you call the correct logging methods when a card is shown and when a user dismisses it.
- Dismissals logged without matching impressions usually indicate a bug in custom logging code, not expected Braze behavior.

For method details, see the platform sections below.

## Missing Content Cards analytics

If Content Cards appear correctly in your app but you consistently do not receive any analytics (unique recipients, impressions, clicks, and so on), it is likely an SDK integration issue.

- **Custom Content Card views (Android, iOS, Web):** The default Braze UI logs impressions and clicks automatically on all platforms. If you are using a custom Content Card view or implementation, you must call the appropriate logging methods explicitly within your application. See [Log analytics]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) for your platform. For custom Web implementations specifically, ensure the Braze Web SDK is loaded, check the browser console for errors, and verify that card data is being received.
- **SDK initialization and user identification:** Ensure the SDK is fully initialized before displaying cards. Events are silently dropped (not queued) if the SDK is uninitialized, in delayed initialization mode, or GDPR-disabled. The SDK does log analytics for anonymous users, but dashboard metrics like "unique recipients" require a resolved user identity, so call `changeUser` before cards are displayed where possible.
