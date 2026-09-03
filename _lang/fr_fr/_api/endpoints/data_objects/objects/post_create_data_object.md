---
nav_title: "POST : Créer un objet de données"
article_title: "POST : Créer un objet de données"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Créer un objet de données."
---
{% api %}
# Créer un objet de données {#create-data-object}
{% apimethod post %}
/data_objects/objects/{type_name}
{% endapimethod %}

> Utilisez cet endpoint pour créer un objet de données pour un type donné.

{% alert important %}
Les objets de données sont actuellement en accès anticipé. Votre espace de travail doit être activé avant que les autorisations de clé API des objets de données n'apparaissent dans **Paramètres** > **Clés API**.
{% endalert %}

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec l'autorisation `data_objects.create`.

## Limite de débit {#rate-limit}

Cet endpoint fait partie du compartiment d'écriture des objets de données avec une limite par défaut de 50 requêtes par minute.

## Paramètres de chemin {#path-parameters}

Le tableau suivant répertorie et décrit les paramètres de chemin pour l'endpoint `/data_objects/objects/{type_name}`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `type_name` | Obligatoire | String | Nom machine du type d'objet de données |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de chemin pour la création d'un objet de données" }

## Paramètres de requête {#request-parameters}

Le tableau suivant répertorie et décrit les paramètres du corps de requête JSON pour l'endpoint `/data_objects/objects/{type_name}`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `external_id` | Obligatoire | String | Identifiant de l'objet, unique au sein du type |
| `attributes` | Obligatoire | Objet | Valeurs associées aux noms de champs, validées par rapport au schéma du type |
| `display_name` | Facultatif | String | Libellé d'affichage de l'objet. Lorsque le type possède un champ source pour le nom d'affichage, la valeur de ce champ est prioritaire. Valeur par défaut : `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête pour la création d'un objet de données" }

## Exemple de requête {#example-request}

Cette section comprend un exemple de payload JSON et un exemple de requête cURL.

### Exemple de payload de requête {#sample-request-payload}

```json
{
  "external_id": "acct-new",
  "attributes": {
    "name": "New Account",
    "industry": "software"
  }
}
```

### Exemple de requête cURL {#sample-curl-request}

Cet exemple crée un enregistrement `account` avec l'identifiant `acct-new` et définit ses attributs `name` et `industry`.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/data_objects/objects/account' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "external_id": "acct-new",
  "attributes": {
    "name": "New Account",
    "industry": "software"
  }
}'
```

## Réponse {#response}

Cette section comprend un exemple de réponse réussie et les champs de la réponse.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `201` peut renvoyer le corps de réponse suivant.

```json
{
  "data_object": {
    "type_name": "account",
    "external_id": "acct-new",
    "attributes": { "name": "New Account", "industry": "software" }
  }
}
```

### Paramètres de réponse {#response-parameters}

Le tableau suivant répertorie et décrit les champs d'une réponse réussie.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `data_object` | Obligatoire | Objet | Enregistrement de l'objet de données créé |
| `data_object.type_name` | Obligatoire | String | Nom machine du type d'objet de données |
| `data_object.external_id` | Obligatoire | String | Identifiant de l'objet de données |
| `data_object.attributes` | Obligatoire | Objet | Attributs de l'objet stocké, indexés par nom de champ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de réponse pour la création d'un objet de données" }

## Erreurs {#errors}

Le tableau suivant répertorie les erreurs courantes pour cet endpoint et comment les résoudre.

| Statut | Cause | Recommandation |
|---|---|---|
| `400` | Champ d'attribut inconnu ou type d'attribut non valide | Vérifiez que chaque champ dans `attributes` existe dans le schéma du type et utilise le bon type de données. |
| `404` | Type introuvable (`data-object-type-not-found`) | Vérifiez que `type_name` existe dans l'espace de travail et correspond exactement au nom machine. |
| `409` | Objet en double (`duplicate-data-object`) | Utilisez un `external_id` différent, ou utilisez `PUT` pour remplacer l'objet existant. |
| `422` | Limite d'enregistrements atteinte (`data-object-record-limit-exceeded`) | Réduisez le nombre d'objets pour le type, ou contactez le support Braze concernant les limites de votre espace de travail. |
| `401` | Clé REST API manquante ou non valide | Vérifiez que l'en-tête `Authorization` utilise `Bearer YOUR_REST_API_KEY` et que la clé est active. |
| `403` | La clé API ne dispose pas de l'autorisation ou la requête est bloquée par la liste d'autorisation | Vérifiez que la clé possède l'autorisation `data_objects.create` et que votre adresse IP source figure dans la liste d'autorisation de la clé, si celle-ci est configurée. |
| `429` | Limite de débit dépassée | Réessayez après `X-RateLimit-Reset` et réduisez la fréquence des requêtes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erreurs de création d'un objet de données" }
{% endapi %}