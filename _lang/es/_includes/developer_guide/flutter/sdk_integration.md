## Acerca del SDK or kit de desarrollo de software de Flutter Braze {#about-the-flutter-braze-sdk}

Después de integrar el SDK or kit de desarrollo de software de Braze Flutter en Android e iOS, podrás utilizar la API de Braze en tus [aplicaciones Flutter](https://flutter.dev/) escritas en Dart. Este complemento proporciona una funcionalidad básica de análisis y te permite integrar mensajes dentro de la aplicación y Content Cards tanto para iOS como para Android con una única base de código.

## Integración del SDK or kit de desarrollo de software de Flutter {#integrating-the-flutter-sdk}

### Requisitos previos {#prerequisites}

Antes de integrar el SDK or kit de desarrollo de software de Braze Flutter, deberás completar lo siguiente:

| Requisito previo | Descripción |
| --- | --- |
| Identificador de aplicación de la API de Braze | Para localizar el identificador de tu aplicación, ve a **Configuración** > **API e identificadores** > **Identificadores de aplicaciones**. Para más información, consulta [Tipos de identificadores de API]({{site.baseurl}}/api/identifier_types#app-identifier).|
| Punto final de SDK or kit de desarrollo de software de Braze | La URL de tu punto final de SDK or kit de desarrollo de software (por ejemplo, `sdk.<cluster>.braze.com`). Tu punto final dependerá de la [URL de Braze para tu instancia]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints).|
| SDK or kit de desarrollo de software de Flutter | Instala el [SDK or kit de desarrollo de software de Flutter](https://docs.flutter.dev/get-started/install) oficial y asegúrate de que cumple con la [versión mínima compatible](https://github.com/braze-inc/braze-flutter-sdk#requirements) del SDK or kit de desarrollo de software de Braze Flutter. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

### Paso 1: Integrar la biblioteca de Braze {#step-1-integrate-the-braze-library}

Añade el paquete del SDK or kit de desarrollo de software de Braze Flutter desde la línea de comandos. Esto añadirá la línea correspondiente a tu `pubspec.yaml`.

```bash
flutter pub add braze_plugin
```

### Paso 2: Completar la configuración del SDK or kit de desarrollo de software nativo {#step-2-complete-native-sdk-setup}

{% tabs %}
{% tab Flutter SDK or kit de desarrollo de software 18.0.0+ %}

#### 2.1 Configurar Android {#21-set-up-android} {#21-set-up-android}

##### Proporcionar credenciales en tiempo de compilación {#provide-credentials-at-compile-time}

Crea un archivo `braze.xml` en la carpeta `android/res/values` de tu proyecto. La clave de API y el punto final se proporcionan en tiempo de ejecución desde Dart, por lo que no son necesarios en este archivo. Para habilitar la inicialización diferida, añade `com_braze_enable_delayed_initialization` al archivo:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <bool name="com_braze_enable_delayed_initialization">true</bool>
  <!-- API key and endpoint are not required here. They are set at runtime via Dart. -->
</resources>
```

##### Proporcionar credenciales en tiempo de ejecución {#provide-credentials-at-runtime}

Alternativamente, puedes habilitar la inicialización diferida de forma programática en tu `MainActivity.kt`:

```kotlin
import com.braze.Braze

class MainActivity : FlutterActivity() {
  override fun onCreate(savedInstanceState: Bundle?) {
    super.onCreate(savedInstanceState)
    Braze.enableDelayedInitialization(context = this)
  }
}
```

Añade los permisos necesarios a tu archivo `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

#### 2.2 Configurar iOS {#22-set-up-ios} {#22-set-up-ios}

Dentro de tu método `application(_:didFinishLaunchingWithOptions:)` existente, añade una llamada a `BrazePlugin.configure(_:postInitialization:)` para almacenar tu configuración. La instancia de Braze se crea más tarde cuando se llama a `initialize()` desde Dart. La clave de API y el punto final no se configuran aquí.

{% subtabs %}
{% subtab SWIFT %}

Añade el siguiente código a tu `AppDelegate.swift`:

```swift
import BrazeKit
import braze_plugin

// ...

override func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
  // ... your existing didFinishLaunchingWithOptions setup ...

  BrazePlugin.configure(
    { configuration in
      configuration.logger.level = .info
      // Set other non-API-key configurations here, such as:
      // configuration.push.automation = true
      // configuration.sessionTimeout = 60
    },
    postInitialization: { braze in
      // Optional: Customize the Braze instance after creation.
      // For example, set a custom in-app message presenter:
      // let customPresenter = CustomInAppMessagePresenter()
      // braze.inAppMessagePresenter = customPresenter
    }
  )

  return true
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Añade el siguiente código a tu `AppDelegate.m`:

```objc
@import BrazeKit;
@import braze_plugin;

// ...

- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [BrazePlugin configure:^(BRZConfiguration *configuration) {
    configuration.logger.level = BRZLoggerLevelInfo;
    // Set other non-API-key configurations here, such as:
    // configuration.push.automation = ...
    // configuration.sessionTimeout = 60;
  } postInitialization:^(Braze *braze) {
    // Optional: customize the Braze instance after creation.
  }];

  return YES;
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
`BrazePlugin.configure()` solo almacena tu configuración. No existe ninguna instancia de Braze hasta que se llama a `initialize()` desde Dart, por lo que no debes llamar a ningún método del SDK or kit de desarrollo de software de Braze en el AppDelegate después de `configure()`.
{% endalert %}

{% endtab %}
{% tab Flutter SDK or kit de desarrollo de software 17.1.0 and earlier %}

#### 2.1 Configurar Android {#21-set-up-android-1}

Para conectarte a los servidores de Braze, crea un archivo `braze.xml` en la carpeta `android/res/values` de tu proyecto. Pega el siguiente código y sustituye la clave de identificador de API y el punto final por tus valores:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

Añade los permisos necesarios a tu archivo `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

#### 2.2 Configurar iOS {#22-set-up-ios-1}

{% subtabs %}
{% subtab SWIFT %}
Añade las importaciones del SDK or kit de desarrollo de software de Braze en la parte superior del archivo `AppDelegate.swift`:
```swift
import BrazeKit
import braze_plugin
```

En el mismo archivo, crea el objeto de configuración de Braze en el método `application(_:didFinishLaunchingWithOptions:)` y sustituye la clave de API y el punto final por los valores de tu aplicación. A continuación, crea la instancia de Braze utilizando la configuración y crea una propiedad estática en `AppDelegate` para facilitar el acceso:

```swift
static var braze: Braze? = nil

override func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]? = nil
) -> Bool {
  // Setup Braze
  let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>"
  )
  // - Enable logging or customize configuration here
  configuration.logger.level = .info
  let braze = BrazePlugin.initBraze(configuration)
  AppDelegate.braze = braze

  return true
}
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}
Importa el SDK or kit de desarrollo de software de Braze en la parte superior del archivo `AppDelegate.m`:
```objc
@import BrazeKit;
@import braze_plugin;
```

