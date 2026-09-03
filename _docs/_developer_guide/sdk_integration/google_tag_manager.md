---
nav_title: Google tag manager
article_title: Google Tag Manager with the Braze SDK
platform: 
  - Android
  - FireOS
  - Swift
page_order: 1.1
description: "Learn how to initialize the Braze SDK using methods like runtime initialization, delayed initialization, or Google Tag Manager."

---

# Google Tag Manager with the Braze SDK

> Learn how to use [Google Tag Manager (GTM)](https://developers.google.com/tag-platform/tag-manager) with the Braze SDK, so you can remotely control Braze event tracking and user attribute updates without requiring code changes or new app releases.

{% sdktabs %}
{% sdktab web %}
## About Google Tag Manager for Web {#google-tag-manager}

Google Tag Manager (GTM) lets you remotely add, remove, and edit tags on your website without requiring a production code release or engineering resources. Braze offers the following templates for the Web SDK:

|Tag Type|Use Case|
|--------|--------|
| Initialization tag | This tag lets you [integrate the Web Braze SDK]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web) without needing to modify your site’s code.|
| Action tag | This tag lets you [create Content Cards]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager), [set user attributes]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web), and [manage data collection]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web).|
{: .reset-td-br-1 .reset-td-br-2 aria-label="About Google Tag Manager for Web #google-tag-manager" }

## Tag sequencing for Braze action tags {#tag-sequencing-for-braze-action-tags}

The Braze Initialization tag must fire before any tags that call Braze SDK methods (such as `braze.getUser()`, `braze.logCustomEvent()`, or `braze.logPurchase()`). If these methods fire before the SDK is initialized, you may encounter errors like `Uncaught TypeError: Cannot read properties of undefined (reading 'getUser')`.

To configure tag sequencing in Google Tag Manager:

1. Open the tag that calls Braze SDK methods (such as a Custom HTML tag or Braze action tag).
2. Go to **Advanced Settings** > **Tag Sequencing**.
3. Select **A tag that fires before [this tag] is fired**.
4. Choose your **Braze Initialization** tag.

This ensures the SDK is fully loaded before any other tags attempt to call Braze methods.

For more detail, see [Verify tag sequencing for custom events]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_tag-sequencing).

## Log purchases with GTM

In Braze action tags and Custom HTML tags, call `braze.logPurchase()` to record revenue. The legacy `appboy.logPurchase()` namespace is not supported in current Web SDK integrations.

## Logging custom events with GTM

You can log custom events using a **Custom HTML** tag in GTM. This approach uses the GTM [data layer](https://developers.google.com/tag-platform/tag-manager/datalayer) to pass event data from your site to a GTM tag that calls the Braze Web SDK.

### Step 1: Push the event to the data layer

In your site's code, push an event to the data layer wherever you want to trigger the custom event. For example, to log a custom event when a button is clicked:

```html
<button onclick="dataLayer.push({'event': 'my_custom_event'});">Track Event</button>
```

### Step 2: Create a trigger in GTM

1. In your GTM container, go to **Triggers** and create a new trigger.
2. Set the **Trigger Type** to **Custom Event**.
3. Set the **Event Name** to the same value you pushed to the data layer (for example, `my_custom_event`).
4. Choose when the trigger should fire (for example, **All Custom Events**).

### Step 3: Create a Custom HTML tag

1. In GTM, go to **Tags** and create a new tag.
2. Set the **Tag Type** to **Custom HTML**.
3. In the HTML field, add the following:

    ```html
    <script>
    window.braze.logCustomEvent("my_custom_event");
    </script>
    ```

4. Under **Triggering**, select the trigger you created in step 2.
5. Save and publish your container.

To include event properties, pass them as the second argument:

```html
<script>
window.braze.logCustomEvent("my_custom_event", {"property_key": "property_value"});
</script>
```

## Google's EU User Consent Policy

{% alert important %}
Google is updating its [EU User Consent Policy](https://www.google.com/about/company/user-consent-policy/) in response to changes to the [Digital Markets Act (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), which is in effect as of March 6, 2024. This new change requires advertisers to disclose certain information to their EEA and UK end users, as well as obtain necessary consents from them. Review the following documentation to learn more.
{% endalert %}

As part of Google's EU User Consent Policy, the following boolean custom attributes need to be logged to user profiles:

- `$google_ad_user_data`
- `$google_ad_personalization`

If setting these via the GTM integration, custom attributes require creating a custom HTML tag. The following is an example of how to log these values as boolean data types (not as strings):

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

For more information, refer to [Audience Sync to Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/).

{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/google_tag_manager.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/google_tag_manager.md %}
{% endsdktab %}
{% endsdktabs %}

## Troubleshooting

### Web SDK sessions attributed to the wrong user

If GTM fires Braze initialization or event tags before your app identifies the signed-in user, sessions and events may attach to the wrong profile. Initialize the Web SDK, call `changeUser()` with the signed-in user's `external_id`, and then call `openSession()` before any tags that log events or set attributes. Use GTM tag sequencing or consent triggers so Braze tags run only after your authentication flow completes.

### Web SDK console logging with Shopify or script-tag installs

The Shopify app embed loads the Web SDK with console logging turned off. Set logging in your GTM Initialization tag or `initialize()` options. The Braze dashboard does not include a logging control for these loaders.

If Braze logs appear in the browser console, remove `enableLogging: true` from the GTM Initialization tag or custom HTML before you publish to production. After initialization, use `toggleLogging()` or the `?brazeLogging=true` URL parameter. For the full Web SDK options, see [Verbose logging]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging).

If Braze does not initialize or events do not appear as expected, confirm your GTM container is published, triggers and tag firing order align with your SDK [lifecycle and initialization strategy]({{site.baseurl}}/developer_guide/sdk_integration), and that test devices are not blocking Braze endpoints.

For initialization failures, verify the Braze tag or custom tag provider receives the expected `actionType` and parameters (see the Android, Swift, and Web tabs on this page). For verbose logging while validating GTM-fired events, enable your platform’s SDK debug logging as described in the platform integration guides linked from those tabs.
