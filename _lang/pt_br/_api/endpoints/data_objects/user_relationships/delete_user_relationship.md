---
nav_title: "DELETE: Excluir relacionamento de usuário"
article_title: "DELETE: Excluir relacionamento de usuário"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint para excluir relacionamento de usuário."
---
{% api %}
# Excluir relacionamento de usuário {#delete-user-relationship}
{% apimethod delete %}
/data_objects/objects/{type_name}/{external_id}/users
{% endapimethod %}

> Use este endpoint para remover um relacionamento entre usuário e objeto.

{% alert important %}
Data Objects está atualmente em acesso antecipado. Seu espaço de trabalho precisa estar ativado antes que as permissões de chave de API de Data Objects apareçam em **Configurações** > **Chaves de API**.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisa de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `data_objects.user_relationships.delete`.

## Limite de frequência {#rate-limit}

Este endpoint está no bucket de escrita de Data Objects com um limite padrão de 50 solicitações por minuto.

## Parâmetros de caminho {#path-parameters}

A tabela a seguir lista e descreve os parâmetros de caminho para o endpoint `/data_objects/objects/{type_name}/{external_id}/users`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `type_name` | Obrigatório | String | Tipo do objeto |
| `external_id` | Obrigatório | String | Identificador do objeto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de caminho para excluir relacionamento de usuário" }

## Parâmetros de solicitação {#request-parameters}

A tabela a seguir lista e descreve os parâmetros do corpo da solicitação JSON para o endpoint `/data_objects/objects/{type_name}/{external_id}/users`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `braze_id` | Obrigatório | String | ID de usuário da Braze |
| `rel_kind` | Obrigatório | String | Tipo de relacionamento |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de solicitação para excluir relacionamento de usuário" }

{% alert note %}
Este endpoint `DELETE` espera um corpo de solicitação JSON. Confirme que seu cliente HTTP envia corpos de solicitação em chamadas `DELETE`.
{% endalert %}

## Exemplo de solicitação {#example-request}

Esta seção inclui um exemplo de carga útil JSON e um exemplo de solicitação cURL.

### Exemplo de carga útil da solicitação {#sample-request-payload}

```json
{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user"
}
```

### Exemplo de solicitação cURL {#sample-curl-request}

Este exemplo remove o relacionamento `account_user` entre o usuário especificado e `acct-123`. O perfil de usuário e o registro da conta permanecem intactos.

```bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123/users' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "braze_id": "507f1f77bcf86cd799439011",
  "rel_kind": "account_user"
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
| `deleted` | Obrigatório | Booleano | Se a exclusão do relacionamento foi bem-sucedida |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de resposta para excluir relacionamento de usuário" }

## Erros {#errors}

A tabela a seguir lista os erros comuns para este endpoint e como resolvê-los.

| Status | Causa | Orientação |
|---|---|---|
| `400` | Erro de validação | Confirme que o corpo da solicitação inclui valores válidos para `braze_id` e `rel_kind`. |
| `404` | Relacionamento ou objeto não encontrado | Confirme que o objeto, o usuário e os valores da chave de relacionamento existem. |
| `401` | Chave da REST API ausente ou inválida | Verifique se o cabeçalho `Authorization` usa `Bearer YOUR_REST_API_KEY` e se a chave está ativa. |
| `403` | A chave de API não tem permissão ou a solicitação está bloqueada pela lista de permissões | Confirme que a chave tem a permissão `data_objects.user_relationships.delete` e que seu IP de origem está na lista de permissões da chave, se configurada. |
| `429` | Limite de frequência excedido | Tente novamente após `X-RateLimit-Reset` e reduza a frequência de solicitações. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erros do endpoint de excluir relacionamento de usuário" }
{% endapi %}