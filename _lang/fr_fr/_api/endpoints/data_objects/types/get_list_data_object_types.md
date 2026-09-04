---
nav_title: "GET : Lister les types d'objets de données"
article_title: "GET : Lister les types d'objets de données"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Lister les types d'objets de données."
---
{% api %}
# Lister les types d'objets de données {#list-data-object-types}
{% apimethod get %}
/data_objects/types
{% endapimethod %}

> Utilisez cet endpoint pour lister les types d'objets de données dans un espace de travail.

{% alert important %}
Les objets de données sont actuellement en accès anticipé. Votre espace de travail doit être activé avant que les permissions de clé API pour les objets de données n'apparaissent dans **Paramètres** > **Clés API**.
{% endalert %}

## Prérequis {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec la permission `data_objects.read`.

## Limite de débit {#rate-limit}

Cet endpoint se trouve dans le compartiment de lecture des objets de données avec une limite par défaut de 50 requêtes par minute.

## Paramètres de requête {#query-parameters}

Le tableau suivant liste et décrit les paramètres de requête pour l'endpoint `/data_objects/types`.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `search_term` | Facultatif | String | Filtre de préfixe insensible à la casse sur le nom du type |
| `limit` | Facultatif | Integer | Taille de page. Valeur par défaut `100`. Limité de `1` à `250` |
| `offset` | Facultatif | Integer | Décalage. Valeur par défaut `0`. Les valeurs négatives sont ramenées à `0` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de requête pour lister les types d'objets de données" }

## Exemple de requête {#example-request}

Cette section comprend un exemple de payload de paramètres de requête et un exemple de requête cURL.

### Exemple de payload de requête {#sample-request-payload}

Utilisez cet objet JSON comme référence pour les paramètres de requête de cette requête.

```json
{
  "search_term": "acc",
  "limit": 2,
  "offset": 0
}
```

### Exemple de requête cURL {#sample-curl-request}

Cet exemple liste les types d'objets de données correspondant au terme de recherche `acc`, en renvoyant deux résultats par page.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/types?search_term=acc&limit=2&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Réponse {#response}

Cette section comprend un exemple de réponse réussie et les champs de la réponse.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `200` peut renvoyer le corps de réponse suivant.

```json
{
  "items": [
    {
      "type_name": "account",
      "metadata": { "display_name_source": "name" }
    },
    {
      "type_name": "contact",
      "metadata": {}
    }
  ],
  "total_count": 2,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

`metadata.display_name_source` est présent lorsqu'un champ de nom d'affichage est configuré pour le type.

### Paramètres de réponse {#response-parameters}

Le tableau suivant liste et décrit les champs d'une réponse réussie.

| Paramètre | Obligatoire | Type de données | Description |
|---|---|---|---|
| `items` | Obligatoire | Array | Liste des enregistrements de types d'objets de données |
| `items[].type_name` | Obligatoire | String | Nom machine du type d'objet de données |
| `items[].metadata` | Obligatoire | Object | Objet de métadonnées du type |
| `total_count` | Obligatoire | Integer | Nombre total d'enregistrements correspondants |
| `has_more` | Obligatoire | Boolean | Indique si une autre page de résultats est disponible |
| `next_offset` | Facultatif | Integer | Décalage pour la page suivante lorsque `has_more` est `true` |
| `offset` | Obligatoire | Integer | Décalage de la page actuelle |
| `limit` | Obligatoire | Integer | Taille de page utilisée par la requête |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de réponse pour lister les types d'objets de données" }

## Erreurs {#errors}

Le tableau suivant liste les erreurs courantes pour cet endpoint et comment les résoudre.

| Statut | Cause | Recommandation |
|---|---|---|
| `400` | Type ou valeur de paramètre de requête invalide | Assurez-vous que `limit` et `offset` sont des entiers et que toutes les valeurs de paramètres sont valides. |
| `401` | Clé REST API manquante ou invalide | Vérifiez que l'en-tête `Authorization` utilise `Bearer YOUR_REST_API_KEY` et que la clé est active. |
| `403` | La clé API ne dispose pas de la permission ou la requête est bloquée par la liste d'autorisation | Confirmez que la clé possède la permission `data_objects.read` et que votre adresse IP source figure sur la liste d'autorisation de la clé, si celle-ci est configurée. |
| `429` | Limite de débit dépassée | Réessayez après `X-RateLimit-Reset` et réduisez la fréquence des requêtes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erreurs pour lister les types d'objets de données" }
{% endapi %}