---
nav_title: "GET: Listar tipos de objetos personalizados"
article_title: "GET: Listar tipos de objetos personalizados"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Este artigo descreve os detalhes do endpoint Listar tipos de objetos personalizados."
---
{% api %}
# Listar tipos de objetos personalizados {#list-custom-object-types}
{% apimethod get %}
/custom_objects/types
{% endapimethod %}

> Use este endpoint para listar os tipos de objetos personalizados em um espaço de trabalho.

{% alert important %}
Objetos personalizados está atualmente em acesso antecipado. Seu espaço de trabalho precisa estar ativado antes que as permissões da chave de API de objetos personalizados apareçam em **Configurações** > **Chaves de API**.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisa de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `custom_objects.read`.

## Limite de frequência {#rate-limit}

Este endpoint está no bucket de leitura de objetos personalizados, com um limite padrão de 50 solicitações por minuto.

## Parâmetros de consulta {#query-parameters}

A tabela a seguir lista e descreve os parâmetros de consulta para o endpoint `/custom_objects/types`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `search_term` | Opcional | String | Filtro de prefixo sem distinção entre maiúsculas e minúsculas no nome do tipo |
| `limit` | Opcional | Inteiro | Tamanho da página. Padrão `100`. Limitado de `1` a `250` |
| `offset` | Opcional | Inteiro | Deslocamento. Padrão `0`. Valores negativos são arredondados para `0` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de consulta para listar tipos de objetos personalizados" }

## Exemplo de solicitação {#example-request}

Esta seção inclui um exemplo de carga útil de parâmetros de consulta e um exemplo de solicitação cURL.

### Exemplo de carga útil da solicitação {#sample-request-payload}

Use este objeto JSON como referência para os parâmetros de consulta desta solicitação.

```json
{
  "search_term": "acc",
  "limit": 2,
  "offset": 0
}
```

### Exemplo de solicitação cURL {#sample-curl-request}

Este exemplo lista os tipos de objetos personalizados que correspondem ao termo de busca `acc`, retornando dois resultados por página.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/types?search_term=acc&limit=2&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Resposta {#response}

Esta seção inclui um exemplo de resposta bem-sucedida e os campos da resposta.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `200` pode retornar o seguinte corpo de resposta.

```json
{
  "items": [
    {
      "type_name": "account",
      "metadata": { "display_name_source": "name" }
    },
    {
      "type_name": "contact",
      "metadata": {}
    }
  ],
  "total_count": 2,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

`metadata.display_name_source` está presente quando um campo de nome de exibição é configurado para o tipo.

### Parâmetros da resposta {#response-parameters}

A tabela a seguir lista e descreve os campos em uma resposta bem-sucedida.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `items` | Obrigatório | Array | Lista de registros de tipos de objetos personalizados |
| `items[].type_name` | Obrigatório | String | Nome de máquina do tipo de objeto personalizado |
| `items[].metadata` | Obrigatório | Objeto | Objeto de metadados do tipo |
| `total_count` | Obrigatório | Inteiro | Número total de registros correspondentes |
| `has_more` | Obrigatório | Booleano | Se há outra página de resultados disponível |
| `next_offset` | Opcional | Inteiro | Deslocamento para a próxima página quando `has_more` é `true` |
| `offset` | Obrigatório | Inteiro | Deslocamento da página atual |
| `limit` | Obrigatório | Inteiro | Tamanho da página usado pela solicitação |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros da resposta para listar tipos de objetos personalizados" }

## Erros {#errors}

A tabela a seguir lista os erros comuns para este endpoint e como resolvê-los.

| Status | Causa | Orientação |
|---|---|---|
| `400` | Tipo ou valor inválido de parâmetro de consulta | Verifique se `limit` e `offset` são inteiros e se todos os valores de parâmetros são válidos. |
| `401` | Chave da API REST ausente ou inválida | Verifique se o cabeçalho `Authorization` usa `Bearer YOUR_REST_API_KEY` e se a chave está ativa. |
| `403` | A chave de API não possui permissão ou a solicitação está bloqueada pela lista de permissões | Confirme se a chave possui `custom_objects.read` e se o IP de origem está na lista de permissões da chave, se configurado. |
| `429` | Limite de frequência excedido | Tente novamente após `X-RateLimit-Reset` e reduza a frequência das solicitações. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erros ao listar tipos de objetos personalizados" }
{% endapi %}