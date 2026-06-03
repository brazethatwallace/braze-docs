---
nav_title: "PUT: Atualizar tradução em um Canvas"
article_title: "PUT: Atualizar tradução em um Canvas"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Atualizar tradução em um Canvas\"."
---

{% api %}
# Atualizar tradução em um Canvas {#update-translation-in-a-canvas}
{% apimethod put %}
/canvas/translations
{% endapimethod %}

> Use esse endpoint para atualizar várias traduções para um Canvas. Consulte [Locais em mensagens]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) para saber mais sobre os recursos de tradução.

Se você quiser atualizar as traduções depois que um Canvas for lançado, precisará [salvar sua mensagem como rascunho]({{site.baseurl}}/post-launch_edits/) primeiro.

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `canvas.translations.update`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parâmetros de caminho {#path-parameters}

Não há parâmetros de caminho para este endpoint.

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `workflow_id` | Obrigatória | String | O ID do Canvas. |
| `step_id` | Obrigatória | String | O ID da sua etapa do Canvas. |
| `message_variation_id` | Obrigatória | String | O ID da sua variação de mensagem. |
| `locale_id` | Obrigatória | String | O ID (UUID) do local. |
| `translation_map` | Obrigatória | Objeto | Objeto contendo as novas traduções. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

{% alert note %}
Todos os IDs de tradução são considerados identificadores únicos universais (UUIDs), que podem ser encontrados na resposta do endpoint GET.
{% endalert %}

## Exemplo de solicitação {#example-request}

```json
{
    "workflow_id": "a74404b3-3626-4de0-bdec-06935f3aa0ad",
    "step_id": "a74404b3-3626-4de0-bdec-06935f3aa0ac",
    "message_variation_id": "a74404b3-3626-4de0-bdec-06935f3aa0ac",
    "locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
    "translation_map": {
        "id_3": "Ein Absatz ohne Formatierung"
    }
}
```

## Resposta {#response}

Há quatro respostas de código de status para esse endpoint: `200`, `400`, `404` e `429`.

### Exemplo de resposta bem-sucedida {#example-success-response}

```json
{
	"message": "success"
}
```

### Exemplo de resposta de erro {#example-error-response}

O código de status `400` poderia retornar o seguinte corpo de resposta. Consulte [Solução de problemas](#troubleshooting) para obter mais informações sobre os erros que você pode encontrar.

```json
{
	"errors": [
		{
			"message": "The provided locale code does not exist."
		}
	]
}
```

{% endapi %}