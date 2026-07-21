## Apples Manifest zum Datenschutz {#privacy-manifest}

### Was sind Tracking-Daten? {#what-is-tracking-data}

Apple definiert „Tracking-Daten“ als Daten, die in Ihrer App über eine:n Endnutzer:in oder ein Gerät gesammelt werden und die mit Drittanbieter-Daten (z. B. gezielte Werbung) oder einem Datenbroker verknüpft sind. Eine vollständige Definition mit Beispielen finden Sie unter [Apple: Tracking](https://developer.apple.com/app-store/app-privacy-details/#user-tracking).

Standardmäßig sammelt das Braze SDK keine Tracking-Daten. Je nach Konfiguration Ihres Braze SDK müssen Sie jedoch möglicherweise Braze-spezifische Daten im Datenschutzmanifest Ihrer App aufführen.

### Was ist ein Datenschutzmanifest? {#what-is-a-privacy-manifest}

Ein Datenschutzmanifest ist eine Datei in Ihrem Xcode-Projekt, die den Grund für die Datenerfassung durch Ihre App und SDKs von Drittanbietern sowie deren Datenerfassungsmethoden beschreibt. Jedes Ihrer externen SDKs, das Daten trackt, benötigt ein eigenes Datenschutzmanifest. Wenn Sie [den Datenschutzbericht Ihrer App erstellen](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187), werden diese Datenschutzmanifestdateien automatisch in einem einzigen Bericht zusammengefasst.

### API-Tracking-Daten-Domains {#api-tracking-data-domains}

Ab iOS 17.2 blockiert Apple alle deklarierten Tracking-Endpunkte in Ihrer App, bis die:der Endnutzer:in eine [Aufforderung zur Ad-Tracking-Transparenz (ATT)](https://support.apple.com/en-us/HT212025) akzeptiert. Braze stellt Tracking-Endpunkte bereit, über die Sie Ihre Tracking-Daten weiterleiten können, während Sie First-Party-Daten, die nicht zum Tracking gehören, weiterhin an den ursprünglichen Endpunkt senden können.

## Deklarieren der Tracking-Daten von Braze {#declaring-braze-tracking-data}

{% alert tip %}
Eine vollständige Anleitung finden Sie im [Tutorial zum Datenschutz-Tracking](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/).
{% endalert %}

### Voraussetzungen {#prerequisites}

Die folgende Braze-SDK-Version ist erforderlich, um dieses Feature zu implementieren:

{% sdk_min_versions swift:9.0.0 %}

### Schritt 1: Überprüfen Sie Ihre aktuellen Richtlinien {#step-1-review-your-current-policies}

Lassen Sie die aktuellen Datenerfassungsrichtlinien Ihres Braze SDK von Ihrer Rechtsabteilung prüfen, um festzustellen, ob Ihre App Tracking-Daten [gemäß der Definition von Apple](#what-is-tracking-data) erfasst. Wenn Sie keine Tracking-Daten sammeln, müssen Sie Ihr Datenschutzmanifest für das Braze SDK zu diesem Zeitpunkt nicht anpassen. Weitere Informationen zu den Datenerfassungsrichtlinien des Braze SDK finden Sie unter [Datenerfassung im SDK]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection).

{% alert important %}
Wenn eines Ihrer SDKs, das nicht von Braze stammt, Tracking-Daten sammelt, müssen Sie diese Richtlinien separat prüfen.
{% endalert %}

### Schritt 2: Erstellen Sie ein Datenschutzmanifest {#step-2-create-a-privacy-manifest}

Prüfen Sie zunächst, ob Sie bereits ein Datenschutzmanifest haben, indem Sie in Ihrem Xcode-Projekt nach einer `PrivacyInfo.xcprivacy`-Datei suchen. Wenn Sie diese Datei bereits haben, können Sie mit dem nächsten Schritt fortfahren. Andernfalls siehe [Apple: Datenschutzmanifest erstellen](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files).

### Schritt 3: Fügen Sie Ihren Endpunkt zum Datenschutzmanifest hinzu {#step-3-add-your-endpoint-to-the-privacy-manifest}

Öffnen Sie in Ihrem Xcode-Projekt die Datei `PrivacyInfo.xcprivacy` Ihrer App, rechtsklicken Sie dann auf die Tabelle und aktivieren Sie **Raw Keys and Values**.

{% alert note %}

{% endalert %}

![Ein Xcode-Projekt mit geöffnetem Kontextmenü und hervorgehobener Option „Raw Keys and Values“.]({% image_buster /assets/img/apple/privacy_manifest/check_raw_keys_and_values.png %})

Wählen Sie unter **App Privacy Configuration** den Eintrag **NSPrivacyTracking** und setzen Sie den Wert auf **YES**.

![Die geöffnete Datei „PrivacyInfo.xcprivacy“ mit „NSPrivacyTracking“ auf „YES“ gesetzt.]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytracking.png %})

Wählen Sie unter **App Privacy Configuration** den Eintrag **NSPrivacyTrackingDomains**. Fügen Sie im Domains-Array ein neues Element hinzu und setzen Sie dessen Wert auf den Endpunkt, den Sie [zuvor zu Ihrem `AppDelegate` hinzugefügt haben]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration#update-your-app-delegate), mit dem Präfix `sdk-tracking`.

![Die geöffnete Datei „PrivacyInfo.xcprivacy“ mit einem Braze-Tracking-Endpunkt unter „NSPrivacyTrackingDomains“.]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytrackingdomains.png %})

