---
nav_title: Pruebas unitarias (opcional)
article_title: Pruebas unitarias de notificación push para iOS
platform: iOS
page_order: 29.5
description: "Este artículo de referencia describe cómo implementar pruebas unitarias opcionales para tu implementación de push en iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Pruebas unitarias {#unit-tests}

Esta guía opcional describe cómo implementar algunas pruebas unitarias que verificarán si el delegado de tu aplicación sigue correctamente los pasos descritos en nuestras [instrucciones de integración push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration).

Si todas las pruebas pasan, en general, significa que la parte basada en código de tu configuración push es funcional. Si una prueba falla, puede significar que has seguido incorrectamente un paso, o puede ser el resultado de una personalización válida que no se ajusta exactamente a nuestras instrucciones predeterminadas.

En cualquier caso, esto puede ser útil para verificar que has seguido los pasos de la integración y para ayudar a detectar cualquier regresión.

## Paso 1: Crear un objetivo de pruebas unitarias {#step-1-creating-a-unit-tests-target}

Omite este paso si el proyecto de tu aplicación en Xcode ya contiene un paquete de pruebas unitarias.

En el proyecto de tu aplicación, ve al menú **File > New > Target** y añade un nuevo "Unit Testing Bundle". Este paquete puede utilizar Objective-C o Swift y tener cualquier nombre. Establece el "Target to be Tested" como el objetivo principal de tu aplicación.

## Paso 2: Añade el SDK or kit de desarrollo de software de Braze a tus pruebas unitarias {#step-2-add-the-braze-sdk-to-your-unit-tests}

Utilizando el mismo método que utilizaste inicialmente para [instalar el SDK or kit de desarrollo de software de Braze]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview), asegúrate de que la misma instalación del SDK or kit de desarrollo de software también esté disponible para el objetivo de tus pruebas unitarias. Por ejemplo, utilizando CocoaPods:

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'

  target 'YourAppTargetTests' do
    inherit! :search_paths
  end
end
```

## Paso 3: Añade OCMock a tus pruebas unitarias {#step-3-add-ocmock-to-your-unit-tests}

Añade [OCMock](https://ocmock.org/) a tu objetivo de prueba mediante CocoaPods, Carthage o su biblioteca estática. Por ejemplo, utilizando CocoaPods:

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'

  target 'YourAppTargetTests' do
    inherit! :search_paths
    pod 'OCMock'
  end
end
```

## Paso 4: Termina de instalar las bibliotecas añadidas {#step-4-finish-installing-the-added-libraries}

Termina de instalar el SDK or kit de desarrollo de software de Braze y OCMock. Por ejemplo, utilizando CocoaPods, navega hasta el directorio de tu proyecto de aplicación Xcode dentro de tu terminal y ejecuta el siguiente comando:

```
pod install
```

En este punto, deberías poder abrir el espacio de trabajo del proyecto Xcode creado por CocoaPods.

## Paso 5: Añadir pruebas push {#step-5-adding-push-tests}

Crea un nuevo archivo Objective-C en tu objetivo de pruebas unitarias.

Si el objetivo de las pruebas unitarias está en Swift, Xcode puede preguntar: "Would you like to configure an Objective-C bridging header?". El encabezado puente es opcional, por lo que puedes hacer clic en **Don't Create** y seguir ejecutando correctamente estas pruebas unitarias.

Añade el contenido de la aplicación de ejemplo HelloSwift [`AppboyPushUnitTests.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/HelloSwiftTests/AppboyPushUnitTests.m) al nuevo archivo.

## Paso 6: Ejecuta el conjunto de pruebas {#step-6-run-test-suite}

Ejecuta las pruebas unitarias de tu aplicación. Puede ser un paso de verificación único, o puedes incluirlo indefinidamente en tu conjunto de pruebas para ayudar a detectar cualquier regresión.