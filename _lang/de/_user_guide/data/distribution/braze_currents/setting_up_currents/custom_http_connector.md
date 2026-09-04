---
nav_title: Benutzerdefinierter Currents-Export
article_title: Benutzerdefinierter Currents-Export
alias: /currents/custom_http_connector/
page_order: 3
page_type: reference
tool: Currents
description: "Dieser Referenzartikel beschreibt, wie Sie einen benutzerdefinierten Currents-Export einrichten, um Braze-Currents-Event-Daten in Echtzeit direkt an Ihren eigenen HTTP-Endpunkt zu streamen."
---

# Benutzerdefinierter Currents-Export {#custom-currents-export}

> Erfahren Sie, wie Sie einen benutzerdefinierten Currents-Konnektor integrieren, um Event-Daten von Braze in Echtzeit zu erhalten und so individuellere Analytics, Berichte und Automatisierung zu ermöglichen.

{% alert note %}
Dieses Feature wird in der technischen Dokumentation und in API-Referenzen auch als „Custom HTTP Connector“ bezeichnet.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um einen angepassten Currents-Konnektor in Braze zu integrieren, müssen Sie eine Endpunkt-URL und ein [optionales Authentifizierungstoken](#authentication) bereitstellen.

Wenn Sie außerdem mehr als eine App-Gruppe in Braze haben, müssen Sie einen angepassten Currents-Konnektor für jede Gruppe konfigurieren. Sie können jedoch alle App-Gruppen auf denselben Endpunkt oder auf einen Endpunkt mit einem zusätzlichen `GET`-Parameter verweisen, z. B. `your_app_group_key="Brand A"`.

## Integration {#integration}

### Schritt 1: Endpunkt einrichten {#step-1-set-up-your-endpoint}

Sie benötigen eine Endpunkt-URL, um diese Integration zu konfigurieren. Ihr Endpunkt sollte HTTP-POST-Anfragen empfangen können und einen `2XX`-Statuscode zurückgeben, um den erfolgreichen Empfang von Events zu bestätigen. Wenn Sie Anfragen von Braze authentifizieren möchten, benötigen Sie außerdem ein Bearer-Token.

### Schritt 2: Braze-Currents konfigurieren {#step-2-configure-braze-currents}

Navigieren Sie in Braze zu **Partnerintegrationen** > **Datenexport**, klicken Sie auf **Create New Current** und wählen Sie **Custom Currents Export** aus.

Geben Sie Ihrem Export einen Namen und eine Kontakt-E-Mail-Adresse an und fahren Sie dann mit der Seite **Current Details** fort. Geben Sie auf dieser Seite Ihre Endpunkt-URL und ein optionales Bearer-Token ein.

Nachdem Sie Ihre Zugangsdaten konfiguriert haben, aktivieren Sie alle Nachrichten-Engagement-, Kundenverhalten- und Nutzer:innen-Events, die Sie exportieren möchten, und klicken Sie auf **Launch Current**.

## Unterstützte Currents-Ereignisse {#supported-currents-events}

Braze unterstützt den Export der folgenden Daten an Ihren Custom HTTP Connector:

- [Nachrichtenengagement-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events?tab=custom%20http%20connector)
- [Kundenverhalten-Ereignisse]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events?tab=custom%20http%20connector)

Für die Payload-Struktur jedes Ereignisses wählen Sie den Tab **Custom HTTP Connector** im Event-Glossar aus.

## Vermeidung von Datenverlust {#preventing-data-loss}

### Fehlerüberwachung {#error-monitoring}

Um Datenverlust und Dienstunterbrechungen zu vermeiden, ist es unerlässlich, dass Sie Ihre Endpunkte jederzeit überwachen und alle Fehler oder Ausfallzeiten umgehend beheben.

Bei den meisten Fehlertypen (wie Server-Fehler und Netzwerkverbindungsfehler) wird Braze aktiv versuchen, die Event-Übertragungen erneut zu senden. Wenn das Problem länger als 5 Tage anhält, wird die Integration automatisch deaktiviert. Neue eingehende Events werden verworfen und gehen dauerhaft verloren.

### Änderungsresilienz {#change-resilience}

Gelegentlich nehmen wir nicht-brechende Änderungen an Braze-Currents-Schemas vor. Nicht-brechende Änderungen sind neue nullable Spalten oder Event-Typen.

In der Regel kündigen wir diese Änderungen zwei Wochen im Voraus an, aber manchmal ist das nicht möglich. Es ist unerlässlich, dass Sie Ihre Integration so gestalten, dass sie nicht erkannte Felder oder Event-Typen verarbeiten kann, da es andernfalls wahrscheinlich zu Datenverlust kommt.

