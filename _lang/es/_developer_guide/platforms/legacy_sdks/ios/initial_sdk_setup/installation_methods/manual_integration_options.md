---
nav_title: Manual
article_title: Opciones de integración manual para iOS
platform: iOS
page_order: 4
description: "En este artículo de referencia se muestra cómo integrar manualmente el SDK or kit de desarrollo de software de Braze para iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integración manual {#manual-integration}

{% alert tip %}
Te recomendamos encarecidamente que implementes el SDK or kit de desarrollo de software mediante un administrador de paquetes como [Swift Package Administrador]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/swift_package_manager), [CocoaPods]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/cocoapods) o [Carthage]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/carthage_integration). Te ahorrará mucho tiempo y automatizará gran parte del proceso. Sin embargo, si no puedes hacerlo, puedes completar la integración manualmente siguiendo las instrucciones.
{% endalert %}

## Paso 1: Descarga del SDK or kit de desarrollo de software de Braze {#step-1-downloading-the-braze-sdk}

### Opción 1: XCFramework dinámico {#option-1-dynamic-xcframework}

1. Descarga `Appboy_iOS_SDK.xcframework.zip` de la [página de la versión](https://github.com/appboy/appboy-ios-sdk/releases) y extrae el archivo.
2. En Xcode, arrastra y suelta este `.xcframework` en tu proyecto.
3. En la pestaña **General** del proyecto, selecciona **Embed & Sign** para `Appboy_iOS_SDK.xcframework`.

### Opción 2: XCFramework estático para integración estática {#option-2-static-xcframework-for-static-integration}

1. Descarga `Appboy_iOS_SDK.zip` desde la [página de la versión](https://github.com/appboy/appboy-ios-sdk/releases).<br><br>
2. En Xcode, desde el navegador de proyectos, selecciona el proyecto o grupo de destino para Braze.<br><br>
3. Navega hasta **File > Add Files > Project_Name**.<br><br>
4. Añade las carpetas `AppboyKit` y `AppboyUI` a tu proyecto como un grupo.
	- Asegúrate de que la opción **Copy items into destination group's folder** está seleccionada si es la primera vez que realizas la integración. Amplía **Options** en el SELECTOR de archivos para seleccionar **Copy items if needed** y **Create groups**.
	- Elimina los directorios `AppboyKit/include` y `AppboyUI/include`.<br><br>
5. (Opcional) Si se te aplica una de las siguientes opciones:
  - Solo quieres las características principales de análisis del SDK or kit de desarrollo de software y no utilizas ninguna característica de la interfaz de usuario (por ejemplo, mensajes dentro de la aplicación o Content Cards).
  - Dispones de una interfaz de usuario personalizada para las características de la interfaz de usuario de Braze y te encargas tú mismo de la descarga de imágenes.<br><br>Puedes utilizar la versión básica del SDK or kit de desarrollo de software eliminando el archivo `ABKSDWebImageProxy.m` y `Appboy.bundle`. Esto eliminará la dependencia del framework `SDWebImage` y todos los recursos relacionados con la interfaz de usuario (por ejemplo, archivos Nib, imágenes, archivos de localización) del SDK or kit de desarrollo de software.

{% alert warning %}
Si intentas utilizar la versión básica del SDK or kit de desarrollo de software sin las características de la interfaz de usuario de Braze, los mensajes dentro de la aplicación no se mostrarán. Si intentas mostrar la interfaz de usuario de Content Cards de Braze con la versión básica, se producirá un comportamiento impredecible.
{% endalert %}

## Paso 2: Añadir las bibliotecas de iOS necesarias {#step-2-adding-required-ios-libraries}

1. Haz clic en el objetivo de tu proyecto (utilizando la navegación de la izquierda) y selecciona la pestaña **Build Phases**.<br><br>
2. Haz clic en el botón <i class="fas fa-plus"></i> situado debajo de **Link Binary With Libraries**.<br><br>
3. En el menú, selecciona `SystemConfiguration.framework`.<br><br>
4. Marca esta biblioteca como necesaria utilizando el menú desplegable situado junto a `SystemConfiguration.framework`.<br><br>
5. Repite la operación para añadir a tu proyecto cada uno de los siguientes frameworks necesarios, marcando cada uno como "required".
	- `QuartzCore.framework`
	- `libz.tbd`
	- `CoreImage.framework`
	- `CoreText.framework`
	- `WebKit.framework`<br><br>
6. Añade los siguientes frameworks y márcalos como opcionales:
	- `CoreTelephony.framework`<br><br>
7. Selecciona la pestaña **Build Settings**. En la sección **Linking**, localiza la configuración **Other Linker Flags** y añade el indicador `-ObjC`.<br><br>
8. El framework `SDWebImage` es necesario para que Content Cards y la mensajería dentro de la aplicación funcionen correctamente. `SDWebImage` se utiliza para descargar y mostrar imágenes, incluidos los GIF. Si pretendes utilizar Content Cards o mensajes dentro de la aplicación, sigue los pasos de integración de SDWebImage.

### Integración de SDWebImage {#sdwebimage-integration}

Para instalar `SDWebImage`, sigue sus [instrucciones](https://github.com/SDWebImage/SDWebImage/wiki/Installation-Guide#build-sdwebimage-as-xcframework) y luego arrastra y suelta el `XCFramework` resultante en tu proyecto.

### Seguimiento de ubicación opcional {#optional-location-tracking}

1. Añade `CoreLocation.framework` para habilitar el seguimiento de ubicación.
2. Debes autorizar la ubicación de tus usuarios utilizando `CLLocationManager` en tu aplicación.

## Paso 3: Cabecera de puente Objective-C {#step-3-objective-c-bridging-header}

{% alert note %}
Si tu proyecto solo utiliza Objective-C, sáltate este paso.
{% endalert %}

Si tu proyecto utiliza Swift, necesitarás un archivo de cabecera puente.

Si no tienes un archivo de cabecera puente, crea uno y nómbralo `your-product-module-name-Bridging-Header.h` eligiendo **File > New > File > (iOS o OS X) > Source > Header File**. A continuación, añade la siguiente línea de código al principio de tu archivo de cabecera puente:
```
#import "AppboyKit.h"
```

En la **Build Settings** de tu proyecto, añade la ruta relativa de tu archivo de cabecera a la configuración de compilación de `Objective-C Bridging Header` en `Swift Compiler - Code Generation`.

## Próximos pasos {#next-steps}

Sigue las instrucciones para [completar la integración]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration).