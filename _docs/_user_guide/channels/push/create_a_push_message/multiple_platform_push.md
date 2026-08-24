---
nav_title: "Multiple platform push messages"
article_title: "Multiple platform messages"
alias: "/multiple_platform_push/"
description: "This article describes things to know when creating a push campaign or Canvas with multiple platforms selected."
page_order: 4
---

# Multiple platform push messages

> This article describes what to know when you create a push campaign or Canvas to target multiple platforms and devices from one composer.

When creating a push campaign or Canvas in Braze, you can select multiple platforms and devices to craft one message for all platforms in a single editing experience.

## Use cases

This editing experience is best for the following use cases:

- Mobile push campaigns and Canvas Message steps that need to be sent to multiple device types (such as both iOS and Android).
- Time-sensitive push notifications that need to target multiple platforms quickly and accurately, where content is the same across platforms (such as breaking news or live game updates).

## Creating a multiple platform push campaign or Canvas

To create a campaign targeting multiple platforms and devices:

1. Create a campaign or add a [Message step]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) to a Canvas.  
2. Select **Push notification**.
3. Select your desired platforms (Mobile, Web, Kindle) and mobile devices (iOS, Android). If you select multiple devices, multivariate testing will not be available for your campaign.

### Selecting platforms for a campaign
![Options to select multiple platforms for a push campaign, such as Mobile, Web, and Kindle, and multiple devices, such as iOS and Android.]({% image_buster /assets/img_archive/push_multiple_platform_message_selection.png %})

### Selecting platforms for a Canvas step
![Options to select multiple platforms for a push Message step, such as Mobile, Web, and Kindle, and multiple devices, such as iOS and Android.]({% image_buster /assets/img_archive/push_multiple_platform_message_selection_canvas.png %})

{:start="4"}
4. Select **Confirm**. After selecting **Confirm**, you are unable to change your selected platforms or devices.
5. Continue setting up your campaign or Canvas.

## Running a multi-platform, multivariate test

Multivariate testing is supported on multi-platform campaigns. Select the plus icon beside the variant name as you would for a single-platform campaign. For setup steps, see [Create multivariate and A/B tests]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests).

{% alert note %}
**Optimize with BrazeAI™** isn't available for push notification campaigns that use multiple platforms and multiple variants.
{% endalert %}

![Easy multi-platform, multivariate tests]({% image_buster /assets/img_archive/push_multiple_platform_message_composer_multivariate.png %})

## Things to know

### Unified messaging
On the **Compose** tab, you can specify one title, message, and on-click behavior for all of your chosen platforms and devices.

The preview pane shows an approximation of what your message looks like for each platform. While it can give you a good indicator of where you might reach character limits, remember to always test your messages on a real device before sending your campaign.

![Single editing view with one title, message, and on-click behavior field for three push types: iOS, Android, and Web.]({% image_buster /assets/img_archive/push_multiple_platform_message_composer.png %})

### Separate assets
In the **Assets** section, select or upload the images you want to appear for each platform. Keep in mind that different devices have different specifications for images and character counts. Refer to [Push message and image formats]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/message_and_image_formats) for help.

![Assets section of the single editing view with fields for Push Icon Image, iOS notification image, Android notification image, and Web notification image.]({% image_buster /assets/img_archive/push_multiple_platform_message_composer_assets.png %}){:style="max-width:50%"}

### Notification type

The notification type defaults to "Standard Push" and cannot be changed. If you want to create a different push, such as Push Stories or Inline Image (Android), create separate campaigns for each device type.

### Device-specific settings

You can edit platform-specific settings in the editor. This includes settings like [push action buttons]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_action_buttons), notification channels and groups, TTL, display priority, sounds, and more. 

For more information on device-specific settings, refer to the following article collections:

- [iOS options]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios)
- [Android options]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android)

### Push Stories

Push stories are available multi-platform on Android and iOS only, if you select Web or Kindle as a platform to send to then this option is unavailable.
