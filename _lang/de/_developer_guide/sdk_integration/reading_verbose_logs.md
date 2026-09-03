---
page_order: 1.5
nav_title: Ausführliche Protokolle lesen
article_title: Ausführliche Protokolle lesen
description: "Erfahren Sie, wie Sie die ausführliche Protokollausgabe des Braze SDK lesen und interpretieren, einschließlich der wichtigsten Einträge für Push-Benachrichtigungen, In-App-Nachrichten, Content Cards und Deeplinks."
---

# Ausführliche Protokolle lesen {#reading-verbose-logs}

> Auf dieser Seite wird erläutert, wie die ausführliche Protokollausgabe des Braze SDK interpretiert werden kann. Für jeden Messaging-Kanal finden Sie die wichtigsten Protokolleinträge, deren Bedeutung und häufige Probleme, auf die Sie achten sollten.

Bevor Sie beginnen, stellen Sie sicher, dass Sie [die ausführliche Protokollierung aktiviert]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging) haben und wissen, wie Sie Protokolle auf Ihrer Plattform erfassen können.

## Sitzungen {#sessions}

Sitzungen bilden die Grundlage der Braze-Analytics und der Nachrichtenzustellung. Viele Messaging-Features – darunter In-App Messages und Content Cards – erfordern den Start einer gültigen Sitzung, bevor sie funktionieren können. Wenn Sitzungen nicht korrekt protokolliert werden, sollten Sie dies zuerst untersuchen. Weitere Informationen zur Aktivierung des Sitzungs-Trackings finden Sie unter [Schritt 5: Tracking von Nutzer:innen-Sitzungen aktivieren]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android#android_step-5-enable-user-session-tracking).

### Wichtige Protokolleinträge {#key-log-entries}

{% tabs %}
{% tab Swift %}

**Sitzungsstart:**

```
Started user session (id: <SESSION_ID>)
```

**Sitzungsende:**

```
Ended user session (id: <SESSION_ID>, duration: <DURATION>s)
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: sessionEnd(duration: <DURATION>)
```

{% endtab %}
{% tab Android %}

**Sitzungsstart:**

Suchen Sie nach den folgenden Einträgen:

```
New session created with ID: <SESSION_ID>
Session start event for new session received
Completed the openSession call
Opened session with activity: <ACTIVITY_NAME>
```

Filtern Sie Netzwerkanfragen nach Ihrem konfigurierten Braze-Endpunkt (zum Beispiel sdk.iad-01.braze.com), um das Sitzungsstart-Ereignis (`ss`) zu sehen.

**Sitzungsende:**

```
Closed session with activity: <ACTIVITY_NAME>
Closed session with session ID: <SESSION_ID>
Requesting data flush on internal session close flush timer.
```

{% endtab %}
{% endtabs %}

### Was Sie überprüfen sollten {#what-to-check}

- Überprüfen Sie, dass ein Sitzungsstart-Protokolleintrag erscheint, wenn die App gestartet wird.
- Wenn Sie keinen Sitzungsstart sehen, prüfen Sie, ob das SDK korrekt initialisiert ist und ob `openSession` (Android) aufgerufen wird.
- Bestätigen Sie unter Android, dass eine Netzwerkanfrage an den Braze-Endpunkt gesendet wird. Wenn Sie diese nicht sehen, überprüfen Sie Ihren API-Schlüssel und die Endpunkt-Konfiguration.

## Push-Benachrichtigungen {#push-notifications}

Push-Benachrichtigungsprotokolle helfen Ihnen zu überprüfen, ob Geräte-Token registriert, Benachrichtigungen zugestellt und Klick-Events getrackt werden.

### Token-Registrierung {#token-registration}

Wenn eine Sitzung beginnt, registriert das SDK das Push-Token des Geräts bei Braze.

{% tabs %}
{% tab Swift %}

```
Updated push notification authorization:
- authorization: authorized

Received remote notifications device token: <PUSH_TOKEN>
```

