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

## Recomendaciones para el monitoreo de la cancelación de suscripción {#opt-out-monitoring-recommendations}

Cumplir con las solicitudes de los destinatarios para cancelar la suscripción a las comunicaciones es un requisito legal. No cumplir con las solicitudes de los destinatarios de SMS para cancelar la suscripción al canal puede acarrear sanciones, incluidas multas, y puede derivar en demandas judiciales. Braze cuenta con características para permitir una gestión robusta de la adhesión voluntaria y la cancelación de suscripción de SMS y MMS, además de mecanismos para ayudar a garantizar que las solicitudes se procesen correctamente.

Según sus acuerdos de suscripción con nosotros, nuestros clientes son los únicos responsables de cumplir con la legislación aplicable en su uso de nuestros servicios. En consecuencia, recomendamos encarecidamente que los clientes presten especial atención a la configuración correcta de su configuración de SMS, que prueben exhaustivamente dichas configuraciones, tomen medidas para monitorear el cumplimiento de las cancelaciones de suscripción y actúen con prontitud en caso de identificar casos de incumplimiento con las solicitudes de cancelación.

Al configurar SMS y MMS en Braze para gestionar las adhesiones voluntarias y cancelaciones de suscripción, consulta la siguiente lista de recursos:
* [Grupos de suscripción de SMS]({{site.baseurl}}/sms_rcs_subscription_groups): grupos de suscripción y métodos y estados de adhesión voluntaria/cancelación de suscripción.
* [API REST de grupos de suscripción]({{site.baseurl}}/api/endpoints/subscription_groups): cómo procesar adhesiones voluntarias y cancelaciones de suscripción recibidas de una fuente distinta a una respuesta directa a un mensaje.
* [Procesamiento de palabras clave]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing): explicaciones sobre cómo Braze aborda el procesamiento y la gestión de palabras clave.
* [Doble adhesión voluntaria de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in): requiere que los usuarios confirmen explícitamente su intención de adhesión voluntaria antes de poder recibir mensajes SMS. La doble adhesión voluntaria de SMS es un requisito en algunos países, por lo que Braze recomienda configurarla.
* [Envío de mensajes SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sms_sending): aspectos fundamentales del envío de SMS en Braze, incluida la importancia de los grupos de suscripción, los requisitos para los segmentos de SMS y los cuerpos de los mensajes, y más.

### Consideraciones {#considerations}

Cuando SMS y MMS están configurados en varias instancias, una mala configuración puede provocar que las cancelaciones de suscripción de Campaign o Canvas se envíen al espacio de trabajo incorrecto.

* Braze cuenta con monitoreo para identificar estos casos. Si se detecta este comportamiento, Braze aplica esas cancelaciones de suscripción a la instancia correcta y completa retroactivamente cualquiera que haya ocurrido durante el período.
* Recomendamos encarecidamente que los clientes prueben las cancelaciones de suscripción para cada grupo de suscripción que tengan en Braze. Identificar este problema antes de lanzar un mensaje es mejor que mitigarlo después de que se haya detectado.

Braze gestiona las suscripciones de SMS/MMS tanto a nivel del perfil de usuario (`user_id`) como a nivel del número de teléfono (`channel_id`). Cuando se registra la adhesión voluntaria o la cancelación de suscripción de un número de teléfono, la actualización se aplica a todos los perfiles que comparten ese número. En el caso en que un usuario se haya suscrito con un determinado número de teléfono y luego cambie de número, el nuevo número hereda el estado del grupo de suscripción del usuario. En consecuencia, si un usuario ha cancelado su suscripción pero luego vuelve a ingresar a la aplicación o al sitio web con un nuevo número de teléfono, no recibirá mensajes no deseados.

## Recomendaciones de higiene de la lista de números de teléfono {#phone-number-list-hygiene-recommendations}

Mantener la higiene de la lista de números de teléfono te ayuda a conservar datos válidos de consentimiento y alcanzabilidad a lo largo del tiempo. Braze marca algunos números de teléfono como no válidos para ayudar a reducir el riesgo de cumplimiento, apoyar las prácticas de mensajería basadas en el consentimiento y evitar enviar mensajes a números que pueden ya no pertenecer al usuario original.

Para conocer las razones por las que los números de teléfono suelen marcarse como no válidos, consulta [Gestión de números de teléfono no válidos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/user_phone_numbers#handling-invalid-phone-numbers).

Recomendamos el siguiente flujo de trabajo para eliminar números de teléfono no válidos:

1. Identifica los números de teléfono afectados a través del [endpoint `/sms/invalid_phone_numbers`]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers).
2. Diferencia entre los números de teléfono que están desactivados y los números de teléfono que recibieron errores del proveedor.
3. Para los números de teléfono desactivados, vuelve a verificar el número de teléfono con el usuario. Después de que el usuario confirme su número de teléfono, elimina el número de teléfono de la lista de no válidos a través del [endpoint `/sms/invalid_phone_numbers/remove`]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers).

## Recomendaciones sobre el inflado de tráfico {#traffic-pumping-recommendations}

### ¿Qué es el inflado de tráfico? {#what-is-traffic-pumping}

El inflado de tráfico es una forma de fraude que ocurre cuando un actor malicioso utiliza un formulario en línea para desencadenar el envío masivo de mensajes SMS (por ejemplo, mensajes de adhesión voluntaria o contraseñas de un solo uso). El actor malicioso configura un número de tarifa premium para que estos mensajes se envíen a dicho número y reclama una participación en los ingresos del operador móvil con el que se ha configurado el número de tarifa premium, generando así ingresos ilícitos.

### Cómo detectar el inflado de tráfico {#how-to-spot-traffic-pumping}

* Los números de tarifa premium que respaldan este tipo de estafa a menudo, aunque no siempre, se configuran en países fuera de tus zonas geográficas de envío habituales.
* Los picos inusuales en el envío de mensajes desde formularios en línea pueden indicar inflado de tráfico.
    * Recomendamos configurar [alertas de Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/campaign_alerts) para limitar y notificar si se envía un número inverosímilmente alto de mensajes.
* Los formularios en línea incompletos pueden indicar un llenado programático de formularios.
* Al crear formularios en línea, recomendamos establecer reglas para garantizar que los formularios se completen en su totalidad y utilizar herramientas como CAPTCHA para minimizar el riesgo.

### Impacto del inflado de tráfico {#impact-of-traffic-pumping}

Los clientes son responsables de monitorear el tráfico que envían y se les factura por todos los SMS enviados a través de su cuenta. Entre Braze y el cliente, el cliente es la parte que se encuentra en una mejor posición para detectar y prevenir el inflado de tráfico.

## Envío de SMS a varios países {#multi-country-sms-sending}

Algunas marcas pueden querer enviar mensajes a un grupo de usuarios que tienen números de teléfono de diferentes países. Para enviar un mensaje SMS a un número de teléfono en un país determinado, la buena práctica es utilizar un código largo o código abreviado del mismo país. De hecho, los códigos abreviados solo pueden enviar SMS a números de teléfono del mismo país en el que se creó el código abreviado.

Para superar esta limitación, durante el [proceso de configuración]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups) de los grupos de suscripción, se pueden configurar grupos que contengan códigos largos y abreviados de varios países diferentes. Una vez completado, los números de teléfono de envío con el mismo código de país que el número de teléfono del usuario objetivo se utilizarán automáticamente al lanzar una Campaign. No tendrás que crear Campaigns separadas para usuarios con números de teléfono con diferentes códigos de país, lo que te permite lanzar una Campaign o usar un componente de Canvas para dirigirte a los usuarios relevantes.

![Las cargas útiles del SMS se envían utilizando el mismo código de país que el número de teléfono del usuario objetivo.]({% image_buster /assets/img/sms/multi_country_subgroups.png %})

### Buenas prácticas generales de envío {#general-sending-best-practices}

