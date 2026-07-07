---
nav_title: "GET : Liste des Content Blocks disponibles"
article_title: "GET : Lister les Content Blocks disponibles"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze permettant de lister les Content Blocks disponibles."

---
{% api %}
# Lister les Content Blocks disponibles {#list-available-content-blocks}
{% apimethod get %}
/content_blocks/list
{% endapimethod %}

> Utilisez cet endpoint pour lister les informations relatives à vos [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) existants.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d87048f-68fd-46c9-aa15-3a970e99540e {% endapiref %}

## Conditions préalables {#prerequisites}
Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/api_key) avec l'autorisation `content_blocks.list`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `modified_after` | Facultatif | Chaîne de caractères au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) | Récupérer uniquement les Content Blocks mis à jour à partir de la date et de l'heure indiquées. |
| `modified_before` | Facultatif | Chaîne de caractères au format [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) | Récupérer uniquement les Content Blocks mis à jour au plus tard à la date et à l'heure indiquées. |
| `limit` | Facultatif | Nombre positif | Nombre maximum de Content Blocks à récupérer. Par défaut à 100 si non renseigné, avec une valeur maximale acceptable de 1 000. |
| `offset` | Facultatif | Nombre positif | Nombre de Content Blocks à ignorer avant de renvoyer le reste des modèles correspondant aux critères de recherche. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/content_blocks/list?modified_after=2020-01-01T01:01:01.000000&modified_before=2020-02-01T01:01:01.000000&limit=100&offset=1' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Réponse {#response}

```json
{
  "count": "integer",
  "content_blocks": [
    {
      "content_block_id": (string) the Content Block identifier,
      "name": (string) the name of the Content Block,
      "content_type": (string) the content type, html or text,
      "liquid_tag": (string) the Liquid tags,
      "inclusion_count" : (integer) the inclusion count,
      "created_at": (string) The time the Content Block was created in ISO 8601,
      "last_edited": (string) The time the Content Block was last edited in ISO 8601,
      "tags": (array) An array of tags formatted as strings
    }
  ]
}
```

## Résolution des problèmes {#troubleshooting}

Le tableau suivant répertorie les erreurs possibles et les étapes de résolution associées.

| Erreur | Résolution des problèmes |
| --- | --- |
| `Modified after time is invalid` | La date fournie n'est pas une date valide ou analysable. Reformatez cette valeur en tant que chaîne de caractères au format ISO 8601 (`yyyy-mm-ddThh:mm:ss.ffffff`). |
| `Modified before time is invalid` | La date fournie n'est pas une date valide ou analysable. Reformatez cette valeur en tant que chaîne de caractères au format ISO 8601 (`yyyy-mm-ddThh:mm:ss.ffffff`). |
| `Modified after time must be earlier than or the same as modified before time.` | Modifiez la valeur `modified_after` pour qu'elle soit antérieure à la valeur `modified_before`. |
| `Content Block number limit is invalid` | Le paramètre `limit` doit être un entier (nombre positif) supérieur à 0. |
| `Content Block number limit must be greater than 0` | Modifiez le paramètre `limit` pour qu'il soit un entier supérieur à 0. |
| `Content Block number limit exceeds maximum of 1000` | Modifiez le paramètre `limit` pour qu'il soit un entier inférieur à 1 000. |
| `Offset is invalid` | Le paramètre `offset` doit être un entier supérieur à 0. |
| `Offset must be greater than 0` | Modifiez le paramètre `offset` pour qu'il soit un entier supérieur à 0. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Résolution des problèmes" }

{% endapi %}