---
nav_title: Métricas por segmentos
article_title: Métricas por segmentos
page_order: 3
page_type: reference
description: "Esta página describe cómo puedes usar las plantillas de informes del generador de consultas para desglosar las métricas de rendimiento de Campaigns, Canvas, variantes y pasos por segmentos."
tool:
  - Segments
  - Reports

---

# Métricas por segmentos {#metrics-by-segments}

> Usa las plantillas de informes del [generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder) para desglosar las métricas de rendimiento de Campaigns, Canvas, variantes y pasos por segmentos.

El [seguimiento de análisis]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking) debe estar activado para los segmentos de los que quieras consultar métricas.

Para ejecutar estos informes, haz lo siguiente:
1. En el **generador de consultas**, elige crear un nuevo informe SQL con una plantilla.
2. Selecciona **Segment breakdowns** para la métrica, lo que filtra las plantillas para aquellas en las que las métricas incluyen desgloses por segmento, que son:
- Métricas de rendimiento de correo electrónico por segmento
- Métricas de participación de correo electrónico para variantes o pasos, por segmento
- Compras e ingresos por segmento
- Compras e ingresos para variantes o pasos, por segmento
- Rendimiento de push por segmento

![La página de desglose por segmento contiene un editor SQL, un panel lateral con pestañas para Variables, tablas de datos disponibles, historial de consultas y el generador de consultas con IA, y una sección de resultados.]({% image_buster /assets/img_archive/segment_breakdown.png %})

## Plantillas de informes {#report-templates}

{% tabs %}
{% tab Métricas de participación de correo electrónico por segmento %}

### Ver métricas para Campaigns o Canvas {#campaign-canvas-email}

