---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre servicio de mensajes cortos, MMS y RCS
page_order: 30
description: "Este artículo responde a las preguntas más frecuentes sobre la mensajería servicio de mensajes cortos, MMS y RCS."
page_type: FAQ
alias: /sms_mms_rcs_faq/
channel:
  - SMS
  - MMS
  - RCS
---

# Preguntas frecuentes {#frequently-asked-questions}

> Este artículo responde a las preguntas más frecuentes sobre la mensajería servicio de mensajes cortos, MMS y RCS.

## General {#general}

### ¿Qué es un `app_id` en el objeto de la API de servicio de mensajes cortos? {#what-is-an-app_id-in-the-sms-api-object}

La clave de API del identificador de la aplicación, o `app_id`, es un parámetro que asocia la actividad con una aplicación específica en tu espacio de trabajo. Designa con qué aplicación dentro del espacio de trabajo estás interactuando. Por ejemplo, tienes un `app_id` para tu aplicación de iOS, un `app_id` para tu aplicación de Android y un `app_id` para tu integración Web.

Para servicio de mensajes cortos, el parámetro `app_id` es obligatorio al enviar mensajes servicio de mensajes cortos a través de la API (como el endpoint `/messages/send`). Especifica qué aplicación de tu espacio de trabajo está asociada con la actividad de servicio de mensajes cortos o la llamada a la API. Puedes usar cualquier `app_id` válido de una aplicación configurada en tu espacio de trabajo para la mensajería servicio de mensajes cortos, independientemente de si el usuario tiene esa aplicación específica en su perfil.

Puedes encontrar tu `app_id` navegando a **Configuración** > **Configuración de la aplicación** y localizando la sección **Identification**.

### ¿Qué ocurre si varios usuarios tienen el mismo número de teléfono? {#what-happens-if-multiple-users-have-the-same-phone-number}

Cuando varios perfiles de usuario que comparten un número de teléfono (habilitado para servicio de mensajes cortos) son elegibles para una Campaign basada en acciones o un componente de Canvas al mismo tiempo, desencadenados por el evento de un servicio de mensajes cortos entrante, Braze deduplicará a los usuarios a nivel del componente de Canvas. Esto evitará que los usuarios reciban más de un mensaje de texto servicio de mensajes cortos por componente de Canvas, incluso si varios usuarios comparten el mismo número de teléfono.

{% alert note %}
Braze no deduplica por número de teléfono en Canvas programados.
{% endalert %}

Braze utilizará el siguiente flujo para determinar el perfil destinatario:
- Comprobar qué perfil recibió servicio de mensajes cortos más recientemente (hasta hace 7 días); si existe uno, enviarle a ese usuario.
- Si ninguno ha recibido servicio de mensajes cortos en los últimos 7 días, enviar al usuario que tenga un alias de usuario de "phone" que coincida con el número de teléfono.
- Si no existe ninguno, enviar a un perfil aleatorio entre los disponibles.

Si recibes una palabra clave "START" o "STOP" desde el número de teléfono compartido, todos los perfiles de usuario serán suscritos y habilitados para servicio de mensajes cortos, o cancelarán su suscripción. Esto también aplica a los cambios de estado mediante la API. Por ejemplo, si varios perfiles con diferentes ID externos tienen los mismos números de teléfono, un cambio de estado del grupo de suscripción a través de la API actualizará todos los perfiles con ese número de teléfono, aunque solo se especifique un ID externo.

{% alert important %}
Si escalas a tus usuarios en un Canvas y tienes diferentes tiempos de programación para cada componente de Canvas, puedes enviar mensajes duplicados a un usuario con el mismo correo electrónico o número de teléfono.
{% endalert %}

Para evitar actualizaciones innecesariamente grandes, Braze actualizará un máximo de 100 perfiles de usuario que compartan un identificador cuando se realice una actualización de suscripción. Si más de 100 perfiles de usuario comparten el mismo número de teléfono, no todos los perfiles se actualizarán.

