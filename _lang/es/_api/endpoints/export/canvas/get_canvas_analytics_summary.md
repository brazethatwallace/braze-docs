---
nav_title: "GET: Exportar análisis de resumen de datos de Canvas"
article_title: "GET: Exportar análisis de resumen de datos de Canvas"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Este artículo describe el punto de conexión de Braze para exportar el resumen de análisis de los datos de Canvas."

---
{% api %}
# Exportar análisis de resumen de datos de Canvas {#export-canvas-data-summary-analytics}
{% apimethod get %}
/canvas/data_summary
{% endapimethod %}

> Utiliza este punto de conexión para exportar resúmenes de datos de series temporales para un Canvas, lo que proporciona un resumen conciso de los resultados del Canvas.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#1eb1b760-6b00-4c03-bcfb-12646f2ba6da {% endapiref %}

## Requisitos previos {#prerequisites}

Para utilizar este punto de conexión, necesitarás una [clave de API]({{site.baseurl}}/api/basics#rest-api-key) con el permiso `canvas.data_summary`.

## Límite de velocidad {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='default' %}

## Parámetros de la solicitud {#request-parameters}

| Parámetro | Obligatorio | Tipo de datos | Descripción |
| --------- | -------- | --------- | ----------- |
| `canvas_id` | Obligatorio | Cadena | Ver [identificador de API de Canvas]({{site.baseurl}}/api/identifier_types). |
| `ending_at` | Obligatorio | Fecha y hora <br>(cadena [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Fecha de finalización de la exportación de datos. Se predetermina a la hora de la solicitud. |
| `starting_at` | Opcional* | Fecha y hora <br>(cadena [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Fecha de inicio de la exportación de datos. <br><br>* Se requiere `length` o `starting_at`. |
| `length` | Opcional* | Cadena | Número máximo de días antes de `ending_at` incluidos en la serie devuelta. Debe estar comprendido entre 1 y 14 (ambos inclusive). <br><br>* Se requiere `length` o `starting_at`. |
| `include_variant_breakdown` | Opcional | Booleano | Si se deben incluir estadísticas de variantes (el valor predeterminado es `false`).  |
| `include_step_breakdown` | Opcional | Booleano | Si se deben incluir estadísticas de pasos (el valor predeterminado es `false`). |
| `include_deleted_step_data` | Opcional | Booleano | Si se deben incluir estadísticas de pasos para los pasos eliminados (el valor predeterminado es `false`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="Parámetros de la solicitud" }

{% alert important %}
Los análisis de Canvas se agregan por día en la zona horaria configurada por tu empresa en Braze (la misma zona horaria que utiliza el dashboard). La API normaliza `starting_at` y `ending_at` a medianoche en esa zona horaria.
{% endalert %}

## Ejemplo de solicitud {#example-request}

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_id}}&ending_at=2018-05-30T23:59:59-05:00&starting_at=2018-05-28T23:59:59-05:00&length=5&include_variant_breakdown=true&include_step_breakdown=true&include_deleted_step_data=true' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Respuesta {#response}

{% alert note %}
En `total_stats`, `variant_stats` y `step_stats`, `conversions` es el recuento del [evento de conversión primaria]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events) del Canvas. Cuando configuras eventos de conversión adicionales, la carga útil también puede incluir `conversions1`, `conversions2` y campos con índices superiores para el segundo, tercer y posteriores eventos. Esto es similar a la [respuesta multivariante]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics#multivariate-response) del punto de conexión `/campaigns/data_series`. Cuando están presentes, los campos que terminan en `_by_entry_time` atribuyen esas conversiones por el momento de entrada al Canvas.
{% endalert %}

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
En la respuesta de la API, el campo `influenced_opens` representa el número total de aperturas (tanto Direct Opens como Influenced Opens combinadas). En el panel de Braze, "Influenced Opens" se refiere únicamente a las aperturas influenciadas, excluyendo las aperturas directas. Esto se debe a una convención de nomenclatura heredada en la API.
{% endalert %}

## Artículos relacionados {#related-articles}

- [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting)


{% endapi %}