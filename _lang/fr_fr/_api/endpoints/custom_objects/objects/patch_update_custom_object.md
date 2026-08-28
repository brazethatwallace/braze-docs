---
nav_title: "PATCH : Mettre à jour un objet personnalisé"
article_title: "PATCH : Mettre à jour un objet personnalisé"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Cet article décrit en détail l'endpoint de mise à jour d'un objet personnalisé."
---
{% api %}
# Mettre à jour un objet personnalisé {#update-custom-object}
{% apimethod patch %}
/custom_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Utilisez cet endpoint pour fusionner des attributs dans un objet personnalisé existant.

{% alert important %}
Les objets personnalisés sont actuellement en accès anticipé. Votre espace de travail doit être activé avant que les permissions de clé API pour les objets personnalisés n'apparaissent dans **Paramètres** > **Clés API**.
{% endalert %}

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec la permission `custom_objects.update`.

## Limite de débit {#rate-limit}

Cet endpoint fait partie du compartiment d'écriture des objets personnalisés avec une limite par défaut de 50 requêtes par minute.

## Paramètres de chemin {#path-parameters}

Le tableau suivant répertorie et décrit les paramètres de chemin pour l'endpoint `/custom_objects/objects/{type_name}/{external_id}`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `type_name` | Obligatoire | String | Nom machine du type d'objet personnalisé |
| `external_id` | Obligatoire | String | Identifiant de l'objet |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de chemin pour la mise à jour d'un objet personnalisé" }

## Paramètres de requête {#request-parameters}

Le tableau suivant répertorie et décrit les paramètres du corps de la requête JSON pour l'endpoint `/custom_objects/objects/{type_name}/{external_id}`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `attributes` | Obligatoire | Objet | Champs de premier niveau à fusionner |
| `display_name` | Facultatif | String | Libellé d'affichage de l'objet. Lorsque le type possède un champ source de nom d'affichage, la valeur de ce champ a la priorité. En cas d'omission, le nom d'affichage existant est conservé |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête pour la mise à jour d'un objet personnalisé" }

## Exemple de requête {#example-request}

Cette section comprend un exemple de payload JSON et un exemple de requête cURL.

### Exemple de payload de requête {#sample-request-payload}

```json
{
  "attributes": {
    "credits": 750
  }
}
```

### Exemple de requête cURL {#sample-curl-request}

Cet exemple met à jour l'attribut `credits` sur `acct-123` et laisse les autres attributs de l'enregistrement inchangés.

```bash
curl --location --request PATCH 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{ "attributes": { "credits": 750 } }'
```

## Réponse {#response}

Cette section comprend un exemple de réponse réussie et les champs de la réponse.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `200` peut renvoyer le corps de réponse suivant. L'objet `attributes` reflète le résultat de la fusion.

```json
{
  "custom_object": {
    "type_name": "account",
    "external_id": "acct-123",
    "attributes": { "name": "Acme", "credits": 750 }
  }
}
```

### Paramètres de réponse {#response-parameters}

Le tableau suivant répertorie et décrit les champs d'une réponse réussie.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `custom_object` | Obligatoire | Objet | Enregistrement de l'objet personnalisé mis à jour |
| `custom_object.type_name` | Obligatoire | String | Nom machine du type d'objet personnalisé |
| `custom_object.external_id` | Obligatoire | String | Identifiant de l'objet personnalisé |
| `custom_object.attributes` | Obligatoire | Objet | Attributs de l'objet après la fusion |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de réponse pour la mise à jour d'un objet personnalisé" }

## Erreurs {#errors}

Le tableau suivant répertorie les erreurs courantes pour cet endpoint et comment les résoudre.

| Statut | Cause | Recommandation |
|---|---|---|
| `400` | Erreur de validation | Vérifiez que chaque champ dans `attributes` existe dans le schéma du type et utilise le type de données correct. |
| `404` | Type introuvable ou objet introuvable | Vérifiez que `type_name` et `external_id` existent bien dans l'espace de travail. |
| `401` | Clé REST API manquante ou invalide | Vérifiez que l'en-tête `Authorization` utilise `Bearer YOUR_REST_API_KEY` et que la clé est active. |
| `403` | La clé API ne possède pas la permission ou la requête est bloquée par la liste d'autorisation | Vérifiez que la clé possède la permission `custom_objects.update` et que votre adresse IP source figure dans la liste d'autorisation de la clé, le cas échéant. |
| `429` | Limite de débit dépassée | Réessayez après `X-RateLimit-Reset` et réduisez la fréquence des requêtes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erreurs pour la mise à jour d'un objet personnalisé" }
{% endapi %}