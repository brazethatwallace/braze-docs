{% alert important %}
Ab iOS 14 funktionieren Geofences nicht mehr zuverlässig für Nutzer:innen, die nur ihre ungefähre Standortberechtigung erteilen.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Einrichten von Geofences {#setting-up-geofences}

### Schritt 1: Enablement in Braze {#step-1-enable-in-braze}

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### Schritt 2: Aktivieren Sie die Standortdienste Ihrer App {#step-2-enable-your-apps-location-services}

Standardmäßig sind die Standortdienste von Braze nicht aktiviert. Um sie in Ihrer App zu aktivieren, führen Sie die folgenden Schritte aus. Eine Schritt-für-Schritt-Anleitung finden Sie unter [Tutorial: Braze Standorte und Geofences](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/).

#### Schritt 2.1: Fügen Sie das Modul `BrazeLocation` hinzu {#step-21-add-the-brazelocation-module}

Öffnen Sie in Xcode den Tab **General**. Fügen Sie unter **Frameworks, Libraries, and Embedded Content** das Modul `BrazeLocation` hinzu.

![Das Modul „BrazeLocation“ in Ihrem Xcode-Projekt hinzufügen]({% image_buster /assets/img/sdk_geofences/add-brazeLocation-module-xcode.png %})

#### Schritt 2.2: Aktualisieren Sie Ihre `Info.plist` {#step-22-update-your-infoplist}

Weisen Sie in Ihrer `info.plist` einem der folgenden Schlüssel einen `String`-Wert zu, der beschreibt, warum Ihre Anwendung den Standort verfolgen muss. Dieser String wird angezeigt, wenn Ihre Nutzer:innen zur Eingabe von Standortdiensten aufgefordert werden. Erklären Sie daher deutlich, welchen Wert die Aktivierung dieses Features für Ihre App hat.

- `NSLocationAlwaysAndWhenInUseUsageDescription`
- `NSLocationWhenInUseUsageDescription`

![Info.plist-Standort-Strings in Xcode]({% image_buster /assets/img/sdk_geofences/info-plist-location-strings.png %})

{% alert important %}
Apple hat `NSLocationAlwaysUsageDescription` als veraltet markiert. Weitere Informationen finden Sie in der [Entwickler:innen-Dokumentation von Apple](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysusagedescription).
{% endalert %}

### Schritt 3: Geofences in Ihrem Code aktivieren {#step-3-enable-geofences-in-your-code}

Aktivieren Sie im Code Ihrer App Geofences, indem Sie `location.geofencesEnabled` auf `true` im `configuration`-Objekt setzen, das die [`Braze`](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/d1-brazelocation/)-Instanz initialisiert. Für weitere `location`-Konfigurationsoptionen siehe [Braze Swift SDK-Referenz](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/location-swift.class).

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.location.brazeLocationProvider = BrazeLocationProvider()
configuration.location.automaticLocationCollection = true
configuration.location.geofencesEnabled = true
configuration.location.automaticGeofenceRequests = true

// Additional configuration customization...

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                    endpoint:brazeEndpoint];
configuration.logger.level = BRZLoggerLevelInfo;
configuration.location.brazeLocationProvider = [[BrazeLocationProvider alloc] init];
configuration.location.automaticLocationCollection = YES;
configuration.location.geofencesEnabled = YES;
configuration.location.automaticGeofenceRequests = YES;

// Additional configuration customization...

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

#### Schritt 3.1: Hintergrundberichte aktivieren (optional) {#step-31-enable-background-reporting-optional}

Standardmäßig werden Geofence-Ereignisse nur überwacht, wenn sich Ihre App im Vordergrund befindet oder über eine `Always`-Autorisierung verfügt, die alle Anwendungszustände überwacht.

Sie können jedoch auch Geofence-Ereignisse überwachen, wenn Ihre App im Hintergrund läuft oder über eine [`When In Use`-Autorisierung](#swift_request-authorization) verfügt.

Um diese zusätzlichen Geofence-Ereignisse zu überwachen, öffnen Sie Ihr Xcode-Projekt und gehen Sie zu **Signing & Capabilities**. Aktivieren Sie unter **Background Modes** die Option **Location updates**.

![In Xcode, Background Modes > Location Updates]({% image_buster /assets/img/sdk_geofences/xcode-background-modes-location-updates.png %})

Aktivieren Sie als Nächstes `allowBackgroundGeofenceUpdates` im Code Ihrer App. So kann Braze den „When In Use“-Status Ihrer App verlängern, indem es kontinuierlich Standort-Updates überwacht. Diese Einstellung funktioniert nur, wenn sich Ihre App im Hintergrund befindet. Wenn die App wieder geöffnet wird, werden alle bestehenden Hintergrundprozesse angehalten und stattdessen Vordergrundprozesse priorisiert.

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)

