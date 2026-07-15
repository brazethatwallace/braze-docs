---
nav_title: トリガーメッセージの延期
article_title: "チュートリアル: トリガーメッセージの延期と復元"
description: ""
page_order: 1
layout: scrolly
---

# チュートリアル: トリガーメッセージの延期と復元 {#tutorial-deferring-and-restoring-triggered-messages}

> このチュートリアルのサンプルコードに従って、Braze SDKを使用してトリガーされたアプリ内メッセージを延期および復元する方法を学びます。

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} ただし、追加の設定は不要です。

## Webのトリガーメッセージの延期と復元 {#deferring-and-restoring-triggered-messages-for-web}

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

### 1. `automaticallyShowInAppMessages()` の呼び出しを削除する {#1-remove-calls-to-automaticallyshowinappmessages}

後で実装するカスタムロジックをオーバーライドしてしまうため、[`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages) のすべての呼び出しを削除します。

!!step
lines-index.js=6

#### 2. デバッグを有効にする（オプション） {#2-enable-debugging-optional}

開発中のトラブルシューティングを容易にするために、デバッグを有効にすることを検討してください。

!!step
lines-index.js=9-16

#### 3. アプリ内メッセージコールバックハンドラーにサブスクライブする {#3-subscribe-to-the-in-app-message-callback-handler}

[`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage) を使用してコールバックを登録し、アプリ内メッセージがトリガーされるたびにメッセージを受信します。

!!step
lines-index.js=11-12

#### 4. `message` インスタンスを延期する {#4-defer-the-message-instance}

メッセージを延期するには、[`deferInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#deferinappmessage) を呼び出します。Brazeはこのメッセージをシリアライズして保存し、将来のページ読み込み時に表示できるようにします。

!!step
lines-index.js=18-24

#### 5. 以前に延期されたメッセージを取得する {#5-retrieve-a-previously-deferred-message}

以前に延期されたメッセージを取得するには、[`getDeferredInAppMessage()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getdeferredinappmessage) を呼び出します。

!!step
lines-index.js=21-23

#### 6. 延期されたメッセージを表示する {#6-display-the-deferred-message}

延期されたメッセージを取得したら、[`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage) にメッセージを渡して表示します。

!!step
lines-index.js=13-15

#### 7. メッセージをすぐに表示する {#7-display-a-message-immediately}

メッセージを延期するのではなくすぐに表示するには、`subscribeToInAppMessage` コールバックで [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage) を直接呼び出します。
{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} また、[Androidのアプリ内メッセージを有効にする]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=android#android_enabling-in-app-messages)必要もあります。

## Androidのトリガーメッセージの延期と復元 {#deferring-and-restoring-triggered-messages-for-android}

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

### 1. シングルトン `Application` インスタンスを作成する {#1-create-a-singleton-application-instance}

コンパニオンオブジェクトを使って `Application` クラスをシングルトンとして公開し、コード内で後からアクセスできるようにします。

!!step
lines-MainApplication.kt=25

#### 2. デバッグを有効にする（オプション）

開発中のトラブルシューティングを容易にするために、デバッグを有効にすることを検討してください。

!!step
lines-MainApplication.kt=34-36

#### 3. アクティビティライフサイクルコールバックを登録する {#3-register-activity-lifecycle-callbacks}

アプリ内メッセージのライフサイクルを処理するBrazeのデフォルトリスナーを登録します。

!!step
lines-MainApplication.kt=39-49

#### 4. アプリ内メッセージリスナーを設定する {#4-set-up-an-in-app-message-listener}

`BrazeInAppMessageManager` を使用して、メッセージが表示される前にインターセプトするカスタムリスナーを設定します。

!!step
lines-MainApplication.kt=43,46

#### 5. 条件付きロジックを作成する {#5-create-conditional-logic}

タイミングを制御するには `showMessage` フラグを使用します&#8212;メッセージをすぐに表示する場合は `DISPLAY_NOW` を返し、延期する場合は `DISPLAY_LATER` を返します。

!!step
lines-MainApplication.kt=52-55

#### 6. 延期メッセージを表示するメソッドを作成する {#6-create-a-method-for-displaying-deferred-messages}

`showDeferredMessage` を使って次のアプリ内メッセージをトリガーします。`showMessage` が `true` の場合、リスナーは `DISPLAY_NOW` を返します。

!!step
lines-MainActivity.kt=29

#### 7. UIからメソッドをトリガーする {#7-trigger-the-method-from-your-ui}

以前に延期されたメッセージを表示するには、ボタンやタップなどのUIから `showDeferredMessage(true)` を呼び出します。

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} また、[Swiftのアプリ内メッセージを有効にする]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=swift#swift_enabling-in-app-messages)必要もあります。

## Swiftのトリガーメッセージの延期と復元 {#deferring-and-restoring-triggered-messages-for-swift}

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

### 1. `BrazeInAppMessageUIDelegate` を実装する {#1-implement-the-brazeinappmessageuidelegate}

`AppDelegate` クラスで [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) を実装して、後で `inAppMessage` メソッドをオーバーライドできるようにします。

!!step
lines-AppDelegate.swift=19

#### 2. デバッグを有効にする（オプション）

開発中のトラブルシューティングを容易にするために、デバッグを有効にすることを検討してください。

!!step
lines-AppDelegate.swift=25-27

#### 3. Braze UIとデリゲートを設定する {#3-set-up-your-braze-ui-and-delegate}

`BrazeInAppMessageUI()` はデフォルトでアプリ内メッセージをレンダリングします。`self` をデリゲートとして割り当てることで、メッセージが表示される前にインターセプトして処理できます。インスタンスは必ず保存してください。後で延期したメッセージを復元するときに必要になります。

!!step
lines-AppDelegate.swift=32-41

#### 4. `DisplayChoice` を条件付きロジックでオーバーライドする {#4-override-displaychoice-with-conditional-logic}

メッセージを表示するタイミングを決定するには、[`inAppMessage(_:displayChoiceForMessage:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) をオーバーライドします。すぐに表示する場合は `.now` を返し、後で表示する場合は `.reenqueue` を返します。

!!step
lines-AppDelegate.swift=43-46

#### 5. 延期メッセージを表示するメソッドを作成する {#5-create-a-method-to-show-deferred-messages}

`showDeferredMessage(true)` を呼び出してスタック内の次の延期メッセージを表示するメソッドを作成します。呼び出されると `showMessage` が `true` に設定され、デリゲートは `.now` を返します。

!!step
lines-ContentView.swift=1-14

#### 6. UIからメソッドをトリガーする {#5-trigger-the-method-from-your-ui}

以前に延期されたメッセージを表示するには、ボタンやタップなどのUIから `showDeferredMessage(true)` を呼び出します。

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}