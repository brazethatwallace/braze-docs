---
nav_title: "DELETE : Supprimer une relation d'objet"
article_title: "DELETE : Supprimer une relation d'objet"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Supprimer une relation d'objet."
---
{% api %}
# Supprimer une relation d'objet {#delete-object-relationship}
{% apimethod delete %}
/custom_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> Utilisez cet endpoint pour supprimer une arête de relation objet-à-objet.

{% alert important %}
Les objets personnalisés sont actuellement en accès anticipé. Votre espace de travail doit être activé avant que les autorisations de clé API pour les objets personnalisés n'apparaissent dans **Paramètres** > **Clés API**.
{% endalert %}

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec l'autorisation `custom_objects.object_relationships.delete`.

## Limite de débit {#rate-limit}

Cet endpoint fait partie du compartiment d'écriture des objets personnalisés avec une limite par défaut de 50 requêtes par minute.

## Paramètres de chemin {#path-parameters}

Le tableau suivant répertorie et décrit les paramètres de chemin pour l'endpoint `/custom_objects/objects/{type_name}/{external_id}/object_relationships`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `type_name` | Obligatoire | String | Type d'objet dans l'URL |
| `external_id` | Obligatoire | String | Identifiant d'objet dans l'URL |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de chemin pour la suppression de relation d'objet" }

## Paramètres de requête {#request-parameters}

Le tableau suivant répertorie et décrit les paramètres du corps de requête JSON pour l'endpoint `/custom_objects/objects/{type_name}/{external_id}/object_relationships`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `rel_kind` | Obligatoire | String | Type de relation |
| `related_type_name` | Obligatoire | String | Type d'objet lié |
| `related_external_id` | Obligatoire | String | Identifiant de l'objet lié |
| `anchor` | Optionnel | String | `source` (par défaut) ou `target` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête pour la suppression de relation d'objet" }

{% alert note %}
Cet endpoint `DELETE` attend un corps de requête JSON. Vérifiez que votre client HTTP envoie bien un corps de requête lors des appels `DELETE`.
{% endalert %}

## Exemple de requête {#example-request}

Cette section comprend un exemple de payload JSON et un exemple de requête cURL.

### Exemple de payload de requête {#sample-request-payload}

```json
{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source"
}
```

### Exemple de requête cURL {#sample-curl-request}

Cet exemple supprime la relation `subaccount` entre `acct-123` et `acct-456`. Les deux enregistrements de compte sont conservés.

```bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/object_relationships' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source"
}'
```

## Réponse {#response}

Cette section comprend un exemple de réponse réussie et les champs de la réponse.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `200` peut renvoyer le corps de réponse suivant.

```json
{ "deleted": true }
```

### Paramètres de réponse {#response-parameters}

Le tableau suivant répertorie et décrit les champs d'une réponse réussie.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `deleted` | Obligatoire | Boolean | Indique si la suppression de la relation a réussi |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de réponse pour la suppression de relation d'objet" }

## Erreurs {#errors}

Le tableau suivant répertorie les erreurs courantes pour cet endpoint et comment les résoudre.

| Statut | Cause | Recommandation |
|---|---|---|
| `400` | Erreur de validation | Vérifiez que le corps de la requête contient des valeurs valides pour `rel_kind`, `related_type_name`, `related_external_id` et `anchor`. |
| `404` | Relation ou objet de l'endpoint introuvable | Vérifiez que les deux objets existent et que les valeurs de clé de la relation correspondent à une arête existante. |
| `401` | Clé REST API manquante ou invalide | Vérifiez que l'en-tête `Authorization` utilise `Bearer YOUR_REST_API_KEY` et que la clé est active. |
| `403` | La clé API ne dispose pas de l'autorisation ou la requête est bloquée par la liste d'autorisation | Vérifiez que la clé dispose de l'autorisation `custom_objects.object_relationships.delete` et que votre adresse IP source figure dans la liste d'autorisation de la clé, si celle-ci est configurée. |
| `429` | Limite de débit dépassée | Réessayez après `X-RateLimit-Reset` et réduisez la fréquence des requêtes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erreurs de suppression de relation d'objet" }
{% endapi %}