---
nav_title: Completar la integración
article_title: Completa la integración del SDK de iOS
platform: iOS
description: "Este artículo de referencia muestra cómo terminar de integrar el SDK de Braze después de instalarlo mediante una de las opciones de integración."
page_order: 2

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Completa la integración {#complete-the-integration}

Antes de seguir estos pasos, asegúrate de haber integrado el SDK mediante [Carthage]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/carthage_integration), [CocoaPods]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/cocoapods), [Swift Package Manager]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/swift_package_manager) o una integración [manual]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options).

## Paso 1: Actualiza tu app delegate {#step-1-update-your-app-delegate}

{% tabs %}
{% tab OBJECTIVE-C %}

Si estás integrando el SDK de Braze con CocoaPods, Carthage o con una [integración manual dinámica]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options), añade la siguiente línea de código a tu archivo `AppDelegate.m`:

```objc
#import "Appboy-iOS-SDK/AppboyKit.h"
```

Si estás integrando con Swift Package Manager o con una [integración manual estática]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options), usa esta línea en su lugar:

```objc
#import "AppboyKit.h"
```

A continuación, dentro de tu archivo `AppDelegate.m`, añade el siguiente fragmento de código en tu método `application:didFinishLaunchingWithOptions:`:

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions];
```

Actualiza `YOUR-APP-IDENTIFIER-API-KEY` con el valor correcto de tu página **Administrar configuración**. Consulta nuestra [documentación de API]({{site.baseurl}}/api/identifier_types#app-identifier) para obtener más información sobre dónde encontrar tu clave de API del identificador de aplicación.

{% endtab %}
{% tab swift %}

Si estás integrando el SDK de Braze con CocoaPods, Carthage o con una [integración manual dinámica]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options), añade la siguiente línea de código a tu archivo `AppDelegate.swift`:

```swift
import Appboy_iOS_SDK
```

Si estás integrando con Swift Package Manager o con una [integración manual estática]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/manual_integration_options), usa esta línea en su lugar:

```swift
import AppboyKit
```
Consulta la [documentación para desarrolladores de Apple](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html) para obtener más información sobre cómo usar código Objective-C en proyectos Swift.

A continuación, en `AppDelegate.swift`, añade el siguiente fragmento de código en tu `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`:

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY", in:application, withLaunchOptions:launchOptions)
```

Actualiza `YOUR-APP-IDENTIFIER-API-KEY` con el valor correcto de tu página **Administrar configuración**. Consulta nuestra [documentación de API]({{site.baseurl}}/api/identifier_types#app-identifier) para obtener más información sobre dónde encontrar tu clave de API del identificador de aplicación.

{% endtab %}
{% endtabs %}

{% alert note %}
El singleton `sharedInstance` será nil antes de que se llame a `startWithApiKey:`, ya que es un requisito previo para usar cualquier funcionalidad de Braze.
{% endalert %}

{% alert warning %}
Asegúrate de inicializar Braze en el hilo principal de tu aplicación. La inicialización asíncrona puede provocar un funcionamiento incorrecto.
{% endalert %}

## Paso 2: Especifica tu clúster de datos {#step-2-specify-your-data-cluster}

{% alert note %}
Ten en cuenta que, a partir de diciembre de 2019, ya no se proporcionan endpoints personalizados. Si tienes un endpoint personalizado preexistente, puedes seguir utilizándolo. Para más detalles, consulta nuestra <a href="{{site.baseurl}}/api/basics#endpoints">lista de endpoints disponibles</a>.
{% endalert %}

### Configuración del endpoint en tiempo de compilación (recomendado) {#compile-time-endpoint-configuration-recommended}

Si se te proporcionó un endpoint personalizado preexistente:
- A partir de Braze iOS SDK v3.0.2, puedes establecer un endpoint personalizado utilizando el archivo `Info.plist`. Añade el diccionario `Braze` a tu archivo `Info.plist`. Dentro del diccionario `Braze`, añade la subentrada de cadena `Endpoint` y establece el valor con la autoridad de la URL de tu endpoint personalizado (por ejemplo, `sdk.iad-01.braze.com`, no `https://sdk.iad-01.braze.com`). Ten en cuenta que antes de Braze iOS SDK v4.0.2, se debe utilizar la clave de diccionario `Appboy` en lugar de `Braze`.

Tu representante de Braze ya debería haberte indicado el [endpoint correcto]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints).

