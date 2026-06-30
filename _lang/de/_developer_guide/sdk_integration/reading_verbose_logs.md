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

Sitzungen bilden die Grundlage für Analytics und die Nachrichtenzustellung von Braze. Viele Messaging-Features – einschließlich In-App-Nachrichten und Content Cards – erfordern eine gültige Sitzung, bevor sie funktionieren können. Sollten Sitzungen nicht korrekt protokolliert werden, untersuchen Sie dies zuerst. Weitere Informationen zum Aktivieren des Sitzungs-Trackings finden Sie unter [Schritt 5: Sitzungs-Tracking für Nutzer:innen aktivieren]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=android#android_step-5-enable-user-session-tracking).

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

Filtern Sie Netzwerkanfragen für Ihren konfigurierten Braze-Endpunkt (z. B. sdk.iad-01.braze.com), um das Sitzungsstart-Ereignis (`ss`) anzuzeigen.

**Sitzungsende:**

```
Closed session with activity: <ACTIVITY_NAME>
Closed session with session ID: <SESSION_ID>
Requesting data flush on internal session close flush timer.
```

{% endtab %}
{% endtabs %}

### Was zu überprüfen ist {#what-to-check}

- Überprüfen Sie, ob beim Start der App ein Sitzungsstart-Protokoll erscheint.
- Wenn Sie keinen Sitzungsstart sehen, prüfen Sie, ob das SDK ordnungsgemäß initialisiert ist und ob `openSession` (Android) aufgerufen wird.
- Überprüfen Sie auf Android, ob eine Netzwerkanfrage an den Braze-Endpunkt gesendet wird. Wenn Sie dies nicht sehen, überprüfen Sie Ihren API-Schlüssel und Ihre Endpunkt-Konfiguration.

## Push-Benachrichtigungen {#push-notifications}

Protokolle für Push-Benachrichtigungen helfen Ihnen zu überprüfen, ob Geräte-Token registriert sind, Benachrichtigungen zugestellt werden und Klick-Ereignisse nachverfolgt werden.

### Token-Registrierung {#token-registration}

Zu Beginn einer Sitzung registriert das SDK das Push-Token des Geräts bei Braze.

{% tabs %}
{% tab Swift %}

```
Updated push notification authorization:
- authorization: authorized

Received remote notifications device token: <PUSH_TOKEN>
```

Filtern Sie Anfragen an Ihren konfigurierten Braze-Endpunkt (z. B. sdk.iad-01.braze.com) und suchen Sie nach `push_token` in den Attributen des Anfragetextes:

```
"attributes": [
  {
    "push_token": "<PUSH_TOKEN>",
    "user_id": "<USER_ID>"
  }
]
```

Überprüfen Sie außerdem, ob die Geräteinformationen Folgendes enthalten:

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
- Die FCM-Absender-ID entspricht Ihrem Firebase-Projekt.

Ein häufiger Fehler ist `SENDER_ID_MISMATCH`, was bedeutet, dass die konfigurierte Absender-ID nicht mit Ihrem Firebase-Projekt übereinstimmt.

{% endtab %}
{% endtabs %}

### Was zu überprüfen ist

- Falls `push_token` im Anfragetext fehlt, wurde das Token nicht erfasst. Überprüfen Sie die Push-Einstellungen in Ihrer App-Konfiguration.
- Wenn `ios_push_auth` den Wert `denied` oder `provisional` anzeigt, haben die Nutzer:innen keine vollständige Push-Berechtigung erteilt.
- Wenn Sie auf Android `SENDER_ID_MISMATCH` sehen, aktualisieren Sie Ihre FCM-Absender-ID, damit sie mit Ihrem Firebase-Projekt übereinstimmt.

### Push-Zustellung und Klick {#push-delivery-and-click}

Wenn eine Push-Benachrichtigung angetippt wird, protokolliert das SDK die Verarbeitungs- und Klick-Ereignisse.

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

Gefolgt vom Klick-Ereignis:

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

Gefolgt von der Push-Nutzlast und den Anzeigeprotokollen. Für Deeplinks suchen Sie nach den Einträgen „Deep Link Delegate“ oder `UriAction`.

{% endtab %}
{% endtabs %}

### Was zu überprüfen ist

- Überprüfen Sie, ob die Push-Nutzlast die erwarteten Werte für `title`, `body` und alle Deeplinks (`ab_uri`) enthält.
- Bestätigen Sie, dass ein `pushClick`-Ereignis nach dem Antippen protokolliert wird.
- Sollte das Klick-Ereignis fehlen, prüfen Sie, ob Ihr App-Delegate oder Benachrichtigungs-Handler Push-Ereignisse ordnungsgemäß an das Braze SDK weiterleitet.

## In-App-Nachrichten {#in-app-messages}

