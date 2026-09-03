---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre SMS, MMS y RCS
page_order: 30
description: "Este artículo responde a las preguntas más frecuentes sobre la mensajería SMS, MMS y RCS."
page_type: FAQ
alias: /sms_mms_rcs_faq/
channel:
  - SMS
  - MMS
  - RCS
---

# Preguntas frecuentes {#frequently-asked-questions}

> Este artículo responde a las preguntas más frecuentes sobre la mensajería SMS, MMS y RCS.

## General {#general}

### ¿Qué es un `app_id` en el objeto de la API de SMS? {#what-is-an-app_id-in-the-sms-api-object}

La clave de API del identificador de la aplicación, o `app_id`, es un parámetro que asocia la actividad con una aplicación específica en tu espacio de trabajo. Designa con qué aplicación dentro del espacio de trabajo estás interactuando. Por ejemplo, tienes un `app_id` para tu aplicación iOS, un `app_id` para tu aplicación Android y un `app_id` para tu integración web.

Para SMS, el parámetro `app_id` es obligatorio cuando envías mensajes SMS a través de la API (como el endpoint `/messages/send`). Especifica qué aplicación de tu espacio de trabajo está asociada con la actividad de SMS o la llamada a la API. Puedes usar cualquier `app_id` válido de una aplicación configurada en tu espacio de trabajo para la mensajería SMS, independientemente de si el usuario tiene esa aplicación específica en su perfil.

Puedes encontrar tu `app_id` navegando a **Configuración** > **Configuración de la aplicación** y localizando la sección **Identificación**.

### ¿Qué ocurre si varios usuarios tienen el mismo número de teléfono? {#what-happens-if-multiple-users-have-the-same-phone-number}

Cuando varios perfiles de usuario que comparten un número de teléfono (habilitado para SMS) son elegibles para una Campaign basada en acciones o un componente de Canvas al mismo tiempo, desencadenados por el evento de un SMS entrante, Braze deduplicará a los usuarios a nivel del componente de Canvas. Esto evitará que los usuarios reciban más de un mensaje de texto SMS para un componente de Canvas, incluso si varios usuarios comparten el mismo número de teléfono.

{% alert note %}
Braze no deduplica por número de teléfono para Canvas programados.
{% endalert %}

Braze utilizará el siguiente flujo para determinar el perfil destinatario:
- Comprobar qué perfil recibió SMS más recientemente (hasta hace 7 días); si existe uno, enviarlo a ese usuario.
- Si ninguno ha recibido SMS en los últimos 7 días, enviarlo al usuario que tenga un alias de usuario de "phone" que coincida con el número de teléfono.
- Si ninguno existe, enviarlo a un perfil aleatorio entre los disponibles.

Si recibes una palabra clave "START" o "STOP" desde el número de teléfono compartido, todos los perfiles de usuario serán suscritos y habilitados para SMS o cancelarán su suscripción. Esto también se aplica a los cambios de estado a través de la API. Por ejemplo, si varios perfiles con diferentes ID externos tienen los mismos números de teléfono, un cambio de estado del grupo de suscripción a través de la API actualizará todos los perfiles con ese número de teléfono, incluso si solo se especifica un ID externo.

{% alert important %}
Si escalas a tus usuarios en un Canvas y tienes diferentes horarios de programación para cada componente del Canvas, puedes enviar a un usuario con el mismo correo electrónico o teléfono mensajes duplicados.
{% endalert %}

Para prevenir actualizaciones innecesariamente grandes, Braze actualizará un máximo de 100 perfiles de usuario que comparten un identificador cuando se realiza una actualización de suscripción. Si más de 100 perfiles de usuario comparten el mismo número de teléfono, no todos los perfiles se actualizarán.

### ¿Por qué veo un pico en las suscripciones de SMS de una fuente específica? {#why-do-i-see-a-spike-in-sms-subscriptions-from-a-specific-source}

Si observas un aumento inesperadamente grande en los recuentos de suscripciones, en particular al revisar datos del endpoint [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) a través de Currents, esto puede deberse a perfiles de usuario duplicados.

Cuando se realiza una solicitud al endpoint `/subscription/status/set` con solo un número de teléfono (sin `external_id` proporcionado), Braze actualiza todos los perfiles de usuario que comparten ese número de teléfono. Si tu espacio de trabajo tiene perfiles duplicados, el recuento de usuarios que actualizaron su estado de suscripción se infla, aunque solo un número de teléfono haya cambiado.

Para analizar los datos de suscripción con mayor precisión al extraerlos de Currents, actualiza tu consulta para contar números de teléfono distintos en lugar de contar todos los eventos de cambio de estado de suscripción.

### ¿Qué son los códigos abreviados compartidos? {#what-are-shared-short-codes}

Con un código abreviado compartido, todos los mensajes de texto, sin importar qué empresa u organización los envíe, llegan al dispositivo móvil del consumidor desde el mismo número de teléfono de 5 o 6 dígitos. Si bien los códigos abreviados compartidos son relativamente económicos y están disponibles de inmediato, esto significa que tu empresa no tendrá un código abreviado dedicado.

Algunas desventajas de este enfoque incluyen:

- Si tus clientes cancelan la suscripción a los mensajes de otra empresa que comparte un código abreviado contigo, también habrán cancelado la suscripción a tus mensajes.
- Si una empresa viola las reglas, los mensajes de todas las empresas se suspenden.
- Problemas de seguridad

## Facturación y precios {#billing-and-pricing}

### ¿Cómo se me facturará por SMS? {#how-will-i-be-billed-for-sms}

Además de los cargos por códigos abreviados y códigos largos, Braze proporciona una asignación de mensajes SMS para diferentes países. Es decir, trabajamos contigo para establecer un número determinado de segmentos de mensajes para diferentes países, que utilizarás para enviar campañas de SMS. La facturación se realiza según el número de segmentos de mensajes enviados por país. Para obtener más información sobre cómo se calculan los segmentos de mensajes, consulta nuestra guía de [Segmentos de mensajes y límites de texto]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator). Tu director de cuentas se pondrá en contacto contigo para informarte si te estás acercando a tu límite máximo y proporcionarte informes relevantes para mantenerte al tanto. Para más preguntas sobre excedentes, contacta a tu representante de Braze.

### ¿Los precios de MMS y SMS son diferentes? {#does-mms-and-sms-pricing-differ}

MMS y SMS tienen costos diferentes y se cobran por separado en función del volumen. Contacta al equipo de incorporación de Braze para obtener información sobre precios.

### ¿Cómo puedo evitar excedentes? {#how-can-i-avoid-overages}

Aunque no podemos garantizar que nunca tendrás un excedente, puedes seguir estas precauciones para reducir las probabilidades de superar tus límites asignados:

- Presta atención al número de caracteres en tu SMS. Enviar involuntariamente más de un segmento podría provocar excedentes. Para más detalles, consulta nuestro [desglose de segmentos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator).
- Calcula cuidadosamente los caracteres de tu SMS para tener en cuenta Liquid o contenido conectado. El creador de SMS de Braze en tu panel no estima ni tiene en cuenta el uso de ninguna de estas características.
- Considera el tipo de codificación que utiliza tu mensaje. Si tu mensaje usa codificación GSM-7, generalmente puedes estimar 160 caracteres por segmento de mensaje (menos si usas caracteres de la tabla de extensión GSM-7). Si tu mensaje usa codificación [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set), generalmente puedes estimar 67 caracteres por segmento de mensaje.
- ¡Prueba, prueba y prueba! Siempre prueba tus mensajes SMS antes de lanzarlos, especialmente cuando uses Liquid y contenido conectado.

### Si se envía un mensaje a un teléfono fijo, ¿el mensaje aún contará en mi recuento de envíos de SMS? {#if-a-message-is-sent-to-a-landline-will-the-message-still-count-toward-my-sms-send-count}

En Estados Unidos, Canadá y el Reino Unido:
- Si se envía un SMS a un teléfono fijo, se marca como **No entregado**. El comportamiento de facturación depende de tu proveedor de servicios de SMS. Con Twilio, el intento de entrega se cobra igualmente, por lo que los mensajes marcados como **Enviado**, **Entregado** o **No entregado** en tus registros de mensajes se facturan.
- En el Reino Unido, algunos operadores convierten el SMS en un mensaje de voz, entregando el mensaje.

En otros países:
- Con Twilio, se genera un error y no se te cobra por el intento de envío del mensaje SMS.

