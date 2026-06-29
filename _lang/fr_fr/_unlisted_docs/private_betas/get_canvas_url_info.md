---
nav_title: "GET : Lister les alias de lien pour un Canvas"
layout: api_page
page_type: reference
hidden: true
permalink: /get_canvas_link_alias/

platform: API
channel:
  - Email
tool:
  - Canvas
  - Campaigns

description: "Cet article présente les détails de l'endpoint permettant de lister les alias de lien pour un Canvas."
---
{% api %}
# Lister les alias de lien pour un Canvas {#list-link-alias-for-canvas}
{% apimethod get %}
/canvas/url_info/details
{% endapimethod %}

> Utilisez cet endpoint pour lister les alias de lien définis dans une étape e-mail spécifique d'un Canvas.

{% apiref postman %}  {% endapiref %}

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `canvas_step_id` | Requis | Chaîne de caractères | Voir [Identifiant API de l'étape du Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier). |
| `message_variation_id ` | Requis | Chaîne de caractères | Identifiant API de la variante de message (pour la variante de message e-mail dans cette étape). Vous pouvez le trouver en cliquant sur **Analyser les variantes** sur la page **Détails du Canvas**. |
| `includes_link_id` | Facultatif | Chaîne de caractères | Un identifiant de lien spécifique (tel qu'attribué par Braze) ou `null`. Permet de filtrer les résultats par un `link_id` spécifique. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Exemple de requête {#example-request}

```
curl --location --request GET 'https://rest.iad-01.braze.com/canvas/url_info/details?campaign_id=4615a404-b2c2-421e-9a04-2233bb3ec4f9&message_variation_id=0ea708fe-36b4-43f7-9f5c-a0650ea2a7a0&includes_link_id=014tk4e0kg97' \
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

Le tableau suivant répertorie les erreurs possibles et les étapes de résolution associées.

| Erreur | Résolution des problèmes |
| --- | --- |
| `Missing/Invalid Canvas ID` | L'ID API du Canvas doit être un identifiant API. Vous pouvez le trouver en utilisant l'[endpoint Exporter la liste des Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) ou en vous connectant au tableau de bord. |
| `Missing/Invalid Message Variant ID` | L'ID API de la variante de message doit être un identifiant API. Vous pouvez le trouver en utilisant l'[endpoint Exporter les détails du Canvas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) ou en vous connectant au tableau de bord. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}