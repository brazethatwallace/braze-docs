## Apples Manifest zum Datenschutz {#privacy-manifest}

### Was sind Tracking-Daten? {#what-is-tracking-data}

Apple definiert „Tracking-Daten“ als Daten, die in Ihrer App über eine:n Endnutzer:in oder ein Gerät gesammelt werden und die mit Drittanbieter-Daten (z. B. gezielte Werbung) oder einem Datenbroker verknüpft sind. Eine vollständige Definition mit Beispielen finden Sie unter [Apple: Tracking](https://developer.apple.com/app-store/app-privacy-details/#user-tracking).

Standardmäßig sammelt das Braze SDK keine Tracking-Daten. Je nach Konfiguration Ihres Braze SDK müssen Sie jedoch möglicherweise Braze-spezifische Daten im Datenschutzmanifest Ihrer App aufführen.

### Was ist ein Datenschutzmanifest? {#what-is-a-privacy-manifest}

Ein Datenschutzmanifest ist eine Datei in Ihrem Xcode-Projekt, die den Grund für die Datenerfassung durch Ihre App und SDKs von Drittanbietern sowie deren Datenerfassungsmethoden beschreibt. Jedes Ihrer externen SDKs, das Daten trackt, benötigt ein eigenes Datenschutzmanifest. Wenn Sie [den Datenschutzbericht Ihrer App erstellen](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187), werden diese Datenschutzmanifestdateien automatisch in einem einzigen Bericht zusammengefasst.

### API-Tracking-Daten-Domains {#api-tracking-data-domains}

Ab iOS 17.2 blockiert Apple alle deklarierten Tracking-Endpunkte in Ihrer App, bis die:der Endnutzer:in eine [Aufforderung zur Ad-Tracking-Transparenz (ATT)](https://support.apple.com/en-us/HT212025) akzeptiert. Braze stellt Tracking-Endpunkte bereit, über die Sie Ihre Tracking-Daten weiterleiten können, während Sie First-Party-Daten, die nicht zum Tracking gehören, weiterhin an den ursprünglichen Endpunkt senden können.

## Tracking-Daten bei Braze deklarieren {#declaring-braze-tracking-data}

{% alert tip %}
Eine vollständige Anleitung finden Sie im [Privacy Tracking Data Tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/).
{% endalert %}

### Voraussetzungen {#prerequisites}

Für die Implementierung dieses Features ist die folgende Braze-SDK-Version erforderlich:

{% sdk_min_versions swift:9.0.0 %}

### Schritt 1: Aktuelle Richtlinien überprüfen {#step-1-review-your-current-policies}

Überprüfen Sie die aktuellen Datenerfassungsrichtlinien Ihres Braze SDK gemeinsam mit Ihrer Rechtsabteilung, um festzustellen, ob Ihre App Tracking-Daten [gemäß Apple-Definition](#what-is-tracking-data) erfasst. Wenn Sie keine Tracking-Daten erfassen, müssen Sie Ihr Datenschutzmanifest für das Braze SDK derzeit nicht anpassen. Weitere Informationen zu den Datenerfassungsrichtlinien des Braze SDK finden Sie unter [SDK-Datenerfassung]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection).

{% alert important %}
Wenn eines Ihrer nicht von Braze stammenden SDKs Tracking-Daten erfasst, müssen Sie diese Richtlinien separat überprüfen.
{% endalert %}

### Schritt 2: Datenschutzmanifest erstellen {#step-2-create-a-privacy-manifest}

Prüfen Sie zunächst, ob Sie bereits ein Datenschutzmanifest besitzen, indem Sie in Ihrem Xcode-Projekt nach der Datei `PrivacyInfo.xcprivacy` suchen. Wenn diese Datei bereits vorhanden ist, können Sie mit dem nächsten Schritt fortfahren. Andernfalls lesen Sie [Apple: Create a privacy manifest](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files).

### Schritt 3: Endpunkt zum Datenschutzmanifest hinzufügen {#step-3-add-your-endpoint-to-the-privacy-manifest}

Öffnen Sie in Ihrem Xcode-Projekt die Datei `PrivacyInfo.xcprivacy` Ihrer App, klicken Sie dann mit der rechten Maustaste auf die Tabelle und aktivieren Sie **Raw Keys and Values**.

{% alert note %}

{% endalert %}

![Ein Xcode-Projekt mit geöffnetem Kontextmenü und hervorgehobener Option „Raw Keys and Values“.]({% image_buster /assets/img/apple/privacy_manifest/check_raw_keys_and_values.png %})

Wählen Sie unter **App Privacy Configuration** die Option **NSPrivacyTracking** und setzen Sie den Wert auf **YES**.

![Die geöffnete Datei „PrivacyInfo.xcprivacy“ mit „NSPrivacyTracking“ auf „YES“ gesetzt.]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytracking.png %})

Wählen Sie unter **App Privacy Configuration** die Option **NSPrivacyTrackingDomains**. Fügen Sie im Domains-Array ein neues Element hinzu und setzen Sie dessen Wert auf den Endpunkt, den Sie [zuvor in Ihrem `AppDelegate` hinzugefügt haben]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration#update-your-app-delegate), mit dem Präfix `sdk-tracking`.

![Die geöffnete Datei „PrivacyInfo.xcprivacy“ mit einem Braze-Tracking-Endpunkt unter „NSPrivacyTrackingDomains“.]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytrackingdomains.png %})

