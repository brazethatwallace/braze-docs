---
nav_title: Getriggerte Nachrichten zurückstellen
article_title: "Anleitung: Getriggerte Nachrichten aufschieben und wiederherstellen"
description: ""
page_order: 1
layout: scrolly
---

# Anleitung: Getriggerte Nachrichten aufschieben und wiederherstellen {#tutorial-deferring-and-restoring-triggered-messages}

> Folgen Sie dem Beispielcode in dieser Anleitung, um getriggerte In-App-Nachrichten mit dem Braze SDK aufzuschieben und wiederherzustellen.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} Es ist jedoch keine zusätzliche Einrichtung erforderlich.

## Getriggerte Nachrichten für Web aufschieben und wiederherstellen {#deferring-and-restoring-triggered-messages-for-web}

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

### 1. Aufrufe von `automaticallyShowInAppMessages()` entfernen {#1-remove-calls-to-automaticallyshowinappmessages}

Entfernen Sie alle Aufrufe von [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages), da sie jede angepasste Logik, die Sie später implementieren, außer Kraft setzen.

!!step
lines-index.js=6

#### 2. Debugging aktivieren (optional) {#2-enable-debugging-optional}

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!!step
lines-index.js=9-16

#### 3. Den Callback-Handler für In-App-Nachrichten abonnieren {#3-subscribe-to-the-in-app-message-callback-handler}

Registrierung Sie einen Callback mit [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage), um jedes Mal eine Nachricht zu erhalten, wenn eine In-App-Nachricht getriggert wird.

!!step
lines-index.js=11-12

#### 4. Die `message`-Instanz aufschieben {#4-defer-the-message-instance}

Um die Nachricht aufzuschieben, rufen Sie [`deferInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#deferinappmessage) auf. Braze serialisiert und speichert diese Nachricht, damit Sie sie bei einem späteren Seitenaufruf anzeigen können.

!!step
lines-index.js=18-24

#### 5. Eine zuvor aufgeschobene Nachricht abrufen {#5-retrieve-a-previously-deferred-message}

Um zuvor aufgeschobene Nachrichten abzurufen, rufen Sie [`getDeferredInAppMessage()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getdeferredinappmessage) auf.

!!step
lines-index.js=21-23

#### 6. Die aufgeschobene Nachricht anzeigen {#6-display-the-deferred-message}

Nachdem Sie eine aufgeschobene Nachricht abgerufen haben, zeigen Sie sie an, indem Sie sie an [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage) übergeben.

!!step
lines-index.js=13-15

#### 7. Eine Nachricht sofort anzeigen {#7-display-a-message-immediately}

Um eine Nachricht sofort anzuzeigen, anstatt sie aufzuschieben, rufen Sie [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage) direkt in Ihrem `subscribeToInAppMessage`-Callback auf.
{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} Außerdem müssen Sie [In-App-Nachrichten für Android aktivieren]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=android#android_enabling-in-app-messages).

## Getriggerte Nachrichten für Android aufschieben und wiederherstellen {#deferring-and-restoring-triggered-messages-for-android}

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

### 1. Eine Singleton-`Application`-Instanz erstellen {#1-create-a-singleton-application-instance}

Verwenden Sie ein Companion-Objekt, um Ihre `Application`-Klasse als Singleton bereitzustellen, damit Sie später in Ihrem Code darauf zugreifen können.

!!step
lines-MainApplication.kt=25

#### 2. Debugging aktivieren (optional)

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!!step
lines-MainApplication.kt=34-36

#### 3. Activity-Lifecycle-Callbacks Registrierung {#3-register-activity-lifecycle-callbacks}

Registrierung Sie den Standard-Listener von Braze, um den Lebenszyklus der In-App-Nachrichten zu verwalten.

!!step
lines-MainApplication.kt=39-49

#### 4. Einen Listener für In-App-Nachrichten einrichten {#4-set-up-an-in-app-message-listener}

