---
nav_title: "POST: Geplante, API-getriggerte Campaigns löschen"
article_title: "POST: Geplante, API-getriggerte Campaigns löschen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Braze-Endpunkt zum Löschen geplanter, API-getriggerter Campaigns."

---
{% api %}
# Geplante, API-getriggerte Campaigns löschen {#delete-scheduled-api-triggered-campaigns}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/campaigns/Trigger or triggern/schedule/delete
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine zuvor per API-Trigger or triggern geplante Campaign-Nachricht zu stornieren, bevor sie gesendet wurde.

Geplante Nachrichten oder Trigger or triggern, die kurz vor oder während des vorgesehenen Sendezeitpunkts gelöscht werden, werden nach bestem Bemühen aktualisiert. Das bedeutet, dass Braze Löschungen in letzter Sekunde möglicherweise auf alle, einige oder keine Ihrer Zielnutzer:innen anwendet.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7 {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `campaigns.trigger.schedule.delete`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfragetext {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) the campaign identifier,
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Erforderlich | String | Siehe [Campaign-Bezeichner]({{site.baseurl}}/api/identifier_types). |
| `schedule_id` | Erforderlich | String | Die zu löschende `schedule_id` (aus der Antwort beim Erstellen des Zeitplans erhalten). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }


## Beispielanfrage {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}