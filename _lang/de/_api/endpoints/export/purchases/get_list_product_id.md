---
nav_title: "GET: Produkt-IDs exportieren"
article_title: "GET: Produkt-IDs exportieren"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze-Endpunkts „Produkt-IDs exportieren“."

---
{% api %}
# Produkt-IDs exportieren {#export-product-ids}
{% apimethod get %}
/purchases/product_list
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um eine paginierte Liste von Produkt-IDs zurückzugeben.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#dff4ed40-81f5-451d-9d44-accc0e932285{% endapiref %}

## Voraussetzungen {#prerequisites}

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key-permissions) mit der Berechtigung `purchases.product_list`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='purchases product list' %}

## Anfrageparameter {#request-parameters}

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| `page` | Optional | String | Die Seite Ihrer Produktliste, die Sie ansehen möchten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Anfrageparameter" }

## Beispielanfrage {#example-request}

{% raw %}
```
https://rest.iad-01.braze.com/purchases/product_list?page=1
```
{% endraw %}

## Antwort {#response}

```json
{
  "products": [
    "product_name" (string), the name of the product
  ],
  "message": (string) returns 'success' when the request completes without errors
}
```

{% endapi %}

{% alert tip %}
Hilfe zu CSV- und API-Exporten finden Sie unter [Fehlerbehebung beim Exportieren]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}