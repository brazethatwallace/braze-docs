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

### ¿Qué es un `app_id` en el objeto de API de SMS? {#what-is-an-app_id-in-the-sms-api-object}

La clave de API del identificador de aplicación o `app_id` es un parámetro que asocia la actividad con una aplicación específica en tu espacio de trabajo. Designa con qué aplicación dentro del espacio de trabajo estás interactuando. Por ejemplo, tendrás un `app_id` para tu aplicación iOS, un `app_id` para tu aplicación Android y un `app_id` para tu integración web.

Puedes encontrar tu `app_id` navegando a **Configuración** > **Configuración de la aplicación** y localizando la sección **Identification**.

### ¿Qué ocurre si varios usuarios tienen el mismo número de teléfono? {#what-happens-if-multiple-users-have-the-same-phone-number}

Cuando varios perfiles de usuario que comparten un número de teléfono (habilitado para SMS) son elegibles para una campaña basada en acciones o un componente de Canvas al mismo tiempo, desencadenados por el evento de un SMS entrante, Braze deduplicará a los usuarios a nivel del componente de Canvas. Esto evitará que los usuarios reciban más de un mensaje de texto SMS por componente de Canvas, incluso si varios usuarios comparten el mismo número de teléfono.

{% alert note %}
Braze no deduplica por número de teléfono para Canvas planificados.
{% endalert %}

Braze utilizará el siguiente flujo para determinar el perfil del destinatario:
- Comprobar qué perfil recibió un SMS más recientemente (hasta hace 7 días); si existe uno, enviarlo a ese usuario.
- Si ninguno ha recibido un SMS en los últimos 7 días, enviar al usuario que tenga un alias de usuario de "phone" que coincida con el número de teléfono.
- Si ninguno existe, enviar a un perfil aleatorio entre los disponibles.

Si recibes una palabra clave "START" o "STOP" desde el número de teléfono compartido, todos los perfiles de usuario serán suscritos y habilitados para SMS o dados de baja. Esto también se aplica a los cambios de estado por API. Por ejemplo, si varios perfiles con diferentes ID externos tienen los mismos números de teléfono, un cambio de estado del grupo de suscripción a través de la API actualizará todos los perfiles con ese número de teléfono, incluso si solo se especifica un ID externo.

{% alert important %}
Si escalas a tus usuarios en un Canvas y tienes diferentes horarios de planificación para cada componente de Canvas, puedes enviar a un usuario con el mismo correo electrónico o teléfono mensajes duplicados.
{% endalert %}

Para evitar actualizaciones innecesariamente grandes, Braze actualizará un máximo de 100 perfiles de usuario que comparten un identificador cuando se realiza una actualización de suscripción. Si más de 100 perfiles de usuario comparten el mismo número de teléfono, no todos los perfiles se actualizarán.

### ¿Qué son los códigos abreviados compartidos? {#what-are-shared-short-codes}

Con un código abreviado compartido, todos los mensajes de texto, sin importar qué empresa u organización los envíe, llegan al dispositivo móvil del consumidor desde el mismo número de teléfono de 5-6 dígitos. Aunque los códigos abreviados compartidos son relativamente económicos y están disponibles de inmediato, esto significa que tu empresa no tendrá un código abreviado dedicado.

Algunas desventajas de este enfoque incluyen:

- Si tus clientes cancelan la suscripción a los mensajes de otra empresa que comparte un código abreviado contigo, también habrán cancelado la suscripción a tus mensajes.
- Si una empresa viola las reglas, los mensajes de todas las empresas se suspenden.
- Problemas de seguridad

## Facturación y precios {#billing-and-pricing}

### ¿Cómo se me facturará por SMS? {#how-will-i-be-billed-for-sms}

