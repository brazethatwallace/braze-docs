---
nav_title: "GET: Consulta à lista de endereços de e-mail que cancelaram inscrição"
article_title: "GET: Consulta à lista de endereços de e-mail que cancelaram inscrição"
search_tag: Endpoint
page_order: 3
layout: api_page
page_type: reference
description: "Este artigo descreve os detalhes sobre o endpoint da Braze para recuperar a lista ou consultar cancelamentos de inscrição de e-mail."

---
{% API or interface de programação do aplicativo (API) %}
# Consulta à lista de endereços de e-mail que cancelaram inscrição {#query-list-of-unsubscribed-email-addresses}
{% apimethod get %}
/email/unsubscribes
{% endapimethod %}

> Use esse endpoint para retornar os e-mails mais recentes que cancelaram inscrição durante o período de `start_date` a `end_date`. Para obter um histórico completo do estado da inscrição, use o [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) para rastrear esses dados.

Você pode usar esse endpoint para configurar uma sincronização bidirecional entre a Braze e outros sistemas de e-mail ou seu próprio banco de dados.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d2966b81-188a-407b-ba7e-e6c252c44b4a {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `email.unsubscribe`.

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| ----------|-----------| ---------|------ |
| `start_date` | Opcional <br>(ver nota) | String no formato YYYY-MM-DD | Data de início do intervalo para recuperar cancelamentos de inscrição; deve ser anterior a end_date. A API or interface de programação do aplicativo (API) trata essa data como meia-noite no horário UTC. |
| `end_date` | Opcional <br>(ver nota) | String no formato YYYY-MM-DD | Data final do intervalo para recuperar cancelamentos de inscrição. A API or interface de programação do aplicativo (API) trata essa data como meia-noite no horário UTC. |
| `limit` | Opcional | Inteiro | Campo opcional para limitar o número de resultados retornados. O padrão é 100, o máximo é 500. |
| `offset` | Opcional | Inteiro | Ponto inicial opcional na lista a ser recuperado. |
| `sort_direction` | Opcional | String | Passe o valor `asc` para classificar os cancelamentos de inscrição do mais antigo para o mais recente. Passe `desc` para classificar do mais recente para o mais antigo. Se `sort_direction` não estiver incluído, a ordem padrão será do mais recente para o mais antigo. |
| `email` | Opcional <br>(ver nota) | String | Se fornecido, retornaremos se o usuário cancelou ou não a inscrição. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

{% alert note %}
Você precisa fornecer um `end_date`, bem como um `email` ou um `start_date`.
{% endalert %}

Se o seu intervalo de datas tiver mais do que `limit` cancelamentos de inscrição, será necessário fazer várias chamadas à API or interface de programação do aplicativo (API), aumentando o `offset` a cada vez até que uma chamada retorne menos do que `limit` ou zero resultados.

## Exemplo de solicitação {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/unsubscribes?start_date=2020-01-01&end_date=2020-02-01&limit=1&offset=1&sort_direction=desc&email=example@example.com' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE'
```

## Resposta {#response}

As entradas são listadas em ordem decrescente.

```json
{
  "emails": [
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    },
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    },
    {
      "email": (string) an email that has been unsubscribed,
      "unsubscribed_at": (string) the time the email was unsubscribed in ISO 8601
    }
  ],
  "message": "success"
}
```
{% endapi %}