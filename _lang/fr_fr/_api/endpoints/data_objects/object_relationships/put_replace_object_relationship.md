---
nav_title: "PUT : Remplacer une relation d'objet"
article_title: "PUT : Remplacer une relation d'objet"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Cet article décrit en détail l'endpoint Remplacer une relation d'objet."
---
{% api %}
# Remplacer une relation d'objet {#replace-object-relationship}
{% apimethod put %}
/data_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> Utilisez cet endpoint pour créer ou remplacer une relation d'objet.

{% alert important %}
Les objets de données sont actuellement en accès anticipé. Votre espace de travail doit être activé avant que les permissions de clé API pour les objets de données n'apparaissent dans **Paramètres** > **Clés API**.
{% endalert %}

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec la permission `data_objects.object_relationships.update`.

## Limite de débit {#rate-limit}

Cet endpoint fait partie du compartiment d'écriture des objets de données avec une limite par défaut de 50 requêtes par minute.

## Paramètres de chemin {#path-parameters}

Le tableau suivant répertorie et décrit les paramètres de chemin pour l'endpoint `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `type_name` | Obligatoire | String | Type d'objet de l'URL |
| `external_id` | Obligatoire | String | Identifiant d'objet de l'URL |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de chemin pour remplacer une relation d'objet" }

## Paramètres de requête {#request-parameters}

Le tableau suivant répertorie et décrit les paramètres du corps de la requête JSON pour l'endpoint `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `rel_kind` | Obligatoire | String | Type de relation |
| `related_type_name` | Obligatoire | String | Type d'objet lié |
| `related_external_id` | Obligatoire | String | Identifiant d'objet lié |
| `anchor` | Facultatif | String | `source` (par défaut) ou `target` |
| `attributes` | Facultatif | Object | Attributs de la relation |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête pour remplacer une relation d'objet" }

## Exemple de requête {#example-request}

Cette section inclut un exemple de payload JSON et un exemple de requête cURL.

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

Cet exemple remplace la relation `subaccount` entre `acct-123` et `acct-456`, en écrasant tous les attributs précédemment stockés sur celle-ci.

```bash
curl --location --request PUT 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships' \
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

Cette section inclut un exemple de réponse réussie et les champs de la réponse.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `200` pourrait renvoyer le corps de réponse suivant.

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
| `object_relationship` | Obligatoire | Object | Enregistrement de la relation créée ou remplacée |
| `object_relationship.rel_kind` | Obligatoire | String | Valeur du type de relation |
| `object_relationship.to_data_object` | Conditionnel | Object | Objet lié lorsque `anchor=source` |
| `object_relationship.from_data_object` | Conditionnel | Object | Objet lié lorsque `anchor=target` |
| `object_relationship.attributes` | Obligatoire | Object | Attributs de la relation |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de réponse pour remplacer une relation d'objet" }

## Erreurs {#errors}

Le tableau suivant répertorie les erreurs courantes pour cet endpoint et comment les résoudre.

| Statut | Cause | Recommandation |
|---|---|---|
| `400` | Erreur de validation | Vérifiez que `rel_kind`, `anchor` et `attributes` sont valides pour le type de relation. |
| `404` | Relation ou objets de l'endpoint introuvables (`data-object-relationship-not-found`) | Vérifiez que les deux objets et les noms de types liés existent dans l'espace de travail. |
| `422` | Limite de relations par objet atteinte (`data-object-relationship-limit-exceeded`) | Réduisez le nombre de relations pour l'objet, ou contactez le support Braze concernant les limites de l'espace de travail. |
| `401` | Clé REST API manquante ou invalide | Vérifiez que l'en-tête `Authorization` utilise `Bearer YOUR_REST_API_KEY` et que la clé est active. |
| `403` | La clé API n'a pas la permission ou la requête est bloquée par la liste d'autorisation | Vérifiez que la clé dispose de la permission `data_objects.object_relationships.update` et que votre adresse IP source figure sur la liste d'autorisation de la clé, si elle est configurée. |
| `429` | Limite de débit dépassée | Réessayez après `X-RateLimit-Reset` et réduisez la fréquence des requêtes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erreurs pour remplacer une relation d'objet" }
{% endapi %}