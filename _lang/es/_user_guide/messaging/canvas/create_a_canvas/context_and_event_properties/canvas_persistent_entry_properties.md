---
nav_title: Propiedades de entrada persistentes
article_title: Propiedades de entrada persistentes
alias: "/persistent_entry/"
page_type: reference
description: "Este artículo de referencia describe cómo utilizar propiedades de entrada persistentes en tu Canvas para enviar mensajes más seleccionados y crear una experiencia de usuario final altamente refinada."
tool: Canvas
page_order: 5
---

# Propiedades de entrada persistentes {#persistent-entry-properties}

> Cuando un Canvas se desencadena mediante un evento personalizado, una compra o una llamada a la API, puedes usar metadatos de la llamada a la API, el evento personalizado o el evento de compra para la personalización en cada paso del flujo de trabajo de tu Canvas. Puedes usar estas propiedades para enviar mensajes más seleccionados.

{% alert important %}
Las propiedades de entrada persistentes son un artefacto del editor original de Canvas, por lo que existen referencias obsoletas a términos como propiedades de entrada de Canvas que permanecen como referencia histórica. Para el editor actual de Canvas, consulta [Propiedades de contexto y propiedades del evento]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/).<br><br>Para usar propiedades de entrada persistentes en el editor actual de Canvas, debes crear un nuevo Canvas o [clonar]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases/) uno existente en el editor actual.
{% endalert %}

## Uso de las propiedades de entrada {#using-entry-properties}

Las propiedades de entrada se pueden usar en Canvas basados en acciones y desencadenados por API. Estas propiedades de entrada se definen cuando un Canvas se desencadena mediante un evento personalizado, una compra o una llamada a la API. Consulta los siguientes artículos para más información:

- [Objeto de propiedades de entrada de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context/)
- [Objeto de propiedades del evento]({{site.baseurl}}/api/objects_filters/event_object/)
- [Objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-product_id)

Las propiedades pasadas desde estos objetos se pueden referenciar usando la etiqueta de Liquid `canvas_entry_properties`. Por ejemplo, una solicitud con `"canvas_entry_properties": {"product_name": "shoes", "product_price": 79.99}` podría añadir la palabra "shoes" a un mensaje agregando el Liquid {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}.

Cuando un Canvas incluye un mensaje con la etiqueta de Liquid `canvas_entry_properties`, los valores asociados con esas propiedades se guardarán durante toda la trayectoria del usuario en el Canvas y se eliminarán cuando el usuario salga del Canvas. Ten en cuenta que las propiedades de entrada de Canvas solo están disponibles para referencia en Liquid. Para filtrar por las propiedades dentro del Canvas, usa la [segmentación por propiedades del evento]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects/) en su lugar.

{% alert note %}
El objeto de propiedades de entrada de Canvas tiene un límite máximo de tamaño de 50 KB.
{% endalert %}

## Actualización de Canvas para usar propiedades de entrada {#updating-canvas-to-use-entry-properties}

Si un Canvas activo que anteriormente no incluía ningún mensaje que use `canvas_entry_properties` se edita para incluir `canvas_entry_properties`, el valor correspondiente a esa propiedad no estará disponible para los usuarios que entraron al Canvas antes de que se añadiera `canvas_entry_properties` al Canvas. Los valores solo se guardarán para los usuarios que entren al Canvas después de que se realice el cambio.

Por ejemplo, si inicialmente lanzaste un Canvas que no usaba ninguna propiedad de entrada el 3 de noviembre, y luego añadiste una nueva propiedad `product_name` al Canvas el 11 de noviembre, los valores de `product_name` solo se guardarían para los usuarios que entraron al Canvas a partir del 11 de noviembre.

En el caso de que una propiedad de entrada de Canvas sea nula o esté en blanco, puedes cancelar mensajes usando condicionales. El siguiente fragmento de código es un ejemplo de cómo podrías usar Liquid para cancelar un mensaje.
{%raw%}
```
{% if canvas_entry_properties.${product_name} == blank %}
{% abort_message() %}
{% endif %}
```
{%endraw%}

Para leer más sobre la cancelación de mensajes con Liquid, consulta nuestra [documentación de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/#abort-messages).

## Propiedades de entrada globales de Canvas {#global-canvas-entry-properties}

Con `canvas_entry_properties`, puedes establecer propiedades globales que se aplican a todos los usuarios o propiedades específicas del usuario que solo se aplican al usuario especificado. La propiedad específica del usuario sustituirá a la propiedad global para ese usuario.

### Ejemplo de solicitud {#example-request}

```bash
curl -X POST \
-H 'Content-Type: application/json' \
-d '{
      "api_key": "a valid rest api key",
      "canvas_id": "the ID of your Canvas",
      "canvas_entry_properties": {
        "food_allergies": "none"
      },
      "recipients": [
        {
          "external_user_id": "Customer_123",
          "canvas_entry_properties": {
            "food_allergies": ["dairy", "soy"],
            "nutrition": {
              "calories_per_serving": 200,
              "serving_size_in_ounces": 4
            }
          }
        }
      ]
    }'
```

En esta solicitud, el valor global para "food allergies" es "none". Para Customer_123, el valor es "dairy". Los mensajes en este Canvas que contengan el fragmento de Liquid {%raw%}`{{canvas_entry_properties.${food_allergies}}}`{%endraw%} se renderizarán con "dairy" para Customer_123 y "none" para el resto.

## Caso de uso {#use-case}

Si tienes un Canvas que se desencadena cuando un usuario navega por un artículo en tu sitio de comercio electrónico pero no lo añade a su carrito, el primer paso del Canvas podría ser una notificación push preguntándole si está interesado en comprar el artículo. Podrías referenciar el nombre del producto usando {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}

![]({% image_buster /assets/img/persistent_entry_properties/PEP1.png %}){: style="border:0;margin-left:15px;"}

El segundo paso puede enviar otra notificación push invitando al usuario a finalizar la compra si añadió el artículo a su carrito pero aún no lo ha comprado. Puedes seguir referenciando la propiedad de entrada `product_name` usando {% raw %}`{{canvas_entry_properties.${product_name}}}`{% endraw %}.

![]({% image_buster /assets/img/persistent_entry_properties/PEP12.png %}){: style="border:0;margin-left:15px;"}