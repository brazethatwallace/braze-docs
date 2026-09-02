---
nav_title: "POST: Criar relacionamento de objeto"
article_title: "POST: Criar relacionamento de objeto"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Criar relacionamento de objeto."
---
{% api %}
# Criar relacionamento de objeto {#create-object-relationship}
{% apimethod post %}
/data_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> Use este endpoint para criar uma aresta de relacionamento direcional entre dois objetos de dados.

{% alert important %}
Data Objects está atualmente em acesso antecipado. Seu espaço de trabalho precisa ser ativado antes que as permissões da chave de API de Data Objects apareçam em **Configurações** > **Chaves de API**.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisa de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `data_objects.object_relationships.create`.

## Limite de frequência {#rate-limit}

Este endpoint está no bucket de escrita de Data Objects com um limite padrão de 50 solicitações por minuto.

## Parâmetros de caminho {#path-parameters}

A tabela a seguir lista e descreve os parâmetros de caminho para o endpoint `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `type_name` | Obrigatório | String | Tipo de objeto da URL |
| `external_id` | Obrigatório | String | Identificador de objeto da URL |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de caminho para criar relacionamento de objeto" }

## Parâmetros de solicitação {#request-parameters}

A tabela a seguir lista e descreve os parâmetros do corpo da solicitação JSON para o endpoint `/data_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `rel_kind` | Obrigatório | String | Tipo de relacionamento |
| `related_type_name` | Obrigatório | String | Tipo de objeto relacionado |
| `related_external_id` | Obrigatório | String | Identificador do objeto relacionado |
| `anchor` | Opcional | String | `source` (padrão) ou `target` |
| `attributes` | Opcional | Objeto | Atributos do relacionamento |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de solicitação para criar relacionamento de objeto" }

## Exemplo de solicitação {#example-request}

Esta seção inclui uma carga útil JSON de exemplo e uma solicitação cURL de exemplo.

### Carga útil de exemplo {#sample-request-payload}

```json
{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source",
  "attributes": {}
}
```

### Exemplo de solicitação cURL {#sample-curl-request}

Este exemplo vincula `acct-123` a `acct-456` como `subaccount`, com `acct-123` como a origem do relacionamento.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/object_relationships' \
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

Esta seção inclui um exemplo de resposta bem-sucedida e os campos da resposta.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `201` pode retornar o seguinte corpo de resposta.

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
| `object_relationship` | Obrigatório | Objeto | Registro de relacionamento criado |
| `object_relationship.rel_kind` | Obrigatório | String | Valor do tipo de relacionamento |
| `object_relationship.to_data_object` | Condicional | Objeto | Objeto relacionado quando `anchor=source` |
| `object_relationship.from_data_object` | Condicional | Objeto | Objeto relacionado quando `anchor=target` |
| `object_relationship.to_data_object.type_name` | Condicional | String | Nome do tipo do objeto relacionado |
| `object_relationship.to_data_object.external_id` | Condicional | String | ID externo do objeto relacionado |
| `object_relationship.to_data_object.attributes` | Condicional | Objeto | Atributos do objeto relacionado |
| `object_relationship.from_data_object.type_name` | Condicional | String | Nome do tipo do objeto relacionado |
| `object_relationship.from_data_object.external_id` | Condicional | String | ID externo do objeto relacionado |
| `object_relationship.from_data_object.attributes` | Condicional | Objeto | Atributos do objeto relacionado |
| `object_relationship.attributes` | Obrigatório | Objeto | Atributos do relacionamento |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de resposta para criar relacionamento de objeto" }

## Erros {#errors}

A tabela a seguir lista os erros comuns para este endpoint e como resolvê-los.

| Status | Causa | Orientação |
|---|---|---|
| `400` | `rel_kind` desconhecido, `anchor` inválido, tipo relacionado inválido para o tipo de relacionamento ou violação de esquema | Confirme que `rel_kind` é válido para o par de tipos, use um `anchor` válido e verifique se `attributes` correspondem ao esquema do relacionamento. |
| `404` | Objeto da URL, objeto relacionado, tipo da URL ou tipo relacionado não encontrado | Confirme que ambos os objetos e ambos os nomes de tipo existem no espaço de trabalho. |
| `409` | Aresta duplicada (`duplicate-object-relationship`) | Use `PUT` para substituir o relacionamento existente ou exclua-o antes de criar novamente. |
| `422` | Limite de relacionamentos por objeto atingido (`data-object-relationship-limit-exceeded`) | Reduza a contagem de relacionamentos para o objeto ou entre em contato com o suporte da Braze sobre os limites do espaço de trabalho. |
| `401` | Chave da API REST ausente ou inválida | Verifique se o cabeçalho `Authorization` usa `Bearer YOUR_REST_API_KEY` e se a chave está ativa. |
| `403` | A chave de API não tem permissão ou a solicitação está bloqueada pela lista de permissões | Confirme que a chave tem a permissão `data_objects.object_relationships.create` e que o IP de origem está na lista de permissões da chave, se configurado. |
| `429` | Limite de frequência excedido | Tente novamente após `X-RateLimit-Reset` e reduza a frequência das solicitações. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erros ao criar relacionamento de objeto" }
{% endapi %}