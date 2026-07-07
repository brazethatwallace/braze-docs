## Acerca del SDK de Braze para React Native {#about-the-react-native-braze-sdk}

La integración del SDK de React Native Braze proporciona funciones básicas de análisis y te permite integrar mensajes dentro de la aplicación y Content Cards tanto para iOS como para Android con un solo código base.

## Compatibilidad con la nueva arquitectura {#new-architecture-compatibility}

La siguiente versión mínima del SDK es compatible con todas las aplicaciones que utilizan [la nueva arquitectura de React Native](https://reactnative.dev/docs/the-new-architecture/landing-page):

{% sdk_min_versions reactnative:2.0.1 %}

A partir de la versión 6.0.0 del SDK, Braze utiliza un módulo React Native Turbo, que es compatible tanto con la nueva arquitectura como con la arquitectura puente heredada. Esto significa que no se requiere ninguna configuración adicional.

{% alert warning %}
Si tu aplicación iOS cumple con `RCTAppDelegate` y sigue nuestra configuración `AppDelegate` anterior, revisa los ejemplos en [Configuración nativa completa](#reactnative_step-2-complete-native-setup) para evitar que se produzcan fallos al suscribirte a eventos en el módulo Turbo.
{% endalert %}

## Requisitos de versión de React y React Native {#react-and-react-native-version-requirements}

Braze no publica versiones mínimas de React independientes más allá de lo que admite el SDK de React Native. Para integrar el SDK, usa React Native versión 0.71 o posterior. Para ver la lista completa de versiones de React Native compatibles, consulta el [repositorio GitHub del SDK de React Native](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support).

Cuando actualices React, React Native o el SDK de Braze, revisa el [CHANGELOG](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md) del SDK en busca de cambios incompatibles antes de desplegar.

## Integración del SDK de React Native {#integrating-the-react-native-sdk}

### Requisitos previos {#prerequisites}

Para las versiones de React Native compatibles y orientación sobre actualizaciones, consulta [Requisitos de versión de React y React Native](#react-and-react-native-version-requirements).

### Paso 1: Integrar la biblioteca de Braze {#step-1-integrate-the-braze-library}

{% tabs local %}
{% tab npm %}
```bash
npm install @braze/react-native-sdk
```
{% endtab %}
{% tab yarn %}
```bash
yarn add @braze/react-native-sdk
```
{% endtab %}
{% endtabs %}

<a id="step-2-choose-a-setup-option"></a>
<a id="reactnative_step-2-complete-native-setup"></a>
### Paso 2: Configuración nativa completa {#step-2-complete-native-setup}

Si tu aplicación usa Expo, consulta [Uso del plugin Expo](#reactnative-using-the-expo-plugin). Si tu aplicación usa React Native puro, consulta [Uso de React Native CLI](#reactnative-using-react-native-cli).
Elige un método de configuración en cada pestaña de versión: plugin Expo o React Native CLI.

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

#### Método 1: Uso del plugin Expo {#reactnative-using-the-expo-plugin}

##### 2.1 Instala el plugin Braze Expo {#21-install-the-braze-expo-plugin}

Asegúrate de que tu versión del plugin Braze Expo sea al menos 4.1.0. Para ver la lista completa de versiones compatibles, consulta el [repositorio del plugin Braze Expo](https://github.com/braze-inc/braze-expo-plugin?tab=readme-ov-file#version-support).

El siguiente fragmento de código muestra el comando para instalar el plugin Braze Expo:

```bash
npx expo install @braze/expo-plugin
```

##### 2.2 Añade el plugin a tu app.json {#22-add-the-plugin-to-your-appjson}

En tu `app.json`, añade el plugin Braze Expo. La clave de API y el punto de conexión ya no se configuran aquí. Proporciónalos en tiempo de ejecución a través de `Braze.initialize()` desde JavaScript. Añade los siguientes parámetros de configuración opcionales según las necesidades de tu implementación:

| Método                                        | Tipo    | Descripción                                                                                                                                              |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enableBrazeIosPush`                          | boolean | Solo para iOS. Si se utiliza Braze para gestionar las notificaciones push en iOS.                       |
| `enableFirebaseCloudMessaging`                | boolean | Solo para Android. Si se utiliza Firebase Cloud Messaging para las notificaciones push.             |
| `firebaseCloudMessagingSenderId`              | string  | Solo para Android. Tu ID de remitente de Firebase Cloud Messaging.                                    |
| `sessionTimeout`                              | integer | El tiempo de espera de la sesión de Braze para tu aplicación en segundos.                                                                                               |
| `enableSdkAuthentication`                     | boolean | Si se habilita la característica de [Autenticación SDK]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication/#sdk-authentication).      |
| `logLevel`                                    | integer | El nivel de registro de tu aplicación. El nivel de registro predeterminado es 8 y registra la información mínima. Para habilitar el registro detallado para la depuración, utiliza el nivel de registro 0.    |
| `minimumTriggerIntervalInSeconds`             | integer | El intervalo de tiempo mínimo en segundos entre desencadenamientos. Predeterminado a 30 segundos.                                                                           |
| `enableAutomaticLocationCollection`           | boolean | Si está habilitada la recopilación automática de ubicaciones (si el usuario lo permite).                                                                                  |
| `enableGeofence`                              | boolean | Si están habilitadas las geovallas.                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | boolean | Si las solicitudes de geovalla deben hacerse automáticamente.                                                                                                  |
| `dismissModalOnOutsideTap`                    | boolean | Solo para iOS. Si un mensaje modal dentro de la aplicación se descarta cuando el usuario hace clic fuera del mensaje dentro de la aplicación.                                           |
| `androidHandlePushDeepLinksAutomatically`     | boolean | Solo para Android. Si el SDK de Braze debe gestionar automáticamente los vínculos profundos push.                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | boolean | Solo para Android. Establece si el contenido de texto de una notificación push debe ser interpretado y renderizado como HTML utilizando `android.text.Html.fromHtml`.        |
| `androidNotificationAccentColor`              | string  | Solo para Android. Establece el color de acento de las notificaciones de Android.                                                                                                |
| `androidNotificationLargeIcon`                | string  | Solo para Android. Establece el icono grande de notificación de Android.                                                                                                  |
| `androidNotificationSmallIcon`                | string  | Solo para Android. Establece el icono pequeño de notificación de Android.                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | boolean | Solo para iOS. Si se debe pedir automáticamente al usuario permisos push al iniciar la aplicación.                                                          |
| `enableBrazeIosRichPush`                      | boolean | Solo para iOS. Si se habilitan las características de notificaciones push enriquecidas para iOS.                                                                                                  |
| `enableBrazeIosPushStories`                   | boolean | Solo para iOS. Si se habilitan las Push Stories de Braze para iOS.                                                                                                  |
| `iosPushStoryAppGroup`                        | string  | Solo para iOS. El grupo de aplicaciones utilizado para las Push Stories de iOS.                                                                                                       |
| `iosUseUUIDAsDeviceId`                        | boolean | Solo para iOS. Si el ID del dispositivo utiliza un UUID generado aleatoriamente.                                                                                       |
| `iosForwardUniversalLinks`                    | boolean | Solo para iOS. Especifica si el SDK debe reconocer y reenviar automáticamente los enlaces universales a los métodos del sistema (predeterminado: `false`). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="2.2 Añade el plugin a tu app.json" }

El siguiente fragmento de código muestra un ejemplo de configuración de `app.json`:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "sessionTimeout": 60,
          "enableGeofence": false,
          "enableBrazeIosPush": false,
          "enableFirebaseCloudMessaging": false,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true,
          "enableSdkAuthentication": false,
          "logLevel": 0,
          "minimumTriggerIntervalInSeconds": 0,
          "enableAutomaticLocationCollection": false,
          "enableAutomaticGeofenceRequests": false,
          "dismissModalOnOutsideTap": true,
          "androidPushNotificationHtmlRenderingEnabled": true,
          "androidNotificationAccentColor": "#ff3344",
          "androidNotificationLargeIcon": "@drawable/custom_app_large_icon",
          "androidNotificationSmallIcon": "@drawable/custom_app_small_icon",
          "iosRequestPushPermissionsAutomatically": false,
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.example.myapp.PushStories",
          "iosForwardUniversalLinks": false
        }
      ]
    ]
  }
}
```

###### Configuración de los iconos de notificaciones push en Android {#android-push-icons}

Cuando utilices `androidNotificationLargeIcon` y `androidNotificationSmallIcon`, sigue estas prácticas recomendadas para que los iconos se muestren correctamente:

**Ubicación y formato de los iconos**

Para utilizar iconos de notificaciones push personalizados con el plugin Braze Expo:

1. Crea tus archivos de iconos siguiendo los requisitos de iconos que se detallan a continuación.
2. Colócalos en los directorios nativos de Android de tu proyecto en `android/app/src/main/res/drawable-<density>/`.
   Por ejemplo, usa `android/app/src/main/res/drawable-mdpi/` y `android/app/src/main/res/drawable-hdpi/`.
3. Como alternativa, si administras activos en tu directorio React Native, puedes utilizar la [configuración de iconos de app.json](https://docs.expo.dev/versions/latest/config/app/#icon) de Expo o crear un [plugin de configuración de Expo](https://docs.expo.dev/config-plugins/introduction/) para copiar los iconos a las carpetas drawable de Android durante la precompilación.

El plugin Braze Expo hace referencia a estos iconos utilizando el sistema de recursos drawable de Android.

**Requisitos de los iconos**

- **Icono pequeño:** Debe ser una silueta blanca sobre un fondo transparente (este es un requisito de la plataforma Android).
- **Icono grande:** Puede ser una imagen a todo color.
- **Formato:** Se recomienda el formato PNG.
- **Nomenclatura:** Utiliza solo letras minúsculas, números y guiones bajos (por ejemplo, `my_large_icon.png`).

**Configuración en app.json**

El siguiente fragmento de código muestra cómo hacer referencia a los iconos de notificación de Android en `app.json` usando el prefijo `@drawable/`:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidNotificationLargeIcon": "@drawable/large_icon",
          "androidNotificationSmallIcon": "@drawable/small_icon"
        }
      ]
    ]
  }
}
```

{% alert important %}
No utilices rutas de archivo relativas (como `src/assets/images/icon.png`) ni incluyas la extensión del archivo al hacer referencia a los iconos. El plugin Expo requiere el prefijo `@drawable/` para ubicar correctamente los iconos en las carpetas nativas de Android después del proceso de precompilación.
{% endalert %}

**Cómo funciona**

El plugin Braze Expo hace referencia a tus archivos de iconos desde los directorios `drawable` de Android. Cuando ejecutas `npx expo prebuild`, Expo genera la estructura nativa del proyecto Android. Tus iconos deben estar presentes en las carpetas `drawable` de Android (ya sea colocados manualmente o copiados a través de un plugin de configuración) antes del proceso de compilación. A continuación, el plugin configura el SDK de Braze para utilizar estos recursos drawable por sus nombres (sin ruta ni extensión), por lo que es necesario incluir el prefijo `@drawable/` en tu configuración.

Para obtener más información sobre los iconos de notificación de Android, consulta las [directrices sobre iconos de notificación de Android](https://developer.android.com/develop/ui/views/notifications#icon).

##### 2.3 Compila y ejecuta tu aplicación {#23-build-and-run-your-application}

La precompilación de tu aplicación genera los archivos nativos necesarios para que el plugin Braze Expo funcione.

El siguiente fragmento de código muestra el comando para precompilar tu aplicación:

```bash
npx expo prebuild
```

Ejecuta tu aplicación como se especifica en la [documentación de Expo](https://docs.expo.dev/workflow/customizing/). Si realizas cambios en las opciones de configuración, precompila y ejecuta la aplicación de nuevo.

#### Método 2: Uso de React Native CLI {#reactnative-using-react-native-cli}

##### Configurar Android {#set-up-android}

**2.1 Añade el plugin Kotlin Gradle**

El siguiente fragmento de código muestra cómo añadir el plugin Kotlin Gradle en el `build.gradle` de nivel superior de tu proyecto bajo `buildscript` > `dependencies`:

```groovy
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}
```

Esto añade Kotlin a tu proyecto.

**2.2 Configura el SDK de Braze**

Crea un archivo `braze.xml` en la carpeta `res/values` de tu proyecto. La clave de API y el punto de conexión se proporcionan en tiempo de ejecución desde JavaScript, por lo que no son necesarios en este archivo. El siguiente fragmento de código muestra cómo habilitar la inicialización diferida con `com_braze_enable_delayed_initialization`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <bool name="com_braze_enable_delayed_initialization">true</bool>
</resources>
```

