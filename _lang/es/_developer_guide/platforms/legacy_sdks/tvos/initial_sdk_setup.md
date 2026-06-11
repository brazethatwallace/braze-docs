---
nav_title: Configuración inicial del SDK
article_title: Configuración inicial del SDK para tvOS
platform: tvOS
page_order: 0
page_type: reference
description: "Esta página cubre los pasos de configuración inicial para el SDK de Braze de tvOS."
search_rank: 1
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Configuración inicial del SDK {#initial-sdk-setup}

> En este artículo de referencia se explica cómo instalar el SDK de Braze para tvOS. La instalación del SDK de Braze te proporcionará una funcionalidad básica de análisis.

{% alert note %}
Nuestro SDK para tvOS admite actualmente la funcionalidad de análisis. Para añadir una aplicación tvOS en tu dashboard, abre un [ticket de soporte]({{site.baseurl}}/braze_support/).
{% endalert %}

El SDK de Braze de tvOS debe instalarse o actualizarse mediante [CocoaPods](http://cocoapods.org/), un administrador de dependencias para proyectos Objective-C y Swift. CocoaPods proporciona una mayor simplicidad para la integración y la actualización.

## Integración del SDK de tvOS en CocoaPods {#tvos-sdk-cocoapods-integration}

### Paso 1: Instalar CocoaPods {#step-1-install-cocoapods}

La instalación del SDK a través de los [CocoaPods](http://cocoapods.org/) de tvOS automatiza la mayor parte del proceso de instalación por ti. Antes de comenzar este proceso, asegúrate de que utilizas la [versión de Ruby 2.0.0](https://www.ruby-lang.org/en/installation/) o superior.

Ejecuta el siguiente comando para empezar:

```bash
$ sudo gem install cocoapods
```

- Si se te pide que sobrescribas el ejecutable `rake`, consulta [Introducción](http://guides.cocoapods.org/using/getting-started.html) en CocoaPods.org para más detalles.
- Si tienes problemas con CocoaPods, consulta la [guía de solución de problemas de CocoaPods](http://guides.cocoapods.org/using/troubleshooting.html).

### Paso 2: Construir el archivo de bibliotecas {#step-2-constructing-the-podfile}

Ahora que has instalado la gema Ruby de CocoaPods, tendrás que crear un archivo en el directorio de tu proyecto de Xcode llamado `Podfile`.

Añade la siguiente línea a tu archivo de bibliotecas:

```
target 'YourAppTarget' do
  pod 'Appboy-tvOS-SDK'
end
```

Te sugerimos que versiones Braze para que las actualizaciones de pods recojan automáticamente cualquier cosa menor que una actualización de versión menor. Esto se ve así: `pod 'Appboy-tvOS-SDK' ~> Major.Minor.Build`. Si quieres integrar automáticamente la última versión del SDK de Braze, incluso con cambios importantes, puedes utilizar `pod 'Appboy-tvOS-SDK'` en tu archivo de bibliotecas.

### Paso 3: Instalación del SDK de Braze {#step-3-installing-the-braze-sdk}

Para instalar los CocoaPods del SDK de Braze, ve al directorio de tu proyecto de aplicación Xcode en tu terminal y ejecuta el siguiente comando:
```
pod install
```

En este punto, deberías poder abrir el nuevo espacio de trabajo del proyecto Xcode creado por CocoaPods. Asegúrate de utilizar este espacio de trabajo de Xcode en lugar de tu proyecto de Xcode.

![]({% image_buster /assets/img_archive/podsworkspace.png %})

### Paso 4: Actualizar el delegado de tu aplicación {#step-4-updating-your-app-delegate}

{% tabs %}
{% tab OBJECTIVE-C %}

Añade la siguiente línea de código a tu archivo `AppDelegate.m`:

```objc
#import <AppboyTVOSKit/AppboyKit.h>
```

Dentro de tu archivo `AppDelegate.m`, añade el siguiente fragmento de código dentro de tu método `application:didFinishLaunchingWithOptions`:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
         inApplication:application
     withLaunchOptions:launchOptions];
```

Por último, actualiza `YOUR-API-KEY` con el valor correcto desde tu página **Administrar configuración**.

{% endtab %}
{% tab swift %}

Si estás integrando el SDK de Braze con CocoaPods o Carthage, añade la siguiente línea de código a tu archivo `AppDelegate.swift`:

```swift
import AppboyTVOSKit
```

Para más información sobre el uso de código Objective-C en proyectos Swift, consulta los [documentos para desarrolladores de Apple](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html).

En `AppDelegate.swift`, añade el siguiente fragmento de código a tu `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```

A continuación, actualiza `YOUR-API-KEY` con el valor correcto desde tu página **Administrar configuración**.

Nuestro singleton `sharedInstance` será nulo antes de llamar a `startWithApiKey:`, ya que es un requisito previo para utilizar cualquier funcionalidad de Braze.

{% endtab %}
{% endtabs %}

{% alert warning %}
Asegúrate de inicializar Braze en el hilo principal de tu aplicación. Inicializar de forma asíncrona puede provocar fallos en la funcionalidad.
{% endalert %}

### Paso 5: Especifica tu punto de conexión personalizado o clúster de datos {#step-5-specify-your-custom-endpoint-or-data-cluster}

{% alert note %}
A partir de diciembre de 2019, ya no se proporcionan puntos de conexión personalizados; si tienes un punto de conexión personalizado preexistente, puedes seguir utilizándolo. Para más detalles, consulta nuestra <a href="{{site.baseurl}}/api/basics/#endpoints">lista de puntos de conexión disponibles</a>.
{% endalert %}

Tu representante de Braze ya debería haberte informado del [punto de conexión correcto]({{ site.baseurl }}/user_guide/administrative/access_braze/sdk_endpoints/).

#### Configuración del punto de conexión en tiempo de compilación (recomendado) {#compile-time-endpoint-configuration-recommended}
Si se te proporciona un punto de conexión personalizado preexistente:
- A partir de la versión 3.0.2 del SDK iOS de Braze, puedes establecer un punto de conexión personalizado utilizando el archivo `Info.plist`. Añade el diccionario `Appboy` a tu archivo Info.plist. Dentro del diccionario `Appboy`, añade la subentrada de cadena `Endpoint` y establece el valor a la autoridad de URL de tu punto de conexión personalizado (por ejemplo, `sdk.iad-01.braze.com`, no `https://sdk.iad-01.braze.com`).

#### Configuración del punto de conexión en tiempo de ejecución {#runtime-endpoint-configuration}
Si se te proporciona un punto de conexión personalizado preexistente:
- A partir de la versión 3.17.0+ del SDK iOS de Braze, puedes anular la configuración de tu punto de conexión a través de `ABKEndpointKey` dentro del parámetro `appboyOptions` pasado a `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Establece el valor a la autoridad de URL de tu punto de conexión personalizado (por ejemplo, `sdk.iad-01.braze.com`, no `https://sdk.iad-01.braze.com`).

{% alert note %}
Se ha eliminado en la versión 3.17.0 del SDK iOS de Braze el soporte para la configuración de puntos de conexión en tiempo de ejecución mediante `ABKAppboyEndpointDelegate`. Si ya utilizas `ABKAppboyEndpointDelegate`, ten en cuenta que en las versiones v3.14.1 a v3.16.0 del SDK de Braze para iOS, cualquier referencia a `dev.appboy.com` en tu método `getApiEndpoint()` debe sustituirse por una referencia a `sdk.iad-01.braze.com`.
{% endalert %}

### Integración del SDK completa {#sdk-integration-complete}

Ahora Braze debería estar recopilando datos de tu aplicación, y tu integración básica debería estar completa. Ten en cuenta que al compilar tu aplicación tvOS y cualquier otra biblioteca de terceros, Bitcode debe estar habilitado.

### Actualizar el SDK de Braze mediante CocoaPods {#updating-the-braze-sdk-via-cocoapods}

Para actualizar un CocoaPod, simplemente ejecuta los siguientes comandos dentro del directorio de tu proyecto:

```
pod update
```

## Personalizar Braze al iniciarse {#customizing-braze-on-startup}

Si deseas personalizar Braze al iniciarse, puedes utilizar en su lugar el método de inicialización de Braze `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions` y pasar un `NSDictionary` opcional de claves de inicio de Braze.
{% tabs %}
{% tab OBJECTIVE-C %}

En tu archivo `AppDelegate.m`, dentro de tu método `application:didFinishLaunchingWithOptions`, añade el siguiente método de Braze:

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab swift %}

En `AppDelegate.swift`, dentro de tu método `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`, añade el siguiente método de Braze:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:appboyOptions)
```

donde `appboyOptions` es un `Dictionary` de valores de configuración de inicio.

{% endtab %}
{% endtabs %}

Este método sustituiría al método de inicialización `startWithApiKey:inApplication:withLaunchOptions:` y se llama con los siguientes parámetros:

- `YOUR-API-KEY`: La clave de API de tu aplicación se encuentra en **Administrar configuración** en el panel de Braze.
- `application`: La aplicación actual.
- `launchOptions`: Las opciones `NSDictionary` que obtienes de `application:didFinishLaunchingWithOptions:`.
- `appboyOptions`: Un `NSDictionary` opcional con valores de configuración de inicio para Braze.

Consulta [Appboy.h](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) para ver una lista de las claves de inicio de Braze.

## Appboy.sharedInstance() y anulabilidad en Swift {#appboysharedinstance-and-swift-nullability}
A diferencia de la práctica habitual, el singleton `Appboy.sharedInstance()` es opcional. Esto se debe a que `sharedInstance` es `nil` antes de que se llame a `startWithApiKey:`, y hay algunas implementaciones no estándar pero no inválidas en las que se puede utilizar una inicialización retardada.

Si llamas a `startWithApiKey:` en tu delegado `didFinishLaunchingWithOptions:` antes de cualquier acceso al `sharedInstance` de Appboy (la implementación estándar), puedes utilizar el encadenamiento opcional, como `Appboy.sharedInstance()?.changeUser("testUser")`, para evitar comprobaciones engorrosas. Esto tendrá paridad con una implementación de Objective-C que haya asumido un `sharedInstance` no nulo.

## Opciones de integración manual {#manual-integration-options}

También puedes integrar nuestro SDK para tvOS manualmente: simplemente obtén el Framework de nuestro [repositorio público](https://github.com/appboy/appboy-ios-sdk) e inicializa Braze como se indica en las secciones anteriores.

## Identificación de usuarios e informes de análisis {#identifying-users-and-reporting-analytics}
Consulta nuestra [documentación de iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=swift) para obtener información sobre la configuración de ID de usuario, el registro de eventos personalizados y la configuración de atributos de usuario. También te recomendamos que te familiarices con nuestras [convenciones de nomenclatura de eventos]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions/).