---
nav_title: "GET : Exporter les ID de produit"
article_title: "GET : Exporter les ID de produit"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Cet article présente en détail l'endpoint Braze Exporter les ID de produit."

---
{% api %}
# Exporter les ID de produit {#export-product-ids}
{% apimethod get %}
/purchases/product_list
{% endapimethod %}

> Utilisez cet endpoint pour renvoyer une liste paginée d'ID de produit.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#dff4ed40-81f5-451d-9d44-accc0e932285{% endapiref %}

## Conditions préalables {#prerequisites}

Pour utiliser cet endpoint, vous aurez besoin d'une [clé API]({{site.baseurl}}/api/basics#rest-api-key/) avec l'autorisation `purchases.product_list`.

## Limite de débit {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## Paramètres de requête {#request-parameters}

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `page` | Facultatif | Chaîne de caractères | La page de votre liste de produits que vous souhaitez consulter. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Paramètres de requête" }

## Exemple de requête {#example-request}

{% raw %}
```
https://rest.iad-01.braze.com/purchases/product_list?page=1
```
{% endraw %}

## Réponse {#response}

```json
{
  "products": [
    "product_name" (string), the name of the product
  ],
  "message": "success"
}
```

{% endapi %}

{% alert tip %}
Pour obtenir de l'aide sur les exportations CSV et API, consultez la section [Résolution des problèmes d'exportation]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/).
{% endalert %}