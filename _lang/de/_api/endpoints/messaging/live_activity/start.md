---
nav_title: "POST: Live-Aktivität starten"
article_title: "POST: Live-Aktivität starten"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Dieser Artikel enthält Einzelheiten zum Endpunkt „Live-Aktivität starten“."
---
{% api %}
# Live-Aktivität starten {#start-live-activity}
{% apimethod post %}
/messages/live_activity/start
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um [Live-Aktivitäten]({{site.baseurl}}/developer_guide/live_notifications?sdktab=swift), die in Ihrer iOS-App angezeigt werden, aus der Ferne zu starten. Dieser Endpunkt erfordert eine zusätzliche Einrichtung.

Nachdem Sie eine Live-Aktivität erstellt haben, senden Sie eine POST-Anfrage, um ein Segment, eine verbundene Zielgruppe oder bestimmte Nutzer:innen anzusprechen. Identifizieren Sie bestimmte Nutzer:innen anhand der externen Nutzer-ID, des Nutzer-Alias oder beidem. Weitere Informationen über die Live-Aktivitäten von Apple finden Sie unter [Starten und Aktualisieren von Live-Aktivitäten mit Push-Benachrichtigungen von ActivityKit](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications).

Wenn `content-available` nicht festgelegt ist, beträgt die Standardpriorität des Apple-Push-Benachrichtigungs-Dienstes (APNs) 10. Wenn `content-available` gesetzt ist, beträgt diese Priorität 5. Weitere Informationen finden Sie unter [Apple-Push-Objekt]({{site.baseurl}}/api/objects_filters/messaging/apple_object).

{% alert tip %}
Um eine Live-Aktivität zu beenden, verwenden Sie den Endpunkt [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update) mit `end_activity` auf `true` gesetzt.
{% endalert %}

## Automatisches Entfernen einrichten {#arranging-automatic-dismissal}

Um das automatische Entfernen nach dem Start einer Live-Aktivität einzurichten, planen Sie eine Folgeanfrage an den Update-Endpunkt über Ihr Backend.

1. Senden Sie eine `/messages/live_activity/start`-Anfrage mit einer `activity_id`, die Sie später wiederverwenden können.
2. Speichern Sie diese `activity_id` und Ihren gewünschten Endzeitpunkt in Ihrem Backend-Scheduler.
3. Senden Sie zum gewünschten Endzeitpunkt eine `/messages/live_activity/update`-Anfrage mit `end_activity` auf `true` gesetzt.
4. Konfigurieren Sie das Entfernungsverhalten in derselben Update-Anfrage. Weitere Details finden Sie beim Endpunkt [`/messages/live_activity/update`]({{site.baseurl}}/api/endpoints/messaging/live_activity/update).
5. Überprüfen Sie Sende- und Ergebnis-Ereignisse im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log).

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, müssen Sie Folgendes tun:

