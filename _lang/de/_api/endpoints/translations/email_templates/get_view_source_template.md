---
nav_title: "GET: Quellübersetzungen für E-Mail-Template anzeigen"
article_title: "GET: Quellübersetzungen für E-Mail-Template anzeigen"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt den Endpunkt zum Anzeigen der Quellübersetzungen für ein E-Mail-Template."
---

{% api %}
# Quellübersetzungen für ein E-Mail-Template anzeigen {#view-the-source-translations-for-an-email-template}
{% apimethod get %}
/templates/email/translations/source
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um die Quellübersetzungen für ein [E-Mail-Template]({{site.baseurl}}/user_guide/messaging/templates/email_templates) anzuzeigen. Weitere Informationen zu Übersetzungsfeatures finden Sie unter [Locales in Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `templates.email.info`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Abfrageparameter {#query-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---------------|----------|-----------|---------------------------------|
| `template_id` | Erforderlich | String | Die ID für Ihr E-Mail-Template. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Abfrageparameter" }

## Beispielanfrage {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/email/translations/source?template_id={template_id}'
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
--Request Body
---template_id: "6ad1507f-ca10-44c4-95bf-aj39fm10fm1ps"
```

## Antwort {#response}

Es gibt vier Statuscode-Antworten für diesen Endpunkt: `200`, `400`, `404` und `429`.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `200` könnte den folgenden Response-Header und -Body zurückgeben.

```json
{
    "translations": {
        "translation_map": {
            "id_0": "Here's a limited time offer for your membership tier!",
            "id_1": "Welcome to a new fashion-forward season!"
        }
    },
    "message": "success"
}
```

### Beispiel für eine Fehlerantwort {#example-error-response}

Der Statuscode `400` könnte den folgenden Antworttext zurückgeben. Unter [Fehlerbehebung](#troubleshooting) finden Sie weitere Informationen zu Fehlern, die auftreten können.

```json
{
    "errors": [
        {
            "message": "The provided locale code does not exist."
        }
    ]
}
```

{% endapi %}