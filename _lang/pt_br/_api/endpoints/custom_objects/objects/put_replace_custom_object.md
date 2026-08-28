---
nav_title: "PUT: Substituir objeto personalizado"
article_title: "PUT: Substituir objeto personalizado"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Substituir objeto personalizado."
---
{% api %}
# Substituir objeto personalizado {#replace-custom-object}
{% apimethod put %}
/custom_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Use este endpoint para criar ou substituir um objeto personalizado com semântica de substituição completa de atributos.

{% alert important %}
Custom Objects está atualmente em acesso antecipado. Seu espaço de trabalho precisa estar ativado antes que as permissões da chave de API de Custom Objects apareçam em **Configurações** > **Chaves de API**.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisa de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `custom_objects.update`.

## Limite de frequência {#rate-limit}

Este endpoint está no bucket de escrita de Custom Objects com um limite padrão de 50 solicitações por minuto.

## Parâmetros de caminho {#path-parameters}

A tabela a seguir lista e descreve os parâmetros de caminho para o endpoint `/custom_objects/objects/{type_name}/{external_id}`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `type_name` | Obrigatório | String | Nome de máquina do tipo de objeto personalizado |
| `external_id` | Obrigatório | String | Identificador do objeto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de caminho para substituir objeto personalizado" }

## Parâmetros de solicitação {#request-parameters}

A tabela a seguir lista e descreve os parâmetros do corpo da solicitação JSON para o endpoint `/custom_objects/objects/{type_name}/{external_id}`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `attributes` | Obrigatório | Objeto | Atributos completos do objeto. Campos omitidos são apagados |
| `display_name` | Opcional | String | Rótulo de exibição do objeto. Quando o tipo tem um campo de origem de nome de exibição, o valor desse campo tem prioridade. O padrão é `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de solicitação para substituir objeto personalizado" }

## Exemplo de solicitação {#example-request}

Esta seção inclui uma carga útil JSON de exemplo e uma solicitação cURL de exemplo.

### Carga útil de exemplo {#sample-request-payload}

```json
{
  "attributes": {
    "name": "Updated Account"
  }
}
```

### Solicitação cURL de exemplo {#sample-curl-request}

Este exemplo substitui os atributos armazenados em `acct-123` pelos da carga útil. Se não existir um registro com esse identificador, esta solicitação o cria.

```bash
curl --location --request PUT 'https://rest.iad-01.braze.com/custom_objects/objects/account/acct-123' \
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

O código de status `200` pode retornar o corpo de resposta a seguir. Este endpoint retorna `200` independentemente de a solicitação ter criado ou substituído o objeto.

```json
{
  "custom_object": {
    "type_name": "account",
    "external_id": "acct-123",
    "attributes": { "name": "Updated Account" }
  }
}
```

### Parâmetros de resposta {#response-parameters}

A tabela a seguir lista e descreve os campos de uma resposta bem-sucedida.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `custom_object` | Obrigatório | Objeto | Registro de objeto personalizado criado ou substituído |
| `custom_object.type_name` | Obrigatório | String | Nome de máquina do tipo de objeto personalizado |
| `custom_object.external_id` | Obrigatório | String | Identificador do objeto personalizado |
| `custom_object.attributes` | Obrigatório | Objeto | Atributos armazenados do objeto, organizados por nome de campo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de resposta para substituir objeto personalizado" }

## Erros {#errors}

A tabela a seguir lista os erros comuns deste endpoint e como resolvê-los.

| Status | Causa | Orientação |
|---|---|---|
| `400` | Erro de validação | Confirme que cada campo em `attributes` existe no esquema do tipo e usa o tipo de dados correto. |
| `404` | Tipo não encontrado (`custom-object-type-not-found`) | Confirme que `type_name` existe no espaço de trabalho e corresponde exatamente ao nome de máquina. |
| `422` | Limite de registros atingido (`custom-object-record-limit-exceeded`) quando esta solicitação criaria um novo objeto | Reduza a contagem de objetos para o tipo ou entre em contato com o suporte da Braze sobre os limites do seu espaço de trabalho. |
| `401` | Chave da API REST ausente ou inválida | Verifique se o cabeçalho `Authorization` usa `Bearer YOUR_REST_API_KEY` e se a chave está ativa. |
| `403` | A chave de API não tem permissão ou a solicitação está bloqueada pela lista de permissões | Confirme que a chave tem `custom_objects.update` e que o IP de origem está na lista de permissões da chave, se configurado. |
| `429` | Limite de frequência excedido | Tente novamente após `X-RateLimit-Reset` e reduza a frequência de solicitações. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erros ao substituir objeto personalizado" }
{% endapi %}