- Generieren Sie einen API-Schlüssel mit der Berechtigung `messages.live_activity.start`.
- [Erstellen Sie eine Live-Aktivität]({{site.baseurl}}/developer_guide/live_notifications/live_activities?tab=local&sdktab=swift#create-an-activity) mit dem Braze Swift SDK.

{% multi_lang_include api/payload_size_alert.md %}

{% alert important %}
Wenn Sie bestimmte Nutzer:innen ansprechen, startet Braze eine Live-Aktivität nur für `external_user_ids` und `user_aliases`, die zu bestehenden Nutzer:innen aufgelöst werden.
{% endalert %}

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfragetext {#request-body}

```json
{
  "app_id": "(required, string) App API identifier retrieved from the Developer Console.",
  "activity_id": "(required, string) Define a custom string as your `activity_id`. Use this ID to send update or end events to your Live Activity.",
  "activity_attributes_type": "(required, string) The activity attributes type you define within `liveActivities.registerPushToStart` in your app.",
  "activity_attributes": "(required, object) The static attribute values for the activity type (such as the sports team names, which don't change)",
  "content_state": "(required, object) You define the ContentState parameters when you create your Live Activity. Pass the updated values for your ContentState using this object. The format of this request must match the shape you initially defined.",
  "stale_date": "(optional, datetime in ISO-8601 format) The time the Live Activity content is marked as outdated in the user’s UI.",
  "notification": "(required, object) Include an `apple_push` object to define a push notification that creates an alert for the user, displayed on paired watchOS devices. Include `notification.alert.title` and `notification.alert.body`.",
  // Include one targeting method:
  // 1. "external_user_ids", "user_aliases", or both (combined maximum 50)
  // 2. "custom_audience"
  // 3. "segment_id"
  "external_user_ids": "(optional, array of strings) see external user identifier",
  "user_aliases": "(optional, array of user alias objects) see user alias object",
  "custom_audience": "(optional, connected audience object) see connected audience",
  "segment_id": "(optional, string) see segment identifier"
}
```

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|-----------|----------|----------|--------------|
| `app_id` | Erforderlich | String | [API-Bezeichner]({{site.baseurl}}/api/identifier_types#app-identifier) der App, abgerufen von der Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers). |
| `activity_id` | Erforderlich | String | Definieren Sie einen angepassten String als Ihre `activity_id`. Verwenden Sie diese ID, um Update- oder End-Ereignisse an Ihre Live-Aktivität zu senden. |
| `activity_attributes_type` | Erforderlich | String | Der Aktivitätsattribut-Typ, den Sie unter `liveActivities.registerPushToStart` in Ihrer App definieren. |
| `activity_attributes` | Erforderlich | Objekt | Die statischen Attributwerte für den Aktivitätstyp (z. B. die Namen der Sportteams, die sich nicht ändern). |
| `content_state` | Erforderlich | Objekt | Sie definieren die `ContentState`-Parameter, wenn Sie Ihre Live-Aktivität erstellen. Übergeben Sie die aktualisierten Werte für Ihren `ContentState` mit diesem Objekt.<br><br>Das Format dieser Anfrage muss mit der Struktur übereinstimmen, die Sie ursprünglich definiert haben. |
| `stale_date` | Optional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)-String) | Dieser Parameter teilt dem System mit, wann der Inhalt der Live-Aktivität in der UI der Nutzer:innen als veraltet markiert wird. |
| `notification` | Erforderlich | Objekt | Fügen Sie ein [`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object)-Objekt ein, um eine Push-Benachrichtigung zu definieren. Das Verhalten dieser Push-Benachrichtigung hängt davon ab, ob die Nutzer:innen aktiv sind oder ein Proxy-Gerät verwenden. {::nomarkdown}<ul><li>Wenn eine <code>notification</code> enthalten ist und die Nutzer:innen auf ihrem iPhone aktiv sind, wenn das Update zugestellt wird, wird die aktualisierte Live-Aktivitäts-UI nach unten geschoben und wie eine Push-Benachrichtigung angezeigt.</li><li>Wenn eine <code>notification</code> enthalten ist und die Nutzer:innen auf ihrem iPhone nicht aktiv sind, leuchtet der Bildschirm auf und zeigt die aktualisierte Live-Aktivitäts-UI auf dem Sperrbildschirm an.</li><li>Der <code>notification alert</code> wird nicht als normale Push-Benachrichtigung angezeigt. Wenn Nutzer:innen ein Proxy-Gerät wie eine Apple Watch besitzen, wird der <code>alert</code> dort angezeigt.</li></ul>{:/} |
| `external_user_ids` | Optional, wenn `user_aliases`, `segment_id` oder `custom_audience` bereitgestellt wird | String-Array | Siehe [externe Nutzer-ID]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields). |
| `user_aliases` | Optional, wenn `external_user_ids`, `segment_id` oder `custom_audience` bereitgestellt wird | Array von Nutzer-Alias-Objekten | Siehe [Nutzer-Alias-Objekt]({{site.baseurl}}/api/objects_filters/user_alias_object). |
| `segment_id` | Optional, wenn `external_user_ids`, `user_aliases` oder `custom_audience` bereitgestellt wird | String | Siehe [Segment-Bezeichner]({{site.baseurl}}/api/identifier_types). |
| `custom_audience` | Optional, wenn `external_user_ids`, `user_aliases` oder `segment_id` bereitgestellt wird | Verbundenes Zielgruppen-Objekt | Siehe [verbundene Zielgruppe]({{site.baseurl}}/api/objects_filters/connected_audience). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfrageparameter" }

Sie können `external_user_ids` und `user_aliases` in derselben Anfrage verwenden. Die kombinierte Array-Länge darf 50 nicht überschreiten. Braze spricht Nutzer:innen an, die einem der beiden Parameter entsprechen, und sendet nur einmal, wenn mehrere Bezeichner zur selben Person aufgelöst werden.

Kombinieren Sie `external_user_ids` oder `user_aliases` nicht mit `segment_id` oder `custom_audience`. Verwenden Sie bei diesem Endpunkt `custom_audience`, um verbundene Zielgruppenfilter zu übergeben.

## Beispielanfrage {#example-request}

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/messages/live_activity/start' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {YOUR_REST_API_KEY}' \
--data-raw '{
  "app_id": "{YOUR_APP_API_IDENTIFIER}",
  "activity_id": "football-chiefs-bills-2024-01-21",
  "content_state": {
    "teamOneScore": 0,
    "teamTwoScore": 0
  },
  "activity_attributes_type": "FootballActivity",
  "activity_attributes": {
    "team1Name": "Chiefs",
    "team2Name": "Bills"
  },
  "stale_date": "2024-01-22T16:55:49+0000",
  "notification": {
    "alert": {
      "body": "The game is starting! Tune in soon!",
      "title": "Chiefs v. Bills"
    }
  },
  "external_user_ids": ["user-id1", "user-id2"],
  "user_aliases": [
    {
      "alias_name": "user-name",
      "alias_label": "user-label"
    }
  ]
}'
```

## Antwort {#response}

Für diesen Endpunkt gibt es zwei Statuscode-Antworten: `201` und `4XX`.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Ein Statuscode `201` wird zurückgegeben, wenn die Anfrage korrekt formatiert ist und Braze sie erhalten hat. Der Statuscode `201` kann den folgenden Antworttext zurückgeben.

```json
{
  "message": "success"
}
```

### Beispiel für eine Fehlerantwort {#example-error-response}

Die Statuscode-Klasse `4XX` weist auf einen Client-Fehler hin. Weitere Informationen zu möglichen Fehlern finden Sie im Artikel [API-Fehler und -Antworten]({{site.baseurl}}/api/errors).

Der Statuscode `400` könnte den folgenden Antworttext zurückgeben.

```json
{
    "error": "\nProblem:\n  message body does not match declared format\nResolution:\n  when specifying application/json as content-type, you must pass valid application/json in the request's 'body' "
}
```

{% endapi %}