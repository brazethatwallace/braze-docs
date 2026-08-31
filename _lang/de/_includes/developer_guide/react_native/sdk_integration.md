## Über das React Native Braze SDK {#about-the-react-native-braze-sdk}

Durch die Integration des React Native Braze SDK erhalten Sie grundlegende Analytics-Funktionalität und können In-App Messages und Content Cards sowohl für iOS als auch für Android mit einer einzigen Codebasis integrieren.

## Kompatibilität mit der neuen Architektur {#new-architecture-compatibility}

Die folgende SDK-Mindestversion ist mit allen Apps kompatibel, die [die neue Architektur von React Native](https://reactnative.dev/docs/the-new-architecture/landing-page) verwenden:

{% sdk_min_versions reactnative:2.0.1 %}

Ab SDK-Version 6.0.0 verwendet Braze ein React Native Turbo Module, das sowohl mit der neuen Architektur als auch mit der älteren Bridge-Architektur kompatibel ist. Das bedeutet, dass keine zusätzliche Einrichtung erforderlich ist.

{% alert warning %}
Wenn Ihre iOS-App `RCTAppDelegate` implementiert und Sie unserer bisherigen `AppDelegate`-Einrichtung gefolgt sind, lesen Sie die Beispiele unter [Vollständige native Einrichtung](#reactnative_step-2-complete-native-setup), um Abstürze beim Abonnieren von Events im Turbo Module zu vermeiden.
{% endalert %}

## Versionsanforderungen für React und React Native {#react-and-react-native-version-requirements}

Braze veröffentlicht keine separaten Mindestversionen für React über das hinaus, was das React Native SDK unterstützt. Um das SDK zu integrieren, verwenden Sie React Native Version 0.71 oder höher. Die vollständige Liste der unterstützten React Native-Versionen finden Sie im [React Native SDK GitHub-Repository](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support).

Wenn Sie React, React Native oder das Braze SDK aktualisieren, überprüfen Sie das SDK-[CHANGELOG](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md) auf Breaking Changes, bevor Sie Ihre Änderungen bereitstellen.

## Integration des React Native SDK {#integrating-the-react-native-sdk}

### Voraussetzungen {#prerequisites}

Informationen zu unterstützten React-Native-Versionen und Hinweise zum Upgrade finden Sie unter [Versionsanforderungen für React und React Native](#react-and-react-native-version-requirements).

### Schritt 1: Braze-Bibliothek integrieren {#step-1-integrate-the-braze-library}

{% tabs local %}
{% tab npm %}
```bash
npm install @braze/react-native-sdk
```
{% endtab %}
{% tab yarn %}
```bash
yarn add @braze/react-native-sdk
```
{% endtab %}
{% endtabs %}

<a id="step-2-choose-a-setup-option"></a>
<a id="reactnative_step-2-complete-native-setup"></a>
### Schritt 2: Native Einrichtung abschließen {#step-2-complete-native-setup}

Wenn Ihre App Expo verwendet, lesen Sie [Verwendung des Expo-Plugins](#reactnative-using-the-expo-plugin). Wenn Ihre App reines React Native verwendet, lesen Sie [Verwendung der React Native CLI](#reactnative-using-react-native-cli).
Wählen Sie in jedem Versions-Tab eine Einrichtungsmethode aus: Expo-Plugin oder React Native CLI.

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

#### Methode 1: Verwendung des Expo-Plugins {#reactnative-using-the-expo-plugin}

##### 2.1 Braze Expo-Plugin installieren {#21-install-the-braze-expo-plugin}

Stellen Sie sicher, dass Ihre Version des Braze Expo-Plugins mindestens 4.1.0 ist. Die vollständige Liste der unterstützten Versionen finden Sie im [Braze Expo-Plugin-Repository](https://github.com/braze-inc/braze-expo-plugin?tab=readme-ov-file#version-support).

Der folgende Codeausschnitt zeigt den Befehl zur Installation des Braze Expo-Plugins:

```bash
npx expo install @braze/expo-plugin
```

##### 2.2 Plugin zur app.json hinzufügen {#22-add-the-plugin-to-your-appjson}

Fügen Sie in Ihrer `app.json` das Braze Expo-Plugin hinzu. Der API-Schlüssel und der Endpunkt werden hier nicht mehr festgelegt. Stellen Sie diese zur Laufzeit über `Braze.initialize()` aus JavaScript bereit. Fügen Sie die folgenden optionalen Konfigurationsparameter je nach Ihren Implementierungsanforderungen hinzu:

| Methode                                       | Typ     | Beschreibung                                                                                                                                             |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enableBrazeIosPush`                          | boolean | Nur iOS. Ob Braze für die Verarbeitung von Push-Benachrichtigungen auf iOS verwendet werden soll.                       |
| `enableFirebaseCloudMessaging`                | boolean | Nur Android. Ob Firebase Cloud Messaging für Push-Benachrichtigungen verwendet werden soll.             |
| `firebaseCloudMessagingSenderId`              | string  | Nur Android. Ihre Firebase Cloud Messaging-Sender-ID.                                    |
| `sessionTimeout`                              | integer | Das Braze-Sitzungs-Timeout für Ihre Anwendung in Sekunden.                                                                                               |
| `enableSdkAuthentication`                     | boolean | Ob das Feature [SDK-Authentifizierung]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication) aktiviert werden soll.      |
| `logLevel`                                    | integer | Die Protokollierungsstufe für Ihre Anwendung. Die Standard-Protokollierungsstufe ist 8 und protokolliert minimal Info-Meldungen. Verwenden Sie für ausführliche Protokollierung zum Debugging die Protokollierungsstufe 0.    |
| `minimumTriggerIntervalInSeconds`             | integer | Das minimale Zeitintervall in Sekunden zwischen Triggern. Standardmäßig 30 Sekunden.                                                                           |
| `enableAutomaticLocationCollection`           | boolean | Ob die automatische Standorterfassung aktiviert ist (sofern der/die Nutzer:in zustimmt).                                                                                  |
| `enableGeofence`                              | boolean | Ob Geofences aktiviert sind.                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | boolean | Ob Geofence-Anfragen automatisch gestellt werden sollen.                                                                                                  |
| `dismissModalOnOutsideTap`                    | boolean | Nur iOS. Ob eine modale In-App-Nachricht geschlossen wird, wenn der/die Nutzer:in außerhalb der In-App-Nachricht tippt.                                           |
| `androidHandlePushDeepLinksAutomatically`     | boolean | Nur Android. Ob das Braze SDK Deeplinks aus Push-Benachrichtigungen automatisch verarbeiten soll.                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | boolean | Nur Android. Legt fest, ob der Textinhalt einer Push-Benachrichtigung als HTML mit `android.text.Html.fromHtml` interpretiert und gerendert werden soll.        |
| `androidNotificationAccentColor`              | string  | Nur Android. Legt die Akzentfarbe für Android-Benachrichtigungen fest.                                                                                                |
| `androidNotificationLargeIcon`                | string  | Nur Android. Legt das große Symbol für Android-Benachrichtigungen fest.                                                                                                  |
| `androidNotificationSmallIcon`                | string  | Nur Android. Legt das kleine Symbol für Android-Benachrichtigungen fest.                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | boolean | Nur iOS. Ob der/die Nutzer:in beim App-Start automatisch nach Push-Berechtigungen gefragt werden soll.                                                          |
| `enableBrazeIosRichPush`                      | boolean | Nur iOS. Ob Rich-Push-Features für iOS aktiviert werden sollen.                                                                                                  |
| `enableBrazeIosPushStories`                   | boolean | Nur iOS. Ob Braze Push Stories für iOS aktiviert werden sollen.                                                                                                  |
| `iosPushStoryAppGroup`                        | string  | Nur iOS. Die App-Gruppe für iOS Push Stories.                                                                                                       |
| `iosUseUUIDAsDeviceId`                        | boolean | Nur iOS. Ob die Geräte-ID eine zufällig generierte UUID verwendet.                                                                                       |
| `iosForwardUniversalLinks`                    | boolean | Nur iOS. Gibt an, ob das SDK Universal Links automatisch erkennen und an die Systemmethoden weiterleiten soll (Standard: `false`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="2.2 Plugin zur app.json hinzufügen" }

Der folgende Codeausschnitt zeigt eine beispielhafte `app.json`-Konfiguration:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "sessionTimeout": 60,
          "enableGeofence": false,
          "enableBrazeIosPush": false,
          "enableFirebaseCloudMessaging": false,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true,
          "enableSdkAuthentication": false,
          "logLevel": 0,
          "minimumTriggerIntervalInSeconds": 0,
          "enableAutomaticLocationCollection": false,
          "enableAutomaticGeofenceRequests": false,
          "dismissModalOnOutsideTap": true,
          "androidPushNotificationHtmlRenderingEnabled": true,
          "androidNotificationAccentColor": "#ff3344",
          "androidNotificationLargeIcon": "@drawable/custom_app_large_icon",
          "androidNotificationSmallIcon": "@drawable/custom_app_small_icon",
          "iosRequestPushPermissionsAutomatically": false,
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.example.myapp.PushStories",
          "iosForwardUniversalLinks": false
        }
      ]
    ]
  }
}
```

###### Konfiguration von Android-Push-Benachrichtigungssymbolen {#android-push-icons}

Wenn Sie `androidNotificationLargeIcon` und `androidNotificationSmallIcon` verwenden, beachten Sie die folgenden Best Practices für die korrekte Symboldarstellung:

**Platzierung und Format der Symbole**

Um benutzerdefinierte Push-Benachrichtigungssymbole mit dem Braze Expo-Plugin zu verwenden:

1. Erstellen Sie Ihre Symboldateien gemäß den unten aufgeführten Symbolanforderungen.
2. Legen Sie sie in den nativen Android-Verzeichnissen Ihres Projekts unter `android/app/src/main/res/drawable-<density>/` ab.
   Verwenden Sie beispielsweise `android/app/src/main/res/drawable-mdpi/` und `android/app/src/main/res/drawable-hdpi/`.
3. Alternativ können Sie, wenn Sie Assets in Ihrem React-Native-Verzeichnis verwalten, Expos [app.json-Symbolkonfiguration](https://docs.expo.dev/versions/latest/config/app/#icon) verwenden oder ein [Expo Config Plugin](https://docs.expo.dev/config-plugins/introduction/) erstellen, um die Symbole während des Prebuilds in die Android-Drawable-Ordner zu kopieren.

Das Braze Expo-Plugin referenziert diese Symbole über Androids Drawable-Ressourcensystem.

**Symbolanforderungen**

- **Kleines Symbol:** Muss eine weiße Silhouette auf transparentem Hintergrund sein (dies ist eine Anforderung der Android-Plattform)
- **Großes Symbol:** Kann ein Vollfarbbild sein.
- **Format:** PNG-Format wird empfohlen.
- **Benennung:** Verwenden Sie nur Kleinbuchstaben, Zahlen und Unterstriche (z. B. `my_large_icon.png`)

**Konfiguration in app.json**

Der folgende Codeausschnitt zeigt, wie Sie Android-Benachrichtigungssymbole in der `app.json` mit dem Präfix `@drawable/` referenzieren:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidNotificationLargeIcon": "@drawable/large_icon",
          "androidNotificationSmallIcon": "@drawable/small_icon"
        }
      ]
    ]
  }
}
```

{% alert important %}
Verwenden Sie keine relativen Dateipfade (wie `src/assets/images/icon.png`) und geben Sie nicht die Dateierweiterung an, wenn Sie Symbole referenzieren. Das Expo-Plugin erfordert das Präfix `@drawable/`, um die Symbole nach dem Prebuild-Prozess korrekt in den nativen Android-Ordnern zu finden.
{% endalert %}

**Funktionsweise**

Das Braze Expo-Plugin referenziert Ihre Symboldateien aus den Android-`drawable`-Verzeichnissen. Wenn Sie `npx expo prebuild` ausführen, generiert Expo die native Android-Projektstruktur. Ihre Symbole müssen vor dem Build-Prozess in den Android-`drawable`-Ordnern vorhanden sein (entweder manuell platziert oder über ein Config Plugin kopiert). Das Plugin konfiguriert dann das Braze SDK so, dass es diese Drawable-Ressourcen anhand ihrer Namen (ohne Pfad oder Erweiterung) verwendet – deshalb ist das Präfix `@drawable/` in Ihrer Konfiguration erforderlich.

Weitere Informationen zu Android-Benachrichtigungssymbolen finden Sie in [Androids Richtlinien für Benachrichtigungssymbole](https://developer.android.com/develop/ui/views/notifications#icon).

##### 2.3 Anwendung erstellen und ausführen {#23-build-and-run-your-application}

Beim Prebuilding Ihrer Anwendung werden die nativen Dateien generiert, die für das Braze Expo-Plugin erforderlich sind.

Der folgende Codeausschnitt zeigt den Befehl zum Prebuilding Ihrer Anwendung:

```bash
npx expo prebuild
```

Führen Sie Ihre Anwendung wie in der [Expo-Dokumentation](https://docs.expo.dev/workflow/customizing/) beschrieben aus. Wenn Sie Änderungen an den Konfigurationsoptionen vornehmen, führen Sie Prebuild und Anwendung erneut aus.

#### Methode 2: Verwendung der React Native CLI {#reactnative-using-react-native-cli}

##### Android einrichten {#set-up-android}

**2.1 Kotlin-Gradle-Plugin hinzufügen**

Der folgende Codeausschnitt zeigt, wie Sie das Kotlin-Gradle-Plugin in der `build.gradle`-Datei Ihres Top-Level-Projekts unter `buildscript` > `dependencies` hinzufügen:

```groovy
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}
```

Dadurch wird Kotlin zu Ihrem Projekt hinzugefügt.

**2.2 Braze SDK konfigurieren**

Erstellen Sie eine `braze.xml`-Datei im Ordner `res/values` Ihres Projekts. Der API-Schlüssel und der Endpunkt werden zur Laufzeit aus JavaScript bereitgestellt und sind in dieser Datei daher nicht erforderlich. Der folgende Codeausschnitt zeigt, wie Sie die verzögerte Initialisierung mit `com_braze_enable_delayed_initialization` aktivieren:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <bool name="com_braze_enable_delayed_initialization">true</bool>
</resources>
```

