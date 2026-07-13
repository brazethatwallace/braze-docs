---
nav_title: "GET : Exporter la liste des segments"
article_title: "GET : Exporter la liste des segments"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Exporter la liste des segments."

---
{% api %}
# Exporter la liste des segments {#export-segment-list}
{% apimethod get %}
/segments/list
{% endapimethod %}

> Utilisez cet endpoint pour exporter une liste de segments, chacun incluant son nom, son identifiant API de segment et l'état d'activation du suivi analytique.

Les segments sont renvoyés par groupes de 100, triés par date de création (du plus ancien au plus récent par défaut). Les segments archivés ne sont pas inclus.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1349e6f4-3ce7-4e60-b3e9-951c99c0993f {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key) avec l'autorisation `segments.list`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| -------- | -------- | --------- | ----------- |
| `page` | Facultatif | Entier | La page de segments à renvoyer, par défaut 0 (renvoie le premier ensemble pouvant contenir jusqu'à 100 éléments). |
| `sort_direction` | Facultatif | Chaîne de caractères | - Trier par date de création du plus récent au plus ancien : indiquez la valeur `desc`.<br> - Trier par date de création du plus ancien au plus récent : indiquez la valeur `asc`. <br><br>Si `sort_direction` n'est pas inclus, l'ordre par défaut est du plus ancien au plus récent. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/segments/list?page=1&sort_direction=desc' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse {#response}

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "segments" : [
        {
            "id" : (string) the Segment API identifier,
            "name" : (string) segment name,
            "analytics_tracking_enabled" : (boolean) whether the segment has analytics tracking enabled,
            "tags" : (array) the tag names associated with the segment formatted as strings
        },
        ...
    ]
}
```

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, consultez la section [Résolution des problèmes d'exportation]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% endapi %}