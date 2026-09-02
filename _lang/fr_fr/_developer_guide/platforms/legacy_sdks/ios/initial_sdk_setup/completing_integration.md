---
nav_title: Terminer l'intégration
article_title: Terminer l'intégration du SDK iOS
platform: iOS
description: "Cet article de référence montre comment terminer l'intégration du SDK Braze après l'avoir installé via l'une des options d'intégration."
page_order: 2

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Terminer l'intégration {#complete-the-integration}

Avant de suivre ces étapes, assurez-vous d'avoir intégré le SDK en utilisant [Carthage]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/carthage_integration), [CocoaPods]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/cocoapods), le [gestionnaire de paquets Swift]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/swift_package_manager) ou une intégration [manuelle]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options).

## Étape 1 : Mettre à jour votre app delegate {#step-1-update-your-app-delegate}

{% tabs %}
{% tab OBJECTIVE-C %}

Si vous intégrez le SDK Braze avec CocoaPods, Carthage ou avec une [intégration manuelle dynamique]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options), ajoutez la ligne de code suivante à votre fichier `AppDelegate.m` :

```objc
#import "Appboy-iOS-SDK/AppboyKit.h"
```

Si vous intégrez avec le gestionnaire de paquets Swift ou avec une [intégration manuelle statique]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options), utilisez plutôt cette ligne :

```objc
#import "AppboyKit.h"
```

Ensuite, dans votre fichier `AppDelegate.m`, ajoutez l'extrait de code suivant dans votre méthode `application:didFinishLaunchingWithOptions:` :

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions];
```

Remplacez `YOUR-APP-IDENTIFIER-API-KEY` par la valeur correcte depuis votre page **Gérer les paramètres**. Consultez notre [documentation API]({{site.baseurl}}/api/identifier_types#app-identifier) pour plus d'informations sur l'emplacement de votre clé API d'identifiant d'application.

{% endtab %}
{% tab swift %}

Si vous intégrez le SDK Braze avec CocoaPods, Carthage ou avec une [intégration manuelle dynamique]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options), ajoutez la ligne de code suivante à votre fichier `AppDelegate.swift` :

```swift
import Appboy_iOS_SDK
```

Si vous intégrez avec le gestionnaire de paquets Swift ou avec une [intégration manuelle statique]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options), utilisez plutôt cette ligne :

```swift
import AppboyKit
```
Consultez la [documentation développeur Apple](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html) pour plus d'informations sur l'utilisation de code Objective-C dans des projets Swift.

Ensuite, dans `AppDelegate.swift`, ajoutez l'extrait de code suivant à votre `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool` :

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY", in:application, withLaunchOptions:launchOptions)
```

Remplacez `YOUR-APP-IDENTIFIER-API-KEY` par la valeur correcte depuis votre page **Gérer les paramètres**. Consultez notre [documentation API]({{site.baseurl}}/api/identifier_types#app-identifier) pour plus d'informations sur l'emplacement de votre clé API d'identifiant d'application.

{% endtab %}
{% endtabs %}

{% alert note %}
Le singleton `sharedInstance` sera nil avant l'appel de `startWithApiKey:`, car il s'agit d'un prérequis pour utiliser toute fonctionnalité de Braze.
{% endalert %}

{% alert warning %}
Assurez-vous d'initialiser Braze dans le thread principal de votre application. Une initialisation asynchrone peut entraîner des dysfonctionnements.
{% endalert %}

## Étape 2 : Spécifier votre cluster de données {#step-2-specify-your-data-cluster}

{% alert note %}
Notez qu'à compter de décembre 2019, les endpoints personnalisés ne sont plus distribués. Si vous disposez d'un endpoint personnalisé préexistant, vous pouvez continuer à l'utiliser. Pour plus de détails, consultez notre <a href="{{site.baseurl}}/api/basics#endpoints">liste des endpoints disponibles</a>.
{% endalert %}

### Configuration de l'endpoint à la compilation (recommandé) {#compile-time-endpoint-configuration-recommended}

Si un endpoint personnalisé préexistant vous a été fourni :
- À partir de la version 3.0.2 du SDK iOS de Braze, vous pouvez définir un endpoint personnalisé à l'aide du fichier `Info.plist`. Ajoutez le dictionnaire `Braze` à votre fichier `Info.plist`. À l'intérieur du dictionnaire `Braze`, ajoutez la sous-entrée de type chaîne de caractères `Endpoint` et définissez sa valeur sur l'autorité de l'URL de votre endpoint personnalisé (par exemple, `sdk.iad-01.braze.com`, et non `https://sdk.iad-01.braze.com`). Notez qu'avant la version 4.0.2 du SDK iOS de Braze, la clé de dictionnaire `Appboy` doit être utilisée à la place de `Braze`.

Votre conseiller Braze devrait déjà vous avoir indiqué l'[endpoint correct]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints).

### Configuration de l'endpoint à l'exécution {#runtime-endpoint-configuration}

Si un endpoint personnalisé préexistant vous a été fourni :
- À partir de la version 3.17.0 et ultérieures du SDK iOS de Braze, vous pouvez remplacer votre endpoint via `ABKEndpointKey` dans le paramètre `appboyOptions` transmis à `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Définissez la valeur sur l'autorité de l'URL de votre endpoint personnalisé (par exemple, `sdk.iad-01.braze.com`, et non `https://sdk.iad-01.braze.com`).

## Intégration SDK terminée {#sdk-integration-complete}

Braze devrait maintenant collecter des données depuis votre application, et votre intégration de base devrait être terminée. Consultez les articles suivants pour activer le [suivi des événements personnalisés]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift), les [notifications push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) et la suite complète des fonctionnalités de Braze.