Die In-App-Nachrichtenprotokolle zeigen Ihnen den gesamten Lebenszyklus: Zustellung vom Server, Auslösung basierend auf Ereignissen, Anzeige, Impression-Protokollierung und Klick-Tracking.

### Nachrichtenzustellung {#message-delivery}

Wenn Nutzer:innen eine Sitzung starten und für eine In-App-Nachricht berechtigt sind, empfängt das SDK die Nachrichtennutzlast vom Server.

{% tabs %}
{% tab Swift %}

Filtern Sie die Antworten von Ihrem konfigurierten Braze-Endpunkt (z. B. sdk.iad-01.braze.com), die die In-App-Nachrichtendaten enthalten.

Der Antworttext enthält die Nachrichtennutzlast, einschließlich:

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

Suchen Sie nach dem Protokoll für das auslösende Ereignis:

```
Triggering action: <CAMPAIGN_BSON_ID>
```

Dies bestätigt, dass die In-App-Nachricht einem Auslöseereignis zugeordnet wurde.

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

Gefolgt vom Impression-Protokoll:

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

Dies ist das erwartete Verhalten, wenn für das Ereignis keine zusätzlichen In-App-Nachrichten konfiguriert sind.

{% endtab %}
{% tab Android %}

Filtern Sie Anfragen an Ihren konfigurierten Braze-Endpunkt (z. B. sdk.iad-01.braze.com) und suchen Sie nach Ereignissen mit dem Namen `sbc` (Button-Klick) oder `si` (Impression) im Anfragetext.

{% endtab %}
{% endtabs %}

### Was zu überprüfen ist

- Sollte die In-App-Nachricht nicht angezeigt werden, überprüfen Sie zunächst, ob ein Sitzungsstart protokolliert wurde.
- Filtern Sie die Antworten von Ihrem konfigurierten Braze-Endpunkt, um zu bestätigen, dass die Nachrichtennutzlast zugestellt wurde.
- Falls keine Impressionen protokolliert werden, prüfen Sie, ob Sie einen benutzerdefinierten `inAppMessageDisplay`-Delegaten implementiert haben, der die Protokollierung unterdrückt.
- Wenn „Kein passender Auslöser für Ereignis“ angezeigt wird, ist dies normal und bedeutet, dass für dieses Ereignis keine zusätzlichen In-App-Nachrichten konfiguriert sind.

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

Deeplink-Protokolle erscheinen in Push-Benachrichtigungen, In-App-Nachrichten und Content Cards. Die Protokollstruktur ist unabhängig vom Quellkanal konsistent.

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

Wobei `<SOURCE_CHANNEL>` eines der folgenden ist: `notification`, `inAppMessage` oder `contentCard`.

{% endtab %}
{% tab Android %}

Für Deeplinks suchen Sie in Logcat nach den Einträgen **Deep Link Delegate** oder **UriAction**. Um die Deeplink-Auflösung unabhängig zu testen, führen Sie den folgenden Befehl aus:

```bash
adb shell am start -W -a android.intent.action.VIEW -d "<YOUR_DEEP_LINK>" "<YOUR_PACKAGE_NAME>"
```

Dies bestätigt, ob der Deeplink außerhalb des Braze SDK korrekt aufgelöst wird.

{% endtab %}
{% endtabs %}

### Was zu überprüfen ist

- Überprüfen Sie, ob die Deeplink-URL mit der in der Campaign konfigurierten URL übereinstimmt.
- Falls der Deeplink über einen Kanal (z. B. Push) funktioniert, jedoch nicht über einen anderen (z. B. Content Cards), prüfen Sie, ob Ihre Deeplink-Implementierung alle Kanäle unterstützt.
- Unter iOS erfordern Universal Links eine zusätzliche Behandlung. Sollten Universal Links über Braze-Kanäle nicht funktionieren, überprüfen Sie, ob Ihre App das `BrazeDelegate`-Protokoll für die URL-Verarbeitung implementiert.
- Überprüfen Sie auf Android, ob die automatische Deeplink-Verarbeitung deaktiviert ist, falls Sie einen angepassten Handler verwenden. Andernfalls kann es zu Konflikten zwischen dem Standard-Handler und Ihrer Implementierung kommen.

## Nutzer:innen-Identifikation {#user-identification}

Wenn Nutzer:innen mit einer `external_id` identifiziert werden, protokolliert das SDK ein Ereignis zur Nutzer:innen-Änderung.

{% tabs %}
{% tab Android %}

```
changeUser called with: <EXTERNAL_ID>
```

Wichtige Informationen:
- Rufen Sie `changeUser` auf, sobald sich Nutzer:innen anmelden – je früher, desto besser.
- Wenn sich Nutzer:innen abmelden, gibt es keine Möglichkeit, `changeUser` aufzurufen, um sie wieder in anonyme Nutzer:innen zurückzuversetzen.
- Wenn Sie keine anonymen Nutzer:innen wünschen, rufen Sie `changeUser` während des Sitzungsstarts oder beim App-Start auf.

