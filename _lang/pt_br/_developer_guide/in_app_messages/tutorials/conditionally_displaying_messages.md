---
nav_title: Exibindo mensagens condicionalmente
article_title: "Tutorial: Exibindo mensagens no app condicionalmente"
description: ""
page_order: 1
layout: scrolly
---

# Tutorial: Exibindo mensagens no app condicionalmente {#tutorial-conditionally-displaying-in-app-messages}

> Siga o exemplo de código neste tutorial para exibir mensagens no app condicionalmente usando o SDK or kit de desenvolvimento de software da Braze.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} No entanto, nenhuma configuração adicional é necessária.

## Exibindo mensagens no app condicionalmente para Web {#conditionally-displaying-in-app-messages-for-web}

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

### 1. Remova chamadas para `automaticallyShowInAppMessages()` {#1-remove-calls-to-automaticallyshowinappmessages}

Remova qualquer chamada para [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages), pois elas substituirão qualquer lógica personalizada que você implemente depois.

!!step
lines-index.js=6

#### 2. Ative a depuração (opcional) {#2-enable-debugging-optional}

Para facilitar a solução de problemas durante o desenvolvimento, considere ativar a depuração.

!!step
lines-index.js=9-18

#### 3. Inscreva-se para atualizações de mensagens no app {#3-subscribe-to-in-app-message-updates}

Registre um retorno de chamada com [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) para receber uma `message` sempre que uma mensagem no app for acionada.

!!step
lines-index.js=10-13

#### 4. Crie a lógica condicional {#4-create-conditional-logic}

Crie uma lógica personalizada para controlar quando as mensagens são exibidas. Neste exemplo, a lógica verifica se a URL contém `"checkout"` ou se um elemento `#checkout` existe na página.

!!step
lines-index.js=16

#### 5. Exiba mensagens com `showInAppMessage` {#5-display-messages-with-showinappmessage}

Para exibir a mensagem, chame [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage). Se omitido, a mensagem será ignorada.

{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} Você também precisará [ativar mensagens no app para Android]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=android#android_enabling-in-app-messages).

## Exibindo mensagens no app condicionalmente para Android {#conditionally-displaying-in-app-messages-for-android}

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

### 1. Ative a depuração (opcional) {#1-enable-debugging-optional}

Para facilitar a solução de problemas durante o desenvolvimento, considere ativar a depuração.

!!step
lines-MainApplication.kt=26-28

#### 2. Registre retornos de chamada do ciclo de vida da atividade {#2-register-activity-lifecycle-callbacks}

Registre o listener padrão da Braze para gerenciar o ciclo de vida da mensagem no app.

!!step
lines-MainApplication.kt=30-44

#### 3. Configure um listener de mensagem no app {#3-set-up-an-in-app-message-listener}

Use `BrazeInAppMessageManager` para definir um listener personalizado que intercepta mensagens antes de serem exibidas.

!!step
lines-MainApplication.kt=34-42

#### 4. Crie a lógica condicional

Use lógica personalizada para controlar o momento de exibição da mensagem. Neste exemplo, a lógica personalizada verifica se o extra `should_display_message` está definido como `"true"`.

!!step
lines-MainApplication.kt=38,41

#### 5. Retorne ou descarte a mensagem {#5-return-or-discard-the-message}

Retorne um `InAppMessageOperation` com `DISPLAY_NOW` para exibir a mensagem, ou com `DISCARD` para suprimi-la.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} Você também precisará [ativar mensagens no app para Swift]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=swift#swift_enabling-in-app-messages).

## Exibindo mensagens no app condicionalmente para Swift {#conditionally-displaying-in-app-messages-for-swift}

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

### 1. Implemente o `BrazeInAppMessageUIDelegate` {#1-implement-the-brazeinappmessageuidelegate}

Na sua classe AppDelegate, implemente o [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/delegate) para que você possa sobrescrever o método `inAppMessage` mais tarde.

!!step
lines-AppDelegate.swift=12

#### 2. Ative a depuração (opcional)

Para facilitar a solução de problemas durante o desenvolvimento, considere ativar a depuração.

!!step
lines-AppDelegate.swift=19-21

#### 3. Configure a interface da Braze e o delegate {#3-set-up-your-braze-ui-and-delegate}

`BrazeInAppMessageUI()` renderiza mensagens no app por padrão. Ao atribuir `self` como delegate, você pode interceptar e manipular mensagens antes que sejam exibidas.

!!step
lines-AppDelegate.swift=26-33

#### 4. Sobrescreva `DisplayChoice` com lógica condicional {#4-override-displaychoice-with-conditional-logic}

Sobrescreva [`inAppMessage(_:displayChoiceForMessage:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) para decidir se uma mensagem deve ser exibida. Retorne `.now` para exibir a mensagem ou `.discard` para suprimi-la.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}