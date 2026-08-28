---
nav_title: "GET: Listar objetos personalizados"
article_title: "GET: Listar objetos personalizados"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Este artigo descreve os detalhes sobre o endpoint Listar objetos personalizados."
---
{% api %}
# Listar objetos personalizados {#list-custom-objects}
{% apimethod get %}
/custom_objects/objects/{type_name}
{% endapimethod %}

> Use este endpoint para listar objetos de um tipo de objeto personalizado específico.

{% alert important %}
Custom Objects está atualmente em acesso antecipado. Seu espaço de trabalho precisa ser ativado antes que as permissões de chave de API de Custom Objects apareçam em **Configurações** > **Chaves de API**.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisa de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `custom_objects.read`.

## Limite de frequência {#rate-limit}

Este endpoint está no bucket de leitura de Custom Objects, com um limite padrão de 50 requisições por minuto.

## Parâmetros de caminho {#path-parameters}

A tabela a seguir lista e descreve os parâmetros de caminho para o endpoint `/custom_objects/objects/{type_name}`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `type_name` | Obrigatório | String | Nome de máquina do tipo de objeto personalizado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de caminho para listar objetos personalizados" }

## Parâmetros de consulta {#query-parameters}

A tabela a seguir lista e descreve os parâmetros de consulta para o endpoint `/custom_objects/objects/{type_name}`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `search_term` | Opcional | String | Filtro de substring no identificador do objeto |
| `limit` | Opcional | Inteiro | Tamanho da página. Padrão `100`. Limitado de `1` a `250` |
| `offset` | Opcional | Inteiro | Deslocamento. Padrão `0`. Valores negativos são arredondados para `0` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de consulta para listar objetos personalizados" }

## Exemplo de requisição {#example-request}

Esta seção inclui um exemplo de carga útil de parâmetros e um exemplo de requisição cURL.

### Exemplo de carga útil da requisição {#sample-request-payload}

Use este objeto JSON como referência para os parâmetros da requisição.

```json
{
  "type_name": "account",
  "search_term": "acct",
  "limit": 100,
  "offset": 0
}
```

### Exemplo de requisição cURL {#sample-curl-request}

Este exemplo lista os registros de `account` correspondentes ao termo de busca `acct`, retornando a primeira página de resultados.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/objects/account?search_term=acct&limit=100&offset=0' \
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
      "external_id": "acct-123",
      "attributes": { "name": "Acme", "industry": "software" }
    }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

### Parâmetros da resposta {#response-parameters}

A tabela a seguir lista e descreve os campos em uma resposta bem-sucedida.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `items` | Obrigatório | Array | Lista de registros de objetos personalizados |
| `items[].type_name` | Obrigatório | String | Nome de máquina do tipo de objeto personalizado |
| `items[].external_id` | Obrigatório | String | Identificador do objeto personalizado |
| `items[].attributes` | Obrigatório | Objeto | Atributos do objeto indexados pelo nome do campo |
| `total_count` | Obrigatório | Inteiro | Número total de registros correspondentes |
| `has_more` | Obrigatório | Booleano | Se há outra página de resultados disponível |
| `next_offset` | Opcional | Inteiro | Deslocamento para a próxima página quando `has_more` é `true` |
| `offset` | Obrigatório | Inteiro | Deslocamento da página atual |
| `limit` | Obrigatório | Inteiro | Tamanho da página usado pela requisição |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros da resposta para listar objetos personalizados" }

## Erros {#errors}

A tabela a seguir lista os erros comuns para este endpoint e como resolvê-los.

| Status | Causa | Orientação |
|---|---|---|
| `404` | Tipo não encontrado (`custom-object-type-not-found`) | Confirme que `type_name` existe no espaço de trabalho e corresponde exatamente ao nome de máquina. |
| `401` | Chave da API REST ausente ou inválida | Verifique se o header `Authorization` usa `Bearer YOUR_REST_API_KEY` e se a chave está ativa. |
| `403` | A chave de API não tem permissão ou a requisição está bloqueada pela lista de permissões | Confirme que a chave possui `custom_objects.read` e que o IP de origem está na lista de permissões da chave, se configurada. |
| `429` | Limite de frequência excedido | Tente novamente após `X-RateLimit-Reset` e reduza a frequência das requisições. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erros ao listar objetos personalizados" }
{% endapi %}