---
nav_title: "DELETE : Supprimer la sélection du catalogue"
article_title: "DELETE : Supprimer la sélection du catalogue"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Braze Supprimer la sélection du catalogue."

---
{% api %}
# Supprimer la sélection du catalogue {#delete-catalog-selection}
{% apimethod delete %}
/catalogs/{catalog_name}/selections/{selection_name}
{% endapimethod %}

> Utilisez cet endpoint pour supprimer une sélection de catalogue.

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec l'autorisation `catalogs.delete_selection`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog selections' %}

## Paramètres de chemin {#path-parameters}

| Paramètre | Requis | Type de données | Description |
| ---------------- | -------- | --------- | ------------------------------ |
| `catalog_name` | Requis | Chaîne de caractères | Nom du catalogue. |
| `selection_name` | Requis | Chaîne de caractères | Nom de la sélection du catalogue. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de chemin" }

## Exemple de requête {#example-request}

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/selections/favorite_list' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
```

## Réponse {#response}

Il existe deux codes de statut de réponse pour cet endpoint : `202` et `404`.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `202` pourrait renvoyer le corps de réponse suivant :

```json
{
  "message": "success"
}
```

### Exemple de réponse échouée {#example-error-response}

Le code de statut `404` pourrait renvoyer le corps de réponse suivant. Consultez la section [Résolution des problèmes](#troubleshooting) pour plus d'informations sur les erreurs que vous pourriez rencontrer.

```json
{
  "errors": [
    {
      "id": "catalog-not-found",
      "message": "Could not find catalog",
      "parameters": [
        "catalog_name"
      ],
      "parameter_values": [
        "restaurants"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## Résolution des problèmes {#troubleshooting}

Le tableau suivant répertorie les erreurs possibles et les étapes de résolution associées.

| Erreur | Résolution des problèmes |
| -------------------- | -------------------------------------------------------- |
| `catalog-not-found` | Vérifiez que le nom du catalogue est valide. |
| `invalid-selection` | Vérifiez que le nom de la sélection est valide. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Résolution des problèmes" }

{% endapi %}