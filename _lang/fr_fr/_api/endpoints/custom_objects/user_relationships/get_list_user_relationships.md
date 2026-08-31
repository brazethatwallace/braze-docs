---
nav_title: "GET : Lister les relations utilisateur"
article_title: "GET : Lister les relations utilisateur"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Cet article décrit en détail l'endpoint Lister les relations utilisateur."
---
{% api %}
# Lister les relations utilisateur {#list-user-relationships}
{% apimethod get %}
/custom_objects/objects/{type_name}/{external_id}/user_relationships
{% endapimethod %}

> Utilisez cet endpoint pour lister les utilisateurs liés à un objet personnalisé.

{% alert important %}
Les objets personnalisés sont actuellement en accès anticipé. Votre espace de travail doit être activé avant que les permissions de clé API pour les objets personnalisés n'apparaissent dans **Paramètres** > **Clés API**.
{% endalert %}

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec la permission `custom_objects.user_relationships.read`.

## Limite de débit {#rate-limit}

Cet endpoint fait partie du compartiment de lecture des objets personnalisés avec une limite par défaut de 50 requêtes par minute.

## Paramètres de chemin {#path-parameters}

Le tableau suivant liste et décrit les paramètres de chemin pour l'endpoint `/custom_objects/objects/{type_name}/{external_id}/user_relationships`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `type_name` | Obligatoire | String | Type d'objet |
| `external_id` | Obligatoire | String | Identifiant de l'objet |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de chemin pour lister les relations utilisateur" }

## Paramètres de requête {#query-parameters}

Le tableau suivant liste et décrit les paramètres de requête pour l'endpoint `/custom_objects/objects/{type_name}/{external_id}/user_relationships`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `rel_kind` | Facultatif | String | Filtrer par type de relation |
| `limit` | Facultatif | Integer | Taille de la page. Par défaut `100`. Limité de `1` à `250` |
| `offset` | Facultatif | Integer | Décalage. Par défaut `0`. Les valeurs négatives sont ramenées à `0` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête pour lister les relations utilisateur" }

## Exemple de requête {#example-request}

Cette section comprend un exemple de payload et un exemple de requête cURL.

### Exemple de payload de requête {#sample-request-payload}

Utilisez cet objet JSON comme référence pour les paramètres de requête.

```json
{
  "type_name": "account",
  "external_id": "acct-123",
  "rel_kind": "account_user",
  "limit": 100,
  "offset": 0
}
```

### Exemple de requête cURL {#sample-curl-request}

Cet exemple liste les utilisateurs liés à `acct-123` via la relation `account_user`.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/user_relationships?rel_kind=account_user&limit=100&offset=0' \
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
      "type_name": "account",
      "external_id": "acct-123",
      "rel_kind": "account_user",
      "user": { "braze_id": "507f1f77bcf86cd799439011" },
      "attributes": { "role": "admin" }
    }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

Le payload `user` contient uniquement `braze_id`.

### Paramètres de réponse {#response-parameters}

Le tableau suivant liste et décrit les champs d'une réponse réussie.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `items` | Obligatoire | Array | Liste des enregistrements de relations utilisateur |
| `items[].type_name` | Obligatoire | String | Nom machine du type d'objet personnalisé |
| `items[].external_id` | Obligatoire | String | Identifiant de l'objet personnalisé |
| `items[].rel_kind` | Obligatoire | String | Valeur du type de relation |
| `items[].user` | Obligatoire | Object | Objet utilisateur lié |
| `items[].user.braze_id` | Obligatoire | String | Identifiant utilisateur Braze |
| `items[].attributes` | Obligatoire | Object | Attributs de la relation |
| `total_count` | Obligatoire | Integer | Nombre total d'enregistrements correspondants |
| `has_more` | Obligatoire | Boolean | Indique si une autre page de résultats est disponible |
| `next_offset` | Facultatif | Integer | Décalage pour la page suivante lorsque `has_more` est `true` |
| `offset` | Obligatoire | Integer | Décalage de la page actuelle |
| `limit` | Obligatoire | Integer | Taille de page utilisée par la requête |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de réponse pour lister les relations utilisateur" }

## Erreurs {#errors}

Le tableau suivant liste les erreurs courantes pour cet endpoint et comment les résoudre.

| Statut | Cause | Recommandation |
|---|---|---|
| `404` | Type ou objet introuvable | Confirmez que `type_name` et `external_id` existent tous les deux dans l'espace de travail. |
| `401` | Clé REST API manquante ou invalide | Vérifiez que l'en-tête `Authorization` utilise `Bearer YOUR_REST_API_KEY` et que la clé est active. |
| `403` | La clé API ne dispose pas de la permission ou la requête est bloquée par la liste d'autorisation | Confirmez que la clé dispose de la permission `custom_objects.user_relationships.read` et que votre adresse IP source figure sur la liste d'autorisation de la clé, si elle est configurée. |
| `429` | Limite de débit dépassée | Réessayez après `X-RateLimit-Reset` et réduisez la fréquence des requêtes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erreurs pour lister les relations utilisateur" }
{% endapi %}