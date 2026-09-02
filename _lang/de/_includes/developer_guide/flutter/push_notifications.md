{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Push-Benachrichtigungen einrichten {#setting-up-push-notifications}

### Schritt 1: Ersteinrichtung abschließen {#step-1-complete-the-initial-setup}

{% tabs %}
{% tab Android %}
#### Schritt 1.1: Für Push Registrierung {#step-11-register-for-push}

Registrierung Sie sich für Push über die Firebase Cloud Messaging (FCM) API von Google. Eine vollständige Anleitung finden Sie in den folgenden Schritten aus dem [nativen Android-Push-Integrationsleitfaden]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/):

1. [Firebase zu Ihrem Projekt hinzufügen]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-1-add-firebase-to-your-project).
2. [Cloud Messaging zu Ihren Abhängigkeiten hinzufügen]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-2-add-cloud-messaging-to-your-dependencies).
3. [Ein Dienstkonto erstellen]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-3-create-a-service-account).
4. [JSON-Zugangsdaten generieren]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-4-generate-json-credentials).
5. [Ihre JSON-Zugangsdaten in Braze hochladen]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration#step-5-upload-your-json-credentials-to-braze).

#### Schritt 1.2: Ihre Google Sender-ID abrufen {#step-12-get-your-google-sender-id}

Öffnen Sie zunächst die Firebase Console, öffnen Sie Ihr Projekt und wählen Sie dann <i class="fa-solid fa-gear" aria-label="Einstellungen"></i>&nbsp;**Settings** > **Project settings**.

![Das Firebase-Projekt mit geöffnetem Menü „Settings“.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Wählen Sie **Cloud Messaging** und kopieren Sie unter **Firebase Cloud Messaging API (V1)** die **Sender ID** in Ihre Zwischenablage.

![Die Seite „Cloud Messaging“ des Firebase-Projekts mit hervorgehobener „Sender ID“.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

#### Schritt 1.3: Ihre `braze.xml` aktualisieren {#step-13-update-your-brazexml}

Fügen Sie Folgendes zu Ihrer `braze.xml`-Datei hinzu. Ersetzen Sie `FIREBASE_SENDER_ID` durch die zuvor kopierte Sender-ID.

```xml
<bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
```

{% endtab %}

{% tab iOS %}
#### Schritt 1.1: APNs-Zertifikate hochladen {#step-11-upload-apns-certificates}

Generieren Sie ein Apple Push Notification Service (APNs)-Zertifikat und laden Sie es in das Braze-Dashboard hoch. Eine vollständige Anleitung finden Sie unter [Ihr APNs-Zertifikat hochladen]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-1-upload-your-apns-certificate).

#### Schritt 1.2: Push-Benachrichtigungsunterstützung zu Ihrer App hinzufügen {#step-12-add-push-notification-support-to-your-app}

Folgen Sie dem [nativen iOS-Integrationsleitfaden]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration).

{% endtab %}
{% endtabs %}

### Schritt 2: Auf Push-Benachrichtigungsereignisse lauschen (optional) {#step-2-listen-for-push-notification-events-optional}

Um auf Push-Benachrichtigungsereignisse zu lauschen, die Braze erkannt und verarbeitet hat, rufen Sie `subscribeToPushNotificationEvents()` auf und übergeben Sie ein auszuführendes Argument.

{% alert note %}
Braze-Push-Benachrichtigungsereignisse sind sowohl auf Android als auch auf iOS verfügbar. Aufgrund von Plattformunterschieden erkennt iOS Braze-Push-Ereignisse nur, wenn Nutzer:innen mit einer Benachrichtigung interagiert haben.
{% endalert %}

```dart
// Create stream subscription
StreamSubscription pushEventsStreamSubscription;

pushEventsStreamSubscription = braze.subscribeToPushNotificationEvents((BrazePushEvent pushEvent) {
  print("Push Notification event of type ${pushEvent.payloadType} seen. Title ${pushEvent.title}\n and deeplink ${pushEvent.url}");
  // Handle push notification events
});

// Cancel stream subscription
pushEventsStreamSubscription.cancel();
```

#### Felder für Push-Benachrichtigungsereignisse {#push-notification-event-fields}

{% alert note %}
Aufgrund von Plattformbeschränkungen unter iOS kann das Braze SDK Push-Payloads nur verarbeiten, während die App im Vordergrund ist. Listener werden unter iOS nur für den Ereignistyp `push_opened` ausgelöst, nachdem Nutzer:innen mit einer Push-Benachrichtigung interagiert haben.
{% endalert %}

Eine vollständige Liste der Push-Benachrichtigungsfelder finden Sie in der folgenden Tabelle:

