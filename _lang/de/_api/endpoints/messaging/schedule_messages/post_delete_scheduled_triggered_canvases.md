---
nav_title: "POST: Geplante API-getriggerte Canvases löschen"
article_title: "POST: Geplante API-getriggerte Canvases löschen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts „Geplante API-getriggerte Canvases löschen“."

---
{% api %}
# Geplante API-getriggerte Canvases löschen {#delete-scheduled-api-triggered-canvases}
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/trigger/schedule/delete
{% endapimethod %}

> Mit dem Endpunkt „Zeitplan löschen“ können Sie eine Nachricht stornieren, die Sie zuvor über API-getriggerte Canvases geplant haben, bevor sie versendet wurde.

Geplante Nachrichten oder Trigger, die kurz vor oder während des vorgesehenen Sendezeitpunkts gelöscht werden, werden nach bestem Bemühen aktualisiert. Das bedeutet, dass Braze Löschungen in letzter Sekunde möglicherweise auf alle, einige oder keine Ihrer Zielnutzer:innen anwendet.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7 {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `canvas.trigger.schedule.delete`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfragetext {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) the Canvas identifier,
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `canvas_id` | Erforderlich | String | Siehe [Canvas-Bezeichner]({{site.baseurl}}/api/identifier_types/). |
| `schedule_id` | Erforderlich | String | Die zu löschende `schedule_id` (aus der Antwort auf die Zeitplanerstellung erhalten). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }


## Beispielanfrage {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}