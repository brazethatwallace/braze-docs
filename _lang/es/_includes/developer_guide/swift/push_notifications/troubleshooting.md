## Comprender el flujo de trabajo de Braze y APN {#understanding-the-brazeapns-workflow}

El servicio de notificaciones push de Apple (APN) es la infraestructura para enviar notificaciones push a aplicaciones que se ejecutan en las plataformas de Apple. Aquí se muestra la estructura simplificada de cómo se habilitan las notificaciones push para los dispositivos de tus usuarios y cómo Braze puede enviarles notificaciones push:

1. Configuras el certificado push y el perfil de aprovisionamiento
2. Los dispositivos se registran en APN y proporcionan a Braze los tokens de notificaciones push
3. Lanzas una Campaign push de Braze
4. Braze elimina los tokens no válidos

### Paso 1: Configurar el certificado push y el perfil de aprovisionamiento {#step-1-configuring-the-push-certificate-and-provisioning-profile}

Al desarrollar tu aplicación, necesitarás crear un certificado SSL para habilitar las notificaciones push. Este certificado se incluirá en el perfil de aprovisionamiento con el que se compila tu aplicación y también deberá cargarse en el panel de Braze. El certificado permite a Braze indicar a APN que estamos autorizados a enviar notificaciones push en tu nombre.

Existen dos tipos de [perfiles de aprovisionamiento](https://developer.apple.com/library/content/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html) y certificados: desarrollo y distribución. Recomendamos usar solo perfiles y certificados de distribución para evitar cualquier confusión. Si decides usar perfiles y certificados diferentes para desarrollo y distribución, asegúrate de que el certificado cargado en el panel coincida con el perfil de aprovisionamiento que estés utilizando actualmente.

{% alert warning %}
No cambies el entorno del certificado push (desarrollo frente a producción). Cambiar el certificado push al entorno equivocado puede provocar que el token de notificaciones push de tus usuarios se elimine accidentalmente, haciéndolos inaccesibles mediante push.
{% endalert %}

### Paso 2: Los dispositivos se registran en APN y proporcionan a Braze los tokens de notificaciones push {#step-2-devices-register-for-apns-and-provide-braze-with-push-tokens}

Cuando los usuarios abren tu aplicación, se les solicita aceptar las notificaciones push. Si aceptan esta solicitud, APN generará un token de notificaciones push para ese dispositivo en particular. El SDK or kit de desarrollo de software de Swift enviará de forma inmediata y asíncrona el token de notificaciones push para las aplicaciones que utilicen la [política de vaciado automático]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/fine_network_traffic_control#automatic-request-processing) predeterminada. Una vez que tengamos un token de notificaciones push asociado a un usuario, este aparecerá como "Registrado para push" en el panel, en su perfil de usuario en la pestaña **Interacción**, y será elegible para recibir notificaciones push de Campaigns de Braze.

{% alert note %}
A partir de macOS 13, en ciertos dispositivos, puedes probar las notificaciones push en un simulador de iOS 16 ejecutándose en Xcode 14. Para más detalles, consulta las [notas de la versión de Xcode 14](https://developer.apple.com/documentation/xcode-release-notes/xcode-14-release-notes).
{% endalert %}

#### Consideraciones sobre la generación de tokens de notificaciones push {#considerations-for-push-token-generation}

- Si los usuarios instalan tu aplicación en otro dispositivo, se creará y capturará otro token de la misma manera.
- Si los usuarios reinstalan tu aplicación, se generará un nuevo token que se pasará a Braze. Sin embargo, es posible que el token original siga registrado como válido por APN y Braze.
- Si los usuarios desinstalan tu aplicación, Braze no recibe una notificación inmediata de esto y el token seguirá apareciendo como válido hasta que APN lo retire.
- En algún momento, APN retirará los tokens antiguos. Braze no tiene control ni visibilidad sobre esto.

### Paso 3: Lanzar una Campaign push de Braze {#step-3-launching-a-braze-push-campaign}

Cuando se lanza una Campaign push, Braze realizará solicitudes a APN para entregar tu mensaje. Específicamente, las solicitudes se pasan a APN para cada token de notificaciones push válido actual, a menos que se seleccione **Enviar al dispositivo más reciente del usuario**. Después de que Braze reciba una respuesta exitosa de APN, registraremos una entrega exitosa en el perfil del usuario, aunque es posible que el usuario no haya recibido el mensaje real por razones que incluyen:
- Su dispositivo está apagado.
- Su dispositivo no está conectado a internet (Wi-Fi o datos celulares).
- Recientemente desinstalaron la aplicación.

Braze utilizará el certificado push SSL cargado en el panel para autenticar y verificar que estamos autorizados a enviar notificaciones push a los tokens de notificaciones push proporcionados. Si un dispositivo está en línea, la notificación debería recibirse poco después de que se haya enviado la Campaign. Ten en cuenta que Braze establece la [fecha de expiración](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns#2947607) predeterminada de APN para las notificaciones en 30 días.

### Paso 4: Eliminar los tokens no válidos {#step-4-removing-invalid-tokens}

Si [APN](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1) nos informa de que alguno de los tokens de notificaciones push a los que intentábamos enviar un mensaje no es válido, eliminamos esos tokens de los perfiles de usuario a los que estaban asociados.

{% alert note %}
Es normal que APN devuelva inicialmente un estado de éxito incluso si un token deja de estar registrado, ya que APN no informa de inmediato sobre los eventos de invalidación de tokens. APN retrasa intencionadamente la devolución de un estado `410` para tokens no válidos según un calendario aleatorio, diseñado para proteger la privacidad del usuario y evitar el rastreo de desinstalaciones de aplicaciones. Puedes seguir enviando notificaciones de forma segura a un token no registrado hasta que APN devuelva un estado `410`.
{% endalert %}

## Uso de los registros de errores push {#using-the-push-error-logs}

El [registro de actividad de mensajes]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) te da la oportunidad de ver cualquier mensaje (especialmente mensajes de error) asociado a tus Campaigns y envíos, incluidos los errores de notificaciones push. Este registro de errores proporciona una variedad de advertencias que pueden ser muy útiles para identificar por qué tus Campaigns no funcionan como se esperaba. Al hacer clic en un mensaje de error, se te redirigirá a la documentación relevante para ayudarte a solucionar un incidente en particular.

![Registros de errores push que muestran la hora en que ocurrió el error, el nombre de la aplicación, el canal, el tipo de error y el mensaje de error.]({% image_buster /assets/img_archive/message_activity_log.png %})

Los errores comunes que puedes ver aquí incluyen notificaciones específicas del usuario, como ["Received Unregistered Sending to Push Token"](#swift_received-unregistered-sending).

Además, Braze también proporciona un registro de cambios push en el perfil de usuario, en la pestaña **Engagement**. Este registro de cambios ofrece información sobre el comportamiento del registro push, como la invalidación de tokens, errores de registro push, tokens que se mueven a nuevos usuarios, etc.

![Pestaña Engagement del perfil de usuario de Braze que muestra el registro de cambios del registro push.]({% image_buster /assets/img_archive/push_changelog.gif %}){: style="max-width:50%;" }

### Errores del registro de actividad de mensajes {#message-activity-log-errors}

#### Received unregistered sending to push token {#received-unregistered-sending}

- Asegúrate de que el token de notificaciones push que se envía a Braze desde el método `AppDelegate.braze?.notifications.register(deviceToken:)` sea válido. Puedes consultar el **registro de actividad de mensajes** para ver el token de notificaciones push. Debería tener un aspecto similar a `6e407a9be8d07f0cdeb9e724733a89445f57a89ec890d63867c482a483506fa6`, una cadena larga que contiene una combinación de letras y números. Si tu token de notificaciones push tiene un aspecto diferente, revisa tu [código]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-4-register-push-tokens-with-braze) para el envío de tokens de notificaciones push a Braze.
- Asegúrate de que tu perfil de aprovisionamiento push coincida con el entorno en el que estás haciendo pruebas. Los certificados universales pueden configurarse en el panel de Braze para enviar al entorno de APN de desarrollo o de producción. Usar un certificado de desarrollo para una aplicación de producción o un certificado de producción para una aplicación de desarrollo no funcionará.
 - Comprueba que el token de notificaciones push que has cargado en Braze coincida con el perfil de aprovisionamiento que usaste para compilar la aplicación desde la que enviaste el token de notificaciones push.

#### Device token not for topic

APN devuelve `DeviceTokenNotForTopic` (estado HTTP 400) cuando el token de notificaciones push no coincide con el tema (ID del paquete) configurado para tus credenciales. Braze puede mostrar esto en el **registro de actividad de mensajes** o en los registros de entrega push como `DeviceTokenNotForTopic`.

Para resolver la discrepancia:

1. Confirma que el **ID del paquete** de la aplicación coincida con el **App Bundle ID** en Braze (**Configuración** > **Configuración de la aplicación** > **Configuración de notificaciones push**).
2. Verifica que el perfil de aprovisionamiento utilizado para compilar la aplicación incluya la capacidad push para ese ID del paquete.
3. Confirma que la credencial push cargada en Braze coincida con el entorno de la aplicación (desarrollo frente a producción).
4. Para claves `.p8`, verifica que el **Team ID** y el **Key ID** en Braze coincidan con tu cuenta de Apple Developer.
5. Vuelve a cargar una clave `.p8` válida o un certificado `.p12` si las credenciales fueron rotadas o revocadas.

Prefiere las claves de autenticación `.p8` cuando sea posible. Para los tipos de credenciales e indicadores de estado del panel, consulta [Migrar a una clave de autenticación .p8]({{site.baseurl}}/user_guide/channels/push/troubleshooting#migrate-to-a-p8-authentication-key).

#### BadDeviceToken sending to push token

`BadDeviceToken` es un código de error de APN y no se origina en Braze. Puede haber varias razones por las que se devuelve esta respuesta, entre ellas las siguientes:

- La aplicación recibió un token de notificaciones push que no era válido para las credenciales cargadas en el panel.
- Push estaba deshabilitado para este espacio de trabajo.
- El usuario optó por no recibir push.
- La aplicación fue desinstalada.
- Apple actualizó el token de notificaciones push, lo que invalidó el token anterior.
- La aplicación fue compilada para un entorno de producción, pero las credenciales push cargadas en Braze están configuradas para un entorno de desarrollo (o viceversa).

## Problemas de registro de push {#push-registration-issues}

### No aparece la solicitud de registro de push {#no-push-registration-prompt}

Si la aplicación no te solicita registrarte para notificaciones push, es probable que haya un problema con tu integración de registro de push. Asegúrate de haber seguido nuestra [documentación]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) e integrado correctamente nuestro registro de push. También puedes establecer puntos de interrupción en tu código para asegurarte de que el código de registro de push se esté ejecutando.

### No aparecen usuarios "registrados para push" en el panel (antes de enviar mensajes) {#no-push-registered-users-showing-in-the-dashboard-prior-to-sending-messages}

Asegúrate de que tu aplicación esté correctamente configurada para permitir notificaciones push. Los puntos de fallo comunes que debes verificar incluyen:

- Comprueba que tu aplicación te está solicitando permitir las notificaciones push. Normalmente, esta solicitud aparecerá la primera vez que abras la aplicación, pero puede programarse para que aparezca en otro lugar. Si no aparece donde debería, es probable que el problema esté en la configuración básica de las capacidades push de tu aplicación.
  - Verifica que los pasos para la [integración de push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) se hayan completado correctamente.
  - Comprueba que el perfil de aprovisionamiento con el que se compiló tu aplicación incluya permisos para push. Asegúrate de descargar todos los perfiles de aprovisionamiento disponibles de tu cuenta de desarrollador de Apple. Para confirmarlo, realiza los siguientes pasos:
    1. En Xcode, ve a **Preferences > Accounts** (o usa el atajo de teclado <kbd>Command</kbd>+<kbd>,</kbd>).
    2. Selecciona el Apple ID que usas para tu cuenta de desarrollador y haz clic en **View Details**.
    3. En la página siguiente, haz clic en **<i class="fas fa-redo-alt"></i> Refresh** y confirma que estás descargando todos los perfiles de aprovisionamiento disponibles.
- Comprueba que hayas [habilitado correctamente la capacidad push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-2-enable-push-capabilities) en tu aplicación.
- Comprueba que tu perfil de aprovisionamiento push coincida con el entorno en el que estás realizando pruebas. Los certificados universales pueden configurarse en el panel de Braze para enviar al entorno de APN de desarrollo o de producción. Usar un certificado de desarrollo para una aplicación de producción o un certificado de producción para una aplicación de desarrollo no funcionará.
- Comprueba que estés llamando a nuestro método `registerPushToken` estableciendo un punto de interrupción en tu código.
- Asegúrate de estar realizando pruebas con un dispositivo (push no funcionará en un simulador) y de tener buena conectividad de red.

## Notificaciones push enviadas pero no mostradas en los dispositivos de los usuarios {#push-notifications-sent-but-not-displayed-on-users-devices}

### Los usuarios "registrados para push" ya no están habilitados después de enviar mensajes {#push-registered-users-no-longer-enabled-after-sending-messages}

Es probable que esto indique que el usuario tenía un token de notificaciones push no válido. Esto puede ocurrir por varias razones:

#### Discrepancia entre el certificado del panel y la aplicación {#dashboard-and-app-certificate-mismatch}

Si el certificado push que subiste en el panel no es el mismo que está en el perfil de aprovisionamiento con el que se creó tu aplicación, APN rechazará el token. Verifica que hayas subido el certificado correcto y completado otra sesión en la aplicación antes de intentar otra notificación de prueba.

#### La aplicación fue desinstalada {#application-was-uninstalled}

Si un usuario ha desinstalado tu aplicación, su token de notificaciones push no será válido y se eliminará en el siguiente envío.

#### Regeneración del perfil de aprovisionamiento {#regenerating-your-provisioning-profile}

Como último recurso, empezar de nuevo y crear un perfil de aprovisionamiento completamente nuevo puede resolver los errores de configuración que surgen al trabajar con múltiples entornos, perfiles y aplicaciones al mismo tiempo. Hay muchas "piezas en movimiento" en la configuración de las notificaciones push, así que a veces es mejor volver a intentarlo desde el principio. Esto también te ayudará a aislar el problema si necesitas continuar con la solución de problemas.

### Los mensajes no se entregan a los usuarios "registrados para push" {#messages-not-delivered-to-push-registered-users}

#### La aplicación está en primer plano {#app-is-foregrounded}

En las versiones de iOS que no integran push a través del framework `UserNotifications`, si la aplicación está en primer plano cuando se recibe el mensaje push, no se mostrará. Deberías poner la aplicación en segundo plano en tus dispositivos de prueba antes de enviar mensajes de prueba.

#### Notificación de prueba programada incorrectamente {#test-notification-scheduled-incorrectly}

Revisa la programación que configuraste para tu mensaje de prueba. Si está configurada para entrega en zona horaria local o [sincronización inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing), es posible que simplemente aún no hayas recibido el mensaje (o que la aplicación estuviera en primer plano cuando se recibió).

### El usuario no está "registrado para push" en la aplicación que se está probando {#user-not-push-registered-for-the-app-being-tested}

Revisa el perfil de usuario de la persona a la que intentas enviar un mensaje de prueba. En la pestaña **Engagement**, debería haber una lista de "aplicaciones con push habilitado". Verifica que la aplicación a la que intentas enviar mensajes de prueba esté en esta lista. Los usuarios aparecerán como "Push Registered" si tienen un token de notificaciones push para cualquier aplicación en tu espacio de trabajo, por lo que esto podría ser un falso positivo.

Lo siguiente indicaría un problema con el registro de push o que el token del usuario fue devuelto a Braze como no válido por APN después de haber sido enviado:

![Un perfil de usuario que muestra la configuración de contacto de un usuario. En Push, se muestra "No Apps".]({% image_buster /assets/img_archive/registration_problem.png %}){: style="max-width:50%"}

## Los clics push no se registran {#push-clicks-not-logged}

- Asegúrate de haber seguido los [pasos de la integración push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-5-enable-push-handling).
- Braze no gestiona las notificaciones push recibidas silenciosamente en primer plano (comportamiento push predeterminado en primer plano antes del framework `UserNotifications`). Esto significa que los enlaces no se abrirán y los clics push no se registrarán. Si tu aplicación aún no ha integrado el framework `UserNotifications`, Braze no gestionará las notificaciones push cuando el estado de la aplicación sea `UIApplicationStateActive`. Asegúrate de que tu aplicación no retrasa las llamadas a los [métodos de gestión push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-5-enable-push-handling); de lo contrario, el SDK or kit de desarrollo de software de Swift puede tratar las notificaciones push como eventos push silenciosos en primer plano y no gestionarlos.

## Los vínculos profundos no funcionan {#deep-links-not-working}

Para una solución de problemas completa en todos los canales, incluidos los enlaces universales, los esquemas personalizados, el correo electrónico y proveedores externos como Branch, consulta [Solución de problemas de vinculación en profundidad]({{site.baseurl}}/developer_guide/push_notifications/deep_linking_troubleshooting).

### Los enlaces web de los clics push no se abren {#web-links-from-push-clicks-not-opening}

Los enlaces en las notificaciones push deben cumplir con ATS para poder abrirse en vistas web. Asegúrate de que tus enlaces web utilicen HTTPS. Para más información, consulta [Cumplimiento de ATS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking#app-transport-security-ats).

### Los vínculos profundos de los clics push no se abren {#deep-links-from-push-clicks-not-opening}

La mayor parte del código que gestiona los vínculos profundos también gestiona las aperturas push. Primero, asegúrate de que las aperturas push se estén registrando. Si no es así, corrige ese problema (ya que la solución suele corregir también la gestión de enlaces).

Si las aperturas se están registrando, verifica si se trata de un problema con el vínculo profundo en general o con la gestión de clics push de vinculación en profundidad. Para ello, prueba si un vínculo profundo desde el clic de un mensaje dentro de la aplicación funciona.