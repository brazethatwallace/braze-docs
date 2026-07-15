---
nav_title: Seguimiento analítico por segmentos
article_title: Seguimiento analítico por segmentos
page_order: 3
page_type: reference
description: "Este artículo de referencia cubre el seguimiento analítico de segmentos y cómo ver los ingresos y las compras a lo largo del tiempo, las sesiones a lo largo del tiempo y los eventos personalizados a lo largo del tiempo."
tool:
  - Segments
  - Reports
---

# Seguimiento analítico por segmentos {#segment-analytics-tracking}

> Cuando el seguimiento analítico está activado para un segmento, puedes ver las sesiones, los eventos personalizados y los ingresos a lo largo del tiempo para ese segmento.

Si no activas el seguimiento analítico para un segmento, podrás acceder a [las estadísticas en tiempo real]({{site.baseurl}}/user_guide/audience/segments/segment_data#segment-statistics) de ese segmento y dirigirte a sus usuarios con Campaigns. La única diferencia es si puedes acceder a las herramientas de análisis específicas mencionadas en esta página.

## Activar el seguimiento analítico por segmentos {#turning-on-segment-analytics}

En la sección **Segment Details** de la página de un segmento, activa **Analytics Tracking**.

![Activación del seguimiento analítico de un segmento]({% image_buster /assets/img_archive/A_Tracking_2.png %})

Una aplicación puede tener activado el seguimiento de hasta 25 segmentos. Braze recomienda realizar un seguimiento de los segmentos que te resulten importantes para analizar los efectos de tus Campaigns sobre las sesiones, los ingresos y las compras.

{% alert note %}
Después de habilitar el seguimiento analítico, puede haber un retraso hasta que se completen los datos del segmento. Si los datos no se completan en un plazo de 24 horas, [ponte en contacto con Soporte]({{site.baseurl}}/braze_support).
{% endalert %}

## Ver los ingresos y las compras a lo largo del tiempo {#viewing-revenue-and-purchases-over-time}

Ve a **Analytics** > **Revenue Report** para ver los datos sobre [ingresos y compras a lo largo del tiempo para este segmento]({{site.baseurl}}/user_guide/analytics/reports/revenue_report).

Los gráficos de ingresos y compras reflejan la actividad registrada después de que se active el seguimiento analítico para ese segmento. Activar el seguimiento no rellena retroactivamente las compras anteriores en esos informes. Cuando compares segmentos, utiliza solo intervalos de tiempo en los que el seguimiento estuviera habilitado para cada segmento que selecciones.

![Datos de ingresos por segmento]({% image_buster /assets/img_archive/Revenue.png %})

Para comparar visualmente los datos de los segmentos en cualquier intervalo de tiempo personalizado, añade o elimina segmentos del gráfico. Selecciona **By Segment** en el desplegable **Breakdown** y, a continuación, selecciona tus segmentos en **Breakdown values**.

Selecciona cualquier nombre de segmento en la leyenda del gráfico para activar o desactivar la visibilidad de las métricas de ese segmento.

![Ingresos por múltiples segmentos]({% image_buster /assets/img_archive/segment_revenue_multiple.png %})

## Sesiones a lo largo del tiempo {#sessions-over-time}

Del mismo modo, puedes encontrar datos sobre [las sesiones a lo largo del tiempo para este segmento en particular]({{site.baseurl}}/user_guide/analytics/dashboards/home#exporting-app-usage-data) en la página **Home**.

![Datos de sesiones por segmento]({% image_buster /assets/img_archive/events_over_time2.png %})

## Ver eventos personalizados a lo largo del tiempo {#view-custom-events-over-time}

Para ver los datos de [los eventos personalizados a lo largo del tiempo para los segmentos]({{site.baseurl}}/user_guide/data/activation/events/custom_events#analytics), ve a **Analytics** > **Custom Events Report**.

## Uso de las plantillas del generador de consultas {#using-query-builder-templates}

Cuando el seguimiento analítico está activado, puedes utilizar las plantillas de informes del generador de consultas para desglosar las métricas de rendimiento de Campaigns, Canvas, variantes y pasos por segmentos. Para saber más, consulta [Datos de segmentos]({{site.baseurl}}/user_guide/audience/segments/segment_data#performance-data-by-segment).

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Qué debo comprobar si el seguimiento analítico parece incorrecto o está vacío? {#what-should-i-check-if-analytics-tracking-looks-wrong-or-empty}

Confirma que **Analytics Tracking** sigue habilitado en **Segment Details**, que no has superado el límite por aplicación (25 segmentos con seguimiento) y espera hasta 24 horas para que los datos se completen después de habilitar el seguimiento por primera vez. Si los problemas continúan, verifica la definición del segmento y el intervalo de fechas del informe, y luego [ponte en contacto con Soporte]({{site.baseurl}}/braze_support).