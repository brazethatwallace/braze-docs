---
nav_title: "GET : Afficher la traduction et la locale spécifiques pour un modèle d'e-mail"
article_title: "GET : Afficher la traduction et la locale spécifiques pour un modèle d'e-mail"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Cet article décrit les détails de l'endpoint permettant d'afficher une traduction et une locale spécifiques pour un modèle d'e-mail."
---

{% api %}
# Afficher une traduction et une locale spécifiques pour l'endpoint du modèle d'e-mail {#view-a-specific-translation-and-locale-for-email-template-endpoint}
{% apimethod get %}
/templates/translations/email
{% endapimethod %}

> Utilisez cet endpoint pour afficher une traduction et une locale spécifiques pour un [modèle d'e-mail]({{site.baseurl}}/user_guide/messaging/templates/email_templates/). Consultez [Locales dans les messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) pour plus d'informations sur les fonctionnalités de traduction.

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l'autorisation `templates.translations.get`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Paramètres de requête {#query-parameters}

| Paramètre     | Requis | Type de données | Description                     |
|---------------|----------|-----------|---------------------------------|
| `template_id` | Requis | Chaîne de caractères    | L'ID de votre modèle d'e-mail. |
| `locale_id`   | Facultatif | Chaîne de caractères    | L'ID (UUID) de la locale.           |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

{% alert note %}
Tous les ID de traduction sont considérés comme des identifiants uniques universels (UUID), que vous pouvez retrouver dans la réponse de l'endpoint GET.
{% endalert %}

## Exemple de requête {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/translations/email?locale_id={locale_uuid}&template_id={template_id}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse {#response}

Il existe quatre codes de statut de réponse pour cet endpoint : `200`, `400`, `404` et `429`.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `200` pourrait renvoyer l'en-tête et le corps de réponse suivants.

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

### Exemple de réponse en erreur {#example-error-response}

Le code de statut `400` pourrait renvoyer le corps de réponse suivant. Consultez la section [Résolution des problèmes](#troubleshooting) pour plus d'informations sur les erreurs que vous pourriez rencontrer.

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