{% alert note %}
Sie können weiterhin andere native Konfigurationswerte zu `braze.xml` hinzufügen (z. B. für Push, Sitzungs-Timeout und Protokollierung). Diese werden automatisch angewendet, wenn `Braze.initialize()` aus JavaScript aufgerufen wird.
{% endalert %}

Der folgende Codeausschnitt zeigt die erforderlichen Berechtigungen für Ihre `AndroidManifest.xml`-Datei:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
Ab Braze Android SDK Version 12.2.0 können Sie die android-sdk-location-Bibliothek automatisch einbinden, indem Sie `importBrazeLocationLibrary=true` in Ihrer `gradle.properties`-Datei festlegen.
{% endalert %}

**2.3 Nutzer:innen-Sitzungsverfolgung implementieren**

Die Aufrufe von `openSession()` und `closeSession()` werden automatisch verarbeitet.
Der folgende Codeausschnitt zeigt, was Sie zur `onCreate()`-Methode Ihrer `MainApplication`-Klasse hinzufügen müssen:

{% subtabs local %}
{% subtab JAVA %}
```java
import com.braze.BrazeActivityLifecycleCallbackListener;

@Override
public void onCreate() {
    super.onCreate();
    ...
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
import com.braze.BrazeActivityLifecycleCallbackListener

override fun onCreate() {
    super.onCreate()
    ...
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
}
```
{% endsubtab %}
{% endsubtabs %}

**2.4 Intent-Aktualisierungen verarbeiten**

Wenn Ihre MainActivity `android:launchMode` auf `singleTask` gesetzt hat, zeigt der folgende Codeausschnitt, was Sie zu Ihrer `MainActivity`-Klasse hinzufügen müssen:

{% subtabs local %}
{% subtab JAVA %}
```java
@Override
public void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    setIntent(intent);
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
override fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    setIntent(intent)
}
```
{% endsubtab %}
{% endsubtabs %}

##### iOS einrichten {#set-up-ios}

**2.5 (Optional) Podfile für dynamische XCFrameworks konfigurieren**

Um bestimmte Braze-Bibliotheken wie BrazeUI in eine Objective-C++-Datei zu importieren, müssen Sie die `#import`-Syntax verwenden. Ab Version `7.4.0` des Braze Swift SDK verfügen die Binärdateien über einen [optionalen Vertriebskanal als dynamische XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic), der mit dieser Syntax kompatibel ist.

Wenn Sie diesen Vertriebskanal nutzen möchten, überschreiben Sie die CocoaPods-Quellorte in Ihrem Podfile manuell. Referenzieren Sie dieses Beispiel und ersetzen Sie `{your-version}` durch die gewünschte Version:

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

**2.6 Pods installieren**

Da React Native die Bibliotheken automatisch mit der nativen Plattform verknüpft, können Sie das SDK mithilfe von CocoaPods installieren.

Der folgende Codeausschnitt zeigt, wie Sie Pods aus dem Stammordner des Projekts installieren:

```bash
# To install using the React Native New Architecture
cd ios && pod install

# To install using the React Native legacy architecture
cd ios && RCT_NEW_ARCH_ENABLED=0 pod install
```

**2.7 Braze SDK konfigurieren**

Verwenden Sie `BrazeReactInitializer.configure` in Ihrem `AppDelegate`, um die native Konfiguration zu registrieren. Die von Ihnen bereitgestellten Closures werden gespeichert und später angewendet, wenn `Braze.initialize(apiKey, endpoint)` aus JavaScript aufgerufen wird.

{% subtabs local %}
{% subtab SWIFT %}

Der folgende Codeausschnitt zeigt, wie Sie das Braze SDK am Anfang der `AppDelegate.swift`-Datei importieren:

```swift
import BrazeKit
import braze_react_native_sdk
```

Registrieren Sie in der `application(_:didFinishLaunchingWithOptions:)`-Methode Ihre native Konfiguration mit `BrazeReactInitializer.configure`. Legen Sie den API-Schlüssel oder Endpunkt hier nicht fest. Diese werden aus JavaScript über `Braze.initialize()` bereitgestellt.

- **`configure`-Closure**: Empfängt eine `Braze.Configuration` und ermöglicht Ihnen, native Konfigurationseigenschaften festzulegen (Protokollierung, Push, Sitzungen und mehr).
- **`postInitialization`-Closure** _(optional)_: Empfängt die aktive `Braze`-Instanz nach der Erstellung für Einrichtungsschritte, die die Instanz erfordern (z. B. Speichern einer Referenz oder Festlegen von Delegates).

Der folgende Codeausschnitt zeigt eine beispielhafte `AppDelegate.swift`-Implementierung mit `BrazeReactInitializer.configure`:

```swift
@main
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
  ) -> Bool {
    BrazeReactInitializer.configure { configuration in
      configuration.logger.level = .info
      configuration.push.automation = true
    } postInitialization: { braze in
      AppDelegate.braze = braze
    }

    // ... React Native setup

    return true
  }
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Der folgende Codeausschnitt zeigt, wie Sie das Braze SDK am Anfang der `AppDelegate.m`-Datei importieren:

```objc
@import BrazeKit;
@import braze_react_native_sdk;
```

Registrieren Sie in der `application:didFinishLaunchingWithOptions:`-Methode Ihre native Konfiguration mit `BrazeReactInitializer`. Legen Sie den API-Schlüssel oder Endpunkt hier nicht fest. Diese werden aus JavaScript über `Braze.initialize()` bereitgestellt.

Der folgende Codeausschnitt zeigt eine beispielhafte `AppDelegate.m`-Implementierung mit `BrazeReactInitializer`:

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [BrazeReactInitializer configure:^(BRZConfiguration *configuration) {
    configuration.logger.level = BRZLoggerLevelInfo;
    configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initWithAutomationEnabled:YES];
  } postInitialization:^(Braze *braze) {
    // Store the Braze instance for later use.
  }];

  /* Other configuration */

  return YES;
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
`BrazeReactInitializer.configure()` speichert nur Ihre Konfiguration. Es existiert keine Braze-Instanz, bis `Braze.initialize()` aus JavaScript aufgerufen wird. Rufen Sie daher nach `configure()` keine Braze-SDK-Methoden im AppDelegate auf.
Wenn Sie `Braze.initialize()` erneut aufrufen, werden dieselben `configure`- und `postInitialization`-Blöcke auf die neue Braze-Instanz angewendet.
{% endalert %}

{% endtab %}
{% tab React Native SDK 19.1.0 und früher %}

#### Methode 1: Verwendung des Expo-Plugins {#method-1-using-the-expo-plugin}

##### Schritt 2.1: Braze Expo-Plugin installieren {#step-21-install-the-braze-expo-plugin}

Stellen Sie sicher, dass Ihre Version des Braze React Native SDK mindestens 1.37.0 ist. Die vollständige Liste der unterstützten Versionen finden Sie im [Braze React Native-Repository](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support).

Der folgende Codeausschnitt zeigt den Befehl zur Installation des Braze Expo-Plugins:

```bash
npx expo install @braze/expo-plugin
```

##### Schritt 2.2: Plugin zur app.json hinzufügen {#step-22-add-the-plugin-to-your-appjson}

Fügen Sie in Ihrer `app.json` das Braze Expo-Plugin hinzu. Sie können die folgenden Konfigurationsoptionen angeben:

| Methode                                       | Typ     | Beschreibung                                                                                                                                             |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `androidApiKey`                               | string  | Erforderlich. Der [API-Schlüssel]({{site.baseurl}}/api/identifier_types) für Ihre Android-Anwendung, zu finden in Ihrem Braze-Dashboard unter **Einstellungen verwalten**. |
| `iosApiKey`                                   | string  | Erforderlich. Der [API-Schlüssel]({{site.baseurl}}/api/identifier_types) für Ihre iOS-Anwendung, zu finden in Ihrem Braze-Dashboard unter **Einstellungen verwalten**.     |
| `baseUrl`                                     | string  | Erforderlich. Der [SDK-Endpunkt]({{site.baseurl}}/api/basics#endpoints) für Ihre Anwendung, zu finden in Ihrem Braze-Dashboard unter **Einstellungen verwalten**.    |
| `enableBrazeIosPush`                          | boolean | Nur iOS. Ob Braze für die Verarbeitung von Push-Benachrichtigungen auf iOS verwendet werden soll. Eingeführt in React Native SDK v1.38.0 und Expo Plugin v0.4.0.                       |
| `enableFirebaseCloudMessaging`                | boolean | Nur Android. Ob Firebase Cloud Messaging für Push-Benachrichtigungen verwendet werden soll. Eingeführt in React Native SDK v1.38.0 und Expo Plugin v0.4.0.             |
| `firebaseCloudMessagingSenderId`              | string  | Nur Android. Ihre Firebase Cloud Messaging-Sender-ID. Eingeführt in React Native SDK v1.38.0 und Expo Plugin v0.4.0.                                    |
| `sessionTimeout`                              | integer | Das Braze-Sitzungs-Timeout für Ihre Anwendung in Sekunden.                                                                                               |
| `enableSdkAuthentication`                     | boolean | Ob das Feature [SDK-Authentifizierung]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication) aktiviert werden soll.      |
| `logLevel`                                    | integer | Die Protokollierungsstufe für Ihre Anwendung. Die Standard-Protokollierungsstufe ist 8 und protokolliert minimal Info-Meldungen. Verwenden Sie für ausführliche Protokollierung zum Debugging die Protokollierungsstufe 0.    |
| `minimumTriggerIntervalInSeconds`             | integer | Das minimale Zeitintervall in Sekunden zwischen Triggern. Standardmäßig 30 Sekunden.                                                                           |
| `enableAutomaticLocationCollection`           | boolean | Ob die automatische Standorterfassung aktiviert ist (sofern der/die Nutzer:in zustimmt).                                                                                  |
| `enableGeofence`                              | boolean | Ob Geofences aktiviert sind.                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | boolean | Ob Geofence-Anfragen automatisch gestellt werden sollen.                                                                                                  |
| `dismissModalOnOutsideTap`                    | boolean | Nur iOS. Ob eine modale In-App-Nachricht geschlossen wird, wenn der/die Nutzer:in außerhalb der In-App-Nachricht tippt.                                           |
| `androidHandlePushDeepLinksAutomatically`     | boolean | Nur Android. Ob das Braze SDK Deeplinks aus Push-Benachrichtigungen automatisch verarbeiten soll.                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | boolean | Nur Android. Legt fest, ob der Textinhalt einer Push-Benachrichtigung als HTML mit `android.text.Html.fromHtml` interpretiert und gerendert werden soll.        |
| `androidNotificationAccentColor`              | string  | Nur Android. Legt die Akzentfarbe für Android-Benachrichtigungen fest.                                                                                                |
| `androidNotificationLargeIcon`                | string  | Nur Android. Legt das große Symbol für Android-Benachrichtigungen fest.                                                                                                  |
| `androidNotificationSmallIcon`                | string  | Nur Android. Legt das kleine Symbol für Android-Benachrichtigungen fest.                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | boolean | Nur iOS. Ob der/die Nutzer:in beim App-Start automatisch nach Push-Berechtigungen gefragt werden soll.                                                          |
| `enableBrazeIosRichPush`                      | boolean | Nur iOS. Ob Rich-Push-Features für iOS aktiviert werden sollen.                                                                                                  |
| `enableBrazeIosPushStories`                   | boolean | Nur iOS. Ob Braze Push Stories für iOS aktiviert werden sollen.                                                                                                  |
| `iosPushStoryAppGroup`                        | string  | Nur iOS. Die App-Gruppe für iOS Push Stories.                                                                                                       |
| `iosUseUUIDAsDeviceId`                        | boolean | Nur iOS. Ob die Geräte-ID eine zufällig generierte UUID verwendet.                                                                                       |
| `iosForwardUniversalLinks`                    | boolean | Nur iOS. Gibt an, ob das SDK Universal Links automatisch erkennen und an die Systemmethoden weiterleiten soll (Standard: `false`). Wenn aktiviert, leitet das SDK Universal Links automatisch an die in [Supporting universal links in your app](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks/) definierten Systemmethoden weiter. Eingeführt in React Native SDK v11.1.0 und Expo Plugin v3.2.0. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Schritt 2.2: Plugin zur app.json hinzufügen" }

Der folgende Codeausschnitt zeigt eine beispielhafte `app.json`-Konfiguration:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY",
          "baseUrl": "YOUR-SDK-ENDPOINT",
          "sessionTimeout": 60,
          "enableGeofence": false,
          "enableBrazeIosPush": false,
          "enableFirebaseCloudMessaging": false,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true,
          "enableSdkAuthentication": false,
          "logLevel": 0,
          "minimumTriggerIntervalInSeconds": 0,
          "enableAutomaticLocationCollection": false,
          "enableAutomaticGeofenceRequests": false,
          "dismissModalOnOutsideTap": true,
          "androidPushNotificationHtmlRenderingEnabled": true,
          "androidNotificationAccentColor": "#ff3344",
          "androidNotificationLargeIcon": "@drawable/custom_app_large_icon",
          "androidNotificationSmallIcon": "@drawable/custom_app_small_icon",
          "iosRequestPushPermissionsAutomatically": false,
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.example.myapp.PushStories",
          "iosForwardUniversalLinks": false
        }
      ],
    ]
  }
}
```

