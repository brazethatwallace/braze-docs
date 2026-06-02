{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## Push-Benachrichtigungen einrichten {#setting-up-push-notifications}

### 1. Schritt: Ersteinrichtung abschließen {#step-1-complete-the-initial-setup}

{% tabs %}
{% tab Android %}
#### Schritt 1.1: Für Push registrieren {#step-11-register-for-push}

Registrieren Sie sich für Push mit der Firebase Cloud Messaging (FCM)-API von Google. Eine ausführliche Anleitung finden Sie in den folgenden Schritten der [nativen Android-Push-Integrationsanleitung]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/):

1. [Firebase zu Ihrem Projekt hinzufügen]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-add-firebase-to-your-project).
2. [Cloud Messaging zu Ihren Abhängigkeiten hinzufügen]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-2-add-cloud-messaging-to-your-dependencies).
3. [Ein Dienstkonto erstellen]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-3-create-a-service-account).
4. [JSON-Zugangsdaten generieren]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-4-generate-json-credentials).
5. [Ihre JSON-Zugangsdaten auf Braze hochladen]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-5-upload-your-json-credentials-to-braze).

#### Schritt 1.2: Ihre Google Sender ID ermitteln {#step-12-get-your-google-sender-id}

Gehen Sie zunächst zur Firebase-Konsole, öffnen Sie Ihr Projekt und wählen Sie dann <i class="fa-solid fa-gear"></i>&nbsp;**Settings** > **Project settings**.

