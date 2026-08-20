---
nav_title: Filtrar por rango de fechas
article_title: Filtrar elementos de catálogo por rango de fechas
page_order: 1
page_type: reference
description: "Usa selecciones de catálogo con expresiones de fecha en Liquid para mostrar elementos de catálogo dentro de una ventana de tiempo dinámica, como eventos en los próximos siete días."
---

# Filtrar elementos de catálogo por rango de fechas {#filter-catalog-items-by-date-range}

> Este ejemplo muestra cómo un mercado de entradas ficticio usa selecciones de catálogo y expresiones de fecha en Liquid para enviar por correo electrónico a los consumidores solo los eventos que están próximos dentro de los siguientes siete días desde el momento del envío. Creas una selección con filtros de tiempo dinámicos y luego renderizas los elementos de catálogo coincidentes en un mensaje de Campaign o Canvas.

## Acerca de este ejemplo {#about-this-example}

MovieCanon, un mercado de entradas ficticio, usa este patrón para asegurar que las Campaigns de correo electrónico listen solo conciertos y espectáculos relevantes en el tiempo.

El patrón usa dos características de Braze juntas:

- Una [selección de catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) con filtros de campo `time` cuyos valores son fragmentos de código Liquid que calculan una ventana de tiempo dinámica en el momento del envío
- La etiqueta de Liquid {% raw %}`{% catalog_selection_items %}`{% endraw %} en el cuerpo del mensaje para renderizar las filas de catálogo coincidentes

## Consideraciones {#considerations}

- Crea un campo `time` en el catálogo para la columna de fecha y hora por la que filtras, no un campo de cadena. Almacena los valores en formato [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601), como `2026-06-20T19:30:00Z`. Para los tipos compatibles, consulta [Tipos de datos compatibles]({{site.baseurl}}/user_guide/data/activation/catalogs/create#supported-data-types).
- Los operadores `before` y `after` usan comparaciones estrictas. Los eventos exactamente iguales a una marca de tiempo límite pueden ser excluidos. Usa marcas de tiempo completas cuando necesites que la ventana comience en el momento del envío. Los valores de solo fecha `YYYY-MM-DD` se convierten a medianoche UTC de ese día.
- El Liquid en los filtros de selección se evalúa en el momento del envío. La variable `'now'` refleja cuándo se renderiza el mensaje, normalmente en UTC. Confirma que la ventana resultante coincida con tu intención en las distintas zonas horarias.
- [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), [Content Blocks]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks), etiquetas de catálogo y `abort_message` no son compatibles en los valores de filtro de selección de catálogo. Si un filtro incluye una etiqueta no permitida, la selección no devuelve elementos sin generar un error.
- Puedes agregar hasta 10 filtros por selección y devolver hasta 50 elementos. Ajusta la ventana de siete días cambiando los segundos sumados a `'now'` (`604800` = 7 días multiplicados por `86400` segundos por día).
- Los arreglos de resultados de selección de catálogo tienen índice base cero (`items[0]` es el primer elemento).
- Prueba el Liquid de los filtros, el Liquid del mensaje y la lógica de cancelación fuera de tu espacio de trabajo de producción antes de enviar a audiencias de producción.

## Configuración {#setup}

Este ejemplo asume un catálogo llamado `live_events` con estos campos:

| Campo | Tipo | Valor de ejemplo |
| ----- | ---- | ---------------- |
| `id` | String | `show-1042` |
| `event_name` | String | `Summer Jazz Night` |
| `event_date_time` | Time | `2026-06-20T19:30:00Z` |
| `ticket_price` | Number | `45` |
| `city` | String | `Austin` |
| `venue` | String | `Riverside Amphitheater` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campos del catálogo" }

Si aún no tienes un catálogo similar, [crea un catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create) y sube o sincroniza tus datos de eventos primero.

### Paso 1: Crear la selección de catálogo {#step-1-create-the-catalog-selection}

