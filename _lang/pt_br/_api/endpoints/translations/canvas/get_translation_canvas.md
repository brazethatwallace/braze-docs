---
nav_title: "GET: Ver tradução para um Canvas"
article_title: "GET: Ver tradução para um Canvas"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Ver tradução para um Canvas\"."
---

{% API or interface de programação do aplicativo (API) %}
# Ver tradução para um Canvas {#view-translation-for-a-canvas}
{% apimethod get %}
/canvas/translations
{% endapimethod %}

> Use este endpoint para pré-visualizar uma mensagem traduzida para um Canvas. Consulte [Locais em mensagens]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) para saber mais sobre os recursos de tradução.

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `canvas.translations.get`.

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parâmetros de consulta {#query-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|------------------------|----------|-----------|------------------------------------|
| `workflow_id` | Obrigatório | String | O ID do Canvas. |
| `step_id` | Obrigatório | String | O ID da sua etapa do Canvas. |
| `message_variation_id` | Obrigatório | String | O ID da sua variação de mensagem. |
| `locale_id` | Opcional | String | O ID (UUID) da localização. |
| `post_launch_draft_version` | Opcional | Booleano | Quando `true`, retorna a versão mais recente do rascunho em vez da versão publicada mais recente. O padrão é `false`, retornando a versão publicada mais recente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de consulta" }

{% alert note %}
Todos os IDs de tradução são considerados identificadores únicos universais (UUIDs), que podem ser encontrados na resposta do endpoint GET.
{% endalert %}

## Exemplo de solicitação {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/canvas/translations/?workflow_id={workflow_id}&step_id={step_id}&message_variation_id={message_variation_id}&locale_id={locale_uuid}&post_launch_draft_version=true' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta {#response}

Há quatro respostas de código de status para esse endpoint: `200`, `400`, `404` e `429`.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `200` poderia retornar o seguinte cabeçalho e corpo de resposta.

```json
{
    "translations": [
        {
            "translation_map": {
                "id_0": "¡Hola!",
                "id_1": "Me llamo Jacky",
                "id_2": "¿Dónde está la biblioteca?"
            },
            "locale": {
                "uuid": "c7c12345-te35-1234-5678-abcdefa99r3f",
                "name": "es-MX",
                "country": "MX",
                "language": "es",
                "locale_key": "es-mx"
            }
        }
    ]
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