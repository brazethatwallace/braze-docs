{% multi_lang_include developer_guide/prerequisites/android.md %} Sie müssen außerdem [Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Angepasstes Benachrichtigungslayout {#custom-notification-layout}

Braze-Benachrichtigungen werden als [Datennachrichten](https://firebase.google.com/docs/cloud-messaging/concept-options) gesendet, was bedeutet, dass Ihre Anwendung immer die Möglichkeit hat, zu reagieren und entsprechendes Verhalten auszuführen, auch im Hintergrund (im Gegensatz zu Benachrichtigungsnachrichten, die automatisch vom System verarbeitet werden können, wenn Ihre App im Hintergrund läuft). Dadurch hat Ihre Anwendung die Möglichkeit, das Erlebnis anzupassen, indem sie beispielsweise personalisierte UI-Elemente innerhalb der Benachrichtigung anzeigt, die im Benachrichtigungsfach zugestellt wird. Obwohl diese Art der Push-Implementierung für manche ungewohnt sein mag, sind eines unserer bekannten Features bei Braze, [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories), ein hervorragendes Beispiel für die Nutzung angepasster Ansichtskomponenten, um ein ansprechendes Erlebnis zu schaffen!

{% alert important %}
Android legt einige Einschränkungen fest, welche Komponenten zur Implementierung angepasster Benachrichtigungsansichten verwendet werden können. Benachrichtigungsansichtslayouts dürfen _nur_ View-Objekte enthalten, die mit dem [RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews)-Framework kompatibel sind.
{% endalert %}

Sie können die Schnittstelle [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) verwenden, um die Anzeige von Braze-Push-Benachrichtigungen anzupassen. Durch die Erweiterung von `BrazeNotificationFactory` ruft Braze die Methode `createNotification()` Ihrer Factory auf, bevor die Benachrichtigung dem Nutzer angezeigt wird. Dabei wird ein Payload mit angepassten Schlüssel-Wert-Paaren übergeben, die über das Braze-Dashboard oder die REST API gesendet wurden.

In diesem Abschnitt arbeiten Sie mit Superb Owl zusammen, dem Moderator einer neuen Spielshow, in der Wildtierrettungsteams gegeneinander antreten, um zu sehen, wer die meisten Eulen retten kann. Sie möchten Live-Update-Benachrichtigungen in ihrer Android-App nutzen, um den Status eines laufenden Spiels anzuzeigen und die Benachrichtigung in Echtzeit dynamisch zu aktualisieren.

![Das Live-Update, das Superb Owl anzeigen möchte, mit einem laufenden Spiel zwischen „Wild Bird Fund“ und „Owl Rescue“. Es ist gerade das vierte Viertel und der Spielstand ist 2-4, wobei OWL in Führung liegt.]({% image_buster /assets/img/android/android-live-activity-superb-owl-example.jpg %}){: style="max-width:65%;"}

### Schritt 1: Ein angepasstes Layout hinzufügen {#step-1-add-a-custom-layout}

Sie können ein oder mehrere angepasste RemoteView-Benachrichtigungslayouts zu Ihrem Projekt hinzufügen. Diese sind nützlich, um zu steuern, wie Benachrichtigungen im eingeklappten oder erweiterten Zustand angezeigt werden. Ihre Verzeichnisstruktur sollte in etwa wie folgt aussehen:

```plaintext
.
├── app/
└── res/
    └── layout/
        ├── liveupdate_collapsed.xml
        └── liveupdate_expanded.xml
```

Erstellen Sie in jeder XML-Datei ein angepasstes Layout. Superb Owl hat die folgenden Layouts für ihre eingeklappten und erweiterten RemoteView-Layouts erstellt:

{% tabs local %}
{% tab  Beispiel: Eingeklapptes Layout %}
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="vertical">

    <TextView
        android:id="@+id/notification_title"
        style="@style/TextAppearance.Compat.Notification.Title"
        android:layout_width="wrap_content"
        android:layout_height="0dp"
        android:layout_weight="1" />
</LinearLayout>
```
{% endtab %}

{% tab Beispiel: Erweitertes Layout %}
{% details Beispielcode anzeigen %}
```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:orientation="horizontal">

    <LinearLayout
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_gravity="center"

        android:layout_height="wrap_content"
        android:orientation="vertical">

        <ImageView
            android:id="@+id/team1logo"
            android:layout_width="wrap_content"
            android:layout_height="60dp"
            android:layout_gravity="center"
            android:src="@drawable/team_default1"/>

        <TextView
            android:id="@+id/team1name"
            android:textAlignment="center"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

    </LinearLayout>

    <LinearLayout
        android:layout_width="0dp"
        android:layout_weight="1.6"
        android:layout_gravity="center"
        android:layout_height="wrap_content"
        android:orientation="vertical">

        <TextView
            android:id="@+id/score"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:text="2-4"
            android:textColor="#555555"
            android:textAlignment="center"
            android:textSize="32sp"
            android:textStyle="bold" />

        <TextView
            android:id="@+id/timeInfo"
            android:textAlignment="center"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

    </LinearLayout>


    <LinearLayout
        android:layout_width="0dp"
        android:layout_weight="1"
        android:layout_gravity="center"
        android:layout_height="wrap_content"
        android:orientation="vertical">

        <ImageView
            android:id="@+id/team2logo"
            android:layout_gravity="center"
            android:layout_width="wrap_content"
            android:layout_height="60dp"
            android:src="@drawable/team_default2"/>

        <TextView
            android:id="@+id/team2name"
            android:textAlignment="center"
            android:layout_width="match_parent"
            android:layout_height="wrap_content" />

    </LinearLayout>
</LinearLayout>
```
{% enddetails %}
{% endtab %}
{% endtabs %}

### Schritt 2: Eine angepasste Benachrichtigungs-Factory erstellen {#step-2-create-a-custom-notification-factory}

Erstellen Sie in Ihrer Anwendung eine neue Datei namens `MyCustomNotificationFactory.kt`, die [`BrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) erweitert, um die Anzeige angepasster RemoteView-Layouts zu steuern.

Im folgenden Beispiel hat Superb Owl eine angepasste Benachrichtigungs-Factory erstellt, um ein RemoteView-Layout für laufende Spiele anzuzeigen. Im [nächsten Schritt](#android_step-3-map-custom-data) erstellen sie eine neue Methode namens `getTeamInfo`, um die Daten eines Teams der Aktivität zuzuordnen.

{% details Beispielcode anzeigen %}
```kotlin
import android.app.Notification
import android.widget.RemoteViews
import androidx.core.app.NotificationCompat
import com.braze.models.push.BrazeNotificationPayload
import com.braze.push.BrazeNotificationFactory
import com.braze.push.BrazeNotificationUtils.getOrCreateNotificationChannelId
import com.braze.support.BrazeLogger.brazelog

class MyCustomNotificationFactory : BrazeNotificationFactory() {
    override fun createNotification(payload: BrazeNotificationPayload): Notification? {
        if (payload.extras.containsKey("live_update")) {
            val kvp = payload.extras
            val notificationChannelId = getOrCreateNotificationChannelId(payload)
            val context = payload.context

            if (context == null) {
                brazelog { "BrazeNotificationPayload has null context. Not creating notification" }
                return null
            }

            val team1 = kvp["team1"]
            val team2 = kvp["team2"]
            val score1 = kvp["score1"]
            val score2 = kvp["score2"]
            val time = kvp["time"]
            val quarter = kvp["quarter"]

            // Superb Owl will define the 'getTeamInfo' method in the next step.
            val (team1name, team1icon) = getTeamInfo(team1)
            val (team2name, team2icon) = getTeamInfo(team2)

            // Get the layouts to use in the custom notification.
            val notificationLayoutCollapsed = RemoteViews(BuildConfig.APPLICATION_ID, R.layout.liveupdate_collapsed)
            val notificationLayoutExpanded = RemoteViews(BuildConfig.APPLICATION_ID, R.layout.liveupdate_expanded)

            // Very simple notification for the small layout
            notificationLayoutCollapsed.setTextViewText(
                R.id.notification_title,
                "$team1 $score1 - $score2 $team2\n$time $quarter"
            )

            notificationLayoutExpanded.setTextViewText(R.id.score, "$score1 - $score2")
            notificationLayoutExpanded.setTextViewText(R.id.team1name, team1name)
            notificationLayoutExpanded.setTextViewText(R.id.team2name, team2name)
            notificationLayoutExpanded.setTextViewText(R.id.timeInfo, "$time - $quarter")
            notificationLayoutExpanded.setImageViewResource(R.id.team1logo, team1icon)
            notificationLayoutExpanded.setImageViewResource(R.id.team2logo, team2icon)

            val customNotification = NotificationCompat.Builder(context, notificationChannelId)
                .setSmallIcon(R.drawable.notification_small_icon)
                .setStyle(NotificationCompat.DecoratedCustomViewStyle())
                .setCustomContentView(notificationLayout)
                .setCustomBigContentView(notificationLayoutExpanded)
                .build()
            return customNotification
        } else {
            // Use the BrazeNotificationFactory for all other notifications
            return super.createNotification(payload)
        }
    }
}
```
{% enddetails %}

### Schritt 3: Angepasste Daten zuordnen {#step-3-map-custom-data}

Erstellen Sie in `MyCustomNotificationFactory.kt` eine neue Methode zur Verarbeitung von Daten, wenn Live-Updates angezeigt werden.

Superb Owl hat die folgende Methode erstellt, um den Namen und das Logo jedes Teams den erweiterten Live-Updates zuzuordnen:

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

### Schritt 4: Die angepasste Benachrichtigungs-Factory festlegen {#step-4-set-the-custom-notification-factory}

Verwenden Sie in Ihrer Application-Klasse [`customBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/custom-braze-notification-factory.html?query=var%20customBrazeNotificationFactory:%20IBrazeNotificationFactory?), um Ihre angepasste Benachrichtigungs-Factory festzulegen.

```kotlin
import com.braze.Braze

class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Tell Braze to use your custom factory for notifications
        Braze.customBrazeNotificationFactory = MyCustomNotificationFactory()
    }
}
```

### Schritt 5: Die Aktivität senden {#step-5-send-the-activity}

Sie können den REST-API-Endpunkt [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) verwenden, um eine Push-Benachrichtigung an das Android-Gerät eines Nutzers zu senden.

#### Beispiel-curl-Befehl {#example-curl-command}

Superb Owl hat ihre Anfrage mit dem folgenden curl-Befehl gesendet:

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
Obwohl curl-Befehle zum Testen nützlich sind, empfehlen wir, diesen Aufruf in Ihrem Backend zu verarbeiten, wo Sie bereits Ihre [iOS Live Activities]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift) verwalten.
{% endalert %}

#### Anfrageparameter {#request-parameters}

| Schlüssel | Beschreibung |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `REST_API_KEY` | Ein Braze-REST-API-Schlüssel mit `messages.send`-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| `BRAZE_REST_ENDPOINT` | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics#endpoints) ab. |
| `USER_ID` | Die ID der Nutzerin oder des Nutzers, an die/den Sie die Benachrichtigung senden. |
| `messages.android_push.title` | Der Titel der Nachricht. Standardmäßig wird dieser für die Live-Benachrichtigungen der angepassten Benachrichtigungs-Factory nicht verwendet, kann aber als Fallback dienen. |
| `messages.android_push.alert` | Der Text der Nachricht. Standardmäßig wird dieser für die Live-Benachrichtigungen der angepassten Benachrichtigungs-Factory nicht verwendet, kann aber als Fallback dienen. |
| `messages.extra` | Schlüssel-Wert-Paare, die die angepasste Benachrichtigungs-Factory für Live-Benachrichtigungen verwendet. Sie können diesem Wert einen beliebigen String zuweisen&#8212;in diesem Beispiel wird jedoch `live_updates` verwendet, um zu bestimmen, ob es sich um eine Standard- oder eine Live-Push-Benachrichtigung handelt. |
| `ASSIGNED_NOTIFICATION_ID` | Die Benachrichtigungs-ID, die Sie der Live-Benachrichtigung der gewählten Nutzerin oder des gewählten Nutzers zuweisen möchten. Die ID muss für dieses Spiel eindeutig sein und muss verwendet werden, um [ihre bestehende Benachrichtigung](#android_step-4-update-data-with-the-braze-rest-api) später zu aktualisieren. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Anfrageparameter" }

### Schritt 6: Die Aktivität aktualisieren {#step-6-update-the-activity}

Um die bestehende RemoteView-Benachrichtigung mit neuen Daten zu aktualisieren, ändern Sie die relevanten Schlüssel-Wert-Paare, die `messages.extra` zugewiesen sind, und rufen Sie dann mit derselben `notification_id` den Endpunkt `/messages/send` erneut auf.

## Personalisierte Push-Benachrichtigungen {#personalized-push-notifications}

Push-Benachrichtigungen können nutzerspezifische Informationen innerhalb einer angepassten Ansichtshierarchie anzeigen. Im folgenden Beispiel wird ein API-Trigger verwendet, um eine personalisierte Push-Benachrichtigung an Nutzer:innen zu senden, damit diese ihren aktuellen Fortschritt nach Abschluss einer bestimmten Aufgabe in der App überprüfen können.

![Beispiel für personalisierte Push-Benachrichtigung im Dashboard]({% image_buster /assets/img/push_implementation_guide/android_push_custom_layout.png %}){: style="max-width:65%;border:0"}

Um einen personalisierten Push im Dashboard einzurichten, Registrieren Sie die spezifische Kategorie, die angezeigt werden soll, und legen Sie dann alle relevanten Nutzerattribute fest, die Sie mithilfe von Liquid anzeigen möchten.

![Beispiel für personalisierte Push-Benachrichtigung im Dashboard]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}