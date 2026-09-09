---
nav_title: "GET : Afficher les traductions source d'un modèle de webhook"
article_title: "GET : Afficher les traductions source d'un modèle de webhook"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint permettant d'afficher les traductions source d'un modèle de webhook."
---

{% api %}
# Afficher les traductions source d'un modèle de webhook {#view-source-translations-for-a-webhook-template}
{% apimethod get %}
/templates/webhook/translations/source
{% endapimethod %}

> Utilisez cet endpoint pour afficher les traductions source par défaut d'un [modèle de webhook]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates). Pour plus d'informations sur les fonctionnalités de traduction, consultez [Messages multilingues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec l'autorisation `templates.translations.get`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Paramètres de requête {#query-parameters}

| Paramètre | Obligatoire | Type de données | Description |
| --- | --- | --- | --- |
| `template_id` | Obligatoire | String | L'ID de votre modèle de webhook. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}

```bash
curl --location --request GET 'https://rest.iad-03.braze.com/templates/webhook/translations/source?template_id={TEMPLATE_ID}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

Remplacez *`TEMPLATE_ID`* par l'ID de votre modèle de webhook.

## Réponse {#response}

Il existe cinq codes de réponse pour cet endpoint : `200`, `400`, `403`, `404` et `429`.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `200` pourrait renvoyer le corps de réponse suivant.

```json
{
  "translations": {
    "translation_map": {
      "id_0": "Hello!",
      "id_1": "Would you like to buy this?"
    }
  }
}
```

### Exemple de réponse d'erreur {#example-error-response}

Le code de statut `400` pourrait renvoyer le corps de réponse suivant.

```json
{
  "message": "This template does not have multi-language setup"
}
```

{% endapi %}