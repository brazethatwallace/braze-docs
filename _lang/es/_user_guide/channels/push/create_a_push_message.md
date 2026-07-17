---
nav_title: "Crear un mensaje push"
article_title: "Crear un mensaje push"
page_order: 1
page_type: tutorial
description: "Esta página del tutorial cubre los diferentes componentes involucrados en la creación de un mensaje push, incluyendo configuración, envío, segmentación y más."
channel: push
tool:
  - Campaigns

---

# Crear un mensaje push {#create-a-push-message}

> Las notificaciones push son excelentes para llamadas a la acción urgentes, así como para volver a captar a usuarios que no han entrado en la aplicación en un tiempo. Las campañas push exitosas dirigen al usuario directamente al contenido y demuestran el valor de tu aplicación. Para ver ejemplos de notificaciones push, consulta los [casos de estudio de clientes de Braze](https://www.braze.com/customers).

## Paso 1: Elige dónde crear tu mensaje {#create-new-campaign-push}

{% alert tip %}
¿No estás seguro de si usar una campaña o un Canvas? Las campañas son mejores para campañas de mensajería únicas y dirigidas, mientras que los Canvas son mejores para recorridos de usuario de varios pasos.
{% endalert %}

{% tabs %}
{% tab Campaign %}
1. Ve a **Mensajería** > **Campaigns** y selecciona **Crear campaña**.
2. Para campañas dirigidas a múltiples canales, selecciona **Multicanal**. De lo contrario, selecciona **Notificación push**.
3. Ponle a tu campaña un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administer/global/user_management/teams) y [etiquetas]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags) según sea necesario.

{% alert tip %}
Las etiquetas facilitan encontrar tus campañas y generar informes a partir de ellas. Por ejemplo, al usar el [generador de informes]({{site.baseurl}}/user_guide/analytics/reports/report_builder), puedes filtrar por etiquetas específicas.
{% endalert %}

{: start="5"}
5. Añade y nombra tantas variantes como necesites para tu campaña. Puedes elegir diferentes plataformas, tipos de mensaje y diseños para cada una de las variantes añadidas. Para más información sobre este tema, consulta [Pruebas multivariante y A/B]({{site.baseurl}}/user_guide/messaging/ab_testing).

{% alert tip %}
Si todos los mensajes en tu campaña van a ser similares o tener el mismo contenido, redacta tu mensaje antes de añadir variantes adicionales. Luego puedes elegir **Copiar desde variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Crea tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas) usando el compositor de Canvas.
2. Después de configurar tu Canvas, añade un paso en el constructor de Canvas. Ponle a tu paso un nombre claro y significativo.
3. Elige una [planificación de paso]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/delivery_and_entry_types) y especifica un retraso según sea necesario.
4. Filtra tu audiencia para este paso según sea necesario. Puedes refinar aún más los destinatarios de este paso especificando segmentos y añadiendo filtros adicionales. Las opciones de audiencia se verificarán después del retraso en el momento en que se envíen los mensajes.
5. Elige tu [comportamiento de avance]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/cloning_canvases).
6. Elige cualquier otro canal de mensajería que desees emparejar con tu mensaje.

{% endtab %}
{% endtabs %}

## Paso 2: Selecciona las plataformas push {#step-2-select-push-platforms}

A continuación, elige qué combinación de plataforma y dispositivo móvil debe recibir el push. Usa esta selección para limitar la entrega de una notificación push a un conjunto específico de aplicaciones.

Hay varias formas de hacer esto dependiendo de tus selecciones anteriores:

| Selección anterior | Opciones |
| --- | --- |
| Campaña de notificación push | Selecciona una o más plataformas y dispositivos. Si eliges dirigirte a múltiples dispositivos y plataformas, tu experiencia de edición se optimiza para redactar un mensaje para todas las plataformas seleccionadas. Consulta [Push multiplataforma]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/multiple_platform_push) para entender qué es diferente en esta experiencia de edición. |
| Campaña multicanal | Selecciona **Añadir canal de mensajería** para agregar plataformas push adicionales. Dado que las selecciones de plataforma son específicas de cada variante, puedes probar la interacción del mensaje por plataforma. |
| Canvas | En tu paso de mensaje, selecciona **+ Añadir más** para agregar plataformas push adicionales. Similar a las campañas multicanal, las selecciones de plataforma son específicas de cada variante. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2: Selecciona las plataformas push" }

## Paso 3: Selecciona el tipo de notificación (iOS y Android) {#step-3-select-notification-type-ios-and-android}

Si estás creando una campaña push multiplataforma y seleccionas Web o Kindle, el tipo de notificación se establece automáticamente en **Push estándar** y no se puede cambiar.

