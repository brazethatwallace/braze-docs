---
nav_title: Propiedades de eventos personalizados
article_title: Propiedades de eventos personalizados
page_order: 0
page_type: reference
description: "Este artículo describe las propiedades de eventos personalizados, su formato esperado, cómo utilizarlas y el almacenamiento de propiedades de eventos personalizados."
---

# Propiedades de eventos personalizados {#custom-event-properties}

> Este artículo describe las propiedades de eventos personalizados, su formato esperado, cómo utilizarlas para mensajería y segmentación, y el almacenamiento de propiedades de eventos personalizados.

Las propiedades de eventos personalizados son metadatos o atributos de eventos personalizados que describen una ocurrencia específica de un evento. Estas propiedades pueden utilizarse para cualificar aún más las condiciones de desencadenamiento, aumentar la personalización en la mensajería, hacer seguimiento de conversiones y generar análisis más sofisticados a través de la exportación de datos en bruto.

Las propiedades de eventos personalizados no se almacenan en el perfil de Braze y, por lo tanto, no registran puntos de datos (consulta [Puntos de datos](#data-points) para conocer las excepciones).

## Ver los valores de las propiedades del evento para un usuario {#viewing-event-property-values-for-a-user}

Para ver el valor de una propiedad de evento personalizado para un usuario específico, las siguientes opciones están disponibles según tu configuración:

- **Currents:** Si los eventos de comportamiento del cliente están habilitados, las propiedades del evento se incluyen en la exportación de Currents.
- **Registro de usuarios del evento:** Si el usuario es un usuario de prueba y realizó el evento recientemente, el evento y sus propiedades aparecerán en **Configuración** > **Registro de usuarios del evento**.
- **Segmentación:** Si el almacenamiento de propiedades de eventos personalizados está habilitado para esa propiedad, puedes crear un segmento utilizando el filtro de propiedades del evento para comprobar si el usuario cumple los requisitos.

{% alert important %}
Cada evento personalizado o compra puede tener hasta 256 propiedades de evento personalizado distintas. Si un evento personalizado o una compra se registra con más de 256 propiedades, solo se capturarán las primeras 256 y estarán disponibles para su uso.
{% endalert %}

## Formato esperado {#expected-format}

Los valores de las propiedades deben ser un objeto: las claves son los nombres de las propiedades (cadenas no vacías, de 255 caracteres o menos, sin `$` inicial), y los valores son los valores de las propiedades. Para los tipos de datos compatibles, los requisitos de formato y los límites de carga útil, consulta [Tipos de datos]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#event-property-data-types).

Puedes cambiar el tipo de datos de tu propiedad de evento personalizado, pero ten en cuenta los impactos de [cambiar los tipos de datos]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#changing-custom-attribute-or-event-data-type) después de que se hayan recopilado los datos.

### Claves reservadas {#reserved-keys}

No puedes usar claves reservadas como nombres de propiedades de eventos. Usar una clave reservada en el objeto `properties` devuelve el error "Invalid 'properties' field".

| Propiedad | Clave reservada |
| --- | --- |
| Eventos personalizados | `time` y `event_name` |
| Eventos de compra | `time`, `product_id`, `quantity`, `event_name`, `price`, `currency` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Claves reservadas" }

## Uso de propiedades de eventos personalizados {#using-custom-event-properties}

Las propiedades de eventos personalizados se pueden utilizar para calificar desencadenantes de Campaigns, realizar seguimiento de conversiones y personalizar la mensajería.

### Desencadenar mensajes {#trigger-messages}

Usa las propiedades de eventos personalizados para acotar aún más tu audiencia para una Campaign o Canvas en particular. Por ejemplo, si tienes una aplicación de comercio electrónico y quieres enviar un mensaje a un usuario cuando abandona su carrito, puedes añadir una propiedad de evento personalizado de `price` para mejorar tu público objetivo y permitir una mayor personalización de la Campaign.

![Filtros de propiedades de eventos personalizados para un carrito abandonado. Dos filtros se combinan con un operador AND para enviar esta Campaign a usuarios que abandonaron su carrito con un precio entre 100 y 200 dólares]({% image_buster /assets/img_archive/customEventProperties.png %} "customEventProperties.png"){: style="max-width:70%;"}

Las propiedades de eventos personalizados anidadas también son compatibles con la [entrega basada en acciones]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery).

![Filtros de propiedades de eventos personalizados para un carrito abandonado. Se selecciona un filtro si algún artículo del carrito tiene un precio superior a 100 dólares.]({% image_buster /assets/img_archive/customEventPropertiesNested.png %} "customEventPropertiesNested.png"){: style="max-width:70%;"}

### Personalizar mensajes {#personalize-messages}

También puedes usar las propiedades de eventos personalizados para la personalización dentro de la plantilla de mensajería. Cualquier Campaign que utilice [entrega basada en acciones]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery) con un evento desencadenante puede usar las propiedades de eventos personalizados de ese evento para la personalización de la mensajería.

