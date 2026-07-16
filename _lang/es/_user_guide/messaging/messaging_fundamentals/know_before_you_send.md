---
nav_title: "Antes de enviar"
article_title: "Antes de enviar"
description: "Después de consultar nuestra guía previa al lanzamiento, consulta esta lista final de comprobaciones o aspectos a tener en cuenta para Content Cards, correo electrónico, mensajes dentro de la aplicación, push y SMS."
alias: /know_before_send/
page_order: 7
tool:
    - Campaigns
    - Canvas
---

# Antes de enviar: canales {#know-before-you-send-channels}

> ¡Lanza tus Campaigns y Canvas con confianza! Consulta esta lista final de comprobaciones o aspectos a tener en cuenta para los [canales]({{site.baseurl}}/user_guide/channels) de mensajería más populares en Braze.

{% alert note %}
Aunque proporcionamos una amplia lista de recursos de referencia previos al envío, cada canal tiene matices individuales que siguen creciendo a medida que evolucionamos nuestros productos. Las comprobaciones que se enumeran a continuación son sugerencias útiles, y te recomendamos que pruebes a fondo tus Campaigns y envíos masivos antes de enviarlos.
{% endalert %}

## General {#general}

### Cosas que comprobar {#things-to-check}
- [**Límites de velocidad de la API**](https://braze.com/resources/articles/whats-rate-limiting): Revisa los [límites de velocidad]({{site.baseurl}}/api/api_limits) de la API de Braze para tus espacios de trabajo y así evitar errores. Si deseas aumentar tus límites de velocidad (y ya estás agrupando solicitudes en lotes), ponte en contacto con tu administrador de éxito de cliente. Ten en cuenta que este proceso requiere tiempo de preparación, así que planifica en consecuencia.
- [**Anulaciones necesarias de la limitación de frecuencia**]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping): Hay algunas Campaigns, como los mensajes transaccionales, que querrás que siempre lleguen al usuario, incluso si ya has alcanzado su límite de frecuencia (por ejemplo, una notificación de entrega). Si deseas que una Campaign en particular anule las reglas de limitación de frecuencia, puedes configurarlo en el panel de Braze al planificar la entrega de esa Campaign desactivando la limitación de frecuencia.