### ¿Por qué el panel de Braze me advierte que podría cobrárseme por segmentos de mensaje adicionales cuando mi mensaje tiene menos de 160 (GSM-7) o 67 (UCS-2) caracteres? {#why-is-the-braze-dashboard-warning-me-i-may-be-charged-for-additional-message-segments-when-my-message-is-under-160-gsm-7-or-67-ucs-2-characters}

Es posible que se te cobren segmentos de mensaje adicionales si tienes personalización Liquid incluida en tu mensaje. La creación de plantillas de bloques de contenido no ocurre hasta que el mensaje se está preparando para ser enviado. Cuando editas un SMS con un bloque de contenido, Braze no sabe qué contendrá el bloque de contenido, pero proporciona una estimación aproximada. Recomendamos que los usuarios utilicen el panel de prueba para previsualizar el mensaje y comprender mejor qué esperar.

## Envío y capacidad de entrega {#sending-and-deliverability}

### ¿Se pueden incluir enlaces en un SMS? {#can-you-include-links-in-an-sms}

Puedes incluir cualquier enlace en cualquier Campaign de SMS que desees. Sin embargo, hay algunas consideraciones a tener en cuenta:

- Los enlaces pueden ocupar gran parte del límite de 160 caracteres para SMS. Si incluyes un enlace y texto, podría resultar en dos mensajes SMS en lugar de uno solo.
- Las empresas suelen usar acortadores de enlaces para reducir el impacto del enlace en el recuento de caracteres. Sin embargo, si envías un enlace acortado a través de un código largo, los operadores pueden bloquear o rechazar el mensaje, ya que podrían sospechar de la redirección del enlace.
- Usar un [código abreviado]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup) sería el tipo de número más fiable para incluir enlaces.

Braze también cuenta con su propia función de acortamiento de enlaces que acortará los enlaces y proporcionará análisis de click-through automáticamente. Consulta [Acortamiento de enlaces]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening) para más información.

### ¿Es necesario limitar la velocidad de envío de mensajes SMS? {#do-you-need-to-rate-limit-how-fast-you-send-sms-messages}

La tasa de concurrencia y el rendimiento predeterminados permiten aproximadamente 360.000 mensajes por hora por código abreviado. Un rendimiento adicional requiere códigos abreviados adicionales.

### ¿Cómo se añaden las URL a la lista de permitidos para SMS? {#how-do-you-allowlist-urls-for-sms}

Antes de enviar mensajes SMS que contengan URL a usuarios en determinados países (por ejemplo, Suecia o los países nórdicos), debes registrar estas URL con el operador. Contacta con tu director de cuentas de Braze para obtener ayuda. Este proceso tardará aproximadamente cinco días.

### ¿Cuáles son las mejores prácticas de envío para evitar la detección de correo no deseado en SMS? {#what-are-the-best-sending-practices-to-avoid-spam-detection-for-sms}

1. Asegúrate de que las instrucciones de adhesión voluntaria y cancelación de suscripción sean claras.
2. Asegúrate de que tú (la marca) tienes una relación con el cliente.
3. Asegúrate de que el contenido sea relevante para la relación y para lo que el usuario ha dado su consentimiento para recibir.

Para más directrices sobre cómo evitar la detección de correo no deseado, visita [Directrices sobre leyes y regulaciones de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations).

### ¿Cuántos caracteres utiliza un emoji? {#how-many-characters-does-an-emoji-use}

Los emojis pueden ser complicados, ya que no existe un recuento de caracteres estándar para todos los emojis. Existe el riesgo de que el emoji supere el límite de caracteres y divida el SMS en varios mensajes, a pesar de mostrarse como un solo mensaje en el creador de Braze. Al probar tus mensajes, puedes verificar mejor si un mensaje se dividirá usando nuestra [calculadora de segmentos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator).

## Grupos de suscripción y adhesión/cancelación voluntaria {#subscription-groups-and-opt-inopt-out}

### ¿Cómo se crea la lógica para adhesiones voluntarias selectivas a SMS de modo que los usuarios estén en el grupo de suscripción correcto? {#how-do-you-create-logic-for-selective-opt-ins-to-sms-so-users-are-in-the-right-subscription-group}

Las palabras clave personalizadas se registrarían como eventos personalizados, por lo que deberías crear segmentos basados en las palabras clave que los clientes pueden enviar por mensaje de texto. Por ejemplo, si un usuario se suscribe a SMS para mensajes VIP pero no para alertas, puedes crear un Segment VIP y un Segment de alertas, y luego asignar al usuario al Segment correspondiente.

### Si un usuario envía "Stop" a nuestro código abreviado, ¿se cancela su suscripción del grupo de suscripción? {#if-a-user-texts-stop-to-our-short-code-are-they-unsubscribed-from-the-subscription-group}

¿Cómo se refleja esto en el perfil de usuario? El grupo de suscripción aparece como cancelado en **Configuración de contacto**, y hay eventos personalizados para suscribirse y cancelar suscripción.

### Si un usuario ha cancelado su suscripción y envía una palabra clave a nuestro código abreviado o código largo, ¿recibe la respuesta que configuramos para esa palabra clave en Braze? {#if-a-user-is-opted-out-and-sends-a-keyword-to-our-short-and-long-code-do-they-receive-the-response-we-configured-for-that-keyword-in-braze}

Si un usuario ha cancelado su suscripción y envía una palabra clave de una de las [categorías de palabras clave predeterminadas]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout), recibirá la respuesta correspondiente a esa palabra clave. Si un usuario ha cancelado su suscripción y envía una [palabra clave personalizada]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling), no recibirá la respuesta correspondiente a esa palabra clave.

### ¿Las propiedades de evento de SMS capturan palabras clave dentro de una oración? {#will-sms-event-properties-capture-keywords-in-a-sentence}

Para que una palabra clave sea reconocida dentro de una oración (por ejemplo, "por favor deja de enviarme mensajes"), necesitarás usar una sentencia Liquid en el mensaje para reconocer la palabra específica. Las propiedades de evento tienen un límite de 256 caracteres; fuera de eso, no hay límite de caracteres.

## Pruebas {#testing}

### ¿Los mensajes de texto de prueba cuentan para los límites? {#do-test-text-messages-count-toward-limits}

Sí. Ten esto en cuenta al probar mensajes.

### ¿Un usuario necesita formar parte de un grupo de suscripción de SMS para recibir mensajes de prueba de SMS? {#does-a-user-need-to-be-part-of-an-sms-subscription-group-to-receive-sms-test-messages}

Sí. Los usuarios deben tener un número de teléfono válido, formar parte del grupo de suscripción de SMS utilizado para el envío de prueba y tener al menos un país seleccionado en **Geographic Permissions** para SMS.

### ¿Hay alguna forma de ver si existe un alias en un perfil de usuario? {#is-there-a-way-to-see-if-an-alias-exists-on-a-user-profile}

Los alias no son visibles en el perfil de usuario. Tendrías que usar los endpoints de [Exportar datos de usuario]({{site.baseurl}}/api/endpoints/export) para confirmar que los alias se hayan configurado.

## MMS

### ¿Hay algún cambio en los datos de Currents al enviar un MMS? {#are-there-any-changes-to-currents-data-when-sending-an-mms}

No, se proporcionará el mismo nivel de información al enviar un mensaje MMS.

### ¿Puedo controlar el orden en que se entregan la imagen y el cuerpo del mensaje de un MMS? {#can-i-control-the-order-in-which-the-image-and-message-body-of-an-mms-are-delivered}

Braze no tiene control sobre el orden de visualización cuando se incluyen tanto un cuerpo de mensaje como imágenes en un mensaje MMS. Esto depende de varios factores que incluyen, entre otros:

- El operador que recibe el mensaje
- El dispositivo que recibe el mensaje
- El tamaño total del mensaje

### ¿MMS requiere un proceso de incorporación separado? {#does-mms-require-a-separate-onboarding-process}

No. MMS ahora está incluido en nuestro proceso de incorporación de SMS. Los clientes existentes que ya pasaron por la incorporación pueden comenzar a enviar campañas de MMS después de completar los siguientes pasos:

1. Comprar MMS.
2. Ponerse en contacto con el equipo de incorporación de Braze para solicitar que se active la función de MMS. Esto habilitará MMS y se creará o actualizará un grupo de suscripción de SMS/MMS para ti.

A continuación, el equipo de incorporación de Braze se asegurará de que tus códigos abreviados y largos estén habilitados (en EE. UU. y Canadá) para MMS. También actualizarán tus grupos de suscripción para mostrar tus números actuales que fueron añadidos o habilitados para MMS. Una vez completados estos pasos, puedes enviar mensajes MMS de inmediato desde nuestro creador nativo de SMS.

### ¿Por qué no puedo encontrar MMS en mi panel aunque la función está habilitada? {#why-cant-i-find-mms-on-my-dashboard-even-though-the-feature-is-enabled}

MMS solo se muestra en el panel de Braze cuando un grupo de suscripción se considera "habilitado para MMS". Esto se refleja mediante una etiqueta de MMS al seleccionar el grupo de suscripción en el creador de un mensaje SMS/MMS. Esto significa que al menos un número en el grupo de suscripción es capaz de enviar un mensaje MMS.

Además, ciertas situaciones requerirán que Twilio vuelva a aprobar la habilitación de códigos abreviados que originalmente no tenían MMS habilitado. Este proceso de aprobación puede tardar semanas.

### ¿Por qué mi MMS con una imagen no se envía? {#why-does-my-mms-with-an-image-fail-to-send}

Algunos proveedores de SMS validan el encabezado `Content-Type` en las URL de las imágenes. Si un MMS con una imagen se cancela, confirma que la URL de la imagen alojada devuelve `image/png` u otro tipo de imagen compatible (por ejemplo, con `curl -I <image-url>`). Vuelve a alojar el activo en la biblioteca multimedia de Braze o en un CDN que sirva el `Content-Type` correcto.

### ¿Por qué la imagen de mi tarjeta de contacto no aparece en un MMS? {#why-doesnt-my-contact-card-image-appear-in-an-mms}

Las fotos de las tarjetas de contacto MMS pueden no mostrarse cuando el archivo de la tarjeta de contacto hace referencia a una URL de imagen que el dispositivo del destinatario no puede obtener. Crea la tarjeta de contacto en un teléfono, exporta el archivo y súbelo a la biblioteca multimedia para usarlo en tu mensaje MMS.

## RCS

### ¿Por qué mi mensaje RCS no se muestra correctamente en dispositivos iOS? {#why-doesnt-my-rcs-message-render-accurately-on-ios-devices}

Los mensajes RCS pueden mostrarse de forma diferente en un dispositivo iOS dependiendo del sistema operativo y la aplicación de mensajería. En dispositivos iOS, pueden ocurrir los siguientes comportamientos:

- Las acciones sugeridas de diferentes mensajes RCS en el mismo hilo de conversación pueden agruparse y mostrarse en el orden incorrecto.
- Los botones de tarjetas enriquecidas y las acciones sugeridas que están fuera de la tarjeta enriquecida pueden permanecer visibles incluso después de tocar un botón de tarjeta enriquecida o una acción sugerida.

{% alert note %}
Braze envía la carga útil de RCS que compones, mientras que el cliente de mensajería controla cómo se ordenan, agrupan y ocultan las acciones sugeridas. Asegúrate de probar los mensajes RCS, especialmente aquellos que usan tarjetas enriquecidas con acciones sugeridas o respuestas sugeridas, tanto en dispositivos Android como iOS antes de enviarlos.
{% endalert %}

### ¿Puedo enviar mensajes de voz pregrabados con RCS? {#can-i-send-pre-recorded-voicemails-with-rcs}

Sí, puedes usar mensajes multimedia para admitir archivos de audio.

### ¿Por qué las adhesiones voluntarias por REST API de SMS no coinciden con el **Total de adhesiones voluntarias** en el rendimiento de SMS/MMS/RCS? {#why-do-rest-api-sms-opt-ins-not-match-total-opt-ins-on-smsmmsrcs-performance}

El **Total de adhesiones voluntarias** y el **Total de cancelaciones de suscripción** en el dashboard de [rendimiento de SMS/MMS/RCS]({{site.baseurl}}/user_guide/analytics/dashboards) cuentan los cambios de suscripción impulsados por el manejo de palabras clave de SMS entrantes (por ejemplo, un usuario que envía una palabra clave de adhesión voluntaria a tu código abreviado). No incluyen todas las actualizaciones de suscripción realizadas a través de la REST API, el dashboard u otras fuentes.

Para analizar las adhesiones voluntarias y las cancelaciones de suscripción por fuente, usa el [Generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder) en `USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED` y filtra por `STATE_CHANGE_SOURCE` (por ejemplo, **Rest API** frente a **Inbound Message**).