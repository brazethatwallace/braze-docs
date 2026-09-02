---
nav_title: Guía de integración de SDK (opcional)
article_title: Guía de integración de Braze SDK para iOS (opcional)
alias: "/ios_sdk/"
description: "Esta guía de integración de iOS te lleva paso a paso por las mejores prácticas de configuración a la hora de integrar por primera vez el SDK de iOS y sus componentes principales en tu aplicación. Esta guía te ayudará a crear un archivo de ayuda BrazeManager.swift."
page_order: 10
platform: iOS

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Guía de integración del SDK de Braze para iOS {#braze-ios-sdk-integration-guide}

> Esta guía opcional de integración de iOS te lleva paso a paso por las mejores prácticas de configuración al integrar por primera vez el SDK de iOS y sus componentes principales en tu aplicación. Esta guía te ayudará a crear un archivo de ayuda `BrazeManager.swift` que desacoplará cualquier dependencia del SDK de Braze para iOS del resto de tu código de producción, dando como resultado un único `import AppboyUI` en toda tu aplicación. Este enfoque limita los problemas que surgen de un exceso de importaciones del SDK, lo que facilita el seguimiento, la depuración y la modificación del código.

{% alert important %}
Esta guía asume que ya has [añadido el SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview) a tu proyecto Xcode.
{% endalert %}

## Resumen de la integración {#integration-overview}

Los siguientes pasos te ayudan a crear un archivo auxiliar `BrazeManager` al que tu código de producción puede invocar. Este archivo auxiliar se encargará de todas las dependencias relacionadas con Braze al agregar varias extensiones para los siguientes temas de integración listados. Cada tema incluirá pasos en pestañas horizontales y fragmentos de código tanto en Swift como en Objective-C. Ten en cuenta que los pasos de Content Cards y mensajes dentro de la aplicación no son necesarios para la integración si no planeas usar estos canales en tu aplicación.

- [Crear BrazeManager.swift](#create-brazemanagerswift)
- [Inicializar el SDK](#initialize-the-sdk)
- [Notificaciones push](#push-notifications)
- [Acceder a variables y métodos de usuario](#access-user-variables-and-methods)
- [Registrar análisis](#log-analytics)
- [Mensajes dentro de la aplicación (opcional)](#in-app-messages)
- [Content Cards (opcional)](#content-cards)
- [Próximos pasos](#next-steps)

### Crear BrazeManager.swift {#create-brazemanagerswift}

{% tabs local %}
{% tab Create BrazeManager swift %}

#### Crear BrazeManager.swift
Para construir tu archivo `BrazeManager.swift`, crea un nuevo archivo Swift llamado _BrazeManager_ para agregarlo a tu proyecto en la ubicación deseada. A continuación, reemplaza `import Foundation` con `import AppboyUI` para SPM (`import Appboy_iOS_SDK` para CocoaPods) y luego crea una clase `BrazeManager` que se usará para alojar todos los métodos y variables relacionados con Braze. `Appboy_iOS_SDK`

{% alert note %}
- `BrazeManager` es una clase `NSObject` y no un struct, por lo que puede conformar con delegados ABK como `ABKInAppMessageUIDelegate`.
- `BrazeManager` es una clase singleton por diseño, de modo que solo se usará una instancia de esta clase. Esto se hace para proporcionar un punto de acceso unificado al objeto.
{% endalert %}

1. Agrega una variable estática llamada _shared_ que inicializa la clase `BrazeManager`. Se garantiza que será iniciada de forma perezosa solo una vez.
2. A continuación, agrega una variable constante privada llamada _apiKey_ y establécela como el valor de clave de API de tu espacio de trabajo en el panel de Braze.
3. Agrega una variable computada privada llamada _appboyOptions_, que almacenará valores de configuración para el SDK. Estará vacía por ahora.

{% subtabs global %}
{% subtab Swift %}

```swift
class BrazeManager: NSObject {
  // 1
  static let shared = BrazeManager()

  // 2
  private let apikey = "YOUR-API-KEY"

  // 3
  private var appboyOptions: [String:Any] {
    return [:]
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
@implementation BrazeManager

// 1
+ (instancetype)shared {
    static BrazeManager *shared = nil;
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        shared = [[BrazeManager alloc] init];
        // Do any other initialisation stuff here
    });
    return shared;
}

// 2
- (NSString *)apiKey {
  return @"YOUR-API-KEY";
}

// 3
- (NSDictionary *)appboyOptions {
  return [NSDictionary dictionary];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Inicializar el SDK {#initialize-the-sdk}

{% tabs local %}
{% tab Step 1: Initialize SDK from BrazeManager swift %}

#### Inicializar el SDK desde BrazeManager.swift {#initialize-sdk-from-brazemanagerswift}
A continuación, debes inicializar el SDK. Esta guía asume que ya has [agregado el SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview) a tu proyecto Xcode. También debes tener configurados tu [endpoint del SDK del espacio de trabajo]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration#step-2-specify-your-data-cluster) y [`LogLevel`]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations#braze-log-level) en tu archivo `Info.plist` o en `appboyOptions`.

Agrega el método `didFinishLaunchingWithOptions` del archivo `AppDelegate.swift` sin un tipo de retorno en tu archivo `BrazeManager.swift`. Al crear un método similar en el archivo `BrazeManager.swift`, no habrá una declaración `import AppboyUI` en tu archivo `AppDelegate.swift`.

A continuación, inicializa el SDK usando tus variables `apiKey` y `appboyOptions` recién declaradas.

{% alert important %}
La inicialización debe realizarse en el hilo principal.
{% endalert %}

{% subtabs global %}
{% subtab Swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {
  Appboy.start(withApiKey: apikey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];
}
```
{% endsubtab %}
{% endsubtabs %}

{% endtab %}
{% tab Step 2: Handle Appboy Initialization %}

##### Gestionar la inicialización de Appboy en AppDelegate.swift {#handle-appboy-initialization-in-the-appdelegateswift}
A continuación, navega de vuelta al archivo `AppDelegate.swift` y agrega el siguiente fragmento de código en el método `didFinishLaunchingWithOptions` del AppDelegate para gestionar la inicialización de Appboy desde el archivo auxiliar `BrazeManager.swift`. Recuerda, no es necesario agregar una declaración `import AppboyUI` en el `AppDelegate.swift`.

{% subtabs global %}
{% subtab Swift %}

```swift
func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
) -> Bool {
  // Override point for customization after application launch

  BrazeManager.shared.application(application, didFinishLaunchingWithOptions: launchOptions)

  return true
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  // Override point for customization after application launch

  [[BrazeManager shared] application:application didFinishLaunchingWithOptions:launchOptions];

  return YES;
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Procede a compilar tu código y ejecutar tu aplicación.<br><br>En este punto, el SDK debería estar en funcionamiento. En tu panel, observa que las sesiones se están registrando antes de avanzar.
{% endalert %}

### Notificaciones push {#push-notifications}

{% tabs local %}
{% tab Step 1: Add Push Certificate %}

#### Agregar certificado push {#add-push-certificate}

Navega a tu espacio de trabajo existente en el panel de Braze. En **Push Notification Settings** sube tu archivo de certificado push a tu panel de Braze y guárdalo.

![Configuración de notificaciones push del panel de Braze con campos de carga de clave de APN.]({% image_buster /assets/img/ios_sdk/ios_sdk2.png %}){: style="max-width:60%;"}

{% endtab %}
{% tab Step 2: Register for Notifications %}

{% alert important %}
¡No te pierdas el checkpoint dedicado al final de este paso!
{% endalert %}

##### Registrarse para notificaciones push {#register-for-push-notifications}

A continuación, regístrate para notificaciones push. Esta guía asume que has [configurado tus credenciales push correctamente]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) en tu portal de desarrollador de Apple y en tu proyecto Xcode.

El código para registrar notificaciones push se agregará en el método `didFinishLaunching...` del archivo `BrazeManager.swift`. Tu código de inicialización debería quedar así:

1. Configura los contenidos para solicitar autorización para interactuar con el usuario. Estas opciones se listan como ejemplo.
2. Solicita autorización para enviar notificaciones push a tus usuarios. La respuesta del usuario para permitir o denegar las notificaciones push se rastrea en la variable `granted`.
3. Reenvía los resultados de autorización push a Braze después de que el usuario interactúe con el aviso de notificación.
4. Inicia el proceso de registro con APN; esto debe hacerse en el hilo principal. Si el registro es exitoso, la aplicación llama al método `didRegisterForRemoteNotificationsWithDeviceToken` del objeto `AppDelegate`.

{% subtabs global %}
{% subtab Swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions:[UIApplication.LaunchOptionsKey:Any]?) {
  Appboy.start(withAPIKey: apikey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)
  // 1
  let options: UNAuthorizationOptions = [.alert, .sound, .badge]
  // 2
  UNUserNotificationCenter.current().requestAuthorization(option: options) { (granted, error) in
  // 3
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }

  // 4
  UIApplications.shared.registerForRemoteNotificiations()
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];

  // 1
  UNAuthorizationOptions options = (UNAuthorizationOptionSound | UNAuthorizationOptionAlert | UNAuthorizationOptionBadge);

  // 2
  [[UNUserNotificationCenter currentNotificationCenter] requestAuthorizationWithOptions:options completionHandler:^(BOOL granted, NSError * _Nullable error) {
  // 3
    [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];

  // 4
  [[UIApplication sharedApplication] registerForRemoteNotifications];
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert checkpoint %}
Procede a compilar tu código y ejecutar tu aplicación.
- En tu aplicación, confirma que se te solicita permiso para notificaciones push antes de avanzar.
- Si no se te solicita, intenta eliminar y reinstalar la aplicación para asegurarte de que el aviso de notificación push no se haya mostrado anteriormente.

Observa que se te solicita permiso para notificaciones push antes de avanzar.
{% endalert %}

{% endtab %}
{% tab Step 3: Forward Methods %}

##### Reenviar métodos de notificación push {#forward-push-notification-methods}

A continuación, reenvía los métodos del sistema de notificaciones push desde `AppDelegate.swift` a `BrazeManager.swift` para ser gestionados por el SDK de Braze para iOS.

###### Paso 1: Crear extensión para código de notificación push {#step-1-create-extension-for-push-notification-code}

Crea una extensión para tu código de notificación push en tu archivo `BrazeManager.swift` para que se lea de manera más organizada en cuanto a qué propósito se cumple en el archivo auxiliar, de esta forma:

1. Siguiendo el patrón de no incluir una declaración `import AppboyUI` en tu `AppDelegate`, gestionaremos los métodos de notificación push en el archivo `BrazeManager.swift`. Los tokens de dispositivo de los usuarios deberán pasarse a Braze desde el método `didRegisterForRemote...`. Este método es necesario para implementar notificaciones push silenciosas. A continuación, agrega el mismo método del `AppDelegate` en tu clase `BrazeManager`.
2. Agrega la siguiente línea dentro del método para registrar el token de dispositivo en Braze. Esto es necesario para que Braze asocie el token con el dispositivo actual.

{% subtabs global %}
{% subtab Swift %}

```swift
// MARK - Push Notifications
extension BrazeManager {
  // 1
  func application(
    _ application: UIApplication,
    didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data
  ) {
    // 2
    Appboy.sharedInstance().?registerDeviceToken(deviceToken)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK - Push Notifications
// 1
- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(NSData *)deviceToken {
  // 2
  [[Appboy sharedInstance] registerDeviceToken:deviceToken];
}
```
{% endsubtab %}
{% endsubtabs %}

###### Paso 2: Dar soporte a notificaciones remotas {#step-2-support-remote-notifications}
En la pestaña **Signing & Capabilities**, agrega soporte de **Background Modes** y selecciona **Remote notifications** para comenzar tu soporte de notificaciones push remotas originadas desde Braze.<br><br>![Signing & Capabilities]({% image_buster /assets/img/ios_sdk/ios_sdk3.png %})

###### Paso 3: Gestión de notificaciones remotas {#step-3-remote-notification-handling}
El SDK de Braze puede gestionar notificaciones push remotas que se originen desde Braze. Reenvía las notificaciones remotas a Braze; el SDK ignorará automáticamente las notificaciones push que no se originen desde Braze. Agrega el siguiente método a tu archivo `BrazeManager.swift` en la extensión de notificaciones push.

{% subtabs global %}
{% subtab Swift %}
```swift
func application(
  _ application: UIApplication,
  didReceiveRemoteNotification userInfo: [AnyHashable : Any],
  fetchCompletionHandler completionHandler: @escaping (UIBackgroundFetchResult) -> Void
) {
  Appboy.sharedInstance()?.register(
    application,
    didReceiveRemoteNotification: userInfo,
    fetchCompletionHandler: completionHandler
  )
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didReceiveRemoteNotification:(NSDictionary *)userInfo fetchCompletionHandler:(void (^)(UIBackgroundFetchResult))completionHandler {
  [[Appboy sharedInstance] registerApplication:application didReceiveRemoteNotification:userInfo fetchCompletionHandler:completionHandler];
}
```
{% endsubtab %}
{% endsubtabs %}

###### Paso 4: Reenviar respuestas de notificación {#step-4-forward-notification-responses}

El SDK de Braze puede gestionar la respuesta de las notificaciones push que se originen desde Braze. Reenvía la respuesta de las notificaciones a Braze; el SDK ignorará automáticamente las respuestas de notificaciones push que no se originen desde Braze. Agrega el siguiente método a tu archivo `BrazeManager.swift`:

{% subtabs global %}
{% subtab Swift %}

```swift
func userNotificationCenter(
  _ center: UNUserNotificationCenter,
  didReceive response: UNNotificationResponse,
  withCompletionHandler completionHandler: @escaping () -> Void
) {
  Appboy.sharedInstance()?.userNotificationCenter(
    center,
    didReceive: response,
    withCompletionHandler: completionHandler
  )
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)userNotificationCenter:(UNUserNotificationCenter *)center
didReceiveNotificationResponse:(UNNotificationResponse *)response
         withCompletionHandler:(void (^)(void))completionHandler {
  [[Appboy sharedInstance] userNotificationCenter:center
                   didReceiveNotificationResponse:response
                            withCompletionHandler:completionHandler];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Procede a compilar tu código y ejecutar tu aplicación. <br><br>Intenta enviarte una notificación push desde el panel de Braze y observa que los análisis se están registrando desde las notificaciones push antes de avanzar.
{% endalert %}

### Acceder a variables y métodos de usuario {#access-user-variables-and-methods}

{% tabs local %}
{% tab Create User Variables and Methods %}

#### Crear variables y métodos de usuario {#create-user-variables-and-methods}

A continuación, querrás tener acceso fácil a las variables y métodos de `ABKUser`. Crea una extensión para tu código de usuario en el archivo `BrazeManager.swift` para que se lea de manera más organizada en cuanto a qué propósito se cumple en el archivo auxiliar, de esta forma:

1. Un objeto `ABKUser` representa un usuario conocido o anónimo en tu aplicación iOS. Agrega una variable computada para obtener el `ABKUser`; esta variable se reutilizará para recuperar variables sobre el usuario.
2. Consulta la variable de usuario para acceder fácilmente al `userId`. Entre las otras variables, el objeto `ABKUser` es responsable de (`firstName`, `lastName`, `phone`, `homeCity`, etc.)
3. Establece el usuario llamando a `changeUser()` con un `userId` correspondiente.

{% subtabs global %}
{% subtab Swift %}

```swift
// MARK: - User
extension BrazeManager {
  // 1
  var user: ABKUser? {
    return Appboy.sharedInstance()?.user
  }

  // 2
  var userId: String? {
    return user?.userID
  }

  // 3
  func changeUser(_ userId: String) {
    Appboy.sharedInstance()?.changeUser(userId)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - User
  // 1
- (ABKUser *)user {
  return [[Appboy sharedInstance] user];
}

   // 2
- (NSString *)userId {
  return [self user].userID;
}

  // 3
- (void)changeUser:(NSString *)userId {
  [[Appboy sharedInstance] changeUser:userId];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Procede a compilar tu código y ejecutar tu aplicación.<br><br>Intenta identificar usuarios desde un inicio de sesión/registro exitoso. Asegúrate de tener una comprensión sólida de lo que es y lo que no es un identificador de usuario apropiado. <br><br>En tu panel, observa que el identificador de usuario se registra antes de avanzar.
{% endalert %}

### Registrar análisis {#log-analytics}

{% tabs local %}
{% tab Step 1: Custom Events %}

#### Crear método para registrar eventos personalizados {#create-log-custom-event-method}

Basándote en el siguiente método `logCustomEvent` del SDK de Braze, crea un método equivalente.

**Método de referencia `logCustomEvent` de Braze**<br>
Esto es por diseño porque solo el archivo `BrazeManager.swift` puede acceder directamente a los métodos del SDK de Braze para iOS. Por lo tanto, al crear un método equivalente, el resultado es el mismo y se hace sin necesidad de dependencias directas del SDK de Braze para iOS en tu código de producción.

```
open func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable : Any]?)
```

**Método equivalente**<br>
Registra eventos personalizados desde el objeto `Appboy` hacia Braze. `Properties` es un parámetro opcional con un valor predeterminado de nil. Los eventos personalizados no requieren tener propiedades, pero sí requieren tener un nombre.

{% subtabs global %}
{% subtab Swift %}
```swift
func logCustomEvent(_ eventName: String, withProperties properties: [AnyHashable: Any]? = nil) {
  Appboy.sharedInstance()?.logCustomEvent(eventName, withProperties: properties)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logCustomEvent:(NSString *)eventName withProperties:(nullable NSDictionary *)properties {
  [[Appboy sharedInstance] logCustomEvent:eventName withProperties:properties];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Step 2: Custom Attributes %}

##### Crear método para registrar atributos personalizados {#create-log-custom-attributes-method}

El SDK puede registrar numerosos tipos como atributos personalizados. No es necesario crear métodos auxiliares para cada tipo de valor que se pueda establecer. En su lugar, solo expón un método que pueda filtrar hacia el valor apropiado.

```
- (BOOL)setCustomAttributeWithKey:(NSString *)key andBOOLValue:(BOOL)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andIntegerValue:(NSIntenger)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDoubleValue:(double)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andStringValue:(NSString *)value;
- (BOOL)setCustomAttributeWithKey:(NSString *)key andDateValue:(NSDate *)value;
```

Los atributos personalizados se registran desde el objeto `ABKUser`.

Crea **un método** que pueda abarcar todos los tipos disponibles que se pueden establecer para un atributo. Agrega este método en tu archivo `BrazeManager.swift` en la extensión de análisis. Esto se puede lograr filtrando a través de los tipos de atributos personalizados válidos y llamando al método asociado con el tipo coincidente.

- El parámetro `value` es un tipo genérico que se conforma al protocolo `Equatable`. Esto se hace explícitamente para que, si el tipo no es lo que el SDK de Braze para iOS espera, se produzca un error en tiempo de compilación.
- Los parámetros `key` y `value` son parámetros opcionales que serán desenvueltos condicionalmente en el método. Esta es solo una forma de asegurar que se pasen valores no nulos al SDK de Braze para iOS.

{% subtabs global %}
{% subtab Swift %}

```swift
func setCustomAttributeWithKey<T: Equatable>(_ key: String?, andValue value: T?) {
  guard let key = key, let value = value else { return }
  switch value.self {
  case let value as Date:
    user?.setCustomAttributeWithKey(key, andDateValue: value)
  case let value as Bool:
    user?.setCustomAttributeWithKey(key, andBOOLValue: value)
  case let value as String:
    user?.setCustomAttributeWithKey(key, andStringValue: value)
  case let value as Double:
    user?.setCustomAttributeWithKey(key, andDoubleValue: value)
  case let value as Int:
    user?.setCustomAttributeWithKey(key, andIntegerValue: value)
  default:
   return
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)setCustomAttributeWith:(NSString *)key andValue:(id)value {
  if ([value isKindOfClass:[NSDate class]]) {
    [[self user] setCustomAttributeWithKey:key andDateValue:value];
  } else if ([value isKindOfClass:[NSString class]]) {
    [[self user] setCustomAttributeWithKey:key andStringValue:value];
  } else if ([value isKindOfClass:[NSNumber class]]) {
    if (strcmp([value objCType], @encode(double)) == 0) {
      [[self user] setCustomAttributeWithKey:key andDoubleValue:[value doubleValue]];
    } else if (strcmp([value objCType], @encode(int)) == 0) {
      [[self user] setCustomAttributeWithKey:key andIntegerValue:[value integerValue]];
    } else if ([value boolValue]) {
      [[self user] setCustomAttributeWithKey:key andBOOLValue:[value boolValue]];
    }
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Step 3: Purchases %}

##### Crear método para registrar compras {#create-log-purchase-method}

A continuación, basándote en el siguiente método `logPurchase` del SDK de Braze, crea un método equivalente.

**Método de referencia `logPurchase` de Braze**<br>
Esto es por diseño porque solo el archivo `BrazeManager.swift` puede acceder directamente a los métodos del SDK de Braze para iOS. Por lo tanto, al crear un método equivalente, el resultado es el mismo y se hace sin necesidad de dependencias directas del SDK de Braze para iOS en tu código de producción.

```
open func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price: NSDecimalNumber, withoutQuantity quantity: UInt)
```
**Método equivalente**<br>
Registra compras desde el objeto `Appboy` hacia Braze. El SDK tiene múltiples métodos para registrar compras, y este es solo un ejemplo. Este método también gestiona la creación de los objetos `NSDecimal` y `UInt`. Cómo quieras manejar esa parte depende de ti; lo proporcionado es solo un ejemplo.

{% subtabs global %}
{% subtab Swift %}

```swift
func logPurchase(_ productIdentifier: String, inCurrency currency: String, atPrice price:
String, withQuantity quantity: Int) {

  Appboy.sharedInstance()?.logPurchase(productIdentifier, inCurrency: currency, atPrice: NSDecimalNumber(string: price), withQuantity: UInt(quantity))

}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)logPurchase:(NSString *)productIdentifier inCurrency:(nonnull NSString *)currencyCode atPrice:(nonnull NSDecimalNumber *)price withQuantity:(NSUInteger)quantity {
  [[Appboy sharedInstance] logPurchase:productIdentifier inCurrency:currencyCode atPrice:price withQuantity:quantity];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Procede a compilar tu código y ejecutar tu aplicación. <br><br>Intenta registrar eventos personalizados.<br><br>En tu panel, observa que los eventos personalizados se están registrando antes de avanzar.
{% endalert %}

### In-App Messages {#in-app-messages}

{% tabs local %}
{% tab Step 1: Conform to Delegate %}

{% alert important %}
La siguiente sección de mensajes dentro de la aplicación no es necesaria para la integración si no planeas usar este canal en tu aplicación.
{% endalert %}

#### Conformar con ABKInAppMessageUIDelegate {#conform-to-abkinappmessageuidelegate}

A continuación, habilita tu código del archivo `BrazeManager.swift` para conformar con el `ABKInAppMessageUIDelegate` y gestionar directamente los métodos asociados.

El código para conformar con el delegado se agregará en los métodos `didFinishLaunching...` del archivo `BrazeManager.swift`. Tu código de inicialización debería quedar así:

{% subtabs global %}
{% subtab swift %}
```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) {
  Appboy.start(withApiKey: apiKey, in: application, withLaunchOptions: launchOptions, withAppboyOptions: appboyOptions)

  let options: UNAuthorizationOptions = [.alert, .sound, .badge]
  UNUserNotificationCenter.current().requestAuthorization(options: options) { (granted, error) in
    Appboy.sharedInstance()?.pushAuthorization(fromUserNotificationCenter: granted)
  }
  UIApplication.shared.registerForRemoteNotifications()

  Appboy.sharedInstance()?.inAppMessageController.inAppMessageUIController?.setInAppMessageUIDelegate?(self)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
- (void)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
  [Appboy startWithApiKey:[self apiKey] inApplication:application withLaunchOptions:launchOptions withAppboyOptions:[self appboyOptions]];

  UNAuthorizationOptions options = (UNAuthorizationOptionSound | UNAuthorizationOptionAlert | UNAuthorizationOptionBadge);
  [[UNUserNotificationCenter currentNotificationCenter] requestAuthorizationWithOptions:options completionHandler:^(BOOL granted, NSError * _Nullable error) {
    [[Appboy sharedInstance] pushAuthorizationFromUserNotificationCenter:granted];
  }];
  [[UIApplication sharedApplication] registerForRemoteNotifications];

  [[Appboy sharedInstance].inAppMessageController.inAppMessageUIController setInAppMessageUIDelegate:self];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Step 2: Add Delegate Methods %}

##### Agregar métodos del delegado {#add-delegate-methods}
A continuación, crea una extensión que conforme con el `ABKInAppMessageUIDelegate`.

Agrega el siguiente fragmento en la sección de análisis. Ten en cuenta que el objeto `BrazeManager.swift` se establece como delegado; aquí es donde el archivo `BrazeManager.swift` gestionará todos los métodos de `ABKInAppMessageUIDelegate`.

{% alert important %}
El `ABKInAppMessageUIDelegate` no viene con métodos obligatorios, pero el siguiente es un ejemplo de uno.
{% endalert %}

{% subtabs global %}
{% subtab Swift %}
```swift
// MARK: - ABKInAppMessage UI Delegate
extension AppboyManager: ABKInAppMessageUIDelegate{
  func inAppMessageViewControllerWith(_ inAppMessage: ABKInAppMessage) -> ABKInAppMessageViewController {
    switch inAppMessage {
    case is ABKInAppMessageSlideup:
      return ABKInAppMessageSlideupViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageModal:
      return ABKInAppMessageModalViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageFull:
      return ABKInAppMessageFullViewController(inAppMessage: inAppMessage)
    case is ABKInAppMessageHTML:
      return ABKInAppMessageHTMLViewController(inAppMessage: inAppMessage)
    default:
      return ABKInAppMessageViewController(inAppMessage: inAppMessage)
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - ABKInAppMessage UI Delegate
- (ABKInAppMessageViewController *)inAppMessageViewControllerWithInAppMessage:(ABKInAppMessage *)inAppMessage {
  if ([inAppMessage isKindOfClass:[ABKInAppMessageSlideup class]]) {
    return [[ABKInAppMessageSlideupViewController alloc] initWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageModal class]]) {
    return [[ABKInAppMessageModalViewController alloc] initWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageFull class]]) {
    return [[ABKInAppMessageFullViewController alloc] initWithInAppMessage:inAppMessage];
  } else if ([inAppMessage isKindOfClass:[ABKInAppMessageHTML class]]) {
    return [[ABKInAppMessageHTMLViewController alloc] initWithInAppMessage:inAppMessage];
  }
  return nil;
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Procede a compilar tu código y ejecutar tu aplicación. <br><br>Intenta enviarte un mensaje dentro de la aplicación. <br><br>En el archivo `BrazeManager.swift`, establece un punto de interrupción en la entrada del método de ejemplo `ABKInAppMessageUIDelegate`. Envíate un mensaje dentro de la aplicación y confirma que se alcanza el punto de interrupción antes de avanzar.
{% endalert %}

### Content Cards {#content-cards}

{% tabs local %}
{% tab Create Content Card Variables and Methods %}

{% alert important %}
La siguiente sección de Content Cards no es necesaria para la integración si no planeas usar este canal en tu aplicación.
{% endalert %}

#### Crear variables y métodos de Content Cards {#create-content-card-variables-and-methods}

Habilita tu código de producción para mostrar el controlador de vista de Content Cards sin la necesidad de declaraciones `import AppboyUI` innecesarias.

Crea una extensión para tu código de Content Cards en tu archivo `BrazeManager.swift`, para que se lea de manera más organizada en cuanto a qué propósito se cumple en el archivo auxiliar, de esta forma:

1. Muestra el `ABKContentCardsTableViewController`. Un `navigationController` opcional es el único parámetro necesario para presentar o hacer push de nuestro controlador de vista.
2. Inicializa un objeto `ABKContentCardsTableViewController` y opcionalmente cambia el título. También debes agregar el controlador de vista inicializado a la pila de navegación.

{% subtabs global %}
{% subtab Swift %}
```swift
// MARK: - Content Cards
extension BrazeManager {

  // 1
  func displayContentCards(navigationController: UINavigationController?) {

    // 2
    let contentCardsVc = ABKContentCardsTableViewController()
    contentCardsVc.title = "Content Cards"
    navigationController?.pushViewController(contentCardsVc, animated: true)
  }
}
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// MARK: - Content Cards
  // 1
- (void)displayContentCards:(UINavigationController *)navigationController {
  // 2
  ABKContentCardsTableViewController *contentCardsVc = [[ABKContentCardsTableViewController alloc] init];
  contentCardsVc.title = @"Content Cards";
  [navigationController pushViewController:contentCardsVc animated:YES];
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert checkpoint %}
Procede a compilar tu código y ejecutar tu aplicación.<br><br>Intenta mostrar el `ABKContentCardsTableViewController` en tu aplicación antes de avanzar.
{% endalert %}

## Próximos pasos {#next-steps}

¡Felicidades! Has completado esta guía de mejores prácticas de integración. Puedes encontrar un archivo de ejemplo `BrazeManager` en [GitHub](https://github.com/braze-inc/braze-growth-shares-ios-demo-app/blob/master/Braze-Demo/BrazeManager.swift).

Ahora que has desacoplado cualquier dependencia del SDK de Braze para iOS del resto de tu código de producción, consulta algunas de nuestras guías opcionales de implementación avanzada:
- [Guía de implementación avanzada de notificaciones push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/implementation_guide)
- [Guía de implementación avanzada de In-App Messages]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/in-app_messaging/implementation_guide)
- [Guía de implementación avanzada de Content Cards]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/content_cards/implementation_guide)