{% alert note %}
Aún puedes añadir otros valores de configuración nativos a `braze.xml` (como push, tiempo de espera de sesión y configuración de registro). Estos se aplican automáticamente cuando se llama a `Braze.initialize()` desde JavaScript.
{% endalert %}

El siguiente fragmento de código muestra los permisos necesarios para tu archivo `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
En la versión 12.2.0 o posterior del SDK de Braze para Android, puedes incorporar automáticamente la biblioteca android-sdk-location configurando `importBrazeLocationLibrary=true` en tu archivo `gradle.properties`.
{% endalert %}

**2.3 Implementa el seguimiento de sesión del usuario**

Las llamadas a `openSession()` y `closeSession()` se gestionan automáticamente.
El siguiente fragmento de código muestra qué añadir al método `onCreate()` de tu clase `MainApplication`:

{% subtabs local %}
{% subtab JAVA %}
```java
import com.braze.BrazeActivityLifecycleCallbackListener;

@Override
public void onCreate() {
    super.onCreate();
    ...
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
import com.braze.BrazeActivityLifecycleCallbackListener

override fun onCreate() {
    super.onCreate()
    ...
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
}
```
{% endsubtab %}
{% endsubtabs %}

**2.4 Gestiona las actualizaciones de intención**

Si tu MainActivity tiene `android:launchMode` configurado en `singleTask`, el siguiente fragmento de código muestra qué añadir a tu clase `MainActivity`:

{% subtabs local %}
{% subtab JAVA %}
```java
@Override
public void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    setIntent(intent);
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
override fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    setIntent(intent)
}
```
{% endsubtab %}
{% endsubtabs %}

##### Configurar iOS {#set-up-ios}

**2.5 (Opcional) Configura el Podfile para XCFrameworks dinámicos**

Para importar determinadas bibliotecas de Braze, como BrazeUI, a un archivo Objective-C++, debes utilizar la sintaxis `#import`. A partir de la versión `7.4.0` del SDK Swift de Braze, los binarios tienen un [canal de distribución opcional como XCFrameworks dinámicos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic), que son compatibles con esta sintaxis.