{% alert tip %}
Die vollständige Liste der Currents-Event-Schemas finden Sie unter [Nachrichten-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) und [Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).
{% endalert %}

## Bündelung und Serialisierung {#batching-and-serialization}

Das Zieldatenformat ist JSON über HTTPS. Standardmäßig werden Events in Batches von jeweils bis zu 100 Events an Ihren Endpunkt gesendet.

Events werden als JSON-Array aller Events im folgenden Format an den Endpunkt gesendet:

```json
{"events": [event1, event2, event3, etc...]}
```

Es gibt ein JSON-Objekt auf oberster Ebene mit dem Schlüssel `"events"`, der auf ein Array weiterer JSON-Objekte verweist, von denen jedes ein einzelnes Event darstellt. Jedes Event enthält zwei Unterobjekte:

| Name | Beschreibung |
|----|-----------|
| `"user"` | Enthält Nutzer:innen-Eigenschaften wie `user_id`, `external_user_id`, `device_id` und `timezone`. |
| `"properties"` | Enthält Attribute eines Events, wie z. B. die `app/campaign/canvas/platform`, auf die es sich bezieht. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Wenn ein nachgelagerter Endpunkt eine Payload mit null Events oder einen leeren Anfragekörper empfängt, sollte das Ergebnis als No-Op betrachtet werden – das bedeutet, dass durch diesen Aufruf keine nachgelagerten Auswirkungen auftreten sollten. Sie sollten dennoch den `Authorization`-Header überprüfen (wie bei einem normalen API-Aufruf) und eine entsprechende HTTP-Antwort für [ungültige Zugangsdaten](#authentication) zurückgeben, z. B. `401` oder `403`. So weiß Braze, dass die Zugangsdaten des Konnektors gültig sind.

## Authentifizierung {#authentication}

Authentifizierungstoken in Ihrem Payload sind optional. Sie können über einen HTTP-`Authorization`-Header mit dem `Bearer`-Autorisierungsschema übergeben werden, wie in [RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1) festgelegt. Obwohl optional, wird Braze ein übergebenes Authentifizierungstoken immer zuerst validieren&#8212;auch wenn keine Events im Payload enthalten sind.

Gemäß RFC 6750 sollten Token Base64-kodierte Werte mit mindestens einem Zeichen sein. Beachten Sie, dass RFC 6750 zusätzlich zu den normalen Base64-Zeichen die folgenden Zeichen in Token erlaubt: `-`, `.`, `_` und `~`. Sie können selbst entscheiden, ob Sie diese Zeichen in Ihr Token aufnehmen möchten oder nicht&#8212;es muss jedoch im Base64-Format vorliegen.

Wenn der `Authorization`-Header vorhanden ist, wird er außerdem im folgenden Format konstruiert:

```plaintext
"Authorization: Bearer " + <token>
```

Wenn Ihr Authentifizierungstoken beispielsweise `0p3n5354m3==` lautet, sollte Ihr `Authorization`-Header ähnlich wie folgt aussehen:

```plaintext
Authorization: Bearer 0p3n5354m3==
```

{% alert note %}
In Zukunft werden wir möglicherweise `Authorization`-Header verwenden, um ein benutzerdefiniertes Autorisierungsschema mit Schlüssel-Wert-Paaren zu implementieren, das speziell für Braze entwickelt wurde. Dies würde der [RFC 7235](https://tools.ietf.org/html/rfc7235)-Spezifikation entsprechen, die von einigen Unternehmen für ihre Authentifizierungsschemata verwendet wird, wie beispielsweise Amazon Web Services (AWS).
{% endalert %}

## Versionierung {#versioning}

Alle Anfragen unserer HTTP-Konnektor-Integration werden mit einem benutzerdefinierten Header gesendet, der die Version der Currents-Anfrage angibt:

```plaintext
Braze-Currents-Version: 1
```

Die Version wird immer `1` sein, da wir nicht erwarten, diese Nummer häufig – wenn überhaupt – zu erhöhen.

Genau wie bei unseren [Data-Warehouse-Speicherschemata]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents/event_delivery_semantics?redirected=1) ist jedes Event-Feld in einem einzelnen Event garantiert abwärtskompatibel mit früheren Event-Payload-Versionen, gemäß der Definition von Abwärtskompatibilität nach [Apache Avro](https://avro.apache.org/):

1. Für bestimmte Event-Felder ist garantiert, dass sie über die Zeit immer den gleichen Datentyp haben.
2. Alle neuen Felder, die im Laufe der Zeit zum Payload hinzugefügt werden, müssen von allen Beteiligten als optional betrachtet werden.
3. Pflichtfelder werden niemals entfernt.

## Fehlerbehandlung und Retry-Mechanismus {#error-handling-and-retry-mechanism}

Wenn ein Fehler auftritt, stellt Braze die Anfrage in eine Warteschlange und versucht sie basierend auf dem empfangenen HTTP-Rückgabecode erneut. Besteht das Problem länger als 5 Tage, wird die Integration automatisch deaktiviert: Neue eingehende Events werden verworfen und gehen dauerhaft verloren, bereits in der Warteschlange befindliche Events werden nach 7 Tagen Aufbewahrung dauerhaft gelöscht. Wenn Daten länger als 24 Stunden blockiert sind, werden unsere Bereitschaftsingenieure automatisch benachrichtigt. Eine vollständige Aufschlüsselung, wie jeder Statuscode behandelt wird, finden Sie in der Tabelle im folgenden Abschnitt.

Wenn Ihre Currents-Integration Authentifizierungsfehler zurückgibt, sendet Braze Ihnen automatisch eine Benachrichtigungs-E-Mail.

Jeder HTTP-Fehlercode, der nicht im folgenden Abschnitt aufgeführt ist, wird als HTTP-`5XX`-Fehler behandelt.

{% alert warning %}
Besteht das Problem länger als 5 Tage, wird die Integration deaktiviert. Neue eingehende Events werden verworfen und gehen dauerhaft verloren, bereits in der Warteschlange befindliche Events werden nach 7 Tagen Aufbewahrung dauerhaft gelöscht.
{% endalert %}

Die folgenden HTTP-Statuscodes werden von unserem Konnektor-Client erkannt:

<table aria-label="Fehlerbehandlung und Retry-Mechanismus">
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
      <td>Event-Daten werden in einem exponentiellen Backoff-Muster mit Jitter erneut gesendet. Besteht das Problem länger als 5 Tage, wird die Integration deaktiviert, und bereits in der Warteschlange befindliche Events werden 7 Tage aufbewahrt.</td>
    </tr>
    <tr>
      <td><code>400</code></td>
      <td>Clientseitiger Fehler</td>
      <td>Der Konnektor hat mindestens ein fehlerhaftes Event gesendet. Die Event-Daten werden in Batches der Größe 1 aufgeteilt und erneut gesendet. Alle Events in diesen Einzel-Batches, die erneut eine <code>400</code>-Antwort erhalten, werden dauerhaft verworfen.</td>
    </tr>
    <tr>
      <td><code>401</code></td>
      <td>Nicht autorisiert</td>
      <td>Der Konnektor wurde mit ungültigen Zugangsdaten konfiguriert. Fehlgeschlagene Events werden nicht erneut gesendet. Korrigieren Sie Ihre Zugangsdaten und aktivieren Sie die Integration erneut, um fortzufahren. Besteht das Problem länger als 5 Tage, wird die Integration deaktiviert, und bereits in der Warteschlange befindliche Events werden 7 Tage aufbewahrt.</td>
    </tr>
    <tr>
      <td><code>403</code></td>
      <td>Verboten</td>
      <td>Der Konnektor wurde mit ungültigen Zugangsdaten konfiguriert. Fehlgeschlagene Events werden nicht erneut gesendet. Korrigieren Sie Ihre Zugangsdaten und aktivieren Sie die Integration erneut, um fortzufahren. Besteht das Problem länger als 5 Tage, wird die Integration deaktiviert, und bereits in der Warteschlange befindliche Events werden 7 Tage aufbewahrt.</td>
    </tr>
    <tr>
      <td><code>404</code></td>
      <td>Nicht gefunden</td>
      <td>Der Konnektor wurde mit einer fehlerhaften Endpunkt-URL oder ungültigen Zugangsdaten konfiguriert. Überprüfen Sie, ob Ihre Endpunkt-URL korrekt und erreichbar ist. Korrigieren Sie Ihre Konfiguration und aktivieren Sie die Integration erneut, um fortzufahren. Besteht das Problem länger als 5 Tage, wird die Integration deaktiviert, und bereits in der Warteschlange befindliche Events werden 7 Tage aufbewahrt.</td>
    </tr>
    <tr>
      <td><code>413</code></td>
      <td>Payload zu groß</td>
      <td>Event-Daten werden in kleinere Batches aufgeteilt und erneut gesendet.</td>
    </tr>
    <tr>
      <td><code>429</code></td>
      <td>Zu viele Anfragen</td>
      <td>Weist auf Rate-Limiting hin. Event-Daten werden in einem exponentiellen Backoff-Muster mit Jitter erneut gesendet. Besteht das Problem länger als 5 Tage, wird die Integration deaktiviert, und bereits in der Warteschlange befindliche Events werden 7 Tage aufbewahrt.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }