## Acerca del SDK or kit de desarrollo de software de Braze para React Native {#about-the-react-native-braze-sdk}

La integración del SDK or kit de desarrollo de software de Braze para React Native proporciona funcionalidad básica de análisis y te permite integrar mensajes dentro de la aplicación y Content Cards tanto para iOS como para Android con una única base de código.

## Compatibilidad con la Nueva Arquitectura {#new-architecture-compatibility}

La siguiente versión mínima del SDK or kit de desarrollo de software es compatible con todas las aplicaciones que utilizan [la Nueva Arquitectura de React Native](https://reactnative.dev/docs/the-new-architecture/landing-page):

{% sdk_min_versions reactnative:2.0.1 %}

A partir de la versión 6.0.0 del SDK or kit de desarrollo de software, Braze utiliza un Turbo Module de React Native, que es compatible tanto con la Nueva Arquitectura como con la arquitectura de puente heredada. Esto significa que no se requiere ninguna configuración adicional.

{% alert warning %}
Si tu aplicación iOS se ajusta a `RCTAppDelegate` y sigue nuestra configuración anterior de `AppDelegate`, revisa los ejemplos en [Configuración nativa completa](#reactnative_step-2-complete-native-setup) para evitar fallos al suscribirte a eventos en el Turbo Module.
{% endalert %}

## Requisitos de versión de React y React Native {#react-and-react-native-version-requirements}

Braze no publica versiones mínimas de React independientes más allá de lo que admite el SDK or kit de desarrollo de software de React Native. Para integrar el SDK or kit de desarrollo de software, usa React Native versión 0.71 o posterior. Para consultar la lista completa de versiones de React Native compatibles, consulta el [repositorio de GitHub del SDK or kit de desarrollo de software de React Native](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support).

Cuando actualices React, React Native o el SDK or kit de desarrollo de software de Braze, revisa el [Registro de cambios](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md) del SDK or kit de desarrollo de software en busca de cambios de última hora antes de desplegar.

## Integración del SDK or kit de desarrollo de software de React Native {#integrating-the-react-native-sdk}

### Requisitos previos {#prerequisites}

Para conocer las versiones de React Native compatibles y las instrucciones de actualización, consulta [Requisitos de versión de React y React Native](#react-and-react-native-version-requirements).

### Paso 1: Integra la biblioteca de Braze {#step-1-integrate-the-braze-library}

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
### Paso 2: Completa la configuración nativa {#step-2-complete-native-setup}

Si tu aplicación usa Expo, consulta [Uso del plugin de Expo](#reactnative-using-the-expo-plugin). Si tu aplicación usa React Native puro, consulta [Uso de React Native CLI](#reactnative-using-react-native-cli).
Elige un método de configuración en cada pestaña de versión: plugin de Expo o React Native CLI.

{% tabs %}
{% tab React Native SDK or kit de desarrollo de software 19.2.0+ %}

#### Método 1: Uso del plugin de Expo {#reactnative-using-the-expo-plugin}

##### 2.1 Instala el plugin de Braze para Expo {#21-install-the-braze-expo-plugin}

Asegúrate de que tu versión del plugin de Braze para Expo sea al menos 4.1.0. Para ver la lista completa de versiones compatibles, consulta el [repositorio del plugin de Braze para Expo](https://github.com/braze-inc/braze-expo-plugin?tab=readme-ov-file#version-support).

El siguiente fragmento de código muestra el comando para instalar el plugin de Braze para Expo:

```bash
npx expo install @braze/expo-plugin
```

##### 2.2 Añade el plugin a tu app.json {#22-add-the-plugin-to-your-appjson}

En tu `app.json`, añade el plugin de Braze para Expo. La clave de API y el endpoint ya no se configuran aquí. Proporciónelos en tiempo de ejecución mediante `Braze.initialize()` desde JavaScript. Añade los siguientes parámetros de configuración opcionales según las necesidades de tu implementación:

| Método                                        | Tipo    | Descripción                                                                                                                                              |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `enableBrazeIosPush`                          | boolean | Solo iOS. Si se utiliza Braze para gestionar las notificaciones push en iOS.                       |
| `enableFirebaseCloudMessaging`                | boolean | Solo Android. Si se utiliza Firebase Cloud Messaging para las notificaciones push.             |
| `firebaseCloudMessagingSenderId`              | string  | Solo Android. Tu ID de remitente de Firebase Cloud Messaging.                                    |
| `sessionTimeout`                              | integer | El tiempo de espera de sesión de Braze para tu aplicación en segundos.                                                                                               |
| `enableSdkAuthentication`                     | boolean | Si se habilita la característica de [autenticación del SDK or kit de desarrollo de software]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication).      |
| `logLevel`                                    | integer | El nivel de registro para tu aplicación. El nivel de registro predeterminado es 8 y registra mínimamente información. Para habilitar el registro detallado para la depuración, utiliza el nivel de registro 0.    |
| `minimumTriggerIntervalInSeconds`             | integer | El intervalo de tiempo mínimo en segundos entre desencadenadores. El valor predeterminado es 30 segundos.                                                                           |
| `enableAutomaticLocationCollection`           | boolean | Si la recopilación automática de ubicación está habilitada (si el usuario lo permite).                                                                                  |
| `enableGeofence`                              | boolean | Si las geovallas están habilitadas.                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | boolean | Si las solicitudes de geovallas deben realizarse automáticamente.                                                                                                  |
| `dismissModalOnOutsideTap`                    | boolean | Solo iOS. Si un mensaje modal dentro de la aplicación se descarta cuando el usuario hace clic fuera del mensaje dentro de la aplicación.                                           |
| `androidHandlePushDeepLinksAutomatically`     | boolean | Solo Android. Si el SDK or kit de desarrollo de software de Braze debe gestionar automáticamente los vínculos profundos de push.                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | boolean | Solo Android. Configura si el contenido de texto en una notificación push debe interpretarse y renderizarse como HTML usando `android.text.Html.fromHtml`.        |
| `androidNotificationAccentColor`              | string  | Solo Android. Configura el color de acento de las notificaciones de Android.                                                                                                |
| `androidNotificationLargeIcon`                | string  | Solo Android. Configura el icono grande de las notificaciones de Android.                                                                                                  |
| `androidNotificationSmallIcon`                | string  | Solo Android. Configura el icono pequeño de las notificaciones de Android.                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | boolean | Solo iOS. Si al usuario se le debe solicitar automáticamente permiso de push al iniciar la aplicación.                                                          |
| `enableBrazeIosRichPush`                      | boolean | Solo iOS. Si se habilitan las características de notificaciones push enriquecidas para iOS.                                                                                                  |
| `enableBrazeIosPushStories`                   | boolean | Solo iOS. Si se habilitan las Push Stories de Braze para iOS.                                                                                                  |
| `iosPushStoryAppGroup`                        | string  | Solo iOS. El grupo de aplicaciones utilizado para las Push Stories de iOS.                                                                                                       |
| `iosUseUUIDAsDeviceId`                        | boolean | Solo iOS. Si el ID de dispositivo utiliza un UUID generado aleatoriamente.                                                                                       |
| `iosForwardUniversalLinks`                    | boolean | Solo iOS. Especifica si el SDK or kit de desarrollo de software debe reconocer y reenviar automáticamente los enlaces universales a los métodos del sistema (valor predeterminado: `false`). |
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

###### Configuración de iconos de notificaciones push en Android {#android-push-icons}

Al utilizar `androidNotificationLargeIcon` y `androidNotificationSmallIcon`, sigue estas mejores prácticas para una visualización correcta de los iconos:

**Ubicación y formato de los iconos**

Para utilizar iconos de notificaciones push personalizados con el plugin de Braze para Expo:

1. Crea tus archivos de iconos siguiendo los requisitos de iconos que se enumeran a continuación.
2. Colócalos en los directorios nativos de Android de tu proyecto en `android/app/src/main/res/drawable-<density>/`.
   Por ejemplo, utiliza `android/app/src/main/res/drawable-mdpi/` y `android/app/src/main/res/drawable-hdpi/`.
3. Alternativamente, si gestionas los activos en tu directorio de React Native, puedes usar la [configuración de iconos en app.json de Expo](https://docs.expo.dev/versions/latest/config/app/#icon) o crear un [plugin de configuración de Expo](https://docs.expo.dev/config-plugins/introduction/) para copiar los iconos a las carpetas drawable de Android durante el prebuild.

El plugin de Braze para Expo hace referencia a estos iconos usando el sistema de recursos drawable de Android.

**Requisitos de iconos**

- **Icono pequeño:** Debe ser una silueta blanca sobre fondo transparente (esto es un requisito de la plataforma Android)
- **Icono grande:** Puede ser una imagen a todo color.
- **Formato:** Se recomienda el formato PNG.
- **Nombres:** Usa solo letras minúsculas, números y guiones bajos (por ejemplo, `my_large_icon.png`)

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
No uses rutas de archivos relativas (como `src/assets/images/icon.png`) ni incluyas la extensión del archivo al hacer referencia a iconos. El plugin de Expo requiere el prefijo `@drawable/` para localizar correctamente los iconos en las carpetas nativas de Android después del proceso de prebuild.
{% endalert %}

**Cómo funciona**

El plugin de Braze para Expo hace referencia a tus archivos de iconos desde los directorios `drawable` de Android. Cuando ejecutas `npx expo prebuild`, Expo genera la estructura nativa del proyecto Android. Tus iconos deben estar presentes en las carpetas `drawable` de Android (ya sea colocados manualmente o copiados a través de un plugin de configuración) antes del proceso de compilación. El plugin entonces configura el SDK or kit de desarrollo de software de Braze para usar estos recursos drawable por sus nombres (sin ruta ni extensión), razón por la cual el prefijo `@drawable/` es necesario en tu configuración.

Para obtener más información sobre los iconos de notificación de Android, consulta las [directrices de iconos de notificación de Android](https://developer.android.com/develop/ui/views/notifications#icon).

##### 2.3 Compila y ejecuta tu aplicación {#23-build-and-run-your-application}

Hacer el prebuild de tu aplicación genera los archivos nativos necesarios para que el plugin de Braze para Expo funcione.

El siguiente fragmento de código muestra el comando para hacer el prebuild de tu aplicación:

```bash
npx expo prebuild
```

Ejecuta tu aplicación como se especifica en la [documentación de Expo](https://docs.expo.dev/workflow/customizing/). Si realizas cambios en las opciones de configuración, haz el prebuild y ejecuta la aplicación de nuevo.

#### Método 2: Uso de React Native CLI {#reactnative-using-react-native-cli}

##### Configura Android {#set-up-android}

**2.1 Añade el plugin de Kotlin Gradle**

El siguiente fragmento de código muestra cómo añadir el plugin de Kotlin Gradle en el archivo `build.gradle` de nivel superior de tu proyecto bajo `buildscript` > `dependencies`:

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

**2.2 Configura el SDK or kit de desarrollo de software de Braze**

Crea un archivo `braze.xml` en la carpeta `res/values` de tu proyecto. La clave de API y el endpoint se proporcionan en tiempo de ejecución desde JavaScript, por lo que no son necesarios en este archivo. El siguiente fragmento de código muestra cómo habilitar la inicialización diferida con `com_braze_enable_delayed_initialization`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <bool name="com_braze_enable_delayed_initialization">true</bool>
</resources>
```

{% alert note %}
Aún puedes añadir otros valores de configuración nativa a `braze.xml` (como push, tiempo de espera de sesión y configuración de registro). Estos se aplican automáticamente cuando se llama a `Braze.initialize()` desde JavaScript.
{% endalert %}

El siguiente fragmento de código muestra los permisos necesarios para tu archivo `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert tip %}
En la versión 12.2.0 o posterior del SDK or kit de desarrollo de software de Braze para Android, puedes incorporar automáticamente la biblioteca android-SDK or kit de desarrollo de software-location configurando `importBrazeLocationLibrary=true` en tu archivo `gradle.properties`.
{% endalert %}

**2.3 Implementa el seguimiento de sesiones de usuario**

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

**2.4 Gestiona las actualizaciones de intent**

Si tu MainActivity tiene `android:launchMode` configurado como `singleTask`, el siguiente fragmento de código muestra qué añadir a tu clase `MainActivity`:

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

##### Configura iOS {#set-up-ios}

**2.5 (Opcional) Configura el Podfile para XCFrameworks dinámicos**

Para importar ciertas bibliotecas de Braze, como BrazeUI, en un archivo Objective-C++, debes usar la sintaxis `#import`. A partir de la versión `7.4.0` del SDK or kit de desarrollo de software Swift de Braze, los binarios tienen un [canal de distribución opcional como XCFrameworks dinámicos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic), que son compatibles con esta sintaxis.

Si deseas usar este canal de distribución, sobrescribe manualmente las ubicaciones de origen de CocoaPods en tu Podfile. Consulta este ejemplo y reemplaza `{your-version}` con la versión relevante que deseas importar:

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

**2.6 Instala los pods**

Dado que React Native vincula automáticamente las bibliotecas a la plataforma nativa, puedes instalar el SDK or kit de desarrollo de software con la ayuda de CocoaPods.

El siguiente fragmento de código muestra cómo instalar los pods desde la carpeta raíz del proyecto:

```bash
# To install using the React Native New Architecture
cd ios && pod install

# To install using the React Native legacy architecture
cd ios && RCT_NEW_ARCH_ENABLED=0 pod install
```

**2.7 Configura el SDK or kit de desarrollo de software de Braze**

Usa `BrazeReactInitializer.configure` en tu `AppDelegate` para registrar la configuración nativa. Los closures que proporciones se almacenan y se aplican más tarde cuando se llama a `Braze.initialize(apiKey, endpoint)` desde JavaScript.

{% subtabs local %}
{% subtab SWIFT %}

El siguiente fragmento de código muestra cómo importar el SDK or kit de desarrollo de software de Braze en la parte superior del archivo `AppDelegate.swift`:

```swift
import BrazeKit
import braze_react_native_sdk
```

En el método `application(_:didFinishLaunchingWithOptions:)`, registra tu configuración nativa usando `BrazeReactInitializer.configure`. No establezcas la clave de API ni el endpoint aquí. Se proporcionan desde JavaScript a través de `Braze.initialize()`.

- **Closure `configure`**: Recibe una `Braze.Configuration` y te permite establecer propiedades de configuración nativa (registro, push, sesiones y más).
- **Closure `postInitialization`** _(opcional)_: Recibe la instancia activa de `Braze` después de su creación, para configuraciones que requieren la instancia (por ejemplo, almacenar una referencia o configurar delegados).

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

El siguiente fragmento de código muestra cómo importar el SDK or kit de desarrollo de software de Braze en la parte superior del archivo `AppDelegate.m`:

```objc
@import BrazeKit;
@import braze_react_native_sdk;
```

En el método `application:didFinishLaunchingWithOptions:`, registra tu configuración nativa usando `BrazeReactInitializer`. No establezcas la clave de API ni el endpoint aquí. Se proporcionan desde JavaScript a través de `Braze.initialize()`.

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
`BrazeReactInitializer.configure()` solo almacena tu configuración. No existe ninguna instancia de Braze hasta que se llama a `Braze.initialize()` desde JavaScript, por lo que no debes llamar a ningún método del SDK or kit de desarrollo de software de Braze en el AppDelegate después de `configure()`.
Cuando vuelves a llamar a `Braze.initialize()`, se aplican los mismos bloques `configure` y `postInitialization` a la nueva instancia de Braze.
{% endalert %}

{% endtab %}
{% tab React Native SDK or kit de desarrollo de software 19.1.0 y anteriores %}

#### Método 1: Uso del plugin de Expo {#method-1-using-the-expo-plugin}

##### Paso 2.1: Instala el plugin de Braze para Expo {#step-21-install-the-braze-expo-plugin}

Asegúrate de que tu versión del SDK or kit de desarrollo de software de React Native de Braze sea al menos 1.37.0. Para ver la lista completa de versiones compatibles, consulta el [repositorio de React Native de Braze](https://github.com/braze-inc/braze-react-native-sdk?tab=readme-ov-file#version-support).

El siguiente fragmento de código muestra el comando para instalar el plugin de Braze para Expo:

```bash
npx expo install @braze/expo-plugin
```

##### Paso 2.2: Añade el plugin a tu app.json {#step-22-add-the-plugin-to-your-appjson}

En tu `app.json`, añade el plugin de Braze para Expo. Puedes proporcionar las siguientes opciones de configuración:

| Método                                        | Tipo    | Descripción                                                                                                                                              |
| --------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `androidApiKey`                               | string  | Obligatorio. La [clave de API]({{site.baseurl}}/api/identifier_types) de tu aplicación Android, ubicada en el panel de Braze en **Administrar configuración**. |
| `iosApiKey`                                   | string  | Obligatorio. La [clave de API]({{site.baseurl}}/api/identifier_types) de tu aplicación iOS, ubicada en el panel de Braze en **Administrar configuración**.     |
| `baseUrl`                                     | string  | Obligatorio. El [endpoint del SDK or kit de desarrollo de software]({{site.baseurl}}/api/basics#endpoints) de tu aplicación, ubicado en el panel de Braze en **Administrar configuración**.    |
| `enableBrazeIosPush`                          | boolean | Solo iOS. Si se utiliza Braze para gestionar las notificaciones push en iOS. Introducido en React Native SDK or kit de desarrollo de software v1.38.0 y Expo Plugin v0.4.0.                       |
| `enableFirebaseCloudMessaging`                | boolean | Solo Android. Si se utiliza Firebase Cloud Messaging para las notificaciones push. Introducido en React Native SDK or kit de desarrollo de software v1.38.0 y Expo Plugin v0.4.0.             |
| `firebaseCloudMessagingSenderId`              | string  | Solo Android. Tu ID de remitente de Firebase Cloud Messaging. Introducido en React Native SDK or kit de desarrollo de software v1.38.0 y Expo Plugin v0.4.0.                                    |
| `sessionTimeout`                              | integer | El tiempo de espera de sesión de Braze para tu aplicación en segundos.                                                                                               |
| `enableSdkAuthentication`                     | boolean | Si se habilita la característica de [autenticación del SDK or kit de desarrollo de software]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication).      |
| `logLevel`                                    | integer | El nivel de registro para tu aplicación. El nivel de registro predeterminado es 8 y registra mínimamente información. Para habilitar el registro detallado para la depuración, utiliza el nivel de registro 0.    |
| `minimumTriggerIntervalInSeconds`             | integer | El intervalo de tiempo mínimo en segundos entre desencadenadores. El valor predeterminado es 30 segundos.                                                                           |
| `enableAutomaticLocationCollection`           | boolean | Si la recopilación automática de ubicación está habilitada (si el usuario lo permite).                                                                                  |
| `enableGeofence`                              | boolean | Si las geovallas están habilitadas.                                                                                                                           |
| `enableAutomaticGeofenceRequests`             | boolean | Si las solicitudes de geovallas deben realizarse automáticamente.                                                                                                  |
| `dismissModalOnOutsideTap`                    | boolean | Solo iOS. Si un mensaje modal dentro de la aplicación se descarta cuando el usuario hace clic fuera del mensaje dentro de la aplicación.                                           |
| `androidHandlePushDeepLinksAutomatically`     | boolean | Solo Android. Si el SDK or kit de desarrollo de software de Braze debe gestionar automáticamente los vínculos profundos de push.                                                                         |
| `androidPushNotificationHtmlRenderingEnabled` | boolean | Solo Android. Configura si el contenido de texto en una notificación push debe interpretarse y renderizarse como HTML usando `android.text.Html.fromHtml`.        |
| `androidNotificationAccentColor`              | string  | Solo Android. Configura el color de acento de las notificaciones de Android.                                                                                                |
| `androidNotificationLargeIcon`                | string  | Solo Android. Configura el icono grande de las notificaciones de Android.                                                                                                  |
| `androidNotificationSmallIcon`                | string  | Solo Android. Configura el icono pequeño de las notificaciones de Android.                                                                                                  |
| `iosRequestPushPermissionsAutomatically`      | boolean | Solo iOS. Si al usuario se le debe solicitar automáticamente permiso de push al iniciar la aplicación.                                                          |
| `enableBrazeIosRichPush`                      | boolean | Solo iOS. Si se habilitan las características de notificaciones push enriquecidas para iOS.                                                                                                  |
| `enableBrazeIosPushStories`                   | boolean | Solo iOS. Si se habilitan las Push Stories de Braze para iOS.                                                                                                  |
| `iosPushStoryAppGroup`                        | string  | Solo iOS. El grupo de aplicaciones utilizado para las Push Stories de iOS.                                                                                                       |
| `iosUseUUIDAsDeviceId`                        | boolean | Solo iOS. Si el ID de dispositivo utilizará un UUID generado aleatoriamente.                                                                                       |
| `iosForwardUniversalLinks`                    | boolean | Solo iOS. Especifica si el SDK or kit de desarrollo de software debe reconocer y reenviar automáticamente los enlaces universales a los métodos del sistema (valor predeterminado: `false`). Cuando está habilitado, el SDK or kit de desarrollo de software reenviará automáticamente los enlaces universales a los métodos del sistema definidos en [Compatibilidad con enlaces universales en tu aplicación](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/forwarduniversallinks/). Introducido en React Native SDK or kit de desarrollo de software v11.1.0 y Expo Plugin v3.2.0. |
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

###### Configuración de iconos de notificaciones push en Android {#configuring-android-push-notification-icons}

Al utilizar `androidNotificationLargeIcon` y `androidNotificationSmallIcon`, sigue estas mejores prácticas para una visualización correcta de los iconos:

**Ubicación y formato de los iconos**

Para utilizar iconos de notificaciones push personalizados con el plugin de Braze para Expo:

1. Crea tus archivos de iconos siguiendo los requisitos de iconos que se enumeran a continuación.
2. Colócalos en los directorios nativos de Android de tu proyecto en `android/app/src/main/res/drawable-<density>/` (por ejemplo, `android/app/src/main/res/drawable-mdpi/`, `drawable-hdpi/` o similares).
3. Alternativamente, si gestionas los activos en tu directorio de React Native, puedes usar la [configuración de iconos en app.json de Expo](https://docs.expo.dev/versions/latest/config/app/#icon) o crear un [plugin de configuración de Expo](https://docs.expo.dev/config-plugins/introduction/) para copiar los iconos a las carpetas drawable de Android durante el prebuild.

El plugin de Braze para Expo hace referencia a estos iconos usando el sistema de recursos drawable de Android.

**Requisitos de iconos**

- **Icono pequeño:** Debe ser una silueta blanca sobre fondo transparente (esto es un requisito de la plataforma Android)
- **Icono grande:** Puede ser una imagen a todo color.
- **Formato:** Se recomienda el formato PNG.
- **Nombres:** Usa solo letras minúsculas, números y guiones bajos (por ejemplo, `my_large_icon.png`)

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
No uses rutas de archivos relativas (como `src/assets/images/icon.png`) ni incluyas la extensión del archivo al hacer referencia a iconos. El plugin de Expo requiere el prefijo `@drawable/` para localizar correctamente los iconos en las carpetas nativas de Android después del proceso de prebuild.
{% endalert %}

**Cómo funciona**

El plugin de Braze para Expo hace referencia a tus archivos de iconos desde los directorios `drawable` de Android. Cuando ejecutas `npx expo prebuild`, Expo genera la estructura nativa del proyecto Android. Tus iconos deben estar presentes en las carpetas `drawable` de Android (ya sea colocados manualmente o copiados a través de un plugin de configuración) antes del proceso de compilación. El plugin entonces configura el SDK or kit de desarrollo de software de Braze para usar estos recursos drawable por sus nombres (sin ruta ni extensión), razón por la cual el prefijo `@drawable/` es necesario en tu configuración.

Para obtener más información sobre los iconos de notificación de Android, consulta las [directrices de iconos de notificación de Android](https://developer.android.com/develop/ui/views/notifications#icon).

##### Paso 2.3: Compila y ejecuta tu aplicación {#step-23-build-and-run-your-application}

Hacer el prebuild de tu aplicación genera los archivos nativos necesarios para que el plugin de Braze para Expo funcione.

El siguiente fragmento de código muestra el comando para hacer el prebuild de tu aplicación:

```bash
npx expo prebuild
```

Ejecuta tu aplicación como se especifica en la [documentación de Expo](https://docs.expo.dev/workflow/customizing/). Ten en cuenta que, si realizas algún cambio en las opciones de configuración, deberás hacer el prebuild y ejecutar la aplicación de nuevo.

#### Método 2: Uso de React Native CLI {#method-2-using-react-native-cli}

##### Configura Android

**Paso 2.1: Añade el plugin de Kotlin Gradle**

El siguiente fragmento de código muestra cómo añadir el plugin de Kotlin Gradle en el archivo `build.gradle` de nivel superior de tu proyecto bajo `buildscript` > `dependencies`:

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

**Paso 2.2: Configura el SDK or kit de desarrollo de software de Braze**

Para conectarte a los servidores de Braze, crea un archivo `braze.xml` en la carpeta `res/values` de tu proyecto. El siguiente fragmento de código muestra un ejemplo de configuración de `braze.xml`. Reemplaza la [clave]({{site.baseurl}}/api/identifier_types) de API y el [endpoint]({{site.baseurl}}/api/basics#endpoints) con tus valores:

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
En la versión 12.2.0 o posterior del SDK or kit de desarrollo de software de Braze para Android, puedes incorporar automáticamente la biblioteca android-SDK or kit de desarrollo de software-location configurando `importBrazeLocationLibrary=true` en tu archivo `gradle.properties`.
{% endalert %}

**Paso 2.3: Implementa el seguimiento de sesiones de usuario**

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

**Paso 2.4: Gestiona las actualizaciones de intent**

Si tu MainActivity tiene `android:launchMode` configurado como `singleTask`, el siguiente fragmento de código muestra qué añadir a tu clase `MainActivity`:

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

##### Configura iOS

**Paso 2.5: (Opcional) Configura el Podfile para XCFrameworks dinámicos**

Para importar ciertas bibliotecas de Braze, como BrazeUI, en un archivo Objective-C++, debes usar la sintaxis `#import`. A partir de la versión `7.4.0` del SDK or kit de desarrollo de software Swift de Braze, los binarios tienen un [canal de distribución opcional como XCFrameworks dinámicos](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic), que son compatibles con esta sintaxis.

Si deseas usar este canal de distribución, sobrescribe manualmente las ubicaciones de origen de CocoaPods en tu Podfile. El siguiente fragmento de código muestra un ejemplo de sobrescritura. Reemplaza `{your-version}` con la versión relevante que deseas importar:

```ruby
pod 'BrazeKit', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeKit.podspec'
pod 'BrazeUI', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeUI.podspec'
pod 'BrazeLocation', :podspec => 'https://raw.githubusercontent.com/braze-inc/braze-swift-sdk-prebuilt-dynamic/{your-version}/BrazeLocation.podspec'
```

**Paso 2.6: Instala los pods**

Dado que React Native vincula automáticamente las bibliotecas a la plataforma nativa, puedes instalar el SDK or kit de desarrollo de software con la ayuda de CocoaPods.

El siguiente fragmento de código muestra cómo instalar los pods desde la carpeta raíz del proyecto:

```bash
# To install using the React Native New Architecture
cd ios && pod install

# To install using the React Native legacy architecture
cd ios && RCT_NEW_ARCH_ENABLED=0 pod install
```

**Paso 2.7: Configura el SDK or kit de desarrollo de software de Braze**

{% subtabs local %}
{% subtab SWIFT %}

El siguiente fragmento de código muestra cómo importar el SDK or kit de desarrollo de software de Braze en la parte superior del archivo `AppDelegate.swift`:
```swift
import BrazeKit
import braze_react_native_sdk
```

En el método `application(_:didFinishLaunchingWithOptions:)`, reemplaza la [clave]({{site.baseurl}}/api/identifier_types) de API y el [endpoint]({{site.baseurl}}/api/basics#endpoints) con los valores de tu aplicación. Luego, crea la instancia de Braze usando la configuración y crea una propiedad estática en el `AppDelegate` para un acceso sencillo.

{% alert note %}
Nuestro ejemplo asume una implementación de [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h), que proporciona una serie de abstracciones en la configuración de React Native. Si utilizas una configuración diferente para tu aplicación, asegúrate de ajustar tu implementación según sea necesario.
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

El siguiente fragmento de código muestra cómo importar el SDK or kit de desarrollo de software de Braze en la parte superior del archivo `AppDelegate.m`:
```objc
#import <BrazeKit/BrazeKit-Swift.h>
#import "BrazeReactBridge.h"
```

En el método `application:didFinishLaunchingWithOptions:`, reemplaza la [clave]({{site.baseurl}}/api/identifier_types) de API y el [endpoint]({{site.baseurl}}/api/basics#endpoints) con los valores de tu aplicación. Luego, crea la instancia de Braze usando la configuración y crea una propiedad estática en el `AppDelegate` para un acceso sencillo.

{% alert note %}
Nuestro ejemplo asume una implementación de [RCTAppDelegate](https://github.com/facebook/react-native/blob/e64756ae5bb5c0607a4d97a134620fafcb132b3b/packages/react-native/Libraries/AppDelegate/RCTAppDelegate.h), que proporciona una serie de abstracciones en la configuración de React Native. Si utilizas una configuración diferente para tu aplicación, asegúrate de ajustar tu implementación según sea necesario.
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

### Paso 3: Inicializa el SDK or kit de desarrollo de software {#step-3-initialize-the-sdk}

{% tabs %}
{% tab React Native SDK or kit de desarrollo de software 19.2.0+ %}

El siguiente fragmento de código muestra cómo importar la biblioteca en tu código de React Native:

```javascript
import Braze from "@braze/react-native-sdk";
```

{% alert note %}
React Native SDK or kit de desarrollo de software 19.2.0+ admite la inicialización de Braze desde la capa de React Native o desde las capas nativas de iOS y Android. Inicializa desde la capa de React Native para utilizar la [inicialización diferida](#delayed-initialization), que inicia el SDK or kit de desarrollo de software después de un evento como el consentimiento o el inicio de sesión. Si tu aplicación inicializa Braze en las capas nativas actualmente, puedes mantener esa configuración cuando actualices. Para confirmar cómo se comportan las notificaciones en cada configuración, consulta [Notificaciones push en arranque en frío](#push-notifications-on-cold-start).
{% endalert %}

Luego llama a `Braze.initialize()` con tu clave de API del identificador de la aplicación y el endpoint del SDK or kit de desarrollo de software para crear la instancia de Braze. Consulta las siguientes opciones sobre dónde llamar a este método en el flujo de tu aplicación.

#### Inicialización estándar {#standard-initialization}

El siguiente fragmento de código muestra cómo inicializar el SDK or kit de desarrollo de software cuando tu aplicación arranca llamando a `Braze.initialize()` en un `useEffect`:

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

El siguiente fragmento de código muestra cómo diferir la inicialización del SDK or kit de desarrollo de software hasta más adelante en la sesión. Por ejemplo, después de que el usuario otorgue su consentimiento o complete el inicio de sesión:

```javascript
function onUserConsent() {
  Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
}
```

{% alert warning %}
En iOS, las notificaciones push recibidas antes de `Braze.initialize()` se ponen en cola y se procesan después de la inicialización. En Android, Braze no resuelve los vínculos profundos de las notificaciones push mientras el SDK or kit de desarrollo de software espera ser inicializado. Para mantener las notificaciones funcionando cuando una de ellas lanza tu aplicación, consulta [Notificaciones push en arranque en frío](#push-notifications-on-cold-start).
{% endalert %}

#### Claves de API específicas por plataforma {#platform-specific-api-keys}

El siguiente fragmento de código muestra cómo usar la detección de plataforma cuando tus aplicaciones de Android e iOS usan claves de API diferentes:

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

Puedes llamar a `Braze.initialize()` varias veces para reinicializar el SDK or kit de desarrollo de software con una clave de API y endpoint diferentes a mitad de sesión. Cada llamada destruye la instancia anterior de Braze y crea una nueva.

{% alert important %}
Todas las llamadas a métodos del SDK or kit de desarrollo de software realizadas antes de `Braze.initialize()` se ignoran en iOS, así que llama a `Braze.initialize()` antes de usar cualquier otro método de Braze.
{% endalert %}

#### Notificaciones push en arranque en frío {#push-notifications-on-cold-start}

Cuando una notificación lanza tu aplicación desde un estado terminado, Braze almacena la carga útil de la notificación en la capa nativa antes de que React Native se cargue. Debido a esto, inicializar desde la capa de React Native no cambia si la carga útil llega a tu aplicación. Para gestionar estas notificaciones, añade los hooks nativos y luego lee la carga útil en tu código de React Native.

En Android, llama a `BrazeReactUtils.populateInitialPushPayloadFromIntent(intent)` en el método `onCreate()` de tu clase `MainActivity`:

```kotlin
import com.braze.reactbridge.BrazeReactUtils

override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    BrazeReactUtils.populateInitialPushPayloadFromIntent(intent)
}
```

En iOS, llama a `populateInitialPayload(fromLaunchOptions:)` en el método `application(_:didFinishLaunchingWithOptions:)` de tu `AppDelegate`:

```swift
if let launchOptions {
  BrazeReactUtils.sharedInstance().populateInitialPayload(fromLaunchOptions: launchOptions)
}
```

Luego, lee la carga útil en tu código de React Native:

```javascript
Braze.getInitialPushPayload((pushPayload) => {
  if (pushPayload) {
    // Handle the notification, such as navigating to the pushPayload.url value
  }
});
```

{% alert important %}
Cuando la inicialización diferida está habilitada en Android, Braze abre tu actividad principal en lugar de resolver el vínculo profundo de la notificación, y luego pasa los datos de la notificación a esa actividad. Gestiona la navegación en tu código de React Native usando el valor `url` de `Braze.getInitialPushPayload()`.
{% endalert %}

La configuración de registro push se mantiene en tu configuración nativa para ambas ubicaciones de inicialización, y Braze la aplica cuando se ejecuta `Braze.initialize()`:

- En Android, configura `com_braze_firebase_cloud_messaging_registration_enabled` y `com_braze_firebase_cloud_messaging_sender_id` en `braze.xml`.
- En iOS, configura las propiedades de `push` en el objeto de configuración dentro del closure `configure` que pasas a `BrazeReactInitializer.configure`.

Si tu aplicación depende de vínculos profundos de notificaciones que la lanzan desde un estado terminado, usa React Native SDK or kit de desarrollo de software 21.1.0 o posterior. Estas versiones incluyen correcciones para capturar la carga útil push inicial y resolver vínculos profundos de push en Android. Para la lista completa de cambios, consulta el [registro de cambios del SDK or kit de desarrollo de software de React Native](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md).

{% endtab %}
{% tab React Native SDK or kit de desarrollo de software 19.1.0 y anteriores %}

Para React Native SDK or kit de desarrollo de software 19.1.0 y anteriores, la inicialización nativa ocurre en el paso 2. Importa la biblioteca en tu código de React Native para llamar a los métodos de Braze. Para más detalles, consulta nuestro [proyecto de ejemplo](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject).

```javascript
import Braze from "@braze/react-native-sdk";
```

{% endtab %}
{% endtabs %}

### Paso 4: Prueba la integración (opcional) {#step-4-test-the-integration-optional}

{% tabs %}
{% tab React Native SDK or kit de desarrollo de software 19.2.0+ %}

Puedes verificar que el SDK or kit de desarrollo de software está integrado comprobando las estadísticas de sesión en el panel. Si ejecutas tu aplicación en cualquiera de las plataformas, deberías ver una nueva sesión en el panel (en la sección **Resumen**).

El siguiente fragmento de código muestra cómo abrir una sesión para un usuario particular en tu aplicación:

```javascript
import Braze from "@braze/react-native-sdk";

Braze.initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT");
Braze.changeUser("{some-user-id}");
```

Busca al usuario con `{some-user-id}` en el panel en **Audiencia** > **Buscar usuarios**. Allí puedes verificar que los datos de sesión y dispositivo se hayan registrado.

{% endtab %}
{% tab React Native SDK or kit de desarrollo de software 19.1.0 y anteriores %}

Para probar tu integración del SDK or kit de desarrollo de software, el siguiente fragmento de código muestra cómo iniciar una nueva sesión en cualquiera de las plataformas para un usuario.

```javascript
Braze.changeUser("userId");
```

El siguiente fragmento de código muestra un ejemplo de asignación del ID de usuario al inicio de la aplicación:

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

En el panel de Braze, ve a [Búsqueda de usuarios]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search#using-user-search) y busca al usuario con el ID que coincida con `some-user-id`. Allí puedes verificar que los datos de sesión y dispositivo se hayan registrado.

{% endtab %}
{% endtabs %}

## Pruebas con Jest {#testing-with-jest}

Las pruebas unitarias de React Native que importan el SDK or kit de desarrollo de software de Braze necesitan mocks para los módulos nativos y el Turbo Module de Braze. El [repositorio del SDK or kit de desarrollo de software de Braze para React Native](https://github.com/braze-inc/braze-react-native-sdk) incluye una configuración de referencia para Jest en [`__tests__/jest.setup.js`](https://github.com/braze-inc/braze-react-native-sdk/blob/master/__tests__/jest.setup.js). Añade ese archivo (o una copia adaptada) a `setupFiles` en tu configuración de Jest para que `NativeEventEmitter`, `TurboModuleRegistry` y `BrazeReactBridge` tengan mocks cuando pruebes componentes que llaman a las API de Braze.

## Próximos pasos {#next-steps}

Después de integrar el SDK or kit de desarrollo de software de Braze, puedes empezar a implementar las características de mensajería más comunes:

- [Notificaciones push]({{site.baseurl}}/developer_guide/push_notifications): Configura y envía notificaciones push a tus usuarios.
- [In-App Messages]({{site.baseurl}}/developer_guide/in_app_messages): Muestra mensajes contextuales dentro de tu aplicación.
- [Banners]({{site.baseurl}}/developer_guide/banners): Muestra banners persistentes en la interfaz de tu aplicación.