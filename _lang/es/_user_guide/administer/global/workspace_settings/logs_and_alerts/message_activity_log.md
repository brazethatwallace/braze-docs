---
nav_title: Registro de actividad de mensajes
article_title: "Registro de actividad de mensajes {#dev-console-troubleshooting}"
page_order: 3
page_type: reference
description: "Este artículo de referencia describe el Registro de actividad de mensajes, que te muestra los mensajes asociados a tus campañas y envíos. Aquí también puedes encontrar información."
---

# Registro de actividad de mensajes {#dev-console-troubleshooting}

> El **Registro de actividad de mensajes** te da la oportunidad de ver cualquier mensaje (especialmente mensajes de error) asociado a tus campañas y envíos.

Puedes ver transacciones de campañas de API, solucionar problemas con detalles sobre mensajes fallidos y obtener información sobre cómo mejorar la entrega de notificaciones o resolver problemas técnicos existentes.

Para acceder al registro, ve a **Configuración** > **Configuración y pruebas** > **Registro de actividad de mensajes**.

![Registro de actividad de mensajes]({% image_buster /assets/img_archive/message_activity_log.png %})

{% alert tip %}
Además de este artículo, también te recomendamos consultar nuestro curso de Braze Learning [Herramientas de control de calidad y depuración](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), que explica cómo usar el Registro de actividad de mensajes para realizar tu propia solución de problemas y depuración.
{% endalert %}

Puedes filtrar por el siguiente contenido registrado en el **Registro de actividad de mensajes**:

- Errores de notificaciones push
- Errores de mensajes dentro de la aplicación con plantilla cancelados
- Errores de webhooks
- Errores de correo electrónico
- Registros de mensajes de API
- Errores de contenido conectado
- Errores de audiencia conectada de REST API
- Errores de asignación de alias de usuario
- Errores de pruebas A/B
- Errores de SMS/MMS
- Errores de WhatsApp
- Errores de Live Activity
- Errores de desencadenantes de usuario incorrectos
- Errores de [límite de invocaciones diarias]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#monitor-your-agent) de Braze Agents
- Errores de [modelo]({{site.baseurl}}/user_guide/brazeai/agents/reference#models) no disponible de Braze Agents

Estos mensajes pueden provenir de nuestro propio sistema, de tus aplicaciones o plataformas, o de nuestros socios externos. Esto puede dar lugar a un número infinito de mensajes que pueden aparecer en este registro.

## Comprender los mensajes del registro {#understanding-log-messages}

Para determinar qué significan tus mensajes, presta atención a la redacción de cada mensaje y a las columnas que le corresponden, ya que esto puede ayudarte a solucionar problemas utilizando pistas contextuales.

Por ejemplo, las entradas de **Aborted Message Error** pueden producirse por muchas razones, no solo por [mensajes de cancelación de Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages). Lee la columna **Message** para ver el motivo específico:

- Si el envío fue cancelado por una etiqueta `abort_message` de Liquid, la columna **Message** muestra el fragmento exacto de Liquid que se invocó, por ejemplo {% raw %}`{% abort_message('Module count is less than or equal to 1') %} called`{% endraw %}.
- Para otros motivos de cancelación, la columna **Message** explica por qué se canceló el envío.

### Cargas útiles de Campaigns de API {#api-campaign-payloads}

El registro de actividad de mensajes registra información diferente según el tipo de Campaign de API. El [endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) registra el cuerpo del mensaje (mensajes) en los registros de mensajes de API, mientras que el [endpoint `/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) no registra la carga útil de la solicitud ni las `api_trigger_properties` en el registro de actividad de mensajes.

### Mensajes comunes {#common-messages}

Hay algunos tipos de mensajes comunes que podrías ver, y algunos incluso pueden proporcionar enlaces de solución de problemas para ayudarte a diagnosticar y corregir incidencias.

Los siguientes mensajes se incluyen a modo de ejemplo y podrían no coincidir exactamente con lo que se muestra en la columna **Message** de tu registro.

| Tipo de mensaje | Mensaje posible | Descripción |
|---|---|---|
| Rebote blando | The email address same@example.com soft bounced. | La dirección de correo electrónico era válida y el mensaje llegó al servidor de correo del destinatario, pero fue rechazado por un problema "temporal". <br><br>Las razones comunes de rebote blando incluyen: {::nomarkdown} <ul> <li> El buzón estaba lleno (el usuario superó su cuota) </li> <li> El servidor estaba caído </li> <li> El mensaje era demasiado grande para el buzón de entrada del destinatario </li>  </ul> {:/} Si un correo electrónico recibe un rebote blando, normalmente reintentamos en un periodo de 72 horas, pero el número de reintentos varía de un receptor a otro. |
| Rebote duro | The email account that you tried to reach does not exist. Try double-checking the recipient's email address for typos or unnecessary spaces. | Tu mensaje nunca llegó al buzón de entrada de esta persona porque no existía un buzón al que llegar. Si quieres investigar más, mensajes como este a veces pueden tener enlaces en la columna **View Details** que te permiten ver el perfil del destinatario previsto.|
| Bloqueo | Spam message is rejected because of anti-spam policy. | Tu mensaje fue categorizado como correo no deseado. Este error de correo se registra para un usuario si hemos recibido un evento del ESP indicando que el correo electrónico fue descartado. Podría ser solo para ese destinatario en concreto, pero si ves este mensaje con frecuencia, tal vez quieras reevaluar tus hábitos de envío o el contenido de tu mensaje. Además, piensa: ¿[calentaste tu IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming)? Si no, contacta con Braze para obtener orientación al respecto.|
| Aborted Message Error | {% raw %}`{% abort_message('Module count is less than or equal to 1') %} called`{% endraw %} | Cuando un envío es cancelado por una etiqueta `abort_message` de Liquid, la columna **Message** muestra el fragmento exacto de Liquid que se invocó. Otras entradas de **Aborted Message Error** pueden tener mensajes diferentes que describen el motivo de la cancelación. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Mensajes comunes" }

### ¿Por qué mi mensaje no aparece aquí? {#why-isnt-my-message-listed-here}

Los mensajes en el registro de actividad de mensajes pueden provenir de diversas fuentes: Braze, tus aplicaciones o plataformas, o nuestros partners externos. Esto significa que hay un número infinito de mensajes que podrían aparecer en este registro, así que, como puedes imaginar, ¡no podemos enumerarlos todos!

Por ejemplo, algunos posibles mensajes de "Bloqueo", además del indicado en la tabla anterior, podrían ser:

- Unfortunately, messages from [_IP_ADDRESS_] weren't sent. Please contact your ISP since part of their network is on our block list.
- Message rejected due to local policy.
- The message was blocked by the receiver as spam.
- Service unavailable, Client host [_IP_ADDRESS_] blocked using Spamhaus.

## Período de retención del almacenamiento {#storage-retention-period}

Los errores de las últimas 60 horas están disponibles en los registros de actividad de mensajes. Los registros con más de 60 horas de antigüedad se limpian y ya no son accesibles.

### Número de registros de errores almacenados {#number-of-error-logs-stored}

El número de registros guardados depende de varias condiciones. Por ejemplo, si se envía una Campaign programada a miles de usuarios, podríamos ver potencialmente una muestra de los errores en el registro de actividad de mensajes en lugar de todos los errores. A continuación se presenta un resumen de las condiciones que afectan cuántos registros se guardan:
- Se guardan hasta 20 registros de errores del mismo tipo de error para la misma Campaign o paso en Canvas dentro de una hora de reloj fija para los siguientes tipos de error:
    - Errores de contenido conectado
    - Errores de anulación de mensaje
    - Errores de webhook
    - Errores de rechazo de SMS
    - Errores de fallo de entrega de SMS
    - Errores de fallo de WhatsApp
    - Errores de Pruebas A/B
- Se guardan hasta 20 registros de errores de notificación push del mismo tipo de error para la misma combinación de Campaign o paso en Canvas y aplicación para los siguientes tipos de error:
    - Credencial push no válida
    - Token push no válido
    - Sin credencial push
    - Errores de token
    - Cuota excedida
    - Tiempo de reintentos agotado
    - Carga útil no válida
    - Error inesperado
- Se guardan hasta 100 registros de errores del mismo tipo de error para la misma aplicación dentro de una hora de reloj fija para los siguientes tipos de error:
    - Error de Live Activity (sin credencial push)
    - Error de Live Activity (credencial push no válida)
    - Otros errores de Live Activity
    - Errores de token eliminado por retroalimentación de APN
- Se guardan hasta 100 registros de errores del mismo tipo de error para la misma Campaign o paso en Canvas dentro de una hora de reloj fija para los siguientes tipos de error:
    - Errores de rebote blando de correo electrónico
    - Errores de rebote duro de correo electrónico
    - Errores de bloqueo de correo electrónico
- Se guardan hasta 100 registros de errores de asignación de alias de usuario para el mismo espacio de trabajo dentro de una hora de reloj fija.

## Envíos de prueba {#test-sends}

El **Registro de actividad de mensajes** muestra registros de prueba para estos canales de mensajería:

- SMS
- WhatsApp
- LINE
- KakaoTalk
- Webhook

Los registros de envíos de prueba no están disponibles para los siguientes canales: correo electrónico, Content Cards, mensajes dentro de la aplicación y push.

Los registros de envíos de prueba tienen el prefijo "[TEST SEND]", pero no se garantiza que todos los registros de envíos de prueba tengan el prefijo (por ejemplo, los errores de contenido conectado no tienen el prefijo).