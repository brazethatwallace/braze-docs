---
nav_title: "GET: Exportar análise de dados resumidos do Canvas"
article_title: "GET: Exportar análise de dados resumidos do Canvas"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve o endpoint da Braze para exportar análise de dados resumidos do Canvas."

---
{% api %}
# Exportar análise de dados resumidos do Canvas {#export-canvas-data-summary-analytics}
{% apimethod get %}
/canvas/data_summary
{% endapimethod %}

> Use este endpoint para exportar consolidações de dados de séries temporais de um Canvas, fornecendo um resumo conciso dos resultados do Canvas.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1eb1b760-6b00-4c03-bcfb-12646f2ba6da {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `canvas.data_summary`.

## Limite de taxa {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | -------- | --------- | ----------- |
| `canvas_id` | Obrigatória | String | Consulte [Identificador de API do Canvas]({{site.baseurl}}/api/identifier_types/). |
| `ending_at` | Obrigatória | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | Data final para a exportação de dados. O padrão é o momento da solicitação. |
| `starting_at` | Opcional* | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | Data de início para a exportação de dados. <br><br>* É necessário informar `length` ou `starting_at`. |
| `length` | Opcional* | String | Número máximo de dias antes de `ending_at` incluídos na série retornada. Deve estar entre 1 e 14 (inclusive). <br><br>* É necessário informar `length` ou `starting_at`. |
| `include_variant_breakdown` | Opcional | booleano | Se deve incluir estatísticas de variantes (o padrão é `false`).  |
| `include_step_breakdown` | Opcional | booleano | Se deve incluir estatísticas de etapas (o padrão é `false`). |
| `include_deleted_step_data` | Opcional | booleano | Se deve incluir estatísticas de etapas excluídas (o padrão é `false`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Request parameters" }

{% alert important %}
**Alinhamento de fuso horário:** A análise de dados do dashboard da Braze é agregada diariamente no fuso horário configurado da sua empresa no dashboard. Certifique-se de que seus timestamps estejam alinhados com o fuso horário da sua empresa para que suas estatísticas correspondam ao dashboard. Por exemplo, se o horário da sua empresa é UTC+2, o timestamp deve ser 00h00 UTC+2.
{% endalert %}

## Exemplo de solicitação {#example-request}
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-05:00&starting_at=2018-05-28T23:59:59-05:00&length=5&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Resposta {#response}

```json
{
  "data": {
    "name": (string) the Canvas name,
    "total_stats": {
      "revenue": (float) the number of dollars of revenue (USD),
      "conversions": (int) the number of conversions,
      "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
      "entries": (int) the number of entries
    },
    "variant_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the variant {
        "name": (string) the name of the variant,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions,
        "entries": (int) the number of entries
      },
      ... (more variants)
    },
    "step_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the step {
        "name": (string) the name of the step,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions,
        "conversions_by_entry_time": (int) the number of conversions for the conversion event by entry time,
        "messages": {
          "android_push": (name of channel) [
            {
              "sent": (int) the number of sends,
              "opens": (int) the number of opens,
              "influenced_opens": (int) the total number of opens (includes both direct opens and influenced opens),
              "bounces": (int) the number of bounces
              ... (more stats for channel)
            }
          ],
          ... (more channels)
        }
      },
      ... (more steps)
    }
  },
  "message": (required, string) the status of the export, returns 'success' on successful completion
}
```

{% alert important %}
**Campo `influenced_opens`:** Na resposta da API, o campo `influenced_opens` representa o número total de aberturas (tanto aberturas diretas quanto aberturas por influência combinadas). No dashboard da Braze, "aberturas por influência" refere-se apenas a aberturas por influência, excluindo aberturas diretas. Isso se deve a uma convenção de nomenclatura legada na API.
{% endalert %}

{% alert tip %}
Para obter ajuda com exportações de CSV e API, acesse [Solução de problemas de exportação]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting/).
{% endalert %}

{% endapi %}