Para ver las métricas de rendimiento de correo electrónico desglosadas por segmento a nivel de Campaign o Canvas, usa la pestaña [Variables](#variables) para especificar las Campaigns o Canvas y un periodo de tiempo para extraer datos. Si no se especifican Campaigns o Canvas, el informe incluirá correos electrónicos de todas las Campaigns y Canvas del periodo de tiempo especificado. También puedes optar por ver todas las Campaigns y Canvas con determinadas etiquetas.

Las siguientes métricas de correo electrónico están disponibles en este informe:
- Envíos
- Entregas
- Quejas
- Unique Opens
- Aperturas únicas de máquina
- Aperturas únicas no de máquina
- Clics únicos
- Cancelaciones de suscripción
- Rebotes
- Rebotes blandos
- Diferidos

#### Resultados {#results}

Tus resultados mostrarán las métricas de participación de correo electrónico por segmento para las Campaigns o Canvas que seleccionaste. Si no seleccionaste Campaigns o Canvas específicos, tu informe mostrará las métricas de correo electrónico para cada segmento en todas las Campaigns y Canvas de correo electrónico dentro del periodo de tiempo de tu informe.

- **Filas:** Segments
- **Columnas:** métricas de participación de correo electrónico

### Ver métricas para variantes o pasos {#viewing-metrics-for-variants-or-steps}

Para ver el rendimiento de correo electrónico desglosado por segmento a nivel de variante de campaña, variante en Canvas o paso en Canvas, primero elige un informe a nivel de variante o paso (estos son informes que tienen "para variantes o pasos" en el título) y luego usa la pestaña **Variables** para especificar lo siguiente:

- Campaign o Canvas específico (obligatorio si usas un informe a nivel de variante o paso)
- Variantes (obligatorio si usas un informe a nivel de variante o paso)
- Paso en Canvas (opcional)

Las métricas son las mismas que las ofrecidas para la plantilla a [nivel de Campaign o Canvas](#campaign-canvas-email). Si eliges múltiples variantes, tus resultados se agruparán por variante.

#### Resultados

Tus resultados mostrarán las métricas de participación de correo electrónico por segmento para las variantes o pasos seleccionados.

- **Filas:** Segments
- **Columnas:** métricas de participación de correo electrónico

{% endtab %}

{% tab Compras e ingresos por segmento %}
### Ver métricas para Campaigns o Canvas {#viewing-metrics-for-campaigns-or-canvases}

Para ver las métricas de compras e ingresos desglosadas por segmento para una Campaign o Canvas específico, usa la pestaña [Variables](#variables) para especificar lo siguiente:

- Ventana de conversión (el número de días después de la recepción o clic del correo electrónico en los que Braze debe atribuir compras o ingresos)
- Producto específico (opcional)

Además, usa la pestaña **Variables** para especificar si deseas ejecutar el informe para una o más Campaigns o Canvas, o una o más etiquetas. Si no se eligen Campaigns, Canvas o etiquetas, el informe se ejecutará para todos los correos electrónicos de Campaigns o Canvas durante el periodo de tiempo elegido.

Actualmente, este informe extrae métricas solo del canal de correo electrónico. Los datos de ingresos o compras de canales distintos al correo electrónico no se reflejarán en el informe.

Las siguientes métricas están disponibles para correos electrónicos:

- Compras únicas tras recepción
- Ingresos tras recepción
- Compras únicas tras clic
- Ingresos tras clic
- Destinatarios únicos
- Clics únicos de correo electrónico

Todas las métricas de tasa usan los destinatarios únicos de correo electrónico como denominador.

#### Definiciones {#definitions}

- "Tras recepción" se refiere a eventos de compra o ingresos que ocurrieron dentro de tu ventana de conversión especificada, después de que los usuarios recibieron las Campaigns o Canvas especificados.
- "Tras clic" se refiere a los eventos de compra o ingresos que ocurrieron después de los eventos de compra, dentro de tu ventana de conversión especificada, después de que los usuarios hicieron clic en las Campaigns o Canvas especificados.

Por ejemplo, supongamos que un segmento contiene 10 usuarios y cinco de ellos realizaron una compra después de recibir tu correo electrónico. Si uno de esos cinco realizó una compra después de hacer clic en tu correo electrónico, tu "tasa de compras únicas tras recepción" sería del 50 % y tu "tasa de compras únicas tras clic" sería del 10 %.

![El informe muestra métricas de correo electrónico que incluyen compras únicas tras recepción, ingresos tras recepción, compras únicas tras clic, ingresos tras clic, destinatarios únicos y clics únicos de correo electrónico.]({% image_buster /assets/img_archive/segment_breakdown_results.png %})

#### Resultados

Tus resultados mostrarán las métricas de compras por segmento para las Campaigns o Canvas seleccionados. Si no seleccionaste Campaigns o Canvas específicos, tu informe mostrará las métricas de compras para cada segmento en todas las Campaigns o Canvas de correo electrónico dentro del periodo de tiempo de tu informe.

- **Filas:** Segments
- **Columnas:** métricas de compras


### Ver métricas para variantes o pasos

Para ver las métricas de compras e ingresos desglosadas por segmento para una variante de campaña, variante en Canvas o paso en Canvas específico, usa la pestaña [Variables](#variables) para especificar lo siguiente:

- Campaign o Canvas específico
- Variantes
- Paso en Canvas (opcional)
- Rango de tiempo
- Producto específico (opcional)

#### Resultados

Tus resultados mostrarán las métricas de compras por segmento para las variantes o pasos que seleccionaste.

- **Filas:** Segments
- **Columnas:** métricas de compras

{% endtab %}
{% tab Mejores o peores mensajes para participación de correo electrónico %}

### Ver métricas para los mejores o peores resultados {#viewing-metrics-for-the-top-or-bottom-performers}

Este informe en la pestaña [Variables](#variables) muestra las Campaigns, Canvas o pasos en Canvas que tuvieron el mejor o peor rendimiento para una métrica de participación de correo electrónico especificada.

Los ejemplos incluyen:
- 10 Campaigns con las tasas más altas de Unique Opens de correo electrónico
- 25 Canvas con la mayor cantidad de cancelaciones de suscripción de correo electrónico
- 50 pasos en Canvas con los clics únicos más altos

Las siguientes métricas de correo electrónico están disponibles en este informe:
- Envíos
- Entregas
- Quejas
- Unique Opens
- Aperturas únicas de máquina
- Aperturas únicas no de máquina
- Clics únicos
- Cancelaciones de suscripción
- Rebotes
- Rebotes blandos
- Quejas

Para ver este informe, debes especificar las siguientes variables en la pestaña **Variables**:
- **Metrics:** selecciona una de las métricas por la cual clasificar tus resultados
- **Number of reports:** selecciona los mejores o peores resultados y la cantidad de resultados, como los 10 mejores o los 15 peores
- **Message type:** especifica si tus resultados son Campaigns, Canvas o pasos en Canvas

#### Resultados

Tus resultados mostrarán las mejores (o peores) Campaigns, Canvas o pasos en Canvas que seleccionaste. Por ejemplo, si seleccionaste las 10 mejores Campaigns por tasa de clics, tus resultados mostrarán las 10 mejores Campaigns ordenadas de mayor a menor tasa de clics. Tus columnas mostrarán todas las métricas de participación de correo electrónico para cada fila (Campaigns, Canvas o pasos de mensaje).

{% endtab %}
{% tab Mejores o peores mensajes para compras %}

### Ver métricas para los mejores o peores resultados

Este informe en la pestaña [Variables](#variables) muestra las Campaigns, Canvas o pasos en Canvas que tuvieron el mejor o peor rendimiento para una métrica de compras o ingresos especificada.

Los ejemplos incluyen:
- 20 Campaigns con las tasas de compra más altas para un producto específico
- 25 Canvas con los mayores ingresos generados
- 10 pasos en Canvas con la tasa de compra de producto más baja

Las siguientes métricas de correo electrónico están disponibles en este informe:
- Compras únicas tras recepción
- Ingresos tras recepción
- Compras únicas tras clic
- Ingresos tras clic
- Destinatarios únicos
- Clics únicos de correo electrónico

Para ver este informe, debes especificar las siguientes variables en la pestaña **Variables**:
- **Metrics:** selecciona una de las métricas por la cual clasificar tus resultados
- **Number of reports:** selecciona los mejores o peores resultados y la cantidad de resultados, como los 10 mejores o los 15 peores
- **Message type:** especifica si tus resultados son Campaigns, Canvas o pasos en Canvas
- **Conversion window:** el número de días después de la recepción o clic del correo electrónico en los que Braze atribuirá compras o ingresos

#### Definiciones

- "Tras recepción" se refiere a eventos de compra o ingresos que ocurrieron dentro de tu ventana de conversión especificada, después de que los usuarios recibieron las Campaigns o Canvas especificados.
- "Tras clic" se refiere a los eventos de compra o ingresos que ocurrieron después de los eventos de compra, dentro de tu ventana de conversión especificada, después de que los usuarios hicieron clic en las Campaigns o Canvas especificados.

Por ejemplo, supongamos que un segmento contiene 10 usuarios y cinco de ellos realizaron una compra después de recibir tu correo electrónico. Si uno de esos cinco realizó una compra después de hacer clic en tu correo electrónico, tu tasa de "compras únicas tras recepción" sería del 50 % y tu tasa de "compras únicas tras clic" sería del 10 %.

#### Resultados

Tus resultados mostrarán las mejores (o peores) Campaigns, Canvas o pasos en Canvas que seleccionaste. Por ejemplo, si seleccionaste las 10 mejores Campaigns por "ingresos tras clic", tus resultados mostrarán las 10 mejores Campaigns ordenadas de mayor a menor "ingresos tras clic". Tus columnas mostrarán todas las métricas de compras para cada fila (Campaigns, Canvas o pasos de mensaje).

{% endtab %}
{% tab Rendimiento de push por segmento %}

### Ver métricas de push para segmentos {#viewing-push-metrics-for-segments}

Este informe en la pestaña [Variables](#variables) muestra las métricas de push desglosadas por segmentos.

En la pestaña **Variables**, especifica las Campaigns o Canvas para los que deseas ver métricas y un periodo de tiempo para extraer datos. Si no seleccionas ninguna Campaign o Canvas, el informe mostrará los push de todas las Campaigns y Canvas en el periodo de tiempo especificado. También puedes ver todas las Campaigns y Canvas con determinadas etiquetas.

Las siguientes métricas de push están disponibles en este informe:

- Envíos
- Rebotes
- Entregas
- Direct Opens

#### Resultados

Tu informe mostrará los siguientes resultados:

- **Filas:** Segments
- **Columnas:** métricas de push
{% endtab %}
{% endtabs %}