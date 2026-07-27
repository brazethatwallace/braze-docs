---
nav_title: React Native SDK
article_title: React Native SDK Repository-Leitfaden
page_order: 7
description: "Braze React Native SDK README-Referenz, gespiegelt von GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# React Native SDK Repository-Leitfaden

## Über das Braze React Native SDK

Das Braze React Native SDK verbindet Ihre iOS- und Android-Apps mit Braze: Nutzerprofile, Messaging-Oberflächen, Analytics und Feature-Flags. Es umschließt das native [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk) und das [Braze Android SDK](https://github.com/braze-inc/braze-android-sdk) hinter einer JavaScript-API.

**Die Initialisierung erfolgt über JavaScript:** Sie richten die native Konfiguration (Push, Logging, Delegates) in Android-Ressourcen und iOS `AppDelegate` ein und rufen dann `Braze.initialize(apiKey, endpoint)` aus JavaScript auf, um das SDK zu starten. So haben Sie die volle Kontrolle darüber, wann das SDK initialisiert wird und mit welchen Zugangsdaten. Nach der Initialisierung rufen Sie bei Bedarf weitere SDK-Methoden auf (zum Beispiel `changeUser`, `logCustomEvent`).

### Was Sie tun können

- **Nutzerverwaltung**: Nutzer:innen identifizieren, Profilfelder, angepasste Attribute, Aliase und Abo-Gruppen festlegen
- **In-App-Nachrichten**: Standard-Braze-UI oder benutzerdefinierte Verarbeitung über Subscriptions und Logging-APIs
- **Content Cards**: Standard-Feed-UI oder Karten abrufen und eine eigene UI erstellen
- **Banner**: Platzierungsbasierte HTML-Banner, einschließlich `BrazeBannerView`
- **Push-Benachrichtigungen**: Berechtigungsabfragen, Token-Registrierung, Payload-Listener (siehe Plattformhinweise unten)
- **Feature-Flags**: Aktualisieren, Eigenschaften lesen, Impressionen protokollieren
- **Analytics**: Angepasste Events, Käufe, sofortiges Flushen
- **SDK-Steuerung**: SDK aktivieren/deaktivieren, lokale Daten löschen, SDK-Authentication-Signaturen

## Voraussetzungen

- **Braze-Konto** mit App-API-Schlüssel und SDK-Endpunkt
- **React Native**-Entwicklungsumgebung ([React Native-Umgebungseinrichtung](https://reactnative.dev/docs/set-up-your-environment))
- **iOS**: Xcode, CocoaPods (`cd ios && pod install`)
- **Android**: Android Studio / Gradle; Kotlin-Gradle-Plugin, wie von Ihrem React Native-Template benötigt
- **Push** (falls verwendet): FCM (Android) und APNs (iOS) gemäß der [Push-Dokumentation](https://www.braze.com/docs/developer_guide/platform_integration_guides/react_native/push_notifications/) einrichten

Informationen zu den Zugangsdaten im Dashboard finden Sie in der [Integrationsübersicht](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native).

## Installation

``` bash
npm install @braze/react-native-sdk
# or:
# yarn add @braze/react-native-sdk
```

---

## Schnellstart

Dieser Abschnitt zeigt die minimale Einrichtung, die erforderlich ist, um das Braze React Native SDK zu initialisieren.

1. Installieren Sie das npm-Paket (siehe oben).
2. Schließen Sie die **native Einrichtung** für Android und iOS ab (Konfiguration, Berechtigungen, Push falls erforderlich).
3. Initialisieren Sie das SDK über JavaScript und beginnen Sie mit der Nutzung:

``` typescript
import Braze from "@braze/react-native-sdk";

// Initialize the SDK — call early in your app lifecycle (e.g. in a useEffect).
// The API key and endpoint are passed from JavaScript; native configuration
// (push, logging, etc.) is applied automatically from your native setup.
Braze.initialize("<YOUR_API_KEY>", "<YOUR_SDK_ENDPOINT>");

Braze.changeUser("user-123");
Braze.logCustomEvent("button_clicked", { screen: "home" });
```

TypeScript-Typisierungen werden mit dem Paket ausgeliefert (`src/index.d.ts` auf GitHub).

Ein erneuter Aufruf von `Braze.initialize` mit anderen Zugangsdaten beendet die aktuelle Instanz und erstellt sie neu, wodurch eine Re-Initialisierung während der Sitzung unterstützt wird.

---

## Native Einrichtung

> **Maßgebliche Quelle:** Schritt-für-Schritt-Anleitungen, Gradle-/CocoaPods-Änderungen und die vollständige Liste der Android-XML-Schlüssel finden Sie im [Braze React Native-Entwicklerleitfaden](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native). Die folgenden Snippets sind minimale Beispiele.

### Android

- Fügen Sie das **Kotlin-Gradle-Plugin** in Ihrer Root-`build.gradle` hinzu, falls Ihr Template es noch nicht enthält (die Versionen hängen von Ihrer React Native-Version ab).
- Fügen Sie eine `braze.xml`-Ressourcendatei in `res/values` mit Ihrer Konfiguration hinzu. Aktivieren Sie die verzögerte Initialisierung, damit das SDK auf `Braze.initialize()` aus JavaScript wartet, bevor es startet. Andere Konfigurationswerte (Push, Sitzungs-Timeout usw.) werden weiterhin aus dieser Datei gelesen und zum Zeitpunkt der Initialisierung angewendet.
- Stellen Sie sicher, dass grundlegende Berechtigungen wie `INTERNET` und `ACCESS_NETWORK_STATE` in `AndroidManifest.xml` vorhanden sind.
- Für Push schließen Sie die FCM-Integration und alle Braze-spezifischen Sender-ID-/Registrierungs-Flags ab, die in der Dokumentation beschrieben sind.

``` xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <!-- Enable delayed initialization so the SDK starts when
       Braze.initialize() is called from JavaScript. -->
  <bool name="com_braze_enable_delayed_initialization">true</bool>

  <!-- Additional native configuration (applied at initialization time) -->
  <bool name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
  <string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">YOUR_SENDER_ID</string>
</resources>
```

{% alert note %}
** Der API-Schlüssel und der Endpunkt werden nicht mehr in `braze.xml` festgelegt – sie werden über `Braze.initialize(apiKey, endpoint)` aus JavaScript übergeben.
{% endalert %}
### iOS

``` bash
cd ios && pod install
```

Verwenden Sie `BrazeReactInitializer.configure` in Ihrem `AppDelegate`, um die native Konfiguration zu registrieren. Die von Ihnen bereitgestellten Closures werden gespeichert und später angewendet, wenn `Braze.initialize(apiKey, endpoint)` aus JavaScript aufgerufen wird.

``` swift
import BrazeKit
import braze_react_native_sdk

@main
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
  ) -> Bool {
    // Register native configuration for when JS calls Braze.initialize().
    BrazeReactInitializer.configure { config in
      config.logger.level = .info
      config.push.automation = true
    } postInitialization: { braze in
      AppDelegate.braze = braze
    }

    // ... React Native setup
    return true
  }
}
```

- **`configure`-Closure**: Empfängt eine `Braze.Configuration` und ermöglicht es Ihnen, native Konfigurationseigenschaften festzulegen (Logging, Push, Sitzungen usw.). Der API-Schlüssel und der Endpunkt werden aus JavaScript bereitgestellt – Sie legen sie hier nicht fest.
- **`postInitialization`-Closure** *(optional)*: Empfängt die aktive `Braze`-Instanz nach der Erstellung, für Einrichtungsschritte, die die Instanz erfordern (z. B. Speichern einer Referenz, Festlegen von Delegates).

{% alert note %}
** `BrazeReactInitializer.configure` ist eine Swift-first-API, die das veraltete `BrazeReactBridge.initBraze(_:)` ersetzt. Sie löst außerdem ein Swift-Typauflösungsproblem mit `Braze.Configuration` in der Objective-C-Bridge.
{% endalert %}
---

## Konfigurationsreferenz

In React Native ist die **Konfiguration nativ**: Android liest `res/values/braze.xml`, und iOS verwendet Closures, die über **`BrazeReactInitializer.configure`** registriert werden. Beide werden angewendet, wenn `Braze.initialize(apiKey, endpoint)` aus JavaScript aufgerufen wird.

### Android (`braze.xml`)

Standardwerte befinden sich in XML; [`BrazeConfig.Builder`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) kann sie beim Start überschreiben. Die vollständige Liste der Schlüssel und Typen finden Sie im [Android-SDK-Integrationsleitfaden](https://www.braze.com/docs/developer_guide/platforms/android/sdk_integration/) und in [`BrazeConfigurationProvider`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/index.html) (jede Kotlin-Eigenschaft entspricht dokumentierten `com_braze_*`-Ressourcen).

Häufig verwendete Einträge:

| Schlüssel | Ressourcentyp | Beschreibung |
|-----|---------------|-------------|
| `com_braze_enable_delayed_initialization` | `bool` | **Erforderlich.** Auf `true` setzen, damit das SDK auf `Braze.initialize()` aus JavaScript wartet. |
| `com_braze_api_key` | `string` | Nicht erforderlich bei Verwendung von `Braze.initialize()` aus JavaScript (Zugangsdaten werden aus JS übergeben). Nur für die ältere native-first-Initialisierung erforderlich. |
| `com_braze_custom_endpoint` | `string` | Nicht erforderlich bei Verwendung von `Braze.initialize()` aus JavaScript. Nur für die ältere native-first-Initialisierung erforderlich. |
| `com_braze_server_target` | `string` | Optionaler Cluster-/Umgebungsselektor (z. B. für interne oder Staging-Builds). Bevorzugen Sie `com_braze_custom_endpoint` für die Produktion, sofern Ihre Braze-Integration nichts anderes vorgibt. |
| `com_braze_firebase_cloud_messaging_registration_enabled` | `bool` | Wenn `true`, registriert sich Braze für FCM (typisches Push-Setup). |
| `com_braze_firebase_cloud_messaging_sender_id` | `string` | FCM-Sender-ID bei aktivierter automatischer Registrierung. |
| `com_braze_handle_push_deep_links_automatically` | `bool` | Braze öffnet Push-Deeplinks automatisch. |
| `com_braze_trigger_action_minimum_time_interval_seconds` | `integer` | Mindestanzahl an Sekunden zwischen In-App-Nachricht-Trigger-Aktionen. |
| **Sonstige** | *verschiedene* | Weitere hier nicht aufgeführte Schlüssel (Session-Timeout, Geofences, Standort, Benachrichtigungsstandards, Geräte-Allowlists, verzögerte Initialisierung, SDK-Authentifizierung und mehr). Siehe [`BrazeConfigurationProvider`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/index.html) und den [Android-SDK-Integrationsleitfaden](https://www.braze.com/docs/developer_guide/platforms/android/sdk_integration/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Android (braze.xml)" }

### iOS (`Braze.Configuration`)

Setzen Sie native Konfigurationseigenschaften in der `configure`-Closure, die an `BrazeReactInitializer.configure` übergeben wird. Die Closure erhält eine `Braze.Configuration`-Instanz – der API-Schlüssel und der Endpunkt werden automatisch aus dem JavaScript-Aufruf `Braze.initialize` gesetzt. Vollständige Details: [`Braze.Configuration`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class) und die verschachtelten Typen **`api`**, **`push`**, **`logger`**, **`location`**.

| Bereich | Mitglieder (repräsentativ) | Hinweise |
|------|--------------------------|--------|
| **Zugangsdaten** | `api.key`, `api.endpoint` | Werden automatisch aus `Braze.initialize(apiKey, endpoint)` in JavaScript gesetzt. Setzen Sie diese nicht in der `configure`-Closure. |
| **Logging** | `logger.level` | Ausführliches Logging ist für die Entwicklung gedacht; reduzieren Sie die Ausgabe in der Produktion. |
| **Push** | `push.automation`, `push.appGroup`, … | Automation vereinfacht die Registrierung; `appGroup` wird für Push Stories / Erweiterungen benötigt, wenn diese verwendet werden. |
| **In-App-Nachrichten** | `triggerMinimumTimeInterval` | Standard: **30** Sekunden zwischen Triggern. |
| **Sessions** | `sessionTimeout` | Inaktivitätsdauer bis zum Start einer neuen Session (siehe Braze-Session-Dokumentation). |
| **Datenschutz / Daten** | `api.trackingPropertyAllowList`, `devicePropertyAllowList`, `api.sdkAuthentication` | Abstimmung mit dem [Privacy Manifest](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/privacy_manifest/) und den SDK-Authentifizierungseinstellungen. |
| **Netzwerk** | `api.requestPolicy`, `api.flushInterval` | Wiederholungsrichtlinie für Anfragen und Flush-Intervall. |
| **Push-Abo** | `optInWhenPushAuthorized` | Wenn `true`, kann das Abo nach der Autorisierung von Benachrichtigungen durch Nutzer:innen auf „Opted-in“ wechseln. |
| **IAM + Nutzer:innenwechsel** | `preventInAppMessageDisplayForDifferentUser` | Reduziert nicht übereinstimmende In-App-Nachrichten bei einem Wechsel der Nutzer-ID. |
| **Sonstige** | `forwardUniversalLinks`, `ephemeralEvents`, `useUUIDAsDeviceId`, … | Siehe die Swift-Dokumentation für das vollständige Verhalten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="iOS (Braze.Configuration)" }

Die React Native Bridge setzt React-spezifische **`api.sdkFlavor`**- / SDK-Metadaten bei der Initialisierung; überschreiben Sie diese nicht, es sei denn, die Braze-Dokumentation weist Sie dazu an.

---

## JavaScript / TypeScript API

Der Standardexport des Pakets ist die Klasse `Braze` mit **statischen** Methoden (zum Beispiel `Braze.changeUser`, `Braze.logPurchase`). Konstanten wie `Braze.Events`, `Braze.Genders` und `Braze.NotificationSubscriptionTypes` sind an denselben Export angehängt.

---

## Kernfunktionen

### Nutzer:innenverwaltung

``` typescript
import Braze from "@braze/react-native-sdk";

Braze.changeUser("user-123");
Braze.setEmail("user@example.com");
Braze.setCustomUserAttribute("plan", "premium");
Braze.addAlias("external_id", "marketing_id");
Braze.addToSubscriptionGroup("NEWSLETTER_GROUP_UUID");
```

Optionale **SDK-Authentifizierung**: Übergeben Sie eine Signatur als zweites Argument an `changeUser` oder rufen Sie `Braze.setSdkAuthenticationSignature(signature)` auf, wenn die Funktion im Dashboard aktiviert ist.

### In-App-Nachrichten

- Mit der **Standard-Braze-UI** folgen Sie der [Dokumentation zu In-App-Nachrichten](https://www.braze.com/docs/developer_guide/in_app_messages?sdktab=react%20native); in der Regel müssen Sie `subscribeToInAppMessage` **nicht** aufrufen, nur um die Standard-UI anzuzeigen.
- Für **angepasste** Verarbeitung abonnieren Sie mit `useBrazeUI: false` und protokollieren Sie dann Impressionen/Klicks nach Bedarf:

``` typescript
Braze.subscribeToInAppMessage(false, (event) => {
  const msg = event.inAppMessage;
  // Render your own UI from msg.message, msg.buttons, etc.
  Braze.logInAppMessageImpression(msg);
});
```

### Content Cards

``` typescript
const cards = await Braze.getCachedContentCards();
Braze.requestContentCardsRefresh();
Braze.launchContentCards(); // default Braze UI

Braze.logContentCardImpression(cardId);
Braze.logContentCardClicked(cardId);
```

Warten Sie auf Aktualisierungen mit `Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, ...)`.

### Banner

``` typescript
import Braze from "@braze/react-native-sdk";

Braze.requestBannersRefresh(["homepage_banner"]);
const banner = await Braze.getBanner("homepage_banner");

// Or use the native Banner view:
// <Braze.BrazeBannerView placementId="homepage_banner" />
```

### Push-Benachrichtigungen

``` typescript
Braze.requestPushPermission({
  alert: true,
  badge: true,
  sound: true,
});
// Token registration is usually handled natively; see docs for your setup.
Braze.registerPushToken(token);
```

- **`getInitialPushPayload`**: Verwenden Sie diese Methode, wenn die App über eine Benachrichtigung geöffnet wird, um Race-Conditions mit RN `Linking` zu vermeiden. Erfordert native Hooks (`BrazeReactUtils` auf iOS, `BrazeReactUtils.populateInitialPushPayloadFromIntent` auf Android), wie in den TypeScript-Dokumentationskommentaren und der Beispiel-App beschrieben.
- **`Braze.addListener(Braze.Events.PUSH_NOTIFICATION_EVENT, ...)`** ist laut den öffentlichen Typdefinitionen **nur für Android** verfügbar.

### Feature-Flags

``` typescript
const flag = await Braze.getFeatureFlag("new_checkout");
if (flag?.enabled) {
  const rollout = flag.getNumberProperty("rollout_percentage") ?? 0;
}
Braze.refreshFeatureFlags();
Braze.logFeatureFlagImpression("new_checkout");
```

### Analytics und Käufe

``` typescript
Braze.logCustomEvent("purchase_completed", { sku: "sku-1" });
Braze.logPurchase("sku-1", "29.99", "USD", 1, { source: "cart" });
Braze.requestImmediateDataFlush();
```

Hinweis: `logPurchase` erwartet den **Preis als String** (siehe Typdefinitionen).

### Datenverwaltung und SDK-Status

**`changeUser`** teilt Braze lediglich mit, welcher Nutzer-ID **neue** Aktivitäten zugeordnet werden sollen. Es löscht **keine** zwischengespeicherten SDK-Daten auf dem Gerät. Es gibt keine separate „Logout“-API: Wenn Sie eine herkömmliche Abmeldung benötigen (lokalen Braze-Status löschen, damit das zwischengespeicherte Profil, die Nachrichten und Token der vorherigen Nutzer:in auf dieser Installation entfernt werden), verwenden Sie in der Regel **`wipeData()`**. Dies ist ein vollständiger lokaler Reset.

``` typescript
Braze.wipeData();
Braze.disableSDK();
Braze.enableSDK();
```

**`wipeData()`** — Löscht die **lokalen** Braze-Daten für diese Installation (zwischengespeicherter Nutzer-/Sitzungs-/Kartenstatus, Push-Token-Zuordnung usw.). Verwenden Sie diese Methode für **Abmelde-Verhalten**, wenn Sie den Braze-Status der vorherigen Nutzer:in nicht auf dem Gerät belassen dürfen, sowie für **„Meine Daten auf diesem Gerät löschen“**, **QA**-Resets ohne Neuinstallation oder strikte **Datenschutz**-Abläufe. **`changeUser`** allein führt diese Bereinigung nicht durch – es legt nur fest, welche Nutzer-ID **neue** Events erhält. Auf **iOS** kann sich das Verhalten von Android unterscheiden (z. B. bei der Interaktion mit dem deaktivierten SDK-Status); konsultieren Sie die nativen Braze-Dokumentationen, wenn Sie dies in der Produktion einsetzen.

**`disableSDK()`** — Stoppt den Betrieb des SDK (keine Datenerfassung/-weiterleitung wie konfiguriert). Verwenden Sie diese Methode für **Nutzer-Opt-out**-Schalter, **eingeschränkte Modi** (Compliance, Kindersicherung) oder **Debugging** ohne Entfernung der Abhängigkeit.

**`enableSDK()`** — Aktiviert das SDK nach **`disableSDK()`** wieder. Auf **iOS** wird die Reaktivierung möglicherweise **erst beim nächsten App-Start** wirksam; überprüfen Sie dies in der Braze Swift/iOS-Dokumentation, bevor Sie sich auf eine sofortige Reaktivierung verlassen.

---

## Events

Abonnieren Sie mit `Braze.addListener(event, callback)`. Der Aufruf gibt ein Abo-Objekt zurück; rufen Sie **`.remove()`** darauf auf, um das Zuhören zu beenden.

**Einen Listener einrichten:**

``` typescript
import Braze from "@braze/react-native-sdk";

const subscription = Braze.addListener(
  Braze.Events.CONTENT_CARDS_UPDATED,
  (update) => {
    console.log("Content cards:", update.cards);
  }
);
```

**Den Listener entfernen:**

``` typescript
subscription.remove();
```

In einer React-Komponente speichern Sie das Abo und rufen `.remove()` in Ihrer Bereinigung auf (z. B. im Return eines `useEffect`):

``` typescript
useEffect(() => {
  const sub = Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
    setCards(update.cards);
  });
  return () => sub.remove();
}, []);
```

| Event-Konstante | Payload (Zusammenfassung) |
|-----------------|--------------------------|
| `Braze.Events.CONTENT_CARDS_UPDATED` | Neueste Content Cards |
| `Braze.Events.BANNER_CARDS_UPDATED` | Neueste Banner |
| `Braze.Events.FEATURE_FLAGS_UPDATED` | Feature-Flag-Array |
| `Braze.Events.IN_APP_MESSAGE_RECEIVED` | In-App-Nachricht-Event |
| `Braze.Events.SDK_AUTHENTICATION_ERROR` | SDK-Authentifizierungsfehlerdetails |
| `Braze.Events.PUSH_NOTIFICATION_EVENT` | Push-Payload (**nur Android**) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Events" }

---

## Hinweise zur Integration

- **Expo**: Verwenden Sie das [Braze Expo Plugin](https://github.com/braze-inc/braze-expo-plugin), um manuelle native Verdrahtung nach Möglichkeit zu vermeiden.
- **New Architecture / Turbo Modules**: Wird in neueren Plugin-Versionen unterstützt. Folgen Sie dem Entwicklerleitfaden und den Beispiel-Einstellungen für `AppDelegate` / Gradle, wenn Sie migrieren.
- **Datenschutz (iOS)**: Methoden wie `updateTrackingPropertyAllowList` unterstützen die Konfiguration im Zusammenhang mit dem Privacy Manifest. Weitere Informationen finden Sie unter [Swift Privacy Manifest](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/privacy_manifest/).

- **Jest**: Mocken Sie die nativen `react-native`-Module oder das Braze-Turbo-Modul (siehe `__tests__/jest.setup.js` in diesem Repo für Beispiele).

## Versionsunterstützung

{% alert note %}
Dieses SDK wurde mit React Native Version **0.85.3** getestet.
{% endalert %}
Die folgende Tabelle listet die unterstützten React Native Versionen nach Braze-Plugin-Release auf.

| Braze-Plugin | React Native | Neue Architektur |
|--------------|--------------|------------------|
| 9.0.0+       | ≥ 0.71       | Ja               |
| 6.0.0+       | ≥ 0.68       | Ja (≥ 0.70.0)    |
| 2.0.0+       | ≥ 0.68       | Ja               |
| ≤ 1.41.0     | ≤ 0.71       | Nein             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Versionsunterstützung" }

Beachten Sie außerdem die Anforderungen der nativen SDKs:

- [Android SDK – Versionsinformationen](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)
- [Swift SDK – Versionsinformationen](https://github.com/braze-inc/braze-swift-sdk?tab=readme-ov-file#version-information)

---

## Braze Expo Plugin

Für Expo-verwaltete Workflows siehe das [Braze Expo Plugin Repository](https://github.com/braze-inc/braze-expo-plugin).

---

## Beispiel-App

`BrazeProject` in diesem Repository ist eine vollständige Beispiel-App (Nutzerverwaltung, Content Cards, Feature-Flags, Banner usw.).

``` bash
cd BrazeProject/
yarn install
npx react-native start
```

**iOS** (aus `BrazeProject`):

``` bash
cd ios && pod install && cd ..
npx react-native run-ios
```

Verwenden Sie `RCT_NEW_ARCH_ENABLED=0 pod install`, wenn Sie die Legacy-Architektur benötigen.

**Android** (aus `BrazeProject`):

``` bash
npx react-native run-android
```

---

## Debugging und Fehlerbehebung

Aktivieren Sie das Braze-Logging in der **nativen** Konfiguration während der Entwicklung, damit das SDK in die Systemkonsole schreibt (Xcode / Android Logcat). Dies hilft bei der Überprüfung der Initialisierung, Nutzer:innenänderungen und Event-Zustellung.

- **iOS** — Setzen Sie in der `configure`-Closure, die an `BrazeReactInitializer.configure` übergeben wird, `config.logger.level = .debug` (oder `.info`). Reduzieren oder deaktivieren Sie dies in der Produktion, damit Logs für Nutzer:innen nicht sichtbar sind.
- **Android** — Verwenden Sie die Ressource `com_braze_logger_initial_log_level` in `braze.xml` oder setzen Sie den entsprechenden Wert über `BrazeConfig.Builder` (siehe [BrazeConfigurationProvider](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/logger-initial-log-level.html)). Verwenden Sie vor der Veröffentlichung ein weniger ausführliches Log-Level oder entfernen Sie die Überschreibung.

Für eine tiefergehende Fehlerbehebung (Netzwerk-, Sitzungs- oder Campaign-Verhalten) lesen Sie den [Braze React Native-Entwicklerleitfaden](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native) und die nativen SDK-Dokumentationen ([Swift](https://github.com/braze-inc/braze-swift-sdk) · [Android](https://github.com/braze-inc/braze-android-sdk)).

---

## Zusätzliche Ressourcen

- [Braze Developer Guide — React Native](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=react%20native)
- [Push-Benachrichtigungen — React Native](https://www.braze.com/docs/developer_guide/platform_integration_guides/react_native/push_notifications/)
- [GitHub-Repository](https://github.com/braze-inc/braze-react-native-sdk)
- [npm-Paket](https://www.npmjs.com/package/@braze/react-native-sdk)

## Kontakt

Bei Fragen wenden Sie sich an den technischen Support von Braze.
<!-- END GENERATED README CONTENT -->

Für Repository-Details und Beispielprojekte siehe [https://github.com/braze-inc/braze-react-native-sdk](https://github.com/braze-inc/braze-react-native-sdk).