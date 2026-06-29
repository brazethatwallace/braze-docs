---
nav_title: "GET: Link-Aliase für Campaigns auflisten"
layout: api_page
page_type: reference
hidden: true
permalink: /get_campaign_link_alias/

platform: API
channel:
  - Email
tool:
  - Canvas
  - Campaigns

description: "Dieser Artikel beschreibt Details zum Braze-Endpunkt zum Auflisten von Link-Aliasen."
---
{% api %}
# Link-Aliase für Campaign auflisten {#list-link-alias-for-campaign}
{% apimethod get %}
/campaigns/url_info/details
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um die in einer bestimmten Campaign-Nachrichtenvariante festgelegten Link-Aliase aufzulisten.

{% apiref postman %}  {% endapiref %}

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `campaign_id` | Erforderlich | String | Siehe [Campaign-API-Bezeichner]({{site.baseurl}}/api/identifier_types/#campaign-api-identifier). |
| `message_variation_id ` | Erforderlich | String | API-Bezeichner der Nachrichtenvariante. Sie finden diesen auf der Campaign-Detailseite unter dem Abschnitt **API Identifier**. |
| `includes_link_id` | Optional | String | Ein bestimmter Link-Bezeichner (wie von Braze zugewiesen) oder `null`. Wird verwendet, um die Ergebnisse nach einer bestimmten `link_id` zu filtern. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Beispielanfrage {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/campaigns/url_info/details?campaign_id=4615a404-b2c2-421e-9a04-2233bb3ec4f9&message_variation_id=0ea708fe-36b4-43f7-9f5c-a0650ea2a7a0&includes_link_id=014tk4e0kg97' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Antwort {#response}

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "channel": "email",
  "name": "Variant 1",
  "link_data": [
    {
      "link_URL": "https://www.braze.com?lid=014tk4e0kg97",
      "link_id": "014tk4e0kg97",
      "content_block_path_info": [],
      "link_alias": "link5"
    }
  ],
  "message": "success"
}
```

### Fehlerbehebung {#troubleshooting}

Die folgende Tabelle listet mögliche zurückgegebene Fehler und die zugehörigen Schritte zur Fehlerbehebung auf.

| Fehler | Fehlerbehebung |
| --- | --- |
| `Missing/Invalid Campaign ID` | Die Campaign-API-ID muss ein API-Bezeichner sein. Sie finden diesen über den [Endpunkt zum Exportieren der Campaign-Liste]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/) oder indem Sie sich im Dashboard anmelden. |
| `Missing/Invalid Message Variant ID` | Die API-ID der Nachrichtenvariante muss ein API-Bezeichner sein. Sie finden diesen über den [Endpunkt zum Exportieren von Campaign-Details]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/) oder indem Sie sich im Dashboard anmelden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endapi %}