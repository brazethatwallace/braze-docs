---
nav_title: "POST : Créer une relation entre objets"
article_title: "POST : Créer une relation entre objets"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Créer une relation entre objets."
---
{% api %}
# Créer une relation entre objets {#create-object-relationship}
{% apimethod post %}
/data_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> Utilisez cet endpoint pour créer un lien de relation directionnel entre deux objets de données.

{% alert important %}
Les objets de données sont actuellement en accès anticipé. Votre espace de travail doit être activé avant que les permissions de clé API pour les objets de données n'apparaissent dans **Paramètres** > **Clés API**.
{% endalert %}

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous avez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec la permission `data_objects.object_relationships.create`.

## Limite de débit {#rate-limit}

Cet endpoint appartient au compartiment d'écriture des objets de données avec une limite par défaut de 50 requêtes par minute.

## Paramètres de chemin {#path-parameters}

Le tableau suivant répertorie et décrit les paramètres de chemin pour l'endpoint `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `type_name` | Obligatoire | String | Type d'objet dans l'URL |
| `external_id` | Obligatoire | String | Identifiant d'objet dans l'URL |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de chemin pour créer une relation entre objets" }

## Paramètres de requête {#request-parameters}

Le tableau suivant répertorie et décrit les paramètres du corps de requête JSON pour l'endpoint `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `rel_kind` | Obligatoire | String | Type de relation |
| `related_type_name` | Obligatoire | String | Type d'objet lié |
| `related_external_id` | Obligatoire | String | Identifiant de l'objet lié |
| `anchor` | Facultatif | String | `source` (par défaut) ou `target` |
| `attributes` | Facultatif | Objet | Attributs de la relation |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête pour créer une relation entre objets" }

## Exemple de requête {#example-request}

Cette section comprend un exemple de payload JSON et un exemple de requête cURL.

### Exemple de payload de requête {#sample-request-payload}

```json
{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source",
  "attributes": {}
}
```

### Exemple de requête cURL {#sample-curl-request}

Cet exemple lie `acct-123` à `acct-456` en tant que `subaccount`, avec `acct-123` comme source de la relation.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source",
  "attributes": {}
}'
```

## Réponse {#response}

Cette section comprend un exemple de réponse réussie et les champs de la réponse.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `201` peut renvoyer le corps de réponse suivant.

```json
{
  "object_relationship": {
    "rel_kind": "subaccount",
    "to_data_object": {
      "type_name": "account",
      "external_id": "acct-456",
      "attributes": { "name": "Child Account" }
    },
    "attributes": {}
  }
}
```

### Paramètres de réponse {#response-parameters}

Le tableau suivant répertorie et décrit les champs d'une réponse réussie.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `object_relationship` | Obligatoire | Objet | Enregistrement de la relation créée |
| `object_relationship.rel_kind` | Obligatoire | String | Valeur du type de relation |
| `object_relationship.to_data_object` | Conditionnel | Objet | Objet lié lorsque `anchor=source` |
| `object_relationship.from_data_object` | Conditionnel | Objet | Objet lié lorsque `anchor=target` |
| `object_relationship.to_data_object.type_name` | Conditionnel | String | Nom du type de l'objet lié |
| `object_relationship.to_data_object.external_id` | Conditionnel | String | ID externe de l'objet lié |
| `object_relationship.to_data_object.attributes` | Conditionnel | Objet | Attributs de l'objet lié |
| `object_relationship.from_data_object.type_name` | Conditionnel | String | Nom du type de l'objet lié |
| `object_relationship.from_data_object.external_id` | Conditionnel | String | ID externe de l'objet lié |
| `object_relationship.from_data_object.attributes` | Conditionnel | Objet | Attributs de l'objet lié |
| `object_relationship.attributes` | Obligatoire | Objet | Attributs de la relation |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de réponse pour créer une relation entre objets" }

## Erreurs {#errors}

Le tableau suivant répertorie les erreurs courantes pour cet endpoint et comment les résoudre.

| Statut | Cause | Recommandation |
|---|---|---|
| `400` | `rel_kind` inconnu, `anchor` invalide, type lié invalide pour le type de relation, ou violation du schéma | Confirmez que `rel_kind` est valide pour la paire de types, utilisez un `anchor` valide et assurez-vous que les `attributes` correspondent au schéma de relation. |
| `404` | Objet de l'URL, objet lié, type de l'URL ou type lié introuvable | Confirmez que les deux objets et les deux noms de type existent dans l'espace de travail. |
| `409` | Lien en double (`duplicate-object-relationship`) | Utilisez `PUT` pour remplacer la relation existante, ou supprimez-la avant de la recréer. |
| `422` | Limite de relations par objet atteinte (`data-object-relationship-limit-exceeded`) | Réduisez le nombre de relations pour l'objet, ou contactez le support Braze au sujet des limites de l'espace de travail. |
| `401` | Clé REST API manquante ou invalide | Vérifiez que l'en-tête `Authorization` utilise `Bearer YOUR_REST_API_KEY` et que la clé est active. |
| `403` | La clé API n'a pas la permission requise ou la requête est bloquée par la liste d'autorisation | Confirmez que la clé possède la permission `data_objects.object_relationships.create` et que votre adresse IP source figure dans la liste d'autorisation de la clé, si elle est configurée. |
| `429` | Limite de débit dépassée | Réessayez après `X-RateLimit-Reset` et réduisez la fréquence des requêtes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erreurs pour créer une relation entre objets" }
{% endapi %}