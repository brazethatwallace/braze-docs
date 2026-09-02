---
nav_title: "POST: Criar objeto de dados"
article_title: "POST: Criar objeto de dados"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Este artigo descreve os detalhes do endpoint Criar objeto de dados."
---
{% API or interface de programação do aplicativo (API) %}
# Criar objeto de dados {#create-data-object}
{% apimethod post %}
/data_objects/objects/{type_name}
{% endapimethod %}

> Use este endpoint para criar um objeto de dados para um tipo.

{% alert important %}
Objetos de dados está atualmente em acesso antecipado. Seu espaço de trabalho precisa estar ativado antes que as permissões de chave de API or interface de programação do aplicativo (API) de objetos de dados apareçam em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisa de uma [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `data_objects.create`.

## Limite de frequência {#rate-limit}

Este endpoint está no bucket de escrita de objetos de dados, com um limite padrão de 50 solicitações por minuto.

## Parâmetros de caminho {#path-parameters}

A tabela a seguir lista e descreve os parâmetros de caminho do endpoint `/data_objects/objects/{type_name}`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `type_name` | Obrigatório | String | Nome de máquina do tipo de objeto de dados |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de caminho para criar objeto de dados" }

## Parâmetros de solicitação {#request-parameters}

A tabela a seguir lista e descreve os parâmetros do corpo da solicitação JSON para o endpoint `/data_objects/objects/{type_name}`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `external_id` | Obrigatório | String | Identificador do objeto, único dentro do tipo |
| `attributes` | Obrigatório | Objeto | Valores com chave de nome de campo validados em relação ao esquema do tipo |
| `display_name` | Opcional | String | Rótulo de exibição para o objeto. Quando o tipo tem um campo de origem de nome de exibição, o valor desse campo tem precedência. O padrão é `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de solicitação para criar objeto de dados" }

## Exemplo de solicitação {#example-request}

Esta seção inclui uma carga útil JSON de exemplo e uma solicitação cURL de exemplo.

### Carga útil de solicitação de exemplo {#sample-request-payload}

```json
{
  "external_id": "acct-new",
  "attributes": {
    "name": "New Account",
    "industry": "software"
  }
}
```

### Solicitação cURL de exemplo {#sample-curl-request}

Este exemplo cria um registro `account` com o identificador `acct-new` e define seus atributos `name` e `industry`.

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/data_objects/objects/account' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "external_id": "acct-new",
  "attributes": {
    "name": "New Account",
    "industry": "software"
  }
}'
```

## Resposta {#response}

Esta seção inclui uma resposta de sucesso de exemplo e os campos da resposta.

### Exemplo de resposta de sucesso {#example-success-response}

O código de status `201` pode retornar o seguinte corpo de resposta.

```json
{
  "data_object": {
    "type_name": "account",
    "external_id": "acct-new",
    "attributes": { "name": "New Account", "industry": "software" }
  }
}
```

### Parâmetros de resposta {#response-parameters}

A tabela a seguir lista e descreve os campos em uma resposta de sucesso.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `data_object` | Obrigatório | Objeto | Registro do objeto de dados criado |
| `data_object.type_name` | Obrigatório | String | Nome de máquina do tipo de objeto de dados |
| `data_object.external_id` | Obrigatório | String | Identificador do objeto de dados |
| `data_object.attributes` | Obrigatório | Objeto | Atributos armazenados do objeto com chave por nome de campo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de resposta para criar objeto de dados" }

## Erros {#errors}

A tabela a seguir lista os erros comuns para este endpoint e como resolvê-los.

| Status | Causa | Orientação |
|---|---|---|
| `400` | Campo de atributo desconhecido ou tipo de atributo inválido | Confirme se todos os campos em `attributes` existem no esquema do tipo e usam o tipo de dados correto. |
| `404` | Tipo não encontrado (`data-object-type-not-found`) | Confirme se `type_name` existe no espaço de trabalho e corresponde exatamente ao nome de máquina. |
| `409` | Objeto duplicado (`duplicate-data-object`) | Use um `external_id` diferente ou use `PUT` para substituir o objeto existente. |
| `422` | Limite de registros atingido (`data-object-record-limit-exceeded`) | Reduza a quantidade de objetos para o tipo ou entre em contato com o suporte da Braze sobre os limites do seu espaço de trabalho. |
| `401` | Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional ausente ou inválida | Verifique se o cabeçalho `Authorization` usa `Bearer YOUR_REST_API_KEY` e se a chave está ativa. |
| `403` | A chave de API or interface de programação do aplicativo (API) não tem permissão ou a solicitação está bloqueada pela lista de permissões | Confirme se a chave tem `data_objects.create` e se o IP de origem está na lista de permissões da chave, caso configurada. |
| `429` | Limite de frequência excedido | Tente novamente após `X-RateLimit-Reset` e reduza a frequência de solicitações. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erros ao criar objeto de dados" }
{% endapi %}