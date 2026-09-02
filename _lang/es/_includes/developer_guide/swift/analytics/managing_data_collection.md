## El manifiesto de privacidad de Apple {#privacy-manifest}

### ¿Qué son los datos de seguimiento? {#what-is-tracking-data}

Apple define los "datos de seguimiento" como los datos recopilados en tu aplicación sobre un usuario final o dispositivo que están vinculados a datos de terceros (como publicidad dirigida), o a un intermediario de datos. Para una definición completa con ejemplos, consulta [Apple: Seguimiento](https://developer.apple.com/app-store/app-privacy-details/#user-tracking).

De manera predeterminada, el SDK de Braze no recopila datos de seguimiento. Sin embargo, dependiendo de la configuración de tu SDK de Braze, es posible que tengas que incluir datos específicos de Braze en el manifiesto de privacidad de tu aplicación.

### ¿Qué es un manifiesto de privacidad? {#what-is-a-privacy-manifest}

Un manifiesto de privacidad es un archivo de tu proyecto Xcode que describe el motivo por el que tu aplicación y los SDK de terceros recopilan datos, junto con sus métodos de recopilación de datos. Cada uno de tus SDK de terceros que hace un seguimiento de datos requiere su propio manifiesto de privacidad. Cuando [creas el informe de privacidad de tu aplicación](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187), estos archivos de manifiesto de privacidad se agregan automáticamente en un único informe.

### Dominios de datos de seguimiento de la API {#api-tracking-data-domains}

A partir de iOS 17.2, Apple bloqueará todos los endpoints de seguimiento declarados en tu aplicación hasta que el usuario final acepte un [aviso de Transparencia de seguimiento de anuncios (ATT)](https://support.apple.com/en-us/HT212025). Braze proporciona endpoints de seguimiento para dirigir tus datos de seguimiento, a la vez que te permite dirigir datos propios que no son de seguimiento al endpoint original.

## Declarar datos de seguimiento de Braze {#declaring-braze-tracking-data}

{% alert tip %}
Para un recorrido completo, consulta el [tutorial de datos de seguimiento de privacidad](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/).
{% endalert %}

### Requisitos previos {#prerequisites}

Se requiere la siguiente versión del SDK de Braze para implementar esta característica:

{% sdk_min_versions swift:9.0.0 %}

### Paso 1: Revisa tus políticas actuales {#step-1-review-your-current-policies}

Revisa las políticas actuales de recopilación de datos del SDK de Braze con tu equipo legal para determinar si tu aplicación recopila datos de seguimiento [según la definición de Apple](#what-is-tracking-data). Si no estás recopilando datos de seguimiento, no necesitas personalizar tu manifiesto de privacidad para el SDK de Braze en este momento. Para más información sobre las políticas de recopilación de datos del SDK de Braze, consulta [Recopilación de datos del SDK]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection).

{% alert important %}
Si alguno de tus SDK que no son de Braze recopila datos de seguimiento, deberás revisar esas políticas por separado.
{% endalert %}

### Paso 2: Crea un manifiesto de privacidad {#step-2-create-a-privacy-manifest}

Primero, comprueba si ya tienes un manifiesto de privacidad buscando un archivo `PrivacyInfo.xcprivacy` en tu proyecto de Xcode. Si ya tienes este archivo, puedes continuar con el siguiente paso. En caso contrario, consulta [Apple: Crear un manifiesto de privacidad](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files).

### Paso 3: Añade tu endpoint al manifiesto de privacidad {#step-3-add-your-endpoint-to-the-privacy-manifest}

En tu proyecto de Xcode, abre el archivo `PrivacyInfo.xcprivacy` de tu aplicación, luego haz clic con el botón derecho en la tabla y marca **Raw Keys and Values**.

{% alert note %}

{% endalert %}

![Un proyecto de Xcode con el menú contextual abierto y "Raw Keys and Values" resaltado.]({% image_buster /assets/img/apple/privacy_manifest/check_raw_keys_and_values.png %})

En **App Privacy Configuration**, elige **NSPrivacyTracking** y establece su valor en **YES**.

![El archivo 'PrivacyInfo.xcprivacy' abierto con "NSPrivacyTracking" establecido en "YES".]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytracking.png %})

En **App Privacy Configuration**, elige **NSPrivacyTrackingDomains**. En el arreglo de dominios, añade un nuevo elemento y establece su valor con el endpoint que [añadiste previamente a tu `AppDelegate`]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration#update-your-app-delegate) precedido por `sdk-tracking`.

![El archivo 'PrivacyInfo.xcprivacy' abierto con un endpoint de seguimiento de Braze listado en "NSPrivacyTrackingDomains".]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytrackingdomains.png %})

