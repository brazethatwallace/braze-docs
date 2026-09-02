---
nav_title: "Antes de enviar"
article_title: "Antes de enviar"
description: "Después de consultar nuestra guía previa al lanzamiento, consulta esta lista final de comprobaciones o aspectos a tener en cuenta para Content Cards, correo electrónico, mensajes dentro de la aplicación, push y servicio de mensajes cortos."
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

### Cosas que verificar {#things-to-check}
- [**Límites de velocidad de la API**](https://braze.com/resources/articles/whats-rate-limiting): Revisa los [límites de velocidad]({{site.baseurl}}/api/api_limits) de la API de Braze para tus espacios de trabajo y así evitar errores. Si deseas aumentar tus límites de velocidad (y ya estás agrupando solicitudes en lotes), ponte en contacto con tu CSM or administrador de éxito de cliente or administrador de éxito de cliente. Ten en cuenta que este proceso requiere tiempo de preparación, así que planifica con antelación.
- [**Anulaciones necesarias de limitación de frecuencia**]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping): Hay algunas campañas, como los mensajes transaccionales, que siempre querrás que lleguen al usuario, incluso si ya has alcanzado su límite de frecuencia (por ejemplo, una notificación de entrega). Si deseas que una Campaign en particular anule las reglas de limitación de frecuencia, puedes configurarlo en el panel de Braze al programar la entrega de esa Campaign desactivando la limitación de frecuencia.

### Cosas que debes saber {#things-to-know}
- [**Grupos de control global**]({{site.baseurl}}/user_guide/audience/global_control_group): Si estás utilizando un grupo de control global, un porcentaje de usuarios no recibirá ninguna Campaign ni Canvas. (Puedes crear excepciones con la [configuración de exclusión]({{site.baseurl}}/user_guide/audience/global_control_group#step-3-assign-exclusion-settings)). Para ver una lista de estos usuarios, expórtalos mediante CSV o [API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group).
- [**Límites de velocidad de Canvas**]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping): En un Canvas, el límite de velocidad se aplica a todo el Canvas, no a los pasos individuales. Por ejemplo, si estableces un límite de velocidad de 10.000 mensajes por minuto en un Canvas con varios pasos, seguirá limitado a 10.000 mensajes porque el límite se habrá alcanzado en el primer paso.
- **Limitación de frecuencia**:
  - Las reglas de limitación de frecuencia se aplican a push, correo electrónico, servicio de mensajes cortos y webhooks, pero no a mensajes dentro de la aplicación ni a Content Cards.
  - La limitación de frecuencia global se programa según la zona horaria del usuario y se calcula por días calendario, no por períodos de 24 horas. Por ejemplo, si configuras una regla de limitación de frecuencia para enviar no más de una Campaign al día, un usuario puede recibir un mensaje a las 11 pm en su zona horaria local, y sería elegible para recibir otro mensaje una hora después.

{% alert tip %}
Para obtener más ayuda con la solución de problemas de Canvas y Campaign, asegúrate de ponerte en contacto con soporte de Braze dentro de los 30 días posteriores a la aparición de tu problema, ya que solo contamos con los últimos 30 días de registros de diagnóstico.
{% endalert %}

## Banners {#banners}

### Cosas que debes comprobar
- **Dimensiones de los Banners:** Crea tus Banners usando un elemento de dimensión fija y pruébalos en el editor.
- **Prioridad:** Si vas a lanzar varios Banners, puedes establecer manualmente la prioridad del modo en que se muestra cada banner.

### Cosas que debes saber
- **Personalización con Liquid:** La personalización con Liquid se actualiza en cada solicitud de actualización.
- **Ratio de ubicación y Banner:** Cada ubicación de Banner puede utilizarse en hasta 25 mensajes en un espacio de trabajo.
- **Clics e impresiones:** Los clics y las impresiones de los Banners se rastrean automáticamente con el SDK or kit de desarrollo de software.
- **Limitaciones:** Actualmente, las siguientes características no son compatibles: integración con Canvas, Campaigns activadas por API y basadas en acciones, contenido conectado, códigos promocionales y `catalog_items` con la [etiqueta `:rerender`]({{site.baseurl}}/user_guide/data/activation/catalogs/use#using-liquid).
- **Pruebas:** Para mostrar el Banner de prueba, el dispositivo que estés usando debe poder recibir notificaciones push en primer plano.
- **HTML personalizado:** Aprovecha el [puente JavaScript]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types/custom_html#javascript-bridge) para registrar clics cuando uses HTML personalizado para definir acciones de clic, como enlaces y botones. Las acciones de clic solo se registran automáticamente cuando se usan los componentes prediseñados en el editor de arrastrar y soltar.
- **Solicitud de ubicaciones:** Se pueden devolver hasta 10 ubicaciones al SDK or kit de desarrollo de software en una sola solicitud de actualización. Cada ubicación incluirá el Banner de mayor prioridad para el que un usuario sea elegible.

## Content Cards

### Cosas que comprobar
- **Tamaño de Content Cards**: Los campos de mensaje de Content Cards están limitados a 2&nbsp;KB en tamaño previo a la compresión, calculado sumando la longitud en bytes de los siguientes campos: título, mensaje, URL de imagen, texto del enlace, URLs del enlace y pares clave-valor. Los mensajes que superen este tamaño no se enviarán. Ten en cuenta que esto no incluye el tamaño de la imagen, sino la longitud de la URL de la imagen.
- **Actualización del texto después del envío**: Después de enviar una tarjeta, no podrás actualizar el texto de esa misma tarjeta. Consulta [Actualización de tarjetas enviadas]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card#updating-launched-cards) para entender cómo puedes abordar este escenario.

### Cosas que debes saber
- **Límite de Campaigns activas de Content Cards**: Puedes tener hasta 500 Campaigns activas de Content Cards. Este recuento incluye Content Cards enviadas con cualquiera de las opciones de [creación de tarjetas]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card).
- [**Términos de informes**]({{site.baseurl}}/user_guide/channels/content_cards/reporting): Revisa términos como impresiones totales, impresiones únicas y destinatarios únicos, ya que las definiciones a veces pueden causar confusión.
- **Actualización de Content Cards**: De forma predeterminada, Braze actualiza las solicitudes de Content Cards cuando se sincronizan al inicio de la sesión, al deslizar hacia abajo en el feed (móvil) y cuando se abre la vista de tarjetas si la última actualización fue hace más de un minuto.
- **Almacenamiento en caché de Content Cards**: Las opciones de almacenamiento en caché de Content Cards se pueden encontrar en nuestra documentación de [Android/FireOS]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style) y [Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#getcachedcontentcards).
- **Limitación de frecuencia**: La limitación de frecuencia no se aplica a Content Cards.
- **Impresiones**: Las impresiones generalmente se registran cuando se ve una tarjeta. Por ejemplo, si tienes un buzón de entrada lleno de Content Cards, no se registrará una impresión hasta que el usuario se desplace hasta la Content Card específica. Existen algunos matices entre las plataformas Web, Android e iOS.
- **Sesiones del SDK or kit de desarrollo de software y creación de tarjetas**: Las Content Cards no se crean para usuarios sin sesiones del SDK or kit de desarrollo de software, incluso si esos usuarios cumplen con los criterios del segmento. Sin embargo, si un usuario ya tiene una sesión de Android, las Content Cards con acciones de clic específicas de iOS se seguirán creando, y el usuario podrá ver esas Content Cards en iOS una vez que tenga una sesión allí. Consulta [Creación de tarjetas]({{site.baseurl}}/user_guide/channels/content_cards/create_a_content_card) para obtener más información sobre cuándo se crean las tarjetas.

## Correo electrónico {#email}

{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}

### Cosas que debes verificar
- **Consentimiento del cliente**: Antes de enviar tus correos electrónicos iniciales, es importante obtener primero el permiso de tus clientes. Consulta [Consentimiento y recopilación de direcciones]({{site.baseurl}}/user_guide/channels/email/email_setup/consent_and_address_collection) y nuestra [Política de uso aceptable de Braze](https://www.braze.com/company/legal/aup) para más información.
- **Volumen previsto**: 2 millones de correos electrónicos por día para una sola IP es la recomendación general, siempre que ese volumen haya sido [correctamente calentado]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming).
  - Si planeas enviar consistentemente un volumen mayor, para evitar que los proveedores limiten la recepción de correos electrónicos (lo que resultaría en una gran cantidad de rebotes blandos, una tasa de capacidad de entrega reducida y una reputación de IP disminuida), considera usar múltiples direcciones IP agrupadas en un pool de IP.
  - Si buscas enviar en un periodo de tiempo más corto, te recomendamos investigar qué tan rápido aceptan correos los diferentes proveedores para determinar la cantidad adecuada de IP desde las que enviar.

### Cosas que debes saber
- **Factores del volumen de envío**: Algunos factores que determinan las capacidades de volumen de envío de una IP incluyen:
  - Buzones de correo: Los grandes proveedores de correo electrónico probablemente pueden gestionar millones de correos por día desde una sola IP, mientras que un proveedor de buzones regional más pequeño o uno con una infraestructura menor podría no ser capaz de gestionar esa cantidad.
  - Reputación del remitente: Puedes enviar un volumen mayor por día desde una sola IP si el remitente ha sido escalado a ese volumen y si su reputación del remitente es lo suficientemente fuerte en cada buzón o dominio al que envía.
- **Prácticas recomendadas**: Consulta las [prácticas recomendadas de correo electrónico]({{site.baseurl}}/user_guide/channels/email/best_practices) de Braze y contacta a tu equipo de cuenta de Braze si deseas obtener más información sobre los servicios de capacidad de entrega.

## Mensajes dentro de la aplicación {#in-app-messages}

### Cosas que debes saber
- **Activación de mensajes dentro de la aplicación**: Al inicio de la sesión, el SDK or kit de desarrollo de software solicita que todos los mensajes dentro de la aplicación elegibles se envíen al dispositivo junto con sus desencadenantes, de modo que si el usuario realiza el evento durante la sesión, pueda recibir el mensaje dentro de la aplicación de forma rápida y fiable.
- **Enviados frente a impresiones**: Para los mensajes dentro de la aplicación, el concepto de "enviado" difiere de los otros canales disponibles. Para ver un mensaje dentro de la aplicación, un usuario tiene que iniciar una sesión, estar en la audiencia elegible y realizar la acción desencadenante. Por eso, hacemos seguimiento de las "impresiones", ya que resulta más claro.
- **Activación**: De forma predeterminada, los mensajes dentro de la aplicación se activan mediante eventos registrados por el SDK or kit de desarrollo de software. Si deseas activar mensajes dentro de la aplicación mediante eventos enviados desde el servidor, también puedes lograrlo a través de estas guías para [iOS]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages?tab=swift) y [Android]({{site.baseurl}}/developer_guide/in_app_messages/customization?sdktab=android).
- [Mensajes dentro de la aplicación en Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas#advancement-behavior): Estos mensajes aparecen la primera vez que el usuario abre la aplicación (activados por el inicio de sesión) después de que el mensaje programado en el componente de Canvas le ha sido enviado.
- **Llamadas de contenido conectado**: Usar contenido conectado te permite enviar contenido dinámico en los mensajes. Cuando envías mensajes a través de un canal como los mensajes dentro de la aplicación, esto puede crear más conexiones simultáneas a los dispositivos de tus usuarios (los mensajes se envían uno a uno en lugar de en lotes). Para gestionar esto, recomendamos aplicar una [limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) a tus mensajes.

## Push {#push}

### Cosas a comprobar
- [**Con adhesión voluntaria/suscrito y push habilitado**]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states): Para que los usuarios reciban un mensaje push de Braze, necesitan que sus estados de suscripción sean con adhesión voluntaria (iOS) o suscrito (Android) y `Push Enabled = True`. Ten en cuenta que Android 13 introduce un cambio importante en la forma en que los usuarios gestionan las aplicaciones que envían notificaciones push. La [guía de actualización del SDK or kit de desarrollo de software de Android 13]({{site.baseurl}}/developer_guide/platforms/android/android_13) de Braze seguirá actualizándose a medida que se publiquen nuevas versiones beta de Android 13.

### Cosas que debes saber
- **Push web**: Si tienes configurado el [SDK or kit de desarrollo de software Web]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/web) de Braze, considera utilizar el push web para interactuar con los usuarios. El push web funciona de la misma forma que las notificaciones push de aplicaciones en tu teléfono. Para más información sobre cómo redactar un push web, consulta [Crear una notificación push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message).
- **Dirigirse a una sola aplicación**: Revisa las [diferencias en la segmentación]({{site.baseurl}}/user_guide/get_started/workspaces) para dirigirte a una sola aplicación y sus usuarios.

## servicio de mensajes cortos

### Cosas que comprobar
- **Asignaciones y rendimiento**: Comprende qué asignaciones de servicio de mensajes cortos están actualmente vinculadas a tu cuenta (código abreviado, código largo y similares) y [cuánto rendimiento te proporcionan]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup) para confirmar que tienes suficiente rendimiento para enviar en el tiempo deseado.
- **Estimar segmentos a partir del texto del servicio de mensajes cortos**: Prueba el texto de tu servicio de mensajes cortos en la [calculadora de segmentos de servicio de mensajes cortos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator#segment-calculator). Ten en cuenta que el número de segmentos de servicio de mensajes cortos debe considerarse junto con tus capacidades de rendimiento. (Audiencia × segmentos de servicio de mensajes cortos = rendimiento necesario). Consulta las preguntas frecuentes de servicio de mensajes cortos sobre [cómo evitar excedentes]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs).
- **Leyes y regulaciones de servicio de mensajes cortos**: [Revisa las leyes, regulaciones y prevención de abuso de servicio de mensajes cortos]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations) para confirmar que estás utilizando los servicios de servicio de mensajes cortos en cumplimiento con todas las leyes aplicables. Asegúrate de buscar el asesoramiento de tu asesor legal antes de enviar.

