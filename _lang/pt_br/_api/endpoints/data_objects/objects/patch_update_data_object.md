---
nav_title: "PATCH: Atualizar objeto de dados"
article_title: "PATCH: Atualizar objeto de dados"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Este artigo descreve os detalhes do endpoint Atualizar objeto de dados."
---
{% api %}
# Atualizar objeto de dados {#update-data-object}
{% apimethod patch %}
/data_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Use este endpoint para mesclar atributos em um objeto de dados existente.

{% alert important %}
Os objetos de dados estão atualmente em acesso antecipado. Seu espaço de trabalho precisa estar ativado para que as permissões de chave de API de objetos de dados apareçam em **Configurações** > **Chaves de API**.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisa de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `data_objects.update`.

## Limite de frequência {#rate-limit}

Este endpoint está no bucket de escrita de objetos de dados, com um limite padrão de 50 solicitações por minuto.

## Parâmetros de caminho {#path-parameters}

A tabela a seguir lista e descreve os parâmetros de caminho para o endpoint `/data_objects/objects/{type_name}/{external_id}`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `type_name` | Obrigatório | String | Nome de máquina do tipo de objeto de dados |
| `external_id` | Obrigatório | String | Identificador do objeto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Update data object path parameters" }

## Parâmetros de solicitação {#request-parameters}

A tabela a seguir lista e descreve os parâmetros do corpo da solicitação JSON para o endpoint `/data_objects/objects/{type_name}/{external_id}`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `attributes` | Obrigatório | Objeto | Campos de nível superior para mesclar |
| `display_name` | Opcional | String | Rótulo de exibição do objeto. Quando o tipo possui um campo de origem para nome de exibição, o valor desse campo tem precedência. Quando omitido, o nome de exibição existente é preservado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Update data object request parameters" }

## Exemplo de solicitação {#example-request}

Esta seção inclui uma carga útil JSON de exemplo e uma solicitação cURL de exemplo.

### Carga útil de exemplo {#sample-request-payload}

```json
{
  "attributes": {
    "credits": 750
  }
}
```

### Solicitação cURL de exemplo {#sample-curl-request}

Este exemplo atualiza o atributo `credits` em `acct-123` e mantém os demais atributos do registro inalterados.

```bash
curl --location --request PATCH 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{ "attributes": { "credits": 750 } }'
```

## Resposta {#response}

Esta seção inclui um exemplo de resposta bem-sucedida e os campos da resposta.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `200` pode retornar o seguinte corpo de resposta. O objeto `attributes` reflete o resultado da mesclagem.

```json
{
  "data_object": {
    "type_name": "account",
    "external_id": "acct-123",
    "attributes": { "name": "Acme", "credits": 750 }
  }
}
```

### Parâmetros de resposta {#response-parameters}

A tabela a seguir lista e descreve os campos de uma resposta bem-sucedida.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `data_object` | Obrigatório | Objeto | Registro do objeto de dados atualizado |
| `data_object.type_name` | Obrigatório | String | Nome de máquina do tipo de objeto de dados |
| `data_object.external_id` | Obrigatório | String | Identificador do objeto de dados |
| `data_object.attributes` | Obrigatório | Objeto | Atributos do objeto após a mesclagem |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Update data object response parameters" }

## Erros {#errors}

A tabela a seguir lista os erros comuns para este endpoint e como resolvê-los.

| Status | Causa | Orientação |
|---|---|---|
| `400` | Erro de validação | Confirme se todos os campos em `attributes` existem no esquema do tipo e usam o tipo de dados correto. |
| `404` | Tipo não encontrado ou objeto não encontrado | Confirme se `type_name` e `external_id` existem no espaço de trabalho. |
| `401` | Chave da API REST ausente ou inválida | Verifique se o cabeçalho `Authorization` usa `Bearer YOUR_REST_API_KEY` e se a chave está ativa. |
| `403` | A chave de API não possui permissão ou a solicitação está bloqueada pela lista de permissões | Confirme se a chave possui a permissão `data_objects.update` e se o IP de origem está na lista de permissões da chave, caso configurada. |
| `429` | Limite de frequência excedido | Tente novamente após `X-RateLimit-Reset` e reduza a frequência das solicitações. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Update data object errors" }
{% endapi %}