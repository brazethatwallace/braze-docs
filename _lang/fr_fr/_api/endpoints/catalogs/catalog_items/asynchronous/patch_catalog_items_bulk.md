---
nav_title: "PATCH : modifier plusieurs produits du catalogue"
article_title: "PATCH : modifier plusieurs produits du catalogue"
alias: /catalogs_items_patch/
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Modifier plusieurs produits du catalogue."

---
{% api %}
# Modifier plusieurs produits du catalogue {#edit-multiple-catalog-items}
{% apimethod patch %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Utilisez cet endpoint pour modifier plusieurs éléments existants dans votre catalogue.

Chaque requête peut prendre en charge jusqu'à 50 éléments. Cet endpoint est asynchrone.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#03f3548e-4139-4f60-812d-7e1a695a738a {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key) avec l'autorisation `catalogs.update_items`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## Paramètres de chemin {#path-parameters}

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `catalog_name` | Requis | Chaîne de caractères | Nom du catalogue. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de chemin" }

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `items` | Requis | Tableau | Un tableau contenant des objets d'éléments. Les objets d'éléments doivent contenir des champs qui existent dans le catalogue. Jusqu'à 50 objets d'éléments sont autorisés par requête. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}

```
curl --location --request PATCH 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "id": "restaurant1",
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
    },
    {
      "id": "restaurant3",
      "City": "San Francisco",
      "Rating": 2,
      "Top_Dishes": [
        "Buffalo Wings",
        "Philly Cheesesteak"
      ]
    }
  ]
}'
```

{% alert note %}
- Le champ `Location` utilise le type de données `geo`, qui attend un tableau au format `[longitude, latitude]`.
- Les opérateurs `$add` et `$remove` ne s'appliquent qu'aux champs de type tableau et ne sont pris en charge que par les endpoints PATCH.
{% endalert %}

## Réponse {#response}

Trois codes de statut de réponse existent pour cet endpoint : `202`, `400` et `404`.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `202` pourrait renvoyer le corps de réponse suivant.

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

Le tableau suivant répertorie les erreurs renvoyées possibles et les étapes de résolution des problèmes associées.

| Erreur | Résolution des problèmes |
| --- | --- |
| `catalog-not-found` | Vérifiez que le nom du catalogue est valide. |
| `ids-too-large` | Les ID d'éléments ne peuvent pas contenir plus de 250 caractères. |
| `ids-not-strings` | Les ID d'éléments doivent être de type chaîne de caractères. |
| `ids-not-unique` | Les ID d'éléments doivent être uniques au sein de la requête. |
| `invalid-ids` | Les ID d'éléments peuvent uniquement inclure des lettres, des chiffres, des traits d'union et des traits de soulignement. |
| `invalid-fields` | Confirmez que tous les champs que vous envoyez dans la requête API existent déjà dans le catalogue. Cela n'a rien à voir avec le champ ID mentionné dans l'erreur. |
| `invalid-keys-in-value-object` | Les clés d'objet d'élément ne peuvent pas inclure `.` ou `$`. |
| `items-missing-ids` | Certains éléments n'ont pas d'ID. Vérifiez que chaque élément possède un ID d'élément. |
| `item-array-invalid` | `items` doit être un tableau d'objets. |
| `items-too-large` | Les valeurs d'éléments ne peuvent pas dépasser 5 000 caractères. |
| `request-includes-too-many-items` | Votre requête contient trop d'éléments. La limite d'éléments par requête est de 50. |
| `too-deep-nesting-in-value-object` | Les objets d'éléments ne peuvent pas avoir plus de 50 niveaux d'imbrication. |
| `unable-to-coerce-value` | Les types d'éléments ne peuvent pas être convertis. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Résolution des problèmes" }

{% endapi %}