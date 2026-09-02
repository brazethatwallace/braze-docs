---
nav_title: Fertigstellung der Integration
article_title: Führen Sie die iOS SDK or Software-Development-Kit-Integration durch
platform: iOS
description: "Dieser Referenzartikel beschreibt, wie Sie die Integration des Braze SDK or Software-Development-Kit abschließen, nachdem Sie es über eine der Integrationsoptionen installiert haben."
page_order: 2

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Die Integration abschließen {#complete-the-integration}

Bevor Sie diese Schritte ausführen, vergewissern Sie sich bitte, dass das SDK or Software-Development-Kit mit [Carthage]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/carthage_integration), [CocoaPods]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/cocoapods), dem [Swift-Paketmanager]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/swift_package_manager) oder einer [manuellen]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options) Integration integriert wurde.

## Schritt 1: Update or aktualisieren or aktualisieren Sie Ihren App-Delegate {#step-1-update-your-app-delegate}

{% tabs %}
{% tab OBJECTIVE-C %}

Wenn Sie das Braze SDK or Software-Development-Kit mit CocoaPods, Carthage oder mit einer [dynamischen manuellen Integration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options) integrieren, fügen Sie die folgende Codezeile zu Ihrer `AppDelegate.m`-Datei hinzu:

```objc
#import "Appboy-iOS-SDK/AppboyKit.h"
```

Wenn Sie mit dem Swift-Paketmanager oder mit einer [statischen manuellen Integration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options) integrieren, verwenden Sie stattdessen diese Zeile:

```objc
#import "AppboyKit.h"
```

Fügen Sie als Nächstes in Ihrer `AppDelegate.m`-Datei das folgende Snippet innerhalb Ihrer `application:didFinishLaunchingWithOptions:`-Methode hinzu:

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions];
```

Update or aktualisieren or aktualisieren Sie `YOUR-APP-IDENTIFIER-API-KEY` mit dem korrekten Wert von Ihrer Seite **Einstellungen verwalten**. Weitere Informationen darüber, wo Sie Ihren App-Bezeichner-API-Schlüssel finden, finden Sie in unserer [API-Dokumentation]({{site.baseurl}}/api/identifier_types#app-identifier).

{% endtab %}
{% tab swift %}

Wenn Sie das Braze SDK or Software-Development-Kit mit CocoaPods, Carthage oder mit einer [dynamischen manuellen Integration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options) integrieren, fügen Sie die folgende Codezeile zu Ihrer `AppDelegate.swift`-Datei hinzu:

```swift
import Appboy_iOS_SDK
```

Wenn Sie mit dem Swift-Paketmanager oder mit einer [statischen manuellen Integration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options) integrieren, verwenden Sie stattdessen diese Zeile:

```swift
import AppboyKit
```
Weitere Informationen zur Verwendung von Objective-C-Code in Swift-Projekten finden Sie in der [Apple-Entwicklerdokumentation](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html).

Fügen Sie als Nächstes in `AppDelegate.swift` das folgende Snippet zu Ihrer `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`-Methode hinzu:

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY", in:application, withLaunchOptions:launchOptions)
```

Update or aktualisieren or aktualisieren Sie `YOUR-APP-IDENTIFIER-API-KEY` mit dem korrekten Wert von Ihrer Seite **Einstellungen verwalten**. Weitere Informationen darüber, wo Sie Ihren App-Bezeichner-API-Schlüssel finden, finden Sie in unserer [API-Dokumentation]({{site.baseurl}}/api/identifier_types#app-identifier).

{% endtab %}
{% endtabs %}

{% alert note %}
Das `sharedInstance`-Singleton ist nil, bevor `startWithApiKey:` aufgerufen wird, da dies eine Voraussetzung für die Nutzung jeglicher Braze-Funktionalität ist.
{% endalert %}

{% alert warning %}
Stellen Sie sicher, dass Sie Braze im Hauptthread Ihrer Anwendung initialisieren. Eine asynchrone Initialisierung kann zu fehlerhafter Funktionalität führen.
{% endalert %}

## Schritt 2: Ihren Daten-Cluster angeben {#step-2-specify-your-data-cluster}

{% alert note %}
Beachten Sie, dass seit Dezember 2019 keine angepassten Endpunkte mehr vergeben werden. Wenn Sie einen bereits bestehenden angepassten Endpunkt haben, können Sie diesen weiterhin verwenden. Weitere Details finden Sie in unserer <a href="{{site.baseurl}}/api/basics#endpoints">Liste der verfügbaren Endpunkte</a>.
{% endalert %}

### Endpunktkonfiguration zur Kompilierzeit (empfohlen) {#compile-time-endpoint-configuration-recommended}

Wenn ein bereits bestehender angepasster Endpunkt vergeben wurde:
- Ab Braze iOS SDK or Software-Development-Kit v3.0.2 können Sie einen angepassten Endpunkt über die `Info.plist`-Datei festlegen. Fügen Sie das `Braze`-Wörterbuch zu Ihrer `Info.plist`-Datei hinzu. Fügen Sie innerhalb des `Braze`-Wörterbuchs den `Endpoint`-String-Untereintrag hinzu und setzen Sie den Wert auf die Autorität der URL Ihres angepassten Endpunkts (zum Beispiel `sdk.iad-01.braze.com`, nicht `https://sdk.iad-01.braze.com`). Beachten Sie, dass vor Braze iOS SDK v4.0.2 der Wörterbuch-Schlüssel `Appboy` anstelle von `Braze` verwendet werden muss.

Ihre Braze-Vertretung sollte Sie bereits über den [richtigen Endpunkt]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints) informiert haben.

### Endpunktkonfiguration zur Laufzeit {#runtime-endpoint-configuration}

Wenn ein bereits bestehender angepasster Endpunkt vergeben wurde:
- Ab Braze iOS SDK or Software-Development-Kit v3.17.0+ können Sie Ihren Endpunkt über den `ABKEndpointKey` innerhalb des `appboyOptions`-Parameters überschreiben, der an `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` übergeben wird. Setzen Sie den Wert auf die Autorität der URL Ihres angepassten Endpunkts (zum Beispiel `sdk.iad-01.braze.com`, nicht `https://sdk.iad-01.braze.com`).

## SDK or Software-Development-Kit-Integration abgeschlossen {#sdk-integration-complete}

Braze sollte nun Daten aus Ihrer Anwendung erfassen, und Ihre grundlegende Integration sollte abgeschlossen sein. In den folgenden Artikeln erfahren Sie, wie Sie [angepasstes Event-Tracking]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift), [Push-Messaging]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) und die gesamte Suite der Braze-Features aktivieren.

## Braze beim Start anpassen {#customizing-braze-on-startup}

Wenn Sie Braze beim Start anpassen möchten, können Sie stattdessen die Braze-Initialisierungsmethode `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` verwenden und ein optionales `NSDictionary` mit Braze-Startschlüsseln übergeben.
{% tabs %}
{% tab OBJECTIVE-C %}

Fügen Sie in Ihrer `AppDelegate.m`-Datei innerhalb Ihrer `application:didFinishLaunchingWithOptions:`-Methode die folgende Braze-Methode hinzu:

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

Beachten Sie, dass diese Methode die Initialisierungsmethode `startWithApiKey:inApplication:withLaunchOptions:` ersetzt.

{% endtab %}
{% tab swift %}

Fügen Sie in `AppDelegate.swift` innerhalb Ihrer `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`-Methode die folgende Braze-Methode hinzu, wobei `appboyOptions` ein `Dictionary` mit Startkonfigurationswerten ist:

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

Beachten Sie, dass diese Methode die Initialisierungsmethode `startWithApiKey:inApplication:withLaunchOptions:` ersetzt.

{% endtab %}
{% endtabs %}

Diese Methode wird mit den folgenden Parametern aufgerufen:

- `YOUR-APP-IDENTIFIER-API-KEY` – Ihr [App-Bezeichner]({{site.baseurl}}/api/identifier_types#app-identifier)-API-Schlüssel aus dem Braze-Dashboard.
- `application` – Die aktuelle App.
- `launchOptions` – Das Options-`NSDictionary`, das Sie von `application:didFinishLaunchingWithOptions:` erhalten.
- `appboyOptions` – Ein optionales `NSDictionary` mit Startkonfigurationswerten für Braze.

Eine Liste der Braze-Startschlüssel finden Sie unter [Appboy.h](https://github.com/braze-inc/braze-ios-sdk/blob/master/AppboyKit/include/Appboy.h).

## Appboy.sharedInstance() und Swift-Nullability {#appboysharedinstance-and-swift-nullability}
Abweichend von der gängigen Praxis ist das `Appboy.sharedInstance()`-Singleton optional. Das liegt daran, dass `sharedInstance` den Wert `nil` hat, bevor `startWithApiKey:` aufgerufen wird, und es einige nicht-standardmäßige, aber dennoch zulässige Implementierungen gibt, bei denen eine verzögerte Initialisierung verwendet werden kann.

Wenn Sie `startWithApiKey:` in Ihrem `didFinishLaunchingWithOptions:`-Delegate aufrufen, bevor auf Appboys `sharedInstance` zugegriffen wird (die Standardimplementierung), können Sie Optional Chaining verwenden, z. B. `Appboy.sharedInstance()?.changeUser("testUser")`, um aufwändige Prüfungen zu vermeiden. Damit erreichen Sie dasselbe Verhalten wie bei einer Objective-C-Implementierung, die von einer nicht-null `sharedInstance` ausgeht.

## Zusätzliche Ressourcen {#additional-resources}

Die vollständige [iOS-Klassendokumentation](http://appboy.github.io/appboy-ios-sdk/docs/annotated.html) steht zur Verfügung und bietet zusätzliche Informationen zu allen SDK or Software-Development-Kit-Methoden.