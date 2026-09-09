---
nav_title: "POST: Nutzer:innen tracken (Bulk)"
layout: api_page
page_type: reference
hidden: true
permalink: /track_users_bulk/
description: "Dieser Artikel beschreibt Details zum Endpunkt „Nutzer:innen tracken (Bulk)“."
---

{% api %}
# Nutzer:innen tracken (Bulk) {#track-users-bulk}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/users/track/bulk
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um angepasste Events und Käufe aufzuzeichnen und Nutzerprofilattribute in großen Mengen zu aktualisieren.

{% alert important %}
Dieser Endpunkt befindet sich derzeit in der Beta-Phase. Kontaktieren Sie Ihren Braze Account Manager:in, wenn Sie an der Beta teilnehmen möchten.
{% endalert %}

## Wann Sie diesen Endpunkt verwenden sollten {#when-to-use-this-endpoint}

Ähnlich wie beim [POST: Endpunkt „Nutzer:innen tracken“]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#prerequisites) können Sie diesen Endpunkt verwenden, um Nutzerprofile zu aktualisieren. Dieser Endpunkt ist jedoch besser für Bulk-Updates geeignet:

- **Größere Anfragen:** Dieser Endpunkt erlaubt 10.000 Nutzer:innen pro Anfrage, sodass Sie weniger Anfragen stellen müssen, um Ihre Bulk-Update-Anforderungen zu erfüllen.
- **Priorisierung:** Bei hohem Datenverkehr werden Anfragen von `/users/track` gegenüber Anfragen von `/users/track/bulk` priorisiert. Die Verwendung beider Endpunkte gibt Ihnen mehr Kontrolle über die Datenaufnahme.

Erwägen Sie die Verwendung dieses Endpunkts, wenn Sie während des Onboardings viele Nutzerprofile nachträglich befüllen oder große Mengen von Nutzerprofilen im Rahmen einer täglichen Synchronisierung abgleichen.

{% alert note %}
Seit dem 26. Mai 2025 kann dieser Endpunkt verwendet werden, um Conversion-Metriken zu tracken sowie Ausnahme-Events oder aktionsbasierte Campaigns und Canvases auszulösen. Dieses Verhalten entspricht jeder anderen Braze-Datenaufnahmemethode.
{% endalert %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen API-Schlüssel mit der Berechtigung `users.track.bulk`.

Wenn Sie die API für Server-zu-Server-Aufrufe verwenden, müssen Sie möglicherweise den Endpunkt (z. B. `rest.iad-01.braze.com`) auf die Zulassungsliste setzen, falls Sie sich hinter einer Firewall befinden. Weitere Informationen finden Sie unter [Endpunkte pro Instanz]({{site.baseurl}}/api/basics/#endpoints).

## Rate-Limit

Wir wenden ein Basis-Geschwindigkeitslimit von 5 Anfragen pro Sekunde auf diesen Endpunkt für alle Kund:innen an.

Jede `/users/sync/bulk`-Anfrage hat ein Payload-Limit von 4&nbsp;MB und kann bis zu 10.000 Event-, Attribut- oder Kauf-Objekte enthalten.

Jedes Objekt (Event-, Attribut- und Kauf-Arrays) kann jeweils eine:n Nutzer:in aktualisieren, d. h. bis zu 10.000 verschiedene Nutzer:innen können in einer einzigen Anfrage aktualisiert werden. Ein einzelnes Kundenprofil kann mit bis zu 100 Objekten in einer einzigen Anfrage aktualisiert werden.

{% alert note %}
Wenn Sie eine Erhöhung Ihres Rate-Limits benötigen, wenden Sie sich an Ihren CSM.
{% endalert %}


## Anfragebody {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, array of attributes object),
  "events": (optional, array of event object),
  "purchases": (optional, array of purchase object),
}
```

### Anfrageparameter {#request-parameters}

{% alert important %}
Für jede in der folgenden Tabelle aufgeführte Anfragekomponente ist eines der folgenden Felder erforderlich: `external_id`, `user_alias`, `braze_id`, `email` oder `phone`.
{% endalert %}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `attributes` | Optional | Array von Attribut-Objekten | Siehe [Nutzerattribut-Objekt]({{site.baseurl}}/api/objects_filters/user_attributes_object/) |
| `events` | Optional | Array von Event-Objekten | Siehe [Event-Objekt]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | Optional | Array von Kauf-Objekten | Siehe [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispielanfragen {#example-requests}

### Bulk-Update von 10.000 Nutzerprofilen in einer Anfrage {#bulk-update-10000-user-profiles-in-one-request}

Sie können bis zu 10.000 Nutzerprofile aktualisieren. Hier ist ein gekürztes Beispiel, bei dem die Anfrage aus 10.000 Attribut-Objekten besteht:

```json
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
                "asparagus",
            ]
        },

...

        {
            "external_id": "user10000",
            "string_attribute": "nuts",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "hazelnut",
                "pistachio"
            ]
        }
    ]
}'
```

Hier ist ein Beispiel, bei dem die Anfrage sowohl aus Attribut- als auch aus Event-Objekten besteht:

```json
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
        },
...
        {
            "external_id": "user10000",
            "app_id": "your_app_identifier",
            "name": "rented_movie",
            "time": "2023-09-16T08:00:00+10:00",
            "properties": {
                "release": {
                    "studio": "FilmStudio",
                    "year": "1988"
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

### Erfolgreiche Nachrichten {#successful-messages}

Erfolgreiche Nachrichten erhalten die folgende Antwort:

```json
{
  "message": "success",
  "attributes_processed": (optional, integer), if attributes are included in the request, this will return an integer of the number of external_ids with attributes that were queued to be processed,
  "events_processed": (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,
  "purchases_processed": (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,
}
```

#### Erfolgreiche Nachricht mit nicht schwerwiegenden Fehlern {#successful-message-with-non-fatal-errors}

Wenn Ihre Nachricht erfolgreich ist, aber nicht schwerwiegende Fehler aufweist, z. B. ein ungültiges Event-Objekt in einer langen Liste von Events, erhalten Sie die folgende Antwort:

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

Wenn Ihre Nachricht einen schwerwiegenden Fehler aufweist, erhalten Sie die folgende Antwort:

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

#### Antwortcodes bei schwerwiegenden Fehlern {#fatal-error-response-codes}

Informationen zu Statuscodes und zugehörigen Fehlermeldungen, die zurückgegeben werden, wenn Ihre Anfrage einen schwerwiegenden Fehler aufweist, finden Sie unter [Schwerwiegende Fehler und Antworten]({{site.baseurl}}/api/errors/#fatal-errors).

Wenn Sie den Fehler `provided external_id is blacklisted and disallowed` erhalten, enthält Ihre Anfrage möglicherweise eine:n „Dummy-Nutzer:in“. Weitere Informationen finden Sie unter [Spam-Blockierung]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_archival/#spam-blocking).

## Häufig gestellte Fragen {#frequently-asked-questions}

### Sollte ich diesen Endpunkt oder den regulären `/users/track` verwenden? {#should-i-use-this-endpoint-or-regular-userstrack}

Wir empfehlen, beide zu verwenden.

- Für große Kundenprofil-Backfills und Synchronisierungen verwenden Sie den Endpunkt `/users/track/bulk`.
- Für Realtime-Anwendungsfälle verwenden Sie den Endpunkt `/users/track`.

### Welche Bezeichner kann ich in /users/track/bulk verwenden? {#what-identifiers-can-i-use-in-userstrackbulk}

Eines der folgenden Felder ist erforderlich: `external_id`, `braze_id`, `user_alias`, `email` oder `phone`. Weitere Beispiele finden Sie in unserer Dokumentation zum [Nutzerattribut-Objekt]({{site.baseurl}}/api/objects_filters/user_attributes_object/), [Event-Objekt]({{site.baseurl}}/api/objects_filters/event_object/) oder [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object/).

### Kann ich Attribute, Events und Käufe in einer Anfrage kombinieren? {#can-i-include-attributes-events-and-purchases-in-one-request}

Ja. Sie können Ihre Anfrage mit einer beliebigen Anzahl von Attribut-, Event- und Kauf-Objekten zusammenstellen – bis zu 10.000 Objekte pro Anfrage.


{% endapi %}