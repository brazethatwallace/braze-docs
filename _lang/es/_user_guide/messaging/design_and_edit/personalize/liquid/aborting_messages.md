---
nav_title: Cancelar mensajes
article_title: Cancelar mensajes con Liquid
page_order: 7
description: "Este artículo de referencia cubre la cancelación de mensajes con Liquid y algunos ejemplos de casos de uso."

---

# Cancelar mensajes {#abort-messages}

> Opcionalmente, puedes usar la etiqueta de mensaje Liquid `abort_message("optional reason for aborting")` dentro de condicionales para evitar el envío de un mensaje a un usuario. Este artículo de referencia enumera algunos ejemplos de cómo se puede usar esta característica en campañas de marketing.

{% alert note %}
Si un paso de mensaje se cancela en un Canvas, el usuario **no** saldrá del Canvas y **sí** avanzará al siguiente paso.
{% endalert %}

## Envíos de prueba con `abort_message()` {#test-sends-with-abort_message}

`abort_message()` detiene el envío para los usuarios que no cumplen tu condición. El mensaje no aparecerá en su perfil y no contará para las entregas ni para la limitación de frecuencia.

Si los envíos de prueba nunca llegan, previsualiza como un usuario que satisface la condición de cancelación, luego en **Test Send** habilita **Override recipients' attributes with current preview user's attributes** (o añade un miembro del grupo de prueba de contenido que cumpla los requisitos).

## Cancelar mensaje si "Number Games Attended" = 0 {#abort-message-if-number-games-attended-0}

Por ejemplo, supongamos que no quieres enviar un mensaje a clientes que no han asistido a un juego:

{% raw %}
```liquid
{% if custom_attribute.${Number_Game_Attended} == 1 %}
Loved the game? Get 10% off your second one with code SAVE10.
{% elsif custom_attribute.${Number_Game Attended} > 1 %}
Love the games? Get 10% off your next one with code SAVE10.
{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

Este mensaje solo se enviará a clientes que se sabe que han asistido a un juego.

## Enviar mensajes solo a clientes de habla inglesa {#message-english-speaking-customers-only}

Puedes enviar mensajes solo a clientes de habla inglesa creando una sentencia "if" que coincida cuando el idioma del cliente sea inglés y una sentencia "else" que cancele el mensaje para cualquiera que no hable inglés o no tenga un idioma en su perfil.

{% raw %}
```liquid

{% if ${language} == 'en' %}
Send this message in English!
{% else %}
{% abort_message() %}
{% endif %}
```

De forma predeterminada, Braze registrará un mensaje de error genérico en tu Registro de actividad de mensajes:

```text
{% abort_message %} called
```

También puedes hacer que el mensaje de cancelación registre algo en tu Registro de actividad de mensajes incluyendo una cadena dentro de los paréntesis:

```liquid
{% abort_message('language was nil') %}
```
{% endraw %}

![Registro de errores de mensajes en la consola para desarrolladores con un mensaje de cancelación de "language was nil".]({% image_buster /assets/img_archive/developer_console.png %})

## Consultar mensajes de cancelación {#query-for-abort-messages}

Puedes usar el [Generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/) o tu propio almacén de datos, si está conectado a Braze, para consultar mensajes de cancelación específicos que se desencadenan cuando la lógica Liquid provoca la cancelación de un mensaje.

## Cuándo se evalúa la lógica de cancelación {#when-abort-logic-is-evaluated}

El momento en que se evalúa la lógica de cancelación depende del canal de mensaje.

### Push, correo electrónico, SMS, webhooks y Content Cards {#push-email-sms-webhooks-and-content-cards}

La lógica de cancelación se evalúa en el momento del envío, cuando Braze procesa el mensaje para su entrega.

### Mensajes dentro de la aplicación {#in-app-messages}

La lógica de cancelación se evalúa solo para [mensajes dentro de la aplicación con plantilla]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/#templated_iam-templated) en el momento en que se desencadena el mensaje dentro de la aplicación (por ejemplo, cuando el usuario realiza el evento desencadenante o inicia una sesión), no cuando el mensaje se envía inicialmente al dispositivo. Los mensajes dentro de la aplicación se entregan al SDK al inicio de la sesión y se almacenan en caché localmente; el Liquid, incluidas las llamadas a `abort_message()`, se ejecuta cuando se cumple la condición de desencadenamiento.

## Consideraciones {#considerations}

La etiqueta de mensaje Liquid `abort_message()` evita que los mensajes se envíen a los usuarios, lo que significa que el mensaje no se mostrará en los perfiles de usuario y no contará para las entregas ni para la limitación de frecuencia.