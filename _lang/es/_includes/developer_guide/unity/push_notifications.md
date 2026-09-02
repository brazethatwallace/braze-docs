{% multi_lang_include developer_guide/prerequisites/unity.md %}

## Configuración de la notificación push {#setting-up-push-notification}

### Paso 1: Configurar la plataforma {#step-1-set-up-the-platform}

{% tabs %}
{% tab Android %}
#### Paso 1.1: Habilitar Firebase {#step-11-enable-firebase}

Para empezar, sigue la [documentación de configuración de Firebase Unity](https://firebase.google.com/docs/unity/setup).

{% alert note %}
La integración del SDK or kit de desarrollo de software Unity de Firebase puede hacer que se anule tu `AndroidManifest.xml`. Si eso ocurre, asegúrate de revertirlo al original.
{% endalert %}

#### Paso 1.2: Configura tus credenciales de Firebase {#step-12-set-your-firebase-credentials}

Tienes que introducir tu clave de servidor Firebase y tu ID de remitente en el panel de Braze. Para ello, accede a la [consola de desarrolladores de Firebase](https://console.firebase.google.com/) y selecciona tu proyecto Firebase. A continuación, selecciona **Cloud Messaging** en **Settings** y copia la clave del servidor y el ID del remitente:<br>![Configuración de Cloud Messaging en la consola de Firebase mostrando la clave del servidor y el ID del remitente.]({% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey")

En Braze, selecciona tu aplicación Android en la página **Configuración de la aplicación**, en **Administrar configuración**. A continuación, introduce tu clave de servidor de Firebase en el campo **Firebase Cloud Messaging Server Key** y el ID de remitente de Firebase en el campo **Firebase Cloud Messaging Sender** ID.

![Configuración de la aplicación Android en Braze con los campos de clave de servidor y ID de remitente de Firebase Cloud Messaging.]({% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey")
{% endtab %}

{% tab Swift %}
#### Paso 1.1: Verifica el método de integración {#step-11-verify-integration-method}

Braze proporciona una solución nativa de Unity para automatizar las integraciones push de iOS. Si prefieres configurar y administrar tu integración manualmente, consulta [Swift: Notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

De lo contrario, continúa con el siguiente paso.

{% alert note %}
Nuestra solución de notificación push automática aprovecha la característica de autorización provisional de iOS 12 y no se puede utilizar con la ventana emergente de notificación push nativa.
{% endalert %}
{% endtab %}

{% tab Amazon Device Messaging %}
#### Paso 1.1: Habilitar ADM {#step-11-enable-adm}

1. Crea una cuenta en el [Portal del Desarrollador de Amazon Apps & Games](https://developer.amazon.com/public) si aún no lo has hecho.
2. Obtén [credenciales OAuth (ID de cliente y secreto de cliente) y una clave de API de ADM](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials).
3. Habilita **Automatic ADM Registration Enabled** en la ventana de configuración de Unity Braze.
  - Alternativamente, puedes añadir la siguiente línea a tu archivo `res/values/braze.xml` para habilitar el registro de ADM:

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```
{% endtab %}
{% endtabs %}

### Paso 2: Configurar notificaciones push {#step-2-configure-push-notifications}

{% tabs %}
{% tab Android %}
#### Paso 2.1: Configurar los ajustes push {#unity_step-21-configure-push-settings}

El SDK or kit de desarrollo de software de Braze puede gestionar automáticamente el registro push con los servidores de Firebase Cloud Messaging para que los dispositivos reciban notificaciones push. En Unity, habilita **Automate Unity Android Integration** y, a continuación, configura los siguientes ajustes de **Push Notification**.

| Configuración | Descripción |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Automatic Firebase Cloud Messaging Registration Enabled | Ordena al SDK or kit de desarrollo de software de Braze que recupere y envíe automáticamente un token de notificaciones push de FCM para un dispositivo. |
| Firebase Cloud Messaging Sender ID | El ID de remitente de tu consola Firebase. |
| Handle Push Deeplinks Automatically | Si el SDK or kit de desarrollo de software debe gestionar la apertura de vínculos profundos o la apertura de la aplicación cuando se hace clic en las notificaciones push. |
| Small Notification Icon Drawable | Referencia de recurso drawable de Android para el icono pequeño que se muestra cuando llega una notificación push. Introduce la referencia completa incluyendo el prefijo `@drawable/` (por ejemplo, `@drawable/hourglass_icon`). La integración automatizada escribe este valor en `braze.xml` tal como se introduce. Si lo dejas vacío, la notificación utiliza el icono de la aplicación como icono pequeño. |
| Large Notification Icon Drawable | Icono grande opcional para las notificaciones. Utiliza el mismo formato `@drawable/` que el icono pequeño (por ejemplo, `@drawable/my_large_icon`). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Paso 2.1: Configurar los ajustes push" }

{% alert note %}
**Small Notification Icon Drawable** y **Large Notification Icon Drawable** aparecen en **Push Configuration** dentro de **Braze > Braze Configuration**. Ambos valores se escriben en `braze.xml` tal como los introduces. Incluye tú mismo el prefijo `@drawable/`: la integración de Braze Unity no lo añade por ti (por ejemplo, `<drawable name="com_braze_push_small_notification_icon">@drawable/hourglass_icon</drawable>`).
{% endalert %}
{% endtab %}

{% tab Swift %}
#### Paso 2.1: Sube tu token de APNs {#step-21-upload-your-apns-token}

{% multi_lang_include developer_guide/swift/apns_token.md %}

#### Paso 2.2: Habilitar push automático {#step-22-enable-automatic-push}

Abre los ajustes de configuración de Braze en el editor de Unity navegando hasta **Braze > Braze Configuration**.

Marca **Integrate Push With Braze** para registrar automáticamente usuarios para notificaciones push, pasar tokens de notificaciones push a Braze, hacer un seguimiento de los análisis de aperturas push y aprovechar nuestra gestión predeterminada de notificaciones push.

#### Paso 2.3: Habilitar push en segundo plano (opcional) {#step-23-enable-background-push-optional}

Marca **Enable Background Push** si quieres habilitar `background mode` para las notificaciones push. Esto permite al sistema despertar tu aplicación del estado `suspended` cuando llega una notificación push, habilitando tu aplicación para descargar contenido en respuesta a las notificaciones push. Marcar esta opción es necesario para nuestra funcionalidad de Uninstall Tracking.

![El editor de Unity muestra las opciones de configuración de Braze. En este editor están habilitadas las opciones "Automate Unity iOS integration", "Integrate push with braze" y "Enable background push".]({% image_buster /assets/img/unity/ios/unity_ios_enable_background.png %})

#### Paso 2.4: Desactivar el registro automático (opcional) {#step-24-disable-automatic-registration-optional}

Los usuarios que aún no hayan optado por la adhesión voluntaria a las notificaciones push serán autorizados automáticamente a recibir notificaciones push al abrir tu aplicación. Para desactivar esta característica y registrar manualmente a los usuarios para push, marca **Disable Automatic Push Registration**.

- Si la opción **Disable Provisional Authorization** no está marcada en iOS 12 o posterior, el usuario estará autorizado provisionalmente (de forma silenciosa) a recibir push silenciosos. Si está marcada, se mostrará al usuario el aviso push nativo.
- Si necesitas configurar exactamente cuándo se muestra el aviso en tiempo de ejecución, desactiva el registro automático desde el editor de configuración de Braze y utiliza en su lugar `AppboyBinding.PromptUserForPushPermissions()`.

![El editor de Unity muestra las opciones de configuración de Braze. En este editor están habilitadas las opciones "Automate Unity iOS integration", "Integrate push with braze" y "Disable automatic push registration".]({% image_buster /assets/img/unity/ios/unity_ios_disable_auto_push.png %})
{% endtab %}

{% tab Amazon Device Messaging %}
#### Paso 2.1: Actualiza `AndroidManifest.xml` {#unity_step-21-update-androidmanifestxml}

Si tu aplicación no tiene un `AndroidManifest.xml`, puedes utilizar la siguiente plantilla. De lo contrario, si ya tienes un `AndroidManifest.xml`, asegúrate de que cualquiera de las siguientes secciones que falten se añadan a tu `AndroidManifest.xml` existente.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />
  <permission
    android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE"
    android:protectionLevel="signature" />
  <uses-permission android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE" />
  <uses-permission android:name="com.amazon.device.messaging.permission.RECEIVE" />

  <application android:icon="@drawable/app_icon"
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity"
      android:label="@string/app_name"
      android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen"
      android:screenOrientation="sensor">
      <meta-data android:name="android.app.lib_name" android:value="unity" />
      <meta-data android:name="unityplayer.ForwardNativeEventsToDalvik" android:value="true" />
      <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
      </intent-filter>
    </activity>

    <receiver android:name="com.braze.push.BrazeAmazonDeviceMessagingReceiver" android:permission="com.amazon.device.messaging.permission.SEND">
      <intent-filter>
          <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
          <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
          <category android:name="REPLACE_WITH_YOUR_PACKAGE_NAME" />
      </intent-filter>
    </receiver>
  </application>
</manifest>
```

#### Paso 2.2: Almacena tu clave de API de ADM {#step-22-store-your-adm-api-key}

En primer lugar, [genera una clave de API de ADM para tu aplicación](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials), luego guarda la clave en un archivo llamado `api_key.txt` y añádelo al directorio [`Assets/`](https://docs.unity3d.com/Manual/AndroidAARPlugins.html) de tu proyecto.

{% alert important %}
Amazon no reconocerá tu clave si `api_key.txt` contiene algún carácter de espacio en blanco, como un salto de línea final.
{% endalert %}

A continuación, en tu archivo `mainTemplate.gradle`, añade lo siguiente:

```gradle
task copyAmazon(type: Copy) {
    def unityProjectPath = $/file:///**DIR_UNITYPROJECT**/$.replace("\\", "/")
    from unityProjectPath + '/Assets/api_key.txt'
    into new File(projectDir, 'src/main/assets')
}

preBuild.dependsOn(copyAmazon)
```

#### Paso 2.3: Añadir archivo JAR de ADM {#step-23-add-adm-jar}

El archivo JAR de ADM necesario puede colocarse en cualquier lugar de tu proyecto de acuerdo con la [documentación JAR de Unity](https://docs.unity3d.com/Manual/AndroidJARPlugins.html).

#### Paso 2.4: Añadir el secreto de cliente y el ID de cliente a tu panel de Braze {#step-24-add-client-secret-and-client-id-to-your-braze-dashboard}

Por último, debes añadir el secreto de cliente y el ID de cliente que obtuviste en el [paso 1](#unity_step-1-enable-adm) a la página **Administrar configuración** del panel de Braze.

![Página de configuración de la aplicación Fire OS en Braze con los campos de ID de cliente y secreto de cliente de ADM.]({% image_buster /assets/img_archive/fire_os_dashboard.png %})
{% endtab %}
{% endtabs %}

### Paso 3: Configurar escuchas push {#step-3-set-push-listeners}

{% tabs %}
{% tab Android %}
#### Paso 3.1: Habilitar la escucha de push recibido {#step-31-enable-push-received-listener}

La escucha de push recibido se activa cuando un usuario recibe una notificación push. Para enviar la carga útil push a Unity, establece el nombre de tu objeto del juego y el método de devolución de llamada de la escucha de push recibido en **Set Push Received Listener**.

#### Paso 3.2: Habilitar la escucha de push abierto {#step-32-enable-push-opened-listener}

La escucha de push abierto se activa cuando un usuario inicia la aplicación haciendo clic en una notificación push. Para enviar la carga útil push a Unity, establece el nombre de tu objeto del juego y el método de devolución de llamada de la escucha de push abierto en **Set Push Opened Listener**.

#### Paso 3.3: Habilitar la escucha de push eliminado {#step-33-enable-push-deleted-listener}

La escucha de push eliminado se activa cuando un usuario desliza o descarta una notificación push. Para enviar la carga útil push a Unity, establece el nombre de tu objeto del juego y el método de devolución de llamada de la escucha de push eliminado en **Set Push Deleted Listener**.

#### Ejemplo de escucha push {#push-listener-example}

El siguiente ejemplo implementa el objeto del juego `BrazeCallback` utilizando un nombre de método de devolución de llamada de `PushNotificationReceivedCallback`, `PushNotificationOpenedCallback` y `PushNotificationDeletedCallback` respectivamente.

![Este gráfico de ejemplo de implementación muestra las opciones de configuración de Braze mencionadas en las secciones anteriores y un fragmento de código en C#.]({% image_buster /assets/img/unity/android/unity_android_full_push_listener.png %} "Android Full Listener Example")

```csharp
public class MainMenu : MonoBehaviour {
  void PushNotificationReceivedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationReceivedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification received: " + pushNotification);
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push received Notification event: " + pushNotification);
#endif
  }

  void PushNotificationOpenedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationOpenedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification opened: " + pushNotification);
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push opened Notification event: " + pushNotification);
#endif
  }

  void PushNotificationDeletedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationDeletedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification dismissed: " + pushNotification);
#endif
  }
}
```
{% endtab %}

{% tab Swift %}
#### Paso 3.1: Habilitar la escucha de push recibido

La escucha de push recibido se activa cuando un usuario recibe una notificación push mientras utiliza activamente la aplicación (por ejemplo, cuando la aplicación está en primer plano). Configura la escucha de push recibido en el editor de configuración de Braze. Si necesitas configurar la escucha de tu objeto del juego en tiempo de ejecución, utiliza `AppboyBinding.ConfigureListener()` y especifica `BrazeUnityMessageType.PUSH_RECEIVED`.

![El editor de Unity muestra las opciones de configuración de Braze. En este editor, se amplía la opción "Set Push Received Listener" y se proporcionan el "Game Object Name" (AppBoyCallback) y el "Callback Method Name" (PushNotificationReceivedCallback).]({% image_buster /assets/img/unity/ios/unity_ios_push_received.png %})

#### Paso 3.2: Habilitar la escucha de push abierto

La escucha de push abierto se activa cuando un usuario inicia la aplicación haciendo clic en una notificación push. Para enviar la carga útil push a Unity, establece el nombre de tu objeto del juego y el método de devolución de llamada de la escucha de push abierto en la opción **Set Push Opened Listener**:

![El editor de Unity muestra las opciones de configuración de Braze. En este editor, se amplía la opción "Set Push Opened Listener" y se proporcionan el "Game Object Name" (AppBoyCallback) y el "Callback Method Name" (PushNotificationOpenedCallback).]({% image_buster /assets/img/unity/ios/unity_ios_push_opened.png %})

Si necesitas configurar la escucha de tu objeto del juego en tiempo de ejecución, utiliza `AppboyBinding.ConfigureListener()` y especifica `BrazeUnityMessageType.PUSH_OPENED`.

#### Ejemplo de escucha push

El siguiente ejemplo implementa el objeto del juego `AppboyCallback` utilizando un nombre de método de devolución de llamada de `PushNotificationReceivedCallback` y `PushNotificationOpenedCallback`, respectivamente.

![Este gráfico de ejemplo de implementación muestra las opciones de configuración de Braze mencionadas en las secciones anteriores y un fragmento de código en C#.]({% image_buster /assets/img/unity/ios/unity_ios_appboy_callback.png %})

```csharp
public class MainMenu : MonoBehaviour {
  void PushNotificationReceivedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationReceivedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification received: " + pushNotification);
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push received Notification event: " + pushNotification);
#endif
  }

  void PushNotificationOpenedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationOpenedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification opened: " + pushNotification);
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push opened Notification event: " + pushNotification);
#endif
  }
}
```
{% endtab %}

{% tab Amazon Device Messaging %}
Al actualizar tu `AndroidManifest.xml` en el [paso anterior](#unity_step-21-update-androidmanifestxml), las escuchas push se configuraron automáticamente cuando añadiste las siguientes líneas. Por lo tanto, no es necesaria ninguna otra configuración.

```xml
<action android:name="com.amazon.device.messaging.intent.RECEIVE" />
<action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
```

{% alert note %}
Para saber más sobre las escuchas push de ADM, consulta [Amazon: Integra Amazon Device Messaging](https://developer.amazon.com/docs/video-skills-fire-tv-apps/integrate-adm.html).
{% endalert %}
{% endtab %}
{% endtabs %}

## Configuraciones opcionales {#optional-configurations}

{% tabs %}
{% tab Android %}
### Vinculación en profundidad a los recursos de la aplicación {#deep-linking-to-in-app-resources}

Aunque Braze puede gestionar vínculos profundos estándar (como URL de sitios web, URI de Android, etc.) de forma predeterminada, la creación de vínculos profundos personalizados requiere una configuración adicional del manifiesto.

Para obtener información sobre la configuración, visita [Vinculación en profundidad con recursos de la aplicación](https://developer.android.com/training/app-links/deep-linking).

#### Añadir iconos de notificación push de Braze {#adding-braze-push-notification-icons}

{% alert important %}
No añadas imágenes de iconos de notificación en `Assets/Plugins/Android/res`. Unity [dejó de admitir la provisión de recursos Android en esa ruta](https://support.unity.com/hc/en-us/articles/115005875443-Providing-Android-resources-in-Assets-Plugins-Android-res-is-deprecated), lo que puede generar advertencias de compilación o errores de validación. Empaqueta tus drawables de iconos en un [plug-in Android Archive (AAR)](https://docs.unity3d.com/Manual/AndroidAARPlugins.html) o en un proyecto de biblioteca Android para que se fusionen con los recursos de la aplicación compilada como cualquier otro drawable.
{% endalert %}

Para añadir iconos push a tu proyecto, crea un plug-in AAR o una biblioteca Android que contenga los archivos de imagen de los iconos en `res/drawable*` (o carpetas específicas por densidad), y luego haz referencia a cada icono en **Braze > Braze Configuration** utilizando el nombre completo del recurso `@drawable/` (consulta el [paso 2.1: Configurar los ajustes push](#unity_step-21-configure-push-settings)). Para conocer los pasos de empaquetado e importación de Unity, consulta [Proyectos de bibliotecas Android y plug-ins de archivos Android](https://docs.unity3d.com/Manual/AndroidAARPlugins.html).

Para las reglas de diseño de iconos pequeños (solo alfa, sin color), consulta [Notificaciones push de Android]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android), paso 2: Ajustar los iconos pequeños a las directrices de diseño.
{% endtab %}

{% tab Swift %}
#### Devolución de llamada de token de notificaciones push {#push-token-callback}

Para recibir una copia de los tokens de dispositivo de Braze del SO, establece un delegado mediante `AppboyBinding.SetPushTokenReceivedFromSystemDelegate()`.
{% endtab %}

{% tab Amazon Device Messaging %}
De momento no hay configuraciones opcionales para ADM.
{% endtab %}
{% endtabs %}