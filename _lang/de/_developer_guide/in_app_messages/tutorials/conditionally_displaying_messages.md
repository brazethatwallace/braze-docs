---
nav_title: Bedingte Anzeige von Nachrichten
article_title: "Anleitung: Bedingte Anzeige von In-App-Nachrichten"
description: ""
page_order: 1
layout: scrolly
---

# Anleitung: Bedingte Anzeige von In-App-Nachrichten {#tutorial-conditionally-displaying-in-app-messages}

> Folgen Sie dem Beispielcode in dieser Anleitung, um In-App-Nachrichten mit dem Braze SDK bedingt anzuzeigen.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} Es ist jedoch keine zusätzliche Einrichtung erforderlich.

## Bedingte Anzeige von In-App-Nachrichten für das Internet {#conditionally-displaying-in-app-messages-for-web}

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

### 1. Aufrufe von `automaticallyShowInAppMessages()` entfernen {#1-remove-calls-to-automaticallyshowinappmessages}

Entfernen Sie alle Aufrufe von [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages), da sie jede angepasste Logik, die Sie später implementieren, außer Kraft setzen.

!!step
lines-index.js=6

#### 2. Debugging aktivieren (optional) {#2-enable-debugging-optional}

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!!step
lines-index.js=9-18

#### 3. Updates für In-App-Nachrichten abonnieren {#3-subscribe-to-in-app-message-updates}

Registrierung Sie einen Callback mit [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage), um jedes Mal eine `message` zu erhalten, wenn eine In-App-Nachricht getriggert wird.

!!step
lines-index.js=10-13

#### 4. Bedingte Logik erstellen {#4-create-conditional-logic}

Erstellen Sie eine angepasste Logik, um zu steuern, wann Nachrichten angezeigt werden. In diesem Beispiel prüft die Logik, ob die URL `"checkout"` enthält oder ob ein `#checkout`-Element auf der Seite existiert.

!!step
lines-index.js=16

#### 5. Nachrichten mit `showInAppMessage` anzeigen {#5-display-messages-with-showinappmessage}

Um die Nachricht anzuzeigen, rufen Sie [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage) auf. Wird dies ausgelassen, wird die Nachricht übersprungen.

{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} Außerdem müssen Sie [In-App-Nachrichten für Android aktivieren]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=android#android_enabling-in-app-messages).

## Bedingte Anzeige von In-App-Nachrichten für Android {#conditionally-displaying-in-app-messages-for-android}

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

### 1. Debugging aktivieren (optional) {#1-enable-debugging-optional}

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!!step
lines-MainApplication.kt=26-28

#### 2. Activity-Lifecycle-Callbacks Registrierung {#2-register-activity-lifecycle-callbacks}

Registrierung Sie den Standard-Listener von Braze, um den Lebenszyklus der In-App-Nachrichten zu verwalten.

!!step
lines-MainApplication.kt=30-44

#### 3. Einen In-App-Nachrichten-Listener einrichten {#3-set-up-an-in-app-message-listener}

Verwenden Sie `BrazeInAppMessageManager`, um einen angepassten Listener einzurichten, der Nachrichten abfängt, bevor sie angezeigt werden.

!!step
lines-MainApplication.kt=34-42

#### 4. Bedingte Logik erstellen

Verwenden Sie eine angepasste Logik, um die Anzeige von Nachrichten zu steuern. In diesem Beispiel prüft die angepasste Logik, ob das Extra `should_display_message` auf `"true"` gesetzt ist.

!!step
lines-MainApplication.kt=38,41

#### 5. Nachricht zurückgeben oder verwerfen {#5-return-or-discard-the-message}

Geben Sie eine `InAppMessageOperation` mit `DISPLAY_NOW` zurück, um die Nachricht anzuzeigen, oder mit `DISCARD`, um sie zu unterdrücken.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} Außerdem müssen Sie [In-App-Nachrichten für Swift aktivieren]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=swift#swift_enabling-in-app-messages).

## Bedingte Anzeige von In-App-Nachrichten für Swift {#conditionally-displaying-in-app-messages-for-swift}

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

### 1. `BrazeInAppMessageUIDelegate` implementieren {#1-implement-the-brazeinappmessageuidelegate}

Implementieren Sie in Ihrer AppDelegate-Klasse das [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/delegate), damit Sie später die Methode `inAppMessage` überschreiben können.

!!step
lines-AppDelegate.swift=12

#### 2. Debugging aktivieren (optional)

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!!step
lines-AppDelegate.swift=19-21

#### 3. Braze-UI und Delegate einrichten {#3-set-up-your-braze-ui-and-delegate}

`BrazeInAppMessageUI()` rendert In-App-Nachrichten standardmäßig. Indem Sie `self` als Delegate zuweisen, können Sie Nachrichten abfangen und verarbeiten, bevor sie angezeigt werden.

!!step
lines-AppDelegate.swift=26-33

#### 4. `DisplayChoice` mit bedingter Logik überschreiben {#4-override-displaychoice-with-conditional-logic}

Überschreiben Sie [`inAppMessage(_:displayChoiceForMessage:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb), um zu entscheiden, ob eine Nachricht angezeigt werden soll. Geben Sie `.now` zurück, um die Nachricht anzuzeigen, oder `.discard`, um sie zu unterdrücken.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}