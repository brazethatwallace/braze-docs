---
nav_title: "PUT : Remplacer un objet personnalisé"
article_title: "PUT : Remplacer un objet personnalisé"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Remplacer un objet personnalisé."
---
{% api %}
# Remplacer un objet personnalisé {#replace-custom-object}
{% apimethod put %}
/custom_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Utilisez cet endpoint pour créer ou remplacer un objet personnalisé avec une sémantique de remplacement complet des attributs.

{% alert important %}
Les objets personnalisés sont actuellement en accès anticipé. Votre espace de travail doit être activé avant que les permissions de clé API des objets personnalisés n'apparaissent dans **Paramètres** > **Clés API**.
{% endalert %}

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous avez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec la permission `custom_objects.update`.

## Limite de débit {#rate-limit}

Cet endpoint fait partie du compartiment d'écriture des objets personnalisés avec une limite par défaut de 50 requêtes par minute.

## Paramètres de chemin {#path-parameters}

Le tableau suivant répertorie et décrit les paramètres de chemin pour l'endpoint `/custom_objects/objects/{type_name}/{external_id}`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `type_name` | Obligatoire | String | Nom machine du type d'objet personnalisé |
| `external_id` | Obligatoire | String | Identifiant de l'objet |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de chemin pour remplacer un objet personnalisé" }

## Paramètres de requête {#request-parameters}

Le tableau suivant répertorie et décrit les paramètres du corps de requête JSON pour l'endpoint `/custom_objects/objects/{type_name}/{external_id}`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `attributes` | Obligatoire | Objet | Attributs complets de l'objet. Les champs omis sont effacés |
| `display_name` | Facultatif | String | Libellé d'affichage de l'objet. Lorsque le type possède un champ source de nom d'affichage, la valeur de ce champ est prioritaire. Par défaut, `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête pour remplacer un objet personnalisé" }

## Exemple de requête {#example-request}

Cette section comprend un exemple de payload JSON et un exemple de requête cURL.

### Exemple de payload de requête {#sample-request-payload}

```json
{
  "attributes": {
    "name": "Updated Account"
  }
}
```

### Exemple de requête cURL {#sample-curl-request}

Cet exemple remplace les attributs stockés sur `acct-123` par ceux contenus dans le payload. Si aucun enregistrement avec cet identifiant n'existe, cette requête le crée.

```bash
curl --location --request PUT 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "attributes": {
    "name": "Updated Account"
  }
}'
```

## Réponse {#response}

Cette section comprend un exemple de réponse réussie et les champs de la réponse.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `200` peut renvoyer le corps de réponse suivant. Cet endpoint renvoie `200` que la requête ait créé ou remplacé l'objet.

```json
{
  "custom_object": {
    "type_name": "account",
    "external_id": "acct-123",
    "attributes": { "name": "Updated Account" }
  }
}
```

### Paramètres de réponse {#response-parameters}

Le tableau suivant répertorie et décrit les champs d'une réponse réussie.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `custom_object` | Obligatoire | Objet | Enregistrement d'objet personnalisé créé ou remplacé |
| `custom_object.type_name` | Obligatoire | String | Nom machine du type d'objet personnalisé |
| `custom_object.external_id` | Obligatoire | String | Identifiant de l'objet personnalisé |
| `custom_object.attributes` | Obligatoire | Objet | Attributs de l'objet stockés, indexés par nom de champ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de réponse pour remplacer un objet personnalisé" }

## Erreurs {#errors}

Le tableau suivant répertorie les erreurs courantes pour cet endpoint et la manière de les résoudre.

| Statut | Cause | Recommandation |
|---|---|---|
| `400` | Erreur de validation | Confirmez que chaque champ dans `attributes` existe dans le schéma du type et utilise le type de données correct. |
| `404` | Type introuvable (`custom-object-type-not-found`) | Confirmez que `type_name` existe dans l'espace de travail et correspond exactement au nom machine. |
| `422` | Limite d'enregistrements atteinte (`custom-object-record-limit-exceeded`) lorsque cette requête créerait un nouvel objet | Réduisez le nombre d'objets pour le type, ou contactez le support Braze concernant les limites de votre espace de travail. |
| `401` | Clé API REST manquante ou invalide | Vérifiez que l'en-tête `Authorization` utilise `Bearer YOUR_REST_API_KEY` et que la clé est active. |
| `403` | La clé API ne dispose pas des permissions nécessaires ou la requête est bloquée par la liste d'autorisation | Confirmez que la clé possède la permission `custom_objects.update` et que votre adresse IP source figure dans la liste d'autorisation de la clé, si elle est configurée. |
| `429` | Limite de débit dépassée | Réessayez après `X-RateLimit-Reset` et réduisez la fréquence des requêtes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erreurs pour remplacer un objet personnalisé" }
{% endapi %}