Además de los cargos por códigos abreviados y largos, Braze proporciona una asignación de mensajes SMS para diferentes países. Es decir, trabajamos contigo para establecer un número determinado de segmentos de mensaje para diferentes países, que utilizarás para enviar campañas de SMS. La facturación se realiza por el número de segmentos de mensaje enviados por país. Para obtener más información sobre cómo se calculan los segmentos de mensaje, consulta nuestra guía de [Segmentos de mensaje y límites de texto]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator/). Tu director de cuentas se pondrá en contacto contigo para informarte si estás cerca de alcanzar tu máximo, proporcionando informes relevantes para mantenerte informado. Para más preguntas sobre excedentes, ponte en contacto con tu representante de Braze.

### ¿Los precios de MMS y SMS son diferentes? {#does-mms-and-sms-pricing-differ}

MMS y SMS tienen costos diferentes y se cobran por separado según el volumen. Ponte en contacto con el equipo de incorporación de Braze para obtener información sobre precios.

### ¿Cómo puedo evitar excedentes? {#how-can-i-avoid-overages}

Aunque no podemos prometer que no tendrás un excedente ocasionalmente, puedes seguir estas precauciones para disminuir las posibilidades de superar tus límites asignados:

- Presta atención al número de caracteres en tu SMS. Enviar involuntariamente más de un segmento puede causar excedentes. Para más detalles, consulta nuestro [desglose de segmentos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator/).
- Calcula cuidadosamente los caracteres de tu SMS para tener en cuenta Liquid o Contenido conectado. El compositor de SMS de Braze en tu dashboard no estima ni tiene en cuenta el uso de ninguna de estas características.
- Considera el tipo de codificación que utiliza tu mensaje: si tu mensaje usa codificación GSM-7, generalmente puedes estimar que puedes enviar un mensaje con 128 caracteres por segmento de mensaje. Si tu mensaje usa codificación [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set), generalmente puedes estimar que puedes enviar un mensaje con 67 caracteres por segmento de mensaje.
- ¡Prueba, prueba y prueba! Siempre prueba tus mensajes SMS antes del lanzamiento, especialmente cuando uses Liquid y Contenido conectado.

### Si se envía un mensaje a un teléfono fijo, ¿el mensaje seguirá contando para mi recuento de envíos de SMS? {#if-a-message-is-sent-to-a-landline-will-the-message-still-count-toward-my-sms-send-count}

En EE. UU., Canadá y el Reino Unido:
- Si se envía un SMS a un teléfono fijo, se marcará como **Undelivered**. Ten en cuenta que Twilio seguirá cobrando por el intento de entrega, por lo que los mensajes marcados como **Sent**, **Delivered** o **Undelivered** en tus registros de mensajes serán facturados.
- En el Reino Unido, algunos operadores convertirán el SMS en un mensaje de voz, entregando el mensaje.

En otros países:
- Twilio generará un error y no se te facturará por el intento de mensaje SMS.

### ¿Por qué el dashboard de Braze me advierte que se me pueden cobrar segmentos de mensaje adicionales cuando mi mensaje tiene menos de 160 (GSM-7) o 70 (UCS-2) caracteres? {#why-is-the-braze-dashboard-warning-me-i-may-be-charged-for-additional-message-segments-when-my-message-is-under-160-gsm-7-or-70-ucs-2-characters}

Es posible que se te cobren segmentos de mensaje adicionales si tienes personalización Liquid incluida en tu mensaje. La plantilla de bloques de contenido no se procesa hasta que el mensaje se está preparando para ser enviado. Cuando estás editando un SMS con un bloque de contenido, Braze no sabe qué contendrá el bloque de contenido, pero proporciona una estimación aproximada. Recomendamos que los usuarios utilicen el panel de prueba para previsualizar el mensaje y comprender mejor qué esperar.

## Envío y capacidad de entrega {#sending-and-deliverability}

### ¿Se pueden incluir enlaces en un SMS? {#can-you-include-links-in-an-sms}

Puedes incluir cualquier enlace en cualquier campaña de SMS que desees. Sin embargo, hay algunas consideraciones a tener en cuenta:

