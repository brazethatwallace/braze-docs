---
nav_title: "GET : Exporter le nombre d'achats"
article_title: "GET : Exporter le nombre d'achats"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Exporter le nombre d'achats."

---
{% api %}
# Exporter le nombre d'achats {#export-number-of-purchases}
{% apimethod get %}
/purchases/quantity_series
{% endapimethod %}

> Utilisez cet endpoint pour renvoyer le nombre total d'achats dans votre application sur une plage de temps.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6ac59282-d231-4317-88df-f7f12169b94e{% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key) avec l'autorisation `purchases.quantity_series`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `ending_at` | Facultatif | Datetime (chaîne de caractères [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Date à laquelle l'exportation de données doit se terminer. Par défaut, l'heure de la requête. |
| `length` | Requis | Entier | Nombre maximum de jours avant `ending_at` à inclure dans la série renvoyée. Doit être compris entre 1 et 100 (inclus). |
| `unit` | Facultatif | Chaîne de caractères | Unité de temps entre les points de données. Peut être « day » ou « hour », la valeur par défaut étant « day ». |
| `app_id` | Facultatif | Chaîne de caractères | Identifiant API de l'application récupéré à partir de la page [Clés API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers). Si ce paramètre est omis, les résultats de toutes les applications de l'espace de travail seront renvoyés. |
| `product` | Facultatif | Chaîne de caractères | Nom du produit par lequel filtrer la réponse. Si ce paramètre est omis, les résultats de toutes les applications seront renvoyés. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}

```
curl --location --request GET 'https://rest.iad-01.braze.com/purchases/quantity_series?length=100' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Réponse {#response}

```json
{
  "message": (required, string) the status of the export, returns 'success' when completed without errors,
  "data" : [
    {
      "time" : (string) the date as ISO 8601 date,
      "purchase_quantity" : (int) the number of items purchased in the time period
      },
    ...
  ]
}
```

{% endapi %}

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, consultez la section [Résolution des problèmes d'exportation]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}