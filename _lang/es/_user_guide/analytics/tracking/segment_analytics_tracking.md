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

# Seguimiento analítico por Segments {#segment-analytics-tracking}

> Cuando el seguimiento analítico está activado para un Segment, puedes ver las sesiones, los eventos personalizados y los ingresos a lo largo del tiempo para ese Segment.

Si no activas el seguimiento analítico para un Segment, podrás acceder a [las estadísticas en tiempo real]({{site.baseurl}}/user_guide/audience/segments/segment_data/#segment-statistics) de ese Segment y dirigirte a sus usuarios con Campaigns. La única diferencia es si puedes acceder a las herramientas de análisis específicas mencionadas en esta página.

## Activar el seguimiento analítico por Segments {#turning-on-segment-analytics}

En la sección **Segment Details** de la página de un Segment, activa **Analytics Tracking**.

![Activación del seguimiento analítico de un Segment]({% image_buster /assets/img_archive/A_Tracking_2.png %})

Una aplicación puede tener activado el seguimiento de hasta 25 Segments. Braze recomienda realizar un seguimiento de los Segments que te resulten importantes para analizar los efectos de tus Campaigns sobre las sesiones, los ingresos y las compras.

## Ver los ingresos y las compras a lo largo del tiempo {#viewing-revenue-and-purchases-over-time}

Ve a **Analytics** > **Revenue Report** para ver los datos sobre [ingresos y compras a lo largo del tiempo para este Segment]({{site.baseurl}}/user_guide/analytics/reports/revenue_report/).

![Datos de ingresos por Segment]({% image_buster /assets/img_archive/Revenue.png %})

Para comparar visualmente los datos de los Segments en cualquier intervalo de tiempo personalizado, añade o elimina Segments del gráfico. Selecciona **By Segment** en el desplegable **Breakdown** y, a continuación, selecciona tus Segments en **Breakdown values**.

Selecciona cualquier nombre de Segment encima del gráfico para activar o desactivar la visibilidad de las métricas de ese Segment.

![Ingresos por múltiples Segments]({% image_buster /assets/img_archive/segment_revenue_multiple.png %})

## Sesiones a lo largo del tiempo {#sessions-over-time}

Del mismo modo, puedes encontrar datos sobre [las sesiones a lo largo del tiempo para este Segment en particular]({{site.baseurl}}/user_guide/analytics/dashboards/home/#exporting-app-usage-data) en la página **Home**.

![Datos de sesiones por Segment]({% image_buster /assets/img_archive/events_over_time2.png %})

## Ver eventos personalizados a lo largo del tiempo {#view-custom-events-over-time}

Para ver los datos de [los eventos personalizados a lo largo del tiempo para los Segments]({{site.baseurl}}/user_guide/data/activation/events/custom_events/#analytics), ve a **Analytics** > **Custom Events Report**.

## Utilización de las plantillas del Generador de consultas {#using-query-builder-templates}

Cuando el seguimiento analítico está activado, puedes utilizar las plantillas de informes del Generador de consultas para desglosar las métricas de rendimiento de Campaigns, Canvas, variantes y pasos por Segments. Para saber más, consulta [Datos de Segments]({{site.baseurl}}/user_guide/audience/segments/segment_data/#performance-data-by-segment).