---
nav_title: "GET: Exportar análise de dados da campanha"
article_title: "GET: Exportar análise de dados da campanha"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve informações sobre o endpoint da Braze para exportar análise de dados da campanha."

---
{% api %}
# Exportar análise de dados da campanha {#export-campaign-analytics}
{% apimethod get %}
/campaigns/data_series
{% endapimethod %}

> Use este endpoint para recuperar uma série diária de diversas estatísticas de uma campanha ao longo do tempo.

Os dados retornados incluem quantas mensagens foram enviadas, abertas, clicadas ou convertidas por canal de envio de mensagens.

{% multi_lang_include api/export_data_series_analytics_dashboard_note.md type='campaign' %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#c07b5ebd-0246-471e-b154-416d63ae28a1 {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key) com a permissão `campaigns.data_series`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='export campaign analytics' %}

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | -------- | --------- | ----------- |
| `campaign_id` | Obrigatória | String | Consulte o [identificador de API da campanha]({{site.baseurl}}/api/identifier_types).<br><br> O `campaign_id` para Campaigns da API pode ser encontrado na página [Chaves de API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers) e na página **Campaign Details** no seu dashboard, ou você pode usar o [endpoint Listar Campaigns]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns). |
| `length` | Obrigatória | Inteiro | Número máximo de dias antes de `ending_at` para incluir na série retornada. Deve estar entre 1 e 100 (inclusive). |
| `ending_at` | Opcional | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | Data em que a série de dados deve terminar. O padrão é o horário da solicitação. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

