---
nav_title: "GET: Exportar análise de dados resumidos do Canvas"
article_title: "GET: Exportar análise de dados resumidos do Canvas"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artigo descreve o endpoint da Braze para exportar análise de dados resumidos do Canvas."

---
{% API or interface de programação do aplicativo (API) %}
# Exportar análise de dados resumidos do Canvas {#export-canvas-data-summary-analytics}
{% apimethod get %}
/canvas/data_summary
{% endapimethod %}

> Use este endpoint para exportar consolidações de dados de séries temporais de um Canvas, fornecendo um resumo conciso dos resultados do Canvas.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1eb1b760-6b00-4c03-bcfb-12646f2ba6da {% endapiref %}

## Pré-requisitos {#prerequisites}

Para usar este endpoint, você precisará de uma [chave de API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics#rest-api-key-permissions) com a permissão `canvas.data_summary`.

## Limite de frequência {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parâmetros de solicitação {#request-parameters}

| Parâmetro | Obrigatório | Tipo de dados | Descrição |
| --------- | -------- | --------- | ----------- |
| `canvas_id` | Obrigatório | String | Consulte [Identificador de API or interface de programação do aplicativo (API) do Canvas]({{site.baseurl}}/api/identifier_types). |
| `ending_at` | Obrigatório | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | Data final para a exportação de dados. O padrão é o momento da solicitação. |
| `starting_at` | Opcional* | Datetime <br>([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) string) | Data de início para a exportação de dados. <br><br>* É necessário informar `length` ou `starting_at`. |
| `length` | Opcional* | String | Número máximo de dias antes de `ending_at` incluídos na série retornada. Deve estar entre 1 e 14 (inclusive). <br><br>* É necessário informar `length` ou `starting_at`. |
| `include_variant_breakdown` | Opcional | Booleano | Se deve incluir estatísticas de variantes (o padrão é `false`). |
| `include_step_breakdown` | Opcional | Booleano | Se deve incluir estatísticas de etapas (o padrão é `false`). |
| `include_deleted_step_data` | Opcional | Booleano | Se deve incluir estatísticas de etapas excluídas (o padrão é `false`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parâmetros de solicitação" }

{% alert important %}
A análise de dados do Canvas é agregada por dia no fuso horário configurado da sua empresa na Braze (o mesmo fuso horário usado pelo dashboard). A API or interface de programação do aplicativo (API) normaliza `starting_at` e `ending_at` para meia-noite nesse fuso horário. Certifique-se de que seus timestamps estejam alinhados com o fuso horário da sua empresa para que suas estatísticas correspondam ao dashboard. Por exemplo, se o fuso horário da sua empresa for UTC+2, o timestamp deve ser 0h UTC+2.
{% endalert %}

## Exemplo de solicitação {#example-request}

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-05:00&starting_at=2018-05-28T23:59:59-05:00&length=5&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Resposta {#response}

### Campos de evento de conversão {#conversion-event-fields}

A resposta inclui um par de campos de conversão para cada evento de conversão configurado no Canvas. O evento de conversão primária usa `conversions` e `conversions_by_entry_time`. Cada evento adicional usa o mesmo nome base com um sufixo numérico que começa em `1` para o segundo evento e aumenta em um para cada evento adicional.

| Ordem do evento de conversão no Canvas | Campo de conversões | Campo por horário de entrada |
| --- | --- | --- |
| Primário | `conversions` | `conversions_by_entry_time` |
| Segundo | `conversions1` | `conversions1_by_entry_time` |
| Terceiro | `conversions2` | `conversions2_by_entry_time` |
| Quarto | `conversions3` | `conversions3_by_entry_time` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Ordem de conversão" }

O quinto evento e os seguintes seguem o mesmo padrão (por exemplo, `conversions4` e `conversions4_by_entry_time`). Esses campos aparecem em `total_stats` e, quando você solicita detalhamentos, em `variant_stats` e `step_stats` usando os mesmos nomes.

{% alert note %}
Em `total_stats`, `variant_stats` e `step_stats`, `conversions` é a contagem do [evento de conversão primária]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) do Canvas. Quando você configura eventos de conversão adicionais, a carga útil também pode incluir `conversions1`, `conversions2` e campos com índices superiores para o segundo, terceiro e demais eventos. Isso é semelhante à [resposta multivariante]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics#multivariate-response) do endpoint `/campaigns/data_series`. Quando presentes, os campos que terminam em `_by_entry_time` atribuem essas conversões pelo horário de entrada no Canvas.
{% endalert %}

```json
{
  "data": {
    "name": (string) the Canvas name,
    "total_stats": {
      "revenue": (float) the number of dollars of revenue (USD),
      "entries": (int) the number of entries,
      "conversions": (int) the number of conversions for the primary conversion event,
      "conversions_by_entry_time": (int) the number of conversions for the primary conversion event by entry time,
      "conversions1": (optional, int) the number of conversions for the second conversion event,
      "conversions1_by_entry_time": (optional, int) the number of conversions for the second conversion event by entry time,
      "conversions2": (optional, int) the number of conversions for the third conversion event,
      "conversions2_by_entry_time": (optional, int) the number of conversions for the third conversion event by entry time,
      "conversions3": (optional, int) the number of conversions for the fourth conversion event,
      "conversions3_by_entry_time": (optional, int) the number of conversions for the fourth conversion event by entry time
    },
    "variant_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the variant {
        "name": (string) the name of the variant,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions for the primary conversion event,
        "conversions_by_entry_time": (optional, int) the number of conversions for the primary conversion event by entry time,
        "conversions1": (optional, int) the number of conversions for the second conversion event,
        "conversions1_by_entry_time": (optional, int) the number of conversions for the second conversion event by entry time,
        "conversions2": (optional, int) the number of conversions for the third conversion event,
        "conversions2_by_entry_time": (optional, int) the number of conversions for the third conversion event by entry time,
        "conversions3": (optional, int) the number of conversions for the fourth conversion event,
        "conversions3_by_entry_time": (optional, int) the number of conversions for the fourth conversion event by entry time,
        "entries": (int) the number of entries
      },
      ... (more variants)
    },
    "step_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (string) the API identifier for the step {
        "name": (string) the name of the step,
        "revenue": (float) the number of dollars of revenue (USD),
        "conversions": (int) the number of conversions for the primary conversion event,
        "conversions_by_entry_time": (int) the number of conversions for the primary conversion event by entry time,
        "conversions1": (optional, int) the number of conversions for the second conversion event,
        "conversions1_by_entry_time": (optional, int) the number of conversions for the second conversion event by entry time,
        "conversions2": (optional, int) the number of conversions for the third conversion event,
        "conversions2_by_entry_time": (optional, int) the number of conversions for the third conversion event by entry time,
        "conversions3": (optional, int) the number of conversions for the fourth conversion event,
        "conversions3_by_entry_time": (optional, int) the number of conversions for the fourth conversion event by entry time,
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
  "message": (string) returns 'success' when the request completes without errors
}
```

{% alert important %}
Na resposta da API or interface de programação do aplicativo (API), o campo `influenced_opens` representa o número total de aberturas (tanto Aberturas Diretas quanto Aberturas por Influência combinadas). No dashboard da Braze, "Aberturas por Influência" refere-se apenas a aberturas por influência, excluindo Aberturas Diretas. Isso se deve a uma convenção de nomenclatura legada na API or interface de programação do aplicativo (API).
{% endalert %}

## Artigos relacionados {#related-articles}

- [Solução de problemas de exportação]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)


{% endapi %}