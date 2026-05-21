---
nav_title: "GET: Informationen zu Content Blocks anzeigen"
article_title: "GET: Informationen zu Content Blocks anzeigen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts „Content-Block-Informationen anzeigen“."
---

{% api %}
# Content-Block-Informationen anzeigen {#see-content-block-information}
{% apimethod get %}
/content_blocks/info
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Informationen zu Ihren bestehenden [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/) abzurufen.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#589adda3-0def-4369-9ddc-eae71923c0ee {% endapiref %}

## Voraussetzungen {#prerequisites}
Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `content_blocks.info`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `content_block_id`  | Erforderlich | String | Der Content-Block-Bezeichner. <br><br>Sie finden diesen, indem Sie entweder die Content-Block-Informationen über einen API-Aufruf auflisten oder die Seite [API-Schlüssel]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers/) aufrufen, dann nach unten scrollen und nach Ihrem Content-Block-API-Bezeichner suchen.|
| `include_inclusion_data`  | Optional | Boolescher Wert | Wenn auf `true` gesetzt, gibt die API den API-Bezeichner der Nachrichtenvariante von Campaigns und Canvases zurück, in denen dieser Content-Block enthalten ist, um ihn in nachfolgenden Aufrufen zu verwenden.  Die Ergebnisse schließen archivierte oder gelöschte Campaigns oder Canvases aus. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

## Beispielanfrage {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/content_blocks/info?content_block_id={{content_block_id}}&include_inclusion_data=false' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Antwort {#response}

```json
{
  "content_block_id": (string) the Content Block identifier,
  "name": (string) the name of the Content Block,
  "content": (string) the content in the Content Block,
  "description": (string) the Content Block description,
  "content_type": (string) the content type, html or text,
  "tags": (array) An array of tags formatted as strings,
  "created_at": (string) The time the Content Block was created in ISO 8601,
  "last_edited": (string) The time the Content Block was last edited in ISO 8601,
  "inclusion_count" : (integer) the inclusion count,
  "inclusion_data": (array) the inclusion data,
  "message": "success"
}
```

## Fehlerbehebung {#troubleshooting}

Die folgende Tabelle listet mögliche zurückgegebene Fehler und die zugehörigen Schritte zur Fehlerbehebung auf.

| Fehler | Fehlerbehebung |
| --- | --- |
| `Content Block ID cannot be blank` | Stellen Sie sicher, dass ein Content-Block in Ihrer Anfrage aufgeführt und in Anführungszeichen (`""`) eingeschlossen ist. |
| `Content Block ID is invalid for this workspace` | Dieser Content-Block existiert nicht oder befindet sich in einem anderen Unternehmenskonto oder Workspace. |
| `Content Block has been deleted—content not available` | Dieser Content-Block wurde gelöscht, auch wenn er zuvor existiert hat. |
| `Include Inclusion Data—error` | Dieser Parameter akzeptiert nur boolesche Werte (true oder false). Stellen Sie sicher, dass der Wert für `include_inclusion_data` nicht in Anführungszeichen (`""`) eingeschlossen ist, da der Wert sonst als String gesendet wird. Weitere Details finden Sie unter [Anfrageparameter](#request-parameters). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }


{% endapi %}