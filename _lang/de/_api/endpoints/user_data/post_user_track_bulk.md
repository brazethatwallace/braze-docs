---
nav_title: "POST: Nutzer:innen erstellen und Update or aktualisieren or aktualisieren (Bulk)"
article_title: "POST: Nutzer:innen erstellen und Update or aktualisieren or aktualisieren (Bulk)"
search_tag: Endpoint
page_order: 4.25
layout: api_page
page_type: reference
alias:
  - /unlisted_docs/track_users_bulk_partners/
  - /api/endpoints/user_data/post_user_track_bulk_partners/
description: "Dieser Artikel beschreibt Details zum Bulk-Endpunkt „Nutzer:innen tracken“."
---
{% api %}
# Nutzer:innen erstellen und Update or aktualisieren or aktualisieren (Bulk) {#create-and-update-users-bulk}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/users/track/bulk
{% endapimethod %}

Verwenden Sie diesen Endpunkt, um angepasste Events und Käufe aufzuzeichnen und Nutzerprofilattribute in großen Mengen (Bulk) zu Update or aktualisieren or aktualisieren.

{% alert important %}
Dieser Endpunkt befindet sich derzeit in einer **eingeschränkten Beta-Phase**. Obwohl wir derzeit keine neuen Kund:innen zur Beta hinzufügen, lassen Sie Ihren Braze Account Manager:in wissen, wenn Sie glauben, dass dieses Feature für Ihre Braze-Integration nützlich sein könnte.
{% endalert %}

## Wann Sie diesen Endpunkt verwenden sollten {#when-to-use-this-endpoint}

Wie der [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track) können Sie diesen Endpunkt verwenden, um Nutzerprofile zu Update or aktualisieren or aktualisieren. Dieser Endpunkt ist besser für Bulk-Updates geeignet:

- **Größere Anfragen:** Senden Sie bis zu 1.000 Nutzer:innen pro Anfrage, sodass Sie bei großen Backfills und Synchronisierungen weniger Anfragen stellen müssen.
- **Priorisierung:** Bei Spitzenverkehr werden Anfragen an `/users/track` gegenüber Anfragen an `/users/track/bulk` priorisiert.

Verwenden Sie diesen Endpunkt, wenn Sie während des Onboardings viele Nutzerprofile nachträglich befüllen oder große Mengen an Profilen im Rahmen einer täglichen Synchronisierung übertragen.

{% alert note %}
Die Limits für Anfrageobjekte des `/users/track`-Endpunkts variieren je nach Preismodell und Konfiguration. Verwenden Sie `/users/track/bulk` für die Bulk-Datenaufnahme.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics) mit der Berechtigung `users.track.bulk`.

Wenn Sie Server-zu-Server-Aufrufe hinter einer Firewall durchführen, müssen Sie möglicherweise Ihren Braze-Representational State Transfer-Endpunkt auf die Zulassungsliste setzen (zum Beispiel `rest.iad-01.braze.com`). Weitere Informationen finden Sie unter [API-Endpunkte]({{site.baseurl}}/api/basics#api-definitions).

## Rate-Limit

{% multi_lang_include api/user_track_custom_attributes_data_points.md endpoint="/users/track/bulk" %}

Für die meisten Kund:innen hat dieser Endpunkt ein Basis-Geschwindigkeitslimit von 50 Anfragen pro Sekunde.

Kund:innen mit neueren Verträgen haben stattdessen möglicherweise Burst- (pro Sekunde) und Steady-Limits (pro Stunde), die auf den vertraglich vereinbarten monatlich aktiven Nutzer:innen basieren.

Jede `/users/track/bulk`-Anfrage hat ein Payload-Limit von 2 MB und kann insgesamt bis zu 1.000 Objekte über Attribute, Events und Käufe hinweg enthalten, abhängig von der Bulk-Rate-Limit-Richtlinie Ihres Kontos.

Jedes Objekt kann eine:n Nutzer:in Update or aktualisieren or aktualisieren, sodass eine einzelne Anfrage bis zum Anfrageobjekt-Limit Ihres Kontos verschiedene Nutzer:innen Update or aktualisieren or aktualisieren kann. Zusätzlich kann jede Anfrage maximal 100 Objekte pro Kundenprofil or Nutzerprofil über Attribute, Events und Käufe hinweg enthalten.

## Anfrage-Body {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, array of attributes object),
  "events": (optional, array of event object),
  "purchases": (optional, array of purchase object)
}
```

### Anfrageparameter {#request-parameters}

{% alert important %}
Für jedes Anfrageobjekt müssen Sie eines der folgenden Felder angeben: `external_id`, `user_alias`, `braze_id`, `email` oder `phone`.
{% endalert %}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --- | --- | --- | --- |
| `attributes` | Optional | Array von Attribut-Objekten | Siehe [Nutzerattribut-Objekt]({{site.baseurl}}/api/objects_filters/user_attributes_object) |
| `events` | Optional | Array von Event-Objekten | Siehe [Event-Objekt]({{site.baseurl}}/api/objects_filters/event_object) |
| `purchases` | Optional | Array von Kauf-Objekten | Siehe [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Anfrageparameter" }

## Beispielanfragen {#example-requests}

### Nutzerprofile per Bulk in einer Anfrage Update or aktualisieren or aktualisieren {#bulk-update-user-profiles-in-one-request}

Update or aktualisieren or aktualisieren Sie bis zum Anfrageobjekt-Limit Ihres Kontos Nutzerprofile in einer einzigen Anfrage.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "user1",
      "string_attribute": "fruit",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": [
        "banana",
        "apple"
      ]
    },
    {
      "external_id": "user2",
      "string_attribute": "vegetables",
      "boolean_attribute_1": false,
      "integer_attribute": 25,
      "array_attribute": [
        "broccoli",
        "asparagus"
      ]
    }
  ]
}'
```

