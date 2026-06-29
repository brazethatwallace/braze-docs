---
nav_title: "POST: Geplante API-getriggerte Canvases aktualisieren"
article_title: "POST: Geplante API-getriggerte Canvases aktualisieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts „Geplante API-getriggerte Canvases aktualisieren“."

---
{% api %}
# Geplante API-getriggerte Canvases aktualisieren {#update-scheduled-api-triggered-canvases}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/canvas/trigger/schedule/update
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um geplante, API-getriggerte Canvases zu aktualisieren, die im Dashboard erstellt wurden.

So können Sie festlegen, welche Aktion den Versand der Nachricht triggern soll. Sie können `trigger_properties` übergeben, die Braze in die Nachricht selbst einfügt.

Beachten Sie, dass Sie zum Versenden von Nachrichten über diesen Endpunkt eine Canvas-ID benötigen, die beim Erstellen eines [Canvas]({{site.baseurl}}/api/identifier_types#canvas-api-identifier) generiert wird.

Jeder Zeitplan überschreibt den Zeitplan, den Sie in der ursprünglichen Anfrage zum Erstellen des Zeitplans oder in früheren Anfragen zum Aktualisieren des Zeitplans angegeben haben, vollständig.
  - Wenn Sie z. B. ursprünglich `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` angeben und dann in Ihrem Update `"schedule" : {"time" : "2015-02-20T14:14:47"}` übergeben, sendet Braze Ihre Nachricht zur angegebenen Zeit in UTC, nicht in der Ortszeit der Nutzer:innen.
  - Geplante Trigger, die Sie kurz vor oder während des vorgesehenen Sendezeitpunkts aktualisieren, werden nach bestem Bemühen aktualisiert, sodass Braze möglicherweise in letzter Sekunde Änderungen an allen, einigen oder keinen Ihrer Zielnutzer:innen vornimmt.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8fdf158b-ce20-41d8-80e4-a9300a6706d4 {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key) mit der Berechtigung `canvas.trigger.schedule.update`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfragetext {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `canvas_id` | Erforderlich | String | Siehe [Canvas-Bezeichner]({{site.baseurl}}/api/identifier_types). |
| `schedule_id` | Optional | String | Die zu aktualisierende `schedule_id` (erhalten aus der Antwort auf die Anfrage zum Erstellen des Zeitplans). |
| `schedule` | Erforderlich | Objekt | Siehe [Zeitplan-Objekt]({{site.baseurl}}/api/objects_filters/schedule_object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

## Beispielanfrage {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T21:30:00Z",
    "in_local_time": true
  }
}'
```

{% endapi %}