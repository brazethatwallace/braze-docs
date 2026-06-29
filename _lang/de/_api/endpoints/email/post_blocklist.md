---
nav_title: "POST: E-Mails auf Blockliste setzen"
article_title: "POST: E-Mails auf Blockliste setzen"
search_tag: Endpoint
page_order: 8
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts „E-Mails auf Blockliste setzen“."

---
{% api %}
# E-Mails auf Blockliste setzen {#blocklist-emails}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/email/blocklist
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Nutzer:in von E-Mails abzumelden und als Hard Bounce zu markieren.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d51155a1-a6e8-4dcc-9f2b-88c54ab9e8c6 {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `email.blacklist`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfragetext {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["blocklist_email1","blocklist_email2"]
}
```

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| -----------|----------| --------|------- |
| `email` | Erforderlich | String oder Array | String-E-Mail-Adresse für die Blockliste oder ein Array mit bis zu 50 E-Mail-Adressen für die Blockliste. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

## Beispielanfrage {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/blocklist' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": ["blocklist_email1","blocklist_email2"]
}'
```

{% endapi %}