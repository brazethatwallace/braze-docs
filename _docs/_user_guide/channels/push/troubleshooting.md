---
nav_title: Troubleshooting
article_title: Troubleshoot push
page_order: 5
page_type: reference
description: "Diagnose push delivery, click behavior, and credential issues using a symptom index and standard investigation path."
channel: push
---

# Troubleshoot push

> Use this page to troubleshoot push delivery, click behavior, and credential issues. For SDK-specific setup, see [Troubleshoot push notifications for the Braze SDK]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting). For error codes, see [Common push error messages]({{site.baseurl}}/user_guide/channels/push/push_error_codes).

## Start here: Match your symptom

| Symptom | Go to |
| --- | --- |
| User didn't receive a push notification | [Missing push notifications](#missing-push-notifications) |
| Push notifications arrive late | [Delayed push notifications](#delayed-push-notifications) |
| Push sends slower than expected | [Push notifications are sending slower than expected](#push-notifications-are-sending-slower-than-expected) |
| `MismatchSenderID` error (Android) | [Error: MismatchSenderID](#error-mismatch-sender-id) |
| Tapping a push doesn't open the app | [Clicking a push notification doesn't open the app](#clicking-a-push-notification-does-not-open-the-app) |
| Push links open in the app instead of the browser | [Push clicks unexpectedly open in app](#push-clicks-unexpectedly-open-in-app) |
| Web push permissions or delivery issues | [Web push notifications aren't behaving as expected](#web-push-notifications-are-not-behaving-as-expected) |
| Need to migrate from `.p12` to `.p8` (iOS) | [Migrate to a .p8 authentication key](#migrate-to-a-p8-authentication-key) |
| Specific push error code in logs | [Push error messages](#push-error-messages) |
| Uninstall counts don't match by platform | [Uninstall metrics](#uninstall-metrics) |
| Migrating users or push data to another app group | [App Group data migration](#app-group-data-migration) |
| Need to know if a session started from a push open | [Session and attribution](#session-and-attribution) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push symptom" }

## Standard investigation path

Use this workflow when a user or test device didn't receive a push. Start at step 1.

1. Confirm the user is push subscribed or opted in and has a valid push token in the **Engagement** tab of their profile.
2. Confirm the user is in the campaign or Canvas target audience at send time (segments update in real time).
3. Check global frequency caps, rate limits, and control group assignment for the campaign or Canvas.
4. Confirm you're using the correct push type for the device (for example, Android, iOS, or Kindle).
5. For internal testing, confirm the tester is logged into the correct app on the device.
6. If delivery still fails, review [Common push error messages]({{site.baseurl}}/user_guide/channels/push/push_error_codes) or contact [Braze Support]({{site.baseurl}}/braze_support) with the campaign or Canvas ID, user ID, and timestamp with timezone.

## Missing push notifications {#missing-push-notifications}

**Symptom:** A user didn't receive an expected push notification.

If push notifications are not arriving as expected, work through the following checks:

- [Push subscription status](#push-subscription-status)
- [Segment](#segment)
- [Push notification caps](#push-notification-caps)
- [Rate limits](#rate-limits)
- [Control group status](#control-group-status)
- [Valid push token](#valid-push-token)
- [Push notification type](#push-notification-type)
- [Current app](#current-app)

### Push subscription status

Pushes can be sent only to subscribed or opted-in users. In the **User Profile**, open the [Engagement]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/#engagement-tab) tab and confirm that you are actively registered for push in the workspace you are testing. If you are registered for multiple apps, they are listed in **Push Registered For**:

![Push Registered For]({% image_buster /assets/img_archive/trouble1.png %})

You can also export user profiles with Braze export endpoints:

- [Users by identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [Users by segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

Either endpoint returns a push token object that includes push enablement information per device.

### Segment

Confirm that you are in the segment you are targeting (if this is a live campaign and not a test). In the **User Profile**, you can see which segments the user currently matches. Segment membership updates in real time.

![List of Segments]({% image_buster /assets/img_archive/trouble2.png %})

You can also confirm that the user is part of the segment by using **User Lookup** when creating a segment. **User Lookup** accepts only `external_id` or `braze_id`—not email addresses or phone numbers. To search by email, phone, push token, or user alias, see [**Search Users**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles).

![User Lookup section with a search field.]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

### Push notification caps

Check the global frequency caps. It's possible you did not receive the push notification because your workspace has global frequency capping in place and you've already hit your push notification cap for the specified time frame.

On the campaign **Analytics** page, check for a frequency capping banner showing approximately how many users didn't receive the campaign in the last 30 days. To investigate individual sends, use the [Messaging Diagnostics dashboard]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard) and filter by **Frequency capped**. To review or change rules, see [global frequency capping]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#freq-cap-feat-over).

![Campaign Details]({% image_buster /assets/img_archive/trouble3.png %})

### Rate limits

If you have a rate limit set for your campaign or Canvas, you might stop receiving messages after you exceed that limit. For more information, see [Rate limiting]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-rate-limiting).

### Control group status

If this is a single-channel campaign or a Canvas with a control group, you might be in the control group.

  1. Check the [variant distribution]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#step-4-choose-a-segment-and-distribute-your-users-across-variants) to see if there is a control group.
  2. If so, create a segment that filters for [in campaign control group]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/retargeting_campaigns#in-campaign-control-group), then [export the segment]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/segment_data_to_csv#segment-csv-export-details) and check whether your user ID is on the list.

### Valid push token

A push token is an identifier that senders use to target a specific device with a push notification. Without a valid push token, Braze cannot send a push to that device.

Braze stores up to 20 devices per user profile. When a 21st device registers, the oldest device is removed (first in, first out, or FIFO). Calling [`changeUser()`]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/) in the SDK re-registers the current device on the profile.

### Push notification type

Use the push type that matches the device or platform you are targeting. For example, use a Kindle push notification for Fire TV, not an Android push campaign. For Android devices, use an Android push notification rather than an iOS push campaign.

For platform-specific troubleshooting workflows, see:

- [Apple push notification troubleshooting]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [Firebase Cloud Messaging troubleshooting]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

### Current app

When you test push with internal users, confirm that the intended recipient is signed in to the correct app. Otherwise, they might not receive the push, or they might receive one you did not expect based on segmentation.

{% alert note %}
If you're sending push messages with images on Android, FCM can sometimes discard the image and only display the text in the push message. This issue is usually caused by server connectivity issues.
{% endalert %}

## Error: MismatchSenderID {#error-mismatch-sender-id}

**Symptom:** Android push fails with a `MismatchSenderID` error.

MismatchSenderID indicates an authentication failure with Firebase Cloud Messaging (FCM). Confirm your Firebase sender ID and FCM API key are correct.

To find the proper Firebase Server Key and replace it:

1. Go to the Firebase console for your app.
2. Under **Project Overview**, select **Project Settings**.
3. In the **Cloud Messaging** tab, check that the Sender ID listed with the API keys matches the one in Braze (in **Settings** > **App Settings** > **Cloud Messaging API Key**).

{% alert warning %}
Do not change your Sender ID in your Braze dashboard. Doing so causes existing push registrations to be invalidated. If the Sender ID does not match, you must find your Firebase project with the matching Sender ID.
{% endalert %}

4. Copy the **Server Key** under **Project credentials**.
5. In Braze, go to **Settings** > **App Settings**, select your app, and paste the server key into the **Cloud Messaging API Key** field (replacing the outdated key).
6. Select **Save**.
7. To verify, send a test push to a device before and after changing the API key without opening the application. This helps confirm that users continue to receive push notifications without requiring a new push registration ID (push token) to be generated.

## Troubleshooting scenarios

### Delayed push notifications {#delayed-push-notifications}

**Symptom:** Push notifications arrive later than expected.

Your push notifications can be delayed for these reasons:

- A weak data connection on the device
- Custom code in the app that can suppress Braze push notifications
- User preferences for push notifications in the device's settings
- Message priority of the push when created in the campaign or Canvas
- Traffic delays or issues with the push service providers (FCM and APNs)

### Push notifications are sending slower than expected {#push-notifications-are-sending-slower-than-expected}

**Symptom:** Campaign or Canvas push sends take longer than expected to complete.

Confirm that your push notification setup follows these best practices:

- If you're sending to large audiences without considering push-enabled status, this may lead to a slower sending speed. Instead, consider sending to push-enabled users only to reduce the size of your audience.
- If possible, try to schedule your campaigns ahead of time rather than immediately.
- If you're targeting a larger number of users with push notifications in a Canvas, you can anticipate that subsequent message steps in the Canvas will require different processing times than a campaign that sends to users immediately. In this case, campaigns would typically finish sending before a Canvas, as the first "step" of a Canvas is to check whether users qualify for the specific user journey.

## Clicking a push notification doesn't open the app {#clicking-a-push-notification-does-not-open-the-app}

**Symptom:** Tapping a push notification doesn't open the app or navigate as configured.

If clicking a push notification doesn't open your app, check the following based on your platform.

### Android

1. **Verify on-click behavior:** Confirm that the campaign is configured to open the app when clicked.
2. **Check deep link handling:** In your `braze.xml` file, check whether `com_braze_handle_push_deep_links_automatically` is set to `true` or `false`.
   - If set to `true`, the Braze SDK handles deep links directly and the app should open as expected.
   - If set to `false`, your app needs a broadcast receiver to listen for and handle push received and opened intents. Verify that this receiver is implemented correctly.
3. **Collect verbose logs:** [Enable verbose logging]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduce the issue, and provide the logs along with your `braze.xml` and `AndroidManifest.xml` to Braze Support.

### iOS

1. **Verify on-click behavior:** Confirm that the campaign is configured to open the app when clicked.
2. **Check push integration:** Deep linking from a push into the app is automatically handled by the Braze [standard push integration]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift). Confirm that the integration is implemented correctly, including any custom delegate handling.
3. **Collect verbose logs:** [Enable verbose logging]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduce the issue, and provide the logs to Braze Support.

## Push clicks unexpectedly open in app {#push-clicks-unexpectedly-open-in-app}

**Symptom:** Links in push notifications open inside the app instead of the device's web browser.

If you're experiencing issues with links in push notifications unexpectedly opening in your app instead of your web browser, there may be an issue with your campaign configuration or SDK implementation. Use the following steps for help.

### Verify on-click behavior

In your campaign or Canvas step, double-check that **Open web URL inside mobile app** is not selected. If it is, clear the selection and relaunch.

The default interaction for the on-click behavior "Open web URL" differs by SDK version. For SDK versions iOS 2.29.0 and Android 2.0.0 and higher, this option is selected by default and web URLs open in a web view within the app. Prior to these versions, this option is cleared by default and web URLs open in the device's default web browser.

If this is not the issue, there may be a problem with your push implementation.

### Double-check push integration

If links in your push notifications are opening in the app unexpectedly, it might be due to issues with your push notification integration or customization settings. Follow these steps to troubleshoot:

1. **Review the push delegate implementation:** Ensure that the Braze push delegate is implemented correctly. For detailed instructions, see the integration guide for push notifications for your [platform]({{site.baseurl}}/developer_guide/home/).
2. **Inspect custom link handling:** Check if the app includes custom handling for all `https://` links. Custom configurations might override default behaviors. Collaborate with your development team to review and adjust these settings if necessary.
3. **Verify iOS push registration:** For iOS, revisit step 1 of the push integration guide on [registering push notifications with APNs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-1-register-for-push-notifications-with-apns). Ensure your delegate object is assigned synchronously before the app finishes launching. This step should be completed in the `application:didFinishLaunchingWithOptions:` method.
4. **Test your integration:** After making adjustments, test the push notification behavior on both iOS and Android devices to confirm the issue is resolved.

### Deep links with app still running in the background (iOS)

If deep links work when the app is not running or when the link is used directly, but not when the application is already running in the background, the issue may be related to how the app handles the link. Check whether you're using any third-party libraries that use method swizzling. We recommend turning swizzling off, as it can cause issues with deep link implementations.

## Migrate to a .p8 authentication key {#migrate-to-a-p8-authentication-key}

**Symptom:** You need to migrate iOS push credentials from a legacy certificate to a `.p8` key, or push delivery failed after a credential change.

Apple `.p8` authentication keys are the required approach for APNs push in Braze. Unlike legacy certificate file types, `.p8` keys don't expire and support all of your apps under a single key, eliminating the need for annual certificate renewals and reducing the risk of push delivery failures.

If you're currently using a `.p12` or `.pem` certificate, migrate to a `.p8` key as soon as possible. For instructions on creating and uploading a `.p8` key, see [Upload your APNs push certificate]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift). For Apple's guidance on generating a `.p8` key from your developer account, see [Communicate with APNs using authentication tokens](https://developer.apple.com/help/account/capabilities/communicate-with-apns-using-authentication-tokens/).

### .p8 keys versus .p12 certificates

Use the following table to compare credential types, expiration, and how each appears in the dashboard.

| Credential | Expiration | Dashboard status indicator |
| --- | --- | --- |
| `.p8` authentication key | Does not expire | No green status indicator (this is expected) |
| `.p12` push certificate | Expires yearly | Green indicator when the certificate is valid |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label=".p8 keys versus .p12 certificates" }

When you replace a `.p12` certificate with a `.p8` key (or upload a new credential), push delivery can pause briefly while Braze processes the change. Plan updates during a maintenance window when possible.

In **Settings** > **App Settings** > **Push Notification Settings**, confirm that **App Bundle ID**, **Team ID**, and **Key ID** (for `.p8` keys) match the values in your Apple Developer account. Multiple Braze workspaces can use the same Apple push credential when the iOS app **bundle ID** is identical; the credential environment (development versus production) must match how the app was built.

Apps on [Braze Swift SDK 10.0.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/10.0.0) or later can use [Dynamic APNs gateway management]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift#dynamic-apns-gateway-management), which routes tokens to the correct APNs environment automatically.

## Web push notifications aren't behaving as expected {#web-push-notifications-are-not-behaving-as-expected}

**Symptom:** Browser push notifications don't display, or site permissions appear stuck.

If you're experiencing issues with push notifications in your browser, you may need to reset your site's notification permissions and clear your site's storage. Use the following steps for help.

{% tabs %}
{% tab Chrome %}

### Reset Chrome on desktop

1. Next to your URL in the Chrome browser, select the **View Site Information** slider icon.
2. Under **Notifications**, select **Reset permission**.
3. Open Chrome DevTools. The following are the relevant shortcuts per operating system.

<style> 
table {
    max-width: 50%;
}
</style>

| OS      | Keyboard shortcuts                                                  |
| ------- | ------------------------------------------------------------------- |
| Mac      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Windows | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Reset Chrome on desktop" }

{:start="4"}
4. In DevTools, navigate to the **Application** tab.
5. In the sidebar, select **Storage**.
6. Select **Clear site data**.
7. Chrome will prompt you to reload the page to apply your updated settings. Select **Reload**.

Your push permissions are now reset. Open a new tab to your site and try it out.

### Reset Chrome on Android

If you have a notification from your site visible in your Android notification drawer:

1. From the push notification, select <i class="fas fa-cog" title="Settings"></i> **Settings** and select **Site settings**.
2. From **Site settings**, tap **Clear & Reset**.

If you don't have a notification from your site open:

1. Open Chrome on Android.
2. Tap the <i class="fas fa-ellipsis-vertical"></i> menu.
3. Go to **Settings** > **Site Settings** > **Notifications**.
4. Verify notifications are set to **Ask before sending (recommended)**.
5. Find your site on the list.
6. Select the entry and tap **Clear and Reset**.

Your push permissions are now reset. Open a new tab to your site and try it out.

{% endtab %}
{% tab Firefox %}

### Reset Firefox on desktop

1. Next to your site URL, select <i class="fa-solid fa-circle-info" alt="info icon"></i> or <i class="fas fa-lock" alt="lock icon"></i>.
2. Under **Permissions**, next to **Receive Notifications**, select <i class="fa-solid fa-circle-xmark" title="Clear this permission and ask again"></i> **Clear permission** to clear notification permissions.
3. On the same menu, select **Clear Cookies and Site Data**.
4. In the dialog to confirm your choice, select **OK**.

Your push permissions are now reset. Open a new tab to your site and try it out.

### Reset Firefox on Android

To reset push permissions on Android, see [Clear your browsing history and other personal data](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser) in Mozilla Support.

{% endtab %}
{% tab Safari %}

### Reset Safari on macOS

{% alert note %}
These steps are for macOS only, as Apple doesn't support Web Push for Safari on Windows.
{% endalert %}

1. Open Safari.
2. From the [menu bar on Mac](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac), go to **Safari** > **Settings** > **Websites** > **Notifications**.
3. Select your site from the list.
4. Select **Remove** to delete notification permissions for the site.
5. Then, go to **Privacy** > **Manage Website Data**.
6. Select your site from the list.
7. Select **Remove**, or to remove all site data, select **Remove All**.
8. Select **Done**.

Your push permissions are now reset. Open a new tab to your site and try it out.

{% endtab %}
{% endtabs %}

## Push open metrics

Braze logs a Direct Open when a user taps the notification and your app starts a session. Expanding a rich push notification without opening the app does not log a Direct Open.

If a user opens your app after receiving a push without tapping the notification, Braze may log an Influenced Open instead. For definitions and reporting, see [Influenced opens]({{site.baseurl}}/user_guide/analytics/tracking/influenced_opens/).

## Push error messages {#push-error-messages}

**Symptom:** You see a specific push error code (for example, `DEVICE_UNREGISTERED`, `Unregistered`, or `NotRegistered`).

For definitions of common push error codes (including `DEVICE_UNREGISTERED`, `NotRegistered`, and `Unregistered`), see [Common push error messages]({{site.baseurl}}/user_guide/channels/push/push_error_codes/).

When FCM returns errors such as `DEVICE_UNREGISTERED`, `NotRegistered`, `BAD_REGISTRATION`, or `SENDER_ID_MISMATCH`, Braze typically removes the affected push token from the user profile. That removal often indicates the app was uninstalled or the token is no longer valid. Uninstall tracking campaigns use the same token-removal logic at scale.

For Android uninstall tracking, Braze may send uninstall detection pushes as a dry run (validation only) or as a live silent push, depending on your workspace configuration. Dry-run sends are less reliable for uninstall detection because FCM does not return the same bounce signals as a live send. If uninstall counts look low, confirm your Android integration meets [uninstall tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking) prerequisites and review bounce errors in the Message Activity Log.

## Uninstall metrics {#uninstall-metrics}

### Why don't total uninstalls match Android plus iOS?

Workspace **Total Uninstalls** can exceed the sum of platform-specific uninstall metrics because web push token invalidation also contributes to uninstall counts. When a web push token becomes invalid (for example, after the user clears site data or revokes permission), Braze may record an uninstall for that web registration even when mobile uninstall metrics are unchanged.

### What subscription status do imported iOS push tokens show?

Imported iOS push tokens usually appear as **Subscribed** until the user logs a session in an app that uses the Braze SDK for that workspace. After the SDK registers the token on session start, the profile typically moves to **Opted-In** when push authorization is granted. For subscription states and profile fields, see [Push subscription states]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states).

## App Group data migration {#app-group-data-migration}

### Can I migrate data between app groups or Braze workspaces?

Braze does not offer a one-click migration between app groups. You can move new data into a destination app group by updating your app or site to use that app group's API key, then sending user updates through the [Users Track]({{site.baseurl}}/api/endpoints/user_data/post_user_track) endpoint or importing profiles with [User Export]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_user_data) and related import tools.

You can often migrate user profile fields, custom attributes, events, and push tokens when you plan the export and import carefully. The following generally **cannot** be migrated between app groups: dashboard users and permissions, campaigns, Canvases, segments (as saved objects), and app group settings. Work with your Braze account team when planning a large workspace move.

## Session and attribution {#session-and-attribution}

### Can I tell from session start whether the user opened the app from a push?

No. Session start events do not include a flag that indicates whether the session began from a push open. Use push **Direct Opens**, **Influenced Opens**, or custom events (for example, logging a click handler in your app) to correlate sessions with push engagement. See [Push open metrics](#push-open-metrics).
