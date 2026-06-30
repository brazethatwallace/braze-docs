---
nav_title: "DELETE: Excluir seleção de catálogo"
article_title: "DELETE: Excluir seleção de catálogo"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze Excluir seleção de catálogo."

---
{% api %}
# Excluir seleção de catálogo {#delete-catalog-selection}
{% apimethod delete %}
/catalogs/{catalog_name}/selections/{selection_name}
{% endapimethod %}

> Use esse endpoint para excluir uma seleção de catálogo.

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key) com a permissão `catalogs.delete_selection`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='asynchronous catalog selections' %}

## Parâmetros de jornada {#path-parameters}

| Parâmetro        | Obrigatória | Tipo de dados | Descrição                    |
| ---------------- | -------- | --------- | ------------------------------ |
| `catalog_name`   | Obrigatória | String    | Nome do catálogo.           |
| `selection_name` | Obrigatória | String    | Nome da seleção do catálogo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de jornada" }

## Exemplo de solicitação {#example-request}

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/restaurants/selections/favorite_list' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
```

## Resposta {#response}

Existem dois códigos de status para esse endpoint: `202` e `404`.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `202` poderia retornar o seguinte corpo de resposta:

```json
{
  "message": "success"
}
```

### Exemplo de resposta de erro {#example-error-response}

O código de status `404` poderia retornar o seguinte corpo de resposta. Consulte [Solução de problemas](#troubleshooting) para saber mais sobre os erros que você pode encontrar.

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

| Erro                | Solução de problemas                                          |
| -------------------- | -------------------------------------------------------- |
| `catalog-not-found`  | Verifique se o nome do catálogo é válido.                    |
| `invalid-selection`  | Verifique se o nome da seleção é válido.                  |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solução de problemas" }

{% endapi %}