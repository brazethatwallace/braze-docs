---
nav_title: React Native SDK
article_title: React Native SDK Repository-Leitfaden
page_order: 7
description: "Braze React Native SDK README-Referenz, gespiegelt von GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## Über das Braze React Native SDK {#about-the-braze-react-native-sdk}

Das Braze React Native SDK verbindet Ihre iOS- und Android-Apps mit Braze: Nutzerprofile, Messaging-Oberflächen, Analytics und Feature-Flags. Es umschließt das native [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk) und das [Braze Android SDK](https://github.com/braze-inc/braze-android-sdk) hinter einer JavaScript-API.

**Die Initialisierung erfolgt über JavaScript:** Sie richten die native Konfiguration (Push, Logging, Delegates) in Android-Ressourcen und im iOS-`AppDelegate` ein und rufen dann `Braze.initialize(apiKey, endpoint)` aus JavaScript auf, um das SDK zu starten. So haben Sie die volle Kontrolle darüber, wann das SDK initialisiert wird und mit welchen Zugangsdaten. Nach der Initialisierung rufen Sie bei Bedarf weitere SDK-Methoden auf (zum Beispiel `changeUser`, `logCustomEvent`).

### Was Sie tun können {#what-you-can-do}

- **Nutzerverwaltung**: Nutzer:innen identifizieren, Profilfelder, angepasste Attribute, Aliase und Abo-Gruppen festlegen
- **In-App-Nachrichten**: Standard-Braze-UI oder benutzerdefinierte Verarbeitung über Abonnements und Logging-APIs
- **Content Cards**: Standard-Feed-UI oder Karten abrufen und eine eigene UI erstellen
- **Banner**: Platzierungsbasierte HTML-Banner, einschließlich `BrazeBannerView`
- **Push-Benachrichtigungen**: Berechtigungsabfragen, Token-Registrierung, Payload-Listener (siehe Plattformhinweise unten)
- **Feature-Flags**: Aktualisieren, Eigenschaften lesen, Impressionen protokollieren
- **Analytics**: Angepasste Events, Käufe, sofortiger Flush
- **SDK-Steuerung**: SDK aktivieren/deaktivieren, lokale Daten löschen, SDK-Authentifizierungssignaturen

## Voraussetzungen {#prerequisites}

- **Braze-Konto** mit App-API-Schlüssel und SDK-Endpunkt
- **React Native**-Entwicklungsumgebung ([React Native Umgebungseinrichtung](https://reactnative.dev/docs/set-up-your-environment))
- **iOS**: Xcode, CocoaPods (`cd ios && pod install`)
- **Android**: Android Studio / Gradle; Kotlin-Gradle-Plugin wie von Ihrem React Native-Template benötigt
- **Push** (falls verwendet): FCM (Android) und APNs (iOS) Einrichtung gemäß der [Push-Dokumentation]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/push_notifications/)

Informationen zu den Zugangsdaten im Dashboard finden Sie in der [Integrationsübersicht]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=react%20native).

## Installation

``` bash
npm install @braze/react-native-sdk
# or:
# yarn add @braze/react-native-sdk
```

---

## Schnellstart {#quick-start}

Dieser Abschnitt zeigt die minimale Einrichtung, die erforderlich ist, um das Braze React Native SDK zu initialisieren.

1. Installieren Sie das npm-Paket (siehe oben).
2. Schließen Sie die **native Einrichtung** für Android und iOS ab (Konfiguration, Berechtigungen, Push falls erforderlich).
3. Initialisieren Sie das SDK aus JavaScript und beginnen Sie mit der Nutzung:

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

Ein erneuter Aufruf von `Braze.initialize` mit anderen Zugangsdaten beendet die aktuelle Instanz und erstellt sie neu, was eine Re-Initialisierung während der Sitzung ermöglicht.

---

## Native Einrichtung {#native-setup}

> **Maßgebliche Quelle:** Schritt-für-Schritt-Anleitungen, Gradle-/CocoaPods-Änderungen und die vollständige Liste der Android-XML-Schlüssel finden Sie im [Braze React Native Entwicklerleitfaden]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=react%20native). Die folgenden Snippets sind minimale Beispiele.

### Android