Si quieres utilizar este canal de distribución, anula manualmente las ubicaciones de las fuentes de CocoaPods en tu Podfile. Consulta el ejemplo a continuación y sustituye `{your-version}` por la versión correspondiente que desees importar:

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

**2.6 Instala los pods**

Dado que React Native vincula automáticamente las bibliotecas a la plataforma nativa, puedes instalar el SDK con la ayuda de CocoaPods.

El siguiente fragmento de código muestra cómo instalar los pods desde la carpeta raíz del proyecto:

```bash
# To install using the React Native New Architecture
cd ios && pod install

# To install using the React Native legacy architecture
cd ios && RCT_NEW_ARCH_ENABLED=0 pod install
```

**2.7 Configura el SDK de Braze**

Usa `BrazeReactInitializer.configure` en tu `AppDelegate` para registrar la configuración nativa. Los closures que proporcionas se almacenan y se aplican posteriormente cuando se llama a `Braze.initialize(apiKey, endpoint)` desde JavaScript.

{% subtabs local %}
{% subtab SWIFT %}

El siguiente fragmento de código muestra cómo importar el SDK de Braze en la parte superior del archivo `AppDelegate.swift`:

```swift
import BrazeKit
import braze_react_native_sdk
```

En el método `application(_:didFinishLaunchingWithOptions:)`, registra tu configuración nativa usando `BrazeReactInitializer.configure`. No establezcas la clave de API ni el punto de conexión aquí. Se proporcionan desde JavaScript a través de `Braze.initialize()`.

