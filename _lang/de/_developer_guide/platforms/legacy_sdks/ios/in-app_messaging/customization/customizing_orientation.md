---
nav_title: Ausrichtung anpassen
article_title: Anpassen der Ausrichtung von In-App-Nachrichten für iOS
platform: iOS
page_order: 3
description: "Dieser Referenzartikel beschreibt, wie Sie die Ausrichtung von In-App-Nachrichten für Ihre iOS-Anwendung festlegen."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Ausrichtung anpassen {#customize-orientation}

## Ausrichtung für alle In-App-Nachrichten einstellen {#setting-orientation-for-all-in-app-messages}

Um eine feste Ausrichtung für alle In-App-Nachrichten festzulegen, können Sie die Eigenschaft `supportedOrientationMask` auf `ABKInAppMessageUIController` setzen. Fügen Sie den folgenden Code nach dem Aufruf Ihrer App an `startWithApiKey:inApplication:withLaunchOptions:` hinzu:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Set fixed in-app message orientation to portrait.
// Use UIInterfaceOrientationMaskLandscape to display in-app messages in landscape
id<ABKInAppMessageUIControlling> inAppMessageUIController = [Appboy sharedInstance].inAppMessageController.inAppMessageUIController;
((ABKInAppMessageUIController *)inAppMessageUIController).supportedOrientationMask = UIInterfaceOrientationMaskPortrait;
```

{% endtab %}
{% tab swift %}

```swift
// Set fixed in-app message orientation to portrait
// Use .landscape to display in-app messages in landscape
if let controller = Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController as? ABKInAppMessageUIController {
  controller.supportedOrientationMask = .portrait
}
```

{% endtab %}
{% endtabs %}

Danach werden alle In-App-Nachrichten in der unterstützten Ausrichtung angezeigt, unabhängig von der Geräteausrichtung. Beachten Sie, dass die Geräteausrichtung auch von der Eigenschaft `orientation` der In-App-Nachricht unterstützt werden muss, damit die Nachricht angezeigt wird.

## Ausrichtung pro In-App-Nachricht einstellen {#setting-orientation-per-in-app-message}

Alternativ können Sie die Ausrichtung auch pro Nachricht einzeln festlegen. Legen Sie dazu einen [Delegaten für In-App-Nachrichten]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates) fest. Setzen Sie dann in Ihrer Delegate-Methode `beforeInAppMessageDisplayed:` die Eigenschaft `orientation` auf `ABKInAppMessage`:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Set inAppMessage orientation to portrait
inAppMessage.orientation = ABKInAppMessageOrientationPortrait;

// Set inAppMessage orientation to landscape
inAppMessage.orientation = ABKInAppMessageOrientationLandscape;
```

{% endtab %}
{% tab swift %}

```swift
  // Set inAppMessage orientation to portrait
  inAppMessage.orientation = ABKInAppMessageOrientation.portrait

  // Set inAppMessage orientation to landscape
  inAppMessage.orientation = ABKInAppMessageOrientation.landscape
```

{% endtab %}
{% endtabs %}

In-App-Nachrichten werden nicht angezeigt, wenn die Geräteausrichtung nicht mit der Eigenschaft `orientation` der In-App-Nachricht übereinstimmt.

{% alert note %}
Bei iPads werden In-App-Nachrichten im von Nutzer:innen bevorzugten Ausrichtungsstil angezeigt, unabhängig von der tatsächlichen Bildschirmausrichtung.
{% endalert %}

## Methodendeklarationen {#method-declarations}

Weitere Informationen finden Sie in der folgenden Header-Datei:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)