- Fügen Sie das **Kotlin-Gradle-Plugin** in Ihrer Root-`build.gradle` hinzu, falls Ihr Template dies nicht bereits enthält (Versionen hängen von Ihrer React Native-Version ab).
- Fügen Sie eine `braze.xml`-Ressourcendatei in `res/values` mit Ihrer Konfiguration hinzu. Aktivieren Sie die verzögerte Initialisierung, damit das SDK auf `Braze.initialize()` aus JavaScript wartet, bevor es startet. Andere Konfigurationswerte (Push, Sitzungs-Timeout usw.) werden weiterhin aus dieser Datei gelesen und bei der Initialisierung angewendet.
- Stellen Sie sicher, dass grundlegende Berechtigungen wie `INTERNET` und `ACCESS_NETWORK_STATE` in der `AndroidManifest.xml` vorhanden sind.
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
- **`postInitialization`-Closure** *(optional)*: Empfängt die aktive `Braze`-Instanz nach der Erstellung, für Einrichtungen, die die Instanz benötigen (z. B. Speichern einer Referenz, Festlegen von Delegates).

{% alert note %}
** `BrazeReactInitializer.configure` ist eine Swift-first-API, die das veraltete `BrazeReactBridge.initBraze(_:)` ersetzt. Sie löst auch ein Swift-Typauflösungsproblem mit `Braze.Configuration` in der Objective-C-Bridge.
{% endalert %}
---

## Konfigurationsreferenz {#configuration-reference}

In React Native ist die **Konfiguration nativ**: Android liest `res/values/braze.xml`, und iOS verwendet Closures, die über **`BrazeReactInitializer.configure`** registriert werden. Beide werden angewendet, wenn `Braze.initialize(apiKey, endpoint)` aus JavaScript aufgerufen wird.

### Android (`braze.xml`)

Standardwerte befinden sich in XML; [`BrazeConfig.Builder`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) kann sie beim Start überschreiben. Die maßgebliche Liste der Schlüssel und Typen finden Sie im [Android SDK-Integrationsleitfaden]({{site.baseurl}}/developer_guide/platforms/android/sdk_integration/) und in [`BrazeConfigurationProvider`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/index.html) (jede Kotlin-Eigenschaft entspricht dokumentierten `com_braze_*`-Ressourcen).

Häufig verwendete Einträge:

