---
nav_title: "GET: Ver traduções de origem para modelo de e-mail"
article_title: "GET: Ver traduções de origem para modelo de e-mail"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint Ver traduções de origem para um modelo de e-mail."
---

{% API or interface de programação do aplicativo (API) %}
# Ver as traduções de origem para um modelo de e-mail {#view-the-source-translations-for-an-email-template}
{% apimethod get %}
/templates/email/translations/source
{% endapimethod %}

> Use este endpoint para ver as traduções de origem de um [modelo de e-mail]({{site.baseurl}}/user_guide/messaging/templates/email_templates). Consulte [Locais em mensagens]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) para saber mais sobre recursos de tradução.

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisará de uma [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `templates.email.info`.

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parâmetros de consulta {#query-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
|---------------|-------------|---------------|------------------------------------|
| `template_id` | Obrigatório | String | O ID do seu modelo de e-mail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de consulta" }

## Exemplo de solicitação {#example-request}

```
curl --location --request GET 'https://rest.iad-03.braze.com/templates/email/translations/source?template_id={template_id}'
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
--Request Body
---template_id: "6ad1507f-ca10-44c4-95bf-aj39fm10fm1ps"
```

## Resposta {#response}

Há quatro respostas de código de status para este endpoint: `200`, `400`, `404` e `429`.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `200` poderia retornar o seguinte cabeçalho e corpo de resposta.

```json
{
    "translations": {
        "translation_map": {
            "id_0": "Here's a limited time offer for your membership tier!",
            "id_1": "Welcome to a new fashion-forward season!"
        }
    },
    "message": "success"
}
```

### Exemplo de resposta de erro {#example-error-response}

O código de status `400` poderia retornar o seguinte corpo de resposta. Consulte [Solução de problemas](#troubleshooting) para saber mais sobre os erros que você pode encontrar.

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