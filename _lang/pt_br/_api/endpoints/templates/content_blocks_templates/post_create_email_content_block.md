---
nav_title: "POST: Criar bloco de conteúdo"
article_title: "POST: Criar bloco de conteúdo"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze \"Criar bloco de conteúdo\"."
---
{% api %}
# Criar bloco de conteúdo {#create-content-block}
{% apimethod post %}
/content_blocks/create
{% endapimethod %}

> Use esse endpoint para criar um [bloco de conteúdo]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks).

{% alert tip %}
Você também pode chamar esse endpoint por meio do [servidor MCP da Braze]({{site.baseurl}}/user_guide/brazeai/mcp_server) usando a função [`create_content_block`]({{site.baseurl}}/user_guide/brazeai/mcp_server/available_api_functions#content-blocks). Isso permite que ferramentas de IA como Claude e Cursor criem blocos de conteúdo por meio de prompts em linguagem natural.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#f1cefa8b-7a28-4e64-b579-198a4610d0a5 {% endapiref %}

## Pré-requisitos {#prerequisites}
Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics) com a permissão `content_blocks.create`.

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "name": (required, string) Must be less than 100 characters,
  "description": (optional, string) The description of the Content Block. Must be less than 250 character,
  "content": (required, string) HTML or text content within Content Block,
  "state": (optional, string) Choose `active` or `draft`. Defaults to `active` if not specified,
  "tags": (optional, array of strings) Tags must already exist
}
```

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `name` | Obrigatório | String | Nome do bloco de conteúdo. Deve ter menos de 100 caracteres. |
| `description` | Opcional | String | Descrição do bloco de conteúdo. Deve ter menos de 250 caracteres. |
| `content` | Obrigatório | String | Conteúdo HTML ou de texto no bloco de conteúdo. |
| `state` | Opcional | String | Escolha `active` ou `draft`. O padrão é `active` se não for especificado. |
| `tags` | Opcional | Matriz de strings | As [tags]({{site.baseurl}}/user_guide/messaging/governance/tags) já devem existir. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Exemplo de solicitação {#example-request}
```bash
curl --location --request POST 'https://rest.iad-01.braze.com/content_blocks/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "name": "content_block",
  "description": "This is my Content Block",
  "content": "HTML content within block",
  "state": "draft",
  "tags": ["marketing"]
}'
```

## Resposta {#response}

```json
{
  "content_block_id": (string) Your newly generated block id,
  "liquid_tag": (string) The generated block tag from the Content Block name,
  "created_at": (string) The time the Content Block was created in ISO 8601,
  "message": "success"
}
```

## Solução de problemas {#troubleshooting}

A tabela a seguir lista os possíveis erros retornados e as etapas de solução de problemas associadas.

| Erro | Solução de problemas |
| --- | --- |
| `Content cannot be blank` | |
| `Content must be a string` | Certifique-se de que seu conteúdo esteja encapsulado entre aspas (`""`). |
| `Content must be smaller than 50kb` | O conteúdo do seu bloco de conteúdo deve ser menor que 50 KB no total. |
| `Content contains malformed liquid` | O Liquid fornecido não é válido ou não pode ser analisado. Tente novamente com Liquid válido ou entre em contato com o suporte. |
| `Content Block cannot be referenced within itself` | |
| `Content Block description cannot be blank` | |
| `Content Block description must be a string` | Certifique-se de que a descrição do bloco de conteúdo esteja encapsulada entre aspas (`""`). |
| `Content Block description must be shorter than 250 characters` | |
| `Content Block name cannot be blank` | |
| `Content Block name must be shorter than 100 characters` | |
| `Content Block name can only contain alphanumeric characters` | Os nomes dos blocos de conteúdo podem incluir qualquer um dos seguintes caracteres: as letras (maiúsculas ou minúsculas) `A` a `Z`, os números `0` a `9`, os traços `-` e os sublinhados `_`. Não pode conter caracteres não alfanuméricos, como emojis, `!`, `@`, `~`, `&` e outros caracteres "especiais". |
| `Content Block with this name already exists` | Tente um nome diferente. |
| `Content Block state must be either active or draft` | |
| `Tags must be an array` | As tags devem ser formatadas como uma matriz de strings, por exemplo, `["marketing", "promotional", "transactional"]`. | |
| `All tags must be strings` | Confira se as tags estão entre aspas (`""`). |
| `Some tags could not be found` | Para adicionar uma tag ao criar um bloco de conteúdo, a tag já deve existir na Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solução de problemas" }


{% endapi %}