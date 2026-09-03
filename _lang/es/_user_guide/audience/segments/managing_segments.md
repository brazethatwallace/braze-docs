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

## Personalizar tu vista {#customizing-your-view}

Adapta tu vista de la lista de segmentos usando filtros y cambiando las columnas que deseas que aparezcan. Cuando salgas de la sección **Segments** y regreses, la lista volverá a la vista predeterminada, eliminando cualquier filtro que hayas seleccionado previamente.

### Filtro de estado {#status-filter}

Puedes reducir la lista para mostrar solo segmentos activos o archivados. Cualquier segmento no archivado se considera activo.

### Filtros {#filters}

Ordena los segmentos de la lista ajustando los siguientes filtros:
- **Last Edited By:** El usuario que editó por última vez los segmentos
- **Last Edited:** Rango de tiempo en el que los segmentos fueron editados por última vez
- **Estimated Size:** Rango aproximado de cuántos usuarios hay en los segmentos
- **Tags:** Etiquetas asociadas con los segmentos
- **Teams:** Equipos asociados con los segmentos
- **Advanced Tracking Segments Only:** Ver solo los segmentos que tienen habilitado el [seguimiento de análisis]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking).

### Columnas {#columns}

Estas son las columnas de información que puedes seleccionar para mostrar en la lista de segmentos:
- **Filters:** Número de filtros en el segmento
- **Last edited:** Fecha en que el segmento fue editado por última vez
- **Last edited by:** El usuario que editó por última vez el segmento
- **Tags:** Etiquetas asociadas con el segmento
- **Teams:** Equipos asociados con el segmento
- **Estimated size:** Número estimado de usuarios en el segmento
- **Canvases:** Número de Canvas que usan el segmento
- **Campaigns:** Número de Campaigns que usan el segmento

### Mostrar solo destacados {#show-starred-only}

Seleccionar **Show Starred Only** reduce tu vista a los segmentos que fueron destacados por ti.

## Ver el uso de mensajería de un segmento {#messaging-use}

Ve a la sección **Messaging Use** de un segmento para obtener un resumen de dónde se está usando el segmento, como dentro de otros segmentos, Campaigns y Canvas.

{% alert note %}
Para evitar bucles de segmentos que se referencian entre sí, los segmentos que usan el filtro **Segment Membership** no pueden ser referenciados por otros segmentos. Para más detalles, consulta [Filtros de segmentación]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).
{% endalert %}

## Administrar segmentos específicos {#managing-specific-segments}

![El menú de edición de un segmento mostrando las opciones "Edit", "Duplicate", "Archive" y "Add to starred".]({% image_buster /assets/img/segment/segments_page_edit_menu.png %}){: style="float:right;max-width:25%;"}

Para administrar un segmento específico, pasa el cursor sobre él y selecciona el icono de menú al final de la fila para revelar las siguientes opciones:
- **Edit:** Edita los filtros de tu segmento.
- **Duplicate:** Haz una copia de tu segmento.
- **Archive:** Archiva el segmento. Ten en cuenta que esto también archivará cualquier Campaign o Canvas que use ese segmento.
- **Add to starred:** Destaca el segmento, lo que te permite acceder rápidamente a él marcando la casilla Show starred only en la sección de segmentos.

También puedes realizar acciones masivas —específicamente archivar en masa y etiquetar en masa— marcando las casillas junto a los nombres de múltiples segmentos.

{% alert tip %}
Si necesitas una exportación legible por máquina de los segmentos existentes en el espacio de trabajo (no solo la vista de tabla actual), usa el [endpoint Exportar lista de segmentos]({{site.baseurl}}/api/endpoints/export/segments/get_segment) y pagina a través de los resultados. Para auditar segmentos archivados, revísalos por separado en el panel de **Segments** usando el filtro de estado.
{% endalert %}

![Múltiples segmentos seleccionados con "CRM" seleccionado en el campo desplegable "Tag As".]({% image_buster /assets/img/segment/segments_bulk_action.png %}){: style="max-width:45%;"}

### Cambios desde la última visualización {#changes-since-last-viewed}

El número de actualizaciones a los segmentos realizadas por otros miembros de tu equipo se rastrea mediante la métrica *Changes Since Last Viewed* en la página de resumen del segmento. Selecciona **Changes Since Last Viewed** para ver un registro de cambios de las actualizaciones al nombre, descripción y público objetivo del segmento. Para cada actualización, puedes ver quién realizó la actualización y cuándo. Puedes usar este registro de cambios para auditar los cambios en tu segmento.

## Buscar segmentos {#searching-for-segments}

Busca nombres de segmentos ingresando términos en el campo de búsqueda.

Se buscarán todos los términos y cadenas ingresados en este campo. Por ejemplo, buscar "test segment 1" devolverá segmentos con "test", "segment" o "1" en cualquier parte de su nombre. Para buscar una cadena exacta, pon comillas alrededor de tu término de búsqueda. Buscar ["test segment 1"] devolverá todos los segmentos que contengan la frase exacta "test segment 1" en su nombre.

![Los resultados de búsqueda al ingresar "all users" en el campo de búsqueda incluyen "All Users (Test)", "All Users", "All Users 15".]({% image_buster /assets/img/segment/segments_search.png %})

### Segmentos en Canvas {#segments-in-canvases}

Para buscar todas las referencias de segmentos, incluidas las que están en otros segmentos, Campaigns o Canvas, ve a la sección [Uso de mensajería](#messaging-use) de un segmento. El filtro **Target segment** en la página de **Canvas** busca solo segmentos de audiencia de Canvas.

![Filtro Target segment en la página de Canvas.]({% image_buster /assets/img/segment/target_segment.png %}){: style="max-width:45%;"}