###### Konfiguration von Android-Push-Benachrichtigungssymbolen {#configuring-android-push-notification-icons}

Wenn Sie `androidNotificationLargeIcon` und `androidNotificationSmallIcon` verwenden, beachten Sie die folgenden Best Practices für die korrekte Symboldarstellung:

**Platzierung und Format der Symbole**

Um benutzerdefinierte Push-Benachrichtigungssymbole mit dem Braze Expo-Plugin zu verwenden:

1. Erstellen Sie Ihre Symboldateien gemäß den unten aufgeführten Symbolanforderungen.
2. Legen Sie sie in den nativen Android-Verzeichnissen Ihres Projekts unter `android/app/src/main/res/drawable-<density>/` ab (z. B. `android/app/src/main/res/drawable-mdpi/`, `drawable-hdpi/` oder ähnlich).
3. Alternativ können Sie, wenn Sie Assets in Ihrem React-Native-Verzeichnis verwalten, Expos [app.json-Symbolkonfiguration](https://docs.expo.dev/versions/latest/config/app/#icon) verwenden oder ein [Expo Config Plugin](https://docs.expo.dev/config-plugins/introduction/) erstellen, um die Symbole während des Prebuilds in die Android-Drawable-Ordner zu kopieren.

Das Braze Expo-Plugin referenziert diese Symbole über Androids Drawable-Ressourcensystem.

**Symbolanforderungen**

- **Kleines Symbol:** Muss eine weiße Silhouette auf transparentem Hintergrund sein (dies ist eine Anforderung der Android-Plattform)
- **Großes Symbol:** Kann ein Vollfarbbild sein.
- **Format:** PNG-Format wird empfohlen.
- **Benennung:** Verwenden Sie nur Kleinbuchstaben, Zahlen und Unterstriche (z. B. `my_large_icon.png`)

**Konfiguration in app.json**

Der folgende Codeausschnitt zeigt, wie Sie Android-Benachrichtigungssymbole in der `app.json` mit dem Präfix `@drawable/` referenzieren:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidNotificationLargeIcon": "@drawable/large_icon",
          "androidNotificationSmallIcon": "@drawable/small_icon"
        }
      ]
    ]
  }
}
```

{% alert important %}
Verwenden Sie keine relativen Dateipfade (wie `src/assets/images/icon.png`) und geben Sie nicht die Dateierweiterung an, wenn Sie Symbole referenzieren. Das Expo-Plugin erfordert das Präfix `@drawable/`, um die Symbole nach dem Prebuild-Prozess korrekt in den nativen Android-Ordnern zu finden.
{% endalert %}

**Funktionsweise**

Das Braze Expo-Plugin referenziert Ihre Symboldateien aus den Android-`drawable`-Verzeichnissen. Wenn Sie `npx expo prebuild` ausführen, generiert Expo die native Android-Projektstruktur. Ihre Symbole müssen vor dem Build-Prozess in den Android-`drawable`-Ordnern vorhanden sein (entweder manuell platziert oder über ein Config Plugin kopiert). Das Plugin konfiguriert dann das Braze SDK so, dass es diese Drawable-Ressourcen anhand ihrer Namen (ohne Pfad oder Erweiterung) verwendet – deshalb ist das Präfix `@drawable/` in Ihrer Konfiguration erforderlich.

Weitere Informationen zu Android-Benachrichtigungssymbolen finden Sie in [Androids Richtlinien für Benachrichtigungssymbole](https://developer.android.com/develop/ui/views/notifications#icon).

##### Schritt 2.3: Anwendung erstellen und ausführen {#step-23-build-and-run-your-application}

Beim Prebuilding Ihrer Anwendung werden die nativen Dateien generiert, die für das Braze Expo-Plugin erforderlich sind.

Der folgende Codeausschnitt zeigt den Befehl zum Prebuilding Ihrer Anwendung:

```bash
npx expo prebuild
```

Führen Sie Ihre Anwendung wie in der [Expo-Dokumentation](https://docs.expo.dev/workflow/customizing/) beschrieben aus. Beachten Sie, dass Sie bei Änderungen an den Konfigurationsoptionen Prebuild und Anwendung erneut ausführen müssen.

#### Methode 2: Verwendung der React Native CLI {#method-2-using-react-native-cli}

##### Android einrichten

**Schritt 2.1: Kotlin-Gradle-Plugin hinzufügen**

Der folgende Codeausschnitt zeigt, wie Sie das Kotlin-Gradle-Plugin in der `build.gradle`-Datei Ihres Top-Level-Projekts unter `buildscript` > `dependencies` hinzufügen:

```groovy
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}
```

Dadurch wird Kotlin zu Ihrem Projekt hinzugefügt.

**Schritt 2.2: Braze SDK konfigurieren**

Um eine Verbindung zu den Braze-Servern herzustellen, erstellen Sie eine `braze.xml`-Datei im Ordner `res/values` Ihres Projekts. Der folgende Codeausschnitt zeigt eine beispielhafte `braze.xml`-Konfiguration. Ersetzen Sie den API-[Schlüssel]({{site.baseurl}}/api/identifier_types) und den [Endpunkt]({{site.baseurl}}/api/basics#endpoints) durch Ihre Werte:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOU_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

Der folgende Codeausschnitt zeigt die erforderlichen Berechtigungen für Ihre `AndroidManifest.xml`-Datei:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
Ab Braze Android SDK Version 12.2.0 können Sie die android-sdk-location-Bibliothek automatisch einbinden, indem Sie `importBrazeLocationLibrary=true` in Ihrer `gradle.properties`-Datei festlegen.
{% endalert %}

**Schritt 2.3: Nutzer:innen-Sitzungsverfolgung implementieren**

Die Aufrufe von `openSession()` und `closeSession()` werden automatisch verarbeitet.
Der folgende Codeausschnitt zeigt, was Sie zur `onCreate()`-Methode Ihrer `MainApplication`-Klasse hinzufügen müssen:

{% subtabs local %}
{% subtab JAVA %}
```java
import com.braze.BrazeActivityLifecycleCallbackListener;

