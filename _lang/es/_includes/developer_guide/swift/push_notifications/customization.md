{% multi_lang_include developer_guide/prerequisites/swift.md %} También tendrás que [configurar las notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

## Personalización de los botones de acción {#push-action-buttons-integration}

El SDK Swift de Braze proporciona soporte de gestión de URL para botones de acción push. Hay cuatro conjuntos de botones de acción para notificación push predeterminados para las categorías push predeterminadas de Braze: `Accept/Decline`, `Yes/No`, `Confirm/Cancel` y `More`.

![Un GIF de un mensaje push que se desliza hacia abajo para mostrar dos botones de acción personalizables.]({% image_buster /assets/img_archive/iOS8Action.gif %}){: style="max-width:60%"}

### Registro manual de botones de acción {#manually-registering-action-buttons}

{% alert important %}
No se recomienda el registro manual de los botones de acción para notificación push.
{% endalert %}

Si [configuras las notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift) mediante la opción de configuración `configuration.push.automation`, Braze registra automáticamente los botones de acción para las categorías push predeterminadas y gestiona el análisis de clics en los botones de acción push y el enrutamiento de URL.

Sin embargo, puedes optar por registrar manualmente los botones de acción para notificación push.

#### Paso 1: Añadir categorías push predeterminadas de Braze {#registering}

Utiliza el siguiente código para registrarte en las categorías push predeterminadas cuando te [registres para push]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-4-register-push-tokens-with-braze):

{% tabs %}
{% tab swift %}
a
```swift
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[[UNUserNotificationCenter currentNotificationCenter] setNotificationCategories:BRZNotifications.categories];
```

{% endtab %}
{% endtabs %}

{% alert note %}
Al hacer clic en los botones de acción push con modo de activación en segundo plano, solo se descartará la notificación y no se abrirá la aplicación. La próxima vez que el usuario abra la aplicación, el análisis de clics en el botón de estas acciones se enviará al servidor.
{% endalert %}

#### Paso 2: Habilitar la gestión interactiva de push {#enable-push-handling}

Para habilitar la gestión de nuestro botón de acción push, incluidos el análisis de clics y el enrutamiento de URL, añade el siguiente código al método delegado `didReceive(_:completionHandler:)` de tu aplicación:

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.notifications.handleUserNotification(response: response, withCompletionHandler: completionHandler)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                              withCompletionHandler:completionHandler];
```

{% endtab %}
{% endtabs %}

Si utilizas el framework `UNNotification` y has implementado los [métodos de notificación]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-5-enable-push-handling) de Braze, ya deberías tener integrado este método.

## Personalización de categorías push {#customizing-push-categories}

Además de proporcionar un conjunto de categorías push predeterminadas, Braze admite categorías y acciones de notificación personalizadas. Después de registrar las categorías en tu aplicación, puedes utilizar el panel de Braze para enviar estas categorías de notificación personalizadas a tus usuarios.

Aquí tienes un ejemplo que aprovecha la `LIKE_CATEGORY` que aparece en el dispositivo:

![Un mensaje push que muestra dos botones de acción para notificación push "unlike" y "like".]({% image_buster /assets/img_archive/push_example_category.png %})

### Paso 1: Registrar una categoría {#step-1-register-a-category}

Para registrar una categoría en tu aplicación, utiliza un enfoque similar al siguiente:

{% tabs %}
{% tab swift %}

```swift
Braze.Notifications.categories.insert(
  .init(identifier: "LIKE_CATEGORY",
        actions: [
          .init(identifier: "LIKE_IDENTIFIER", title: "Like", options: [.foreground]),
          .init(identifier: "UNLIKE_IDENTIFIER", title: "Unlike", options: [.foreground])
        ],
        intentIdentifiers: []
       )
)
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
NSMutableSet<UNNotificationCategory *> *categories = [BRZNotifications.categories mutableCopy];

UNNotificationAction *likeAction = [UNNotificationAction actionWithIdentifier:@"LIKE_IDENTIFIER"
                                                                        title:@"Like"
                                                                      options:UNNotificationActionOptionForeground];

UNNotificationAction *unlikeAction = [UNNotificationAction actionWithIdentifier:@"UNLIKE_IDENTIFIER"
                                                                          title:@"Unlike"
                                                                        options:UNNotificationActionOptionForeground];

UNNotificationCategory *likeCategory = [UNNotificationCategory categoryWithIdentifier:@"LIKE_CATEGORY"
                                                                              actions:@[likeAction, unlikeAction]
                                                                    intentIdentifiers:@[]
                                                                              options:UNNotificationCategoryOptionNone];

