---
nav_title: 트리거된 메시지 지연
article_title: "튜토리얼: 트리거된 메시지 지연 및 복원"
description: ""
page_order: 1
layout: scrolly
---

# 튜토리얼: 트리거된 메시지 지연 및 복원 {#tutorial-deferring-and-restoring-triggered-messages}

> 이 튜토리얼의 샘플 코드를 따라 Braze SDK를 사용하여 트리거된 인앱 메시지를 지연하고 복원하는 방법을 알아보세요.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} 그러나 추가 설정은 필요하지 않습니다.

## 웹용 트리거된 메시지 지연 및 복원 {#deferring-and-restoring-triggered-messages-for-web}

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

### 1. `automaticallyShowInAppMessages()` 호출 제거 {#1-remove-calls-to-automaticallyshowinappmessages}

나중에 구현할 커스텀 로직을 재정의하므로 [`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages)에 대한 모든 호출을 제거하세요.

!!step
lines-index.js=6

#### 2. 디버깅 활성화(선택 사항) {#2-enable-debugging-optional}

개발 중 문제 해결을 쉽게 하기 위해 디버깅을 활성화하는 것을 고려하세요.

!!step
lines-index.js=9-16

#### 3. 인앱 메시지 콜백 핸들러 구독 {#3-subscribe-to-the-in-app-message-callback-handler}

인앱 메시지가 트리거될 때마다 메시지를 수신하려면 [`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage)에 콜백을 등록하세요.

!!step
lines-index.js=11-12

#### 4. `message` 인스턴스 지연 {#4-defer-the-message-instance}

메시지를 지연하려면 [`deferInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#deferinappmessage)를 호출하세요. Braze는 이 메시지를 직렬화하고 저장하여 이후 페이지 로드 시 표시할 수 있도록 합니다.

!!step
lines-index.js=18-24

#### 5. 이전에 지연된 메시지 검색 {#5-retrieve-a-previously-deferred-message}

이전에 지연된 메시지를 검색하려면 [`getDeferredInAppMessage()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getdeferredinappmessage)를 호출하세요.

!!step
lines-index.js=21-23

#### 6. 지연된 메시지 표시 {#6-display-the-deferred-message}

지연된 메시지를 검색한 후 [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage)에 전달하여 표시하세요.

!!step
lines-index.js=13-15

#### 7. 메시지 즉시 표시 {#7-display-a-message-immediately}

메시지를 지연하지 않고 바로 표시하려면 `subscribeToInAppMessage` 콜백에서 [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage)를 직접 호출하세요.
{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} 또한 [Android용 인앱 메시지 활성화]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=android#android_enabling-in-app-messages)가 필요합니다.

## Android용 트리거된 메시지 지연 및 복원 {#deferring-and-restoring-triggered-messages-for-android}

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

### 1. 싱글톤 `Application` 인스턴스 생성 {#1-create-a-singleton-application-instance}

컴패니언 오브젝트를 사용하여 `Application` 클래스를 싱글톤으로 노출하면 코드의 다른 곳에서 접근할 수 있습니다.

!!step
lines-MainApplication.kt=25

#### 2. 디버깅 활성화(선택 사항)

개발 중 문제 해결을 쉽게 하기 위해 디버깅을 활성화하는 것을 고려하세요.

!!step
lines-MainApplication.kt=34-36

#### 3. 액티비티 라이프사이클 콜백 등록 {#3-register-activity-lifecycle-callbacks}

Braze의 기본 리스너를 등록하여 인앱 메시지 라이프사이클을 처리합니다.

!!step
lines-MainApplication.kt=39-49

#### 4. 인앱 메시지 리스너 설정 {#4-set-up-an-in-app-message-listener}

`BrazeInAppMessageManager`를 사용하여 메시지가 표시되기 전에 가로채는 커스텀 리스너를 설정합니다.

!!step
lines-MainApplication.kt=43,46

#### 5. 조건 로직 생성 {#5-create-conditional-logic}

`showMessage` 플래그를 사용하여 타이밍을 제어하세요&#8212;메시지를 지금 표시하려면 `DISPLAY_NOW`를 반환하고, 지연하려면 `DISPLAY_LATER`를 반환합니다.

!!step
lines-MainApplication.kt=52-55

#### 6. 지연된 메시지를 표시하는 메서드 생성 {#6-create-a-method-for-displaying-deferred-messages}

`showDeferredMessage`를 사용하여 다음 인앱 메시지를 트리거하세요. `showMessage`가 `true`이면 리스너가 `DISPLAY_NOW`를 반환합니다.

!!step
lines-MainActivity.kt=29

#### 7. UI에서 메서드 트리거 {#7-trigger-the-method-from-your-ui}

이전에 지연된 메시지를 표시하려면 버튼이나 탭과 같은 UI에서 `showDeferredMessage(true)`를 호출하세요.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} 또한 [Swift용 인앱 메시지 활성화]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=swift#swift_enabling-in-app-messages)가 필요합니다.

## Swift용 트리거된 메시지 지연 및 복원 {#deferring-and-restoring-triggered-messages-for-swift}

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

### 1. `BrazeInAppMessageUIDelegate` 구현 {#1-implement-the-brazeinappmessageuidelegate}

`AppDelegate` 클래스에서 [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate)를 구현하여 나중에 `inAppMessage` 메서드를 재정의할 수 있도록 합니다.

!!step
lines-AppDelegate.swift=19

#### 2. 디버깅 활성화(선택 사항)

개발 중 문제 해결을 쉽게 하기 위해 디버깅을 활성화하는 것을 고려하세요.

!!step
lines-AppDelegate.swift=25-27

#### 3. Braze UI 및 델리게이트 설정 {#3-set-up-your-braze-ui-and-delegate}

`BrazeInAppMessageUI()`는 기본적으로 인앱 메시지를 렌더링합니다. `self`를 델리게이트로 할당하면 메시지가 표시되기 전에 가로채고 처리할 수 있습니다. 나중에 지연된 메시지를 복원할 때 필요하므로 인스턴스를 반드시 저장하세요.

!!step
lines-AppDelegate.swift=32-41

#### 4. 조건 로직으로 `DisplayChoice` 재정의 {#4-override-displaychoice-with-conditional-logic}

[`inAppMessage(_:displayChoiceForMessage:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb)를 재정의하여 메시지를 표시할 시점을 결정합니다. 즉시 표시하려면 `.now`를 반환하고, 나중으로 지연하려면 `.reenqueue`를 반환합니다.

!!step
lines-AppDelegate.swift=43-46

#### 5. 지연된 메시지를 표시하는 메서드 생성 {#5-create-a-method-to-show-deferred-messages}

`showDeferredMessage(true)`를 호출하여 스택의 다음 지연된 메시지를 표시하는 메서드를 생성합니다. 호출되면 `showMessage`가 `true`로 설정되어 델리게이트가 `.now`를 반환합니다.

!!step
lines-ContentView.swift=1-14

#### 6. UI에서 메서드 트리거 {#5-trigger-the-method-from-your-ui}

이전에 지연된 메시지를 표시하려면 버튼이나 탭과 같은 UI에서 `showDeferredMessage(true)`를 호출하세요.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}