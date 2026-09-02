---
nav_title: "GET: Ver traduções de origem para modelo de webhook"
article_title: "GET: Ver traduções de origem para modelo de webhook"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint para visualizar traduções de origem de um modelo de webhook."
---

{% API or interface de programação do aplicativo (API) %}
# Ver traduções de origem para um modelo de webhook {#view-source-translations-for-a-webhook-template}
{% apimethod get %}
/templates/webhook/translations/source
{% endapimethod %}

> Use este endpoint para visualizar as traduções de origem padrão de um [modelo de webhook]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates). Para saber mais sobre os recursos de tradução, consulte [Mensagens em vários idiomas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisará de uma [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `templates.translations.get`.

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parâmetros de consulta {#query-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `template_id` | Obrigatório | String | O ID do seu modelo de webhook. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de consulta" }

## Exemplo de solicitação {#example-request}

```bash
curl --location --request GET 'https://rest.iad-03.braze.com/templates/webhook/translations/source?template_id={TEMPLATE_ID}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY'
```

Substitua *`TEMPLATE_ID`* pelo ID do seu modelo de webhook.

## Resposta {#response}

Existem cinco respostas de código de status para este endpoint: `200`, `400`, `403`, `404` e `429`.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `200` pode retornar o seguinte corpo de resposta.

```json
{
  "translations": {
    "translation_map": {
      "id_0": "Hello!",
      "id_1": "Would you like to buy this?"
    }
  }
}
```

### Exemplo de resposta com erro {#example-error-response}

O código de status `400` pode retornar o seguinte corpo de resposta.

```json
{
  "message": "This template does not have multi-language setup"
}
```

{% endapi %}