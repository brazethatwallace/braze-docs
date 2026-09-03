---
nav_title: Administrar segmentos
article_title: Administrar segmentos
page_order: 2
page_type: tutorial
tool: Segments
description: "Este artículo cubre las acciones que puedes realizar para administrar tus segmentos, como filtrar una lista de segmentos, crear segmentos y editar segmentos."

---

# Administrar segmentos {#manage-segments}

> La sección Segments te permite ver una lista completa de tus segmentos existentes, crear nuevos segmentos y editar los existentes. Puedes refinar la lista de segmentos seleccionando una variedad de filtros y columnas para que solo se muestre la información más relevante para ti.

![La sección Segments mostrando una lista de segmentos activos.]({% image_buster /assets/img/segment/segments_page.png %})

## Personalización de tu vista {#customizing-your-view}

Adapta tu vista de la lista de Segments usando filtros y cambiando las columnas que deseas que aparezcan. Cuando salgas de la sección **Segments** y regreses, la lista volverá a la vista predeterminada, eliminando cualquier filtro que hayas seleccionado previamente.

### Filtro de estado {#status-filter}

Puedes reducir la lista para mostrar solo los Segments activos o archivados. Cualquier Segment no archivado se considera activo.

### Filtros {#filters}

Ordena los Segments de la lista ajustando los siguientes filtros:
- **Última edición por:** El usuario que editó por última vez los Segments
- **Última edición:** Rango de tiempo en el que los Segments fueron editados por última vez
- **Tamaño estimado:** Rango aproximado de cuántos usuarios hay en los Segments
- **Etiquetas:** Etiquetas asociadas con los Segments
- **Equipos:** Equipos asociados con los Segments
- **Solo Segments con seguimiento avanzado:** Ver solo los Segments que tienen habilitado el [seguimiento de análisis]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking).

### Columnas {#columns}

Estas son las columnas de información que puedes seleccionar para mostrar en la lista de Segments:
- **Filtros:** Número de filtros en el Segment
- **Última edición:** Fecha en que el Segment fue editado por última vez
- **Última edición por:** El usuario que editó por última vez el Segment
- **Etiquetas:** Etiquetas asociadas con el Segment
- **Equipos:** Equipos asociados con el Segment
- **Tamaño estimado:** Número estimado de usuarios en el Segment
- **Canvas:** Número de Canvas que usan el Segment
- **Campaigns:** Número de Campaigns que usan el Segment

### Mostrar solo destacados {#show-starred-only}

Seleccionar **Show Starred Only** reduce tu vista a los Segments que hayas marcado como destacados.

## Ver el uso de mensajería de un segmento {#messaging-use}

Ve a la sección **Messaging Use** de un segmento para obtener un resumen de dónde se está usando el segmento, como dentro de otros segmentos, Campaigns y Canvas.

{% alert note %}
Para evitar bucles de segmentos que se referencian entre sí, los segmentos que usan el filtro **Segment Membership** no pueden ser referenciados por otros segmentos. Para más detalles, consulta [Filtros de segmentación]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).
{% endalert %}

## Gestión de segmentos específicos {#managing-specific-segments}

![El menú de edición de un segmento que muestra las opciones "Editar", "Duplicar", "Archivar" y "Añadir a destacados".]({% image_buster /assets/img/segment/segments_page_edit_menu.png %}){: style="float:right;max-width:25%;"}

Para gestionar un segmento específico, coloca el cursor sobre él y selecciona el icono de menú al final de la fila para ver las siguientes opciones:
- **Editar:** Edita los filtros de tu segmento.
- **Duplicar:** Crea una copia de tu segmento.
- **Archivar:** Archiva el segmento. Ten en cuenta que esto también archivará cualquier Campaign o Canvas que use ese segmento.
- **Añadir a destacados:** Destaca el segmento, lo que te permite acceder rápidamente a él marcando la casilla Mostrar solo destacados en la sección de Segments.

También puedes realizar acciones masivas, específicamente archivar y etiquetar en bloque, marcando las casillas junto a los nombres de varios segmentos.

{% alert tip %}
Si necesitas una exportación legible por máquina de los segmentos existentes en el espacio de trabajo (no solo la vista de tabla actual), usa el [endpoint Exportar lista de segmentos]({{site.baseurl}}/api/endpoints/export/segments/get_segment) y pagina a través de los resultados. Para auditar segmentos archivados, revísalos por separado en el panel de **Segments** usando el filtro de estado.
{% endalert %}

![Varios segmentos seleccionados con "CRM" seleccionado en el campo desplegable "Etiquetar como".]({% image_buster /assets/img/segment/segments_bulk_action.png %}){: style="max-width:45%;"}

### Cambios desde la última visualización {#changes-since-last-viewed}

El número de actualizaciones a los segmentos realizadas por otros miembros de tu equipo se registra mediante la métrica *Cambios desde la última visualización* en la página de resumen de segmentos. Selecciona **Cambios desde la última visualización** para ver un registro de cambios de las actualizaciones del nombre, la descripción y el público objetivo del segmento. Para cada actualización, puedes ver quién la realizó y cuándo. Puedes usar este registro de cambios para auditar los cambios en tu segmento.

## Búsqueda de Segments {#searching-for-segments}

Busca nombres de Segments introduciendo términos en el campo de búsqueda.

Se buscarán todos los términos y cadenas introducidos en este campo. Por ejemplo, al buscar "test segment 1" se devolverán Segments que contengan "test", "segment" o "1" en cualquier parte de su nombre. Para buscar una cadena exacta, pon comillas alrededor de tu término de búsqueda. Al buscar ["test segment 1"] se devolverán todos los Segments que contengan la frase exacta "test segment 1" en su nombre.

![Los resultados de búsqueda al introducir "all users" en el campo de búsqueda incluyen "All Users (Test)", "All Users", "All Users 15".]({% image_buster /assets/img/segment/segments_search.png %})

### Segments en Canvas {#segments-in-canvases}

Para buscar todas las referencias de Segments, incluidas las que se encuentran en otros Segments, Campaigns o Canvas, ve a la sección [Uso en mensajería](#messaging-use) de un Segment. El filtro **Target segment** en la página de **Canvas** busca solo Segments de audiencia de Canvas.

![Filtro de Target segment en la página de Canvas.]({% image_buster /assets/img/segment/target_segment.png %}){: style="max-width:45%;"}

## Solución de problemas {#troubleshooting}

{% multi_lang_include audience/segments.md section='Canvas variant archived segment' %}