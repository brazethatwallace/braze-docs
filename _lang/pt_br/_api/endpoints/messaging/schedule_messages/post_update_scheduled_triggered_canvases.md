---
nav_title: "POST: Atualizar Canvas programados disparados pela API"
article_title: "POST: Atualizar Canvas programados disparados pela API"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint da Braze \"Atualizar Canvas programados disparados pela API\"."

---
{% api %}
# Atualizar Canvas programados disparados pela API {#update-scheduled-api-triggered-canvases}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/canvas/trigger/schedule/update
{% endapimethod %}

> Use esse endpoint para atualizar Canvas programados disparados pela API que foram criados no dashboard.

Isso permite que você decida qual ação aciona o envio da mensagem. Você pode passar `trigger_properties` que a Braze insere como template na própria mensagem.

Note que, para enviar mensagens com esse endpoint, você deve ter um ID de Canvas, criado quando você constrói um [Canvas]({{site.baseurl}}/api/identifier_types/#canvas-api-identifier).

Qualquer agendamento substituirá completamente o que você forneceu na solicitação de criação de agendamento ou em solicitações anteriores de atualização de agendamento.
  - Por exemplo, se você originalmente fornecer `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` e então na sua atualização fornecer `"schedule" : {"time" : "2015-02-20T14:14:47"}`, a Braze envia sua mensagem no horário fornecido em UTC, não no horário local do usuário.
  - Os gatilhos agendados que você atualiza perto ou durante o horário em que deveriam ser enviados são atualizados com o melhor esforço, então a Braze pode aplicar mudanças de última hora a todos, alguns ou nenhum dos seus usuários-alvo.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8fdf158b-ce20-41d8-80e4-a9300a6706d4 {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `canvas.trigger.schedule.update`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "canvas_id": (required, string) see Canvas identifier,
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `canvas_id` | Obrigatório | String | Consulte [identificador de Canvas]({{site.baseurl}}/api/identifier_types/). |
| `schedule_id` | Opcional | String | O `schedule_id` a ser atualizado (obtido da resposta para criar agendamento). |
| `schedule` | Obrigatório | Objeto | Consulte [objeto de agendamento]({{site.baseurl}}/api/objects_filters/schedule_object/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Exemplo de solicitação {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/canvas/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "canvas_id": "canvas_identifier",
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T21:30:00Z",
    "in_local_time": true
  }
}'
```

{% endapi %}