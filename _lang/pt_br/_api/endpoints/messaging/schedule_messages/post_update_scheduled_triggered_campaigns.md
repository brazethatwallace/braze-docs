---
nav_title: "POST: Atualizar Campaigns agendadas disparadas por API"
article_title: "POST: Atualizar Campaigns agendadas disparadas por API"
search_tag: Endpoint
page_order: 4
layout: api_page
description: "Este artigo descreve os detalhes sobre o endpoint da Braze \"Atualizar Campaigns agendadas disparadas por API\"."

---
{% api %}
# Atualizar Campaigns agendadas disparadas por API {#update-scheduled-api-triggered-campaigns}
{% apimethod post core_endpoint|/docs/core_endpoints %}
/campaigns/trigger/schedule/update
{% endapimethod %}

> Use esse endpoint para atualizar Campaigns agendadas disparadas por API criadas no dashboard, permitindo que você decida qual ação deve disparar o envio da mensagem.

Você pode passar `trigger_properties` que a Braze usa como template na própria mensagem.

Observe que, para enviar mensagens com esse endpoint, você deve ter um ID de campanha, criado ao criar uma [campanha disparada por API]({{site.baseurl}}/api/api_campaigns).

Qualquer programação sobrescreve completamente a que você forneceu na solicitação de criação de programação ou nas solicitações de atualização de programação anteriores. Por exemplo, se você originalmente definiu a programação como `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` e depois a atualizou para `"schedule" : {"time" : "2015-02-20T14:14:47"}`, a Braze envia a mensagem no horário especificado em UTC, não no horário local do usuário.

Os gatilhos programados que são atualizados perto ou durante o horário em que deveriam ser enviados são atualizados com o melhor esforço para que a Braze possa aplicar mudanças de última hora a todos, alguns ou nenhum dos seus usuários-alvo. As atualizações não são aplicadas se a programação original usou o horário local e o horário original já passou em qualquer fuso horário.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#6d2a6e66-9d6f-4ae1-965a-79fa52b86b1d {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key) com a permissão `campaigns.trigger.schedule.update`.

## Limite de taxa {#rate-limit}

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

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | ---------| --------- | ----------- |
| `campaign_id` | Obrigatória | String | Consulte [identificador de campanha]({{site.baseurl}}/api/identifier_types) |
| `schedule_id` | Obrigatória | String | O `schedule_id` a ser atualizado (obtido da resposta ao criar uma programação). |
| `schedule` | Obrigatória | Objeto | Consulte [objeto de programação]({{site.baseurl}}/api/objects_filters/schedule_object). |
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