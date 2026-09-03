---
nav_title: "POST : Supprimer des campagnes planifiées déclenchées par API"
article_title: "POST : Supprimer des campagnes planifiées déclenchées par API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Supprimer des campagnes planifiées déclenchées par API."

---
{% api %}
# Supprimer des campagnes planifiées déclenchées par API {#delete-scheduled-api-triggered-campaigns}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/campaigns/trigger/schedule/delete
{% endapimethod %}

> Utilisez cet endpoint pour annuler un message de campagne que vous avez précédemment planifié via l'API avant qu'il ne soit envoyé.

Les messages planifiés ou les déclencheurs supprimés peu avant ou pendant leur heure d'envoi prévue sont mis à jour au mieux. Il est donc possible que Braze applique des suppressions de dernière seconde à la totalité, à une partie ou à aucun de vos utilisateurs ciblés.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7 {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec l'autorisation `campaigns.trigger.schedule.delete`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la requête {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) the campaign identifier,
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Requis | Chaîne de caractères | Voir [identifiant de campagne]({{site.baseurl}}/api/identifier_types). |
| `schedule_id` | Requis | Chaîne de caractères | Le `schedule_id` à supprimer (obtenu à partir de la réponse de création de planification). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête" }


## Exemple de requête {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}