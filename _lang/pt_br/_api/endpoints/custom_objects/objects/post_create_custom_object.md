---
nav_title: "POST: Criar objeto personalizado"
article_title: "POST: Criar objeto personalizado"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Este artigo descreve os detalhes do endpoint Criar objeto personalizado."
---
{% api %}
# Criar objeto personalizado {#create-custom-object}
{% apimethod post %}
/custom_objects/objects/{type_name}
{% endapimethod %}

> Use este endpoint para criar um objeto personalizado para um tipo.

{% alert important %}
Objetos personalizados está atualmente em acesso antecipado. Seu espaço de trabalho precisa estar ativado antes que as permissões da chave de API de objetos personalizados apareçam em **Configurações** > **Chaves de API**.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisa de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `custom_objects.create`.

## Limite de frequência {#rate-limit}

Este endpoint está no bucket de escrita de objetos personalizados com um limite padrão de 50 solicitações por minuto.

## Parâmetros de caminho {#path-parameters}

A tabela a seguir lista e descreve os parâmetros de caminho para o endpoint `/custom_objects/objects/{type_name}`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `type_name` | Obrigatório | String | Nome de máquina do tipo de objeto personalizado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de caminho para criar objeto personalizado" }

## Parâmetros de solicitação {#request-parameters}

A tabela a seguir lista e descreve os parâmetros do corpo da solicitação JSON para o endpoint `/custom_objects/objects/{type_name}`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `external_id` | Obrigatório | String | Identificador do objeto, exclusivo dentro do tipo |
| `attributes` | Obrigatório | Objeto | Valores com chave de nome de campo validados em relação ao esquema do tipo |
| `display_name` | Opcional | String | Rótulo de exibição do objeto. Quando o tipo tem um campo de origem de nome de exibição, o valor desse campo tem precedência. O padrão é `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de solicitação para criar objeto personalizado" }

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
curl --location --request POST 'https://rest.iad-01.braze.com/custom_objects/objects/account' \
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

Esta seção inclui um exemplo de resposta bem-sucedida e os campos de resposta.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `201` pode retornar o seguinte corpo de resposta.

```json
{
  "custom_object": {
    "type_name": "account",
    "external_id": "acct-new",
    "attributes": { "name": "New Account", "industry": "software" }
  }
}
```

### Parâmetros de resposta {#response-parameters}

A tabela a seguir lista e descreve os campos em uma resposta bem-sucedida.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `custom_object` | Obrigatório | Objeto | Registro de objeto personalizado criado |
| `custom_object.type_name` | Obrigatório | String | Nome de máquina do tipo de objeto personalizado |
| `custom_object.external_id` | Obrigatório | String | Identificador do objeto personalizado |
| `custom_object.attributes` | Obrigatório | Objeto | Atributos armazenados do objeto com chave de nome de campo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de resposta para criar objeto personalizado" }

## Erros {#errors}

A tabela a seguir lista os erros comuns para este endpoint e como resolvê-los.

| Status | Causa | Orientação |
|---|---|---|
| `400` | Campo de atributo desconhecido ou tipo de atributo inválido | Confirme que todos os campos em `attributes` existem no esquema do tipo e usam o tipo de dados correto. |
| `404` | Tipo não encontrado (`custom-object-type-not-found`) | Confirme que o `type_name` existe no espaço de trabalho e corresponde exatamente ao nome de máquina. |
| `409` | Objeto duplicado (`duplicate-custom-object`) | Use um `external_id` diferente ou use `PUT` para substituir o objeto existente. |
| `422` | Limite de registros atingido (`custom-object-record-limit-exceeded`) | Reduza a contagem de objetos para o tipo ou entre em contato com o suporte da Braze sobre os limites do seu espaço de trabalho. |
| `401` | Chave da API REST ausente ou inválida | Verifique se o cabeçalho `Authorization` usa `Bearer YOUR_REST_API_KEY` e se a chave está ativa. |
| `403` | A chave de API não tem permissão ou a solicitação está bloqueada pela lista de permissões | Confirme que a chave tem `custom_objects.create` e que seu IP de origem está na lista de permissões da chave, se configurada. |
| `429` | Limite de frequência excedido | Tente novamente após `X-RateLimit-Reset` e reduza a frequência de solicitações. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erros ao criar objeto personalizado" }
{% endapi %}