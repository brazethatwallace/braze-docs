---
nav_title: "GET : Lister les relations d'objets"
article_title: "GET : Lister les relations d'objets"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Cet article décrit en détail l'endpoint Lister les relations d'objets."
---
{% api %}
# Lister les relations d'objets {#list-object-relationships}
{% apimethod get %}
/data_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> Utilisez cet endpoint pour lister les objets de données liés à partir d'un ancrage d'objet.

{% alert important %}
Les objets de données sont actuellement en accès anticipé. Votre espace de travail doit être activé avant que les permissions de clé API des objets de données n'apparaissent dans **Paramètres** > **Clés API**.
{% endalert %}

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec la permission `data_objects.read`.

## Limite de débit {#rate-limit}

Cet endpoint appartient au compartiment de lecture des objets de données, avec une limite par défaut de 50 requêtes par minute.

## Paramètres de chemin {#path-parameters}

Le tableau suivant répertorie et décrit les paramètres de chemin pour l'endpoint `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `type_name` | Obligatoire | String | Type de l'objet source |
| `external_id` | Obligatoire | String | Identifiant de l'objet source |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de chemin pour lister les relations d'objets" }

## Paramètres de requête {#query-parameters}

Le tableau suivant répertorie et décrit les paramètres de requête pour l'endpoint `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `anchor` | Facultatif | String | `source` (par défaut) ou `target` |
| `rel_kind` | Facultatif | String | Filtrer par un type de relation |
| `limit` | Facultatif | Integer | Taille de la page. Par défaut `100`. Limité de `1` à `250` |
| `offset` | Facultatif | Integer | Décalage. Par défaut `0`. Les valeurs négatives sont ramenées à `0` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête pour lister les relations d'objets" }

## Exemple de requête {#example-request}

Cette section comprend un exemple de payload et un exemple de requête cURL.

### Exemple de payload de requête {#sample-request-payload}

Utilisez cet objet JSON comme référence pour les paramètres de requête.

```json
{
  "type_name": "account",
  "external_id": "acct-123",
  "anchor": "source",
  "rel_kind": "subaccount",
  "limit": 100,
  "offset": 0
}
```

### Exemple de requête cURL {#sample-curl-request}

Cet exemple liste les enregistrements `subaccount` vers lesquels `acct-123` pointe, en renvoyant la première page de résultats.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships?anchor=source&rel_kind=subaccount&limit=100&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Réponse {#response}

Cette section comprend un exemple de réponse réussie et les champs de réponse.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `200` peut renvoyer le corps de réponse suivant.

```json
{
  "items": [
    {
      "rel_kind": "subaccount",
      "to_data_object": {
        "type_name": "account",
        "external_id": "acct-456",
        "attributes": { "name": "Child Account" }
      },
      "attributes": {}
    }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

Avec `anchor=target`, les objets liés sont renvoyés en tant que `from_data_object`.

### Paramètres de réponse {#response-parameters}

Le tableau suivant répertorie et décrit les champs d'une réponse réussie.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `items` | Obligatoire | Array | Liste des enregistrements de relations d'objets |
| `items[].rel_kind` | Obligatoire | String | Valeur du type de relation |
| `items[].to_data_object` | Conditionnel | Object | Objet lié lorsque `anchor=source` |
| `items[].from_data_object` | Conditionnel | Object | Objet lié lorsque `anchor=target` |
| `items[].to_data_object.type_name` | Conditionnel | String | Nom du type de l'objet lié |
| `items[].to_data_object.external_id` | Conditionnel | String | ID externe de l'objet lié |
| `items[].to_data_object.attributes` | Conditionnel | Object | Attributs de l'objet lié |
| `items[].from_data_object.type_name` | Conditionnel | String | Nom du type de l'objet lié |
| `items[].from_data_object.external_id` | Conditionnel | String | ID externe de l'objet lié |
| `items[].from_data_object.attributes` | Conditionnel | Object | Attributs de l'objet lié |
| `items[].attributes` | Obligatoire | Object | Attributs de la relation |
| `total_count` | Obligatoire | Integer | Nombre total d'enregistrements correspondants |
| `has_more` | Obligatoire | Boolean | Indique si une autre page de résultats est disponible |
| `next_offset` | Facultatif | Integer | Décalage pour la page suivante lorsque `has_more` est `true` |
| `offset` | Obligatoire | Integer | Décalage de la page actuelle |
| `limit` | Obligatoire | Integer | Taille de page utilisée par la requête |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de réponse pour lister les relations d'objets" }

## Erreurs {#errors}

Le tableau suivant répertorie les erreurs courantes pour cet endpoint et comment les résoudre.

| Statut | Cause | Recommandation |
|---|---|---|
| `400` | `anchor` non valide | Utilisez `source` ou `target` pour `anchor`. |
| `404` | Type ou objet introuvable | Vérifiez que `type_name` et `external_id` existent tous deux dans l'espace de travail. |
| `401` | Clé REST API manquante ou non valide | Vérifiez que l'en-tête `Authorization` utilise `Bearer YOUR_REST_API_KEY` et que la clé est active. |
| `403` | La clé API n'a pas la permission requise ou la requête est bloquée par la liste d'autorisation | Vérifiez que la clé dispose de la permission `data_objects.read` et que votre adresse IP source figure dans la liste d'autorisation de la clé, si elle est configurée. |
| `429` | Limite de débit dépassée | Réessayez après `X-RateLimit-Reset` et réduisez la fréquence des requêtes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erreurs pour lister les relations d'objets" }
{% endapi %}