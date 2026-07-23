---
nav_title: Solución de problemas
article_title: Solución de problemas de notificaciones push para iOS
platform: iOS
page_order: 30
description: "Este artículo de referencia cubre posibles temas de solución de problemas para tu implementación de push en iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Solución de problemas {#push-troubleshooting}

## Comprender el flujo de trabajo de Braze/APN {#understanding-the-brazeapns-workflow}

El servicio de notificaciones push de Apple (APN) es la infraestructura de Apple para el envío de notificaciones push a aplicaciones de iOS y OS X. A continuación se muestra la estructura simplificada de cómo se habilitan las notificaciones push para los dispositivos de tus usuarios y cómo Braze puede enviarles notificaciones push:

{% multi_lang_include developer_guide/push_notifications/push_registration_flow_steps.md %}

### Paso 1: Configurar el certificado push y el perfil de aprovisionamiento {#step-1-configuring-the-push-certificate-and-provisioning-profile}

Cuando desarrolles tu aplicación, crea un certificado SSL para habilitar las notificaciones push. Este certificado se incluye en el perfil de aprovisionamiento con el que se compila tu aplicación y también debe cargarse en el panel de Braze. El certificado permite a Braze indicar a APN que estamos autorizados a enviar notificaciones push en tu nombre.

Existen dos tipos de [perfiles de aprovisionamiento](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) y certificados: desarrollo y distribución. Recomendamos utilizar únicamente perfiles y certificados de distribución para evitar confusiones. Si decides utilizar perfiles y certificados diferentes para desarrollo y distribución, asegúrate de que el certificado cargado en el panel coincida con el perfil de aprovisionamiento que estás utilizando actualmente.

{% alert warning %}
No cambies el entorno del certificado push (desarrollo frente a producción). Cambiar el certificado push al entorno incorrecto puede provocar que los tokens de push de tus usuarios se eliminen accidentalmente, haciéndolos inaccesibles por push.
{% endalert %}

#### Paso 2: Los dispositivos se registran en APN y proporcionan a Braze los tokens de push {#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens}

Cuando los usuarios abran tu aplicación, se les pedirá que acepten las notificaciones push. Si aceptan esta solicitud, APN generará un token de push para ese dispositivo en particular. El SDK de iOS enviará de forma inmediata y asíncrona el token de push para las aplicaciones que utilicen la [política de vaciado automático]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/fine_network_traffic_control#automatic-request-processing) predeterminada. Una vez que tengamos un token de push asociado a un usuario, aparecerá como "Push Registered" en el panel, en su perfil de usuario, en la pestaña **Interacción**, y será elegible para recibir notificaciones push de Campaigns de Braze.

{% alert note %}
A partir de Xcode 14, puedes probar notificaciones push remotas en un simulador de iOS.
{% endalert %}

#### Paso 3: Lanzar una Campaign push de Braze {#step-3-launching-a-braze-push-campaign}

Cuando se lanza una Campaign push, Braze realizará solicitudes a APN para entregar tu mensaje. Braze utilizará el certificado SSL push cargado en el panel para autenticarse y verificar que estamos autorizados a enviar notificaciones push a los tokens de push proporcionados. Si un dispositivo está en línea, la notificación debería recibirse poco después de que se haya enviado la Campaign. Ten en cuenta que Braze establece la [fecha de expiración](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) predeterminada de APN para las notificaciones en 30 días.

#### Paso 4: Eliminar tokens no válidos {#step-4-removing-invalid-tokens}

Si [APN](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) nos informa de que alguno de los tokens de push a los que intentábamos enviar un mensaje no es válido, eliminamos esos tokens de los perfiles de usuario con los que estaban asociados.

## Uso de los registros de errores de push {#utilizing-the-push-error-logs}

Braze proporciona un registro de errores de notificaciones push dentro del **Registro de actividad de mensajes**. Este registro de errores ofrece una variedad de advertencias que pueden ser muy útiles para identificar por qué tus Campaigns no están funcionando como se espera. Al seleccionar un mensaje de error, se te redirige a la documentación relevante para ayudarte a solucionar un incidente en particular.