### Cosas que debes saber {#things-to-know}
- [**Grupos de control global**]({{site.baseurl}}/user_guide/audience/global_control_group): Si estás utilizando un grupo de control global, un porcentaje de usuarios no recibirá ninguna Campaign ni Canvas. (Puedes crear excepciones con la [configuración de exclusión]({{site.baseurl}}/user_guide/audience/global_control_group#step-3-assign-exclusion-settings)). Para ver una lista de estos usuarios, expórtalos mediante CSV o [API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group).
- [**Límites de velocidad de Canvas**]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping): En un Canvas, el límite de velocidad se aplica a todo el Canvas, no a los pasos individuales. Por ejemplo, si estableces un límite de velocidad de 10 000 mensajes por minuto en un Canvas con múltiples pasos, seguirá limitado a 10 000 mensajes porque el límite se habrá alcanzado en el primer paso.
- **Limitación de frecuencia**:
  - Las reglas de limitación de frecuencia se aplican a push, correo electrónico, SMS y webhooks, pero no a los mensajes dentro de la aplicación ni a Content Cards.
  - La limitación de frecuencia global se programa en función de la zona horaria del usuario y se calcula por días calendario, no por períodos de 24 horas. Por ejemplo, si configuras una regla de limitación de frecuencia de no enviar más de una Campaign al día, un usuario puede recibir un mensaje a las 11 pm en su zona horaria local y sería elegible para recibir otro mensaje una hora después.

{% alert tip %}
Para obtener más ayuda con la solución de problemas de Canvas y Campaigns, asegúrate de ponerte en contacto con soporte de Braze dentro de los 30 días posteriores a la ocurrencia de tu problema, ya que solo disponemos de los últimos 30 días de registros de diagnóstico.
{% endalert %}

## Banners {#banners}

### Cosas que comprobar
- **Dimensiones de los banners:** Crea tus banners utilizando un elemento de dimensión fija y pruébalos en el editor.
- **Prioridad:** Si estás lanzando múltiples banners, puedes establecer manualmente la prioridad de cómo se muestra cada banner.

### Cosas que debes saber
- **Personalización con Liquid:** La personalización con Liquid se actualiza en cada solicitud de actualización.
- **Proporción de ubicación y banner:** Cada ubicación de banner se puede utilizar en hasta 25 mensajes en un espacio de trabajo.
- **Clics e impresiones:** Los clics e impresiones de los banners se rastrean automáticamente con el SDK.
- **Limitaciones:** Actualmente, las siguientes características no son compatibles: integración con Canvas, Campaigns activadas por API y basadas en acciones, contenido conectado, códigos promocionales y `catalog_items` que usan la [etiqueta `:rerender`]({{site.baseurl}}/user_guide/data/activation/catalogs/use#using-liquid).
- **Pruebas:** Para mostrar el banner de prueba, el dispositivo que estés utilizando debe poder recibir notificaciones push en primer plano.
- **HTML personalizado:** Aprovecha el [puente JavaScript]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge) para registrar clics cuando uses HTML personalizado para definir acciones de clic, como enlaces y botones. Las acciones de clic solo se registran automáticamente cuando se utilizan los componentes prediseñados en el editor de arrastrar y soltar.
- **Solicitud de ubicaciones:** Se pueden devolver hasta 10 ubicaciones al SDK en una sola solicitud de actualización. Cada ubicación incluirá el banner de mayor prioridad para el que un usuario sea elegible.

## Content Cards

### Cosas que comprobar
- **Tamaño de Content Cards**: Los campos de mensaje de Content Cards están limitados a 2&nbsp;KB en tamaño previo a la compresión, calculado sumando la longitud en bytes de los siguientes campos: título, mensaje, URL de imagen, texto del enlace, URLs del enlace y pares clave-valor. Los mensajes que superen este tamaño no se enviarán. Ten en cuenta que esto no incluye el tamaño de la imagen, sino la longitud de la URL de la imagen.
- **Actualización del texto después del envío**: Después de enviar una tarjeta, no podrás actualizar el texto de esa misma tarjeta. Consulta [Actualización de tarjetas enviadas]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#updating-launched-cards) para entender cómo puedes abordar este escenario.

### Cosas que debes saber
- **Límite de Campaigns activas de Content Cards**: Puedes tener hasta 500 Campaigns activas de Content Cards. Este recuento incluye Content Cards enviadas con cualquiera de las opciones de [creación de tarjetas]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card).
- [**Términos de informes**]({{site.baseurl}}/user_guide/channels/content_cards/reporting): Revisa términos como impresiones totales, impresiones únicas y destinatarios únicos, ya que las definiciones a veces pueden causar confusión.
- **Actualización de Content Cards**: De forma predeterminada, Braze actualiza las solicitudes de Content Cards cuando se sincronizan al inicio de la sesión, al deslizar hacia abajo en el feed (móvil) y cuando se abre la vista de tarjetas si la última actualización fue hace más de un minuto.
- **Almacenamiento en caché de Content Cards**: Las opciones de almacenamiento en caché de Content Cards se pueden encontrar en nuestra documentación de [Android/FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization/custom_styling#customizing-card-rendering-for-android) y [Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#getcachedcontentcards).
- **Limitación de frecuencia**: La limitación de frecuencia no se aplica a Content Cards.
- **Impresiones**: Las impresiones generalmente se registran cuando se ve una tarjeta. Por ejemplo, si tienes un buzón de entrada lleno de Content Cards, no se registrará una impresión hasta que el usuario se desplace hasta la Content Card específica. Existen algunos matices entre las plataformas Web, Android e iOS.
- **Sesiones del SDK y creación de tarjetas**: Las Content Cards no se crean para usuarios sin sesiones del SDK, incluso si esos usuarios cumplen con los criterios del segmento. Sin embargo, si un usuario ya tiene una sesión de Android, las Content Cards con acciones de clic específicas de iOS se seguirán creando, y el usuario podrá ver esas Content Cards en iOS una vez que tenga una sesión allí. Consulta [Creación de tarjetas]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card) para obtener más información sobre cuándo se crean las tarjetas.