Filtern Sie nach Anfragen an Ihren konfigurierten Braze-Endpunkt (z. B. sdk.iad-01.braze.com) und suchen Sie nach `push_token` in den Attributen des Request-Body:

```
"attributes": [
  {
    "push_token": "<PUSH_TOKEN>",
    "user_id": "<USER_ID>"
  }
]
```

Bestätigen Sie außerdem, dass die Geräteinformationen Folgendes enthalten:

```
"device": {
  "ios_push_auth": "authorized",
  "remote_notification_enabled": 1
}
```

{% endtab %}
{% tab Android %}

Suchen Sie nach dem FCM-Registrierungsprotokoll:

```
Registering for Firebase Cloud Messaging token using sender id: <SENDER_ID>
```

Überprüfen Sie Folgendes:

- `com_braze_firebase_cloud_messaging_registration_enabled` ist `true`.
- Die FCM-Sender-ID stimmt mit Ihrem Firebase-Projekt überein.

Ein häufiger Fehler ist `SENDER_ID_MISMATCH`, was bedeutet, dass die konfigurierte Sender-ID nicht mit Ihrem Firebase-Projekt übereinstimmt.

{% endtab %}
{% endtabs %}

### Worauf Sie achten sollten

- Wenn `push_token` im Request-Body fehlt, wurde das Token nicht erfasst. Überprüfen Sie die Push-Einrichtung in Ihrer App-Konfiguration.
- Wenn `ios_push_auth` den Wert `denied` oder `provisional` anzeigt, hat die/der Nutzer:in keine vollständige Push-Berechtigung erteilt.
- Wenn auf Android `SENDER_ID_MISMATCH` angezeigt wird, aktualisieren Sie Ihre FCM-Sender-ID, damit sie mit Ihrem Firebase-Projekt übereinstimmt.

### Push-Zustellung und Klick {#push-delivery-and-click}

Wenn eine Push-Benachrichtigung angetippt wird, protokolliert das SDK die Verarbeitung und die Klick-Events.

{% tabs %}
{% tab Swift %}

```
Processing push notification:
- date: <TIMESTAMP>
- silent: false
- userInfo: {
  "ab": { ... },
  "ab_uri": "<DEEP_LINK_OR_URL>",
  "aps": {
    "alert": {
      "body": "<MESSAGE_BODY>",
      "title": "<MESSAGE_TITLE>"
    }
  }
}
```

Gefolgt vom Klick-Event:

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: pushClick(campaignId: ...)
```

Wenn die Push-Benachrichtigung einen Deeplink enthält, sehen Sie außerdem:

```
Opening '<URL>':
- channel: notification
- useWebView: false
- isUniversalLink: false
```

{% endtab %}
{% tab Android %}

```
BrazeFirebaseMessagingService: Got Remote Message from FCM
```

Gefolgt vom Push-Payload und den Anzeige-Protokollen. Für Deeplinks suchen Sie nach dem Deep Link Delegate oder `UriAction`-Einträgen.

{% endtab %}
{% endtabs %}

### Worauf Sie achten sollten

- Überprüfen Sie, ob der Push-Payload den erwarteten `title`, `body` sowie etwaige Deeplinks (`ab_uri`) enthält.
- Bestätigen Sie, dass nach dem Antippen ein `pushClick`-Event protokolliert wird.
- Wenn das Klick-Event fehlt, überprüfen Sie, ob Ihr App-Delegate oder Benachrichtigungs-Handler Push-Events korrekt an das Braze SDK weiterleitet.

## In-App-Nachrichten {#in-app-messages}

In-App-Nachrichten-Logs zeigen Ihnen den vollständigen Lebenszyklus: Zustellung vom Server, Triggern basierend auf Ereignissen, Anzeige, Impression-Protokollierung und Klick-Tracking.

### Nachrichtenzustellung {#message-delivery}

Wenn eine:r Nutzer:in eine Sitzung startet und für eine In-App-Nachricht qualifiziert ist, empfängt das SDK den Nachrichten-Payload vom Server.

{% tabs %}
{% tab Swift %}

Filtern Sie nach Antworten von Ihrem konfigurierten Braze-Endpunkt (zum Beispiel sdk.iad-01.braze.com), die die In-App-Nachrichtendaten enthalten.

Der Antworttext enthält den Nachrichten-Payload, einschließlich:

```
"templated_message": {
  "data": {
    "message": "...",
    "type": "HTML",
    "message_close": "SWIPE",
    "trigger_id": "<TRIGGER_ID>"
  },
  "type": "inapp"
}
```

{% endtab %}
{% tab Android %}

Suchen Sie nach dem passenden Trigger-Ereignis-Log:

```
Triggering action: <CAMPAIGN_BSON_ID>
```

Dies bestätigt, dass die In-App-Nachricht einem Trigger-Ereignis zugeordnet wurde.

{% endtab %}
{% endtabs %}

### Nachrichtenanzeige und Impression {#message-display-and-impression}

{% tabs %}
{% tab Swift %}

```
In-app message ready for display:
- triggerId: (campaignId: <CAMPAIGN_ID>, ...)
- extras: { ... }
```

Gefolgt vom Impression-Log:

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: inAppMessageImpression(triggerIds: [...])
```

