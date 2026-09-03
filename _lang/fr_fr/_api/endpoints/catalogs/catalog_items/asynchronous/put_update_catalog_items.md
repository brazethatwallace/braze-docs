---
nav_title: "PUT : Remplacer plusieurs éléments du catalogue"
article_title: "PUT : Remplacer plusieurs éléments du catalogue"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Braze Remplacer plusieurs éléments du catalogue."

---
{% api %}
# Remplacer des éléments du catalogue {#replace-catalog-items}
{% apimethod put %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Utilisez cet endpoint pour remplacer plusieurs éléments dans votre catalogue.

Si un élément du catalogue n'existe pas, cet endpoint créera l'élément dans votre catalogue. Chaque requête peut prendre en charge jusqu'à 50 éléments de catalogue. Cet endpoint est asynchrone.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#ab30a4fc-60bc-4460-885c-1b92af8bc061 {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec l'autorisation `catalogs.replace_items`.

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
| `items` | Requis | Tableau | Un tableau contenant des objets d'éléments. Chaque objet doit avoir un ID. Les objets d'éléments doivent contenir des champs qui existent dans le catalogue. Jusqu'à 50 objets d'éléments sont autorisés par requête. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}

```
curl --location --request PUT 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
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
      "Top_Dishes": [
        "Hamburger",
        "Deluxe Cheeseburger"
      ],
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    },
    {
      "id": "restaurant3",
      "City": "San Francisco",
      "Rating": 2,
      "Top_Dishes": [
        "Hot Dog",
        "French Fries"
      ]
    }
  ]
}'
```

{% alert note %}
Le champ `Location` utilise le type de données `geo`, qui attend un tableau au format `[longitude, latitude]`.
{% endalert %}

## Réponse {#response}

Trois codes de statut de réponse existent pour cet endpoint : `202`, `400` et `404`.

{% alert note %}
Le système peut également renvoyer une réponse `400` si votre entreprise a atteint sa limite de stockage de catalogue. La version gratuite des catalogues est plafonnée à 500&nbsp;Mo. Pour plus d'informations sur les niveaux de stockage et comment effectuer une mise à niveau, consultez [Limitations du stockage de données]({{site.baseurl}}/user_guide/data/activation/catalogs#data-storage-limitations).
{% endalert %}

### Exemple de réponse réussie {#example-success-response}

Le code de statut `202` pourrait renvoyer le corps de réponse suivant.

```json
{
  "message": "success"
}
```

### Exemple de réponse échouée {#example-error-response}

Le code de statut `400` pourrait renvoyer le corps de réponse suivant. Consultez la section [Résolution des problèmes](#troubleshooting) pour plus d'informations concernant les erreurs que vous pourriez rencontrer.

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
| `catalog-not-found` | Vérifiez que le nom du catalogue est valide. |
| `company-size-limit-already-reached` | La limite de stockage du catalogue est atteinte. Pour en savoir plus sur les niveaux de stockage, consultez [Limitations du stockage de données]({{site.baseurl}}/user_guide/data/activation/catalogs#data-storage-limitations). |
| `company-size-limit-surge` | La requête dépasse la capacité de stockage restante de votre entreprise pour les catalogues. Réessayez avec une mise à jour plus petite. Pour en savoir plus sur les niveaux de stockage, consultez [Limitations du stockage de données]({{site.baseurl}}/user_guide/data/activation/catalogs#data-storage-limitations). |
| `ids-not-string` | Confirmez que chaque ID d'élément est une chaîne de caractères. |
| `ids-not-unique` | Vérifiez que chaque ID d'élément est unique. |
| `ids-too-large` | La limite de caractères pour chaque ID d'élément est de 250 caractères. |
| `item-array-invalid` | `items` doit être un tableau d'objets. |
| `items-missing-ids` | Certains éléments n'ont pas d'ID. Confirmez que chaque élément possède un ID. |
| `items-too-large` | Les valeurs des éléments ne peuvent pas dépasser 5 000 caractères. |
| `invalid-ids` | Les caractères pris en charge pour les noms d'ID d'éléments sont les lettres, les chiffres, les tirets et les traits de soulignement. |
| `invalid-fields` | Confirmez que tous les champs que vous envoyez dans la requête API existent déjà dans le catalogue. Cela n'a rien à voir avec le champ ID mentionné dans l'erreur. |
| `invalid-keys-in-value-object` | Les clés d'objet d'élément ne peuvent pas inclure `.` ou `$`. |
| `too-deep-nesting-in-value-object` | Les objets d'éléments ne peuvent pas avoir plus de 50 niveaux d'imbrication. |
| `request-includes-too-many-items` | Votre requête contient trop d'éléments. La limite d'éléments par requête est de 50. |
| `unable-to-coerce-value` | Les types d'éléments ne peuvent pas être convertis. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Résolution des problèmes" }

{% endapi %}