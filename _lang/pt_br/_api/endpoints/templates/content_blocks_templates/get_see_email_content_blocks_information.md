---
nav_title: "GET: Ver informações sobre Content Blocks"
article_title: "GET: Ver informações sobre Content Blocks"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze para ver informações sobre Content Blocks."
---

{% API or interface de programação do aplicativo (API) %}
# Ver informações do bloco de conteúdo {#see-content-block-information}
{% apimethod get %}
/content_blocks/info
{% endapimethod %}

> Use este endpoint para consultar informações dos seus [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks) existentes.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#589adda3-0def-4369-9ddc-eae71923c0ee {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisará de uma [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics) com a permissão `content_blocks.info`.

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---|---|---|---|
| `content_block_id` | Obrigatório | String | O identificador do bloco de conteúdo. <br><br>Você pode encontrá-lo listando as informações do bloco de conteúdo por meio de uma chamada de API or interface de programação do aplicativo (API) ou acessando a página [Chaves de API or interface de programação do aplicativo (API)]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers), rolando até a parte inferior e pesquisando o identificador de API or interface de programação do aplicativo (API) do seu bloco de conteúdo.|
| `include_inclusion_data` | Opcional | Booleano | Quando definido como `true`, a API or interface de programação do aplicativo (API) retorna o identificador de API or interface de programação do aplicativo (API) da variação de mensagem de Campaigns e Canvas em que esse bloco de conteúdo está incluído, para ser usado em chamadas subsequentes. Os resultados excluem Campaigns ou Canvas arquivados ou excluídos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Exemplo de solicitação {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/content_blocks/info?content_block_id={{content_block_id}}&include_inclusion_data=false' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Resposta {#response}

```json
{
  "content_block_id": (string) the Content Block identifier,
  "name": (string) the name of the Content Block,
  "content": (string) the content in the Content Block,
  "description": (string) the Content Block description,
  "content_type": (string) the content type, html or text,
  "tags": (array) An array of tags formatted as strings,
  "created_at": (string) The time the Content Block was created in ISO 8601,
  "last_edited": (string) The time the Content Block was last edited in ISO 8601,
  "inclusion_count" : (integer) the inclusion count,
  "inclusion_data": (array) the inclusion data,
  "message": "success"
}
```

## Solução de problemas {#troubleshooting}

A tabela a seguir lista os possíveis erros retornados e as etapas de solução de problemas associadas.

| Erro | Solução de problemas |
| --- | --- |
| `Content Block ID cannot be blank` | Verifique se um bloco de conteúdo está listado na sua solicitação e está entre aspas (`""`). |
| `Content Block ID is invalid for this workspace` | Esse bloco de conteúdo não existe ou está em uma conta de empresa ou espaço de trabalho diferente. |
| `Content Block has been deleted—content not available` | Esse bloco de conteúdo, embora possa ter existido anteriormente, foi excluído. |
| `Include Inclusion Data—error` | Esse parâmetro aceita apenas valores booleanos (true ou false). Verifique se o valor de `include_inclusion_data` não está entre aspas (`""`), o que faz com que o valor seja enviado como uma string. Consulte os [parâmetros de solicitação](#request-parameters) para mais detalhes. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solução de problemas" }


{% endapi %}