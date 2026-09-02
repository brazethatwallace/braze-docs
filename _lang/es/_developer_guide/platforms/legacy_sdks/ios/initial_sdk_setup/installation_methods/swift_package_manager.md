---
nav_title: Swift Package Administrador
article_title: Integración de Swift Package Administrador para iOS
platform: iOS
page_order: 3
description: "Este tutorial cubre la instalación del SDK or kit de desarrollo de software de Braze utilizando Swift Package Administrador para iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integración con Swift Package Administrador {#swift-package-manager-integration}

La instalación del SDK or kit de desarrollo de software de iOS mediante [Swift Package Administrador](https://swift.org/package-manager/) (SPM) automatiza la mayor parte del proceso de instalación. Antes de comenzar este proceso, asegúrate de que utilizas Xcode 12 o superior.

{% alert note %}
tvOS no está disponible actualmente a través de Swift Package Administrador.
{% endalert %}

## Paso 1: Añadir la dependencia a tu proyecto {#step-1-adding-the-dependency-to-your-project}

### Importar versión del SDK or kit de desarrollo de software {#import-sdk-version}

Abre tu proyecto y ve a la configuración del mismo. Selecciona la pestaña **Swift Packages** y haz clic en el botón <i class="fas fa-plus"></i> añadir debajo de la lista de paquetes.

![Configuración del proyecto en Xcode con la pestaña Swift Packages seleccionada.]({% image_buster /assets/img/ios/spm/swiftpackages.png %})

Al importar la versión del SDK or kit de desarrollo de software `3.33.1` o posterior, introduce la URL de nuestro repositorio del SDK or kit de desarrollo de software de iOS (`https://github.com/braze-inc/braze-ios-sdk`) en el campo de texto y haz clic en **Next**.

Para las versiones `3.29.0` a `3.32.0`, utiliza la URL `https://github.com/Appboy/Appboy-ios-sdk`.

![Diálogo de Xcode para añadir dependencia de paquete con la URL del repositorio del SDK de Braze para iOS.]({% image_buster /assets/img/ios/spm/importsdk_example.png %})

En la siguiente pantalla, selecciona la versión del SDK or kit de desarrollo de software y haz clic en **Next**. Las versiones `3.29.0` y posteriores son compatibles con Swift Package Administrador.

![Selección de versión de paquete en Xcode para el SDK de Braze para iOS.]({% image_buster /assets/img/ios/spm/select_version.png %})

### Seleccionar paquetes {#select-packages}

Selecciona el paquete que mejor se adapte a tus necesidades y haz clic en **Finish**. Asegúrate de seleccionar `AppboyKit` o `AppboyUI`. Incluir ambos paquetes puede provocar un comportamiento no deseado:

- `AppboyUI`
  - Es el más adecuado si piensas utilizar componentes de interfaz de usuario proporcionados por Braze.
  - Incluye `AppboyKit` automáticamente.
- `AppboyKit`
  - Es el más adecuado si no necesitas utilizar ninguno de los componentes de interfaz de usuario proporcionados por Braze (por ejemplo, Content Cards, mensajes dentro de la aplicación, etc.).
- `AppboyPushStory`
  - Incluye este paquete si has integrado Push Stories en tu aplicación. Esto se admite a partir de la versión `3.31.0`.
  - En el menú desplegable de **Add to Target**, selecciona tu destino `ContentExtension` en lugar del destino de tu aplicación principal.

![Pantalla de Xcode para añadir paquete seleccionando los destinos de la biblioteca del SDK de Braze.]({% image_buster /assets/img/ios/spm/add_package.png %})

## Paso 2: Configurar tu proyecto {#step-2-configuring-your-project}

A continuación, ve a la **configuración de compilación** de tu proyecto y añade el indicador `-ObjC` a la opción **Other Linker Flags**. Hay que añadir este indicador y resolver cualquier [error](https://developer.apple.com/library/archive/qa/qa1490/_index.html) para poder seguir integrando el SDK or kit de desarrollo de software.

![Configuración de compilación en Xcode mostrando el campo Other Linker Flags.]({% image_buster /assets/img/ios/spm/buildsettings.png %})

{% alert note %}
Si no añades el indicador `-ObjC`, pueden faltar partes de la API y el comportamiento será indefinido. Puedes encontrarte con errores inesperados como "unrecognized SELECTOR sent to class", fallos de la aplicación y otros problemas.
{% endalert %}

## Paso 3: Editar el esquema del objetivo {#step-3-editing-the-targets-scheme}
{% alert important %}
Si utilizas Xcode 12.5 o posterior, omite este paso.
{% endalert %}

Si utilizas Xcode 12.4 o anterior, edita el esquema del objetivo que incluye el paquete Appboy (elemento del menú **Product > Scheme > Edit Scheme**):
1. Despliega el menú **Build** y selecciona **Post-actions**. Pulsa el botón más (+) y selecciona **New Run Script Action**.
2. En el desplegable **Provide build settings from**, selecciona el destino de tu aplicación.
3.  Copia este script en el campo abierto:
```sh
# iOS
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Appboy.bundle/appboy-spm-cleanup.sh"
# macOS (if applicable)
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Contents/Resources/Appboy.bundle/appboy-spm-cleanup.sh"
```

![Menú de fases de compilación en Xcode para añadir una fase de script de ejecución.]({% image_buster /assets/img/ios/spm/swiftmanager_buildmenu.png %})

## Próximos pasos {#next-steps}

Sigue las instrucciones para [completar la integración]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration).