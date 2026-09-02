---
nav_title: "POST: Content-Block aktualisieren"
article_title: "POST: Content-Block aktualisieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt Details zum Braze-Endpunkt „Content Blocks aktualisieren“."
---
{% api %}
# Content-Block aktualisieren {#update-content-block}
{% apimethod post %}
/content_blocks/update
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um einen [Content-Block]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) zu aktualisieren.

{% alert tip %}
Sie können diesen Endpunkt auch über den [Braze MCP-Server]({{site.baseurl}}/user_guide/brazeai/mcp_server) mit der Funktion [`update_content_block`]({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions#content-blocks) aufrufen. So können KI-Tools wie Claude und Cursor Content Blocks über natürlichsprachliche Eingaben aktualisieren.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#4782239a-cb60-4217-9de0-51411434d57d {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics) mit der Berechtigung `content_blocks.update`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfragetext {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "content_block_id" : (required, string) Content Block's API identifier.
  "name": (optional, string) Must be less than 100 characters,
  "description": (optional, string) The description of the Content Block. Must be less than 250 character,
  "content": (optional, string) HTML or text content within Content Block,
  "state": (optional, string) Choose `active` or `draft`. Defaults to `active` if not specified,
  "tags": (optional, array of strings) Tags must already exist
}
```

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `content_block_id` | Erforderlich | String | Der API-Bezeichner Ihres Content-Blocks. |
| `name` | Optional | String | Name des Content-Blocks. Muss weniger als 100 Zeichen umfassen. |
| `description` | Optional | String | Beschreibung des Content-Blocks. Muss weniger als 250 Zeichen umfassen. |
| `content` | Optional | String | HTML- oder Textinhalte innerhalb von Content Blocks. |
| `state` | Optional | String | Wählen Sie `active` oder `draft`. Der Standardwert ist `active`, wenn nichts angegeben wird. |
| `tags` | Optional | String-Array | [Tags]({{site.baseurl}}/user_guide/messaging/governance/tags) müssen bereits existieren. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

## Beispielanfrage {#example-request}

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/content_blocks/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "content_block_id" :"content_block_id",
  "name": "content_block",
  "description": "This is my Content Block",
  "content": "HTML or text content within block",
  "state": "draft",
  "tags": ["marketing"]
}'
```

## Antwort {#response}

```json
{
  "content_block_id": (string) Your newly generated block id,
  "liquid_tag": (string) The generated block tag from the Content Block name,
  "created_at": (string) The time the Content Block was created in ISO 8601,
  "message": "success"
}
```

## Fehlerbehebung {#troubleshooting}

In der folgenden Tabelle finden Sie eine Liste möglicher zurückgegebener Fehler und die entsprechenden Schritte zur Fehlerbehebung.

| Fehler | Fehlerbehebung |
| --- | --- |
| `Content cannot be blank` |
| `Content must be a string` | Achten Sie darauf, dass Ihr Inhalt in Anführungszeichen (`""`) eingeschlossen ist. |
| `Content must be smaller than 50kb` | Der Inhalt Ihres Content-Blocks muss insgesamt weniger als 50 KB groß sein. |
| `Content contains malformed liquid` | Das angegebene Liquid ist ungültig oder nicht parsbar. Bitte versuchen Sie es erneut mit gültigem Liquid oder wenden Sie sich an den Support. |
| `Content Block cannot be referenced within itself` |
| `Content Block description cannot be blank` |
| `Content Block description must be a string` | Achten Sie darauf, dass die Beschreibung Ihres Content-Blocks in Anführungszeichen (`""`) eingeschlossen ist. |
| `Content Block description must be shorter than 250 characters` |
| `Content Block name cannot be blank` |
| `Content Block name must be shorter than 100 characters` |
| `Content Block name can only contain alphanumeric characters` | Content-Block-Namen können jedes der folgenden Zeichen enthalten: die Buchstaben (groß- oder kleingeschrieben) `A` bis `Z`, die Zahlen `0` bis `9`, Bindestriche `-` und Unterstriche `_`. Er kann keine nicht-alphanumerischen Zeichen wie Emojis, `!`, `@`, `~`, `&` und andere „Sonderzeichen“ enthalten. |
| `Content Block with this name already exists` | Versuchen Sie einen anderen Namen. |
| `Content Block name cannot be updated for active Content Blocks` |
| `Content Block state must be either active or draft` |
| `Active Content Block can not be updated to Draft. Create a new Content Block.` |
| `Tags must be an array` | Tags müssen als String-Array formatiert werden, zum Beispiel `["marketing", "promotional", "transactional"]`. |
| `All tags must be strings` | Achten Sie darauf, dass Ihre Tags in Anführungszeichen (`""`) eingeschlossen sind. |
| `Some tags could not be found` | Um bei der Erstellung eines Content-Blocks ein Tag hinzuzufügen, muss das Tag bereits in Braze vorhanden sein. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fehlerbehebung" }


{% endapi %}