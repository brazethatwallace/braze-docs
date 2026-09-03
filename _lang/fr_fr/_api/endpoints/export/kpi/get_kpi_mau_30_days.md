---
nav_title: "GET : Exporter les utilisateurs actifs mensuels des 30 derniers jours"
article_title: "GET : Exporter les utilisateurs actifs mensuels des 30 derniers jours"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Exporter les utilisateurs actifs mensuels."

---
{% api %}
# Exporter les utilisateurs actifs mensuels des 30 derniers jours {#export-monthly-active-users-for-last-30-days}
{% apimethod get %}
/kpi/mau/data_series
{% endapimethod %}

> Utilisez cet endpoint pour récupérer une série quotidienne du nombre total d'utilisateurs actifs uniques sur une période glissante de 30 jours.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#68f45461-3bf1-425c-b918-f0bbf3f87149 {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec l'autorisation `kpi.mau.data_series`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| -------- | -------- | --------- | ----------- |
| `length` | Requis | Entier | Nombre maximum de jours avant `ending_at` à inclure dans la série renvoyée. Doit être compris entre 1 et 100 (inclus). |
| `ending_at` | Facultatif | Datetime <br>(chaîne [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Date à laquelle la série de données doit se terminer. Par défaut, correspond à l'heure de la requête. |
| `app_id` | Facultatif | Chaîne de caractères | Identifiant API de l'application, récupéré depuis la page [Clés API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers). Si omis, les résultats de toutes les applications de l'espace de travail seront renvoyés. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/kpi/mau/data_series?length=7&ending_at=2018-06-28T23:59:59-05:00&app_id={{app_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse {#response}

```json
{
    "message": (string) returns 'success' when the request completes without errors,
    "data" : [
        {
            "time" : (string) the date as ISO 8601 date,
            "mau" : (int) the number of monthly active users
        },
        ...
    ]
}
```

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, consultez la section [Résolution des problèmes d'exportation]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% endapi %}