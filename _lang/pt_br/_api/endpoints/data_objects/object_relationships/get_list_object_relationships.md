---
nav_title: "GET: Listar relacionamentos de objetos"
article_title: "GET: Listar relacionamentos de objetos"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "Este artigo descreve os detalhes do endpoint Listar relacionamentos de objetos."
---
{% API or interface de programação do aplicativo (API) %}
# Listar relacionamentos de objetos {#list-object-relationships}
{% apimethod get %}
/data_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> Use este endpoint para listar objetos de dados relacionados a partir de uma âncora de objeto.

{% alert important %}
Data Objects está atualmente em acesso antecipado. Seu espaço de trabalho precisa estar ativado antes que as permissões de chave de API or interface de programação do aplicativo (API) de Data Objects apareçam em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisa de uma [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `data_objects.read`.

## Limite de frequência {#rate-limit}

Este endpoint está no bucket de leitura de Data Objects, com um limite padrão de 50 solicitações por minuto.

## Parâmetros de caminho {#path-parameters}

A tabela a seguir lista e descreve os parâmetros de caminho para o endpoint `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `type_name` | Obrigatório | String | Tipo do objeto de origem |
| `external_id` | Obrigatório | String | Identificador do objeto de origem |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de caminho para listar relacionamentos de objetos" }

## Parâmetros de consulta {#query-parameters}

A tabela a seguir lista e descreve os parâmetros de consulta para o endpoint `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `anchor` | Opcional | String | `source` (padrão) ou `target` |
| `rel_kind` | Opcional | String | Filtrar por um tipo de relacionamento |
| `limit` | Opcional | Integer | Tamanho da página. Padrão `100`. Limitado de `1` a `250` |
| `offset` | Opcional | Integer | Deslocamento. Padrão `0`. Valores negativos são arredondados para `0` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de consulta para listar relacionamentos de objetos" }

## Exemplo de solicitação {#example-request}

Esta seção inclui um exemplo de carga útil de parâmetros e um exemplo de solicitação cURL.

### Exemplo de carga útil da solicitação {#sample-request-payload}

Use este objeto JSON como referência para os parâmetros da solicitação.

```json
{
  "type_name": "account",
  "external_id": "acct-123",
  "anchor": "source",
  "rel_kind": "subaccount",
  "limit": 100,
  "offset": 0
}
```

### Exemplo de solicitação cURL {#sample-curl-request}

Este exemplo lista os registros de `subaccount` vinculados a `acct-123`, retornando a primeira página de resultados.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships?anchor=source&rel_kind=subaccount&limit=100&offset=0' \
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
      "rel_kind": "subaccount",
      "to_data_object": {
        "type_name": "account",
        "external_id": "acct-456",
        "attributes": { "name": "Child Account" }
      },
      "attributes": {}
    }
  ],
  "total_count": 1,
  "has_more": false,
  "next_offset": null,
  "offset": 0,
  "limit": 100
}
```

Com `anchor=target`, os objetos relacionados são retornados como `from_data_object`.

### Parâmetros da resposta {#response-parameters}

A tabela a seguir lista e descreve os campos em uma resposta bem-sucedida.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `items` | Obrigatório | Array | Lista de registros de relacionamento de objetos |
| `items[].rel_kind` | Obrigatório | String | Valor do tipo de relacionamento |
| `items[].to_data_object` | Condicional | Object | Objeto relacionado quando `anchor=source` |
| `items[].from_data_object` | Condicional | Object | Objeto relacionado quando `anchor=target` |
| `items[].to_data_object.type_name` | Condicional | String | Nome do tipo do objeto relacionado |
| `items[].to_data_object.external_id` | Condicional | String | ID externo do objeto relacionado |
| `items[].to_data_object.attributes` | Condicional | Object | Atributos do objeto relacionado |
| `items[].from_data_object.type_name` | Condicional | String | Nome do tipo do objeto relacionado |
| `items[].from_data_object.external_id` | Condicional | String | ID externo do objeto relacionado |
| `items[].from_data_object.attributes` | Condicional | Object | Atributos do objeto relacionado |
| `items[].attributes` | Obrigatório | Object | Atributos do relacionamento |
| `total_count` | Obrigatório | Integer | Número total de registros correspondentes |
| `has_more` | Obrigatório | Boolean | Se há mais uma página de resultados disponível |
| `next_offset` | Opcional | Integer | Deslocamento para a próxima página quando `has_more` é `true` |
| `offset` | Obrigatório | Integer | Deslocamento da página atual |
| `limit` | Obrigatório | Integer | Tamanho da página usado pela solicitação |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros da resposta para listar relacionamentos de objetos" }

## Erros {#errors}

A tabela a seguir lista os erros comuns para este endpoint e como resolvê-los.

| Status | Causa | Orientação |
|---|---|---|
| `400` | `anchor` inválido | Use `source` ou `target` para `anchor`. |
| `404` | Tipo ou objeto não encontrado | Confirme que `type_name` e `external_id` existem no espaço de trabalho. |
| `401` | Chave da REST or transferir estado representacional API or interface de programação do aplicativo (API) ausente ou inválida | Verifique se o cabeçalho `Authorization` usa `Bearer YOUR_REST_API_KEY` e se a chave está ativa. |
| `403` | A chave de API or interface de programação do aplicativo (API) não tem permissão ou a solicitação está bloqueada pela lista de permissões | Confirme que a chave tem a permissão `data_objects.read` e que o IP de origem está na lista de permissões da chave, se configurada. |
| `429` | Limite de frequência excedido | Tente novamente após `X-RateLimit-Reset` e reduza a frequência das solicitações. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erros do endpoint listar relacionamentos de objetos" }
{% endapi %}