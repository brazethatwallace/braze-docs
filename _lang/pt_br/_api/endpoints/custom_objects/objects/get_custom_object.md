---
nav_title: "GET: Obter objeto personalizado"
article_title: "GET: Obter objeto personalizado"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Obter objeto personalizado."
---
{% api %}
# Obter objeto personalizado {#get-custom-object}
{% apimethod get %}
/custom_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Use este endpoint para retornar um objeto personalizado.

{% alert important %}
Custom Objects está atualmente em acesso antecipado. Seu espaço de trabalho deve ser ativado antes que as permissões de chave de API de Custom Objects apareçam em **Configurações** > **Chaves de API**.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisa de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `custom_objects.read`.

## Limite de frequência {#rate-limit}

Este endpoint está no bucket de leitura de Custom Objects com um limite padrão de 50 solicitações por minuto.

## Parâmetros de caminho {#path-parameters}

A tabela a seguir lista e descreve os parâmetros de caminho para o endpoint `/custom_objects/objects/{type_name}/{external_id}`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `type_name` | Obrigatório | String | Nome de máquina do tipo de objeto personalizado |
| `external_id` | Obrigatório | String | Identificador do objeto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de caminho para obter objeto personalizado" }

## Exemplo de solicitação {#example-request}

Esta seção inclui um exemplo de carga útil de parâmetros de caminho e um exemplo de solicitação cURL.

### Exemplo de carga útil da solicitação {#sample-request-payload}

Use este objeto JSON como referência para os parâmetros de caminho desta solicitação.

```json
{
  "type_name": "account",
  "external_id": "acct-123"
}
```

### Exemplo de solicitação cURL {#sample-curl-request}

Este exemplo recupera o registro da conta `acct-123` e seus atributos armazenados.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Resposta {#response}

Esta seção inclui um exemplo de resposta bem-sucedida e os campos da resposta.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `200` pode retornar o seguinte corpo de resposta.

```json
{
  "custom_object": {
    "type_name": "account",
    "external_id": "acct-123",
    "attributes": { "name": "Acme", "industry": "software" }
  }
}
```

### Parâmetros de resposta {#response-parameters}

A tabela a seguir lista e descreve os campos em uma resposta bem-sucedida.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `custom_object` | Obrigatório | Objeto | Registro de objeto personalizado retornado |
| `custom_object.type_name` | Obrigatório | String | Nome de máquina do tipo de objeto personalizado |
| `custom_object.external_id` | Obrigatório | String | Identificador do objeto personalizado |
| `custom_object.attributes` | Obrigatório | Objeto | Atributos do objeto indexados pelo nome do campo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de resposta para obter objeto personalizado" }

## Erros {#errors}

A tabela a seguir lista erros comuns para este endpoint e como resolvê-los.

| Status | Causa | Orientação |
|---|---|---|
| `404` | Tipo não encontrado (`custom-object-type-not-found`) ou objeto não encontrado (`custom-object-not-found`) | Confirme que `type_name` e `external_id` existem no espaço de trabalho. |
| `401` | Chave da API REST ausente ou inválida | Verifique se o cabeçalho `Authorization` usa `Bearer YOUR_REST_API_KEY` e se a chave está ativa. |
| `403` | A chave de API não tem permissão ou a solicitação está bloqueada pela lista de permissões | Confirme que a chave possui `custom_objects.read` e que o IP de origem está na lista de permissões da chave, se configurada. |
| `429` | Limite de frequência excedido | Tente novamente após `X-RateLimit-Reset` e reduza a frequência das solicitações. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erros ao obter objeto personalizado" }
{% endapi %}