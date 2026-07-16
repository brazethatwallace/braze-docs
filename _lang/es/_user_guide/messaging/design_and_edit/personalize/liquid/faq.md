---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes
page_order: 12
description: "Este artículo ofrece respuestas a preguntas frecuentes sobre Liquid."
toc_headers: h2
---

# Preguntas frecuentes {#frequently-asked-questions}

> En esta página encontrarás respuestas a preguntas frecuentes sobre Liquid.

{% alert note %}
Actualmente, Braze no es compatible con el 100 % de Liquid de Shopify, solo con ciertas partes que hemos intentado describir en nuestra documentación. Prueba todos los mensajes que usen Liquid antes de enviarlos para reducir el riesgo de errores o de usar Liquid no compatible.
{% endalert %}

## Acerca de Liquid en Braze {#about-liquid-in-braze}

### ¿Cómo uso fragmentos de código de Liquid en Braze? {#how-do-i-use-liquid-snippets-in-braze}

En muchos casos, puedes incorporar fragmentos de código de Liquid navegando a tus Campaigns o Canvas e insertando Liquid en el modal de personalización en áreas como el cuerpo del mensaje de correo electrónico o en tus Segments.

#### ¿Dónde puedo aprender más? {#where-can-i-learn-more}

Para más información sobre Liquid, consulta nuestra ruta guiada de Braze Learning [Personalización dinámica con Liquid](https://learning.braze.com/path/dynamic-personalization-with-liquid). También puedes consultar la [biblioteca de casos de uso de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases) para inspirarte y ver una variedad de ejemplos de personalización con Liquid.

### ¿Cuál es la diferencia entre usar Liquid y contenido conectado para la personalización? {#whats-the-difference-between-using-liquid-and-connected-content-for-personalization}

El contenido conectado de Braze es un ejemplo de etiqueta de Liquid. También se usa para la personalización, pero estos datos provienen de un endpoint externo en lugar de datos almacenados dentro de Braze. Consulta nuestra sección dedicada de [Contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) para aprender más sobre cómo ampliar la personalización de tus mensajes.

### ¿Qué es la plantilla de Liquid? {#what-is-liquid-templating}

Es la forma más común de usar Liquid en Braze. La plantilla de Liquid consiste en extraer datos del perfil de un usuario e insertarlos en un mensaje. Estos datos pueden ir desde el nombre del usuario hasta eventos personalizados de un mensaje desencadenado por un evento.

Consulta [Etiquetas de personalización compatibles]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) para ver una lista completa de las etiquetas de Liquid compatibles.

### ¿Usar Liquid registra puntos de datos? {#does-using-liquid-log-data-points}

No.

## Etiquetas de personalización y orígenes de datos {#personalization-tags-and-data-sources}

### ¿Cómo puedo usar Liquid para enviar un saludo personalizado? {#how-can-i-use-liquid-to-send-a-personalized-greeting}

Para un saludo personalizado usando el nombre del usuario, puedes extraer los atributos estándar del perfil de usuario como {% raw %}`{{${first_name}}}` y `{{${last_name}}}`{% endraw %}.

También puedes usar una sentencia {% raw %}`{% if X %}`{% endraw %} de Liquid para hacer renderizado condicional basado en cualquier cosa, como el día de la semana o atributos personalizados. Para más información sobre los operadores de Liquid compatibles que pueden usarse en sentencias condicionales, consulta [Operadores]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/operators).

### ¿Cómo puedo personalizar un mensaje según la ubicación de un usuario? {#how-can-i-personalize-a-message-based-on-a-users-location}

{% raw %}
Existe un atributo predeterminado para la ubicación del usuario: `{{${most_recent_location}}}`.
{% endraw %}

{% raw %}
### ¿Cuál es la diferencia entre {{campaign.${name}}} y {{campaign.${message_name}}}? {#whats-the-difference-between-campaignname-and-campaignmessage_name}

