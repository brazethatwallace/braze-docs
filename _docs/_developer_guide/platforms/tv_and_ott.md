---
nav_title: TV and OTT
article_title: TV and OTT Integrations for Braze
page_order: 15

description: "This article will give you details on Braze TV and OTT features, integrations, available platforms, and other capabilities."
platform:
  - tvOS
  - Roku
  - Web
  - Android
  - FireOS
---

# TV and OTT integrations

> As technology evolves to new platforms and devices, so can your messaging with Braze! Braze offers different engagement channels for a number of different TV Operating Systems and Over-the-Top (OTT) content delivery methods.

## Platforms and features

The following table summarizes messaging channel support for common TV and OTT platforms. All platforms also support data and analytics, Canvas, and Feature Flags. For Kindle Fire, use the same guidance as Amazon Fire TV. For Apple Vision Pro, see [visionOS support]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/visionos).

<style>
#tv-feature-table td,
#tv-feature-table th {
    text-align: center;
    vertical-align: middle;
    word-break: normal;
    overflow-wrap: normal;
    hyphens: none;
}

#tv-feature-table td:first-child,
#tv-feature-table th:first-child {
    text-align: left;
}

</style>
<table aria-label="TV and OTT messaging channel support" id="tv-feature-table">
  <caption>TV and OTT messaging channel support</caption>
    <thead>
        <tr>
            <th>Device type</th>
            <th>SDK</th>
            <th>In-app messages</th>
            <th>Content Cards</th>
            <th>Push notifications</th>
            <th>Banners</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Amazon Fire TV</td>
            <td><a href="https://github.com/braze-inc/braze-vega-sdk">Vega SDK</a></td>
            <td>✅ Supported</td>
            <td>✅ Supported</td>
            <td>✅ Supported</td>
            <td>🔧 Headless only</td>
        </tr>
        <tr>
            <td>Android TV</td>
            <td><a href="https://github.com/braze-inc/braze-android-sdk">Android SDK</a></td>
            <td>✅ Supported</td>
            <td>✅ Supported</td>
            <td>✅ Supported</td>
            <td>🔧 Headless only</td>
        </tr>
        <tr>
            <td>LG TV (webOS)</td>
            <td><a href="https://github.com/braze-inc/braze-web-sdk">Web SDK</a></td>
            <td>🔧 Headless only</td>
            <td>🔧 Headless only</td>
            <td>➖ OTT platform unsupported</td>
            <td>🔧 Headless only</td>
        </tr>
        <tr>
            <td>Samsung Tizen TV</td>
            <td><a href="https://github.com/braze-inc/braze-web-sdk">Web SDK</a></td>
            <td>🔧 Headless only</td>
            <td>🔧 Headless only</td>
            <td>➖ OTT platform unsupported</td>
            <td>🔧 Headless only</td>
        </tr>
        <tr>
            <td>Roku</td>
            <td><a href="https://github.com/braze-inc/braze-roku-sdk">Roku SDK</a></td>
            <td>🔧 Headless only</td>
            <td>❌ Not supported by Braze</td>
            <td>➖ OTT platform unsupported</td>
            <td>❌ Not supported by Braze</td>
        </tr>
        <tr>
            <td>Apple TV OS (tvOS)</td>
            <td><a href="https://github.com/braze-inc/braze-swift-sdk">Swift SDK</a></td>
            <td>🔧 Headless only</td>
            <td>🔧 Headless only</td>
            <td>❌ Not supported by Braze</td>
            <td>🔧 Headless only</td>
        </tr>
    </tbody>
</table>

{% alert note %}
In this table, **Headless only** means that you will need to build a custom UI.
{% endalert %}

## Integration guides

### Amazon Fire TV {#fire-tv}

Use the Braze Fire OS SDK to integrate with Amazon Fire TV devices.

Features include:

- Data and Analytics collection for cross-channel engagement
- Push Notifications (known as ["Heads Up Notifications"](https://developer.amazon.com/docs/fire-tv/notifications.html#headsup))
  - The priority must be set to "HIGH" for these to appear. All notifications appear in the Fire TV settings menu.
- Content Cards
- Feature Flags
- In-app messages
  - To show HTML messages on non-touch environments like TVs, set `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` to `false` (available from [Android SDK v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310))
- Banners
  - Use [Banner placements]({{site.baseurl}}/developer_guide/banners/placements) to embed messages directly in your Fire TV app.

For more information, visit the [Fire OS integration guide]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android).

### Kindle Fire {#kindle-fire}

Use the Braze Fire OS SDK to integrate with Amazon Kindle Fire devices.

Features include:

- Data and Analytics collection for cross-channel engagement
- Push Notifications
- Content Cards
- Feature Flags
- In-app messages
- Banners
  - Use [Banner placements]({{site.baseurl}}/developer_guide/banners/placements) to embed messages directly in your Kindle Fire. 

For more information, visit the [Fire OS integration guide]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android).

### Android TV {#android-tv}

Use the Braze Android SDK to integrate with Android TV devices.

Features include:

- Data and Analytics collection for cross-channel engagement
- Content Cards
- Feature Flags
- In-app messages 
  - To show HTML messages on non-touch environments like TVs, set `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` to `false` (available from [Android SDK v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310))
