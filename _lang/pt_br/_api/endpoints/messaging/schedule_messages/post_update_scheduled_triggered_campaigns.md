---
nav_title: "POST: Atualizar Campaigns agendadas disparadas por API or interface de programação do aplicativo (API)"
article_title: "POST: Atualizar Campaigns agendadas disparadas por API or interface de programação do aplicativo (API)"
search_tag: Endpoint
page_order: 4
layout: api_page
description: "Este artigo descreve os detalhes sobre o endpoint da Braze \"Atualizar Campaigns agendadas disparadas por API or interface de programação do aplicativo (API)\"."

---
{% API or interface de programação do aplicativo (API) %}
# Atualizar Campaigns agendadas disparadas por API or interface de programação do aplicativo (API) {#update-scheduled-api-triggered-campaigns}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/campaigns/trigger/agendar/cronograma/update
{% endapimethod %}

> Use esse endpoint para atualizar Campaigns agendadas disparadas por API or interface de programação do aplicativo (API) criadas no dashboard, permitindo que você decida qual ação deve disparar o envio da mensagem.

Você pode passar `trigger_properties` que a Braze usa como template na própria mensagem.

Observe que, para enviar mensagens com esse endpoint, você deve ter um ID de campanha, criado ao criar uma [campanha disparada por API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/api_campaigns).

Qualquer cronograma sobrescreve completamente o que você forneceu na solicitação de criação de cronograma ou nas solicitações de atualização de cronograma anteriores. Por exemplo, se você originalmente definiu o cronograma como `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` e depois o atualizou para `"schedule" : {"time" : "2015-02-20T14:14:47"}`, a Braze envia a mensagem no horário especificado em UTC, não no fuso local do usuário.

Os disparos agendados que são atualizados perto ou durante o horário em que deveriam ser enviados são atualizados com o melhor esforço para que a Braze possa aplicar mudanças de última hora a todos, alguns ou nenhum dos seus usuários-alvo. As atualizações não são aplicadas se o cronograma original usou fuso local e o horário original já passou em qualquer fuso horário.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d2a6e66-9d6f-4ae1-965a-79fa52b86b1d {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `campaigns.trigger.schedule.update`.

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "campaign_id": (required, string) see campaign identifier,
  "schedule_id": (required, string) the `schedule_id` to update (obtained from the response to create schedule),
  "schedule": {
    // required, see create schedule documentation
  }
}
```

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Obrigatório | String | Consulte [identificador de campanha]({{site.baseurl}}/api/identifier_types) |
| `schedule_id` | Obrigatório | String | O `schedule_id` a ser atualizado (obtido da resposta ao criar um cronograma). |
| `schedule` | Obrigatório | Objeto | Consulte [objeto de cronograma]({{site.baseurl}}/api/objects_filters/schedule_object). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Exemplo de solicitação {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/campaigns/trigger/schedule/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "campaign_id": "campaign_identifier",
  "schedule_id": "schedule_identifier",
  "schedule": {
    "time": "2017-05-24T21:30:00Z",
    "in_local_time": true
  }
}'
```

{% endapi %}