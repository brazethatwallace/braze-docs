---
nav_title: "GET: Ver traduções para modelo de webhook"
article_title: "GET: Ver traduções para modelo de webhook"
search_tag: Endpoint
page_order: 2

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint para visualizar traduções de um modelo de webhook."
---

{% API or interface de programação do aplicativo (API) %}
# Ver traduções para um modelo de webhook {#view-translations-for-a-webhook-template}
{% apimethod get %}
/templates/webhook/translations
{% endapimethod %}

> Use este endpoint para ver traduções de um [modelo de webhook]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates). Você pode retornar todos os locais configurados ou filtrar a resposta por local. Para saber mais sobre os recursos de tradução, consulte [Mensagens multilíngues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisará de uma [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `templates.translations.get`.

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parâmetros de consulta {#query-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `template_id` | Obrigatório | String | O ID do seu modelo de webhook. |
| `locale_id` | Opcional | String | O UUID do local a ser retornado. Se omitido, a resposta inclui todos os locais configurados para o modelo de webhook. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de consulta" }

## Exemplo de solicitação {#example-request}

```bash
curl --location --request GET 'https://rest.iad-03.braze.com/templates/webhook/translations?template_id={TEMPLATE_ID}&locale_id={LOCALE_ID}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

Substitua *`TEMPLATE_ID`* pelo ID do seu modelo de webhook e *`LOCALE_ID`* pelo UUID do local que você deseja retornar. Omita `locale_id` para retornar todos os locais configurados.

## Resposta {#response}

Existem cinco códigos de status de resposta para este endpoint: `200`, `400`, `403`, `404` e `429`.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `200` pode retornar o seguinte corpo de resposta.

```json
{
  "translations": [
    {
      "translation_map": {
        "id_0": "¡Hola!",
        "id_1": "¿Te gustaría comprar esto?"
      },
      "locale": {
        "uuid": "c7c12345-de35-1234-5678-abcdefa99a3f",
        "name": "es-MX",
        "country": "MX",
        "language": "es",
        "locale_key": "es-mx"
      }
    },
    {
      "translation_map": {
        "id_0": "你好！",
        "id_1": "你想買這個嗎？"
      },
      "locale": {
        "uuid": "a1b12345-cd35-1234-5678-abcdefa99a3f",
        "name": "zh-HK",
        "country": "HK",
        "language": "zh",
        "locale_key": "zh-hk"
      }
    }
  ]
}
```

### Exemplo de resposta de erro {#example-error-response}

O código de status `400` pode retornar o seguinte corpo de resposta.

```json
{
  "message": "Invalid locale ID"
}
```

{% endapi %}