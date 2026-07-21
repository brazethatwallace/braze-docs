---
nav_title: Propiedades de contexto y de evento
article_title: Propiedades de contexto y de evento
page_order: 4.2
page_type: reference
description: "Este artículo de referencia describe las diferencias entre las propiedades de contexto y las propiedades de evento, y cuándo utilizar cada una."
tool: Canvas
---

# Propiedades de contexto y de evento {#context-and-event-properties}

> Este artículo de referencia cubre información sobre `context` y `event_properties`, incluyendo cuándo usar cada propiedad y las diferencias en su comportamiento. <br><br> Para información sobre las propiedades de eventos personalizados en general, consulta [Propiedades de eventos personalizados]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties).

{% multi_lang_include alerts/important_alerts.md alert='context variable' %}

Las propiedades de contexto y las propiedades de evento funcionan de manera diferente dentro de tus flujos de trabajo de Canvas. Las propiedades de eventos o llamadas a la API que desencadenan la entrada de un usuario en un Canvas se conocen como `context`. Las propiedades de eventos que ocurren mientras un usuario avanza dentro de un recorrido en Canvas se conocen como `event_properties`. La diferencia clave es que `context` se enfoca en más que solo eventos, ya que también accede a las propiedades de las cargas útiles de entrada en Canvas activados por API.

Consulta la siguiente tabla para un resumen de las diferencias entre las propiedades de contexto y las propiedades de evento.

| | Propiedades de contexto | Propiedades de evento |
|----|----|----|
| **Liquid** | `context` | `event_properties` |
| **Persistencia** | Pueden ser referenciadas por todos los pasos de [Mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) durante toda la duración de un Canvas construido usando Canvas. | - Solo pueden ser referenciadas una vez. <br> - No pueden ser referenciadas por pasos de Mensaje posteriores. |
| **Comportamiento en Canvas** | Puedes referenciar `context` en cualquier paso de un Canvas. Para el comportamiento posterior al lanzamiento, consulta [Editar Canvas después del lanzamiento]({{site.baseurl}}/post-launch_edits#canvas-entry-properties). | - Puedes referenciar `event_properties` en el primer paso de Mensaje **después** de un paso de [Rutas de Acción]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) donde la acción realizada es un evento personalizado o un evento de compra. <br> - No puede estar después de la ruta El resto del paso de Rutas de Acción. <br> - Puede haber otros componentes que no sean de Mensaje entre los pasos de Rutas de Acción y Mensaje. Si uno de estos componentes que no son de Mensaje es un paso de Rutas de Acción, el usuario puede pasar por la ruta El resto de esa ruta de acción. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Propiedades de contexto y de evento" }

{% details Detalles del editor de Canvas original %}

Ya no puedes crear ni duplicar Canvas usando el editor original. Ten en cuenta que el contexto de Canvas no es compatible con el editor de Canvas original, por lo que esta sección está disponible como referencia al usar propiedades de entrada de Canvas y propiedades de evento para el flujo de trabajo de Canvas anterior.

**Propiedades de entrada de Canvas:**
- Deben tener activadas las propiedades de entrada persistentes.
- Solo pueden referenciar `canvas_entry_properties` en el primer paso completo de un Canvas. El Canvas debe ser basado en acciones o activado por API.

**Propiedades de entrada:**
- Pueden referenciar `event_properties` en cualquier paso completo que use entrega basada en acciones en un Canvas.
- No pueden usarse en pasos completos planificados que no sean el primer paso completo de un Canvas basado en acciones. Sin embargo, si un usuario está usando un [componente de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/about), el comportamiento sigue las reglas actuales del flujo de trabajo de Canvas para `event_properties`.

**Propiedades de evento:**
- No se puede usar `event_properties` en el paso de Mensaje principal. En su lugar, debes usar `canvas_entry_properties` o añadir un paso de Rutas de Acción con el evento correspondiente **antes** del paso de Mensaje que incluye `event_properties`.

{% enddetails %}

## Cosas que debes saber {#things-to-know}

- El contexto solo está disponible para referencia en Liquid. Para filtrar por las propiedades dentro del Canvas, usa la [segmentación por propiedades de evento]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects) en su lugar.
- Para canales de mensajes dentro de la aplicación, puedes referenciar `context` y `event_properties` en un Canvas. Se puede acceder a `event_properties` cuando se incluyen en el primer paso del Canvas porque está basado en desencadenantes.
- No puedes usar `event_properties` en el paso de Mensaje principal. En su lugar, puedes usar `context` o añadir un paso de Rutas de Acción con el evento correspondiente **antes** del paso de Mensaje que incluye `event_properties`.
- Cuando un paso de Rutas de Acción contiene un desencadenante "Envió un mensaje SMS de entrada" o "Envió un mensaje WhatsApp de entrada", los pasos posteriores del Canvas pueden incluir una propiedad Liquid de SMS o WhatsApp. Esto refleja cómo funcionan las propiedades de evento en Canvas. De esta manera puedes aprovechar tus mensajes para guardar y referenciar datos propios en perfiles de usuario y mensajería conversacional.

{% alert note %}
La elegibilidad de la audiencia se evalúa una vez en la entrada al Canvas. Si un usuario se fusiona durante la entrada, el usuario identificado continúa a través del Canvas y no se vuelve a evaluar contra los criterios de segmentación del Canvas.
{% endalert %}

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### Marcas de tiempo para desencadenantes {#timestamps-for-triggers}

Si estás usando marcas de tiempo con un [tipo datetime]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties) de eventos que desencadenan Canvas basados en acciones, que se referencian usando [contexto]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties), las marcas de tiempo se normalizan a UTC.

Dado este comportamiento, Braze recomienda encarecidamente que uses un filtro de zona horaria de Liquid como el siguiente ejemplo para garantizar que tus mensajes se envíen con tu [zona horaria preferida]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters).

{% raw %}
```liquid
{{context.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%H:%M" }}
```
{% endraw %}

## Caso de uso {#use-case}

![Un paso de Rutas de Acción seguido de un paso de Retraso y un paso de Mensaje para usuarios que han añadido un artículo a su lista de deseos, y una ruta para el resto.]({% image_buster /assets/img_archive/canvas_entry_properties1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Para comprender mejor las diferencias entre `context` y `event_properties`, consideremos este escenario donde los usuarios entran en un Canvas basado en acciones si realizan el evento personalizado "añadir artículo a la lista de deseos".

El contexto se configura en el paso de [Horario de entrada]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-12-determine-your-canvas-entry-schedule) al crear un Canvas y corresponde al momento en que un usuario entra en un Canvas. El contexto también puede ser referenciado en cualquier paso de Mensaje.

En este Canvas, tenemos un recorrido de usuario que comienza con un paso de Rutas de Acción para determinar si un usuario ha añadido un artículo a su lista de deseos. Desde aquí, si el usuario ha añadido un artículo, experimenta un retraso antes de recibir el mensaje "¡Nuevo artículo en tu lista de deseos!" del paso de Mensaje.

El primer paso de Mensaje en un recorrido de usuario tiene acceso a las `event_properties` personalizadas de tu paso de Rutas de Acción. En este caso, podemos incluir ``{% raw %} {{event_properties.${property_name}}} {% endraw %}`` en este paso de Mensaje como parte del contenido de nuestro mensaje. Si un usuario no añade un artículo a su lista de deseos, pasa por la ruta El resto, lo que significa que no se pueden referenciar las `event_properties` y se muestra un error de configuración no válida.

Ten en cuenta que solo tendrás acceso a `event_properties` si tu paso de Mensaje puede rastrearse hasta una ruta que no sea El resto en un paso de Rutas de Acción. Si el paso de Mensaje está conectado a una ruta El resto pero puede rastrearse hasta un paso de Rutas de Acción en el recorrido del usuario, entonces también tienes acceso a `event_properties`. Para más información sobre estos comportamientos, consulta [Paso de mensaje]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step).