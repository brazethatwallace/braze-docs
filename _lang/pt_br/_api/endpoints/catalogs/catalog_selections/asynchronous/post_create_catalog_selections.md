---
nav_title: "POST: Criar seleção de catálogo"
article_title: "POST: Criar seleção de catálogo"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Criar seleção de catálogo\"."

---
{% API or interface de programação do aplicativo (API) %}
# Criar seleção de catálogo {#create-catalog-selection}
{% apimethod post %}
/catalogs/{catalog_name}/selections
{% endapimethod %}

> Use este endpoint para criar uma seleção em seu catálogo.

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `catalogs.create_selection`.

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog selections' %}

## Parâmetros de jornada {#path-parameters}

| Parâmetro      | Obrigatório | Tipo de dados | Descrição          |
| -------------- | -------- | --------- | -------------------- |
| `catalog_name` | Obrigatório | String    | Nome do catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Parâmetros de solicitação {#request-parameters}

| Parâmetro   | Obrigatório | Tipo de dados | Descrição                                                                                                                                                        |
| ----------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `selection` | Obrigatório | Objeto    | Um objeto que contém critérios de seleção. Consulte o [objeto de seleção de catálogo]({{site.baseurl}}/api/objects_filters/catalog_selection_object) para uma descrição completa do objeto e seus campos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Parâmetros do objeto de seleção {#selection-object-parameters}

| Parâmetro        | Obrigatório | Tipo de dados | Descrição                                                                                                                                                        |
| ---------------- | -------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `name`           | Obrigatório | String    | O nome da seleção de catálogo. |
| `description`    | Opcional | String    | Uma descrição da seleção de catálogo. |
| `external_id`    | Opcional | String    | Um identificador único para a seleção. |
| `source`         | Opcional | String    | A origem dos dados do catálogo. Para catálogos do Shopify, defina como `"Shopify"`. Os valores aceitos são `"Shopify"` e `"Braze"`. |
| `filters`        | Obrigatório | Array    | Um array de objetos de filtro a serem aplicados aos itens do catálogo. Você pode especificar até dez filtros por solicitação. Se um array de filtros vazio for fornecido, todos os itens do catálogo são incluídos. |
| `results_limit`  | Obrigatório | Inteiro   | O número máximo de resultados a retornar. Deve ser um número entre 1 e 50. |
| `sort_field`     | Opcional | String    | O campo para ordenar os resultados. Deve ser usado em conjunto com `sort_order`. Se `sort_field` e `sort_order` não estiverem presentes, os resultados são randomizados. |
| `sort_order`     | Opcional | String    | A ordem para classificar os resultados. Os valores aceitos são `"asc"` (crescente) ou `"desc"` (decrescente). Deve ser usado em conjunto com `sort_field`. Se `sort_field` e `sort_order` não estiverem presentes, os resultados são randomizados. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
Os parâmetros `sort_field` e `sort_order` devem ser usados juntos. Se você fornecer um sem o outro, ou se omitir ambos os parâmetros, os resultados da seleção são retornados em uma ordem aleatória.
{% endalert %}

## Exemplo de solicitação {#example-request}

```
curl --location --request POST 'https://rest.iad-03.braze.com/catalogs/restaurants/selections' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "selection": {
    "name": "favorite-restaurants",
    "description": "Favorite restaurants in NYC",
    "external_id": "favorite-nyc-restaurants",
    "source": "Braze",
    "filters": [
      {
        "field": "City",
        "operator": "equals",
        "value": "NYC"
      },
      {
        "field": "Rating",
        "operator": "greater than",
        "value": 7
      }
    ],
    "results_limit": 10,
    "sort_field": "Rating",
    "sort_order": "desc"
  }
}'
```

### Operadores de filtro {#filter-operators}

| Tipo de campo | Operadores compatíveis                                     |
| ---------- | ------------------------------------------------------- |
| `string`   | `equals`, `does not equal`                              |
| `number`   | `equals`, `does not equal`, `greater than`, `less than` |
| `boolean`  | `is`                                                    |
| `time`     | `before`, `after`                                       |
| `array`    | `includes value`, `does not include value`              |
| `geo`      | `geo within`, `geo outside`                             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
A API or interface de programação do aplicativo (API) aceita um máximo de dez filtros por solicitação de seleção. Os filtros são aplicados na ordem em que aparecem no array.
{% endalert %}

{% alert note %}
Quando você aplica um filtro `geo`, o sistema ordena automaticamente os resultados por distância, com o item mais próximo primeiro, independentemente dos parâmetros `sort_field` e `sort_order`.
{% endalert %}

## Resposta {#response}

Há três respostas de código de status para esse endpoint: `202`, `400` e `404`.

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
      "id": "catalog-not-found",
      "message": "Could not find catalog",
      "parameters": [
        "catalog_name"
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

| Erro                                 | Solução de problemas                                                                               |
|--------------------------------------|-----------------------------------------------------------------------------------------------|
| `catalog-not-found`                  | Verifique se o nome do catálogo é válido.                                                         |
| `company-size-limit-already-reached` | O limite de tamanho do armazenamento do catálogo foi atingido.                                                    |
| `selection-limit-reached`            | O limite de seleções do catálogo foi atingido.                                                      |
| `invalid-selection`                  | Verifique se a seleção é válida.                                                            |
| `too-many-filters`                   | Verifique se a seleção tem filtros demais.                                                  |
| `selection-name-already-exists`      | Verifique se o nome da seleção já existe no catálogo.                                    |
| `selection-has-invalid-filter`       | Verifique se o filtro da seleção é válido.                                                       |
| `selection-invalid-results-limit`    | Verifique se o limite de resultados da seleção é válido.                                                |
| `invalid-sorting`                    | Verifique se a ordenação da seleção é válida.                                                      |
| `invalid-sort-field`                 | Verifique se o campo de ordenação da seleção é válido.                                                   |
| `invalid-sort-order`                 | Verifique se a ordem de classificação da seleção é válida.                                                   |
| `selection-contains-too-many-arrays` | Verifique se a seleção contém mais de um campo com o tipo `array`. Apenas um é compatível. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}