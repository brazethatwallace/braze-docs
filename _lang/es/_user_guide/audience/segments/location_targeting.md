---
nav_title: Segmentación por ubicación
article_title: Segmentación por ubicación
page_order: 7
page_type: tutorial
tool:
- Segments
- Location
description: "Este artículo te explicará cómo configurar la segmentación por ubicación, lo que te permite segmentar usuarios por su ubicación."

---

# Segmentación por ubicación {#location-targeting}

> Este artículo explica cómo configurar la segmentación por ubicación para que puedas segmentar usuarios según su ubicación más reciente.

## Paso 1: Crea tu segment {#step-1-create-your-segment}

Navega a la página **Segments**, en **Audiencia**, para ver todos tus segments de usuarios actuales. En esta página, puedes crear y nombrar nuevos segments. Para comenzar, selecciona **Create Segment** y dale un nombre a tu segment.

![Modal para crear un segment.]({% image_buster /assets/img_archive/createsegment2.png %}){: style="max-width:70%;"}

## Paso 2: Personaliza tu ubicación {#step-2-customize-your-location}

Después de crear tu Segment, añade un filtro `Most Recent Location` para destacar a los usuarios según el último lugar donde usaron tu aplicación. Tienes la opción de destacar usuarios dentro o fuera de una región circular estándar o una región poligonal personalizable.

![Filtro para una ubicación más reciente dentro de un círculo.]({% image_buster /assets/img_archive/filter_recent_location.png %})

### Usuarios sin datos de ubicación {#users-without-location-data}

Los usuarios sin datos de ubicación —incluidos los usuarios cuya ubicación se registró previamente y luego se borró— coinciden con los filtros de `most recent location outside of circle` y `most recent location outside of polygon`. Para excluir a los usuarios sin datos de ubicación, combina el filtro `Most Recent Location` con un filtro `Location Available`.

{% tabs %}
{% tab Circular %}

### Regiones circulares {#circular-regions}

Para las regiones circulares, puedes mover el origen y ajustar el radio de ubicación para tu segmentación.

![Un contorno circular de ciudades entre Nueva Jersey y Nueva York.]({% image_buster /assets/img_archive/location_circle.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Poligonal %}

### Regiones poligonales {#polygonal-regions}

Para las regiones poligonales, puedes designar de forma más específica qué áreas deseas incluir en tu Segment.

![Un contorno del estado de Nueva York como la región poligonal seleccionada.]({% image_buster /assets/img_archive/create_polygon.png %}){: style="max-width:70%;"}

{% endtab %}
{% endtabs %}

## Soporte de partners para balizas y geovallas {#partnership-support-for-beacon-and-geofence}

Combinar el soporte existente de balizas o geovallas con nuestras características de segmentación y mensajería te brinda más información sobre las acciones físicas de tus usuarios para que puedas enviarles mensajes en consecuencia. Puedes aprovechar el seguimiento de ubicación con algunos de nuestros partners:

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare)