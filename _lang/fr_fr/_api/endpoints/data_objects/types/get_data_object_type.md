---
nav_title: "GET : Obtenir un type d'objet de données"
article_title: "GET : Obtenir un type d'objet de données"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Obtenir un type d'objet de données."
---
{% api %}
# Obtenir un type d'objet de données {#get-data-object-type}
{% apimethod get %}
/data_objects/types/{type_name}
{% endapimethod %}

> Utilisez cet endpoint pour renvoyer un type d'objet de données et sa définition de schéma.

{% alert important %}
Les objets de données sont actuellement en accès anticipé. Votre espace de travail doit être activé avant que les permissions de clé API des objets de données n'apparaissent dans **Paramètres** > **Clés API**.
{% endalert %}

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec la permission `data_objects.read`.

## Limite de débit {#rate-limit}

Cet endpoint fait partie du compartiment de lecture des objets de données avec une limite par défaut de 50 requêtes par minute.

## Paramètres de chemin {#path-parameters}

Le tableau suivant répertorie et décrit les paramètres de chemin pour l'endpoint `/data_objects/types/{type_name}`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `type_name` | Obligatoire | String | Nom machine du type d'objet de données |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de chemin pour obtenir un type d'objet de données" }

## Exemple de requête {#example-request}

Cette section comprend un exemple de payload de paramètre de chemin et un exemple de requête cURL.

### Exemple de payload de requête {#sample-request-payload}

Utilisez cet objet JSON comme référence pour le paramètre de chemin de cette requête.

```json
{
  "type_name": "account"
}
```

### Exemple de requête cURL {#sample-curl-request}

Cet exemple récupère la définition du type d'objet de données `account`.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/types/account' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Réponse {#response}

Cette section comprend un exemple de réponse réussie et les champs de réponse.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `200` pourrait renvoyer le corps de réponse suivant.

```json
{
  "data_object_type": {
    "type_name": "account",
    "metadata": { "display_name_source": "name" },
    "schema_def": {
      "type": "object",
      "properties": {
        "name": { "type": "string", "title": "Name" },
        "industry": { "type": "string", "title": "Industry" },
        "renewal_date": { "type": "string", "format": "date-time", "title": "Renewal date" }
      },
      "required": ["name"]
    }
  }
}
```

`schema_def` décrit les champs autorisés pour l'objet. Les écritures rejettent toujours les champs non déclarés, même si ce schéma de réponse est descriptif.

### Paramètres de réponse {#response-parameters}

Le tableau suivant répertorie et décrit les champs d'une réponse réussie.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `data_object_type` | Obligatoire | Objet | Enregistrement du type d'objet de données renvoyé |
| `data_object_type.type_name` | Obligatoire | String | Nom machine du type d'objet de données |
| `data_object_type.metadata` | Obligatoire | Objet | Objet de métadonnées du type |
| `data_object_type.schema_def` | Obligatoire | Objet | Définition de schéma JSON pour les attributs de l'objet |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de réponse pour obtenir un type d'objet de données" }

## Erreurs {#errors}

Le tableau suivant répertorie les erreurs courantes pour cet endpoint et comment les résoudre.

| Statut | Cause | Recommandation |
|---|---|---|
| `404` | Type non trouvé (`data-object-type-not-found`) | Vérifiez que `type_name` existe dans l'espace de travail et correspond exactement au nom machine. |
| `401` | Clé API REST manquante ou invalide | Vérifiez que l'en-tête `Authorization` utilise `Bearer YOUR_REST_API_KEY` et que la clé est active. |
| `403` | La clé API ne dispose pas de la permission ou la requête est bloquée par la liste d'autorisation | Vérifiez que la clé dispose de la permission `data_objects.read` et que votre adresse IP source figure sur la liste d'autorisation de la clé, si elle est configurée. |
| `429` | Limite de débit dépassée | Réessayez après `X-RateLimit-Reset` et réduisez la fréquence des requêtes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erreurs pour obtenir un type d'objet de données" }
{% endapi %}