---
nav_title: 조건부로 메시지 표시하기
article_title: "튜토리얼: 조건부 인앱 메시지 표시"
description: ""
page_order: 1
layout: scrolly
---

# 튜토리얼: 조건부 인앱 메시지 표시 {#tutorial-conditionally-displaying-in-app-messages}

> 이 튜토리얼의 샘플 코드를 따라 Braze SDK를 사용하여 인앱 메시지를 조건부로 표시하는 방법을 알아보세요.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/prerequisites/web.md %} 그러나 추가 설정은 필요하지 않습니다.

## 웹용 인앱 메시지 조건부 표시 {#conditionally-displaying-in-app-messages-for-web}

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

### 1. `automaticallyShowInAppMessages()` 호출 제거 {#1-remove-calls-to-automaticallyshowinappmessages}

[`automaticallyShowInAppMessages()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#automaticallyshowinappmessages)에 대한 호출을 모두 제거하세요. 이 호출은 나중에 구현하는 커스텀 로직을 재정의하기 때문입니다.

!!step
lines-index.js=6

#### 2. 디버깅 활성화(선택 사항) {#2-enable-debugging-optional}

개발 중 문제 해결을 쉽게 하려면 디버깅을 활성화하는 것을 고려하세요.

!!step
lines-index.js=9-18

#### 3. 인앱 메시지 업데이트 구독 {#3-subscribe-to-in-app-message-updates}

[`subscribeToInAppMessage(callback)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetoinappmessage)로 콜백을 등록하면 인앱 메시지가 트리거될 때마다 `message`를 수신할 수 있습니다.

!!step
lines-index.js=10-13

#### 4. 조건 로직 생성 {#4-create-conditional-logic}

메시지가 표시되는 시점을 제어하는 커스텀 로직을 생성합니다. 이 예제에서는 URL에 `"checkout"`이 포함되어 있는지 또는 페이지에 `#checkout` 요소가 있는지 확인합니다.

!!step
lines-index.js=16

#### 5. `showInAppMessage`로 메시지 표시 {#5-display-messages-with-showinappmessage}

메시지를 표시하려면 [`showInAppMessage(message)`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showinappmessage)를 호출합니다. 생략하면 메시지를 건너뜁니다.

{% endscrolly %}
{% endsdktab %}
{% sdktab android %}
{% multi_lang_include developer_guide/prerequisites/android.md %} 또한 [Android용 인앱 메시지 활성화]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=android#android_enabling-in-app-messages)가 필요합니다.

## Android용 인앱 메시지 조건부 표시 {#conditionally-displaying-in-app-messages-for-android}

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

### 1. 디버깅 활성화(선택 사항) {#1-enable-debugging-optional}

개발 중 문제 해결을 쉽게 하려면 디버깅을 활성화하는 것을 고려하세요.

!!step
lines-MainApplication.kt=26-28

#### 2. 액티비티 수명 주기 콜백 등록 {#2-register-activity-lifecycle-callbacks}

Braze의 기본 리스너를 등록하여 인앱 메시지 수명 주기를 처리합니다.

!!step
lines-MainApplication.kt=30-44

#### 3. 인앱 메시지 리스너 설정 {#3-set-up-an-in-app-message-listener}

`BrazeInAppMessageManager`를 사용하여 메시지가 표시되기 전에 가로채는 커스텀 리스너를 설정합니다.

!!step
lines-MainApplication.kt=34-42

#### 4. 조건 로직 생성

커스텀 로직을 사용하여 메시지 표시 타이밍을 제어합니다. 이 예제에서는 `should_display_message` 추가 항목이 `"true"`로 설정되어 있는지 확인합니다.

!!step
lines-MainApplication.kt=38,41

#### 5. 메시지 반환 또는 삭제 {#5-return-or-discard-the-message}

메시지를 표시하려면 `DISPLAY_NOW`와 함께, 숨기려면 `DISCARD`와 함께 `InAppMessageOperation`을 반환합니다.

{% endscrolly %}
{% endsdktab %}
{% sdktab swift %}
{% multi_lang_include developer_guide/prerequisites/swift.md %} 또한 [Swift용 인앱 메시지 활성화]({{site.baseurl}}/developer_guide/in_app_messages?sdktab=swift#swift_enabling-in-app-messages)가 필요합니다.

## Swift용 인앱 메시지 조건부 표시 {#conditionally-displaying-in-app-messages-for-swift}

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

### 1. `BrazeInAppMessageUIDelegate` 구현 {#1-implement-the-brazeinappmessageuidelegate}

AppDelegate 클래스에서 [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/delegate)를 구현하여 나중에 `inAppMessage` 메서드를 재정의할 수 있도록 합니다.

!!step
lines-AppDelegate.swift=12

#### 2. 디버깅 활성화(선택 사항)

개발 중 문제 해결을 쉽게 하려면 디버깅을 활성화하는 것을 고려하세요.

!!step
lines-AppDelegate.swift=19-21

#### 3. Braze UI 및 델리게이트 설정 {#3-set-up-your-braze-ui-and-delegate}

`BrazeInAppMessageUI()`는 기본적으로 인앱 메시지를 렌더링합니다. `self`를 델리게이트로 지정하면 메시지가 표시되기 전에 가로채서 처리할 수 있습니다.

!!step
lines-AppDelegate.swift=26-33

#### 4. 조건 로직으로 `DisplayChoice` 재정의 {#4-override-displaychoice-with-conditional-logic}

[`inAppMessage(_:displayChoiceForMessage:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb)를 재정의하여 메시지 표시 여부를 결정합니다. 메시지를 표시하려면 `.now`를, 숨기려면 `.discard`를 반환합니다.

{% endscrolly %}
{% endsdktab %}
{% endsdktabs %}