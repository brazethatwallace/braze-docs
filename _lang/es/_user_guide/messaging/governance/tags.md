---
nav_title: Etiquetas
article_title: Etiquetas
page_order: 6
page_type: reference
description: "Este artículo de referencia cubre las etiquetas para Campaigns, Canvas, Segments y datos personalizados en el panel de Braze."
tool:
  - Campaigns
  - Canvas
---

# Etiquetas {#tags}

> Braze rastrea información sobre el autor, editor, fecha y estado de Segments, Campaigns y Canvas, y te da la posibilidad de crear etiquetas para organizar y ordenar aún más tu participación.

## Etiquetas de Campaign, Canvas y Segment {#campaign-canvas-and-segment-tags}

Puedes añadir etiquetas al crear o editar una Campaign, un Canvas o un Segment. Haz clic en <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tags** debajo del nombre de la participación y selecciona una etiqueta existente, o empieza a escribir para añadir una nueva etiqueta.

![Añadiendo etiquetas durante la creación de una Campaign.]({% image_buster /assets/img_archive/tags_add_tag.png %}){: style="max-width:60%;" }

{% alert important %}
Puedes añadir hasta 175 etiquetas a una Campaign, un Canvas o un Segment.
{% endalert %}

### Etiquetado masivo {#bulk-tagging}

También puedes añadir etiquetas a múltiples Campaigns, Canvas o Segments seleccionando varias participaciones y haciendo clic en <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-tag" ></span>**Tag As**.

![Añadiendo etiquetas a múltiples Campaigns al mismo tiempo.]({% image_buster /assets/img_archive/tags_apply_multiple.gif %})

{% alert important %}
Cuando usas el etiquetado masivo para aplicar una nueva etiqueta a múltiples Campaigns que ya tienen etiquetas diferentes, cada Campaign seleccionada recibe la nueva etiqueta, y cualquier etiqueta presente en una Campaign se aplica a todas las demás Campaigns seleccionadas, incluso si esas etiquetas no estaban originalmente asociadas a ellas.
{% endalert %}

### Ver etiquetas {#viewing-tags}

Las etiquetas asignadas a una Campaign, un Canvas o un Segment son visibles en la página de detalles cerca del nombre de la participación. También aparecen en los análisis de Campaign.

![Etiquetas mostradas en la página de análisis de Campaign.]({% image_buster /assets/img_archive/tag_details_page.png %}){: style="max-width:60%;" }

### Filtrar por etiqueta {#filtering-by-tag}

Las etiquetas son visibles en la lista de Campaigns, Canvas o Segments, junto con etiquetas adicionales para indicadores de estado como **Archived** y **Draft**. Para filtrar por una etiqueta, selecciona el nombre de la etiqueta de la lista de etiquetas.

![Etiquetas en la lista de Campaigns.]({% image_buster /assets/img_archive/tags_grid.png %})

## Etiquetas de datos personalizados {#custom-data-tags}

También se pueden añadir etiquetas a los datos personalizados al gestionar [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#managing-custom-attributes) y [eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events#adding-tags).

{% alert important %}
Esta característica se encuentra actualmente en acceso anticipado. Ponte en contacto con tu administrador de éxito de cliente si te interesa participar en este acceso anticipado.
{% endalert %}

Para obtener información sobre cómo renombrar, quitar o anidar etiquetas en tu panel, consulta [Gestión de etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags).