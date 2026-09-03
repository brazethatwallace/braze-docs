---
nav_title: Prep guide
article_title: In-App Message Prep Guide
page_order: 0.5

page_type: reference
description: "This article covers questions and best practices to consider before building in-app messages, including targeting, scheduling, content, performance, and conversions."
channel: in-app messages
toc_headers: h2
---

# In-app message prep guide

> Before you build your in-app messages, consider the following topics to make the process more efficient.

## General considerations

- If you are building a campaign, how many variants of this message would you like to display? For variant testing ideas, check out [Tips for different channels]({{site.baseurl}}/user_guide/messaging/ab_testing/create_tests#tips-different-channels).
- If you are building a Canvas, will this message be paired with other messaging channels in that step?
- When would you like [your message to expire]({{site.baseurl}}/canvas_in-app_messages)?

## Targeting considerations

- In-app messages are best for users who regularly visit your app. Are you including this audience?
- Where do you want your users to see your message? In your Web app? In your mobile app?
- Which event should trigger this message?
- Are any of your users using older versions of your app? If so, they might not be able to see some elements of your message.
- What type of device or devices are you building this message for? Remember, you can preview your message using the **Preview** box or **Test** tab. Refer to [Send test messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message) for more information.

## Scheduling, delays, and session starts

When an in-app message campaign has **Schedule Delay** with a trigger on session start, a user who starts a session and then closes the app before the in-app message displays can still get that message on the next session start, after the delay expires.

In-app message campaigns can delay delivery after the trigger by up to two hours. For a longer wait, add a [Delay]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step) step before an in-app message step in a Canvas. For delay setup, see [Action-based delivery]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery#step-2-select-delay-length).

That timing can produce unexpected display behavior, especially if **Re-evaluate campaign eligibility before displaying** isn't selected on the campaign.

For example, a user might receive an in-app message with an eight-second delay a month after the campaign launched. That can happen if they started a session, immediately ended the session, started a session a month later, and then eight seconds later received the in-app message. If they navigate away from the app without closing it, the in-app message displays when they return to the app.

## Content considerations

- Which languages will you be using in this message?
- What is your header and body copy? Are they eye-catching and relevant to your user?
- In-app messages only appear for a set amount of time. Is your copy concise and memorable?
- Will you be using [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) to add custom copy?
- Do users need to copy message text (such as a discount or voucher code)? On iOS and Android, users can long-press text or text input fields to copy content. Long-press doesn't work on images, so use text or text input fields instead of images that contain codes or other copy users might need to copy.
- For fullscreen in-app messages, is your image or other media within the [safe zone]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/fullscreen#image-safe-zone)?
- For survey in-app messages, do you want to log attributes or submissions? Have you set up your confirmation page?
- For custom HTML in-app messages, does your HTML include UTF-8 encoding to properly display special characters? See [Custom HTML in-app messages]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#character-encoding) for details.
- If you're including video in your in-app message: While Braze doesn't enforce a technical limit on video file size for local playback on device, keep in mind that users may have slow connections, costly data plans, or limited storage. Optimize video files to balance quality and file size.

## Optimize in-app message performance

Braze delivers eligible in-app message triggers to the user on session start. Preparing many messages with Liquid can delay session start and affect app performance.

If this work takes more than a few seconds, Braze may defer the remaining Liquid rendering. Each message then renders when triggered and is fetched on demand. This [templated delivery]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages) protects your users from poor app performance caused by increased response latency.

Use these best practices to speed up your message delivery:

- Target only users who can perform the campaign's trigger. Overly broad targeting can result in users receiving an in-app message trigger that they're never able to activate. For example, an in-app message triggered by a specific push campaign can be narrowed in scope so that it uses the same target audience. This can be applied similarly for other campaign types, Canvases, custom events that can only be triggered by certain users, and more.
- Set an end date for time-sensitive campaigns. Stop campaigns when you no longer expect them to receive impressions.
- Avoid inserting large static stylesheets, scripts, or base64-encoded media assets directly in the message or through a Content Block. Use the [media library]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library) instead to help reduce time spent rendering your message.
- Reduce complex branching or looping Liquid logic.
- Only enable re-eligibility when users should receive a message multiple times. If re-eligibility is left off, Braze stops delivering the in-app message trigger after the user sees it. For more information, see [Re-eligibility]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility).
- Give important campaigns a higher priority. Braze renders higher-priority eligible messages first, making templated delivery less likely when a user qualifies for many campaigns. For more information, see [Choose a priority]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#choose-a-priority).