![Tipo de notificación con push estándar seleccionado como ejemplo.]({% image_buster /assets/img_archive/push_2.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

De lo contrario, para iOS y Android, selecciona tu tipo de notificación:

- Push estándar
- [Historias push]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories) (compatible con Android + iOS)
- Imagen en línea (solo Android)

Si deseas incluir imágenes en tu campaña push, consulta las siguientes guías sobre cómo crear una notificación enriquecida para [iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications) o [Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/rich_notifications).

## Paso 4: Redacta tu mensaje push {#step-4-compose-your-push-message}

¡Ahora es el momento de escribir tu mensaje push! La pestaña **Compose** te permite editar todos los aspectos del contenido y comportamiento de tu mensaje.

![Pestaña Compose de la creación de una notificación push.]({% image_buster /assets/img_archive/push_multiple_platform_message_composer.png %})

El contenido de la pestaña **Compose** varía según el tipo de notificación elegido en el paso anterior, pero puede incluir cualquiera de las siguientes opciones:

### Canal o grupo de notificación (iOS y Android) {#notification-channel-or-group-ios-and-android}

Para más información sobre las opciones de notificación específicas de cada plataforma, consulta [Opciones de notificación de iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options) u [Opciones de notificación de Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/notification_options).

### Idioma {#language}

Añade texto en múltiples idiomas usando el botón **Add Languages**. Te recomendamos seleccionar tus idiomas antes de escribir tu contenido para que puedas completar tu texto donde corresponda en Liquid. Para nuestra lista completa de idiomas disponibles que puedes usar, consulta [Idiomas compatibles]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization#languages-supported).

Si estás añadiendo texto en un idioma que se escribe de derecha a izquierda, ten en cuenta que la apariencia final de los mensajes de derecha a izquierda depende en gran medida de cómo los proveedores de servicios los renderizan. Para conocer las mejores prácticas sobre cómo crear mensajes de derecha a izquierda que se muestren con la mayor precisión posible, consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).

### Título y cuerpo {#title-and-body}

{% tabs local %}
{% tab ios %}
Comienza a escribir en el cuadro de mensaje y observa cómo aparece una vista previa en el cuadro de vista previa junto a él. Los mensajes push deben estar formateados en texto plano.

Añade un encabezado usando el campo **Title**. Para hacer tu push personalizado y dirigido, puedes incluir [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid).
{% endtab %}

{% tab android %}
Comienza a escribir en el cuadro de mensaje y observa cómo aparece una vista previa en el cuadro de vista previa junto a él. Los mensajes push deben estar formateados en texto plano.

Para hacer tu push personalizado y dirigido, puedes incluir [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid).

{% alert important %}
**No puedes** enviar un mensaje push de Android sin un título&#8212;sin embargo, puedes introducir un solo espacio en su lugar. Ten en cuenta que si tu mensaje solo contiene un solo espacio, se enviará como una notificación push silenciosa. Para más información, consulta [Notificaciones push silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=android).
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
¿Necesitas ayuda para crear un texto excelente? Prueba usar el [asistente de redacción con IA]({{site.baseurl}}/user_guide/brazeai/operator/capabilities#generate-copy). Introduce un nombre o descripción de producto y la IA generará un texto de marketing similar al humano para usar en tu mensajería.

![Botón Lanzar redactor con IA, ubicado en el campo Cuerpo del compositor push.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_push.png %}){: style="max-width:60%"}
{% endalert %}

### Imagen {#image}

Donde sea compatible, el icono de tu aplicación se añade automáticamente como la imagen de tu notificación push. También tienes la opción de enviar notificaciones enriquecidas, que permiten más personalización en tus notificaciones push al añadir contenido adicional más allá del texto.

Para orientación adicional sobre el uso de imágenes en tus notificaciones push, consulta los siguientes artículos:

- [Crear notificaciones enriquecidas para iOS]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/rich_notifications)
- [Crear notificaciones enriquecidas para Android]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/android/rich_notifications)

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

### Comportamiento al hacer clic {#on-click-behavior}

Especifica qué sucede cuando un usuario selecciona el cuerpo de una notificación push con **On-Click Behavior**. Por ejemplo, puedes solicitar a los clientes que abran tu aplicación, redirigir a los clientes a una URL web específica, o incluso abrir una página específica de tu aplicación con un [vínculo profundo]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls).

Aquí también puedes configurar indicaciones de botones dentro de tu notificación push, como:

- Aceptar/Rechazar
- Sí/No
- Confirmar/Cancelar
- Más

### Opciones de envío {#sending-options}

Si un usuario tiene tu aplicación instalada en múltiples dispositivos, de forma predeterminada, tu mensaje push se envía a todos los dispositivos con un token de push válido asignado. Si lo deseas, puedes seleccionar **Dispositivo usado más recientemente**.

