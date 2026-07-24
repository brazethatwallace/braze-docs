---
nav_title: "GET : Exporter les données de chiffre d'affaires"
article_title: "GET : Exporter les données de chiffre d'affaires"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Exporter les données de chiffre d'affaires."

---
{% api %}
# Exporter les données de chiffre d'affaires par période {#export-revenue-data-by-time}
{% apimethod get %}
/purchases/revenue_series
{% endapimethod %}

> Utilisez cet endpoint pour renvoyer le montant total dépensé dans votre application sur une plage de temps.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f6e05f9a-13c0-4d66-8caa-4a376d25749f{% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key-permissions) avec l'autorisation `purchases.revenue_series`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `ending_at` | Facultatif | Datetime (chaîne de caractères [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Date à laquelle l'exportation de données doit se terminer. Par défaut, correspond à l'heure de la requête. |
| `length` | Requis | Entier | Nombre maximum de jours avant `ending_at` à inclure dans la série renvoyée. Doit être compris entre 1 et 100 (inclus). |
| `unit` | Facultatif | Chaîne de caractères | Unité de temps entre les points de données. Peut être « day » ou « hour », la valeur par défaut étant « day ». |
| `app_id` | Facultatif | Chaîne de caractères | Identifiant API de l'application récupéré à partir de la page [Clés API et identifiants]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers). Si ce paramètre est omis, les résultats de toutes les applications de l'espace de travail seront renvoyés. |
| `product` | Facultatif | Chaîne de caractères | Nom du produit par lequel filtrer la réponse. Si ce paramètre est omis, les résultats de toutes les applications seront renvoyés. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}

```
curl --location --request GET 'https://rest.iad-01.braze.com/purchases/revenue_series?length=100' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse {#response}

```json
{
  "message": (required, string) the status of the export, returns 'success' when completed without errors,
  "data" : [
    {
      "time" : (string) the date as ISO 8601 date,
      "revenue" : (int) amount of revenue for the time period
      },
    ...
  ]
}
```

{% endapi %}

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, consultez la section [Résolution des problèmes d'exportation]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}