#### Consideraciones con los filtros {#considerations-with-filters}

- **Llamadas a la API:** Al realizar llamadas a la API y usar el filtro "está en blanco", una propiedad de evento personalizado se considera "en blanco" si se excluye de la llamada. Por ejemplo, si incluyes `"event_property": ""`, tus usuarios se consideran "no en blanco".
- **Enteros:** Al filtrar por una propiedad de evento personalizado numérica y el número es muy grande, no uses el filtro "exactamente". Si un número es demasiado grande, puede redondearse a cierta longitud, por lo que tu filtro no funcionará como se espera.

#### Coerción de tipos para comparaciones {#type-coercion-for-comparisons}

Al usar propiedades de eventos en sentencias condicionales de Liquid, puedes encontrar el error `Liquid error: comparison of String with 0 failed` si estás comparando una propiedad de evento de tipo entero usando operadores como mayor que, menor que o igual a. Esto ocurre porque Liquid trata la propiedad como una cadena de forma predeterminada.

Para solucionarlo, usa el filtro `plus: 0` para convertir la propiedad a un número antes de la comparación:

{% raw %}
```liquid
{% assign time_spent = {{event_properties.${time_spent}}} | plus: 0 %}
{% if time_spent >= 100 %}
  Great job completing the level quickly!
{% endif %}
```
{% endraw %}

Por ejemplo, si tienes una aplicación de juegos y quieres enviar un mensaje a los usuarios que completaron un nivel, podrías personalizar aún más tu mensaje con una propiedad para el tiempo que les tomó a los usuarios completar ese nivel.

El siguiente mensaje está personalizado para tres segmentos diferentes usando [lógica condicional]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic). La propiedad de evento personalizado llamada `time_spent` se puede incluir en el mensaje llamando a ``{% raw %} {{event_properties.${time_spent}}} {% endraw %}``.

{% raw %}
```liquid
{% assign time_spent = {{event_properties.${time_spent}}} | plus: 0 %}
{% if time_spent < 600 %}
Incredible work, hero! Are you ready to test your skills against other powerful heroes? Visit the Arena for real-time battles with top players from around the globe.
{% elsif time_spent < 1800 %}
Great job, hero! Don't forget to visit the town store between levels to upgrade your tools.
{% else %}
Well done, hero! Talk to villagers for tips on how to beat levels faster and unlock more rewards.
{% endif %}
```
{% endraw %}

{% alert warning %}
Si el usuario no tiene conexión a internet, los mensajes dentro de la aplicación desencadenados con propiedades de eventos personalizados con plantilla (por ejemplo, {% raw %}``{{event_properties.${time_spent}}}``{% endraw %}) fallan y no se muestran.
{% endalert %}

Para obtener una lista completa de las etiquetas de Liquid que hacen que los mensajes dentro de la aplicación se entreguen como mensajes dentro de la aplicación con plantilla, consulta [Preguntas frecuentes]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages).

#### Canvas {#canvas}

En Canvas, `context` y `event_properties` tienen propósitos diferentes:

- **`context`**: Propiedades del evento o la llamada a la API que desencadenó la entrada al Canvas. Usa `context` en cualquier paso de mensaje, incluido el primero.
- **`event_properties`**: Propiedades de un evento personalizado o compra que ocurre durante el recorrido. Úsalas solo en el primer paso de mensaje después de un paso de [Rutas de Acción]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths), no en la ruta de Todos los demás ni en pasos de mensaje posteriores.

{% alert important %}
En el primer paso de mensaje de un Canvas, usa `context` en lugar de `event_properties`, o añade un paso de Rutas de Acción antes del paso de mensaje. Excepción: para mensajes dentro de la aplicación, puedes usar `event_properties` en el primer paso de mensaje cuando ese evento es el desencadenante de entrada al Canvas.
{% endalert %}

