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

### ¿Cómo uso los fragmentos de código de Liquid en Braze? {#how-do-i-use-liquid-snippets-in-braze}

En muchos casos, puedes incorporar fragmentos de código de Liquid yendo a tus Campaigns o Canvas e insertando Liquid en el modal de personalización en áreas como el cuerpo del mensaje de correo electrónico o en tus Segments.

#### ¿Dónde puedo aprender más? {#where-can-i-learn-more}

Para más información sobre Liquid, consulta nuestro recorrido guiado [Personalización dinámica con Liquid](https://learning.braze.com/path/dynamic-personalization-with-liquid) en Braze Learning. También puedes consultar la [biblioteca de casos de uso de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases) para encontrar inspiración y una variedad de ejemplos de personalización con Liquid.

### ¿Cuál es la diferencia entre usar Liquid y contenido conectado para la personalización? {#whats-the-difference-between-using-liquid-and-connected-content-for-personalization}

El contenido conectado de Braze es un ejemplo de una etiqueta de Liquid. También se usa para la personalización, pero estos datos provienen de un endpoint externo en lugar de datos almacenados en Braze. Consulta nuestra sección dedicada de [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) para aprender más sobre cómo ampliar la personalización de tus mensajes.

### ¿Qué es la creación de plantillas con Liquid? {#what-is-liquid-templating}

Esta es la forma más común de usar Liquid en Braze. La creación de plantillas con Liquid implica extraer datos del perfil de un usuario para incluirlos en un mensaje. Estos datos pueden ir desde el nombre de un usuario hasta eventos personalizados de un mensaje desencadenado por un evento.

Consulta las [etiquetas de personalización compatibles]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) para obtener una lista completa de las etiquetas de Liquid compatibles.

### ¿Usar Liquid registra puntos de datos? {#does-using-liquid-log-data-points}

No.

## Etiquetas de personalización y orígenes de datos {#personalization-tags-and-data-sources}

### ¿Cómo puedo usar Liquid para enviar un saludo personalizado? {#how-can-i-use-liquid-to-send-a-personalized-greeting}

Para un saludo personalizado utilizando el nombre del usuario, extrae los atributos estándar del perfil de usuario como {% raw %}`{{${first_name}}}` y `{{${last_name}}}`{% endraw %}.

También puedes usar una sentencia {% raw %}`{% if X %}`{% endraw %} de Liquid para hacer renderizado condicional basado en cualquier cosa, como el día de la semana o atributos personalizados. Para más información sobre los operadores de Liquid admitidos que pueden usarse en sentencias condicionales, consulta [Operadores]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/operators).

### ¿Cómo puedo personalizar un mensaje según la ubicación de un usuario? {#how-can-i-personalize-a-message-based-on-a-users-location}

{% raw %}
Existe un atributo predeterminado para la ubicación del usuario: `{{${most_recent_location}}}`.
{% endraw %}

{% raw %}
### ¿Cuál es la diferencia entre {{campaign.${name}}} y {{campaign.${message_name}}}? {#whats-the-difference-between-campaignname-and-campaignmessage_name}

Tanto `{{campaign.${name}}}` como `{{campaign.${message_name}}}` son etiquetas de personalización de Liquid admitidas. Ambas etiquetas hacen referencia a atributos de Campaign. `{{campaign.${name}}}` indica el nombre de tu Campaign, y `{{campaign.${message_name}}}` es el nombre de tu variante de mensaje.
{% endraw %}

Para el uso en URL y cadenas de consulta (por ejemplo, cuando un nombre contiene `%` o espacios), consulta [Nombres de Campaign en URL]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#campaign-names-in-urls).

### ¿Cómo uso Liquid con objetos anidados? {#how-do-i-use-liquid-with-nested-objects}

Braze tiene una característica integrada que genera código Liquid para Segments que se puede usar en un mensaje. Específicamente, puedes crear un Segment que coincida con múltiples criterios en un objeto.

Para más información, consulta [Segmentación multicriterio]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support#segmentation-behavior-with-arrays-of-objects).

### ¿Cómo uso los atributos de evento para personalizar un mensaje que un evento está desencadenando? {#how-do-i-use-event-attributes-to-personalize-a-message-that-an-event-is-triggering}

{% raw %}
Puedes acceder a las propiedades de los eventos desencadenados por API con la etiqueta `api_triggered_property`: `{{api_trigger_properties.${attribute_key}}}`.
{% endraw %}

### ¿Braze admite un arreglo de arreglos en Liquid? {#does-braze-support-an-array-of-arrays-in-liquid}

Liquid no admite de forma nativa arreglos de arreglos. Almacena los valores como un arreglo de cadenas separadas por comas y usa el filtro `split` para analizarlos cuando sea necesario.

## Variables y sintaxis {#variables-and-syntax}

### ¿Cómo asigno variables con Liquid? {#how-do-i-assign-variables-with-liquid}

Puedes crear y asignar variables usando la etiqueta `assign`. Esto crea una variable en el creador de mensajes que también se puede referenciar a lo largo de tu mensaje.

Puedes dividir un `assign` en varias líneas si envuelves todas las variables de Braze Liquid con dobles llaves {% raw %}(`{{ }}`){% endraw %}. Sin esas llaves, las sentencias assign multilínea pueden causar un renderizado inesperado, incluyendo atributos personalizados que no se procesan como plantilla. Para ver ejemplos y reglas de sintaxis relacionadas, consulta [Usar Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#liquid-syntax).

### ¿Cuándo debo usar `assign` en lugar de `capture`? {#when-should-i-use-assign-versus-capture}

Tanto `assign` como `capture` crean variables de Liquid, pero tienen propósitos diferentes:

- `assign` es para variables simples que almacenan un solo valor, como un booleano, un número o una cadena simple. También puedes aplicar un único filtro en la misma línea.
- `capture` es para almacenar un bloque de texto que puede incluir múltiples variables, cadenas o expresiones complejas.

Usa `capture` cuando el valor sea demasiado complejo para una sola sentencia `assign`, como URLs que usan otras variables de Liquid o atributos personalizados como parámetros. `capture` también se recomienda cuando se implementan variables de Liquid en el cuerpo de llamadas de contenido conectado.

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

Los bucles for también se conocen como [etiquetas de iteración](https://shopify.github.io/liquid/tags/iteration/). Usar la lógica de bucle for en tus fragmentos de Liquid te permite recorrer bloques de Liquid hasta que se cumpla una condición.

En Braze, esto se puede usar para revisar elementos en un atributo personalizado de tipo array, o una lista de valores y objetos devueltos por un [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs), una [selección]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) o una respuesta de llamada de [contenido conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content). Específicamente, puedes usar la lógica de bucle for como parte de tu mensajería para verificar si un producto está en existencia, o si un producto tiene una calificación mínima.

Por ejemplo, supongamos que tienes un catálogo llamado "Games" que tiene una selección llamada "cheap_games". Para obtener los títulos de los juegos en "cheap_games", podrías usar este fragmento de Liquid:

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

La lógica de cancelación te permite detener el envío de un mensaje si se cumplen las condiciones. Esto es especialmente útil para evitar que se envíen mensajes incompletos a tus usuarios. Para ver ejemplos de lógica de cancelación en tus Campaigns de marketing, lee más en [Cancelar mensajes]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages).

### ¿Puedo usar Liquid dentro de la etiqueta `abort_message`? {#can-i-use-liquid-inside-the-abort_message-tag}

No. La etiqueta {% raw %}`{% abort_message %}`{% endraw %} acepta una cadena estática entre comillas, no personalización con Liquid. Usa otra lógica de Liquid antes de la etiqueta si necesitas un comportamiento de cancelación condicional.

### ¿Cómo enmascaro números de teléfono con Liquid? {#how-do-i-mask-phone-numbers-with-liquid}

Puedes enmascarar números de teléfono usando el filtro `slice` para extraer dígitos específicos y el filtro `append` para combinarlos con caracteres de enmascaramiento.

#### Enmascarar todo excepto los últimos cuatro dígitos {#mask-all-but-the-last-four-digits}

Para mostrar un número de teléfono de 10 dígitos como `******7890`:

{% raw %}
```liquid
{% assign phone = {{${phone_number}}} | split: '' %}
{% assign masked_phone = '' %}
{% for i in (0..5) %}
  {% assign masked_phone = masked_phone | append: '*' %}
{% endfor %}
{% for i in (6..9) %}
  {% assign masked_phone = masked_phone | append: phone[i] %}
{% endfor %}
{{ masked_phone }}
```
{% endraw %}