### ¿Por qué veo un pico en las suscripciones de servicio de mensajes cortos desde una fuente específica? {#why-do-i-see-a-spike-in-sms-subscriptions-from-a-specific-source}

Si observas un aumento inesperadamente grande en los recuentos de suscripciones, en particular al revisar datos del endpoint [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) a través de Currents, esto puede deberse a perfiles de usuario duplicados.

Cuando se realiza una solicitud al endpoint `/subscription/status/set` solo con un número de teléfono (sin proporcionar `external_id`), Braze actualiza todos los perfiles de usuario que comparten ese número de teléfono. Si tu espacio de trabajo tiene perfiles duplicados, el recuento de usuarios que actualizaron su estado de suscripción se infla, aunque solo un número de teléfono haya cambiado.

Para analizar los datos de suscripción con mayor precisión al consultar desde Currents, actualiza tu consulta para contar números de teléfono distintos en lugar de contar todos los eventos de cambio de estado de suscripción.

### ¿Qué son los códigos abreviados compartidos? {#what-are-shared-short-codes}

Con un código abreviado compartido, todos los mensajes de texto, sin importar qué empresa u organización los envíe, llegan al dispositivo móvil del consumidor desde el mismo número de teléfono de 5-6 dígitos. Aunque los códigos abreviados compartidos son relativamente económicos y están disponibles de inmediato, esto significa que tu empresa no tendrá un código abreviado dedicado.

Algunas desventajas de este enfoque incluyen:

- Si tus clientes cancelan la suscripción a los mensajes de otra empresa que comparte un código abreviado contigo, también habrán cancelado la suscripción a tus mensajes.
- Si una empresa viola las reglas, los mensajes de todas las empresas se suspenden.
- Problemas de seguridad

## Facturación y precios {#billing-and-pricing}

### ¿Cómo se me facturará por servicio de mensajes cortos? {#how-will-i-be-billed-for-sms}

Además de los cargos por códigos abreviados y códigos largos, Braze proporciona una asignación de mensajes servicio de mensajes cortos para diferentes países. Es decir, trabajamos contigo para establecer un número determinado de segmentos del mensaje para diferentes países, que utilizarás para enviar Campaigns de servicio de mensajes cortos. La facturación se realiza según el número de segmentos del mensaje enviados por país. Para obtener más información sobre cómo se calculan los segmentos del mensaje, consulta nuestra guía de [Segmentos del mensaje y límites de texto]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator). Tu director de cuentas se pondrá en contacto contigo para informarte si estás cerca de alcanzar tu máximo, proporcionando informes relevantes para mantenerte al tanto. Para más preguntas sobre excedentes, contacta con tu representante de Braze.

### ¿Los precios de MMS y servicio de mensajes cortos son diferentes? {#does-mms-and-sms-pricing-differ}

MMS y servicio de mensajes cortos tienen costes diferentes y se cobran por separado en función del volumen. Contacta con el equipo de incorporación de Braze para obtener información sobre precios.

### ¿Cómo puedo evitar excedentes? {#how-can-i-avoid-overages}

Si bien no podemos garantizar que no tengas un excedente ocasional, puedes seguir estas precauciones para reducir las probabilidades de superar tus límites asignados:

- Presta atención al número de caracteres en tu servicio de mensajes cortos. Enviar involuntariamente más de un segmento puede causar excedentes. Para más detalles, consulta nuestro [desglose de segmentos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator).
- Calcula cuidadosamente los caracteres de tu servicio de mensajes cortos teniendo en cuenta Liquid o contenido conectado. El creador de servicio de mensajes cortos de Braze en tu panel no estima ni tiene en cuenta el uso de ninguna de estas características.
- Considera el tipo de codificación que utiliza tu mensaje. Si tu mensaje usa codificación GSM-7, normalmente puedes estimar 160 caracteres por segmento del mensaje (menos si usas caracteres de la tabla de extensión GSM-7). Si tu mensaje usa codificación [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set), normalmente puedes estimar 67 caracteres por segmento del mensaje.
- ¡Prueba, prueba y prueba! Siempre prueba tus mensajes servicio de mensajes cortos antes de lanzarlos, especialmente cuando uses Liquid y contenido conectado.