| Schlüssel | Ressourcentyp | Beschreibung |
|-----------|---------------|--------------|
| `com_braze_enable_delayed_initialization` | `bool` | **Erforderlich.** Auf `true` setzen, damit das SDK auf `Braze.initialize()` aus JavaScript wartet. |
| `com_braze_api_key` | `string` | Nicht erforderlich bei Verwendung von `Braze.initialize()` aus JavaScript (Zugangsdaten werden aus JS übergeben). Nur für die Legacy-native-first-Initialisierung erforderlich. |
| `com_braze_custom_endpoint` | `string` | Nicht erforderlich bei Verwendung von `Braze.initialize()` aus JavaScript. Nur für die Legacy-native-first-Initialisierung erforderlich. |
| `com_braze_server_target` | `string` | Optionaler Cluster-/Umgebungsselektor (z. B. einige interne oder Staging-Builds). Bevorzugen Sie `com_braze_custom_endpoint` für die Produktion, es sei denn, Ihre Braze-Integration gibt etwas anderes vor. |
| `com_braze_firebase_cloud_messaging_registration_enabled` | `bool` | Wenn `true`, registriert sich Braze für FCM (typische Push-Einrichtung). |
| `com_braze_firebase_cloud_messaging_sender_id` | `string` | FCM-Sender-ID, wenn die automatische Registrierung aktiviert ist. |
| `com_braze_handle_push_deep_links_automatically` | `bool` | Lässt Braze Push-Deeplinks automatisch öffnen. |
| `com_braze_trigger_action_minimum_time_interval_seconds` | `integer` | Minimale Sekunden zwischen In-App-Nachricht-Trigger-Aktionen. |
| **Sonstige** | *verschiedene* | Weitere hier nicht aufgeführte Schlüssel (Sitzungs-Timeout, Geofences, Standort, Benachrichtigungsstandards, Geräte-Allowlists, verzögerte Initialisierung, SDK-Authentifizierung usw.). Siehe [`BrazeConfigurationProvider`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/index.html) und den [Android SDK-Integrationsleitfaden]({{site.baseurl}}/developer_guide/platforms/android/sdk_integration/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Android (braze.xml)" }

### iOS (`Braze.Configuration`)

Legen Sie native Konfigurationseigenschaften in der `configure`-Closure fest, die an `BrazeReactInitializer.configure` übergeben wird. Die Closure empfängt eine `Braze.Configuration`-Instanz – der API-Schlüssel und der Endpunkt werden automatisch aus dem JavaScript-Aufruf `Braze.initialize` gesetzt. Vollständige Details: [`Braze.Configuration`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class) und verschachtelte Typen **`api`**, **`push`**, **`logger`**, **`location`**.

| Bereich | Mitglieder (repräsentativ) | Hinweise |
|---------|---------------------------|----------|
| **Zugangsdaten** | `api.key`, `api.endpoint` | Werden automatisch aus `Braze.initialize(apiKey, endpoint)` in JavaScript gesetzt. Legen Sie diese nicht in der `configure`-Closure fest. |
| **Logging** | `logger.level` | Ausführliches Logging ist für die Entwicklung; reduzieren Sie die Ausgabe in der Produktion. |
| **Push** | `push.automation`, `push.appGroup`, … | Automation vereinfacht die Registrierung; `appGroup` wird für Push Stories / Erweiterungen benötigt, wenn diese verwendet werden. |
| **In-App-Nachrichten** | `triggerMinimumTimeInterval` | Standard **30** Sekunden zwischen Triggern. |
| **Sitzungen** | `sessionTimeout` | Inaktivität vor einer neuen Sitzung (siehe Braze-Sitzungsdokumentation). |
| **Datenschutz / Daten** | `api.trackingPropertyAllowList`, `devicePropertyAllowList`, `api.sdkAuthentication` | Abstimmung mit dem [Privacy Manifest]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest/) und den SDK-Authentifizierungseinstellungen. |
| **Netzwerk** | `api.requestPolicy`, `api.flushInterval` | Anfrage-Wiederholungsrichtlinie und Flush-Kadenz. |
| **Push-Abo** | `optInWhenPushAuthorized` | Wenn `true`, kann das Abo nach der Autorisierung von Benachrichtigungen durch die Nutzer:innen auf „opted-in“ wechseln. |
| **IAM und Nutzerwechsel** | `preventInAppMessageDisplayForDifferentUser` | Reduziert nicht übereinstimmende IAM bei Änderung der Nutzer-ID. |
| **Sonstige** | `forwardUniversalLinks`, `ephemeralEvents`, `useUUIDAsDeviceId`, … | Siehe Swift-Dokumentation für das vollständige Verhalten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="iOS (Braze.Configuration)" }

Die React Native Bridge setzt React-spezifische **`api.sdkFlavor`**-/SDK-Metadaten bei der Initialisierung; überschreiben Sie diese nicht, es sei denn, die Braze-Dokumentation weist Sie dazu an.

---

## JavaScript-/TypeScript-API

Der Standard-Export des Pakets ist die `Braze`-Klasse mit **statischen** Methoden (zum Beispiel `Braze.changeUser`, `Braze.logPurchase`). Konstanten wie `Braze.Events`, `Braze.Genders` und `Braze.NotificationSubscriptionTypes` sind an denselben Export angehängt.

---

## Kernfunktionen {#core-features}

### Nutzerverwaltung {#user-management}

``` typescript
import Braze from "@braze/react-native-sdk";

Braze.changeUser("user-123");
Braze.setEmail("user@example.com");
Braze.setCustomUserAttribute("plan", "premium");
Braze.addAlias("external_id", "marketing_id");
Braze.addToSubscriptionGroup("NEWSLETTER_GROUP_UUID");
```

Optionale **SDK-Authentifizierung**: Übergeben Sie eine Signatur als zweites Argument an `changeUser`, oder rufen Sie `Braze.setSdkAuthenticationSignature(signature)` auf, wenn dies im Dashboard aktiviert ist.

### In-App-Nachrichten {#in-app-messages}

- Mit der **Standard-Braze-UI** folgen Sie der [In-App-Nachricht-Dokumentation]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=react%20native); Sie müssen in der Regel **nicht** `subscribeToInAppMessage` aufrufen, nur um die Standard-UI anzuzeigen.
- Für **benutzerdefinierte** Verarbeitung abonnieren Sie mit `useBrazeUI: false` und protokollieren Sie dann Impressionen/Klicks nach Bedarf:

``` typescript
Braze.subscribeToInAppMessage(false, (event) => {
  const msg = event.inAppMessage;
  // Render your own UI from msg.message, msg.buttons, etc.
  Braze.logInAppMessageImpression(msg);
});
```

### Content Cards

