## Integración del SDK de Android {#integrating-the-android-sdk}

### Paso 1: Actualiza tu configuración de compilación de Gradle {#step-1-update-your-gradle-build-configuration}

En la configuración del repositorio de tu proyecto (por ejemplo, `settings.gradle`, `settings.gradle.kts` o el `build.gradle` de nivel superior), añade [`mavenCentral()`](https://docs.gradle.org/current/kotlin-dsl/gradle/org.gradle.api.artifacts.dsl/-repository-handler/maven-central.html) a tu lista de repositorios. Esta sintaxis es la misma tanto para Groovy como para Kotlin DSL.

```groovy
repositories {
  mavenCentral()
}
```

A continuación, añade Braze a tus dependencias. En los siguientes ejemplos, sustituye `SDK_VERSION` por la versión actual de tu SDK de Android Braze. Para ver la lista completa de versiones, consulta [Registro de cambios]({{site.baseurl}}/developer_guide/changelogs/?sdktab=android).

{% alert note %}
- Para Kotlin DSL (`build.gradle.kts`), utiliza la sintaxis `implementation("...")`.
- Para Groovy (`build.gradle`), utiliza la sintaxis `implementation '...'`.
- Para [catálogos de versiones](https://developer.android.com/build/migrate-to-catalogs), añade entradas a tu archivo `gradle/libs.versions.toml` y haz referencia a ellas utilizando los accesores generados.
{% endalert %}

{% tabs local %}
{% tab base only %}
Si no tienes pensado utilizar los componentes de la interfaz de usuario de Braze, añade lo siguiente a tus dependencias.

{% subtabs local %}
{% subtab Groovy %}
```groovy
dependencies {
    implementation 'com.braze:android-sdk-base:SDK_VERSION' // (Required) Adds dependencies for the base Braze SDK.
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Kotlin DSL %}
```kotlin
dependencies {
    implementation("com.braze:android-sdk-base:SDK_VERSION") // (Required) Adds dependencies for the base Braze SDK.
    implementation("com.braze:android-sdk-location:SDK_VERSION") // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Version catalog %}
En tu archivo `gradle/libs.versions.toml`:

```toml
[versions]
braze = "SDK_VERSION"

[libraries]
braze-android-sdk-base = { group = "com.braze", name = "android-sdk-base", version.ref = "braze" }
braze-android-sdk-location = { group = "com.braze", name = "android-sdk-location", version.ref = "braze" }
```

A continuación, en tu archivo `build.gradle` o `build.gradle.kts`, añade las siguientes dependencias. Esta sintaxis es la misma tanto para Groovy como para Kotlin DSL.

```groovy
dependencies {
    implementation(libs.braze.android.sdk.base) // (Required) Adds dependencies for the base Braze SDK.
    implementation(libs.braze.android.sdk.location) // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab with ui components %}
Si tienes pensado utilizar los componentes de la interfaz de usuario de Braze, añade lo siguiente a tus dependencias.

{% subtabs local %}
{% subtab Groovy %}
```groovy
dependencies {
    implementation 'com.braze:android-sdk-ui:SDK_VERSION' // (Required) Adds dependencies for the Braze SDK and Braze UI components.
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Kotlin DSL %}
```kotlin
dependencies {
    implementation("com.braze:android-sdk-ui:SDK_VERSION") // (Required) Adds dependencies for the Braze SDK and Braze UI components.
    implementation("com.braze:android-sdk-location:SDK_VERSION") // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Version catalog %}
En tu archivo `gradle/libs.versions.toml`:

```toml
[versions]
braze = "SDK_VERSION"

[libraries]
braze-android-sdk-ui = { group = "com.braze", name = "android-sdk-ui", version.ref = "braze" }
braze-android-sdk-location = { group = "com.braze", name = "android-sdk-location", version.ref = "braze" }
```

A continuación, en tu archivo `build.gradle` o `build.gradle.kts`, añade las siguientes dependencias. Esta sintaxis es la misma tanto para Groovy como para Kotlin DSL.

```groovy
dependencies {
    implementation(libs.braze.android.sdk.ui) // (Required) Adds dependencies for the Braze SDK and Braze UI components.
    implementation(libs.braze.android.sdk.location) // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Paso 2: Configura tu `braze.xml` {#step-2-configure-your-brazexml}

{% alert note %}
A partir de diciembre de 2019, ya no se proporcionan endpoints personalizados; si tienes un endpoint personalizado preexistente, puedes seguir utilizándolo. Para más detalles, consulta nuestra <a href="{{site.baseurl}}/api/basics/#endpoints">lista de endpoints disponibles</a>.
{% endalert %}

Crea un archivo `braze.xml` en la carpeta `res/values` de tu proyecto. Si estás en un clúster de datos específico o tienes un endpoint personalizado preexistente, también necesitas especificar el endpoint en tu archivo `braze.xml`.

El contenido de ese archivo debe parecerse al siguiente fragmento de código. Asegúrate de sustituir `YOUR_APP_IDENTIFIER_API_KEY` por el identificador que se encuentra en la página **Administrar configuración** del panel de Braze. Inicia sesión en [dashboard.braze.com](https://dashboard.braze.com) para encontrar la [dirección de tu clúster]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints).

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

### Paso 3: Añade permisos a `AndroidManifest.xml` {#step-3-add-permissions-to-androidmanifestxml}

A continuación, añade los siguientes permisos a tu `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert note %}
Con el lanzamiento de Android M, Android pasó de un modelo de permisos en tiempo de instalación a un modelo de permisos en tiempo de ejecución. Sin embargo, ambos permisos son normales y se conceden automáticamente si figuran en el manifiesto de la aplicación. Para más información, visita la [documentación sobre permisos](https://developer.android.com/training/permissions/index.html) de Android.
{% endalert %}

### Paso 4: Habilita la inicialización diferida (opcional) {#step-4-enable-delayed-initialization-optional}

Para utilizar la inicialización diferida, se requiere la versión mínima del SDK de Braze:

{% sdk_min_versions android:38.0.0 %}

{% alert note %}
Mientras la inicialización diferida está habilitada, todas las conexiones de red se cancelan, lo que impide que el SDK envíe datos a los servidores de Braze.
{% endalert %}

#### Paso 4.1: Actualiza tu `braze.xml` {#step-41-update-your-brazexml}

La inicialización diferida está desactivada de forma predeterminada. Para habilitarla, utiliza una de las siguientes opciones:

{% tabs %}
{% tab Braze XML file %}
En el archivo `braze.xml` de tu proyecto, establece `com_braze_enable_delayed_initialization` en `true`.

```xml
<bool name="com_braze_enable_delayed_initialization">true</bool>
```
{% endtab %}

{% tab At runtime %}
Para habilitar la inicialización diferida en tiempo de ejecución, utiliza el siguiente método.

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert note %}
Cuando la inicialización diferida está habilitada y una notificación push contiene una acción de vínculo profundo, el vínculo profundo no se resuelve.
{% endalert %}

#### Paso 4.2: Configura los análisis push (opcional) {#step-42-configure-push-analytics-optional}

Cuando la inicialización diferida está habilitada, los análisis push se ponen en cola de forma predeterminada. Sin embargo, puedes optar por [poner en cola explícitamente](#explicitly-queue-push-analytics) o [descartar](#drop-push-analytics) los análisis push.

##### Cola explícita {#explicitly-queue-push-analytics}

Para poner explícitamente en cola los análisis push, elige una de las siguientes opciones:

{% tabs %}
{% tab Braze XML file %}
En tu archivo `braze.xml`, establece `com_braze_delayed_initialization_analytics_behavior` como `QUEUE`:

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">QUEUE</string>
```
{% endtab %}

{% tab At runtime %}
Añade `QUEUE` a tu método [`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html):

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

##### Descartar {#drop-push-analytics}

Para descartar los análisis push, elige una de las siguientes opciones:

{% tabs %}
{% tab Braze XML file %}
En tu archivo `braze.xml`, establece `com_braze_delayed_initialization_analytics_behavior` como `DROP`:

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">DROP</string>
```
{% endtab %}

{% tab At runtime %}
Añade `DROP` al método [`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html):

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### Paso 4.3: Inicializa manualmente el SDK {#step-43-manually-initialize-the-sdk}

Tras el periodo de retraso elegido, utiliza el método [`Braze.disableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-delayed-initialization.html) para inicializar manualmente el SDK.

{% tabs local %}
{% tab JAVA %}

```java
Braze.disableDelayedInitialization(context);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.disableDelayedInitialization(context)
```

{% endtab %}
{% endtabs %}

### Paso 5: Habilita el seguimiento de sesiones de usuario {#step-5-enable-user-session-tracking}

Cuando habilitas el seguimiento de sesiones de usuario, las llamadas a `openSession()`, `closeSession()`, [`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html) y el registro de `InAppMessageManager` se pueden gestionar automáticamente.

Para registrar las devoluciones de llamada del ciclo de vida de la actividad, añade el siguiente código al método `onCreate()` de tu clase `Application`.

{% tabs local %}
{% tab JAVA %}

```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
  }
}
```

Para ver la lista de parámetros disponibles, consulta [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html).

{% endtab %}
{% endtabs %}

## Probar el seguimiento de sesiones {#testing-session-tracking}

{% alert tip %}
También puedes utilizar el [depurador del SDK]({{site.baseurl}}/developer_guide/debugging) para diagnosticar problemas relacionados con el SDK.
{% endalert %}

Si experimentas problemas durante las pruebas, habilita [el registro detallado](#android_enabling-logs) y, a continuación, utiliza logcat para detectar llamadas `openSession` y `closeSession` que faltan en tus actividades.

1. En Braze, ve a **Overview**, selecciona tu aplicación y, a continuación, en el menú desplegable **Display Data For**, selecciona **Today**.
    ![La página "Overview" de Braze, con el campo "Display Data For" configurado en "Today".]({% image_buster /assets/img_archive/android_sessions.png %})
2. Abre tu aplicación y actualiza el panel de Braze. Comprueba que tus métricas hayan aumentado en 1.
3. Navega por tu aplicación y comprueba que solo se ha registrado una sesión en Braze.
4. Envía la aplicación al segundo plano durante al menos 10 segundos y, a continuación, vuelve a ponerla en primer plano. Verifica que se haya registrado una nueva sesión.

## Configuraciones opcionales {#optional-configurations}

### Configuración en tiempo de ejecución {#runtime-configuration}

Para configurar las opciones de Braze en el código en lugar de en el archivo `braze.xml`, utiliza [la configuración en tiempo de ejecución](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html). Si existe un valor en ambos lugares, se utilizará el valor en tiempo de ejecución. Una vez que se haya proporcionado toda la configuración necesaria en tiempo de ejecución, puedes eliminar tu archivo `braze.xml`.

En el siguiente ejemplo, se crea un [objeto constructor](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) y luego se pasa a [`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html). Ten en cuenta que solo se muestran algunas de las opciones de tiempo de ejecución disponibles&#8212;consulta nuestro [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html) para ver la lista completa.

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

{% alert tip %}
¿Buscas otro ejemplo? Echa un vistazo a nuestra [aplicación de muestra Hello Braze](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/hello-braze/src/main/java/com/braze/helloworld/CustomApplication.java).
{% endalert %}

### ID de publicidad de Google {#google-advertising-id}

El [ID de publicidad de Google (GAID)](https://support.google.com/googleplay/android-developer/answer/6048248/advertising-id?hl=en) es un identificador opcional específico del usuario, anónimo, único y restablecible para fines publicitarios, proporcionado por los servicios de Google Play. GAID ofrece a los usuarios la posibilidad de restablecer su identificador, excluirse voluntariamente de los anuncios basados en intereses dentro de las aplicaciones de Google Play, y proporciona a los desarrolladores un sistema sencillo y estándar para seguir monetizando sus aplicaciones.

El SDK de Braze no recopila automáticamente el ID de publicidad de Google, por lo que debe establecerse manualmente mediante el método [`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html).

{% tabs local %}
{% tab JAVA %}

```java
new Thread(new Runnable() {
  @Override
  public void run() {
    try {
      AdvertisingIdClient.Info idInfo = AdvertisingIdClient.getAdvertisingIdInfo(getApplicationContext());
      Braze.getInstance(getApplicationContext()).setGoogleAdvertisingId(idInfo.getId(), idInfo.isLimitAdTrackingEnabled());
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}).start();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
suspend fun fetchAndSetAdvertisingId(
  context: Context,
  scope: CoroutineScope = GlobalScope
) {
  scope.launch(Dispatchers.IO) {
    try {
      val idInfo = AdvertisingIdClient.getAdvertisingIdInfo(context)
      Braze.getInstance(context).setGoogleAdvertisingId(
        idInfo.id,
        idInfo.isLimitAdTrackingEnabled
      )
    } catch (e: Exception) {
      e.printStackTrace()
    }
  }
}
```

{% endtab %}
{% endtabs %}

{% alert important %}
Google requiere que el ID de publicidad se recopile en un hilo que no sea de interfaz de usuario.
{% endalert %}


### Seguimiento de ubicación {#location-tracking}

Para habilitar la recopilación de ubicación de Braze, configura `com_braze_enable_location_collection` en `true` en tu archivo `braze.xml`:

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
A partir de la versión 3.6.0 del SDK de Braze para Android, la recopilación de ubicación de Braze está desactivada de forma predeterminada.
{% endalert %}

### Registro {#logging}

De forma predeterminada, el nivel de registro del SDK de Braze para Android está configurado en `INFO`. Puedes [suprimir estos registros](#android_suppressing-logs) o [establecer un nivel de registro diferente](#android_enabling-logs), como `VERBOSE`, `DEBUG` o `WARN`.

#### Habilitar registros {#enabling-logs}

Para ayudar a solucionar problemas en tu aplicación o reducir los tiempos de respuesta con el soporte de Braze, puedes habilitar los registros detallados para el SDK. Cuando envíes registros detallados al soporte de Braze, asegúrate de que empiezan en cuanto inicias la aplicación y terminan mucho después de que se produzca el problema. Para obtener un resumen centralizado, consulta [Registro detallado]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging). Para aprender a interpretar la salida del registro, consulta [Lectura de registros detallados]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs).

Ten en cuenta que los registros detallados solo están pensados para tu entorno de desarrollo, por lo que deberás desactivarlos antes de publicar tu aplicación.

{% alert important %}
Habilita los registros detallados antes de cualquier otra llamada en `Application.onCreate()` para asegurarte de que tus registros son lo más completos posible.
{% endalert %}

{% tabs local %}
{% tab Application %}
Para habilitar los registros directamente en tu aplicación, añade lo siguiente al método `onCreate()` de tu aplicación antes de cualquier otro método.

{% subtabs local %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.MIN_LOG_LEVEL);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.MIN_LOG_LEVEL
```
{% endsubtab %}
{% endsubtabs %}

Sustituye `MIN_LOG_LEVEL` por la **Constante** del nivel de registro que quieras establecer como nivel mínimo de registro. Cualquier registro en un nivel `>=` a tu `MIN_LOG_LEVEL` configurado se reenviará al método predeterminado de Android [`Log`](https://developer.android.com/reference/android/util/Log). Se descartará cualquier registro `<` a tu `MIN_LOG_LEVEL` configurado.

| Constante   | Valor          | Descripción                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | Registra los mensajes más detallados para depuración y desarrollo.            |
| `DEBUG`     | 3              | Registra mensajes descriptivos para depuración y desarrollo.                  |
| `INFO`      | 4              | Registra mensajes informativos para los aspectos generales destacados.                       |
| `WARN`      | 5              | Registra mensajes de advertencia para identificar situaciones potencialmente perjudiciales.     |
| `ERROR`     | 6              | Registra mensajes de error para indicar fallos de la aplicación o problemas graves. |
| `ASSERT`    | 7              | Registra mensajes de aserción cuando las condiciones son falsas durante el desarrollo.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Habilitar registros" }

Por ejemplo, el siguiente código reenviará los niveles de registro `2`, `3`, `4`, `5`, `6` y `7` al método `Log`.

{% subtabs local %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.VERBOSE);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.VERBOSE
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab xml %}
Para habilitar los registros en `braze.xml`, añade lo siguiente a tu archivo:

```xml
<integer name="com_braze_logger_initial_log_level">MIN_LOG_LEVEL</integer>
```

Sustituye `MIN_LOG_LEVEL` por el **Valor** del nivel de registro que quieras establecer como nivel de registro mínimo. Cualquier registro en un nivel `>=` a tu `MIN_LOG_LEVEL` configurado se reenviará al método predeterminado de Android [`Log`](https://developer.android.com/reference/android/util/Log). Se descartará cualquier registro `<` a tu `MIN_LOG_LEVEL` configurado.

| Constante   | Valor          | Descripción                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | Registra los mensajes más detallados para depuración y desarrollo.            |
| `DEBUG`     | 3              | Registra mensajes descriptivos para depuración y desarrollo.                  |
| `INFO`      | 4              | Registra mensajes informativos para los aspectos generales destacados.                       |
| `WARN`      | 5              | Registra mensajes de advertencia para identificar situaciones potencialmente perjudiciales.     |
| `ERROR`     | 6              | Registra mensajes de error para indicar fallos de la aplicación o problemas graves. |
| `ASSERT`    | 7              | Registra mensajes de aserción cuando las condiciones son falsas durante el desarrollo.     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Habilitar registros" }

Por ejemplo, el siguiente código reenviará los niveles de registro `2`, `3`, `4`, `5`, `6` y `7` al método `Log`.

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```
{% endtab %}
{% endtabs %}

#### Verificar registros detallados {#verifying-verbose-logs}

Para verificar que tus registros están configurados en `VERBOSE`, comprueba si `V/Braze` aparece en algún lugar de tus registros. Si lo hace, es que se han habilitado correctamente los registros detallados. Por ejemplo:

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

#### Suprimir registros {#suppressing-logs}

Para suprimir todos los registros del SDK de Braze para Android, establece el nivel de registro en `BrazeLogger.SUPPRESS` en el método `onCreate()` de tu aplicación _antes que_ cualquier otro método.

{% tabs local %}
{% tab JAVA %}
```java
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS);
```
{% endtab %}

{% tab KOTLIN %}
```kotlin
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS)
```
{% endtab %}
{% endtabs %}

### Múltiples claves de API {#multiple-api-keys}

El caso de uso más común para múltiples claves de API es separar las claves de API para las variantes de compilación de depuración y de lanzamiento.

Para cambiar fácilmente entre varias claves de API en tus compilaciones, te recomendamos crear un archivo `braze.xml` distinto para cada [variante de compilación](https://developer.android.com/studio/build/build-variants.html) relevante. Una variante de compilación es una combinación del tipo de compilación y la variante de producto. De forma predeterminada, los nuevos proyectos de Android se configuran con [los tipos de compilación `debug` y `release`](https://developer.android.com/reference/tools/gradle-api/8.3/null/com/android/build/api/dsl/BuildType) y sin variantes de producto.

Para cada variante de compilación relevante, crea un nuevo `braze.xml` en el directorio `src/<build variant name>/res/values/`. Cuando se compile la variante de compilación, utilizará la nueva clave de API.

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

{% alert tip %}
Para aprender a configurar la clave de API en tu código, consulta [Configuración en tiempo de ejecución]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#runtime-configuration).
{% endalert %}

### TalkBack exclusivo para mensajes dentro de la aplicación {#exclusive-in-app-message-talkback}

En cumplimiento de las [directrices de accesibilidad de Android](https://developer.android.com/guide/topics/ui/accessibility), el SDK de Braze para Android ofrece Android TalkBack de forma predeterminada. Para garantizar que solo se lean en voz alta los contenidos de los mensajes dentro de la aplicación, sin incluir otros elementos de la pantalla como la barra de título de la aplicación o la navegación, puedes habilitar el modo exclusivo de TalkBack.

Para habilitar el modo exclusivo para los mensajes dentro de la aplicación:

{% tabs local %}
{% tab Braze XML %}
```xml
<bool name="com_braze_device_in_app_message_accessibility_exclusive_mode_enabled">true</bool>
```
{% endtab %}

{% tab Kotlin %}
```kotlin
val brazeConfigBuilder = BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```
{% endtab %}

{% tab Java %}
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```
{% endtab %}
{% endtabs %}

### R8 y ProGuard {#r8-and-proguard}

La configuración de [reducción de código](https://developer.android.com/build/shrink-code) se incluye automáticamente con tu integración de Braze.

Las aplicaciones cliente que ofuscan el código de Braze deben almacenar archivos de mapeo de versiones para que Braze pueda interpretar las trazas de pila. Si quieres seguir conservando todo el código de Braze, añade lo siguiente a tu archivo ProGuard:

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```