- **Closure `configure`**: Recibe un `Braze.Configuration` y te permite establecer propiedades de configuración nativas (registro, push, sesiones y más).
- **Closure `postInitialization`** *(opcional)*: Recibe la instancia `Braze` activa después de su creación, para configuraciones que requieren la instancia (por ejemplo, almacenar una referencia o establecer delegados).

El siguiente fragmento de código muestra un ejemplo de implementación de `AppDelegate.swift` que usa `BrazeReactInitializer.configure`:

```swift
@main
class AppDelegate: UIResponder, UIApplicationDelegate {
  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil
  ) -> Bool {
    BrazeReactInitializer.configure { configuration in
      configuration.logger.level = .info
      configuration.push.automation = true
    } postInitialization: { braze in
      AppDelegate.braze = braze
    }

    // ... React Native setup

    return true
  }
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

El siguiente fragmento de código muestra cómo importar el SDK de Braze en la parte superior del archivo `AppDelegate.m`:

```objc
@import BrazeKit;
@import braze_react_native_sdk;
```

En el método `application:didFinishLaunchingWithOptions:`, registra tu configuración nativa usando `BrazeReactInitializer`. No establezcas la clave de API ni el punto de conexión aquí. Se proporcionan desde JavaScript a través de `Braze.initialize()`.

El siguiente fragmento de código muestra un ejemplo de implementación de `AppDelegate.m` que usa `BrazeReactInitializer`:

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [BrazeReactInitializer configure:^(BRZConfiguration *configuration) {
    configuration.logger.level = BRZLoggerLevelInfo;
    configuration.push.automation = [[BRZConfigurationPushAutomation alloc] initWithAutomationEnabled:YES];
  } postInitialization:^(Braze *braze) {
    // Store the Braze instance for later use.
  }];

  /* Other configuration */

  return YES;
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
`BrazeReactInitializer.configure()` solo almacena tu configuración. No existe ninguna instancia de Braze hasta que se llama a `Braze.initialize()` desde JavaScript, por lo que no debes llamar a ningún método del SDK de Braze en el AppDelegate después de `configure()`.
Cuando llamas a `Braze.initialize()` de nuevo, los mismos bloques `configure` y `postInitialization` se aplican a la nueva instancia de Braze.
{% endalert %}

{% endtab %}
{% tab React Native SDK 19.1.0 y anteriores %}

#### Método 1: Uso del plugin Expo {#method-1-using-the-expo-plugin}

##### Paso 2.1: Instala el plugin Braze Expo {#step-21-install-the-braze-expo-plugin}

Asegúrate de que tu versión del SDK de React Native de Braze sea al menos 1.37.0. Para ver la lista completa de versiones compatibles, consulta el [repositorio de Braze React Native](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support).

El siguiente fragmento de código muestra el comando para instalar el plugin Braze Expo:

```bash
npx expo install @braze/expo-plugin
```

##### Paso 2.2: Añade el plugin a tu app.json {#step-22-add-the-plugin-to-your-appjson}

En tu `app.json`, añade el plugin Braze Expo. Puedes proporcionar las siguientes opciones de configuración:

| Método                                        | Tipo    | Descripción                                                                                                                                              |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `androidApiKey`                               | string  | Obligatoria. La [clave de API]({{site.baseurl}}/api/identifier_types/) para tu aplicación Android, ubicada en tu panel de Braze en **Administrar configuración**. |
| `iosApiKey`                                   | string  | Obligatoria. La [clave de API]({{site.baseurl}}/api/identifier_types/) para tu aplicación iOS, ubicada en tu panel de Braze en **Administrar configuración**.     |
| `baseUrl`                                     | string  | Obligatoria. El [punto final de SDK]({{site.baseurl}}/api/basics/#endpoints) de tu aplicación, ubicado en tu panel de Braze en **Administrar configuración**.    |
| `enableBrazeIosPush`                          | boolean | Solo para iOS. Si se utiliza Braze para gestionar las notificaciones push en iOS. Introducido en el SDK de React Native v1.38.0 y Expo Plugin v0.4.0.                       |
| `enableFirebaseCloudMessaging`                | boolean | Solo para Android. Si se utiliza Firebase Cloud Messaging para las notificaciones push. Introducido en el SDK de React Native v1.38.0 y Expo Plugin v0.4.0.             |
| `firebaseCloudMessagingSenderId`              | string  | Solo para Android. Tu ID de remitente de Firebase Cloud Messaging. Introducido en el SDK de React Native v1.38.0 y Expo Plugin v0.4.0.                                    |
| `sessionTimeout`                              | integer | El tiempo de espera de la sesión de Braze para tu aplicación en segundos.                                                                                               |
| `enableSdkAuthentication`                     | boolean | Si se habilita la característica de [Autenticación SDK]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication/#sdk-authentication).      |
| `logLevel`                                    | integer | El nivel de registro de tu aplicación. El nivel de registro predeterminado es 8 y registra la información mínima. Para habilitar el registro detallado para la depuración, utiliza el nivel de registro 0.    |
| `minimumTriggerIntervalInSeconds`             | integer | El intervalo de tiempo mínimo en segundos entre desencadenamientos. Predeterminado a 30 segundos.                                                                           |
| `enableAutomaticLocationCollection`           | boolean | Si está habilitada la recopilación automática de ubicaciones (si el usuario lo permite).                                                                                  |
| `enableGeofence`                              | boolean | Si están habilitadas las geovallas.                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | boolean | Si las solicitudes de geovalla deben hacerse automáticamente.                                                                                                  |
| `dismissModalOnOutsideTap`                    | boolean | Solo para iOS. Si un mensaje modal dentro de la aplicación se descarta cuando el usuario hace clic fuera del mensaje dentro de la aplicación.                                           |
| `androidHandlePushDeepLinksAutomatically`     | boolean | Solo para Android. Si el SDK de Braze debe gestionar automáticamente los vínculos profundos push.                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | boolean | Solo para Android. Establece si el contenido de texto de una notificación push debe ser interpretado y renderizado como HTML utilizando `android.text.Html.fromHtml`.        |
| `androidNotificationAccentColor`              | string  | Solo para Android. Establece el color de acento de las notificaciones de Android.                                                                                                |
| `androidNotificationLargeIcon`                | string  | Solo para Android. Establece el icono grande de notificación de Android.                                                                                                  |
| `androidNotificationSmallIcon`                | string  | Solo para Android. Establece el icono pequeño de notificación de Android.                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | boolean | Solo para iOS. Si se debe pedir automáticamente al usuario permisos push al iniciar la aplicación.                                                          |
| `enableBrazeIosRichPush`                      | boolean | Solo para iOS. Si se habilitan las características de notificaciones push enriquecidas para iOS.                                                                                                  |
| `enableBrazeIosPushStories`                   | boolean | Solo para iOS. Si se habilitan las Push Stories de Braze para iOS.                                                                                                  |
| `iosPushStoryAppGroup`                        | string  | Solo para iOS. El grupo de aplicaciones utilizado para las Push Stories de iOS.                                                                                                       |
| `iosUseUUIDAsDeviceId`                        | boolean | Solo para iOS. Si el ID del dispositivo utilizará un UUID generado aleatoriamente.                                                                                       |
| `iosForwardUniversalLinks`                    | boolean | Solo para iOS. Especifica si el SDK debe reconocer y reenviar automáticamente los enlaces universales a los métodos del sistema (predeterminado: `false`). Cuando está habilitado, el SDK reenviará automáticamente los enlaces universales a los métodos del sistema definidos en [Compatibilidad con enlaces universales en tu aplicación](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks/). Introducido en React Native SDK v11.1.0 y Expo Plugin v3.2.0. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Paso 2.2: Añade el plugin a tu app.json" }

El siguiente fragmento de código muestra un ejemplo de configuración de `app.json`:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidApiKey": "YOUR-ANDROID-API-KEY",
          "iosApiKey": "YOUR-IOS-API-KEY",
          "baseUrl": "YOUR-SDK-ENDPOINT",
          "sessionTimeout": 60,
          "enableGeofence": false,
          "enableBrazeIosPush": false,
          "enableFirebaseCloudMessaging": false,
          "firebaseCloudMessagingSenderId": "YOUR-FCM-SENDER-ID",
          "androidHandlePushDeepLinksAutomatically": true,
          "enableSdkAuthentication": false,
          "logLevel": 0,
          "minimumTriggerIntervalInSeconds": 0,
          "enableAutomaticLocationCollection": false,
          "enableAutomaticGeofenceRequests": false,
          "dismissModalOnOutsideTap": true,
          "androidPushNotificationHtmlRenderingEnabled": true,
          "androidNotificationAccentColor": "#ff3344",
          "androidNotificationLargeIcon": "@drawable/custom_app_large_icon",
          "androidNotificationSmallIcon": "@drawable/custom_app_small_icon",
          "iosRequestPushPermissionsAutomatically": false,
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.example.myapp.PushStories",
          "iosForwardUniversalLinks": false
        }
      ],
    ]
  }
}
```

