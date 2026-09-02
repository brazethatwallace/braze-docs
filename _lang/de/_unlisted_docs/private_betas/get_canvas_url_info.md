---
nav_title: "GET: Link-Aliase für Canvas auflisten"
layout: api_page
page_type: reference
hidden: true
permalink: /get_canvas_link_alias/

platform: API
channel:
  - Email
tool:
  - Canvas
  - Campaigns

description: "Dieser Artikel beschreibt Details zum Endpunkt „Link-Aliase für Canvas auflisten“."
---
{% api %}
# Link-Aliase für Canvas auflisten {#list-link-alias-for-canvas}
{% apimethod get %}
/canvas/url_info/details
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um die in einem bestimmten E-Mail-Canvas-Schritt festgelegten Link-Aliase aufzulisten.

{% apiref postman %}  {% endapiref %}

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `canvas_step_id` | Erforderlich | String | Siehe [Canvas-Schritt-API-Bezeichner]({{site.baseurl}}/api/identifier_types#canvas-identifier). |
| `message_variation_id ` | Erforderlich | String | API-Bezeichner der Nachrichtenvariante (für die E-Mail-Nachrichtenvariante in diesem Schritt). Sie finden diesen, indem Sie auf der Seite **Canvas-Details** auf **Varianten analysieren** klicken. |
| `includes_link_id` | Optional | String | Ein bestimmter Link-Bezeichner (wie von Braze zugewiesen) oder `null`. Wird verwendet, um die Ergebnisse nach einer bestimmten `link_id` zu filtern. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Beispielanfrage {#example-request}

```
curl --location --request GET 'https://rest.iad-01.braze.com/canvas/url_info/details?campaign_id=4615a404-b2c2-421e-9a04-2233bb3ec4f9&message_variation_id=0ea708fe-36b4-43f7-9f5c-a0650ea2a7a0&includes_link_id=014tk4e0kg97' \
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
| `Missing/Invalid Canvas ID` | Die Canvas-API-ID muss ein API-Bezeichner sein. Sie finden diesen über den [Endpunkt „Canvas-Liste exportieren“]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases) oder indem Sie sich im Dashboard anmelden. |
| `Missing/Invalid Message Variant ID` | Die API-ID der Nachrichtenvariante muss ein API-Bezeichner sein. Sie finden diesen über den [Endpunkt „Canvas-Details exportieren“]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details) oder indem Sie sich im Dashboard anmelden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}