---
nav_title: Ubicaciones y geovallas
article_title: Ubicaciones y geovallas para iOS
platform: iOS
page_order: 6
description: "Este artículo de referencia explica cómo implementar ubicaciones y geovallas en tu aplicación de iOS."
tool:
  - Location

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Ubicaciones y geovallas {#locations-and-geofences}

Para habilitar geovallas en iOS:

1. Tu integración debe admitir notificaciones push en segundo plano.
2. Las geovallas de Braze [deben habilitarse]({{site.baseurl}}/developer_guide/geofences?sdktab=swift) a través del SDK, ya sea habilitando implícitamente la recopilación de ubicaciones o habilitando explícitamente la recopilación de geovallas. No están habilitadas de forma predeterminada.

{% alert important %}
A partir de iOS 14, las geovallas no funcionan de forma fiable para los usuarios que deciden dar permiso de ubicación aproximada.
{% endalert %}

## Paso 1: Habilitar push en segundo plano {#step-1-enable-background-push}

Para utilizar completamente nuestra estrategia de sincronización de geovallas, debes tener habilitado el [push en segundo plano]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/silent_push_notifications#use-silent-push-notifications-to-trigger-background-work) además de completar la integración push estándar.

## Paso 2: Habilitar geovallas {#step-2-enable-geofences}

De forma predeterminada, las geovallas se habilitan en función de si la recopilación automática de ubicación está habilitada. Puedes habilitar las geovallas utilizando el archivo `Info.plist`. Añade el diccionario `Braze` a tu archivo `Info.plist`. Dentro del diccionario `Braze`, añade la subentrada booleana `EnableGeofences` y establece el valor en `YES`. Ten en cuenta que antes de la versión v4.0.2 del SDK de Braze para iOS, se debe utilizar la clave de diccionario `Appboy` en lugar de `Braze`.

También puedes habilitar las geovallas en el momento de inicio de la aplicación utilizando el método [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24). En el diccionario `appboyOptions`, establece `ABKEnableGeofencesKey` en `YES`. Por ejemplo:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKEnableGeofencesKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKEnableGeofencesKey : true ])
```

{% endtab %}
{% endtabs %}

## Paso 3: Verificar el push en segundo plano de Braze {#step-3-check-for-braze-background-push}

Braze sincroniza las geovallas con los dispositivos mediante notificaciones push en segundo plano. Sigue el artículo de [personalización de iOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/ignoring_internal_push) para asegurarte de que tu aplicación no realice acciones no deseadas al recibir las notificaciones de sincronización de geovallas de Braze.

## Paso 4: Añadir NSLocationAlwaysUsageDescription a tu Info.plist {#step-4-add-nslocationalwaysusagedescription-to-your-infoplist}

Añade las claves `NSLocationAlwaysUsageDescription` y `NSLocationAlwaysAndWhenInUseUsageDescription` a tu `info.plist` con un valor `String` que contenga una descripción de por qué tu aplicación necesita rastrear la ubicación. Ambas claves son obligatorias en iOS 11 o posterior.
Esta descripción se mostrará cuando el mensaje del sistema de ubicación solicite autorización y debe explicar claramente los beneficios del seguimiento de ubicación a tus usuarios.

## Paso 5: Solicitar autorización del usuario {#step-5-request-authorization-from-the-user}

La característica de geovallas solo funciona cuando se concede la autorización de ubicación `Always`.

Para solicitar la autorización de ubicación `Always`, utiliza el siguiente código:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
CLLocationManager *locationManager = [[CLLocationManager alloc] init];
[locationManager requestAlwaysAuthorization];
```

{% endtab %}
{% tab swift %}

```swift
var locationManager = CLLocationManager()
locationManager.requestAlwaysAuthorization()
```

{% endtab %}
{% endtabs %}

## Paso 6: Habilitar geovallas en el panel {#step-6-enable-geofences-on-the-dashboard}

iOS solo permite almacenar hasta 20 geovallas para una aplicación determinada. El uso de ubicaciones ocupará algunas de estas 20 ranuras de geovallas disponibles. Para evitar interrupciones accidentales o no deseadas en otras funciones relacionadas con las geovallas de tu aplicación, las geovallas de ubicación deben habilitarse para aplicaciones individuales en el panel.

Para que las ubicaciones funcionen correctamente, también debes confirmar que tu aplicación no está utilizando todas las ranuras de geovallas disponibles.

### Habilitar geovallas desde la página de ubicaciones: {#enable-geofences-from-the-locations-page}

![Las opciones de geovallas en la página de ubicaciones de Braze.]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### Habilitar geovallas desde la página de configuración: {#enable-geofences-from-the-settings-page}

![La casilla de verificación de geovallas en las páginas de configuración de Braze.]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %})

## Desactivar las solicitudes automáticas de geovallas {#disabling-automatic-geofence-requests}

A partir de la versión 3.21.3 del SDK para iOS, puedes desactivar la solicitud automática de geovallas. Puedes hacerlo utilizando el archivo `Info.plist`. Añade el diccionario `Braze` a tu archivo `Info.plist`. Dentro del diccionario `Braze`, añade la subentrada booleana `DisableAutomaticGeofenceRequests` y establece el valor en `YES`.

También puedes desactivar las solicitudes automáticas de geovallas en el momento del inicio de la aplicación a través del método [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`](https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24). En el diccionario `appboyOptions`, establece `ABKDisableAutomaticGeofenceRequestsKey` en `YES`. Por ejemplo:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKDisableAutomaticGeofenceRequestsKey : @(YES) }];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKDisableAutomaticGeofenceRequestsKey : true ])
```

{% endtab %}
{% endtabs %}

Si eliges utilizar esta opción, tendrás que solicitar manualmente las geovallas para que la característica funcione.

## Solicitar geovallas manualmente {#manually-requesting-geofences}

Cuando el SDK de Braze solicita geovallas para monitorear desde el backend, informa la ubicación actual del usuario y recibe las geovallas que se consideran óptimamente relevantes según la ubicación reportada. Existe un límite de velocidad de una actualización de geovallas por sesión.

Para controlar la ubicación que el SDK informa con el fin de recibir las geovallas más relevantes, a partir de la versión 3.21.3 del SDK para iOS, puedes solicitar geovallas manualmente proporcionando la latitud y longitud de una ubicación. Se recomienda desactivar las solicitudes automáticas de geovallas cuando utilices este método. Para hacerlo, usa el siguiente código:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] requestGeofencesWithLongitude:longitude
                                              latitude:latitude];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.requestGeofences(withLongitude: longitude, latitude: latitude)
```

{% endtab %}
{% endtabs %}