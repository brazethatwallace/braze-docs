---
nav_title: Affichage conditionnel des messages
article_title: "Tutoriel : Affichage conditionnel des messages in-app"
description: ""
page_order: 1
layout: scrolly
---

# Tutoriel : Affichage conditionnel des messages in-app {#tutorial-conditionally-displaying-in-app-messages}

> Suivez l'exemple de code de ce tutoriel pour afficher de manière conditionnelle des messages in-app à l'aide du SDK Braze.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} Cependant, aucune configuration supplémentaire n'est nécessaire.

## Affichage conditionnel des messages in-app pour le web {#conditionally-displaying-in-app-messages-for-web}

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

### 1. Supprimer les appels à `automaticallyShowInAppMessages()` {#1-remove-calls-to-automaticallyshowinappmessages}

Supprimez tous les appels à [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages), car ils remplaceront toute logique personnalisée que vous implémenterez ultérieurement.

!!step
lines-index.js=6

#### 2. Activer le débogage (facultatif) {#2-enable-debugging-optional}

Pour faciliter la résolution des problèmes lors du développement, pensez à activer le débogage.

!!step
lines-index.js=9-18

#### 3. S'abonner aux mises à jour des messages in-app {#3-subscribe-to-in-app-message-updates}

Enregistrez un rappel avec [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) pour recevoir un `message` chaque fois qu'un message in-app est déclenché.

!!step
lines-index.js=10-13

#### 4. Créer une logique conditionnelle {#4-create-conditional-logic}

Créez une logique personnalisée pour contrôler l'affichage des messages. Dans cet exemple, la logique vérifie si l'URL contient `"checkout"` ou si un élément `#checkout` existe sur la page.

!!step
lines-index.js=16

#### 5. Afficher les messages avec `showInAppMessage` {#5-display-messages-with-showinappmessage}

Pour afficher le message, appelez [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage). En cas d'omission, le message sera ignoré.

{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} Vous devrez également [activer les messages in-app pour Android]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=android#android_enabling-in-app-messages).

## Affichage conditionnel des messages in-app pour Android {#conditionally-displaying-in-app-messages-for-android}

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

### 1. Activer le débogage (facultatif) {#1-enable-debugging-optional}

Pour faciliter la résolution des problèmes lors du développement, pensez à activer le débogage.

!!step
lines-MainApplication.kt=26-28

#### 2. Enregistrer les rappels du cycle de vie des activités {#2-register-activity-lifecycle-callbacks}

Enregistrez le listener par défaut de Braze pour gérer le cycle de vie des messages in-app.

!!step
lines-MainApplication.kt=30-44

#### 3. Configurer un listener de messages in-app {#3-set-up-an-in-app-message-listener}

Utilisez `BrazeInAppMessageManager` pour définir un listener personnalisé qui intercepte les messages avant qu'ils ne soient affichés.

!!step
lines-MainApplication.kt=34-42

#### 4. Créer une logique conditionnelle

Utilisez une logique personnalisée pour contrôler le moment d'affichage des messages. Dans cet exemple, la logique vérifie si l'extra `should_display_message` est défini sur `"true"`.

!!step
lines-MainApplication.kt=38,41

#### 5. Renvoyer ou rejeter le message {#5-return-or-discard-the-message}

Renvoyez un `InAppMessageOperation` avec `DISPLAY_NOW` pour afficher le message, ou avec `DISCARD` pour le supprimer.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} Vous devrez également [activer les messages in-app pour Swift]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=swift#swift_enabling-in-app-messages).

## Affichage conditionnel des messages in-app pour Swift {#conditionally-displaying-in-app-messages-for-swift}

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

### 1. Implémenter le `BrazeInAppMessageUIDelegate` {#1-implement-the-brazeinappmessageuidelegate}

Dans votre classe AppDelegate, implémentez le protocole [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/delegate) afin de pouvoir redéfinir sa méthode `inAppMessage` ultérieurement.

!!step
lines-AppDelegate.swift=12

#### 2. Activer le débogage (facultatif)

Pour faciliter la résolution des problèmes lors du développement, pensez à activer le débogage.

!!step
lines-AppDelegate.swift=19-21

#### 3. Configurer l'interface utilisateur Braze et le délégué {#3-set-up-your-braze-ui-and-delegate}

`BrazeInAppMessageUI()` affiche les messages in-app par défaut. En attribuant `self` comme délégué, vous pouvez intercepter et traiter les messages avant qu'ils ne soient affichés.

!!step
lines-AppDelegate.swift=26-33

#### 4. Redéfinir `DisplayChoice` avec une logique conditionnelle {#4-override-displaychoice-with-conditional-logic}

Redéfinissez [`inAppMessage(_:displayChoiceForMessage:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) pour décider si un message doit être affiché. Renvoyez `.now` pour afficher le message ou `.discard` pour le supprimer.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}