### Paso 4: Declara tus datos de seguimiento {#step-4-declare-your-tracking-data}

A continuación, abre `AppDelegate.swift` y luego enumera cada [propiedad de seguimiento](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/) que desees declarar creando una lista de seguimiento estática o dinámica. Ten en cuenta que Apple bloqueará estas propiedades hasta que el usuario final acepte la solicitud de ATT, así que solo enumera las propiedades que tú y tu equipo legal consideren como datos de seguimiento. Por ejemplo:

{% tabs %}
{% tab ejemplo estático %}
En el siguiente ejemplo, `dateOfBirth`, `customEvent` y `customAttribute` se declaran como datos de seguimiento dentro de una lista estática.

```swift
import UIKit
import BrazeKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let configuration = Braze.Configuration(apiKey: brazeApiKey, endpoint: brazeEndpoint)
    // Declare which types of data you wish to collect for user tracking.
    configuration.api.trackingPropertyAllowList = [
      .dateOfBirth,
      .customEvent(["event-1"]),
      .customAttribute(["attribute-1", "attribute-2"])
    ]
    let braze = Braze(configuration: configuration)
    AppDelegate.braze = braze
    return true
  }
}
```
{% endtab %}

{% tab ejemplo dinámico %}
En el siguiente ejemplo, la lista de seguimiento se actualiza automáticamente después de que el usuario final acepte la [solicitud de Transparencia de Seguimiento de Aplicaciones (ATT)](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/requesttrackingauthorization(completionhandler:)). La solicitud de autorización durante la activación de la aplicación es un evento por escena, por lo que este código pertenece al método `sceneDidBecomeActive(_:)` de tu archivo `SceneDelegate.swift` en lugar de `applicationDidBecomeActive(_:)` de `AppDelegate.swift` (obligatorio para aplicaciones que han adoptado el [ciclo de vida `UIScene`](https://developer.apple.com/documentation/technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle)). Tu instancia de Braze permanece accesible desde `SceneDelegate` a través de la propiedad estática `AppDelegate.braze` configurada en el paso 1.

```swift
func sceneDidBecomeActive(_ scene: UIScene) {
  // Request and check your user's tracking authorization status.
  ATTrackingManager.requestTrackingAuthorization { status in
    // Let Braze know whether user data is allowed to be collected for tracking.
    let enableAdTracking = status == .authorized
    AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)

    // Add the `.firstName` and `.lastName` properties, while removing the `.everything` configuration.
    AppDelegate.braze?.updateTrackingAllowList(
      adding: [.firstName, .lastName],
      removing: [.everything]
    )
  }
}
```
{% endtab %}
{% endtabs %}

### Paso 5: Prevenir bucles de reintento infinitos {#step-5-prevent-infinite-retry-loops}

Para evitar que el SDK entre en un bucle de reintento infinito, utiliza el método `set(adTrackingEnabled: enableAdTracking)` para gestionar los permisos de ATT. La propiedad `adTrackingEnabled` en tu método de `SceneDelegate.swift` debe gestionarse de manera similar a la siguiente:

```swift
func sceneDidBecomeActive(_ scene: UIScene) {
    // Request and check your user's tracking authorization status.
    ATTrackingManager.requestTrackingAuthorization { status in
      // Let Braze know whether user data is allowed to be collected for tracking.
      let enableAdTracking = status == .authorized
      AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)
    }
}
```

## Desactivar el seguimiento de datos {#disabling-data-tracking}

Para desactivar la actividad de seguimiento de datos en el SDK de Swift, establece la propiedad [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) en `false` en tu instancia de Braze. Cuando `enabled` se establece en `false`, el SDK de Braze ignora cualquier llamada a la API pública. El SDK también cancela todas las acciones en curso, como solicitudes de red, procesamiento de eventos, etc.

## Borrar datos almacenados previamente {#wiping-previously-stored-data}

Puedes usar el método [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) para borrar completamente los datos del SDK almacenados localmente en el dispositivo de un usuario.

Para las versiones 7.0.0 y posteriores de Braze Swift, el SDK y el método `wipeData()` generan aleatoriamente un UUID como ID de dispositivo. Sin embargo, si tu `useUUIDAsDeviceId` está configurado como `false` _o_ estás usando la versión 5.7.0 o anterior del SDK Swift, también necesitarás hacer una solicitud post a [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) ya que tu identificador para proveedores (IDFV) se usará automáticamente como el ID de dispositivo de ese usuario.

Si usas la integración push manual y tu aplicación llama a `wipeData()` y después vuelve a habilitar el SDK en la misma ejecución de la aplicación, llama a `registerForRemoteNotifications()` de nuevo para que Braze pueda recibir un token de dispositivo actualizado. Para más información, consulta [configurar notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Reanudación del seguimiento de datos {#resuming-data-tracking}

Para reanudar la recopilación de datos, establece [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) en `true`. Ten en cuenta que esto no restaurará ningún dato borrado previamente.

## Cierre de sesión y cancelar registro push {#logout-and-unregister-push}

El SDK de Braze proporciona métodos para dejar de segmentar un dispositivo cuando un usuario cancela su registro de notificaciones push o cierra sesión. Estos métodos eliminan los datos de registro push del usuario actual en el servidor de Braze y el SDK, de modo que Braze ya no envíe futuras Campaigns de notificaciones push a ese usuario.

### Cierre de sesión {#logout}

Cuando un usuario cierra sesión en una aplicación, llama al método `logout` del SDK para eliminar el registro push del dispositivo del usuario actual y realizar automáticamente acciones de limpieza en el SDK. El método `logout` realiza lo siguiente:

- Cancela el registro del token push del dispositivo y de cualquier token push-to-start de Live Activities del usuario actual en el servidor de Braze.
- Si la llamada de cancelación de registro tiene éxito, el SDK borra los datos del SDK almacenados localmente y deshabilita el SDK.
- En caso de fallo, genera un error y una bandera `isRetriable` para permitir al integrador tomar acción.

{% subtabs local %}
{% subtab Swift %}

El siguiente ejemplo con completion handler muestra el manejo de éxito y fallo de `logout`. Úsalo para flujos basados en devolución de llamada y reemplaza el registro con la lógica de reintento o reautenticación de tu aplicación.

```swift
// Completion handler
AppDelegate.braze?.logout { result in
  switch result {
  case .success:
    print("Logout successful")
  case .failure(let error):
    print("Logout failed: \(error.message), isRetriable: \(error.isRetriable)")
  }
}
```

El siguiente ejemplo async muestra la API suspendida de `logout`. Úsalo para flujos de trabajo asíncronos y personaliza las ramas de éxito y fallo para tu aplicación.

```swift
// Async/await
do {
  try await AppDelegate.braze?.logout()
  print("Logout successful")
} catch let error as Braze.LogoutErrorResult {
  print("Logout failed: \(error.message), isRetriable: \(error.isRetriable)")
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Este ejemplo en Objective-C muestra el manejo de `logout` basado en completion. Úsalo en integraciones de Objective-C y reemplaza el registro con el flujo de tu aplicación.

```objc
[AppDelegate.braze logoutWithCompletion:^(NSError * _Nullable error) {
  if (error) {
    NSNumber *isRetriable = error.userInfo[BRZLogoutErrorUserInfoKey.isRetriable];
    NSLog(@"Logout failed: %@, isRetriable=%@", error.localizedDescription, isRetriable);
  }
}];
```

{% endsubtab %}
{% endsubtabs local %}

{% alert note %}
`logout` no finaliza las Live Activities que están en ejecución actualmente. En la devolución de llamada de éxito, finaliza manualmente cualquier Live Activity en ejecución usando el método [`end(_:dismissalPolicy:)`](https://developer.apple.com/documentation/activitykit/activity/end(_:dismissalpolicy:)) de ActivityKit.
{% endalert %}

#### Rehabilitar el seguimiento y push después de `logout` {#re-enable-tracking-and-push-after-logout}

Después de un `logout` exitoso, establece [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) de nuevo a `true`, luego vuelve a registrarte para notificaciones con tu sistema operativo (SO) o proveedor push siguiendo la [configuración push de Swift]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

#### Evita llamadas de cancelación de registro inmediatas {#avoid-immediate-unregister-calls}

Evita llamar a `logout` o `unregisterPush` directamente después de registrarte para notificaciones push con el SO o proveedor push. Debido al procesamiento asíncrono del servidor, esto puede en raras ocasiones volver a agregar el token push al usuario de Braze.

### Cancelar registro push {#unregister-push}

Para dejar de enviar push a un dispositivo sin limpieza automatizada adicional, usa el método `unregisterPush`. Esto elimina el token push del dispositivo del usuario actual en el servidor de Braze y borra el token almacenado localmente.

{% subtabs local %}
{% subtab Swift %}

El siguiente ejemplo con completion handler muestra el manejo de éxito y fallo de `unregisterPush`. Úsalo para flujos basados en devolución de llamada y reemplaza el registro con tu propia lógica de reintento.

```swift
// Completion handler
AppDelegate.braze?.notifications.unregisterPush { result in
  switch result {
  case .success:
    print("Push unregistered successfully")
  case .failure(let error):
    print("Push unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
  }
}
```

El siguiente ejemplo async muestra la API suspendida de `unregisterPush`. Úsalo para flujos de trabajo asíncronos y personaliza las ramas de éxito y fallo para tu aplicación.

```swift
// Async/await
do {
  try await AppDelegate.braze?.notifications.unregisterPush()
  print("Push unregistered successfully")
} catch let error as Braze.PushUnregistrationError {
  print("Push unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

Este ejemplo en Objective-C muestra el manejo de `unregisterPush` basado en completion. Úsalo en integraciones de Objective-C y reemplaza el registro con el flujo de tu aplicación.

```objc
[AppDelegate.braze.notifications unregisterPushWithCompletion:^(NSError * _Nullable error) {
  if (error) {
    NSNumber *isRetriable = error.userInfo[BRZPushUnregistrationErrorUserInfoKey.isRetriable];
    NSNumber *statusCode = error.userInfo[BRZPushUnregistrationErrorUserInfoKey.httpStatusCode];
    NSLog(@"Push unregistration failed: %@, isRetriable=%@ status=%@",
          error.localizedDescription, isRetriable, statusCode);
  }
}];
```

{% endsubtab %}
{% endsubtabs local %}

#### Volver a registrarse para push después de `unregisterPush` {#re-register-push-after-unregisterpush}

Después de llamar a `unregisterPush`, vuelve a registrarte para notificaciones con tu SO o proveedor push siguiendo la [configuración push de Swift]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) antes de enviar notificaciones push de Braze nuevamente.

#### Evita llamadas de cancelación de registro inmediatas

Evita llamar a `logout` o `unregisterPush` directamente después de registrarte para notificaciones push con el SO o proveedor push. Debido al procesamiento asíncrono del servidor, esto puede en raras ocasiones volver a agregar el token push al usuario de Braze.

### Cancelar registro de tokens push-to-start para Live Activities {#unregister-push-to-start}

Las Live Activities se pueden iniciar de forma remota usando tokens push-to-start. Para evitar que Braze inicie Live Activities de forma remota en un dispositivo, llama al método `unregisterPushToStart` para cancelar el registro de todos los tipos registrados actualmente (predeterminado) o una lista específica de tipos de Activity.

Ten en cuenta que las Live Activities que están en ejecución actualmente siguen recibiendo actualizaciones y que este método solo elimina la capacidad de iniciar nuevas actividades de forma remota. Para obtener más información sobre Live Activities, consulta [Live Activities]({{site.baseurl}}/developer_guide/live_notifications/live_activities).

#### Finalizar cualquier Live Activity en ejecución {#end-any-running-live-activities}

`unregisterPushToStart` no finaliza las Live Activities que están en ejecución actualmente. En la devolución de llamada de éxito, finaliza manualmente cualquier Live Activity en ejecución usando el método [`end(_:dismissalPolicy:)`](https://developer.apple.com/documentation/activitykit/activity/end(_:dismissalpolicy:)) de ActivityKit.

{% alert note %}
Evita llamar a `logout` o `unregisterPushToStart` directamente después de llamar a `registerPushToStart` para una Live Activity. Debido a la naturaleza asíncrona del procesamiento del servidor, en raras ocasiones esto puede provocar que el token push-to-start se vuelva a agregar al usuario de Braze.
{% endalert %}

El siguiente ejemplo muestra cómo cancelar el registro de todos los tipos de actividades push-to-start. Úsalo cuando un usuario que ha cerrado sesión ya no deba recibir nuevas Live Activities iniciadas de forma remota.

```swift
// Unregister all currently-registered activity types
// Completion handler
AppDelegate.braze?.liveActivities.unregisterPushToStart { result in
  switch result {
  case .success:
    print("Push-to-start unregistered successfully")
  case .failure(let error):
    print("Push-to-start unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
  }
}

// Async/await
do {
  try await AppDelegate.braze?.liveActivities.unregisterPushToStart()
  print("Push-to-start unregistered successfully")
} catch let error as Braze.PushUnregistrationError {
  print("Push-to-start unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
}
```

El siguiente ejemplo muestra cómo cancelar el registro de tipos de actividad específicos. Úsalo cuando solo determinadas Live Activities deban dejar de iniciarse de forma remota.

```swift
// Unregister specific activity types
AppDelegate.braze?.liveActivities.unregisterPushToStart(types: ["ActivityType1", "ActivityType2"]) { result in
  switch result {
  case .success:
    print("Push-to-start unregistered successfully")
  case .failure(let error):
    print("Push-to-start unregistration failed: \(error.message), isRetriable: \(error.isRetriable)")
  }
}
```

{% alert note %}
`unregisterPushToStart` no tiene una API de Objective-C, ya que las Live Activities dependen de tipos exclusivos de Swift.
{% endalert %}

## Recopilación de IDFV {#idfv-collection}

En versiones anteriores del SDK de Braze para iOS, el campo IDFV (Identifier for Vendor) se recopilaba automáticamente como el ID de dispositivo del usuario. A partir de la versión `v5.7.0` del SDK de Swift, el campo IDFV podía deshabilitarse opcionalmente, y en su lugar Braze establecía un UUID aleatorio como ID de dispositivo. A partir de la versión `v7.0.0` del SDK de Swift, el campo IDFV no se recopilará de forma predeterminada y se establecerá un UUID como ID de dispositivo en su lugar.

La característica `useUUIDAsDeviceId` configura el [SDK de Swift](https://github.com/braze-inc/braze-swift-sdk) para establecer el ID de dispositivo como un UUID. Tradicionalmente, el SDK de iOS asignaba al ID de dispositivo el valor IDFV generado por Apple. Con esta característica habilitada de forma predeterminada en tu aplicación iOS, a todos los nuevos usuarios creados a través del SDK se les asignará un ID de dispositivo igual a un UUID.

Si aún deseas recopilar el IDFV por separado, puedes utilizar [`set(identifierforvendor:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)).

{% alert note %}
Apple es responsable de la creación del IDFV, y el IDFV es administrado por Apple. Braze no transforma ni modifica los IDFV, y Apple no ofrece garantías sobre el uso de mayúsculas/minúsculas ni el formato.
{% endalert %}

{% alert note %}
La lectura de `braze.deviceId` bloquea el hilo que la invoca hasta que el SDK haya completado sus operaciones posteriores a la inicialización. Para contextos en el hilo principal o sensibles a la latencia, utiliza en su lugar las alternativas no bloqueantes.

{% subtabs local %}
{% subtab Swift %}
```swift
// Completion handler — always delivers on the main thread.
AppDelegate.braze?.getDeviceId { deviceId in
  print("Device ID:", deviceId)
}

// Async/await (iOS 13.0+, tvOS 13.0+, watchOS 6.0+, macOS 10.15+)
let deviceId = await AppDelegate.braze?.getDeviceId()
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// Completion handler — always delivers on the main thread.
[AppDelegate.braze getDeviceIdWithCompletion:^(NSString *deviceId) {
  NSLog(@"Device ID: %@", deviceId);
}];
```
{% endsubtab %}
{% endsubtabs local %}
{% endalert %}

### Consideraciones {#considerations}

#### Versión del SDK {#sdk-version}

En la versión `v7.0.0+` del SDK de Swift, cuando `useUUIDAsDeviceId` está habilitado (predeterminado), a todos los nuevos usuarios creados se les asignará un ID de dispositivo aleatorio. Todos los usuarios existentes previamente mantendrán el mismo valor de ID de dispositivo, que podría haber sido un IDFV.

Cuando esta característica no está habilitada, los dispositivos seguirán recibiendo un IDFV asignado en el momento de su creación.

#### Impacto posterior {#downstream}

**Partners tecnológicos**: Cuando esta característica está habilitada, cualquier partner tecnológico que obtenga el valor IDFV a partir del ID de dispositivo de Braze ya no tendrá acceso a estos datos. Si el valor IDFV derivado del dispositivo es necesario para tu integración del partner, te recomendamos que establezcas esta característica en `false`.

**Currents**: Con `useUUIDAsDeviceId` establecido en true, el ID de dispositivo enviado en Currents ya no será igual al valor IDFV.

### Preguntas frecuentes {#frequently-asked-questions}

#### ¿Este cambio afectará a mis usuarios existentes en Braze? {#will-this-change-impact-my-existing-users-in-braze}

No. Cuando esta característica está habilitada, no sobrescribirá ningún dato de usuario en Braze. Los nuevos ID de dispositivo UUID solo se crearán para nuevos dispositivos o cuando se llame a `wipedata()`.

#### ¿Puedo desactivar esta característica después de haberla activado? {#can-i-turn-this-feature-off-after-turning-it-on}

Sí, esta característica puede activarse y desactivarse a tu discreción. Los ID de dispositivo almacenados previamente nunca se sobrescribirán.

#### ¿Puedo seguir capturando el valor IDFV a través de Braze en otro lugar? {#can-i-still-capture-the-idfv-value-through-braze-elsewhere}

Sí, aún puedes recopilar opcionalmente el IDFV a través del SDK de Swift (la recopilación está deshabilitada de forma predeterminada).