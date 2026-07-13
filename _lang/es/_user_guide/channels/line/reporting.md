---
nav_title: Informes
article_title: Informes de LINE
page_order: 21
description: "Este artículo de referencia cubre las métricas de LINE utilizadas en Braze, así como cómo verlas en tus campañas de LINE."
page_type: reference
channel:
 - LINE
alias: /line/reporting/
---

# Informes de LINE {#line-reporting}

> Después de lanzar tu campaña o Canvas, puedes ver las métricas clave en la página de detalles de la campaña o en los análisis de Canvas. Este artículo explica dónde puedes encontrar esas métricas y qué representan.

{% alert tip %}
¿Buscas definiciones de los términos y métricas de tu informe? Consulta el [Glosario de métricas de informes]({{site.baseurl}}/user_guide/analytics/metrics_glossary).
{% endalert %}

## Análisis de campaña {#campaign-analytics}

En la pestaña **Campaign Analytics**, puedes ver tus informes en una serie de paneles. Es posible que veas más o menos de los que se enumeran aquí, pero cada uno tiene su propósito.

{% alert note %}
Las estadísticas relacionadas con aperturas y clics de LINE solo se calculan si más de 20 usuarios realizan el evento en un día determinado.
{% endalert %}

### Detalles de la campaña {#campaign-details}

El panel **Campaign Details** muestra un resumen general del rendimiento de tus mensajes de LINE.

Revisa este panel para ver métricas generales como el número de mensajes enviados a los destinatarios, la tasa de conversión primaria y los ingresos totales generados por este mensaje. También puedes revisar la configuración de entrega, audiencia y conversión desde esta página.

#### Grupos de control {#control-groups}

Para medir el impacto de un mensaje de LINE individual, puedes añadir un [grupo de control]({{site.baseurl}}/user_guide/messaging/ab_testing) a una prueba A/B. El panel de nivel superior **Campaign Details** no incluye métricas de la variante del grupo de control.

### Rendimiento de LINE {#line-performance}

El panel **LINE Performance** describe el rendimiento de tu mensaje en varias dimensiones. Las métricas de este panel varían en función del canal de mensajería elegido y de si estás ejecutando una prueba multivariante o no. Puedes hacer clic en el icono <i class="fa fa-eye preview-icon"></i> **Preview** para ver una vista previa de tu mensaje para cada variante o canal.

![El panel "LINE Performance" muestra métricas para dos variantes.]({% image_buster /assets/img/line/line_performance.png %})

Si quieres simplificar tu vista, selecciona **+ Add/Remove Columns** y desmarca las métricas que desees. De forma predeterminada, se muestran todas las métricas.

#### Métricas de LINE {#line-metrics}

Estas son algunas métricas clave de LINE que puedes ver en tus análisis. Para consultar las definiciones de todas las métricas de LINE utilizadas en Braze, consulta el [Glosario de métricas de informes]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

| Término | Definición |
| --- | --- |
| Envíos | El número total de envíos comunicados correctamente entre Braze y LINE. Esto no significa que el mensaje haya sido recibido por el usuario. |
| Aperturas únicas | El número total de mensajes de LINE enviados que fueron abiertos por los usuarios después de alcanzar un umbral mínimo de 20 mensajes por día. |
| Aperturas totales | El número total de veces que los mensajes de LINE enviados fueron abiertos por los usuarios después de alcanzar un umbral mínimo de 20 mensajes por día. |
| Clics únicos | El número total de mensajes de LINE enviados en los que los usuarios hicieron clic, después de alcanzar un umbral mínimo de 20 mensajes por día. |
| Clics totales | El número total de veces que los usuarios hicieron clic en los mensajes de LINE enviados después de alcanzar un umbral mínimo de 20 mensajes por día. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Métricas de LINE" }

### Rendimiento histórico {#historical-performance}

El panel **Historical Performance** te permite ver las métricas del panel **Message Performance** como un gráfico a lo largo del tiempo. Usa los filtros en la parte superior del panel para modificar las estadísticas y los canales que se muestran en el gráfico. El rango de tiempo de este gráfico siempre coincide con el rango de tiempo especificado en la parte superior de la página.

Para obtener un desglose día a día, selecciona el menú de hamburguesa <i class="fas fa-bars"></i> y selecciona **Download CSV** para recibir una exportación CSV del informe.

### Detalles del evento de conversión {#conversion-event-details}

El panel **Conversion Event Details** te muestra el rendimiento de tus eventos de conversión para tu campaña. Para más información, consulta [Eventos de conversión]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/conversion_correlation).

### Correlación de conversión {#conversion-correlation}

El panel **Conversion Correlation** te ofrece información sobre qué atributos y comportamientos de los usuarios ayudan o perjudican los resultados que estableciste para las campañas. Para más información, consulta [Correlación de conversión]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/conversion_correlation).