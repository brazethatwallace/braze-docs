---
nav_title: "GET: Obter tipo de objeto de dados"
article_title: "GET: Obter tipo de objeto de dados"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "Este artigo descreve os detalhes do endpoint Obter tipo de objeto de dados."
---
{% API or interface de programação do aplicativo (API) %}
# Obter tipo de objeto de dados {#get-data-object-type}
{% apimethod get %}
/data_objects/types/{type_name}
{% endapimethod %}

> Use este endpoint para retornar um tipo de objeto de dados e sua definição de esquema.

{% alert important %}
Objetos de dados está atualmente em acesso antecipado. Seu espaço de trabalho precisa estar ativado antes que as permissões de chave de API or interface de programação do aplicativo (API) de objetos de dados apareçam em **Configurações** > **Chaves de API or interface de programação do aplicativo (API)**.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisa de uma [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `data_objects.read`.

## Limite de frequência {#rate-limit}

Este endpoint está no bucket de leitura de objetos de dados, com um limite padrão de 50 solicitações por minuto.

## Parâmetros de caminho {#path-parameters}

A tabela a seguir lista e descreve os parâmetros de caminho para o endpoint `/data_objects/types/{type_name}`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `type_name` | Obrigatório | String | Nome de máquina do tipo de objeto de dados |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de caminho do endpoint Obter tipo de objeto de dados" }

## Exemplo de solicitação {#example-request}

Esta seção inclui um exemplo de carga útil de parâmetro de caminho e um exemplo de solicitação cURL.

### Exemplo de carga útil da solicitação {#sample-request-payload}

Use este objeto JSON como referência para o parâmetro de caminho nesta solicitação.

```json
{
  "type_name": "account"
}
```

### Exemplo de solicitação cURL {#sample-curl-request}

Este exemplo recupera a definição do tipo de objeto de dados `account`.

```bash
curl --location --request GET 'https://rest.iad-01.braze.com/data_objects/types/account' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Resposta {#response}

Esta seção inclui um exemplo de resposta bem-sucedida e os campos da resposta.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `200` pode retornar o seguinte corpo de resposta.

```json
{
  "data_object_type": {
    "type_name": "account",
    "metadata": { "display_name_source": "name" },
    "schema_def": {
      "type": "object",
      "properties": {
        "name": { "type": "string", "title": "Name" },
        "industry": { "type": "string", "title": "Industry" },
        "renewal_date": { "type": "string", "format": "date-time", "title": "Renewal date" }
      },
      "required": ["name"]
    }
  }
}
```

`schema_def` descreve os campos permitidos do objeto. As operações de escrita ainda rejeitam campos não declarados, mesmo que o esquema desta resposta seja descritivo.

### Parâmetros da resposta {#response-parameters}

A tabela a seguir lista e descreve os campos de uma resposta bem-sucedida.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `data_object_type` | Obrigatório | Objeto | Registro do tipo de objeto de dados retornado |
| `data_object_type.type_name` | Obrigatório | String | Nome de máquina do tipo de objeto de dados |
| `data_object_type.metadata` | Obrigatório | Objeto | Objeto de metadados do tipo |
| `data_object_type.schema_def` | Obrigatório | Objeto | Definição de esquema JSON para os atributos do objeto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros da resposta do endpoint Obter tipo de objeto de dados" }

## Erros {#errors}

A tabela a seguir lista os erros comuns para este endpoint e como resolvê-los.

| Status | Causa | Orientação |
|---|---|---|
| `404` | Tipo não encontrado (`data-object-type-not-found`) | Confirme se `type_name` existe no espaço de trabalho e corresponde exatamente ao nome de máquina. |
| `401` | Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional ausente ou inválida | Verifique se o cabeçalho `Authorization` usa `Bearer YOUR_REST_API_KEY` e se a chave está ativa. |
| `403` | A chave de API or interface de programação do aplicativo (API) não tem permissão ou a solicitação está bloqueada pela lista de permissões | Confirme se a chave possui a permissão `data_objects.read` e se o IP de origem está na lista de permissões da chave, caso configurada. |
| `429` | Limite de frequência excedido | Tente novamente após `X-RateLimit-Reset` e reduza a frequência das solicitações. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erros do endpoint Obter tipo de objeto de dados" }
{% endapi %}