###### Configuración de los iconos de notificaciones push en Android {#configuring-android-push-notification-icons}

Cuando utilices `androidNotificationLargeIcon` y `androidNotificationSmallIcon`, sigue estas prácticas recomendadas para que los iconos se muestren correctamente:

**Ubicación y formato de los iconos**

Para utilizar iconos de notificaciones push personalizados con el plugin Braze Expo:

1. Crea tus archivos de iconos siguiendo los requisitos de iconos que se detallan a continuación.
2. Colócalos en los directorios nativos de Android de tu proyecto en `android/app/src/main/res/drawable-<density>/` (por ejemplo, `android/app/src/main/res/drawable-mdpi/`, `drawable-hdpi/`, o similar).
3. Como alternativa, si administras activos en tu directorio React Native, puedes utilizar la [configuración de iconos de app.json](https://docs.expo.dev/versions/latest/config/app/#icon) de Expo o crear un [plugin de configuración de Expo](https://docs.expo.dev/config-plugins/introduction/) para copiar los iconos a las carpetas drawable de Android durante la precompilación.

El plugin Braze Expo hace referencia a estos iconos utilizando el sistema de recursos drawable de Android.

**Requisitos de los iconos**

- **Icono pequeño:** Debe ser una silueta blanca sobre un fondo transparente (este es un requisito de la plataforma Android).
- **Icono grande:** Puede ser una imagen a todo color.
- **Formato:** Se recomienda el formato PNG.
- **Nomenclatura:** Utiliza solo letras minúsculas, números y guiones bajos (por ejemplo, `my_large_icon.png`).

**Configuración en app.json**

El siguiente fragmento de código muestra cómo hacer referencia a los iconos de notificación de Android en `app.json` usando el prefijo `@drawable/`:

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "androidNotificationLargeIcon": "@drawable/large_icon",
          "androidNotificationSmallIcon": "@drawable/small_icon"
        }
      ]
    ]
  }
}
```

{% alert important %}
No utilices rutas de archivo relativas (como `src/assets/images/icon.png`) ni incluyas la extensión del archivo al hacer referencia a los iconos. El plugin Expo requiere el prefijo `@drawable/` para ubicar correctamente los iconos en las carpetas nativas de Android después del proceso de precompilación.
{% endalert %}

**Cómo funciona**

El plugin Braze Expo hace referencia a tus archivos de iconos desde los directorios `drawable` de Android. Cuando ejecutas `npx expo prebuild`, Expo genera la estructura nativa del proyecto Android. Tus iconos deben estar presentes en las carpetas `drawable` de Android (ya sea colocados manualmente o copiados a través de un plugin de configuración) antes del proceso de compilación. A continuación, el plugin configura el SDK de Braze para utilizar estos recursos drawable por sus nombres (sin ruta ni extensión), por lo que es necesario incluir el prefijo `@drawable/` en tu configuración.

Para obtener más información sobre los iconos de notificación de Android, consulta las [directrices sobre iconos de notificación de Android](https://developer.android.com/develop/ui/views/notifications#icon).

##### Paso 2.3: Compila y ejecuta tu aplicación {#step-23-build-and-run-your-application}

La precompilación de tu aplicación genera los archivos nativos necesarios para que el plugin Braze Expo funcione.

El siguiente fragmento de código muestra el comando para precompilar tu aplicación:

```bash
npx expo prebuild
```

Ejecuta tu aplicación como se especifica en la [documentación de Expo](https://docs.expo.dev/workflow/customizing/). Ten en cuenta que, si realizas algún cambio en las opciones de configuración, tendrás que precompilar y ejecutar la aplicación de nuevo.

#### Método 2: Uso de React Native CLI {#method-2-using-react-native-cli}

##### Configurar Android

**Paso 2.1: Añade el plugin Kotlin Gradle**

El siguiente fragmento de código muestra cómo añadir el plugin Kotlin Gradle en el `build.gradle` de nivel superior de tu proyecto bajo `buildscript` > `dependencies`:

```groovy
buildscript {
    dependencies {
        ...
        // Choose your Kotlin version
        classpath("org.jetbrains.kotlin:kotlin-gradle-plugin:1.8.10")
    }
}
```

Esto añade Kotlin a tu proyecto.

**Paso 2.2: Configura el SDK de Braze**

Para conectarte a los servidores de Braze, crea un archivo `braze.xml` en la carpeta `res/values` de tu proyecto. El siguiente fragmento de código muestra un ejemplo de configuración de `braze.xml`. Sustituye la [clave]({{site.baseurl}}/api/identifier_types/) de API y el [punto de conexión]({{site.baseurl}}/api/basics/#endpoints) por tus valores:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOU_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

El siguiente fragmento de código muestra los permisos necesarios para tu archivo `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
En la versión 12.2.0 o posterior del SDK de Braze para Android, puedes incorporar automáticamente la biblioteca android-sdk-location configurando `importBrazeLocationLibrary=true` en tu archivo `gradle.properties`.
{% endalert %}

