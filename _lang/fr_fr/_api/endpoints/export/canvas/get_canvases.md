---
nav_title: "GET : Exporter la liste des Canvas"
article_title: "GET : Exporter la liste des Canvas"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Exporter la liste des Canvas."

---
{% api %}
# Exporter la liste des Canvas {#export-canvas-list}
{% apimethod get %}
/canvas/list
{% endapimethod %}

> Utilisez cet endpoint pour exporter une liste de Canvas, y compris le nom, l'identifiant API du Canvas et les tags associés.

Les Canvas sont renvoyés par groupes de 100 triés par date de création (des plus anciens aux plus récents par défaut).

Les Canvas archivés ne seront pas inclus dans la réponse API, sauf si le champ `include_archived` est spécifié. En revanche, les Canvas arrêtés, mais non archivés seront renvoyés par défaut.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e6c150d7-fceb-4b10-91e2-a9ca4d5806d1 {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec l'autorisation `canvas.list`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| --------- | -------- | --------- | ----------- |
| `page` | Facultatif | Entier | La page de Canvas à renvoyer, par défaut `0` (renvoie le premier ensemble de 100 éléments maximum). |
| `include_archived` | Facultatif | Booléen | Indique s'il faut inclure ou non les Canvas archivés, par défaut `false`. |
| `sort_direction` | Facultatif | Chaîne de caractères | - Trier par date de création de la plus récente à la plus ancienne : indiquer la valeur `desc`.<br> - Trier par date de création de la plus ancienne à la plus récente : indiquer la valeur `asc`. <br><br>Si `sort_direction` n'est pas inclus, l'ordre par défaut est du plus ancien au plus récent. |
| `last_edit.time[gt]` | Facultatif | Date | Filtre les résultats et renvoie uniquement les Canvas modifiés après l'heure indiquée. Le format est `yyyy-MM-DDTHH:mm:ss`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/list?page=1&include_archived=false&sort_direction=desc&last_edit.time[gt]=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse {#response}

```json
{
  "canvases" : [
  	{
  		"id" : (string) the Canvas API identifier,
  		"last_edited": (ISO 8601 string) the last edited time for the message,
  		"name" : (string) the Canvas name,
  		"tags" : (array) the tag names associated with the Canvas formatted as strings,
  	},
    ... (more Canvases)
  ],
  "message": (string) returns 'success' when the request completes without errors
}
```

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, consultez la section [Résolution des problèmes d'exportation]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% endapi %}