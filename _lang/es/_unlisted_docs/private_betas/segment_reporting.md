---
nav_title: Informes por Segment
article_title: Informes por Segment en el generador de informes
permalink: /segment_reporting_report_builder/
description: "Este artículo de referencia cubre Segment como dimensión de informes en el generador de informes, incluyendo cómo generar informes sobre Segments, desglosar por Segment y qué combinaciones son compatibles."
hidden: true
noindex: true
page_type: reference
---

# Informes por Segment en el generador de informes {#segment-reporting-in-report-builder}

> Este artículo explica cómo usar Segments como dimensión de informes en el generador de informes, incluyendo cómo generar informes sobre Segments, desglosar por Segment y qué combinaciones son compatibles.

{% multi_lang_include alerts/early_access_beta_alert.md feature='Segment reporting' contact='CSM or administrador de éxito de cliente or administrador de éxito de cliente' %}

El generador de informes admite **Segments** en filas y como opción de desglose, para que puedas ver el rendimiento de tus Segments y desglosar el rendimiento de Campaigns o Canvas por pertenencia a un Segment. Si **Segments** no aparece en los desplegables de **Rows** o **Drilldown**, esta característica no se ha habilitado para tu cuenta.

Puedes responder preguntas como:

- ¿Cómo está rindiendo un Segment específico a lo largo del tiempo?
- ¿Qué Campaigns y Canvas están dirigidos a un Segment determinado, y cómo rindió cada uno?
- ¿Cómo se compara la participación entre Segments para una sola Campaign o Canvas?

{% alert note %}
Los informes por Segment solo están disponibles para Segments con [seguimiento de análisis]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking) habilitado. Para seleccionar **Segments** en el desplegable de **Rows**, necesitas el [permiso "Ver informes del panel"]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) a nivel de espacio de trabajo.
{% endalert %}

## Generar informes sobre Segments {#report-on-segments}

Para generar informes sobre Segments directamente:

1. Ve a **Analytics** > **Report Builder (New)**.
2. Haz clic en **Create New Report**.
3. En el desplegable de **Rows**, selecciona **Segments**.
4. (Opcional) Selecciona **Add drilldown** para desglosar aún más los datos del Segment:
   - **Campaigns and Canvases:** Ve qué Campaigns y Canvas están dirigidos al Segment, y cómo rindió cada uno.
   - **Date:** Ve cómo el tamaño o las tendencias de rendimiento de un Segment evolucionan a lo largo del tiempo. Combínalo con un gráfico de líneas para visualizar la tendencia.
5. En **Report content**, abre el desplegable de **Segments** y selecciona los Segments que deseas añadir a tu informe.
6. Selecciona métricas en **Columns** > **Customize Metrics**, luego establece tu rango de fechas en **Report content**.
7. Si añadiste un desglose de **Campaigns and Canvases**, añade las Campaigns y Canvas que deseas incluir en el informe.
8. Haz clic en **Save and run**.

Para el flujo de trabajo completo del generador de informes, consulta [Crear un informe]({{site.baseurl}}/user_guide/analytics/reports/report_builder#creating-a-report).

## Desglosar por Segment {#drill-down-by-segment}

Para desglosar informes de Campaigns, Canvas o canales por Segment:

1. En el desplegable de **Rows**, selecciona **Campaigns**, **Canvases** o **Campaigns and Canvases**.
2. Selecciona **Add drilldown** y elige **Segment**.
3. En **Report content**, abre el desplegable de **Segments** y selecciona los Segments que deseas añadir a tu informe.
4. Selecciona métricas en **Columns** > **Customize Metrics**, luego establece tu rango de fechas en **Report content**.
5. Añade las Campaigns o Canvas que deseas incluir en el informe.
6. Haz clic en **Save and run** para ver el rendimiento desglosado por cada Segment al que se dirigieron tus Campaigns o Canvas.

Esto es especialmente útil para espacios de trabajo que envían la misma Campaign o Canvas a múltiples Segments. Puedes ver cómo respondió cada Segment sin tener que cruzar manualmente la pertenencia al Segment con el rendimiento de la Campaign.

## Combinaciones compatibles {#supported-combinations}

Las siguientes combinaciones de **Rows** y **Drilldown** son compatibles para los informes por Segment:

| Filas | Desglose |
| ----- | ----- |
| Segment | Campaigns y Canvas |
| Segment | Fecha |
| Campaign | Segment |
| Campaign | Variante |
| Canvas | Segment |
| Campaigns y Canvas | Segment |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Combinaciones compatibles de filas y desglose"}

{% alert note %}
El generador de informes admite un desglose a la vez. Si seleccionas **Campaigns** en el desplegable de **Rows**, puedes desglosar por **Variant** o **Segment**, pero no ambos en el mismo informe.
{% endalert %}

## Disponibilidad de métricas {#metrics-availability}

No todas las métricas del generador de informes están disponibles cuando generas informes sobre Segments. Las métricas que puedes seleccionar también dependen de si **Segments** está en **Rows** o en **Drilldown**, y de si el informe incluye una dimensión de Campaign o Canvas.

| Métrica | Disponibilidad |
| ----- | ----- |
| Métricas de canal y mensajería general | Disponibles para las combinaciones compatibles de filas y desglose. |
| Recuentos de conversión (Conversiones A–D) y nombres de eventos de conversión | Disponibles cuando las dimensiones de Segment y Campaign o Canvas aparecen juntas. Usa **Segments** en filas con un desglose de **Campaigns and Canvases**; o usa **Campaigns**, **Canvases** o **Campaigns and Canvases** en filas con un desglose de **Segment**. |
| Ingresos y tasa de conversión | No disponibles para informes con dimensión de Segment. |
| Ingresos y recuento de compras del Segment | Disponibles solo cuando **Segments** está en filas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Disponibilidad de métricas de informes por Segment"}

Para más información sobre cómo tus selecciones de filas y desglose afectan las métricas, consulta [Disponibilidad de métricas]({{site.baseurl}}/user_guide/analytics/reports/report_builder#metrics-availability) en el generador de informes.