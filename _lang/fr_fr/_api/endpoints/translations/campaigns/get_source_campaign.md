---
nav_title: "GET : Afficher les valeurs sources par défaut pour les étiquettes de traduction de Campaign"
article_title: "GET : Afficher les valeurs sources par défaut pour les étiquettes de traduction de Campaign"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint source de traduction de Campaign."
---

{% api %}
# Afficher les valeurs sources par défaut pour les étiquettes de traduction d'une Campaign {#view-default-source-values-for-a-campaigns-translation-tags}
{% apimethod get %}
/campaigns/translations/source
{% endapimethod %}

> Utilisez cet endpoint pour afficher toutes les sources de traduction par défaut pour les étiquettes de traduction d'une Campaign. Il s'agit des valeurs contenues dans {% raw %}`{% translation id %} source {% endtranslation %}`{% endraw %}. Consultez [Locales dans les messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) pour plus d'informations sur les fonctionnalités de traduction.

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec l'autorisation `campaigns.translations.get`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Paramètres de requête {#query-parameters}

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Requis | Chaîne de caractères | L'ID de votre Campaign. |
| `message_variation_id` | Requis | Chaîne de caractères | L'ID de la variation de votre message. |
| `locale_id` | Facultatif | Chaîne de caractères | Un UUID de locale pour filtrer les réponses. |
| `post_launch_draft_version` | Facultatif | Booléen | Lorsque la valeur est `true`, renvoie la dernière version brouillon au lieu de la dernière version publiée en production. La valeur par défaut est `false`, ce qui renvoie la dernière version en production. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

{% alert note %}
Tous les ID de traduction sont considérés comme des identifiants uniques universels (UUID), qui peuvent être trouvés dans la réponse de l'endpoint GET.
{% endalert %}

## Exemple de requête {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/campaigns/translations/source?campaign_id={campaign_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse {#response}

Il existe quatre codes de statut de réponse pour cet endpoint : `200`, `400`, `404` et `429`.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `200` pourrait renvoyer l'en-tête et le corps de réponse suivants.

```json
{
   "translations": {
       "translation_map": {
           "id_0": "Here's a Million Dollars",
           "id_1": "Hello World!"
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
			"message": "This message does not support multi-language."
		}
	]
}
```

{% endapi %}