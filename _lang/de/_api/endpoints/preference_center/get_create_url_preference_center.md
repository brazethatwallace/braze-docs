---
nav_title: "GET: URL für das Präferenzzentrum generieren"
article_title: "GET: URL für das Präferenzzentrum generieren"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts „URL für das Präferenzzentrum generieren“."

---
{% api %}
# URL für das Präferenzzentrum generieren {#generate-preference-center-url}
{% apimethod get %}
/preference_center/v1/{preferenceCenterExternalID}/url/{userID}
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine URL für ein Präferenzzentrum zu generieren.

Jede URL des Präferenzzentrums ist für jede:n Nutzer:in eindeutig.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0bc750ff-068e-4391-897e-6eddca2561cd {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `preference_center.user.get`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='get preference center' %} Dieses Rate-Limit ist fest und nicht konfigurierbar.

## Pfad-Parameter {#path-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `preferenceCenterExternalID` | Erforderlich | String | Die ID für Ihr Präferenzzentrum. |
| `userID` | Erforderlich | String | Die Nutzer-ID. |
{: aria-label="Pfad-Parameter" }

## Anfrage-Parameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
| `preference_center_api_id` | Erforderlich | String | Die ID für Ihr Präferenzzentrum. |
| `external_id` | Erforderlich | String | Die externe ID für eine:n Nutzer:in. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrage-Parameter" }

## Beispielanfrage {#example-request}

```
curl --location --request GET 'https://rest.iad-01.braze.com/preference_center/v1/$preference_center_external_id/url/$user_external_id' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Antwort {#response}

```json
{
  "preference_center_url": "https://www.example.com/preferences"
}
```

{% endapi %}

{% alert note %}
Dieser Endpunkt generiert nur URLs für das neue Präferenzzentrum (wie Präferenzzentren, die mit unserer API oder dem Drag-and-Drop-Editor erstellt wurden).
{% endalert %}