---
nav_title: Operadores
article_title: Operadores de Liquid
page_order: 2
description: "Esta página de referencia describe los operadores que admite Liquid, así como ejemplos relevantes."

---

# Operadores {#operators}

> Liquid admite muchos [operadores](https://docs.shopify.com/themes/liquid/basics/operators) que puedes usar en tus sentencias condicionales. Esta página cubre los operadores que admite Liquid y proporciona ejemplos de cómo puedes utilizarlos en tus mensajes.

Esta tabla enumera los operadores admitidos. Ten en cuenta que los paréntesis son caracteres no válidos en Liquid e impiden que tus etiquetas funcionen.

| Sintaxis | Descripción del operador |
|---------|-----------|
| ==  | igual a        |
| !=  | no es igual a |
|  >  | mayor que  |
| <   | menor que     |
| >= | mayor o igual que |
| <= | menor o igual que |
| or | condición A o condición B |
| and | condición A y condición B |
| contains | comprueba si una cadena o un arreglo de cadenas contiene una cadena |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Operadores" }

{% alert note %}
Los operadores se pueden usar en sentencias condicionales (`if`, `elsif`, `unless`) pero no en sentencias `assign`, bucles `for` ni corchetes de acceso a arreglos. En las etiquetas `case` y `when`, cada rama compara la expresión `case` con un valor `when` usando igualdad en lugar de expresiones de operadores arbitrarios. Para ver ejemplos, consulta [Lógica condicional de mensajería]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#case-and-when). Para un desglose completo, consulta [Dónde usar operadores y filtros]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#where-to-use-operators-and-filters).
{% endalert %}

## Agrupar condiciones sin paréntesis {#grouping-conditions-without-parentheses}

Liquid no admite paréntesis para agrupar expresiones. Para evaluar lógica booleana compleja como `(a and b) or c`, usa sentencias `if` anidadas o variables intermedias.

Por ejemplo, para comprobar si un valor satisface una condición compuesta, asigna una variable intermedia:

{% raw %}
```liquid
{% assign qualifies = false %}
{% if points > 100 %}
{% assign qualifies = true %}
{% elsif points == 100 and member_level == 'gold' %}
{% assign qualifies = true %}
{% endif %}

{% if qualifies %}
You qualify for a reward!
{% endif %}
```
{% endraw %}

## Tutoriales {#tutorials}

Veamos algunos tutoriales para aprender a usar estos operadores en tus campañas de marketing:

### Elegir un mensaje con un atributo personalizado de tipo entero {#choose-a-message-with-an-integer-custom-attribute}

Enviemos notificaciones push con descuentos promocionales personalizados a usuarios que hayan realizado o no compras. La notificación push usará un atributo personalizado de tipo entero llamado `total_spend` para comprobar el gasto total de un usuario.

1. Escribe una sentencia condicional usando el operador mayor que (`>`) para comprobar si el gasto total de un usuario es mayor que `0`, lo que indica que ha realizado una compra. Luego, crea un mensaje para enviar a esos usuarios.

{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
{% endraw %}

{: start="2"}
2. Añade la etiqueta {% raw %}`{% else %}`{% endraw %} para capturar a los usuarios cuyo gasto total sea igual a `0` o no exista. Luego, crea un mensaje para enviar a esos usuarios.

{% raw %}
```liquid
{% else %}
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```
{% endraw %}

{: start="3"}
3. Cierra la lógica condicional con la etiqueta {% raw %}`{% endif %}`{% endraw %}.

{% raw %}
```liquid
{% endif %}
```
{% endraw %}

![Un creador de notificaciones push con el código Liquid completo del tutorial.]({% image_buster /assets/img/liquid-if-totalspend.png %}){: width="100%"}

{% details Código Liquid completo %}
{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
{% else %}
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
{% endif %}
```
{% endraw %}
{% enddetails %}

Ahora, si el atributo personalizado "Total Spend" de un usuario es mayor que `0`, recibirá el mensaje:

```
Surprise! We added a 15% discount code to your account that automatically applies to your next order.
```
Si el atributo personalizado "Total Spend" de un usuario no existe o es igual a `0`, recibirá el siguiente mensaje:

```
Need a sign to update your wardrobe? We added a 15% discount code to your account that will automatically apply to your first order.
```

### Elegir un mensaje con un atributo personalizado de tipo cadena {#choose-a-message-with-a-string-custom-attribute}

Enviemos notificaciones push a los usuarios y personalicemos el mensaje según el juego más reciente de cada usuario. Esto usará un atributo personalizado de tipo cadena llamado `recent_game` para comprobar qué juego ha jugado un usuario por última vez.

1. Escribe una sentencia condicional usando el operador igual a (`==`) para comprobar si el juego más reciente de un usuario es *Awkward Dinner Party*. Luego, crea un mensaje para enviar a esos usuarios.

{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```
{% endraw %}

{: start="2"}
2. Usa la etiqueta `elsif` con el operador igual a (`==`) para comprobar si el juego más reciente del usuario es *Proxy War 3: War of Thirst*. Luego, crea un mensaje para enviar a esos usuarios.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```
{% endraw %}

{: start="3"}
3. Usa la etiqueta `elsif` con los operadores "no es igual a" (`!=`) y "and" (`and`) para comprobar si el usuario tiene un juego reciente (es decir, el valor no está en blanco) y que el juego no sea *Awkward Dinner Party* ni *Proxy War 3: War of Thirst*. Luego, crea un mensaje para enviar a esos usuarios.

{% raw %}
```liquid
{% elsif {{custom_attribute.${recent_game}}} != blank and {{custom_attribute.${recent_game}}} != 'Awkward Dinner Party' and {{custom_attribute.${recent_game}}} != 'Proxy War 3: War of Thirst' %}
Limited Time Deal! Get 15% off our best-selling classics!
```
{% endraw %}

{: start="4"}
4. Añade la etiqueta {% raw %}`{% else %}`{% endraw %} para capturar a los usuarios que no tienen un juego reciente. Luego, crea un mensaje para enviar a esos usuarios.

{% raw %}
```liquid
{% else %}
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
```
{% endraw %}

{: start="5"}
5. Cierra la lógica condicional con la etiqueta {% raw %}`{% endif %}`{% endraw %}.

{% raw %}
```liquid
{% endif %}
```
{% endraw %}

{% details Código Liquid completo %}
{% raw %}
```liquid
{% if {{custom_attribute.${recent_game}}} == 'Awkward Dinner Party' %}
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
{% elsif {{custom_attribute.${recent_game}}} == 'Proxy War 3: War of Thirst' %}
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
{% elsif {{custom_attribute.${recent_game}}} != blank and {{custom_attribute.${recent_game}}} != 'Awkward Dinner Party' and {{custom_attribute.${recent_game}}} != 'Proxy War 3: War of Thirst' %}
Limited Time Deal! Get 15% off our best-selling classics!
{% else %}
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
{% endif %}
```
{% endraw %}
{% enddetails %}

![Un creador de notificaciones push con el código Liquid completo del tutorial.]({% image_buster /assets/img/liquid-if-elsif-games.png %})

Ahora, si un usuario jugó por última vez *Awkward Dinner Party*, recibirá este mensaje:

```
You are formally invited to our next dinner party. Log on next week for another round of delectable dishes and curious conversations.
```

Si el juego más reciente de un usuario es *Proxy War 3: War of Thirst*, recibirá este mensaje:

```
Your fleet awaits your next orders. Log on when you're ready to rejoin the war for hydration.
```

Si un usuario ha jugado recientemente un juego que no era *Awkward Dinner Party* ni *Proxy War 3: War of Thirst*, recibirá este mensaje:

```
Limited Time Deal! Get 15% off our best-selling classics!
```

Si un usuario no ha jugado ningún juego o ese atributo personalizado no existe en su perfil, recibirá este mensaje:

```
Hey! I've got a deal for you. Buy 2 of our newest releases and get 10% off!
```

### Cancelar un mensaje según la ubicación {#abort-message-based-on-location}

Puedes cancelar un mensaje basándote en prácticamente cualquier cosa. Cancelemos un mensaje si un usuario no se encuentra en un área específica, ya que podría no ser elegible para la promoción, el evento o la entrega.

1. Escribe una sentencia condicional usando el operador igual a (`==`) para comprobar si la zona horaria del usuario es `America/Los_Angeles`, y luego crea un mensaje para enviar a esos usuarios.

{% raw %}
```liquid
{% if {{${time_zone}}} == 'America/Los_Angeles' %}
Stream now!
```
{% endraw %}

{: start="2"}
2. Para evitar enviar mensajes a usuarios fuera de la zona horaria `America/Los_Angeles`, envuelve las etiquetas {% raw %}`{% else %}`{% endraw %} y {% raw %}`{% endif %}`{% endraw %} alrededor de una etiqueta {% raw %}`{% abort_message () %}`{% endraw %}.

{% raw %}
```liquid
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}

{% details Código Liquid completo %}
{% raw %}
```liquid
{% if {{${time_zone}}} =='America/Los_Angeles' %}
Stream now!
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}
{% enddetails %}

![Un creador de notificaciones push con el código Liquid completo del tutorial.]({% image_buster /assets/img/abort-if.png %})

También puedes [cancelar mensajes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content) basándote en contenido conectado.

## Solución de problemas {#troubleshooting}

### El envío de prueba no llega al usar `abort_message` {#test-send-doesnt-arrive-when-using-abort_message}

Si usas [`abort_message`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) y un envío de prueba nunca llega, es posible que al usuario de vista previa le falten atributos que tu Liquid espera. La lógica de cancelación se ejecuta durante el renderizado; cuando se activa, Braze no envía el mensaje. Previsualiza con un usuario que tenga los datos de perfil necesarios, o usa **Previsualizar como usuario** para probar campos de destinatario que proporcionen los mismos valores que tendría tu audiencia de producción.

### La vista previa puede convertir incorrectamente los tipos de propiedad {#preview-may-incorrectly-coerce-property-types}

Al previsualizar un mensaje en el panel, la mayoría de las variables (como los atributos personalizados) se convierten al tipo correcto. Sin embargo, algunas variables no tienen un tipo definido que la vista previa pueda consultar:

- `api_trigger_properties`
- `canvas_entry_properties`
- `context`

Para estas propiedades, la vista previa intenta inferir el tipo a partir del valor. Esto significa que un valor que pretendes que sea una **cadena** podría interpretarse erróneamente como un **número**. Por ejemplo, si el valor de una propiedad es la cadena `"3"`, la vista previa puede convertirlo al entero `3`, lo que puede causar un comportamiento inesperado en operaciones de cadena como `contains` o `split`.

Si ves resultados inesperados en la vista previa al usar estos tipos de propiedades, ten en cuenta que la inferencia de tipos de la vista previa puede no coincidir con lo que ocurre en el momento del envío. En el momento del envío, se preservan los tipos de datos reales del evento desencadenante o la llamada a la API.

Para forzar un tipo específico en la vista previa, puedes convertir explícitamente el valor:

{% raw %}
```liquid
{% comment %} Force a value to be treated as a number {% endcomment %}
{% assign orders = {{canvas_entry_properties.${number_of_orders}}} | plus: 0 %}

{% comment %} Force a value to be treated as a string {% endcomment %}
{% assign code = {{api_trigger_properties.${promo_code}}} | append: "" %}
```
{% endraw %}