![Registros de errores de push que muestran la hora en que ocurrió el error, el nombre de la aplicación, el canal, el tipo de error y el mensaje de error.]({% image_buster /assets/img_archive/message_activity_log.png %})

Los errores comunes que podrías ver aquí incluyen notificaciones específicas del usuario, como ["Received Unregistered Sending to Push Token"](#received-unregistered-sending).

Además, Braze también proporciona un registro de cambios de push en el perfil de usuario, en la pestaña **Interacción**. Este registro de cambios ofrece información sobre el comportamiento del registro push, como la invalidación de tokens, errores de registro push, tokens que se transfieren a nuevos usuarios, etc.

![Ejemplo animado de tarjeta de contenido.]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

## Problemas con el registro push {#push-registration-issues}

Para añadir verificación a la lógica de registro push de tu aplicación, implementa [pruebas unitarias de push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests).

### Sin solicitud de registro push {#no-push-registration-prompt}

Si la aplicación no te solicita registrarte para notificaciones push, es probable que haya un problema con la integración del registro push. Asegúrate de haber seguido nuestra [documentación]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) e integrado correctamente nuestro registro push. También puedes establecer puntos de interrupción en tu código para asegurarte de que el código de registro push se está ejecutando.

#### No aparecen usuarios "registrados para push" en el panel {#no-push-registered-users-showing-in-the-dashboard}

- Comprueba que tu aplicación te solicita permitir las notificaciones push. Normalmente, esta solicitud aparecerá la primera vez que abras la aplicación, pero puede programarse para que aparezca en otro lugar. Si no aparece donde debería, es probable que el problema esté en la configuración básica de las capacidades push de tu aplicación.
  - Verifica que los pasos de la [integración push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) se completaron correctamente.
  - Comprueba que el perfil de aprovisionamiento con el que se compiló tu aplicación incluye permisos para push. Asegúrate de que estás descargando todos los perfiles de aprovisionamiento disponibles de tu cuenta de desarrollador de Apple. Para confirmarlo, sigue estos pasos:
    1. En Xcode, ve a **Preferences > Accounts** (o usa el atajo de teclado <kbd>Command</kbd>+<kbd>,</kbd>).
    2. Selecciona el Apple ID que usas para tu cuenta de desarrollador y haz clic en **View Details**.
    3. En la siguiente página, haz clic en **<i class="fas fa-redo-alt"></i> Refresh** y confirma que estás descargando todos los perfiles de aprovisionamiento disponibles.
- Comprueba que has [habilitado correctamente la capacidad push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-2-enable-push-capabilities) en tu aplicación.
- Comprueba que tu perfil de aprovisionamiento push coincide con el entorno en el que estás probando. Los certificados universales pueden configurarse en el panel de Braze para enviar al entorno de APN de desarrollo o de producción. Usar un certificado de desarrollo para una aplicación de producción o un certificado de producción para una aplicación de desarrollo no funcionará.
- Comprueba que estás llamando a nuestro método `registerPushToken` estableciendo un punto de interrupción en tu código.
- Comprueba que estás en un dispositivo (push no funcionará en un simulador) y que tienes buena conectividad de red.

## Dispositivos que no reciben notificaciones push {#devices-not-receiving-push-notifications}

### Los usuarios ya no están "registrados para push" después de enviar una notificación push {#users-no-longer-push-registered-after-sending-a-push-notification}

Esto probablemente indica que el usuario tenía un token de push no válido. Esto puede ocurrir por varias razones:

#### Discrepancia entre el certificado del panel y la aplicación {#dashboard-and-app-certificate-mismatch}

Si el certificado push que subiste en el panel no es el mismo que el del perfil de aprovisionamiento con el que se compiló tu aplicación, APN rechazará el token. Verifica que hayas subido el certificado correcto y completado otra sesión en la aplicación antes de intentar otra notificación de prueba.

##### Desinstalaciones {#uninstalls}

Si un usuario ha desinstalado tu aplicación, su token de push será no válido y se eliminará en el siguiente envío.

##### Regenerar tu perfil de aprovisionamiento {#regenerating-your-provisioning-profile}

Como último recurso, empezar de cero y crear un perfil de aprovisionamiento completamente nuevo puede resolver errores de configuración que surgen al trabajar con múltiples entornos, perfiles y aplicaciones al mismo tiempo. Hay muchas "piezas en movimiento" al configurar las notificaciones push para aplicaciones iOS, por lo que a veces es mejor volver a intentarlo desde el principio. Esto también te ayudará a aislar el problema si necesitas continuar con la solución de problemas.

#### Los usuarios siguen "registrados para push" después de enviar una notificación push {#users-still-push-registered-after-sending-a-push-notification}

##### La aplicación está en primer plano {#app-is-foregrounded}

En las versiones de iOS que no integran push a través del framework `UserNotifications`, si la aplicación está en primer plano cuando se recibe el mensaje push, no se mostrará. Debes poner la aplicación en segundo plano en tus dispositivos de prueba antes de enviar mensajes de prueba.

##### Notificación de prueba programada incorrectamente {#test-notification-scheduled-incorrectly}

Comprueba la programación que estableciste para tu mensaje de prueba. Si está configurada para entrega en zona horaria local o [sincronización inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing), es posible que simplemente aún no hayas recibido el mensaje (o que la aplicación estuviera en primer plano cuando se recibió).

#### El usuario no está "registrado para push" en la aplicación que se está probando {#user-not-push-registered-for-the-app-being-tested}

Comprueba el perfil de usuario de la persona a la que intentas enviar un mensaje de prueba. En la pestaña **Interacción**, debería haber una lista de "aplicaciones con push habilitado". Verifica que la aplicación a la que intentas enviar mensajes de prueba esté en esta lista. Los usuarios aparecerán como "Push Registered" si tienen un token de push para cualquier aplicación en tu espacio de trabajo, por lo que esto podría ser un falso positivo.

Lo siguiente indicaría un problema con el registro de push o que el token del usuario fue devuelto a Braze como no válido por APN después de haber sido enviado:

![Un perfil de usuario que muestra la configuración de contacto de un usuario. Aquí puedes ver para qué aplicaciones está registrado el push.]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## Los mensajes push no se envían {#push-messages-not-sending}

Para solucionar problemas con las notificaciones push que no se envían, consulta [Solución de problemas de push]({{site.baseurl}}/user_guide/channels/push/troubleshooting).

## Errores del registro de actividad de mensajes {#message-activity-log-errors}

### Recibido no registrado enviando al token de push {#received-unregistered-sending}

