---
nav_title: Angepasster Currents-Konnektor
alias: /currents_connector/
hidden: true
---

# Angepasster Currents-Konnektor {#custom-currents-connector}

> Erfahren Sie, wie Sie einen angepassten Currents-Konnektor integrieren, damit Sie Event-Daten von Braze in Echtzeit abrufen können, um individuellere Analytics, Berichte und Automatisierung zu ermöglichen.

## Voraussetzungen {#prerequisites}

Um einen angepassten Currents-Konnektor in Braze zu integrieren, müssen Sie eine Endpunkt-URL und ein [optionales Authentifizierungs-Token](#authentication) bereitstellen.

Wenn Sie mehr als eine App-Gruppe in Braze haben, müssen Sie außerdem für jede Gruppe einen angepassten Currents-Konnektor konfigurieren. Sie können jedoch alle App-Gruppen auf denselben Endpunkt verweisen oder auf einen Endpunkt mit einem zusätzlichen `GET`-Parameter, wie z. B. `your_app_group_key="Brand A"`.

## Verhinderung von Datenverlusten {#preventing-data-loss}

### Fehlerüberwachung {#error-monitoring}

Um Datenverluste und Dienstunterbrechungen zu vermeiden, ist es wichtig, dass Sie Ihre Endpunkte jederzeit überwachen und versuchen, schwerwiegende Fehler oder Ausfallzeiten innerhalb von 24 Stunden zu beheben.

Bei den meisten Fehlertypen (z. B. Serverfehler, Netzwerkverbindungsfehler usw.) wird Braze die Übertragung von Events bis zu 24 Stunden lang in die Warteschlange stellen und erneut versuchen. Nach dieser Zeit werden nicht übermittelte Events verworfen. Konnektoren mit konstant schlechten Fehlerraten oder Uptime werden automatisch gesperrt.

### Änderungsresilienz {#change-resilience}

Gelegentlich nehmen wir nicht-unterbrechende Änderungen an Braze-Currents-Schemata vor. Nicht-unterbrechende Änderungen sind neue optionale Spalten oder Event-Typen.

Normalerweise kündigen wir diese Änderungen mit einer Frist von zwei Wochen an, aber manchmal ist das nicht möglich. Es ist wichtig, dass Sie Ihre Integration so gestalten, dass sie mit nicht erkannten Feldern oder Event-Typen umgehen kann, da es sonst wahrscheinlich zu Datenverlusten kommen wird.

{% alert tip %}
Die vollständige Liste der Currents-Event-Schemata finden Sie unter [Messaging-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/).
{% endalert %}

## Batching und Serialisierung {#batching-and-serialization}

Das Zieldatenformat ist JSON über HTTPS. Standardmäßig werden die Events in 100er-Gruppen zusammengefasst, basierend auf folgenden Kriterien:

- **Anzahl der Events in der Warteschlange**: Wenn zum Beispiel die Stapelgröße für 200 Events konfiguriert ist und sich 200 Events in der Warteschlange befinden.
- **Dauer eines Events:** Normalerweise werden Events nicht in die Warteschlange gestellt, wenn ein Event länger als 15 Minuten dauert. Jeder Event-Typ hat eine eigene Warteschlange, sodass die Latenzzeit je nach Event-Typ variieren kann.

Die Events werden dann als JSON-Array aller Events im folgenden Format an den Endpunkt gesendet:

```json
{"events": [event1, event2, event3, etc...]}
```

Es gibt ein JSON-Objekt der obersten Ebene mit dem Schlüssel `"events"`, das auf ein Array weiterer JSON-Objekte abgebildet wird, die jeweils ein einzelnes Event darstellen.

## Payload-Beispiele {#payload-examples}

Die folgenden Beispiele zeigen Payloads für einzelne Events, d. h. die Payloads gehören zu einem größeren Array von JSON-Objekten, wobei jedes JSON-Objekt ein einzelnes Event im Batch darstellt.

Außerdem weicht ihre Struktur leicht von der flachen Struktur der [Messaging-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) ab. Sie enthalten insbesondere zwei Unterobjekte:

| Name | Beschreibung |
|----|-----------|
| `"user"` | Enthält Nutzer:innen-Eigenschaften wie `user_id`, `external_user_id`, `device_id` und `timezone`. |
| `"properties"` | Enthält Attribute eines Events, wie z. B. die `app/campaign/canvas/platform`, auf die es sich bezieht. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Wenn ein nachgelagerter Endpunkt eine Payload mit null Events oder einen leeren Anfragekörper empfängt, sollte das Ergebnis als No-Op betrachtet werden, d. h. es sollten keine nachgelagerten Effekte durch diesen Aufruf auftreten. Sie sollten jedoch trotzdem den `Authorization`-Header überprüfen (wie bei einem normalen API-Aufruf) und bei [ungültigen Zugangsdaten](#authentication) eine entsprechende HTTP-Antwort geben, z. B. `401` oder `403`. Damit weiß Braze, dass die Zugangsdaten des Konnektors gültig sind.

### Campaign-assoziierte Events {#campaign-associated-events}

Hier finden Sie einige Beispiel-Event-Payloads für verschiedene Events, wie sie erscheinen würden, wenn sie mit einer Campaign verbunden wären:

#### In-App-Nachricht-Klick {#in-app-message-click}

```json
// In-App Message Click: users.messages.inappmessage.Click
{
  "event_type": "users.messages.inappmessage.Click",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "platform": "android",
     "os_version": "Android (N)",
    "device_model": "Nexus 5X",
    "button_id": "0",
    "send_id": "f123456789abcdef01234567"
  }
}
```

#### Push-Benachrichtigung senden {#push-notification-send}

```json
// Push Notification Send: users.messages.pushnotification.Send
{
  "event_type": "users.messages.pushnotification.Send",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "send_id": "f123456789abcdef01234567",
    "dispatch_id": "01234567-89ab-cdef-0123-456789abcdef"
  }
}
```

#### E-Mail-Öffnung {#email-open}

```json
// Email Open: users.messages.email.Open
{
  "event_type": "users.messages.email.Open",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "dispatch_id": "12345qwert",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "email_address": "test@test.com",
    "send_id": "f123456789abcdef01234567",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
  }
}
```

#### SMS-Zustellung {#sms-delivery}

```json
// SMS Delivery: users.messages.sms.Delivery
{
  "event_type": "users.messages.sms.Delivery",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "campaign_id": "11234567-89ab-cdef-0123-456789abcdef",
    "campaign_name": "Test Campaign",
    "dispatch_id": "12345qwert",
    "message_variation_id": "c1234567-89ab-cdef-0123-456789abcdef",
    "message_variation_name": "Test Message Variation",
    "to_phone_number": "+16462345678",
    "subscription_group_id": "41234567-89ab-cdef-0123-456789abcdef",
    "from_phone_number": "+12123470922"
  }
}
```

### Canvas-assoziierte Events {#canvas-associated-events}

Hier finden Sie einige Beispiel-Event-Payloads für verschiedene Events, wie sie erscheinen würden, wenn sie mit einem Canvas verbunden wären:

#### In-App-Nachricht-Klick {#in-app-message-click}

```json
// In-App Message Click: users.messages.inappmessage.Click
{
  "event_type": "users.messages.inappmessage.Click",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Campaign",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "platform": "android",
    "os_version": "Android (N)",
    "device_model": "Nexus 5X",
    "button_id": "0",
    "send_id": "f123456789abcdef01234567"
  }
}
```

#### Push-Benachrichtigung senden {#push-notification-send}

```json
// Push Notification Send: users.messages.pushnotification.Send
{
  "event_type": "users.messages.pushnotification.Send",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Campaign",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "send_id": "f123456789abcdef01234567",
    "dispatch_id": "01234567-89ab-cdef-0123-456789abcdef"
  }
}
```

#### E-Mail-Öffnung {#email-open}

```json
// Email Open: users.messages.email.Open
{
  "event_type": "users.messages.email.Open",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Canvas",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "dispatch_id": "12345qwert",
    "email_address": "test@test.com",
    "send_id": "f123456789abcdef01234567",
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
  }
}
```

#### SMS-Zustellung {#sms-delivery}

```json
// SMS Delivery: users.messages.sms.Delivery
{
  "event_type": "users.messages.sms.Delivery",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "timezone": "America/Chicago"
  },
  "properties": {
    "canvas_id": "11234567-89ab-cdef-0123-456789abcdef",
    "canvas_name": "My Cool Canvas",
    "canvas_variation_id": "31234567-89ab-cdef-0123-456789abcdef",
    "canvas_step_id": "41234567-89ab-cdef-0123-456789abcdef",
    "dispatch_id": "12345qwert",
    "to_phone_number": "+16462345678",
    "subscription_group_id": "41234567-89ab-cdef-0123-456789abcdef",
    "from_phone_number": "+12123470922"
  }
}
```

### Andere Events {#other-events}

Hier finden Sie einige Beispiel-Event-Payloads für verschiedene andere Events, die weder mit Campaigns noch mit Canvases verbunden sind:

#### Angepasstes Event {#custom-event}

```json
// Custom Event: users.behaviors.CustomEvent
{
  "event_type": "users.behaviors.CustomEvent",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "name": "custom event name",
    "ad_id": "01234567-89ab-cdef-0123-456789abcdef",
    "ad_id_type": "roku_ad_id",
    "ad_tracking_enabled": true,
    "custom_properties": {
      "string property name": "a",
      "number property name": 1,
      "list property name": ["a", "b"]
    }
  }
}
```

#### Kauf-Event {#purchase-event}

```json
// Purchase Event: users.behaviors.Purchase
{
  "event_type": "users.behaviors.Purchase",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id"
    "device_id": "fedcba87-6543-210f-edc-ba9876543210",
    "timezone": "America/Chicago"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "product_id": "1234",
    "price": 12.34,
    "currency": "AED,
    "ad_id": "01234567-89ab-cdef-0123-456789abcdef",
    "ad_id_type": "roku_ad_id",
    "ad_tracking_enabled": true,
    "purchase_properties": {
      "string property name": "a",
      "number property name": 1,
      "list property name": ["a", "b"]
    }
  }
}
```

#### Sitzungsbeginn {#session-start}

```json
// Session Start: users.behaviors.app.SessionStart
{
  "event_type": "users.behaviors.app.SessionStart",
  "id": "a1234567-89ab-cdef-0123-456789abcdef",
  "time": 1477502783,
  "user": {
    "user_id": "0123456789abcdef01234567",
    "external_user_id": "user_id",
    "device_id": "fedcba87-6543-210f-edc-ba9876543210"
  },
  "properties": {
    "app_id": "01234567-89ab-cdef-0123-456789abcdef",
    "platform": "ios",
    "os_version": "iOS 10.3.1",
    "device_model": "iPhone 7 Plus",
    "session_id": "b1234567-89ab-cdef-0123-456789abcdef"
  }
}
```

## Authentifizierung {#authentication}

Authentifizierungs-Token in Ihrer Payload sind optional. Sie können über einen HTTP-`Authorization`-Header unter Verwendung des `Bearer`-Autorisierungsschemas übergeben werden, wie in [RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1) beschrieben. Obwohl dies optional ist, wird Braze bei der Übergabe eines Authentifizierungs-Tokens dieses immer zuerst validieren&#8212;auch wenn keine Events in der Payload enthalten sind.

Gemäß RFC 6750 sollten Token Base64-kodierte Werte mit mindestens einem Zeichen sein. Beachten Sie, dass nach RFC 6750 Token zusätzlich zu den normalen Base64-Zeichen auch die folgenden Zeichen enthalten dürfen: `-`, `.`, `_` und `~`. Sie können wählen, ob Sie diese Zeichen in Ihr Token aufnehmen möchten oder nicht&#8212;es muss jedoch im Base64-Format vorliegen.

Wenn der `Authorization`-Header vorhanden ist, wird er außerdem im folgenden Format erstellt:

```plaintext
"Authorization: Bearer " + <token>
```

Wenn Ihr Authentifizierungs-Token beispielsweise `0p3n5354m3==` lautet, sollte Ihr `Authorization`-Header in etwa wie folgt aussehen:

```plaintext
Authorization: Bearer 0p3n5354m3==
```

{% alert note %}
In Zukunft werden wir möglicherweise `Authorization`-Header verwenden, um ein angepasstes Schlüssel-Wert-Paar-Autorisierungsschema zu implementieren, das speziell auf Braze zugeschnitten ist. Dies würde der [RFC 7235-Spezifikation](https://tools.ietf.org/html/rfc7235) entsprechen, mit der einige Unternehmen wie Amazon Web Services (AWS) ihre Authentifizierungssysteme implementieren.
{% endalert %}

## Versionierung {#versioning}

Alle Anfragen unserer HTTP-Konnektor-Integration werden mit einem angepassten Header gesendet, der die Version der Currents-Anfrage angibt:

```plaintext
Braze-Currents-Version: 1
```

Die Version wird immer `1` sein, da wir nicht erwarten, diese Zahl sehr oft zu erhöhen, wenn überhaupt.

Genau wie unsere [Data-Warehouse-Speicherschemata]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics?redirected=1) ist jedes Event-Feld in einem einzelnen Event gemäß der [Apache-Avro](https://avro.apache.org/)-Definition von Abwärtskompatibilität garantiert abwärtskompatibel mit früheren Event-Payload-Versionen:

1. Bestimmte Event-Felder haben im Laufe der Zeit garantiert immer den gleichen Datentyp.
2. Alle neuen Felder, die im Laufe der Zeit zur Payload hinzugefügt werden, müssen von allen Parteien als optional betrachtet werden.
3. Erforderliche Felder werden nie entfernt.

## Fehlerbehandlung und Wiederholungsmechanismus {#error-handling-and-retry-mechanism}

Wenn ein Fehler auftritt, stellt Braze die Anfrage in eine Warteschlange und wiederholt sie anhand des empfangenen HTTP-Rückgabecodes. Die Wiederholungsversuche werden mindestens zwei Tage lang fortgesetzt, solange die Daten im System gepuffert sind. Bleiben Daten länger als 24 Stunden liegen, wird unser Bereitschaftsdienst automatisch alarmiert. Zurzeit besteht unsere Backoff-Strategie darin, es regelmäßig zu wiederholen.

Wenn Ihre Currents-Integration anfängt, `4XX`-Fehler zu melden, sendet Braze Ihnen automatisch eine Benachrichtigungs-E-Mail und verlängert die Aufbewahrungsfrist automatisch auf mindestens sieben Tage.

Jeder HTTP-Fehlercode, der nicht unten aufgeführt ist, wird als HTTP-`5XX`-Fehler behandelt.

{% alert warning %}
Wenn der Wiederholungsmechanismus von Braze ein Event länger als 24 Stunden nicht zustellen kann, kommt es zu einem Datenverlust.
{% endalert %}

Die folgenden HTTP-Statuscodes werden von unserem Konnektor-Client erkannt:

<table>
  <thead>
    <tr>
      <th>Statuscode</th>
      <th>Antwort</th>
      <th>Beschreibung</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2XX</code></td>
      <td>Erfolg</td>
      <td>Event-Daten werden nicht erneut gesendet.</td>
    </tr>
    <tr>
      <td><code>5XX</code></td>
      <td>Serverseitiger Fehler</td>
      <td>Event-Daten werden in einem exponentiellen Backoff-Muster mit Jitter erneut gesendet. Wenn die Daten nicht innerhalb von 24 Stunden erfolgreich gesendet werden, werden sie gelöscht.</td>
    </tr>
    <tr>
      <td><code>400</code></td>
      <td>Clientseitiger Fehler</td>
      <td>Der Konnektor hat mindestens ein fehlerhaftes Event gesendet. Die Event-Daten werden in Stapel der Größe 1 aufgeteilt und erneut gesendet. Alle Events in diesen Stapeln der Größe 1, die eine weitere <code>400</code>-Antwort erhalten, werden dauerhaft gelöscht. Wiederholte Vorkommen sollten Sie melden.</td>
    </tr>
    <tr>
      <td><code>401</code></td>
      <td>Nicht autorisiert</td>
      <td>Der Konnektor wurde mit ungültigen Zugangsdaten konfiguriert. Event-Daten werden mit einer Verzögerung von 2–5 Minuten erneut gesendet. Wenn innerhalb von 48 Stunden keine Lösung gefunden wird, werden die Event-Daten gelöscht.</td>
    </tr>
    <tr>
      <td><code>403</code></td>
      <td>Verboten</td>
      <td>Der Konnektor wurde mit ungültigen Zugangsdaten konfiguriert. Event-Daten werden mit einer Verzögerung von 2–5 Minuten erneut gesendet. Wenn innerhalb von 48 Stunden keine Lösung gefunden wird, werden die Event-Daten gelöscht.</td>
    </tr>
    <tr>
      <td><code>404</code></td>
      <td>Nicht gefunden</td>
      <td>Der Konnektor wurde mit ungültigen Zugangsdaten konfiguriert. Event-Daten werden mit einer Verzögerung von 2–5 Minuten erneut gesendet. Wenn innerhalb von 48 Stunden keine Lösung gefunden wird, werden die Event-Daten gelöscht.</td>
    </tr>
    <tr>
      <td><code>413</code></td>
      <td>Payload zu groß</td>
      <td>Die Event-Daten werden in kleinere Stapel aufgeteilt und erneut gesendet.</td>
    </tr>
    <tr>
      <td><code>429</code></td>
      <td>Zu viele Anfragen</td>
      <td>Zeigt Rate-Limiting an. Event-Daten werden in einem exponentiellen Backoff-Muster mit Jitter erneut gesendet. Wenn die Daten nicht innerhalb von 24 Stunden erfolgreich gesendet werden, werden sie gelöscht.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }