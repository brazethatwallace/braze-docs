{% multi_lang_include developer_guide/prerequisites/android.md %}

## Configuración de notificaciones push {#setting-up-push-notifications}

Los teléfonos más nuevos fabricados por [Huawei](https://huaweimobileservices.com/) vienen equipados con Huawei Mobile Services (HMS), un servicio utilizado para entregar notificaciones push en lugar de Firebase Cloud Messaging (FCM) de Google.

### Paso 1: Regístrate para una cuenta de desarrollador de Huawei {#step-1-register-for-a-huawei-developer-account}

Antes de empezar, tendrás que registrarte y configurar una [cuenta de desarrollador de Huawei](https://developer.huawei.com/consumer/en/console). En tu cuenta de Huawei, ve a **My Projects > Project Settings > App Information**, y toma nota de `App ID` y `App secret`.

![Página de información de la aplicación en la consola para desarrolladores de Huawei mostrando el App ID y el App secret.]({% image_buster /assets/img/huawei/huawei-credentials.png %})

### Paso 2: Crea una nueva aplicación Huawei en el panel de Braze {#step-2-create-a-new-huawei-app-in-the-braze-dashboard}

En el panel de Braze, ve a **Configuración de la aplicación**, que aparece en la navegación **Configuración**.

Haz clic en **+ Añadir aplicación**, ponle un nombre (como Mi aplicación Huawei) y selecciona `Android` como plataforma.

![Diálogo de añadir aplicación en Braze creando una aplicación Android de Huawei.]({% image_buster /assets/img/huawei/huawei-create-app.png %}){: style="max-width:60%;"}

Una vez creada tu nueva aplicación de Braze, localiza la configuración de notificaciones push y selecciona `Huawei` como proveedor de notificaciones push. A continuación, proporciona tu `Huawei Client Secret` y `Huawei App ID`.

![Configuración del proveedor push de Huawei en Braze con los campos Huawei App ID y Client Secret.]({% image_buster /assets/img/huawei/huawei-dashboard-credentials.png %})

### Paso 3: Integra el SDK de mensajería de Huawei en tu aplicación {#step-3-integrate-the-huawei-messaging-sdk-into-your-app}

Huawei proporcionó un [codelab de integración en Android](https://developer.huawei.com/consumer/en/codelab/HMSPushKit/index.html) en el que se detalla la integración del servicio de mensajería de Huawei en tu aplicación. Sigue esos pasos para empezar.

Después de completar el codelab, tendrás que crear un [servicio de mensajes personalizado de Huawei](https://developer.huawei.com/consumer/en/doc/development/HMS-References/push-HmsMessageService-cls) para obtener tokens de notificaciones push y reenviar mensajes al SDK de Braze.

{% tabs %}
{% tab JAVA %}

```java
public class CustomPushService extends HmsMessageService {
  @Override
  public void onNewToken(String token) {
    super.onNewToken(token);
    Braze.getInstance(this.getApplicationContext()).setRegisteredPushToken(token);
  }

  @Override
  public void onMessageReceived(RemoteMessage remoteMessage) {
    super.onMessageReceived(remoteMessage);
    if (BrazeHuaweiPushHandler.handleHmsRemoteMessageData(this.getApplicationContext(), remoteMessage.getDataOfMap())) {
      // Braze has handled the Huawei push notification
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class CustomPushService: HmsMessageService() {
  override fun onNewToken(token: String?) {
    super.onNewToken(token)
    Braze.getInstance(applicationContext).setRegisteredPushToken(token!!)
  }

  override fun onMessageReceived(hmsRemoteMessage: RemoteMessage?) {
    super.onMessageReceived(hmsRemoteMessage)
    if (BrazeHuaweiPushHandler.handleHmsRemoteMessageData(applicationContext, hmsRemoteMessage?.dataOfMap)) {
      // Braze has handled the Huawei push notification
    }
  }
}
```

{% endtab %}
{% endtabs %}

Después de añadir tu servicio push personalizado, añade lo siguiente a tu `AndroidManifest.xml`:

```xml
<service
  android:name="package.of.your.CustomPushService"
  android:exported="false">
  <intent-filter>
    <action android:name="com.huawei.push.action.MESSAGING_EVENT" />
  </intent-filter>
</service>
```

### Paso 4: Gestionar las notificaciones en primer plano {#step-4-handle-foreground-notifications}

De forma predeterminada, cuando llega una notificación push mientras la aplicación está en primer plano, Huawei la muestra automáticamente. Para que Braze procese la carga útil de la notificación push (para el seguimiento de análisis, la gestión de vínculos profundos y el procesamiento personalizado), envía los datos push entrantes a Braze dentro de tu método `HmsMessageService.onMessageReceived`.

Cuando llamas a `BrazeHuaweiPushHandler.handleHmsRemoteMessageData`, Braze determina si la carga útil es una notificación push de Braze y, si es así, crea y muestra la notificación. Para obtener más información, consulta [Gestión de notificaciones en primer plano]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android#handling-foreground-notifications) en la documentación sobre notificaciones push de Android.

Para ver un ejemplo completo, consulta la [referencia del controlador Huawei](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-huawei-push-handler/index.html) en la documentación del SDK de Braze para Android.

### Paso 5: Prueba tus notificaciones push (opcional) {#step-5-test-your-push-notifications-optional}

En este punto, habrás creado una nueva aplicación Android de Huawei en el panel de Braze, la habrás configurado con tus credenciales de desarrollador de Huawei y habrás integrado los SDK de Braze y Huawei en tu aplicación.

A continuación, podemos poner a prueba la integración probando una nueva campaña push en Braze.

#### Paso 5.1: Crea una nueva campaña de notificación push {#step-51-create-a-new-push-notification-campaign}

En la página **Campaigns**, crea una nueva campaña y elige **Push Notification** como tipo de mensaje.

Después de nombrar tu campaña, elige **Android Push** como plataforma push.

![El creador de campañas muestra las plataformas push disponibles.]({% image_buster /assets/img/huawei/huawei-test-push-platforms.png %})

A continuación, crea tu campaña push con un título y un mensaje.

#### Paso 5.2: Envía un push de prueba {#step-52-send-a-test-push}

En la pestaña **Prueba**, introduce tu ID de usuario, que habrás configurado en tu aplicación utilizando el [método `changeUser(USER_ID_STRING)`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids#assigning-a-user-id), y haz clic en **Enviar prueba** para enviar un push de prueba.

![La pestaña de prueba en el creador de campañas muestra que puedes enviarte un mensaje de prueba proporcionando tu ID de usuario e introduciéndolo en el campo «Añadir usuarios individuales».]({% image_buster /assets/img/huawei/huawei-test-send.png %})

En este punto, deberías recibir una notificación push de prueba de Braze en tu dispositivo Huawei (HMS).

#### Paso 5.3: Configura la segmentación de Huawei (opcional) {#step-53-set-up-huawei-segmentation-optional}

Como tu aplicación de Huawei en el panel de Braze se basa en la plataforma push de Android, tienes la flexibilidad de enviar push a todos los usuarios de Android (Firebase Cloud Messaging y Huawei Mobile Services), o puedes elegir segmentar la audiencia de tu campaña en aplicaciones específicas.

Para enviar notificaciones push solo a aplicaciones Huawei, [crea un nuevo Segment]({{ site.baseurl }}/user_guide/engagement_tools/segments/creating_a_segment/#step-3-choose-your-app-or-platform) y selecciona tu aplicación Huawei en la sección **Aplicaciones**.

![Filtro de aplicación en un Segment de Braze seleccionando la aplicación Huawei para la segmentación push.]({% image_buster /assets/img/huawei/huawei-segmentation.png %})

Por supuesto, si quieres enviar el mismo push a todos los proveedores de push de Android, puedes elegir no especificar la aplicación, lo que enviará a todas las aplicaciones de Android configuradas dentro del espacio de trabajo actual.