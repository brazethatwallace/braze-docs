---
nav_title: "GET : Consulter les traductions sources pour un modèle d'e-mail"
article_title: "GET : Consulter les traductions sources pour un modèle d'e-mail"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint permettant de consulter les traductions sources d'un modèle d'e-mail."
---

{% api %}
# Consulter les traductions sources d'un modèle d'e-mail {#view-the-source-translations-for-an-email-template}
{% apimethod get %}
/templates/email/translations/source
{% endapimethod %}

> Utilisez cet endpoint pour consulter les traductions sources d'un [modèle d'e-mail]({{site.baseurl}}/user_guide/messaging/templates/email_templates). Consultez [Paramètres régionaux dans les messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) pour plus d'informations sur les fonctionnalités de traduction.

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec l'autorisation `templates.email.info`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Paramètres de requête {#query-parameters}

| Paramètre | Requis | Type de données | Description |
|---------------|----------|-----------|---------------------------------|
| `template_id` | Requis | Chaîne de caractères | L'ID de votre modèle d'e-mail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/email/translations/source?template_id={template_id}'
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
--Request Body
---template_id: "6ad1507f-ca10-44c4-95bf-aj39fm10fm1ps"
```

## Réponse {#response}

Quatre codes de statut sont possibles pour cet endpoint : `200`, `400`, `404` et `429`.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `200` pourrait renvoyer l'en-tête et le corps de réponse suivants.

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