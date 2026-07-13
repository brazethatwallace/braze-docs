---
nav_title: Segmentación por ubicación
article_title: Segmentación por ubicación
page_order: 7
page_type: tutorial
tool:
- Segments
- Location
description: "Este artículo te guiará sobre cómo configurar la segmentación por ubicación, permitiéndote segmentar usuarios por su ubicación."

---

# Segmentación por ubicación {#location-targeting}

> Este artículo te guiará sobre cómo configurar la segmentación por ubicación, permitiéndote segmentar usuarios por su ubicación más reciente. Esto es perfecto si estás explorando campañas y estrategias basadas en la ubicación.

## Paso 1: Crea tu segmento {#step-1-create-your-segment}

Navega a la página **Segments**, en **Audience**, para ver todos tus segmentos de usuarios actuales. En esta página, puedes crear y nombrar nuevos segmentos. Para empezar, selecciona **Create Segment** y dale un nombre a tu segmento.

![Modal para crear un segmento.]({% image_buster /assets/img_archive/createsegment2.png %}){: style="max-width:70%;"}

## Paso 2: Personaliza tu ubicación {#step-2-customize-your-location}

Después de haber creado tu segmento, añade un filtro de **Most Recent Location** para segmentar usuarios por el último lugar en el que usaron tu aplicación. Tienes la opción de destacar usuarios dentro o fuera de una región circular estándar o una región poligonal personalizable.

![Filtro para una ubicación más reciente dentro de un círculo.]({% image_buster /assets/img_archive/filter_recent_location.png %})

{% tabs %}
{% tab Circular %}

### Regiones circulares {#circular-regions}

Para las regiones circulares, puedes mover el origen y ajustar el radio de ubicación para tu segmentación.

![Un contorno circular de ciudades entre Nueva Jersey y Nueva York.]({% image_buster /assets/img_archive/location_circle.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Poligonal %}

### Regiones poligonales {#polygonal-regions}

Para las regiones poligonales, puedes designar de forma más específica qué áreas deseas incluir en tu segmento.

![Un contorno del estado de Nueva York como la región poligonal seleccionada.]({% image_buster /assets/img_archive/create_polygon.png %}){: style="max-width:70%;"}

{% endtab %}
{% endtabs %}

## Soporte de socios para balizas y geovallas {#partnership-support-for-beacon-and-geofence}

Combinar el soporte existente de balizas o geovallas con nuestras funciones de segmentación y mensajería te proporciona más información sobre las acciones físicas de tus usuarios para que puedas enviarles mensajes en consecuencia. Puedes aprovechar el seguimiento de ubicación con algunos de nuestros socios:

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare)