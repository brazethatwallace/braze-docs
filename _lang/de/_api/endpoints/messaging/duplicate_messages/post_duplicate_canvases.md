---
nav_title: "POST: Canvases duplizieren"
article_title: "POST: Canvases duplizieren"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Einzelheiten zum Endpunkt „Canvases duplizieren“."
---

{% api %}
# Canvases über die API duplizieren {#duplicate-canvases-using-the-api}
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/canvas/duplicate
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um Canvases zu duplizieren. Dieser API-Endpunkt ist vergleichbar mit dem [Duplizieren von Canvases im Braze-Dashboard][1].

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, müssen Sie einen API-Schlüssel mit der Berechtigung `canvas.duplicate` generieren.

## Rate-Limits {#rate-limit}

Dieser Endpunkt ist auf 100 API-Aufrufe pro Minute beschränkt.

## Anfragetext {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) The Canvas identifier,
  "name": (required, string) The name of the resulting Canvas,
  "description": (optional, string) The description of the resulting Canvas,
  "tag_names": (optional, string) The tags of the resulting Canvas,
}
```

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `canvas_id` | Erforderlich | String | Siehe [Canvas-Bezeichner](https://www.braze.com/docs/api/identifier_types/). |
| `name` | Erforderlich | String | Der Name des resultierenden Canvas. |
| `description` | Optional | String | Das Beschreibungsfeld für das resultierende Canvas. |
| `tag_names` | Optional | String | Die Tags für das resultierende Canvas. Es muss sich um bestehende Tags handeln. Wenn Sie in der Anfrage neue Tags hinzufügen, überschreiben diese alle Tags, die sich auf dem ursprünglichen Canvas befanden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

## Antwort {#response}

Dieser Endpunkt gibt einen Statuscode `202` zurück, und die Erstellung des Canvas erfolgt asynchron. Sie können den [Download der Sicherheitsereignisse][2] verwenden, um Aufzeichnungen darüber einzusehen, wann Canvases dupliziert wurden und mit welchem API-Schlüssel.

[1]: {{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/duplicating
[2]: {{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings

{% endapi %}