### Si un mensaje se envía a un teléfono fijo, ¿se contará igualmente en mi recuento de envíos de servicio de mensajes cortos? {#if-a-message-is-sent-to-a-landline-will-the-message-still-count-toward-my-sms-send-count}

En Estados Unidos, Canadá y Reino Unido:
- Si un servicio de mensajes cortos se envía a un teléfono fijo, se marca como **No entregado**. El comportamiento de facturación depende de tu proveedor de servicios de servicio de mensajes cortos. Con Twilio, el intento de entrega se cobra igualmente, por lo que los mensajes marcados como **Enviado**, **Entregado** o **No entregado** en tus registros de mensajes se facturan.
- En el Reino Unido, algunos operadores convierten el servicio de mensajes cortos en un mensaje de voz, entregando el mensaje.

En otros países:
- Con Twilio, se genera un error y no se te factura por el intento de envío del servicio de mensajes cortos.

### ¿Por qué el panel de Braze me advierte de que se me pueden cobrar segmentos del mensaje adicionales cuando mi mensaje tiene menos de 160 (GSM-7) o 67 (UCS-2) caracteres? {#why-is-the-braze-dashboard-warning-me-i-may-be-charged-for-additional-message-segments-when-my-message-is-under-160-gsm-7-or-67-ucs-2-characters}

Es posible que se te cobren segmentos del mensaje adicionales si incluyes personalización con Liquid en tu mensaje. La creación de plantillas de bloques de contenido no ocurre hasta que el mensaje se está preparando para enviarse. Cuando editas un servicio de mensajes cortos con un bloque de contenido, Braze no sabe qué contendrá el bloque de contenido, pero proporciona una estimación aproximada. Recomendamos que uses el panel de prueba para previsualizar el mensaje y comprender mejor qué esperar.

## Envío y capacidad de entrega {#sending-and-deliverability}

### ¿Se pueden incluir enlaces en un servicio de mensajes cortos? {#can-you-include-links-in-an-sms}

Puedes incluir cualquier enlace en cualquier Campaign de servicio de mensajes cortos que desees. Sin embargo, hay algunas consideraciones a tener en cuenta:

- Los enlaces pueden ocupar gran parte del límite de 160 caracteres para servicio de mensajes cortos. Si incluyes un enlace y texto, puede resultar en dos mensajes servicio de mensajes cortos en lugar de uno solo.
- Las empresas suelen utilizar acortadores de enlaces para limitar el impacto en el conteo de caracteres. Sin embargo, si envías un enlace acortado a través de un código largo, los operadores pueden bloquear o rechazar el mensaje, ya que pueden sospechar de la redirección del enlace.
- Usar un [código abreviado]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup) sería el tipo de número más fiable para incluir enlaces.

Braze también tiene su propia función de acortamiento de enlaces que acorta los enlaces y proporciona análisis de click-through de forma automática. Consulta [Acortamiento de enlaces]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening) para más información.

### ¿Es necesario limitar la tasa de envío de mensajes servicio de mensajes cortos? {#do-you-need-to-rate-limit-how-fast-you-send-sms-messages}

La tasa de concurrencia y rendimiento predeterminada permite aproximadamente 360 000 mensajes por hora por código abreviado. Un rendimiento adicional requiere códigos abreviados adicionales.

### ¿Cómo se incluyen URLs en la lista de permitidos para servicio de mensajes cortos? {#how-do-you-allowlist-urls-for-sms}

Antes de enviar mensajes servicio de mensajes cortos con URLs a usuarios en ciertos países (por ejemplo, Suecia o países nórdicos), debes registrar estas URLs con el operador. Contacta a tu director de cuentas de Braze para obtener ayuda. Este proceso tarda aproximadamente cinco días.