### Schritt 4: Deklarieren Sie Ihre Tracking-Daten {#step-4-declare-your-tracking-data}

Öffnen Sie als Nächstes `AppDelegate.swift` und listen Sie alle [Tracking-Eigenschaften](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/) auf, die Sie deklarieren möchten, indem Sie eine statische oder dynamische Tracking-Liste erstellen. Beachten Sie, dass Apple diese Eigenschaften blockiert, bis die:der Endnutzer:in die ATT-Aufforderung akzeptiert. Listen Sie daher nur die Eigenschaften auf, die Sie und Ihre Rechtsabteilung als Tracking betrachten. Zum Beispiel:

{% tabs %}
{% tab Statisches Beispiel %}
Im folgenden Beispiel werden `dateOfBirth`, `customEvent` und `customAttribute` als Tracking-Daten innerhalb einer statischen Liste deklariert.

```swift
import UIKit
import BrazeKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let configuration = Braze.Configuration(apiKey: brazeApiKey, endpoint: brazeEndpoint)
    // Declare which types of data you wish to collect for user tracking.
    configuration.api.trackingPropertyAllowList = [
      .dateOfBirth,
      .customEvent(["event-1"]),
      .customAttribute(["attribute-1", "attribute-2"])
    ]
    let braze = Braze(configuration: configuration)
    AppDelegate.braze = braze
    return true
  }
}
```
{% endtab %}

