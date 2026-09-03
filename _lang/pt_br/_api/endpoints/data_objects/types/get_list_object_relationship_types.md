---
nav_title: "GET: Listar tipos de relacionamento de objetos"
article_title: "GET: Listar tipos de relacionamento de objetos"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Listar tipos de relacionamento de objetos."
---
{% api %}
# Listar tipos de relacionamento de objetos {#list-object-relationship-types}
{% apimethod get %}
/data_objects/types/{type_name}/object_relationship_types
{% endapimethod %}

> Use este endpoint para listar os tipos de relacionamento disponíveis para vínculos entre objetos em uma determinada direção de âncora.

{% alert important %}
Data Objects está atualmente em acesso antecipado. Seu espaço de trabalho deve ser ativado antes que as permissões de chave de API de Data Objects apareçam em **Configurações** > **Chaves de API**.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisa de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `data_objects.read`.

## Limite de frequência {#rate-limit}

Este endpoint está no bucket de leitura de Data Objects com um limite padrão de 50 solicitações por minuto.

## Parâmetros de caminho {#path-parameters}

A tabela a seguir lista e descreve os parâmetros de caminho para o endpoint `/data_objects/types/{type_name}/object_relationship_types`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `type_name` | Obrigatório | String | Nome de máquina do tipo de objeto de dados |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de caminho para listar tipos de relacionamento de objetos" }

## Parâmetros de consulta {#query-parameters}

A tabela a seguir lista e descreve os parâmetros de consulta para o endpoint `/data_objects/types/{type_name}/object_relationship_types`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `anchor` | Opcional | String | `source` (padrão) ou `target` |
| `limit` | Opcional | Número inteiro | Tamanho da página. Padrão `100`. Limitado de `1` a `250` |
| `offset` | Opcional | Número inteiro | Deslocamento. Padrão `0`. Valores negativos são arredondados para `0` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de consulta para listar tipos de relacionamento de objetos" }

## Exemplo de solicitação {#example-request}

Esta seção inclui um exemplo de carga útil de parâmetros e um exemplo de solicitação cURL.

### Exemplo de carga útil de solicitação {#sample-request-payload}

Use este objeto JSON como referência para os parâmetros de solicitação.

```json
{
  "type_name": "account",
  "anchor": "source",
  "limit": 10,
  "offset": 0
}
```

### Exemplo de solicitação cURL {#sample-curl-request}

Este exemplo lista os tipos de relacionamento de objetos disponíveis para o tipo `account` quando `account` é a origem do relacionamento.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/types/account/object_relationship_types?anchor=source&limit=10&offset=0' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Resposta {#response}

Esta seção inclui um exemplo de resposta bem-sucedida e os campos de resposta.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `200` pode retornar o seguinte corpo de resposta.

```json
{
  "items": [
    {
      "from_type_name": "account",
      "to_type_name": "account",
      "rel_kind": "subaccount",
      "display_name": "subaccount",
      "related_type_name": "account"
    }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 10
}
```

`related_type_name` é o tipo do outro lado do relacionamento para a `anchor` selecionada.

### Parâmetros de resposta {#response-parameters}

A tabela a seguir lista e descreve os campos em uma resposta bem-sucedida.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `items` | Obrigatório | Array | Lista dos tipos de relacionamento de objetos disponíveis |
| `items[].from_type_name` | Obrigatório | String | Nome do tipo de objeto de dados de origem |
| `items[].to_type_name` | Obrigatório | String | Nome do tipo de objeto de dados de destino |
| `items[].rel_kind` | Obrigatório | String | Valor do tipo de relacionamento |
| `items[].display_name` | Obrigatório | String | Rótulo de exibição do tipo de relacionamento |
| `items[].related_type_name` | Obrigatório | String | Tipo do lado oposto para a `anchor` solicitada |
| `total_count` | Obrigatório | Número inteiro | Número total de registros correspondentes |
| `has_more` | Obrigatório | Booleano | Se há outra página de resultados disponível |
| `next_offset` | Opcional | Número inteiro | Deslocamento para a próxima página quando `has_more` é `true` |
| `offset` | Obrigatório | Número inteiro | Deslocamento da página atual |
| `limit` | Obrigatório | Número inteiro | Tamanho de página usado pela solicitação |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de resposta para listar tipos de relacionamento de objetos" }

## Erros {#errors}

A tabela a seguir lista os erros comuns para este endpoint e como resolvê-los.

| Status | Causa | Orientação |
|---|---|---|
| `400` | `anchor` inválido | Use `source` ou `target` para `anchor`. |
| `404` | Tipo não encontrado (`data-object-type-not-found`) | Confirme se `type_name` existe no espaço de trabalho e corresponde exatamente ao nome de máquina. |
| `401` | Chave da REST API ausente ou inválida | Verifique se o cabeçalho `Authorization` usa `Bearer YOUR_REST_API_KEY` e se a chave está ativa. |
| `403` | A chave de API não tem permissão ou a solicitação está bloqueada pela lista de permissões | Confirme se a chave tem `data_objects.read` e se o IP de origem está na lista de permissões da chave, se configurada. |
| `429` | Limite de frequência excedido | Tente novamente após `X-RateLimit-Reset` e reduza a frequência de solicitações. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erros para listar tipos de relacionamento de objetos" }
{% endapi %}