---
nav_title: Standorte und Geofences
article_title: Standorte und Geofences für iOS
platform: iOS
page_order: 6
description: "Dieser Referenzartikel beschreibt, wie Sie Standorte und Geofences in Ihrer iOS-Anwendung implementieren."
tool:
  - Location

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Standorte und Geofences {#locations-and-geofences}

Zur Unterstützung von Geofences für iOS:

1. Ihre Integration muss Push-Benachrichtigungen im Hintergrund unterstützen.
2. Braze Geofences [müssen]({{site.baseurl}}/developer_guide/geofences?sdktab=swift) über das SDK or Software-Development-Kit aktiviert werden – entweder implizit durch Aktivieren der Standorterfassung oder explizit durch Aktivieren der Geofence-Erfassung. Sie sind standardmäßig nicht aktiviert.

{% alert important %}
Ab iOS 14 funktionieren Geofences nicht mehr zuverlässig für Nutzer:innen, die lediglich ihren ungefähren Standort freigeben.
{% endalert %}

## Schritt 1: Hintergrund-Push aktivieren {#step-1-enable-background-push}

Um unsere Geofence-Synchronisierungsstrategie vollständig nutzen zu können, müssen Sie [Hintergrund-Push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications#use-silent-push-notifications-to-trigger-background-work) aktiviert haben, zusätzlich zur Durchführung der Standard-Push-Integration.

## Schritt 2: Geofences aktivieren {#step-2-enable-geofences}

Standardmäßig werden Geofences basierend darauf aktiviert, ob die automatische Standorterfassung aktiviert ist. Sie können Geofences über die `Info.plist`-Datei aktivieren. Fügen Sie das `Braze`-Wörterbuch zu Ihrer `Info.plist`-Datei hinzu. Fügen Sie innerhalb des `Braze`-Wörterbuchs den booleschen Untereintrag `EnableGeofences` hinzu und setzen Sie den Wert auf `YES`. Beachten Sie, dass vor dem Braze iOS SDK or Software-Development-Kit v4.0.2 der Wörterbuchschlüssel `Appboy` anstelle von `Braze` verwendet werden muss.

Sie können Geofences auch beim App-Start über die Methode [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24) aktivieren. Setzen Sie im `appboyOptions`-Wörterbuch `ABKEnableGeofencesKey` auf `YES`. Zum Beispiel:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKEnableGeofencesKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKEnableGeofencesKey : true ])
```

{% endtab %}
{% endtabs %}

## Schritt 3: Braze-Hintergrund-Push überprüfen {#step-3-check-for-braze-background-push}

Braze synchronisiert Geofences mit Geräten über Push-Benachrichtigungen im Hintergrund. Lesen Sie den Artikel zur [iOS-Anpassung]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/ignoring_internal_push), um sicherzustellen, dass Ihre Anwendung bei Empfang von Braze-Geofence-Synchronisierungsbenachrichtigungen keine ungewünschten Aktionen ausführt.

## Schritt 4: NSLocationAlwaysUsageDescription zu Ihrer Info.plist hinzufügen {#step-4-add-nslocationalwaysusagedescription-to-your-infoplist}

Fügen Sie den Schlüssel `NSLocationAlwaysUsageDescription` und `NSLocationAlwaysAndWhenInUseUsageDescription` zu Ihrer `info.plist` mit einem `String`-Wert hinzu, der beschreibt, warum Ihre Anwendung den Standort tracken muss. Beide Schlüssel sind ab iOS 11 erforderlich.
Diese Beschreibung wird angezeigt, wenn die Standortberechtigung vom System angefordert wird, und sollte Ihren Nutzer:innen die Vorteile des Standort-Trackings klar erläutern.

## Schritt 5: Autorisierung der Nutzer:innen anfordern {#step-5-request-authorization-from-the-user}

Die Geofence-Funktion ist nur verfügbar, wenn die Standortberechtigung `Always` erteilt wurde.

Um die Standortberechtigung `Always` anzufordern, verwenden Sie den folgenden Code:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```

{% endtab %}
{% tab swift %}

```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```

{% endtab %}
{% endtabs %}

## Schritt 6: Geofences im Dashboard aktivieren {#step-6-enable-geofences-on-the-dashboard}

iOS erlaubt nur die Speicherung von bis zu 20 Geofences für eine bestimmte App. Die Verwendung von Standorten belegt einige dieser 20 verfügbaren Geofence-Slots. Um versehentliche oder unerwünschte Störungen anderer Geofence-bezogener Funktionen in Ihrer App zu vermeiden, müssen Standort-Geofences für einzelne Apps im Dashboard aktiviert werden.

Damit Standorte korrekt funktionieren, sollten Sie außerdem sicherstellen, dass Ihre App nicht alle verfügbaren Geofence-Slots belegt.

### Geofences über die Standortseite aktivieren: {#enable-geofences-from-the-locations-page}

![Die Geofence-Optionen auf der Braze-Standortseite.]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### Geofences über die Einstellungsseite aktivieren: {#enable-geofences-from-the-settings-page}

![Das Geofence-Kontrollkästchen auf den Braze-Einstellungsseiten.]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %})

## Automatische Geofence-Anfragen deaktivieren {#disabling-automatic-geofence-requests}

Ab iOS SDK or Software-Development-Kit Version 3.21.3 können Sie die automatische Anforderung von Geofences deaktivieren. Sie können dies über die Datei `Info.plist` tun. Fügen Sie das `Braze`-Wörterbuch zu Ihrer `Info.plist`-Datei hinzu. Fügen Sie innerhalb des `Braze`-Wörterbuchs den booleschen Untereintrag `DisableAutomaticGeofenceRequests` hinzu und setzen Sie den Wert auf `YES`.

Sie können automatische Geofence-Anfragen auch beim App-Start über die Methode [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24) deaktivieren. Setzen Sie im `appboyOptions`-Wörterbuch `ABKDisableAutomaticGeofenceRequestsKey` auf `YES`. Zum Beispiel:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKDisableAutomaticGeofenceRequestsKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKDisableAutomaticGeofenceRequestsKey : true ])
```

{% endtab %}
{% endtabs %}

Wenn Sie diese Option verwenden, müssen Sie Geofences manuell anfordern, damit das Feature funktioniert.

## Geofences manuell anfordern {#manually-requesting-geofences}

Wenn das Braze SDK or Software-Development-Kit Geofences zur Überwachung vom Backend anfordert, meldet es den aktuellen Standort der Nutzer:innen und empfängt Geofences, die basierend auf dem gemeldeten Standort als optimal relevant bestimmt wurden. Es gibt ein Rate-Limit von einer Geofence-Aktualisierung pro Sitzung.

Um den Standort zu steuern, den das SDK or Software-Development-Kit meldet, um die relevantesten Geofences zu erhalten, können Sie ab iOS SDK or Software-Development-Kit Version 3.21.3 Geofences manuell anfordern, indem Sie den Breiten- und Längengrad eines Standorts angeben. Es wird empfohlen, automatische Geofence-Anfragen zu deaktivieren, wenn Sie diese Methode verwenden. Verwenden Sie dazu den folgenden Code:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] requestGeofencesWithLongitude:longitude
                                              latitude:latitude];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.requestGeofences(withLongitude: longitude, latitude: latitude)
```

{% endtab %}
{% endtabs %}