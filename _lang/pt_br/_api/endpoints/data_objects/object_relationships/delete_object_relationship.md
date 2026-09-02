---
nav_title: "DELETE: Excluir relacionamento de objeto"
article_title: "DELETE: Excluir relacionamento de objeto"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Este artigo descreve os detalhes do endpoint Excluir relacionamento de objeto."
---
{% API or interface de programação do aplicativo (API) %}
# Excluir relacionamento de objeto {#delete-object-relationship}
{% apimethod delete %}
/data_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> Use este endpoint para excluir uma aresta de relacionamento entre objetos.

{% alert important %}
Data Objects está atualmente em acesso antecipado. Seu espaço de trabalho precisa estar ativado antes que as permissões de chave de API or interface de programação do aplicativo (API) de Data Objects apareçam em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisa de uma [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `data_objects.object_relationships.delete`.

## Limite de frequência {#rate-limit}

Este endpoint está no bucket de escrita de Data Objects, com um limite padrão de 50 solicitações por minuto.

## Parâmetros de caminho {#path-parameters}

A tabela a seguir lista e descreve os parâmetros de caminho para o endpoint `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `type_name` | Obrigatório | String | Tipo do objeto na URL |
| `external_id` | Obrigatório | String | Identificador do objeto na URL |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de caminho para excluir relacionamento de objeto" }

## Parâmetros de solicitação {#request-parameters}

A tabela a seguir lista e descreve os parâmetros do corpo da solicitação JSON para o endpoint `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `rel_kind` | Obrigatório | String | Tipo de relacionamento |
| `related_type_name` | Obrigatório | String | Tipo do objeto relacionado |
| `related_external_id` | Obrigatório | String | Identificador do objeto relacionado |
| `anchor` | Opcional | String | `source` (padrão) ou `target` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de solicitação para excluir relacionamento de objeto" }

{% alert note %}
Este endpoint `DELETE` espera um corpo de solicitação JSON. Verifique se seu cliente HTTP envia corpos de solicitação em chamadas `DELETE`.
{% endalert %}

## Exemplo de solicitação {#example-request}

Esta seção inclui uma carga útil JSON de exemplo e uma solicitação cURL de exemplo.

### Carga útil de exemplo {#sample-request-payload}

```json
{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source"
}
```

### Solicitação cURL de exemplo {#sample-curl-request}

Este exemplo remove o relacionamento `subaccount` entre `acct-123` e `acct-456`. Ambos os registros de conta permanecem.

```bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source"
}'
```

## Resposta {#response}

Esta seção inclui um exemplo de resposta bem-sucedida e os campos da resposta.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `200` pode retornar o seguinte corpo de resposta.

```json
{ "deleted": true }
```

### Parâmetros de resposta {#response-parameters}

A tabela a seguir lista e descreve os campos em uma resposta bem-sucedida.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `deleted` | Obrigatório | Boolean | Se a exclusão do relacionamento foi bem-sucedida |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de resposta para excluir relacionamento de objeto" }

## Erros {#errors}

A tabela a seguir lista os erros comuns para este endpoint e como resolvê-los.

| Status | Causa | Orientação |
|---|---|---|
| `400` | Erro de validação | Confirme se o corpo da solicitação inclui valores válidos para `rel_kind`, `related_type_name`, `related_external_id` e `anchor`. |
| `404` | Relacionamento ou objeto do endpoint não encontrado | Confirme se ambos os objetos existem e se os valores-chave do relacionamento correspondem a uma aresta existente. |
| `401` | Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional ausente ou inválida | Verifique se o cabeçalho `Authorization` usa `Bearer YOUR_REST_API_KEY` e se a chave está ativa. |
| `403` | A chave de API or interface de programação do aplicativo (API) não tem permissão ou a solicitação está bloqueada pela lista de permissões | Confirme se a chave tem a permissão `data_objects.object_relationships.delete` e se o IP de origem está na lista de permissões da chave, se configurada. |
| `429` | Limite de frequência excedido | Tente novamente após `X-RateLimit-Reset` e reduza a frequência das solicitações. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erros do endpoint de exclusão de relacionamento de objeto" }
{% endapi %}