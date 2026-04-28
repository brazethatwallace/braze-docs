---
nav_title: Administrar Segments
article_title: Administrar Segments
page_order: 2
page_type: tutorial
tool: Segments
description: "Este artículo cubre las acciones que puedes realizar para administrar tus Segments, como filtrar una lista de Segments, crear Segments y editar Segments."

---

# Administrar Segments {#manage-segments}

> La sección Segments te permite ver una lista completa de tus Segments existentes, crear nuevos Segments y editar los existentes. Puedes refinar la lista de Segments seleccionando una variedad de filtros y columnas para que solo se muestre la información más relevante para ti.

![La sección Segments mostrando una lista de Segments activos.]({% image_buster /assets/img/segment/segments_page.png %})

## Personalizar tu vista {#customizing-your-view}

Adapta tu vista de la lista de Segments usando filtros y cambiando las columnas que deseas que aparezcan. Cuando salgas de la sección **Segments** y regreses, la lista volverá a la vista predeterminada, eliminando cualquier filtro que hayas seleccionado previamente.

### Filtro de estado {#status-filter}

Puedes reducir la lista para mostrar solo Segments activos o archivados. Cualquier Segment no archivado se considera activo.

### Filtros {#filters}

Ordena los Segments de la lista ajustando los siguientes filtros:
- **Last Edited By:** El usuario que editó por última vez los Segments
- **Last Edited:** Rango de tiempo en el que los Segments fueron editados por última vez
- **Estimated Size:** Rango aproximado de cuántos usuarios hay en los Segments
- **Tags:** Etiquetas asociadas con los Segments
- **Teams:** Equipos asociados con los Segments
- **Advanced Tracking Segments Only:** Ver solo los Segments que tienen habilitado el [seguimiento de análisis]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/#segment-analytics-tracking).

### Columnas {#columns}

Estas son las columnas de información que puedes seleccionar para mostrar en la lista de Segments:
- **Filters:** Número de filtros en el Segment
- **Last edited:** Fecha en que el Segment fue editado por última vez
- **Last edited by:** El usuario que editó por última vez el Segment
- **Tags:** Etiquetas asociadas con el Segment
- **Teams:** Equipos asociados con el Segment
- **Estimated size:** Número estimado de usuarios en el Segment
- **Canvases:** Número de Canvas que usan el Segment
- **Campaigns:** Número de Campaigns que usan el Segment

### Mostrar solo destacados {#show-starred-only}

Seleccionar **Show Starred Only** reduce tu vista a los Segments que fueron destacados por ti.

## Ver el uso de mensajería de un Segment {#messaging-use}

Ve a la sección **Messaging Use** de un Segment para obtener un resumen de dónde se está usando el Segment, como dentro de otros Segments, Campaigns y Canvas.

{% alert note %}
Para evitar bucles de Segments que se referencian entre sí, los Segments que usan el filtro **Segment Membership** no pueden ser referenciados por otros Segments. Para más detalles, consulta [Filtros de segmentación]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/).
{% endalert %}

## Administrar Segments específicos {#managing-specific-segments}

![El menú de edición de un Segment mostrando las opciones "Edit", "Duplicate", "Archive" y "Add to starred".]({% image_buster /assets/img/segment/segments_page_edit_menu.png %}){: style="float:right;max-width:25%;"}

Para administrar un Segment específico, pasa el cursor sobre él y selecciona el icono de menú al final de la fila para revelar las siguientes opciones:
- **Edit:** Edita los filtros de tu Segment.
- **Duplicate:** Haz una copia de tu Segment.
- **Archive:** Archiva el Segment. Ten en cuenta que esto también archivará cualquier Campaign o Canvas que use ese Segment.
- **Add to starred:** Destaca el Segment, lo que te permite acceder rápidamente a él marcando la casilla Show starred only en la sección de Segments.

También puedes realizar acciones masivas —específicamente archivar en masa y etiquetar en masa— marcando las casillas junto a los nombres de múltiples Segments.

![Múltiples Segments seleccionados con "CRM" seleccionado en el campo desplegable "Tag As".]({% image_buster /assets/img/segment/segments_bulk_action.png %}){: style="max-width:45%;"}

### Cambios desde la última visualización {#changes-since-last-viewed}

El número de actualizaciones a los Segments realizadas por otros miembros de tu equipo se rastrea mediante la métrica *Changes Since Last Viewed* en la página de resumen del Segment. Selecciona **Changes Since Last Viewed** para ver un registro de cambios de las actualizaciones al nombre, descripción y audiencia objetivo del Segment. Para cada actualización, puedes ver quién realizó la actualización y cuándo. Puedes usar este registro de cambios para auditar los cambios en tu Segment.

## Buscar Segments {#searching-for-segments}

Busca nombres de Segments ingresando términos en el campo de búsqueda.

Se buscarán todos los términos y cadenas ingresados en este campo. Por ejemplo, buscar "test segment 1" devolverá Segments con "test", "segment" o "1" en cualquier parte de su nombre. Para buscar una cadena exacta, pon comillas alrededor de tu término de búsqueda. Buscar ["test segment 1"] devolverá todos los Segments que contengan la frase exacta "test segment 1" en su nombre.

![Los resultados de búsqueda al ingresar "all users" en el campo de búsqueda incluyen "All Users (Test)", "All Users", "All Users 15".]({% image_buster /assets/img/segment/segments_search.png %})

### Segments en Canvas {#segments-in-canvases}

Para buscar todas las referencias de Segments, incluidas las que están en otros Segments, Campaigns o Canvas, ve a la sección [Uso de mensajería](#messaging-use) de un Segment. El filtro **Target segment** en la página de **Canvas** busca solo Segments de audiencia de Canvas.

![Filtro Target segment en la página de Canvas.]({% image_buster /assets/img/segment/target_segment.png %}){: style="max-width:45%;"}