## Estados de suscripción push {#push-sub-states}

Un "Estado de suscripción push" en Braze identifica la preferencia global de un **usuario** en cuanto a su deseo de recibir notificaciones push. Dado que el estado de suscripción se basa en el usuario, no es específico de ninguna aplicación concreta. Los estados de suscripción se convierten en indicadores útiles a la hora de decidir a qué usuarios dirigir las notificaciones push.

{% alert note %}
El estado de suscripción push de un usuario se aplica a todo su perfil de usuario, que incluye todos los dispositivos del usuario.
{% endalert %}

Existen las siguientes opciones de estado de suscripción: `Subscribed`, `Opted-In` y `Unsubscribed`.

De forma predeterminada, para que tu usuario pueda recibir tus mensajes a través de push, su estado de suscripción push debe ser `Subscribed` u `Opted-In`, y debe tener habilitadas las notificaciones push en primer plano. Puedes anular esta configuración si es necesario al redactar un mensaje.

| Estado de adhesión voluntaria | Descripción |
|---|---|
| `Subscribed` | Estado predeterminado de la suscripción push cuando se crea un perfil de usuario en Braze. |
| `Opted-In` | Un usuario ha expresado explícitamente su preferencia por recibir notificaciones push. Braze cambia automáticamente el estado de adhesión voluntaria de un usuario a `Opted-In` si este acepta un mensaje de push a nivel del sistema operativo.<br><br>Esto no se aplica a los usuarios de Android 12 o inferior. |
| `Unsubscribed` | Un usuario se da de baja explícitamente de push a través de tu aplicación o de otros métodos que tu marca pone a disposición. De forma predeterminada, las Campaigns push de Braze se dirigen únicamente a los usuarios que están `Subscribed` u `Opted-in` para push. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados de suscripción push" }

{% alert important %}
Braze no cambia automáticamente el estado de suscripción push de un usuario a `Unsubscribed`. Recuerda que si el estado de la suscripción push de un usuario es `Unsubscribed`, entonces el filtro `Foreground Push Enabled` del usuario en la segmentación es `false`.
{% endalert %}

### Registro push y usuarios alcanzables {#push-registration-and-reachable-users}

El estado de suscripción push refleja la preferencia de un usuario, pero que cuente como **alcanzable** para push en el panel también depende del [registro push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_token_lifecycle), es decir, de que exista un token de push en primer plano válido en su perfil. Para saber cómo Braze calcula los recuentos a nivel de canal, consulta [Medir el tamaño de un segmento]({{site.baseurl}}/user_guide/audience/segments/measuring_segment_size).

- **Campaigns push y Canvas:** Los usuarios que no están registrados para push no se incluyen en **Usuarios alcanzables** para push de Android o push de iOS en las estadísticas de audiencia, incluso cuando su estado de suscripción push es `Subscribed` u `Opted-In`.
- **Otros canales:** Los mismos usuarios pueden seguir contando como alcanzables para otros canales en los que califiquen (por ejemplo, correo electrónico o mensajes dentro de la aplicación).
- **Segments:** La pertenencia a un segmento sigue tus filtros. Los usuarios sin registro push permanecen en el segmento a menos que un filtro los excluya (por ejemplo, **Foreground Push Enabled**). La pertenencia total al segmento puede ser mayor que la suma de usuarios que se muestran en las filas de **Usuarios alcanzables** específicas de push.

Un perfil de usuario puede mostrar el estado de suscripción push `Subscribed` sin tener un token de push asignado. Esos usuarios aún no cuentan como **Usuarios alcanzables** para push de Android o push de iOS hasta que Braze registre un token válido.

Para las definiciones de filtros, consulta [Filtros de segmentación]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

### Actualización de los estados de suscripción push {#update-push-subscription-state}

Revisa las siguientes formas de actualizar el estado de la suscripción push de un usuario:

#### Adhesión voluntaria automática (por defecto) {#automatic-opt-in-default}

Por defecto, Braze establece el estado de suscripción push de un usuario en `Opted-In` cuando autoriza por primera vez las notificaciones push para tu aplicación. Braze también lo hace cuando un usuario vuelve a habilitar los permisos push en la configuración del sistema tras haberlos desactivado previamente.

{% tabs local %}
{% tab android %}
Para desactivar este comportamiento predeterminado, añade la siguiente propiedad al archivo `braze.xml` de tu proyecto de Android Studio:

```xml
<bool name="com_braze_optin_when_push_authorized">false</bool>
```
{% endtab %}

{% tab swift %}
En iOS, una nueva instalación normalmente muestra el estado de suscripción push como **`Subscribed`** hasta que el usuario permite las notificaciones. Después de que el usuario seleccione **Permitir** en el mensaje del sistema operativo, Braze establece el estado en **`Opted-In`** cuando la adhesión voluntaria automática está habilitada. Si el usuario selecciona **No permitir** y luego activa las notificaciones push en los ajustes de iOS, el estado se actualiza después de que el usuario registre una sesión, no en el momento en que cambia los ajustes.

