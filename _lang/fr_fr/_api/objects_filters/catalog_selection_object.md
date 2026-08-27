---
nav_title: "Objet de sélection du catalogue"
article_title: Objet de sélection du catalogue API
page_order: 12
page_type: reference
description: "Cet article de référence décrit les différents composants de l'objet de sélection du catalogue."
tool: Catalogs

---

# Objet de sélection du catalogue {#catalog-selection-object}

> Lors de la création d'une sélection de catalogue, vous pouvez fournir un objet de sélection afin de définir les critères de filtrage, de tri et de limitation pour les éléments renvoyés par votre catalogue.

L'objet `selection` vous permet de spécifier quels éléments de votre catalogue doivent être inclus dans la sélection en fonction de filtres, comment ils doivent être triés et combien de résultats renvoyer. Utilisez cet objet lors de la création de sélections de catalogue via l'API.

## Corps de l'objet {#object-body}

```json
{
  "selection": {
    "name": "Sale",
    "description": "Sales Collection",
    "external_id": "12345678",
    "source": "Shopify",
    "filters": [
      {
        "field": "collection",
        "operator": "includes value",
        "value": "Best Seller"
      },
      {
        "field": "collection",
        "operator": "does not include value",
        "value": "Sale"
      }
    ],
    "results_limit": 5,
    "sort_field": "id",
    "sort_order": "asc"
  }
}
```

## Détails de l'objet {#object-details}

| Clé | Obligatoire | Type de données | Description |
| --- | ----------- | --------------- | ----------- |
| `name` | Obligatoire | String | Le nom de la sélection de catalogue. |
| `description` | Facultatif | String | Une description de la sélection de catalogue. |
| `external_id` | Facultatif | String | Un identifiant unique pour la sélection. |
| `source` | Facultatif | String | La source des données du catalogue. Pour les catalogues Shopify, définissez cette valeur sur `"Shopify"`. Les valeurs acceptées sont `"Shopify"` et `"Braze"`. |
| `filters` | Obligatoire | Tableau d'objets | Un tableau d'objets de filtre à appliquer aux éléments du catalogue. Vous pouvez spécifier jusqu'à dix filtres par requête. Si un tableau de filtres vide est fourni, tous les éléments du catalogue sont inclus. |
| `results_limit` | Obligatoire | Entier | Le nombre maximum de résultats à renvoyer. Doit être un nombre compris entre 1 et 50. |
| `sort_field` | Facultatif | String | Le champ selon lequel trier les résultats. Ce paramètre doit être associé à `sort_order`. Si `sort_field` et `sort_order` ne sont pas présents, les résultats sont renvoyés dans un ordre aléatoire. |
| `sort_order` | Facultatif | String | L'ordre de tri des résultats. Les valeurs acceptées sont `"asc"` (croissant) ou `"desc"` (décroissant). Ce paramètre doit être associé à `sort_field`. Si `sort_field` et `sort_order` ne sont pas présents, les résultats sont renvoyés dans un ordre aléatoire. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Détails de l'objet" }

### Objet filtre {#filter-object}

Chaque objet filtre dans le tableau `filters` contient les champs décrits dans le tableau suivant.

| Clé | Obligatoire | Type de données | Description |
| --- | ----------- | --------------- | ----------- |
| `field` | Obligatoire | String | Le champ du catalogue sur lequel filtrer. |
| `operator` | Obligatoire | String | L'opérateur de comparaison à utiliser pour le filtrage. Les exemples incluent `"includes value"` et `"does not include value"`. |
| `value` | Obligatoire | Variable (string, nombre, booléen, heure) | La valeur à comparer. Elle doit correspondre au type de données du champ de catalogue sous-jacent (par exemple, string, nombre, booléen, heure). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Objet filtre" }

{% alert note %}
L'API prend en charge un maximum de dix filtres par requête de sélection. Les filtres sont appliqués dans l'ordre où ils apparaissent dans le tableau.
{% endalert %}