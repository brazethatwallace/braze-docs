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
Para un recorrido completo, consulta el [tutorial Privacidad de los datos de seguimiento](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/).
{% endalert %}

### Requisitos previos {#prerequisites}

Para implementar esta característica se necesita la siguiente versión del SDK de Braze:

{% sdk_min_versions swift:9.0.0 %}

### Paso 1: Revisa tus políticas actuales {#step-1-review-your-current-policies}

Revisa las políticas actuales de recopilación de datos de tu SDK de Braze con tu equipo legal para determinar si tu aplicación recopila datos de seguimiento [según la definición de Apple](#what-is-tracking-data). Si no recopilas datos de seguimiento, no necesitas personalizar tu manifiesto de privacidad para el SDK de Braze en este momento. Para más información sobre las políticas de recopilación de datos del SDK de Braze, consulta [Recopilación de datos del SDK]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection).

{% alert important %}
Si alguno de tus SDK que no sea de Braze recopila datos de seguimiento, tendrás que revisar esas políticas por separado.
{% endalert %}

### Paso 2: Crea un manifiesto de privacidad {#step-2-create-a-privacy-manifest}

Primero, comprueba si ya tienes un manifiesto de privacidad buscando un archivo `PrivacyInfo.xcprivacy` en tu proyecto de Xcode. Si ya tienes este archivo, puedes continuar con el paso siguiente. Si no, consulta [Apple: Crea un manifiesto de privacidad](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files).

### Paso 3: Añade tu endpoint al manifiesto de privacidad {#step-3-add-your-endpoint-to-the-privacy-manifest}

En tu proyecto de Xcode, abre el archivo `PrivacyInfo.xcprivacy` de tu aplicación, luego haz clic con el botón derecho en la tabla y marca **Raw Keys and Values**.

{% alert note %}

{% endalert %}

![Un proyecto de Xcode con el menú contextual abierto y "Raw Keys and Values" resaltado.]({% image_buster /assets/img/apple/privacy_manifest/check_raw_keys_and_values.png %})

En **App Privacy Configuration**, elige **NSPrivacyTracking** y establece su valor en **YES**.

![El archivo 'PrivacyInfo.xcprivacy' abierto con "NSPrivacyTracking" ajustado a "YES".]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytracking.png %})

En **App Privacy Configuration**, elige **NSPrivacyTrackingDomains**. En la matriz de dominios, añade un nuevo elemento y establece su valor en el endpoint que [añadiste previamente a tu `AppDelegate`]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration#update-your-app-delegate) con el prefijo `sdk-tracking`.

![El archivo 'PrivacyInfo.xcprivacy' abierto con un endpoint de seguimiento de Braze listado en "NSPrivacyTrackingDomains".]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytrackingdomains.png %})

### Paso 4: Declara tus datos de seguimiento {#step-4-declare-your-tracking-data}

A continuación, abre `AppDelegate.swift` y enumera cada [propiedad de seguimiento](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/) que quieras declarar creando una lista de seguimiento estática o dinámica. Ten en cuenta que Apple bloqueará estas propiedades hasta que el usuario final acepte su solicitud de ATT, así que enumera solo las propiedades que tú y tu equipo legal consideréis de seguimiento. Por ejemplo:

{% tabs %}
{% tab static example %}
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

{% tab dynamic example %}
En el siguiente ejemplo, la lista de seguimiento se actualiza automáticamente después de que el usuario final acepte el aviso de ATT.

```swift
func applicationDidBecomeActive(_ application: UIApplication) {
  // Request and check your user's tracking authorization status.
  ATTrackingManager.requestTrackingAuthorization { status in
    // Let Braze know whether user data is allowed to be collected for tracking.
    let enableAdTracking = status == .authorized
    AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)

    // Add the `.firstName` and `.lastName` properties, while removing the `.everything` configuration.
    AppDelegate.braze.updateTrackingAllowList(
      adding: [.firstName, .lastName],
      removing: [.everything]
    )
  }
}
```
{% endtab %}
{% endtabs %}

### Paso 5: Evitar bucles de reintento infinitos {#step-5-prevent-infinite-retry-loops}

Para evitar que el SDK entre en un bucle infinito de reintentos, utiliza el método `set(adTrackingEnabled: enableAdTracking)` para gestionar los permisos ATT. La propiedad `adTrackingEnabled` de tu método debe tratarse de forma similar a la siguiente:

```swift
func applicationDidBecomeActive(_ application: UIApplication) {
    // Request and check your user's tracking authorization status.
    ATTrackingManager.requestTrackingAuthorization { status in
      // Let Braze know whether user data is allowed to be collected for tracking.
      let enableAdTracking = status == .authorized
      AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)
    }
}
```

## Desactivar el seguimiento de datos {#disabling-data-tracking}

