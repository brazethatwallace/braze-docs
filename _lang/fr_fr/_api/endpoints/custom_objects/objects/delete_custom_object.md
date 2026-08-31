---
nav_title: "DELETE : Supprimer un objet personnalisé"
article_title: "DELETE : Supprimer un objet personnalisé"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Supprimer un objet personnalisé."
---
{% api %}
# Supprimer un objet personnalisé {#delete-custom-object}
{% apimethod delete %}
/custom_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Utilisez cet endpoint pour supprimer un objet personnalisé.

{% alert important %}
Les objets personnalisés sont actuellement en accès anticipé. Votre espace de travail doit être activé avant que les permissions de clé API pour les objets personnalisés n'apparaissent dans **Paramètres** > **Clés API**.
{% endalert %}

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous avez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec la permission `custom_objects.delete`.

## Limite de débit {#rate-limit}

Cet endpoint se trouve dans le compartiment d'écriture des objets personnalisés avec une limite par défaut de 50 requêtes par minute.

## Paramètres de chemin {#path-parameters}

Le tableau suivant répertorie et décrit les paramètres de chemin pour l'endpoint `/custom_objects/objects/{type_name}/{external_id}`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `type_name` | Obligatoire | String | Nom machine du type d'objet personnalisé |
| `external_id` | Obligatoire | String | Identifiant de l'objet |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de chemin pour la suppression d'un objet personnalisé" }

## Exemple de requête {#example-request}

Cette section comprend un exemple de payload de paramètres de chemin et un exemple de requête cURL.

### Exemple de payload de requête {#sample-request-payload}

Utilisez cet objet JSON comme référence pour les paramètres de chemin de cette requête.

```json
{
  "type_name": "account",
  "external_id": "acct-123"
}
```

### Exemple de requête cURL {#sample-curl-request}

Cet exemple supprime l'enregistrement de compte `acct-123`.

```bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Réponse {#response}

Cette section comprend un exemple de réponse réussie et les champs de réponse.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `200` peut renvoyer le corps de réponse suivant.

```json
{ "deleted": true }
```

La suppression est synchrone. Supprimer un objet ne supprime pas les objets associés.

### Paramètres de réponse {#response-parameters}

Le tableau suivant répertorie et décrit les champs d'une réponse réussie.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `deleted` | Obligatoire | Booléen | Indique si la suppression de l'objet a réussi |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de réponse pour la suppression d'un objet personnalisé" }

## Erreurs {#errors}

Le tableau suivant répertorie les erreurs courantes pour cet endpoint et comment les résoudre.

| Statut | Cause | Recommandation |
|---|---|---|
| `404` | Type introuvable ou objet introuvable | Vérifiez que `type_name` et `external_id` existent bien dans l'espace de travail. |
| `401` | Clé API REST manquante ou invalide | Vérifiez que l'en-tête `Authorization` utilise `Bearer YOUR_REST_API_KEY` et que la clé est active. |
| `403` | La clé API n'a pas la permission ou la requête est bloquée par la liste d'autorisation | Vérifiez que la clé possède la permission `custom_objects.delete` et que l'adresse IP source figure dans la liste d'autorisation de la clé, le cas échéant. |
| `429` | Limite de débit dépassée | Réessayez après `X-RateLimit-Reset` et réduisez la fréquence des requêtes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erreurs de suppression d'un objet personnalisé" }
{% endapi %}