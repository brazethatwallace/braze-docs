---
nav_title: Push notifications
article_title: "Push notifications for the Braze SDK"
page_order: 2.3
description: "This landing page is home to all things push notifications."
---

# Push notifications

> [Push notifications]({{site.baseurl}}/user_guide/channels/push) allow you to send out notifications from your app when important events occur. You might send a push notification when you have new instant messages to deliver, breaking news alerts to send, or the latest episode of your user's favorite TV show ready for them to download for offline viewing. They are also more efficient than background fetch, as your application only launches when necessary.

{% alert note %}
If **Redirect to web URL** with **Open web URL inside app** isn't selected, but the link still opens inside the app, the app may be handling the URL (for example, with universal links on iOS or App Links on Android). To open the link in the browser instead, confirm your app delegates the URL to the system browser when the user taps the notification, or adjust your app's URL handling so that the click action matches the Braze dashboard setting. See your platform's push documentation for how click actions and URL handling are configured.
{% endalert %}

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/push_notifications.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/push_notifications.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/push_notifications.md %}
{% endsdktab %}

{% sdktab android tv %}
## About push notifications for Android TV

![Android TV device illustration used for the Android TV push notifications guide.]({% image_buster /assets/img/Television.png %}){: style="float:right;max-width:25%;margin-left:15px; border: 0"}

While not a native feature, Android TV push integration is made possible by leveraging the Braze Android SDK and Firebase Cloud Messaging to register a push token for Android TV. However, you must build a UI to display the notification payload after it is received.

## Prerequisites

To use this feature, you'll need to complete the following:

- [Integrate the Braze Android SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)
- [Set up push notifications for the Braze Android SDK]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)

## Setting up push notifications

To set up push notifications for Android TV:

1. Create a custom view in your app to display your notifications.
2. Create a [custom notification factory]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_customization-display). This overrides the default SDK behavior and allows you to manually display the notifications. By returning `null`, this prevents the SDK from processing and requires custom code to display the notification. After these steps have been completed, you can start sending push to Android TV!<br><br>
3. (Optional) To track click analytics effectively, set up click analytics tracking. This can be achieved by creating a [push callback]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_push-callback) to listen for Braze push opened and received intents.

{% alert note %}
These notifications do not persist and are only visible to the user when the device displays them. This is due to Android TV's notification center not supporting historical notifications.
{% endalert %} 

## Testing Android TV push notifications

To test if your push implementation is successful, send a notification from the Braze dashboard as you would normally for an Android device.

- **If the application is closed**: The push message displays a toast notification on the screen.
- **If the application is open**: You have the opportunity to display the message in your own hosted UI. Follow the UI styling of the Android Mobile SDK in-app messages.

## Best practices

For marketers using Braze, launching a campaign to Android TV will be identical to launching a push to Android mobile apps. To target these devices exclusively, select the Android TV App in segmentation.

The delivered and clicked response returned by FCM will follow the same convention as a mobile Android device; therefore, any errors will be visible in the message activity log.

{% endsdktab %}

{% sdktab cordova %}
{% multi_lang_include developer_guide/cordova/push_notifications.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/push_notifications.md %}
{% endsdktab %}

{% sdktab huawei %}
{% multi_lang_include developer_guide/huawei/push_notifications.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/push_notifications.md %}
{% endsdktab %}

{% sdktab safari %}
{% multi_lang_include developer_guide/safari/push_notifications.md %}
{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/push_notifications.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin)%}
{% multi_lang_include developer_guide/xamarin/push_notifications.md %}
{% endsdktab %}
{% endsdktabs %}