- Los enlaces pueden ocupar gran parte del límite de 160 caracteres para SMS. Si incluyes un enlace y texto, puede resultar en dos mensajes SMS en lugar de solo uno.
- Las empresas a menudo usan acortadores de enlaces para limitar el impacto en el recuento de caracteres de un enlace. Sin embargo, si envías un enlace acortado a través de un código largo, los operadores pueden bloquear o rechazar el mensaje, ya que pueden sospechar de la redirección del enlace.
- Usar un [código abreviado]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup/) sería el tipo de número más confiable para incluir enlaces.

Braze también tiene su propia función de acortamiento de enlaces que acortará los enlaces y proporcionará análisis de click-through automáticamente. Consulta [Acortamiento de enlaces]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/link_shortening/) para más información.

### ¿Es necesario limitar la tasa de envío de mensajes SMS? {#do-you-need-to-rate-limit-how-fast-you-send-sms-messages}

La tasa de concurrencia y rendimiento predeterminada permite aproximadamente 360 000 mensajes por hora por código abreviado. Se requieren códigos abreviados adicionales para un rendimiento adicional.

### ¿Cómo se incluyen URL en la lista de permitidos para SMS? {#how-do-you-allowlist-urls-for-sms}

Antes de enviar mensajes SMS que contengan URL a usuarios en ciertos países (por ejemplo, Suecia o países nórdicos), debes registrar estas URL con el operador. Ponte en contacto con tu administrador de servicio al cliente de Braze para obtener ayuda. Este proceso tardará aproximadamente cinco días.

### ¿Cuáles son las mejores prácticas de envío para evitar la detección de correo no deseado en SMS? {#what-are-the-best-sending-practices-to-avoid-spam-detection-for-sms}

1. Asegúrate de que las instrucciones de adhesión voluntaria y cancelación de suscripción sean claras.
2. Asegúrate de que tú (la marca) tengas una relación con el cliente.
3. Asegúrate de que el contenido sea relevante para la relación y para lo que el usuario ha aceptado recibir.

Para más directrices sobre cómo evitar la detección de correo no deseado, visita las [directrices sobre leyes y regulaciones de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations/).

### ¿Cuántos caracteres usa un emoji? {#how-many-characters-does-an-emoji-use}

Los emojis pueden ser complicados, ya que no existe un recuento de caracteres estándar para todos los emojis. Existe el riesgo de que el emoji exceda el límite de caracteres y divida el SMS en varios mensajes, a pesar de que se muestre como un solo mensaje en el compositor de Braze. Al probar tus mensajes, puedes verificar mejor si un mensaje se dividirá usando nuestra [calculadora de segmentos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator/#segment-calculator).

## Grupos de suscripción y adhesión voluntaria/cancelación de suscripción {#subscription-groups-and-opt-inopt-out}

### ¿Cómo se crea la lógica para adhesiones voluntarias selectivas a SMS para que los usuarios estén en el grupo de suscripción correcto? {#how-do-you-create-logic-for-selective-opt-ins-to-sms-so-users-are-in-the-right-subscription-group}

Las palabras clave personalizadas se escribirían como eventos personalizados, por lo que querrías crear segmentos basados en las palabras clave que los clientes pueden enviar por mensaje de texto. Por ejemplo, si un usuario se suscribe a SMS para mensajes VIP pero no para alertas, puedes crear un segmento VIP y un segmento de alertas, y luego asignar al usuario al segmento apropiado.

### Si un usuario envía "Stop" a nuestro código abreviado, ¿se da de baja del grupo de suscripción? {#if-a-user-texts-stop-to-our-short-code-are-they-unsubscribed-from-the-subscription-group}

¿Cómo se ve eso en el perfil de usuario? El grupo de suscripción volverá a 2 guiones (- -), y habrá eventos personalizados para suscripción y cancelación de suscripción.

### Si un usuario se ha dado de baja y envía una palabra clave a nuestro código abreviado y largo, ¿recibe la respuesta que configuramos para esa palabra clave en Braze? {#if-a-user-is-opted-out-and-sends-a-keyword-to-our-short-and-long-code-do-they-receive-the-response-we-configured-for-that-keyword-in-braze}

Si un usuario se ha dado de baja y envía una palabra clave de una de las [categorías de palabras clave predeterminadas]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout/), recibirá la respuesta para esa palabra clave. Si un usuario se ha dado de baja y envía una [palabra clave personalizada]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling/), no recibirá la respuesta para esa palabra clave.

