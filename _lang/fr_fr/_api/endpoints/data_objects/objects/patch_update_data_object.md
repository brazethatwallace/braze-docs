---
nav_title: "PATCH : Mettre à jour un objet de données"
article_title: "PATCH : Mettre à jour un objet de données"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Cet article décrit en détail l'endpoint Mettre à jour un objet de données."
---
{% api %}
# Mettre à jour un objet de données {#update-data-object}
{% apimethod patch %}
/data_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Utilisez cet endpoint pour fusionner des attributs dans un objet de données existant.

{% alert important %}
Les objets de données sont actuellement en accès anticipé. Votre espace de travail doit être activé avant que les permissions de clé API des objets de données n'apparaissent dans **Paramètres** > **Clés API**.
{% endalert %}

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec la permission `data_objects.update`.

## Limite de débit {#rate-limit}

Cet endpoint appartient au compartiment d'écriture des objets de données avec une limite par défaut de 50 requêtes par minute.

## Paramètres de chemin {#path-parameters}

Le tableau suivant répertorie et décrit les paramètres de chemin pour l'endpoint `/data_objects/objects/{type_name}/{external_id}`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `type_name` | Obligatoire | String | Nom machine du type d'objet de données |
| `external_id` | Obligatoire | String | Identifiant de l'objet |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de chemin pour la mise à jour d'un objet de données" }

## Paramètres de requête {#request-parameters}

Le tableau suivant répertorie et décrit les paramètres du corps de requête JSON pour l'endpoint `/data_objects/objects/{type_name}/{external_id}`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `attributes` | Obligatoire | Objet | Champs de premier niveau à fusionner |
| `display_name` | Facultatif | String | Libellé d'affichage de l'objet. Lorsque le type possède un champ source pour le nom d'affichage, la valeur de ce champ est prioritaire. S'il est omis, le nom d'affichage existant est conservé |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête pour la mise à jour d'un objet de données" }

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
curl --location --request PATCH 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123' \
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
  "data_object": {
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
| `data_object` | Obligatoire | Objet | Enregistrement de l'objet de données mis à jour |
| `data_object.type_name` | Obligatoire | String | Nom machine du type d'objet de données |
| `data_object.external_id` | Obligatoire | String | Identifiant de l'objet de données |
| `data_object.attributes` | Obligatoire | Objet | Attributs de l'objet après la fusion |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de réponse pour la mise à jour d'un objet de données" }

## Erreurs {#errors}

Le tableau suivant répertorie les erreurs courantes pour cet endpoint et comment les résoudre.

| Statut | Cause | Recommandation |
|---|---|---|
| `400` | Erreur de validation | Vérifiez que chaque champ dans `attributes` existe dans le schéma du type et utilise le type de données correct. |
| `404` | Type introuvable ou objet introuvable | Vérifiez que `type_name` et `external_id` existent tous les deux dans l'espace de travail. |
| `401` | Clé REST API manquante ou invalide | Vérifiez que l'en-tête `Authorization` utilise `Bearer YOUR_REST_API_KEY` et que la clé est active. |
| `403` | La clé API ne dispose pas de la permission ou la requête est bloquée par la liste d'autorisation | Vérifiez que la clé possède la permission `data_objects.update` et que votre adresse IP source figure dans la liste d'autorisation de la clé, si elle est configurée. |
| `429` | Limite de débit dépassée | Réessayez après `X-RateLimit-Reset` et réduisez la fréquence des requêtes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erreurs de mise à jour d'un objet de données" }
{% endapi %}