A partir de la [versión 7.5.0 del SDK de Braze Swift](https://github.com/braze-inc/braze-swift-sdk/releases/tag/7.5.0), puedes desactivar o personalizar aún más este comportamiento añadiendo la configuración `optInWhenPushAuthorized` al archivo `AppDelegate.swift` de tu proyecto Xcode:

```swift
configuration.optInWhenPushAuthorized = false // disables the default behavior

let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% endtabs %}

#### Integración de SDK {#sdk-integration}

Puedes actualizar el estado de suscripción de un usuario con el SDK de Braze utilizando el método `setPushNotificationSubscriptionType` en [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setpushnotificationsubscriptiontype), [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-push-notification-subscription-type.html) o [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/set(pushnotificationsubscriptionstate:)). Por ejemplo, puedes utilizar este método para crear una página de configuración en tu aplicación en la que los usuarios puedan activar o desactivar manualmente las notificaciones push.

#### REST API

Puedes actualizar el estado de suscripción de un usuario con la REST API de Braze utilizando el [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para actualizar su atributo [`push_subscribe`]({{site.baseurl}}/api/objects_filters/user_attributes_object).

### Diferencias entre la habilitación push y el estado de suscripción push {#differences-between-push-enablement-and-push-subscription-status}

La habilitación push se refiere a si un usuario ha concedido permiso a nivel del sistema operativo o del navegador para recibir notificaciones en un dispositivo específico. El estado de suscripción push es una configuración a nivel de Braze que representa la preferencia global de un usuario para recibir notificaciones push en todo su perfil.

Cuando la adhesión voluntaria automática está habilitada (el comportamiento predeterminado), Braze actualiza el estado de suscripción push de un usuario a `Opted-In` cuando autoriza las notificaciones push para tu aplicación o vuelve a habilitar los permisos en la configuración del sistema (por ejemplo, en iOS, Android 13+ y navegadores web compatibles). De lo contrario, el estado de suscripción push del usuario permanece en `Subscribed` hasta que lo cambies explícitamente mediante un método del SDK o una llamada a la REST API.

Braze no cambia automáticamente el estado de suscripción push de un usuario a `Unsubscribed` cuando este desactiva las notificaciones a nivel del sistema operativo, del navegador o de la aplicación. Para actualizar el estado de suscripción push de un usuario, debes actualizarlo en Braze. Por ejemplo, si un usuario desactiva las notificaciones push desde un centro de preferencias dentro de la aplicación, actualiza el estado de suscripción push a `Unsubscribed` en Braze. Braze no actualiza los perfiles de usuario basándose en tu centro de preferencias. Para alinear los estados de suscripción con las preferencias del usuario dentro de la aplicación, llama a los métodos correspondientes utilizando el SDK (iOS o Android) o la REST API. Para más información, consulta [Actualización de los estados de suscripción push]({{site.baseurl}}/user_guide/channels/push/push_setup/push_subscription_states#update-push-subscription-state).

### Tokens de push importados (iOS) {#imported-push-tokens-ios}

Cuando [importas tokens de push de iOS]({{site.baseurl}}/api/objects_filters/user_attributes_object#push-token-import) con `push_token_import`, el estado de suscripción push del usuario suele ser **`Subscribed`** hasta que registre una sesión en tu aplicación integrada con Braze. Después de la primera sesión, Braze puede actualizar el estado a **`Opted-In`** si se aplica la [adhesión voluntaria automática](#automatic-opt-in-default) (por ejemplo, cuando el usuario autoriza las notificaciones push en iOS y `optInWhenPushAuthorized` está habilitado).

Revisa **Configuración de contacto** en el perfil del usuario después de la importación y de nuevo después de la primera sesión del usuario en la aplicación para confirmar el estado esperado.

### Comprobación del estado de la suscripción push {#checking-push-subscription-state}

![Perfil de usuario de John Doe con su estado de suscripción push establecido en Subscribed.]({% image_buster /assets/img/push_example.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Puedes comprobar el estado de la suscripción push de un usuario con Braze de cualquiera de las siguientes maneras:

* **Perfil del usuario:** Puedes acceder a los perfiles de usuario individuales a través del panel de Braze en la página **[Búsqueda de usuarios]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles)**. Después de encontrar el perfil de un usuario (a través de la dirección de correo electrónico, el número de teléfono o el ID de usuario externo), puedes seleccionar la pestaña **Engagement** para ver y ajustar manualmente el estado de suscripción de un usuario.
* **Exportación de la REST API:** Puedes exportar perfiles de usuario individuales en formato JSON utilizando los endpoints [Usuarios por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment) o [Usuarios por identificador]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier). Braze devuelve un objeto de tokens de notificaciones push que contiene información sobre la habilitación de push por dispositivo.