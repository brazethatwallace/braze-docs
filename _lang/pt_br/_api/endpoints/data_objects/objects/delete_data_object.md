---
nav_title: "DELETE: Excluir objeto de dados"
article_title: "DELETE: Excluir objeto de dados"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "Este artigo descreve os detalhes do endpoint para exclusão de objeto de dados."
---
{% api %}
# Excluir objeto de dados {#delete-data-object}
{% apimethod delete %}
/data_objects/objects/{type_name}/{external_id}
{% endapimethod %}

> Use este endpoint para excluir um objeto de dados.

{% alert important %}
Data Objects está atualmente em acesso antecipado. Seu espaço de trabalho precisa estar ativado antes que as permissões de chave de API de Data Objects apareçam em **Configurações** > **Chaves de API**.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisa de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `data_objects.delete`.

## Limite de frequência {#rate-limit}

Este endpoint está no bucket de escrita de Data Objects, com um limite padrão de 50 solicitações por minuto.

## Parâmetros de caminho {#path-parameters}

A tabela a seguir lista e descreve os parâmetros de caminho para o endpoint `/data_objects/objects/{type_name}/{external_id}`.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `type_name` | Obrigatório | String | Nome de máquina do tipo de objeto de dados |
| `external_id` | Obrigatório | String | Identificador do objeto |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de caminho para exclusão de objeto de dados" }

## Exemplo de solicitação {#example-request}

Esta seção inclui um exemplo de carga útil de parâmetros de caminho e um exemplo de solicitação cURL.

### Exemplo de carga útil da solicitação {#sample-request-payload}

Use este objeto JSON como referência para os parâmetros de caminho nesta solicitação.

```json
{
  "type_name": "account",
  "external_id": "acct-123"
}
```

### Exemplo de solicitação cURL {#sample-curl-request}

Este exemplo exclui o registro de conta `acct-123`.

```bash
curl --location --request DELETE 'https://rest.iad-01.braze.com/data_objects/objects/account/acct-123' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

## Resposta {#response}

Esta seção inclui um exemplo de resposta bem-sucedida e os campos de resposta.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `200` pode retornar o seguinte corpo de resposta.

```json
{ "deleted": true }
```

A exclusão é síncrona. Excluir um objeto não exclui objetos relacionados.

### Parâmetros de resposta {#response-parameters}

A tabela a seguir lista e descreve os campos em uma resposta bem-sucedida.

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `deleted` | Obrigatório | Booleano | Se a exclusão do objeto foi bem-sucedida |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de resposta para exclusão de objeto de dados" }

## Erros {#errors}

A tabela a seguir lista os erros comuns para este endpoint e como resolvê-los.

| Status | Causa | Orientação |
|---|---|---|
| `404` | Tipo não encontrado ou objeto não encontrado | Confirme que `type_name` e `external_id` existem no espaço de trabalho. |
| `401` | Chave da API REST ausente ou inválida | Verifique se o cabeçalho `Authorization` usa `Bearer YOUR_REST_API_KEY` e se a chave está ativa. |
| `403` | A chave de API não tem permissão ou a solicitação foi bloqueada pela lista de permissões | Confirme que a chave tem a permissão `data_objects.delete` e que o IP de origem está na lista de permissões da chave, se configurada. |
| `429` | Limite de frequência excedido | Tente novamente após `X-RateLimit-Reset` e reduza a frequência de solicitações. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Erros de exclusão de objeto de dados" }
{% endapi %}