| Feldname | Typ | Beschreibung |
| ------------------ | --------- | ----------- |
| `payloadType` | String | Gibt den Payload-Typ der Benachrichtigung an. Die beiden Werte, die vom Braze Flutter SDK gesendet werden, sind `push_opened` und `push_received`. Nur `push_opened`-Ereignisse werden unter iOS unterstützt. |
| `url` | String | Gibt die URL an, die durch die Benachrichtigung geöffnet wurde. |
| `useWebview` | Boolean | Wenn `true`, wird die URL in der App in einem modalen Webview geöffnet. Wenn `false`, wird die URL im Gerätebrowser geöffnet. |
| `title` | String | Stellt den Titel der Benachrichtigung dar. |
| `body` | String | Stellt den Text- oder Inhaltstext der Benachrichtigung dar. |
| `summaryText` | String | Stellt den Zusammenfassungstext der Benachrichtigung dar. Dieser wird unter iOS von `subtitle` abgebildet. |
| `badgeCount` | Number | Stellt die Badge-Anzahl der Benachrichtigung dar. |
| `timestamp` | Number | Stellt den Zeitpunkt dar, zu dem der Payload von der Anwendung empfangen wurde. |
| `isSilent` | Boolean | Wenn `true`, wird der Payload still empfangen. Details zum Senden stiller Android-Push-Benachrichtigungen finden Sie unter [Stille Push-Benachrichtigungen auf Android]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android). Details zum Senden stiller iOS-Push-Benachrichtigungen finden Sie unter [Stille Push-Benachrichtigungen auf iOS]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift). |
| `isBrazeInternal` | Boolean | Dies ist `true`, wenn ein Benachrichtigungs-Payload für ein internes SDK-Feature gesendet wurde, z. B. Feature-Flag-Synchronisierung oder Uninstall-Tracking. Der Payload wird für die Nutzer:innen still empfangen. |
| `imageUrl` | String | Gibt die URL an, die mit dem Benachrichtigungsbild verknüpft ist. |
| `brazeProperties` | Object | Stellt Braze-Eigenschaften dar, die mit der Campaign verknüpft sind (Schlüssel-Wert-Paare). |
| `ios` | Object | Stellt iOS-spezifische Felder dar. |
| `android` | Object | Stellt Android-spezifische Felder dar. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Felder für Push-Benachrichtigungsereignisse" }

### Schritt 3: Anzeige von Push-Benachrichtigungen testen {#step-3-test-displaying-push-notifications}

Um Ihre Integration nach der Konfiguration von Push-Benachrichtigungen in der nativen Schicht zu testen:

1. Legen Sie eine:n aktive:n Nutzer:in in der Flutter-Anwendung fest. Initialisieren Sie dazu Ihr Plugin, indem Sie `braze.changeUser('your-user-id')` aufrufen.
2. Gehen Sie zu **Campaigns** und erstellen Sie eine neue Push-Benachrichtigungs-Campaign. Wählen Sie die Plattformen aus, die Sie testen möchten.
3. Verfassen Sie Ihre Testbenachrichtigung und wechseln Sie zum Tab **Test**. Fügen Sie dieselbe `user-id` als Testnutzer:in hinzu und klicken Sie auf **Send Test**.
4. Sie sollten die Benachrichtigung in Kürze auf Ihrem Gerät erhalten. Möglicherweise müssen Sie im Benachrichtigungscenter nachsehen oder die Einstellungen aktualisieren, wenn sie nicht angezeigt wird.

{% alert tip %}
Ab Xcode 14 können Sie Remote-Push-Benachrichtigungen auf einem iOS-Simulator testen.
{% endalert %}

### Schritt 4: Deeplinks hinzufügen (Android) {#step-4-add-deep-links-android}

{% alert warning %}
Unter Android ist `com_braze_handle_push_deep_links_automatically` standardmäßig auf `false` gesetzt. Mit der Standardeinstellung sendet das Tippen auf eine Push-Benachrichtigung zwar ein `push_opened`-Ereignis an Ihren Dart-Listener, aber das native SDK bringt Ihre App nicht in den Vordergrund und öffnet das Deeplink-Ziel nicht automatisch. Wenn Ihre App beim Tippen auf eine Benachrichtigung nicht gestartet wird, ist dieses Flag die wahrscheinlichste Ursache.
{% endalert %}

Um Braze zu ermöglichen, Ihre App und alle Deeplinks automatisch zu öffnen, wenn auf eine Push-Benachrichtigung getippt wird, setzen Sie `com_braze_handle_push_deep_links_automatically` in Ihrer `braze.xml` auf `true`:

```xml
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

Dieses Flag kann auch über die [Laufzeitkonfiguration]({{site.baseurl}}/developer_guide/sdk_integration#android_runtime-configuration) in Ihrem nativen Android-Code gesetzt werden:

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setHandlePushDeepLinksAutomatically(true)
        .build()
Braze.configure(this, brazeConfig)
```

Wenn Sie Deeplinks stattdessen benutzerdefiniert verarbeiten möchten, verwenden Sie den in Schritt 2 beschriebenen `subscribeToPushNotificationEvents()`-Listener, um das `url`-Feld des `push_opened`-Ereignisses selbst weiterzuleiten. Weitere Informationen finden Sie unter [Deeplinking]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=flutter).