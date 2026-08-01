---
nav_title: Integración con Baidu
article_title: Integración de notificaciones push de Baidu para Android
platform: Android
permalink: /baidu_integration/
description: "Este artículo muestra cómo configurar una integración de Baidu en Android."
hidden: true
excerpt_separator: ""
---
# Integración con Baidu {#baidu-integration}
{% alert warning %}
La integración de Baidu Push de Braze está obsoleta desde el 24 de marzo de 2022.

* **24 de marzo de 2022:** no se pueden crear nuevas aplicaciones de Baidu en el panel de Braze.
* **15 de septiembre de 2022:** no se pueden crear nuevos mensajes push de Baidu. Los mensajes existentes y la recopilación de datos no se ven afectados.
* **15 de enero de 2023:** Braze ya no envía mensajes ni recopila datos de las aplicaciones de Baidu.
{% endalert %}

Braze puede enviar notificaciones push a dispositivos Android utilizando [Baidu Cloud Push]({% image_buster /assets/img_archive/baidu_app_console.png %}). Ten en cuenta que el uso de Baidu Cloud Push no requiere que distribuyas tus aplicaciones a través de Baidu App Store.

## Paso 1: Crear una cuenta de Baidu {#step-1-create-a-baidu-account}

Para crear una cuenta de Baidu, visita el [portal de Baidu](https://www.baidu.com/) y haz clic en **登录** (Iniciar sesión) para abrir un cuadro de diálogo que te permitirá iniciar sesión o crear una cuenta nueva.

![Portal de Baidu]({% image_buster /assets/img_archive/baidu_portal.png %})

Para crear una cuenta nueva, en la parte inferior del cuadro de diálogo de inicio de sesión, haz clic en **立即注册** (cuenta nueva).

![Cuadro de diálogo de inicio de sesión de Baidu]({% image_buster /assets/img_archive/baidu_login_dialog.png %}){: style="max-width:70%;"}

Introduce tu nombre de usuario, número de teléfono y contraseña en la página de creación de cuenta. A continuación, haz clic en el botón para recibir el código de verificación. Recibirás un mensaje SMS de Baidu con un código de verificación. Por último, acepta el acuerdo de licencia y haz clic en **注册** (crear cuenta) para registrarte. Si estos pasos de configuración fallan, intenta registrarte a través del inicio de sesión de Baidu Cloud como se describe en este [artículo de inicio de sesión](https://www.adchina.io/how-to-open-a-baidu-account-outside-china/).

![Página de registro de Baidu]({% image_buster /assets/img_archive/baidu_signup.png %}){: style="max-width:80%;"}

## Paso 2: Registrarse como desarrollador de Baidu {#step-2-register-as-a-baidu-developer}

A continuación, debes registrarte como desarrollador de Baidu. Primero, visita el [portal de desarrolladores de Baidu](http://developer.baidu.com/) y elige **注册** (crear nueva cuenta de desarrollador) para comenzar el registro.

![Portal de desarrolladores de Baidu]({% image_buster /assets/img_archive/baidu_dev_portal.png %})

En la página de registro, elige tu tipo de cuenta (个人 para personal, 公司 para empresa) y el tipo de desarrollador (desarrollador está preseleccionado y es correcto para la mayoría de los casos). Introduce tu nombre, una biografía y un número de teléfono con el código de país entre paréntesis (por ejemplo, (1)xxxxxxxxxx). Haz clic en **发送验证码** (enviar código de verificación) e introduce el código de verificación en la siguiente línea. Los dos campos siguientes, sitio web del desarrollador y logotipo del desarrollador, son opcionales. Acepta el acuerdo de licencia y haz clic en **提交** (enviar) para completar el envío. Ahora tienes una cuenta de desarrollador de Baidu.

![Página de registro de desarrollador de Baidu]({% image_buster /assets/img_archive/baidu_dev_reg.png %})

## Paso 3: Registra tu aplicación con Baidu {#step-3-register-your-application-with-baidu}

Para registrar tu aplicación con Baidu, visita el [portal de proyectos de Baidu](http://developer.baidu.com/console#app/project) y haz clic en **创建工程** (crear proyecto).

![Portal de proyectos de Baidu]({% image_buster /assets/img_archive/baidu_project.png %})

En la página siguiente, introduce el nombre de tu aplicación. Las dos casillas de verificación siguientes sirven para activar servicios adicionales de Baidu. En la mayoría de los casos, deben dejarse en blanco.

![Página de nombre de la aplicación en Baidu]({% image_buster /assets/img_archive/baidu_app_name.png %})

Una vez configurada tu aplicación, accederás a una consola que muestra información sobre tu aplicación, incluida la clave de API. A continuación, navega a **云推送** (push en la nube) en la barra lateral. En la página siguiente, haz clic en **推送设置** (configurar push).

![Consola de la aplicación en Baidu]({% image_buster /assets/img_archive/baidu_app_console.png %})

![Página de continuación en Baidu]({% image_buster /assets/img_archive/baidu_continue.png %})

En la página siguiente, introduce el nombre del paquete de tu aplicación (por ejemplo, `com.braze.sample`) y especifica si deseas almacenar mensajes en caché y, de ser así, durante cuánto tiempo (en horas). Esto indica a Baidu durante cuánto tiempo debe seguir intentando enviar mensajes a usuarios sin conexión. Haz clic en **保存设置** (guardar configuración) para guardar.

![Página de configuración de push en la nube de Baidu]({% image_buster /assets/img_archive/baidu_configure_cloud.png %})

## Paso 4: Añadir Baidu a tu aplicación {#step-4-add-baidu-to-your-application}

Visita el [portal del SDK push de Baidu](http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk) y descarga el SDK más reciente de Baidu Cloud Push para Android.

![Portal del SDK de Baidu]({% image_buster /assets/img_archive/baidu_sdk.png %})

Dentro del SDK, encontrarás el archivo jar del servicio push y las bibliotecas nativas específicas de cada plataforma. Intégralas en tu proyecto. Asegúrate de que tu aplicación apunte a la versión más alta del SDK actualmente compatible con Baidu. Esta documentación está actualizada para la versión `4.6.2.38` del SDK de Baidu Cloud Push para Android.

Añade los siguientes permisos requeridos de Baidu al archivo `AndroidManifest.xml` de tu aplicación.

```xml
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
    <uses-permission android:name="android.permission.WRITE_SETTINGS" />
    <uses-permission android:name="android.permission.VIBRATE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.DISABLE_KEYGUARD" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
```

La biblioteca de Baidu contiene receptores de difusión que gestionan los mensajes push entrantes. Declara los receptores internos de Baidu en el archivo `AndroidManifest.xml` de tu aplicación dentro del elemento `<application>`.

```xml
  <!-- 用于接收系统消息以保证 PushService 正常运行 -->
      <receiver
        android:name="com.baidu.android.pushservice.PushServiceReceiver"
        android:process=":bdservice_v1">
        <intent-filter>
          <action android:name="android.intent.action.BOOT_COMPLETED"/>
          <action android:name="android.net.conn.CONNECTIVITY_CHANGE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.SHOW"/>
          <action android:name="com.baidu.android.pushservice.action.media.CLICK"/>
        </intent-filter>
      </receiver>
      <!-- Push 服务接收客户端发送的各种请求-->
      <!-- 注意:RegistrationReceiver 在 2.1.1 及之前版本有拼写失误,为 RegistratonReceiver ,用 新版本 SDK 时请更改为如下代码-->
      <receiver
        android:name="com.baidu.android.pushservice.RegistrationReceiver"
        android:process=":bdservice_v1">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.METHOD"/>
          <action android:name="com.baidu.android.pushservice.action.BIND_SYNC"/>
        </intent-filter>
        <intent-filter>
          <action android:name="android.intent.action.PACKAGE_REMOVED"/>
          <data android:scheme="package"/>
        </intent-filter>
      </receiver>
      <!-- Push 服务 -->
      <!-- 注意:在 4.0 (包含)之后的版本需加上如下所示的 intent-filter action -->
      <service
        android:name="com.baidu.android.pushservice.PushService"
        android:exported="true"
        android:process=":bdservice_v1">
        <intent-filter >
          <action android:name="com.baidu.android.pushservice.action.PUSH_SERVICE"/>
        </intent-filter>
      </service>
```

También necesitarás crear un receptor de difusión que escuche los mensajes push y las notificaciones entrantes. Declara tu receptor en el archivo `AndroidManifest.xml` de tu aplicación dentro del elemento `<application>`. Este receptor deberá extender `com.baidu.android.pushservice.PushMessageReceiver` e implementar métodos que reciban actualizaciones de eventos del servicio push de Baidu.

```xml
      <receiver android:name=".MyPushMessageReceiver">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.MESSAGE"/>
          <action android:name="com.baidu.android.pushservice.action.RECEIVE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.CLICK"/>
        </intent-filter>
      </receiver>
```

En el método `onCreate()` de tu actividad principal, añade la siguiente línea, que registrará tu aplicación con Baidu y comenzará a escuchar mensajes push entrantes. Asegúrate de reemplazar "Your-API-Key" con la clave de API de Baidu de tu proyecto.

```
PushManager.startWork(getApplicationContext(), PushConstants.LOGIN_TYPE_API_KEY, "Your-API-Key");
```

Por último, necesitarás registrar a tus usuarios con Braze. En el método `onBind()` del receptor de difusión de Baidu que creaste en este paso, envía el `channelId` a Braze usando `Braze.registerAppboyPushMessages(channelId)`.

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).setRegisteredPushToken(channelId);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).setRegisteredPushToken(channelId)
```

{% endtab %}
{% endtabs %}

## Paso 5: Registrar las aperturas de push {#step-5-registering-push-opens}

Baidu admite el envío de pares clave-valor adicionales con mensajes push en formato JSON. El método `public void onNotificationClicked(Context context, String title, String description, String customContentString)` de tu receptor de difusión se llamará cada vez que un usuario haga clic en un mensaje push entrante. El parámetro `customContentString` contiene los extras en formato JSON. Todos los mensajes de Braze contendrán los siguientes dos pares clave-valor:

  ```json
  {
    "source": "Appboy",
    "cid": "your-campaign-Id"
  }
  ```

Cada vez que se llame a `onNotificationClicked` en tu receptor de Baidu, tu receptor debe enviar un [Intent](http://developer.android.com/reference/android/content/Intent.html) a tu aplicación que contenga `customContentString`. Tu aplicación registrará el clic en Braze utilizando el `customContentString`.

El siguiente código de ejemplo pasa `customContentString` a Braze y registra un clic:

{% tabs %}
{% tab JAVA %}

  ```java
  String customContentString = intent.getStringExtra(ChinaPushMessageReceiver.NOTIFICATION_CLICKED_KEY);
  BrazeNotificationUtils.logBaiduNotificationClick(mApplicationContext, customContentString);
  ```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val customContentString = intent.getStringExtra(ChinaPushMessageReceiver.NOTIFICATION_CLICKED_KEY)
BrazeNotificationUtils.logBaiduNotificationClick(context, customContentString)
```

{% endtab %}
{% endtabs %}

## Paso 6: Extras {#step-6-extras}

Aparte de las claves reservadas utilizadas por Braze, el parámetro `customContentString` también contendrá todos los pares clave-valor personalizados definidos por el usuario. Para extraer tus pares clave-valor, envuelve `customContentString` en un JSONObject y recupera tus extras:

{% tabs %}
{% tab JAVA %}

```java
try {
  JSONObject myExtras = new JSONObject(customContentString);
  String myValue = myExtras.optString("my_key", null);
} catch (Exception e) {
  Log.e(TAG, "Caught an exception processing customContentString");
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
try {
  val myExtras = JSONObject(customContentString)
  val myValue = myExtras.optString("my_key", null)
} catch (e: Exception) {
  Log.e(TAG, "Caught an exception processing customContentString", e)
}
```

{% endtab %}
{% endtabs %}

## Paso 7: Configurar las claves de Baidu {#step-7-set-up-baidu-keys}

Necesitas introducir tu clave de API de Baidu y tu clave secreta de Baidu en el panel de Braze. Ambas claves están disponibles en la consola de aplicaciones de Baidu.

En la página **Administrar configuración**, selecciona tu aplicación Android China e introduce tu clave de API de Baidu y tu clave secreta de Baidu en la sección de notificaciones push.

![Clave de API de Baidu]({% image_buster /assets/img_archive/baidu_api_key.png %} "APIKey"){: style="max-width:80%;"}

## Recursos adicionales {#additional-resources}

- [Portal de Baidu](https://www.baidu.com/)
- [Portal para desarrolladores de Baidu](http://developer.baidu.com/)
- [Portal de proyectos de Baidu](http://developer.baidu.com/console#app/project)
- [Portal del SDK push de Baidu](http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk)
- [Documentación de integración de Baidu](http://developer.baidu.com/wiki/index.php?title=docs/frontia/guide-android/overview)