``` typescript
const cards = await Braze.getContentCards();
Braze.requestContentCardsRefresh();
Braze.launchContentCards(); // default Braze UI

Braze.logContentCardImpression(cardId);
Braze.logContentCardClicked(cardId);
```

Warten Sie auf Aktualisierungen mit `Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, ...)`.

### Banner {#banners}

``` typescript
import Braze from "@braze/react-native-sdk";

Braze.requestBannersRefresh(["homepage_banner"]);
const banner = await Braze.getBanner("homepage_banner");

// Or use the native Banner view:
// <Braze.BrazeBannerView placementID="homepage_banner" />
```

### Push-Benachrichtigungen {#push-notifications}

``` typescript
Braze.requestPushPermission({
  alert: true,
  badge: true,
  sound: true,
});
// Token registration is usually handled natively; see docs for your setup.
Braze.registerPushToken(token);
```

- **`getInitialPushPayload`**: Verwenden Sie dies, wenn die App über eine Benachrichtigung geöffnet wird, um Race-Conditions mit RN `Linking` zu vermeiden; erfordert native Hooks (`BrazeReactUtils` auf iOS, `BrazeReactUtils.populateInitialPushPayloadFromIntent` auf Android), wie in den TypeScript-Dokumentkommentaren und der Beispiel-App beschrieben.
- **`Braze.addListener(Braze.Events.PUSH_NOTIFICATION_EVENT, ...)`** ist gemäß den öffentlichen Typisierungen **nur für Android** verfügbar.

### Feature-Flags

``` typescript
const flag = await Braze.getFeatureFlag("new_checkout");
if (flag?.enabled) {
  const rollout = flag.getNumberProperty("rollout_percentage") ?? 0;
}
Braze.refreshFeatureFlags();
Braze.logFeatureFlagImpression("new_checkout");
```

### Analytics und Käufe {#analytics-and-purchases}

``` typescript
Braze.logCustomEvent("purchase_completed", { sku: "sku-1" });
Braze.logPurchase("sku-1", "29.99", "USD", 1, { source: "cart" });
Braze.requestImmediateDataFlush();
```

Hinweis: `logPurchase` nimmt den **Preis als String** entgegen (siehe Typisierungen).

### Datenverwaltung und SDK-Status {#data-management-and-sdk-state}

**`changeUser`** teilt Braze nur mit, welcher Nutzer-ID **neue** Aktivitäten zugeordnet werden sollen. Es löscht **keine** zwischengespeicherten SDK-Daten auf dem Gerät. Es gibt keine separate „Logout“-API: Wenn Sie eine herkömmliche Abmeldung benötigen (lokalen Braze-Status löschen, damit das zwischengespeicherte Profil, die Nachrichten und Token der vorherigen Nutzer:innen auf dieser Installation verschwinden), verwenden Sie in der Regel **`wipeData()`**. Dies ist ein vollständiger lokaler Reset.

``` typescript
Braze.wipeData();
Braze.disableSDK();
Braze.enableSDK();
```

**`wipeData()`** — Löscht die **lokalen** Braze-Daten für diese Installation (zwischengespeicherter Nutzer-/Sitzungs-/Kartenstatus, Push-Token-Zuordnung usw.). Verwenden Sie dies für **Abmelde-Verhalten**, wenn Sie den Braze-Status der vorherigen Nutzer:innen nicht auf dem Gerät belassen dürfen, sowie für **„Meine Daten auf diesem Gerät löschen“**, **QA**-Resets ohne Neuinstallation oder strenge **Datenschutz**-Abläufe. **`changeUser`** allein führt diese Bereinigung nicht durch – es legt nur fest, welche Nutzer-ID **neue** Ereignisse empfängt. Auf **iOS** kann sich das Verhalten von Android unterscheiden (z. B. Interaktion mit dem deaktivierten SDK-Status); siehe die nativen Braze-Dokumentationen, wenn Sie dies in der Produktion einsetzen.

**`disableSDK()`** — Stoppt den Betrieb des SDK (keine Erfassung/Weiterleitung wie konfiguriert). Verwenden Sie dies für **Nutzer-Opt-out**-Umschalter, **eingeschränkte Modi** (Compliance, Kindereinstellungen) oder **Debugging** ohne Entfernung der Abhängigkeit.

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

## Integrationshinweise {#integration-notes}

