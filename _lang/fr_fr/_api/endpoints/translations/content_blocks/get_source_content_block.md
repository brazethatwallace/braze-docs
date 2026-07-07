---
nav_title: "GET : Afficher les valeurs source par défaut des étiquettes de traduction d'un bloc de contenu"
article_title: "GET : Afficher les valeurs source par défaut des étiquettes de traduction d'un bloc de contenu"
search_tag: Endpoint
page_order: 0

layout: api_page
page_type: reference
description: "Cet article décrit en détail l'endpoint source de traduction des blocs de contenu."
---

{% api %}
# Afficher les valeurs source par défaut des étiquettes de traduction d'un bloc de contenu {#view-default-source-values-for-a-content-blocks-translation-tags}
{% apimethod get %}
/content_blocks/translations/source
{% endapimethod %}

> Utilisez cet endpoint pour afficher toutes les sources de traduction par défaut des étiquettes de traduction d'un bloc de contenu. Il s'agit des valeurs contenues dans {% raw %}`{% translation id %} source {% endtranslation %}`{% endraw %}. Consultez [Paramètres régionaux dans les messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) pour plus d'informations sur les fonctionnalités de traduction.

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key) avec la permission `content_blocks.translations.get`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Paramètres de requête {#query-parameters}

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `content_block_id` | Requis | Chaîne de caractères | L'ID de votre bloc de contenu. |
| `locale_id` | Facultatif | Chaîne de caractères | Un UUID de paramètre régional pour filtrer les réponses. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

{% alert note %}
Tous les ID de traduction sont considérés comme des identifiants universels uniques (UUID), qui peuvent être trouvés dans la réponse de l'endpoint GET.
{% endalert %}

## Exemple de requête {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/content_blocks/translations/source?content_block_id={content_block_id}&locale_id={locale_uuid}' \
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
           "id_0": "Welcome!",
           "id_1": "Thank you for joining our program"
       }
   },
   "message": "success"
}
```

### Exemple de réponse d'erreur {#example-error-response}

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