---
nav_title: "Buenas prácticas"
article_title: Buenas prácticas para SMS, MMS y RCS
page_order: 2
description: "Este artículo de referencia cubre las buenas prácticas para SMS/MMS."
alias: /sms_mms_rcs_best_practices/
page_type: reference
channel:
  - SMS
  - MMS
  - RCS



---

# Buenas prácticas para SMS, MMS y RCS {#best-practices-for-sms-mms-and-rcs}

> Obtén más información sobre las buenas prácticas para SMS, MMS y RCS con Braze, incluidas nuestras recomendaciones para la supervisión de la cancelación de suscripción y el bombeo de tráfico.

## Recomendaciones de monitorización de cancelación de suscripción {#opt-out-monitoring-recommendations}

Cumplir con las solicitudes de los destinatarios para cancelar la suscripción a las comunicaciones es un requisito legal. No cumplir con las solicitudes de los destinatarios de SMS para cancelar la suscripción del canal puede conllevar sanciones, incluidas multas, y puede dar lugar a demandas judiciales. Braze dispone de funciones para permitir una gestión sólida de la adhesión voluntaria y la cancelación de suscripción de SMS y MMS, además de mecanismos para garantizar que las solicitudes se procesen correctamente.

Conforme a sus acuerdos de suscripción con nosotros, nuestros clientes son los únicos responsables de cumplir con la legislación aplicable en el uso de nuestros servicios. En consecuencia, recomendamos encarecidamente que los clientes presten especial atención a la configuración correcta de su configuración de SMS, que prueben esas configuraciones a fondo, tomen medidas para monitorizar el cumplimiento de las cancelaciones de suscripción y actúen con prontitud si identifican casos de incumplimiento con las solicitudes de cancelación de suscripción.

Al configurar SMS y MMS en Braze para gestionar las adhesiones voluntarias y cancelaciones de suscripción, consulta la siguiente lista de recursos:
* [Grupos de suscripción de SMS]({{site.baseurl}}/sms_rcs_subscription_groups): Grupos de suscripción y métodos y estados de adhesión voluntaria y cancelación de suscripción.
* [REST APIs de grupos de suscripción]({{site.baseurl}}/api/endpoints/subscription_groups): Cómo procesar las adhesiones voluntarias y cancelaciones de suscripción recibidas desde una fuente que no sea una respuesta directa a un mensaje.
* [Procesamiento de palabras clave]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing): Explicaciones sobre cómo Braze aborda el procesamiento y la gestión de palabras clave.
* [Doble adhesión voluntaria de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in): Requiere que los usuarios confirmen explícitamente su intención de adhesión voluntaria antes de poder recibir mensajes SMS. La doble adhesión voluntaria de SMS es un requisito en algunos países, por lo que Braze recomienda configurarla.
* [Envío de mensajes SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sms_sending): Aspectos básicos del envío de SMS en Braze, incluida la importancia de los grupos de suscripción, los requisitos para los segmentos de SMS y los cuerpos de los mensajes, y más.

### Consideraciones {#considerations}

Cuando SMS y MMS están configurados en múltiples instancias, una configuración incorrecta puede provocar que las cancelaciones de suscripción de Campaign o Canvas se envíen al espacio de trabajo incorrecto.

* Braze cuenta con monitorización para identificar dichas instancias. Si se detecta este comportamiento, Braze redirige las cancelaciones de suscripción a la instancia correcta y recupera todas las cancelaciones de suscripción que se produjeron durante el periodo.
* Recomendamos encarecidamente que los clientes prueben las cancelaciones de suscripción para cada grupo de suscripción que tengan en Braze. Identificar este problema antes de lanzar un mensaje es mejor que mitigarlo después de que se haya detectado un problema.

Braze gestiona las suscripciones de SMS/MMS tanto a nivel del perfil de usuario (`user_id`) como a nivel del número de teléfono (`channel_id`). Cuando un número de teléfono se adhiere voluntariamente o cancela la suscripción, la actualización se aplica a todos los perfiles que comparten ese número. En el caso de que un usuario final se haya adherido voluntariamente con un número de teléfono determinado, pero luego cambie de número, el nuevo número hereda el estado del grupo de suscripción del usuario. En consecuencia, si un usuario final ha cancelado la suscripción, pero luego vuelve a ingresar a la aplicación o sitio web con un nuevo número de teléfono, no recibirá mensajes no deseados.

## Recomendaciones de higiene de la lista de números de teléfono {#phone-number-list-hygiene-recommendations}

Mantener la higiene de la lista de números de teléfono te ayuda a conservar datos válidos de consentimiento y alcanzabilidad a lo largo del tiempo. Braze marca algunos números de teléfono como no válidos para ayudar a reducir el riesgo de cumplimiento, apoyar las prácticas de mensajería basadas en el consentimiento y evitar envíos a números que pueden ya no pertenecer al usuario original.

Para conocer las razones por las que los números de teléfono suelen marcarse como no válidos, consulta [Gestión de números de teléfono no válidos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#handling-invalid-phone-numbers).

Recomendamos el siguiente flujo de trabajo para eliminar números de teléfono no válidos:

1. Identifica los números de teléfono afectados a través del [endpoint `/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers).
2. Diferencia entre números de teléfono que están desactivados, marcados como no válidos debido a errores del proveedor y marcados como no válidos debido a problemas de formato (`invalid_format`, como números que no cumplen con E.164). Usa el filtro `reason` en la API de números de teléfono no válidos para consultar por categoría. Para más información, consulta [Gestión de números de teléfono no válidos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#handling-invalid-phone-numbers).
3. Para números de teléfono desactivados, vuelve a verificar el número de teléfono con el usuario. Después de que el usuario confirme su número de teléfono, elimina el número de teléfono de la lista de no válidos a través del [endpoint `/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers).

## Recomendaciones sobre el tráfico inflado {#traffic-pumping-recommendations}

### ¿Qué es el tráfico inflado? {#what-is-traffic-pumping}

El tráfico inflado es una forma de fraude que ocurre cuando un actor malintencionado utiliza un formulario en línea para provocar el envío masivo de mensajes SMS (por ejemplo, mensajes de adhesión voluntaria o contraseñas de un solo uso). El actor malintencionado configura un número de tarificación especial para que estos mensajes se envíen a dicho número y reclama una participación en los ingresos del operador móvil con el que se ha establecido el número de tarificación especial, generando así ingresos ilícitos.

### Cómo detectar el tráfico inflado {#how-to-spot-traffic-pumping}

* Los números de tarificación especial que respaldan este tipo de estafa se configuran a menudo, aunque no siempre, en países fuera de tus zonas geográficas de envío habituales.
* Picos inusuales en el envío de mensajes desde formularios en línea pueden indicar tráfico inflado.
    * Te recomendamos configurar [alertas de Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/campaign_alerts) para limitar y notificar si se envía un número implausiblemente alto de mensajes.
* Los formularios en línea incompletos pueden indicar un llenado programático del formulario.
* Al crear formularios en línea, te recomendamos establecer reglas para asegurar que los formularios se completen en su totalidad y utilizar herramientas como CAPTCHA para minimizar el riesgo.

### Impacto del tráfico inflado {#impact-of-traffic-pumping}

Los clientes son responsables de supervisar el tráfico que envían y se les factura por todos los SMS enviados a través de su cuenta. Entre Braze y el cliente, el cliente es la parte en mejor posición para detectar y prevenir el tráfico inflado.

## Envío de SMS a múltiples países {#multi-country-sms-sending}

Algunas marcas pueden desear enviar mensajes a un grupo de usuarios que tienen números de teléfono de distintos países. Para enviar un mensaje SMS a un número de teléfono en un país determinado, la buena práctica es utilizar un código largo o código abreviado del mismo país. De hecho, los códigos abreviados solo pueden enviar SMS a números de teléfono del mismo país en el que se creó el código abreviado.

Para superar esta limitación, durante el [proceso de configuración]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups) de los grupos de suscripción, se pueden configurar grupos que contengan códigos largos y abreviados de varios países diferentes. Una vez completado, los números de teléfono con el mismo código de país que el número de teléfono del usuario objetivo se utilizan automáticamente al lanzar una Campaign. No necesitas crear Campaigns separadas para usuarios con números de teléfono con diferentes códigos de país, lo que te permite lanzar una Campaign o usar un componente de Canvas para dirigirte a los usuarios relevantes.

![Las cargas útiles de SMS se envían utilizando el mismo código de país que el número de teléfono del usuario objetivo.]({% image_buster /assets/img/sms/multi_country_subgroups.png %})

### Buenas prácticas generales de envío {#general-sending-best-practices}