{% endtab %}
{% tab Android %}

```
handleExistingInAppMessagesInStackWithDelegate:: Displaying in-app message
```

{% endtab %}
{% endtabs %}

### Klick- und Button-Ereignisse {#click-and-button-events}

Wenn Nutzer:innen auf einen Button tippen oder die Nachricht schließen:

{% tabs %}
{% tab Swift %}

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: inAppMessageButtonClick(triggerIds: [...], buttonId: "<BUTTON_ID>")
```

Wenn keine weiteren getriggerten Nachrichten übereinstimmen, sehen Sie außerdem:

```
No matching trigger for event.
```

Dies ist das erwartete Verhalten, wenn keine zusätzlichen In-App-Nachrichten für das Ereignis konfiguriert sind.

{% endtab %}
{% tab Android %}

Filtern Sie nach Anfragen an Ihren konfigurierten Braze-Endpunkt (zum Beispiel sdk.iad-01.braze.com) und suchen Sie nach Ereignissen mit dem Namen `sbc` (Button-Klick) oder `si` (Impression) im Anfragetext.

{% endtab %}
{% endtabs %}

### Worauf Sie achten sollten

- Wenn die In-App-Nachricht nicht angezeigt wird, überprüfen Sie, ob zuerst ein Sitzungsstart protokolliert wurde.
- Filtern Sie nach Antworten von Ihrem konfigurierten Braze-Endpunkt, um zu bestätigen, dass der Nachrichten-Payload zugestellt wurde.
- Wenn Impressionen nicht protokolliert werden, überprüfen Sie, ob Sie nicht einen benutzerdefinierten `inAppMessageDisplay`-Delegate implementiert haben, der die Protokollierung unterdrückt.
- Wenn „No matching trigger for event“ erscheint, ist dies normal und bedeutet, dass keine zusätzlichen In-App-Nachrichten für dieses Ereignis konfiguriert sind.

## Content Cards

Mithilfe von Content-Card-Protokollen können Sie überprüfen, ob Karten mit dem Gerät synchronisiert und den Nutzer:innen angezeigt werden und ob Interaktionen (Impressionen, Klicks, Ablehnungen) nachverfolgt werden.

### Kartensynchronisierung {#card-sync}

Content Cards werden zu Beginn der Sitzung und bei einer manuellen Aktualisierung synchronisiert. Wenn keine Sitzung protokolliert ist, werden keine Content Cards angezeigt.

{% tabs %}
{% tab Swift %}

Filtern Sie die Antworten von Ihrem konfigurierten Braze-Endpunkt (z. B. sdk.iad-01.braze.com), die die Kartendaten enthalten.

Der Antworttext enthält die Kartendaten, darunter:

```
"cards": [
  {
    "id": "<CARD_ID>",
    "tt": "<CARD_TITLE>",
    "ds": "<CARD_DESCRIPTION>",
    "tp": "short_news",
    "v": 0,
    "cl": 0,
    "p": 1
  }
]
```

Schlüsselfelder:
- `v` (angesehen): `0` = nicht angesehen, `1` = angesehen
- `cl` (angeklickt): `0` = nicht angeklickt, `1` = angeklickt
- `p` (angeheftet): `0` = nicht angeheftet, `1` = angeheftet
- `tp` (Typ): `short_news`, `captioned_image`, `classic` usw.

{% endtab %}
{% tab Android %}

```
Requesting content cards sync.
```

Gefolgt von einer POST-Anfrage an Ihren konfigurierten Braze-Endpunkt (z. B. sdk.iad-01.braze.com), die Nutzer:innen- und Geräteinformationen enthält.

{% endtab %}
{% endtabs %}

### Impressionen, Klicks und Ablehnungen {#impressions-clicks-and-dismissals}

{% tabs %}
{% tab Swift %}

**Impression:**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardImpression(cardIds: [...])
```

