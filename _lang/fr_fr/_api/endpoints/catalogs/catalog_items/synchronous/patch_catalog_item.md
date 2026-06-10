---
nav_title: "PATCH : Modifier un élément du catalogue"
article_title: "PATCH : Modifier un élément du catalogue"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Modifier un élément du catalogue."

---
{% api %}
# Modifier un élément du catalogue {#edit-catalog-item}
{% apimethod patch %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> Utilisez cet endpoint pour modifier un élément existant dans votre catalogue.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e35976ae-ff77-42b7-b691-a883c980d8c0 {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l'autorisation `catalogs.update_item`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## Paramètres de chemin {#path-parameters}

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `catalog_name` | Requis | Chaîne de caractères | Nom du catalogue. |
| `item_id` | Requis | Chaîne de caractères | L'ID de l'élément du catalogue. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Path parameters" }

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `items` | Requis | Tableau | Un tableau contenant des objets d'éléments. Les objets d'éléments doivent contenir les champs qui existent dans le catalogue, à l'exception du champ `id`. Un seul objet d'élément est autorisé par requête. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Request parameters" }

## Exemple de requête {#example-request}

```
curl --location --request PATCH 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Location": [-73.988103, 40.779109],
      "Preferences": {
        "favorite_brand": "Nike",
        "shirt_size": "L"
      },
      "Top_Dishes": {
        "$add": [
          "Biscuits",
          "Coleslaw"
        ],
        "$remove": [
          "French Fries"
        ]
      },
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    }
  ]
}'
```

{% alert note %}
- Le champ `Location` utilise le type de données `geo`, qui attend un tableau au format `[longitude, latitude]`.
- Les opérateurs `$add` et `$remove` ne s'appliquent qu'aux champs de type tableau et ne sont pris en charge que par les endpoints PATCH.
{% endalert %}

## Réponse {#response}

Trois codes de statut de réponse existent pour cet endpoint : `200`, `400` et `404`.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `200` pourrait renvoyer le corps de réponse suivant.

```json
{
  "message": "success"
}
```

### Exemple de réponse échouée {#example-error-response}

Le code de statut `400` pourrait renvoyer le corps de réponse suivant. Consultez la [résolution des problèmes](#troubleshooting) pour plus d'informations concernant les erreurs que vous pourriez rencontrer.

```json
{
  "errors": [
    {
      "id": "invalid-fields",
      "message": "Some of the fields given do not exist in the catalog",
      "parameters": [
        "id"
      ],
      "parameter_values": [
        "restaurant1"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## Résolution des problèmes {#troubleshooting}

Le tableau suivant répertorie les erreurs possibles et les étapes de résolution associées.

| Erreur | Résolution des problèmes |
| --- | --- |
| `arbitrary-error` | Une erreur arbitraire est survenue. Veuillez réessayer ou contacter l'[assistance]({{site.baseurl}}/support_contact/). |
| `catalog-not-found` | Vérifiez que le nom du catalogue est valide. |
| `filtered-set-field-too-long` | La valeur du champ est utilisée dans un ensemble filtré qui dépasse la limite de caractères pour un élément. |
| `id-in-body` | Un ID d'élément existe déjà dans le catalogue. |
| `ids-too-large` | La limite de caractères pour chaque ID d'élément est de 250 caractères. |
| `invalid-ids` | Les caractères pris en charge pour les noms d'ID d'éléments sont les lettres, les chiffres, les tirets et les traits de soulignement. |
| `invalid-fields` | Confirmez que les champs de la requête existent dans le catalogue. |
| `invalid-keys-in-value-object` | Les clés d'objet d'élément ne peuvent pas contenir `.` ou `$`. |
| `item-not-found` | Vérifiez que l'élément est dans le catalogue. |
| `item-array-invalid` | `items` doit être un tableau d'objets. |
| `items-too-large` | La limite de caractères pour chaque élément est de 5 000 caractères. |
| `request-includes-too-many-items` | Vous ne pouvez modifier qu'un seul élément de catalogue par requête. |
| `too-deep-nesting-in-value-object` | Les objets d'éléments ne peuvent pas avoir plus de 50 niveaux d'imbrication. |
| `unable-to-coerce-value` | Les types d'éléments ne peuvent pas être convertis. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

{% endapi %}