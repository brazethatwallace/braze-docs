---
nav_title: Mostrar mensajes de forma condicional
article_title: "Tutorial: Mostrar mensajes dentro de la aplicación de forma condicional"
description: ""
page_order: 1
layout: scrolly
---

# Tutorial: Mostrar mensajes dentro de la aplicación de forma condicional {#tutorial-conditionally-displaying-in-app-messages}

> Sigue el código de ejemplo de este tutorial para mostrar mensajes dentro de la aplicación de forma condicional utilizando el SDK de Braze.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} Sin embargo, no es necesario realizar ninguna configuración adicional.

## Visualización condicional de mensajes dentro de la aplicación para Web {#conditionally-displaying-in-app-messages-for-web}

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Conditionally Displaying Messages Web" %}

{% scrolly %}

```js file=index.js
import * as braze from "@braze/web-sdk";
// Remove any calls to `braze.automaticallyShowInAppMessages()`

braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
  enableLogging: true,
});

braze.subscribeToInAppMessage(function (message) {
  if (
    location.pathname === "/checkout" ||
    document.getElementById("#checkout")
  ) {
    // do not show the message
  } else {
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
lines-index.js=9-18

#### 3. Suscribirse a las actualizaciones de mensajes dentro de la aplicación {#3-subscribe-to-in-app-message-updates}

Registra una devolución de llamada con [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) para recibir un `message` cada vez que se desencadene un mensaje dentro de la aplicación.

!!step
lines-index.js=10-13

#### 4. Crear lógica condicional {#4-create-conditional-logic}

Crea una lógica personalizada para controlar cuándo se muestran los mensajes. En este ejemplo, la lógica comprueba si la URL contiene `"checkout"` o si existe un elemento `#checkout` en la página.

!!step
lines-index.js=16

#### 5. Mostrar mensajes con `showInAppMessage` {#5-display-messages-with-showinappmessage}

Para mostrar el mensaje, llama a [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage). Si se omite, el mensaje se descartará.

{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} También tendrás que [habilitar los mensajes dentro de la aplicación para Android]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=android#android_enabling-in-app-messages).

## Visualización condicional de mensajes dentro de la aplicación para Android {#conditionally-displaying-in-app-messages-for-android}

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Conditionally Displaying Messages Android" %}

{% scrolly %}

```kotlin file=MainApplication.kt
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

        // Set up in-app message listener
        BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(object : IInAppMessageManagerListener {
            override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
                // Check if we should show the message
                val shouldShow = inAppMessage.extras["should_display_message"] == "true"

                return if (shouldShow) {
                    // Show the message using Braze's UI
                    InAppMessageOperation.DISPLAY_NOW
                } else {
                    // Discard the message (or we could also create our own UI using KVP values)
                    InAppMessageOperation.DISCARD
                }
            }
        })
    }
}
```

!!step
lines-MainApplication.kt=17

### 1. Habilitar depuración (opcional) {#1-enable-debugging-optional}

Para facilitar la solución de problemas durante el desarrollo, considera habilitar la depuración.

!!step
lines-MainApplication.kt=26-28

#### 2. Registrar las devoluciones de llamada del ciclo de vida de la actividad {#2-register-activity-lifecycle-callbacks}

Registra el listener predeterminado de Braze para gestionar el ciclo de vida de los mensajes dentro de la aplicación.

!!step
lines-MainApplication.kt=30-44

#### 3. Configurar un listener de mensajes dentro de la aplicación {#3-set-up-an-in-app-message-listener}

Utiliza `BrazeInAppMessageManager` para configurar un listener personalizado que intercepte los mensajes antes de que se muestren.

!!step
lines-MainApplication.kt=34-42

#### 4. Crear lógica condicional

Utiliza lógica personalizada para controlar el momento en que se muestran los mensajes. En este ejemplo, la lógica personalizada comprueba si el extra `should_display_message` está establecido en `"true"`.

!!step
lines-MainApplication.kt=38,41

#### 5. Devolver o descartar el mensaje {#5-return-or-discard-the-message}

Devuelve un `InAppMessageOperation` con `DISPLAY_NOW` para mostrar el mensaje, o con `DISCARD` para suprimirlo.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} También tendrás que [habilitar los mensajes dentro de la aplicación para Swift]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=swift#swift_enabling-in-app-messages).

## Visualización condicional de mensajes dentro de la aplicación para Swift {#conditionally-displaying-in-app-messages-for-swift}

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Conditionally Displaying Messages Swift" %}

{% scrolly %}

```swift file=AppDelegate.swift
import SwiftUI
import BrazeKit
import BrazeUI

class AppDelegate: NSObject, UIApplicationDelegate, BrazeInAppMessageUIDelegate {
    static var braze: Braze?

    func application(_ application: UIApplication,
                     didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]? = nil) -> Bool {
        // 1. Braze configuration with your SDK API key and endpoint
        let configuration = Braze.Configuration(apiKey: "YOUR_API_ENDPOINT", endpoint: "YOUR_API_KEY")
        configuration.logger.level = .debug

        // 2. Initialize Braze SDK instance
        let brazeInstance = Braze(configuration: configuration)
        AppDelegate.braze = brazeInstance

        // 3. Set up Braze In-App Message UI and delegate
        let inAppMessageUI = BrazeInAppMessageUI()
        inAppMessageUI.delegate = self
        brazeInstance.inAppMessagePresenter = inAppMessageUI

        return true
    }

    func inAppMessage(_ ui: BrazeInAppMessageUI,
                      displayChoiceForMessage message: Braze.InAppMessage) -> BrazeInAppMessageUI.DisplayChoice {
        if let showFlag = message.extras["should_display_message"] as? String, showFlag == "true" {
            return .now
        } else {
            return .discard
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

### 1. Implementar el `BrazeInAppMessageUIDelegate` {#1-implement-the-brazeinappmessageuidelegate}

En tu clase AppDelegate, implementa [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/delegate) para poder sobrescribir su método `inAppMessage` más adelante.

!!step
lines-AppDelegate.swift=12

#### 2. Habilitar depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera habilitar la depuración.

!!step
lines-AppDelegate.swift=19-21

#### 3. Configurar la interfaz de usuario de Braze y el delegado {#3-set-up-your-braze-ui-and-delegate}

`BrazeInAppMessageUI()` muestra mensajes dentro de la aplicación de forma predeterminada. Al asignar `self` como delegado, puedes interceptar y gestionar los mensajes antes de que se muestren.

!!step
lines-AppDelegate.swift=26-33

#### 4. Sobrescribir `DisplayChoice` con lógica condicional {#4-override-displaychoice-with-conditional-logic}

Sobrescribe [`inAppMessage(_:displayChoiceForMessage:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) para decidir si se debe mostrar un mensaje. Devuelve `.now` para mostrar el mensaje o `.discard` para suprimirlo.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}