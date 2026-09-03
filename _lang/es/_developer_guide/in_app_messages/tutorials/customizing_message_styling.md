---
nav_title: Personalizar el estilo de los mensajes
article_title: "Tutorial: Personalización del estilo mediante pares clave-valor"
description: ""
page_order: 1
layout: scrolly
---

# Tutorial: Personalización del estilo de los mensajes mediante pares clave-valor {#tutorial-customizing-message-styling-using-key-value-pairs}

> Sigue el código de ejemplo de este tutorial para personalizar el estilo de los mensajes dentro de la aplicación utilizando pares clave-valor en el SDK de Braze.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} Sin embargo, no es necesario realizar ninguna configuración adicional.

## Personalización del estilo de los mensajes mediante pares clave-valor para Web {#customizing-message-styling-using-key-value-pairs-for-web}

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Customizing Message Styling Web" %}

{% scrolly %}

```js file=index.js
import * as braze from "@braze/web-sdk";
// Remove any calls to `braze.automaticallyShowInAppMessages()`

braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
  enableLogging: true,
});

braze.subscribeToInAppMessage(function (message) {
  const extras = message.extras;
  const customTemplateType = extras["custom-template"] || "";
  const customColor = extras["custom-color"] || "";
  const customMessageId = extras["message-id"] || "";

  if (customTemplateType) {
    // add your own custom code to render this message
  } else {
    // otherwise, use Braze built-in UI
    braze.showInAppMessage(message);
  }
});
```

!!step
lines-index.js=2

### 1. Eliminar llamadas a `automaticallyShowInAppMessages()` {#1-remove-calls-to-automaticallyshowinappmessages}

Elimina cualquier llamada a [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages), ya que anularán cualquier lógica personalizada que implementes más adelante.

!!step
lines-index.js=6

#### 2. Habilitar depuración (opcional) {#2-enable-debugging-optional}

Para facilitar la solución de problemas durante el desarrollo, considera habilitar la depuración.

!!step
lines-index.js=9-21

#### 3. Suscríbete al controlador de devolución de llamada de mensajes dentro de la aplicación {#3-subscribe-to-the-in-app-message-callback-handler}

Registra una devolución de llamada con [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) para recibir un mensaje cada vez que se desencadene un mensaje dentro de la aplicación.

!!step
lines-index.js=10-13

#### 4. Acceder a la propiedad `message.extras` {#4-access-the-messageextras-property}

Utiliza `message.extras` para acceder a los tipos de personalización, los atributos de estilo o cualquier otro valor definido en el dashboard. Todos los valores se devuelven como cadenas.

!!step
lines-index.js=19

#### 5. Llamada condicional a `showInAppMessage` {#5-conditionally-call-showinappmessage}

Para mostrar el mensaje, llama a [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage). De lo contrario, utiliza las propiedades personalizadas según sea necesario.

{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} También tendrás que [habilitar los mensajes dentro de la aplicación para Android]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=android#android_enabling-in-app-messages).

## Personalización del estilo de los mensajes mediante pares clave-valor para Android {#customizing-message-styling-using-key-value-pairs-for-android}

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Customizing Message Styling Android" %}

{% scrolly %}

```kotlin file=MainApplication.kt
package com.example.brazedevlab

import android.app.Application
import com.braze.Braze
import com.braze.support.BrazeLogger
import com.braze.configuration.BrazeConfig
import com.braze.ui.inappmessage.BrazeInAppMessageManager
import com.braze.BrazeActivityLifecycleCallbackListener
import com.braze.ui.inappmessage.listeners.IInAppMessageManagerListener
import com.braze.models.inappmessage.IInAppMessage
import com.braze.ui.inappmessage.InAppMessageOperation
import android.util.Log

class MyApplication : Application() {
    override fun onCreate() {
        super.onCreate()

        // Enable verbose Braze SDK logs
        BrazeLogger.logLevel = Log.VERBOSE

        // Initialize Braze
        val brazeConfig = BrazeConfig.Builder()
            .setApiKey("YOUR-API-KEY")
            .setCustomEndpoint("YOUR-ENDPOINT")
            .build()
        Braze.configure(this, brazeConfig)

        registerActivityLifecycleCallbacks(
            BrazeActivityLifecycleCallbackListener()
        )

        // Set up custom in-app message view factory
        BrazeInAppMessageManager.getInstance()
        .setCustomInAppMessageViewFactory(CustomInAppMessageViewFactory())
    }
}
```

```kotlin file=CustomInAppMessageViewFactory.kt
import android.app.Activity
import android.graphics.Color
import android.view.View
import com.braze.models.inappmessage.IInAppMessage
import com.braze.ui.inappmessage.BrazeInAppMessageManager
import com.braze.ui.inappmessage.IInAppMessageViewFactory

class CustomInAppMessageViewFactory : IInAppMessageViewFactory {

    override fun createInAppMessageView(
        activity: Activity,
        inAppMessage: IInAppMessage
    ): View {
        // 1) Obtain Braze’s default view factory for this message type
        val defaultFactory =
            BrazeInAppMessageManager.getInstance()
                .getDefaultInAppMessageViewFactory(inAppMessage)
                ?: throw IllegalStateException(
                    "Braze default IAM view factory is missing"
                )

        // 2) Inflate the default view
        val iamView = defaultFactory
            .createInAppMessageView(activity, inAppMessage)
            ?: throw IllegalStateException(
                "Braze default IAM view is null"
            )

        // 3) Get your KVP extras
        val extras = inAppMessage.extras ?: emptyMap()
        val customization = extras["customization"]
        val overrideColor = extras["custom-color"]

        // 4) Style your root view
        if (customization == "slideup-attributes" && overrideColor != null) {
            try {
                iamView.setBackgroundColor(Color.parseColor(overrideColor))
            } catch (_: IllegalArgumentException) {
                // ignore bad styling
            }
        }

        return iamView
    }
}
```

!!step
lines-MainApplication.kt=19

### 1. Habilitar depuración (opcional) {#1-enable-debugging-optional}

Para facilitar la solución de problemas durante el desarrollo, considera habilitar la depuración.

!!step
lines-MainApplication.kt=28-30

#### 2. Registrar las devoluciones de llamada del ciclo de vida de la actividad {#2-register-activity-lifecycle-callbacks}

Registra el listener predeterminado de Braze para gestionar el ciclo de vida de los mensajes dentro de la aplicación.

!!step
lines-CustomInAppMessageViewFactory.kt=8

#### 3. Crear tu clase de fábrica de vistas personalizada {#3-create-your-custom-view-factory-class}

Asegúrate de que tu clase cumpla con [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) para que pueda construir y devolver vistas de mensajes personalizadas.

!!step
lines-CustomInAppMessageViewFactory.kt=15-20

#### 4. Delegar a la fábrica predeterminada de Braze {#4-delegate-to-brazes-default-factory}

Delega en la fábrica predeterminada para conservar el estilo integrado de Braze antes de aplicar tus propios cambios condicionales.

!!step
lines-CustomInAppMessageViewFactory.kt=30-32,35-41

#### 5. Acceder a los pares clave-valor desde `inAppMessage.extras` {#5-access-key-value-pairs-from-inappmessageextras}

Utiliza `inAppMessage.extras` para acceder a los tipos de personalización, los atributos de estilo o cualquier otro valor definido en el dashboard. Aplica las modificaciones de estilo antes de devolver la vista.

!!step
lines-MainApplication.kt=33-34

#### 6. Implementar un `IInAppMessageViewFactory` personalizado {#6-implement-a-custom-iinappmessageviewfactory}

Implementa [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) en tu clase personalizada para construir y renderizar vistas de mensajes dentro de la aplicación.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} También tendrás que [habilitar los mensajes dentro de la aplicación para Swift]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=swift#swift_enabling-in-app-messages).

## Personalización del estilo de los mensajes mediante pares clave-valor para Swift {#customizing-message-styling-using-key-value-pairs-for-swift}

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Customizing Message Styling Swift" %}

{% scrolly %}

```swift file=AppDelegate.swift
import UIKit
import BrazeKit
import BrazeUI

class AppDelegate: UIResponder, UIApplicationDelegate, BrazeInAppMessageUIDelegate {
  var window: UIWindow?
  static var braze: Braze?

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let configuration = Braze.Configuration(
      apiKey: "YOUR-API-KEY",
      endpoint: "YOUR-ENDPOINT"
    )
    configuration.logger.level = .debug

    let braze = Braze(configuration: configuration)
    AppDelegate.braze = braze

    // Set up Braze In-App Message UI and delegate
    let inAppMessageUI = BrazeInAppMessageUI()
    inAppMessageUI.delegate = self
    brazeInstance.inAppMessagePresenter = inAppMessageUI

    return true
  }

    func inAppMessage(
      _ ui: BrazeInAppMessageUI,
      prepareWith context: inout BrazeInAppMessageUI.PresentationContext
    ) {
      let customization = context.message.extras["customization"] as? String

      if customization == "slideup-attributes" {
        // Create a new attributes object and make customizations.
        var attributes = context.attributes?.slideup
        attributes?.font = UIFont(name: "Chalkduster", size: 17)!
        attributes?.imageSize = CGSize(width: 65, height: 65)
        attributes?.cornerRadius = 20
        attributes?.imageCornerRadius = 10
        if #available(iOS 13.0, *) {
          attributes?.cornerCurve = .continuous
          attributes?.imageCornerCurve = .continuous
        }

        context.attributes?.slideup = attributes
      }
    }
}
```

```swift file=SampleApp.swift
import SwiftUI

@main
struct SampleApp: App {
  @UIApplicationDelegateAdaptor(AppDelegate.self) var appDelegate

  var body: some Scene {
    WindowGroup {
      YourView()
    }
  }
}
```

!!step
lines-AppDelegate.swift=5

### 1. Implementar `BrazeInAppMessageUIDelegate` {#1-implement-brazeinappmessageuidelegate}

En tu clase `AppDelegate`, implementa [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/delegate) para que puedas sobrescribir su método `inAppMessage` más adelante.

!!step
lines-AppDelegate.swift=17

#### 2. Habilitar depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera habilitar la depuración.

!!step
lines-AppDelegate.swift=30-50

#### 3. Preparar los mensajes antes de que se muestren {#3-prepare-messages-before-theyre-displayed}

Braze llama a `inAppMessage(_:prepareWith:)` durante la preparación del mensaje. Úsalo para personalizar el estilo o aplicar lógica basada en pares clave-valor.

!!step
lines-AppDelegate.swift=34

#### 4. Acceder a los pares clave-valor desde `message.extras` {#4-access-key-value-pairs-from-messageextras}

Utiliza `message.extras` para acceder a los tipos de personalización, los atributos de estilo o cualquier otro valor definido en el dashboard.

!!step
lines-AppDelegate.swift=38-46

#### 5. Actualizar los atributos de estilo del mensaje {#5-update-the-messages-styling-attributes}

Utiliza [`inAppMessage(_:prepareWith:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) para acceder al `PresentationContext` y poder modificar directamente los atributos de estilo. Cada tipo de mensaje dentro de la aplicación expone atributos diferentes.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}