**Klick:**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardClick(cardIds: [...])
```

Wenn die Karte eine URL enthält, sehen Sie außerdem:

```
Opening '<URL>':
- channel: contentCard
- useWebView: true
```

**Ablehnung:**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardDismissed(cardIds: [...])
```

{% endtab %}
{% tab Android %}

Filtern Sie Anfragen an Ihren konfigurierten Braze-Endpunkt (z. B. sdk.iad-01.braze.com) und suchen Sie nach Ereignisnamen im Anfragetext:
- `cci` — Content-Card-Impression
- `ccc` — Content-Card-Klick
- `ccd` — Content Card abgelehnt

{% endtab %}
{% endtabs %}

### Was zu überprüfen ist

- **Keine Karten angezeigt**: Überprüfen Sie, ob ein Sitzungsstart protokolliert wurde. Content Cards erfordern eine aktive Sitzung, um synchronisiert zu werden.
- **Fehlende Karten für neue Nutzer:innen**: Neue Nutzer:innen sehen möglicherweise bei ihrer ersten Sitzung keine Content Cards bis zur nächsten Sitzung. Dies ist das erwartete Verhalten.
- **Karte überschreitet die Größenbeschränkung**: Content Cards über 2 KB werden nicht angezeigt, und die Nachricht wird abgebrochen.
- **Karte bleibt nach Beendigung der Campaign bestehen**: Überprüfen Sie, ob die Synchronisierung nach Beendigung der Campaign abgeschlossen wurde. Content Cards werden nach einer erfolgreichen Synchronisierung vom Gerät entfernt. Stellen Sie beim Beenden einer Campaign sicher, dass die Option zum Entfernen aktiver Karten aus den Feeds der Nutzer:innen ausgewählt ist.

## Deeplinks {#deep-links}

Deeplink-Protokolle erscheinen bei Push-Benachrichtigungen, In-App-Nachrichten und Content Cards. Die Protokollstruktur ist unabhängig vom Quellkanal konsistent.

{% tabs %}
{% tab Swift %}

Wenn das SDK einen Deeplink verarbeitet:

```
Opening '<DEEP_LINK_URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: false
- isUniversalLink: false
- extras: { ... }
```

Dabei ist `<SOURCE_CHANNEL>` einer der folgenden Werte: `notification`, `inAppMessage` oder `contentCard`.

{% endtab %}
{% tab Android %}

Für Deeplinks suchen Sie nach den Einträgen **Deep Link Delegate** oder **UriAction** in Logcat. Um die Deeplink-Auflösung unabhängig zu testen, führen Sie den folgenden Befehl aus:

```bash
adb shell am start -W -a android.intent.action.VIEW -d "<YOUR_DEEP_LINK>" "<YOUR_PACKAGE_NAME>"
```

