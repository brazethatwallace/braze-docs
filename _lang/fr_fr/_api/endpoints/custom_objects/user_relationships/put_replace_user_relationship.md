---
nav_title: "PUT : Remplacer une relation utilisateur"
article_title: "PUT : Remplacer une relation utilisateur"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Remplacer une relation utilisateur."
---
{% api %}
# Remplacer une relation utilisateur {#replace-user-relationship}
{% apimethod put %}
/custom_objects/objects/{type_name}/{external_id}/users
{% endapimethod %}

> Utilisez cet endpoint pour créer ou remplacer une relation utilisateur.

{% alert important %}
Les objets personnalisés sont actuellement en accès anticipé. Votre espace de travail doit être activé avant que les autorisations de clé API des objets personnalisés n'apparaissent dans **Paramètres** > **Clés API**.
{% endalert %}

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec l'autorisation `custom_objects.user_relationships.update`.

## Limite de débit {#rate-limit}

Cet endpoint fait partie du compartiment d'écriture des objets personnalisés avec une limite par défaut de 50 requêtes par minute.

## Paramètres de chemin {#path-parameters}

Le tableau suivant répertorie et décrit les paramètres de chemin pour l'endpoint `/custom_objects/objects/{type_name}/{external_id}/users`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `type_name` | Obligatoire | String | Type d'objet |
| `external_id` | Obligatoire | String | Identifiant de l'objet |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de chemin pour remplacer une relation utilisateur" }

## Paramètres de requête {#request-parameters}

Le tableau suivant répertorie et décrit les paramètres du corps de requête JSON pour l'endpoint `/custom_objects/objects/{type_name}/{external_id}/users`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `braze_id` | Obligatoire | String | ID utilisateur Braze |
| `rel_kind` | Obligatoire | String | Type de relation |
| `attributes` | Facultatif | Objet | Attributs de la relation |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête pour remplacer une relation utilisateur" }

## Exemple de requête {#example-request}

Cette section comprend un exemple de payload JSON et un exemple de requête cURL.

### Exemple de payload de requête {#sample-request-payload}

```json
{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "admin"
  }
}
```

### Exemple de requête cURL {#sample-curl-request}

Cet exemple remplace les attributs de la relation `account_user` entre l'utilisateur et `acct-123`, en écrasant tous les attributs précédemment stockés.

```bash
curl --location --request PUT 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/users' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "admin"
  }
}'
```

## Réponse {#response}

Cette section comprend un exemple de réponse réussie et les champs de la réponse.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `200` peut renvoyer le corps de réponse suivant.

```json
{
  "user_relationship": {
    "type_name": "account",
    "external_id": "acct-123",
    "rel_kind": "account_user",
    "user": { "braze_id": "507f1f77bcf86cd799439011" },
    "attributes": { "role": "admin" }
  }
}
```

### Paramètres de réponse {#response-parameters}

Le tableau suivant répertorie et décrit les champs d'une réponse réussie.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `user_relationship` | Obligatoire | Objet | Enregistrement de la relation utilisateur créée ou remplacée |
| `user_relationship.type_name` | Obligatoire | String | Nom machine du type d'objet personnalisé |
| `user_relationship.external_id` | Obligatoire | String | Identifiant de l'objet personnalisé |
| `user_relationship.rel_kind` | Obligatoire | String | Valeur du type de relation |
| `user_relationship.user` | Obligatoire | Objet | Objet utilisateur lié |
| `user_relationship.user.braze_id` | Obligatoire | String | Identifiant utilisateur Braze |
| `user_relationship.attributes` | Obligatoire | Objet | Attributs de la relation |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de réponse pour remplacer une relation utilisateur" }

## Erreurs {#errors}

Le tableau suivant répertorie les erreurs courantes pour cet endpoint et comment les résoudre.

| Statut | Cause | Recommandation |
|---|---|---|
| `400` | Erreur de validation | Vérifiez que `rel_kind` est valide pour le type d'objet et que les `attributes` correspondent au schéma de la relation. |
| `404` | Relation ou objet introuvable (`custom-object-relationship-not-found`) | Vérifiez que l'objet, l'utilisateur et les valeurs de la clé de relation existent bien. |
| `422` | Limite d'objets par utilisateur atteinte (`custom-objects-per-user-limit-exceeded`) ou limite d'utilisateurs par objet atteinte (`users-per-custom-object-limit-exceeded`) | Réduisez le nombre de relations pour l'utilisateur ou l'objet, ou contactez le support Braze concernant les limites de votre espace de travail. |
| `401` | Clé REST API manquante ou invalide | Vérifiez que l'en-tête `Authorization` utilise `Bearer YOUR_REST_API_KEY` et que la clé est active. |
| `403` | La clé API n'a pas l'autorisation ou la requête est bloquée par la liste d'autorisation | Vérifiez que la clé dispose de l'autorisation `custom_objects.user_relationships.update` et que votre adresse IP source figure dans la liste d'autorisation de la clé, si elle est configurée. |
| `429` | Limite de débit dépassée | Réessayez après `X-RateLimit-Reset` et réduisez la fréquence des requêtes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erreurs pour remplacer une relation utilisateur" }
{% endapi %}