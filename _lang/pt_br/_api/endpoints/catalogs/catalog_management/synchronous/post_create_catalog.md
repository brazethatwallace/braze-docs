---
nav_title: "POST: Criar catálogo"
article_title: "POST: Criar catálogo"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Criar catálogo da Braze."

---
{% api %}
# Criar catálogo {#create-catalog}
{% apimethod post %}
/catalogs
{% endapimethod %}

> Use este endpoint para criar um catálogo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#af9f3e2d-b7e7-49e7-aa64-f4652892be6e {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `catalogs.create`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='synchronous catalog' %}

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `catalogs` | Obrigatória | Array | Um array que contém objetos de catálogo. Somente um objeto de catálogo é permitido para esta solicitação. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Request parameters" }

### Parâmetros do objeto de catálogo {#catalog-object-parameters}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `name` | Obrigatória | String | O nome do catálogo que você deseja criar. |
| `description` | Obrigatória | String | A descrição do catálogo que você deseja criar. |
| `fields` | Obrigatória | Array | Um array de objetos em que o objeto contém as chaves `name` e `type`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Catalog object parameters" }

## Exemplo de solicitação {#example-request}
```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "catalogs": [
    {
      "name": "restaurants",
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
          "name": "Location",
          "type": "geo"
        },
        {
          "name": "Preferences",
          "type": "object"
        },
        {
          "name": "Top_Dishes",
          "type": "array"
        },
        {
          "name": "Created_At",
          "type": "time"
        }
      ]
    }
  ]
}'
```

{% alert note %}
O tipo de dados `geo` armazena uma coordenada geográfica como um array formatado como `[longitude, latitude]`. Por exemplo, `[-73.988103, 40.779109]`.
{% endalert %}

## Resposta {#response}

Existem dois códigos de status para este endpoint: `201` e `400`.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `201` pode retornar o seguinte corpo de resposta.

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
          "name": "Location",
          "type": "geo"
        },
        {
          "name": "Preferences",
          "type": "object"
        },
        {
          "name": "Top_Dishes",
          "type": "array"
        },
        {
          "name": "Created_At",
          "type": "time"
        }
      ],
      "name": "restaurants",
      "num_items": 0,
      "updated_at": "2022-11-02T20:04:06.879+00:00"
    }
  ],
  "message": "success"
}
```

### Exemplo de resposta de erro {#example-error-response}

O código de status `400` pode retornar o seguinte corpo de resposta. Consulte [Solução de problemas](#troubleshooting) para saber mais sobre os erros que você pode encontrar.

```json
{
  "errors": [
    {
      "id": "catalog-name-already-exists",
      "message": "A catalog with that name already exists",
      "parameters": [
        "name"
      ],
      "parameter_values": [
        "restaurants"
      ]
    }
  ],
  "message": "Invalid Request"
}
```

## Solução de problemas {#troubleshooting}

A tabela a seguir lista os possíveis erros retornados e as etapas de solução de problemas associadas.

| Erro | Solução de problemas |
| --- | --- |
| `catalog-array-invalid` | `catalogs` deve ser um array de objetos. |
| `catalog-name-already-exists` | Já existe um catálogo com esse nome. |
| `catalog-name-too-large` | O limite de caracteres para um nome de catálogo é 250. |
| `description-too-long` | O limite de caracteres para a descrição é 250. |
| `field-names-not-unique` | O mesmo nome de campo é referenciado duas vezes. |
| `field-names-too-large` | O limite de caracteres para um nome de campo é 250. |
| `id-not-first-column` | O `id` deve ser o primeiro campo no array. Verifique se o tipo é uma string. |
| `invalid-catalog-name` | O nome do catálogo só pode incluir letras, números, hífens e sublinhados. |
| `invalid-field-names` | Os campos só podem incluir letras, números, hífens e sublinhados. |
| `invalid-field-types` | Verifique se os tipos de campo são válidos. |
| `invalid-fields` | `fields` não está formatado corretamente. |
| `too-many-catalog-atoms` | Você só pode criar um catálogo por solicitação. |
| `too-many-fields` | O limite de número de campos é 500. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

{% endapi %}