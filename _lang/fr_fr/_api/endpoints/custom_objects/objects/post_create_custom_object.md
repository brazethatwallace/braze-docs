---
nav_title: "POST : Créer un objet personnalisé"
article_title: "POST : Créer un objet personnalisé"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Cet article décrit en détail l'endpoint Créer un objet personnalisé."
---
{% api %}
# Créer un objet personnalisé {#create-custom-object}
{% apimethod post %}
/custom_objects/objects/{type_name}
{% endapimethod %}

> Utilisez cet endpoint pour créer un objet personnalisé pour un type donné.

{% alert important %}
Les objets personnalisés sont actuellement en accès anticipé. Votre espace de travail doit être activé avant que les permissions de clé API pour les objets personnalisés n'apparaissent dans **Paramètres** > **Clés API**.
{% endalert %}

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec la permission `custom_objects.create`.

## Limite de débit {#rate-limit}

Cet endpoint fait partie du compartiment d'écriture des objets personnalisés avec une limite par défaut de 50 requêtes par minute.

## Paramètres de chemin {#path-parameters}

Le tableau suivant répertorie et décrit les paramètres de chemin pour l'endpoint `/custom_objects/objects/{type_name}`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `type_name` | Obligatoire | String | Nom machine du type d'objet personnalisé |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de chemin pour créer un objet personnalisé" }

## Paramètres de requête {#request-parameters}

Le tableau suivant répertorie et décrit les paramètres du corps de requête JSON pour l'endpoint `/custom_objects/objects/{type_name}`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `external_id` | Obligatoire | String | Identifiant de l'objet, unique au sein du type |
| `attributes` | Obligatoire | Objet | Valeurs indexées par nom de champ, validées par rapport au schéma du type |
| `display_name` | Facultatif | String | Libellé d'affichage de l'objet. Lorsque le type dispose d'un champ source pour le nom d'affichage, la valeur de ce champ est prioritaire. La valeur par défaut est `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête pour créer un objet personnalisé" }

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
curl --location --request POST 'https://rest.iad-01.braze.com/custom_objects/objects/account' \
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

Le code de statut `201` pourrait renvoyer le corps de réponse suivant.

```json
{
  "custom_object": {
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
| `custom_object` | Obligatoire | Objet | Enregistrement de l'objet personnalisé créé |
| `custom_object.type_name` | Obligatoire | String | Nom machine du type d'objet personnalisé |
| `custom_object.external_id` | Obligatoire | String | Identifiant de l'objet personnalisé |
| `custom_object.attributes` | Obligatoire | Objet | Attributs de l'objet stockés, indexés par nom de champ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de réponse pour créer un objet personnalisé" }

## Erreurs {#errors}

Le tableau suivant répertorie les erreurs courantes pour cet endpoint et comment les résoudre.

| Statut | Cause | Recommandation |
|---|---|---|
| `400` | Champ d'attribut inconnu ou type d'attribut invalide | Vérifiez que chaque champ dans `attributes` existe dans le schéma du type et utilise le type de données correct. |
| `404` | Type introuvable (`custom-object-type-not-found`) | Vérifiez que `type_name` existe dans l'espace de travail et correspond exactement au nom machine. |
| `409` | Objet en double (`duplicate-custom-object`) | Utilisez un `external_id` différent, ou utilisez `PUT` pour remplacer l'objet existant. |
| `422` | Limite d'enregistrements atteinte (`custom-object-record-limit-exceeded`) | Réduisez le nombre d'objets pour le type, ou contactez le support Braze concernant les limites de votre espace de travail. |
| `401` | Clé REST API manquante ou invalide | Vérifiez que l'en-tête `Authorization` utilise `Bearer YOUR_REST_API_KEY` et que la clé est active. |
| `403` | La clé API ne dispose pas de la permission ou la requête est bloquée par la liste d'autorisation | Vérifiez que la clé dispose de la permission `custom_objects.create` et que votre adresse IP source figure dans la liste d'autorisation de la clé, si elle est configurée. |
| `429` | Limite de débit dépassée | Réessayez après `X-RateLimit-Reset` et réduisez la fréquence des requêtes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erreurs pour créer un objet personnalisé" }
{% endapi %}