### Cosas que debes saber
- **Envío predeterminado de mensajes servicio de mensajes cortos**: Los mensajes servicio de mensajes cortos normalmente se envían de forma predeterminada desde el código abreviado en el pool de remitentes.
- **ID de remitente alfanumérico**: La mensajería bidireccional ya no funcionará si utilizas un ID de remitente alfanumérico; ahora son solo unidireccionales.
- **Rendimiento actualizado en EE. UU.**: El rendimiento ha cambiado en EE. UU. con el [registro A2P 10DLC en EE. UU.](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US). Ten en cuenta que no nos comprometemos contractualmente con ningún SLA de velocidad de envío debido a múltiples factores como la congestión del tráfico y problemas con los operadores que pueden afectar las tasas de entrega reales.
- **Grupo de suscripción**: Para lanzar una Campaign de servicio de mensajes cortos a través de Braze, se debe seleccionar un grupo de suscripción. Además, para cumplir con las [directrices y normativas internacionales de telecomunicaciones]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations), Braze nunca enviará servicio de mensajes cortos a usuarios que no se hayan [suscrito al grupo de suscripción seleccionado]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups#check-a-users-group).

## WhatsApp

### Cosas que debes saber

- [**Mejores prácticas**]({{site.baseurl}}/user_guide/channels/whatsapp/best_practices): Revisa nuestras mejores prácticas sugeridas para WhatsApp.