- &#42; Push Notifications (Manual Integration Required)
  - Push notifications are not supported natively on Android TV. To learn why, see Google's [Design Guidelines](https://designguidelines.withgoogle.com/android-tv/patterns/notifications.html). You may however, **do a manual integration of Push notification UI to achieve this**. See our [documentation]({{site.baseurl}}/developer_guide/push_notifications?sdktab=android%20tv) on how to set this up.
- Banners
  - Use [Banner placements]({{site.baseurl}}/developer_guide/banners/placements) to embed messages directly in your Android TV app.

For more information, visit the [Android SDK integration guide]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android).

{% alert note %}
Make sure to create a new Android app in the dashboard for your Android OTT integration.
{% endalert %}

### LG webOS {#lg-webos}

Use the Braze Web SDK to integrate with [LG webOS TVs](https://webostv.developer.lge.com/discover).

Features include:

- Data and analytics collection for cross-channel engagement
- Content Cards (via [Headless UI](#custom-ui))
- Feature Flags
- In-app messages (via [Headless UI](#custom-ui))
- Banners
  - Use [Banner placements]({{site.baseurl}}/developer_guide/banners/placements) to embed messages directly in your webOS app.

For more information, visit the [Web Smart TV integration guide]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs).

### Samsung Tizen {#tizen}

Use the Braze Web SDK to integrate with the [Samsung Tizen TVs](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html).

Features include:

- Data and analytics collection for cross-channel engagement
- Content Cards (via [Headless UI](#custom-ui))
- Feature Flags
- In-app messages (via [Headless UI](#custom-ui))
- Banners
  - Use [Banner placements]({{site.baseurl}}/developer_guide/banners/placements) to embed messages directly in your Tizen app.

For more information, visit the [Web Smart TV integration guide]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs).

### Roku {#roku}

Use the Braze Roku SDK to integrate with [Roku TVs](https://developer.roku.com/docs/developer-program/getting-started/roku-dev-prog.md).

Features include:

- Data and analytics collection for cross-channel engagement
- In-app messages (via [Headless UI](#custom-ui))
  - Webviews are not supported by the Roku platform, so HTML in-app messages are therefore not supported.
- Feature Flags

For more information, visit the [Roku integration guide]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=roku).

### Apple TV OS {#tvos}

Use the Braze Swift SDK to integrate with tvOS. Keep in mind, the Swift SDK doesn't include any default UI or views for tvOS, so you will need to implement your own.

Features include:

- Data and analytics collection for cross-channel engagement
- Content Cards (via [Headless UI](#custom-ui))
- Feature Flags
- In-app messages (via [Headless UI](#custom-ui))
  - Webviews are not supported by the tvOS platform, so HTML in-app messages are therefore not supported.
  - See our [sample app](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui) to learn more about how to use a Headless UI for customized messaging on tvOS.
- Silent push notifications and update badging
- Banners
  - Use [Banner placements]({{site.baseurl}}/developer_guide/banners/placements) to embed messages directly in your tvOS app.

For more information, visit the [iOS Swift SDK integration guide](https://github.com/braze-inc/braze-swift-sdk).

{% alert note %}
To avoid showing mobile in-app messages to your TV users, be sure to set up either [App Targeting](#app-targeting) or use key-value pairs to filter out messages. For example, only displaying tvOS messages if they contain a special `tv = true` key-value pair.
{% endalert %}

### Apple Vision Pro {#vision-pro}

Use the Braze Swift SDK to integrate with visionOS. Most features available on iOS are also available on visionOS, including:

- Analytics (sessions, custom events, purchases, etc.)
- In-App Messaging (data models and UI)
- Content Cards (data models and UI)
- Push Notifications (user-visible with action buttons and silent notifications)
- Feature Flags
- Location Analytics
- Banners
  - Use [Banner placements]({{site.baseurl}}/developer_guide/banners/placements) to embed messages directly in your visionOS app.

For more information, visit the [iOS Swift SDK integration guide](https://github.com/braze-inc/braze-swift-sdk).

{% alert important %}
Some iOS features are partially-supported or unsupported. For the full list, see [visionOS support]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/visionos).
{% endalert %}

## App targeting {#app-targeting}

To target OTT apps for messaging, we recommend creating a segment specific to your OTT app.

![A segment created using the Android OTT app.]({% image_buster /assets/img/android_ott.png %})

## Headless UI {#custom-ui}

{% alert important %}
Platforms that support in-app messages or Content Cards through headless UI **do not** include any default UI or views. Build your own custom UI (such as for in-app messages) and then use the SDK-provided data models to populate those UIs.
{% endalert %}

With headless UI, Braze will deliver a data model, such as JSON, that your app can read and use within a UI your app controls. This data will contain the fields configured in the dashboard (title, body, button text, colors, etc.) which your app can read and display accordingly. For more information about custom handling messaging, see the following:

**Android SDK**
- [In-App Message Customization]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=android#android_setting-custom-manager-listeners)
- [Content Cards Customization]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style)

**Swift SDK**
- [In-App Message Customization](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/)
- [Headless UI Sample App](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui)
- [Content Cards Customization](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/)

**Web SDK**
- [In-App Message Customization]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=web)
- [Content Cards Customization]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style)

