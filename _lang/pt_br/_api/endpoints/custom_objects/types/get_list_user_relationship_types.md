---
nav_title: "GET: Listar tipos de relacionamento de usuário"
article_title: "GET: Listar tipos de relacionamento de usuário"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Este artigo descreve os detalhes sobre o endpoint Listar tipos de relacionamento de usuário."
---
{% api %}
# Listar tipos de relacionamento de usuário {#list-user-relationship-types}
{% apimethod get %}
/custom_objects/types/{type_name}/user_relationship_types
{% endapimethod %}

> Use este endpoint para listar valores válidos de `rel_kind` para relacionamentos de usuário em um tipo de objeto personalizado.

{% alert important %}
Custom Objects está atualmente em acesso antecipado. Seu espaço de trabalho deve ser ativado antes que as permissões de chave de API de Custom Objects apareçam em **Configurações** > **Chaves de API**.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `custom_objects.read`.

## Limite de frequência {#rate-limit}

Este endpoint está no bucket de leitura de Custom Objects com um limite padrão de 50 solicitações por minuto.

## Parâmetros de caminho {#path-parameters}

A tabela a seguir lista e descreve os parâmetros de caminho para o endpoint `/custom_objects/types/{type_name}/user_relationship_types`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `type_name` | Obrigatório | String | Nome de máquina do tipo de objeto personalizado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de caminho para listar tipos de relacionamento de usuário" }

## Parâmetros de consulta {#query-parameters}

A tabela a seguir lista e descreve os parâmetros de consulta para o endpoint `/custom_objects/types/{type_name}/user_relationship_types`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `limit` | Opcional | Inteiro | Tamanho da página. Padrão `100`. Limitado de `1` a `250` |
| `offset` | Opcional | Inteiro | Deslocamento. Padrão `0`. Valores negativos são arredondados para `0` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de consulta para listar tipos de relacionamento de usuário" }

## Exemplo de solicitação {#example-request}

Esta seção inclui um exemplo de carga útil de parâmetros e um exemplo de solicitação cURL.

### Exemplo de carga útil da solicitação {#sample-request-payload}

Use este objeto JSON como referência para os parâmetros da solicitação.

```json
{
  "type_name": "account",
  "limit": 100,
  "offset": 0
}
```

### Exemplo de solicitação cURL {#sample-curl-request}

Este exemplo lista os tipos de relacionamento de usuário que você pode usar para vincular usuários a registros `account`.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/types/account/user_relationship_types?limit=100&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Resposta {#response}

Esta seção inclui um exemplo de resposta bem-sucedida e os campos da resposta.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `200` pode retornar o seguinte corpo de resposta.

```json
{
  "items": [
    { "rel_kind": "account_user", "display_name": "account_user" }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

Atualmente, `display_name` corresponde a `rel_kind`.

### Parâmetros de resposta {#response-parameters}

A tabela a seguir lista e descreve os campos em uma resposta bem-sucedida.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `items` | Obrigatório | Array | Lista de tipos de relacionamento de usuário disponíveis |
| `items[].rel_kind` | Obrigatório | String | Valor do tipo de relacionamento de usuário |
| `items[].display_name` | Obrigatório | String | Rótulo de exibição para o tipo de relacionamento |
| `total_count` | Obrigatório | Inteiro | Número total de registros correspondentes |
| `has_more` | Obrigatório | Booleano | Se há outra página de resultados disponível |
| `next_offset` | Opcional | Inteiro | Deslocamento para a próxima página quando `has_more` é `true` |
| `offset` | Obrigatório | Inteiro | Deslocamento da página atual |
| `limit` | Obrigatório | Inteiro | Tamanho da página usado pela solicitação |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de resposta para listar tipos de relacionamento de usuário" }

## Erros {#errors}

A tabela a seguir lista os erros comuns para este endpoint e como resolvê-los.

| Status | Causa | Orientação |
|---|---|---|
| `404` | Tipo não encontrado (`custom-object-type-not-found`) | Confirme se `type_name` existe no espaço de trabalho e corresponde exatamente ao nome de máquina. |
| `401` | Chave da API REST ausente ou inválida | Verifique se o cabeçalho `Authorization` usa `Bearer YOUR_REST_API_KEY` e se a chave está ativa. |
| `403` | A chave de API não tem permissão ou a solicitação está bloqueada pela lista de permissões | Confirme se a chave tem `custom_objects.read` e se o IP de origem está na lista de permissões da chave, se configurado. |
| `429` | Limite de frequência excedido | Tente novamente após `X-RateLimit-Reset` e reduza a frequência de solicitações. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erros para listar tipos de relacionamento de usuário" }
{% endapi %}