### ¿Cuáles son las mejores prácticas de envío para evitar la detección de correo no deseado en servicio de mensajes cortos? {#what-are-the-best-sending-practices-to-avoid-spam-detection-for-sms}

1. Asegúrate de que las instrucciones de adhesión voluntaria y cancelación de suscripción sean claras.
2. Asegúrate de que tú (la marca) tengas una relación con el cliente.
3. Asegúrate de que el contenido sea relevante para la relación y para lo que el usuario ha optado por recibir.

Para más directrices sobre cómo evitar la detección de correo no deseado, visita [Directrices sobre leyes y regulaciones de servicio de mensajes cortos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations).

### ¿Cuántos caracteres usa un emoji? {#how-many-characters-does-an-emoji-use}

Los emojis pueden ser complicados, ya que no existe un conteo de caracteres estándar para todos los emojis. Existe el riesgo de que el emoji supere el límite de caracteres y divida el servicio de mensajes cortos en varios mensajes, a pesar de mostrarse como un solo mensaje en el creador de Braze. Al probar tus mensajes, puedes verificar mejor si un mensaje se dividirá utilizando nuestra [calculadora de segmentos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator).

## Grupos de suscripción y adhesión/cancelación voluntaria {#subscription-groups-and-opt-inopt-out}

### ¿Cómo se crea la lógica para adhesiones selectivas a servicio de mensajes cortos de modo que los usuarios estén en el grupo de suscripción correcto? {#how-do-you-create-logic-for-selective-opt-ins-to-sms-so-users-are-in-the-right-subscription-group}

Las palabras clave personalizadas se registrarían como eventos personalizados, así que querrás crear segmentos basados en las palabras clave que los clientes pueden enviar por mensaje de texto. Por ejemplo, si un usuario se suscribe a servicio de mensajes cortos para mensajes VIP pero no para alertas, puedes crear un Segment VIP y un Segment de alertas, y luego asignar al usuario al Segment correspondiente.

### Si un usuario envía "Stop" a nuestro código abreviado, ¿se cancela su suscripción del grupo de suscripción? {#if-a-user-texts-stop-to-our-short-code-are-they-unsubscribed-from-the-subscription-group}

¿Cómo se refleja eso en el perfil de usuario? El grupo de suscripción aparece como cancelado en **Configuración de contacto**, y existen eventos personalizados para suscripción y cancelación de suscripción.

### Si un usuario ha cancelado su suscripción y envía una palabra clave a nuestro código abreviado y código largo, ¿recibe la respuesta que configuramos para esa palabra clave en Braze? {#if-a-user-is-opted-out-and-sends-a-keyword-to-our-short-and-long-code-do-they-receive-the-response-we-configured-for-that-keyword-in-braze}

Si un usuario ha cancelado su suscripción y envía una palabra clave de una de las [categorías de palabras clave predeterminadas]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout), recibirá la respuesta correspondiente a esa palabra clave. Si un usuario ha cancelado su suscripción y envía una [palabra clave personalizada]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling), no recibirá la respuesta correspondiente a esa palabra clave.

### ¿Las propiedades de evento de servicio de mensajes cortos capturan palabras clave dentro de una oración? {#will-sms-event-properties-capture-keywords-in-a-sentence}

Para que una palabra clave sea reconocida dentro de una oración (por ejemplo, "por favor deja de enviarme mensajes"), necesitarás usar una sentencia Liquid en el mensaje para reconocer la palabra específica. Las propiedades del evento tienen un límite de 256 caracteres; fuera de eso, no hay límite de caracteres.

## Pruebas {#testing}

### ¿Los mensajes de texto de prueba cuentan para los límites? {#do-test-text-messages-count-toward-limits}

Sí, cuentan. Ten esto en cuenta al probar mensajes.

### ¿Un usuario necesita ser parte de un grupo de suscripción de servicio de mensajes cortos para recibir mensajes de texto de prueba por servicio de mensajes cortos? {#does-a-user-need-to-be-part-of-an-sms-subscription-group-to-receive-sms-test-messages}