Tanto `{{campaign.${name}}}` como `{{campaign.${message_name}}}` son etiquetas de personalización de Liquid compatibles. Ambas etiquetas hacen referencia a atributos de la campaña. `{{campaign.${name}}}` indica el nombre de tu campaña, y `{{campaign.${message_name}}}` es el nombre de tu variante de mensaje.
{% endraw %}

Para el uso en URL y cadenas de consulta (por ejemplo, cuando un nombre contiene `%` o espacios), consulta [Nombres de Campaign en URL]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#campaign-names-in-urls).

### ¿Cómo uso Liquid con objetos anidados? {#how-do-i-use-liquid-with-nested-objects}

Braze tiene una característica integrada que genera código Liquid para segmentos que pueden usarse en un mensaje. Específicamente, puedes crear un segmento que coincida con múltiples criterios en un objeto.

Para más información, consulta [Segmentación multicriterio]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support#segmentation-behavior-with-arrays-of-objects).

### ¿Cómo uso propiedades de eventos para personalizar un mensaje que un evento está desencadenando? {#how-do-i-use-event-attributes-to-personalize-a-message-that-an-event-is-triggering}

{% raw %}
Puedes acceder a las propiedades de eventos desencadenados por API con la etiqueta `api_triggered_property`: `{{api_trigger_properties.${attribute_key}}}`.
{% endraw %}

### ¿Braze admite un array de arrays en Liquid? {#does-braze-support-an-array-of-arrays-in-liquid}

Liquid no admite de forma nativa arrays de arrays. Almacena los valores como un array de cadenas separadas por comas y usa el filtro `split` para analizarlos cuando sea necesario.

## Variables y sintaxis {#variables-and-syntax}

### ¿Cómo asigno variables con Liquid? {#how-do-i-assign-variables-with-liquid}

Puedes crear y asignar variables usando la etiqueta `assign`. Esto crea una variable en el creador de mensajes que también puede referenciarse a lo largo de tu mensaje.

### ¿Cuándo debo usar `assign` en lugar de `capture`? {#when-should-i-use-assign-versus-capture}

Tanto `assign` como `capture` crean variables de Liquid, pero tienen propósitos diferentes:

- `assign` es para variables simples que almacenan un solo valor, como un booleano, un número o una cadena simple. También puedes aplicar un solo filtro en la misma línea.
- `capture` es para almacenar un bloque de texto que puede incluir múltiples variables, cadenas o expresiones complejas.

Usa `capture` cuando el valor sea demasiado complejo para una sola sentencia `assign`, como URL que utilizan otras variables de Liquid o atributos personalizados como parámetros. `capture` también es preferible cuando implementas variables de Liquid en el cuerpo de llamadas de contenido conectado.

#### Ejemplos {#examples}

{% raw %}
```liquid
{% comment %}Use assign for custom attributes{% endcomment %}
{% assign name = {{custom_attribute.${first_name}}} %}
{% assign price = {{custom_attribute.${price}}} | plus: 0 %}

{% comment %}Use assign for a simple variable{% endcomment %}
{% assign discount_label = "20% off" %}
Hello {{ customer.first_name | default: "there" }}, enjoy {{ discount_label }} on your next order!

{% comment %}Use capture for complex strings{% endcomment %}
{% capture greeting %}Hello, {{custom_attribute.${first_name}}}! Your order #{{custom_attribute.${order_id}}} is ready.{% endcapture %}
{{ greeting }}

{% comment %}Use capture to create conditional content{% endcomment %}
{% capture promo_block %}
{% if customer.vip == true %}
As a VIP member, you get free shipping.
{% else %}
Join our VIP program to unlock free shipping.
{% endif %}
{% endcapture %}
```
{% endraw %}

### ¿Las variables de Liquid se comparten entre la línea del asunto y el cuerpo? {#do-liquid-variables-carry-between-subject-line-and-body}

No. Braze renderiza cada componente del mensaje por separado (como la línea del asunto, el cuerpo HTML, el preencabezado y el título push). Las asignaciones o capturas que hagas en un campo no están disponibles en otro. Repite la llamada de Liquid o contenido conectado en cada campo que necesite el valor.

### ¿Qué es la lógica de bucle for y cómo puedo usarla? {#what-is-for-loop-logic-and-how-can-i-use-it}

Los bucles for también se conocen como [etiquetas de iteración](https://shopify.github.io/liquid/tags/iteration/). Usar la lógica de bucle for en tus fragmentos de código de Liquid te permite recorrer bloques de Liquid hasta que se cumpla una condición.

En Braze, esto podría usarse para verificar elementos en un atributo personalizado de tipo array, o una lista de valores y objetos devueltos por una llamada de [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs), [selección]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) o respuesta de [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content). Específicamente, puedes usar la lógica de bucle for como parte de tu mensajería para verificar si un producto está en stock o si un producto tiene una calificación mínima.

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

### ¿Qué es la lógica de cancelación y cómo puedo usarla? {#what-is-abort-logic-and-how-can-i-use-it}

La lógica de cancelación te permite detener el envío de un mensaje si se cumplen las condiciones. Esto es especialmente útil para evitar que se envíen mensajes incompletos a tus usuarios. Para ver ejemplos de lógica de cancelación en tus campañas de marketing, lee más en [Cancelar mensajes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages).

### ¿Puedo usar Liquid dentro de la etiqueta `abort_message`? {#can-i-use-liquid-inside-the-abort_message-tag}

No. La etiqueta {% raw %}`{% abort_message %}`{% endraw %} acepta una cadena estática entre comillas, no personalización de Liquid. Usa otra lógica de Liquid antes de la etiqueta si necesitas un comportamiento de cancelación condicional.

## Canvas, catálogos y propiedades de desencadenamiento {#canvas-catalogs-and-trigger-properties}

### ¿Por qué mi Liquid desencadenado por API falla en Braze? {#why-is-my-api-triggered-liquid-failing-in-braze}

{% raw %}
Una causa común es un par extra de llaves. Por ejemplo, `{{{api_trigger_properties.${attribute_key}}}}` no es una sintaxis de personalización válida en Braze. Usa exactamente dos llaves de apertura y dos de cierre: `{{api_trigger_properties.${attribute_key}}}`.
{% endraw %}

### ¿Hay límites de tamaño para las propiedades de contexto de Canvas? {#are-there-size-limits-for-canvas-context-properties}

Braze no impone un límite estricto en las [propiedades de contexto de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties), pero mantén las cargas útiles por debajo de aproximadamente 1 KB (~1000 caracteres). Los objetos más grandes pueden aumentar el uso de memoria y retrasar el renderizado de mensajes durante envíos de alto volumen.

### ¿Por qué obtengo un error de Liquid al previsualizar ciertos tipos de datos en el panel? {#why-do-i-get-a-liquid-error-when-previewing-certain-data-types-in-the-dashboard}

Algunos tipos de [propiedades de contexto de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) requieren conversión en Liquid antes de usarlos en comparaciones u operaciones matemáticas. Por ejemplo, cuando necesitas un comportamiento numérico:

{% raw %}
```liquid
{{context.${property_name} | plus: 0}}
```
{% endraw %}

### ¿Por qué mi fragmento de código de Liquid de catálogo devuelve un mensaje de cancelación? {#why-does-my-catalog-liquid-snippet-return-an-abort-message}

Si un fragmento de código de Liquid de catálogo se cancela durante el envío, recrea el fragmento desde el menú de personalización seleccionando elementos individuales del catálogo en lugar de usar una selección masiva o completamente dinámica. Consulta [Catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs) y [Selecciones]({{site.baseurl}}/user_guide/data/activation/catalogs/selections).

## Content Blocks y el creador de mensajes {#content-blocks-and-the-message-composer}

### ¿Por qué hay espaciado extra en los mensajes que usan Content Blocks? {#why-is-there-extra-spacing-in-messages-that-use-content-blocks}

