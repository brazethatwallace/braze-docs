---
nav_title: Registro de actividad de mensajes
article_title: Registro de actividad de mensajes
page_order: 3
page_type: reference
description: "Este artículo de referencia describe el Registro de actividad de mensajes, que te muestra los mensajes asociados a tus campañas y envíos. Aquí también puedes encontrar información sobre cómo entender los mensajes del registro."

---

# Registro de actividad de mensajes {#dev-console-troubleshooting}

> El **Registro de actividad de mensajes** te da la oportunidad de ver cualquier mensaje (especialmente mensajes de error) asociado a tus campañas y envíos.

Puedes ver transacciones de campañas de API, solucionar problemas con detalles sobre mensajes fallidos y obtener información sobre cómo mejorar la entrega de notificaciones o resolver problemas técnicos existentes.

Para acceder al registro, ve a **Configuración** > **Registro de actividad de mensajes**.

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

Para determinar qué significan tus mensajes, presta atención a la redacción de cada mensaje y a las columnas que le corresponden, ya que esto puede ayudarte a solucionar problemas usando pistas contextuales.

Por ejemplo, si tienes una entrada de registro cuyo mensaje dice "empty-cart_app" y no estás seguro de lo que significa, mira a la izquierda en la columna **Tipo**. Si ves "Error de mensaje cancelado", puedes asumir con seguridad que el mensaje fue lo que se escribió como [mensaje de cancelación]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages#abort-messages) usando Liquid, y que el mensaje fue cancelado porque el destinatario previsto del mensaje tenía un carrito vacío en tu aplicación.

### Mensajes comunes {#common-messages}

Hay algunos tipos de mensajes comunes que podrías ver, y algunos incluso pueden proporcionar enlaces de solución de problemas para ayudarte a diagnosticar y corregir incidencias.

Los siguientes mensajes listados son a modo de ejemplo y pueden no coincidir exactamente con lo que se muestra en la columna **Mensaje** de tu registro.

| Tipo de mensaje | Mensaje potencial | Descripción |
|---|---|---|
| Rebote blando | La dirección de correo electrónico same@example.com tuvo un rebote blando. | La dirección de correo electrónico era válida y el mensaje llegó al servidor de correo del destinatario, pero fue rechazado por un problema "temporal". <br><br>Las razones comunes de rebote blando incluyen: {::nomarkdown} <ul> <li> El buzón estaba lleno (el usuario superó su cuota) </li> <li> El servidor estaba caído </li> <li> El mensaje era demasiado grande para el buzón del destinatario </li>  </ul> {:/} Si un correo electrónico ha recibido un rebote blando, normalmente reintentamos en un período de 72 horas, pero el número de reintentos varía de un receptor a otro. |
| Rebote duro | La cuenta de correo electrónico que intentaste alcanzar no existe. Intenta verificar la dirección de correo electrónico del destinatario en busca de errores tipográficos o espacios innecesarios. | Tu mensaje nunca llegó al buzón de entrada de esta persona porque no había un buzón al que llegar. Si quieres profundizar más, mensajes como este a veces pueden tener enlaces en la columna **Visualizar detalles** que te permiten ver el perfil del destinatario previsto.|
| Bloqueo | El mensaje de correo no deseado fue rechazado debido a la política antispam. | Tu mensaje fue categorizado como correo no deseado. Este error de correo se registra para un usuario si hemos recibido un evento del ESP indicando que el correo electrónico fue descartado. Podría ser solo para ese destinatario previsto, pero si ves este mensaje con frecuencia, es posible que quieras reevaluar tus hábitos de envío o el contenido de tu mensaje. Además, piensa: ¿[calentaste tu IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming)? Si no, ponte en contacto con Braze para obtener asesoramiento sobre cómo hacerlo.|
| Error de mensaje cancelado | empty-cart_web | Si tienes una aplicación con un carrito o creas un envío con un mensaje de cancelación en Liquid, puedes personalizar qué mensaje se te devuelve si el envío se cancela. En este caso, el mensaje devuelto es empty-cart_web.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Mensajes comunes" }

### ¿Por qué mi mensaje no aparece aquí? {#why-isnt-my-message-listed-here}

Los mensajes en el Registro de actividad de mensajes pueden provenir de diversas fuentes: Braze, tus aplicaciones o plataformas, o nuestros socios externos. Esto significa que hay un número infinito de mensajes que podrían aparecer en este registro; como puedes imaginar, ¡no podemos listarlos todos!

Por ejemplo, algunos posibles mensajes de "Bloqueo", además del listado en la tabla anterior, podrían ser:

- Lamentablemente, los mensajes desde [_IP_ADDRESS_] no se enviaron. Por favor, contacta a tu proveedor de servicios de Internet ya que parte de su red está en nuestra lista de bloqueo.
- Mensaje rechazado debido a política local.
- El mensaje fue bloqueado por el receptor como correo no deseado.
- Servicio no disponible, host del cliente [_IP_ADDRESS_] bloqueado usando Spamhaus.

## Período de retención de almacenamiento {#storage-retention-period}

Los errores de las últimas 60 horas están disponibles en los registros de actividad de mensajes. Los registros con más de 60 horas de antigüedad se eliminan y ya no son accesibles.

### Número de registros de errores almacenados {#number-of-error-logs-stored}

El número de registros guardados está influenciado por varias condiciones. Por ejemplo, si una campaña planificada se envía a miles de usuarios, potencialmente veríamos una muestra de los errores en el Registro de actividad de mensajes en lugar de todos los errores. A continuación se presenta un resumen de las condiciones que afectan cuántos registros se guardan:
- Se guardan hasta 20 registros de errores del mismo tipo de error para la misma campaña o paso en Canvas dentro de una hora fija de reloj para los siguientes tipos de error:
    - Errores de contenido conectado
    - Errores de mensajes cancelados
    - Errores de webhooks
    - Errores de rechazo de SMS
    - Errores de fallo de entrega de SMS
    - Errores de fallo de WhatsApp
    - Errores de pruebas A/B
- Se guardan hasta 20 registros de errores de notificaciones push del mismo tipo de error para la misma campaña o paso en Canvas y combinación de aplicación para los siguientes tipos de error:
    - Credencial push no válida
    - Token push no válido
    - Sin credencial push
    - Errores de token
    - Cuota excedida
    - Reintentos agotados
    - Carga útil no válida
    - Error inesperado
- Se guardan hasta 100 registros de errores del mismo tipo de error para la misma aplicación dentro de una hora fija de reloj para los siguientes tipos de error:
    - Error de Live Activity (sin credencial push)
    - Error de Live Activity (credencial push no válida)
    - Otros errores de Live Activity
    - Errores de token eliminado por retroalimentación de APNs
- Se guardan hasta 100 registros de errores del mismo tipo de error para la misma campaña o paso en Canvas dentro de una hora fija de reloj para los siguientes tipos de error:
    - Errores de rebote blando de correo electrónico
    - Errores de rebote duro de correo electrónico
    - Errores de bloqueo de correo electrónico
- Se guardan hasta 100 registros de errores de asignación de alias de usuario para el mismo espacio de trabajo dentro de una hora fija de reloj.

## Envíos de prueba {#test-sends}

El **Registro de actividad de mensajes** muestra registros de prueba para estos canales de mensajería:

- SMS
- WhatsApp
- LINE
- KakaoTalk
- Webhook

Los registros de envíos de prueba no están disponibles para los siguientes canales: correo electrónico, Content Cards, mensajes dentro de la aplicación y push.

Los registros de envíos de prueba tienen el prefijo "[TEST SEND]", pero no se garantiza que todos los registros de envíos de prueba tengan el prefijo (por ejemplo, los errores de contenido conectado no tienen el prefijo).