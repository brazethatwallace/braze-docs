---
page_order: 10.9
nav_title: Solución de problemas
article_title: Solución de problemas de notificaciones push para el SDK de Braze
description: "Diagnostica problemas de entrega y visualización de notificaciones push utilizando un índice de síntomas, una ruta de investigación estándar y comprobaciones específicas del SDK por plataforma."
channel:
  - push notifications
---

# Solución de problemas de notificaciones push {#troubleshoot-push-notifications}

> Usa esta página para diagnosticar problemas de entrega y visualización de notificaciones push en un dispositivo. Para comprobaciones de entrega del lado del panel (estado de suscripción, Segments, límites), consulta [Solución de problemas de push]({{site.baseurl}}/user_guide/channels/push/troubleshooting).

Antes de depurar, añádete como [usuario de prueba]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups#adding-test-users) y revisa [Envío de mensajes de prueba]({{site.baseurl}}/developer_guide/push_notifications/sending_test_messages).

## Empieza aquí: identifica tu síntoma {#start-here-match-your-symptom}

Busca el comportamiento que estás viendo en la tabla y sigue los pasos de esa sección. Si no estás seguro de qué sección aplica, usa la [ruta de investigación estándar](#standard-investigation-path).

| Síntoma | Ir a |
| --- | --- |
| Push no recibido en una plataforma | Selecciona tu pestaña de SDK en [Solución de problemas específica de la plataforma](#platform-specific-troubleshooting) |
| Los saltos de línea alrededor de las etiquetas de Liquid se ven mal al guardar | [Saltos de línea en las notificaciones push](#push-linebreaks) |
| Verificaciones de entrega del panel (suscripción, Segment, límites) | [Solución de problemas de push]({{site.baseurl}}/user_guide/channels/push/troubleshooting) |
| El vínculo profundo desde push no se abre correctamente | [Solución de problemas de vinculación en profundidad]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting) |
| Códigos de error push comunes | [Mensajes de error push comunes]({{site.baseurl}}/user_guide/channels/push/push_error_codes) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Síntoma de push del SDK" }

## Ruta de investigación estándar {#standard-investigation-path}

Usa este flujo de trabajo para cada incidente de notificación push. Empieza en el paso 1.

1. Confirma que el dispositivo tiene un token de notificaciones push válido y que el permiso de push está concedido en la configuración del dispositivo.
2. En el panel, confirma que el usuario de prueba coincide con el [Segment]({{site.baseurl}}/user_guide/channels/push/troubleshooting#segment) de la Campaign o Canvas y que no está en el [grupo de control]({{site.baseurl}}/user_guide/channels/push/troubleshooting#control-group-status).
3. Envía una [notificación push de prueba]({{site.baseurl}}/developer_guide/push_notifications/sending_test_messages) al dispositivo de prueba.
4. [Habilita el registro detallado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging), reproduce el problema y revisa la guía específica de la plataforma en tu [pestaña del SDK](#platform-specific-troubleshooting).
5. Si el problema persiste, ponte en contacto con [soporte de Braze]({{site.baseurl}}/braze_support) con los registros detallados, la plataforma, la versión del SDK y el ID de la Campaign o Canvas.

## Solución de problemas específica de la plataforma {#platform-specific-troubleshooting}

Selecciona la pestaña de tu SDK para verificaciones de configuración y visualización específicas de la plataforma.

{% sdktabs %}
{% sdktab web %}
## Solución de problemas {#troubleshooting}

Si tienes problemas después de configurar las notificaciones push, ten en cuenta lo siguiente:

- Las notificaciones push web requieren que tu sitio sea HTTPS.
- No todos los navegadores pueden recibir mensajes push. Asegúrate de que `braze.isPushSupported()` devuelva `true` en el navegador.
- Algunos navegadores, como Firefox, no muestran imágenes en las notificaciones push. Para más detalles sobre la compatibilidad de navegadores, consulta la [documentación de MDN para imágenes de Notification](https://developer.mozilla.org/en-US/docs/Web/API/Notification/image).
- Si un usuario ha denegado el acceso push a un sitio, no se le volverá a solicitar permiso a menos que elimine el estado denegado de las preferencias de su navegador.

{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab swift %}
## Comprender el flujo de trabajo Braze/APN {#understanding-the-brazeapns-workflow}

El servicio de notificaciones push de Apple (APN) es la infraestructura para enviar notificaciones push a las aplicaciones que se ejecutan en las plataformas de Apple. Aquí tienes la estructura simplificada de cómo se habilitan las notificaciones push para los dispositivos de tus usuarios y cómo Braze puede enviarles notificaciones push:

{% multi_lang_include developer_guide/push_notifications/push_registration_flow_steps.md %}

### Paso 1: Configurar el certificado push y el perfil de aprovisionamiento {#step-1-configuring-the-push-certificate-and-provisioning-profile}

Para desarrollar tu aplicación, crea un certificado SSL para habilitar las notificaciones push. Este certificado se incluye en el perfil de aprovisionamiento con el que se compila tu aplicación y también debe cargarse en el panel de Braze. El certificado permite a Braze indicar a los APN que está autorizado para enviar notificaciones push en tu nombre.

Existen dos tipos de [perfiles de aprovisionamiento](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) y certificados: desarrollo y distribución. Recomendamos usar solo perfiles y certificados de distribución para evitar confusiones. Si decides usar perfiles y certificados diferentes para desarrollo y distribución, asegúrate de que el certificado cargado en el panel coincida con el perfil de aprovisionamiento que estás usando actualmente.

{% alert warning %}
No cambies el entorno del certificado push (desarrollo frente a producción). Cambiar el certificado push al entorno incorrecto puede provocar que los tokens push de tus usuarios se eliminen accidentalmente, haciéndolos inalcanzables por push.
{% endalert %}

### Paso 2: Los dispositivos se registran en los APN y proporcionan a Braze los tokens push {#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens}

Cuando los usuarios abren tu aplicación, se les solicita aceptar las notificaciones push. Si aceptan esta solicitud, los APN generan un token push para ese dispositivo en particular. El SDK de Swift envía el token push de forma inmediata y asíncrona para las aplicaciones que usan la [política de vaciado automático]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/advanced_use_cases/fine_network_traffic_control#automatic-request-processing) predeterminada. Una vez que tenemos un token push asociado a un usuario, aparecerá como "Push Registered" en el panel, en su perfil de usuario en la pestaña **Engagement**, y será elegible para recibir notificaciones push de Campaigns de Braze.

{% alert note %}
A partir de macOS 13, en ciertos dispositivos, puedes probar las notificaciones push en un simulador de iOS 16 ejecutándose en Xcode 14. Para más detalles, consulta las [notas de la versión de Xcode 14](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

#### Consideraciones sobre la generación de tokens push {#considerations-for-push-token-generation}

- Si los usuarios instalan tu aplicación en otro dispositivo, Braze crea y captura otro token de la misma manera.
- Si los usuarios reinstalan tu aplicación, el SDK genera un nuevo token y lo pasa a Braze. Sin embargo, los APN y Braze pueden seguir registrando el token original como válido.
- Si los usuarios desinstalan tu aplicación, Braze no recibe una notificación de inmediato y el token sigue apareciendo como válido hasta que los APN lo retiran.
- En algún momento, los APN retiran los tokens antiguos. Braze no controla ni tiene visibilidad sobre este proceso.

### Paso 3: Lanzar una Campaign push de Braze {#step-3-launching-a-braze-push-campaign}

Cuando se lanza una Campaign push, Braze realiza solicitudes a los APN para entregar tu mensaje. En concreto, las solicitudes se pasan a los APN para cada token push válido actual, a menos que se seleccione **Enviar al dispositivo más reciente del usuario**. Después de que Braze recibe una respuesta exitosa de los APN, registra una entrega exitosa en el perfil del usuario, aunque el usuario puede no haber recibido el mensaje real por razones que incluyen:
- Su dispositivo está apagado.
- Su dispositivo no está conectado a internet (Wi-Fi o datos móviles).
- Desinstaló la aplicación recientemente.

Braze usa el certificado SSL push cargado en el panel para autenticarse y verificar que está autorizado para enviar notificaciones push a los tokens push proporcionados. Si un dispositivo está en línea, la notificación debería recibirse poco después de que se haya enviado la Campaign. Ten en cuenta que Braze establece la [fecha de expiración](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) predeterminada de los APN para las notificaciones en 30 días.

### Paso 4: Eliminar tokens no válidos {#step-4-removing-invalid-tokens}

Si los [APN](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) nos informan de que alguno de los tokens push a los que intentamos enviar un mensaje no es válido, eliminamos esos tokens de los perfiles de usuario a los que estaban asociados.

{% alert note %}
Es normal que los APN devuelvan inicialmente un estado de éxito incluso si un token deja de estar registrado, ya que los APN no informan de inmediato sobre los eventos de invalidación de tokens. Los APN retrasan intencionadamente la devolución de un estado `410` para tokens no válidos de forma aleatoria, diseñado para proteger la privacidad del usuario y evitar el seguimiento de desinstalaciones de aplicaciones. Puedes seguir enviando notificaciones de forma segura a un token no registrado hasta que los APN devuelvan un estado `410`.
{% endalert %}

## Usar los registros de errores push {#using-the-push-error-logs}

El [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab) te permite ver cualquier mensaje (especialmente mensajes de error) asociado con tus Campaigns y envíos, incluidos los errores de notificaciones push. Este registro de errores proporciona diversas advertencias que pueden ser muy útiles para identificar por qué tus Campaigns no funcionan como se esperaba. Al seleccionar un mensaje de error, se te redirige a la documentación pertinente para ayudarte a solucionar un incidente en particular.

![Registros de errores push que muestran la hora en que ocurrió el error, el nombre de la aplicación, el canal, el tipo de error y el mensaje de error.]({% image_buster /assets/img_archive/message_activity_log.png %})

Los errores comunes que podrías ver aquí incluyen notificaciones específicas del usuario, como ["Received Unregistered Sending to Push Token"](#swift_received-unregistered-sending).

Además, Braze también proporciona un registro de cambios push en el perfil de usuario en la pestaña **Engagement**. Este registro de cambios ofrece información sobre el comportamiento del registro push, como la invalidación de tokens, los errores de registro push, los tokens que se transfieren a nuevos usuarios, etc.

![Pestaña Engagement del perfil de usuario de Braze que muestra el registro de cambios del registro push.]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

### Errores del Registro de actividad de mensajes {#message-activity-log-errors}

#### Received unregistered sending to push token {#received-unregistered-sending}

- Asegúrate de que el token push que se envía a Braze desde el método `AppDelegate.braze?.notifications.register(deviceToken:)` sea válido. Puedes consultar el **Registro de actividad de mensajes** para ver el token push. Debería parecerse a algo como `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, una cadena larga que contiene una combinación de letras y números. Si tu token push tiene un aspecto diferente, revisa tu [código]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-32-register-push-tokens-with-braze) para enviar los tokens push a Braze.
- Asegúrate de que tu perfil de aprovisionamiento push coincida con el entorno en el que estás probando. Los certificados universales pueden configurarse en el panel de Braze para enviar al entorno de APN de desarrollo o de producción. Usar un certificado de desarrollo para una aplicación de producción o un certificado de producción para una aplicación de desarrollo no funcionará.
 - Verifica que el token push que has cargado en Braze coincida con el perfil de aprovisionamiento que usaste para compilar la aplicación desde la que enviaste el token push.

#### Device token not for topic {#device-token-not-for-topic}

Los APN devuelven `DeviceTokenNotForTopic` (estado HTTP 400) cuando el token push no coincide con el tema (ID de paquete) configurado para tus credenciales. Braze puede mostrar esto en el **Registro de actividad de mensajes** o en los registros de entrega push como `DeviceTokenNotForTopic`.

Para resolver la discrepancia:

1. Confirma que el **ID de paquete** de la aplicación coincide con el **App Bundle ID** en Braze (**Configuración** > **Configuración de la aplicación** > **Configuración de notificaciones push**).
2. Verifica que el perfil de aprovisionamiento usado para compilar la aplicación incluya la capacidad push para ese ID de paquete.
3. Confirma que la credencial push cargada en Braze coincide con el entorno de la aplicación (desarrollo frente a producción).
4. Para claves `.p8`, verifica que el **Team ID** y el **Key ID** en Braze coincidan con tu cuenta de Apple Developer.
5. Vuelve a cargar una clave `.p8` o un certificado `.p12` válido si las credenciales se rotaron o revocaron.

Prefiere las claves de autenticación `.p8` cuando sea posible. Para tipos de credenciales e indicadores de estado del panel, consulta [Migrar a una clave de autenticación .p8]({{site.baseurl}}/user_guide/channels/push/troubleshooting#migrate-to-a-p8-authentication-key).

#### BadDeviceToken sending to push token {#baddevicetoken-sending-to-push-token}

El `BadDeviceToken` es un código de error de los APN y no tiene su origen en Braze. Puede haber varias razones por las que se devuelve esta respuesta, entre ellas:

{% multi_lang_include developer_guide/push_notifications/invalid_push_token_reasons.md %}

## Problemas con el registro push {#push-registration-issues}

### No aparece la solicitud de registro push {#no-push-registration-prompt}

Si la aplicación no te solicita registrarte para las notificaciones push, es probable que haya un problema con la integración del registro push. Asegúrate de haber seguido nuestra [documentación]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) e integrado correctamente nuestro registro push. También puedes establecer puntos de interrupción en tu código para asegurarte de que se está ejecutando el código de registro push.

### No aparecen usuarios "push registered" en el panel (antes de enviar mensajes) {#no-push-registered-users-showing-in-the-dashboard-prior-to-sending-messages}

Asegúrate de que tu aplicación esté correctamente configurada para permitir las notificaciones push. Los puntos de fallo comunes que debes verificar incluyen:

- Comprueba que tu aplicación te solicita permitir las notificaciones push. Normalmente, esta solicitud aparecerá en la primera apertura de la aplicación, pero puede programarse para que aparezca en otro lugar. Si no aparece donde debería, es probable que el problema esté en la configuración básica de las capacidades push de tu aplicación.
  - Verifica que los pasos de [integración push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) se hayan completado correctamente.
  - Comprueba que el perfil de aprovisionamiento con el que se compiló tu aplicación incluya permisos para push. Asegúrate de estar descargando todos los perfiles de aprovisionamiento disponibles de tu cuenta de Apple Developer. Para confirmarlo, sigue estos pasos:
    1. En Xcode, ve a **Preferences > Accounts** (o usa el atajo de teclado <kbd>Command</kbd>+<kbd>,</kbd>).
    2. Selecciona el Apple ID que usas para tu cuenta de desarrollador y haz clic en **View Details**.
    3. En la siguiente página, haz clic en **<i class="fas fa-redo-alt"></i> Refresh** y confirma que estás descargando todos los perfiles de aprovisionamiento disponibles.
- Comprueba que has [habilitado correctamente la capacidad push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-2-enable-push-capabilities) en tu aplicación.
- Comprueba que tu perfil de aprovisionamiento push coincida con el entorno en el que estás probando. Los certificados universales pueden configurarse en el panel de Braze para enviar al entorno de APN de desarrollo o de producción. Usar un certificado de desarrollo para una aplicación de producción o un certificado de producción para una aplicación de desarrollo no funcionará.
- Comprueba que estás llamando a nuestro método `registerPushToken` estableciendo un punto de interrupción en tu código.
- Asegúrate de que estás probando con un dispositivo (push no funciona en un simulador) y que tienes buena conectividad de red.

## Notificaciones push enviadas pero no mostradas en los dispositivos de los usuarios {#push-notifications-sent-but-not-displayed-on-users-devices}

### Los usuarios "push registered" ya no están habilitados después de enviar mensajes {#push-registered-users-no-longer-enabled-after-sending-messages}

Es probable que esto indique que el usuario tenía un token push no válido. Esto puede ocurrir por varias razones:

#### Discrepancia entre el certificado del panel y la aplicación {#dashboard-and-app-certificate-mismatch}

Si el certificado push que cargaste en el panel no es el mismo que está en el perfil de aprovisionamiento con el que se compiló tu aplicación, los APN rechazarán el token. Verifica que has cargado el certificado correcto y completa otra sesión en la aplicación antes de intentar otra notificación de prueba.

#### La aplicación fue desinstalada {#application-was-uninstalled}

Si un usuario ha desinstalado tu aplicación, su token push será no válido y se eliminará en el siguiente envío.

#### Regenerar tu perfil de aprovisionamiento {#regenerating-your-provisioning-profile}

Como último recurso, empezar de nuevo y crear un perfil de aprovisionamiento completamente nuevo puede resolver los errores de configuración que surgen de trabajar con múltiples entornos, perfiles y aplicaciones al mismo tiempo. Hay muchas "piezas móviles" en la configuración de las notificaciones push, por lo que a veces es mejor volver a empezar desde el principio. Esto también ayudará a aislar el problema si necesitas continuar con la solución de problemas.

### Mensajes no entregados a usuarios "push registered" {#messages-not-delivered-to-push-registered-users}

#### La aplicación está en primer plano {#app-is-foregrounded}

En las versiones de iOS que no integran push a través del framework `UserNotifications`, si la aplicación está en primer plano cuando se recibe el mensaje push, este no se mostrará. Debes poner la aplicación en segundo plano en tus dispositivos de prueba antes de enviar mensajes de prueba.

#### Notificación de prueba programada incorrectamente {#test-notification-scheduled-incorrectly}

Revisa la programación que estableciste para tu mensaje de prueba. Si está configurada con entrega en zona horaria local o [sincronización inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing), es posible que simplemente aún no hayas recibido el mensaje (o que la aplicación estuviera en primer plano cuando se recibió).

### El usuario no está "push registered" para la aplicación que se está probando {#user-not-push-registered-for-the-app-being-tested}

Revisa el perfil del usuario al que intentas enviar un mensaje de prueba. En la pestaña **Engagement**, debería haber una lista de "aplicaciones con push habilitado". Verifica que la aplicación a la que intentas enviar mensajes de prueba esté en esta lista. Los usuarios aparecerán como "Push Registered" si tienen un token push para cualquier aplicación en tu espacio de trabajo, por lo que esto podría ser un falso positivo.

Lo siguiente indicaría un problema con el registro push o que el token del usuario fue devuelto a Braze como no válido por los APN después de haber sido enviado:

![Un perfil de usuario que muestra la configuración de contacto de un usuario. Debajo de Push, se muestra "No Apps".]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## Los clics en push no se registran {#push-clicks-not-logged}

- Asegúrate de haber seguido los [pasos de integración push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling).
- Braze no gestiona las notificaciones push recibidas silenciosamente en primer plano (comportamiento predeterminado de push en primer plano antes del framework `UserNotifications`). Esto significa que los enlaces no se abrirán y los clics en push no se registrarán. Si tu aplicación aún no ha integrado el framework `UserNotifications`, Braze no gestionará las notificaciones push cuando el estado de la aplicación sea `UIApplicationStateActive`. Asegúrate de que tu aplicación no retrase las llamadas a los [métodos de gestión push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_step-33-enable-push-handling); de lo contrario, el SDK de Swift puede tratar las notificaciones push como eventos push silenciosos en primer plano y no gestionarlos.

## Los vínculos profundos no funcionan {#deep-links-not-working}

Para una solución de problemas integral en todos los canales —incluidos los enlaces universales, los esquemas personalizados, el correo electrónico y proveedores externos como Branch— consulta [Solución de problemas de vinculación en profundidad]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).

### Los enlaces web desde clics push no se abren {#web-links-from-push-clicks-not-opening}

Los enlaces en las notificaciones push deben cumplir con ATS para abrirse en vistas web. Asegúrate de que tus enlaces web usen HTTPS. Para más información, consulta [Cumplimiento de ATS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/advanced_use_cases/linking#app-transport-security-ats).

### Los vínculos profundos desde clics push no se abren {#deep-links-from-push-clicks-not-opening}

La mayor parte del código que gestiona los vínculos profundos también gestiona las aperturas de push. Primero, asegúrate de que se estén registrando las aperturas de push. Si no es así, corrige ese problema (ya que la corrección a menudo también soluciona la gestión de enlaces).

Si las aperturas se están registrando, verifica si se trata de un problema con el vínculo profundo en general o con la gestión de clics push de vinculación en profundidad. Para ello, prueba si un vínculo profundo desde un clic en un mensaje dentro de la aplicación funciona.

### Los toques en imágenes de Push Story no hacen nada {#push-story-image-taps-do-nothing}

Si tocar una imagen de Push Story no hace nada, abre el `Info.plist` de la Notification Content Extension y confirma que `UNNotificationExtensionUserInteractionEnabled` sea `YES`. El módulo `BrazePushStory` del SDK de Swift necesita esa clave para que la extensión pueda recibir toques. Consulta [Push Stories]({{site.baseurl}}/developer_guide/push_notifications/push_stories/?sdktab=swift).

{% endsdktab %}

{% sdktab fireos %}
{% multi_lang_include developer_guide/android/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab flutter %}
{% multi_lang_include developer_guide/flutter/push_notifications/troubleshooting.md %}
{% endsdktab %}

{% sdktab .NET MAUI (Xamarin) %}
## Solución de problemas

### Push no aparece después de cerrar la aplicación desde el selector de tareas {#push-doesnt-appear-after-app-is-closed-from-task-switcher}

Si observas que las notificaciones push ya no aparecen después de cerrar la aplicación desde el selector de tareas, es probable que tu aplicación esté en modo Debug. .NET MAUI añade andamiaje en modo Debug que impide que las aplicaciones reciban push después de que su proceso sea finalizado. Si ejecutas tu aplicación en modo Release, deberías ver push incluso después de cerrar la aplicación desde el selector de tareas.

### La fábrica de notificaciones personalizada no se configura correctamente {#custom-notification-factory-not-being-set-correctly}

Las fábricas de notificaciones personalizadas (y todos los delegados) deben extender [`Java.Lang.Object`](https://developer.xamarin.com/api/type/Android.Runtime.IJavaObject/) para funcionar correctamente a través de la división entre C# y Java. Consulta [Xamarin](https://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/working_with_jni/#Implementing_Interfaces) sobre la implementación de interfaces Java para más información.

{% endsdktab %}
{% endsdktabs %}

## Saltos de línea en las notificaciones push {#push-linebreaks}

Al redactar notificaciones push con etiquetas de Liquid, los saltos de línea adyacentes a las etiquetas de Liquid se eliminan automáticamente antes de que se envíe el mensaje. En el [creador de notificaciones push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message), estos saltos de línea se vuelven a añadir para que tu mensaje siga siendo legible mientras lo editas. Si notas saltos de línea alrededor de las etiquetas de Liquid al guardar tu mensaje, se trata de un comportamiento esperado.