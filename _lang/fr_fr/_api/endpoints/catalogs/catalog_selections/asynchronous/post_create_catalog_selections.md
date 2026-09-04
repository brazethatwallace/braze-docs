---
nav_title: "POST : Créer une sélection dans le catalogue"
article_title: "POST : Créer une sélection dans le catalogue"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Braze Créer une sélection de catalogue."

---
{% api %}
# Créer une sélection dans le catalogue {#create-catalog-selection}
{% apimethod post %}
/catalogs/{catalog_name}/selections
{% endapimethod %}

> Utilisez cet endpoint pour créer une sélection dans votre catalogue.

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec l'autorisation `catalogs.create_selection`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog selections' %}

## Paramètres de chemin {#path-parameters}

| Paramètre      | Requis | Type de données | Description          |
| -------------- | -------- | --------- | -------------------- |
| `catalog_name` | Requis | Chaîne de caractères    | Nom du catalogue. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Paramètres de requête {#request-parameters}

| Paramètre   | Requis | Type de données | Description                                                                                                                                                        |
| ----------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `selection` | Requis | Objet    | Un objet contenant les critères de sélection. Consultez l'[objet de sélection de catalogue]({{site.baseurl}}/api/objects_filters/catalog_selection_object) pour une description complète de l'objet et de ses champs. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Paramètres de l'objet de sélection {#selection-object-parameters}

| Paramètre        | Requis | Type de données | Description                                                                                                                                                        |
| ---------------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `name`           | Requis | Chaîne de caractères    | Le nom de la sélection du catalogue. |
| `description`    | Facultatif | Chaîne de caractères    | Une description de la sélection du catalogue. |
| `external_id`    | Facultatif | Chaîne de caractères    | Un identifiant unique pour la sélection. |
| `source`         | Facultatif | Chaîne de caractères    | La source des données du catalogue. Pour les catalogues Shopify, définissez cette valeur sur `"Shopify"`. Les valeurs acceptées sont `"Shopify"` et `"Braze"`. |
| `filters`        | Requis | Tableau    | Un tableau d'objets filtres à appliquer aux éléments du catalogue. Vous pouvez spécifier jusqu'à dix filtres par requête. Si un tableau de filtres vide est fourni, tous les éléments du catalogue sont inclus. |
| `results_limit`  | Requis | Nombre entier   | Le nombre maximal de résultats à renvoyer. Ce nombre doit être compris entre 1 et 50. |
| `sort_field`     | Facultatif | Chaîne de caractères    | Le champ selon lequel trier les résultats. Ce paramètre doit être associé à `sort_order`. Si `sort_field` et `sort_order` ne sont pas présents, les résultats sont renvoyés dans un ordre aléatoire. |
| `sort_order`     | Facultatif | Chaîne de caractères    | L'ordre de tri des résultats. Les valeurs acceptées sont `"asc"` (ascendant) ou `"desc"` (descendant). Ce paramètre doit être associé à `sort_field`. Si `sort_field` et `sort_order` ne sont pas présents, les résultats sont renvoyés dans un ordre aléatoire. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
Les paramètres `sort_field` et `sort_order` doivent être utilisés conjointement. Si vous fournissez l'un sans l'autre, ou si vous omettez les deux paramètres, les résultats de la sélection sont renvoyés dans un ordre aléatoire.
{% endalert %}

## Exemple de requête {#example-request}

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/selections' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "selection": {
    "name": "favorite-restaurants",
    "description": "Favorite restaurants in NYC",
    "external_id": "favorite-nyc-restaurants",
    "source": "Braze",
    "filters": [
      {
        "field": "City",
        "operator": "equals",
        "value": "NYC"
      },
      {
        "field": "Rating",
        "operator": "greater than",
        "value": 7
      }
    ],
    "results_limit": 10,
    "sort_field": "Rating",
    "sort_order": "desc"
  }
}'
```

### Opérateurs de filtrage {#filter-operators}

| Type de champ | Opérateurs pris en charge                                     |
| ---------- | ------------------------------------------------------- |
| `string`   | `equals`, `does not equal`                              |
| `number`   | `equals`, `does not equal`, `greater than`, `less than` |
| `boolean`  | `is`                                                    |
| `time`     | `before`, `after`                                       |
| `array`    | `includes value`, `does not include value`              |
| `geo`      | `geo within`, `geo outside`                             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
L'API prend en charge un maximum de dix filtres par requête de sélection. Les filtres sont appliqués dans l'ordre dans lequel ils apparaissent dans le tableau.
{% endalert %}

{% alert note %}
Lorsque vous appliquez un filtre `geo`, le système trie automatiquement les résultats par distance, l'élément le plus proche apparaissant en premier, indépendamment des paramètres `sort_field` et `sort_order`.
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

Le code de statut `400` pourrait renvoyer le corps de réponse suivant. Consultez la section [Résolution des problèmes](#troubleshooting) pour plus d'informations sur les erreurs que vous pourriez rencontrer.

```json
{
  "errors": [
    {
      "id": "catalog-not-found",
      "message": "Could not find catalog",
      "parameters": [
        "catalog_name"
      ],
      "parameter_values": [
        "restaurants"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## Résolution des problèmes {#troubleshooting}

Le tableau suivant répertorie les erreurs possibles et les étapes de résolution associées.

| Erreur                                | Résolution                                                                               |
|--------------------------------------|-----------------------------------------------------------------------------------------------|
| `catalog-not-found`                  | Vérifiez que le nom du catalogue est valide.                                                         |
| `company-size-limit-already-reached` | La limite de taille de stockage du catalogue est atteinte.                                                    |
| `selection-limit-reached`            | La limite de sélections du catalogue est atteinte.                                                      |
| `invalid-selection`                  | Vérifiez que la sélection est valide.                                                            |
| `too-many-filters`                   | Vérifiez si la sélection comporte trop de filtres.                                                  |
| `selection-name-already-exists`      | Vérifiez si le nom de la sélection existe déjà dans le catalogue.                                    |
| `selection-has-invalid-filter`       | Vérifiez que le filtre de sélection est valide.                                                       |
| `selection-invalid-results-limit`    | Vérifiez que la limite de résultats de la sélection est valide.                                                |
| `invalid-sorting`                    | Vérifiez que le tri de la sélection est valide.                                                      |
| `invalid-sort-field`                 | Vérifiez que le champ de tri de la sélection est valide.                                                   |
| `invalid-sort-order`                 | Vérifiez que l'ordre de tri de la sélection est valide.                                                   |
| `selection-contains-too-many-arrays` | Vérifiez si la sélection contient plus d'un champ de type `array`. Un seul est pris en charge. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}