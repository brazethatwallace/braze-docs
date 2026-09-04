---
nav_title: "POST: Externe ID entfernen"
article_title: "POST: Externe ID entfernen"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts „Externe IDs entfernen“."
---
{% api %}
# Externe ID entfernen {#remove-external-id}
{% apimethod post %}
/users/external_ids/remove
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um die alten, veralteten externen IDs Ihrer Nutzer:innen zu entfernen.

Sie können bis zu 50 externe IDs pro Anfrage senden.

{% alert warning %}
Dieser Endpunkt löscht die veraltete ID vollständig und kann nicht rückgängig gemacht werden. Wenn Sie diesen Endpunkt verwenden, um veraltete `external_ids` zu entfernen, die noch mit Nutzer:innen in Ihrem System verbunden sind, können Sie die Daten dieser Nutzer:innen möglicherweise dauerhaft nicht mehr finden.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e16b5340-5f44-42b6-9033-2398faf8908e {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics) mit der Berechtigung `users.external_ids.remove`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## Anfragetext {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_ids" : (required, array of external identifiers to remove)
}
```

### Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `external_ids` | Erforderlich | String-Array | Externe Bezeichner für die zu entfernenden Nutzer:innen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

## Beispiel für eine Anfrage {#request-example}

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_ids" :[
    "existing_deprecated_external_id_string",
    ...
  ]
}'
```

{% alert important %}
Nur veraltete IDs können entfernt werden. Der Versuch, eine primäre externe ID zu entfernen, führt zu einem Fehler.
{% endalert %}

## Antwort {#response}

Die Antwort bestätigt alle erfolgreichen Entfernungen sowie erfolglose Entfernungen mit den dazugehörigen Fehlern. Fehlermeldungen im Feld `removal_errors` referenzieren den Index im Array der ursprünglichen Anfrage.

```
{
  "message" : (string) status message,
  "removed_ids" : (array of strings) successful remove operations,
  "removal_errors": (array of arrays) <minor error message>
}
```

Das Feld `message` gibt für jede gültige Anfrage `success` zurück. Spezifischere Fehler werden im Array `removal_errors` erfasst. Das Feld `message` gibt einen Fehler zurück in folgenden Fällen:
- Ungültiger API-Schlüssel
- Leeres `external_ids`-Array
- `external_ids`-Array mit mehr als 50 Elementen
- Rate-Limit erreicht (mehr als 1.000 Anfragen/Minute)

{% endapi %}