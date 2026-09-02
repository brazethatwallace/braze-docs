---
nav_title: "GET : Lister les types de relations utilisateur"
article_title: "GET : Lister les types de relations utilisateur"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Lister les types de relations utilisateur."
---
{% api %}
# Lister les types de relations utilisateur {#list-user-relationship-types}
{% apimethod get %}
/data_objects/types/{type_name}/user_relationship_types
{% endapimethod %}

> Utilisez cet endpoint pour lister les valeurs `rel_kind` valides pour les relations utilisateur sur un type d'objet de données.

{% alert important %}
Les objets de données sont actuellement en accès anticipé. Votre espace de travail doit être activé avant que les permissions de clé API pour les objets de données n'apparaissent dans **Paramètres** > **Clés API**.
{% endalert %}

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec la permission `data_objects.read`.

## Limite de débit {#rate-limit}

Cet endpoint fait partie du compartiment de lecture des objets de données avec une limite par défaut de 50 requêtes par minute.

## Paramètres de chemin {#path-parameters}

Le tableau suivant répertorie et décrit les paramètres de chemin pour l'endpoint `/data_objects/types/{type_name}/user_relationship_types`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `type_name` | Obligatoire | String | Nom machine du type d'objet de données |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de chemin pour lister les types de relations utilisateur" }

## Paramètres de requête {#query-parameters}

Le tableau suivant répertorie et décrit les paramètres de requête pour l'endpoint `/data_objects/types/{type_name}/user_relationship_types`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `limit` | Facultatif | Integer | Taille de la page. Valeur par défaut `100`. Borné entre `1` et `250` |
| `offset` | Facultatif | Integer | Décalage. Valeur par défaut `0`. Les valeurs négatives sont ramenées à `0` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête pour lister les types de relations utilisateur" }

## Exemple de requête {#example-request}

Cette section comprend un exemple de payload et un exemple de requête cURL.

### Exemple de payload de requête {#sample-request-payload}

Utilisez cet objet JSON comme référence pour les paramètres de requête.

```json
{
  "type_name": "account",
  "limit": 100,
  "offset": 0
}
```

### Exemple de requête cURL {#sample-curl-request}

Cet exemple liste les types de relations utilisateur que vous pouvez utiliser pour associer des utilisateurs à des enregistrements `account`.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/types/account/user_relationship_types?limit=100&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Réponse {#response}

Cette section comprend un exemple de réponse réussie et les champs de la réponse.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `200` peut renvoyer le corps de réponse suivant.

```json
{
  "items": [
    { "rel_kind": "account_user", "display_name": "account_user" }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

`display_name` correspond actuellement à `rel_kind`.

### Paramètres de réponse {#response-parameters}

Le tableau suivant répertorie et décrit les champs d'une réponse réussie.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `items` | Obligatoire | Array | Liste des types de relations utilisateur disponibles |
| `items[].rel_kind` | Obligatoire | String | Valeur du type de relation utilisateur |
| `items[].display_name` | Obligatoire | String | Libellé d'affichage du type de relation |
| `total_count` | Obligatoire | Integer | Nombre total d'enregistrements correspondants |
| `has_more` | Obligatoire | Boolean | Indique si une autre page de résultats est disponible |
| `next_offset` | Facultatif | Integer | Décalage pour la page suivante lorsque `has_more` est `true` |
| `offset` | Obligatoire | Integer | Décalage de la page actuelle |
| `limit` | Obligatoire | Integer | Taille de la page utilisée par la requête |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de réponse pour lister les types de relations utilisateur" }

## Erreurs {#errors}

Le tableau suivant répertorie les erreurs courantes pour cet endpoint et comment les résoudre.

| Statut | Cause | Recommandation |
|---|---|---|
| `404` | Type introuvable (`data-object-type-not-found`) | Vérifiez que `type_name` existe dans l'espace de travail et correspond exactement au nom machine. |
| `401` | Clé API REST manquante ou invalide | Vérifiez que l'en-tête `Authorization` utilise `Bearer YOUR_REST_API_KEY` et que la clé est active. |
| `403` | La clé API ne dispose pas de la permission ou la requête est bloquée par la liste d'autorisations | Vérifiez que la clé possède la permission `data_objects.read` et que votre adresse IP source figure dans la liste d'autorisations de la clé, si celle-ci est configurée. |
| `429` | Limite de débit dépassée | Réessayez après `X-RateLimit-Reset` et réduisez la fréquence des requêtes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erreurs pour lister les types de relations utilisateur" }
{% endapi %}