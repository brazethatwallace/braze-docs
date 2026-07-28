---
nav_title: "GET: Ver valores de origem padrão para tags de tradução do Canvas"
article_title: "GET: Ver valores de origem padrão para tags de tradução do Canvas"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint de origem de tradução do Canvas."
---

{% api %}
# Ver valores de origem padrão para as tags de tradução de um Canvas {#view-default-source-values-for-a-canvass-translation-tags}
{% apimethod get %}
/canvas/translations/source
{% endapimethod %}

> Use este endpoint para ver todas as fontes de tradução padrão para as tags de tradução de um Canvas. Estes são os valores com o {% raw %}`{% translation id %} source {% endtranslation %}`{% endraw %}. Consulte [Locais em mensagens]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) para saber mais sobre os recursos de tradução.

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `canvas.translations.get`.

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parâmetros de consulta {#query-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|------------------------|----------|-----------|------------------------------------|
| `workflow_id` | Obrigatório | String | O ID do Canvas. |
| `step_id` | Obrigatório | String | O ID da sua etapa do Canvas. |
| `message_variation_id` | Obrigatório | String | O ID da sua variação de mensagem. |
| `locale_id` | Opcional | String | O ID (UUID) do local. |
| `post_launch_draft_version` | Opcional | Booleano | Quando `true`, retorna a versão de rascunho mais recente em vez da versão publicada mais recente. O padrão é `false`, retornando a versão publicada mais recente.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de consulta" }

{% alert note %}
Todos os IDs de tradução são considerados identificadores únicos universais (UUIDs), que podem ser encontrados na resposta do endpoint GET.
{% endalert %}

## Exemplo de solicitação {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/canvas/translations/source?workflow_id={workflow_id}&step_id={step_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta {#response}

Há quatro respostas de código de status para esse endpoint: `200`, `400`, `404` e `429`.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `200` poderia retornar o seguinte cabeçalho e corpo de resposta.

```json
{
   "translations": {
       "translation_map": {
           "id_0": "Here's a Million Dollars",
           "id_1": "Hello World!"
       }
   },
   "message": "success"
}
```

### Exemplo de resposta de erro {#example-error-response}

O código de status `400` poderia retornar o seguinte corpo de resposta. Consulte [Solução de problemas](#troubleshooting) para obter mais informações sobre os erros que você pode encontrar.

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