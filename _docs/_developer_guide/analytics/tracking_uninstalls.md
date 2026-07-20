---
nav_title: Track uninstalls
article_title: Track uninstalls through the Braze SDK
page_order: 3.5
description: "Learn how to track uninstalls through the Braze SDK."

---

# Track uninstalls

> Learn how to set up uninstall tracking through the Braze SDK. For general information, see [User Guide: Uninstall tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking).

{% sdktabs %}
{% sdktab android %}
## Setting up uninstall tracking

### Step 1: Set up FCM

The Android Braze SDK uses Firebase Cloud Messaging (FCM) to send silent push notifications, which are used to collect uninstall tracking analytics. If you haven't already, [set up]({{site.baseurl}}/developer_guide/platforms/android/push_notifications/#setting-up-push-notifications) or [migrate to]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android) the Firebase Cloud Messaging API for push notifications.

### Step 2: Manually detect uninstall tracking (optional)

By default, the Android Braze SDK will automatically detect and ignore silent push notifications related to uninstall tracking. However, you choose to manually detect uninstall tracking using the [`isUninstallTrackingPush()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/is-uninstall-tracking-push.html) method.

{% alert important %}
Because silent notifications for uninstall tracking are not forwarded to any Braze push callbacks, you can only use this method before you pass a push notification to Braze.
{% endalert %}

### Step 3: Remove automatic server pings

A silent push notification will wake your app and instantiate the `Application` component if it app isn't already running. So, if you have a custom [`Application`](https://developer.android.com/reference/android/app/Application) subclass, remove any logic that automatically pings your servers during your [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application#onCreate()) lifecycle method.

### Step 4: Enable uninstall tracking

Finally, enable uninstall tracking in Braze. For a full walkthrough, see [Enable uninstall tracking]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking).

{% alert important %}
Tracking uninstalls can be imprecise. The metrics you see on Braze may be delayed or inaccurate.
{% endalert %}

{% endsdktab %}

{% sdktab swift %}
## Setting up uninstall tracking

### Step 1: Enable background push

In your Xcode project, go to **Capabilities** and ensure you have **Background Modes** enabled. For more information, see [silent push notification]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift).

### Step 2: Ignore internal push notifications

The Swift Braze SDK uses background push notifications to collect uninstall tracking analytics. To ensure your app doesn't make unwanted actions when these are sent, you'll need to ensure that [internal push notifications are ignored]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications).

### Step 3: Send a test push (optional)

Next, send yourself a test push notification from the Braze dashboard (don't worry&#8212;it won't update your user profile).

1. Go to **Messaging** > **Campaigns** and create a push notification campaign using the relevant platform.
2. Go to **Settings** > **App Settings** and add the `appboy_uninstall_tracking` key with relevant `true` value, then check **Add Content-Available Flag**.
3. Use the **Preview** page to send yourself a test uninstall tracking push.
4. Check that your app does not make any unwanted automatic actions when it receives a push notification.

{% alert note %}
A badge number will be sent along with the test push notification&#8212;however a real uninstall tracking push won't send any badge numbers.
{% endalert %}

### Step 3: Enable uninstall tracking

Finally, enable uninstall tracking in Braze. For a full walkthrough, see [Enable uninstall tracking]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking).

{% alert important %}
Tracking uninstalls can be imprecise. The metrics you see on Braze may be delayed or inaccurate.
{% endalert %}

{% endsdktab %}
{% endsdktabs %}
