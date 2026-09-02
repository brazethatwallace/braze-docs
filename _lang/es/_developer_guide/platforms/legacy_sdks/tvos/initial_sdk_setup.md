---
nav_title: Configuración inicial del SDK or kit de desarrollo de software
article_title: Configuración inicial del SDK or kit de desarrollo de software para tvOS
platform: tvOS
page_order: 0
page_type: reference
description: "Esta página cubre los pasos de configuración inicial para el SDK or kit de desarrollo de software de Braze de tvOS."
search_rank: 1
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Configuración inicial del SDK or kit de desarrollo de software {#initial-sdk-setup}

> En este artículo de referencia se explica cómo instalar el SDK or kit de desarrollo de software de Braze para tvOS. La instalación del SDK or kit de desarrollo de software de Braze te proporcionará una funcionalidad básica de análisis.

{% alert note %}
Nuestro SDK or kit de desarrollo de software para tvOS admite actualmente la funcionalidad de análisis. Para añadir una aplicación tvOS en tu panel, abre un [ticket de soporte]({{site.baseurl}}/user_guide/administer/personal/braze_support).
{% endalert %}

El SDK or kit de desarrollo de software de Braze de tvOS debe instalarse o actualizarse mediante [CocoaPods](http://cocoapods.org/), un administrador de dependencias para proyectos Objective-C y Swift. CocoaPods proporciona una mayor simplicidad para la integración y la actualización.

## Integración del SDK or kit de desarrollo de software de tvOS con CocoaPods

### Paso 1: Instalar CocoaPods

Instalar el SDK or kit de desarrollo de software a través de [CocoaPods](http://cocoapods.org/) para tvOS automatiza la mayor parte del proceso de instalación. Antes de comenzar este proceso, asegúrate de que estás utilizando [Ruby versión 2.0.0](https://www.ruby-lang.org/en/installation/) o superior.

Ejecuta el siguiente comando para empezar:

```bash
$ sudo gem install cocoapods
```

- Si se te pide que sobrescribas el ejecutable `rake`, consulta [Getting started](http://guides.cocoapods.org/using/getting-started.html) en CocoaPods.org para más detalles.
- Si tienes problemas con CocoaPods, consulta la [guía de solución de problemas de CocoaPods](http://guides.cocoapods.org/using/troubleshooting.html).

### Paso 2: Construir el Podfile

Ahora que has instalado la gema Ruby de CocoaPods, vas a necesitar crear un archivo en el directorio de tu proyecto Xcode llamado `Podfile`.

Añade la siguiente línea a tu Podfile:

```
target 'YourAppTarget' do
  pod 'Appboy-tvOS-SDK'
end
```

Te sugerimos versionar Braze para que las actualizaciones del pod obtengan automáticamente cualquier cambio menor a una actualización de versión menor. Esto se ve así: `pod 'Appboy-tvOS-SDK' ~> Major.Minor.Build`. Si quieres integrar automáticamente la última versión del SDK or kit de desarrollo de software de Braze, incluso con cambios importantes, puedes usar `pod 'Appboy-tvOS-SDK'` en tu Podfile.

### Paso 3: Instalar el SDK or kit de desarrollo de software de Braze

Para instalar los CocoaPods del SDK or kit de desarrollo de software de Braze, navega al directorio de tu proyecto de aplicación Xcode dentro de tu terminal y ejecuta el siguiente comando:
```
pod install
```

En este punto, deberías poder abrir el nuevo espacio de trabajo del proyecto Xcode creado por CocoaPods. Asegúrate de usar este espacio de trabajo de Xcode en lugar de tu proyecto Xcode.

![En este punto, deberías poder abrir el nuevo espacio de trabajo del proyecto Xcode creado por CocoaPods. Asegúrate de usar este espacio de trabajo de Xcode en lugar de tu proyecto Xcode.]({% image_buster /assets/img_archive/podsworkspace.png %})

### Paso 4: Actualizar el delegado de tu aplicación

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

Por último, actualiza `YOUR-API-KEY` con el valor correcto de tu página **Administrar configuración**.

{% endtab %}
{% tab swift %}

Si estás integrando el SDK or kit de desarrollo de software de Braze con CocoaPods o Carthage, añade la siguiente línea de código a tu archivo `AppDelegate.swift`:

```swift
import AppboyTVOSKit
```

Para más información sobre el uso de código Objective-C en proyectos Swift, consulta la [documentación para desarrolladores de Apple](https://developer.apple.com/library/ios/documentation/swift/conceptual/buildingcocoaapps/MixandMatch.html).

En `AppDelegate.swift`, añade el siguiente fragmento de código a tu `application(application: UIApplication, didFinishLaunchingWithOptions launchOptions: [NSObject: AnyObject]?) -> Bool`:

```swift
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions)
```

A continuación, actualiza `YOUR-API-KEY` con el valor correcto de tu página **Administrar configuración**.

Nuestro singleton `sharedInstance` será nil antes de que se llame a `startWithApiKey:`, ya que es un requisito previo para usar cualquier funcionalidad de Braze.

{% endtab %}
{% endtabs %}

{% alert warning %}
Asegúrate de inicializar Braze en el hilo principal de tu aplicación. Inicializar de forma asíncrona puede provocar un funcionamiento incorrecto.
{% endalert %}

### Paso 5: Especificar tu endpoint personalizado o clúster de datos

{% alert note %}
A partir de diciembre de 2019, ya no se proporcionan endpoints personalizados. Si tienes un endpoint personalizado preexistente, puedes seguir utilizándolo. Para más detalles, consulta nuestra <a href="{{site.baseurl}}/api/basics#endpoints">lista de endpoints disponibles</a>.
{% endalert %}

Tu representante de Braze ya debería haberte indicado el [endpoint correcto]({{ site.baseurl }}/user_guide/administrative/access_braze/sdk_endpoints/).

#### Configuración del endpoint en tiempo de compilación (recomendado)
Si se te proporcionó un endpoint personalizado preexistente:
- A partir del SDK or kit de desarrollo de software de iOS de Braze v3.0.2, puedes establecer un endpoint personalizado utilizando el archivo `Info.plist`. Añade el diccionario `Appboy` a tu archivo Info.plist. Dentro del diccionario `Appboy`, añade la subentrada de cadena `Endpoint` y establece el valor como la autoridad de la URL de tu endpoint personalizado (por ejemplo, `sdk.iad-01.braze.com`, no `https://sdk.iad-01.braze.com`).

#### Configuración del endpoint en tiempo de ejecución
Si se te proporcionó un endpoint personalizado preexistente:
- A partir del SDK or kit de desarrollo de software de iOS de Braze v3.17.0+, puedes sobrescribir tu endpoint a través de `ABKEndpointKey` dentro del parámetro `appboyOptions` pasado a `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:`. Establece el valor como la autoridad de la URL de tu endpoint personalizado (por ejemplo, `sdk.iad-01.braze.com`, no `https://sdk.iad-01.braze.com`).

{% alert note %}
La compatibilidad para establecer endpoints en tiempo de ejecución utilizando `ABKAppboyEndpointDelegate` se eliminó en el SDK or kit de desarrollo de software de iOS de Braze v3.17.0. Si ya utilizas `ABKAppboyEndpointDelegate`, ten en cuenta que en las versiones v3.14.1 a v3.16.0 del SDK or kit de desarrollo de software de iOS de Braze, cualquier referencia a `dev.appboy.com` en tu método `getApiEndpoint()` debe reemplazarse con una referencia a `sdk.iad-01.braze.com`.
{% endalert %}

### Integración del SDK or kit de desarrollo de software completada

Braze debería estar recopilando datos de tu aplicación y tu integración básica debería estar completa. Ten en cuenta que, al compilar tu aplicación tvOS y cualquier otra biblioteca de terceros, Bitcode debe estar habilitado.

### Actualizar el SDK or kit de desarrollo de software de Braze a través de CocoaPods

Para actualizar un CocoaPod, simplemente ejecuta los siguientes comandos dentro del directorio de tu proyecto:

```
pod update
```

## Personalizar Braze durante el inicio

Si deseas personalizar Braze durante el inicio, puedes utilizar en su lugar el método de inicialización de Braze `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions` y pasar un `NSDictionary` opcional de claves de inicio de Braze.
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

Este método reemplazaría al método de inicialización `startWithApiKey:inApplication:withLaunchOptions:` y se llama con los siguientes parámetros:

- `YOUR-API-KEY`: La clave de API de tu aplicación se encuentra en **Administrar configuración** en el panel de Braze.
- `application`: La aplicación actual.
- `launchOptions`: El `NSDictionary` de opciones que obtienes de `application:didFinishLaunchingWithOptions:`.
- `appboyOptions`: Un `NSDictionary` opcional con valores de configuración de inicio para Braze.

Consulta [Appboy.h](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) para obtener una lista de las claves de inicio de Braze.

## Appboy.sharedInstance() y la nulabilidad en Swift
A diferencia de la práctica habitual, el singleton `Appboy.sharedInstance()` es opcional. Esto se debe a que `sharedInstance` es `nil` antes de que se llame a `startWithApiKey:`, y existen algunas implementaciones no estándar, aunque válidas, en las que se puede utilizar una inicialización diferida.

Si llamas a `startWithApiKey:` en tu delegado `didFinishLaunchingWithOptions:` antes de cualquier acceso al `sharedInstance` de Appboy (la implementación estándar), puedes usar el encadenamiento opcional, como `Appboy.sharedInstance()?.changeUser("testUser")`, para evitar comprobaciones engorrosas. Esto tendrá paridad con una implementación en Objective-C que asumiera un `sharedInstance` no nulo.

También puedes integrar nuestro SDK or kit de desarrollo de software de tvOS de forma manual. Simplemente descarga el Framework de nuestro [repositorio público](https://github.com/appboy/appboy-ios-sdk) e inicializa Braze como se indica en las secciones anteriores.

## Identificación de usuarios y análisis de informes
Consulta nuestra [documentación de iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=swift) para obtener información sobre cómo configurar ID de usuario, registrar eventos personalizados y establecer atributos de usuario. También te recomendamos familiarizarte con nuestras [convenciones de nomenclatura de eventos]({{site.baseurl}}/user_guide/data/activation/events/event_naming_conventions).