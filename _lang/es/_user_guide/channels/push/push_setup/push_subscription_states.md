---
nav_title: "Estados de suscripción push"
article_title: "Estados de suscripción push"
page_order: 2
page_type: reference
description: "Este artículo de referencia cubre los conceptos de habilitación push y estados de suscripción push en Braze, incluyendo las diferencias fundamentales de comportamiento entre iOS, Android y web."
channel:
  - push

---

# Habilitación push y suscripción push {#push-enablement-and-push-subscription}

> Este artículo de referencia cubre los conceptos de habilitación push y estados de suscripción push en Braze, incluyendo las diferencias fundamentales de comportamiento entre iOS, Android y Web.

{% multi_lang_include push/subscription_states.md %}

## Dónde aparecen el registro push y el estado {#where-push-registration-and-status-appear}

Puedes revisar el estado de suscripción push, el registro y la habilitación en tres lugares principales en Braze:

1. **[Perfiles de usuario](#user-profiles-and-push-changelog)** en la pestaña **Engagement**
2. **[Segmentación](#segmentation-and-push-filters)** en el constructor de segmentos
3. **[Análisis de Campaign y Canvas](#campaign-and-canvas-analytics)** en la página de análisis de cada mensaje

### Perfiles de usuario y registro de cambios push {#user-profiles-and-push-changelog}

En el perfil de un usuario ([**Buscar usuarios**]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles) > selecciona el usuario > pestaña **Engagement**), **Contact Settings** muestra el estado de suscripción push, **Push Registered For** (qué aplicaciones y plataformas puede usar Braze para enviar push en primer plano a ese perfil) y el **Push Changelog** para movimientos de tokens, errores y actualizaciones de registro. Para saber cómo leer **Push Registered For** y la autorización en primer plano frente a segundo plano, consulta [Verificar el estado de registro push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle#checking-push-registration-status).

En iOS y Android, cuando un dispositivo pasa de autorización push en primer plano a solo segundo plano (por ejemplo, después de que el usuario desactiva las notificaciones en la configuración del sistema y el SDK reporta el cambio), el registro de cambios push puede incluir una entrada como "Push token was updated from foreground push enabled to foreground push disabled".

Después de que esperes nuevos datos del SDK (por ejemplo, justo después de una sesión de prueba), selecciona **Refresh** en el perfil del usuario si los valores parecen desactualizados. Puede haber un breve retraso entre el envío de datos del SDK y la actualización del perfil con el último registro push.

Para los usuarios que agregues a un [grupo interno]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups), selecciona **Record User Events for group members** en la **Internal Group Settings** de ese grupo para que las solicitudes del SDK aparezcan en el registro. Luego abre el [Registro de eventos de usuario]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log) en **Settings** > **Event User Log**, busca las solicitudes del SDK del usuario y expande la carga útil sin procesar. Puedes inspeccionar campos como `remote_notification_enabled` mientras validas si el dispositivo reporta las notificaciones remotas como habilitadas o deshabilitadas.

### Segmentación y filtros push {#segmentation-and-push-filters}

En el constructor de segmentos, usa filtros como **`Foreground Push Enabled`**, **`Foreground Push Enabled for App`**, **`Background or Foreground Push Enabled`** y filtros de suscripción push para segmentar o auditar usuarios por preferencia y autorización a nivel de dispositivo. En iOS, cómo leen esos filtros para un usuario dado depende de si completó el aviso del sistema operativo, cambió la configuración o usa [autorización provisional](#provisional-push); consulta [Acciones del usuario en iOS y estado push](#ios-user-actions-push-status) y [Otros escenarios específicos de plataforma](#foreground-push-enabled).

### Análisis de Campaign y Canvas {#campaign-and-canvas-analytics}

En la página de análisis de una **Campaign** o **Canvas** push, métricas como *Enviados*, *Rebotes* y *Aperturas* reflejan la entrega y la participación de ese envío. Para vincular esos números con perfiles individuales, exporta los destinatarios desde **Campaign Details** o **Canvas Details** usando **User Data** (CSV). Para los pasos y permisos, consulta [Exportar datos de Campaign]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_campaign_results_data) y [Exportar datos de Canvas]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_canvas_data). Si los recuentos entre los análisis y una exportación no coinciden, consulta [Análisis de Campaign y Canvas]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/export_troubleshooting#campaign-and-canvas-analytics) en la solución de problemas de exportación.

## Acciones del usuario en iOS y estado push {#ios-user-actions-push-status}

La siguiente tabla muestra cómo las diferentes acciones del usuario afectan la habilitación push en iOS, el registro push en primer plano o segundo plano, y el estado de suscripción push en Braze. Cuando un usuario instala tu aplicación e inicia su primera sesión, su estado es generalmente el que se muestra en la primera fila. Cada acción posterior puede actualizar algunos de estos valores, pero no otros.

| Acción del usuario | `Foreground Push Enabled` | `Foreground Push Enabled for App` | Tipo de registro push | Estado de suscripción push |
| --- | --- | --- | --- | --- |
| El usuario instala la aplicación y registra una sesión | `false`* | No actualizado | Segundo plano | `Subscribed` |
| El usuario recibe el aviso push nativo de iOS y selecciona **Allow** | `true` | `true` | Primer plano | `Opted-In`** |
| El usuario recibe el aviso push nativo de iOS y selecciona **Don't Allow** | `false` | No actualizado | Segundo plano | No actualizado |
| El usuario habilita push desde la configuración del dispositivo y registra una sesión | `true` | `true` | Primer plano | `Opted-In`** |
| El usuario deshabilita push desde la configuración del dispositivo y registra una sesión | `false` | `false` | Segundo plano | No actualizado |
| El usuario elimina la aplicación | No actualizado | Actualizado cuando se retira el token push | Actualizado cuando se retira el token push | No actualizado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 aria-label="Acciones del usuario en iOS y estado push" }

<sup>* Si la aplicación no utiliza push provisional, `Foreground Push Enabled` es `false` hasta que el usuario permita las notificaciones push. Si la aplicación utiliza push provisional, `Foreground Push Enabled` es `true` al inicio de la primera sesión. Para más información, consulta [Autorización provisional y push silencioso](#provisional-push).</sup>

<sup>** A partir de la [versión 7.5.0 de Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0), la propiedad de configuración `optInWhenPushAuthorized` controla si el estado de suscripción push se establece automáticamente en `Opted-In` cuando se autoriza el permiso push. Para más información, consulta [Tokens push](#push-tokens).</sup>

## Permiso push {#push-permission}

Todas las plataformas habilitadas para push (iOS, Web y Android) requieren adhesión voluntaria explícita a través de un aviso a nivel del sistema operativo, con algunas ligeras diferencias que se describen a continuación.

Dado que la decisión del usuario es definitiva y no puedes volver a preguntar después de que rechace, usar mensajes dentro de la aplicación de [push primer]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) es una estrategia importante para aumentar tus tasas de adhesión voluntaria.

**Avisos nativos de permiso push del sistema operativo**

| Plataforma | Captura de pantalla | Descripción |
|--|--|--|
| iOS | ![Un aviso push nativo de iOS que pregunta "My App would like to send you notifications" con dos botones, "Don't Allow" y "Allow" en la parte inferior del mensaje.]({% image_buster /assets/img/push_implementation_guide/ios-push-prompt.png %}){: style="max-width:410px;"} | Esto no aplica cuando se solicita permiso de [push provisional](#provisional-push). |
| Android | ![Un mensaje push de Android que pregunta "Allow Kitchenerie to send you notifications?" con dos botones, "Allow" y "Don't allow" en la parte inferior del mensaje.]({% image_buster /assets/img/push_implementation_guide/android-push-prompt.png %}){: style="max-width:410px;"} | Este permiso push se introdujo en Android 13. Antes de Android 13, no se requería permiso para enviar push. |
| Web | ![Un aviso push nativo del navegador web que pregunta "Braze.com wants to show notification" con dos botones, "Block" y "Allow" en la parte inferior del mensaje.]({% image_buster /assets/img/push_implementation_guide/web-push-prompt.png %}){: style="max-width:410px;"} | |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Permiso push" }

### Android

Antes de Android 13, no se necesitaba permiso para enviar notificaciones push. En Android 12 e inferior, todos los usuarios se consideran `Subscribed` en su primera sesión cuando Braze solicita automáticamente un token push. En ese momento, el usuario está **habilitado para push** con un token push válido para ese dispositivo y un estado de suscripción predeterminado de `Subscribed`.

A partir de [Android 13]({{site.baseurl}}/developer_guide/platforms/android/android_13), el permiso push debe solicitarse y ser otorgado por el usuario. Tu aplicación puede solicitar manualmente el permiso al usuario en momentos oportunos, pero si no lo hace, los usuarios recibirán el aviso automáticamente cuando tu aplicación cree un [canal de notificaciones](https://developer.android.com/reference/android/app/NotificationChannel).

### iOS

![Una notificación en el centro de notificaciones del sistema con un mensaje en la parte inferior que pregunta "Keep receiving notifications from the Yachtr app?" con dos botones debajo para "Keep" o "Turn Off"]({% image_buster /assets/img/push_implementation_guide/ios-provisional-push.png %}){: style="float:right;max-width:430px;width:40%;margin-left:15px;border:0"}

Tu aplicación puede solicitar push provisional o push autorizado.

El push autorizado requiere permiso explícito del usuario antes de enviar cualquier notificación, mientras que el [push provisional](https://www.braze.com/resources/articles/mastering-provisional-push) te permite enviar notificaciones __silenciosamente__, directamente al centro de notificaciones sin ningún sonido ni alerta.

#### Autorización provisional y push silencioso {#provisional-push}

Antes de iOS 12 (lanzado en 2018), todos los usuarios debían adherirse explícitamente para recibir notificaciones push.

En iOS 12, Apple introdujo la [autorización provisional](https://www.braze.com/resources/articles/mastering-provisional-push), que permite a las marcas enviar notificaciones push silenciosas al centro de notificaciones de sus usuarios antes de que se adhieran explícitamente, dándote la oportunidad de demostrar el valor de tus mensajes de forma temprana. Consulta [autorización provisional]({{site.baseurl}}/user_guide/channels/push/platform_specific_resources/ios/notification_options#provisional-push) para obtener más información.

### Web {#web}

Para Web, debes solicitar la adhesión voluntaria explícita del usuario a través del diálogo de permiso nativo del navegador.

A diferencia de iOS y Android, que permiten que tu aplicación muestre el aviso de permiso en cualquier momento, algunos navegadores modernos solo mostrarán el aviso si es desencadenado por un "gesto del usuario" (clic del ratón o pulsación de tecla). Si tu sitio intenta solicitar permiso de notificaciones push al cargar la página, probablemente será ignorado o silenciado por el navegador.

Como resultado, solo debes solicitar permiso cuando un usuario haga clic en algún lugar de tu sitio web y no de forma aleatoria cuando se carga una página.

## Tokens push {#push-tokens}

Los [tokens push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle) son un identificador anónimo único generado por el dispositivo del usuario y enviado a Braze para identificar dónde enviar la notificación de cada destinatario.

Hay dos formas en que un [token push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle) puede clasificarse, que son esenciales para entender cómo se puede enviar una notificación push a tus usuarios.

1. **Push en primer plano** proporciona la capacidad de enviar notificaciones push visibles regulares al primer plano del dispositivo del usuario.
2. **Push en segundo plano** está disponible independientemente de si un dispositivo en particular ha optado por recibir notificaciones push de esa marca. El push en segundo plano permite a las marcas enviar notificaciones push silenciosas (notificaciones que intencionalmente no se muestran) a los dispositivos para soportar funcionalidades clave como [Uninstall Tracking]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking).

Cuando un perfil de usuario tiene un token push de primer plano válido asociado con una aplicación, Braze considera al usuario como "registrado para push" en la aplicación dada. Braze, entonces, proporciona un filtro de segmentación específico, `Foreground Push Enabled for App,` para ayudar a identificar a estos usuarios.

{% alert note %}
El filtro `Foreground Push Enabled for App` solo considera la presencia de un token push de primer plano y segundo plano válido para la aplicación dada. Sin embargo, el filtro más genérico [`Foreground Push Enabled`](#foreground-push-enabled) segmenta a los usuarios que han activado explícitamente las notificaciones push para cualquier aplicación en tu espacio de trabajo. Este recuento incluye solo push en primer plano y no incluye a los usuarios que han cancelado su suscripción. Puedes obtener más información sobre estos y otros filtros en [Filtros de segmentación]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

Para un pequeño porcentaje de usuarios, los retrasos en el procesamiento pueden causar una discrepancia temporal: un usuario puede tener un token push de primer plano válido en su perfil pero aún no coincidir con el filtro `Foreground Push Enabled`. Su perfil puede mostrar brevemente que el push en primer plano no está habilitado aunque haya un token presente. Esto generalmente se resuelve una vez que el procesamiento se pone al día.
{% endalert %}

### Múltiples usuarios en un dispositivo {#multiple-users-on-one-device}

Los tokens push son específicos tanto del dispositivo como de la aplicación, por lo que no es posible usar tokens push para distinguir entre múltiples usuarios que usan el mismo dispositivo.

Por ejemplo, supongamos que tienes dos usuarios: Charlie y Kim. Si Charlie ha habilitado las notificaciones push para tu aplicación en su teléfono y Kim usa el teléfono de Charlie para cerrar la sesión del perfil de Charlie e iniciar sesión en el suyo, el token push se reasignará al perfil de Kim. El token push permanecerá asignado al perfil de Kim en ese dispositivo hasta que ella cierre sesión y Charlie vuelva a iniciar sesión.

Una aplicación o sitio web solo puede tener una suscripción push por dispositivo. Así que cuando un usuario cierra sesión en un dispositivo o sitio web, y un nuevo usuario inicia sesión, el token push se reasigna al nuevo usuario. Esto se refleja en el perfil del usuario, en la sección **Contact Settings** de la pestaña **Engagement**:

![Registro de cambios del token push en la pestaña Engagement del perfil de un usuario, que muestra cuándo se movió el token push a otro usuario y cuál era el token.]({% image_buster /assets/img/push_token_changelog.png %})

Dado que no hay forma de que los proveedores push (APNs/FCM) distingan entre múltiples usuarios en un dispositivo, pasamos el token push al último usuario que inició sesión para determinar a qué usuario dirigir en el dispositivo para push.

### Múltiples dispositivos y un usuario {#multiple-devices-and-one-user}

El estado de suscripción push se basa en el usuario y no es específico de ninguna aplicación individual. El estado de la suscripción push es el último valor establecido. Así que si un usuario ha optado por recibir notificaciones push, su estado de suscripción push es `Opted-In` en todos los dispositivos elegibles. Si un usuario posteriormente cancela explícitamente su suscripción a las notificaciones push a través de tu aplicación u otros métodos que tu marca proporcione, su estado de suscripción push se actualiza a `Unsubscribed` y ningún dispositivo registrado para push puede recibir notificaciones push.

## Filtro Foreground Push Enabled {#foreground-push-enabled}

`Foreground Push Enabled` es un filtro de segmentación en Braze que permite a los especialistas en marketing identificar fácilmente a los usuarios que permiten que Braze les envíe notificaciones push y a los usuarios que no han expresado preferencias para no recibir notificaciones push.

El filtro `Foreground Push Enabled` tiene en cuenta lo siguiente:
- La capacidad de Braze para enviar una notificación push (token push de primer plano)
- La preferencia general del usuario para recibir push en cualquiera de sus dispositivos (estado de suscripción push)

![Una captura de pantalla del panel que muestra que un usuario está "Push Registered for Marketing (iOS)"]({% image_buster /assets/img/push_enablement.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Un usuario se considera "habilitado para push" o "registrado para push" si tiene un token push de primer plano activo para una aplicación dentro de tu espacio de trabajo, lo que significa que el estado de habilitación push es específico de la aplicación.

{% alert note %}
Para obtener información sobre cómo verificar el estado de registro push, visita [estado de registro push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle#checking-push-registration-status).
{% endalert %}

## Cómo encontrar información de registro push y registro de cambios {#finding-push-registration-and-changelog-information}

En el panel, puedes encontrar información sobre el registro push y los registros de cambios push en:

- **Segmentación** – Filtra por estados de suscripción de los usuarios, estado habilitado, y estado habilitado en primer plano y segundo plano.
- **Análisis de Campaign** – Consulta las estadísticas push y los comentarios de una sola Campaign o Canvas.
- **Perfil de usuario (pestaña Engagement)** – Consulta **Contact Settings** y el registro de cambios push de un usuario específico.

Al revisar el estado de habilitación push, **Push Registered for** indica para qué plataformas Braze puede enviar push en primer plano a ese usuario. En iOS y Android, si un usuario ha pasado de push en primer plano habilitado a push en segundo plano habilitado (`remote_notification_enabled`), esto se documentará en el registro de cambios push como "Push token was updated from foreground push enabled to foreground push disabled."

Si el usuario se agrega como usuario de prueba, en **Consola para desarrolladores** > **User Event Log**, el perfil del usuario mostrará una solicitud del SDK con `remote_notification_enabled` como `true` o `false`. Es posible que necesites actualizar el perfil del usuario para ver las actualizaciones, ya que hay un breve retraso para que las actualizaciones del SDK lleguen al perfil del usuario.

**Filtros de segmentación para el estado push en iOS:**

- **Push en primer plano y segundo plano deshabilitado en iOS:** El usuario aún no ha recibido un aviso push.
- **Push en segundo plano habilitado en iOS:** El usuario ha recibido el aviso push y dijo que no, o dijo que sí y luego desactivó las notificaciones push en la configuración de su dispositivo (reflejado después de que el usuario tenga una sesión).
- **Push en primer plano habilitado en iOS:** El usuario ha recibido el aviso push y es elegible para recibir push en primer plano.

Los análisis de Campaign reflejarán las estadísticas push en línea con los detalles anteriores en esta sección. También puedes descargar los perfiles de usuario que ingresaron a la Campaign o Canvas para hacer una referencia cruzada de los perfiles de usuario.

## Otros escenarios específicos de plataforma {#other-platform-specific-scenarios}

{% tabs %}
{% tab Web %}

Cuando un usuario acepta el aviso nativo de permiso push, su estado de suscripción cambiará a `opted in`.

Para gestionar las suscripciones, puedes usar el método de usuario [`setPushNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype) para crear una página de configuración de preferencias en tu sitio, después de lo cual puedes filtrar usuarios por estado de cancelación en el panel.

Si un usuario deshabilita las notificaciones en su navegador, la siguiente notificación push enviada a ese usuario rebotará, y Braze actualizará el token push del usuario en consecuencia. Esto se usa para gestionar la elegibilidad de los filtros habilitados para push (`Background or Foreground Push Enabled`, `Foreground Push Enabled` y `Foreground Push Enabled for App`). El estado de suscripción establecido en el perfil del usuario es una configuración a nivel de usuario y no cambia cuando un push rebota.

### Errores de token push web 410 {#410-web-push-token-errors}

Si recibes un error `410: Gone`, esto puede ocurrir cuando un usuario deshabilita las notificaciones push web desde el navegador en la configuración de su sistema operativo, o si está iniciando sesión como un usuario diferente en el mismo dispositivo, o si el usuario no ha visitado el sitio web en algún tiempo.

Si recibes un error `410: Endpoint Not Valid`, esto puede significar que el token push web (esencialmente la URL) ha expirado. Esto puede ocurrir si el usuario nunca vuelve a visitar el sitio o si el navegador invalida el token. También puede ocurrir periódicamente (a menudo cada pocos meses), dependiendo del navegador. Cuando el usuario visite el sitio de nuevo, si aún tiene su navegador configurado en "Allow", Braze recopilará automáticamente un token nuevo para el dispositivo. Esto asume que la [opción de inicialización `disablePushTokenMaintenance`](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#initializationoptions) no se está utilizando durante la inicialización del SDK.

{% alert note %}
Las plataformas web no permiten push en segundo plano ni push silencioso.
{% endalert %}
{% endtab %}
{% tab Android %}

Si un usuario habilitado para push en primer plano deshabilita push en la configuración de su sistema operativo, al inicio de la siguiente sesión:
- Braze lo marca como deshabilitado para push en primer plano y ya no intenta enviarle mensajes push.
- El filtro `Foreground Push Enabled for App (Android)` y el filtro de segmentación `Foreground Push Enabled` (asumiendo que ninguna otra aplicación en el perfil del usuario tiene un token push de primer plano válido) devolverán `false`.

En este escenario, dado que un token push en segundo plano seguirá existiendo, puedes continuar enviando notificaciones push en segundo plano (silenciosas) con el filtro de segmentación `Background or Foreground Push Enabled = true`.

Para Android, Braze considerará a un usuario como deshabilitado para push si:

- Un usuario desinstala la aplicación de su dispositivo.
- Un mensaje push no se entrega debido a un rebote. Esto generalmente es causado por una desinstalación, pero también puede deberse a actualizaciones de la aplicación, una nueva versión del token push o un cambio de formato.
- El registro push falla en Firebase Cloud Messaging (a veces causado por conexiones de red deficientes o una falla al conectarse a FCM o de FCM para devolver un token válido).
- El usuario bloquea las notificaciones push para la aplicación en la configuración de su dispositivo y posteriormente registra una sesión.

{% alert note %}
Solo puedes interceptar una notificación push de Android cuando la aplicación está en primer plano o en segundo plano (pero aún en ejecución). No puedes interceptar notificaciones cuando la aplicación está terminada o completamente cerrada.
{% endalert %}

{% endtab %}
{% tab iOS %}

Independientemente de si un usuario acepta el aviso de adhesión voluntaria de push en primer plano, aún podrás enviar push en segundo plano si tienes las notificaciones remotas habilitadas en Xcode y tu aplicación llama a [`registerForRemoteNotifications()`](https://developer.apple.com/documentation/uikit/uiapplication/1623078-registerforremotenotifications).

Si tu aplicación tiene autorización provisional o el usuario ha optado por push, reciben un token push de primer plano, lo que te permite enviarles todo tipo de push. Dentro de Braze, consideramos que un usuario en iOS que está habilitado para push en primer plano está habilitado para push, ya sea explícitamente (a nivel de aplicación) o provisionalmente (a nivel de dispositivo).

Si un usuario rechaza recibir notificaciones push a nivel del sistema operativo, su estado de suscripción push será `Subscribed`, y su perfil no mostrará que se ha registrado un token push de primer plano.

En el escenario en que un usuario, que inicialmente optó por push a nivel del sistema operativo, deshabilita las notificaciones push en la configuración de su sistema operativo, al inicio de la siguiente sesión ocurrirá lo siguiente:
- Braze lo marca como deshabilitado para push en primer plano y ya no intenta enviar mensajes push.
- El filtro `Foreground Push Enabled for App (iOS)` y el filtro de segmentación `Foreground Push Enabled` (asumiendo que ninguna otra aplicación en el perfil del usuario tiene un token push de primer plano válido) devolverán `false`.

En este escenario, dado que un token push en segundo plano seguirá existiendo, puedes continuar enviando notificaciones push en segundo plano (silenciosas) con el filtro de segmentación `Background or Foreground Push Enabled = true`.

{% alert note %}
iOS no permite que las aplicaciones intercepten una notificación push antes de que se muestre. Esto significa que las aplicaciones (y Braze) no tienen control sobre si puedes mostrar u ocultar la notificación. Un usuario puede desactivar las notificaciones push para una aplicación en la configuración del dispositivo, pero eso es controlado por el sistema operativo.
{% endalert %}

{% endtab %}
{% endtabs %}

## Buenas prácticas {#best-practices}

Consulta nuestro artículo dedicado sobre [buenas prácticas de push]({{site.baseurl}}/user_guide/channels/push/best_practices) para obtener orientación detallada sobre cómo optimizar tu uso de push en Braze.