---
nav_title: Aplazamiento de mensajes desencadenados
article_title: "Tutorial: Aplazamiento y restauración de mensajes desencadenados"
description: ""
page_order: 1
layout: scrolly
---

# Tutorial: Aplazamiento y restauración de mensajes desencadenados {#tutorial-deferring-and-restoring-triggered-messages}

> Sigue el código de ejemplo de este tutorial para aplazar y restaurar mensajes desencadenados dentro de la aplicación utilizando el SDK or kit de desarrollo de software de Braze.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} Sin embargo, no es necesario realizar ninguna configuración adicional.

## Aplazamiento y restauración de mensajes desencadenados para Web {#deferring-and-restoring-triggered-messages-for-web}

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Deferring Triggered Messages Web" %}

{% scrolly %}

```js file=index.js
import * as braze from "@braze/web-sdk";
// Remove any calls to `braze.automaticallyShowInAppMessages()`

braze.initialize("YOUR-API-KEY", {
  baseUrl: "YOUR-ENDPOINT",
  enableLogging: true,
});

braze.subscribeToInAppMessage(function (message) {
  const shouldDefer = true; // customize for your own logic
  if (shouldDefer) {
    braze.deferInAppMessage(message);
  } else {
    braze.showInAppMessage(message);
  }
});

// elsewhere in your app
document.getElementById("button").onclick = function () {
  const deferredMessage = braze.getDeferredInAppMessage();
  if (deferredMessage) {
    braze.showInAppMessage(deferredMessage);
  }
};
```

!!step
lines-index.js=2

### 1. Eliminar llamadas a `automaticallyShowInAppMessages()` {#1-remove-calls-to-automaticallyshowinappmessages}

Elimina cualquier llamada a [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages) , ya que anularán cualquier lógica personalizada que implementes más adelante.

!!step
lines-index.js=6

#### 2. Habilitar depuración (opcional) {#2-enable-debugging-optional}

Para facilitar la solución de problemas durante el desarrollo, considera habilitar la depuración.

!!step
lines-index.js=9-16

#### 3. Suscríbete al controlador de devolución de llamada de mensajes dentro de la aplicación {#3-subscribe-to-the-in-app-message-callback-handler}

Registra una devolución de llamada con [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) para recibir un mensaje cada vez que se desencadene un mensaje dentro de la aplicación.

!!step
lines-index.js=11-12

#### 4. Aplazar la instancia `message` {#4-defer-the-message-instance}

Para aplazar el mensaje, llama a [`deferInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#deferinappmessage). Braze serializará y guardará este mensaje para que puedas mostrarlo en una futura carga de la página.

!!step
lines-index.js=18-24

#### 5. Recuperar un mensaje aplazado anteriormente {#5-retrieve-a-previously-deferred-message}

Para recuperar cualquier mensaje aplazado anteriormente, llama a [`getDeferredInAppMessage()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getdeferredinappmessage).

!!step
lines-index.js=21-23

#### 6. Mostrar el mensaje aplazado {#6-display-the-deferred-message}

Después de recuperar un mensaje aplazado, muéstralo pasándolo a [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage).

!!step
lines-index.js=13-15

#### 7. Mostrar un mensaje inmediatamente {#7-display-a-message-immediately}

Para mostrar un mensaje en lugar de aplazarlo, llama a [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage) directamente en tu devolución de llamada `subscribeToInAppMessage`.
{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} También tendrás que [habilitar los mensajes dentro de la aplicación para Android]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=android#android_enabling-in-app-messages).

## Aplazamiento y restauración de mensajes desencadenados para Android {#deferring-and-restoring-triggered-messages-for-android}

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Deferring Triggered Messages Android" %}

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
    companion object {
        private var instance: MyApplication? = null
        fun getInstance(): MyApplication = instance!!
    }

    private var showMessage = false

    override fun onCreate() {
        super.onCreate()
        instance = this

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
                return if (showMessage) {
                    // Show the message using Braze's UI
                    InAppMessageOperation.DISPLAY_NOW
                } else {
                    // Re-enqueue the message for later
                    InAppMessageOperation.DISPLAY_LATER
                }
            }
        })
    }

    fun showDeferredMessage(show: Boolean) {
        showMessage = show
        BrazeInAppMessageManager.getInstance().requestDisplayInAppMessage()
    }
}
```

```kotlin file=MainActivity.kt
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material.Button
import androidx.compose.material.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            ContentView()
        }
    }
}

