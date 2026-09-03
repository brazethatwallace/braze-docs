---
nav_title: "PUT : Mettre à jour les traductions d'un modèle de webhook"
article_title: "PUT : Mettre à jour les traductions d'un modèle de webhook"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "Cet article décrit l'endpoint permettant de mettre à jour les traductions d'un modèle de webhook."
---

{% api %}
# Mettre à jour les traductions d'un modèle de webhook {#update-translations-for-a-webhook-template}
{% apimethod put %}
/templates/webhook/translations
{% endapimethod %}

> Utilisez cet endpoint pour mettre à jour les traductions d'un [modèle de webhook]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates). Pour plus d'informations sur les fonctionnalités de traduction, consultez [Messages multilingues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec la permission `templates.translations.update`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Paramètres de chemin {#path-parameters}

Il n'y a pas de paramètres de chemin pour cet endpoint.

## Paramètres de requête {#request-parameters}

| Paramètre | Obligatoire | Type de données | Description |
| --- | --- | --- | --- |
| `template_id` | Obligatoire | String | L'ID de votre modèle de webhook. |
| `locale_id` | Obligatoire | String | L'UUID de la locale à mettre à jour. La locale doit être configurée pour le modèle de webhook. |
| `translation_map` | Obligatoire | Objet | Un objet contenant les traductions mises à jour. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}

```bash
curl --location --request PUT 'https://rest.iad-03.braze.com/templates/webhook/translations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "template_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
  "locale_id": "a14404b3-3626-4de0-bdec-06935f3aa0ad",
  "translation_map": {
    "id_0": "¡Hola!",
    "id_1": "¿Te gustaría comprar esto?"
  }
}'
```

## Réponse {#response}

Il existe cinq codes de statut de réponse pour cet endpoint : `200`, `400`, `403`, `404` et `429`.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `200` renvoie le corps de réponse vide suivant.

```json
{}
```

### Exemple de réponse d'erreur {#example-error-response}

Le code de statut `400` pourrait renvoyer le corps de réponse suivant.

```json
{
  "message": "Locale not found"
}
```

{% endapi %}