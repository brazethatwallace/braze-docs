---
nav_title: "PUT: Substituir relacionamento de objeto"
article_title: "PUT: Substituir relacionamento de objeto"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Substituir relacionamento de objeto."
---
{% api %}
# Substituir relacionamento de objeto {#replace-object-relationship}
{% apimethod put %}
/custom_objects/objects/{type_name}/{external_id}/object_relationships
{% endapimethod %}

> Use este endpoint para criar ou substituir um relacionamento de objeto.

{% alert important %}
Custom Objects está atualmente em acesso antecipado. Seu espaço de trabalho precisa estar ativado antes que as permissões de chave de API de Custom Objects apareçam em **Configurações** > **Chaves de API**.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisa de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `custom_objects.object_relationships.update`.

## Limite de frequência {#rate-limit}

Este endpoint está no bucket de escrita de Custom Objects com um limite padrão de 50 solicitações por minuto.

## Parâmetros de caminho {#path-parameters}

A tabela a seguir lista e descreve os parâmetros de caminho para o endpoint `/custom_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `type_name` | Obrigatório | String | Tipo de objeto da URL |
| `external_id` | Obrigatório | String | Identificador de objeto da URL |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de caminho para substituir relacionamento de objeto" }

## Parâmetros de solicitação {#request-parameters}

A tabela a seguir lista e descreve os parâmetros do corpo da solicitação JSON para o endpoint `/custom_objects/objects/{type_name}/{external_id}/object_relationships`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `rel_kind` | Obrigatório | String | Tipo de relacionamento |
| `related_type_name` | Obrigatório | String | Tipo de objeto relacionado |
| `related_external_id` | Obrigatório | String | Identificador de objeto relacionado |
| `anchor` | Opcional | String | `source` (padrão) ou `target` |
| `attributes` | Opcional | Objeto | Atributos do relacionamento |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de solicitação para substituir relacionamento de objeto" }

## Exemplo de solicitação {#example-request}

Esta seção inclui uma carga útil JSON de exemplo e uma solicitação cURL de exemplo.

### Carga útil de solicitação de exemplo {#sample-request-payload}

```json
{
  "rel_kind": "subaccount",
  "related_type_name": "account",
  "related_external_id": "acct-456",
  "anchor": "source",
  "attributes": {}
}
```

### Solicitação cURL de exemplo {#sample-curl-request}

Este exemplo substitui o relacionamento `subaccount` entre `acct-123` e `acct-456`, sobrescrevendo quaisquer atributos armazenados anteriormente nele.

```bash
curl --location --request PUT 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/object_relationships' \
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

O código de status `200` pode retornar o seguinte corpo de resposta.

```json
{
  "object_relationship": {
    "rel_kind": "subaccount",
    "to_custom_object": {
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
| `object_relationship` | Obrigatório | Objeto | Registro de relacionamento criado ou substituído |
| `object_relationship.rel_kind` | Obrigatório | String | Valor do tipo de relacionamento |
| `object_relationship.to_custom_object` | Condicional | Objeto | Objeto relacionado quando `anchor=source` |
| `object_relationship.from_custom_object` | Condicional | Objeto | Objeto relacionado quando `anchor=target` |
| `object_relationship.attributes` | Obrigatório | Objeto | Atributos do relacionamento |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de resposta para substituir relacionamento de objeto" }

## Erros {#errors}

A tabela a seguir lista erros comuns para este endpoint e como resolvê-los.

| Status | Causa | Orientação |
|---|---|---|
| `400` | Erro de validação | Confirme que `rel_kind`, `anchor` e `attributes` são válidos para o tipo de relacionamento. |
| `404` | Relacionamento ou objetos do endpoint não encontrados (`custom-object-relationship-not-found`) | Confirme que ambos os objetos e os nomes de tipo relacionados existem no espaço de trabalho. |
| `422` | Limite de relacionamento por objeto atingido (`custom-object-relationship-limit-exceeded`) | Reduza a contagem de relacionamentos para o objeto ou entre em contato com o suporte da Braze sobre os limites do espaço de trabalho. |
| `401` | Chave da API REST ausente ou inválida | Verifique se o cabeçalho `Authorization` usa `Bearer YOUR_REST_API_KEY` e se a chave está ativa. |
| `403` | A chave de API não tem permissão ou a solicitação está bloqueada pela lista de permissões | Confirme que a chave possui `custom_objects.object_relationships.update` e que seu IP de origem está na lista de permissões da chave, se configurada. |
| `429` | Limite de frequência excedido | Tente novamente após `X-RateLimit-Reset` e reduza a frequência de solicitações. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erros de substituir relacionamento de objeto" }
{% endapi %}