- Asegúrate de que el token de push que se envía a Braze desde el método `[[Appboy sharedInstance] registerPushToken:]` sea válido. Puedes consultar el **Registro de actividad de mensajes** para ver el token de push. Debería tener un aspecto similar a `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, una cadena larga que contiene una mezcla de letras y números. Si tu token de push tiene un aspecto diferente, revisa tu [código]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-4-register-push-tokens-with-braze) para el envío de tokens de push a Braze.
- Asegúrate de que tu perfil de aprovisionamiento push coincida con el entorno en el que estás realizando pruebas. Los certificados universales pueden configurarse en el panel de Braze para enviar al entorno de APN de desarrollo o de producción. Usar un certificado de desarrollo para una aplicación de producción o un certificado de producción para una aplicación de desarrollo no funcionará.
 - Comprueba que el token de push que has subido a Braze coincida con el perfil de aprovisionamiento que usaste para compilar la aplicación desde la que enviaste el token de push.

#### El token del dispositivo no corresponde al tema {#device-token-not-for-topic}

Este error indica que el certificado push de tu aplicación y el ID del paquete no coinciden. Comprueba que el certificado push que subiste a Braze coincida con el perfil de aprovisionamiento utilizado para compilar la aplicación desde la que se envió el token de push.

#### BadDeviceToken al enviar al token de push {#baddevicetoken-sending-to-push-token}

`BadDeviceToken` es un código de error de APN y no se origina en Braze. Puede haber varias razones por las que se devuelve esta respuesta, entre ellas las siguientes:

{% multi_lang_include developer_guide/push_notifications/invalid_push_token_reasons.md %}

## Problemas después de la entrega push {#issues-after-push-delivery}

Para añadir verificación del manejo de push en tu aplicación, implementa [pruebas unitarias de push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/unit_tests).

### Los clics en push no se registran {#push-clicks-not-logged}

- Si esto solo ocurre en iOS 10, asegúrate de haber seguido los pasos de integración push para [iOS 10]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-5-enable-push-handling).
- Braze no gestiona las notificaciones push recibidas silenciosamente en primer plano (por ejemplo, el comportamiento push en primer plano predeterminado antes del framework `UserNotifications`). Esto significa que los enlaces no se abrirán y los clics en push no se registrarán. Si tu aplicación aún no ha integrado el framework `UserNotifications`, Braze no gestionará las notificaciones push cuando el estado de la aplicación sea `UIApplicationStateActive`. Debes asegurarte de que tu aplicación no retrase las llamadas a nuestros [métodos de manejo de push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration#step-5-enable-push-handling); de lo contrario, el SDK de iOS puede tratar las notificaciones push como eventos push silenciosos en primer plano y no gestionarlas.

#### Los enlaces web de los clics en push no se abren {#web-links-from-push-clicks-not-opening}

iOS 9+ requiere que los enlaces cumplan con ATS para abrirse en vistas web. Asegúrate de que tus enlaces web usen HTTPS. Consulta nuestro artículo sobre [cumplimiento de ATS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking#app-transport-security-ats) para más información.

#### Los vínculos profundos de los clics en push no se abren {#deep-links-from-push-clicks-not-opening}

La mayor parte del código que gestiona los vínculos profundos también gestiona las aperturas de push. Primero, asegúrate de que las aperturas de push se estén registrando. Si no es así, [soluciona ese problema](#push-clicks-not-logged) (ya que la solución a menudo también corrige el manejo de enlaces).

Si las aperturas se están registrando, comprueba si el problema es con el vínculo profundo en general o con el manejo de clics en push con vinculación en profundidad. Para ello, prueba si un vínculo profundo desde un clic en un mensaje dentro de la aplicación funciona.

#### Pocas o ninguna apertura directa {#few-or-no-direct-opens}

Si al menos un usuario abre tu notificación push de iOS, pero se registran pocas o ninguna _Direct Opens_ en Braze, puede haber un problema con tu [integración de SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview). Ten en cuenta que las _Direct Opens_ no se registran para envíos de prueba ni para notificaciones push silenciosas.

- Asegúrate de que los mensajes no se estén enviando como [notificaciones push silenciosas]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications#sending-silent-push-notifications). El mensaje debe tener texto en el título o en el cuerpo para no considerarse silencioso.
- Vuelve a comprobar los siguientes pasos de la [guía de integración push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration):
   - [Registrarse para push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-1-register-for-push-notifications-with-apns): En cada inicio de la aplicación, preferiblemente dentro de `application:didFinishLaunchingWithOptions:`, el código del paso 3 debe ejecutarse. La propiedad delegate de `UNUserNotificationCenter.current()` debe asignarse a un objeto que implemente `UNUserNotificationCenterDelegate` y contenga el método `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:`.
   - [Habilitar el manejo de push]({{site.baseurl}}/developer_guide/platform_integration_guides/legacy_sdks/ios/push_notifications/integration#step-5-enable-push-handling): Verifica que el método `(void)userNotificationCenter:didReceiveNotificationResponse:withCompletionHandler:` se haya implementado.