Damit wird bestätigt, ob der Deeplink außerhalb des Braze SDK korrekt aufgelöst wird.

{% endtab %}
{% endtabs %}

### Worauf Sie achten sollten

- Überprüfen Sie, ob die Deeplink-URL mit der in der Campaign konfigurierten URL übereinstimmt.
- Wenn der Deeplink über einen Kanal funktioniert (z. B. Push), aber nicht über einen anderen (z. B. Content Cards), prüfen Sie, ob Ihre Deeplink-Implementierung alle Kanäle unterstützt.
- Unter iOS erfordern Universal Links eine zusätzliche Behandlung. Wenn Universal Links über Braze-Kanäle nicht funktionieren, stellen Sie sicher, dass Ihre App das `BrazeDelegate`-Protokoll für die URL-Behandlung implementiert.
- Unter Android prüfen Sie, ob die automatische Deeplink-Behandlung deaktiviert ist, wenn Sie einen benutzerdefinierten Handler verwenden. Andernfalls kann der Standard-Handler mit Ihrer Implementierung in Konflikt geraten.

## Nutzeridentifikation {#user-identification}

Wenn ein:e Nutzer:in mit einer `external_id` identifiziert wird, protokolliert das SDK ein Change-User-Ereignis.

{% tabs %}
{% tab Android %}

```
changeUser called with: <EXTERNAL_ID>
```

Wichtige Hinweise:
- Rufen Sie `changeUser` auf, sobald sich die/der Nutzer:in anmeldet – je früher, desto besser.
- Wenn sich ein:e Nutzer:in abmeldet, gibt es keine Möglichkeit, `changeUser` aufzurufen, um sie/ihn wieder zu einem anonymen Profil zurückzusetzen.
- Wenn Sie keine anonymen Nutzer:innen möchten, rufen Sie `changeUser` beim Sitzungsstart oder beim App-Start auf.

{% endtab %}
{% tab Swift %}

Filtern Sie nach Anfragen an Ihren konfigurierten Braze-Endpunkt (zum Beispiel sdk.iad-01.braze.com) und suchen Sie im Anfrage-Body nach der Nutzeridentifikation:

```
"user_id": "<EXTERNAL_ID>"
```

{% endtab %}
{% endtabs %}

## Netzwerkanfragen {#network-requests}

Ausführliche Protokolle enthalten vollständige HTTP-Anfrage- und Antwortdetails für die SDK-Kommunikation mit Braze-Servern. Diese sind nützlich für die Diagnose von Verbindungsproblemen.

### Anfragestruktur {#request-structure}

Filtern Sie nach Anfragen an Ihren konfigurierten Braze-Endpunkt (zum Beispiel sdk.iad-01.braze.com). Die Anfragestruktur umfasst:

{% tabs %}
{% tab Swift %}

```
[http] request POST: <YOUR_BRAZE_ENDPOINT>
- Headers:
  - Content-Type: application/json
  - X-Braze-Api-Key: <REDACTED>
  - X-Braze-Req-Attempt: 1
  - X-Braze-Req-Tokens-Remaining: <COUNT>
- Body: { ... }
```

{% endtab %}
{% tab Android %}

```
Making request(id = <REQUEST_ID>) to <YOUR_BRAZE_ENDPOINT>
```

{% endtab %}
{% endtabs %}

### Worauf Sie achten sollten

- **API-Schlüssel**: Überprüfen Sie, ob `XBraze-ApiKey` mit dem API-Schlüssel Ihres Workspace übereinstimmt.
- **Endpunkt**: Bestätigen Sie, dass die Anfrage-URL mit Ihrem konfigurierten SDK-Endpunkt übereinstimmt.
- **Wiederholungsversuche**: Ein `XBraze-Req-Attempt`-Wert größer als 1 zeigt an, dass das SDK eine fehlgeschlagene Anfrage erneut versucht, was auf Verbindungsprobleme hindeuten kann.
- **Rate-Limiting**: `XBraze-Req-Tokens-Remaining` zeigt die verbleibenden Anfrage-Token an. Ein niedriger Wert kann darauf hinweisen, dass das SDK sich den Rate-Limits nähert.
- **Fehlende Anfragen**: Wenn Sie unter Android nach dem Sitzungsstart keine Anfrage an den Braze-Endpunkt sehen, überprüfen Sie Ihre API-Schlüssel- und Endpunkt-Konfiguration.

