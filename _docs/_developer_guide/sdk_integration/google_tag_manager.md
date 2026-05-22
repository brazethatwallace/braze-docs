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
{% multi_lang_include developer_guide/web/google_tag_manager.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/google_tag_manager.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/google_tag_manager.md %}
{% endsdktab %}
{% endsdktabs %}

## Troubleshooting

If Braze does not initialize or events do not appear as expected, confirm your GTM container is published, triggers and tag firing order align with your SDK [lifecycle and initialization strategy]({{site.baseurl}}/developer_guide/sdk_integration/), and that test devices are not blocking Braze endpoints.

For initialization failures, verify the Braze tag or custom tag provider receives the expected `actionType` and parameters (see the Android, Swift, and Web tabs on this page). For verbose logging while validating GTM-fired events, enable your platform’s SDK debug logging as described in the platform integration guides linked from those tabs.
