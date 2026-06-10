---
nav_title: "PUT: Atualizar traduções para um modelo de e-mail"
article_title: "PUT: Atualizar traduções para um modelo de e-mail"
search_tag: Endpoint
page_order: 4

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Atualizar traduções para um modelo de e-mail."
---

{% api %}
# Atualizar traduções para um modelo de e-mail {#update-translations-for-an-email-template}
{% apimethod put %}
/templates/email/translations/
{% endapimethod %}

> Use este endpoint para atualizar traduções para um [modelo de e-mail]({{site.baseurl}}/user_guide/messaging/templates/email_templates/). Consulte [Locais em mensagens]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages/) para saber mais sobre os recursos de tradução.

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `templates.translations.update`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parâmetros de caminho {#path-parameters}

Não há parâmetros de caminho para este endpoint.

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `template_id` | Obrigatória | String | O ID do seu modelo de e-mail. |
| `locale_id` | Obrigatória | String | O ID da localização. |
| `translations_map` | Obrigatória | String | O mapa das traduções para o seu modelo de e-mail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

{% alert note %}
Todos os IDs de tradução são considerados identificadores únicos universais (UUIDs), que podem ser encontrados na resposta do endpoint GET.
{% endalert %}

## Exemplo de solicitação {#example-request}

```json
{
    "template_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
    "locale_id": "h94404b3-3626-4de0-bdec-06935f3aa0ad",
    "translation_map": {
        "id_0": "¡Hola!",
        "id_1": "Me llamo Jacky",
        "id_2": "¿Dónde está la biblioteca?"
    }
}
```

## Resposta {#response}

Há quatro respostas de código de status para este endpoint: `200`, `400`, `404` e `429`.

### Exemplo de resposta bem-sucedida {#example-success-response}

```json
{
    "message": "success"
}
```

### Exemplo de resposta de erro {#example-error-response}

O código de status `400` pode retornar o seguinte corpo de resposta. Consulte [Solução de problemas](#troubleshooting) para mais informações sobre os erros que você pode encontrar.

```json
{
	"errors": [
		{
			"id": "1234567-abc-123-012345678",
			"message": "The provided translations yielded errors when parsing. Please contact Braze for more information."
		}
	]
}
```

{% endapi %}