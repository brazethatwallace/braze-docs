---
nav_title: "POST: Sende-IDs erstellen"
article_title: "POST: Sende-IDs erstellen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts „Sende-IDs erstellen“."

---
{% api %}
# Sende-IDs erstellen {#create-send-ids}
{% apimethod post %}
/sends/id/create
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Sende-IDs zu erstellen, die zum programmgesteuerten Senden von Nachrichten und zum Tracking der Nachrichten-Performance verwendet werden können, ohne dass für jeden Sendevorgang eine Campaign erstellt werden muss.

Die Verwendung des Sende-Bezeichners zum Tracking und Versenden von Nachrichten ist nützlich, wenn Sie planen, Inhalte programmatisch zu erstellen und zu versenden.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#74a04e53-659f-4473-abc5-0f6f735550ff {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, müssen Sie einen API-Schlüssel mit der Berechtigung `sends.id.create` generieren.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='sends id create' %}

## Anfragetext {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "send_id": (optional, string) see send identifier
}
```

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Erforderlich | String | Siehe [Campaign-Bezeichner]({{site.baseurl}}/api/identifier_types). |
| `send_id` | Optional | String | Siehe [Sende-Bezeichner]({{site.baseurl}}/api/identifier_types). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

## Beispielanfrage {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/sends/id/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "send_id": "send_identifier"
}'
```

## Antwort {#response}

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

```json
{
  "message": "success",
  "send_id" : (string) the send identifier
}
```

{% endapi %}