### ¿Las propiedades de eventos de SMS capturan palabras clave en una oración? {#will-sms-event-properties-capture-keywords-in-a-sentence}

Para que una palabra clave sea reconocida dentro de una oración (por ejemplo, "por favor deja de enviarme mensajes"), necesitarás usar una declaración Liquid en el mensaje para reconocer la palabra específica. Las propiedades de eventos tienen un límite de 256 caracteres; de lo contrario, no hay límite de caracteres.

## Pruebas {#testing}

### ¿Los mensajes de texto de prueba cuentan para los límites? {#do-test-text-messages-count-toward-limits}

Sí, así es. Ten esto en cuenta al probar mensajes.

### ¿Un usuario necesita ser parte de un grupo de suscripción de SMS para recibir mensajes de prueba de SMS? {#does-a-user-need-to-be-part-of-an-sms-subscription-group-to-receive-sms-test-messages}

Sí, así es. Los usuarios deben tener un número de teléfono válido, ser parte del grupo de suscripción de SMS utilizado para el envío de prueba y tener al menos un país seleccionado en **Geographic Permissions** para SMS.

### ¿Hay alguna forma de ver si existe un alias en un perfil de usuario? {#is-there-a-way-to-see-if-an-alias-exists-on-a-user-profile}

Los alias no son visibles en el perfil de usuario. Necesitarías usar los puntos finales de [Exportar datos de usuario]({{site.baseurl}}/api/endpoints/export/) para confirmar que los alias se hayan establecido.

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

A continuación, el equipo de incorporación de Braze se asegurará de que tus códigos abreviados y largos estén habilitados (en EE. UU. y Canadá) para MMS. También actualizarán tus grupos de suscripción para mostrar tus números actuales que fueron añadidos o habilitados para MMS. Una vez completados estos pasos, puedes enviar mensajes MMS de inmediato desde nuestro compositor nativo de SMS.

### ¿Por qué no puedo encontrar MMS en mi dashboard aunque la función está habilitada? {#why-cant-i-find-mms-on-my-dashboard-even-though-the-feature-is-enabled}

MMS solo se muestra en el dashboard de Braze cuando un grupo de suscripción se considera "habilitado para MMS". Esto se refleja mediante una etiqueta de MMS al seleccionar el grupo de suscripción en el compositor de un mensaje SMS/MMS. Esto significa que al menos un número en el grupo de suscripción es capaz de enviar un mensaje MMS.

Además, ciertas situaciones requerirán que Twilio vuelva a aprobar la habilitación de códigos abreviados que originalmente no tenían MMS habilitado. Este proceso de aprobación puede tardar semanas.

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

El **Total de adhesiones voluntarias** y el **Total de cancelaciones de suscripción** en el dashboard de [rendimiento de SMS/MMS/RCS]({{site.baseurl}}/user_guide/analytics/dashboards/) cuentan los cambios de suscripción impulsados por el manejo de palabras clave de SMS entrantes (por ejemplo, un usuario que envía una palabra clave de adhesión voluntaria a tu código abreviado). No incluyen todas las actualizaciones de suscripción realizadas a través de la REST API, el dashboard u otras fuentes.

Para analizar las adhesiones voluntarias y las cancelaciones de suscripción por fuente, usa el [Generador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/) en `USERS_BEHAVIORS_SUBSCRIPTIONGROUP_STATECHANGE_SHARED` y filtra por `STATE_CHANGE_SOURCE` (por ejemplo, **Rest API** frente a **Inbound Message**).