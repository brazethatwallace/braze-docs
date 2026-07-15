---
nav_title: Delegates festlegen
article_title: In-App-Nachrichten-Delegates für iOS festlegen
platform: iOS
page_order: 2
description: "Dieser Referenzartikel behandelt das Festlegen von In-App-Nachrichten-Delegates für Ihre iOS-Anwendung."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Delegates festlegen {#set-delegates}

Die Anzeige und Zustellung von In-App-Nachrichten kann im Code angepasst werden, indem Sie unsere optionalen Delegates festlegen.

## In-App-Nachrichten-Delegate {#in-app-message-delegate}

Der [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h)-Delegate kann verwendet werden, um getriggerte In-App-Nachrichten-Payloads zur weiteren Verarbeitung zu empfangen, Ereignisse im Anzeige-Lebenszyklus zu empfangen und das Anzeige-Timing zu steuern.

Setzen Sie Ihr `ABKInAppMessageUIDelegate`-Delegate-Objekt auf der Braze-Instanz, indem Sie Folgendes aufrufen:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance].inAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController?.setInAppMessageUIDelegate?(self)
```

{% endtab %}
{% endtabs %}

In unserer [Beispiel-App](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m) für In-App-Nachrichten finden Sie ein Beispiel für die Implementierung. Beachten Sie, dass dieser Delegate nicht verfügbar ist, wenn Sie die Braze-UI-Bibliothek nicht in Ihr Projekt einbinden (ungewöhnlich).

## Kern-Delegate für In-App-Nachrichten {#core-in-app-message-delegate}

Wenn Sie die Braze-UI-Bibliothek nicht in Ihr Projekt einbinden und getriggerte In-App-Nachrichten-Payloads zur weiteren Verarbeitung oder angepassten Anzeige in Ihrer App empfangen möchten, implementieren Sie das Protokoll [`ABKInAppMessageControllerDelegate`]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates).

Setzen Sie Ihr `ABKInAppMessageControllerDelegate`-Delegate-Objekt auf der Braze-Instanz, indem Sie Folgendes aufrufen:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy sharedInstance].inAppMessageController.delegate = self;
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.inAppMessageController.delegate = self
```

{% endtab %}
{% endtabs %}

Alternativ können Sie Ihren Kern-Delegate für In-App-Nachrichten zur Initialisierungszeit über `appboyOptions` mit dem Schlüssel `ABKInAppMessageControllerDelegateKey` festlegen:
{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKInAppMessageControllerDelegateKey : self }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKInAppMessageControllerDelegateKey : self ])
```
{% endtab %}
{% endtabs %}

## Methodendeklarationen {#method-declarations}

Weitere Informationen finden Sie in den folgenden Header-Dateien:

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)
- [`ABKInAppMessageControllerDelegate.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h)

## Implementierungsbeispiele {#implementation-samples}

Siehe [`ViewController.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m) in der Beispiel-App für In-App-Nachrichten.