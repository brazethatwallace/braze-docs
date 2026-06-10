---
nav_title: "GET : Voir toutes les traductions pour une campagne"
article_title: "GET : Voir toutes les traductions pour une campagne"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Voir toutes les traductions pour une campagne."
---

{% api %}
# Voir toutes les traductions pour une campagne {#view-all-translations-for-a-campaign}
{% apimethod get %}
/campaigns/translations
{% endapimethod %}

> Utilisez cet endpoint pour voir toutes les traductions de chaque variante de message dans une campagne. Consultez [Locales dans les messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) pour en savoir plus sur les fonctionnalités de traduction.

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l'autorisation `campaigns.translations.get`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Paramètres de requête {#query-parameters}

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Requis | Chaîne de caractères | L'ID de votre campagne. |
| `message_variation_id` | Requis | Chaîne de caractères | L'ID de votre variante de message. |
| `locale_id` | Facultatif | Chaîne de caractères | Un UUID de locale pour filtrer les réponses. |
| `post_launch_draft_version` | Facultatif | Valeur booléenne | Lorsque la valeur est `true`, renvoie la dernière version brouillon au lieu de la dernière version publiée en production. La valeur par défaut est `false`, ce qui renvoie la dernière version en production. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Query parameters" }

{% alert note %}
Tous les ID de traduction sont considérés comme des identifiants uniques universels (UUID), disponibles dans la réponse de l'endpoint GET.
{% endalert %}

## Exemple de requête {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/campaigns/translations?campaign_id={campaign_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
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
            "translation_map": {
                "id_0": "¡Hola!",
                "id_1": "Me llamo Jacky",
                "id_2": "¿Dónde está la biblioteca?"
            },
            "locale": {
                "uuid": "c7c12345-te35-1234-5678-abcdefa99r3f",
                "name": "es-MX",
                "country": "MX",
                "language": "es",
                "locale_key": "es-mx"
            }
        },
        {
            "translation_map": {
                "id_0": "你好",
                "id_1": "我的名字是 Jacky",
                "id_2": "圖書館在哪裡?"
            },
            "locale": {
                "uuid": "a1b12345-cd35-1234-5678-abcdefa99r3f",
                "name": "zh-HK",
                "country": "HK",
                "language": "zh",
                "locale_key": "zh-hk"
            }
        }
    ]
}
```

### Exemple de réponse en erreur {#example-error-response}

Le code de statut `400` pourrait renvoyer le corps de réponse suivant.

```json
{
	"errors": [
		{
			"message": "This message does not support multi-language."
		}
	]
}
```


{% endapi %}