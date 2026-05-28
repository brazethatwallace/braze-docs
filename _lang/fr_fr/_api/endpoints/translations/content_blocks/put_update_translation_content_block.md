---
nav_title: "PUT : Mettre à jour la traduction dans un bloc de contenu"
article_title: "PUT : Mettre à jour la traduction dans un bloc de contenu"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Mettre à jour la traduction dans un bloc de contenu."
---

{% api %}
# Mettre à jour la traduction dans un bloc de contenu {#update-translation-in-a-content-block}
{% apimethod put %}
/content_blocks/translations
{% endapimethod %}

> Utilisez cet endpoint pour mettre à jour plusieurs traductions d'un [bloc de contenu]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks/). Consultez [Locales dans les messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) pour en savoir plus sur les fonctionnalités de traduction.

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l'autorisation `content_blocks.translations.update`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Paramètres de chemin {#path-parameters}

Cet endpoint ne comporte pas de paramètres de chemin.

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `content_block_id` | Requis | Chaîne de caractères | L'ID de votre bloc de contenu. |
| `locale_id` | Requis | Chaîne de caractères | L'ID (UUID) de la locale. |
| `translation_map` | Requis | Objet | Objet contenant les nouvelles traductions. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

{% alert note %}
Tous les ID de traduction sont considérés comme des identifiants uniques universels (UUID), qui peuvent être trouvés dans la réponse de l'endpoint GET.
{% endalert %}

## Exemple de requête {#example-request}

```json
{
    "content_block_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
    "locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
    "translation_map": {
        "id_3": "Ein Absatz ohne Formatierung"
    }
}
```

## Réponse {#response}

Il existe quatre codes de statut de réponse pour cet endpoint : `200`, `400`, `404` et `429`.

### Exemple de réponse réussie {#example-success-response}

```json
{
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