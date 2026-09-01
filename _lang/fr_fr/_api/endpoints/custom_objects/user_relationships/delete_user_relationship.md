---
nav_title: "DELETE : Supprimer une relation utilisateur"
article_title: "DELETE : Supprimer une relation utilisateur"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Cet article décrit en détail l'endpoint Supprimer une relation utilisateur."
---
{% api %}
# Supprimer une relation utilisateur {#delete-user-relationship}
{% apimethod delete %}
/custom_objects/objects/{type_name}/{external_id}/users
{% endapimethod %}

> Utilisez cet endpoint pour supprimer une relation entre un utilisateur et un objet.

{% alert important %}
Les objets personnalisés sont actuellement en accès anticipé. Votre espace de travail doit être activé avant que les permissions de clé API pour les objets personnalisés n'apparaissent dans **Paramètres** > **Clés API**.
{% endalert %}

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec la permission `custom_objects.user_relationships.delete`.

## Limite de débit {#rate-limit}

Cet endpoint fait partie du compartiment d'écriture des objets personnalisés avec une limite par défaut de 50 requêtes par minute.

## Paramètres de chemin {#path-parameters}

Le tableau suivant répertorie et décrit les paramètres de chemin pour l'endpoint `/custom_objects/objects/{type_name}/{external_id}/users`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `type_name` | Obligatoire | String | Type d'objet |
| `external_id` | Obligatoire | String | Identifiant de l'objet |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de chemin pour supprimer une relation utilisateur" }

## Paramètres de requête {#request-parameters}

Le tableau suivant répertorie et décrit les paramètres du corps de requête JSON pour l'endpoint `/custom_objects/objects/{type_name}/{external_id}/users`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `braze_id` | Obligatoire | String | ID utilisateur Braze |
| `rel_kind` | Obligatoire | String | Type de relation |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête pour supprimer une relation utilisateur" }

{% alert note %}
Cet endpoint `DELETE` attend un corps de requête JSON. Vérifiez que votre client HTTP envoie bien des corps de requête lors des appels `DELETE`.
{% endalert %}

## Exemple de requête {#example-request}

Cette section comprend un exemple de payload JSON et un exemple de requête cURL.

### Exemple de payload de requête {#sample-request-payload}

```json
{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user"
}
```

### Exemple de requête cURL {#sample-curl-request}

Cet exemple supprime la relation `account_user` entre l'utilisateur spécifié et `acct-123`. Le profil utilisateur et l'enregistrement du compte sont tous deux conservés.

```bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/users' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user"
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
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de réponse pour supprimer une relation utilisateur" }

## Erreurs {#errors}

Le tableau suivant répertorie les erreurs courantes pour cet endpoint et comment les résoudre.

| Statut | Cause | Recommandation |
|---|---|---|
| `400` | Erreur de validation | Vérifiez que le corps de la requête contient des valeurs `braze_id` et `rel_kind` valides. |
| `404` | Relation ou objet introuvable | Vérifiez que l'objet, l'utilisateur et les valeurs de clé de relation existent tous. |
| `401` | Clé REST API manquante ou invalide | Vérifiez que l'en-tête `Authorization` utilise `Bearer YOUR_REST_API_KEY` et que la clé est active. |
| `403` | La clé API ne dispose pas de la permission ou la requête est bloquée par la liste d'autorisation | Vérifiez que la clé possède la permission `custom_objects.user_relationships.delete` et que votre adresse IP source figure dans la liste d'autorisation de la clé, si elle est configurée. |
| `429` | Limite de débit dépassée | Réessayez après `X-RateLimit-Reset` et réduisez la fréquence des requêtes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erreurs pour supprimer une relation utilisateur" }
{% endapi %}