Verwenden Sie `BrazeInAppMessageManager`, um einen angepassten Listener einzurichten, der Nachrichten abfängt, bevor sie angezeigt werden.

!!step
lines-MainApplication.kt=43,46

#### 5. Bedingte Logik erstellen {#5-create-conditional-logic}

Verwenden Sie das Flag `showMessage`, um das Timing zu steuern – geben Sie `DISPLAY_NOW` zurück, um die Nachricht sofort anzuzeigen, oder `DISPLAY_LATER`, um sie aufzuschieben.

!!step
lines-MainApplication.kt=52-55

#### 6. Eine Methode zur Anzeige aufgeschobener Nachrichten erstellen {#6-create-a-method-for-displaying-deferred-messages}

Verwenden Sie `showDeferredMessage`, um die nächste In-App-Nachricht zu triggern. Wenn `showMessage` den Wert `true` hat, gibt der Listener `DISPLAY_NOW` zurück.

!!step
lines-MainActivity.kt=29

#### 7. Die Methode über Ihre UI triggern {#7-trigger-the-method-from-your-ui}

Um die zuvor aufgeschobene Nachricht anzuzeigen, rufen Sie `showDeferredMessage(true)` über Ihre UI auf, z. B. über einen Button oder durch Antippen.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} Außerdem müssen Sie [In-App-Nachrichten für Swift aktivieren]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=swift#swift_enabling-in-app-messages).

## Getriggerte Nachrichten für Swift aufschieben und wiederherstellen {#deferring-and-restoring-triggered-messages-for-swift}

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

### 1. Das `BrazeInAppMessageUIDelegate` implementieren {#1-implement-the-brazeinappmessageuidelegate}

Implementieren Sie in Ihrer `AppDelegate`-Klasse das [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate), damit Sie die Methode `inAppMessage` später überschreiben können.

!!step
lines-AppDelegate.swift=19

#### 2. Debugging aktivieren (optional)

Um die Fehlerbehebung während der Entwicklung zu erleichtern, sollten Sie das Debugging aktivieren.

!!step
lines-AppDelegate.swift=25-27

#### 3. Braze-UI und Delegate einrichten {#3-set-up-your-braze-ui-and-delegate}

`BrazeInAppMessageUI()` rendert In-App-Nachrichten standardmäßig. Wenn Sie `self` als Delegate zuweisen, können Sie Nachrichten abfangen und verarbeiten, bevor sie angezeigt werden. Speichern Sie die Instanz unbedingt, da Sie sie später benötigen, um aufgeschobene Nachrichten wiederherzustellen.

!!step
lines-AppDelegate.swift=32-41

#### 4. `DisplayChoice` mit bedingter Logik überschreiben {#4-override-displaychoice-with-conditional-logic}

Überschreiben Sie [`inAppMessage(_:displayChoiceForMessage:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb), um festzulegen, wann eine Nachricht angezeigt werden soll. Geben Sie `.now` zurück, um sie sofort anzuzeigen, oder `.reenqueue`, um sie aufzuschieben.

!!step
lines-AppDelegate.swift=43-46

#### 5. Eine Methode zur Anzeige aufgeschobener Nachrichten erstellen {#5-create-a-method-to-show-deferred-messages}

Erstellen Sie eine Methode, die `showDeferredMessage(true)` aufruft, um die nächste aufgeschobene Nachricht im Stack anzuzeigen. Beim Aufruf wird `showMessage` auf `true` gesetzt, sodass der Delegate `.now` zurückgibt.

!!step
lines-ContentView.swift=1-14

#### 6. Die Methode über Ihre UI triggern {#5-trigger-the-method-from-your-ui}

Um die zuvor aufgeschobene Nachricht anzuzeigen, rufen Sie `showDeferredMessage(true)` über Ihre UI auf, z. B. über einen Button oder durch Antippen.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}