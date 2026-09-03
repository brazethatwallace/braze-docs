Puedes utilizar las propiedades de entrada de Canvas y las propiedades del evento en tus recorridos de usuario de Canvas.

{% tabs local %}
{% tab Canvas Entry Properties %}

[Las propiedades de entrada de Canvas]({{site.baseurl}}/api/objects_filters/context_object) son las propiedades que asignas a los Canvas basados en acciones o activados por API. Ten en cuenta que el objeto `canvas_entry_properties` tiene un límite de tamaño máximo de 50 KB.

{% alert note %}
En el caso concreto de los canales de mensajes dentro de la aplicación, solo se puede hacer referencia a `context` en Canvas.
{% endalert %}

Puedes hacer referencia a `context` en cualquier paso de mensaje con este formato Liquid: ``{% raw %} context.${property_name} {% endraw %}``. Ten en cuenta que los eventos deben ser eventos personalizados o eventos de compra para poder utilizarse de esta manera.

#### Caso de uso {#use-case}

{% raw %}
Supongamos que una tienda de comercio minorista, RetailApp, tiene la siguiente solicitud: `"context" : {"product_name" : "shoes", "product_price" : 79.99}`.

RetailApp puede incluir el nombre del producto (shoes) en un mensaje con este Liquid: `{{context.${product_name}}}`.
{% endraw %}

RetailApp también puede desencadenar el envío de mensajes específicos para diferentes propiedades de `product_name` en un Canvas dirigido a los usuarios después de que hayan desencadenado un evento de compra. Por ejemplo, pueden enviar mensajes diferentes a los usuarios que compraron zapatos y a los usuarios que compraron otra cosa añadiendo el siguiente Liquid en un paso de mensaje.

{% raw %}
```markdown
{% if  {{context.${product_name}}} == "shoes" %}
  Your order is set to ship soon. While you're waiting, why not step up your shoe care routine with a little upgrade? Check out our selection of shoelaces and premium shoe polish.
{% else %}
  Your order will be on its way shortly. If you missed something, you have until the end of the week to add more items to your cart for the same discounts.
{% endif %}

```
{% endraw %}

{% details Ampliar para el editor de Canvas original %}

Ya no puedes crear ni duplicar Canvas con el editor original. Esta sección está disponible solo como referencia. Para los Canvas creados con el editor original, solo se puede hacer referencia a las propiedades de entrada de Canvas en el primer paso completo de un Canvas.

{% enddetails %}
{% endtab %}

{% tab Event Properties %}

Las propiedades del evento se refieren a las propiedades que estableces para los eventos personalizados y las compras. Estas `event_properties` se pueden utilizar en Campaigns con entrega basada en acciones y en Canvas.

{% alert important %}
No puedes utilizar `event_properties` en el primer paso de mensaje de tu Canvas. En su lugar, debes utilizar `context` o añadir un paso de Rutas de acción con el evento correspondiente **antes** del paso de mensaje que incluye `event_properties`.
{% endalert %}

En Canvas, las propiedades de eventos personalizados y de eventos de compra se pueden utilizar en Liquid en cualquier paso de mensaje que siga a un paso de Rutas de acción. Asegúrate de utilizar {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} si haces referencia a estas propiedades del evento. Estos eventos deben ser eventos personalizados o eventos de compra para poder utilizarse de esta forma en el componente de mensaje.

En el primer paso de mensaje que sigue a una ruta de acción, puedes utilizar las propiedades del evento relacionadas con el evento al que se hace referencia en esa ruta de acción. Sin embargo, estas propiedades del evento solo se pueden utilizar si el usuario realmente realizó la acción (y no fue clasificado en el grupo El resto). Puedes tener otros pasos (que no sean otro paso de Rutas de acción o de mensaje) entre esta ruta de acción y el paso de mensaje.

{% details Ampliar para el editor de Canvas original %}

Ya no puedes crear ni duplicar Canvas con el editor original. Esta sección está disponible solo como referencia. En el editor de Canvas original, las propiedades del evento no se pueden utilizar en pasos completos planificados. Sin embargo, puedes utilizar las propiedades del evento en el primer paso completo de un Canvas basado en acciones, incluso si el paso completo está planificado.

{% enddetails %}

{% endtab %}
{% endtabs %}

Consulta [Propiedades de entrada de Canvas y propiedades del evento]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) para obtener más información y ejemplos.