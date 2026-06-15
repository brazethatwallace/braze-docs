---
nav_title: Doble adhesión voluntaria
article_title: Doble adhesión voluntaria
description: "Este artículo de referencia cubre la función de doble adhesión voluntaria y explica cómo habilitar la función, seleccionar palabras clave de adhesión voluntaria y mensajes de respuesta, e incorporar usuarios al flujo de trabajo de doble adhesión voluntaria a través de actualizaciones de suscripción que ocurren en REST API, SDK y actualizaciones del centro de preferencias."
page_type: reference
page_order: 1
channel:
  - SMS
  - MMS
  - RCS
---

# Doble adhesión voluntaria {#double-opt-in}

> La función de doble adhesión voluntaria requiere que los usuarios confirmen explícitamente su intención de adhesión voluntaria antes de poder recibir mensajes SMS, MMS o RCS. Esto enfoca la mensajería en usuarios comprometidos y apoya las mejores prácticas de cumplimiento.

Cuando la doble adhesión voluntaria está activada, se envía a los usuarios un mensaje que solicita su consentimiento explícito antes de que puedan recibir mensajes de tus Campaigns o Canvas.

Aunque no es un requisito explícito de la Ley de Protección al Consumidor Telefónico de 1991 (TCPA), Braze recomienda que configures la doble adhesión voluntaria para confirmar que los usuarios están informados y dan su consentimiento para formar parte de tu programa de SMS, MMS o RCS. Para más información sobre cumplimiento, consulta [Leyes, regulaciones y prevención de abuso para SMS, MMS y RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations/).

## Flujos de trabajo de doble adhesión voluntaria {#double-opt-in-workflows}

La doble adhesión voluntaria te permite obtener consentimiento explícito a través de campañas de adhesión voluntaria de entrada y de salida.

### De salida {#outbound}

Cuando un usuario proporciona su número de teléfono, se le envía un mensaje que solicita su consentimiento.

![Captura de pantalla de un mensaje SMS de salida donde la marca envía "¡Bienvenido a las actualizaciones de texto de BRAND! 1 mensaje por semana con las últimas ofertas. Responde Y para la adhesión voluntaria.", el usuario responde con "Y" y la marca responde con "¡Gracias! Ahora estás suscrito a las alertas de BRAND. Aquí tienes un código promocional SMS10 para un 10% de descuento en tu primera compra."]({% image_buster /assets/img/double_opt_in_outbound.png %}){:style="max-width:40%;"}

### De entrada {#inbound}

Cuando un usuario envía un mensaje que contiene una palabra clave de adhesión voluntaria, se le envía un mensaje que solicita su consentimiento.

![Captura de pantalla de un mensaje SMS de entrada donde un usuario envía "JOIN" y recibe la respuesta "Responde Y para confirmar que quieres unirte a nuestro programa de SMS. 3 mensajes/semana, envía STOP en cualquier momento para STOP", y luego responde "Y".]({% image_buster /assets/img/double_opt_in_inbound.png %}){:style="max-width:40%;"}

## Habilitar la doble adhesión voluntaria {#enabling-double-opt-in}

Para activar la doble adhesión voluntaria, ve a la tabla **Global Keywords** en el grupo de suscripción correspondiente y haz clic en **Edit** en la **Opt-In Keyword Category**. A continuación, selecciona tu método de adhesión voluntaria (**Opt-In** o **Double Opt-In**). Seleccionar **Double Opt-In** expandirá la página para mostrar [campos configurables](#configurable-fields) adicionales.

![La sección de método de adhesión voluntaria tiene dos métodos de adhesión voluntaria para elegir: Opt-In y Double Opt-In.]({% image_buster /assets/img/double_opt_in_method.png %}){:style="max-width:50%;"}

### Campos configurables {#configurable-fields}

| Categoría   |    Campos    | Descripción
| ----------- |----------- |----------------
| Mensaje de adhesión voluntaria | Palabras clave | Estas son las palabras clave que un usuario puede enviar por mensaje de texto para indicar su intención de adhesión voluntaria. `START` es una palabra clave obligatoria. Este mensaje de adhesión voluntaria también se enviará al usuario cuando su estado de suscripción sea actualizado por las fuentes listadas en la sección [Fuentes de suscripción](#subscription-sources).
| | Mensaje de respuesta | Esta es la respuesta inicial que un usuario recibirá después de enviar una palabra clave de adhesión voluntaria (por ejemplo, "Responde Y para confirmar que deseas recibir mensajes de este número. Pueden aplicarse tarifas de mensajes y datos.")
| Confirmación de doble adhesión voluntaria | Palabras clave | Estas son las palabras clave con las que un usuario puede responder para confirmar su intención de adhesión voluntaria. Se requiere al menos una palabra clave. Estas palabras clave deben especificarse en el campo **Mensaje de respuesta del mensaje de adhesión voluntaria**.
| | Mensaje de respuesta | Esta es la respuesta de confirmación que un usuario recibirá después de haber confirmado explícitamente su adhesión voluntaria y ahora puede recibir mensajes. El estado del grupo de suscripción del usuario se establecerá como `Subscribed`.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Configurable fields #configurable-fields" }

Cuando un usuario recibe un mensaje de adhesión voluntaria, tiene 30 días para confirmar su intención de adhesión voluntaria. Si un usuario desea suscribirse después de la ventana de 30 días, necesita enviar una palabra clave de adhesión voluntaria para iniciar el flujo de trabajo de doble adhesión voluntaria nuevamente.

![Los campos configurables tienen dos secciones, Mensaje de adhesión voluntaria y Confirmación de doble adhesión voluntaria, cada una con los campos Palabras clave y Mensaje de respuesta.]({% image_buster /assets/img/double_opt_in_fields.png %})

## Estado del grupo de suscripción {#subscription-group-status}

Solo después de que el usuario complete el flujo de trabajo de doble adhesión voluntaria se actualiza su [estado del grupo de suscripción]({{site.baseurl}}/sms_rcs_subscription_groups/) a `Subscribed`. Si el usuario comienza el flujo de trabajo pero no lo completa, permanece como `Unsubscribed` y no se le pueden enviar mensajes desde ese grupo de suscripción.

Los usuarios también pueden ingresar al flujo de trabajo de doble adhesión voluntaria si están [suscritos desde otras fuentes]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/) (por ejemplo, REST API, SDK).

## Fuentes de suscripción {#subscription-sources}

Los usuarios también pueden ingresar al flujo de trabajo de doble adhesión voluntaria a través de actualizaciones de suscripción que ocurren fuera de los mensajes de entrada. Estas fuentes incluyen actualizaciones desde REST API, SDK y el centro de preferencias. Cuando un usuario ingresa al flujo de trabajo de doble adhesión voluntaria a través de estas fuentes, recibirá el **mensaje de respuesta del mensaje de adhesión voluntaria**.

{% alert important %}
Cuando los usuarios ingresan al flujo de trabajo de doble adhesión voluntaria a través de fuentes distintas a los mensajes de entrada, reciben como máximo un mensaje de respuesta de adhesión voluntaria en un período continuo de 24 horas, independientemente del número de veces que ingresen a este flujo de trabajo.
{% endalert %}

Cada fuente de suscripción tiene un comportamiento de inscripción diferente, como se describe en la siguiente tabla.

Fuente    | Comportamiento de inscripción en doble adhesión voluntaria
----------- | -----------
SDK | Los usuarios ingresarán automáticamente al flujo de trabajo de doble adhesión voluntaria cuando se suscriban a través del SDK de Braze.
REST API | Los usuarios pueden ingresar al flujo de trabajo cuando el estado de suscripción se establece a través de `/subscription/status/set`, `/v2/subscription/status/set` o `/users/track` y se pasa el parámetro opcional `use_double_opt_in_logic` como `true` (por ejemplo, [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed", "use_double_opt_in_logic": true}]). Si se omite este parámetro, los usuarios no ingresarán al flujo de trabajo de doble adhesión voluntaria.
Shopify | Los usuarios no ingresarán al flujo de trabajo de doble adhesión voluntaria cuando su estado de suscripción sea establecido por nuestra integración con Shopify.
Importación de usuarios | Los usuarios no ingresarán al flujo de trabajo de doble adhesión voluntaria cuando su estado de suscripción sea establecido por la importación de usuarios.
[Centro de preferencias]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/) | Los usuarios ingresarán automáticamente al flujo de trabajo de doble adhesión voluntaria cuando se suscriban a través de un centro de preferencias.
Paso de actualización de usuario | Los usuarios pueden ingresar al flujo de trabajo de doble adhesión voluntaria cuando su estado de suscripción se establece a través del paso de actualización de usuario y se pasa el parámetro opcional `use_double_opt_in_logic` como `true`. Si se omite este parámetro, los usuarios no ingresarán al flujo de trabajo de doble adhesión voluntaria.
{: .reset-td-br-1 .reset-td-br-2 aria-label="Subscription sources #subscription-sources" }

## Asistencia en varios idiomas {#multi-language-support}
Para mensajes de entrada, la doble adhesión voluntaria es compatible con todos los idiomas definidos en el grupo de suscripción. Esto significa que puedes definir tus respuestas automáticas en diferentes idiomas y Braze enviará la respuesta automática asociada con un idioma específico cuando se reciba una palabra clave coincidente.

Los usuarios que ingresen al flujo de trabajo de doble adhesión voluntaria a través de actualizaciones de suscripción que ocurren fuera de los mensajes de entrada (por ejemplo, SDK, REST API, Shopify) solo recibirán las palabras clave en inglés.