---
nav_title: "PATCH: Editar vários itens do catálogo"
article_title: "PATCH: Editar vários itens do catálogo"
alias: /catalogs_items_patch/
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Editar vários itens do catálogo\"."

---
{% api %}
# Editar vários itens do catálogo {#edit-multiple-catalog-items}
{% apimethod patch %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Use este endpoint para editar vários itens existentes em seu catálogo.

Cada solicitação pode suportar até 50 itens. Este endpoint é assíncrono.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#03f3548e-4139-4f60-812d-7e1a695a738a {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `catalogs.update_items`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog item' %}

## Parâmetros de jornada {#path-parameters}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `catalog_name` | Obrigatória | String | Nome do catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Path parameters" }

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `items` | Obrigatória | Vetor | Um vetor que contém objetos de item. Os objetos de item devem conter campos que existem no catálogo. São permitidos até 50 objetos de item por solicitação. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Request parameters" }

## Exemplo de solicitação {#example-request}

```
curl --location --request PATCH 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {
      "id": "restaurant1",
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
    },
    {
      "id": "restaurant3",
      "City": "San Francisco",
      "Rating": 2,
      "Top_Dishes": [
        "Buffalo Wings",
        "Philly Cheesesteak"
      ]
    }
  ]
}'
```

{% alert note %}
- O campo `Location` usa o tipo de dados `geo`, que espera um vetor formatado como `[longitude, latitude]`.
- Os operadores `$add` e `$remove` são aplicáveis somente a campos do tipo vetor e são compatíveis apenas com endpoints PATCH.
{% endalert %}

## Resposta {#response}

Há três respostas de código de status para este endpoint: `202`, `400` e `404`.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `202` poderia retornar o seguinte corpo de resposta.

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
| `catalog-not-found` | Verifique se o nome do catálogo é válido. |
| `ids-too-large` | Os IDs de item não podem ter mais de 250 caracteres. |
| `ids-not-strings` | Os IDs de item devem ser do tipo string. |
| `ids-not-unique` | Os IDs de item devem ser exclusivos na solicitação. |
| `invalid-ids` | Os IDs de item só podem conter letras, números, hifens e underscores. |
| `invalid-fields` | Confirme se todos os campos que está enviando na solicitação de API já existem no catálogo. Isso não está relacionado ao campo ID mencionado no erro. |
| `invalid-keys-in-value-object` | As chaves de objeto do item não podem incluir `.` ou `$`. |
| `items-missing-ids` | Alguns itens não têm IDs de item. Verifique se cada item tem um ID de item. |
| `item-array-invalid` | `items` deve ser um vetor de objetos. |
| `items-too-large` | Os valores dos itens não podem exceder 5.000 caracteres. |
| `request-includes-too-many-items` | Sua solicitação tem muitos itens. O limite de itens por solicitação é de 50. |
| `too-deep-nesting-in-value-object` | Os objetos de item não podem ter mais de 50 níveis de aninhamento. |
| `unable-to-coerce-value` | Os tipos de item não podem ser convertidos. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

{% endapi %}