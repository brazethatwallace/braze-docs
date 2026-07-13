---
nav_title: "PUT : Mise à jour des traductions d'un modèle d'e-mail"
article_title: "PUT : Mise à jour des traductions d'un modèle d'e-mail"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Mise à jour des traductions d'un modèle d'e-mail."
---

{% api %}
# Mise à jour des traductions d'un modèle d'e-mail {#update-translations-for-an-email-template}
{% apimethod put %}
/templates/email/translations/
{% endapimethod %}

> Utilisez cet endpoint pour mettre à jour les traductions d'un [modèle d'e-mail]({{site.baseurl}}/user_guide/messaging/templates/email_templates). Consultez [Locales dans les messages]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) pour plus d'informations sur les fonctionnalités de traduction.

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key) avec l'autorisation `templates.translations.update`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Paramètres de chemin {#path-parameters}

Cet endpoint ne comporte pas de paramètres de chemin.

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `template_id` | Requis | Chaîne de caractères | L'ID de votre modèle d'e-mail. |
| `locale_id` | Requis | Chaîne de caractères | L'ID de la locale. |
| `translations_map` | Requis | Chaîne de caractères | Le mappage des traductions pour votre modèle d'e-mail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

{% alert note %}
Tous les ID de traduction sont considérés comme des identifiants uniques universels (UUID), qui peuvent être trouvés dans la réponse de l'endpoint GET.
{% endalert %}

## Exemple de requête {#example-request}

```json
{
    "template_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
    "locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
    "translation_map": {
        "id_0": "¡Hola!",
        "id_1": "Me llamo Jacky",
        "id_2": "¿Dónde está la biblioteca?"
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
			"id": "1234567-abc-123-012345678",
			"message": "The provided translations yielded errors when parsing. Please contact Braze for more information."
		}
	]
}
```

{% endapi %}