Sí. Los usuarios deben tener un número de teléfono válido, ser parte del grupo de suscripción de servicio de mensajes cortos utilizado para el envío de prueba y tener al menos un país seleccionado en **Geographic Permissions** para servicio de mensajes cortos.

### ¿Hay alguna forma de ver si existe un alias en un perfil de usuario? {#is-there-a-way-to-see-if-an-alias-exists-on-a-user-profile}

Los alias no son visibles en el perfil de usuario. Necesitarías usar los endpoints de [Exportar datos de usuario]({{site.baseurl}}/api/endpoints/export) para confirmar que los alias estén configurados.

## MMS

### ¿Hay algún cambio en los datos de Currents al enviar un MMS? {#are-there-any-changes-to-currents-data-when-sending-an-mms}

No, se proporcionará el mismo nivel de información al enviar un mensaje MMS.

### ¿Puedo controlar el orden en que se entregan la imagen y el cuerpo del mensaje de un MMS? {#can-i-control-the-order-in-which-the-image-and-message-body-of-an-mms-are-delivered}

Braze no tiene control sobre el orden de visualización cuando se incluyen tanto un cuerpo de mensaje como imágenes en un mensaje MMS. Esto depende de varios factores que incluyen, entre otros:

- El operador que recibe el mensaje
- El dispositivo que recibe el mensaje
- El tamaño total del mensaje

### ¿MMS requiere un proceso de incorporación separado? {#does-mms-require-a-separate-onboarding-process}

No. MMS ahora está incluido en nuestro proceso de incorporación de servicio de mensajes cortos. Los clientes existentes que ya pasaron por la incorporación pueden comenzar a enviar campañas de MMS después de completar los siguientes pasos:

1. Comprar MMS.
2. Ponerse en contacto con el equipo de incorporación de Braze para solicitar que se active la función de MMS. Esto habilitará MMS y se creará o actualizará un grupo de suscripción de servicio de mensajes cortos/MMS para ti.

A continuación, el equipo de incorporación de Braze se asegurará de que tus códigos abreviados y largos estén habilitados (en EE. UU. y Canadá) para MMS. También actualizarán tus grupos de suscripción para mostrar tus números actuales que fueron añadidos o habilitados para MMS. Una vez completados estos pasos, puedes enviar mensajes MMS de inmediato desde nuestro creador nativo de servicio de mensajes cortos.

### ¿Por qué no puedo encontrar MMS en mi panel aunque la función está habilitada? {#why-cant-i-find-mms-on-my-dashboard-even-though-the-feature-is-enabled}

MMS solo se muestra en el panel de Braze cuando un grupo de suscripción se considera "habilitado para MMS". Esto se refleja mediante una etiqueta de MMS al seleccionar el grupo de suscripción en el creador de un mensaje servicio de mensajes cortos/MMS. Esto significa que al menos un número en el grupo de suscripción es capaz de enviar un mensaje MMS.

Además, ciertas situaciones requerirán que Twilio vuelva a aprobar la habilitación de códigos abreviados que originalmente no tenían MMS habilitado. Este proceso de aprobación puede tardar semanas.

### ¿Por qué mi MMS con una imagen no se envía? {#why-does-my-mms-with-an-image-fail-to-send}

Algunos proveedores de servicio de mensajes cortos validan el encabezado `Content-Type` en las URL de las imágenes. Si un MMS con una imagen se cancela, confirma que la URL de la imagen alojada devuelve `image/png` u otro tipo de imagen compatible (por ejemplo, con `curl -I <image-url>`). Vuelve a alojar el activo en la biblioteca multimedia de Braze o en un CDN que sirva el `Content-Type` correcto.

### ¿Por qué la imagen de mi tarjeta de contacto no aparece en un MMS? {#why-doesnt-my-contact-card-image-appear-in-an-mms}

