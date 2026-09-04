---
page_order: 10.9
nav_title: Troubleshooting
article_title: Troubleshoot push notifications for the Braze SDK
description: "Diagnose push notification delivery and display issues using a symptom index, standard investigation path, and platform-specific SDK checks."
channel:
  - push notifications
---

# Troubleshoot push notifications

> Use this page to diagnose push notification delivery and display issues on a device. For dashboard-side delivery checks (subscription status, segments, caps), see [Troubleshoot push]({{site.baseurl}}/user_guide/channels/push/troubleshooting).

Before you debug, add yourself as a [test user]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users) and review [Sending test messages]({{site.baseurl}}/developer_guide/push_notifications/sending_test_messages).

## Start here: Match your symptom

Find the behavior you're seeing in the table, then follow that section's steps. If you're not sure which section applies, use the [standard investigation path](#standard-investigation-path).

| Symptom | Go to |
| --- | --- |
| Push not received on one platform | Select your SDK tab in [Platform-specific troubleshooting](#platform-specific-troubleshooting) |
| Line breaks around Liquid tags look wrong when saving | [Line breaks in push notifications](#push-linebreaks) |
| Dashboard delivery checks (subscription, segment, caps) | [Troubleshoot push]({{site.baseurl}}/user_guide/channels/push/troubleshooting) |
| Deep link from push doesn't open correctly | [Deep linking troubleshooting]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting) |
| Common push error codes | [Common push error messages]({{site.baseurl}}/user_guide/channels/push/push_error_codes) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Push SDK symptom" }

## Standard investigation path

Use this workflow for every push notification incident. Start at step 1.

1. Confirm the device has a valid push token and push permission is granted in device settings.
2. In the dashboard, confirm the test user matches the campaign or Canvas [segment]({{site.baseurl}}/user_guide/channels/push/troubleshooting#segment) and is not in the [control group]({{site.baseurl}}/user_guide/channels/push/troubleshooting#control-group-status).
3. Send a [test push]({{site.baseurl}}/developer_guide/push_notifications/sending_test_messages) to the test device.
4. [Enable verbose logging]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduce the issue, and review platform-specific guidance in your [SDK tab](#platform-specific-troubleshooting).
5. If the issue persists, contact [Braze Support]({{site.baseurl}}/user_guide/administer/personal/braze_support) with verbose logs, platform, SDK version, and campaign or Canvas ID.

## Platform-specific troubleshooting

Select your SDK tab for platform-specific setup and display checks.

{% sdktabs %}
{% sdktab web %}
## Troubleshooting

If you're experiencing issues after setting up push notifications, consider the following:

- Web push notifications require that your site be HTTPS.
- Not all browsers can receive push messages. Ensure that `braze.isPushSupported()` returns `true` in the browser.
- Some browsers, such as Firefox, do not display images in push notifications. For details on browser support, refer to the [MDN documentation for Notification images](https://developer.mozilla.org/en-US/docs/Web/API/Notification/image).
- If a user has denied a site push access, they won't be prompted for permission again unless they remove the denied status from their browser preferences.

{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab swift %}
## Understanding the Braze/APNs workflow

The Apple Push Notification service (APNs) is the infrastructure for sending push notifications to applications running on Apple's platforms. Here is the simplified structure of how push notifications are enabled for your users' devices and how Braze can send push notifications to them:

{% multi_lang_include developer_guide/push_notifications/push_registration_flow_steps.md %}

### Step 1: Configuring the push certificate and provisioning profile

To develop your app, create an SSL certificate to enable push notifications. This certificate is included in the provisioning profile your app is built with and must also be uploaded to the Braze dashboard. The certificate allows Braze to tell APNs that it is authorized to send push notifications on your behalf.

There are two types of [provisioning profiles](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) and certificates: development and distribution. We recommend using only distribution profiles and certificates to avoid any confusion. If you choose to use different profiles and certificates for development and distribution, ensure that the certificate uploaded to the dashboard matches the provisioning profile you are currently using.

{% alert warning %}
Do not change the push certificate environment (development versus production). Changing the push certificate to the wrong environment can lead to your users having their push token accidentally removed, making them unreachable by push. 
{% endalert %}

### Step 2: Devices register for APNs and provide Braze with push tokens

When users open your app, they are prompted to accept push notifications. If they accept this prompt, APNs generates a push token for that particular device. The Swift SDK immediately and asynchronously sends the push token for apps using the default [automatic flush policy]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/advanced_use_cases/fine_network_traffic_control#automatic-request-processing). After we have a push token associated with a user, they show as "Push Registered" in the dashboard on their user profile under the **Engagement** tab and are eligible to receive push notifications from Braze campaigns.

{% alert note %}
Starting in macOS 13, on certain devices, you can test push notifications on an iOS 16 Simulator running on Xcode 14. For further details, refer to the [Xcode 14 Release Notes](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

#### Considerations for push token generation

- If users install your app on another device, Braze creates and captures another token the same way.
- If users reinstall your app, the SDK generates a new token and passes it to Braze. However, APNs and Braze may still log the original token as valid.
- If users uninstall your app, Braze does not immediately receive a notification, and the token still appears as valid until APNs retires it.
- At some point, APNs retires old tokens. Braze does not control or have visibility into this.

### Step 3: Launching a Braze push campaign

When a push campaign is launched, Braze makes requests to APNs to deliver your message. Specifically, the requests are passed to APNs for each current valid push token unless **Send to a user's most recent device** is selected. After Braze receives a successful response from APNs, Braze logs a successful delivery on the user profile, though the user may not have received the actual message for reasons including:
- Their device is powered off.
- Their device isn't connected to the internet (Wi-Fi or cellular).
- They recently uninstalled the app.

Braze uses the SSL push certificate uploaded in the dashboard to authenticate and verify that it is authorized to send push notifications to the push tokens provided. If a device is online, the notification should be received shortly after the campaign has been sent. Note that Braze sets the default APNs [expiration date](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) for notifications to 30 days.

### Step 4: Removing invalid tokens

If [APNs](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) informs us that any of the push tokens we were attempting to send a message to are invalid, we remove those tokens from the user profiles they were associated with.

{% alert note %}
It's normal for APNs to initially return a success status even if a token becomes unregistered, as APNs doesn't immediately report token invalidation events. APNs intentionally delays returning a `410` status for invalid tokens on a randomized schedule, designed to protect user privacy and prevent tracking of app uninstalls. You can safely continue sending notifications to an unregistered token until APNs returns a `410` status.
{% endalert %}

## Using the push error logs

The [Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) lets you see any messages (especially error messages) associated with your campaigns and sends, including push notification errors. This error log provides a variety of warnings which can be very helpful for identifying why your campaigns aren't working as expected. Selecting an error message redirects you to relevant documentation to help you troubleshoot a particular incident.

![Push error logs displaying the time the error occurred, the app name, the channel, error type, and error message.]({% image_buster /assets/img_archive/message_activity_log.png %})

Common errors you might see here include user-specific notifications, such as ["Received Unregistered Sending to Push Token"](#swift_received-unregistered-sending).

In addition, Braze also provides a push changelog on the user profile under the **Engagement** tab. This changelog provides insight into push registration behavior such as token invalidation, push registration errors, tokens being moved to new users, etc.

![Braze user profile Engagement tab showing the push registration changelog.]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

### Message Activity Log errors

#### Received unregistered sending to push token {#received-unregistered-sending}

- Make sure that the push token being sent to Braze from the method `AppDelegate.braze?.notifications.register(deviceToken:)` is valid. You can look in the **Message Activity Log** to see the push token. It should look something like `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, a long string containing a mix of letters and numbers. If your push token looks different, check your [code]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-32-register-push-tokens-with-braze) for sending Braze the push tokens.
- Ensure that your push provisioning profile matches the environment you're testing. Universal certificates may be configured in the Braze dashboard to send to either the development or production APNs environment. Using a development certificate for a production app or a production certificate for a development app does not work.
 - Check that the push token you have uploaded to Braze matches the provisioning profile you used to build the app you sent the push token from.

#### Device token not for topic

APNs returns `DeviceTokenNotForTopic` (HTTP status 400) when the push token doesn't match the topic (bundle ID) configured for your credentials. Braze may surface this in **Message Activity Log** or push delivery logs as `DeviceTokenNotForTopic`.

To resolve the mismatch:

1. Confirm the app's **bundle ID** matches the **App Bundle ID** in Braze (**Settings** > **App Settings** > **Push Notification Settings**).
2. Verify the provisioning profile used to build the app includes push capability for that bundle ID.
3. Confirm the push credential uploaded to Braze matches the app's environment (development versus production).
4. For `.p8` keys, verify **Team ID** and **Key ID** in Braze match your Apple Developer account.
5. Re-upload a valid `.p8` key or `.p12` certificate if credentials were rotated or revoked.

Prefer `.p8` authentication keys when possible. For credential types and dashboard status indicators, see [Migrate to a .p8 authentication key]({{site.baseurl}}/user_guide/channels/push/troubleshooting/#migrate-to-a-p8-authentication-key).

#### BadDeviceToken sending to push token

The `BadDeviceToken` is an APNs error code and does not originate from Braze. There could be a number of reasons for this response being returned, including the following:

{% multi_lang_include developer_guide/push_notifications/invalid_push_token_reasons.md %}

## Push registration issues

### No push registration prompt

If the application does not prompt you to register for push notifications, there is likely an issue with your push registration integration. Ensure you have followed our [documentation]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) and correctly integrated our push registration. You can also set breakpoints in your code to ensure the push registration code is running.

### No "push registered" users showing in the dashboard (prior to sending messages)

Ensure that your app is correctly configured to allow push notifications. Common failure points to check include:

- Check that your app is prompting you to allow push notifications. Typically, this prompt will appear upon your first open of the app, but it can be programmed to appear elsewhere. If it does not appear where it should be, the problem is likely with the basic configuration of your app's push capabilities.
  - Verify the steps for [push integration]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) were successfully completed.
  - Check that the provisioning profile your app was built with includes permissions for push. Make sure that you're pulling down all of the available provisioning profiles from your Apple developer account. To confirm this, perform the following steps:
    1. In Xcode, navigate to **Preferences > Accounts** (or use the keyboard shortcut <kbd>Command</kbd>+<kbd>,</kbd>).
    2. Select the Apple ID you use for your developer account and click **View Details**.
    3. On the next page, click **<i class="fas fa-redo-alt"></i> Refresh** and confirm that you're pulling all available provisioning profiles.
- Check you have [properly enabled push capability]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-2-enable-push-capabilities) in your app.
- Check your push provisioning profile matches the environment you're testing in. Universal certificates may be configured in the Braze dashboard to send to either the development or production APNs environment. Using a development certificate for a production app or a production certificate for a development app does not work.
- Check that you are calling our `registerPushToken` method by setting a breakpoint in your code.
- Make sure you're testing using a device (push will not work on a simulator) and have good network connectivity.

## Push notifications sent but not displayed on users’ devices

### "Push registered" users no longer enabled after sending messages

This likely indicates that the user had an invalid push token. This can happen for several reasons:

#### Dashboard and app certificate mismatch

If the push certificate you uploaded in the dashboard is not the same one in the provisioning profile that your app was built with, APNs will reject the token. Verify that you have uploaded the correct certificate and completed another session in the app before attempting another test notification.

#### Application was uninstalled

If a user has uninstalled your application, their push token will be invalid and removed upon the next send.

#### Regenerating your provisioning profile

As a last resort, starting over fresh and creating a whole new provisioning profile can clear up configuration errors that come from working with multiple environments, profiles, and apps at the same time. There are many "moving parts" in setting up push notifications, so sometimes, it is best to retry from the beginning. This will also help isolate the problem if you need to continue troubleshooting.

### Messages not delivered to "push registered" users

#### App is foregrounded

On iOS versions that do not integrate push via the `UserNotifications` framework, if the app is in the foreground when the push message is received, it will not be displayed. You should background the app on your test devices before sending test messages.

#### Test notification scheduled incorrectly

Check the schedule you set for your test message. If it is set to local time zone delivery or [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/), you may have just not received the message yet (or had the app in the foreground when it was received).

### User not "push registered" for the app being tested

Check the user profile of the user you are trying to send a test message to. Under the **Engagement** tab, there should be a list of "pushable apps." Verify the app you are trying to send test messages to is in this list. Users will show up as "Push Registered" if they have a push token for any app in your workspace, so this could be something of a false positive.

The following would indicate a problem with push registration or that the user's token had been returned to Braze as invalid by APNs after being pushed:

![A user profile displaying the contact settings of a user. Under Push, "No Apps" are displayed.]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## Push clicks not logged {#push-clicks-not-logged}

- Make sure you have followed the [push integration steps]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling).
- Braze does not handle push notifications received silently in the foreground (default foreground push behavior prior to the `UserNotifications` framework). This means that links will not be opened,  and push clicks will not be logged. If your application has not yet integrated the `UserNotifications` framework, Braze will not handle push notifications when the application state is `UIApplicationStateActive`. Ensure that your app does not delay calls to [push handling methods]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling); otherwise, the Swift SDK may treat push notifications as silent foreground push events and not handle them.

## Deep links not working

For comprehensive troubleshooting across all channels—including universal links, custom schemes, email, and third-party providers like Branch—see [Deep linking troubleshooting]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).

### Web links from push clicks not opening

Links in push notifications need to be ATS compliant to be opened in web views. Ensure that your web links use HTTPS. For more information, refer to [ATS compliance]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/advanced_use_cases/linking#app-transport-security-ats).

### Deep links from push clicks not opening

Most of the code that handles deep links also handles push opens. First, ensure that push opens are being logged. If not, fix that issue (as the fix often fixes link handling).

If opens are being logged, check whether it is an issue with the deep link in general or with the deep linking push click handling. To do this, test to see if a deep link from an in-app message click works.

### Push Story image taps do nothing

If tapping a Push Story image does nothing, open the Notification Content Extension `Info.plist` and confirm `UNNotificationExtensionUserInteractionEnabled` is `YES`. The Swift SDK `BrazePushStory` module needs that key so the extension can receive taps. See [Push stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories/?sdktab=swift).

{% endsdktab %}

{% sdktab fireos %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
## Troubleshooting

### Push doesn't appear after app is closed from task switcher

If you observe that push notifications no longer appear after the app is closed from the task switcher, your app is likely in Debug mode. .NET MAUI adds scaffolding in Debug mode that prevents apps from receiving push after their process is killed. If you run your app in Release Mode, you should see push even after the app is closed from the task switcher.

### Custom notification factory not being set correctly

Custom notification factories (and all delegates) must extend [`Java.Lang.Object`](https://developer.xamarin.com/api/type/Android.Runtime.IJavaObject/) to work properly across the C# and Java divide. See [Xamarin](https://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/working_with_jni/#Implementing_Interfaces) on implementing Java interfaces for more information.

{% endsdktab %}
{% endsdktabs %}

## Line breaks in push notifications {#push-linebreaks}

When composing push notifications with Liquid tags, line breaks adjacent to Liquid tags are automatically removed before the message is sent. In the [push notification composer]({{site.baseurl}}/user_guide/channels/push/create_a_push_message), these line breaks are re-added so your message remains readable while editing. If you notice line breaks around Liquid tags when saving your message, this is expected behavior.

