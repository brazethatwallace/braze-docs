---
nav_title: 메시지 사용자 지정
article_title: Braze SDK용 인앱 메시지 사용자 지정
page_order: 0.1
description: "Braze SDK의 인앱 메시지를 설정하는 방법을 알아보세요."
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# 인앱 메시지 사용자 지정 {#customize-in-app-messages}

> Braze SDK의 인앱 메시지를 사용자 지정하는 방법을 알아보세요. 고급 스타일링 기술에 대해서는 [키-값 페어를 사용한 메시지 스타일링 사용자 지정]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/customizing_message_styling) 튜토리얼을 확인하세요.

{% sdktabs %}
{% sdktab web %}
{% multi_lang_include developer_guide/web/in_app_messages/customization.md %}
{% endsdktab %}

{% sdktab android %}
{% multi_lang_include developer_guide/android/in_app_messages/customization.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/in_app_messages/customization.md %}
{% endsdktab %}

{% sdktab react native %}
{% multi_lang_include developer_guide/react_native/analytics/logging_iam_data.md %}
{% endsdktab %}

{% sdktab unity %}
## 표시 동작 사용자 지정 {#customizing-the-display-behavior}

런타임에 다음을 통해 인앱 메시지의 표시 동작을 변경할 수 있습니다.

```csharp
// Sets in-app messages to display immediately when triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_NOW);

// Sets in-app messages to display at a later time and be saved in a stack.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER);

// Sets in-app messages to be discarded after being triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISCARD);
```

## 커스텀 리스너 설정 {#setting-a-custom-listener}

사용자가 인앱 메시지와 상호작용하는 방식을 더 세밀하게 제어해야 하는 경우, `BrazeInAppMessageListener`를 사용하여 `Appboy.AppboyBinding.inAppMessageListener`에 할당하세요. 사용하지 않으려는 델리게이트는 `null`로 남겨두면 됩니다.

```csharp
BrazeInAppMessageListener listener = new BrazeInAppMessageListener() {
  BeforeInAppMessageDisplayed = BeforeInAppMessageDisplayed,
  OnInAppMessageButtonClicked = OnInAppMessageButtonClicked,
  OnInAppMessageClicked       = OnInAppMessageClicked,
  OnInAppMessageHTMLClicked   = OnInAppMessageHTMLClicked,
  OnInAppMessageDismissed     = OnInAppMessageDismissed,
};
Appboy.AppboyBinding.inAppMessageListener = listener;

public void BeforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  // Executed before an in-app message is displayed.
}

public void OnInAppMessageButtonClicked(IInAppMessage inAppMessage, InAppMessageButton inAppMessageButton) {
  // Executed whenever an in-app message button is clicked.
}

public void OnInAppMessageClicked(IInAppMessage inAppMessage) {
  // Executed whenever an in-app message is clicked.
}

public void OnInAppMessageHTMLClicked(IInAppMessage inAppMessage, Uri uri) {
  // Executed whenever an HTML in-app message is clicked.
}

public void OnInAppMessageDismissed(IInAppMessage inAppMessage) {
  // Executed whenever an in-app message is dismissed without a click.
}
```

{% endsdktab %}
{% endsdktabs %}