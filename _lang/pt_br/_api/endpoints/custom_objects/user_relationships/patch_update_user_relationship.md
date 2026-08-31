---
nav_title: "PATCH: Atualizar relacionamento de usuário"
article_title: "PATCH: Atualizar relacionamento de usuário"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Atualizar relacionamento de usuário."
---
{% api %}
# Atualizar relacionamento de usuário {#update-user-relationship}
{% apimethod patch %}
/custom_objects/objects/{type_name}/{external_id}/users
{% endapimethod %}

> Use este endpoint para mesclar atributos em um relacionamento de usuário existente.

{% alert important %}
Custom Objects está atualmente em acesso antecipado. Seu espaço de trabalho precisa estar ativado antes que as permissões de chave de API de Custom Objects apareçam em **Configurações** > **Chaves de API**.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisa de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `custom_objects.user_relationships.update`.

## Limite de frequência {#rate-limit}

Este endpoint está no bucket de escrita de Custom Objects com um limite padrão de 50 requisições por minuto.

## Parâmetros de caminho {#path-parameters}

A tabela a seguir lista e descreve os parâmetros de caminho para o endpoint `/custom_objects/objects/{type_name}/{external_id}/users`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `type_name` | Obrigatório | String | Tipo de objeto |
| `external_id` | Obrigatório | String | Identificador do objeto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de caminho para atualizar relacionamento de usuário" }

## Parâmetros de requisição {#request-parameters}

A tabela a seguir lista e descreve os parâmetros do corpo da requisição JSON para o endpoint `/custom_objects/objects/{type_name}/{external_id}/users`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `braze_id` | Obrigatório | String | ID do usuário da Braze |
| `rel_kind` | Obrigatório | String | Tipo de relacionamento |
| `attributes` | Opcional | Objeto | Atributos de relacionamento a serem mesclados |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de requisição para atualizar relacionamento de usuário" }

## Exemplo de requisição {#example-request}

Esta seção inclui um exemplo de carga útil JSON e um exemplo de requisição cURL.

### Exemplo de carga útil da requisição {#sample-request-payload}

```json
{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "billing_admin"
  }
}
```

### Exemplo de requisição cURL {#sample-curl-request}

Este exemplo altera o atributo `role` no relacionamento `account_user` existente para `billing_admin`, mantendo os demais atributos do relacionamento inalterados.

```bash
curl --location --request PATCH 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/users' \
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

A tabela a seguir lista e descreve os campos em uma resposta bem-sucedida.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `user_relationship` | Obrigatório | Objeto | Registro atualizado do relacionamento de usuário |
| `user_relationship.type_name` | Obrigatório | String | Nome de máquina do tipo de objeto personalizado |
| `user_relationship.external_id` | Obrigatório | String | Identificador do objeto personalizado |
| `user_relationship.rel_kind` | Obrigatório | String | Valor do tipo de relacionamento |
| `user_relationship.user` | Obrigatório | Objeto | Objeto de usuário vinculado |
| `user_relationship.user.braze_id` | Obrigatório | String | Identificador de usuário da Braze |
| `user_relationship.attributes` | Obrigatório | Objeto | Atributos do relacionamento após a mesclagem |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de resposta para atualizar relacionamento de usuário" }

## Erros {#errors}

A tabela a seguir lista erros comuns para este endpoint e como resolvê-los.

| Status | Causa | Orientação |
|---|---|---|
| `400` | Erro de validação | Confirme que `rel_kind` é válido para o tipo de objeto e que `attributes` correspondem ao esquema do relacionamento. |
| `404` | Relacionamento não encontrado (`custom-object-relationship-not-found`) | Confirme que o objeto, o usuário e os valores da chave de relacionamento existem. |
| `401` | Chave da API REST ausente ou inválida | Verifique se o header `Authorization` usa `Bearer YOUR_REST_API_KEY` e se a chave está ativa. |
| `403` | A chave de API não tem permissão ou a requisição está bloqueada pela lista de permissões | Confirme que a chave tem a permissão `custom_objects.user_relationships.update` e que o IP de origem está na lista de permissões da chave, se configurada. |
| `429` | Limite de frequência excedido | Tente novamente após `X-RateLimit-Reset` e reduza a frequência das requisições. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erros ao atualizar relacionamento de usuário" }
{% endapi %}