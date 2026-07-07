---
nav_title: "PUT: Atualizar tradução em um bloco de conteúdo"
article_title: "PUT: Atualizar tradução em um bloco de conteúdo"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Atualizar tradução em um bloco de conteúdo."
---

{% api %}
# Atualizar tradução em um bloco de conteúdo {#update-translation-in-a-content-block}
{% apimethod put %}
/content_blocks/translations
{% endapimethod %}

> Use este endpoint para atualizar várias traduções para um [bloco de conteúdo]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks). Consulte [Locais em mensagens]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) para saber mais sobre os recursos de tradução.

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key) com a permissão `content_blocks.translations.update`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parâmetros de jornada {#path-parameters}

Não há parâmetros de jornada para este endpoint.

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `content_block_id` | Obrigatória | String | O ID do seu bloco de conteúdo. |
| `locale_id` | Obrigatória | String | O ID (UUID) da localidade. |
| `translation_map` | Obrigatória | Objeto | Objeto contendo as novas traduções. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

{% alert note %}
Todos os IDs de tradução são considerados identificadores únicos universais (UUIDs), que podem ser encontrados na resposta do endpoint GET.
{% endalert %}

## Exemplo de solicitação {#example-request}

```json
{
    "content_block_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
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