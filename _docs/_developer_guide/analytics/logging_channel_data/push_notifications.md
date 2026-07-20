---
nav_title: Push notifications
article_title: Log push notification data through the Braze SDK
page_order: 7.2
description: "Learn how to log push notification data through the Braze SDK."
noindex: true
---

# Log push notification data

> Learn how to log push notification data through the Braze SDK.

{% sdktabs %}
{% sdktab android %}
## Logging data with the Braze API (recommended)

You can log analytics in real-time by making calls to the [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). To log analytics, send the `braze_id` value from the Braze dashboard to identify which user profile to update.

![Personalized Push dashboard Example]({% image_buster /assets/img/push_implementation_guide/android_braze_id_configuration.png %}){: style="max-width:79%;"}

## Manually logging data

Depending on the details of your payload, you can log analytics manually within your `FirebaseMessagingService.onMessageReceived` implementation or your startup activity. Your `FirebaseMessagingService` subclass must finish execution within 9 seconds of invocation to avoid being [flagged or terminated](https://firebase.google.com/docs/cloud-messaging/android/receive) by the Android system.

{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/analytics/logging_push_data.md %}
{% endsdktab %}
{% endsdktabs %}
