---
nav_title: "PATCH: Atualizar relacionamento de objeto"
article_title: "PATCH: Atualizar relacionamento de objeto"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Atualizar relacionamento de objeto."
---
{% api %}
# Atualizar relacionamento de objeto {#update-object-relationship}
{% apimethod patch %}
/data_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> Use este endpoint para mesclar atributos em um relacionamento de objeto existente.

{% alert important %}
Data Objects está atualmente em acesso antecipado. Seu espaço de trabalho precisa estar ativado antes que as permissões de chave de API de Data Objects apareçam em **Configurações** > **Chaves de API**.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `data_objects.object_relationships.update`.

## Limite de frequência {#rate-limit}

Este endpoint está no bucket de escrita de Data Objects com um limite padrão de 50 requisições por minuto.

## Parâmetros de caminho {#path-parameters}

A tabela a seguir lista e descreve os parâmetros de caminho para o endpoint `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `type_name` | Obrigatório | String | Tipo de objeto da URL |
| `external_id` | Obrigatório | String | Identificador de objeto da URL |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de caminho para atualizar relacionamento de objeto" }

## Parâmetros de requisição {#request-parameters}

A tabela a seguir lista e descreve os parâmetros do corpo da requisição JSON para o endpoint `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `rel_kind` | Obrigatório | String | Tipo de relacionamento |
| `related_type_name` | Obrigatório | String | Tipo de objeto relacionado |
| `related_external_id` | Obrigatório | String | Identificador do objeto relacionado |
| `anchor` | Opcional | String | `source` (padrão) ou `target` |
| `attributes` | Opcional | Object | Atributos de relacionamento para mesclar |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de requisição para atualizar relacionamento de objeto" }

## Exemplo de requisição {#example-request}

Esta seção inclui um exemplo de carga útil JSON e um exemplo de requisição cURL.

### Exemplo de carga útil da requisição {#sample-request-payload}

```json
{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source",
  "attributes": {}
}
```

### Exemplo de requisição cURL {#sample-curl-request}

Este exemplo mescla atributos no relacionamento `subaccount` existente entre `acct-123` e `acct-456`, mantendo inalterados quaisquer atributos que você omitir.

```bash
curl --location --request PATCH 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source",
  "attributes": {}
}'
```

## Resposta {#response}

Esta seção inclui um exemplo de resposta bem-sucedida e os campos de resposta.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `200` pode retornar o seguinte corpo de resposta.

```json
{
  "object_relationship": {
    "rel_kind": "subaccount",
    "to_data_object": {
      "type_name": "account",
      "external_id": "acct-456",
      "attributes": { "name": "Child Account" }
    },
    "attributes": {}
  }
}
```

### Parâmetros de resposta {#response-parameters}

A tabela a seguir lista e descreve os campos em uma resposta bem-sucedida.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `object_relationship` | Obrigatório | Object | Registro de relacionamento atualizado |
| `object_relationship.rel_kind` | Obrigatório | String | Valor do tipo de relacionamento |
| `object_relationship.to_data_object` | Condicional | Object | Objeto relacionado quando `anchor=source` |
| `object_relationship.from_data_object` | Condicional | Object | Objeto relacionado quando `anchor=target` |
| `object_relationship.attributes` | Obrigatório | Object | Atributos do relacionamento após a mesclagem |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de resposta para atualizar relacionamento de objeto" }

## Erros {#errors}

A tabela a seguir lista os erros comuns para este endpoint e como resolvê-los.

| Status | Causa | Orientação |
|---|---|---|
| `400` | Erro de validação | Confirme que `rel_kind`, `anchor` e `attributes` são válidos para o tipo de relacionamento. |
| `404` | Relacionamento não encontrado (`data-object-relationship-not-found`) | Confirme que o objeto de origem, o objeto relacionado e os valores da chave de relacionamento existem. |
| `401` | Chave da REST API ausente ou inválida | Verifique se o cabeçalho `Authorization` usa `Bearer YOUR_REST_API_KEY` e se a chave está ativa. |
| `403` | A chave de API não tem permissão ou a requisição está bloqueada pela lista de permissões | Confirme que a chave tem `data_objects.object_relationships.update` e que o IP de origem está na lista de permissões da chave, se configurado. |
| `429` | Limite de frequência excedido | Tente novamente após `X-RateLimit-Reset` e reduza a frequência de requisições. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erros ao atualizar relacionamento de objeto" }
{% endapi %}