### Attribute und Events in einer Anfrage senden {#send-attributes-and-events-in-one-request}

Fügen Sie Attribute und Events in derselben Anfrage zusammen, bis zum kombinierten Objektlimit Ihres Kontos.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/bulk' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "user1",
      "string_attribute": "fruit",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": [
        "banana",
        "apple"
      ]
    }
  ],
  "events": [
    {
      "external_id": "user2",
      "app_id": "your_app_identifier",
      "name": "rented_movie",
      "time": "2022-12-06T19:20:45+01:00",
      "properties": {
        "release": {
          "studio": "FilmStudio",
          "year": "2022"
        },
        "cast": [
          {
            "name": "Actor1"
          },
          {
            "name": "Actor2"
          }
        ]
      }
    }
  ]
}'
```

## Antworten {#responses}

### Erfolgreiche Nachricht {#successful-message}

Erfolgreiche Nachrichten geben die folgende Antwort zurück:

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this returns an integer of the number of external IDs with attributes that Braze queued for processing,
  "events_processed": (optional, integer), if events are included in the request, this returns an integer of the number of events that Braze queued for processing,
  "purchases_processed": (optional, integer), if purchases are included in the request, this returns an integer of the number of purchases that Braze queued for processing
}
```

### Erfolgreiche Nachricht mit nicht schwerwiegenden Fehlern {#successful-message-with-non-fatal-errors}

Wenn Ihre Anfrage erfolgreich ist, aber nicht schwerwiegende Fehler enthält (zum Beispiel ein ungültiges Event-Objekt in einem großen Batch), erhalten Sie die folgende Antwort:

```json
{
  "message": "success",
  "errors": [
    {
      <minor error message>
    }
  ]
}
```

### Nachricht mit schwerwiegenden Fehlern {#message-with-fatal-errors}

Wenn Ihre Anfrage einen schwerwiegenden Fehler enthält, erhalten Sie die folgende Antwort:

```json
{
  "message": <fatal error message>,
  "errors": [
    {
      <fatal error message>
    }
  ]
}
```

### Antwortcodes bei schwerwiegenden Fehlern {#fatal-error-response-codes}

Informationen zu Statuscodes und zugehörigen Fehlermeldungen, die Braze zurückgibt, wenn Ihre Anfrage einen schwerwiegenden Fehler enthält, finden Sie unter [Schwerwiegende Fehler und Antworten]({{site.baseurl}}/api/errors#fatal-errors).

Wenn Sie den Fehler „provided external_id is blacklisted and disallowed“ erhalten, enthält Ihre Anfrage möglicherweise eine:n „Dummy-Nutzer:in“. Weitere Informationen finden Sie unter [Spam-Blockierung]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival#spam-blocking).

## Häufig gestellte Fragen {#frequently-asked-questions}

### Sollte ich diesen Endpunkt oder `/users/track` verwenden? {#should-i-use-this-endpoint-or-userstrack}

Verwenden Sie beide Endpunkte je nach Anwendungsfall:

- Für große Backfills und Synchronisierungen verwenden Sie `/users/track/bulk`.
- Für Realtime-Anwendungsfälle verwenden Sie `/users/track`.

### Welche Bezeichner kann ich in `/users/track/bulk` verwenden? {#what-identifiers-can-i-use-in-userstrackbulk}

Geben Sie für jedes Anfrageobjekt eines der folgenden Felder an: `external_id`, `braze_id`, `user_alias`, `email` oder `phone`.

### Kann ich Attribute, Events und Käufe in einer Anfrage zusammenfassen? {#can-i-include-attributes-events-and-purchases-in-one-request}

Ja. Fügen Sie eine beliebige Kombination aus Attributen, Events und Käufen hinzu, bis zum kombinierten Anfrageobjekt-Limit Ihres Kontos.

{% endapi %}