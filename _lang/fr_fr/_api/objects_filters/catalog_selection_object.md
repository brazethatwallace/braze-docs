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

| Clé | Requis | Type de données | Description |
| --- | -------- | --------- | ----------- |
| `name` | Requis | Chaîne de caractères | Le nom de la sélection du catalogue. |
| `description` | Facultatif | Chaîne de caractères | Une description de la sélection du catalogue. |
| `external_id` | Requis | Chaîne de caractères | Un identifiant unique pour la sélection. |
| `source` | Facultatif | Chaîne de caractères | La source des données du catalogue. Pour les catalogues Shopify, définissez cette valeur sur `"Shopify"`. Les valeurs acceptées sont `"Shopify"` et `"Braze"`. |
| `filters` | Facultatif | Tableau d'objets | Un ensemble d'objets filtres à appliquer aux éléments du catalogue. Vous pouvez spécifier jusqu'à quatre filtres par requête. Si aucun filtre n'est fourni, tous les éléments du catalogue sont inclus. |
| `results_limit` | Facultatif | Nombre entier | Le nombre maximal de résultats à renvoyer. Il doit s'agir d'un nombre compris entre 1 et 50. |
| `sort_field` | Facultatif | Chaîne de caractères | Le champ selon lequel trier les résultats. Ce paramètre doit être associé à `sort_order`. Si ni `sort_field` ni `sort_order` ne sont présents, les résultats sont renvoyés dans un ordre aléatoire. |
| `sort_order` | Facultatif | Chaîne de caractères | L'ordre de tri des résultats. Les valeurs acceptées sont `"asc"` (ascendant) ou `"desc"` (descendant). Ce paramètre doit être associé à `sort_field`. Si ni `sort_field` ni `sort_order` ne sont présents, les résultats sont renvoyés dans un ordre aléatoire. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Object details" }

### Objet filtre {#filter-object}

Chaque objet filtre du tableau `filters` contient les champs décrits dans le tableau suivant.

| Clé | Requis | Type de données                                   | Description |
| --- | -------- | ------------------------------------------- | ----------- |
| `field`    | Requis | Chaîne de caractères                                      | Le champ du catalogue sur lequel appliquer le filtre. |
| `operator` | Requis | Chaîne de caractères                                      | L'opérateur de comparaison à utiliser pour le filtrage. Par exemple, `"includes value"` et `"does not include value"`. |
| `value`    | Requis | Variable (chaîne de caractères, nombre, valeur booléenne, heure)     | La valeur à comparer. Elle doit correspondre au type de données du champ du catalogue sous-jacent (par exemple, chaîne de caractères, nombre, valeur booléenne, heure). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Filter object" }

{% alert note %}
L'API prend en charge un maximum de quatre filtres par requête de sélection. Dans le tableau de bord de Braze, vous pouvez ajouter jusqu'à 10 filtres par sélection. Les filtres sont appliqués dans l'ordre dans lequel ils apparaissent dans le tableau.
{% endalert %}