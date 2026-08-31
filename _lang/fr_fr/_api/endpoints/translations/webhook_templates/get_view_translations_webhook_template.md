---
nav_title: "GET : Afficher les traductions pour un modèle de webhook"
article_title: "GET : Afficher les traductions pour un modèle de webhook"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint permettant d'afficher les traductions pour un modèle de webhook."
---

{% api %}
# Afficher les traductions pour un modèle de webhook {#view-translations-for-a-webhook-template}
{% apimethod get %}
/templates/webhook/translations
{% endapimethod %}

> Utilisez cet endpoint pour afficher les traductions d'un [modèle de webhook]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates). Vous pouvez retourner toutes les langues configurées ou filtrer la réponse par langue. Pour en savoir plus sur les fonctionnalités de traduction, consultez [Messages multilingues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec l'autorisation `templates.translations.get`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Paramètres de requête {#query-parameters}

| Paramètre | Obligatoire | Type de données | Description |
| --- | --- | --- | --- |
| `template_id` | Obligatoire | String | L'ID de votre modèle de webhook. |
| `locale_id` | Facultatif | String | L'UUID de la langue à retourner. S'il est omis, la réponse inclut toutes les langues configurées pour le modèle de webhook. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}

```bash
curl --location --request GET 'https://rest.iad-03.braze.com/templates/webhook/translations?template_id={TEMPLATE_ID}&locale_id={LOCALE_ID}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

Remplacez *`TEMPLATE_ID`* par l'ID de votre modèle de webhook et *`LOCALE_ID`* par l'UUID de la langue que vous souhaitez retourner. Omettez `locale_id` pour retourner toutes les langues configurées.

## Réponse {#response}

Il existe cinq codes de statut de réponse pour cet endpoint : `200`, `400`, `403`, `404` et `429`.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `200` pourrait retourner le corps de réponse suivant.

```json
{
  "translations": [
    {
      "translation_map": {
        "id_0": "¡Hola!",
        "id_1": "¿Te gustaría comprar esto?"
      },
      "locale": {
        "uuid": "c7c12345-de35-1234-5678-abcdefa99a3f",
        "name": "es-MX",
        "country": "MX",
        "language": "es",
        "locale_key": "es-mx"
      }
    },
    {
      "translation_map": {
        "id_0": "你好！",
        "id_1": "你想買這個嗎？"
      },
      "locale": {
        "uuid": "a1b12345-cd35-1234-5678-abcdefa99a3f",
        "name": "zh-HK",
        "country": "HK",
        "language": "zh",
        "locale_key": "zh-hk"
      }
    }
  ]
}
```

### Exemple de réponse d'erreur {#example-error-response}

Le code de statut `400` pourrait retourner le corps de réponse suivant.

```json
{
  "message": "Invalid locale ID"
}
```

{% endapi %}