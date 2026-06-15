---
nav_title: "DELETE: Excluir vários itens do catálogo"
article_title: "DELETE: Excluir vários itens do catálogo"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Excluir vários itens do catálogo\"."

---
{% api %}
# Excluir vários itens do catálogo {#delete-multiple-catalog-items}
{% apimethod delete %}
/catalogs/{catalog_name}/items
{% endapimethod %}

> Use esse endpoint para excluir vários itens do seu catálogo.

Cada solicitação pode suportar até 50 itens. Esse endpoint é assíncrono.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#647c82e8-8b38-4df2-bde2-b1d8e19fd332 {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `catalogs.delete_items`.

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
| `items` | Obrigatória | Vetor | Um vetor que contém objetos de item. Os objetos de item devem conter um `id` referenciando os itens que a Braze deve excluir. São permitidos até 50 objetos de item por solicitação. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Request parameters" }

## Exemplo de solicitação {#example-request}

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {"id": "restaurant1"},
    {"id": "restaurant2"},
    {"id": "restaurant3"}
  ]
}'
```

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
      "id": "items-missing-ids",
      "message": "There are 1 item(s) that do not have ids",
      "parameters": [],
      "parameter_values": []
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
| `ids-not-unique` | Verifique se os IDs de item são exclusivos na solicitação. |
| `ids-not-strings` | Os IDs de item devem ser do tipo string. |
| `items-missing-ids` | Alguns itens não têm IDs de item. Verifique se cada item tem um ID de item. |
| `invalid-ids` | Os IDs de item só podem conter letras, números, hifens e underscores. |
| `request-includes-too-many-items` | Sua solicitação tem muitos itens. O limite de itens por solicitação é de 50. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }

{% endapi %}