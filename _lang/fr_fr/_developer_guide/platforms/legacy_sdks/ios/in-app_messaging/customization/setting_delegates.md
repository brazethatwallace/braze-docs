---
nav_title: Définir les délégués
article_title: Définir les délégués de messages in-app pour iOS
platform: iOS
page_order: 2
description: "Cet article de référence couvre la définition des délégués de messages in-app pour votre application iOS."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Définir les délégués {#set-delegates}

Les personnalisations de l'affichage et de la distribution des messages in-app peuvent être réalisées dans le code en définissant nos délégués facultatifs.

## Délégué de message in-app {#in-app-message-delegate}

Le délégué [`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h) peut être utilisé pour recevoir des payloads de messages in-app déclenchés en vue d'un traitement ultérieur, pour recevoir des événements liés au cycle de vie de l'affichage et pour contrôler la synchronisation de l'affichage.

Définissez votre objet délégué `ABKInAppMessageUIDelegate` sur l'instance Braze en appelant :

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

Consultez notre [exemple d'application](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m) de message in-app pour un exemple d'implémentation. Notez que si vous n'incluez pas la bibliothèque d'interface utilisateur de Braze dans votre projet (peu courant), ce délégué n'est pas disponible.

## Délégué principal de message in-app {#core-in-app-message-delegate}

Si vous n'incluez pas la bibliothèque d'interface utilisateur de Braze dans votre projet et que vous souhaitez recevoir des payloads de messages in-app déclenchés pour un traitement ultérieur ou un affichage personnalisé dans votre application, implémentez le protocole [`ABKInAppMessageControllerDelegate`]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/customization/setting_delegates).

Définissez votre objet délégué `ABKInAppMessageControllerDelegate` sur l'instance Braze en appelant :

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

Vous pouvez également définir votre délégué principal de message in-app au moment de l'initialisation via `appboyOptions` à l'aide de la clé `ABKInAppMessageControllerDelegateKey` :
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

## Déclarations de méthode {#method-declarations}

Pour plus d'informations, consultez les fichiers d'en-tête suivants :

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)
- [`ABKInAppMessageControllerDelegate.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessageControllerDelegate.h)

## Exemples d'implémentation {#implementation-samples}

Consultez [`ViewController.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/Samples/InAppMessage/BrazeInAppMessageSample/BrazeInAppMessageSample/ViewController.m) dans l'exemple d'application de message in-app.