- **Expo**: Verwenden Sie das [Braze Expo Plugin](https://github.com/braze-inc/braze-expo-plugin), um manuelle native Verdrahtung nach Möglichkeit zu vermeiden.
- **New Architecture / Turbo Modules**: Wird in neueren Plugin-Versionen unterstützt; folgen Sie dem Entwicklerleitfaden und den Beispiel-`AppDelegate`-/Gradle-Einstellungen, wenn Sie migrieren.
- **Datenschutz (iOS)**: Methoden wie `updateTrackingPropertyAllowList` unterstützen die Konfiguration im Zusammenhang mit dem Privacy Manifest; siehe [Swift Privacy Manifest]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest/).
## - **Jest**: Mocken Sie `react-native`-native Module oder das Braze Turbo Module (siehe `__tests__/jest.setup.js` in diesem Repository für Muster). {#jest-mock-react-native-native-modules-or-the-braze-turbo-module-see-__tests__jestsetupjs-in-this-repo-for-patterns}

## Versionsunterstützung {#version-support}

{% alert note %}
Dieses SDK wurde mit React Native Version **0.85.3** getestet.
{% endalert %}
Die folgende Tabelle listet unterstützte React Native-Versionen nach Braze-Plugin-Release auf.

| Braze Plugin | React Native | New Architecture |
|--------------|--------------|------------------|
| 9.0.0+       | ≥ 0.71       | Ja               |
| 6.0.0+       | ≥ 0.68       | Ja (≥ 0.70.0)    |
| 2.0.0+       | ≥ 0.68       | Ja               |
| ≤ 1.41.0     | ≤ 0.71       | Nein             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Versionsunterstützung" }

Beachten Sie auch die Anforderungen der nativen SDKs:

- [Android SDK-Versionsinformationen](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)
- [Swift SDK-Versionsinformationen](https://github.com/braze-inc/braze-swift-sdk?tab=readme-ov-file#version-information)

---

## Braze Expo Plugin

Für Expo-verwaltete Workflows siehe das [Braze Expo Plugin Repository](https://github.com/braze-inc/braze-expo-plugin).

---

## Beispiel-App {#sample-app}

`BrazeProject` in diesem Repository ist ein vollständiges Beispiel (Nutzerverwaltung, Content Cards, Feature-Flags, Banner usw.).

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

## Debugging und Fehlerbehebung {#debugging-and-troubleshooting}

Aktivieren Sie das Braze-Logging in der **nativen** Konfiguration während der Entwicklung, damit das SDK in die Systemkonsole schreibt (Xcode / Android Logcat). Dies hilft bei der Überprüfung von Initialisierung, Nutzerwechseln und Event-Zustellung.

- **iOS** — Setzen Sie in der `configure`-Closure, die an `BrazeReactInitializer.configure` übergeben wird, `config.logger.level = .debug` (oder `.info`). Reduzieren oder deaktivieren Sie dies in der Produktion, damit Logs für Nutzer:innen nicht sichtbar sind.
- **Android** — Verwenden Sie die Ressource `com_braze_logger_initial_log_level` in `braze.xml` oder setzen Sie den entsprechenden Wert über `BrazeConfig.Builder` (siehe [BrazeConfigurationProvider](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-configuration-provider/logger-initial-log-level.html)). Verwenden Sie vor der Veröffentlichung ein weniger ausführliches Level oder entfernen Sie die Überschreibung.

Für eine tiefergehende Fehlerbehebung (Netzwerk, Sitzung oder Campaign-Verhalten) siehe den [Braze React Native Entwicklerleitfaden]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=react%20native) und die nativen SDK-Dokumentationen ([Swift](https://github.com/braze-inc/braze-swift-sdk) · [Android](https://github.com/braze-inc/braze-android-sdk)).

---

## Zusätzliche Ressourcen {#additional-resources}

- [Braze Entwicklerleitfaden — React Native]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=react%20native)
- [Push-Benachrichtigungen — React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/push_notifications/)
- [GitHub-Repository](https://github.com/braze-inc/braze-react-native-sdk)
- [npm-Paket](https://www.npmjs.com/package/@braze/react-native-sdk)

## Kontakt {#contact}

Wenn Sie Fragen haben, kontaktieren Sie bitte [support@braze.com](mailto:support@braze.com).
<!-- END GENERATED README CONTENT -->

Für Repository-Details und Beispielprojekte siehe [https://github.com/braze-inc/braze-react-native-sdk](https://github.com/braze-inc/braze-react-native-sdk).