Para desactivar la actividad de seguimiento de datos en el SDK de Swift, establece la propiedad [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) en `false` en tu instancia de Braze. Cuando `enabled` está configurado como `false`, el SDK de Braze ignora cualquier llamada a la API pública. El SDK también cancela todas las acciones en curso, como solicitudes de red, procesamiento de eventos, etc.

## Borrar datos almacenados previamente {#wiping-previously-stored-data}

Puedes utilizar el método [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) para borrar completamente los datos del SDK almacenados localmente en el dispositivo de un usuario.

Para las versiones 7.0.0 y posteriores de Braze Swift, el SDK y el método `wipeData()` generan aleatoriamente un UUID para su ID de dispositivo. Sin embargo, si tu `useUUIDAsDeviceId` está configurado en `false` _o_ utilizas la versión 5.7.0 o anterior del SDK de Swift, también tendrás que hacer una solicitud POST a [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete) ya que tu identificador para proveedores (IDFV) se utilizará automáticamente como ID del dispositivo de ese usuario.

Si utilizas la integración manual de push y tu aplicación llama a `wipeData()` y luego vuelve a habilitar el SDK en la misma ejecución de la aplicación, llama a `registerForRemoteNotifications()` de nuevo para que Braze pueda recibir un token de dispositivo actualizado. Para más información, consulta [configurar notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Reanudar el seguimiento de datos {#resuming-data-tracking}

Para reanudar la recopilación de datos, configura [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) en `true`. Ten en cuenta que esto no restaurará ningún dato borrado previamente.

## Recopilación de IDFV {#idfv-collection}

En versiones anteriores del SDK de Braze para iOS, el campo IDFV (identificador para proveedores) se recopilaba automáticamente como ID del dispositivo del usuario. A partir del SDK de Swift `v5.7.0`, el campo IDFV se pudo desactivar opcionalmente y, en su lugar, Braze establecía un UUID aleatorio como ID del dispositivo. A partir del SDK de Swift `v7.0.0`, el campo IDFV no se recopilará de forma predeterminada, y en su lugar se establecerá un UUID como ID del dispositivo.

La característica `useUUIDAsDeviceId` configura el [SDK de Swift](https://github.com/braze-inc/braze-swift-sdk) para establecer el ID del dispositivo como UUID. Tradicionalmente, el SDK de iOS asignaba el ID del dispositivo igual al valor IDFV generado por Apple. Con esta característica habilitada de forma predeterminada en tu aplicación para iOS, a todos los nuevos usuarios creados a través del SDK se les asignará un ID de dispositivo igual a un UUID.

Si todavía quieres recopilar IDFV por separado, puedes utilizar [`set(identifierforvendor:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)).

{% alert note %}
La lectura de `braze.deviceId` bloquea el hilo de llamada hasta que el SDK haya completado sus operaciones posteriores a la inicialización. Para contextos del hilo principal o sensibles a la latencia, utiliza las alternativas no bloqueantes en su lugar.

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

En el SDK de Swift `v7.0.0+`, cuando `useUUIDAsDeviceId` está habilitado (predeterminado), a todos los nuevos usuarios creados se les asignará un ID de dispositivo aleatorio. Todos los usuarios existentes mantendrán su mismo valor de ID de dispositivo, que puede haber sido IDFV.

Si esta característica no está habilitada, se seguirá asignando IDFV a los dispositivos al crearlos.

#### Downstream

**Partners tecnológicos**: cuando se habilita esta característica, los partners tecnológicos que obtengan el valor IDFV del ID del dispositivo de Braze dejarán de tener acceso a estos datos. Si el valor IDFV derivado del dispositivo es necesario para tu integración del partner, te recomendamos que configures esta característica en `false`.

**Currents**: `useUUIDAsDeviceId` configurado como verdadero significa que el ID del dispositivo enviado en Currents ya no será igual al valor de IDFV.

### Preguntas frecuentes {#frequently-asked-questions}

#### ¿Este cambio afectará a mis usuarios actuales en Braze? {#will-this-change-impact-my-existing-users-in-braze}

No. Cuando esté habilitada, esta característica no sobrescribirá ningún dato de usuario en Braze. Solo se crearán nuevos ID de dispositivo UUID para los dispositivos nuevos o cuando se llame a `wipedata()`.

#### ¿Puedo desactivar esta característica después de activarla? {#can-i-turn-this-feature-off-after-turning-it-on}

Sí, esta característica se puede alternar entre activarla y desactivarla a tu discreción. Los ID de dispositivo almacenados anteriormente nunca se sobrescribirán.

#### ¿Puedo seguir recopilando el valor IDFV a través de Braze en otro lugar? {#can-i-still-capture-the-idfv-value-via-braze-elsewhere}

Sí, aún puedes recopilar opcionalmente el IDFV a través del SDK de Swift (la recopilación está desactivada de forma predeterminada).