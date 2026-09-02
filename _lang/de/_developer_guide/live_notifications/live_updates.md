---
nav_title: Live-Updates für Android
article_title: Live Updates für das Android Braze SDK or Software-Development-Kit
page_order: 0.3
description: "Erfahren Sie, wie Sie Android Live Updates im Braze SDK or Software-Development-Kit verwenden."
platform:
  - Android
hidden: true
---

# Live Updates für Android {#live-updates-for-android}

> Erfahren Sie, wie Sie Android Live Updates im Braze SDK or Software-Development-Kit verwenden, auch bekannt als [Progress Centric Notifications](https://developer.android.com/about/versions/16/features/progress-centric-notifications). Diese Benachrichtigungen ähneln den [Live-Aktivitäten für das Swift Braze SDK or Software-Development-Kit]({{site.baseurl}}/developer_guide/live_notifications/live_activities) und ermöglichen es Ihnen, interaktive Sperrbildschirm-Benachrichtigungen anzuzeigen. Android 16 führt fortschrittsorientierte Benachrichtigungen ein, mit denen Nutzer:innen nahtlos von ihnen initiierte End-to-End-Journeys verfolgen können.

## So funktioniert es {#how-it-works}

Sie können die Schnittstelle [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) verwenden, um die Darstellung von Braze-Push-Benachrichtigungen anzupassen. Wenn Sie `BrazeNotificationFactory` erweitern, ruft Braze die Methode `createNotification()` Ihrer Factory auf, bevor die Benachrichtigung den Nutzer:innen angezeigt wird. Dabei wird ein Payload übergeben, der benutzerdefinierte Schlüssel-Wert-Paare enthält, die über das Braze-Dashboard oder die Representational State Transfer API gesendet wurden.

## Anzeigen eines Live Updates {#displaying-a-live-update}

In diesem Abschnitt arbeiten Sie mit Superb Owl zusammen, dem Moderator einer neuen Spielshow, in der Wildtierrettungsteams darum wetteifern, wer die meisten Eulen retten kann. Das Team möchte Live Updates in seiner Android-App nutzen, um den Status eines laufenden Spiels anzuzeigen und dynamische Aktualisierungen der Benachrichtigung in Echtzeit vorzunehmen.

![Ein Beispiel für ein Live Update unter Android]({% image_buster /assets/img/android/android-live-update.png %}){: style="max-width:40%;"}

{% multi_lang_include developer_guide/prerequisites/android.md %}

### Schritt 1: Eine benutzerdefinierte Notification Factory erstellen {#step-1-create-a-custom-notification-factory}

Erstellen Sie in Ihrer Anwendung eine neue Datei namens `MyCustomNotificationFactory.kt`, die [`BrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) erweitert, um zu steuern, wie Braze Live Updates angezeigt werden.

Im folgenden Beispiel hat Superb Owl eine benutzerdefinierte Notification Factory erstellt, um ein Live Update or aktualisieren für laufende Spiele anzuzeigen. Im nächsten Schritt erstellen Sie eine neue Methode namens `getTeamInfo`, um die Daten eines Teams der Activity zuzuordnen.

```kotlin
class MyCustomNotificationFactory : IBrazeNotificationFactory {
    override fun createNotification(payload: BrazeNotificationPayload): Notification? {
        val notificationBuilder = populateNotificationBuilder(payload)
        val context = payload.context ?: return null

        if (notificationBuilder == null) {
            brazelog { "Notification could not be built. Returning null as created notification." }
            return null
        }
        notificationBuilder.setContentTitle("Android Live Updates").setContentText("Ongoing updates below")
        setProgressStyle(notificationBuilder, context)
        return notificationBuilder.build()
    }

    private fun setProgressStyle(notificationBuilder: NotificationCompat.Builder, context: Context) {
        val style = NotificationCompat.ProgressStyle()
            .setStyledByProgress(false)
            .setProgress(200)
            .setProgressTrackerIcon(IconCompat.createWithResource(context, R.drawable.notification_small_icon))
            .setProgressSegments(
                mutableListOf(
                    NotificationCompat.ProgressStyle.Segment(1000).setColor(Color.GRAY),
                    NotificationCompat.ProgressStyle.Segment(200).setColor(Color.BLUE),
                )
            )
            .setProgressPoints(
                mutableListOf(
                    NotificationCompat.ProgressStyle.Point(60).setColor(Color.RED),
                    NotificationCompat.ProgressStyle.Point(560).setColor(Color.GREEN)
                )
            )

        notificationBuilder.setStyle(style)
    }
}
```

### Schritt 2: Benutzerdefinierte Daten zuordnen {#step-2-map-custom-data}

Erstellen Sie in `MyCustomNotificationFactory.kt` eine neue Methode für die Datenverarbeitung, wenn Live Updates angezeigt werden.

Superb Owl hat die folgende Methode erstellt, um den Namen und das Logo jedes Teams den erweiterten Live Updates zuzuordnen:

```kotlin
class CustomNotificationFactory : BrazeNotificationFactory() {
    override fun createNotification(payload: BrazeNotificationPayload): Notification? {
        // Your existing code
        return super.createNotification(payload)
    }

    // Your new method
    private fun getTeamInfo(team: String?): Pair<String, Int> {
        return when (team) {
            "WBF" -> Pair("Wild Bird Fund", R.drawable.team_wbf)
            "OWL" -> Pair("Owl Rehab", R.drawable.team_owl)
            else  -> Pair("Unknown", R.drawable.notification_small_icon)
        }
    }
}
```

### Schritt 3: Die benutzerdefinierte Notification Factory festlegen {#step-3-set-the-custom-notification-factory}

Verwenden Sie in Ihrer Application-Klasse [`customBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/custom-braze-notification-factory.html?query=var%20customBrazeNotificationFactory:%20IBrazeNotificationFactory?), um Ihre benutzerdefinierte Notification Factory festzulegen.

```kotlin
class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Tell Braze to use your custom factory for notifications
        Braze.customBrazeNotificationFactory = MyCustomNotificationFactory()
    }
}
```

### Schritt 4: Die Activity senden {#step-4-send-the-activity}

Sie können den Representational State Transfer-API-Endpunkt [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) verwenden, um eine Push-Benachrichtigung an das Android-Gerät einer Nutzerin oder eines Nutzers zu senden.

#### Beispiel-curl-Befehl {#example-curl-command}

Superb Owl hat die Anfrage mit dem folgenden curl-Befehl gesendet:

```
curl -X POST "https://BRAZE_REST_ENDPOINT/messages/send" \
  -H "Authorization: Bearer {REST_API_KEY}" \
  -H "Content-Type: application/json" \
  --data '{
    "external_user_ids": ["USER_ID"],
    "messages": {
      "android_push": {
        "title": "WBF vs OWL",
        "alert": "2 to 4 1:33 Q4",
        "extra": {
          "live_update": "true",
          "team1": "WBF",
          "team2": "OWL",
          "score1": "2",
          "score2": "4",
          "time": "1:33",
          "quarter": "Q4"
        },
        "notification_id": "ASSIGNED_NOTIFICATION_ID"
      }
    }
  }'
```

{% alert tip %}
Obwohl curl-Befehle zum Testen hilfreich sind, empfehlen wir, diesen Aufruf in Ihrem Backend zu verarbeiten, wo Sie bereits Ihre [iOS Live Activities]({{site.baseurl}}/developer_guide/live_notifications?sdktab=swift) verwalten.
{% endalert %}

#### Anfrageparameter {#request-parameters}

| Schlüssel | Beschreibung |
|------------------------------|------------|
| `REST_API_KEY` | Ein Braze-Representational State Transfer-API-Schlüssel mit `messages.send`-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| `BRAZE_REST_ENDPOINT` | Ihre Representational State Transfer-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL Ihrer Instanz]({{site.baseurl}}/api/basics#endpoints) ab. |
| `USER_ID` | Die ID der Nutzerin oder des Nutzers, an die bzw. den Sie die Benachrichtigung senden. |
| `messages.android_push.title` | Der Titel der Nachricht. Standardmäßig wird dieser nicht für die Live-Benachrichtigungen der benutzerdefinierten Notification Factory verwendet, kann aber als Fallback dienen. |
| `messages.android_push.alert` | Der Nachrichtentext. Standardmäßig wird dieser nicht für die Live-Benachrichtigungen der benutzerdefinierten Notification Factory verwendet, kann aber als Fallback dienen. |
| `messages.extra` | Schlüssel-Wert-Paare, die von der benutzerdefinierten Notification Factory für Live-Benachrichtigungen verwendet werden. Sie können diesem Wert einen beliebigen String zuweisen&#8212;im [Beispiel-curl-Befehl](#example-curl-command) wird jedoch `live_updates` verwendet, um zu bestimmen, ob es sich um eine Standard- oder eine Live-Push-Benachrichtigung handelt. |
| `ASSIGNED_NOTIFICATION_ID` | Die Benachrichtigungs-ID, die Sie der Live-Benachrichtigung der ausgewählten Nutzerin oder des ausgewählten Nutzers zuweisen möchten. Die ID muss für dieses Spiel eindeutig sein und muss verwendet werden, um die [bestehende Benachrichtigung später zu Update or aktualisieren or aktualisieren](#android_step-4-update-data-with-the-braze-rest-api). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anfrageparameter" }

### Schritt 5: Die Activity Update or aktualisieren or aktualisieren {#step-5-update-the-activity}

Um das bestehende Live Update or aktualisieren mit neuen Daten zu Update or aktualisieren or aktualisieren, ändern Sie die relevanten Schlüssel-Wert-Paare, die `messages.extra` zugewiesen sind, und rufen Sie dann mit derselben `notification_id` den Endpunkt `/messages/send` erneut auf.