[categories addObject:likeCategory];
[UNUserNotificationCenter.currentNotificationCenter setNotificationCategories:categories];
```

{% endtab %}
{% endtabs %}

{% alert note %}
Cuando creas un `UNNotificationAction`, puedes especificar una lista de opciones de acción. Por ejemplo, `.foreground` permite a tus usuarios abrir tu aplicación después de pulsar el botón de acción. Esto es necesario para los comportamientos de navegación al hacer clic, como "Abrir aplicación" y "Vínculo profundo dentro de la aplicación". Si deseas un botón de acción que simplemente descarte la notificación sin abrir la aplicación, omite `.foreground` de la matriz `options` de la acción. Para más información, consulta [`UNNotificationActionOptions`](https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions).
{% endalert %}

### Paso 2: Selecciona tus categorías {#step-2-select-your-categories}

Después de registrar una categoría, utiliza el panel de Braze para enviar notificaciones de ese tipo a los usuarios.

{% alert tip %}
Solo necesitas definir botones de acción en el panel de Braze para comportamientos que no se pueden crear localmente en tu código Swift, como vínculos en profundidad a tu aplicación o redireccionamientos a una URL web. Estas acciones deben configurarse en el panel para que puedan definir qué URL o vínculo profundo abrir. En el caso de los botones de acción que simplemente descartan la notificación sin abrir la aplicación, no es necesario configurarlos en el panel, ya que iOS gestiona automáticamente el comportamiento de descarte. Solo tienes que registrar tu categoría personalizada y sus acciones en el código de tu aplicación y, a continuación, introducir el nombre de la categoría correspondiente en el panel.
{% endalert %}

1. En el panel de Braze, selecciona **Mensajería** > **Notificaciones push** y, a continuación, elige tu [campaña push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message) de iOS.
2. En **Redactar notificación push**, activa **Botones de acción**.
3. En el desplegable **Categoría de notificación de iOS**, selecciona **Introducir categoría personalizada de iOS previamente registrada**.
4. Por último, introduce una de las categorías que creaste anteriormente. El siguiente ejemplo utiliza la categoría personalizada: `LIKE_CATEGORY`.

![El panel de Campaign de notificaciones push con la configuración de categorías personalizadas.]({% image_buster /assets/img_archive/ios-notification-category.png %})

### Ejemplo: categoría push personalizada {#example-custom-push-category}

Supongamos que deseas crear una notificación push con dos botones de acción: **Administrar**, que establece un vínculo profundo a tu aplicación, y **Conservar**, que simplemente descarta la notificación.

En el siguiente ejemplo, la acción `MANAGE_IDENTIFIER` incluye la opción `.foreground`, que abre la aplicación cuando se pulsa; esto es necesario porque establecerá un vínculo profundo con una parte específica de la aplicación. La acción `KEEP_IDENTIFIER` utiliza una matriz de opciones vacía, lo que significa que descartará la notificación sin abrir la aplicación.

{% tabs %}
{% tab swift %}

```swift
Braze.Notifications.categories.insert(
  .init(identifier: "YOUR_CATEGORY",
        actions: [
          .init(identifier: "KEEP_IDENTIFIER", title: "Keep", options: []),
          .init(identifier: "MANAGE_IDENTIFIER", title: "Manage", options: [.foreground])
        ],
        intentIdentifiers: []
       )
)
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% endtabs %}

Dado que `MANAGE_IDENTIFIER` establece un vínculo profundo a la aplicación, deberías configurar ese botón de acción en el panel de Braze con la URL del vínculo profundo asociado. Sin embargo, no es necesario definir un botón en el panel para `KEEP_IDENTIFIER`, ya que solo descarta la notificación. En el panel, solo tienes que introducir el nombre de la categoría (por ejemplo, `YOUR_CATEGORY`) que coincida con el que registraste en el código de tu aplicación.

## Personalización de señales {#customizing-badges}

Las señales son pequeños iconos ideales para llamar la atención del usuario. Puedes especificar un recuento de señales en la pestaña [**Configuración**]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_settings) cuando redactes una notificación push utilizando el panel de Braze. También puedes actualizar manualmente el recuento de señales a través de la propiedad [`applicationIconBadgeNumber`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber) de tu aplicación o la [carga útil de notificación remota](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1).

Braze borrará automáticamente el recuento de señales cuando se reciba una notificación de Braze mientras la aplicación esté en primer plano. Si estableces manualmente el número de la señal en 0, también se borrarán las notificaciones del centro de notificaciones.

Si no tienes un plan para borrar las señales como parte del funcionamiento normal de la aplicación o mediante el envío de push que borren la señal, debes borrar la señal cuando la aplicación se active añadiendo el siguiente código al método delegado `applicationDidBecomeActive:` de tu aplicación:

{% tabs %}
{% tab swift %}