En el mismo archivo, crea el objeto de configuración de Braze en el método `application:didFinishLaunchingWithOptions:` y sustituye la clave de API y el punto final por los valores de tu aplicación. A continuación, crea la instancia de Braze utilizando la configuración y crea una propiedad estática en `AppDelegate` para facilitar el acceso:

```objc
- (BOOL)application:(UIApplication *)application
    didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Setup Braze
  BRZConfiguration *configuration =
      [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                      endpoint:@"<BRAZE_ENDPOINT>"];
  // - Enable logging or customize configuration here
  configuration.logger.level = BRZLoggerLevelInfo;
  Braze *braze = [BrazePlugin initBraze:configuration];
  AppDelegate.braze = braze;

  [self.window makeKeyAndVisible];
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

### Paso 3: Configurar el complemento {#step-3-set-up-the-plugin}

{% tabs %}
{% tab Flutter SDK or kit de desarrollo de software 18.0.0+ %}

Importa el complemento y crea una única instancia de `BrazePlugin`:

```dart
import 'package:braze_plugin/braze_plugin.dart';

final BrazePlugin braze = BrazePlugin();
```

Luego llama a `initialize()` con tu clave de API del identificador de aplicación y el punto final de SDK or kit de desarrollo de software para crear la instancia de Braze. Consulta las siguientes opciones para saber dónde llamar a este método en el flujo de tu aplicación.

#### Inicialización estándar {#standard-initialization}

Para inicializar el SDK or kit de desarrollo de software cuando tu aplicación se inicia, llama a `initialize()` en `initState()`:

```dart
@override
void initState() {
  super.initState();
  braze.initialize("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
}
```

#### Inicialización diferida {#delayed-initialization}

Para aplazar la inicialización del SDK or kit de desarrollo de software hasta un momento posterior en la sesión —por ejemplo, después de que el usuario otorgue su consentimiento o complete el inicio de sesión— llama a `initialize()` cuando estés listo:

```dart
// ...
void onUserConsent() {
  braze.initialize("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
}
```

{% alert warning %}
Las notificaciones push y los vínculos profundos recibidos antes de llamar a `initialize()` no se procesan en iOS. En Android, los vínculos profundos de las notificaciones push no se resuelven mientras el SDK or kit de desarrollo de software está esperando ser inicializado. Si tu aplicación depende de notificaciones push o vínculos profundos al inicio, utiliza la [inicialización estándar](#standard-initialization) en su lugar.
{% endalert %}

#### Claves de API específicas por plataforma {#platform-specific-api-keys}

Dado que tus aplicaciones de Android e iOS utilizan claves de API diferentes, usa la detección de plataforma:

```dart
import 'dart:io' show Platform;

if (Platform.isAndroid) {
  braze.initialize("<ANDROID_API_KEY>", "<BRAZE_ENDPOINT>");
} else if (Platform.isIOS) {
  braze.initialize("<IOS_API_KEY>", "<BRAZE_ENDPOINT>");
}
```

#### Reinicialización {#re-initialization}

Puedes llamar a `initialize()` varias veces para reinicializar el SDK or kit de desarrollo de software con una clave de API y un punto final diferentes durante la sesión. Cada llamada destruye la instancia de Braze anterior y crea una nueva.

{% alert important %}
Para evitar comportamientos indefinidos, asigna y utiliza una única instancia de `BrazePlugin` en tu código Dart. Todas las llamadas a métodos del SDK or kit de desarrollo de software realizadas antes de `initialize()` se ignoran en iOS, así que llama a `initialize()` antes de usar cualquier otro método de Braze.
{% endalert %}

{% endtab %}
{% tab Flutter SDK or kit de desarrollo de software 17.1.0 and earlier %}

Para importar el complemento en tu código Dart, utiliza lo siguiente:

```dart
import 'package:braze_plugin/braze_plugin.dart';
```

A continuación, inicializa una instancia del complemento de Braze llamando a `new BrazePlugin()` como en [nuestra aplicación de ejemplo](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/lib/main.dart).

{% alert important %}
Para evitar comportamientos indefinidos, asigna y utiliza una única instancia de `BrazePlugin` en tu código Dart.
{% endalert %}

{% endtab %}
{% endtabs %}

## Probar la integración {#testing-the-integration}

Puedes verificar que el SDK or kit de desarrollo de software está integrado comprobando las estadísticas de sesión en el panel. Si ejecutas tu aplicación en cualquiera de las dos plataformas, deberías ver una nueva sesión en el panel (en la sección **Overview**).

Abre una sesión para un usuario concreto llamando al siguiente código en tu aplicación.

{% tabs %}
{% tab Flutter SDK or kit de desarrollo de software 18.0.0+ %}

```dart
BrazePlugin braze = BrazePlugin();
braze.initialize("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
braze.changeUser("{some-user-id}");
```

{% endtab %}
{% tab Flutter SDK or kit de desarrollo de software 17.1.0 and earlier %}

```dart
BrazePlugin braze = BrazePlugin();
braze.changeUser("{some-user-id}");
```

{% endtab %}
{% endtabs %}

Busca al usuario con `{some-user-id}` en el panel, en **Audience** > **Search Users**. Allí podrás comprobar que se han registrado los datos de sesión y de dispositivo.