## Correo electrónico {#email}

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

### Cosas que comprobar
- **Consentimiento del cliente**: Antes de enviar tus correos electrónicos iniciales, es importante obtener primero el permiso de tus clientes. Consulta [Consentimiento y recopilación de direcciones]({{site.baseurl}}/user_guide/channels/email/email_setup/consent_and_address_collection) y nuestra [Política de uso aceptable de Braze](https://www.braze.com/company/legal/aup) para obtener más información.
- **Volumen previsto**: 2 millones de correos electrónicos por día para una sola IP es la recomendación general, siempre que ese volumen se haya [calentado correctamente]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming#ip-warming).
  - Si planeas enviar consistentemente un volumen mayor que este, para evitar que los proveedores limiten la recepción de correos electrónicos, lo que resultaría en una gran cantidad de rebotes blandos, una tasa de capacidad de entrega reducida y una reputación de IP disminuida, considera usar múltiples direcciones IP agrupadas en un pool de IP.
  - Si deseas enviar en un período de tiempo más corto, te recomendamos investigar qué tan rápido los diferentes proveedores aceptan correo para determinar el número apropiado de IPs desde las cuales enviar.

### Cosas que debes saber
- **Factores del volumen de envío**: Algunos factores que determinan las capacidades de volumen de envío para una IP incluyen:
  - Buzones de correo: Los grandes proveedores de correo electrónico probablemente pueden manejar millones por día desde una sola IP, mientras que un proveedor de buzón regional más pequeño o uno con una infraestructura menor podría no ser capaz de manejar esa cantidad.
  - Reputación del remitente: Es posible que puedas enviar un volumen mayor por día desde una sola IP si el remitente ha aumentado gradualmente hasta ese volumen y si su reputación como remitente es lo suficientemente sólida en cada buzón o dominio al que envía.
- **Mejores prácticas**: Revisa las [mejores prácticas de correo electrónico]({{site.baseurl}}/user_guide/channels/email/best_practices) de Braze y ponte en contacto con tu equipo de cuenta de Braze si deseas obtener más información sobre los servicios de capacidad de entrega.

## Mensajes dentro de la aplicación {#in-app-messages}

### Cosas que debes saber
- **Activación de mensajes dentro de la aplicación**: Al inicio de la sesión, el SDK solicita que todos los mensajes dentro de la aplicación elegibles se envíen al dispositivo junto con sus desencadenantes, de modo que si el usuario realiza el evento durante la sesión, pueda recibir el mensaje dentro de la aplicación de forma rápida y fiable.
- **Enviados versus impresiones**: Para los mensajes dentro de la aplicación, el concepto de "enviado" difiere de los otros canales disponibles. Para ver un mensaje dentro de la aplicación, un usuario debe iniciar una sesión, estar en la audiencia elegible y realizar el desencadenante. Debido a esto, rastreamos las "impresiones" ya que es más claro.
- **Activación**: De forma predeterminada, los mensajes dentro de la aplicación se activan mediante eventos registrados por el SDK. Si deseas activar mensajes dentro de la aplicación mediante eventos enviados desde el servidor, también puedes lograrlo a través de estas guías para [iOS]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=swift) y [Android]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=android).
- [Mensajes dentro de la aplicación en Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas#advancement-behavior): Estos mensajes aparecen la primera vez que tu usuario abre la aplicación (activados por el inicio de sesión) después de que el mensaje planificado en el componente de Canvas les haya sido enviado.
- **Llamadas de contenido conectado**: El uso de contenido conectado te permite enviar contenido dinámico en los mensajes. Cuando envías mensajes a través de un canal como los mensajes dentro de la aplicación, esto puede crear más conexiones simultáneas a los dispositivos de tus usuarios (los mensajes se envían uno por uno en lugar de en lotes). Para gestionar esto, te recomendamos [limitar la velocidad]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) de tus mensajes.

