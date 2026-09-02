---
nav_title: "PATCH: Atualizar relacionamento de usuário"
article_title: "PATCH: Atualizar relacionamento de usuário"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Atualizar relacionamento de usuário."
---
{% API or interface de programação do aplicativo (API) %}
# Atualizar relacionamento de usuário {#update-user-relationship}
{% apimethod patch %}
/data_objects/objects/{type_name}/{external_id}/users
{% endapimethod %}

> Use este endpoint para mesclar atributos em um relacionamento de usuário existente.

{% alert important %}
Data Objects está atualmente em acesso antecipado. Seu espaço de trabalho precisa estar ativado antes que as permissões de chave de API or interface de programação do aplicativo (API) de Data Objects apareçam em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisa de uma [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `data_objects.user_relationships.update`.

## Limite de frequência {#rate-limit}

Este endpoint está no bucket de escrita de Data Objects com um limite padrão de 50 requisições por minuto.

## Parâmetros de caminho {#path-parameters}

A tabela a seguir lista e descreve os parâmetros de caminho para o endpoint `/data_objects/objects/{type_name}/{external_id}/users`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `type_name` | Obrigatório | String | Tipo de objeto |
| `external_id` | Obrigatório | String | Identificador do objeto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de caminho para atualizar relacionamento de usuário" }

## Parâmetros de requisição {#request-parameters}

A tabela a seguir lista e descreve os parâmetros do corpo da requisição JSON para o endpoint `/data_objects/objects/{type_name}/{external_id}/users`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `braze_id` | Obrigatório | String | ID de usuário da Braze |
| `rel_kind` | Obrigatório | String | Tipo de relacionamento |
| `attributes` | Opcional | Objeto | Atributos de relacionamento a serem mesclados |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de requisição para atualizar relacionamento de usuário" }

## Exemplo de requisição {#example-request}

Esta seção inclui uma carga útil JSON de exemplo e uma requisição cURL de exemplo.

### Carga útil de requisição de exemplo {#sample-request-payload}

```json
{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "billing_admin"
  }
}
```

### Requisição cURL de exemplo {#sample-curl-request}

Este exemplo altera o atributo `role` no relacionamento `account_user` existente para `billing_admin`, mantendo os demais atributos do relacionamento inalterados.

```bash
curl --location --request PATCH 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/users' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "billing_admin"
  }
}'
```

## Resposta {#response}

Esta seção inclui um exemplo de resposta bem-sucedida e os campos da resposta.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `200` pode retornar o seguinte corpo de resposta.

```json
{
  "user_relationship": {
    "type_name": "account",
    "external_id": "acct-123",
    "rel_kind": "account_user",
    "user": { "braze_id": "507f1f77bcf86cd799439011" },
    "attributes": { "role": "billing_admin" }
  }
}
```

### Parâmetros de resposta {#response-parameters}

A tabela a seguir lista e descreve os campos de uma resposta bem-sucedida.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `user_relationship` | Obrigatório | Objeto | Registro atualizado do relacionamento de usuário |
| `user_relationship.type_name` | Obrigatório | String | Nome de máquina do tipo de objeto de dados |
| `user_relationship.external_id` | Obrigatório | String | Identificador do objeto de dados |
| `user_relationship.rel_kind` | Obrigatório | String | Valor do tipo de relacionamento |
| `user_relationship.user` | Obrigatório | Objeto | Objeto de usuário vinculado |
| `user_relationship.user.braze_id` | Obrigatório | String | Identificador de usuário da Braze |
| `user_relationship.attributes` | Obrigatório | Objeto | Atributos do relacionamento após a mesclagem |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de resposta para atualizar relacionamento de usuário" }

## Erros {#errors}

A tabela a seguir lista os erros comuns para este endpoint e como resolvê-los.

| Status | Causa | Orientação |
|---|---|---|
| `400` | Erro de validação | Confirme se `rel_kind` é válido para o tipo de objeto e se `attributes` corresponde ao esquema do relacionamento. |
| `404` | Relacionamento não encontrado (`data-object-relationship-not-found`) | Confirme se o objeto, o usuário e os valores de chave do relacionamento existem. |
| `401` | Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional ausente ou inválida | Verifique se o cabeçalho `Authorization` usa `Bearer YOUR_REST_API_KEY` e se a chave está ativa. |
| `403` | A chave de API or interface de programação do aplicativo (API) não tem permissão ou a requisição está bloqueada pela lista de permissões | Confirme se a chave possui `data_objects.user_relationships.update` e se o IP de origem está na lista de permissões da chave, se configurada. |
| `429` | Limite de frequência excedido | Tente novamente após `X-RateLimit-Reset` e reduza a frequência das requisições. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erros do endpoint de atualizar relacionamento de usuário" }
{% endapi %}