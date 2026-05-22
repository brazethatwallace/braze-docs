---
nav_title: "DELETE : Supprimer un catalogue"
article_title: "DELETE : Supprimer un catalogue"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Supprimer un catalogue."

---
{% api %}
# Supprimer un catalogue {#delete-catalog}
{% apimethod delete %}
/catalogs/{catalog_name}
{% endapimethod %}

> Utilisez cet endpoint pour supprimer un catalogue.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c0915a86-797a-4486-8217-24cd1c689d0f {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l'autorisation `catalogs.delete`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='synchronous catalog' %}

## Paramètres de chemin {#path-parameters}

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `catalog_name` | Requis | Chaîne de caractères | Nom du catalogue. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Paramètres de chemin" }

## Exemple de requête {#example-request}

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
```

## Réponse {#response}

Deux codes de statut sont possibles pour cet endpoint : `200` et `404`.

### Exemple de réponse réussie {#example-success-response}

Le code de statut `200` pourrait renvoyer le corps de réponse suivant :

```json
{
  "message": "success"
}
```

### Exemple de réponse échouée {#example-error-response}

Le code de statut `404` pourrait renvoyer le corps de réponse suivant. Consultez la section [Résolution des problèmes](#troubleshooting) pour plus d'informations concernant les erreurs que vous pourriez rencontrer.

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

Le tableau suivant répertorie les erreurs renvoyées possibles et les étapes de résolution des problèmes associées.

| Erreur | Résolution des problèmes |
| --- | --- |
| `catalog-not-found` | Vérifiez que le nom du catalogue est valide. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Résolution des problèmes" }

{% endapi %}