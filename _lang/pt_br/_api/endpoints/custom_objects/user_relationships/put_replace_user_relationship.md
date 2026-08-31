---
nav_title: "PUT: Substituir relacionamento de usuário"
article_title: "PUT: Substituir relacionamento de usuário"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Substituir relacionamento de usuário."
---
{% api %}
# Substituir relacionamento de usuário {#replace-user-relationship}
{% apimethod put %}
/custom_objects/objects/{type_name}/{external_id}/users
{% endapimethod %}

> Use este endpoint para criar ou substituir um relacionamento de usuário.

{% alert important %}
Custom Objects está atualmente em acesso antecipado. Seu espaço de trabalho precisa estar ativado antes que as permissões da chave de API de Custom Objects apareçam em **Configurações** > **Chaves de API**.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisa de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `custom_objects.user_relationships.update`.

## Limite de frequência {#rate-limit}

Este endpoint está no bucket de escrita de Custom Objects com um limite padrão de 50 solicitações por minuto.

## Parâmetros de caminho {#path-parameters}

A tabela a seguir lista e descreve os parâmetros de caminho para o endpoint `/custom_objects/objects/{type_name}/{external_id}/users`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `type_name` | Obrigatório | String | Tipo de objeto |
| `external_id` | Obrigatório | String | Identificador do objeto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de caminho para substituir relacionamento de usuário" }

## Parâmetros de solicitação {#request-parameters}

A tabela a seguir lista e descreve os parâmetros do corpo da solicitação JSON para o endpoint `/custom_objects/objects/{type_name}/{external_id}/users`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `braze_id` | Obrigatório | String | ID do usuário da Braze |
| `rel_kind` | Obrigatório | String | Tipo de relacionamento |
| `attributes` | Opcional | Objeto | Atributos do relacionamento |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de solicitação para substituir relacionamento de usuário" }

## Exemplo de solicitação {#example-request}

Esta seção inclui um exemplo de carga útil JSON e um exemplo de solicitação cURL.

### Exemplo de carga útil da solicitação {#sample-request-payload}

```json
{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "admin"
  }
}
```

### Exemplo de solicitação cURL {#sample-curl-request}

Este exemplo substitui os atributos no relacionamento `account_user` entre o usuário e `acct-123`, sobrescrevendo quaisquer atributos armazenados anteriormente nele.

```bash
curl --location --request PUT 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123/users' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user",
  "attributes": {
    "role": "admin"
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
    "attributes": { "role": "admin" }
  }
}
```

### Parâmetros de resposta {#response-parameters}

A tabela a seguir lista e descreve os campos em uma resposta bem-sucedida.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `user_relationship` | Obrigatório | Objeto | Registro de relacionamento de usuário criado ou substituído |
| `user_relationship.type_name` | Obrigatório | String | Nome de máquina do tipo de objeto personalizado |
| `user_relationship.external_id` | Obrigatório | String | Identificador do objeto personalizado |
| `user_relationship.rel_kind` | Obrigatório | String | Valor do tipo de relacionamento |
| `user_relationship.user` | Obrigatório | Objeto | Objeto de usuário vinculado |
| `user_relationship.user.braze_id` | Obrigatório | String | Identificador de usuário da Braze |
| `user_relationship.attributes` | Obrigatório | Objeto | Atributos do relacionamento |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de resposta para substituir relacionamento de usuário" }

## Erros {#errors}

A tabela a seguir lista os erros comuns para este endpoint e como resolvê-los.

| Status | Causa | Orientação |
|---|---|---|
| `400` | Erro de validação | Confirme que `rel_kind` é válido para o tipo de objeto e que `attributes` correspondem ao esquema do relacionamento. |
| `404` | Relacionamento ou objeto não encontrado (`custom-object-relationship-not-found`) | Confirme que o objeto, o usuário e os valores de chave do relacionamento existem. |
| `422` | Limite de objetos por usuário atingido (`custom-objects-per-user-limit-exceeded`) ou limite de usuários por objeto atingido (`users-per-custom-object-limit-exceeded`) | Reduza a contagem de relacionamentos para o usuário ou o objeto, ou entre em contato com o suporte da Braze sobre os limites do seu espaço de trabalho. |
| `401` | Chave da API REST ausente ou inválida | Verifique se o cabeçalho `Authorization` usa `Bearer YOUR_REST_API_KEY` e se a chave está ativa. |
| `403` | A chave de API não tem permissão ou a solicitação está bloqueada pela lista de permissões | Confirme que a chave possui `custom_objects.user_relationships.update` e que o IP de origem está na lista de permissões da chave, se configurada. |
| `429` | Limite de frequência excedido | Tente novamente após `X-RateLimit-Reset` e reduza a frequência das solicitações. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erros ao substituir relacionamento de usuário" }
{% endapi %}