![Casilla de opciones de dispositivo para enviar este push solo al dispositivo usado más recientemente del usuario.]({% image_buster /assets/img_archive/push_recent_device.png %}){: style="max-width:70%;" }

Hay algunos matices para esta configuración. Si se selecciona esta opción, Braze limitará los envíos múltiples excepto cuando una campaña se dirija a múltiples plataformas, como iOS y Android. Si el usuario tiene tu aplicación tanto en un dispositivo iOS como en uno Android, recibirá un push para ambas plataformas. Si el dispositivo usado más recientemente de un usuario no tiene [push habilitado]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#foreground-push-enabled), el mensaje no se enviará.

De forma predeterminada, Braze envía mensajes a cada dispositivo que posee un usuario y que tiene un token de push válido. Para iOS, puedes refinar aún más tu alcance eligiendo enviar notificaciones solo a dispositivos iPad, o solo a dispositivos iPhone e iPod.

Si lo deseas, puedes establecer el destino del push en **Dispositivo usado más recientemente**.

#### Dispositivo usado más recientemente {#most-recently-used-device}

"Usado más recientemente" es un estado técnico, no conductual. Dado que Braze envía por defecto a todos los dispositivos, cambiar a esta configuración reduce significativamente tu alcance y depende completamente del estado del único dispositivo con el token más reciente.

El dispositivo usado más recientemente se determina por cuál dispositivo tiene el token de push actualizado más recientemente, en lugar de cuál dispositivo tuvo la sesión más reciente.
* Si se añade un token de push de un nuevo dispositivo a un perfil de usuario a través de la API, ese dispositivo se considera inmediatamente como el usado más recientemente, incluso si el usuario aún no ha iniciado una sesión en él.
* Si el dispositivo usado más recientemente de un usuario no tiene [push habilitado]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#foreground-push-enabled), el mensaje no se enviará en absoluto.

Los envíos múltiples aún pueden ocurrir si una campaña se dirige a diferentes plataformas, como iOS y Android. Si un usuario tiene la aplicación en ambas, puede recibir un push para ambas plataformas.

Para iOS, puedes limitar aún más la mensajería enviando notificaciones push solo a dispositivos iPad, o enviando solo a dispositivos iPhone e iPod.

## Paso 5: Previsualiza y prueba tu mensaje (opcional) {#step-5-preview-and-test-your-message-optional}

Probar es posiblemente uno de los pasos más críticos. Después de terminar de redactar tu mensaje push perfecto, pruébalo antes de enviarlo. Selecciona la pestaña **Test** para elegir entre las opciones de cómo probar tu mensaje push. En **Destinatarios de prueba**, puedes seleccionar un grupo de prueba de contenido o usuarios individuales. También puedes usar **Previsualizar mensaje como usuario** para tener una idea de cómo puede verse tu mensaje en el móvil para un usuario aleatorio, un usuario existente, un usuario personalizado o un usuario multilingüe.

Para más información, consulta [Enviar mensajes de prueba]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=push).

## Paso 6: Construye el resto de tu campaña o Canvas {#step-6-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab Campaign %}

Construye el resto de tu campaña; consulta las siguientes secciones para más detalles sobre cómo usar mejor nuestras herramientas para crear notificaciones push.

### Elige la planificación de entrega o el desencadenante {#choose-delivery-schedule-or-trigger}

Los mensajes push pueden entregarse según un horario planificado, una acción o un desencadenante de API. Para más información, consulta [Planificar tu campaña]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign).

Para la entrega basada en acciones, también puedes establecer la duración de la campaña y las [horas tranquilas]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours).

En este paso también puedes especificar controles de entrega, como permitir que los usuarios vuelvan a ser [elegibles]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility) para recibir la campaña, o habilitar reglas de [limitación de frecuencia]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping).

### Elige los usuarios objetivo {#choose-users-to-target}

A continuación, debes [dirigirte a los usuarios]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users) eligiendo segmentos o filtros para reducir tu audiencia. Recibirás automáticamente una vista previa de cómo se ve la población aproximada de ese segmento. Las estadísticas detalladas de audiencia para los canales a los que se dirige tu campaña están disponibles en el pie de página. Para ver qué porcentaje de tu base de usuarios está siendo objetivo y el valor de duración del ciclo de vida para este segmento, selecciona **Mostrar estadísticas adicionales**.

{% multi_lang_include audience/target_audiences.md %}

{% details ¿Por qué mi métrica de total de usuarios alcanzables no coincide con la suma de todos los canales? %}

