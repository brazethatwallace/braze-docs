---
nav_title: SDK or Software-Development-Kit-Ersteinrichtung
article_title: SDK or Software-Development-Kit-Ersteinrichtung für tvOS
platform: tvOS
page_order: 0
page_type: reference
description: "Auf dieser Seite werden die Schritte zur Ersteinrichtung des tvOS Braze SDK or Software-Development-Kit beschrieben."
search_rank: 1
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# SDK or Software-Development-Kit-Ersteinrichtung {#initial-sdk-setup}

> Dieser Referenzartikel beschreibt, wie Sie das Braze SDK or Software-Development-Kit für tvOS installieren. Durch die Installation des Braze SDK or Software-Development-Kit erhalten Sie grundlegende Analytics-Funktionen.

{% alert note %}
Unser tvOS SDK or Software-Development-Kit unterstützt derzeit Analytics-Funktionen. Um eine tvOS-App in Ihrem Dashboard hinzuzufügen, öffnen Sie ein [Support-Ticket]({{site.baseurl}}/user_guide/administer/personal/braze_support).
{% endalert %}

Das tvOS Braze SDK or Software-Development-Kit sollte mit [CocoaPods](http://cocoapods.org/), einem Abhängigkeitsmanager für Objective-C- und Swift-Projekte, installiert oder aktualisiert werden. CocoaPods bietet zusätzliche Einfachheit bei der Integration und Aktualisierung.

## tvOS SDK or Software-Development-Kit CocoaPods-Integration

### Schritt 1: CocoaPods installieren

Die Installation des SDK or Software-Development-Kit über die tvOS-[CocoaPods](http://cocoapods.org/) automatisiert den Großteil des Installationsprozesses für Sie. Bevor Sie diesen Prozess starten, stellen Sie sicher, dass Sie [Ruby Version 2.0.0](https://www.ruby-lang.org/en/installation/) oder höher verwenden.

Führen Sie den folgenden Befehl aus, um zu beginnen:

```bash
$ sudo gem install cocoapods
```

- Wenn Sie aufgefordert werden, die `rake`-Executable zu überschreiben, lesen Sie die Seite [Getting started](http://guides.cocoapods.org/using/getting-started.html) auf CocoaPods.org für weitere Details.
- Wenn Sie Probleme mit CocoaPods haben, lesen Sie den [Leitfaden zur Fehlerbehebung bei CocoaPods](http://guides.cocoapods.org/using/troubleshooting.html).

### Schritt 2: Das Podfile erstellen

Nachdem Sie das CocoaPods Ruby Gem installiert haben, müssen Sie eine Datei in Ihrem Xcode-Projektverzeichnis mit dem Namen `Podfile` erstellen.

Fügen Sie die folgende Zeile zu Ihrem Podfile hinzu:

```
target 'YourAppTarget' do
  pod 'Appboy-tvOS-SDK'
end
```

Wir empfehlen, Braze zu versionieren, damit Pod-Aktualisierungen automatisch alles abrufen, was kleiner als ein Minor-Versionsupdate ist. Das sieht wie folgt aus: `pod 'Appboy-tvOS-SDK' ~> Major.Minor.Build`. Wenn Sie automatisch die neueste Braze SDK or Software-Development-Kit-Version integrieren möchten, auch bei größeren Änderungen, können Sie `pod 'Appboy-tvOS-SDK'` in Ihrem Podfile verwenden.

### Schritt 3: Braze SDK or Software-Development-Kit installieren

Um die Braze SDK or Software-Development-Kit CocoaPods zu installieren, navigieren Sie im Terminal zum Verzeichnis Ihres Xcode-App-Projekts und führen Sie den folgenden Befehl aus:
```
pod install
```

An diesem Punkt sollten Sie den neuen Xcode-Projekt-Workspace öffnen können, der von CocoaPods erstellt wurde. Stellen Sie sicher, dass Sie diesen Xcode-Workspace anstelle Ihres Xcode-Projekts verwenden.

![An diesem Punkt sollten Sie den neuen Xcode-Projekt-Workspace öffnen können, der von CocoaPods erstellt wurde. Stellen Sie sicher, dass Sie diesen Xcode-Workspace anstelle Ihres Xcode-Projekts verwenden.]({% image_buster /assets/img_archive/podsworkspace.png %})

### Schritt 4: Ihren App-Delegate Update or aktualisieren or aktualisieren

{% tabs %}
{% tab OBJECTIVE-C %}

Fügen Sie die folgende Codezeile zu Ihrer `AppDelegate.m`-Datei hinzu:

```objc
#import <AppboyTVOSKit/AppboyKit.h>
```

Fügen Sie innerhalb Ihrer `AppDelegate.m`-Datei das folgende Snippet in Ihre `application:didFinishLaunchingWithOptions`-Methode ein:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

Update or aktualisieren or aktualisieren Sie abschließend `YOUR-API-KEY` mit dem korrekten Wert von Ihrer Seite **Einstellungen verwalten**.

{% endtab %}
{% tab swift %}

Wenn Sie das Braze SDK or Software-Development-Kit mit CocoaPods oder Carthage integrieren, fügen Sie die folgende Codezeile zu Ihrer `AppDelegate.swift`-Datei hinzu:

```swift
import AppboyTVOSKit
```

Weitere Informationen zur Verwendung von Objective-C-Code in Swift-Projekten finden Sie in den [Apple Developer Docs](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html).

Fügen Sie in `AppDelegate.swift` das folgende Snippet zu Ihrer `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`-Methode hinzu:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```

Update or aktualisieren or aktualisieren Sie anschließend `YOUR-API-KEY` mit dem korrekten Wert von Ihrer Seite **Einstellungen verwalten**.

Unser `sharedInstance`-Singleton ist `nil`, bevor `startWithApiKey:` aufgerufen wird, da dies eine Voraussetzung für die Nutzung jeglicher Braze-Funktionalität ist.

{% endtab %}
{% endtabs %}

{% alert warning %}
Stellen Sie sicher, dass Sie Braze im Hauptthread Ihrer Anwendung initialisieren. Eine asynchrone Initialisierung kann zu fehlerhafter Funktionalität führen.
{% endalert %}

### Schritt 5: Ihren angepassten Endpunkt oder Datencluster angeben

{% alert note %}
Seit Dezember 2019 werden keine angepassten Endpunkte mehr ausgegeben. Wenn Sie einen bereits bestehenden angepassten Endpunkt haben, können Sie diesen weiterhin verwenden. Weitere Details finden Sie in unserer <a href="{{site.baseurl}}/api/basics#endpoints">Liste der verfügbaren Endpunkte</a>.
{% endalert %}

Ihre Braze-Vertretung sollte Sie bereits über den [korrekten Endpunkt]({{ site.baseurl }}/user_guide/administrative/access_braze/sdk_endpoints/) informiert haben.

#### Endpunkt-Konfiguration zur Kompilierungszeit (empfohlen)
Wenn Ihnen ein bereits bestehender angepasster Endpunkt zugeteilt wurde:
- Ab Braze iOS SDK or Software-Development-Kit v3.0.2 können Sie einen angepassten Endpunkt über die `Info.plist`-Datei festlegen. Fügen Sie das `Appboy`-Dictionary zu Ihrer Info.plist-Datei hinzu. Fügen Sie innerhalb des `Appboy`-Dictionarys den `Endpoint`-String-Untereintrag hinzu und setzen Sie den Wert auf die Authority Ihrer angepassten Endpunkt-URL (zum Beispiel `sdk.iad-01.braze.com`, nicht `https://sdk.iad-01.braze.com`).

#### Endpunkt-Konfiguration zur Laufzeit
Wenn Ihnen ein bereits bestehender angepasster Endpunkt zugeteilt wurde:
- Ab Braze iOS SDK or Software-Development-Kit v3.17.0+ können Sie Ihren Endpunkt über den `ABKEndpointKey` innerhalb des `appboyOptions`-Parameters überschreiben, der an `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` übergeben wird. Setzen Sie den Wert auf die Authority Ihrer angepassten Endpunkt-URL (zum Beispiel `sdk.iad-01.braze.com`, nicht `https://sdk.iad-01.braze.com`).

{% alert note %}
Die Unterstützung für das Festlegen von Endpunkten zur Laufzeit über `ABKAppboyEndpointDelegate` wurde in Braze iOS SDK or Software-Development-Kit v3.17.0 entfernt. Wenn Sie bereits `ABKAppboyEndpointDelegate` verwenden, beachten Sie, dass in den Braze iOS SDK or Software-Development-Kit Versionen v3.14.1 bis v3.16.0 jede Referenz auf `dev.appboy.com` in Ihrer `getApiEndpoint()`-Methode durch eine Referenz auf `sdk.iad-01.braze.com` ersetzt werden muss.
{% endalert %}

### SDK or Software-Development-Kit-Integration abgeschlossen

Braze sollte jetzt Daten aus Ihrer Anwendung sammeln, und Ihre grundlegende Integration sollte abgeschlossen sein. Beachten Sie, dass beim Kompilieren Ihrer tvOS-App und aller anderen Drittanbieter-Bibliotheken Bitcode aktiviert sein muss.

### Braze SDK or Software-Development-Kit über CocoaPods Update or aktualisieren or aktualisieren

Um ein CocoaPod zu Update or aktualisieren or aktualisieren, führen Sie einfach die folgenden Befehle in Ihrem Projektverzeichnis aus:

```
pod update
```

## Braze beim Start anpassen

Wenn Sie Braze beim Start anpassen möchten, können Sie stattdessen die Braze-Initialisierungsmethode `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions` verwenden und ein optionales `NSDictionary` mit Braze-Startschlüsseln übergeben.
{% tabs %}
{% tab OBJECTIVE-C %}

Fügen Sie in Ihrer `AppDelegate.m`-Datei innerhalb Ihrer `application:didFinishLaunchingWithOptions`-Methode die folgende Braze-Methode hinzu:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab swift %}

Fügen Sie in `AppDelegate.swift` innerhalb Ihrer `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`-Methode die folgende Braze-Methode hinzu:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

wobei `appboyOptions` ein `Dictionary` mit Startkonfigurationswerten ist.

{% endtab %}
{% endtabs %}

Diese Methode ersetzt die Initialisierungsmethode `startWithApiKey:inApplication:withLaunchOptions:` und wird mit den folgenden Parametern aufgerufen:

- `YOUR-API-KEY`: Der API-Schlüssel Ihrer Anwendung befindet sich unter **Einstellungen verwalten** im Braze-Dashboard.
- `application`: Die aktuelle App.
- `launchOptions`: Das Options-`NSDictionary`, das Sie von `application:didFinishLaunchingWithOptions:` erhalten.
- `appboyOptions`: Ein optionales `NSDictionary` mit Startkonfigurationswerten für Braze.

Eine Liste der Braze-Startschlüssel finden Sie unter [Appboy.h](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h).

## Appboy.sharedInstance() und Swift-Nullability
Anders als häufig üblich ist das Singleton `Appboy.sharedInstance()` optional. Das liegt daran, dass `sharedInstance` den Wert `nil` hat, bevor `startWithApiKey:` aufgerufen wird, und es einige nicht standardmäßige, aber durchaus zulässige Implementierungen gibt, bei denen eine verzögerte Initialisierung verwendet werden kann.

Wenn Sie `startWithApiKey:` in Ihrem `didFinishLaunchingWithOptions:`-Delegate aufrufen, bevor Sie auf Appboys `sharedInstance` zugreifen (die Standardimplementierung), können Sie Optional Chaining verwenden, z. B. `Appboy.sharedInstance()?.changeUser("testUser")`, um umständliche Prüfungen zu vermeiden. Dies entspricht dem Verhalten einer Objective-C-Implementierung, die ein nicht-null `sharedInstance` voraussetzt.

Sie können unser tvOS SDK or Software-Development-Kit auch manuell integrieren – laden Sie einfach das Framework aus unserem [Public Repository](https://github.com/appboy/appboy-ios-sdk) herunter und initialisieren Sie Braze wie in den vorhergehenden Abschnitten beschrieben.

## Nutzer:innen identifizieren und Analytics erfassen
Informationen zum Festlegen von Nutzer-IDs, zum Protokollieren angepasster Events und zum Setzen von Nutzerattributen finden Sie in unserer [iOS-Dokumentation]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift). Wir empfehlen außerdem, sich mit unseren [Namenskonventionen für Events]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions) vertraut zu machen.