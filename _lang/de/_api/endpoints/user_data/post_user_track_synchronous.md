---
nav_title: "POST: Nutzer:innen erstellen und aktualisieren (synchron)"
article_title: "POST: Nutzer:innen erstellen und aktualisieren (synchron)"
alias: /post_user_track_synchronous/
layout: api_page
page_order: 4.5
page_type: reference
description: "Dieser Artikel beschreibt Details zum synchronen Endpunkt „Nutzer:innen tracken“ in Braze."

---
{% api %}
# Nutzer:innen erstellen und aktualisieren (synchron) {#create-and-update-users-synchronous}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/users/track/sync
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um angepasste Events und Käufe aufzuzeichnen und Nutzerprofilattribute synchron zu aktualisieren. Dieser Endpunkt funktioniert ähnlich wie der [Endpunkt `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track), der Nutzerprofile asynchron aktualisiert.

{% alert important %}
Dieser Endpunkt befindet sich derzeit in einer **eingeschränkten Beta-Phase**. Obwohl wir derzeit keine neuen Kund:innen zur Beta hinzufügen, informieren Sie bitte Ihren Braze Account Manager, wenn Sie der Meinung sind, dass dieses Feature für Ihre Braze-Integration nützlich sein könnte.
{% endalert %}

## Synchrone und asynchrone API-Aufrufe {#synchronous-and-asynchronous-api-calls}

Bei einem asynchronen Aufruf gibt die API den Statuscode `201` zurück, der anzeigt, dass Ihre Anfrage erfolgreich empfangen, verstanden und akzeptiert wurde. Dies bedeutet jedoch nicht, dass Ihre Anfrage vollständig abgeschlossen wurde.

Bei einem synchronen Aufruf gibt die API den Statuscode `201` zurück, der anzeigt, dass Ihre Anfrage erfolgreich empfangen, verstanden, akzeptiert und abgeschlossen wurde. Die Antwort auf den Aufruf zeigt ausgewählte Felder des Nutzerprofils als Ergebnis der Operation an.

Dieser Endpunkt hat ein niedrigeres Rate-Limit als der Endpunkt `/users/track` (siehe [Rate-Limit](#rate-limit) unten). Jede `/users/track/sync`-Anfrage kann nur ein Event-Objekt, ein Attribut-Objekt **oder** ein Kauf-Objekt enthalten. Dieser Endpunkt sollte für Nutzerprofil-Updates reserviert sein, bei denen ein synchroner Aufruf erforderlich ist. Für eine stabile Implementierung empfehlen wir, `/users/track/sync` und `/users/track` gemeinsam zu verwenden.

Wenn Sie beispielsweise innerhalb eines kurzen Zeitraums aufeinanderfolgende Anfragen für dieselbe Nutzer:in senden, sind Race-Conditions mit dem asynchronen Endpunkt `/users/track` möglich. Mit dem Endpunkt `/users/track/sync` können Sie diese Anfragen jedoch nacheinander senden, jeweils nach Erhalt einer `2XX`-Antwort.

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key) mit der Berechtigung `users.track.sync`.

Kund:innen, die die API für Server-zu-Server-Aufrufe verwenden, müssen möglicherweise `rest.iad-01.braze.com` auf die Zulassungsliste setzen, wenn sie sich hinter einer Firewall befinden.

## Rate-Limit {#rate-limit}

{% multi_lang_include api/user_track_custom_attributes_data_points.md endpoint="/users/track/sync" %}

Für diesen Endpunkt gilt für alle Kund:innen ein Basis-Rate-Limit von 500 Anfragen pro Minute. Jede `/users/track/sync`-Anfrage kann bis zu ein Event-Objekt, ein Attribut-Objekt oder ein Kauf-Objekt enthalten. Jedes Objekt (Event-, Attribut- und Kauf-Arrays) kann jeweils eine:n Nutzer:in aktualisieren.

## Anfragetext {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "attributes": (optional, one attributes object),
  "events": (optional, one event object),
  "purchases": (optional, one purchase object),
}
```

### Anfrageparameter {#request-parameters}

{% alert important %}
Für jede in der folgenden Tabelle aufgeführte Anfragekomponente müssen Sie eines der folgenden Felder angeben: `external_id`, `user_alias`, `braze_id`, `email` oder `phone`.
{% endalert %}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `attributes` | Optional | Ein Attribut-Objekt | Siehe [Nutzerattribut-Objekt]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrating-push-tokens) |
| `events` | Optional | Ein Event-Objekt | Siehe [Event-Objekt]({{site.baseurl}}/api/objects_filters/event_object) |
| `purchases` | Optional | Ein Kauf-Objekt | Siehe [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

## Antworten {#responses}

Wenn Sie die [Anfrageparameter](#request-parameters) dieses Endpunkts verwenden, sollten Sie eine der folgenden Antworten erhalten: eine Erfolgsmeldung oder eine Nachricht mit schwerwiegenden Fehlern.

### Erfolgsmeldung {#successful-message}

Erfolgsmeldungen geben die folgende Antwort zurück, die Informationen zu den von Braze aktualisierten Nutzerprofildaten enthält.

```json
{
    "users": (optional, object), the identifier of the user in the request. May be empty if no users are found and _update_existing_only key is set to true,
        "custom_attributes": (optional, object), the custom attributes as a result of the request. Braze lists only custom attributes from the request,
        "custom_events": (optional, object), the custom events as a result of the request. Braze lists only custom events from the request,
        "purchase_events": (optional, object), the purchase events as a result of the request. Braze lists only purchase events from the request,
    },
    "message": "success"
```

### Nachricht mit schwerwiegenden Fehlern {#message-with-fatal-errors}

Wenn Ihre Nachricht einen schwerwiegenden Fehler enthält, erhalten Sie die folgende Antwort:

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

## Beispielanfragen und -antworten {#example-requests-and-responses}

### Angepasstes Attribut anhand der externen ID aktualisieren {#update-a-custom-attribute-by-external-id}

#### Anfrage {#request}

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "attributes": [
        {
            "external_id": "xyz123",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}'
```

#### Antwort {#response}

```
{
    "users": [
        {
            "external_id": "xyz123",
            "custom_attributes": {
                "string_attribute": "fruit",
                "boolean_attribute_1": true,
                "integer_attribute": 25,
                "array_attribute": [
                    "banana",
                    "apple",
                ]
            }
        }
    ],
    "message": "success"
}
```

### Angepasstes Event per E-Mail aktualisieren {#update-a-custom-event-by-email}

#### Anfrage

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
    "events": [
        {
            "email": "test@example.com",
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

#### Antwort

```
{
    "users": [
        {
            "email": "test@example.com",
            "custom_events": [
                {
                "name": "rented_movie",
                "first": "2022-01-001T00:00:00.000Z",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 10
                }
            ]
        }
    ],
    "message": "success"
}
```

### Kauf-Event anhand des Nutzer-Alias aktualisieren {#update-a-purchase-event-by-user-alias}

#### Anfrage

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track/sync' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "purchases" : [
    {
      "user_alias" : {
          "alias_name" : "device123",
          "alias_label" : "my_device_identifier"
      }
      "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
      "product_id" : "Completed Order",
      "currency" : "USD",
      "price" : 219.98,
      "time" : "2022-12-06T19:20:45+01:00",
      "properties" : {
          "products" : [
            {
              "name": "Monitor",
              "category": "Gaming",
              "product_amount": 19.99
            },
            {
              "name": "Gaming Keyboard",
              "category": "Gaming ",
              "product_amount": 199.99
            }
          ]
      }
   }
  ]
}'
```

#### Antwort

```
{
    "users": [
        {
          "user_alias" : {
            "alias_name" : "device123",
            "alias_label" : "my_device_identifier"
          },
          "purchase_events": [
                {
                "product_id": "Completed Order",
                "first": "2013-07-16T19:20:30+01:00",
                "last": "2022-12-06T18:20:45.000Z",
                "count": 3
                }
            ]
        }
    ],
    "message": "success"
}
```

## Häufig gestellte Fragen {#frequently-asked-questions}

### Sollte ich den asynchronen oder den synchronen Endpunkt verwenden? {#should-i-use-the-asynchronous-or-synchronous-endpoint}

Für die meisten Profil-Updates eignet sich der Endpunkt `/users/track` am besten, da er höhere Rate-Limits und die Flexibilität bietet, Anfragen gebündelt zu senden. Der Endpunkt `/users/track/sync` ist jedoch nützlich, wenn Sie Race-Conditions aufgrund von schnellen, aufeinanderfolgenden Anfragen für dieselbe Nutzer:in erleben.

### Unterscheidet sich die Antwortzeit vom Endpunkt `/users/track`? {#does-the-response-time-differ-from-the-userstrack-endpoint}

Bei einem synchronen Aufruf wartet die API, bis Braze die Anfrage abgeschlossen hat, bevor eine Antwort zurückgegeben wird. Infolgedessen dauern synchrone Anfragen im Durchschnitt länger als asynchrone Anfragen an `/users/track`. Für die meisten Anfragen können Sie eine Antwort innerhalb von Sekunden erwarten.

### Kann ich mehrere Anfragen gleichzeitig senden? {#can-i-send-multiple-requests-at-the-same-time}

Ja, solange die Anfragen für verschiedene Nutzer:innen bestimmt sind oder jede Anfrage unterschiedliche Attribute, Events oder Käufe für eine:n Nutzer:in aktualisiert.

Wenn Sie mehrere Anfragen für eine:n Nutzer:in für dasselbe Attribut, Event oder denselben Kauf senden, empfiehlt Braze, zwischen den einzelnen Anfragen auf eine erfolgreiche Antwort zu warten, um Race-Conditions zu vermeiden.

### Warum stimmt der Antwortwert nicht mit dem in meiner ursprünglichen Anfrage überein? {#why-doesnt-the-response-value-match-the-one-in-my-original-request}

Obwohl Ihre Anfrage abgeschlossen wurde, ist es möglich, dass der Wert Ihres angepassten Attributs nicht aktualisiert wurde. Dies kann passieren, wenn Ihr Update des angepassten Attributs die maximale Zeichenanzahl überschreitet, Array-Grenzen überschreitet oder wenn die Nutzer:in nicht in Braze existiert und Sie `_update_existing_only = true` gesetzt haben.

In diesen Fällen sollten Sie die Antwort als Hinweis darauf betrachten, dass Ihre Anfrage zwar abgeschlossen, das gewünschte Update jedoch nicht durchgeführt wurde. Prüfen Sie die oben genannten Gründe, um die Ursache zu ermitteln.

{% endapi %}