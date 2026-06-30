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

Um einen benutzerdefinierten Currents-Konnektor in Braze zu integrieren, müssen Sie eine Endpunkt-URL und ein [optionales Authentifizierungs-Token](#authentication) bereitstellen.

Wenn Sie außerdem mehr als eine App-Gruppe in Braze haben, müssen Sie für jede Gruppe einen eigenen benutzerdefinierten Currents-Konnektor konfigurieren. Sie können jedoch alle App-Gruppen auf denselben Endpunkt oder auf einen Endpunkt mit einem zusätzlichen `GET`-Parameter verweisen, z. B. `your_app_group_key="Brand A"`.

## Integration {#integration}

### 1. Schritt: Endpunkt einrichten {#step-1-set-up-your-endpoint}

Sie benötigen eine Endpunkt-URL, um diese Integration zu konfigurieren. Ihr Endpunkt sollte HTTP-POST-Anfragen empfangen und einen `2XX`-Statuscode zurückgeben können, um den erfolgreichen Empfang von Events zu bestätigen. Wenn Sie Anfragen von Braze authentifizieren möchten, benötigen Sie außerdem ein Bearer-Token.

### 2. Schritt: Braze-Currents konfigurieren {#step-2-configure-braze-currents}

Navigieren Sie in Braze zu **Partnerintegrationen** > **Datenexport**, klicken Sie auf **Neuen Current erstellen** und wählen Sie **Custom Currents Export**.

Geben Sie Ihrem Export einen Namen und eine Kontakt-E-Mail-Adresse und fahren Sie dann mit der Seite **Current Details** fort. Geben Sie auf dieser Seite Ihre Endpunkt-URL und das optionale Bearer-Token ein.

Nachdem Sie Ihre Zugangsdaten konfiguriert haben, aktivieren Sie alle Nachrichten-Engagement-, Kundenverhalten- und Nutzer:innen-Events, die Sie exportieren möchten, und klicken Sie auf **Current starten**.

## Unterstützte Currents-Events {#supported-currents-events}

Braze unterstützt den Export der folgenden Daten an Ihren benutzerdefinierten HTTP-Konnektor:

- [Nachrichten-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events?tab=custom%20http%20connector)
- [Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events?tab=custom%20http%20connector)

Für die Payload-Struktur jedes Events wählen Sie den Tab **Custom HTTP Connector** im Event-Glossar.

## Datenverlust vermeiden {#preventing-data-loss}

### Fehlerüberwachung {#error-monitoring}

Um Datenverlust und Dienstunterbrechungen zu vermeiden, ist es unerlässlich, dass Sie Ihre Endpunkte jederzeit überwachen und Fehler oder Ausfallzeiten umgehend beheben.

Bei den meisten Fehlertypen (wie Serverfehler und Netzwerkverbindungsfehler) wird Braze die Event-Übertragungen aktiv wiederholen. Wenn das Problem länger als 5 Tage bestehen bleibt, wird die Integration automatisch deaktiviert. Neue eingehende Events werden verworfen und gehen dauerhaft verloren.

### Änderungsresilienz {#change-resilience}

Gelegentlich nehmen wir nicht-brechende Änderungen an Braze-Currents-Schemas vor. Nicht-brechende Änderungen sind neue nullable Spalten oder Event-Typen.

In der Regel geben wir eine zweiwöchige Vorankündigung für diese Änderungen, aber manchmal ist dies nicht möglich. Es ist unerlässlich, dass Sie Ihre Integration so gestalten, dass sie unbekannte Felder oder Event-Typen verarbeiten kann, da es andernfalls wahrscheinlich zu Datenverlust kommt.

{% alert tip %}
Die vollständige Liste der Currents-Event-Schemas finden Sie unter [Nachrichten-Engagement-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) und [Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events).
{% endalert %}

## Batching und Serialisierung {#batching-and-serialization}

Das Zieldatenformat ist JSON über HTTPS. Standardmäßig werden Events in Batches von bis zu 100 Events an Ihren Endpunkt gesendet.

Events werden als JSON-Array aller Events im folgenden Format an den Endpunkt gesendet:

```json
{"events": [event1, event2, event3, etc...]}
```

Es gibt ein JSON-Objekt auf oberster Ebene mit dem Schlüssel `"events"`, der auf ein Array weiterer JSON-Objekte verweist, von denen jedes ein einzelnes Event darstellt. Jedes Event enthält zwei Unterobjekte:

| Name | Beschreibung |
|----|-----------|
| `"user"` | Enthält Nutzer:innen-Eigenschaften wie `user_id`, `external_user_id`, `device_id` und `timezone`. |
| `"properties"` | Enthält Attribute eines Events, wie die `app/campaign/canvas/platform`, auf die es sich bezieht. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Wenn ein nachgelagerter Endpunkt eine Payload mit null Events oder einen leeren Anfragekörper empfängt, sollte das Ergebnis als No-Op betrachtet werden, d. h. es sollten keine nachgelagerten Auswirkungen durch diesen Aufruf entstehen. Sie sollten jedoch weiterhin den `Authorization`-Header überprüfen (wie bei einem normalen API-Aufruf) und eine entsprechende HTTP-Antwort für [ungültige Zugangsdaten](#authentication) zurückgeben, z. B. `401` oder `403`. So weiß Braze, dass die Zugangsdaten des Konnektors gültig sind.

## Authentifizierung {#authentication}

Authentifizierungs-Token in Ihrer Payload sind optional. Sie können über einen HTTP-`Authorization`-Header mit dem `Bearer`-Autorisierungsschema übergeben werden, wie in [RFC 6750](https://tools.ietf.org/html/rfc6750#section-2.1) spezifiziert. Obwohl optional, wird Braze ein übergebenes Authentifizierungs-Token immer zuerst validieren&#8212;auch wenn keine Events in der Payload enthalten sind.

Gemäß RFC 6750 sollten Token Base64-kodierte Werte mit mindestens einem Zeichen sein. Beachten Sie, dass RFC 6750 zusätzlich zu den normalen Base64-Zeichen die folgenden Zeichen in Token erlaubt: `-`, `.`, `_` und `~`. Sie können selbst entscheiden, ob Sie diese Zeichen in Ihr Token aufnehmen möchten oder nicht&#8212;es muss jedoch im Base64-Format vorliegen.

Wenn der `Authorization`-Header vorhanden ist, wird er außerdem im folgenden Format erstellt:

```plaintext
"Authorization: Bearer " + <token>
```

Wenn Ihr Authentifizierungs-Token beispielsweise `0p3n5354m3==` lautet, sollte Ihr `Authorization`-Header wie folgt aussehen:

```plaintext
Authorization: Bearer 0p3n5354m3==
```

{% alert note %}
In Zukunft werden wir möglicherweise `Authorization`-Header verwenden, um ein benutzerdefiniertes Schlüssel-Wert-Paar-Autorisierungsschema zu implementieren, das einzigartig für Braze ist. Dies würde der [RFC 7235](https://tools.ietf.org/html/rfc7235)-Spezifikation entsprechen, die von einigen Unternehmen für ihre Authentifizierungsschemata verwendet wird, wie z. B. Amazon Web Services (AWS).
{% endalert %}

## Versionierung {#versioning}

Alle Anfragen unserer HTTP-Konnektor-Integration werden mit einem benutzerdefinierten Header gesendet, der die Version der Currents-Anfrage angibt:

```plaintext
Braze-Currents-Version: 1
```

Die Version wird immer `1` sein, da wir nicht erwarten, diese Zahl häufig – wenn überhaupt – zu erhöhen.

Genau wie bei unseren [Data-Warehouse-Speicherschemas]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics?redirected=1) ist jedes Event-Feld in einem einzelnen Event garantiert abwärtskompatibel mit früheren Event-Payload-Versionen, gemäß der [Apache Avro](https://avro.apache.org/)-Definition von Abwärtskompatibilität:

1. Bestimmte Event-Felder haben garantiert immer denselben Datentyp.
2. Alle neuen Felder, die im Laufe der Zeit zur Payload hinzugefügt werden, müssen von allen Parteien als optional betrachtet werden.
3. Erforderliche Felder werden niemals entfernt.

## Fehlerbehandlung und Retry-Mechanismus {#error-handling-and-retry-mechanism}

Wenn ein Fehler auftritt, stellt Braze die Anfrage in eine Warteschlange und wiederholt sie basierend auf dem empfangenen HTTP-Rückgabecode. Wenn das Problem länger als 5 Tage bestehen bleibt, wird die Integration automatisch deaktiviert: Neue eingehende Events werden verworfen und gehen dauerhaft verloren, und bereits in der Warteschlange befindliche Events werden nach einer Aufbewahrungsfrist von 7 Tagen dauerhaft gelöscht. Wenn Daten länger als 24 Stunden feststecken, werden unsere Bereitschaftsingenieur:innen automatisch benachrichtigt. Eine vollständige Aufschlüsselung, wie jeder Statuscode behandelt wird, finden Sie in der folgenden Tabelle.

Wenn Ihre Currents-Integration Authentifizierungsfehler zurückgibt, sendet Braze Ihnen automatisch eine Benachrichtigungs-E-Mail.

Jeder HTTP-Fehlercode, der unten nicht aufgeführt ist, wird als HTTP-`5XX`-Fehler behandelt.

{% alert warning %}
Wenn das Problem länger als 5 Tage bestehen bleibt, wird die Integration deaktiviert. Neue eingehende Events werden verworfen und gehen dauerhaft verloren, und bereits in der Warteschlange befindliche Events werden nach einer Aufbewahrungsfrist von 7 Tagen dauerhaft gelöscht.
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
      <td>Event-Daten werden in einem exponentiellen Backoff-Muster mit Jitter erneut gesendet. Wenn das Problem länger als 5 Tage bestehen bleibt, wird die Integration deaktiviert, und bereits in der Warteschlange befindliche Events werden 7 Tage lang aufbewahrt.</td>
    </tr>
    <tr>
      <td><code>400</code></td>
      <td>Clientseitiger Fehler</td>
      <td>Der Konnektor hat mindestens ein fehlerhaftes Event gesendet. Die Event-Daten werden in Batches der Größe 1 aufgeteilt und erneut gesendet. Events in diesen Einzel-Batches, die eine weitere <code>400</code>-Antwort erhalten, werden dauerhaft verworfen.</td>
    </tr>
    <tr>
      <td><code>401</code></td>
      <td>Unauthorized</td>
      <td>Der Konnektor wurde mit ungültigen Zugangsdaten konfiguriert. Fehlgeschlagene Events werden nicht erneut gesendet. Korrigieren Sie Ihre Zugangsdaten und aktivieren Sie die Integration erneut, um fortzufahren. Wenn das Problem länger als 5 Tage bestehen bleibt, wird die Integration deaktiviert, und bereits in der Warteschlange befindliche Events werden 7 Tage lang aufbewahrt.</td>
    </tr>
    <tr>
      <td><code>403</code></td>
      <td>Forbidden</td>
      <td>Der Konnektor wurde mit ungültigen Zugangsdaten konfiguriert. Fehlgeschlagene Events werden nicht erneut gesendet. Korrigieren Sie Ihre Zugangsdaten und aktivieren Sie die Integration erneut, um fortzufahren. Wenn das Problem länger als 5 Tage bestehen bleibt, wird die Integration deaktiviert, und bereits in der Warteschlange befindliche Events werden 7 Tage lang aufbewahrt.</td>
    </tr>
    <tr>
      <td><code>404</code></td>
      <td>Not Found</td>
      <td>Der Konnektor wurde mit einer falschen Endpunkt-URL oder ungültigen Zugangsdaten konfiguriert. Überprüfen Sie, ob Ihre Endpunkt-URL korrekt und erreichbar ist. Korrigieren Sie Ihre Konfiguration und aktivieren Sie die Integration erneut, um fortzufahren. Wenn das Problem länger als 5 Tage bestehen bleibt, wird die Integration deaktiviert, und bereits in der Warteschlange befindliche Events werden 7 Tage lang aufbewahrt.</td>
    </tr>
    <tr>
      <td><code>413</code></td>
      <td>Payload Too Large</td>
      <td>Event-Daten werden in kleinere Batches aufgeteilt und erneut gesendet.</td>
    </tr>
    <tr>
      <td><code>429</code></td>
      <td>Too Many Requests</td>
      <td>Weist auf Rate-Limiting hin. Event-Daten werden in einem exponentiellen Backoff-Muster mit Jitter erneut gesendet. Wenn das Problem länger als 5 Tage bestehen bleibt, wird die Integration deaktiviert, und bereits in der Warteschlange befindliche Events werden 7 Tage lang aufbewahrt.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }