---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes
page_order: 12
description: "Este artículo ofrece respuestas a preguntas frecuentes sobre Liquid."

---

# Preguntas frecuentes

> En esta página encontrarás respuestas a algunas preguntas frecuentes sobre Liquid.<br><br>Actualmente, Braze no es compatible con el 100 % de Liquid de Shopify, solo con ciertas partes que hemos intentado describir en nuestra documentación. Recomendamos encarecidamente probar todos los mensajes que usen Liquid antes de enviarlos para reducir el riesgo de errores o de usar Liquid no compatible.

### ¿Cómo uso fragmentos de código de Liquid en Braze?

En muchos casos, puedes incorporar fragmentos de código de Liquid navegando a tus Campaigns o Canvas e insertando Liquid en el modal de personalización en áreas como el cuerpo del mensaje de correo electrónico o en tus Segments.

#### ¿Dónde puedo aprender más?

Para más información sobre Liquid, consulta nuestra ruta guiada de Braze Learning [Personalización dinámica con Liquid](https://learning.braze.com/path/dynamic-personalization-with-liquid). También puedes consultar la [biblioteca de casos de uso de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases/) para inspirarte y ver una variedad de ejemplos de personalización con Liquid.

### ¿Cuál es la diferencia entre usar Liquid y Contenido conectado para la personalización?

El Contenido conectado de Braze es un ejemplo de etiqueta de Liquid. También se usa para la personalización, pero estos datos provienen de un punto de conexión externo en lugar de datos almacenados dentro de Braze. Consulta nuestra sección dedicada de [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) para aprender más sobre cómo ampliar la personalización de tus mensajes.

### ¿Qué es la plantilla de Liquid?

Es la forma más común de usar Liquid en Braze. La plantilla de Liquid consiste en extraer datos del perfil de un usuario e insertarlos en un mensaje. Estos datos pueden ir desde el nombre del usuario hasta eventos personalizados de un mensaje desencadenado por un evento.

Consulta [Etiquetas de personalización compatibles]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/) para ver una lista completa de las etiquetas de Liquid compatibles.

### ¿Cómo asigno variables con Liquid?

Puedes crear y asignar variables usando la etiqueta `assign`. Esto crea una variable en el creador de mensajes que también puede referenciarse a lo largo de tu mensaje.

### ¿Usar Liquid registra puntos de datos?

No.

### ¿Cómo puedo usar Liquid para enviar un saludo personalizado?

Para un saludo personalizado usando el nombre del usuario, puedes extraer los atributos estándar del perfil de usuario como {% raw %} `{{${first_name}}}`, `{{${last_name}}}`.

También puedes usar una sentencia `{% if X %}` {% endraw %} de Liquid para hacer renderizado condicional basado en cualquier cosa, como el día de la semana o atributos personalizados. Para más información sobre los operadores de Liquid compatibles que pueden usarse en sentencias condicionales, consulta [Operadores]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/operators/).

### ¿Cómo puedo personalizar un mensaje según la ubicación de un cliente?

{% raw %}
Existe un atributo predeterminado para la ubicación del usuario: `{{${most_recent_location}}}`.

### ¿Cuál es la diferencia entre {{campaign.${name}}} y {{campaign.${message_name}}}?

Tanto `{{campaign.${name}}}` como `{{campaign.${message_name}}}` son etiquetas de personalización de Liquid compatibles. Ambas etiquetas hacen referencia a atributos de la campaña. `{{campaign.${name}}}` indica el nombre de tu campaña, y `{{campaign.${message_name}}}` es el nombre de tu variante de mensaje.
{% endraw %}

### ¿Cómo uso Liquid con objetos anidados?

Braze tiene una característica integrada que genera código Liquid para segmentos que pueden usarse en un mensaje. Específicamente, puedes crear un segmento que coincida con múltiples criterios en un objeto.

Para más información, consulta [Segmentación multicriterio]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support/#multi-criteria-segmentation).

### ¿Cómo uso atributos de eventos para personalizar un mensaje que un evento está desencadenando?