## Exemplo de solicitação {#example-request}

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/campaigns/data_series?campaign_id={{campaign_identifier}}&length=7&ending_at=2020-06-28T23:59:59-5:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Respostas {#responses}

### Resposta multicanal {#multichannel-response}

```json
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time": (string) the date as ISO 8601 date,
            "conversions_by_send_time": (optional, int),
            "conversions1_by_send_time": (optional, int),
            "conversions2_by_send_time": (optional, int),
            "conversions3_by_send_time": (optional, int),
            "conversions": (optional, int),
            "conversions1": (optional, int),
            "conversions2": (optional, int),
            "conversions3": (optional, int),
            "unique_recipients": (int),
            "revenue": (optional, float)
            "messages" : {
                "ios_push" : [
                    {
                      "variation_api_id": (string) the variation API identifier,
                      "sent" : (int) the number of sends,
                      "direct_opens" : (int) the number of direct opens,
                      "total_opens" : (int)the number of total opens,
                      "bounces" : (int) the number of bounces,
                      "body_clicks" : (int) the number of body clicks
                    }
                ],
                "android_push" : [
                    {
                      "variation_api_id": (string) the variation API identifier,
                      "sent" : (int) the number of sends,
                      "direct_opens" : (int) the number of direct opens,
                      "total_opens" : (int)the number of total opens,
                      "bounces" : (int) the number of bounces,
                      "body_clicks" : (int) the number of body clicks
                    }
                ],
                "webhook": [
                    {
                      "variation_api_id": (string) the variation API identifier,
                      "sent": (int) the number of sends,
                      "errors": (int) the number of errors
                    }
                ],
                "email" : [
                    {
                      "variation_api_id": (string) the variation API identifier,
                      "sent": (int) the number of sends,
                      "opens": (int) the number of opens,
                      "unique_opens": (int) the number of unique opens,
                      "clicks": (int) the number of clicks,
                      "unique_clicks": (int) the number of unique clicks,
                      "unsubscribes": (int) the number of unsubscribes,
                      "bounces": (int) the number of bounces,
                      "delivered": (int) the number of messages delivered,
                      "reported_spam": (int) the number of messages reported as spam
                    }
                ],
                "sms" : [
                    {
                      "variation_api_id": (string) the variation API identifier,
                      "sent": (int) the number of sends,
                      "sent_to_carrier" : (int) the number of messages sent to the carrier,
                      "delivered": (int) the number of delivered messages,
                      "rejected": (int) the number of rejected messages,
                      "delivery_failed": (int) the number of failed deliveries,
                      "clicks": (int) the number of clicks on shortened links,
                      "opt_out" : (int) the number of opt outs,
                      "help" : (int) the number of help messages received
                  }
                ],
                "whats_app": [
                    {
                      "variation_api_id": (string) the variation API identifier,
                      "sent": (int) the number of sends,
                      "delivered": (int) the number of delivered messages,
                      "failed": (int) the number of failed deliveries,
                      "read": (int) the number of opened messages
                    },
                ],
                "content_cards" : [
                  {
                    "variation_api_id": (string) the variation API identifier,
                    "sent": (int) the number of sends,
                    "total_clicks": (int) the number of total clicks,
                    "total_dismissals": (int) the number of total dismissals,
                    "total_impressions": (int) the number of total impressions,
                    "unique_clicks": (int) the number of unique clicks,
                    "unique_dismissals": (int) the number of unique dismissals,
                    "unique_impressions": (int) the number of unique impressions
                  }
                ],
                ...
            }
        }
    ],
}
```

### Resposta multivariante {#multivariate-response}

```json
{
    "data" : [
        {
            "time" : (string) the date as ISO 8601 date,
            "conversions" : (int) the number of conversions,
            "revenue": (float) the number of dollars of revenue (USD),
            "conversions_by_send_time": (int) the number of conversions attributed to the date the campaign was sent,
            "messages" : {
               "trigger_in_app_message": [{
                    "variation_name": (optional, string) the variation name,
                    "impressions": (int) the number of impressions,
                    "clicks": (int) the number of clicks,
                    "first_button_clicks": (int) the number of first button clicks,
                    "second_button_clicks": (int) the number of second button clicks,
                    "revenue": (float) the number of dollars of revenue (USD),
                    "unique_recipients": (int) the number of unique recipients,
                    "conversions": (int) the number of conversions,
                    "conversions_by_send_time": (int) the number of conversions attributed to the date the campaign was sent,
                    "conversions1": (optional, int) the number of conversions for the second conversion event,
                    "conversions1_by_send_time": (optional, int) the number of conversions for the second conversion event attributed to the date the campaign was sent,
                    "conversions2": (optional, int) the number of conversions for the third conversion event,
                    "conversions2_by_send_time": (optional, int) the number of conversions for the third conversion event attributed to the date the campaign was sent,
                    "conversions3": (optional, int) the number of conversions for the fourth conversion event,
                    "conversions3_by_send_time": (optional, int) the number of conversions for the fourth conversion event attributed to the date the campaign was sent
      			}, {
      				"variation_name": (optional, string) the variation name,
      				"impressions": (int) the number of impressions,
      				"clicks": (int) the number of clicks,
      				"first_button_clicks": (int) the number of first button clicks,
      				"second_button_clicks": (int) the number of second button clicks,
                    "revenue": (float) the number of dollars of revenue (USD),
                    "unique_recipients": (int) the number of unique recipients,
                    "conversions": (int) the number of conversions,
                    "conversions_by_send_time": (int) the number of conversions attributed to the date the campaign was sent,
                    "conversions1": (optional, int) the number of conversions for the second conversion event,
                    "conversions1_by_send_time": (optional, int) the number of conversions for the second conversion event attributed to the date the campaign was sent,
                    "conversions2": (optional, int) the number of conversions for the third conversion event,
                    "conversions2_by_send_time": (optional, int) the number of conversions for the third conversion event attributed to the date the campaign was sent,
                    "conversions3": (optional, int) the number of conversions for the fourth conversion event,
                    "conversions3_by_send_time": (optional, int) the number of conversions for the fourth conversion event attributed to the date the campaign was sent
      			}, {
      				"variation_name": (optional, string) the variation name,
      				"revenue": (float) the number of dollars of revenue (USD),
      				"unique_recipients": (int) the number of unique recipients,
      				"conversions": (int) the number of conversions,
                    "conversions_by_send_time": (int) the number of conversions attributed to the date the campaign was sent,
                    "conversions1": (optional, int) the number of conversions for the second conversion event,
                    "conversions1_by_send_time": (optional, int) the number of conversions for the second conversion event attributed to the date the campaign was sent,
                    "conversions2": (optional, int) the number of conversions for the third conversion event,
                    "conversions2_by_send_time": (optional, int) the number of conversions for the third conversion event attributed to the date the campaign was sent,
                    "conversions3": (optional, int) the number of conversions for the fourth conversion event,
                    "conversions3_by_send_time": (optional, int) the number of conversions for the fourth conversion event attributed to the date the campaign was sent
      				"enrolled": (optional, int) the number of enrolled users
      			}]
      		},
      		"conversions_by_send_time": (optional, int),
      		"conversions1_by_send_time": (optional, int),
      		"conversions2_by_send_time": (optional, int),
      		"conversions3_by_send_time": (optional, int),
      		"conversions": (optional, int),
      		"conversions1": (optional, int),
      		"conversions2": (optional, int),
      		"conversions3": (optional, int),
      		"unique_recipients": (int),
      		"revenue": (optional, float)
         }],
         ...
}
```

Os tipos de mensagens possíveis são: `email`, `trigger_in_app_message`, `webhook`, `android_push`, `ios_push`, `kindle_push` e `web_push`. Todos os tipos de mensagens push terão as mesmas estatísticas mostradas em `android_push`.

{% alert tip %}
Para obter ajuda com exportações de CSV e API, acesse [Resolução de problemas de exportação]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}

{% endapi %}

## Solução de problemas {#troubleshooting}

### Visualizar falhas de entrega para Campaigns disparadas por API {#viewing-delivery-failures-for-api-triggered-campaigns}

O endpoint [`/campaigns/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics) retorna estatísticas diárias agregadas (por exemplo, `delivery_failed` para SMS ou `errors` para webhooks). Ele não retorna motivos de falha por destinatário.

Para falhas de envio, bounces e cancelamentos por mensagem de Campaigns disparadas por API ou Campaigns da API, use o [Registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) no dashboard. Para relatórios personalizados sobre eventos de envio e entrega, use o [Criador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder) com [modelos de consulta]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates) ou SQL personalizado. Você também pode transmitir eventos de falha por meio de Currents ou Compartilhamento de dados do Snowflake se o seu espaço de trabalho tiver esses produtos ativados.