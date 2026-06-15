---
nav_title: "POST: Campaigns duplizieren"
article_title: "POST: Campaigns duplizieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Einzelheiten zum Endpunkt „Campaigns duplizieren“."

---
{% api %}
# Campaigns über die API duplizieren {#duplicate-campaigns-using-the-api}
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/campaigns/duplicate
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Campaigns zu duplizieren. Dieser API-Endpunkt ist vergleichbar mit dem [Duplizieren von Campaigns im Braze-Dashboard][1].

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, müssen Sie einen API-Schlüssel mit der Berechtigung `campaigns.duplicate` erstellen.

## Rate-Limit

Dieser Endpunkt ist auf 100 API-Aufrufe pro Minute beschränkt.

## Anfragetext {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) The campaign identifier,
  "name": (required, string) The name of the resulting campaign,
  "description": (optional, string) The description of the resulting campaign,
  "tag_names": (optional, string) The tags of the resulting campaign,
}
```

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Erforderlich | String | Siehe [Campaign-Bezeichner]({{site.baseurl}}/api/identifier_types/). |
| `name` | Erforderlich | String | Der Name der resultierenden Campaign. |
| `description` | Optional | String | Das Beschreibungsfeld für die resultierende Campaign. |
| `tag_names` | Optional | String | Die Tags für die resultierende Campaign. Diese müssen bereits vorhandene Tags sein. Wenn Sie in der Anfrage neue Tags hinzufügen, überschreiben diese alle Tags, die der ursprünglichen Campaign zugewiesen waren. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }


## Antwort {#response}

Dieser Endpunkt gibt den Statuscode `202` zurück, und die Erstellung der Campaign erfolgt asynchron. Mit dem [Sicherheitsereignis-Download][2] können Sie Aufzeichnungen darüber einsehen, wann Campaigns dupliziert wurden und mit welchem API-Schlüssel.


[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns#duplicating-segments-campaigns-and-canvases
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#downloading-a-security-event-report

{% endapi %}