@Override
public void onCreate() {
    super.onCreate();
    ...
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
import com.braze.BrazeActivityLifecycleCallbackListener

override fun onCreate() {
    super.onCreate()
    ...
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
}
```
{% endsubtab %}
{% endsubtabs %}

**Schritt 2.4: Intent-Aktualisierungen verarbeiten**

Wenn Ihre MainActivity `android:launchMode` auf `singleTask` gesetzt hat, zeigt der folgende Codeausschnitt, was Sie zu Ihrer `MainActivity`-Klasse hinzufügen müssen:

{% subtabs local %}
{% subtab JAVA %}
```java
@Override
public void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    setIntent(intent);
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
override fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    setIntent(intent)
}
```
{% endsubtab %}
{% endsubtabs %}

##### iOS einrichten

**Schritt 2.5: (Optional) Podfile für dynamische XCFrameworks konfigurieren**

Um bestimmte Braze-Bibliotheken wie BrazeUI in eine Objective-C++-Datei zu importieren, müssen Sie die `#import`-Syntax verwenden. Ab Version `7.4.0` des Braze Swift SDK verfügen die Binärdateien über einen [optionalen Vertriebskanal als dynamische XCFrameworks](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic), der mit dieser Syntax kompatibel ist.

Wenn Sie diesen Vertriebskanal nutzen möchten, überschreiben Sie die CocoaPods-Quellorte in Ihrem Podfile manuell. Der folgende Codeausschnitt zeigt eine Beispielüberschreibung. Ersetzen Sie `{your-version}` durch die gewünschte Version:

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

**Schritt 2.6: Pods installieren**

Da React Native die Bibliotheken automatisch mit der nativen Plattform verknüpft, können Sie das SDK mithilfe von CocoaPods installieren.

Der folgende Codeausschnitt zeigt, wie Sie Pods aus dem Stammordner des Projekts installieren:

```bash
# To install using the React Native New Architecture
cd ios && pod install

# To install using the React Native legacy architecture
cd ios && RCT_NEW_ARCH_ENABLED=0 pod install
```

**Schritt 2.7: Braze SDK konfigurieren**

{% subtabs local %}
{% subtab SWIFT %}

Der folgende Codeausschnitt zeigt, wie Sie das Braze SDK am Anfang der `AppDelegate.swift`-Datei importieren:
```swift
import BrazeKit
import braze_react_native_sdk
```

Ersetzen Sie in der `application(_:didFinishLaunchingWithOptions:)`-Methode den API-[Schlüssel]({{site.baseurl}}/api/identifier_types) und den [Endpunkt]({{site.baseurl}}/api/basics#endpoints) durch die Werte Ihrer App. Erstellen Sie dann die Braze-Instanz mit der Konfiguration und erstellen Sie eine statische Eigenschaft auf dem `AppDelegate` für einfachen Zugriff.

{% alert note %}
Unser Beispiel setzt eine Implementierung von [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h) voraus, das eine Reihe von Abstraktionen im React-Native-Setup bereitstellt. Wenn Sie ein anderes Setup für Ihre App verwenden, passen Sie Ihre Implementierung entsprechend an.
{% endalert %}

Der folgende Codeausschnitt zeigt ein beispielhaftes `AppDelegate.swift`-Setup:

```swift
func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
    // Setup Braze
    let configuration = Braze.Configuration(
        apiKey: "{BRAZE_API_KEY}",
        endpoint: "{BRAZE_ENDPOINT}")
    // Enable logging and customize the configuration here.
    configuration.logger.level = .info
    let braze = BrazeReactBridge.perform(
      #selector(BrazeReactBridge.initBraze(_:)),
      with: configuration
    ).takeUnretainedValue() as! Braze

    AppDelegate.braze = braze

    /* Other configuration */

    return true
}

// MARK: - AppDelegate.braze

static var braze: Braze? = nil
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Der folgende Codeausschnitt zeigt, wie Sie das Braze SDK am Anfang der `AppDelegate.m`-Datei importieren:
```objc
#import <BrazeKit/BrazeKit-Swift.h>
#import "BrazeReactBridge.h"
```

Ersetzen Sie in der `application:didFinishLaunchingWithOptions:`-Methode den API-[Schlüssel]({{site.baseurl}}/api/identifier_types) und den [Endpunkt]({{site.baseurl}}/api/basics#endpoints) durch die Werte Ihrer App. Erstellen Sie dann die Braze-Instanz mit der Konfiguration und erstellen Sie eine statische Eigenschaft auf dem `AppDelegate` für einfachen Zugriff.

{% alert note %}
Unser Beispiel setzt eine Implementierung von [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h) voraus, das eine Reihe von Abstraktionen im React-Native-Setup bereitstellt. Wenn Sie ein anderes Setup für Ihre App verwenden, passen Sie Ihre Implementierung entsprechend an.
{% endalert %}

Der folgende Codeausschnitt zeigt ein beispielhaftes `AppDelegate.m`-Setup:

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                                                    endpoint:@"{BRAZE_ENDPOINT}"];
  // Enable logging and customize the configuration here.
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  AppDelegate.braze = braze;

  /* Other configuration */

  return YES;
}

#pragma mark - AppDelegate.braze

static Braze *_braze = nil;

+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

### Schritt 3: SDK initialisieren {#step-3-initialize-the-sdk}

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

Der folgende Codeausschnitt zeigt, wie Sie die Bibliothek in Ihrem React-Native-Code importieren:

```javascript
import Braze from "@braze/react-native-sdk";
```

{% alert note %}
React Native SDK 19.2.0+ unterstützt die Initialisierung von Braze sowohl aus der React-Native-Ebene als auch aus den nativen iOS- und Android-Ebenen. Initialisieren Sie aus der React-Native-Ebene, um die [verzögerte Initialisierung](#delayed-initialization) zu nutzen, die das SDK erst nach einem Ereignis wie Einwilligung oder Anmeldung startet. Wenn Ihre App Braze heute in den nativen Ebenen initialisiert, können Sie dieses Setup beim Upgrade beibehalten. Informationen zum Verhalten von Benachrichtigungen in den jeweiligen Setups finden Sie unter [Push-Benachrichtigungen beim Kaltstart](#push-notifications-on-cold-start).
{% endalert %}

Rufen Sie dann `Braze.initialize()` mit Ihrem App-Bezeichner-API-Schlüssel und dem SDK-Endpunkt auf, um die Braze-Instanz zu erstellen. Im Folgenden finden Sie die Optionen, wo Sie diese Methode in Ihrem App-Ablauf aufrufen können.

#### Standard-Initialisierung {#standard-initialization}

Der folgende Codeausschnitt zeigt, wie Sie das SDK beim App-Start initialisieren, indem Sie `Braze.initialize()` in einem `useEffect` aufrufen:

```javascript
import React, { useEffect } from "react";
import Braze from "@braze/react-native-sdk";

const App = () => {
  useEffect(() => {
    Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
  }, []);

  return (
    // Your app components
  );
};
```

#### Verzögerte Initialisierung {#delayed-initialization}

Der folgende Codeausschnitt zeigt, wie Sie die SDK-Initialisierung auf einen späteren Zeitpunkt in der Sitzung verschieben, z. B. nachdem der/die Nutzer:in die Einwilligung erteilt hat oder die Anmeldung abgeschlossen ist:

```javascript
function onUserConsent() {
  Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
}
```

{% alert warning %}
Unter iOS werden Push-Benachrichtigungen, die vor `Braze.initialize()` empfangen werden, in eine Warteschlange gestellt und nach der Initialisierung verarbeitet. Unter Android löst Braze keine Deeplinks aus Push-Benachrichtigungen auf, während das SDK auf die Initialisierung wartet. Damit Benachrichtigungen weiterhin funktionieren, wenn eine davon Ihre App startet, lesen Sie [Push-Benachrichtigungen beim Kaltstart](#push-notifications-on-cold-start).
{% endalert %}

#### Plattformspezifische API-Schlüssel {#platform-specific-api-keys}

Der folgende Codeausschnitt zeigt, wie Sie die Plattformerkennung verwenden, wenn Ihre Android- und iOS-Apps unterschiedliche API-Schlüssel verwenden:

```javascript
import { Platform } from "react-native";
import Braze from "@braze/react-native-sdk";

const apiKey = Platform.select({
  android: "YOUR-ANDROID-API-KEY",
  ios: "YOUR-IOS-API-KEY",
}) ?? "";

Braze.initialize(apiKey, "YOUR-SDK-ENDPOINT");
```

#### Erneute Initialisierung {#re-initialization}

Sie können `Braze.initialize()` mehrmals aufrufen, um das SDK mit einem anderen API-Schlüssel und Endpunkt mitten in der Sitzung neu zu initialisieren. Jeder Aufruf entfernt die vorherige Braze-Instanz und erstellt eine neue.

{% alert important %}
Alle SDK-Methodenaufrufe, die vor `Braze.initialize()` erfolgen, werden unter iOS ignoriert. Rufen Sie daher `Braze.initialize()` auf, bevor Sie andere Braze-Methoden verwenden.
{% endalert %}

#### Push-Benachrichtigungen beim Kaltstart {#push-notifications-on-cold-start}

Wenn eine Benachrichtigung Ihre App aus einem beendeten Zustand startet, speichert Braze die Benachrichtigungsdaten in der nativen Ebene, bevor React Native geladen wird. Daher ändert die Initialisierung aus der React-Native-Ebene nicht, ob die Daten Ihre App erreichen. Um diese Benachrichtigungen zu verarbeiten, fügen Sie die nativen Hooks hinzu und lesen Sie die Daten dann in Ihrem React-Native-Code.

Rufen Sie unter Android `BrazeReactUtils.populateInitialPushPayloadFromIntent(intent)` in der `onCreate()`-Methode Ihrer `MainActivity`-Klasse auf:

```kotlin
import com.braze.reactbridge.BrazeReactUtils

override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    BrazeReactUtils.populateInitialPushPayloadFromIntent(intent)
}
```

Rufen Sie unter iOS `populateInitialPayload(fromLaunchOptions:)` in der `application(_:didFinishLaunchingWithOptions:)`-Methode Ihres `AppDelegate` auf:

```swift
if let launchOptions {
  BrazeReactUtils.sharedInstance().populateInitialPayload(fromLaunchOptions: launchOptions)
}
```

Lesen Sie dann die Daten in Ihrem React-Native-Code:

```javascript
Braze.getInitialPushPayload((pushPayload) => {
  if (pushPayload) {
    // Handle the notification, such as navigating to the pushPayload.url value
  }
});
```

{% alert important %}
Wenn die verzögerte Initialisierung unter Android aktiviert ist, öffnet Braze Ihre Hauptaktivität anstatt den Deeplink in der Benachrichtigung aufzulösen und übergibt die Benachrichtigungsdaten an diese Aktivität. Verarbeiten Sie die Navigation in Ihrem React-Native-Code mithilfe des `url`-Werts aus `Braze.getInitialPushPayload()`.
{% endalert %}

Ihre Push-Registrierungseinstellungen verbleiben in Ihrer nativen Konfiguration für beide Initialisierungsorte, und Braze wendet sie an, wenn `Braze.initialize()` ausgeführt wird:

- Unter Android legen Sie `com_braze_firebase_cloud_messaging_registration_enabled` und `com_braze_firebase_cloud_messaging_sender_id` in `braze.xml` fest.
- Unter iOS legen Sie die `push`-Eigenschaften am Konfigurationsobjekt im `configure`-Closure fest, den Sie an `BrazeReactInitializer.configure` übergeben.

Wenn Ihre App auf Deeplinks aus Benachrichtigungen angewiesen ist, die sie aus einem beendeten Zustand starten, verwenden Sie React Native SDK 21.1.0 oder höher. Diese Versionen enthalten Fehlerbehebungen für das Erfassen der initialen Push-Daten und das Auflösen von Push-Deeplinks unter Android. Die vollständige Liste der Änderungen finden Sie im [React Native SDK Changelog](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md).

{% endtab %}
{% tab React Native SDK 19.1.0 und früher %}

Für React Native SDK 19.1.0 und früher erfolgt die native Initialisierung in Schritt 2. Importieren Sie die Bibliothek in Ihrem React-Native-Code, um Braze-Methoden aufzurufen. Weitere Details finden Sie in unserem [Beispielprojekt](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject).

```javascript
import Braze from "@braze/react-native-sdk";
```

{% endtab %}
{% endtabs %}

### Schritt 4: Integration testen (optional) {#step-4-test-the-integration-optional}

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

Sie können überprüfen, ob das SDK integriert ist, indem Sie die Sitzungsstatistiken im Dashboard prüfen. Wenn Sie Ihre Anwendung auf einer der beiden Plattformen ausführen, sollten Sie eine neue Sitzung im Dashboard sehen (im Abschnitt **Übersicht**).

Der folgende Codeausschnitt zeigt, wie Sie eine Sitzung für eine/n bestimmte/n Nutzer:in in Ihrer App öffnen:

```javascript
import Braze from "@braze/react-native-sdk";

Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
Braze.changeUser("{some-user-id}");
```

Suchen Sie nach dem/der Nutzer:in mit `{some-user-id}` im Dashboard unter **Zielgruppe** > **Nutzersuche**. Dort können Sie überprüfen, ob Sitzungs- und Gerätedaten protokolliert wurden.

{% endtab %}
{% tab React Native SDK 19.1.0 und früher %}

Um Ihre SDK-Integration zu testen, zeigt der folgende Codeausschnitt, wie Sie auf einer der beiden Plattformen eine neue Sitzung für eine/n Nutzer:in starten.

```javascript
Braze.changeUser("userId");
```

Der folgende Codeausschnitt zeigt ein Beispiel für die Zuweisung der Nutzer-ID beim App-Start:

```javascript
import React, { useEffect } from "react";
import Braze from "@braze/react-native-sdk";

const App = () => {
  useEffect(() => {
    Braze.changeUser("some-user-id");
  }, []);

  return (
    <div>
      ...
    </div>
  )
```

Gehen Sie im Braze-Dashboard zu [Nutzersuche]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search#using-user-search) und suchen Sie nach dem/der Nutzer:in mit der ID `some-user-id`. Dort können Sie überprüfen, ob Sitzungs- und Gerätedaten protokolliert wurden.

{% endtab %}
{% endtabs %}

## Testen mit Jest {#testing-with-jest}

React-Native-Unit-Tests, die das Braze SDK importieren, benötigen Mocks für native Module und das Braze Turbo Module. Das [Braze React Native SDK-Repository](https://github.com/braze-inc/braze-react-native-sdk) enthält ein Referenz-Jest-Setup in [`__tests__/jest.setup.js`](https://github.com/braze-inc/braze-react-native-sdk/blob/master/__tests__/jest.setup.js). Fügen Sie diese Datei (oder eine angepasste Kopie) zu `setupFiles` in Ihrer Jest-Konfiguration hinzu, damit `NativeEventEmitter`, `TurboModuleRegistry` und `BrazeReactBridge` gemockt werden, wenn Sie Komponenten testen, die Braze-APIs aufrufen.

## Nächste Schritte {#next-steps}

Nach der Integration des Braze SDK können Sie mit der Implementierung gängiger Messaging-Features beginnen:

- [Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications): Richten Sie Push-Benachrichtigungen ein und senden Sie diese an Ihre Nutzer:innen.
- [In-App Messages]({{site.baseurl}}/developer_guide/in_app_messages): Zeigen Sie kontextuelle Nachrichten innerhalb Ihrer App an.
- [Banner]({{site.baseurl}}/developer_guide/banners): Zeigen Sie persistente Banner in der Benutzeroberfläche Ihrer App an.