// Additional configuration customization...

// Enable background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = true

// Determines the number of meters required to trigger a new location update.
configuration.location.distanceFilter = 8000

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:brazeApiKey
                                    endpoint:brazeEndpoint];

// Additional configuration customization...

// Enable background geofence reporting with `When In Use` authorization.
configuration.location.allowBackgroundGeofenceUpdates = YES;

// Determines the number of meters required to trigger a new location update.
configuration.location.distanceFilter = 8000;

Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

{% alert important %}
Um Batterieverbrauch und Rate-Limiting zu vermeiden, konfigurieren Sie `distanceFilter` auf einen Wert, der den spezifischen Anforderungen Ihrer App entspricht. Wenn Sie `distanceFilter` auf einen höheren Wert einstellen, wird verhindert, dass Ihre App den Standort der Nutzer:innen zu häufig anfragt.
{% endalert %}

### Schritt 4: Autorisierung anfragen {#request-authorization}

Wenn Sie eine Autorisierung von Nutzer:innen anfordern, fragen Sie entweder die `When In Use`- oder die `Always`-Autorisierung an.

{% tabs local %}
{% tab When In Use %}
Um eine `When In Use`-Autorisierung anzufragen, verwenden Sie die Methode `requestWhenInUseAuthorization()`:

{% subtabs %}
{% subtab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestWhenInUseAuthorization()
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestWhenInUseAuthorization];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Always %}
Standardmäßig gewährt `requestAlwaysAuthorization()` Ihrer App nur die `When In Use`-Autorisierung und fordert Ihre Nutzer:innen nach einiger Zeit erneut zur `Always`-Autorisierung auf.

Sie können Ihre Nutzer:innen jedoch auch sofort auffordern, indem Sie zuerst `requestWhenInUseAuthorization()` und dann `requestAlwaysAuthorization()` aufrufen, nachdem Sie die erste `When In Use`-Autorisierung erhalten haben.

{% alert important %}
Sie können nur ein einziges Mal sofort eine `Always`-Autorisierung anfordern.
{% endalert %}

{% subtabs %}
{% subtab swift %}
```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```
{% endsubtab %}

{% subtab OBJECTIVE-C %}
```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Manuelle Anfrage für Geofences {#manually-request-geofences}

Wenn das Braze SDK Geofences vom Backend anfragt, meldet es den aktuellen Standort der Nutzer:innen und erhält Geofences, die auf der Grundlage des gemeldeten Standorts als optimal relevant eingestuft werden.

Um den Standort zu kontrollieren, den das SDK meldet, um die relevantesten Geofences zu erhalten, können Sie Geofences manuell anfragen, indem Sie die gewünschten Koordinaten angeben.

### Schritt 1: Setzen Sie `automaticGeofenceRequests` auf `false` {#step-1-set-automaticgeofencerequests-to-false}

Sie können automatische Geofence-Anfragen in Ihrem `configuration`-Objekt deaktivieren, das an [`init(configuration)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/init(configuration:)) übergeben wird. Setzen Sie `automaticGeofenceRequests` auf `false`.

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "{BRAZE_API_KEY}",
  endpoint: "{BRAZE_ENDPOINT}"
)
configuration.automaticGeofencesRequest = false
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
BRZConfiguration *configuration =
  [[BRZConfiguration alloc] initWithApiKey:{BRAZE_API_KEY}
                                  endpoint:{BRAZE_ENDPOINT}];
configuration.automaticGeofencesRequest = NO;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```

{% endtab %}
{% endtabs %}

### Schritt 2: Rufen Sie `requestGeofences` manuell auf {#step-2-call-requestgeofences-manually}

Fragen Sie in Ihrem Code Geofences mit dem entsprechenden Breiten- und Längengrad an.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.requestGeofences(latitude: latitude, longitude: longitude)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze requestGeofencesWithLatitude:latitude
                                      longitude:longitude];
```