**Paso 2.3: Implementa el seguimiento de sesión del usuario**

Las llamadas a `openSession()` y `closeSession()` se gestionan automáticamente.
El siguiente fragmento de código muestra qué añadir al método `onCreate()` de tu clase `MainApplication`:

{% subtabs local %}
{% subtab JAVA %}
```java
import com.braze.BrazeActivityLifecycleCallbackListener;

@Override
public void onCreate() {
    super.onCreate();
    ...
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
import com.braze.BrazeActivityLifecycleCallbackListener

override fun onCreate() {
    super.onCreate()
    ...
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
}
```
{% endsubtab %}
{% endsubtabs %}

**Paso 2.4: Gestiona las actualizaciones de intención**

Si tu MainActivity tiene `android:launchMode` configurado en `singleTask`, el siguiente fragmento de código muestra qué añadir a tu clase `MainActivity`:

{% subtabs local %}
{% subtab JAVA %}
```java
@Override
public void onNewIntent(Intent intent) {
    super.onNewIntent(intent);
    setIntent(intent);
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
override fun onNewIntent(intent: Intent) {
    super.onNewIntent(intent)
    setIntent(intent)
}
```
{% endsubtab %}
{% endsubtabs %}

##### Configurar iOS

**Paso 2.5: (Opcional) Configura el Podfile para XCFrameworks dinámicos**

