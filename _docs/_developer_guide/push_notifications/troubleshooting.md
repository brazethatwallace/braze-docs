---
page_order: 10.9
nav_title: Troubleshooting
article_title: Troubleshoot push notifications for the Braze SDK
channel:
  - push notifications
---

# Troubleshoot push notifications

> Learn how to troubleshoot push notifications for the Braze SDK.

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
{% multi_lang_include developer_guide/swift/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab fireos %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
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

When composing push notifications with Liquid tags, line breaks adjacent to Liquid tags are automatically removed before the message is sent. In the [push notification composer]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message), these line breaks are re-added so your message remains readable while editing. If you notice line breaks around Liquid tags when saving your message, this is expected behavior.