Cuando ves el total de usuarios alcanzables para tu audiencia filtrada, puedes notar que la suma de las columnas individuales es menor que el total de usuarios alcanzables. Esta diferencia generalmente se debe a que hay varios usuarios que califican para el segmento o los filtros de la campaña, pero no son alcanzables a través de push (por ejemplo, porque no tienen [tokens de push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle#push-tokens) válidos o activos).

{% enddetails %}

![Tabla de estadísticas detalladas de audiencia para usuarios alcanzables.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

Ten en cuenta que la membresía exacta del segmento siempre se calcula antes de que se envíe el mensaje.

También puedes elegir enviar tu campaña solo a usuarios que tengan un [estado de suscripción]({{site.baseurl}}/user_guide/channels/email/subscriptions) específico, como aquellos que están suscritos y han optado por recibir push.

Opcionalmente, también puedes limitar la entrega a un número específico de usuarios dentro del segmento, o permitir que los usuarios reciban el mismo mensaje dos veces en caso de recurrencia de la campaña.

#### Campañas multicanal con correo electrónico y push {#multichannel-campaigns-with-email-and-push}

Para campañas multicanal dirigidas tanto a canales de correo electrónico como de push, es posible que desees limitar tu campaña para que solo los usuarios que hayan optado explícitamente reciban el mensaje (excluyendo a los usuarios suscritos o que cancelaron su suscripción). Por ejemplo, supongamos que tienes tres usuarios con diferentes estados de adhesión:

- **Usuario A** está suscrito al correo electrónico y tiene push habilitado. Este usuario no recibe el correo electrónico pero recibirá el push.
- **Usuario B** ha optado por recibir correo electrónico pero no tiene push habilitado. Este usuario recibirá el correo electrónico pero no recibirá el push.
- **Usuario C** ha optado por recibir correo electrónico y tiene push habilitado. Este usuario recibirá tanto el correo electrónico como el push.

Para hacerlo, en **Resumen de audiencia**, selecciona enviar esta campaña a "solo usuarios que han optado por recibir". Esta opción asegurará que solo los usuarios que han optado recibirán tu correo electrónico, y Braze solo enviará tu push a los usuarios que tienen push habilitado de forma predeterminada.

{% alert important %}
Con esta configuración, no incluyas ningún filtro en el paso **Públicos objetivo** que limite la audiencia a un solo canal (por ejemplo, `Foreground Push Enabled = True` o `Email Subscription = Opted-In`).
{% endalert %}

### Elige eventos de conversión {#choose-conversion-events}

Braze te permite rastrear con qué frecuencia los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events), después de recibir una campaña. Tienes la opción de permitir una ventana de hasta 30 días durante la cual se contará una conversión si el usuario realiza la acción especificada.

{% endtab %}

{% tab Canvas %}

Si aún no lo has hecho, completa las secciones restantes de tu componente de Canvas. Para más detalles sobre cómo construir el resto de tu Canvas, implementar pruebas multivariante y selección inteligente, y más, consulta el paso [Construir tu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas) de nuestra documentación de Canvas.

{% endtab %}
{% endtabs %}

## Paso 7: Revisa y despliega {#review-and-deploy-push}

Después de terminar de construir la última parte de tu campaña o Canvas, revisa sus detalles. Para las campañas, la página final te ofrece un resumen de la campaña que diseñaste. Confirma todos los detalles relevantes, asegúrate de haber probado tu mensaje, luego envíalo y ¡observa cómo llegan los datos!

A continuación, consulta [Informes push]({{site.baseurl}}/user_guide/channels/push/reporting) para aprender cómo puedes acceder a los resultados de tu campaña push. Para las notificaciones push, podrás ver estadísticas del número de mensajes enviados, entregados, rebotados, abiertos y abiertos directamente.

### Solución de problemas {#troubleshooting}

#### Comportamiento al hacer clic

Si estás usando el comportamiento al hacer clic predeterminado para tu versión del SDK y al seleccionar una notificación push con una URL web se abre dentro de la aplicación en lugar de en un navegador web, consulta las siguientes guías de integración para determinar el manejo de notificaciones push:

- [Swift]({{site.baseurl}}/developer_guide/push_notifications?sdktab=swift#swift_step-2-enable-push-capabilities)
- [Android]({{site.baseurl}}/developer_guide/push_notifications#android_step-1-register-braze-firebase-messaging-service)

{% alert important %}
Debes asignar tu objeto delegado usando `center.delegate = self` de forma sincrónica antes de que tu aplicación termine de lanzarse, preferiblemente en `application:didFinishLaunchingWithOptions:`. De lo contrario, tu aplicación podría perder notificaciones push entrantes. Consulta la [documentación de `UNUserNotificationCenterDelegate` de Apple](https://developer.apple.com/documentation/usernotifications/unusernotificationcenterdelegate) para obtener más información.
{% endalert %}