{% endtab %}
{% endtabs %}

## Häufig gestellte Fragen (FAQ) {#faq}

### Warum erhalte ich keine Geofences auf meinem Gerät? {#why-am-i-not-receiving-geofences-on-my-device}

Um zu überprüfen, ob Geofences auf Ihrem Gerät empfangen werden, verwenden Sie zunächst den [SDK-Debugger]({{site.baseurl}}/developer_guide/sdk_integration/debugging), um die Protokolle des SDK zu prüfen. Sie können dann sehen, ob Geofences erfolgreich vom Server empfangen werden und ob es bemerkenswerte Fehler gibt.

Nachstehend finden Sie weitere mögliche Gründe, warum Geofences auf Ihrem Gerät nicht empfangen werden:

#### Einschränkungen des iOS-Betriebssystems {#ios-operating-system-limitations}

Das iOS-Betriebssystem erlaubt es nur, bis zu 20 Geofences für eine bestimmte App zu speichern. Wenn Geofences aktiviert sind, wird Braze einige dieser 20 verfügbaren Slots verwenden.

Um versehentliche oder unerwünschte Störungen anderer Geofence-Funktionen in Ihrer App zu vermeiden, müssen Sie Standort-Geofences für einzelne Apps im Dashboard aktivieren. Damit unsere Standortdienste korrekt funktionieren, überprüfen Sie, ob Ihre App nicht alle verfügbaren Geofence-Slots nutzt.

#### Rate-Limiting

Braze hat ein Limit von 1 Geofence-Aktualisierung pro Sitzung, um unnötige Anfragen zu vermeiden.

### Wie funktioniert es, wenn ich sowohl Braze- als auch Nicht-Braze-Geofence-Features verwende? {#how-does-it-work-if-i-am-using-both-braze-and-non-braze-geofence-features}

Wie bereits erwähnt, erlaubt iOS einer einzelnen App, maximal 20 Geofences zu speichern. Dieser Speicher wird sowohl von Braze- als auch von Nicht-Braze-Geofences gemeinsam genutzt und wird von [CLLocationManager](https://developer.apple.com/documentation/corelocation/cllocationmanager) verwaltet.

Wenn Ihre App beispielsweise 20 Nicht-Braze-Geofences enthält, wäre kein Speicherplatz verfügbar, um Braze-Geofences zu verfolgen (oder umgekehrt). Um neue Geofences zu erhalten, müssen Sie [die Standort-APIs von Apple](https://developer.apple.com/documentation/corelocation) verwenden, um die Überwachung einiger der bestehenden Geofences auf dem Gerät zu beenden.

### Kann das Geofences-Feature verwendet werden, wenn ein Gerät offline ist? {#can-the-geofences-feature-be-used-while-a-device-is-offline}

Ein Gerät muss nur dann mit dem Internet verbunden sein, wenn eine Aktualisierung erfolgt. Sobald es erfolgreich Geofences vom Server empfangen hat, ist es möglich, einen Geofence-Eintritt oder -Austritt zu protokollieren, selbst wenn das Gerät offline ist. Das liegt daran, dass der Standort eines Geräts unabhängig von seiner Internetverbindung funktioniert.

Nehmen wir an, ein Gerät hat zu Beginn der Sitzung erfolgreich Geofences empfangen und registriert und geht dann offline. Wenn es dann in einen dieser registrierten Geofences eintritt, kann es eine Braze-Campaign triggern.

### Warum werden Geofences nicht überwacht, wenn meine App im Hintergrund läuft oder beendet wird? {#why-are-geofences-not-monitored-when-my-app-is-backgroundedterminated}

Ohne `Always`-Autorisierung schränkt Apple die Ausführung von Standortdiensten ein, wenn eine App nicht benutzt wird. Dies wird durch das Betriebssystem erzwungen und liegt außerhalb der Kontrolle des Braze SDK. Braze bietet zwar separate Konfigurationen für die Ausführung von Diensten, während sich die App im Hintergrund befindet, aber es gibt keine Möglichkeit, diese Einschränkungen für Apps zu umgehen, die ohne ausdrückliche Genehmigung der Nutzer:innen beendet werden.