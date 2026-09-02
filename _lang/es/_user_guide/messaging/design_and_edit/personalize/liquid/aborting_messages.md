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

`abort_message()` detiene el envío para los usuarios que no cumplen tu condición. El mensaje no aparecerá en su perfil y no contará como entrega ni para la limitación de frecuencia.

Si los envíos de prueba nunca llegan, previsualiza como un usuario que satisface la condición de cancelación y, a continuación, en **Test Send** habilita **Override recipients' attributes with current vista previa user's attributes** (o añade un miembro de un grupo de prueba de contenido que cumpla los requisitos).

## Abortar mensaje si "Number Games Attended" = 0 {#abort-message-if-number-games-attended-0}

Por ejemplo, supongamos que no quieres enviar un mensaje a clientes que no han asistido a un partido:

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

Este mensaje solo se enviará a los clientes que se sabe que han asistido a un partido.

## Enviar mensajes solo a clientes de habla inglesa {#message-english-speaking-customers-only}

Puedes enviar mensajes solo a clientes de habla inglesa creando una sentencia "if" que coincida cuando el idioma de un cliente sea inglés, y una sentencia "else" que anule el mensaje para cualquier persona que no hable inglés o que no tenga un idioma en su perfil.

{% raw %}
```liquid

{% if ${language} == 'en' %}
Send this message in English!
{% else %}
{% abort_message() %}
{% endif %}
```

De forma predeterminada, Braze registrará un mensaje de error genérico en tu registro de actividad de mensajes:

```text
{% abort_message %} called
```

También puedes hacer que el mensaje de anulación registre algo en tu registro de actividad de mensajes incluyendo una cadena dentro de los paréntesis:

```liquid
{% abort_message('language was nil') %}
```
{% endraw %}

![Registro de errores de mensajes en la consola para desarrolladores con un mensaje de anulación que dice "language was nil".]({% image_buster /assets/img_archive/developer_console.png %})

## Consultar mensajes de cancelación {#query-for-abort-messages}

Puedes usar el [Generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder) o tu propio almacén de datos, si está conectado a Braze, para consultar mensajes de cancelación específicos que se desencadenan cuando la lógica de Liquid provoca la cancelación de un mensaje.

## Cuándo se evalúa la lógica de cancelación {#when-abort-logic-is-evaluated}

El momento en que se evalúa la lógica de cancelación depende del canal de mensaje.

### Push, correo electrónico, SMS, webhooks y Content Cards {#push-email-sms-webhooks-and-content-cards}

La lógica de cancelación se evalúa en el momento del envío, cuando Braze procesa el mensaje para su entrega.

### In-App Messages {#in-app-messages}

La lógica de cancelación se evalúa para [mensajes dentro de la aplicación con plantilla]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages#templated_iam-templated) solo en el momento en que se activa el mensaje dentro de la aplicación (por ejemplo, cuando el usuario realiza el evento desencadenante o inicia una sesión), no cuando el mensaje se envía inicialmente al dispositivo. Los mensajes dentro de la aplicación se entregan al SDK al inicio de la sesión y se almacenan en caché de forma local; el Liquid, incluidas las llamadas a `abort_message()`, se ejecuta cuando se cumple la condición de activación.

## Solución de problemas de tasas de cancelación altas {#troubleshooting-high-abort-rates}

Si un Campaign o un paso en Canvas muestra que muchos usuarios ingresaron pero hay pocos envíos, o las entregas parecen más bajas de lo esperado, la lógica de cancelación es una causa común, especialmente cuando Liquid requiere atributos, datos de catálogo o valores de lista que faltan en el momento de la evaluación.

### Consulta el registro de actividad de mensajes {#check-the-message-activity-log}

1. En el panel de Braze, abre el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) del Campaign o del paso de mensaje en Canvas.
2. Filtra por entradas relacionadas con cancelaciones. De forma predeterminada, Braze registra las llamadas a {% raw %}`{% abort_message %}`{% endraw %}. Si pasaste una cadena de motivo a `abort_message()`, ese texto aparece en su lugar.
3. Observa si las cancelaciones se agrupan en un canal (por ejemplo, solo correo electrónico) o en varios canales dentro del mismo Canvas.

### Verifica los atributos y Liquid en el momento del envío {#verify-attributes-and-liquid-at-send-time}

Para push, correo electrónico, SMS, webhooks y Content Cards, la lógica de cancelación se ejecuta cuando Braze procesa el mensaje para la entrega, no cuando el usuario ingresó a un Canvas ni cuando un evento desencadenante se activó anteriormente.

- Confirma que los [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) requeridos, las propiedades del evento o los campos de [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs) estén configurados en el usuario antes de que se ejecute el paso de mensaje.
- Agrega comprobaciones explícitas de nil o vacío antes de llamar a `abort_message()`. Una rama `else` que cancela cuando falta un valor detiene el envío para cualquier usuario sin esos datos.
- Si la personalización depende de una lista, un Segment o una respuesta de contenido conectado, confirma que los datos estén disponibles cuando se ejecute el paso de mensaje. Un usuario puede ingresar a un Canvas antes de que la pertenencia a la lista o los datos posteriores estén listos.

### Comportamiento específico de Canvas {#canvas-specific-behavior}

Si un paso de mensaje se cancela en un Canvas, el usuario no sale del Canvas. En su lugar, avanza al siguiente paso. Las cancelaciones afectan únicamente el recuento de envíos de ese paso de mensaje.

Al diagnosticar cancelaciones en Canvas:

- Compara los usuarios que ingresaron en el paso de mensaje con los usuarios enviados en el mismo paso.
- Si solo un canal se cancela, revisa el Liquid específico del canal o el estado de suscripción de ese paso.
- Si las cancelaciones aumentan después de una actualización de lista o catálogo, verifica si el paso de mensaje se ejecutó antes de que se completara la actualización.

### Valida con vista previa y envíos de prueba {#validate-with-preview-and-test-sends}

Previsualiza como un usuario en el creador de mensajes cuyo perfil coincida con un destinatario afectado. Para envíos de prueba, habilita **Reemplazar los atributos de los destinatarios con los atributos del usuario de vista previa actual** cuando tu lógica de cancelación dependa de datos del perfil.

Para más ejemplos de cancelación, consulta [Consultar mensajes de cancelación](#query-for-abort-messages).

## Consideraciones {#considerations}

La etiqueta de mensaje Liquid `abort_message()` evita que los mensajes se envíen a los usuarios, lo que significa que el mensaje no se mostrará en los perfiles de usuario y no contará para las entregas ni para la limitación de frecuencia.