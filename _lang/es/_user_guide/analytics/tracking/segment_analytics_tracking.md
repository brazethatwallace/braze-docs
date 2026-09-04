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

Si no activas el seguimiento analítico para un segmento, podrás acceder a [las estadísticas en tiempo real]({{site.baseurl}}/user_guide/audience/segments/segment_data#segment-statistics) de ese segmento y dirigirte a sus usuarios con campañas. La única diferencia es si puedes acceder a las herramientas de análisis específicas mencionadas en esta página.

## Activar el análisis de segmentos {#turning-on-segment-analytics}

En la sección **Segment Details** de la página de un segmento, activa **Analytics Tracking**.

![Alternador de seguimiento de análisis para un segmento]({% image_buster /assets/img_archive/A_Tracking_2.png %})

Un espacio de trabajo puede tener el seguimiento activado para un máximo de 25 segmentos. Braze recomienda realizar el seguimiento de los segmentos que son importantes para ti a la hora de analizar y entender los efectos de tus Campaigns en las sesiones, los ingresos y las compras.

{% alert note %}
Después de habilitar el seguimiento de análisis, espera un tiempo antes de que los datos del segmento se completen en tus informes. Si los datos no se completan en un plazo de 24 horas, [contacta con Soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support).
{% endalert %}

## Ver ingresos y compras a lo largo del tiempo {#viewing-revenue-and-purchases-over-time}

Ve a **Analytics** > **Revenue Report** para consultar datos sobre [ingresos y compras a lo largo del tiempo para este segmento]({{site.baseurl}}/user_guide/analytics/reports/revenue_report).

Los gráficos de ingresos y compras reflejan la actividad registrada después de que se activa el seguimiento de análisis para ese segmento. Activar el seguimiento no rellena retroactivamente las compras anteriores en esos informes. Cuando compares segmentos, utiliza solo rangos de tiempo en los que el seguimiento estuviera habilitado para cada segmento que selecciones.

![Datos de ingresos por segmento]({% image_buster /assets/img_archive/Revenue.png %})

Para comparar visualmente los datos de segmentos en cualquier rango de tiempo personalizado, añade o elimina segmentos del gráfico. Selecciona **By Segment** en el menú desplegable **Breakdown** y, a continuación, selecciona tus segmentos en **Breakdown values**.

Selecciona cualquier nombre de segmento en la leyenda del gráfico para activar o desactivar la visibilidad de las métricas de ese segmento.

![Ingresos para múltiples segmentos]({% image_buster /assets/img_archive/segment_revenue_multiple.png %})

## Sesiones a lo largo del tiempo {#sessions-over-time}

De manera similar, puedes encontrar datos sobre las [sesiones a lo largo del tiempo para este Segment en particular]({{site.baseurl}}/user_guide/analytics/dashboards/home) en la página **Inicio**.

![Datos de sesiones por Segment]({% image_buster /assets/img_archive/events_over_time2.png %})

## Ver eventos personalizados a lo largo del tiempo {#view-custom-events-over-time}

Consulta los datos sobre [eventos personalizados a lo largo del tiempo para Segments]({{site.baseurl}}/user_guide/data/activation/events/custom_events#analytics) yendo a **Analytics** > **Informe de eventos personalizados**.

## Uso de plantillas del Generador de consultas {#using-query-builder-templates}

Cuando el seguimiento de análisis está activado, puedes usar las plantillas de informes del Generador de consultas para desglosar las métricas de rendimiento de Campaigns, Canvas, variantes y pasos por Segments. Para obtener más información, consulta [Datos de Segment]({{site.baseurl}}/user_guide/audience/segments/segment_data#viewing-performance-data-by-segment).

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Qué debo comprobar si el seguimiento de análisis parece incorrecto o está vacío? {#what-should-i-check-if-analytics-tracking-looks-wrong-or-empty}

Confirma que **Analytics Tracking** sigue habilitado en **Segment Details**, que no has superado el límite por espacio de trabajo (25 Segments con seguimiento) y espera hasta 24 horas para que los datos se completen después de habilitar el seguimiento por primera vez. Si los problemas continúan, verifica la definición del Segment y el rango de fechas del informe, y luego [contacta con soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support).