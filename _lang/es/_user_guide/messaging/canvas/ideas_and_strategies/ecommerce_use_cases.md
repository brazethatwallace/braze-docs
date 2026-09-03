---
nav_title: Casos de uso de comercio electrónico
article_title: Casos de uso de comercio electrónico
alias: /ecommerce_use_cases/
page_order: 4
description: "Este artículo de referencia cubre varias plantillas prediseñadas de Braze adaptadas específicamente para especialistas en marketing de comercio electrónico, facilitando la implementación de estrategias esenciales."
toc_headers: h2
---

# Cómo usar los eventos recomendados de comercio electrónico {#how-to-use-ecommerce-recommended-events}

> Esta página explica cómo y dónde puedes usar los eventos recomendados de comercio electrónico en toda la plataforma, incluyendo cómo usar las plantillas de Canvas de comercio electrónico de Braze.

{% alert note %}
Si estás usando el nuevo conector de Shopify, los eventos recomendados de comercio electrónico estarán disponibles automáticamente a través de la integración.
{% endalert %}

## Usar una plantilla de Canvas {#using-a-canvas-template}

Para usar una plantilla de Canvas:
1. Ve a **Mensajería** > **Canvas**.
2. Selecciona **Crear Canvas** > **Usar una plantilla de Canvas**.
3. Examina la pestaña **Plantillas de Braze** para encontrar la plantilla que quieras usar. Puedes previsualizar una plantilla seleccionando su nombre.
4. Selecciona **Aplicar plantilla** para la plantilla que quieras usar.<br><br>![Página de plantillas de Canvas abierta en la pestaña de plantillas de Braze que muestra una lista de plantillas usadas recientemente y plantillas de Braze seleccionables.]({% image_buster /assets/img_archive/apply_template.png %}){: style="max-width:80%;"}

## Plantillas de Canvas de comercio electrónico {#ecommerce-canvas-templates}

Braze ofrece cuatro plantillas de Canvas de comercio electrónico.

{% multi_lang_include canvas/ecommerce_templates.md %}

## Personalización de mensajes {#message-personalization}

[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) es un potente lenguaje de plantillas utilizado por Braze que te permite crear contenido dinámico y personalizado para tus clientes. Mediante el uso de etiquetas de Liquid, puedes personalizar mensajes basándote en datos de clientes, información de productos y otras variables, mejorando la experiencia de compra e impulsando la participación.

### Características principales de Liquid {#key-features-of-liquid}

- **Contenido dinámico:** Inserta información específica del cliente, como nombres, detalles de pedidos y preferencias, en tus mensajes.
- **Lógica condicional:** Usa sentencias if/else para mostrar contenido diferente según condiciones específicas (como la ubicación del cliente y el historial de compras).
- **Bucles:** Itera sobre colecciones de productos o datos de clientes para mostrar listas o cuadrículas de artículos.

### Primeros pasos con Liquid {#getting-started-with-liquid}

Para empezar a personalizar tus mensajes usando etiquetas de Liquid, puedes consultar los siguientes recursos:

- <a href="/docs/partners/ecommerce/shopify/shopify_data_features#tracked-shopify-events">Datos de Shopify</a> de referencia con etiquetas de Liquid predefinidas
- [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)

## Segmentación {#segmentation}

Usa los segmentos de Braze para crear segmentos de clientes específicos basados en atributos y comportamientos concretos, y entregar mensajería y campañas personalizadas. Con esta potente característica, puedes interactuar eficazmente con tus clientes llegando a la audiencia adecuada con el mensaje correcto en el momento oportuno.

Para más información sobre cómo empezar con los segmentos, consulta [Acerca de los segmentos de Braze]({{site.baseurl}}/user_guide/audience/segments).

### Eventos recomendados {#recommended-events}

Los eventos de comercio electrónico se basan en [eventos recomendados]({{site.baseurl}}/recommended_events).
Dado que los eventos recomendados son eventos personalizados más específicos, puedes buscar los nombres de eventos recomendados de comercio electrónico seleccionando cualquier [filtro de evento personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events#segmentation-filters).

### Filtros de comercio electrónico {#ecommerce-filters}

Segmenta a tus usuarios con filtros de comercio electrónico, como **Ecommerce Source** y **Total Revenue**, yendo a la sección **Ecommerce** dentro del segmentador.

Para ver una lista de filtros de comercio electrónico y sus definiciones, consulta [Filtros de segmento]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters) y selecciona la categoría de búsqueda "eCommerce".

![Desplegable de filtros de segmento con filtros de comercio electrónico.]({% image_buster /assets/img_archive/ecommerce_filters.png %}){: style="max-width:50%"}

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation for eCommerce filters' %}

## Propiedades de eventos anidados {#nested-event-properties}

Para segmentar por propiedades de eventos anidados, puedes aprovechar las [extensiones de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension#why-use-segment-extensions). Por ejemplo, puedes usar extensiones de segmento para encontrar quién ha comprado el producto "SKU-123" en los últimos 90 días.

## Análisis {#analytics}

### Informe de eventos personalizados {#custom-events-report}

Puedes rastrear el volumen de eventos recomendados de comercio electrónico en el [informe de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events#analytics). Filtra por **Perform Custom Event** y luego especifica el [nombre del evento recomendado de comercio electrónico]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events) para ver su rendimiento a lo largo del tiempo.

![Gráfico de eventos personalizados que muestra resultados para seis eventos seleccionados.]({% image_buster /assets/img/ecommerce/custom_events_chart.png %})

### Paneles {#dashboards}

#### Panel de conversiones {#conversions-dashboard}

Después de lanzar una campaña o Canvas usando el evento de conversión "Places Order", puedes crear un [informe de conversión]({{site.baseurl}}/user_guide/analytics/dashboards/conversions#setting-up-your-report) correspondiente para rastrear el rendimiento.

![Tabla de detalles de conversiones con campañas y Canvas, y las estadísticas de conversión asociadas.]({% image_buster /assets/img_archive/conversion_details_table.png %})

#### Panel de ingresos de comercio electrónico {#ecommerce-revenue-dashboard}

Para obtener información sobre los ingresos atribuidos a la última campaña o Canvas con los que un usuario interactuó antes de realizar un pedido, usa el [panel de ingresos de comercio electrónico]({{site.baseurl}}/ecommerce_revenue_dashboard) y selecciona una ventana de conversión.

### Informe de ingresos {#revenue-report}

Para analizar datos de estos nuevos eventos, ve al [generador de paneles]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder) y consulta el [panel **eCommerce Revenue - Last Touch Attribution**]({{site.baseurl}}/ecommerce_revenue_dashboard).