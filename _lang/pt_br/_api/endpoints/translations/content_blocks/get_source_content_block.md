---
nav_title: "GET: Ver valores de origem padrão para tags de tradução de bloco de conteúdo"
article_title: "GET: Ver valores de origem padrão para tags de tradução de bloco de conteúdo"
search_tag: Endpoint
page_order: 0

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint de origem de tradução de bloco de conteúdo."
---

{% api %}
# Ver valores de origem padrão para tags de tradução de um bloco de conteúdo {#view-default-source-values-for-a-content-blocks-translation-tags}
{% apimethod get %}
/content_blocks/translations/source
{% endapimethod %}

> Use este endpoint para ver todas as origens de tradução padrão para as tags de tradução de um bloco de conteúdo. Esses são os valores dentro de {% raw %}`{% translation id %} source {% endtranslation %}`{% endraw %}. Consulte [Locais em mensagens]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) para saber mais sobre os recursos de tradução.

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key) com a permissão `content_blocks.translations.get`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parâmetros de consulta {#query-parameters}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `content_block_id` | Obrigatória | String | O ID do seu bloco de conteúdo. |
| `locale_id` | Opcional | String | Um UUID de locale para filtrar as respostas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de consulta" }

{% alert note %}
Todos os IDs de tradução são considerados identificadores universais únicos (UUIDs), que podem ser encontrados na resposta do endpoint GET.
{% endalert %}

## Exemplo de solicitação {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/content_blocks/translations/source?content_block_id={content_block_id}&locale_id={locale_uuid}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta {#response}

Existem quatro códigos de status de resposta para este endpoint: `200`, `400`, `404` e `429`.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `200` pode retornar o seguinte cabeçalho e corpo de resposta.

```json
{
   "translations": {
       "translation_map": {
           "id_0": "Welcome!",
           "id_1": "Thank you for joining our program"
       }
   },
   "message": "success"
}
```

### Exemplo de resposta de erro {#example-error-response}

O código de status `400` pode retornar o seguinte corpo de resposta. Consulte [Solução de problemas](#troubleshooting) para saber mais sobre os erros que você pode encontrar.

```json
{
	"errors": [
		{
			"message": "This message does not support multi-language."
		}
	]
}
```

{% endapi %}