Las fotos de las tarjetas de contacto MMS pueden no mostrarse cuando el archivo de la tarjeta de contacto hace referencia a una URL de imagen que el dispositivo del destinatario no puede obtener. Crea la tarjeta de contacto en un teléfono, exporta el archivo y súbelo a la biblioteca multimedia para usarlo en tu mensaje MMS.

## RCS

### ¿Por qué mi mensaje RCS no se muestra correctamente en dispositivos iOS? {#why-doesnt-my-rcs-message-render-accurately-on-ios-devices}

Los mensajes RCS pueden mostrarse de forma diferente en un dispositivo iOS dependiendo del sistema operativo y la aplicación de mensajería. En dispositivos iOS, pueden ocurrir los siguientes comportamientos:

- Las acciones sugeridas de diferentes mensajes RCS en el mismo hilo de conversación pueden agruparse y mostrarse en el orden incorrecto.
- Los botones de tarjetas enriquecidas y las acciones sugeridas que están fuera de la tarjeta enriquecida pueden permanecer visibles incluso después de tocar un botón de tarjeta enriquecida o una acción sugerida.
- Los GIF en tarjetas enriquecidas se muestran como imágenes estáticas. Para más detalles, consulta [¿Por qué los GIF en tarjetas enriquecidas de RCS aparecen estáticos en iOS?](#why-do-gifs-in-rcs-rich-cards-appear-static-on-ios).

{% alert note %}
Braze envía la carga útil de RCS que compones, mientras que el cliente de mensajería controla cómo se ordenan, agrupan y ocultan las acciones sugeridas. Asegúrate de probar los mensajes RCS, especialmente aquellos que usan tarjetas enriquecidas con acciones sugeridas o respuestas sugeridas, tanto en dispositivos Android como iOS antes de enviarlos.
{% endalert %}

### ¿Por qué los GIF en tarjetas enriquecidas de RCS aparecen estáticos en iOS? {#why-do-gifs-in-rcs-rich-cards-appear-static-on-ios}

En iOS, los GIF en tarjetas enriquecidas de RCS se muestran como una imagen estática (el primer fotograma). En Android, se animan como se espera.

El cliente de mensajería de iOS controla este comportamiento. Un GIF puede seguir animándose en la vista previa de Braze. Envía un mensaje de prueba a un dispositivo iOS para confirmar cómo se ve el mensaje entregado.

Para enviar contenido animado a iOS:

- Usa un mensaje de **Media** de RCS, que envía el GIF como un archivo
- Usa video en la tarjeta enriquecida

### ¿Puedo enviar mensajes de voz pregrabados con RCS? {#can-i-send-pre-recorded-voicemails-with-rcs}

Sí, puedes usar mensajes multimedia para admitir archivos de audio.

### ¿Por qué las adhesiones voluntarias por REST or transferencia de estado representacional API de servicio de mensajes cortos no coinciden con el **Total de adhesiones voluntarias** en el rendimiento de servicio de mensajes cortos/MMS/RCS? {#why-do-rest-api-sms-opt-ins-not-match-total-opt-ins-on-smsmmsrcs-performance}

El **Total de adhesiones voluntarias** y el **Total de cancelaciones de suscripción** en el panel de [rendimiento de servicio de mensajes cortos/MMS/RCS]({{site.baseurl}}/user_guide/analytics/dashboards) cuentan los cambios de suscripción impulsados por el manejo de palabras clave de servicio de mensajes cortos entrantes (por ejemplo, un usuario que envía una palabra clave de adhesión voluntaria a tu código abreviado). No incluyen todas las actualizaciones de suscripción realizadas a través de la REST or transferencia de estado representacional API, el panel u otras fuentes.

Para analizar las adhesiones voluntarias y las cancelaciones de suscripción por fuente, usa el [Generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder) en `USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED` y filtra por `STATE_CHANGE_SOURCE` (por ejemplo, **REST or transferencia de estado representacional API** frente a **Inbound Message**).