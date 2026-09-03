---
nav_title: 条件付きでメッセージを表示する
article_title: "チュートリアル: 条件付きでアプリ内メッセージを表示する"
description: ""
page_order: 1
layout: scrolly
---

# チュートリアル: 条件付きでアプリ内メッセージを表示する {#tutorial-conditionally-displaying-in-app-messages}

> このチュートリアルのサンプルコードに従って、Braze SDKを使用してアプリ内メッセージを条件付きで表示する方法を学びます。

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} ただし、追加の設定は不要です。

## Webでアプリ内メッセージを条件付きで表示する {#conditionally-displaying-in-app-messages-for-web}

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

### 1. `automaticallyShowInAppMessages()` の呼び出しを削除する {#1-remove-calls-to-automaticallyshowinappmessages}

[`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages) の呼び出しは、後で実装するカスタムロジックをオーバーライドするため、すべて削除してください。

!!step
lines-index.js=6

#### 2. デバッグを有効にする（オプション） {#2-enable-debugging-optional}

開発中のトラブルシューティングを容易にするために、デバッグを有効にすることを検討してください。

!!step
lines-index.js=9-18

#### 3. アプリ内メッセージの更新を購読する {#3-subscribe-to-in-app-message-updates}

[`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) にコールバックを登録して、アプリ内メッセージがトリガーされるたびに `message` を受信します。

!!step
lines-index.js=10-13

#### 4. 条件付きロジックを作成する {#4-create-conditional-logic}

メッセージを表示するタイミングをコントロールするカスタムロジックを作成します。この例では、URLに `"checkout"` が含まれているかどうか、またはページに `#checkout` 要素が存在するかどうかをチェックします。

!!step
lines-index.js=16

#### 5. `showInAppMessage` でメッセージを表示する {#5-display-messages-with-showinappmessage}

メッセージを表示するには、[`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage) を呼び出します。省略した場合、メッセージはスキップされます。

{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} また、[Androidでアプリ内メッセージを有効にする]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=android#android_enabling-in-app-messages)必要もあります。

## Androidでアプリ内メッセージを条件付きで表示する {#conditionally-displaying-in-app-messages-for-android}

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

### 1. デバッグを有効にする（オプション） {#1-enable-debugging-optional}

開発中のトラブルシューティングを容易にするために、デバッグを有効にすることを検討してください。

!!step
lines-MainApplication.kt=26-28

#### 2. アクティビティライフサイクルコールバックを登録する {#2-register-activity-lifecycle-callbacks}

アプリ内メッセージのライフサイクルを処理するBrazeのデフォルトリスナーを登録します。

!!step
lines-MainApplication.kt=30-44

#### 3. アプリ内メッセージリスナーを設定する {#3-set-up-an-in-app-message-listener}

`BrazeInAppMessageManager` を使用して、メッセージが表示される前にインターセプトするカスタムリスナーを設定します。

!!step
lines-MainApplication.kt=34-42

#### 4. 条件付きロジックを作成する

カスタムロジックを使用して、メッセージの表示タイミングをコントロールします。この例では、`should_display_message` エクストラが `"true"` に設定されているかどうかをチェックします。

!!step
lines-MainApplication.kt=38,41

#### 5. メッセージを返すか破棄する {#5-return-or-discard-the-message}

メッセージを表示するには `DISPLAY_NOW` を、非表示にするには `DISCARD` を指定して `InAppMessageOperation` を返します。

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} また、[Swiftでアプリ内メッセージを有効にする]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=swift#swift_enabling-in-app-messages)必要もあります。

## Swiftでアプリ内メッセージを条件付きで表示する {#conditionally-displaying-in-app-messages-for-swift}

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

### 1. `BrazeInAppMessageUIDelegate` を実装する {#1-implement-the-brazeinappmessageuidelegate}

AppDelegateクラスで [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/delegate) を実装し、後で `inAppMessage` メソッドをオーバーライドできるようにします。

!!step
lines-AppDelegate.swift=12

#### 2. デバッグを有効にする（オプション）

開発中のトラブルシューティングを容易にするために、デバッグを有効にすることを検討してください。

!!step
lines-AppDelegate.swift=19-21

#### 3. Braze UIとデリゲートを設定する {#3-set-up-your-braze-ui-and-delegate}

`BrazeInAppMessageUI()` はデフォルトでアプリ内メッセージをレンダリングします。`self` をデリゲートとして割り当てることで、メッセージが表示される前にインターセプトして処理できます。

!!step
lines-AppDelegate.swift=26-33

#### 4. `DisplayChoice` を条件付きロジックでオーバーライドする {#4-override-displaychoice-with-conditional-logic}

[`inAppMessage(_:displayChoiceForMessage:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) をオーバーライドして、メッセージを表示するかどうかを決定します。メッセージを表示する場合は `.now` を、非表示にする場合は `.discard` を返します。

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}