```swift
// For iOS 16.0+
let center = UNUserNotificationCenter.current()
do {
  try await center.setBadgeCount(0)
} catch {
  // Handle errors
}

// Prior to iOS 16. Deprecated in iOS 17+.
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
// For iOS 16.0+
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
[center setBadgeCount:0 withCompletionHandler:^(NSError * _Nullable error) {
    if (error != nil) {
        // Handle errors
    }
}];

// Prior to iOS 16. Deprecated in iOS 17+.
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% endtabs %}

## Personalización de sonidos {#customizing-sounds}

### Paso 1: Aloja el sonido en tu aplicación {#step-1-host-the-sound-in-your-app}

Los sonidos de notificación push personalizados deben alojarse localmente dentro del paquete principal de tu aplicación. Se aceptan los siguientes formatos de datos de audio:

- PCM lineal
- MA4
- µLaw
- aLaw

Puedes empaquetar los datos de audio en un archivo AIFF, WAV o CAF. En Xcode, añade el archivo de sonido a tu proyecto como un recurso no localizado del paquete de la aplicación.

{% alert note %}
Los sonidos personalizados deben durar menos de 30 segundos cuando se reproducen. Si un sonido personalizado supera ese límite, se reproduce en su lugar el sonido predeterminado del sistema.
{% endalert %}

#### Convertir archivos de sonido {#converting-sound-files}

Puedes utilizar la herramienta afconvert para convertir sonidos. Por ejemplo, para convertir el sonido del sistema PCM lineal de 16 bits Submarine.aiff a audio IMA4 en un archivo CAF, utiliza el siguiente comando en el terminal:

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

{% alert tip %}
Puedes inspeccionar un sonido para determinar su formato de datos abriéndolo en QuickTime Player y eligiendo **Show Movie Inspector** en el menú **Movie**.
{% endalert %}

### Paso 2: Proporciona una URL de protocolo para el sonido {#step-2-provide-a-protocol-url-for-the-sound}

Debes especificar una URL de protocolo que dirija a la ubicación del archivo de sonido en tu aplicación. Hay dos métodos para hacerlo:

* Utiliza el parámetro `sound` del [objeto push de Apple]({{site.baseurl}}/api/objects_filters/messaging/apple_object#apple-push-object) para pasar la URL a Braze.
* Especifica la URL en el panel. En el [creador push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message#step-3-select-notification-type-ios-and-android), selecciona **Configuración** e introduce la URL del protocolo en el campo **Sonido**.

![El creador push en el panel de Braze]({% image_buster /assets/img_archive/sound_push_ios.png %})

Si el archivo de sonido especificado no existe o se introduce la palabra clave "default", Braze utilizará el sonido de alerta predeterminado del dispositivo. Además de nuestro panel, el sonido también se puede configurar a través de nuestra [API de mensajería][12].

Consulta la documentación para desarrolladores de Apple relativa a la [preparación de sonidos de alerta personalizados](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html) para obtener información adicional.

## Configuración {#settings}

Al crear una campaña push a través del panel, haz clic en la pestaña **Configuración** del paso **Redactar** para ver la configuración avanzada disponible.

![Pestaña de configuración avanzada del creador de Campaign push de Braze para iOS.]({% image_buster /assets/img_archive/ios_advanced_settings.png %})

### Pares clave-valor {#key-value-pairs}

Braze te permite enviar pares clave-valor de cadena definidos a medida, conocidos como `extras`, junto con una notificación push a tu aplicación. Los extras pueden definirse a través del panel o de la API y estarán disponibles como pares clave-valor dentro del diccionario `notification` pasado a tus implementaciones de delegados push.

### Opciones de alerta {#alert-options}

Selecciona la casilla **Opciones de alerta** para ver un desplegable de valores clave disponibles para ajustar cómo aparece la notificación en los dispositivos.

### Añadir el indicador de contenido disponible {#adding-content-available-flag}

Marca la casilla **Añadir indicador de contenido disponible** para indicar a los dispositivos que descarguen nuevos contenidos en segundo plano. Lo más habitual es marcar esta opción si te interesa enviar [notificaciones silenciosas]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift).

### Añadir el indicador de contenido mutable {#adding-mutable-content-flag}

Marca la casilla **Añadir indicador de contenido mutable** para habilitar la personalización avanzada del receptor. Este indicador se enviará automáticamente al componer una [notificación enriquecida]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift), independientemente del valor de esta casilla.

### ID de contracción {#collapse-id}

Especifica un ID de contracción para agrupar notificaciones similares. Si envías varias notificaciones con el mismo ID de contracción, el dispositivo solo mostrará la notificación recibida más recientemente. Consulta la documentación de Apple sobre [notificaciones agrupadas](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1).

### Caducidad {#expiry}

Si marcas la casilla **Caducidad**, podrás establecer un tiempo de caducidad para tu mensaje. Si el dispositivo de un usuario pierde la conectividad, Braze seguirá intentando enviar el mensaje hasta la hora especificada. Si no se configura, la plataforma tendrá una caducidad predeterminada de 30 días. Ten en cuenta que las notificaciones push que caducan antes de la entrega no se consideran fallidas y no se registrarán como rebotadas.