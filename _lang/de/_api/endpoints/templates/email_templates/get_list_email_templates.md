---
nav_title: "GET: Liste der verfügbaren E-Mail-Templates"
article_title: "GET: Liste der verfügbaren E-Mail-Templates"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Braze-Endpunkt „Liste der verfügbaren E-Mail-Templates“."
---
{% api %}
# Liste der verfügbaren E-Mail-Templates {#list-available-email-templates}
{% apimethod get %}
/templates/email/list
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine Liste der verfügbaren E-Mail-Templates in Ihrem Braze-Konto abzurufen.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#eec24bf4-a3f4-47cb-b4d8-bb8f03964cca {% endapiref %}

## Voraussetzungen {#prerequisites}
Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics) mit der Berechtigung `templates.email.list`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `modified_after` | Optional | String im [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)-Format | Ruft nur Templates ab, die zum oder nach dem angegebenen Zeitpunkt aktualisiert wurden. |
| `modified_before` | Optional | String im [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)-Format | Ruft nur Templates ab, die zum oder vor dem angegebenen Zeitpunkt aktualisiert wurden. |
| `limit` | Optional | Positive Zahl | Maximale Anzahl der abzurufenden Templates. Standardmäßig 100, wenn nicht angegeben, mit einem maximal zulässigen Wert von 1000. |
| `offset` | Optional | Positive Zahl | Anzahl der Templates, die übersprungen werden sollen, bevor der Representational State Transfer der Templates zurückgegeben wird, die den Suchkriterien entsprechen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

## Beispielanfrage {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/templates/email/list?modified_after=2020-01-01T01:01:01.000000&modified_before=2020-02-01T01:01:01.000000&limit=1&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Antwort {#response}

{% alert important %}
Templates, die mit dem Drag-and-Drop-Editor für E-Mails erstellt wurden, werden in dieser Antwort nicht bereitgestellt.
{% endalert %}

```json
{
  "count": the number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string) the time the email was created at in ISO 8601,
    "updated_at": (string) the time the email was updated in ISO 8601,
    "tags": (array of strings) tags appended to the template
}
```
{% endapi %}