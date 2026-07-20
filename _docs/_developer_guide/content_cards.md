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
## Prerequisites

Before you can use Braze Content Cards, you'll need to integrate the [Braze Android SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android) into your app. However, no additional setup is required.

## Google fragments

In Android, the Content Cards feed is implemented as a [fragment](https://developer.android.com/guide/components/fragments.html) available in the Braze Android UI project. The [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) class will automatically refresh and display the contents of the Content Cards and log usage analytics. The cards that can appear in a user's `ContentCards` are created on the Braze dashboard.

To learn how to add a fragment to an activity, see [Google's fragments documentation](https://developer.android.com/guide/fragments#Adding).

## Card types and properties

The Content Cards data model is available in the Android SDK and offers the following unique Content Card types. Each type shares a base model, which allows them to inherit common properties from the base model, in addition to having their own unique properties. For full reference documentation, see [`com.braze.models.cards`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html).

### Base card model {#base-card-for-android}

The [base card](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) model provides foundational behavior for all cards.  

|Property | Description |
|---|---|
|`getId()` | Returns the card's ID set by Braze.|
|`getViewed()` | Returns a boolean reflects if the card is read or unread by the user.|
|`getExtras()` | Returns a map of key-value extras for this card.|
|`getCreated()`  | Returns the unix timestamp of the card's creation time from Braze.|
|`isPinned` | Returns a boolean that reflects whether the card is pinned.|
|`getOpenUriInWebView()`  | Returns a boolean that reflects whether Uris for this card should be opened <br> in the Braze WebView or not.|
|`getExpiredAt()` | Gets the expiration date of the card.|
|`isRemoved()` | Returns a boolean that reflects whether the end user has dismissed this card.|
|`isDismissibleByUser()`  | Returns a boolean that reflects whether the card is dismissible by the user.|
|`isClicked()` | Returns a boolean that reflects the clicked state of this card.|
|`isDismissed` | Returns a boolean that reflects whether the card has been dismissed. Set to `true` to mark the card as dismissed. If a card is already marked as dismissed, it cannot be marked as dismissed again.|
|`isControl()` | Returns a boolean if this card is a control card and should not be rendered.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Base card model #base-card-for-android" }

### Image only {#banner-image-card-for-android}

[Image only cards](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-image-only-card/index.html) are clickable full-sized images.

|Property | Description |
|---|---|
|`getImageUrl()` | Returns the URL of the card's image.|
|`getUrl()` | Returns the URL that will be opened after the card is clicked. It can be a HTTP(s) URL or a protocol URL.|
|`getDomain()` | Returns link text for the property URL.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Image only #banner-image-card-for-android" }

### Captioned image {#captioned-image-card-for-android}

[Captioned image cards](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-captioned-image-card/index.html) are clickable, full-sized images with accompanying descriptive text.

|Property | Description |
|---|---|
|`getImageUrl()` | Returns the URL of the card's image.|
|`getTitle()` | Returns the title text for the card.|
|`getDescription()` | Returns the body text for the card.|
|`getUrl()` | Returns the URL that will be opened after the card is clicked. It can be a HTTP(s) URL or a protocol URL.|
|`getDomain()` | Returns the link text for the property URL. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Captioned image #captioned-image-card-for-android" }

### Classic {#text-Announcement-card-for-android}

A classic card without an image included will result in a [text announcement card](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-text-announcement-card/index.html). If an image is included, you will receive a [short news card](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-short-news-card/index.html).

|Property | Description |
|---|---|
|`getTitle()` | Returns the title text for the card. |
|`getDescription()` | Returns the body text for the card. |
|`getUrl()` | Returns the URL that will be opened after the card is clicked. It can be a HTTP(s) URL or a protocol URL. | 
|`getDomain()` | Returns the link text for the property URL. |
|`getImageUrl()` | Returns the URL of the card's image, applies only to the classic Short News Card. |
|`isDismissed` | Returns a boolean that reflects whether the card has been dismissed. Set to `true` to mark the card as dismissed. If a card is already marked as dismissed, it cannot be marked as dismissed again. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Classic #text-Announcement-card-for-android" }

## Card methods

All [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/index.html) data model objects offer the following analytics methods for logging user events to Braze servers.

|Method | Description |
|---|---|
|`logImpression()` | Manually log an impression to Braze for a particular card. |
|`logClick()` | Manually log a click to Braze for a particular card. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Card methods" }

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

Before you can use Content Cards, you'll need to integrate the [Braze Swift SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) into your app. Then you'll need to complete the steps for setting up your tvOS app.

{% alert important %}
Keep in mind, you'll need to implement your own custom UI since Content Cards are supported via headless UI using the Swift SDK&#8212;which does not include any default UI or views for tvOS.
{% endalert %}

## Setting up your tvOS app

### Step 1: Create a new iOS app

In Braze, select **Settings** > **App Settings**, then select **Add App**. Enter a name for your tvOS app, select **iOS**&#8212;_not tvOS_&#8212;then select **Add App**.

![ALT_TEXT.]({% image_buster /assets/img/tvos.png %}){: style="width:70%"}

{% alert warning %}
If you select the **tvOS** checkbox, you will not be able to customize Content Cards for tvOS.
{% endalert %}

### Step 2: Get your app's API key

In your app settings, select your new tvOS app then take note of your app's API key. You'll use this key to configure your app in Xcode.

![ALT_TEXT]({% image_buster /assets/img/tvos1.png %}){: style="width:70%"}

### Step 3: Integrate BrazeKit

Use your app's API key to integrate the [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk) into your tvOS project in Xcode. You only need to integrate BrazeKit from the Braze Swift SDK.

### Step 4: Create your custom UI

Because Braze doesn't provide a default UI for content cards on tvOS, you'll need to customize it yourself. For a full walkthrough, see our step-by-step tutorial: [Customizing content cards for tvOS](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/content-cards-customization/). For a sample project, see [Braze Swift SDK samples](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#contentcards-custom-ui).

{% endsdktab %}

{% sdktab unity %}
{% multi_lang_include developer_guide/unity/content_cards.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
{% multi_lang_include developer_guide/xamarin/content_cards.md %}
{% endsdktab %}
{% endsdktabs %}