### Schritt 4: Tracking-Daten deklarieren {#step-4-declare-your-tracking-data}

Öffnen Sie als Nächstes `AppDelegate.swift` und listen Sie jede [Tracking-Eigenschaft](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/) auf, die Sie deklarieren möchten, indem Sie eine statische oder dynamische Tracking-Liste erstellen. Beachten Sie, dass Apple diese Eigenschaften blockiert, bis die Endnutzer:innen die ATT-Aufforderung akzeptieren. Listen Sie daher nur die Eigenschaften auf, die Sie und Ihre Rechtsabteilung als Tracking-Daten betrachten. Beispiel:

{% tabs %}
{% tab Statisches Beispiel %}
Im folgenden Beispiel werden `dateOfBirth`, `customEvent` und `customAttribute` als Tracking-Daten in einer statischen Liste deklariert.

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
Im folgenden Beispiel wird die Tracking-Liste automatisch aktualisiert, nachdem die Endnutzer:innen die [App-Tracking-Transparenz-Aufforderung (ATT)](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/requesttrackingauthorization(completionhandler:)) akzeptiert haben. Die Autorisierungsanfrage bei der App-Aktivierung ist ein szenenspezifisches Ereignis. Dieser Code gehört daher in die `sceneDidBecomeActive(_:)`-Methode Ihrer `SceneDelegate.swift`-Datei und nicht in `applicationDidBecomeActive(_:)` von `AppDelegate.swift` (erforderlich für Apps, die den [`UIScene`-Lebenszyklus](https://developer.apple.com/documentation/technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle) übernommen haben). Ihre Braze-Instanz bleibt über die statische Eigenschaft `AppDelegate.braze` aus `SceneDelegate` erreichbar, die in Schritt 1 konfiguriert wurde.

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

### Schritt 5: Endlose Wiederholungsschleifen verhindern {#step-5-prevent-infinite-retry-loops}

Um zu verhindern, dass das SDK in eine endlose Wiederholungsschleife gerät, verwenden Sie die Methode `set(adTrackingEnabled: enableAdTracking)` zur Handhabung von ATT-Berechtigungen. Die Eigenschaft `adTrackingEnabled` in Ihrer `SceneDelegate.swift`-Methode sollte ähnlich wie folgt behandelt werden:

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

Um die Daten-Tracking-Aktivität im Swift SDK zu deaktivieren, setzen Sie die Eigenschaft [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) auf Ihrer Braze-Instanz auf `false`. Wenn `enabled` auf `false` gesetzt ist, ignoriert das Braze SDK alle Aufrufe der öffentlichen API. Das SDK bricht außerdem alle laufenden Aktionen ab, wie z. B. Netzwerkanfragen, Ereignisverarbeitung usw.

## Zuvor gespeicherte Daten löschen {#wiping-previously-stored-data}

Sie können die Methode [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) verwenden, um lokal gespeicherte SDK-Daten auf dem Gerät einer Nutzerin oder eines Nutzers vollständig zu löschen.

Ab Braze Swift Version 7.0.0 generieren das SDK und die Methode `wipeData()` eine zufällige UUID als Geräte-ID. Wenn jedoch `useUUIDAsDeviceId` auf `false` gesetzt ist _oder_ Sie Swift SDK Version 5.7.0 oder früher verwenden, müssen Sie zusätzlich eine POST-Anfrage an [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) senden, da der Identifier for Vendors (IDFV) automatisch als Geräte-ID dieser Nutzerin bzw. dieses Nutzers verwendet wird.

Wenn Sie die manuelle Push-Integration verwenden und Ihre App `wipeData()` aufruft und das SDK anschließend im selben App-Durchlauf wieder aktiviert, rufen Sie erneut `registerForRemoteNotifications()` auf, damit Braze ein aktualisiertes Geräte-Token / Textbaustein empfangen kann. Weitere Informationen finden Sie unter [Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Datenerfassung fortsetzen {#resuming-data-tracking}

Um die Datenerfassung fortzusetzen, setzen Sie [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) auf `true`. Beachten Sie, dass dadurch keine zuvor gelöschten Daten wiederhergestellt werden.

## Abmelden und Push-Registrierung aufheben {#logout-and-unregister-push}

Das Braze SDK stellt Methoden bereit, um ein Gerät nicht mehr anzusprechen, wenn Nutzer:innen sich von Push-Benachrichtigungen abmelden oder sich ausloggen. Diese Methoden entfernen die Push-Registrierungsdaten der aktuellen Nutzer:innen auf dem Braze-Server und im SDK, sodass Braze keine zukünftigen Push-Benachrichtigungs-Campaigns mehr an diese Nutzer:innen sendet.

### Abmelden {#logout}

Wenn sich Nutzer:innen aus einer Anwendung abmelden, rufen Sie die `logout`-Methode des SDK auf, um die Push-Registrierung des Geräts von den aktuellen Nutzer:innen zu entfernen und automatisch Bereinigungsaktionen im SDK durchzuführen. Die `logout`-Methode führt Folgendes aus:

- Hebt die Registrierung des Push-Tokens des Geräts und aller Push-to-Start-Tokens für Live Activities von den aktuellen Nutzer:innen auf dem Braze-Server auf.
- Wenn der Abmeldeaufruf erfolgreich ist, löscht das SDK lokal gespeicherte SDK-Daten und deaktiviert das SDK.
- Bei einem Fehler wird ein Fehler und ein `isRetriable`-Flag ausgelöst, damit die Integration entsprechende Maßnahmen ergreifen kann.

{% subtabs local %}
{% subtab Swift %}

Das folgende Completion-Handler-Beispiel zeigt die Erfolgs- und Fehlerbehandlung von `logout`. Verwenden Sie es für Callback-basierte Abläufe und ersetzen Sie das Logging durch die Wiederholungs- oder Neuauthentifizierungslogik Ihrer App.

```swift
// Completion handler
AppDelegate.braze?.logout { result in
  switch result {
  case .success:
    print("Logout successful")
  case .failure(let error):
    print("Logout failed: \(error.message), isRetriable: \(error.isRetriable)")
  }
}
```

Das folgende async-Beispiel zeigt die suspendierende `logout`-API. Verwenden Sie es für asynchrone Workflows und passen Sie die Erfolgs- und Fehlerzweige für Ihre App an.

```swift
// Async/await
do {
  try await AppDelegate.braze?.logout()
  print("Logout successful")
} catch let error as Braze.LogoutErrorResult {
  print("Logout failed: \(error.message), isRetriable: \(error.isRetriable)")
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Dieses Objective-C-Beispiel zeigt die Completion-basierte `logout`-Behandlung. Verwenden Sie es in Objective-C-Integrationen und ersetzen Sie das Logging durch Ihren App-Ablauf.

```objc
[AppDelegate.braze logoutWithCompletion:^(NSError * _Nullable error) {
  if (error) {
    NSNumber *isRetriable = error.userInfo[BRZLogoutErrorUserInfoKey.isRetriable];
    NSLog(@"Logout failed: %@, isRetriable=%@", error.localizedDescription, isRetriable);
  }
}];
```

{% endsubtab %}
{% endsubtabs local %}

{% alert note %}
`logout` beendet keine aktuell laufenden Live Activities. Beenden Sie im Erfolgs-Callback laufende Live Activities manuell mit der [`end(_:dismissalPolicy:)`](https://developer.apple.com/documentation/activitykit/activity/end(_:dismissalpolicy:))-Methode von ActivityKit.
{% endalert %}

#### Tracking und Push nach `logout` wieder aktivieren {#re-enable-tracking-and-push-after-logout}

Setzen Sie nach einem erfolgreichen `logout` [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) wieder auf `true` und Registrieren Sie sich dann erneut für Benachrichtigungen bei Ihrem Betriebssystem oder Push-Anbieter, indem Sie der [Swift-Push-Einrichtung]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) folgen.

#### Sofortige Abmeldeaufrufe vermeiden {#avoid-immediate-unregister-calls}

Vermeiden Sie es, `logout` oder `unregisterPush` direkt nach der Registrierung für Push-Benachrichtigungen beim Betriebssystem oder Push-Anbieter aufzurufen. Aufgrund der asynchronen Serververarbeitung kann dies in seltenen Fällen dazu führen, dass das Push-Token / Textbaustein erneut zu den Braze-Nutzer:innen hinzugefügt wird.

### Push-Registrierung aufheben {#unregister-push}

Um Push-Benachrichtigungen an ein Gerät zu stoppen, ohne zusätzliche automatische Bereinigung durchzuführen, verwenden Sie die Methode `unregisterPush`. Diese entfernt das Push-Token / Textbaustein des Geräts von den aktuellen Nutzer:innen auf dem Braze-Server und löscht das lokal gespeicherte Token / Textbaustein.

{% subtabs local %}
{% subtab Swift %}

Das folgende Completion-Handler-Beispiel zeigt die Erfolgs- und Fehlerbehandlung von `unregisterPush`. Verwenden Sie es für Callback-basierte Abläufe und ersetzen Sie das Logging durch Ihre eigene Wiederholungslogik.

```swift
// Completion handler
AppDelegate.braze?.notifications.unregisterPush { result in
  switch result {
  case .success:
    print("Push unregistered successfully")
  case .failure(let error):
    print("Push unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
  }
}
```

Das folgende async-Beispiel zeigt die suspendierende `unregisterPush`-API. Verwenden Sie es für asynchrone Workflows und passen Sie die Erfolgs- und Fehlerzweige für Ihre App an.

```swift
// Async/await
do {
  try await AppDelegate.braze?.notifications.unregisterPush()
  print("Push unregistered successfully")
} catch let error as Braze.PushUnregistrationError {
  print("Push unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Dieses Objective-C-Beispiel zeigt die Completion-basierte `unregisterPush`-Behandlung. Verwenden Sie es in Objective-C-Integrationen und ersetzen Sie das Logging durch Ihren App-Ablauf.

```objc
[AppDelegate.braze.notifications unregisterPushWithCompletion:^(NSError * _Nullable error) {
  if (error) {
    NSNumber *isRetriable = error.userInfo[BRZPushUnregistrationErrorUserInfoKey.isRetriable];
    NSNumber *statusCode = error.userInfo[BRZPushUnregistrationErrorUserInfoKey.httpStatusCode];
    NSLog(@"Push unregistration failed: %@, isRetriable=%@ status=%@",
          error.localizedDescription, isRetriable, statusCode);
  }
}];
```

{% endsubtab %}
{% endsubtabs local %}

#### Push nach `unregisterPush` erneut registrieren {#re-register-push-after-unregisterpush}

Registrieren Sie sich nach dem Aufruf von `unregisterPush` erneut für Benachrichtigungen bei Ihrem Betriebssystem oder Push-Anbieter, indem Sie der [Swift-Push-Einrichtung]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) folgen, bevor Sie erneut Braze-Push-Benachrichtigungen senden.

#### Sofortige Abmeldeaufrufe vermeiden

Vermeiden Sie es, `logout` oder `unregisterPush` direkt nach der Registrierung für Push-Benachrichtigungen beim Betriebssystem oder Push-Anbieter aufzurufen. Aufgrund der asynchronen Serververarbeitung kann dies in seltenen Fällen dazu führen, dass das Push-Token / Textbaustein erneut zu den Braze-Nutzer:innen hinzugefügt wird.

### Push-to-Start-Tokens für Live Activities abmelden {#unregister-push-to-start}

Live Activities können mit Push-to-Start-Tokens remote gestartet werden. Um zu verhindern, dass Braze Live Activities auf einem Gerät remote startet, rufen Sie die Methode `unregisterPushToStart` auf, um alle aktuell registrierten Typen (Standard) oder eine bestimmte Liste von Activity-Typen abzumelden.

Beachten Sie, dass aktuell laufende Live Activities weiterhin Updates erhalten und diese Methode nur die Möglichkeit entfernt, neue Activities remote zu starten. Weitere Informationen zu Live Activities finden Sie unter [Live Activities]({{site.baseurl}}/developer_guide/live_notifications/live_activities).

#### Laufende Live Activities beenden {#end-any-running-live-activities}

`unregisterPushToStart` beendet keine aktuell laufenden Live Activities. Beenden Sie im Erfolgs-Callback laufende Live Activities manuell mit der [`end(_:dismissalPolicy:)`](https://developer.apple.com/documentation/activitykit/activity/end(_:dismissalpolicy:))-Methode von ActivityKit.

{% alert note %}
Vermeiden Sie es, `logout` oder `unregisterPushToStart` direkt nach dem Aufruf von `registerPushToStart` für eine Live Activity aufzurufen. Aufgrund der asynchronen Serververarbeitung kann dies in seltenen Fällen dazu führen, dass das Push-to-Start-Token / Textbaustein erneut zu den Braze-Nutzer:innen hinzugefügt wird.
{% endalert %}

Das folgende Beispiel zeigt, wie Sie alle Push-to-Start-Activity-Typen abmelden. Verwenden Sie es, wenn abgemeldete Nutzer:innen keine neuen remote gestarteten Live Activities mehr erhalten sollen.

```swift
// Unregister all currently-registered activity types
// Completion handler
AppDelegate.braze?.liveActivities.unregisterPushToStart { result in
  switch result {
  case .success:
    print("Push-to-start unregistered successfully")
  case .failure(let error):
    print("Push-to-start unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
  }
}

// Async/await
do {
  try await AppDelegate.braze?.liveActivities.unregisterPushToStart()
  print("Push-to-start unregistered successfully")
} catch let error as Braze.PushUnregistrationError {
  print("Push-to-start unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
}
```

Das folgende Beispiel zeigt, wie Sie bestimmte Activity-Typen abmelden. Verwenden Sie es, wenn nur ausgewählte Live Activities nicht mehr remote gestartet werden sollen.

```swift
// Unregister specific activity types
AppDelegate.braze?.liveActivities.unregisterPushToStart(types: ["ActivityType1", "ActivityType2"]) { result in
  switch result {
  case .success:
    print("Push-to-start unregistered successfully")
  case .failure(let error):
    print("Push-to-start unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
  }
}
```

{% alert note %}
`unregisterPushToStart` verfügt über keine Objective-C-API, da Live Activities auf reine Swift-Typen angewiesen sind.
{% endalert %}

## IDFV-Erfassung {#idfv-collection}

In früheren Versionen des Braze iOS SDK wurde das IDFV-Feld (Identifier for Vendors) automatisch als Geräte-ID der Nutzer:innen erfasst. Ab Swift SDK `v5.7.0` konnte das IDFV-Feld optional deaktiviert werden, und Braze setzte stattdessen eine zufällige UUID als Geräte-ID. Ab Swift SDK `v7.0.0` wird das IDFV-Feld standardmäßig nicht mehr erfasst, und stattdessen wird eine UUID als Geräte-ID gesetzt.

Das Feature `useUUIDAsDeviceId` konfiguriert das [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) so, dass die Geräte-ID als UUID gesetzt wird. Traditionell hat das iOS SDK die Geräte-ID gleich dem von Apple generierten IDFV-Wert gesetzt. Wenn dieses Feature standardmäßig in Ihrer iOS-App aktiviert ist, wird allen neuen Nutzer:innen, die über das SDK erstellt werden, eine UUID als Geräte-ID zugewiesen.

Wenn Sie das IDFV weiterhin separat erfassen möchten, können Sie [`set(identifierforvendor:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)) verwenden.

{% alert note %}
Apple ist für die Erstellung von IDFV verantwortlich, und IDFV wird von Apple verwaltet. Braze transformiert oder verändert IDFVs nicht, und Apple gibt keine Garantien hinsichtlich Groß-/Kleinschreibung oder Format.
{% endalert %}

{% alert note %}
Das Lesen von `braze.deviceId` blockiert den aufrufenden Thread, bis das SDK seine Operationen nach der Initialisierung abgeschlossen hat. Verwenden Sie für den Haupt-Thread oder latenzsensitive Kontexte stattdessen die nicht-blockierenden Alternativen.

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

### Hinweise {#considerations}

#### SDK-Version

Wenn in Swift SDK `v7.0.0+` `useUUIDAsDeviceId` aktiviert ist (Standard), wird allen neu erstellten Nutzer:innen eine zufällige Geräte-ID zugewiesen. Alle bereits vorhandenen Nutzer:innen behalten ihren bestehenden Geräte-ID-Wert bei, der möglicherweise ein IDFV war.

Wenn dieses Feature nicht aktiviert ist, wird Geräten bei der Erstellung weiterhin ein IDFV zugewiesen.

#### Nachgelagerte Auswirkungen {#downstream}

**Technologie-Partner**: Wenn dieses Feature aktiviert ist, haben Technologie-Partner, die den IDFV-Wert aus der Braze-Geräte-ID ableiten, keinen Zugriff mehr auf diese Daten. Falls der vom Gerät abgeleitete IDFV-Wert für Ihre Partnerintegration benötigt wird, empfehlen wir, dieses Feature auf `false` zu setzen.

**Currents**: Wenn `useUUIDAsDeviceId` auf „true“ gesetzt ist, entspricht die in Currents gesendete Geräte-ID nicht mehr dem IDFV-Wert.

### Häufig gestellte Fragen {#frequently-asked-questions}

#### Wirkt sich diese Änderung auf meine bestehenden Nutzer:innen in Braze aus? {#will-this-change-impact-my-existing-users-in-braze}

Nein. Wenn dieses Feature aktiviert ist, werden keine bestehenden Nutzerdaten in Braze überschrieben. Neue UUID-Geräte-IDs werden nur für neue Geräte erstellt oder wenn `wipedata()` aufgerufen wird.

#### Kann ich dieses Feature nach der Aktivierung wieder deaktivieren? {#can-i-turn-this-feature-off-after-turning-it-on}

Ja, dieses Feature kann nach eigenem Ermessen aktiviert und deaktiviert werden. Zuvor gespeicherte Geräte-IDs werden niemals überschrieben.

#### Kann ich den IDFV-Wert an anderer Stelle über Braze erfassen? {#can-i-still-capture-the-idfv-value-through-braze-elsewhere}

Ja, Sie können das IDFV weiterhin optional über das Swift SDK erfassen (die Erfassung ist standardmäßig deaktiviert).