## Push {#push}

### Cosas que comprobar
- [**Aceptación/suscripción y push habilitado**]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states): Para que los usuarios reciban un mensaje push de Braze, necesitan que sus estados de suscripción sean aceptación (iOS) o suscrito (Android) y `Push Enabled = True`. Ten en cuenta que Android 13 introduce un cambio importante en cómo los usuarios gestionan las aplicaciones que envían notificaciones push. La [guía de actualización del SDK de Android 13]({{site.baseurl}}/developer_guide/platforms/android/android_13) de Braze seguirá actualizándose a medida que se publiquen nuevas versiones beta de Android 13.

### Cosas que debes saber
- **Notificación push web**: Si tienes configurado el [SDK Web]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web) de Braze, considera utilizar las notificaciones push web para interactuar con los usuarios. Las notificaciones push web funcionan de la misma manera que las notificaciones push de aplicaciones en tu teléfono. Para obtener más información sobre cómo componer una notificación push web, consulta [Crear una notificación push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message#create-a-push-message).
- **Dirigirse a una aplicación individual**: Revisa las [diferencias en la segmentación]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration#targeting-a-singular-app) para dirigirte a una aplicación individual y sus usuarios.

## SMS

### Cosas que comprobar
- **Asignaciones y rendimiento**: Comprende qué asignaciones de SMS están actualmente vinculadas a tu cuenta (código abreviado, código largo y similares) y [cuánto rendimiento te proporcionan]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup) para confirmar que tienes suficiente rendimiento para enviar en el tiempo deseado.
- **Estimar segmentos a partir del texto del SMS**: Prueba el texto de tu SMS en la [calculadora de segmentos de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator). Ten en cuenta que el número de segmentos de SMS debe considerarse junto con tus capacidades de rendimiento. (Audiencia × segmentos de SMS = rendimiento necesario). Consulta las preguntas frecuentes de SMS sobre [cómo evitar excedentes]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs).
- **Leyes y regulaciones de SMS**: [Revisa las leyes, regulaciones y prevención de abuso de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations) para confirmar que estás utilizando los servicios de SMS en cumplimiento con todas las leyes aplicables. Asegúrate de buscar el asesoramiento de tu asesor legal antes de enviar.

### Cosas que debes saber
- **Envío predeterminado de mensajes SMS**: Los mensajes SMS normalmente se envían de forma predeterminada desde el código abreviado en el pool de remitentes.
- **ID de remitente alfanumérico**: La mensajería bidireccional ya no funcionará si utilizas un ID de remitente alfanumérico; ahora son solo unidireccionales.
- **Rendimiento actualizado en EE. UU.**: El rendimiento ha cambiado en EE. UU. con el [registro A2P 10DLC en EE. UU.](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US). Ten en cuenta que no nos comprometemos contractualmente con ningún SLA de velocidad de envío debido a múltiples factores como la congestión del tráfico y problemas con los operadores que pueden afectar las tasas de entrega reales.
- **Grupo de suscripción**: Para lanzar una Campaign de SMS a través de Braze, se debe seleccionar un grupo de suscripción. Además, para cumplir con las [directrices y normativas internacionales de telecomunicaciones]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations), Braze nunca enviará SMS a usuarios que no se hayan [suscrito al grupo de suscripción seleccionado]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#check-a-users-group).

## WhatsApp

### Cosas que debes saber

- [**Mejores prácticas**]({{site.baseurl}}/user_guide/channels/whatsapp/best_practices): Revisa nuestras mejores prácticas sugeridas para WhatsApp.