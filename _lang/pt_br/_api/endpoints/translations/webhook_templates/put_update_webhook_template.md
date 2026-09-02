---
nav_title: "PUT: Atualizar traduções para modelo de webhook"
article_title: "PUT: Atualizar traduções para modelo de webhook"
search_tag: Endpoint
page_order: 3

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint para atualizar traduções de um modelo de webhook."
---

{% api %}
# Atualizar traduções para um modelo de webhook {#update-translations-for-a-webhook-template}
{% apimethod put %}
/templates/webhook/translations
{% endapimethod %}

> Use este endpoint para atualizar traduções de um [modelo de webhook]({{site.baseurl}}/user_guide/messaging/templates/webhook_templates). Para saber mais sobre recursos de tradução, consulte [Mensagens multilíngues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages).

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `templates.translations.update`.

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='translation endpoints' %}

## Parâmetros de caminho {#path-parameters}

Não há parâmetros de caminho para este endpoint.

## Parâmetros de requisição {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| --- | --- | --- | --- |
| `template_id` | Obrigatório | String | O ID do seu modelo de webhook. |
| `locale_id` | Obrigatório | String | O UUID do local a ser atualizado. O local deve estar configurado para o modelo de webhook. |
| `translation_map` | Obrigatório | Objeto | Um objeto contendo as traduções atualizadas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Parâmetros de requisição" }

## Exemplo de requisição {#example-request}

```bash
curl --location --request PUT 'https://rest.iad-03.braze.com/templates/webhook/translations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "template_id": "e24404b3-3626-4de0-bdec-06935f3aa0ab",
  "locale_id": "a14404b3-3626-4de0-bdec-06935f3aa0ad",
  "translation_map": {
    "id_0": "¡Hola!",
    "id_1": "¿Te gustaría comprar esto?"
  }
}'
```

## Resposta {#response}

Existem cinco códigos de status de resposta para este endpoint: `200`, `400`, `403`, `404` e `429`.

### Exemplo de resposta bem-sucedida {#example-success-response}

O código de status `200` retorna o seguinte corpo de resposta vazio.

```json
{}
```

### Exemplo de resposta com erro {#example-error-response}

O código de status `400` pode retornar o seguinte corpo de resposta.

```json
{
  "message": "Locale not found"
}
```

{% endapi %}