{% raw %}
Puedes acceder a las propiedades de eventos desencadenados por API con la etiqueta `api_triggered_property`: `{{api_trigger_properties.${attribute_key}}}`.
{% endraw %}

### ¿Por qué mi Liquid desencadenado por API falla en Braze?

{% raw %}
Una causa común es un par extra de llaves. Por ejemplo, `{{{api_trigger_properties.${attribute_key}}}}` no es una sintaxis de personalización válida en Braze. Usa exactamente dos llaves de apertura y dos de cierre: `{{api_trigger_properties.${attribute_key}}}`.
{% endraw %}

### ¿Qué es la lógica de cancelación y cómo puedo usarla?

La lógica de cancelación te permite detener el envío de un mensaje si se cumplen las condiciones. Esto es especialmente útil para evitar que se envíen mensajes incompletos a tus usuarios. Para ver ejemplos de lógica de cancelación en tus campañas de marketing, lee más en [Cancelar mensajes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/).

### ¿Qué es la lógica de bucle for y cómo puedo usarla?

Los bucles for también se conocen como [etiquetas de iteración](https://shopify.github.io/liquid/tags/iteration/). Usar la lógica de bucle for en tus fragmentos de código de Liquid te permite recorrer bloques de Liquid hasta que se cumpla una condición.

En Braze, esto podría usarse para verificar elementos en un atributo personalizado de tipo array, o una lista de valores y objetos devueltos por una llamada de [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/), [selección]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) o respuesta de [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/). Específicamente, puedes usar la lógica de bucle for como parte de tu mensajería para verificar si un producto está en stock o si un producto tiene una calificación mínima.

Por ejemplo, supongamos que tienes un catálogo llamado "Games" que tiene una selección llamada "cheap_games". Para extraer los títulos de los juegos en "cheap_games", podrías usar este fragmento de código de Liquid:

{% raw %}
```liquid
{% catalog_selection_items Games cheap_games %}
{% for item in items %}
 Get this game: {{ item.title }}
{% endfor %}
```
{% endraw %}

Una vez que se cumplan las condiciones establecidas, tu mensaje puede continuar. Usar esta lógica es una forma útil de ahorrar tiempo, en lugar de repetir bloques de Liquid para diferentes condiciones.

### ¿Por qué hay espaciado extra en los mensajes que usan Content Blocks?

Si notas espaciado extra en los mensajes enviados que usan Content Blocks con Liquid, es posible que tengas saltos de párrafo o de línea innecesarios dentro de tus sentencias condicionales. Escribe tus sentencias condicionales en una sola línea en lugar de en múltiples líneas.

#### Ejemplo

{% raw %}
```liquid
{% if {{custom_attribute.${has_discount}}} == true %}Discounted Item{% elsif {{custom_attribute.${is_new_arrival}}} == true %}New Arrival{% else %}Regular Item{% endif %}
```
{% endraw %}

### ¿Cuándo debo usar `assign` en lugar de `capture`?

Tanto `assign` como `capture` crean variables de Liquid, pero tienen propósitos diferentes:

- `assign` es para variables simples que almacenan un solo valor, como un booleano, un número o una cadena simple. También puedes aplicar un solo filtro en la misma línea.
- `capture` es para almacenar un bloque de texto que puede incluir múltiples variables, cadenas o expresiones complejas. Usa `capture` cuando el valor sea demasiado complejo para una sola sentencia `assign`, como URLs que utilizan otras variables de Liquid o atributos personalizados como parámetros. `capture` también es preferible cuando implementas variables de Liquid en el cuerpo de llamadas de Contenido conectado.

#### Ejemplos

{% raw %}
```liquid
{% comment %} Valid assign usage {% endcomment %}
{% assign name = {{custom_attribute.${first_name}}} %}
{% assign price = {{custom_attribute.${price}}} | plus: 0 %}

{% comment %} Use capture for complex strings {% endcomment %}
{% capture greeting %}Hello, {{custom_attribute.${first_name}}}! Your order #{{custom_attribute.${order_id}}} is ready.{% endcapture %}
{{ greeting }}
```
{% endraw %}