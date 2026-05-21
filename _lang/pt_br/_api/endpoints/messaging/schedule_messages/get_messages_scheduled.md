---
nav_title: "GET: Listar próximas Campaigns e Canvas agendados"
article_title: "GET: Listar próximas Campaigns e Canvas agendados"
search_tag: Endpoint
page_order: 0
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze para listar próximas Campaigns e Canvas agendados."

---
{% api %}
# Listar próximas Campaigns e Canvas agendados {#list-upcoming-scheduled-campaigns-and-canvases}
{% apimethod get %}
/messages/scheduled_broadcasts
{% endapimethod %}

> Use este endpoint para retornar uma lista JSON de informações sobre Campaigns agendadas e Canvas de entrada entre agora e um `end_time` designado especificado na solicitação.

Mensagens diárias e recorrentes aparecerão apenas uma vez com sua próxima ocorrência. Os resultados retornados neste endpoint incluem Campaigns e Canvas criados e agendados no dashboard da Braze.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6f623cc3-383b-4bf7-b14d-7c56fc5562f5 {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `messages.schedule_broadcasts`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | -------- | --------- | ----------- |
| `end_time` | Obrigatória | String no formato [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) | Data final do intervalo para recuperar as próximas Campaigns e Canvas agendados. Isso é tratado como meia-noite no horário UTC pela API. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Exemplo de solicitação {#example-request}
```
curl --location --request GET 'https://rest.iad-01.braze.com/messages/scheduled_broadcasts?end_time=2018-09-01T00:00:00-04:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Resposta {#response}

```json
{
  "scheduled_broadcasts": [
    {
      "name": (string) the name of the scheduled broadcast,
      "id": (stings) the Canvas or campaign identifier,
      "type": (string) the broadcast type either Canvas or Campaign,
      "tags": (array) an array of tag names formatted as strings,
      "next_send_time": (string) The next send time formatted in ISO 8601, may also include time zone if not local/intelligent delivery,
      "schedule_type": (string) The schedule type, either local_time_zones, intelligent_delivery or the name of your company's time zone
    }
  ]
}
```

{% endapi %}