Para importar determinadas bibliotecas de Braze, como BrazeUI, a un archivo Objective-C++, debes utilizar la sintaxis `#import`. A partir de la versión `7.4.0` del SDK Swift de Braze, los binarios tienen un [canal de distribución opcional como XCFrameworks dinámicos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic), que son compatibles con esta sintaxis.

Si quieres utilizar este canal de distribución, anula manualmente las ubicaciones de las fuentes de CocoaPods en tu Podfile. El siguiente fragmento de código muestra un ejemplo de anulación. Sustituye `{your-version}` por la versión correspondiente que desees importar:

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

**Paso 2.6: Instala los pods**

Dado que React Native vincula automáticamente las bibliotecas a la plataforma nativa, puedes instalar el SDK con la ayuda de CocoaPods.

El siguiente fragmento de código muestra cómo instalar los pods desde la carpeta raíz del proyecto:

```bash
# To install using the React Native New Architecture
cd ios && pod install

# To install using the React Native legacy architecture
cd ios && RCT_NEW_ARCH_ENABLED=0 pod install
```

**Paso 2.7: Configura el SDK de Braze**

{% subtabs local %}
{% subtab SWIFT %}

El siguiente fragmento de código muestra cómo importar el SDK de Braze en la parte superior del archivo `AppDelegate.swift`:
```swift
import BrazeKit
import braze_react_native_sdk
```