@Composable
fun ContentView() {
    Column(
        modifier = Modifier.padding(16.dp),
        verticalArrangement = Arrangement.spacedBy(20.dp)
    ) {
        // ... your UI

        Button(onClick = {
            MyApplication.getInstance().showDeferredMessage(true)
        }) {
            Text("Show Deferred IAM")
        }
    }
}
```

!!step
lines-MainApplication.kt=13-16

### 1. Crear una instancia singleton de `Application` {#1-create-a-singleton-application-instance}

Utiliza un objeto companion para exponer tu clase `Application` como un singleton, de modo que se pueda acceder a ella más adelante en tu código.

!!step
lines-MainApplication.kt=25

#### 2. Habilitar depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera habilitar la depuración.

!!step
lines-MainApplication.kt=34-36

#### 3. Registrar las devoluciones de llamada del ciclo de vida de la actividad {#3-register-activity-lifecycle-callbacks}

Registra el listener predeterminado de Braze para gestionar el ciclo de vida de los mensajes dentro de la aplicación.

!!step
lines-MainApplication.kt=39-49

#### 4. Configurar un listener de mensajes dentro de la aplicación {#4-set-up-an-in-app-message-listener}

Utiliza `BrazeInAppMessageManager` para configurar un listener personalizado que intercepte los mensajes antes de que se muestren.

!!step
lines-MainApplication.kt=43,46

#### 5. Crear lógica condicional {#5-create-conditional-logic}

Utiliza la bandera `showMessage` para controlar el momento&#8212;devuelve `DISPLAY_NOW` para mostrar el mensaje ahora o `DISPLAY_LATER` para aplazarlo.

!!step
lines-MainApplication.kt=52-55

#### 6. Crear un método para mostrar mensajes aplazados {#6-create-a-method-for-displaying-deferred-messages}

Utiliza `showDeferredMessage` para desencadenar el siguiente mensaje dentro de la aplicación. Cuando `showMessage` es `true`, el listener devolverá `DISPLAY_NOW`.

!!step
lines-MainActivity.kt=29

#### 7. Desencadenar el método desde tu interfaz de usuario {#7-trigger-the-method-from-your-ui}

Para mostrar el mensaje previamente aplazado, llama a `showDeferredMessage(true)` desde tu interfaz de usuario, por ejemplo, un botón o un toque.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} También tendrás que [habilitar los mensajes dentro de la aplicación para Swift]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=swift#swift_enabling-in-app-messages).

## Aplazamiento y restauración de mensajes desencadenados para Swift {#deferring-and-restoring-triggered-messages-for-swift}

{% multi_lang_include developer_guide/_shared/tutorial_feedback.md tutorial="Deferring Triggered Messages Swift" %}

{% scrolly %}

```swift file=AppDelegate.swift
import SwiftUI
import BrazeKit
import BrazeUI

class AppDelegate: UIResponder, UIApplicationDelegate, BrazeInAppMessageUIDelegate {
    static private(set) var shared: AppDelegate!

    private var braze: Braze!
    public var showMessage: Bool = false

    func application(
      _ application: UIApplication,
      didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
    ) -> Bool {
        AppDelegate.shared = self

        // 1. Braze configuration with your SDK API key and endpoint
        let configuration = Braze.Configuration(apiKey: "a1fc095b-ae3d-40f4-bb33-3fb5176562c0", endpoint: "sondheim.braze.com")
        configuration.logger.level = .debug

        // 2. Initialize Braze SDK instance
        braze = Braze(configuration: configuration)

        // 3. Set up Braze In-App Message UI and delegate
        let ui = BrazeInAppMessageUI()
        ui.delegate = self
        braze.inAppMessagePresenter = ui

        return true
    }

    func inAppMessage(
      _ ui: BrazeInAppMessageUI,
      displayChoiceForMessage message: Braze.InAppMessage
    ) -> BrazeInAppMessageUI.DisplayChoice {
        if !showMessage {
            return .reenqueue
        }

        return .now
    }

    func showDeferredMessage(showMessage: Bool) {
        self.showMessage = showMessage
        (braze.inAppMessagePresenter as? BrazeInAppMessageUI)?.presentNext()
    }
}
```

```swift file=SampleApp.swift
import SwiftUI

@main
struct IAMDeferApp: App {
    @UIApplicationDelegateAdaptor(AppDelegate.self) var delegate

    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
```

```swift file=ContentView.swift
import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack(spacing: 20) {
            // ...your UI

            Button("Show Deferred IAM") {
                AppDelegate.shared.showDeferredMessage(showMessage: true)
            }
        }
        .padding()
    }
}
```

!!step
lines-AppDelegate.swift=5

### 1. Implementar el `BrazeInAppMessageUIDelegate` {#1-implement-the-brazeinappmessageuidelegate}

En tu clase `AppDelegate`, implementa el [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) para que puedas sobrescribir su método `inAppMessage` más adelante.

!!step
lines-AppDelegate.swift=19

#### 2. Habilitar depuración (opcional)

Para facilitar la solución de problemas durante el desarrollo, considera habilitar la depuración.

!!step
lines-AppDelegate.swift=25-27

#### 3. Configurar tu interfaz de usuario de Braze y el delegado {#3-set-up-your-braze-ui-and-delegate}

`BrazeInAppMessageUI()` muestra mensajes dentro de la aplicación de forma predeterminada. Al asignar `self` como su delegado, puedes interceptar y gestionar los mensajes antes de que se muestren. Asegúrate de guardar la instancia, ya que la necesitarás más adelante para restaurar los mensajes aplazados.

!!step
lines-AppDelegate.swift=32-41

#### 4. Sobrescribir `DisplayChoice` con lógica condicional {#4-override-displaychoice-with-conditional-logic}

Sobrescribe [`inAppMessage(_:displayChoiceForMessage:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) para determinar cuándo se debe mostrar un mensaje. Devuelve `.now` para mostrarlo inmediatamente o `.reenqueue` para aplazarlo.

!!step
lines-AppDelegate.swift=43-46

#### 5. Crear un método para mostrar mensajes aplazados {#5-create-a-method-to-show-deferred-messages}

Crea un método que llame a `showDeferredMessage(true)` para mostrar el siguiente mensaje aplazado de la pila. Cuando se llama, `showMessage` se establece en `true`, lo que hace que el delegado devuelva `.now`.

!!step
lines-ContentView.swift=1-14

#### 6. Desencadenar el método desde tu interfaz de usuario {#5-trigger-the-method-from-your-ui}

Para mostrar el mensaje previamente aplazado, llama a `showDeferredMessage(true)` desde tu interfaz de usuario, por ejemplo, un botón o un toque.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}