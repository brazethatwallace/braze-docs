---
nav_title: Propiedades de entrada de Canvas
article_title: Propiedades de entrada de Canvas
page_order: 4
description: "Aprende a usar las propiedades de entrada de Canvas como fuente de personalización en tus mensajes."
---

# Propiedades de entrada de Canvas

> Cuando un Canvas se desencadena por un evento personalizado, una compra o una llamada a la API, puedes usar los metadatos de ese desencadenador para personalizar los mensajes a lo largo del flujo de trabajo del Canvas. Estos valores se conocen como propiedades de entrada y persisten en todos los pasos de un Canvas.

## Cómo funciona

{% raw %}
Las propiedades de entrada están disponibles a través de la etiqueta de Liquid `{{context.${property_name}}}`. Cuando un usuario entra en un Canvas, Braze captura las propiedades del evento desencadenador o de la llamada a la API, y puedes hacer referencia a ellas en cualquier paso posterior del Canvas.

Por ejemplo, si un Canvas se desencadena por un evento `completed_order` con una propiedad `product_name`:

```liquid
Thanks for ordering {{context.${product_name}}}! We'll send you a tracking number soon.
```
{% endraw %}

Las propiedades de entrada están disponibles en Canvas basados en acciones y desencadenados por API.

## Propiedades de entrada persistentes

Las propiedades de entrada persistentes te permiten hacer referencia a los datos de entrada originales en cada paso de tu Canvas, incluidos los pasos que ocurren después de un retraso. Sin persistencia, las propiedades de entrada solo están disponibles en el primer paso.

{% alert important %}
Las propiedades de entrada persistentes forman parte del flujo de trabajo original de propiedades de entrada de Canvas. Para el editor de Canvas actualizado actual, consulta [Propiedades de contexto y evento]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/).
{% endalert %}

Para la referencia completa sobre las propiedades de entrada persistentes, consulta [Propiedades de entrada persistentes]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties/).