Si notas espaciado extra en los mensajes enviados que usan Content Blocks con Liquid, es posible que tengas saltos de párrafo o de línea innecesarios dentro de tus sentencias condicionales. Escribe tus sentencias condicionales en una sola línea en lugar de en múltiples líneas.

#### Ejemplo {#example}

{% raw %}
```liquid
{% if {{custom_attribute.${has_discount}}} == true %}Discounted Item{% elsif {{custom_attribute.${is_new_arrival}}} == true %}New Arrival{% else %}Regular Item{% endif %}
```
{% endraw %}

### ¿Por qué mi Content Block no aparece en **Row** en la herramienta de búsqueda de arrastrar y soltar? {#why-is-my-content-block-missing-from-row-in-the-drag-and-drop-search-tool}

Algunos Content Blocks no aparecen en **Row** en la búsqueda del editor de arrastrar y soltar. Añade un bloque HTML desde la pestaña **Content** (**Advanced**), luego inserta la etiqueta de Liquid del Content Block en ese bloque HTML para renderizar el contenido del bloque.

### ¿Por qué la vista previa de mi Content Block de arrastrar y soltar difiere de la vista de redacción? {#why-does-my-drag-and-drop-content-block-preview-differ-from-the-compose-view}

Cuando usas una plantilla de Content Block con Liquid, las consultas de medios para móviles en el bloque pueden no aplicarse en la vista previa de la misma manera que cuando arrastras el bloque directamente a un mensaje. Arrastrar el bloque preserva el diseño pero lo desacopla del bloque fuente, por lo que las ediciones futuras del bloque ya no actualizan el mensaje automáticamente.

### ¿Cómo previsualizo los valores de propiedades de eventos en el creador de mensajes? {#how-do-i-preview-event-property-values-in-message-composer}

Usa **Preview as Custom User** e introduce valores de ejemplo de propiedades de eventos personalizados para el usuario que previsualizas. Esto también es útil para mensajes con lógica de cancelación cuando necesitas valores de vista previa que no desencadenen una cancelación.

## Liquid en mensajes de correo electrónico {#liquid-in-email-messages}

### ¿Por qué mi mensaje se cancela con "Invalid from email address for recipient:"? {#why-does-my-message-abort-with-invalid-from-email-address-for-recipient}

Esta cancelación ocurre cuando el Liquid en la dirección **De** produce una sintaxis no válida, como una variable faltante, espacios adicionales o caracteres no permitidos. Previsualiza con un usuario de prueba y verifica que la dirección **De** renderizada coincida con tu dominio de envío configurado.

### ¿Cómo creo una dirección de respuesta dinámica? {#how-do-i-create-a-dynamic-reply-to-address}

Usa Liquid en el campo **Responder a** cuando tu espacio de trabajo admita la configuración dinámica de respuesta. Combínalo con la configuración del nombre para mostrar de **De** según sea necesario. Consulta [Configuración del correo electrónico]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences) para ver las opciones específicas del espacio de trabajo.

## Solución de problemas de errores de Liquid {#troubleshooting-liquid-errors}

### ¿Por qué veo un error de Liquid "Unexpected end token"? {#why-am-i-seeing-an-unexpected-end-token-liquid-error}

Este error generalmente indica llaves adicionales o faltantes. No anides {% raw %}`{{ }}`{% endraw %} dentro de otra expresión de etiqueta de Liquid. Por ejemplo, usa {% raw %}`{{custom_attribute.${date_of_birth} | date: '%s'}}`{% endraw %} en lugar de envolver la referencia del atributo en un par adicional de llaves.

### ¿Por qué el reintento de contenido conectado no está disponible para mi mensaje dentro de la aplicación? {#why-is-connected-content-retry-unavailable-for-my-in-app-message}

{% raw %}
La etiqueta `{% connected_content %}` con reintento no es compatible con todos los tipos de mensajes, incluidos algunos formatos de mensajes dentro de la aplicación. Elimina los parámetros de reintento o usa un canal compatible para las llamadas de contenido conectado con reintento.
{% endraw %}