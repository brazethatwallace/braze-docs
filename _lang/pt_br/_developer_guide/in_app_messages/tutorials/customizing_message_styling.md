---
nav_title: Personalizar o estilo da mensagem
article_title: "Tutorial: Personalizando o estilo usando pares chave-valor"
description: ""
page_order: 1
layout: scrolly
---

# Tutorial: Personalizando o estilo da mensagem usando pares chave-valor {#tutorial-customizing-message-styling-using-key-value-pairs}

> Siga o código de exemplo neste tutorial para personalizar o estilo da sua mensagem no app usando pares chave-valor no SDK da Braze.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} No entanto, nenhuma configuração adicional é necessária.

## Personalizando o estilo da mensagem usando pares chave-valor para Web {#customizing-message-styling-using-key-value-pairs-for-web}

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

### 1. Remova chamadas para `automaticallyShowInAppMessages()` {#1-remove-calls-to-automaticallyshowinappmessages}

Remova qualquer chamada para [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages), pois elas substituirão qualquer lógica personalizada que você implemente depois.

!!step
lines-index.js=6

#### 2. Ative a depuração (opcional) {#2-enable-debugging-optional}

Para facilitar a solução de problemas durante o desenvolvimento, considere ativar a depuração.

!!step
lines-index.js=9-21

#### 3. Inscreva-se no manipulador de retorno de chamada da mensagem no app {#3-subscribe-to-the-in-app-message-callback-handler}

Registre um retorno de chamada com [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) para receber uma mensagem sempre que uma mensagem no app for acionada.

!!step
lines-index.js=10-13

#### 4. Acesse a propriedade `message.extras` {#4-access-the-messageextras-property}

Use `message.extras` para acessar tipos de personalização, atributos de estilo ou quaisquer outros valores definidos no dashboard. Todos os valores são retornados como strings.

!!step
lines-index.js=19

#### 5. Chame condicionalmente `showInAppMessage` {#5-conditionally-call-showinappmessage}

Para exibir a mensagem, chame [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage). Caso contrário, use quaisquer propriedades personalizadas conforme necessário.

{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} Você também precisará [ativar mensagens no app para Android]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=android#android_enabling-in-app-messages).

## Personalizando o estilo da mensagem usando pares chave-valor para Android {#customizing-message-styling-using-key-value-pairs-for-android}

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

### 1. Ative a depuração (opcional) {#1-enable-debugging-optional}

Para facilitar a solução de problemas durante o desenvolvimento, considere ativar a depuração.

!!step
lines-MainApplication.kt=28-30

#### 2. Registre retornos de chamada do ciclo de vida da atividade {#2-register-activity-lifecycle-callbacks}

Registre o listener padrão da Braze para gerenciar o ciclo de vida da mensagem no app.

!!step
lines-CustomInAppMessageViewFactory.kt=8

#### 3. Crie sua classe de fábrica de visualização personalizada {#3-create-your-custom-view-factory-class}

Certifique-se de que sua classe esteja em conformidade com [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) para que possa construir e retornar visualizações de mensagens personalizadas.

!!step
lines-CustomInAppMessageViewFactory.kt=15-20

#### 4. Delegue à fábrica padrão da Braze {#4-delegate-to-brazes-default-factory}

Delegue à fábrica padrão para manter o estilo nativo da Braze antes de aplicar suas próprias alterações condicionais.

!!step
lines-CustomInAppMessageViewFactory.kt=30-32,35-41

#### 5. Acesse pares chave-valor de `inAppMessage.extras` {#5-access-key-value-pairs-from-inappmessageextras}

Use `inAppMessage.extras` para acessar tipos de personalização, atributos de estilo ou quaisquer outros valores definidos no dashboard. Aplique substituições de estilo antes de retornar a visualização.

!!step
lines-MainApplication.kt=33-34

#### 6. Implemente um `IInAppMessageViewFactory` personalizado {#6-implement-a-custom-iinappmessageviewfactory}

Implemente [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) na sua classe personalizada para construir e renderizar visualizações de mensagens no app.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} Você também precisará [ativar mensagens no app para Swift]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=swift#swift_enabling-in-app-messages).

## Personalizando o estilo da mensagem usando pares chave-valor para Swift {#customizing-message-styling-using-key-value-pairs-for-swift}

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

### 1. Implemente `BrazeInAppMessageUIDelegate` {#1-implement-brazeinappmessageuidelegate}

Na sua classe `AppDelegate`, implemente [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/delegate) para que você possa sobrescrever o método `inAppMessage` mais tarde.

!!step
lines-AppDelegate.swift=17

#### 2. Ative a depuração (opcional)

Para facilitar a solução de problemas durante o desenvolvimento, considere ativar a depuração.

!!step
lines-AppDelegate.swift=30-50

#### 3. Prepare as mensagens antes que sejam exibidas {#3-prepare-messages-before-theyre-displayed}

A Braze chama `inAppMessage(_:prepareWith:)` durante a preparação da mensagem. Use isso para personalizar o estilo ou aplicar lógica com base em pares chave-valor.

!!step
lines-AppDelegate.swift=34

#### 4. Acesse pares chave-valor de `message.extras` {#4-access-key-value-pairs-from-messageextras}

Use `message.extras` para acessar tipos de personalização, atributos de estilo ou quaisquer outros valores definidos no dashboard.

!!step
lines-AppDelegate.swift=38-46

#### 5. Atualize os atributos de estilo da mensagem {#5-update-the-messages-styling-attributes}

Use [`inAppMessage(_:prepareWith:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) para acessar o `PresentationContext` e modificar os atributos de estilo diretamente. Cada tipo de mensagem no app expõe atributos diferentes.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}