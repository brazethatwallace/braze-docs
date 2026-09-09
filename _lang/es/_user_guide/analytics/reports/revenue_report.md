---
nav_title: Informe de ingresos
article_title: Informe de ingresos
page_order: 7
page_type: reference
description: "Esta página describe dónde encontrar el informe de ingresos en el panel de Braze y cómo ver datos sobre ingresos en periodos de tiempo específicos, los ingresos de un producto específico y los ingresos totales de tu aplicación."
tool: Reports
---

# Informe de ingresos {#revenue-report}

> La página **Informe de ingresos** te permite ver datos sobre ingresos en periodos de tiempo específicos, los ingresos de un producto específico y los ingresos totales de tu aplicación.

Para ver tu informe de ingresos en el panel de Braze, ve a **Analytics** > **Reports** > **Revenue Report**.

## Personalización de tu informe de ingresos {#customizing-your-revenue-report}

Puedes personalizar tu informe de ingresos seleccionando un rango de fechas, las aplicaciones sobre las que informar y los parámetros.

![La página "Revenue Report" mostrando el gráfico "Performance Over Time" con "Revenue" configurado como parámetro.]({% image_buster /assets/img/revenue_report.png %})

### Filtrar por fecha y aplicaciones {#filtering-by-date-and-apps}

Selecciona el rango de fechas para tu informe de ingresos y, si lo deseas, una aplicación específica o una selección de aplicaciones.

### Filtrar por parámetros {#filtering-by-parameters}

El gráfico **Performance Over Time** muestra los datos de diferentes parámetros, que se pueden seleccionar en el menú desplegable **Statistics for**. Opcionalmente, puedes desglosar los datos de ciertos parámetros en el menú desplegable **Breakdown**.

Puedes ver los siguientes datos en el gráfico **Performance Over Time**:
- Fórmulas de indicadores clave de rendimiento
- Compras
    - (Opcional) Compras por producto
- Ingresos
    - (Opcional) Ingresos por Segment
    - (Opcional) Ingresos por producto
- Ingresos por hora
    - (Opcional) Ingresos por hora por Segment
- Ingresos por usuario

## Comprender los cálculos de ingresos {#understanding-revenue-calculations}

{% alert note %}
Cuando registras ingresos en una moneda sin tipo de cambio, Braze lo registra como una compra de 0,00 USD.
{% endalert %}

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table aria-label="Comprender los cálculos de ingresos">
  <caption>Comprender los cálculos de ingresos</caption>
    <thead>
        <tr>
            <th>Métrica</th>
            <th>Definición</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#lifetime-revenue">Lifetime Revenue</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#lifetime-value-per-user">Lifetime Value Per User</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#average-daily-revenue">Average Daily Revenue</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#daily-purchases">Daily Purchases</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/analytics/metrics_glossary#daily-revenue-per-user">Daily Revenue Per User</a></td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}</td>
        </tr>
    </tbody>
</table>

## Ver el desglose de productos {#viewing-the-product-breakdown}

Consulta la tabla **Desglose de productos** para ver una lista de los productos comprados durante el período seleccionado, cuántas unidades de cada producto se compraron y cuántos ingresos generó cada uno.

![La tabla "Desglose de productos" que muestra las columnas "Nombre del producto", "Comprados" e "Ingresos".]({% image_buster /assets/img/revenue_report_product_breakdown.png %})

## Exportar datos de ingresos {#exporting-revenue-data}

Para exportar tus datos de ingresos, selecciona <i class="fas fa-bars" title="Menú contextual del gráfico"></i> **Menú contextual del gráfico** en el gráfico **Rendimiento a lo largo del tiempo** y selecciona tu opción de exportación.

{% alert tip %}
¿Buscas más formas de obtener datos de ingresos? Prueba añadir el comportamiento de compra (así como la compra de un producto) a Campaigns o Canvas como [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events).
{% endalert %}

También puedes ver estadísticas de ingresos caso por caso en las páginas de [análisis de Campaign]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics) o [análisis de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics).

{% alert tip %}
Los informes de ingresos no se pueden exportar a través de la API. Para obtener ayuda con las exportaciones de CSV, consulta [solución de problemas de exportación]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting).
{% endalert %}