---
nav_title: "POST: Remover endereços de e-mail da lista de spam"
article_title: "POST: Remover endereços de e-mail da lista de spam"
search_tag: Endpoint
page_order: 7
layout: api_page
page_type: reference
description: "Este artigo traz informações sobre o endpoint da Braze \"Remover endereços de e-mail da lista de spam\"."

---
{% api %}
# Remover endereços de e-mail da lista de spam {#remove-email-addresses-from-spam-list}
{% apimethod post %}
/email/spam/remove
{% endapimethod %}

> Use esse endpoint para remover endereços de e-mail da sua lista de spam da Braze e da lista de spam mantida pelo seu provedor de e-mail.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1614a82f-510a-4c37-95a6-8207a125e487 {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `email.spam.remove`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação {#request-body}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": "example@braze.com"
}
```

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| ----------|-----------| --------|------- |
| `email` | Obrigatório | String ou matriz | Endereço de e-mail em string para modificar ou uma matriz de até 50 endereços de e-mail para modificar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Exemplo de solicitação {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/email/spam/remove' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email": "example@braze.com"
}'
```
{% endapi %}