{% tab Dynamisches Beispiel %}
Im folgenden Beispiel wird die Tracking-Liste automatisch aktualisiert, nachdem die:der Endnutzer:in die [App-Tracking-Transparenz-Aufforderung (ATT)](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/requesttrackingauthorization(completionhandler:)) akzeptiert hat. Die Autorisierungsanfrage bei App-Aktivierung ist ein szenenspezifisches Ereignis, daher gehört dieser Code in die Methode `sceneDidBecomeActive(_:)` Ihrer `SceneDelegate.swift`-Datei und nicht in `applicationDidBecomeActive(_:)` von `AppDelegate.swift` (erforderlich für Apps, die den [`UIScene`-Lebenszyklus](https://developer.apple.com/documentation/technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle) übernommen haben). Ihre Braze-Instanz bleibt über die statische Eigenschaft `AppDelegate.braze`, die in Schritt 1 konfiguriert wurde, aus `SceneDelegate` erreichbar.

```swift
func sceneDidBecomeActive(_ scene: UIScene) {
  // Request and check your user's tracking authorization status.
  ATTrackingManager.requestTrackingAuthorization { status in
    // Let Braze know whether user data is allowed to be collected for tracking.
    let enableAdTracking = status == .authorized
    AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)

    // Add the `.firstName` and `.lastName` properties, while removing the `.everything` configuration.
    AppDelegate.braze?.updateTrackingAllowList(
      adding: [.firstName, .lastName],
      removing: [.everything]
    )
  }
}
```
{% endtab %}
{% endtabs %}

### Schritt 5: Verhindern Sie unendliche Wiederholungsschleifen {#step-5-prevent-infinite-retry-loops}

Um zu verhindern, dass das SDK in eine unendliche Wiederholungsschleife gerät, verwenden Sie die Methode `set(adTrackingEnabled: enableAdTracking)` zur Behandlung von ATT-Berechtigungen. Die Eigenschaft `adTrackingEnabled` in Ihrer `SceneDelegate.swift`-Methode sollte ähnlich wie folgt behandelt werden:

```swift
func sceneDidBecomeActive(_ scene: UIScene) {
    // Request and check your user's tracking authorization status.
    ATTrackingManager.requestTrackingAuthorization { status in
      // Let Braze know whether user data is allowed to be collected for tracking.
      let enableAdTracking = status == .authorized
      AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)
    }
}
```

## Deaktivieren des Daten-Trackings {#disabling-data-tracking}

Um die Daten-Tracking-Aktivität im Swift SDK zu deaktivieren, setzen Sie die Eigenschaft [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) in Ihrer Braze-Instanz auf `false`. Wenn `enabled` auf `false` gesetzt ist, ignoriert das Braze SDK alle Aufrufe an die öffentliche API. Das SDK bricht außerdem alle laufenden Aktionen ab, z. B. Netzwerkanfragen, Eventverarbeitung usw.

## Löschen zuvor gespeicherter Daten {#wiping-previously-stored-data}

Sie können die Methode [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) verwenden, um lokal gespeicherte SDK-Daten auf dem Gerät einer:eines Nutzer:in vollständig zu löschen.

Ab Braze Swift Version 7.0.0 generieren das SDK und die Methode `wipeData()` eine zufällige UUID als Geräte-ID. Wenn Ihr `useUUIDAsDeviceId` jedoch auf `false` gesetzt ist _oder_ Sie Swift SDK Version 5.7.0 oder früher verwenden, müssen Sie zusätzlich eine POST-Anfrage an [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) senden, da Ihr Identifier for Vendors (IDFV) automatisch als Geräte-ID der:des Nutzer:in verwendet wird.

Wenn Sie die manuelle Push-Integration verwenden und Ihre App `wipeData()` aufruft und das SDK später im selben App-Lauf wieder aktiviert, rufen Sie erneut `registerForRemoteNotifications()` auf, damit Braze ein aktualisiertes Geräte-Token erhalten kann. Weitere Informationen finden Sie unter [Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Wiederaufnahme des Daten-Trackings {#resuming-data-tracking}

Um die Datenerfassung wieder aufzunehmen, setzen Sie [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) auf `true`. Beachten Sie, dass dadurch keine zuvor gelöschten Daten wiederhergestellt werden.

## IDFV-Erfassung {#idfv-collection}

In früheren Versionen des Braze iOS SDK wurde das IDFV-Feld (Identifier for Vendors) automatisch als Geräte-ID der:des Nutzer:in erfasst. Ab Swift SDK `v5.7.0` konnte das IDFV-Feld optional deaktiviert werden, und Braze setzte stattdessen eine zufällige UUID als Geräte-ID. Ab Swift SDK `v7.0.0` wird das IDFV-Feld standardmäßig nicht mehr erfasst, und stattdessen wird eine UUID als Geräte-ID festgelegt.

Das Feature `useUUIDAsDeviceId` konfiguriert das [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) so, dass die Geräte-ID als UUID gesetzt wird. Traditionell wies das iOS SDK den von Apple generierten IDFV-Wert als Geräte-ID zu. Wenn dieses Feature in Ihrer iOS-App standardmäßig aktiviert ist, wird allen neuen Nutzer:innen, die über das SDK erstellt werden, eine Geräte-ID zugewiesen, die einer UUID entspricht.

Wenn Sie den IDFV dennoch separat erfassen möchten, können Sie [`set(identifierforvendor:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)) verwenden.

{% alert note %}
Das Lesen von `braze.deviceId` blockiert den aufrufenden Thread, bis das SDK seine Initialisierungsvorgänge abgeschlossen hat. Verwenden Sie für den Haupt-Thread oder latenzempfindliche Kontexte stattdessen die nicht-blockierenden Alternativen.

{% subtabs local %}
{% subtab Swift %}
```swift
// Completion handler — always delivers on the main thread.
AppDelegate.braze?.getDeviceId { deviceId in
  print("Device ID:", deviceId)
}

// Async/await (iOS 13.0+, tvOS 13.0+, watchOS 6.0+, macOS 10.15+)
let deviceId = await AppDelegate.braze?.getDeviceId()
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// Completion handler — always delivers on the main thread.
[AppDelegate.braze getDeviceIdWithCompletion:^(NSString *deviceId) {
  NSLog(@"Device ID: %@", deviceId);
}];
```
{% endsubtab %}
{% endsubtabs local %}
{% endalert %}

### Überlegungen {#considerations}

#### SDK-Version

Wenn `useUUIDAsDeviceId` im Swift SDK `v7.0.0+` aktiviert ist (Standard), wird allen neu erstellten Nutzer:innen eine zufällige Geräte-ID zugewiesen. Alle bereits bestehenden Nutzer:innen behalten ihren bisherigen Geräte-ID-Wert bei, der möglicherweise der IDFV war.

Wenn dieses Feature nicht aktiviert ist, wird Geräten bei der Erstellung weiterhin der IDFV zugewiesen.

#### Downstream

**Technologie-Partner**: Wenn dieses Feature aktiviert ist, haben alle Technologie-Partner, die den IDFV-Wert von der Braze-Geräte-ID ableiten, keinen Zugriff mehr auf diese Daten. Wenn der vom Gerät abgeleitete IDFV-Wert für Ihre Partnerintegration benötigt wird, empfehlen wir Ihnen, dieses Feature auf `false` zu setzen.

**Currents**: Wenn `useUUIDAsDeviceId` auf `true` gesetzt ist, entspricht die in Currents gesendete Geräte-ID nicht mehr dem IDFV-Wert.

### Häufig gestellte Fragen {#frequently-asked-questions}

#### Wird sich diese Änderung auf meine bestehenden Nutzer:innen in Braze auswirken? {#will-this-change-impact-my-existing-users-in-braze}

Nein. Wenn dieses Feature aktiviert ist, werden keine Nutzerdaten in Braze überschrieben. Neue UUID-Geräte-IDs werden nur für neue Geräte erstellt oder wenn `wipedata()` aufgerufen wird.

#### Kann ich dieses Feature ausschalten, nachdem ich es eingeschaltet habe? {#can-i-turn-this-feature-off-after-turning-it-on}

Ja, dieses Feature kann nach Ihrem Ermessen ein- und ausgeschaltet werden. Zuvor gespeicherte Geräte-IDs werden niemals überschrieben.

#### Kann ich den IDFV-Wert auch anderweitig über Braze erfassen? {#can-i-still-capture-the-idfv-value-through-braze-elsewhere}

Ja, Sie können den IDFV weiterhin optional über das Swift SDK erfassen (die Erfassung ist standardmäßig deaktiviert).