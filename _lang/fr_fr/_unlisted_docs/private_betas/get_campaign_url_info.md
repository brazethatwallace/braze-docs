---
nav_title: "GET : Lister les alias de lien pour les Campaigns"
layout: api_page
page_type: reference
hidden: true
permalink: /get_campaign_link_alias/

platform: API
channel:
  - Email
tool:
  - Canvas
  - Campaigns

description: "Cet article décrit en détail l'endpoint Braze permettant de lister les alias de lien."
---
{% api %}
# Lister les alias de lien pour une Campaign {#list-link-alias-for-campaign}
{% apimethod get %}
/campaigns/url_info/details
{% endapimethod %}

> Utilisez cet endpoint pour lister les alias de lien définis dans une variante de message spécifique d'une Campaign.

{% apiref postman %}  {% endapiref %}

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `campaign_id` | Requis | Chaîne de caractères | Voir [identifiant API de Campaign](https://www.braze.com/docs/api/identifier_types/#campaign-api-identifier). |
| `message_variation_id` | Requis | Chaîne de caractères | Identifiant API de la variante de message. Vous pouvez le trouver sur la page de détails de la Campaign, dans la section **Identifiant API**. |
| `includes_link_id` | Facultatif | Chaîne de caractères | Un identifiant de lien spécifique (tel qu'attribué par Braze) ou `null`. Ce paramètre permet de filtrer les résultats par un `link_id` spécifique. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Exemple de requête {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/campaigns/url_info/details?campaign_id=4615a404-b2c2-421e-9a04-2233bb3ec4f9&message_variation_id=0ea708fe-36b4-43f7-9f5c-a0650ea2a7a0&includes_link_id=014tk4e0kg97' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Réponse {#response}

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "channel": "email",
  "name": "Variant 1",
  "link_data": [
    {
      "link_URL": "https://www.braze.com?lid=014tk4e0kg97",
      "link_id": "014tk4e0kg97",
      "content_block_path_info": [],
      "link_alias": "link5"
    }
  ],
  "message": "success"
}
```

### Résolution des problèmes {#troubleshooting}

Le tableau suivant répertorie les erreurs possibles renvoyées et les étapes de résolution associées.

| Erreur | Résolution des problèmes |
| --- | --- |
| `Missing/Invalid Campaign ID` | L'ID API de la Campaign doit être un identifiant API. Vous pouvez le trouver en utilisant l'[endpoint Exporter la liste des Campaigns](https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaigns/) ou en vous connectant au tableau de bord. |
| `Missing/Invalid Message Variant ID` | L'ID API de la variante de message doit être un identifiant API. Vous pouvez le trouver en utilisant l'[endpoint Exporter les détails d'une Campaign](https://www.braze.com/docs/api/endpoints/export/campaigns/get_campaign_details/) ou en vous connectant au tableau de bord. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endapi %}