## Häufige Ereignisabkürzungen {#common-event-abbreviations}

In ausführlichen Protokoll-Payloads verwendet Braze abgekürzte Ereignisnamen. Hier eine Übersicht:

| Abkürzung | Ereignis |
|---|---|
| `ss` | Sitzungsstart |
| `se` | Sitzungsende |
| `si` | In-App-Nachricht-Impression |
| `sbc` | In-App-Nachricht-Button-Klick |
| `cci` | Content-Card-Impression |
| `ccc` | Content-Card-Klick |
| `ccd` | Content-Card abgelehnt |
| `lr` | Standort aufgezeichnet |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Häufige Ereignisabkürzungen" }

## Fehlerbehebung {#troubleshooting}

### Geofences werden auf Android SDK 13.1.0–15.x nicht ausgelöst {#geofences-not-triggering-on-android-sdk-131015x}

Braze Android SDK 13.1.0 bis 15.x hatte eine Regression, die dazu führen konnte, dass Geofence-Update-Ereignisse nicht aufgezeichnet wurden. Auf Geräten mit Android 10 oder älter konnten auch Standortaktualisierungen beim Sitzungsstart fehlschlagen. Führen Sie ein Upgrade auf Android SDK 16.0.0 oder höher durch. Informationen zur SDK-Einrichtung finden Sie unter [Geofences]({{site.baseurl}}/developer_guide/geofences).

### Wann kann ein Nutzerprofil 0 aufgezeichnete Sitzungen aufweisen? {#when-might-a-user-have-0-sessions-recorded-against-their-profile}

Ein Nutzerprofil kann 0 Sitzungen anzeigen, wenn Sie die:den Nutzer:in über die REST API ([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)) oder einen CSV-Import ohne die Felder **First session** oder **Last session** importieren. Sitzungen werden aufgezeichnet, wenn Nutzer:innen über das SDK mit Ihrer App interagieren. Weitere Informationen finden Sie unter [Nutzerprofil hat 0 Sitzungen]({{site.baseurl}}/developer_guide/analytics/tracking_sessions#user-profile-has-0-sessions).

### Diskrepanzen bei Nutzerdaten bei gleichzeitiger Verwendung von SDK und REST API {#user-data-discrepancies-when-using-the-sdk-and-rest-api-together}

Wenn Sie das SDK und die REST API gleichzeitig verwenden, können Race-Conditions zu Datendiskrepanzen führen. Nachdem Sie `changeUser()` aufgerufen haben, lassen Sie das SDK ausstehende Daten senden, bevor Sie kritische REST-API-Aufrufe durchführen, vermeiden Sie die Bündelung zeitkritischer Updates und erwägen Sie, eine kurze Verzögerung zwischen SDK- und API-Anfragen einzufügen. Informationen zum Verhalten von `changeUser()` finden Sie unter [Wie changeUser() funktioniert]({{site.baseurl}}/developer_guide/analytics/setting_user_ids#how-changeuser-works).

### Daten erreichen Braze nicht {#data-not-reaching-braze}

Wenn Daten Braze nicht erreichen, stellen Sie sicher, dass Ihre Firewall ausgehenden Datenverkehr zu Braze-API-Endpunkten und CDN-Anbietern zulässt. Führen Sie einen MTR-Test durch und verwenden Sie [Fastly Debug](https://www.fastly-debug.com/), während das Problem auftritt. Informationen zu Allowlisting und Fehlerbehebung bei der Konnektivität finden Sie unter [Probleme mit der API-Netzwerkverbindung]({{site.baseurl}}/api/network_connectivity_issues).