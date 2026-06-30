---
nav_title: "GET: Listar catálogos"
article_title: "GET: Listar catálogos"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Listar catálogos\"."

---
{% api %}
# Listar catálogos {#list-catalogs}
{% apimethod get %}
/catalogs
{% endapimethod %}

> Use esse endpoint para retornar uma lista de catálogos em um espaço de trabalho.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d65fb86-ccf7-423f-9eb2-f68ab36df824 {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key) com a permissão `catalogs.get`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='synchronous catalog' %}

## Parâmetros de caminho e de solicitação {#path-and-request-parameters}

Não há parâmetros de caminho ou de solicitação para esse endpoint.

## Exemplo de solicitação {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta {#response}

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `200` poderia retornar o seguinte corpo de resposta.

```json
{
  "catalogs": [
    {
      "description": "My Restaurants",
      "fields": [
        {
          "name": "id",
          "type": "string"
        },
        {
          "name": "Name",
          "type": "string"
        },
        {
          "name": "City",
          "type": "string"
        },
        {
          "name": "Cuisine",
          "type": "string"
        },
        {
          "name": "Rating",
          "type": "number"
        },
        {
          "name": "Loyalty_Program",
          "type": "boolean"
        },
        {
          "name": "Created_At",
          "type": "time"
        }
      ],
      "name": "restaurants",
      "num_items": 10,
      "updated_at": "2022-11-02T20:04:06.879+00:00"
    },
    {
      "description": "My Catalog",
      "fields": [
        {
          "name": "id",
          "type": "string"
        },
        {
          "name": "string_field",
          "type": "string"
        },
        {
          "name": "number_field",
          "type": "number"
        },
        {
          "name": "boolean_field",
          "type": "boolean"
        },
        {
          "name": "time_field",
          "type": "time"
        }
      ],
      "name": "my_catalog",
      "num_items": 3,
      "updated_at": "2022-11-02T09:03:19.967+00:00"
    }
  ],
  "message": "success"
}
```

{% endapi %}