---
nav_title: CocoaPods
article_title: Integración de CocoaPods para iOS
platform: iOS
page_order: 2
description: "Este artículo de referencia muestra cómo integrar el SDK de Braze utilizando CocoaPods para iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integración de CocoaPods {#cocoapods-integration}

## Paso 1: Instalar CocoaPods {#step-1-install-cocoapods}

La instalación del SDK de iOS a través de [CocoaPods](http://cocoapods.org/) automatiza la mayor parte del proceso de instalación por ti. Antes de comenzar este proceso, asegúrate de que utilizas [la versión 2.0.0 de Ruby](https://www.ruby-lang.org/en/installation/) o superior. No te preocupes, no es necesario conocer la sintaxis de Ruby para instalar este SDK.

Ejecuta el siguiente comando para empezar:

```bash
$ sudo gem install cocoapods
```

Si tienes problemas relacionados con CocoaPods, consulta la [guía de solución de problemas](http://guides.cocoapods.org/using/troubleshooting.html) de CocoaPods.

{% alert note %}
Si se te pide que sobrescribas el ejecutable `rake`, consulta las instrucciones de [primeros pasos](http://guides.cocoapods.org/using/getting-started.html) en CocoaPods.org para más detalles.
{% endalert %}

## Paso 2: Construir el Podfile {#step-2-constructing-the-podfile}

Ahora que has instalado la gema de Ruby de CocoaPods, tendrás que crear un archivo en el directorio de tu proyecto Xcode llamado `Podfile`.

Añade la siguiente línea a tu Podfile:

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'
end
```

Te sugerimos que versiones Braze para que las actualizaciones de pods recojan automáticamente cualquier cambio menor a una actualización de versión menor. Esto se ve así: `pod 'Appboy-iOS-SDK' ~> Major.Minor.Build`. Si quieres integrar automáticamente la última versión del SDK de Braze, incluso con cambios importantes, puedes utilizar `pod 'Appboy-iOS-SDK'` en tu Podfile.

### Subspecs {#subspecs}

Recomendamos que los integradores importen nuestro SDK completo. Sin embargo, si estás seguro de que solo vas a integrar una característica concreta de Braze, puedes importar solo la subspec de interfaz de usuario deseada en lugar del SDK completo.

| Subspec | Detalles |
| ------- | ------- |
| `pod 'Appboy-iOS-SDK/InAppMessage'` | La subspec `InAppMessage` contiene la interfaz de usuario de mensajes dentro de la aplicación de Braze y el SDK central.|
| `pod 'Appboy-iOS-SDK/ContentCards'` | La subspec `ContentCards` contiene la interfaz de usuario de Content Cards de Braze y el SDK central. |
| `pod 'Appboy-iOS-SDK/NewsFeed'` | La subspec `NewsFeed` contiene el SDK central de Braze. |
| `pod 'Appboy-iOS-SDK/Core'` | La subspec `Core` contiene soporte para análisis, como eventos personalizados y atributos. |
{: .ws-td-nw-1 aria-label="Subspecs" }

## Paso 3: Instalación del SDK de Braze {#step-3-installing-the-braze-sdk}

Para instalar el SDK de Braze mediante CocoaPods, navega al directorio de tu proyecto de aplicación Xcode en tu terminal y ejecuta el siguiente comando:
```
pod install
```

En este punto, deberías poder abrir el nuevo espacio de trabajo del proyecto Xcode creado por CocoaPods. Asegúrate de utilizar este espacio de trabajo de Xcode en lugar de tu proyecto de Xcode.

![Una carpeta de ejemplo de Appboy expandida para mostrar el nuevo `AppbpyExample.workspace`.]({% image_buster /assets/img_archive/podsworkspace.png %})

## Próximos pasos {#next-steps}

Sigue las instrucciones para [completar la integración]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration).

## Actualizar el SDK de Braze mediante CocoaPods {#updating-the-braze-sdk-via-cocoapods}

Para actualizar un CocoaPod, simplemente ejecuta el siguiente comando dentro del directorio de tu proyecto:

```
pod update
```