Para más información, consulta [Contexto y propiedades de eventos]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) y [Propiedades de entrada de Canvas y propiedades de eventos](#canvas-entry-properties-and-event-properties).

### Segmentación {#segmentation}

Usa la segmentación por propiedades de eventos para segmentar usuarios en función de los eventos personalizados realizados y las propiedades asociadas a esos eventos. Esto aumenta tus opciones de filtrado al segmentar por compras y eventos personalizados.

Las propiedades de eventos para eventos personalizados se actualizan en tiempo real para cualquier Segment que las utilice. Puedes gestionar las propiedades yendo a **Configuración de datos** > **Eventos personalizados** y seleccionando **Gestionar propiedades** para el evento personalizado asociado. Las propiedades de eventos personalizados utilizadas en ciertos filtros de Segment tienen un historial máximo de retrospectiva de 30 días.

#### Añadir propiedades de eventos para segmentación {#adding-event-properties-for-segmentation}

Necesitas el [permiso de usuario]({{site.baseurl}}/user_guide/data/infrastructure/data_points#viewing-data-point-usage) "Edit Custom Event Property Segmentation" para crear Segments basados en la frecuencia y la antigüedad de las propiedades de eventos.

De forma predeterminada, puedes tener 20 propiedades de eventos segmentables por espacio de trabajo. Contacta a tu director de cuentas de Braze para aumentar este límite.

Para añadir propiedades de eventos para segmentación, haz lo siguiente:

1. Ve a tu evento personalizado y selecciona **Gestionar propiedades**.
2. Selecciona el conmutador **Habilitar segmentación** para añadir la propiedad de evento para segmentación. Puedes acceder a opciones de filtrado adicionales al segmentar.

Los filtros de segmentación por propiedades de eventos incluyen:

{% multi_lang_include data_activation/custom_event_property_filters.md %}

![Un grupo de filtros que tiene "Carrito abandonado" con la propiedad "número de artículos" y valor 2 más de 1 vez en los últimos 30 días calendario.]({% image_buster /assets/img/nested_object3.png %})

Los datos solo se registran para una propiedad de evento determinada después de habilitarla, y las propiedades de eventos están disponibles solo a partir de esa fecha en adelante.

#### Puntos de datos {#data-points}

En lo que respecta al uso de la suscripción, las propiedades de eventos personalizados habilitadas para segmentación con los siguientes filtros se cuentan como puntos de datos separados, además del punto de datos contado por el propio evento personalizado:

- `X Custom Event Property in Y Days`
- `X Purchase Property in Y Days`

### Propiedades de entrada de Canvas y propiedades de eventos {#canvas-entry-properties-and-event-properties}

{% multi_lang_include canvas/entry_event_properties.md %}

### Objetos anidados {#nested-objects}

Puedes usar objetos anidados (objetos dentro de otro objeto) para enviar datos JSON anidados como propiedades de eventos personalizados y compras. Estos datos anidados se pueden utilizar para crear plantillas de información personalizada en mensajes, desencadenar envíos de mensajes y segmentar usuarios.

Para obtener más información, consulta nuestra página dedicada sobre [Objetos anidados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects).

## Almacenamiento de propiedades de eventos personalizados {#custom-event-property-storage}

Las propiedades de eventos personalizados están diseñadas para ayudarte a aumentar la precisión de la segmentación y hacer que los mensajes se sientan aún más personalizados. Las propiedades de eventos personalizados se pueden almacenar en Braze tanto a corto como a largo plazo.

Puedes segmentar en función de los valores de las propiedades de eventos de dos maneras:

1. **En los últimos 30 días:** Puedes usar la segmentación por propiedades de eventos basada en la frecuencia y la antigüedad de valores específicos de propiedades de eventos dentro de Braze Segments. Esta opción afecta al uso de datos.<br><br>
2. **Dentro y más allá de 30 días:** Para cubrir tanto la segmentación por propiedades de eventos a corto como a largo plazo, puedes usar las [extensiones de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension). Esta característica segmenta a los usuarios en función de eventos personalizados y propiedades de eventos registrados en los últimos dos años. Esta opción no afecta al uso de datos.

Ponte en contacto con tu administrador de éxito de cliente de Braze para obtener recomendaciones sobre el mejor enfoque en función de tus necesidades específicas.