### Separate static code and assets

Keep personalized values and conditional rules in the message. Host reusable CSS, JavaScript, and media assets in the [media library]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library), then link to them.

This doesn't need to be done for all scripts and styles. This is primarily helpful to reduce bloat from large assets such as shared brand styles and complex scripts such as interactive widgets.

Media library stylesheets and scripts don't evaluate Liquid, allowing the user's device to cache them. The following example keeps dynamic values inline and loads reusable code from static files:

{% raw %}

```liquid
<head>
  <style>
    /* Select a hero image URL based on the user's subscription tier. */
    {% capture hero_image_url %}
      {% if custom_attribute.${subscription_tier} == 'premium' %}
        https://braze-images.com/path/to/premium/hero.jpg
      {% else %}
        https://braze-images.com/path/to/standard/hero.jpg
      {% endif %}
    {% endcapture %}
    /* Assigning to a CSS variable so it can be used inside our stylesheet. */
    :root {
      --hero-image: url("{{ hero_image_url | url_escape }}");
    }
  </style>
  <script>
    // Assigning to the global window object so the value can be referenced in our script.
    window.brandConfig = {
      subscriptionTier: "{{custom_attribute.${subscription_tier} | json_escape }}"
    };
  </script>
  <!-- Linking to a stylesheet from the Braze media library. -->
  <link rel="stylesheet" href="https://braze-images.com/path/to/media/library/asset.css">
  <!-- Linking to a script from the Braze media library. -->
  <script src="https://braze-images.com/path/to/other/media/library/asset.js" defer></script>
</head>

<body>
  <div class="hero"></div>
  <div class="user-styles" data-subscription-tier="{{custom_attribute.${subscription_tier} | escape}}">
    ...
  </div>
</body>
```

{% endraw %}

The media library stylesheet can reference the CSS variables and define other reusable styles:

```css
.hero {
  background-image: var(--hero-image);
}

.user-styles {
  /* styles for all users */
}

.user-styles[data-subscription-tier="premium"] {
  /* premium subscription tier user styles, color scheme, etc */
}

.user-styles[data-subscription-tier="standard"] {
  /* standard subscription tier user styles, color scheme, etc */
}
```

The media library script can use the inline JavaScript variables to add reusable behavior:

```javascript
const config = window.brandConfig || {};

if (config.subscriptionTier === "standard") {
  // add some sort of logic to show a "subscribe to premium" button
} else if (config.subscriptionTier === "premium") {
  // thank the user for being a premium user
}
```

## Conversion considerations

- What is your goal for this message? How can you represent that in your message?
- Do your buttons offer options that make sense to your user? What is your [primary call to action]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#buttons)?
- Are you [deep linking to other in-app content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls#deep-link-to-in-app-content)? Are you using this in-app message to send and accept a [permission or push priming request]({{site.baseurl}}/user_guide/channels/push/best_practices)?
- Do you have a message exit option? If not, you can always copy and paste this snippet to create a quick button:
  ```html
  <a href="appboy://close">X</a>
  ```

## Drag-and-drop editor considerations

### Adding deep links for different devices

The drag-and-drop editor doesn't support adding different deep links for different devices (unlike the traditional editor).

### Adjusting background image opacity

The opacity setting doesn't allow complete transparency of background images (unlike the traditional IAM editor). You can use opacity settings to make the message background color completely transparent.

### Setting the maximum width

The maximum width in the drag-and-drop editor is limited at 325px; this is primarily meant to accommodate the dashboard preview. Messages can display properly on smaller screen devices.

### Selecting different backgrounds for different platforms

It's not possible to show two different backgrounds for the same message on different platforms (such as web and mobile).

### Applying message styles

Background images apply to the full message and can't be customized per page. Message styles apply to the full message, not individual pages.

### Measuring Spacer blocks height

The measurement unit for Spacer blocks is pixels (px) and can't be changed.

### Supported formats

Currently, only modal and fullscreen in-app messages are supported in the drag-and-drop editor.

### Adjusting to size and aspect ratio

The background image will stretch the in-app message, as the modal adjusts to fit the size and aspect ratio of the background image; you can adjust the ratio as needed.

### Background images and on-click behavior

These persist across pages. For multi-page in-app messages with different full images on each page, add a button to allow users to click to the next page.
