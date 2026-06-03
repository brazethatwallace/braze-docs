---
nav_title: "GET : Lister les détails d'un élément du catalogue"
article_title: "GET : Lister les détails d'un élément du catalogue"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Lister les détails d'un élément du catalogue."

---
{% api %}
# Lister les détails d'un élément du catalogue {#list-catalog-item-details}
{% apimethod get %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> Utilisez cet endpoint pour renvoyer un élément de catalogue et son contenu.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#52c6631c-7366-48e5-9e0e-16de7b6285cc {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l'autorisation `catalogs.get_item`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## Paramètres de chemin {#path-parameters}

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `catalog_name` | Requis | Chaîne de caractères | Nom du catalogue. |
| `item_id` | Requis | Chaîne de caractères | L'ID de l'élément du catalogue. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Path parameters" }

## Paramètres de requête {#request-parameters}

Cet endpoint n'a pas de corps de requête.

## Exemple de requête {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse {#response}

Deux codes de statut sont possibles pour cet endpoint : `200` et `404`.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `200` pourrait renvoyer le corps de réponse suivant.

```json
{
  "items": [
    {
      "id": "restaurant3",
      "Name": "Restaurant1",
      "City": "New York",
      "Cuisine": "American",
      "Rating": 5,
      "Loyalty_Program": true,
      "Open_Time": "2022-11-01T09:03:19.967Z"
    }
  ],
  "message": "success"
}
```

### Exemple de réponse en erreur {#example-error-response}

Le code de statut `404` pourrait renvoyer la réponse suivante. Consultez la section [Résolution des problèmes](#troubleshooting) pour plus d'informations concernant les erreurs que vous pourriez rencontrer.

```json
{
  "errors": [
    {
      "id": "item-not-found",
      "message": "Could not find item",
      "parameters": [
        "item_id"
      ],
      "parameter_values": [
        "restaurant34"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## Résolution des problèmes {#troubleshooting}

Le tableau suivant répertorie les erreurs possibles et les étapes de résolution associées, le cas échéant.

| Erreur | Résolution des problèmes |
| --- | --- |
| `catalog-not-found` | Vérifiez que le nom du catalogue est valide. |
| `item-not-found` | Vérifiez que l'élément est bien présent dans le catalogue. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

{% endapi %}