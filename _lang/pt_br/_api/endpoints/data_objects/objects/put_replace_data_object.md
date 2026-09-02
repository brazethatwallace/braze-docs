---
nav_title: "PUT: Substituir objeto de dados"
article_title: "PUT: Substituir objeto de dados"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Substituir objeto de dados."
---
{% API or interface de programação do aplicativo (API) %}
# Substituir objeto de dados {#replace-data-object}
{% apimethod put %}
/data_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Use este endpoint para criar ou substituir um objeto de dados com semântica de substituição completa de atributos.

{% alert important %}
Data Objects está atualmente em acesso antecipado. Seu espaço de trabalho precisa estar ativado antes que as permissões de chave de API or interface de programação do aplicativo (API) de Data Objects apareçam em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisa de uma [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `data_objects.update`.

## Limite de frequência {#rate-limit}

Este endpoint está no bucket de escrita de Data Objects com um limite padrão de 50 requisições por minuto.

## Parâmetros de caminho {#path-parameters}

A tabela a seguir lista e descreve os parâmetros de caminho para o endpoint `/data_objects/objects/{type_name}/{external_id}`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `type_name` | Obrigatório | String | Nome de máquina do tipo de objeto de dados |
| `external_id` | Obrigatório | String | Identificador do objeto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Replace data object jornada parameters" }

## Parâmetros de requisição {#request-parameters}

A tabela a seguir lista e descreve os parâmetros do corpo da requisição JSON para o endpoint `/data_objects/objects/{type_name}/{external_id}`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `attributes` | Obrigatório | Objeto | Atributos completos do objeto. Campos omitidos serão apagados |
| `display_name` | Opcional | String | Rótulo de exibição para o objeto. Quando o tipo possui um campo de origem de nome de exibição, o valor desse campo tem precedência. O padrão é `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Replace data object request parameters" }

## Exemplo de requisição {#example-request}

Esta seção inclui um exemplo de carga útil JSON e um exemplo de requisição cURL.

### Exemplo de carga útil da requisição {#sample-request-payload}

```json
{
  "attributes": {
    "name": "Updated Account"
  }
}
```

### Exemplo de requisição cURL {#sample-curl-request}

Este exemplo substitui os atributos armazenados em `acct-123` pelos da carga útil. Se nenhum registro com esse identificador existir, esta requisição o criará.

```bash
curl --location --request PUT 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "attributes": {
    "name": "Updated Account"
  }
}'
```

## Resposta {#response}

Esta seção inclui um exemplo de resposta bem-sucedida e os campos da resposta.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `200` pode retornar o seguinte corpo de resposta. Este endpoint retorna `200` independentemente de a requisição ter criado ou substituído o objeto.

```json
{
  "data_object": {
    "type_name": "account",
    "external_id": "acct-123",
    "attributes": { "name": "Updated Account" }
  }
}
```

### Parâmetros de resposta {#response-parameters}

A tabela a seguir lista e descreve os campos em uma resposta bem-sucedida.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `data_object` | Obrigatório | Objeto | Registro de objeto de dados criado ou substituído |
| `data_object.type_name` | Obrigatório | String | Nome de máquina do tipo de objeto de dados |
| `data_object.external_id` | Obrigatório | String | Identificador do objeto de dados |
| `data_object.attributes` | Obrigatório | Objeto | Atributos armazenados do objeto, organizados por nome de campo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Replace data object response parameters" }

## Erros {#errors}

A tabela a seguir lista erros comuns para este endpoint e como resolvê-los.

| Status | Causa | Orientação |
|---|---|---|
| `400` | Erro de validação | Confirme que cada campo em `attributes` existe no esquema do tipo e usa o tipo de dados correto. |
| `404` | Tipo não encontrado (`data-object-type-not-found`) | Confirme que `type_name` existe no espaço de trabalho e corresponde exatamente ao nome de máquina. |
| `422` | Limite de registros atingido (`data-object-record-limit-exceeded`) quando esta requisição criaria um novo objeto | Reduza a contagem de objetos para o tipo ou entre em contato com o suporte da Braze sobre os limites do seu espaço de trabalho. |
| `401` | Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional ausente ou inválida | Verifique se o cabeçalho `Authorization` usa `Bearer YOUR_REST_API_KEY` e se a chave está ativa. |
| `403` | A chave de API or interface de programação do aplicativo (API) não tem permissão ou a requisição está bloqueada pela lista de permissões | Confirme que a chave possui `data_objects.update` e que o IP de origem está na lista de permissões da chave, se configurada. |
| `429` | Limite de frequência excedido | Tente novamente após `X-RateLimit-Reset` e reduza a frequência de requisições. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Replace data object errors" }
{% endapi %}