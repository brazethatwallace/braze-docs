---
nav_title: "POST: E-Mails auf die Blacklist setzen"
article_title: "POST: E-Mails auf die Blacklist setzen"
search_tag: Endpoint
page_order: 10
layout: api_page
page_type: reference
alias: /blacklist/
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts „E-Mails auf die Blacklist setzen“."

---
{% api %}
# E-Mails auf die Blacklist setzen {#blacklist-emails}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/email/blacklist
{% endapimethod %}

{% alert important %}
Braze hat den [`/email/blocklist`-Endpunkt]({{site.baseurl}}/api/endpoints/email/post_blocklist) mit denselben Funktionen wie den `/email/blacklist`-Endpunkt veröffentlicht. Wir empfehlen Ihnen, stattdessen den `/email/blocklist`-Endpunkt zu verwenden.
{% endalert %}

> Verwenden Sie diesen Endpunkt, um Nutzer:innen von E-Mails abzumelden und als Hard Bounce zu markieren.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d51155a1-a6e8-4dcc-9f2b-88c54ab9e8c6 {% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key) mit der Berechtigung `email.blacklist`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfragetext {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["blacklist_email1","blacklist_email2"]
}
```

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
| -----------|----------| --------|------- |
| `email` | Erforderlich | String oder Array | String-E-Mail-Adresse für die Blacklist oder ein Array mit bis zu 50 E-Mail-Adressen für die Blacklist. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

## Beispielanfrage {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/blacklist' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
  "email": ["blacklist_email1","blacklist_email2"]
}'
```

{% endapi %}