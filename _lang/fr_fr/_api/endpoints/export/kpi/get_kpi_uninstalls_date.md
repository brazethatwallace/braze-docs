---
nav_title: "GET : Exporter les KPI pour les désinstallations quotidiennes d'application par date"
article_title: "GET : Exporter les KPI pour les désinstallations quotidiennes d'application par date"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Exporter les désinstallations quotidiennes d'application par date."

---
{% api %}
# Exporter les KPI pour les désinstallations quotidiennes d'application par date {#export-kpis-for-daily-app-uninstalls-by-date}
{% apimethod get %}
/kpi/uninstalls/data_series
{% endapimethod %}

> Utilisez cet endpoint pour récupérer une série quotidienne du nombre total de désinstallations pour chaque date.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#59c4d592-3e77-42f8-8ff1-d5d250acbeae {% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key) avec l'autorisation `kpi.uninstalls.data_series`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
| -------- | -------- | --------- | ----------- |
| `length` | Requis | Entier | Nombre maximum de jours avant `ending_at` à inclure dans la série renvoyée. Doit être compris entre 1 et 100 (inclus). |
| `ending_at` | Facultatif | Datetime <br>(chaîne [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Date à laquelle la série de données doit se terminer. Par défaut, correspond à l'heure de la requête. |
| `app_id` | Facultatif | Chaîne de caractères | Identifiant API de l'application, récupéré depuis la page [Clés API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers). Si omis, les résultats pour toutes les applications de l'espace de travail seront renvoyés. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/kpi/uninstalls/data_series?length=14&ending_at=2018-06-28T23:59:59-5:00&app_id={{app_identifier}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse {#response}

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) the date as ISO 8601 date,
            "uninstalls" : (int) the number of uninstalls
        },
        ...
    ]
}
```

{% multi_lang_include alerts/tip_alerts.md alert='Export troubleshooting' %}

{% endapi %}