#### Mostrar los primeros tres y los últimos cuatro dígitos {#show-the-first-three-and-last-four-digits}

Para mostrar un número de teléfono de 10 dígitos como `123***7890`:

{% raw %}
```liquid
{% assign first_part = {{${phone_number}}} | slice: 0, 3 %}
{% assign last_part = {{${phone_number}}} | slice: -4, 4 %}
{% assign masked_phone_number = first_part | append: "***" | append: last_part %}
{{ masked_phone_number }}
```
{% endraw %}

## Canvas, catálogos y propiedades de desencadenamiento {#canvas-catalogs-and-trigger-properties}

### ¿Por qué falla mi Liquid desencadenado por API en Braze? {#why-is-my-api-triggered-liquid-failing-in-braze}

{% raw %}
Un par extra de llaves es una causa habitual. Por ejemplo, `{{{api_trigger_properties.${attribute_key}}}}` no es una sintaxis de personalización válida en Braze. Usa exactamente dos llaves de apertura y dos de cierre: `{{api_trigger_properties.${attribute_key}}}`.
{% endraw %}

### ¿Existen límites de tamaño para las propiedades de contexto de Canvas? {#are-there-size-limits-for-canvas-context-properties}

Braze no impone un límite estricto sobre las [propiedades de contexto de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties), pero mantén las cargas útiles por debajo de aproximadamente 1 KB (~1000 caracteres). Los objetos más grandes pueden aumentar el uso de memoria y retrasar la renderización de mensajes durante envíos de alto volumen.

### ¿Por qué obtengo un error de Liquid al previsualizar ciertos tipos de datos en el panel? {#why-do-i-get-a-liquid-error-when-previewing-certain-data-types-in-the-dashboard}

Algunos tipos de [propiedades de contexto de Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) requieren conversión en Liquid antes de usarlos en comparaciones u operaciones matemáticas. Por ejemplo, cuando necesitas comportamiento numérico:

{% raw %}
```liquid
{{context.${property_name} | plus: 0}}
```
{% endraw %}

### ¿Por qué mi fragmento de Liquid de catálogo devuelve un mensaje de cancelación? {#why-does-my-catalog-liquid-snippet-return-an-abort-message}

Si un fragmento de Liquid de catálogo se cancela durante el envío, recrea el fragmento desde el menú de personalización seleccionando elementos individuales del catálogo en lugar de usar una selección masiva o completamente dinámica. Consulta [Catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs) y [Selecciones]({{site.baseurl}}/user_guide/data/activation/catalogs/selections).

## Content Blocks y el creador de mensajes {#content-blocks-and-the-message-composer}

### ¿Por qué hay espaciado adicional en los mensajes que usan Content Blocks? {#why-is-there-extra-spacing-in-messages-that-use-content-blocks}

Si notas espaciado adicional en los mensajes enviados que usan Content Blocks con Liquid, es posible que tengas saltos de párrafo o de línea innecesarios dentro de tus sentencias condicionales. Escribe tus sentencias condicionales en una sola línea en lugar de en varias líneas.

#### Ejemplo {#example}

{% raw %}
```liquid
{% if {{custom_attribute.${has_discount}}} == true %}Discounted Item{% elsif {{custom_attribute.${is_new_arrival}}} == true %}New Arrival{% else %}Regular Item{% endif %}
```
{% endraw %}


### ¿Por qué el Liquid multilínea crea espacios en blanco inesperados en los editores de arrastrar y soltar? {#why-does-multi-line-liquid-create-unexpected-whitespace-in-the-drag-and-drop-editors}

Cuando el código Liquid se distribuye en varias líneas en el editor de arrastrar y soltar de mensajes dentro de la aplicación o en el editor de arrastrar y soltar de correo electrónico, cada bloque {% raw %}`{% %}`{% endraw %} se renderiza como texto no visible. Los saltos de línea se conservan como líneas vacías antes de la salida visible, lo que causa espacios en blanco inesperados.

#### Solución 1: Usar etiquetas de control de espacios en blanco (recomendado) {#solution-1-use-whitespace-control-tags-recommended}

Añade guiones dentro de los delimitadores de etiqueta para eliminar los espacios en blanco circundantes manteniendo el código legible:

{% raw %}
```liquid
{%- assign event_date = {{custom_attribute.${PreferredPickupDate}}} | date: "%s" -%}
{%- assign today = 'now' | date: "%s" -%}
{%- assign difference = event_date | minus: today -%}
{%- assign difference_days = difference | divided_by: 86400 -%}
Only {{ difference_days }} days until your move!
```
{% endraw %}

#### Solución 2: Consolidar Liquid en una sola línea {#solution-2-consolidate-liquid-onto-a-single-line}

Elimina todos los saltos de línea para que el Liquid quede en una sola línea continua:

{% raw %}
```liquid
{% assign event_date = {{custom_attribute.${PreferredPickupDate}}} | date: "%s" %}{% assign today = 'now' | date: "%s" %}{% assign difference = event_date | minus: today %}{% assign difference_days = difference | divided_by: 86400 %}Only {{ difference_days }} days until your move!
```
{% endraw %}

Ambos enfoques evitan líneas vacías no deseadas en tu mensaje renderizado. Esto aplica al editor de arrastrar y soltar de mensajes dentro de la aplicación, al editor de arrastrar y soltar de correo electrónico y a los Content Blocks con Liquid. Para más información, consulta la documentación de Shopify sobre [control de espacios en blanco](https://shopify.github.io/liquid/basics/whitespace/) y la [sintaxis de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#liquid-syntax) de Braze.

### ¿Por qué mi Content Block no aparece en **Row** en la herramienta de búsqueda de arrastrar y soltar? {#why-is-my-content-block-missing-from-row-in-the-drag-and-drop-search-tool}

Algunos Content Blocks no aparecen en **Row** en la búsqueda del editor de arrastrar y soltar. Añade un bloque HTML desde la pestaña **Content** (**Advanced**) y luego inserta la etiqueta de Liquid del Content Block en ese bloque HTML para renderizar el contenido del bloque.

### ¿Por qué la vista previa de mi Content Block de arrastrar y soltar difiere de la vista de composición? {#why-does-my-drag-and-drop-content-block-preview-differ-from-the-compose-view}

Cuando creas una plantilla de un Content Block con Liquid, las consultas de medios móviles en el bloque pueden no aplicarse en la vista previa de la misma forma que cuando arrastras el bloque directamente a un mensaje. Arrastrar el bloque conserva el diseño, pero lo desvincula del bloque de origen, por lo que las ediciones futuras del bloque ya no actualizan el mensaje automáticamente.

### ¿Cómo puedo previsualizar los valores de propiedades de evento en el creador de mensajes? {#how-do-i-preview-event-property-values-in-message-composer}

Usa **vista previa as Custom User** e introduce valores de muestra de propiedades de evento personalizado para el usuario que previsualices. Esto también es útil para mensajes con lógica de cancelación cuando necesitas valores de vista previa que no desencadenen una cancelación.

## Liquid en los mensajes de correo electrónico {#liquid-in-email-messages}

### ¿Por qué mi mensaje se aborta con "Invalid from email address for recipient:"? {#why-does-my-message-abort-with-invalid-from-email-address-for-recipient}

Este aborto ocurre cuando el Liquid en la dirección **De** produce una sintaxis no válida, como una variable faltante, espacios adicionales o caracteres no permitidos. Haz una vista previa con un usuario de prueba y verifica que la dirección **De** renderizada coincida con tu dominio de envío configurado.

### ¿Cómo creo una dirección de respuesta dinámica? {#how-do-i-create-a-dynamic-reply-to-address}

Usa Liquid en el campo **Responder a** cuando tu espacio de trabajo admita la configuración dinámica de responder a. Combínalo con la configuración del nombre de visualización **De** según sea necesario. Consulta [Configuración de correo electrónico]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences) para ver las opciones específicas del espacio de trabajo.

## Solución de problemas de errores de Liquid {#troubleshooting-liquid-errors}

### ¿Por qué mi código Liquid no funciona si parece correcto? {#why-is-my-liquid-code-not-working-when-it-looks-correct}

