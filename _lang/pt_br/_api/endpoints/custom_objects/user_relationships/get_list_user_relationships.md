---
nav_title: "GET: Listar relacionamentos de usuários"
article_title: "GET: Listar relacionamentos de usuários"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Este artigo descreve os detalhes do endpoint Listar relacionamentos de usuários."
---
{% api %}
# Listar relacionamentos de usuários {#list-user-relationships}
{% apimethod get %}
/custom_objects/objects/{type_name}/{external_id}/user_relationships
{% endapimethod %}

> Use este endpoint para listar os usuários vinculados a um objeto personalizado.

{% alert important %}
Custom Objects está atualmente em acesso antecipado. Seu espaço de trabalho precisa estar ativado antes que as permissões da chave de API de Custom Objects apareçam em **Configurações** > **Chaves de API**.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisa de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `custom_objects.user_relationships.read`.

## Limite de frequência {#rate-limit}

Este endpoint está no bucket de leitura de Custom Objects, com um limite padrão de 50 requisições por minuto.

## Parâmetros de caminho {#path-parameters}

A tabela a seguir lista e descreve os parâmetros de caminho do endpoint `/custom_objects/objects/{type_name}/{external_id}/user_relationships`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `type_name` | Obrigatório | String | Tipo de objeto |
| `external_id` | Obrigatório | String | Identificador do objeto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de caminho para listar relacionamentos de usuários" }

## Parâmetros de consulta {#query-parameters}

A tabela a seguir lista e descreve os parâmetros de consulta do endpoint `/custom_objects/objects/{type_name}/{external_id}/user_relationships`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `rel_kind` | Opcional | String | Filtrar por tipo de relacionamento |
| `limit` | Opcional | Inteiro | Tamanho da página. Padrão: `100`. Limitado entre `1` e `250` |
| `offset` | Opcional | Inteiro | Deslocamento. Padrão: `0`. Valores negativos são arredondados para `0` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de consulta para listar relacionamentos de usuários" }

## Exemplo de requisição {#example-request}

Esta seção inclui um exemplo de carga útil de parâmetros e um exemplo de requisição cURL.

### Exemplo de carga útil da requisição {#sample-request-payload}

Use este objeto JSON como referência para os parâmetros da requisição.

```json
{
  "type_name": "account",
  "external_id": "acct-123",
  "rel_kind": "account_user",
  "limit": 100,
  "offset": 0
}
```

### Exemplo de requisição cURL {#sample-curl-request}

Este exemplo lista os usuários vinculados a `acct-123` por meio do relacionamento `account_user`.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/user_relationships?rel_kind=account_user&limit=100&offset=0' \
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
      "rel_kind": "account_user",
      "user": { "braze_id": "507f1f77bcf86cd799439011" },
      "attributes": { "role": "admin" }
    }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

A carga útil de `user` contém apenas `braze_id`.

### Parâmetros de resposta {#response-parameters}

A tabela a seguir lista e descreve os campos de uma resposta bem-sucedida.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `items` | Obrigatório | Array | Lista de registros de relacionamento de usuários |
| `items[].type_name` | Obrigatório | String | Nome de máquina do tipo de objeto personalizado |
| `items[].external_id` | Obrigatório | String | Identificador do objeto personalizado |
| `items[].rel_kind` | Obrigatório | String | Valor do tipo de relacionamento |
| `items[].user` | Obrigatório | Objeto | Objeto do usuário vinculado |
| `items[].user.braze_id` | Obrigatório | String | Identificador de usuário da Braze |
| `items[].attributes` | Obrigatório | Objeto | Atributos do relacionamento |
| `total_count` | Obrigatório | Inteiro | Número total de registros correspondentes |
| `has_more` | Obrigatório | Booleano | Indica se há outra página de resultados disponível |
| `next_offset` | Opcional | Inteiro | Deslocamento para a próxima página quando `has_more` é `true` |
| `offset` | Obrigatório | Inteiro | Deslocamento da página atual |
| `limit` | Obrigatório | Inteiro | Tamanho da página usado pela requisição |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de resposta para listar relacionamentos de usuários" }

## Erros {#errors}

A tabela a seguir lista os erros comuns deste endpoint e como resolvê-los.

| Status | Causa | Orientação |
|---|---|---|
| `404` | Tipo ou objeto não encontrado | Confirme que `type_name` e `external_id` existem no espaço de trabalho. |
| `401` | Chave da API REST ausente ou inválida | Verifique se o cabeçalho `Authorization` usa `Bearer YOUR_REST_API_KEY` e se a chave está ativa. |
| `403` | A chave de API não tem permissão ou a requisição está bloqueada pela lista de permissões | Confirme que a chave tem a permissão `custom_objects.user_relationships.read` e que seu IP de origem está na lista de permissões da chave, se configurada. |
| `429` | Limite de frequência excedido | Tente novamente após `X-RateLimit-Reset` e reduza a frequência das requisições. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erros ao listar relacionamentos de usuários" }
{% endapi %}