En el método `application(_:didFinishLaunchingWithOptions:)`, sustituye la [clave]({{site.baseurl}}/api/identifier_types/) de API y el [punto de conexión]({{site.baseurl}}/api/basics/#endpoints) por los valores de tu aplicación. A continuación, crea la instancia de Braze utilizando la configuración, y crea una propiedad estática en `AppDelegate` para facilitar el acceso.

{% alert note %}
Nuestro ejemplo supone una implementación de [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h), que proporciona una serie de abstracciones en la configuración de React Native. Si utilizas una configuración diferente para tu aplicación, asegúrate de ajustar tu implementación según sea necesario.
{% endalert %}

El siguiente fragmento de código muestra un ejemplo de configuración de `AppDelegate.swift`:

```swift
func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
    // Setup Braze
    let configuration = Braze.Configuration(
        apiKey: "{BRAZE_API_KEY}",
        endpoint: "{BRAZE_ENDPOINT}")
    // Enable logging and customize the configuration here.
    configuration.logger.level = .info
    let braze = BrazeReactBridge.perform(
      #selector(BrazeReactBridge.initBraze(_:)),
      with: configuration
    ).takeUnretainedValue() as! Braze

    AppDelegate.braze = braze

    /* Other configuration */

    return true
}

// MARK: - AppDelegate.braze

static var braze: Braze? = nil
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

El siguiente fragmento de código muestra cómo importar el SDK de Braze en la parte superior del archivo `AppDelegate.m`:
```objc
#import <BrazeKit/BrazeKit-Swift.h>
#import "BrazeReactBridge.h"
```

En el método `application:didFinishLaunchingWithOptions:`, sustituye la [clave]({{site.baseurl}}/api/identifier_types/) de API y el [punto de conexión]({{site.baseurl}}/api/basics/#endpoints) por los valores de tu aplicación. A continuación, crea la instancia de Braze utilizando la configuración, y crea una propiedad estática en `AppDelegate` para facilitar el acceso.

{% alert note %}
Nuestro ejemplo supone una implementación de [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h), que proporciona una serie de abstracciones en la configuración de React Native. Si utilizas una configuración diferente para tu aplicación, asegúrate de ajustar tu implementación según sea necesario.
{% endalert %}

El siguiente fragmento de código muestra un ejemplo de configuración de `AppDelegate.m`:

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze
  BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                                                    endpoint:@"{BRAZE_ENDPOINT}"];
  // Enable logging and customize the configuration here.
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazeReactBridge initBraze:configuration];
  AppDelegate.braze = braze;

  /* Other configuration */

  return YES;
}

#pragma mark - AppDelegate.braze

static Braze *_braze = nil;

+ (Braze *)braze {
  return _braze;
}

+ (void)setBraze:(Braze *)braze {
  _braze = braze;
}
```

{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% endtabs %}

### Paso 3: Inicializa el SDK {#step-3-initialize-the-sdk}

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

El siguiente fragmento de código muestra cómo importar la biblioteca en tu código React Native:

```javascript
import Braze from "@braze/react-native-sdk";
```

Luego llama a `Braze.initialize()` con tu clave de API del identificador de la aplicación y el punto de conexión del SDK para crear la instancia de Braze. Consulta las opciones a continuación para saber dónde llamar a este método en tu aplicación.

#### Inicialización estándar {#standard-initialization}

El siguiente fragmento de código muestra cómo inicializar el SDK cuando tu aplicación se inicia llamando a `Braze.initialize()` en un `useEffect`:

```javascript
import React, { useEffect } from "react";
import Braze from "@braze/react-native-sdk";

const App = () => {
  useEffect(() => {
    Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
  }, []);

  return (
    // Your app components
  );
};
```

#### Inicialización diferida {#delayed-initialization}

El siguiente fragmento de código muestra cómo diferir la inicialización del SDK hasta más adelante en la sesión. Por ejemplo, después de que el usuario otorgue su consentimiento o complete el inicio de sesión:

```javascript
function onUserConsent() {
  Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
}
```

{% alert warning %}
En iOS, las notificaciones push recibidas antes de `Braze.initialize()` se ponen en cola y se procesan después de la inicialización. En Android, los vínculos profundos de las notificaciones push no se resuelven mientras el SDK está esperando ser inicializado. Si tu aplicación depende del manejo inmediato de vínculos profundos al inicio, usa la [inicialización estándar](#standard-initialization) en su lugar.
{% endalert %}

#### Claves de API específicas por plataforma {#platform-specific-api-keys}

El siguiente fragmento de código muestra cómo usar la detección de plataforma cuando tus aplicaciones Android e iOS usan claves de API diferentes:

```javascript
import { Platform } from "react-native";
import Braze from "@braze/react-native-sdk";

const apiKey = Platform.select({
  android: "YOUR-ANDROID-API-KEY",
  ios: "YOUR-IOS-API-KEY",
}) ?? "";

Braze.initialize(apiKey, "YOUR-SDK-ENDPOINT");
```

#### Reinicialización {#re-initialization}

Puedes llamar a `Braze.initialize()` varias veces para reinicializar el SDK con una clave de API y punto de conexión diferentes durante la sesión. Cada llamada destruye la instancia de Braze anterior y crea una nueva.

{% alert important %}
Todas las llamadas a métodos del SDK realizadas antes de `Braze.initialize()` se ignoran en iOS, así que llama a `Braze.initialize()` antes de usar cualquier otro método de Braze.
{% endalert %}

{% endtab %}
{% tab React Native SDK 19.1.0 y anteriores %}

Para React Native SDK 19.1.0 y anteriores, la inicialización nativa ocurre en el paso 2. Importa la biblioteca en tu código React Native para llamar a los métodos de Braze. Para más detalles, consulta nuestro [proyecto de ejemplo](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject).

```javascript
import Braze from "@braze/react-native-sdk";
```

{% endtab %}
{% endtabs %}

### Paso 4: Prueba la integración (opcional) {#step-4-test-the-integration-optional}

{% tabs %}
{% tab React Native SDK 19.2.0+ %}

Puedes verificar que el SDK está integrado comprobando las estadísticas de sesión en el dashboard. Si ejecutas tu aplicación en cualquiera de las plataformas, deberías ver una nueva sesión en el dashboard (en la sección **Overview**).

El siguiente fragmento de código muestra cómo abrir una sesión para un usuario en particular en tu aplicación:

```javascript
import Braze from "@braze/react-native-sdk";

Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
Braze.changeUser("{some-user-id}");
```

Busca al usuario con `{some-user-id}` en el dashboard en **Audience** > **Search Users**. Ahí puedes verificar que se hayan registrado los datos de sesión y dispositivo.

{% endtab %}
{% tab React Native SDK 19.1.0 y anteriores %}

Para probar la integración del SDK, el siguiente fragmento de código muestra cómo iniciar una nueva sesión en cualquiera de las plataformas para un usuario.

```javascript
Braze.changeUser("userId");
```

El siguiente fragmento de código muestra un ejemplo de asignación del ID de usuario al iniciar la aplicación:

```javascript
import React, { useEffect } from "react";
import Braze from "@braze/react-native-sdk";

const App = () => {
  useEffect(() => {
    Braze.changeUser("some-user-id");
  }, []);

  return (
    <div>
      ...
    </div>
  )
```

En el panel de Braze, ve a [Búsqueda de usuarios]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#using-user-search) y busca al usuario con el ID correspondiente a `some-user-id`. Ahí puedes verificar que se hayan registrado los datos de sesión y dispositivo.

{% endtab %}
{% endtabs %}

## Próximos pasos {#next-steps}

Después de integrar el SDK de Braze, puedes empezar a implementar características de mensajería comunes:

- [Notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/): Configura y envía notificaciones push a tus usuarios.
- [In-App Messages]({{site.baseurl}}/developer_guide/in_app_messages/): Muestra mensajes contextuales dentro de tu aplicación.
- [Banners]({{site.baseurl}}/developer_guide/banners/): Muestra banners persistentes en la interfaz de tu aplicación.