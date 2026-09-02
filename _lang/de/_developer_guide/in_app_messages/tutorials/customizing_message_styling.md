---
nav_title: Nachrichtenstil anpassen
article_title: "Anleitung: Stil mit Schlüssel-Wert-Paaren anpassen"
description: ""
page_order: 1
layout: scrolly
---

# Anleitung: Nachrichtenstil mit Schlüssel-Wert-Paaren anpassen {#tutorial-customizing-message-styling-using-key-value-pairs}

> Folgen Sie dem Beispielcode in dieser Anleitung, um den Stil Ihrer In-App-Nachricht mithilfe von Schlüssel-Wert-Paaren im Braze SDK anzupassen.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} Es ist jedoch keine zusätzliche Einrichtung erforderlich.

## Nachrichtenstil mit Schlüssel-Wert-Paaren für Web anpassen {#customizing-message-styling-using-key-value-pairs-for-web}

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

### 1. Aufrufe von `automaticallyShowInAppMessages()` entfernen {#1-remove-calls-to-automaticallyshowinappmessages}

Entfernen Sie alle Aufrufe von [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages), da diese jede angepasste Logik überschreiben, die Sie später implementieren.

!!step
lines-index.js=6

#### 2. Debugging aktivieren (optional) {#2-enable-debugging-optional}

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!!step
lines-index.js=9-21

#### 3. Den Callback-Handler für In-App-Nachrichten abonnieren {#3-subscribe-to-the-in-app-message-callback-handler}

Registrieren Sie einen Callback mit [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage), um jedes Mal eine Nachricht zu erhalten, wenn eine In-App-Nachricht getriggert wird.

!!step
lines-index.js=10-13

#### 4. Auf die Eigenschaft `message.extras` zugreifen {#4-access-the-messageextras-property}

Verwenden Sie `message.extras`, um auf Anpassungstypen, Styling-Attribute oder andere im Dashboard definierte Werte zuzugreifen. Alle Werte werden als Strings zurückgegeben.

!!step
lines-index.js=19

#### 5. `showInAppMessage` bedingt aufrufen {#5-conditionally-call-showinappmessage}

Um die Nachricht anzuzeigen, rufen Sie [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage) auf. Andernfalls verwenden Sie die angepassten Eigenschaften nach Bedarf.

{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} Außerdem müssen Sie [In-App-Nachrichten für Android aktivieren]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=android#android_enabling-in-app-messages).

## Nachrichtenstil mit Schlüssel-Wert-Paaren für Android anpassen {#customizing-message-styling-using-key-value-pairs-for-android}

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

### 1. Debugging aktivieren (optional) {#1-enable-debugging-optional}

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!!step
lines-MainApplication.kt=28-30

#### 2. Activity-Lifecycle-Callbacks registrieren {#2-register-activity-lifecycle-callbacks}

Registrieren Sie den Standard-Listener von Braze, um den Lebenszyklus der In-App-Nachrichten zu verwalten.

!!step
lines-CustomInAppMessageViewFactory.kt=8

#### 3. Ihre angepasste View-Factory-Klasse erstellen {#3-create-your-custom-view-factory-class}

Stellen Sie sicher, dass Ihre Klasse [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) implementiert, damit sie angepasste Nachrichtenansichten erstellen und zurückgeben kann.

!!step
lines-CustomInAppMessageViewFactory.kt=15-20

#### 4. An die Standard-Factory von Braze delegieren {#4-delegate-to-brazes-default-factory}

Delegieren Sie an die Standard-Factory, um das in Braze integrierte Styling beizubehalten, bevor Sie Ihre eigenen bedingten Änderungen anwenden.

!!step
lines-CustomInAppMessageViewFactory.kt=30-32,35-41

#### 5. Auf Schlüssel-Wert-Paare über `inAppMessage.extras` zugreifen {#5-access-key-value-pairs-from-inappmessageextras}

Verwenden Sie `inAppMessage.extras`, um auf Anpassungstypen, Styling-Attribute oder andere im Dashboard definierte Werte zuzugreifen. Wenden Sie Styling-Überschreibungen an, bevor Sie die Ansicht zurückgeben.

!!step
lines-MainApplication.kt=33-34

#### 6. Eine angepasste `IInAppMessageViewFactory` implementieren {#6-implement-a-custom-iinappmessageviewfactory}

Implementieren Sie [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) in Ihrer angepassten Klasse, um In-App-Nachricht-Ansichten zu erstellen und darzustellen.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} Außerdem müssen Sie [In-App-Nachrichten für Swift aktivieren]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=swift#swift_enabling-in-app-messages).

## Nachrichtenstil mit Schlüssel-Wert-Paaren für Swift anpassen {#customizing-message-styling-using-key-value-pairs-for-swift}

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

### 1. `BrazeInAppMessageUIDelegate` implementieren {#1-implement-brazeinappmessageuidelegate}

Implementieren Sie in Ihrer `AppDelegate`-Klasse [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/delegate), damit Sie die Methode `inAppMessage` später überschreiben können.

!!step
lines-AppDelegate.swift=17

#### 2. Debugging aktivieren (optional)

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!!step
lines-AppDelegate.swift=30-50

#### 3. Nachrichten vor der Anzeige vorbereiten {#3-prepare-messages-before-theyre-displayed}

Braze ruft `inAppMessage(_:prepareWith:)` während der Nachrichtenvorbereitung auf. Verwenden Sie diese Methode, um den Stil anzupassen oder Logik auf Grundlage von Schlüssel-Wert-Paaren anzuwenden.

!!step
lines-AppDelegate.swift=34

#### 4. Auf Schlüssel-Wert-Paare über `message.extras` zugreifen {#4-access-key-value-pairs-from-messageextras}

Verwenden Sie `message.extras`, um auf Anpassungstypen, Styling-Attribute oder andere im Dashboard definierte Werte zuzugreifen.

!!step
lines-AppDelegate.swift=38-46

#### 5. Styling-Attribute der Nachricht aktualisieren {#5-update-the-messages-styling-attributes}

Verwenden Sie [`inAppMessage(_:prepareWith:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog), um auf den `PresentationContext` zuzugreifen und Styling-Attribute direkt zu ändern. Jeder In-App-Nachrichtentyp stellt unterschiedliche Attribute bereit.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}