1. **Obtén permiso.** Una de las reglas más importantes para usar SMS como empresa es que primero debes obtener permiso de los clientes para contactarlos. No hacerlo puede dañar tu marca y resultar en cuantiosas multas legales.
2. **Elige el número adecuado para tu caso de uso.** Tres tipos principales de números de teléfono pueden enviar y recibir mensajes SMS: códigos largos, códigos abreviados e identificadores alfanuméricos de remitente, y sus capacidades y disponibilidad en diferentes regiones varían. Piensa con antelación si a tu empresa le conviene más un código personalizado.
3. **Presta atención al momento.** Ten en cuenta que los clientes son más receptivos a los materiales que se dirigen directamente a ellos. Un poco de personalización marca una gran diferencia, como usar el nombre del destinatario o añadir un toque conversacional que refleje los intereses de tus clientes.
4. **Participa en conversaciones bidireccionales.** SMS es un canal tan efectivo para interactuar con los clientes que es importante anticiparse y manejar eficazmente las respuestas a tus mensajes. El 85 % de los consumidores no solo quiere poder recibir información, sino también responder a las empresas o participar en una conversación.
5. **Mide lo que funciona.** ¿Estás llegando a los clientes en el momento adecuado, con la mejor frecuencia y utilizando las llamadas a la acción más efectivas? Usar las herramientas de seguimiento adecuadas puede ofrecer métricas directas y medibles que demuestren su ROI.

## Envío de alto volumen {#high-volume-sending}

¿Planeas realizar envíos de alto volumen? Tenemos algunas buenas prácticas para ti que te ayudarán a que todo funcione sin problemas.

- Ajusta el límite de velocidad de entrega de tu Campaign o Canvas según sea necesario, en función del tamaño del público objetivo. Esto garantiza que alcances el volumen de envío que necesitas y que Braze envíe los mensajes a la tasa que Twilio espera y puede manejar.
- Asegúrate de respetar el límite de 160 caracteres y ten en cuenta que los caracteres especiales cuentan doble (por ejemplo, barras invertidas `\`, acentos circunflejos `^` y virgulillas `~`).

## Recomendaciones de horas tranquilas {#quiet-hours-recommendations}

{% alert warning %}
**Las horas tranquilas nativas de Braze no garantizan los tiempos de entrega a nivel del dispositivo.** Cuando se envía un mensaje, se entrega a un operador. Una vez que el operador acepta el mensaje, Braze ya no tiene control sobre el momento exacto en que se entrega al dispositivo del usuario.<br><br> Por ejemplo, si un mensaje se entrega a un operador a las 8:59 pm, puede que no llegue al dispositivo hasta las 9:02 pm. Para reducir el riesgo, te recomendamos utilizar el siguiente método de horas tranquilas basado en Liquid. Esto suprime el mensaje a nivel del motor de Braze antes de la transferencia.
{% endalert %}

### Horas tranquilas nativas de Braze {#braze-native-quiet-hours}

Recomendamos encarecidamente habilitar las [horas tranquilas]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing#quiet-hours) en todas las Campaigns y Canvas de SMS para ayudar a cumplir con las regulaciones regionales y las buenas prácticas.

### Protección adicional a través de Content Blocks {#additional-safeguard-through-content-blocks}

Puedes añadir una verificación basada en Liquid dentro de un bloque de contenido. Esto proporciona una protección fiable y escalable que funciona junto con la configuración nativa.

#### Configuración {#setup}

Incluye el siguiente fragmento de código en la parte superior del cuerpo de tu mensaje SMS. Este ejemplo aborta el envío si cae fuera de una ventana de 9 am a 9 pm en la [zona horaria local]({{site.baseurl}}/user_guide/messaging/campaigns/faq#what-does-local-time-zone-delivery-offer) del usuario.

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

- {% raw %}`time_zone: ${time_zone}`{% endraw %} permite que la ventana se evalúe en función de la hora local de cada usuario, no de una hora global fija, como se explica en las [preguntas frecuentes de Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/faq#what-does-local-time-zone-delivery-offer).
- Los mensajes suprimidos por {% raw %}`abort_message()`{% endraw %} no se reprograman para el día siguiente; se cancelan.
- {% raw %} De forma predeterminada, los mensajes abortados no son visibles en los informes estándar de Campaign. Sin embargo, cuando Liquid aborta un envío con `{% abort_message %}`, Braze lo registra en el registro de actividad de mensajes como un error de mensaje (de forma predeterminada muestra `{% abort_message %}` llamado). Si pasas una cadena, esa razón es lo que se muestra en el registro, como `{% abort_message('language was nil') %}`{% endraw %}. Para tener visibilidad de estas supresiones en el panel, contacta con tu CSM para obtener acceso al [panel de diagnóstico de mensajería]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder/diagnostics_dashboard).