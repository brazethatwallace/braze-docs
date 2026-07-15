---
nav_title: Etiqueta message extras
article_title: Etiqueta message extras
page_order: 1
description: "Este artículo explica cómo usar la etiqueta de Liquid message extras y cómo comprobar la sintaxis."
alias: "/message_extras_tag/"
---

# Etiqueta de Liquid message extras {#message-extras-liquid-tag}

> Usa la etiqueta de Liquid `message_extras` para anotar tus eventos de envío con datos dinámicos de contenido conectado, catálogos, atributos personalizados (como idioma, país), propiedades de entrada de Canvas u otros orígenes de datos.

La etiqueta de Liquid `message_extras` añade pares clave-valor al evento de envío correspondiente en Currents y Uso compartido de datos de Snowflake.

Para enviar datos dinámicos o adicionales a tu evento de envío de Currents o Uso compartido de datos de Snowflake, inserta la etiqueta de Liquid adecuada en el cuerpo de tu mensaje.

Este es un ejemplo del formato estándar de la etiqueta de Liquid para `message_extras`:

{% raw %}
```liquid
{% message_extras :key test :value 123 %}
```
{% endraw %}

Puedes añadir estas etiquetas según sea necesario para tus pares clave-valor en el cuerpo del mensaje. Sin embargo, la longitud de todas las claves y valores no debe superar los 1000 bytes (1&nbsp;KB). En Currents y Uso compartido de datos de Snowflake, verás un nuevo campo de evento llamado `message_extras` para tus eventos de envío. Esto genera una cadena serializada en JSON en un solo campo.

## Cómo se envían los datos de message extras usando Currents {#how-message-extras-data-is-sent-using-currents}

Los **message extras** son pares clave-valor adjuntos en el momento del envío. La configuración depende del canal. Para correo electrónico, se añaden mediante encabezados. Para push en iOS, se incluyen en la carga útil del push. Todos los eventos de envío compatibles muestran el mismo campo `message_extras` en Currents (y Snowflake) una vez que se envía el mensaje.

## Canales compatibles {#supported-channels}

La etiqueta `message_extras` es compatible con todos los tipos de mensaje que tienen un evento de envío, junto con los eventos de impresión de mensajes dentro de la aplicación. Usar `message_extras` con mensajes dentro de la aplicación requiere cumplir con ciertas [versiones mínimas del SDK](#iam-sdk).

## Cómo usar la etiqueta `message_extras` {#how-to-use-the-message_extras-tag}

1. En el cuerpo del mensaje para el canal, introduce la etiqueta de Liquid `message_extras`. O bien, puedes usar el modal **Añadir personalización** y seleccionar **Message Extras** para el tipo de personalización.

![El modal Añadir personalización con Message Extras seleccionado como tipo de personalización.]({% image_buster /assets/img_archive/message_extras1.png %}){: style="max-width:35%;"}

{: start="2"}

2. Introduce el [par clave-valor]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/key_value_pairs) para cada etiqueta `message_extras`.

![Un ejemplo de pares clave-valor para la etiqueta message extras. El campo de título dice "Your New Favorites". El mensaje muestra pares clave-valor para la etiqueta message extras y la siguiente frase: "We're excited to bring you a side selection of fresh and exciting products that are sure to become your new go-to favorites".]({% image_buster /assets/img_archive/message_extras2.png %}){: style="max-width:70%;"}

{: start="3"}

3. Después de que tu campaña o Canvas se haya enviado, Braze adjuntará los datos dinámicos en el momento del envío a través de los eventos de envío de Currents o Uso compartido de datos de Snowflake en el campo `message_extras`.

## Comprobación de la sintaxis {#checking-syntax}

Cualquier otra entrada que no coincida con el estándar de la etiqueta descrito anteriormente puede no pasar a Currents o Snowflake. Comprueba que tu sintaxis o formato no incluya ninguno de los siguientes problemas:

- Delimitadores inexistentes, vacíos o mal escritos
- Claves duplicadas (Braze enviará de forma predeterminada el par clave-valor que se encuentre primero)
- Texto adicional antes de que se definan las claves o los valores
- Claves y valores desordenados
  - {% raw %}Por ejemplo, `{% message_extras :value 123 :key test %}`{% endraw %}

## Envío de información de códigos promocionales a Currents {#sending-promotion-code-information-to-currents}

{% multi_lang_include partners/shopify.md section='Liquid promotion codes with Currents' %}

## Consideraciones {#considerations}

- Los pares clave-valor que superen los 1000 bytes (1&nbsp;KB) se truncarán.
- Los espacios en blanco cuentan para el recuento de caracteres. Ten en cuenta que Braze omite los espacios en blanco iniciales y finales.
- El JSON resultante solo genera valores de cadena.
- Puedes incluir variables de Liquid como clave o valor, pero no puedes anidar etiquetas de Liquid adicionales dentro de `message_extras`.
  - Por ejemplo, podrías usar el siguiente Liquid: {% raw %}`{% assign value = '123' %} {% assign key = 'test' %} {% message_extras :key {{key}} :value {{value}} %}`{% endraw %}

## Preguntas frecuentes {#frequently-asked-questions}

### ¿Cómo puedo asociar el campo message_extras en los eventos de envío con mis eventos de interacción como aperturas y clics? {#how-can-i-associate-the-message_extras-field-in-the-send-events-to-my-engagement-events-like-opens-and-clicks}

Se genera un `dispatch_id` y se proporciona en tus eventos de envío, que puedes usar como identificador único para vincularlo a eventos específicos de clic, apertura o entrega. Consulta este campo en Currents o Snowflake. Para más información, consulta [Comportamiento del ID de envío]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id).

#### ¿Puedo usar message_extras con mensajes dentro de la aplicación? {#iam-sdk}

Sí, puedes usar `message_extras` en tus mensajes dentro de la aplicación siempre que los dispositivos de tus usuarios tengan las siguientes versiones mínimas del SDK:

{% sdk_min_versions web:5.2.0 android:30.4.0 swift:8.4.0 %}