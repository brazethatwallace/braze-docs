---
nav_title: "PATCH: Editar item do catálogo"
article_title: "PATCH: Editar item do catálogo"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Editar item do catálogo\"."

---
{% api %}
# Editar item do catálogo {#edit-catalog-item}
{% apimethod patch %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> Use esse endpoint para editar um item existente em seu catálogo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e35976ae-ff77-42b7-b691-a883c980d8c0 {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `catalogs.update_item`.

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## Parâmetros de caminho {#path-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `catalog_name` | Obrigatório | String | Nome do catálogo. |
| `item_id` | Obrigatório | String | O ID do item do catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de caminho" }

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `items` | Obrigatório | Vetor | Um vetor que contém objetos de item. Os objetos de item devem conter campos que existem no catálogo, exceto o campo `id`. Somente um objeto de item é permitido por solicitação. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Exemplo de solicitação {#example-request}

```
curl --location --request PATCH 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "Name": "Restaurant",
      "Loyalty_Program": false,
      "Location": [-73.988103, 40.779109],
      "Preferences": {
        "favorite_brand": "Nike",
        "shirt_size": "L"
      },
      "Top_Dishes": {
        "$add": [
          "Biscuits",
          "Coleslaw"
        ],
        "$remove": [
          "French Fries"
        ]
      },
      "Open_Time": "2021-09-03T09:03:19.967+00:00"
    }
  ]
}'
```

{% alert note %}
- O campo `Location` usa o tipo de dados `geo`, que espera um vetor formatado como `[longitude, latitude]`.
- Os operadores `$add` e `$remove` são aplicáveis somente a campos do tipo vetor e são compatíveis apenas com endpoints PATCH.
{% endalert %}

## Resposta {#response}

Há três respostas de código de status para esse endpoint: `200`, `400` e `404`.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `200` poderia retornar o seguinte corpo de resposta.

```json
{
  "message": "success"
}
```

### Exemplo de resposta de erro {#example-error-response}

O código de status `400` poderia retornar o seguinte corpo de resposta. Consulte [Solução de problemas](#troubleshooting) para saber mais sobre os erros que você pode encontrar.

```json
{
  "errors": [
    {
      "id": "invalid-fields",
      "message": "Some of the fields given do not exist in the catalog",
      "parameters": [
        "id"
      ],
      "parameter_values": [
        "restaurant1"
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
| `arbitrary-error` | Ocorreu um erro arbitrário. Tente novamente ou entre em contato com o [suporte]({{site.baseurl}}/support_contact). |
| `catalog-not-found` | Verifique se o nome do catálogo é válido. |
| `filtered-set-field-too-long` | O valor do campo está sendo usado em um conjunto filtrado que excede o limite de caracteres de um item. |
| `id-in-body` | Já existe um ID de item no catálogo. |
| `ids-too-large` | O limite de caracteres para cada ID de item é de 250 caracteres. |
| `invalid-ids` | Os caracteres compatíveis com os nomes de ID de item são letras, números, hífens e sublinhados. |
| `invalid-fields` | Confirme se os campos da solicitação existem no catálogo. |
| `invalid-keys-in-value-object` | As chaves de objeto do item não podem incluir `.` ou `$`. |
| `item-not-found` | Verifique se o item está no catálogo. |
| `item-array-invalid` | `items` deve ser um vetor de objetos. |
| `items-too-large` | O limite de caracteres para cada item é de 5.000 caracteres. |
| `request-includes-too-many-items` | Você só pode editar um item do catálogo por solicitação. |
| `too-deep-nesting-in-value-object` | Os objetos de item não podem ter mais de 50 níveis de aninhamento. |
| `unable-to-coerce-value` | Os tipos de itens não podem ser convertidos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solução de problemas" }

{% endapi %}