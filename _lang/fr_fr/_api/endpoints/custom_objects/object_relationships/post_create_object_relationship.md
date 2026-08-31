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
/custom_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> Utilisez cet endpoint pour créer un lien de relation directionnel entre deux objets personnalisés.

{% alert important %}
Les objets personnalisés sont actuellement en accès anticipé. Votre espace de travail doit être activé avant que les permissions de clé API pour les objets personnalisés n'apparaissent dans **Paramètres** > **Clés API**.
{% endalert %}

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous avez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec la permission `custom_objects.object_relationships.create`.

## Limite de débit {#rate-limit}

Cet endpoint appartient au compartiment d'écriture des objets personnalisés avec une limite par défaut de 50 requêtes par minute.

## Paramètres de chemin {#path-parameters}

Le tableau suivant répertorie et décrit les paramètres de chemin pour l'endpoint `/custom_objects/objects/{type_name}/{external_id}/object_relationships`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `type_name` | Obligatoire | String | Type d'objet dans l'URL |
| `external_id` | Obligatoire | String | Identifiant d'objet dans l'URL |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de chemin pour la création de relation entre objets" }

## Paramètres de requête {#request-parameters}

Le tableau suivant répertorie et décrit les paramètres du corps de requête JSON pour l'endpoint `/custom_objects/objects/{type_name}/{external_id}/object_relationships`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `rel_kind` | Obligatoire | String | Type de relation |
| `related_type_name` | Obligatoire | String | Type d'objet associé |
| `related_external_id` | Obligatoire | String | Identifiant de l'objet associé |
| `anchor` | Facultatif | String | `source` (par défaut) ou `target` |
| `attributes` | Facultatif | Object | Attributs de la relation |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête pour la création de relation entre objets" }

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

Cet exemple relie `acct-123` à `acct-456` en tant que `subaccount`, avec `acct-123` comme source de la relation.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/object_relationships' \
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

Le code de statut `201` pourrait renvoyer le corps de réponse suivant.

```json
{
  "object_relationship": {
    "rel_kind": "subaccount",
    "to_custom_object": {
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
| `object_relationship` | Obligatoire | Object | Enregistrement de la relation créée |
| `object_relationship.rel_kind` | Obligatoire | String | Valeur du type de relation |
| `object_relationship.to_custom_object` | Conditionnel | Object | Objet associé lorsque `anchor=source` |
| `object_relationship.from_custom_object` | Conditionnel | Object | Objet associé lorsque `anchor=target` |
| `object_relationship.to_custom_object.type_name` | Conditionnel | String | Nom du type d'objet associé |
| `object_relationship.to_custom_object.external_id` | Conditionnel | String | ID externe de l'objet associé |
| `object_relationship.to_custom_object.attributes` | Conditionnel | Object | Attributs de l'objet associé |
| `object_relationship.from_custom_object.type_name` | Conditionnel | String | Nom du type d'objet associé |
| `object_relationship.from_custom_object.external_id` | Conditionnel | String | ID externe de l'objet associé |
| `object_relationship.from_custom_object.attributes` | Conditionnel | Object | Attributs de l'objet associé |
| `object_relationship.attributes` | Obligatoire | Object | Attributs de la relation |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de réponse pour la création de relation entre objets" }

## Erreurs {#errors}

Le tableau suivant répertorie les erreurs courantes pour cet endpoint et comment les résoudre.

| Statut | Cause | Recommandation |
|---|---|---|
| `400` | `rel_kind` inconnu, `anchor` invalide, type associé invalide pour le type de relation, ou violation de schéma | Vérifiez que `rel_kind` est valide pour la paire de types, utilisez un `anchor` valide et assurez-vous que les `attributes` correspondent au schéma de la relation. |
| `404` | Objet de l'URL, objet associé, type de l'URL ou type associé introuvable | Vérifiez que les deux objets et les deux noms de type existent dans l'espace de travail. |
| `409` | Lien en double (`duplicate-object-relationship`) | Utilisez `PUT` pour remplacer la relation existante, ou supprimez-la avant de la recréer. |
| `422` | Limite de relations par objet atteinte (`custom-object-relationship-limit-exceeded`) | Réduisez le nombre de relations pour l'objet, ou contactez le support Braze pour les limites de l'espace de travail. |
| `401` | Clé API REST manquante ou invalide | Vérifiez que l'en-tête `Authorization` utilise `Bearer YOUR_REST_API_KEY` et que la clé est active. |
| `403` | La clé API n'a pas la permission ou la requête est bloquée par la liste d'autorisation | Vérifiez que la clé dispose de la permission `custom_objects.object_relationships.create` et que votre adresse IP source figure dans la liste d'autorisation de la clé, le cas échéant. |
| `429` | Limite de débit dépassée | Réessayez après `X-RateLimit-Reset` et réduisez la fréquence des requêtes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erreurs pour la création de relation entre objets" }
{% endapi %}