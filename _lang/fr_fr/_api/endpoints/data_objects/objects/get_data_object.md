---
nav_title: "GET : Obtenir un objet de données"
article_title: "GET : Obtenir un objet de données"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Cet article décrit en détail l'endpoint Obtenir un objet de données."
---
{% api %}
# Obtenir un objet de données {#get-data-object}
{% apimethod get %}
/data_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Utilisez cet endpoint pour renvoyer un objet de données.

{% alert important %}
Les objets de données sont actuellement en accès anticipé. Votre espace de travail doit être activé avant que les permissions de clé API des objets de données n'apparaissent dans **Paramètres** > **Clés API**.
{% endalert %}

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous avez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec la permission `data_objects.read`.

## Limite de débit {#rate-limit}

Cet endpoint se trouve dans le compartiment de lecture des objets de données avec une limite par défaut de 50 requêtes par minute.

## Paramètres de chemin {#path-parameters}

Le tableau suivant répertorie et décrit les paramètres de chemin pour l'endpoint `/data_objects/objects/{type_name}/{external_id}`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `type_name` | Obligatoire | String | Nom machine du type d'objet de données |
| `external_id` | Obligatoire | String | Identifiant de l'objet |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de chemin pour obtenir un objet de données" }

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

Cet exemple récupère l'enregistrement du compte `acct-123` et ses attributs stockés.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Réponse {#response}

Cette section comprend un exemple de réponse réussie et les champs de la réponse.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `200` peut renvoyer le corps de réponse suivant.

```json
{
  "data_object": {
    "type_name": "account",
    "external_id": "acct-123",
    "attributes": { "name": "Acme", "industry": "software" }
  }
}
```

### Paramètres de la réponse {#response-parameters}

Le tableau suivant répertorie et décrit les champs d'une réponse réussie.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `data_object` | Obligatoire | Object | Enregistrement de l'objet de données renvoyé |
| `data_object.type_name` | Obligatoire | String | Nom machine du type d'objet de données |
| `data_object.external_id` | Obligatoire | String | Identifiant de l'objet de données |
| `data_object.attributes` | Obligatoire | Object | Attributs de l'objet indexés par nom de champ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de la réponse pour obtenir un objet de données" }

## Erreurs {#errors}

Le tableau suivant répertorie les erreurs courantes pour cet endpoint et comment les résoudre.

| Statut | Cause | Recommandation |
|---|---|---|
| `404` | Type non trouvé (`data-object-type-not-found`) ou objet non trouvé (`data-object-not-found`) | Vérifiez que `type_name` et `external_id` existent bien dans l'espace de travail. |
| `401` | Clé API REST manquante ou invalide | Vérifiez que l'en-tête `Authorization` utilise `Bearer YOUR_REST_API_KEY` et que la clé est active. |
| `403` | La clé API ne dispose pas de la permission ou la requête est bloquée par la liste d'autorisation | Vérifiez que la clé dispose de la permission `data_objects.read` et que votre adresse IP source figure sur la liste d'autorisation de la clé, si elle est configurée. |
| `429` | Limite de débit dépassée | Réessayez après `X-RateLimit-Reset` et réduisez la fréquence des requêtes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erreurs pour obtenir un objet de données" }
{% endapi %}