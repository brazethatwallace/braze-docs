---
nav_title: "POST: Geplante API-getriggerte Campaigns aktualisieren"
article_title: "POST: Geplante API-getriggerte Campaigns aktualisieren"
search_tag: Endpoint
page_order: 4
layout: api_page
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts zum Aktualisieren geplanter API-getriggerter Campaigns."

---
{% api %}
# Geplante API-getriggerte Campaigns aktualisieren {#update-scheduled-api-triggered-campaigns}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/campaigns/trigger/schedule/update
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um geplante API-getriggerte Campaigns zu aktualisieren, die im Dashboard erstellt wurden. So können Sie entscheiden, welche Aktion den Versand der Nachricht triggern soll.

Sie können `trigger_properties` übergeben, die Braze als Templates in die Nachricht selbst einfügt.

Beachten Sie, dass Sie zum Versenden von Nachrichten mit diesem Endpunkt eine Campaign-ID benötigen, die beim Erstellen einer [API-getriggerten Campaign]({{site.baseurl}}/api/api_campaigns/) erzeugt wurde.

Jeder Zeitplan überschreibt vollständig den Zeitplan, den Sie in der Anfrage zum Erstellen des Zeitplans oder in früheren Anfragen zum Aktualisieren des Zeitplans angegeben haben. Wenn Sie den Zeitplan beispielsweise ursprünglich auf `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` eingestellt haben und ihn später auf `"schedule" : {"time" : "2015-02-20T14:14:47"}` aktualisieren, sendet Braze die Nachricht zur angegebenen Zeit in UTC, nicht in der Ortszeit der Nutzer:innen.

Geplante Trigger, die kurz vor oder während der geplanten Sendezeit aktualisiert werden, werden nach bestem Bemühen aktualisiert, sodass Braze Änderungen in letzter Sekunde auf alle, einige oder keine Ihrer Zielgruppen-Nutzer:innen anwenden kann. Updates werden nicht übernommen, wenn der ursprüngliche Zeitplan die Ortszeit verwendete und die ursprüngliche Zeit in einer beliebigen Zeitzone bereits vergangen ist.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d2a6e66-9d6f-4ae1-965a-79fa52b86b1d {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `campaigns.trigger.schedule.update`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfragetext {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Erforderlich | String | Siehe [Campaign-Bezeichner]({{site.baseurl}}/api/identifier_types/) |
| `schedule_id` | Erforderlich | String | Die zu aktualisierende `schedule_id` (erhalten aus der Antwort zum Erstellen eines Zeitplans). |
| `schedule` | Erforderlich | Objekt | Siehe [Zeitplan-Objekt]({{site.baseurl}}/api/objects_filters/schedule_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

## Beispielanfrage {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T21:30:00Z",
    "in_local_time": true
  }
}'
```

{% endapi %}