![Das Firebase-Projekt mit geöffnetem Menü „Settings“.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

Wählen Sie **Cloud Messaging** und kopieren Sie dann unter **Firebase Cloud Messaging API (V1)** die **Sender ID** in Ihre Zwischenablage.

![Die Seite „Cloud Messaging“ des Firebase-Projekts mit hervorgehobener „Sender ID“.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

#### Schritt 1.3: Ihre `braze.xml` aktualisieren {#step-13-update-your-brazexml}

Fügen Sie Folgendes zu Ihrer Datei `braze.xml` hinzu. Ersetzen Sie `FIREBASE_SENDER_ID` durch die Sender ID, die Sie zuvor kopiert haben.

```xml
<bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
```

{% endtab %}

{% tab iOS %}
#### Schritt 1.1: APNs-Zertifikate hochladen {#step-11-upload-apns-certificates}

Generieren Sie ein Apple Push Notification Service (APNs)-Zertifikat und laden Sie es in das Braze-Dashboard hoch. Eine vollständige Anleitung finden Sie unter [Hochladen Ihres APNs-Zertifikats]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-upload-your-apns-certificate).

#### Schritt 1.2: Push-Benachrichtigungsunterstützung zu Ihrer App hinzufügen {#step-12-add-push-notification-support-to-your-app}

Folgen Sie der [Anleitung für die native iOS-Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration).

{% endtab %}
{% endtabs %}

### 2. Schritt: Auf Push-Benachrichtigungsereignisse lauschen (optional) {#step-2-listen-for-push-notification-events-optional}

Um auf Push-Benachrichtigungsereignisse zu lauschen, die Braze erkannt und verarbeitet hat, rufen Sie `subscribeToPushNotificationEvents()` auf und übergeben Sie ein Argument zur Ausführung.

{% alert note %}
Push-Benachrichtigungsereignisse von Braze sind sowohl auf Android als auch auf iOS verfügbar. Aufgrund von Plattformunterschieden erkennt iOS Braze-Push-Ereignisse nur, wenn Nutzer:innen mit einer Benachrichtigung interagiert haben.
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

##### Ereignisfelder für Push-Benachrichtigungen {#push-notification-event-fields}

{% alert note %}
Aufgrund von Plattformbeschränkungen unter iOS kann das Braze SDK Push-Payloads nur verarbeiten, wenn die App im Vordergrund ist. Listener werden unter iOS nur beim Ereignistyp `push_opened` getriggert, nachdem Nutzer:innen mit einem Push interagiert haben.
{% endalert %}

Eine vollständige Liste der Felder für Push-Benachrichtigungen finden Sie in der folgenden Tabelle:

| Feldname | Typ | Beschreibung |
| ------------------ | --------- | ----------- |
| `payloadType` | String | Gibt den Payload-Typ der Benachrichtigung an. Die beiden Werte, die vom Braze Flutter SDK gesendet werden, sind `push_opened` und `push_received`. Unter iOS werden nur `push_opened`-Ereignisse unterstützt. |
| `url` | String | Gibt die URL an, die durch die Benachrichtigung geöffnet wurde. |
| `useWebview` | Boolescher Wert | Wenn `true`, wird die URL in der App in einer modalen Webansicht geöffnet. Wenn `false`, wird die URL im Browser des Geräts geöffnet. |
| `title` | String | Stellt den Titel der Benachrichtigung dar. |
| `body` | String | Stellt den Textkörper oder Inhalt der Benachrichtigung dar. |
| `summaryText` | String | Stellt den zusammenfassenden Text der Benachrichtigung dar. Dieser wird unter iOS von `subtitle` zugeordnet. |
| `badgeCount` | Zahl | Stellt die Badge-Anzahl der Benachrichtigung dar. |
| `timestamp` | Zahl | Stellt den Zeitpunkt dar, zu dem der Payload von der Anwendung empfangen wurde. |
| `isSilent` | Boolescher Wert | Wenn `true`, wird der Payload still empfangen. Einzelheiten zum Senden stiller Push-Benachrichtigungen unter Android finden Sie unter [Stille Push-Benachrichtigungen unter Android]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android). Einzelheiten zum Senden stiller Push-Benachrichtigungen unter iOS finden Sie unter [Stille Push-Benachrichtigungen unter iOS]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift). |
| `isBrazeInternal` | Boolescher Wert | Dies ist `true`, wenn ein Benachrichtigungs-Payload für eine interne SDK-Funktion gesendet wurde, wie z. B. die Synchronisierung von Feature-Flags oder das Uninstall-Tracking. Der Payload wird für Nutzer:innen still empfangen. |
| `imageUrl` | String | Gibt die URL an, die mit dem Benachrichtigungsbild verknüpft ist. |
| `brazeProperties` | Objekt | Stellt die mit der Campaign verbundenen Braze-Eigenschaften dar (Schlüssel-Wert-Paare). |
| `ios` | Objekt | Stellt iOS-spezifische Felder dar. |
| `android` | Objekt | Stellt Android-spezifische Felder dar. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Ereignisfelder für Push-Benachrichtigungen" }

### 3. Schritt: Anzeige von Push-Benachrichtigungen testen {#step-3-test-displaying-push-notifications}

So testen Sie Ihre Integration, nachdem Sie Push-Benachrichtigungen in der nativen Schicht konfiguriert haben:

1. Legen Sie eine:n aktive:n Nutzer:in in der Flutter-Anwendung fest. Dazu initialisieren Sie das Plugin, indem Sie `braze.changeUser('your-user-id')` aufrufen.
2. Gehen Sie zu **Campaigns** und erstellen Sie eine neue Push-Benachrichtigungs-Campaign. Wählen Sie die Plattformen, die Sie testen möchten.
3. Verfassen Sie Ihre Testbenachrichtigung und gehen Sie auf den Tab **Test**. Fügen Sie die gleiche `user-id` wie die:der Testnutzer:in hinzu und klicken Sie auf **Send Test**.
4. Sie sollten die Benachrichtigung in Kürze auf Ihrem Gerät erhalten. Wenn sie nicht angezeigt wird, müssen Sie möglicherweise im Benachrichtigungscenter nachsehen oder die Einstellungen aktualisieren.

{% alert tip %}
Ab Xcode 14 können Sie Remote-Push-Benachrichtigungen auf einem iOS-Simulator testen.
{% endalert %}