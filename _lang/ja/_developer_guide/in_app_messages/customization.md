---
nav_title: メッセージングをカスタマイズする
article_title: アプリ内メッセージをカスタマイズする
page_order: 0.1
description: "Braze SDKのアプリ内メッセージの設定方法について説明します。"
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# アプリ内メッセージをカスタマイズする {#customize-in-app-messages}

> Braze SDKのアプリ内メッセージをカスタマイズする方法を説明します。高度なスタイル設定については、[キーと値のペアを使ってメッセージのスタイルをカスタマイズする]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/customizing_message_styling)チュートリアルを参照してください。

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
## 表示動作をカスタマイズする {#customizing-the-display-behavior}

アプリ内メッセージの表示動作は、以下の方法で実行時に変更できます。

```csharp
// Sets in-app messages to display immediately when triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_NOW);

// Sets in-app messages to display at a later time and be saved in a stack.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER);

// Sets in-app messages to be discarded after being triggered.
Appboy.AppboyBinding.SetInAppMessageDisplayAction(BrazeUnityInAppMessageDisplayActionType.IAM_DISCARD);
```

## カスタムリスナーを設定する {#setting-a-custom-listener}

ユーザーがアプリ内メッセージとやり取りする方法をより細かく制御する必要がある場合は、`BrazeInAppMessageListener`を使用して`Appboy.AppboyBinding.inAppMessageListener`に割り当てます。使用しないデリゲートについては、単に`null`のままにしておくことができます。

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