1. **Obtén permiso.** Una de las reglas más importantes para el uso de SMS como empresa es que primero debes obtener el permiso de los clientes para contactarlos. No hacerlo puede dañar tu marca y resultar en costosas sanciones legales.
2. **Elige el número adecuado para tu caso de uso.** Tres tipos principales de números de teléfono pueden enviar y recibir mensajes SMS: códigos largos, códigos abreviados e IDs alfanuméricos de remitente, y sus capacidades y disponibilidad en distintas regiones varían. Piensa de antemano si a tu empresa le conviene más un código personalizado.
3. **Presta atención al momento.** Ten en cuenta que los clientes responden mejor a los materiales que se dirigen directamente a ellos. Un poco de personalización marca una gran diferencia, como usar el nombre del destinatario o agregar un toque conversacional que refleje los intereses de tus clientes.
4. **Participa en conversaciones bidireccionales.** El SMS es un canal tan eficaz para interactuar con los clientes que es importante anticipar y gestionar eficazmente las respuestas a tus mensajes. El 85% de los consumidores no solo quieren poder recibir información, sino también responder a las empresas o entablar una conversación.
5. **Mide lo que funciona.** ¿Estás llegando a los clientes en el momento adecuado, con la mejor frecuencia y usando las llamadas a la acción más eficaces? Utilizar las herramientas de seguimiento adecuadas puede ofrecer métricas directas y medibles que demuestren su ROI.

## Envío de gran volumen {#high-volume-sending}

¿Planeas hacer envíos de gran volumen? Tenemos algunas buenas prácticas para que todo funcione sin problemas.

- Ajusta el límite de velocidad de entrega para tu Campaign o Canvas según sea necesario, en función del tamaño del público objetivo. Esto garantiza que alcances el volumen de envío que necesitas y que Braze envíe los mensajes a la tasa que tu proveedor de SMS o RCS espera y puede manejar.
- Asegúrate de respetar el límite de 160 caracteres, y ten en cuenta que los caracteres especiales cuentan doble (por ejemplo, barras invertidas `\`, acentos circunflejos `^` y tildes `~`).

## Recomendaciones de horas tranquilas {#quiet-hours-recommendations}

{% alert warning %}
**Las horas tranquilas nativas de Braze no garantizan los horarios de entrega a nivel de dispositivo.** Cuando se envía un mensaje, se entrega a un operador. Una vez que el operador acepta el mensaje, Braze ya no tiene control sobre el momento preciso en que se entrega al dispositivo del usuario.<br><br> Por ejemplo, si un mensaje se entrega a un operador a las 8:59 pm, puede que no llegue al dispositivo hasta las 9:02 pm. Para reducir el riesgo, recomendamos usar el siguiente método de horas tranquilas basado en Liquid. Esto suprime el mensaje a nivel del motor de Braze antes de la entrega al operador.
{% endalert %}

### Horas tranquilas nativas de Braze {#braze-native-quiet-hours}

Puedes habilitar las [horas tranquilas]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing#quiet-hours) en Campaigns y Canvas de SMS como un control adicional de programación. Para envíos sensibles al cumplimiento normativo, usa la protección basada en Liquid de la siguiente sección como tu control principal antes de que los mensajes se entreguen a los operadores.

### Protección adicional mediante Content Blocks {#additional-safeguard-through-content-blocks}

Puedes añadir una verificación basada en Liquid dentro de un Content Block. Esto proporciona una protección fiable y escalable que funciona junto con la configuración nativa.

#### Configuración {#setup}

Incluye el siguiente fragmento de código en la parte superior del cuerpo de tu mensaje SMS. Este ejemplo cancela el envío si cae fuera de una ventana de 9 am a 9 pm en la [zona horaria local]({{site.baseurl}}/user_guide/messaging/campaigns/faq#what-does-local-time-zone-delivery-offer) del usuario.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}
{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour >= 21 or hour < 9 %}
  {% abort_message("Outside allowed time window") %}
{% endif %}
```
{% endraw %}

#### Consideraciones

- {% raw %}`time_zone: ${time_zone}`{% endraw %} permite que la ventana se evalúe según la hora local de cada usuario, no una hora global fija, como se explica en las [preguntas frecuentes sobre Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/faq#what-does-local-time-zone-delivery-offer).
- Los mensajes suprimidos por {% raw %}`abort_message()`{% endraw %} no se reprograman para el día siguiente; se cancelan.
- {% raw %} De forma predeterminada, los mensajes cancelados no son visibles en los informes estándar de Campaign. Sin embargo, cuando Liquid cancela un envío con `{% abort_message %}`, Braze lo registra en el registro de actividad de mensajes como un error de mensaje (por defecto muestra `{% abort_message %}` llamado). Si pasas una cadena, esa razón es la que aparece en el registro, como `{% abort_message('language was nil') %}`{% endraw %}. Para tener visibilidad de estas supresiones en el panel, contacta con tu administrador de éxito de cliente para obtener acceso al [panel de diagnóstico de mensajería]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard).