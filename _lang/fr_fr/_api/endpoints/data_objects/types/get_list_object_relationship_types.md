---
nav_title: "GET : Lister les types de relations d'objets"
article_title: "GET : Lister les types de relations d'objets"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article décrit en détail l'endpoint permettant de lister les types de relations d'objets."
---
{% api %}
# Lister les types de relations d'objets {#list-object-relationship-types}
{% apimethod get %}
/data_objects/types/{type_name}/object_relationship_types
{% endapimethod %}

> Utilisez cet endpoint pour lister les types de relations disponibles pour les liens objet-à-objet selon une direction d'ancrage donnée.

{% alert important %}
Les objets de données sont actuellement en accès anticipé. Votre espace de travail doit être activé avant que les permissions de clé API pour les objets de données n'apparaissent dans **Paramètres** > **Clés API**.
{% endalert %}

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous avez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec la permission `data_objects.read`.

## Limite de débit {#rate-limit}

Cet endpoint fait partie du compartiment de lecture des objets de données, avec une limite par défaut de 50 requêtes par minute.

## Paramètres de chemin {#path-parameters}

Le tableau suivant répertorie et décrit les paramètres de chemin pour l'endpoint `/data_objects/types/{type_name}/object_relationship_types`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `type_name` | Obligatoire | String | Nom machine du type d'objet de données |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de chemin pour lister les types de relations d'objets" }

## Paramètres de requête {#query-parameters}

Le tableau suivant répertorie et décrit les paramètres de requête pour l'endpoint `/data_objects/types/{type_name}/object_relationship_types`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `anchor` | Facultatif | String | `source` (par défaut) ou `target` |
| `limit` | Facultatif | Integer | Taille de la page. Par défaut `100`. Limité de `1` à `250` |
| `offset` | Facultatif | Integer | Décalage. Par défaut `0`. Les valeurs négatives sont ramenées à `0` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête pour lister les types de relations d'objets" }

## Exemple de requête {#example-request}

Cette section comprend un exemple de payload et un exemple de requête cURL.

### Exemple de payload de requête {#sample-request-payload}

Utilisez cet objet JSON comme référence pour les paramètres de requête.

```json
{
  "type_name": "account",
  "anchor": "source",
  "limit": 10,
  "offset": 0
}
```

### Exemple de requête cURL {#sample-curl-request}

Cet exemple liste les types de relations d'objets disponibles pour le type `account` lorsque `account` est la source de la relation.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/types/account/object_relationship_types?anchor=source&limit=10&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Réponse {#response}

Cette section comprend un exemple de réponse réussie et les champs de la réponse.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `200` pourrait renvoyer le corps de réponse suivant.

```json
{
  "items": [
    {
      "from_type_name": "account",
      "to_type_name": "account",
      "rel_kind": "subaccount",
      "display_name": "subaccount",
      "related_type_name": "account"
    }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 10
}
```

`related_type_name` est le type situé de l'autre côté de la relation pour l'ancrage (`anchor`) sélectionné.

### Paramètres de réponse {#response-parameters}

Le tableau suivant répertorie et décrit les champs d'une réponse réussie.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `items` | Obligatoire | Array | Liste des types de relations d'objets disponibles |
| `items[].from_type_name` | Obligatoire | String | Nom du type d'objet de données source |
| `items[].to_type_name` | Obligatoire | String | Nom du type d'objet de données cible |
| `items[].rel_kind` | Obligatoire | String | Valeur du type de relation |
| `items[].display_name` | Obligatoire | String | Libellé d'affichage du type de relation |
| `items[].related_type_name` | Obligatoire | String | Type du côté opposé pour l'ancrage (`anchor`) demandé |
| `total_count` | Obligatoire | Integer | Nombre total d'enregistrements correspondants |
| `has_more` | Obligatoire | Boolean | Indique si une page de résultats supplémentaire est disponible |
| `next_offset` | Facultatif | Integer | Décalage pour la page suivante lorsque `has_more` est `true` |
| `offset` | Obligatoire | Integer | Décalage de la page actuelle |
| `limit` | Obligatoire | Integer | Taille de page utilisée par la requête |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de réponse pour lister les types de relations d'objets" }

## Erreurs {#errors}

Le tableau suivant répertorie les erreurs courantes pour cet endpoint et explique comment les résoudre.

| Statut | Cause | Recommandation |
|---|---|---|
| `400` | Valeur `anchor` non valide | Utilisez `source` ou `target` pour `anchor`. |
| `404` | Type introuvable (`data-object-type-not-found`) | Vérifiez que `type_name` existe dans l'espace de travail et correspond exactement au nom machine. |
| `401` | Clé API REST manquante ou non valide | Vérifiez que l'en-tête `Authorization` utilise `Bearer YOUR_REST_API_KEY` et que la clé est active. |
| `403` | La clé API ne dispose pas de la permission ou la requête est bloquée par la liste d'autorisation | Vérifiez que la clé dispose de la permission `data_objects.read` et que votre adresse IP source figure dans la liste d'autorisation de la clé, si celle-ci est configurée. |
| `429` | Limite de débit dépassée | Réessayez après `X-RateLimit-Reset` et réduisez la fréquence des requêtes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erreurs pour lister les types de relations d'objets" }
{% endapi %}