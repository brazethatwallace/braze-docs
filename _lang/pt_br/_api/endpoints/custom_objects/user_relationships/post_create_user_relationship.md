---
nav_title: "POST: Criar relacionamento de usuário"
article_title: "POST: Criar relacionamento de usuário"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Criar relacionamento de usuário."
---
{% api %}
# Criar relacionamento de usuário {#create-user-relationship}
{% apimethod post %}
/custom_objects/objects/{type_name}/{external_id}/users
{% endapimethod %}

> Use este endpoint para vincular um usuário da Braze a um objeto personalizado.

{% alert important %}
Custom Objects está atualmente em acesso antecipado. Seu espaço de trabalho precisa ser ativado antes que as permissões de chave de API de Custom Objects apareçam em **Configurações** > **Chaves de API**.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisa de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `custom_objects.user_relationships.create`.

## Limite de frequência {#rate-limit}

Este endpoint está no bucket de escrita de Custom Objects com um limite padrão de 50 solicitações por minuto.

## Parâmetros de caminho {#path-parameters}

A tabela a seguir lista e descreve os parâmetros de caminho para o endpoint `/custom_objects/objects/{type_name}/{external_id}/users`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `type_name` | Obrigatório | String | Tipo de objeto |
| `external_id` | Obrigatório | String | Identificador do objeto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de caminho para criar relacionamento de usuário" }

## Parâmetros de solicitação {#request-parameters}

A tabela a seguir lista e descreve os parâmetros do corpo da solicitação JSON para o endpoint `/custom_objects/objects/{type_name}/{external_id}/users`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `braze_id` | Obrigatório | String | ID de usuário da Braze |
| `rel_kind` | Obrigatório | String | Tipo de relacionamento |
| `attributes` | Opcional | Objeto | Atributos do relacionamento |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de solicitação para criar relacionamento de usuário" }

## Exemplo de solicitação {#example-request}

Esta seção inclui uma carga útil JSON de exemplo e uma solicitação cURL de exemplo.

### Carga útil de exemplo {#sample-request-payload}

```json
{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "owner"
  }
}
```

### Solicitação cURL de exemplo {#sample-curl-request}

Este exemplo vincula um usuário a `acct-123` como `account_user` e registra seu `role` como `owner`.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/users' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "owner"
  }
}'
```

## Resposta {#response}

Esta seção inclui um exemplo de resposta bem-sucedida e os campos da resposta.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `201` pode retornar o seguinte corpo de resposta.

```json
{
  "user_relationship": {
    "type_name": "account",
    "external_id": "acct-123",
    "rel_kind": "account_user",
    "user": { "braze_id": "507f1f77bcf86cd799439011" },
    "attributes": { "role": "owner" }
  }
}
```

### Parâmetros da resposta {#response-parameters}

A tabela a seguir lista e descreve os campos em uma resposta bem-sucedida.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `user_relationship` | Obrigatório | Objeto | Registro do relacionamento de usuário criado |
| `user_relationship.type_name` | Obrigatório | String | Nome de máquina do tipo de objeto personalizado |
| `user_relationship.external_id` | Obrigatório | String | Identificador do objeto personalizado |
| `user_relationship.rel_kind` | Obrigatório | String | Valor do tipo de relacionamento |
| `user_relationship.user` | Obrigatório | Objeto | Objeto do usuário vinculado |
| `user_relationship.user.braze_id` | Obrigatório | String | Identificador do usuário da Braze |
| `user_relationship.attributes` | Obrigatório | Objeto | Atributos do relacionamento |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros da resposta de criar relacionamento de usuário" }

## Erros {#errors}

A tabela a seguir lista os erros comuns deste endpoint e como resolvê-los.

| Status | Causa | Orientação |
|---|---|---|
| `400` | `rel_kind` desconhecido para o tipo ou erro de validação de esquema | Confirme que `rel_kind` é válido para o tipo de objeto e que `attributes` corresponde ao esquema do relacionamento. |
| `404` | Tipo ou objeto não encontrado | Confirme que `type_name` e `external_id` existem no espaço de trabalho. |
| `409` | Relacionamento duplicado (`duplicate-user-relationship`) | Use `PUT` para substituir o relacionamento existente ou exclua-o antes de criar novamente. |
| `422` | Limite de objetos por usuário atingido (`custom-objects-per-user-limit-exceeded`) ou limite de usuários por objeto atingido (`users-per-custom-object-limit-exceeded`) | Reduza a contagem de relacionamentos do usuário ou do objeto, ou entre em contato com o suporte da Braze sobre os limites do seu espaço de trabalho. |
| `401` | Chave da API REST ausente ou inválida | Verifique se o cabeçalho `Authorization` usa `Bearer YOUR_REST_API_KEY` e se a chave está ativa. |
| `403` | A chave de API não tem permissão ou a solicitação está bloqueada pela lista de permissões | Confirme que a chave tem `custom_objects.user_relationships.create` e que o IP de origem está na lista de permissões da chave, se configurada. |
| `429` | Limite de frequência excedido | Tente novamente após `X-RateLimit-Reset` e reduza a frequência das solicitações. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erros de criar relacionamento de usuário" }
{% endapi %}