Si tu código Liquid parece sintácticamente correcto pero no funciona, comprueba si hay comillas tipográficas (comillas curvas como `' '` o `" "`) y guiones tipográficos (guiones largos como `—`) en lugar de comillas rectas (`' '` o `" "`) y guiones cortos (`-`). Liquid solo reconoce caracteres ASCII rectos, por lo que las comillas y guiones tipográficos provocarán errores de análisis.

Esto suele ocurrir cuando la configuración del teclado de macOS **Usar comillas y guiones tipográficos** está habilitada, lo que convierte automáticamente los caracteres mientras escribes en el panel de Braze.

Para desactivar esta configuración en macOS:

1. Ve a **Configuración del sistema** > **Teclado** > **Entrada de texto** > **Editar**.
2. Desmarca **Usar comillas y guiones tipográficos**.

| Ejemplo | Comillas curvas (no funciona) | Comillas rectas (funciona) |
| --- | --- | --- |
| Valor predeterminado | {% raw %}`{{${first_name} | default: 'Torchie'}}`{% endraw %} | {% raw %}`{{${first_name} | default: 'Torchie'}}`{% endraw %} |
| Condicional | {% raw %}`{% if ${country} contains 'US' %}`{% endraw %} | {% raw %}`{% if ${country} contains 'US' %}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Ejemplos de comillas tipográficas" }

Esto aplica a valores predeterminados, condicionales y cualquier otro Liquid que use comillas. Las comillas curvas y rectas pueden verse iguales en pantalla, así que compara tu código cuidadosamente o pégalo en un editor de texto sin formato.

Para más información sobre el uso de comillas en Liquid, consulta [Sintaxis de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#liquid-syntax).

### ¿Por qué veo un error de Liquid "Unexpected end token"? {#why-am-i-seeing-an-unexpected-end-token-liquid-error}

Este error generalmente indica llaves de más o faltantes. No anides {% raw %}`{{ }}`{% endraw %} dentro de otra expresión de etiqueta Liquid. Por ejemplo, usa {% raw %}`{{custom_attribute.${date_of_birth} | date: '%s'}}`{% endraw %} en lugar de envolver la referencia del atributo en un par adicional de llaves.

### ¿Por qué el reintento de contenido conectado no está disponible para mi mensaje dentro de la aplicación? {#why-is-connected-content-retry-unavailable-for-my-in-app-message}

{% raw %}
La etiqueta `{% connected_content %}` con reintento no es compatible con todos los tipos de mensajes, incluidos algunos formatos de mensajes dentro de la aplicación. Elimina los parámetros de reintento o usa un canal compatible para las llamadas de contenido conectado con reintento.
{% endraw %}

### ¿Por qué veo "Liquid Error: Comparison of Time with String Failed"? {#why-am-i-seeing-liquid-error-comparison-of-time-with-string-failed}

Este error ocurre al comparar un atributo personalizado de tipo tiempo o una propiedad de evento directamente con un valor en blanco (una cadena vacía). Liquid no admite comparaciones directas entre tipos de datos diferentes, como un objeto de tiempo y una cadena.

El siguiente es un ejemplo común que causa este error:

{% raw %}
```liquid
{% if {{custom_attribute.${expiration_date}}} == blank %}
  <a>Some words</a>
{% endif %}
```
{% endraw %}

Esto falla porque no puedes comparar un atributo personalizado con un tipo de datos de tiempo con una cadena (`blank`).

Para resolverlo, convierte el atributo de tiempo a una cadena asignándolo a una variable y usando el filtro `default` cuando el atributo se evalúa como vacío en el momento del renderizado:

{% raw %}
```liquid
{% assign expiration_date = {{custom_attribute.${expiration_date}}} | default: "" %}

{% if expiration_date == blank %}
  <a>Example Words</a>
{% endif %}
```
{% endraw %}


Al comparar un atributo personalizado de tipo tiempo con la hora actual o fechas futuras, usa el mismo enfoque:

{% raw %}
```liquid
{% assign today = 'now' | date: '%s' %}
{% assign month = 'now' | date: '%s' | plus: 2592000 %}
{% assign expiration_date = {{custom_attribute.${expiration_date}}} | default: "" %}

{% if expiration_date == blank %}
  <a>Example Words</a>
{% elsif expiration_date >= today and expiration_date >= month %}
  <a>More Words</a>
{% endif %}
```
{% endraw %}