## Personnalisation de Braze au démarrage {#customizing-braze-on-startup}

Si vous souhaitez personnaliser Braze au démarrage, vous pouvez utiliser la méthode d'initialisation de Braze `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` et transmettre un `NSDictionary` optionnel de clés de démarrage Braze.
{% tabs %}
{% tab OBJECTIVE-C %}

Dans votre fichier `AppDelegate.m`, au sein de votre méthode `application:didFinishLaunchingWithOptions:`, ajoutez la méthode Braze suivante :

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

Notez que cette méthode remplacerait la méthode d'initialisation `startWithApiKey:inApplication:withLaunchOptions:`.

{% endtab %}
{% tab swift %}

Dans `AppDelegate.swift`, au sein de votre méthode `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`, ajoutez la méthode Braze suivante où `appboyOptions` est un `Dictionary` de valeurs de configuration de démarrage :

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

Notez que cette méthode remplacerait la méthode d'initialisation `startWithApiKey:inApplication:withLaunchOptions:`.

{% endtab %}
{% endtabs %}

Cette méthode est appelée avec les paramètres suivants :

- `YOUR-APP-IDENTIFIER-API-KEY` – Votre clé API d'[identifiant d'application]({{site.baseurl}}/api/identifier_types#app-identifier) depuis le tableau de bord de Braze.
- `application` – L'application actuelle.
- `launchOptions` – Le `NSDictionary` d'options que vous obtenez depuis `application:didFinishLaunchingWithOptions:`.
- `appboyOptions` – Un `NSDictionary` optionnel contenant les valeurs de configuration de démarrage pour Braze.

Consultez [Appboy.h](https://github.com/braze-inc/braze-ios-sdk/blob/master/AppboyKit/include/Appboy.h) pour obtenir la liste des clés de démarrage de Braze.

## Appboy.sharedInstance() et la nullabilité en Swift {#appboysharedinstance-and-swift-nullability}
Contrairement à la pratique courante, le singleton `Appboy.sharedInstance()` est optionnel. Cela s'explique par le fait que `sharedInstance` est `nil` avant l'appel de `startWithApiKey:`, et qu'il existe des implémentations non standard mais valides dans lesquelles une initialisation différée peut être utilisée.

Si vous appelez `startWithApiKey:` dans votre délégué `didFinishLaunchingWithOptions:` avant tout accès au `sharedInstance` d'Appboy (l'implémentation standard), vous pouvez utiliser le chaînage optionnel, comme `Appboy.sharedInstance()?.changeUser("testUser")`, pour éviter des vérifications fastidieuses. Le comportement sera identique à celui d'une implémentation en Objective-C qui suppose un `sharedInstance` non nul.

## Ressources supplémentaires {#additional-resources}

La [documentation complète des classes iOS](http://appboy.github.io/appboy-ios-sdk/docs/annotated.html) est disponible pour fournir des informations supplémentaires sur les méthodes du SDK.