### Configuración del endpoint en tiempo de ejecución {#runtime-endpoint-configuration}

Si se te proporcionó un endpoint personalizado preexistente:
- A partir de Braze iOS SDK v3.17.0+, puedes sobrescribir tu endpoint a través de `ABKEndpointKey` dentro del parámetro `appboyOptions` pasado a `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Establece el valor con la autoridad de la URL de tu endpoint personalizado (por ejemplo, `sdk.iad-01.braze.com`, no `https://sdk.iad-01.braze.com`).

## Integración de SDK completa {#sdk-integration-complete}

Braze debería estar recopilando datos de tu aplicación, y tu integración básica debería estar completa. Consulta los siguientes artículos para habilitar el [seguimiento de eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift), la [mensajería push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) y la línea de productos completa de características de Braze.

## Personalización de Braze al inicio {#customizing-braze-on-startup}

Si deseas personalizar Braze al inicio, puedes usar en su lugar el método de inicialización de Braze `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` y pasar un `NSDictionary` opcional de claves de inicio de Braze.
{% tabs %}
{% tab OBJECTIVE-C %}

En tu archivo `AppDelegate.m`, dentro del método `application:didFinishLaunchingWithOptions:`, añade el siguiente método de Braze:

```objc
[Appboy startWithApiKey:@"YOUR-APP-IDENTIFIER-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

Ten en cuenta que este método reemplazaría al método de inicialización `startWithApiKey:inApplication:withLaunchOptions:`.

{% endtab %}
{% tab swift %}

En `AppDelegate.swift`, dentro del método `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`, añade el siguiente método de Braze, donde `appboyOptions` es un `Dictionary` de valores de configuración de inicio:

```swift
Appboy.start(withApiKey: "YOUR-APP-IDENTIFIER-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

Ten en cuenta que este método reemplazaría al método de inicialización `startWithApiKey:inApplication:withLaunchOptions:`.

{% endtab %}
{% endtabs %}

Este método se llama con los siguientes parámetros:

- `YOUR-APP-IDENTIFIER-API-KEY` – Tu clave de API de [identificador de aplicación]({{site.baseurl}}/api/identifier_types#app-identifier) del panel de Braze.
- `application` – La aplicación actual.
- `launchOptions` – El `NSDictionary` de opciones que obtienes de `application:didFinishLaunchingWithOptions:`.
- `appboyOptions` – Un `NSDictionary` opcional con valores de configuración de inicio para Braze.

Consulta [Appboy.h](https://github.com/braze-inc/braze-ios-sdk/blob/master/AppboyKit/include/Appboy.h) para ver una lista de claves de inicio de Braze.

## Appboy.sharedInstance() y la nulabilidad en Swift {#appboysharedinstance-and-swift-nullability}
A diferencia de la práctica común, el singleton `Appboy.sharedInstance()` es opcional. Esto se debe a que `sharedInstance` es `nil` antes de que se llame a `startWithApiKey:`, y existen algunas implementaciones no estándar pero válidas en las que se puede utilizar una inicialización diferida.

Si llamas a `startWithApiKey:` en tu delegado `didFinishLaunchingWithOptions:` antes de cualquier acceso al `sharedInstance` de Appboy (la implementación estándar), puedes usar encadenamiento opcional, como `Appboy.sharedInstance()?.changeUser("testUser")`, para evitar comprobaciones engorrosas. Esto tendrá paridad con una implementación en Objective-C que asumiera un `sharedInstance` no nulo.

## Recursos adicionales {#additional-resources}

La [documentación completa de clases de iOS](http://appboy.github.io/appboy-ios-sdk/docs/annotated.html) está disponible para proporcionar orientación adicional sobre cualquier método del SDK.