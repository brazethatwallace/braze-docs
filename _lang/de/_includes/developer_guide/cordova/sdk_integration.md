## Integration des Cordova SDK {#integrating-the-cordova-sdk}

### Voraussetzungen {#prerequisites}

Bevor Sie beginnen, stellen Sie sicher, dass Ihre Umgebung von der [aktuellen Version des Braze Cordova SDK](https://github.com/braze-inc/braze-cordova-sdk?tab=readme-ov-file#minimum-version-requirements) unterstützt wird.

### Schritt 1: SDK zu Ihrem Projekt hinzufügen {#step-1-add-the-sdk-to-your-project}

{% alert warning %}
Fügen Sie das Braze Cordova SDK nur mit den folgenden Methoden hinzu. Versuchen Sie nicht, die Installation mit anderen Methoden durchzuführen, da dies zu einer Sicherheitslücke führen könnte.
{% endalert %}

Wenn Sie Cordova 6 oder höher verwenden, können Sie das SDK direkt von GitHub hinzufügen. Alternativ können Sie eine ZIP-Datei des [GitHub-Repository](https://github.com/braze-inc/braze-cordova-sdk) herunterladen und das SDK manuell hinzufügen.

{% tabs local %}
{% tab Geofence deaktiviert %}
Wenn Sie nicht planen, Standorterfassung und Geofences zu verwenden, nutzen Sie den `master`-Branch von GitHub.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master
```
{% endtab %}

{% tab Geofence aktiviert %}
Wenn Sie planen, Standorterfassung und Geofences zu verwenden, nutzen Sie den `geofence-branch` von GitHub.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```
{% endtab %}
{% endtabs %}

{% alert tip %}
Sie können jederzeit zwischen `master` und `geofence-branch` wechseln, indem Sie diesen Schritt wiederholen.
{% endalert %}

### Schritt 2: Projekt konfigurieren {#step-2-configure-your-project}

Fügen Sie als Nächstes die folgenden Einstellungen zum `platform`-Element in der `config.xml`-Datei Ihres Projekts hinzu.

{% tabs %}
{% tab ios %}
```xml
<preference name="com.braze.ios_api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.ios_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}

{% tab android %}
```xml
<preference name="com.braze.android_api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.android_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}
{% endtabs %}

Ersetzen Sie die folgenden Werte:

| Wert                  | Beschreibung                                                                                                                                    |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `BRAZE_API_KEY`       | Ihr [Braze-REST-API-Schlüssel]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab#rest-api-keys).                        |
| `CUSTOM_API_ENDPOINT` | Ein angepasster API-Endpunkt. Dieser Endpunkt wird verwendet, um die Daten Ihrer Braze-Instanz an die richtige App-Gruppe in Ihrem Braze-Dashboard weiterzuleiten. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Schritt 2: Projekt konfigurieren" }

Das `platform`-Element in Ihrer `config.xml`-Datei sollte in etwa wie folgt aussehen:

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.ios_api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.ios_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}

{% tab android %}
```xml
<platform name="android">
    <preference name="com.braze.android_api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.android_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}
{% endtabs %}

## Plattformspezifische Syntax {#platform-specific-syntax}

Der folgende Abschnitt behandelt die plattformspezifische Syntax bei der Verwendung von Cordova mit iOS oder Android.

### Integers

{% tabs %}
{% tab ios %}
Integer-Einstellungen werden als String-Darstellungen gelesen, wie im folgenden Beispiel:

```xml
<platform name="ios">
    <preference name="com.braze.ios_flush_interval_seconds" value="10" />
    <preference name="com.braze.ios_session_timeout" value="5" />
</platform>
```
{% endtab %}

{% tab android %}
Aufgrund der Art und Weise, wie das Cordova 8.0.0+-Framework Einstellungen verarbeitet, müssen reine Integer-Einstellungen (wie z. B. Sender-IDs) als Strings mit dem Präfix `str_` gesetzt werden, wie im folgenden Beispiel:

```xml
<platform name="android">
    <preference name="com.braze.android_fcm_sender_id" value="str_64422926741" />
    <preference name="com.braze.android_default_session_timeout" value="str_10" />
</platform>
```
{% endtab %}
{% endtabs %}

### Booleans

{% tabs %}
{% tab ios %}
Boolean-Einstellungen werden vom SDK mithilfe der Schlüsselwörter `YES` und `NO` als String-Darstellung gelesen, wie im folgenden Beispiel:

```xml
<platform name="ios">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="YES" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
{% endtab %}

{% tab android %}
Boolean-Einstellungen werden vom SDK mithilfe der Schlüsselwörter `true` und `false` als String-Darstellung gelesen, wie im folgenden Beispiel:

```xml
<platform name="android">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="true" />
    <preference name="com.braze.is_session_start_based_timeout_enabled" value="false" />
</platform>
```
{% endtab %}
{% endtabs %}

## Optionale Konfigurationen {#optional}

Sie können jede der folgenden Einstellungen zum Element `platform` in der Datei `config.xml` Ihres Projekts hinzufügen:

{% tabs %}
{% tab ios %}
| Methode                                           | Beschreibung                                                                                                                                                                                                                                          |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ios_api_key`                                     | Legt den API-Schlüssel für Ihre Anwendung fest.                                                                                                                                                                                                       |
| `ios_api_endpoint`                                | Legt den [SDK-Endpunkt]({{site.baseurl}}/api/basics#endpoints) für Ihre Anwendung fest.                                                                                                                                                              |
| `ios_disable_automatic_push_registration`         | Legt fest, ob die automatische Push-Registrierung deaktiviert werden soll.                                                                                                                                                                            |
| `ios_disable_automatic_push_handling`             | Legt fest, ob die automatische Push-Behandlung deaktiviert werden soll.                                                                                                                                                                               |
| `ios_enable_idfa_automatic_collection`            | Legt fest, ob das Braze SDK automatisch die IDFA-Informationen sammeln soll. Weitere Informationen finden Sie in [der Dokumentation zur IDFA-Methode von Braze](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/). |
| `enable_location_collection`                      | Legt fest, ob die automatische Standorterfassung aktiviert ist (sofern die Nutzer:innen dies zulassen). Der `geofence-branch`                                                                                                                         |
| `geofences_enabled`                               | Legt fest, ob Geofences aktiviert sind.                                                                                                                                                                                                               |
| `ios_session_timeout`                             | Legt das Braze-Session-Timeout für Ihre Anwendung in Sekunden fest. Der Standardwert ist 10 Sekunden.                                                                                                                                                 |
| `sdk_authentication_enabled`                      | Legt fest, ob das Feature [SDK-Authentifizierung]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication) aktiviert werden soll.                                                                                         |
| `display_foreground_push_notifications`           | Legt fest, ob Push-Benachrichtigungen angezeigt werden sollen, während sich die Anwendung im Vordergrund befindet.                                                                                                                                    |
| `ios_disable_un_authorization_option_provisional` | Legt fest, ob `UNAuthorizationOptionProvisional` deaktiviert werden soll.                                                                                                                                                                             |
| `trigger_action_minimum_time_interval_seconds`    | Legt das minimale Zeitintervall in Sekunden zwischen Triggern fest. Der Standardwert ist 30 Sekunden.                                                                                                                                                 |
| `ios_push_app_group`                              | Legt die ID der App-Gruppe für iOS-Push-Erweiterungen fest.                                                                                                                                                                                           |
| `ios_forward_universal_links`                     | Legt fest, ob das SDK Universal Links automatisch erkennt und an die Systemmethoden weiterleitet. Erforderlich, damit Deeplinks aus Push-Benachrichtigungen unter iOS funktionieren. Standardmäßig deaktiviert.                                       |
| `ios_log_level`                                   | Legt die minimale Protokollierungsstufe für `Braze.Configuration.Logger` fest.                                                                                                                                                                        |
| `ios_use_uuid_as_device_id`                       | Legt fest, ob eine zufällig generierte UUID als Geräte-ID verwendet werden soll.                                                                                                                                                                      |
| `ios_flush_interval_seconds`                      | Legt das Intervall in Sekunden zwischen automatischen Datenflushes fest. Der Standardwert ist 10 Sekunden.                                                                                                                                            |
| `ios_use_automatic_request_policy`                | Legt fest, ob die Anfrage-Richtlinie für `Braze.Configuration.Api` automatisch oder manuell sein soll.                                                                                                                                               |
| `should_opt_in_when_push_authorized`              | Legt fest, ob der Abo-Status für Benachrichtigungen eines Nutzers bzw. einer Nutzerin automatisch auf `optedIn` gesetzt werden soll, wenn die Push-Berechtigungen autorisiert werden.                                                                 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Optionale Konfigurationen" }

{% alert tip %}
Ausführlichere Informationen finden Sie unter [GitHub: Braze iOS Cordova Plugin](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/ios/BrazePlugin.m).
{% endalert %}
{% endtab %}

{% tab android %}
| Methode                                                           | Beschreibung                                                                                                                                                                                  |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `android_api_key`                                                 | Legt den API-Schlüssel für Ihre Anwendung fest.                                                                                                                                               |
| `android_api_endpoint`                                            | Legt den [SDK-Endpunkt]({{site.baseurl}}/api/basics#endpoints) für Ihre Anwendung fest.                                                                                                      |
| `android_small_notification_icon`                                 | Legt das kleine Benachrichtigungssymbol fest.                                                                                                                                                 |
| `android_large_notification_icon`                                 | Legt das große Benachrichtigungssymbol fest.                                                                                                                                                  |
| `android_notification_accent_color`                               | Legt die Akzentfarbe der Benachrichtigung in hexadezimaler Darstellung fest.                                                                                                                  |
| `android_default_session_timeout`                                 | Legt das Braze-Session-Timeout für Ihre Anwendung in Sekunden fest. Der Standardwert ist 10 Sekunden.                                                                                         |
| `android_handle_push_deep_links_automatically`                    | Legt fest, ob das Braze SDK Push-Deeplinks automatisch verarbeitet. Erforderlich, damit Deeplinks aus Push-Benachrichtigungen auf Android funktionieren. Standardmäßig deaktiviert.            |
| `android_log_level`                                               | Legt die Protokollstufe für Ihre Anwendung fest. Die Standard-Protokollstufe ist 4 und protokolliert nur minimale Informationen. Um die ausführliche Protokollierung für die Fehlersuche zu aktivieren, verwenden Sie die Protokollstufe 2. |
| `firebase_cloud_messaging_registration_enabled`                   | Legt fest, ob Firebase Cloud Messaging für Push-Benachrichtigungen verwendet werden soll.                                                                                                     |
| `android_fcm_sender_id`                                           | Legt die Firebase Cloud Messaging Sender-ID fest.                                                                                                                                             |
| `enable_location_collection`                                      | Legt fest, ob die automatische Standorterfassung aktiviert ist (sofern die Nutzer:innen dies zulassen).                                                                                       |
| `geofences_enabled`                                               | Legt fest, ob Geofences aktiviert sind.                                                                                                                                                       |
| `android_disable_auto_session_tracking`                           | Deaktiviert das automatische Session-Tracking im Android Cordova Plugin. Weitere Informationen finden Sie unter [Deaktivieren des automatischen Session-Trackings](#cordova_disable-automatic-session-tracking). |
| `sdk_authentication_enabled`                                      | Legt fest, ob das Feature [SDK-Authentifizierung]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication) aktiviert werden soll.                                 |
| `trigger_action_minimum_time_interval_seconds`                    | Legt das minimale Zeitintervall in Sekunden zwischen Triggern fest. Der Standardwert ist 30 Sekunden.                                                                                         |
| `is_session_start_based_timeout_enabled`                          | Legt fest, ob das Session-Timeout-Verhalten auf Sitzungsstart- oder Sitzungsend-Ereignissen basieren soll.                                                                                    |
| `default_notification_channel_name`                               | Legt den für Nutzer:innen sichtbaren Namen fest, wie er über `NotificationChannel.getName` für den Braze-Standard-`NotificationChannel` angezeigt wird.                                       |
| `default_notification_channel_description`                        | Legt die für Nutzer:innen sichtbare Beschreibung fest, wie sie über `NotificationChannel.getDescription` für den Braze-Standard-`NotificationChannel` angezeigt wird.                         |
| `does_push_story_dismiss_on_click`                                | Legt fest, ob eine Push Story beim Klicken automatisch geschlossen wird.                                                                                                                      |
| `is_fallback_firebase_messaging_service_enabled`                  | Legt fest, ob die Verwendung eines Fallback-Firebase-Cloud-Messaging-Dienstes aktiviert ist.                                                                                                  |
| `fallback_firebase_messaging_service_classpath`                   | Legt den Klassenpfad für den Fallback-Firebase-Cloud-Messaging-Dienst fest.                                                                                                                   |
| `is_content_cards_unread_visual_indicator_enabled`                | Legt fest, ob die visuelle Anzeigeleiste für ungelesene Content Cards aktiviert ist.                                                                                                          |
| `is_firebase_messaging_service_on_new_token_registration_enabled` | Legt fest, ob das Braze SDK Token automatisch in `com.google.firebase.messaging.FirebaseMessagingService.onNewToken` registrieren soll.                                                       |
| `is_push_deep_link_back_stack_activity_enabled`                   | Legt fest, ob Braze eine Aktivität zum Back Stack hinzufügt, wenn es automatisch Deeplinks für Push folgt.                                                                                    |
| `push_deep_link_back_stack_activity_class_name`                   | Legt die Aktivität fest, die Braze zum Back Stack hinzufügt, wenn es automatisch Deeplinks für Push folgt.                                                                                    |
| `should_opt_in_when_push_authorized`                              | Legt fest, ob Braze bei der Autorisierung von Push automatisch ein Opt-in für die Nutzer:innen durchführen soll.                                                                              |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Optionale Konfigurationen" }

{% alert tip %}
Ausführlichere Informationen finden Sie unter [GitHub: Braze Android Cordova Plugin](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/android/BrazePlugin.kt).
{% endalert %}
{% endtab %}
{% endtabs %}

Im Folgenden finden Sie ein Beispiel für eine `config.xml`-Datei mit zusätzlichen Konfigurationen:

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO"/"YES" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO"/"YES" />
    <preference name="com.braze.ios_enable_idfa_automatic_collection" value="YES"/"NO" />
    <preference name="com.braze.enable_location_collection" value="NO"/"YES" />
    <preference name="com.braze.geofences_enabled" value="NO"/"YES" />
    <preference name="com.braze.ios_session_timeout" value="5" />
    <preference name="com.braze.sdk_authentication_enabled" value="YES"/"NO" />
    <preference name="com.braze.display_foreground_push_notifications" value="YES"/"NO" />
    <preference name="com.braze.ios_disable_un_authorization_option_provisional" value="NO"/"YES" />
    <preference name="com.braze.trigger_action_minimum_time_interval_seconds" value="30" />
    <preference name="com.braze.ios_push_app_group" value="PUSH_APP_GROUP_ID" />
    <preference name="com.braze.ios_forward_universal_links" value="YES"/"NO" />
    <preference name="com.braze.ios_log_level" value="2" />
    <preference name="com.braze.ios_use_uuid_as_device_id" value="YES"/"NO" />
    <preference name="com.braze.ios_flush_interval_seconds" value="10" />
    <preference name="com.braze.ios_use_automatic_request_policy" value="YES"/"NO" />
    <preference name="com.braze.should_opt_in_when_push_authorized" value="YES"/"NO" />
</platform>
```
{% endtab %}

{% tab android %}
```xml
<platform name="android">
    <preference name="com.braze.android_small_notification_icon" value="RESOURCE_ENTRY_NAME_FOR_ICON_DRAWABLE" />
    <preference name="com.braze.android_large_notification_icon" value="RESOURCE_ENTRY_NAME_FOR_ICON_DRAWABLE" />
    <preference name="com.braze.android_notification_accent_color" value="str_ACCENT_COLOR_INTEGER" />
    <preference name="com.braze.android_default_session_timeout" value="str_SESSION_TIMEOUT_INTEGER" />
    <preference name="com.braze.android_handle_push_deep_links_automatically" value="true"/"false" />
    <preference name="com.braze.android_log_level" value="str_LOG_LEVEL_INTEGER" />
    <preference name="com.braze.firebase_cloud_messaging_registration_enabled" value="true"/"false" />
    <preference name="com.braze.android_fcm_sender_id" value="str_YOUR_FCM_SENDER_ID" />
    <preference name="com.braze.enable_location_collection" value="true"/"false" />
    <preference name="com.braze.geofences_enabled" value="true"/"false" />
    <preference name="com.braze.android_disable_auto_session_tracking" value="true"/"false" />
    <preference name="com.braze.sdk_authentication_enabled" value="true"/"false" />
    <preference name="com.braze.trigger_action_minimum_time_interval_seconds" value="str_MINIMUM_INTERVAL_INTEGER" />
    <preference name="com.braze.is_session_start_based_timeout_enabled" value="false"/"true" />
    <preference name="com.braze.default_notification_channel_name" value="DEFAULT_NAME" />
    <preference name="com.braze.default_notification_channel_description" value="DEFAULT_DESCRIPTION" />
    <preference name="com.braze.does_push_story_dismiss_on_click" value="true"/"false" />
    <preference name="com.braze.is_fallback_firebase_messaging_service_enabled" value="true"/"false" />
    <preference name="com.braze.fallback_firebase_messaging_service_classpath" value="FALLBACK_FIREBASE_MESSAGING_CLASSPATH" />
    <preference name="com.braze.is_content_cards_unread_visual_indicator_enabled" value="true"/"false" />
    <preference name="com.braze.is_firebase_messaging_service_on_new_token_registration_enabled" value="true"/"false" />
    <preference name="com.braze.is_push_deep_link_back_stack_activity_enabled" value="true"/"false" />
    <preference name="com.braze.push_deep_link_back_stack_activity_class_name" value="DEEPLINK_BACKSTACK_ACTIVITY_CLASS_NAME" />
    <preference name="com.braze.should_opt_in_when_push_authorized" value="true"/"false" />
</platform>
```
{% endtab %}
{% endtabs %}

## Deaktivieren des automatischen Session-Trackings (nur Android) {#disable-automatic-session-tracking}

Standardmäßig verfolgt das Android Cordova Plugin Sitzungen automatisch. Um das automatische Session-Tracking zu deaktivieren, fügen Sie die folgende Einstellung zum Element `platform` in der Datei `config.xml` Ihres Projekts hinzu:

```xml
<platform name="android">
    <preference name="com.braze.android_disable_auto_session_tracking" value="true" />
</platform>
```

Um das Session-Tracking erneut zu starten, rufen Sie `BrazePlugin.startSessionTracking()` auf. Beachten Sie, dass nur Sitzungen verfolgt werden, die nach dem nächsten `Activity.onStart()` gestartet werden.

## Benachrichtigungskanäle für Heads-up-Benachrichtigungen konfigurieren (nur Android) {#configuring-notification-channels-for-heads-up-notifications-android-only}

Ab Android 8.0 (API-Level 26) wird das Benachrichtigungsverhalten über Benachrichtigungskanäle gesteuert. Um Heads-up-Benachrichtigungen anzuzeigen – Hinweise, die kurz am oberen Bildschirmrand erscheinen, während Nutzer:innen ihr Gerät verwenden – müssen Sie in Ihrem Android-Anwendungscode einen Benachrichtigungskanal mit `NotificationManager.IMPORTANCE_HIGH` erstellen.

Das Cordova SDK ermöglicht es Ihnen zwar, den Standardnamen und die Beschreibung des Benachrichtigungskanals über `config.xml`-Einstellungen (`default_notification_channel_name` und `default_notification_channel_description`) festzulegen, die Wichtigkeitsstufe muss jedoch programmatisch in Ihrem nativen Android-Code konfiguriert werden.

### Beispiel: Einen Benachrichtigungskanal mit hoher Wichtigkeit erstellen {#example-creating-a-high-importance-notification-channel}

Fügen Sie den folgenden Code in die `onCreate()`-Methode der `Application`-Klasse Ihrer Android-Anwendung ein:

{% subtabs local %}
{% subtab Kotlin %}
```kotlin
import android.app.NotificationChannel
import android.app.NotificationManager
import android.content.Context
import android.os.Build

override fun onCreate() {
    super.onCreate()

    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
        val channelId = "high_priority_channel"
        val channelName = "High Priority Notifications"
        val importance = NotificationManager.IMPORTANCE_HIGH

        val channel = NotificationChannel(channelId, channelName, importance).apply {
            description = "Notifications that require immediate attention"
        }

        val notificationManager = getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
        notificationManager.createNotificationChannel(channel)
    }
}
```
{% endsubtab %}

{% subtab Java %}
```java
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.content.Context;
import android.os.Build;

@Override
public void onCreate() {
    super.onCreate();

    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.O) {
        String channelId = "high_priority_channel";
        String channelName = "High Priority Notifications";
        int importance = NotificationManager.IMPORTANCE_HIGH;

        NotificationChannel channel = new NotificationChannel(channelId, channelName, importance);
        channel.setDescription("Notifications that require immediate attention");

        NotificationManager notificationManager = (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);
        notificationManager.createNotificationChannel(channel);
    }
}
```
{% endsubtab %}
{% endsubtabs %}

Nachdem Sie den Kanal in Ihrem Android-Code erstellt haben, verwenden Sie die Kanal-ID beim Senden von Push-Benachrichtigungen über das Braze-Dashboard. Weitere Informationen zu Benachrichtigungskanälen finden Sie unter [Android-Benachrichtigungskanäle]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_channels).

## Fehlerbehebung bei iOS-Builds nach dem Upgrade des Plugins {#troubleshooting-ios-builds-after-upgrading-the-plugin}

Das Cordova Braze SDK 9.0.0 und höher verwendet das Swift SDK 9.0.0 oder höher. Ab dem Swift SDK 8.0.0 wird dieses native SDK mit **Xcode 15.2** kompiliert. Wenn Ihr iOS-Build nach dem Upgrade des Cordova-Plugins auf 9.0.0 oder höher fehlschlägt, aktualisieren Sie Xcode auf 15.2 oder neuer und stellen Sie sicher, dass die Version mit dem [Swift SDK Changelog]({{site.baseurl}}/developer_guide/changelogs/?sdktab=swift) für die native iOS-Version übereinstimmt, die Ihr Plugin verwendet.