1. Ve a **Configuración de datos** > **Catálogos** y selecciona el catálogo `live_events`.
2. Abre la pestaña **Selección** y selecciona **Crear selección**.
3. Nombra la selección `seven_day_window` y agrega una descripción opcional, como "Eventos que ocurren dentro de los próximos siete días."
4. Establece un **Límite de resultados** para el número máximo de eventos a devolver (hasta 50).
5. No guardes aún. Agrega los filtros de fecha en los siguientes pasos.

### Paso 2: Agregar el filtro de límite superior {#step-2-add-the-upper-bound-filter}

Agrega un filtro en el campo `event_date_time`:

| Configuración | Valor |
| ------------- | ----- |
| **Campo de filtro** | `event_date_time` |
| **Operador** | `before` |
| **Valor** | Fragmento de código Liquid |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configuración del filtro de límite superior" }

En el campo de valor del filtro, ingresa este fragmento de código Liquid. Calcula una marca de tiempo siete días después del momento del envío:

{% raw %}
```liquid
{% assign seven_days = 'now' | date: '%s' | plus: 604800 %}{{ seven_days | date: "%Y-%m-%dT%H:%M:%SZ" }}
```
{% endraw %}

Esto establece el límite superior de la ventana para que solo se incluyan eventos antes de esa marca de tiempo.

### Paso 3: Agregar el filtro de límite inferior {#step-3-add-the-lower-bound-filter}

Agrega un segundo filtro en el mismo campo:

| Configuración | Valor |
| ------------- | ----- |
| **Campo de filtro** | `event_date_time` |
| **Operador** | `after` |
| **Valor** | Fragmento de código Liquid |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Configuración del filtro de límite inferior" }

Ingresa este fragmento de código Liquid para el límite inferior. Usa el momento de envío actual para que se excluyan los eventos que ya han comenzado:

{% raw %}
```liquid
{{ 'now' | date: "%Y-%m-%dT%H:%M:%SZ" }}
```
{% endraw %}

Juntos, los dos filtros devuelven elementos del catálogo donde `event_date_time` es posterior al momento de envío actual y anterior a siete días desde el momento del envío. Selecciona **Crear selección** para guardar.

### Paso 4: Hacer referencia a la selección en un mensaje {#step-4-reference-the-selection-in-a-message}

En tu mensaje de Campaign o Canvas, inserta Liquid que extraiga elementos de la selección. Puedes usar **Agregar personalización** (**Elementos de catálogo** > **Usar una selección**) o pegar la etiqueta manualmente:

{% raw %}
```liquid
{% catalog_selection_items live_events seven_day_window %}
Here are some upcoming events:

{{ items[0].event_name }} — ${{ items[0].ticket_price }}
{{ items[0].city }} · {{ items[0].venue }}

{{ items[1].event_name }} — ${{ items[1].ticket_price }}
{{ items[1].city }} · {{ items[1].venue }}
```
{% endraw %}

Reemplaza los índices de arreglo codificados con un bucle si necesitas renderizar un número variable de resultados.

### Paso 5: Manejar resultados vacíos {#step-5-handle-empty-results}

Cuando ningún elemento del catálogo coincide con la selección, el arreglo `items` está vacío y el bloque etiquetado no renderiza nada. Para omitir el envío o mostrar contenido alternativo, envuelve la etiqueta en un condicional:

{% raw %}
```liquid
{% catalog_selection_items live_events seven_day_window %}
{% if items.size == 0 %}
{% abort_message('Catalog selection returned 0 items') %}
{% endif %}

Here are some upcoming events:
{{ items[0].event_name }}
```
{% endraw %}

Para más información, consulta [Cancelar mensajes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages).

## Artículos relacionados {#related-articles}

- [Crear un catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/create)
- [Selecciones]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)
- [Usar catálogos en Campaigns]({{site.baseurl}}/user_guide/data/activation/catalogs/use)
- [Filtro `date` de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters#date-filter)
- [Biblioteca de casos de uso de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases)