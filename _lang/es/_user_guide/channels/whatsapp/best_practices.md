---
nav_title: Buenas prácticas
article_title: Buenas prácticas
page_order: 22
description: "Este artículo describe las buenas prácticas sugeridas al utilizar el canal de mensajería de WhatsApp, incluyendo cómo mantener una calificación de calidad del teléfono alta y evitar una tasa elevada de bloqueos e informes."
page_type: reference
channel:
  - WhatsApp

---
# Buenas prácticas de WhatsApp {#whatsapp-best-practices}

> Antes de enviar tus mensajes de WhatsApp, consulta estas buenas prácticas sugeridas para mantener una calificación de calidad del teléfono alta, evitar bloqueos e informes, y gestionar la adhesión voluntaria y la cancelación de suscripción de los usuarios.

## Mantener una calificación de calidad del teléfono alta {#maintain-a-high-phone-quality-rating}

WhatsApp basa su [calificación de calidad del teléfono](https://www.facebook.com/business/help/896873687365001) en las acciones que realizan los usuarios que reciben tus mensajes, como bloquear o reportar tu empresa. Es importante mantener una calificación de calidad alta porque, si es baja y no mejora en un periodo determinado, tu límite de mensajería puede disminuir.

La primera vez que envías un mensaje a un usuario en WhatsApp, estas opciones se muestran dentro del hilo del mensaje.

![Hilo de mensajes de WhatsApp con opciones para bloquear o reportar una empresa]({% image_buster /assets/img/whatsapp/whatsapp_block_report.png %}){: style="max-width:30%;"}

{% alert note %}
Para ver métricas sobre tus bloqueos e informes, asegúrate de que la [pestaña Insights](https://www.facebook.com/business/help/683499390267496) esté activada en tu WhatsApp Manager.
{% endalert %}

Para evitar altas tasas de bloqueos e informes, Braze sugiere las siguientes buenas prácticas para mantener una calificación de calidad del teléfono alta y límites de mensajería estables.

### Seguir los requisitos y directrices de adhesión voluntaria de WhatsApp {#follow-whatsapp-opt-in-requirements-and-guidelines}

Asegúrate de que todos los usuarios hayan dado su consentimiento activo para recibir mensajes de WhatsApp antes de comenzar a comunicarte con ellos por WhatsApp. Al solicitar la adhesión voluntaria de los usuarios, se les debe informar de que están aceptando específicamente recibir mensajes de tu empresa a través de WhatsApp.

{% alert note %}
Para obtener información sobre los requisitos de adhesión voluntaria y consejos útiles, consulta [Get Opt-in for WhatsApp](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/).
{% endalert %}

### Seguir las buenas prácticas de mensajería {#follow-messaging-best-practices}

- Haz que el nombre de tu canal refleje tu marca para que los usuarios reconozcan que el mensaje proviene de ti y no es correo no deseado.
- Envía un mensaje de confirmación a los usuarios después de recopilar su consentimiento de adhesión voluntaria.
- Envía mensajes en horarios apropiados.

### Dar a los clientes la opción de cancelar suscripción {#give-customers-the-option-to-opt-out}

Las cancelaciones de suscripción no afectan tu calificación de calidad del teléfono, por lo que es mejor que un usuario cancele su suscripción a las comunicaciones de WhatsApp en lugar de bloquearte o reportarte.

Una buena práctica sugerida es proporcionar instrucciones sobre cómo cancelar la suscripción en el pie del primer mensaje que envíes a los usuarios. Por ejemplo, podrías indicar que los usuarios pueden cancelar su suscripción a tu canal de WhatsApp respondiendo con tu palabra clave de cancelación. También podrías incluir regularmente el pie de cancelación de suscripción en futuras campañas. Para aprender cómo configurar esto, consulta [Adhesión voluntaria y cancelación de suscripción]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs).

![Mensaje de WhatsApp con un pie que indica responder STOP para cancelar la suscripción al canal]({% image_buster /assets/img/whatsapp/whatsapp_unsubscribe.png %}){: style="max-width:35%;"}