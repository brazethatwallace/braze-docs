---
page_order: 2.2
nav_title: Content Cards
article_title: Content Cards in the Braze SDK
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Content Cards

> Learn about Content Cards for the Braze SDK, including the different data models and card-specific properties available for your application.

{% multi_lang_include banners/content_card_alert.md %}

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/content_cards.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/content_cards.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/content_cards.md %}
{% endsdktab %}

{% sdktab cordova %}
{% multi_lang_include developer_guide/cordova/content_cards.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/content_cards.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/content_cards.md %}
{% endsdktab %}

{% sdktab tvos %}
## Prerequisites

Before you can use Content Cards, integrate the [Braze Swift SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) into your app. Then complete the steps for setting up your tvOS app.

{% alert important %}
Implement your own custom UI since Content Cards are supported via headless UI using the Swift SDK&#8212;which does not include any default UI or views for tvOS.
{% endalert %}

## Setting up your tvOS app

### Step 1: Create a new iOS app

In Braze, select **Settings** > **App Settings**, then select **Add App**. Enter a name for your tvOS app, select **iOS**&#8212;_not tvOS_&#8212;then select **Add App**.

![Add App dialog in Braze with the iOS platform selected to register a tvOS app.]({% image_buster /assets/img/tvos.png %}){: style="width:70%"}

{% alert warning %}
If you select the **tvOS** checkbox, you cannot customize Content Cards for tvOS.
{% endalert %}

### Step 2: Get your app's API key

In your app settings, select your new tvOS app, then take note of your app's API key. Use this key to configure your app in Xcode.

![App settings for a tvOS app showing the API key used for SDK integration.]({% image_buster /assets/img/tvos1.png %}){: style="width:70%"}

### Step 3: Integrate BrazeKit

Use your app's API key to integrate the [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk) into your tvOS project in Xcode. You only need to integrate BrazeKit from the Braze Swift SDK.

### Step 4: Create your custom UI

Because Braze doesn't provide a default UI for content cards on tvOS, customize it yourself. For a full walkthrough, see our step-by-step tutorial: [Customizing content cards for tvOS](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/content-cards-customization/). For a sample project, see [Braze Swift SDK samples](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#contentcards-custom-ui).

{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/content_cards.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
{% multi_lang_include developer_guide/xamarin/content_cards.md %}
{% endsdktab %}
{% endsdktabs %}
