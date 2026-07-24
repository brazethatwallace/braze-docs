---
nav_title: "POST: Excluir Canvas programados disparados pela API"
article_title: "POST: Excluir Canvas programados disparados pela API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze para excluir Canvas programados disparados pela API."

---
{% api %}
# Excluir Canvas programados disparados pela API {#delete-scheduled-api-triggered-canvases}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/canvas/trigger/schedule/delete
{% endapimethod %}

> O endpoint de exclusão de agendamento permite cancelar uma mensagem que você agendou anteriormente por meio de Canvas disparados pela API antes que ela seja enviada.

As mensagens programadas ou os disparos que são excluídos perto ou durante o horário em que deveriam ser enviados são atualizados com base no melhor esforço, de modo que a Braze pode aplicar exclusões de último segundo a todos, alguns ou nenhum dos seus usuários direcionados.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#7d34037f-4bf2-4fab-bc9c-c972988051a7 {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `canvas.trigger.schedule.delete`.

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) the Canvas identifier,
  "schedule_id": (required, string) the `schedule_id` to delete (obtained from the response to create schedule)
}
```

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `canvas_id` | Obrigatório | String | Consulte [Identificador do Canvas]({{site.baseurl}}/api/identifier_types). |
| `schedule_id` | Obrigatório | String | O `schedule_id` a ser excluído (obtido da resposta à programação de criação). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }


## Exemplo de solicitação {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/delete' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "schedule_id": "schedule_identifier"
}'
```

{% endapi %}