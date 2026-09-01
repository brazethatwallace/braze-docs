---
nav_title: "PATCH: Atualizar objeto personalizado"
article_title: "PATCH: Atualizar objeto personalizado"
search_tag: Endpoint
page_order: 5
layout: api_page
page_type: reference
description: "Este artigo descreve os detalhes sobre o endpoint Atualizar objeto personalizado."
---
{% api %}
# Atualizar objeto personalizado {#update-custom-object}
{% apimethod patch %}
/custom_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Use este endpoint para mesclar atributos em um objeto personalizado existente.

{% alert important %}
Custom Objects está atualmente em acesso antecipado. Seu espaço de trabalho precisa estar ativado antes que as permissões de chave de API de Custom Objects apareçam em **Configurações** > **Chaves de API**.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisa de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `custom_objects.update`.

## Limite de frequência {#rate-limit}

Este endpoint está no bucket de escrita de Custom Objects, com um limite padrão de 50 requisições por minuto.

## Parâmetros de caminho {#path-parameters}

A tabela a seguir lista e descreve os parâmetros de caminho para o endpoint `/custom_objects/objects/{type_name}/{external_id}`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `type_name` | Obrigatório | String | Nome de máquina do tipo de objeto personalizado |
| `external_id` | Obrigatório | String | Identificador do objeto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de caminho para atualizar objeto personalizado" }

## Parâmetros de requisição {#request-parameters}

A tabela a seguir lista e descreve os parâmetros do corpo da requisição JSON para o endpoint `/custom_objects/objects/{type_name}/{external_id}`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `attributes` | Obrigatório | Objeto | Campos de nível superior para mesclar |
| `display_name` | Opcional | String | Rótulo de exibição do objeto. Quando o tipo possui um campo de origem para o nome de exibição, o valor desse campo tem prioridade. Quando omitido, o nome de exibição existente é preservado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de requisição para atualizar objeto personalizado" }

## Exemplo de requisição {#example-request}

Esta seção inclui um exemplo de carga útil JSON e um exemplo de requisição cURL.

### Exemplo de carga útil da requisição {#sample-request-payload}

```json
{
  "attributes": {
    "credits": 750
  }
}
```

### Exemplo de requisição cURL {#sample-curl-request}

Este exemplo atualiza o atributo `credits` em `acct-123` e deixa os demais atributos do registro inalterados.

```bash
curl --location --request PATCH 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123' \
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
  "custom_object": {
    "type_name": "account",
    "external_id": "acct-123",
    "attributes": { "name": "Acme", "credits": 750 }
  }
}
```

### Parâmetros de resposta {#response-parameters}

A tabela a seguir lista e descreve os campos em uma resposta bem-sucedida.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `custom_object` | Obrigatório | Objeto | Registro do objeto personalizado atualizado |
| `custom_object.type_name` | Obrigatório | String | Nome de máquina do tipo de objeto personalizado |
| `custom_object.external_id` | Obrigatório | String | Identificador do objeto personalizado |
| `custom_object.attributes` | Obrigatório | Objeto | Atributos do objeto após a mesclagem |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de resposta para atualizar objeto personalizado" }

## Erros {#errors}

A tabela a seguir lista os erros comuns para este endpoint e como resolvê-los.

| Status | Causa | Orientação |
|---|---|---|
| `400` | Erro de validação | Confirme se todos os campos em `attributes` existem no esquema do tipo e usam o tipo de dados correto. |
| `404` | Tipo não encontrado ou objeto não encontrado | Confirme se `type_name` e `external_id` existem no espaço de trabalho. |
| `401` | Chave da API REST ausente ou inválida | Verifique se o cabeçalho `Authorization` usa `Bearer YOUR_REST_API_KEY` e se a chave está ativa. |
| `403` | A chave de API não tem permissão ou a requisição está bloqueada pela lista de permissões | Confirme se a chave possui `custom_objects.update` e se o IP de origem está na lista de permissões da chave, se configurado. |
| `429` | Limite de frequência excedido | Tente novamente após `X-RateLimit-Reset` e reduza a frequência das requisições. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erros ao atualizar objeto personalizado" }
{% endapi %}