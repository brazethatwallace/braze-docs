---
nav_title: Historias push
article_title: Push Stories para iOS
platform: iOS
page_order: 27
description: "Este artículo de referencia muestra cómo configurar Push Stories para tu aplicación iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Configuración de Push Stories {#push-story-setup}

La función Push Stories requiere el framework `UNNotification` e iOS 10. La función solo está disponible a partir de la versión 3.2.1 del SDK de iOS.

## Paso 1: Habilitar push en tu aplicación {#step-1-enable-push-in-your-app}

Sigue la [integración de notificaciones push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) para habilitar el push en tu aplicación.

## Paso 2: Añadir el objetivo de la extensión de contenido de notificación {#step-2-adding-the-notification-content-extension-target}

En el proyecto de tu aplicación, ve al menú **File > New > Target...** y añade un nuevo objetivo `Notification Content Extension` y actívalo.

![En el proyecto de tu aplicación, ve al menú File > New > Target... y añade un nuevo objetivo Notification Content Extension y actívalo.]({% image_buster /assets/img/ios/push_story/add_content_extension.png %})

Xcode debería generar un nuevo objetivo y crear archivos automáticamente para ti, entre ellos:

{% tabs %}
{% tab OBJECTIVE-C %}

- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

{% endtab %}
{% tab swift %}

- `NotificationViewController.swift`
- `MainInterface.storyboard`

{% endtab %}
{% endtabs %}

## Paso 3: Habilitar capacidades {#step-3-enable-capabilities}

La característica Push Stories requiere el modo en segundo plano en la sección **Capabilities** del objetivo principal de la aplicación. Después de activar los modos en segundo plano, selecciona **Background fetch** y **Remote notifications**.

![La característica Push Stories requiere el modo en segundo plano en la sección Capabilities del objetivo principal de la aplicación. Después de activar los modos en segundo plano, selecciona Background fetch y Remote notifications.]({% image_buster /assets/img/ios/push_story/enable_background_mode.png %})

### Añadir un grupo de aplicaciones {#adding-an-app-group}

También necesitas añadir `Capability App Groups`. Si no tienes ningún grupo de aplicaciones en tu aplicación, ve a la **Capability** del objetivo principal de la aplicación, activa `App Groups` y haz clic en el botón **+**. Utiliza el ID del paquete de tu aplicación para crear el grupo de aplicaciones. Por ejemplo, si el ID del paquete de tu aplicación es `com.company.appname`, puedes llamar a tu grupo de aplicaciones `group.com.company.appname.xyz`. Debes activar `App Groups` tanto para la aplicación principal como para los objetivos de extensión de contenido.

{% alert important %}
`App Groups` en este contexto se refiere al [derecho a grupos de aplicaciones](https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_security_application-groups) de Apple y no a tu ID de espacio de trabajo de Braze (anteriormente grupo de aplicaciones).
{% endalert %}

Si no añades tu aplicación a un grupo de aplicaciones, es posible que tu aplicación no rellene determinados campos de la carga útil push y no funcione completamente como se espera.

## Paso 4: Añadir el framework de Push Stories a tu aplicación {#step-4-adding-the-push-story-framework-to-your-app}

{% tabs local %}
{% tab Swift Package Manager %}

Después de seguir la [guía de integración de Swift Package Manager]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/installation_methods/swift_package_manager), añade `AppboyPushStory` a tu `Notification Content Extension`:

![En Xcode, en frameworks y bibliotecas, selecciona el icono "+" para añadir un framework.]({% image_buster /assets/img/ios/push_story/spm1.png %})

![Después de seguir la guía de integración de Swift Package Manager, añade AppboyPushStory a tu Notification Content Extension.]({% image_buster /assets/img/ios/push_story/spm2.png %})

{% endtab %}
{% tab CocoaPods %}

Añade la siguiente línea a tu archivo de bibliotecas:

```ruby
target 'YourContentExtensionTarget' do
  pod 'Appboy-Push-Story'
end
```

Tras actualizar el archivo de bibliotecas, ve al directorio de tu proyecto de aplicación Xcode dentro de tu terminal y ejecuta `pod install`.

{% endtab %}
{% tab Manual %}

Descarga la última versión de `AppboyPushStory.zip` de la [página de versiones de GitHub](https://github.com/Appboy/appboy-ios-sdk/releases), extráela y añade los siguientes archivos a la `Notification Content Extension` de tu proyecto:
- `Resources/ABKPageView.nib`
- `AppboyPushStory.xcframework`

![Descarga la última versión de AppboyPushStory.zip de la página de versiones de GitHub, extráela y añade los siguientes archivos a la Notification Content Extension de tu proyecto.]({% image_buster /assets/img/ios/push_story/manual1.png %})

{% alert important %}
Asegúrate de que la opción **Do Not Embed** está seleccionada para **AppboyPushStory.xcframework** en la columna **Embed**.
{% endalert %}

Añade la bandera `-ObjC` a la `Notification Content Extension` de tu proyecto en **Build Settings > Other Linker Flags**.

{% endtab %}
{% endtabs %}

## Paso 5: Actualizar tu controlador de vista de notificación {#step-5-updating-your-notification-view-controller}

{% tabs %}
{% tab OBJECTIVE-C %}

En tu `NotificationViewController.h`, añade las siguientes líneas para añadir nuevas propiedades e importar los archivos de cabecera:

```objc
#import <AppboyPushStory/AppboyPushStory.h>
```

```objc
@property (nonatomic) IBOutlet ABKStoriesView *storiesView;
@property (nonatomic) ABKStoriesViewDataSource *dataSource;
```

En tu `NotificationViewController.m`, elimina la implementación predeterminada y añade el siguiente código:

```objc
@implementation NotificationViewController

- (void)didReceiveNotification:(UNNotification *)notification {
  self.dataSource = [[ABKStoriesViewDataSource alloc] initWithNotification:notification
                                                               storiesView:self.storiesView
                                                                  appGroup:@"YOUR-APP-GROUP-IDENTIFIER"];
}

- (void)didReceiveNotificationResponse:(UNNotificationResponse *)response
                     completionHandler:(void (^)(UNNotificationContentExtensionResponseOption option))completion {
  UNNotificationContentExtensionResponseOption option = [self.dataSource didReceiveNotificationResponse:response];
  completion(option);
}

- (void)viewWillDisappear:(BOOL)animated {
  [self.dataSource viewWillDisappear];
  [super viewWillDisappear:animated];
}

@end
```

{% endtab %}
{% tab swift %}

En tu `NotificationViewController.swift`, añade la siguiente línea para importar los archivos de cabecera:

```swift
import AppboyPushStory
```

A continuación, elimina la implementación predeterminada y añade el siguiente código:

```swift
class NotificationViewController: UIViewController, UNNotificationContentExtension {

  @IBOutlet weak var storiesView: ABKStoriesView!
  var dataSource: ABKStoriesViewDataSource?

  func didReceive(_ notification: UNNotification) {
    dataSource = ABKStoriesViewDataSource(notification: notification, storiesView: storiesView, appGroup: "YOUR-APP-GROUP-IDENTIFIER")
  }

  func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
    if dataSource != nil {
      let option: UNNotificationContentExtensionResponseOption = dataSource!.didReceive(response)
      completion(option)
    }
  }

  override func viewWillDisappear(_ animated: Bool) {
    dataSource?.viewWillDisappear()
    super.viewWillDisappear(animated)
  }
}
```

{% endtab %}
{% endtabs %}

## Paso 6: Configurar el storyboard de la extensión de contenido de notificación {#step-6-set-the-notification-content-extension-storyboard}

Abre el storyboard de `Notification Content Extension` y coloca un nuevo `UIView` en el controlador de la vista de notificación. Cambia el nombre de la clase a `ABKStoriesView`. Haz que la anchura y la altura de la vista se ajusten automáticamente al marco de la vista principal del controlador de la vista de notificación.

![Abre el storyboard de Notification Content Extension y coloca un nuevo UIView en el controlador de la vista de notificación. Cambia el nombre de la clase a ABKStoriesView. Haz que la anchura y la altura de la vista se ajusten automáticamente al marco de la vista principal del controlador de la vista de notificación.]({% image_buster /assets/img/ios/push_story/abkstoriesview_class.png %})

![Abre el storyboard de Notification Content Extension y coloca un nuevo UIView en el controlador de la vista de notificación. Cambia el nombre de la clase a ABKStoriesView. Haz que la anchura y la altura de la vista se ajusten automáticamente al marco de la vista principal del controlador de la vista de notificación.]({% image_buster /assets/img/ios/push_story/abkstoriesview_size.png %})

A continuación, enlaza el IBOutlet `storiesView` del controlador de la vista de notificación con el `ABKStoriesView` añadido.

![Captura de pantalla relacionada con el paso 6: configurar el storyboard de la extensión de contenido de notificación.]({% image_buster /assets/img/ios/push_story/abkstoriesview_outlet.png %})

## Paso 7: Configurar el plist de la extensión de contenido de notificación {#step-7-set-the-notification-content-extension-plist}

Abre el archivo `Info.plist` de `Notification Content Extension` y añade y cambia las siguientes claves en `NSExtension \ NSExtensionAttributes`:

`UNNotificationExtensionCategory` = `ab_cat_push_story_v2` (tipo `String`)
`UNNotificationExtensionDefaultContentHidden` = `YES` (tipo `Boolean`)
`UNNotificationExtensionInitialContentSizeRatio` = `0.65` (tipo `Number`)

![Captura de pantalla relacionada con el paso 7: configurar el plist de la extensión de contenido de notificación.]({% image_buster /assets/img/ios/push_story/notificationcontentextension_plist.png %})

## Paso 8: Actualizar la integración de Braze en tu aplicación principal {#step-8-updating-the-braze-integration-in-your-main-app}

### Opción 1: Tiempo de ejecución {#option-1-runtime}

En el diccionario `appboyOptions` utilizado para configurar tu instancia de Braze, añade una entrada `ABKPushStoryAppGroupKey` y establece el valor en el identificador de API de tu espacio de trabajo.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
NSMutableDictionary *appboyOptions = [NSMutableDictionary dictionary];
appboyOptions[ABKPushStoryAppGroupKey] = @"YOUR-APP-GROUP-IDENTIFIER";
[Appboy startWithApiKey:@"YOUR-API-KEY"
          inApplication:application
      withLaunchOptions:launchOptions
      withAppboyOptions:appboyOptions];
```

{% endtab %}
{% tab swift %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  ABKPushStoryAppGroupKey : "YOUR-APP-GROUP-IDENTIFIER"
]
Appboy.start(withApiKey: "YOUR-API-KEY", in:application, withLaunchOptions:launchOptions, withAppboyOptions:appboyOptions)
```

{% endtab %}
{% endtabs %}

#### Opción 2: Info.plist {#option-2-infoplist}

Alternativamente, para configurar el espacio de trabajo de Push Stories desde tu archivo `Info.plist`, añade un diccionario llamado `Braze` a tu archivo `Info.plist`. Dentro del diccionario `Braze`, añade una subentrada de tipo cadena `PushStoryAppGroup` y establece el valor en el identificador de tu espacio de trabajo. Ten en cuenta que, antes de la versión 4.0.2 del SDK de iOS de Braze, debe usarse la clave de diccionario `Appboy` en lugar de `Braze`.

## Próximos pasos {#next-steps}

A continuación, consulta los pasos para la integración de [botones de acción]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/customization/action_buttons), necesaria para que los botones se muestren en un mensaje de Push Stories.