---
nav_title: "DELETE: excluir item do catálogo"
article_title: "DELETE: excluir item do catálogo"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Este artigo descreve o endpoint da Braze \"Excluir item do catálogo\"."

---
{% api %}
# Excluir um item do catálogo {#delete-a-catalog-item}
{% apimethod delete %}
/catalogs/{catalog_name}/items/{item_id}
{% endapimethod %}

> Use esse endpoint para excluir um item do seu catálogo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#0dcce797-1346-472f-9384-082f14541689 {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key) com a permissão `catalogs.delete_item`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='synchronous catalog item' %}

## Parâmetros de caminho {#path-parameters}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
|---|---|---|---|
| `catalog_name` | Obrigatória | String | Nome do catálogo. |
| `item_id` | Obrigatória | String | O ID do item do catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de caminho" }

## Parâmetros de solicitação {#request-parameters}

Não há corpo de solicitação para esse endpoint.

## Exemplo de solicitação {#example-request}

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/items/restaurant1' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
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
      "id": "item-not-found",
      "message": "Could not find item",
      "parameters": [
        "item_id"
      ],
      "parameter_values": [
        "restaurant34"
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
| `arbitrary-error` | Ocorreu um erro arbitrário. Tente novamente ou entre em contato com o [Suporte]({{site.baseurl}}/support_contact). |
| `catalog-not-found` | Verifique se o nome do catálogo é válido. |
| `item-not-found` | Verifique se o item a ser excluído existe no seu catálogo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solução de problemas" }

{% endapi %}