---
nav_title: Personnaliser le style des messages
article_title: "Tutoriel : Personnalisation du style à l'aide de paires clé-valeur"
description: ""
page_order: 1
layout: scrolly
---

# Tutoriel : Personnalisation du style des messages à l'aide de paires clé-valeur {#tutorial-customizing-message-styling-using-key-value-pairs}

> Suivez l'exemple de code de ce tutoriel pour personnaliser le style de vos messages in-app à l'aide de paires clé-valeur dans le SDK de Braze.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} Cependant, aucune configuration supplémentaire n'est nécessaire.

## Personnalisation du style des messages à l'aide de paires clé-valeur pour le Web {#customizing-message-styling-using-key-value-pairs-for-web}

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

### 1. Supprimer les appels à `automaticallyShowInAppMessages()` {#1-remove-calls-to-automaticallyshowinappmessages}

Supprimez tous les appels à [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages), car ils remplaceront toute logique personnalisée que vous implémenterez ultérieurement.

!!step
lines-index.js=6

#### 2. Activer le débogage (facultatif) {#2-enable-debugging-optional}

Pour faciliter la résolution des problèmes lors du développement, pensez à activer le débogage.

!!step
lines-index.js=9-21

#### 3. S'abonner au gestionnaire de rappel des messages in-app {#3-subscribe-to-the-in-app-message-callback-handler}

Enregistrez un rappel avec [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) pour recevoir un message chaque fois qu'un message in-app est déclenché.

!!step
lines-index.js=10-13

#### 4. Accéder à la propriété `message.extras` {#4-access-the-messageextras-property}

Utilisez `message.extras` pour accéder aux types de personnalisation, aux attributs de style ou à toute autre valeur définie dans le tableau de bord. Toutes les valeurs sont renvoyées sous forme de chaînes de caractères.

!!step
lines-index.js=19

#### 5. Appeler conditionnellement `showInAppMessage` {#5-conditionally-call-showinappmessage}

Pour afficher le message, appelez [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage). Sinon, utilisez les propriétés personnalisées selon vos besoins.

{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} Vous devrez également [activer les messages in-app pour Android]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=android#android_enabling-in-app-messages).

## Personnalisation du style des messages à l'aide de paires clé-valeur pour Android {#customizing-message-styling-using-key-value-pairs-for-android}

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

### 1. Activer le débogage (facultatif) {#1-enable-debugging-optional}

Pour faciliter la résolution des problèmes lors du développement, pensez à activer le débogage.

!!step
lines-MainApplication.kt=28-30

#### 2. Enregistrer les rappels du cycle de vie des activités {#2-register-activity-lifecycle-callbacks}

Enregistrez l'écouteur par défaut de Braze pour gérer le cycle de vie des messages in-app.

!!step
lines-CustomInAppMessageViewFactory.kt=8

#### 3. Créer votre classe de fabrique de vues personnalisée {#3-create-your-custom-view-factory-class}

Assurez-vous que votre classe est conforme à [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) afin qu'elle puisse construire et renvoyer des vues de messages personnalisées.

!!step
lines-CustomInAppMessageViewFactory.kt=15-20

#### 4. Déléguer à la fabrique par défaut de Braze {#4-delegate-to-brazes-default-factory}

Déléguez à la fabrique par défaut pour conserver le style intégré de Braze avant d'appliquer vos propres modifications conditionnelles.

!!step
lines-CustomInAppMessageViewFactory.kt=30-32,35-41

#### 5. Accéder aux paires clé-valeur depuis `inAppMessage.extras` {#5-access-key-value-pairs-from-inappmessageextras}

Utilisez `inAppMessage.extras` pour accéder aux types de personnalisation, aux attributs de style ou à toute autre valeur définie dans le tableau de bord. Appliquez les surcharges de style avant de renvoyer la vue.

!!step
lines-MainApplication.kt=33-34

#### 6. Implémenter une `IInAppMessageViewFactory` personnalisée {#6-implement-a-custom-iinappmessageviewfactory}

Implémentez [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) dans votre classe personnalisée pour construire et afficher les vues de messages in-app.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} Vous devrez également [activer les messages in-app pour Swift]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=swift#swift_enabling-in-app-messages).

## Personnalisation du style des messages à l'aide de paires clé-valeur pour Swift {#customizing-message-styling-using-key-value-pairs-for-swift}

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

### 1. Implémenter `BrazeInAppMessageUIDelegate` {#1-implement-brazeinappmessageuidelegate}

Dans votre classe `AppDelegate`, implémentez [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/delegate) afin de pouvoir surcharger sa méthode `inAppMessage` ultérieurement.

!!step
lines-AppDelegate.swift=17

#### 2. Activer le débogage (facultatif)

Pour faciliter la résolution des problèmes lors du développement, pensez à activer le débogage.

!!step
lines-AppDelegate.swift=30-50

#### 3. Préparer les messages avant leur affichage {#3-prepare-messages-before-theyre-displayed}

Braze appelle `inAppMessage(_:prepareWith:)` pendant la préparation du message. Utilisez cette méthode pour personnaliser le style ou appliquer une logique basée sur des paires clé-valeur.

!!step
lines-AppDelegate.swift=34

#### 4. Accéder aux paires clé-valeur depuis `message.extras` {#4-access-key-value-pairs-from-messageextras}

Utilisez `message.extras` pour accéder aux types de personnalisation, aux attributs de style ou à toute autre valeur définie dans le tableau de bord.

!!step
lines-AppDelegate.swift=38-46

#### 5. Mettre à jour les attributs de style du message {#5-update-the-messages-styling-attributes}

Utilisez [`inAppMessage(_:prepareWith:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) pour accéder au `PresentationContext` et modifier directement les attributs de style. Chaque type de message in-app expose des attributs différents.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}