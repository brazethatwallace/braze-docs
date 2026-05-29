{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Push-Benachrichtigungen einrichten {#setting-up-push-notification}

### 1. Schritt: Plattform einrichten {#step-1-set-up-the-platform}

{% tabs %}
{% tab Android %}
#### Schritt 1.1: Firebase aktivieren {#step-11-enable-firebase}

Um loszulegen, folgen Sie der [Dokumentation zur Einrichtung von Firebase Unity](https://firebase.google.com/docs/unity/setup).

{% alert note %}
Durch die Integration des Firebase Unity SDK kann Ihre `AndroidManifest.xml` überschrieben werden. Stellen Sie in diesem Fall sicher, dass Sie die ursprüngliche Datei wiederherstellen.
{% endalert %}

#### Schritt 1.2: Firebase-Zugangsdaten festlegen {#step-12-set-your-firebase-credentials}

Sie müssen den Firebase-Serverschlüssel und die Sender-ID in das Braze-Dashboard eingeben. Melden Sie sich dazu in der [Firebase Developers Console](https://console.firebase.google.com/) an und wählen Sie Ihr Firebase-Projekt aus. Wählen Sie dann unter **Settings** die Option **Cloud Messaging** und kopieren Sie den Serverschlüssel und die Sender-ID:<br>![]({% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey")

Wählen Sie in Braze Ihre Android-App auf der Seite **App-Einstellungen** unter **Einstellungen verwalten** aus. Geben Sie anschließend Ihren Firebase-Serverschlüssel in das Feld **Firebase Cloud Messaging Server Key** und die Firebase-Sender-ID in das Feld **Firebase Cloud Messaging Sender** ID ein.

![]({% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey")
{% endtab %}

{% tab Swift %}
#### Schritt 1.1: Integrationsmethode überprüfen {#step-11-verify-integration-method}

Braze bietet eine native Unity-Lösung für die Automatisierung von iOS-Push-Integrationen. Wenn Sie Ihre Integration stattdessen manuell einrichten und verwalten möchten, lesen Sie [Swift: Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

Andernfalls fahren Sie mit dem nächsten Schritt fort.

{% alert note %}
Unsere Lösung für automatische Push-Benachrichtigungen nutzt die Funktion „Provisorische Autorisierung“ von iOS 12 und kann nicht mit dem nativen Push-Prompt-Pop-up verwendet werden.
{% endalert %}
{% endtab %}

{% tab Amazon Device Messaging %}
#### Schritt 1.1: ADM aktivieren {#step-11-enable-adm}

1. Erstellen Sie ein Konto im [Amazon Apps & Games Developer Portal](https://developer.amazon.com/public), falls Sie dies noch nicht getan haben.
2. Holen Sie sich die [OAuth-Zugangsdaten (Client-ID und Client Secret) und einen ADM-API-Schlüssel](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).
3. Aktivieren Sie **Automatic ADM Registration Enabled** im Unity-Braze-Konfigurationsfenster.
  - Alternativ können Sie die folgende Zeile in Ihre `res/values/braze.xml`-Datei einfügen, um die ADM-Registrierung zu aktivieren:

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```
{% endtab %}
{% endtabs %}

### 2. Schritt: Push-Benachrichtigungen konfigurieren {#step-2-configure-push-notifications}

{% tabs %}
{% tab Android %}
#### Schritt 2.1: Push-Einstellungen konfigurieren {#unity_step-21-configure-push-settings}

Das Braze SDK kann die Push-Registrierung bei den Firebase Cloud Messaging-Servern automatisch übernehmen, damit Geräte Push-Benachrichtigungen empfangen können. Aktivieren Sie in Unity **Automate Unity Android Integration** und konfigurieren Sie dann die folgenden **Push Notification**-Einstellungen.

| Einstellung | Beschreibung |
|---|---|
| Automatic Firebase Cloud Messaging Registration Enabled | Weist das Braze SDK an, automatisch ein FCM-Push-Token für ein Gerät abzurufen und zu senden. |
| Firebase Cloud Messaging Sender ID | Die Sender-ID aus Ihrer Firebase-Konsole. |
| Handle Push Deeplinks Automatically | Gibt an, ob das SDK das Öffnen von Deeplinks oder das Öffnen der App beim Klicken auf Push-Benachrichtigungen verarbeiten soll. |
| Small Notification Icon Drawable | Android-Drawable-Ressourcenreferenz für das kleine Symbol, das beim Empfang einer Push-Benachrichtigung angezeigt wird. Geben Sie die vollständige Referenz einschließlich des Präfixes `@drawable/` ein (z. B. `@drawable/hourglass_icon`). Die automatisierte Integration schreibt diesen Wert wie eingegeben in `braze.xml`. Wenn Sie dieses Feld leer lassen, verwendet die Benachrichtigung das Anwendungssymbol als kleines Symbol. |
| Large Notification Icon Drawable | Optionales großes Symbol für Benachrichtigungen. Verwenden Sie dasselbe `@drawable/`-Format wie beim kleinen Symbol (z. B. `@drawable/my_large_icon`). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2.1: Configure push settings" }

{% alert note %}
**Small Notification Icon Drawable** und **Large Notification Icon Drawable** befinden sich unter **Push Configuration** in **Braze > Braze Configuration**. Beide Werte werden wie eingegeben in `braze.xml` geschrieben. Fügen Sie das Präfix `@drawable/` selbst hinzu – die Braze-Unity-Integration ergänzt es nicht automatisch (z. B. `<drawable name="com_braze_push_small_notification_icon">@drawable/hourglass_icon</drawable>`).
{% endalert %}
{% endtab %}

{% tab Swift %}
#### Schritt 2.1: APNs-Token hochladen {#step-21-upload-your-apns-token}

{% multi_lang_include developer_guide/swift/apns_token.md %}

#### Schritt 2.2: Automatischen Push aktivieren {#step-22-enable-automatic-push}

Öffnen Sie die Braze-Konfigurationseinstellungen im Unity-Editor, indem Sie zu **Braze > Braze Configuration** navigieren.

Aktivieren Sie **Integrate Push With Braze**, um Nutzer:innen automatisch für Push-Benachrichtigungen zu registrieren, Push-Token an Braze weiterzugeben, Analytics für Push-Öffnungen zu verfolgen und die Vorteile unserer standardmäßigen Push-Benachrichtigungsverarbeitung zu nutzen.

#### Schritt 2.3: Hintergrund-Push aktivieren (optional) {#step-23-enable-background-push-optional}

Aktivieren Sie **Enable Background Push**, wenn Sie `background mode` für Push-Benachrichtigungen aktivieren möchten. Dadurch kann das System Ihre Anwendung aus dem Zustand `suspended` aufwecken, wenn eine Push-Benachrichtigung eintrifft, sodass Ihre Anwendung als Reaktion auf Push-Benachrichtigungen Inhalte herunterladen kann. Das Aktivieren dieser Option ist für unsere Uninstall-Tracking-Funktion erforderlich.

![Der Unity-Editor zeigt die Braze-Konfigurationsoptionen an. In diesem Editor sind die Optionen „Automate Unity iOS integration“, „Integrate push with braze“ und „Enable background push“ aktiviert.]({% image_buster /assets/img/unity/ios/unity_ios_enable_background.png %})

#### Schritt 2.4: Automatische Registrierung deaktivieren (optional) {#step-24-disable-automatic-registration-optional}

Nutzer:innen, die sich noch nicht für Push-Benachrichtigungen entschieden haben, werden beim Öffnen Ihrer Anwendung automatisch für Push autorisiert. Um diese Funktion zu deaktivieren und Nutzer:innen manuell für Push zu registrieren, aktivieren Sie **Disable Automatic Push Registration**.

- Wenn **Disable Provisional Authorization** unter iOS 12 oder höher nicht aktiviert ist, werden Nutzer:innen vorläufig (stillschweigend) für den Empfang stiller Push-Benachrichtigungen autorisiert. Wenn diese Option aktiviert ist, wird den Nutzer:innen der native Push-Prompt angezeigt.
- Wenn Sie genau konfigurieren möchten, wann der Prompt zur Laufzeit angezeigt werden soll, deaktivieren Sie die automatische Registrierung im Braze-Konfigurationseditor und verwenden Sie stattdessen `AppboyBinding.PromptUserForPushPermissions()`.

![Der Unity-Editor zeigt die Braze-Konfigurationsoptionen an. In diesem Editor sind die Optionen „Automate Unity iOS integration“, „Integrate push with braze“ und „Disable automatic push registration“ aktiviert.]({% image_buster /assets/img/unity/ios/unity_ios_disable_auto_push.png %})
{% endtab %}

{% tab Amazon Device Messaging %}
#### Schritt 2.1: `AndroidManifest.xml` aktualisieren {#unity_step-21-update-androidmanifestxml}

Wenn Ihre App keine `AndroidManifest.xml` hat, können Sie die folgende Vorlage verwenden. Wenn Sie bereits eine `AndroidManifest.xml` haben, stellen Sie sicher, dass alle fehlenden Abschnitte zu Ihrer bestehenden `AndroidManifest.xml` hinzugefügt werden.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />
  <permission
    android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE"
    android:protectionLevel="signature" />
  <uses-permission android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE" />
  <uses-permission android:name="com.amazon.device.messaging.permission.RECEIVE" />

  <application android:icon="@drawable/app_icon"
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity"
      android:label="@string/app_name"
      android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen"
      android:screenOrientation="sensor">
      <meta-data android:name="android.app.lib_name" android:value="unity" />
      <meta-data android:name="unityplayer.ForwardNativeEventsToDalvik" android:value="true" />
      <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
      </intent-filter>
    </activity>

    <receiver android:name="com.braze.push.BrazeAmazonDeviceMessagingReceiver" android:permission="com.amazon.device.messaging.permission.SEND">
      <intent-filter>
          <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
          <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
          <category android:name="REPLACE_WITH_YOUR_PACKAGE_NAME" />
      </intent-filter>
    </receiver>
  </application>
</manifest>
```

#### Schritt 2.2: ADM-API-Schlüssel speichern {#step-22-store-your-adm-api-key}

Zunächst [generieren Sie einen ADM-API-Schlüssel für Ihre App](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials) und speichern den Schlüssel in einer Datei namens `api_key.txt`. Fügen Sie diese dann in das [`Assets/`](https://docs.unity3d.com/Manual/AndroidAARPlugins.html)-Verzeichnis Ihres Projekts ein.

{% alert important %}
Amazon erkennt Ihren Schlüssel nicht, wenn `api_key.txt` Leerzeichen enthält, z. B. einen Zeilenumbruch am Ende.
{% endalert %}

Fügen Sie anschließend in Ihrer `mainTemplate.gradle`-Datei Folgendes hinzu:

```gradle
task copyAmazon(type: Copy) {
    def unityProjectPath = $/file:///**DIR_UNITYPROJECT**/$.replace("\\", "/")
    from unityProjectPath + '/Assets/api_key.txt'
    into new File(projectDir, 'src/main/assets')
}

preBuild.dependsOn(copyAmazon)
```

#### Schritt 2.3: ADM-Jar hinzufügen {#step-23-add-adm-jar}

Die erforderliche ADM-Jar-Datei kann gemäß der [Unity-JAR-Dokumentation](https://docs.unity3d.com/Manual/AndroidJARPlugins.html) an beliebiger Stelle in Ihrem Projekt platziert werden.

#### Schritt 2.4: Client Secret und Client-ID zum Braze-Dashboard hinzufügen {#step-24-add-client-secret-and-client-id-to-your-braze-dashboard}

Abschließend müssen Sie das Client Secret und die Client-ID, die Sie in [Schritt 1](#unity_step-1-enable-adm) erhalten haben, auf der Seite **Einstellungen verwalten** des Braze-Dashboards hinzufügen.

![]({% image_buster /assets/img_archive/fire_os_dashboard.png %})
{% endtab %}
{% endtabs %}

### 3. Schritt: Push-Listener einrichten {#step-3-set-push-listeners}

{% tabs %}
{% tab Android %}
#### Schritt 3.1: Push-Empfangs-Listener aktivieren {#step-31-enable-push-received-listener}

Der Push-Empfangs-Listener wird ausgelöst, wenn Nutzer:innen eine Push-Benachrichtigung empfangen. Um die Push-Nutzlast an Unity zu senden, legen Sie den Namen Ihres Spielobjekts und die Callback-Methode des Push-Empfangs-Listeners unter **Set Push Received Listener** fest.

#### Schritt 3.2: Push-Öffnungs-Listener aktivieren {#step-32-enable-push-opened-listener}

Der Push-Öffnungs-Listener wird ausgelöst, wenn Nutzer:innen die App durch Klicken auf eine Push-Benachrichtigung starten. Um die Push-Nutzlast an Unity zu senden, legen Sie den Namen Ihres Spielobjekts und die Callback-Methode des Push-Öffnungs-Listeners unter **Set Push Opened Listener** fest.

#### Schritt 3.3: Push-Löschungs-Listener aktivieren {#step-33-enable-push-deleted-listener}

Der Push-Löschungs-Listener wird ausgelöst, wenn Nutzer:innen eine Push-Benachrichtigung wegwischen oder verwerfen. Um die Push-Nutzlast an Unity zu senden, legen Sie den Namen Ihres Spielobjekts und die Callback-Methode des Push-Löschungs-Listeners unter **Set Push Deleted Listener** fest.

#### Beispiel für Push-Listener {#push-listener-example}

Das folgende Beispiel implementiert das Spielobjekt `BrazeCallback` mit den Callback-Methoden `PushNotificationReceivedCallback`, `PushNotificationOpenedCallback` bzw. `PushNotificationDeletedCallback`.

![Diese Beispielgrafik zur Implementierung zeigt die in den vorangegangenen Abschnitten erwähnten Braze-Konfigurationsoptionen und ein C#-Code-Snippet.]({% image_buster /assets/img/unity/android/unity_android_full_push_listener.png %} "Android Full Listener Example")

```csharp
public class MainMenu : MonoBehaviour {
  void PushNotificationReceivedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationReceivedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification received: " + pushNotification);
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push received Notification event: " + pushNotification);
#endif
  }

  void PushNotificationOpenedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationOpenedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification opened: " + pushNotification);
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push opened Notification event: " + pushNotification);
#endif
  }

  void PushNotificationDeletedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationDeletedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification dismissed: " + pushNotification);
#endif
  }
}
```
{% endtab %}

{% tab Swift %}
#### Schritt 3.1: Push-Empfangs-Listener aktivieren

Der Push-Empfangs-Listener wird ausgelöst, wenn Nutzer:innen eine Push-Benachrichtigung empfangen, während sie die Anwendung aktiv nutzen (z. B. wenn sich die App im Vordergrund befindet). Legen Sie den Push-Empfangs-Listener im Braze-Konfigurationseditor fest. Wenn Sie den Spielobjekt-Listener zur Laufzeit konfigurieren müssen, verwenden Sie `AppboyBinding.ConfigureListener()` und geben Sie `BrazeUnityMessageType.PUSH_RECEIVED` an.

![Der Unity-Editor zeigt die Braze-Konfigurationsoptionen an. In diesem Editor wird die Option „Set Push Received Listener“ erweitert und der „Game Object Name“ (AppBoyCallback) sowie der „Callback Method Name“ (PushNotificationReceivedCallback) angegeben.]({% image_buster /assets/img/unity/ios/unity_ios_push_received.png %})

#### Schritt 3.2: Push-Öffnungs-Listener aktivieren

Der Push-Öffnungs-Listener wird ausgelöst, wenn Nutzer:innen die App durch Klicken auf eine Push-Benachrichtigung starten. Um die Push-Nutzlast an Unity zu senden, legen Sie den Namen Ihres Spielobjekts und die Callback-Methode des Push-Öffnungs-Listeners unter der Option **Set Push Opened Listener** fest:

![Der Unity-Editor zeigt die Braze-Konfigurationsoptionen an. In diesem Editor wird die Option „Set Push Opened Listener“ erweitert und der „Game Object Name“ (AppBoyCallback) sowie der „Callback Method Name“ (PushNotificationOpenedCallback) angegeben.]({% image_buster /assets/img/unity/ios/unity_ios_push_opened.png %})

Wenn Sie den Spielobjekt-Listener zur Laufzeit konfigurieren müssen, verwenden Sie `AppboyBinding.ConfigureListener()` und geben Sie `BrazeUnityMessageType.PUSH_OPENED` an.

#### Beispiel für Push-Listener

Das folgende Beispiel implementiert das Spielobjekt `AppboyCallback` mit den Callback-Methoden `PushNotificationReceivedCallback` bzw. `PushNotificationOpenedCallback`.

![Diese Beispielgrafik zur Implementierung zeigt die in den vorangegangenen Abschnitten erwähnten Braze-Konfigurationsoptionen und ein C#-Code-Snippet.]({% image_buster /assets/img/unity/ios/unity_ios_appboy_callback.png %})

```csharp
public class MainMenu : MonoBehaviour {
  void PushNotificationReceivedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationReceivedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification received: " + pushNotification);
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push received Notification event: " + pushNotification);
#endif
  }

  void PushNotificationOpenedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationOpenedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification opened: " + pushNotification);
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push opened Notification event: " + pushNotification);
#endif
  }
}
```
{% endtab %}

{% tab Amazon Device Messaging %}
Durch das Aktualisieren Ihrer `AndroidManifest.xml` im [vorherigen Schritt](#unity_step-21-update-androidmanifestxml) wurden Push-Listener automatisch eingerichtet, als Sie die folgenden Zeilen hinzugefügt haben. Es ist also keine weitere Einrichtung erforderlich.

```xml
<action android:name="com.amazon.device.messaging.intent.RECEIVE" />
<action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
```

{% alert note %}
Weitere Informationen zu ADM-Push-Listenern finden Sie unter [Amazon: Amazon Device Messaging integrieren](https://developer.amazon.com/docs/video-skills-fire-tv-apps/integrate-adm.html).
{% endalert %}
{% endtab %}
{% endtabs %}

## Optionale Konfigurationen {#optional-configurations}

{% tabs %}
{% tab Android %}
#### Deeplinking zu In-App-Ressourcen {#deep-linking-to-in-app-resources}

Obwohl Braze standardmäßig Standard-Deeplinks (wie Website-URLs, Android-URIs usw.) verarbeiten kann, ist für die Erstellung angepasster Deeplinks eine zusätzliche Manifest-Einrichtung erforderlich.

Eine Anleitung zur Einrichtung finden Sie unter [Deeplinking zu In-App-Ressourcen](https://developer.android.com/training/app-links/deep-linking).

#### Braze-Push-Benachrichtigungssymbole hinzufügen {#adding-braze-push-notification-icons}

{% alert important %}
Fügen Sie keine Benachrichtigungssymbol-Bilder unter `Assets/Plugins/Android/res` hinzu. Unity hat [die Bereitstellung von Android-Ressourcen in diesem Pfad als veraltet markiert](https://support.unity.com/hc/en-us/articles/115005875443-Providing-Android-resources-in-Assets-Plugins-Android-res-is-deprecated), was zu Build-Warnungen oder Validierungsfehlern führen kann. Packen Sie Ihre Symbol-Drawables stattdessen in ein [Android-Archive-Plug-in (AAR)](https://docs.unity3d.com/Manual/AndroidAARPlugins.html) oder ein Android-Bibliotheksprojekt, damit sie wie jedes andere Drawable in die Ressourcen der erstellten App eingebunden werden.
{% endalert %}

Um Ihrem Projekt Push-Symbole hinzuzufügen, erstellen Sie ein AAR-Plug-in oder eine Android-Bibliothek, die die Bilddateien für die Symbole unter `res/drawable*` (oder dichteabhängigen Ordnern) enthält, und referenzieren Sie jedes Symbol in **Braze > Braze Configuration** mit dem vollständigen `@drawable/`-Ressourcennamen (siehe [Schritt 2.1: Push-Einstellungen konfigurieren](#unity_step-21-configure-push-settings)). Informationen zu den Paketierungs- und Importschritten in Unity finden Sie unter [Android-Library-Projekte und Android-Archive-Plug-ins](https://docs.unity3d.com/Manual/AndroidAARPlugins.html).

Informationen zu den Gestaltungsregeln für kleine Symbole (nur Alpha-Kanal, keine Farbe) finden Sie unter [Android-Push-Benachrichtigungen]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android), Schritt 2: Kleine Symbole an die Designrichtlinien anpassen.
{% endtab %}

{% tab Swift %}
#### Push-Token-Callback

Um eine Kopie der Braze-Geräte-Token vom Betriebssystem zu erhalten, setzen Sie einen Delegaten mit `AppboyBinding.SetPushTokenReceivedFromSystemDelegate()`.
{% endtab %}

{% tab Amazon Device Messaging %}
Derzeit gibt es keine optionalen Konfigurationen für ADM.
{% endtab %}
{% endtabs %}