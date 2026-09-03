---
nav_title: "GET: Spezifische Übersetzung und Lokalisierung für E-Mail-Template anzeigen"
article_title: "GET: Spezifische Übersetzung und Lokalisierung für E-Mail-Template anzeigen"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts „Spezifische Übersetzung und Lokalisierung für E-Mail-Template anzeigen“."
---

{% api %}
# Spezifische Übersetzung und Lokalisierung für E-Mail-Template anzeigen {#view-a-specific-translation-and-locale-for-email-template-endpoint}
{% apimethod get %}
/templates/translations/email
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine bestimmte Übersetzung und Lokalisierung für ein [E-Mail-Template]({{site.baseurl}}/user_guide/messaging/templates/email_templates) anzuzeigen. Weitere Informationen zu Übersetzungsfeatures finden Sie unter [Lokalisierungen in Nachrichten]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `templates.translations.get`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Abfrageparameter {#query-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---------------|----------|-----------|---------------------------------|
| `template_id` | Erforderlich | String | Die ID für Ihr E-Mail-Template. |
| `locale_id` | Optional | String | Die ID (UUID) der Lokalisierung. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Abfrageparameter" }

{% alert note %}
Alle Übersetzungs-IDs gelten als universelle eindeutige Bezeichner (UUIDs), die in der Antwort des GET-Endpunkts zu finden sind.
{% endalert %}

## Beispielanfrage {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/translations/email?locale_id={locale_uuid}&template_id={template_id}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Antwort {#response}

Es gibt vier Statuscode-Antworten für diesen Endpunkt: `200`, `400`, `404` und `429`.

### Beispiel für eine erfolgreiche Antwort {#example-success-response}

Der Statuscode `200` könnte den folgenden Antwort-Header und -Body zurückgeben.

```json
{
    "translations": [
        {
            "locale": {
                "uuid": "c7c12345-te35-1234-5678-abcdefa99r3f",
                "name": "es-MX",
                "country": "MX",
                "language": "es",
                "locale_key": "es-mx"
            },
            "translation_map": {
                "id_0": "¡Hola!",
                "id_1": "Me llamo Jacky",
                "id_2": "¿Dónde está la biblioteca?"
            }
        }
    ]
}
```

### Beispiel für eine Fehlerantwort {#example-error-response}

Der Statuscode `400` könnte den folgenden Antwort-Body zurückgeben. Unter [Fehlerbehebung](#troubleshooting) finden Sie weitere Informationen zu Fehlern, die auftreten können.

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