{% endtab %}
{% tab Swift %}

Filtern Sie Anfragen an Ihren konfigurierten Braze-Endpunkt (z. B. sdk.iad-01.braze.com) und suchen Sie im Anfragetext nach der Nutzer:innen-Identifikation:

```
"user_id": "<EXTERNAL_ID>"
```

{% endtab %}
{% endtabs %}

## Netzwerkanfragen {#network-requests}

Ausführliche Protokolle enthalten vollständige Details zu HTTP-Anfragen und -Antworten für die SDK-Kommunikation mit Braze-Servern. Diese sind hilfreich bei der Diagnose von Verbindungsproblemen.

### Anfragestruktur {#request-structure}

Filtern Sie Anfragen an Ihren konfigurierten Braze-Endpunkt (z. B. sdk.iad-01.braze.com). Die Anfragestruktur umfasst:

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

### Was zu überprüfen ist

- **API-Schlüssel**: Überprüfen Sie, ob `X-Braze-Api-Key` mit dem API-Schlüssel Ihres Workspaces übereinstimmt.
- **Endpunkt**: Bestätigen Sie, dass die Anfrage-URL mit Ihrem konfigurierten SDK-Endpunkt übereinstimmt.
- **Wiederholungsversuche**: Ein `X-Braze-Req-Attempt`-Wert größer als 1 bedeutet, dass das SDK eine fehlgeschlagene Anfrage erneut versucht, was auf Verbindungsprobleme hindeuten kann.
- **Rate-Limiting**: `X-Braze-Req-Tokens-Remaining` zeigt die verbleibenden Anfrage-Token an. Ein niedriger Wert kann darauf hindeuten, dass das SDK die Rate-Limits erreicht.
- **Fehlende Anfragen**: Wenn Sie auf Android nach dem Sitzungsstart keine Anfrage an den Braze-Endpunkt sehen, überprüfen Sie Ihren API-Schlüssel und die Endpunkt-Konfiguration.

## Gängige Ereignisabkürzungen {#common-event-abbreviations}

In ausführlichen Protokollnutzlasten verwendet Braze abgekürzte Ereignisnamen. Hier ist eine Referenz:

| Abkürzung | Ereignis |
|---|---|
| `ss` | Sitzungsstart |
| `se` | Sitzungsende |
| `si` | In-App-Nachrichten-Impression |
| `sbc` | In-App-Nachrichten-Button-Klick |
| `cci` | Content-Card-Impression |
| `ccc` | Content-Card-Klick |
| `ccd` | Content Card abgelehnt |
| `lr` | Standort aufgezeichnet |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Gängige Ereignisabkürzungen" }

## Fehlerbehebung {#troubleshooting}

### Wann kann ein Nutzerprofil 0 Sitzungen aufweisen? {#when-might-a-user-have-0-sessions-recorded-against-their-profile}

Ein Nutzerprofil kann 0 Sitzungen anzeigen, wenn Sie Nutzer:innen über die REST API ([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)) oder einen CSV-Import ohne die Felder **Erste Sitzung** oder **Letzte Sitzung** importieren. Sitzungen werden aufgezeichnet, wenn Nutzer:innen über das SDK mit Ihrer App interagieren. Weitere Details finden Sie unter [Nutzerprofil hat 0 Sitzungen]({{site.baseurl}}/developer_guide/analytics/tracking_sessions#user-profile-has-0-sessions).

### Datendiskrepanzen bei gleichzeitiger Verwendung von SDK und REST API {#user-data-discrepancies-when-using-the-sdk-and-rest-api-together}

Wenn Sie das SDK und die REST API gleichzeitig verwenden, können Race-Conditions zu Datendiskrepanzen führen. Nachdem Sie `changeUser()` aufgerufen haben, lassen Sie das SDK ausstehende Daten senden, bevor Sie kritische REST-API-Aufrufe durchführen. Vermeiden Sie das Bündeln zeitkritischer Updates und erwägen Sie, eine kurze Verzögerung zwischen SDK- und API-Anfragen einzufügen. Informationen zum Verhalten von `changeUser()` finden Sie unter [Wie changeUser() funktioniert]({{site.baseurl}}/developer_guide/analytics/setting_user_ids#how-changeuser-works).

### Daten erreichen Braze nicht {#data-not-reaching-braze}

Wenn Daten Braze nicht erreichen, bestätigen Sie, dass Ihre Firewall ausgehenden Datenverkehr zu Braze-API-Endpunkten und CDN-Anbietern zulässt. Führen Sie einen MTR-Test durch und verwenden Sie [Fastly Debug](https://www.fastly-debug.com/), während das Problem auftritt. Informationen zum Allowlisting und zur Fehlerbehebung bei Verbindungsproblemen finden Sie unter [API-Netzwerkverbindungsprobleme]({{site.baseurl}}/api/network_connectivity_issues).