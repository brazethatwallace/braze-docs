---
nav_title: クリック時のカスタム動作
article_title: iOS向けアプリ内メッセージのクリック時の動作をカスタマイズする
platform: iOS
page_order: 5
description: "この参考記事では、iOS アプリケーションのアプリ内メッセージングのカスタムクリック時動作について説明します。"
channel:
  - in-app messages
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# アプリ内メッセージのクリック時の動作をカスタマイズする {#customize-in-app-message-behavior-on-click}

`ABKInAppMessage`の`inAppMessageClickActionType` プロパティは、アプリ内メッセージがクリックされた後のアクション動作を定義します。このプロパティは読み取り専用です。アプリ内メッセージのクリック動作を変更する場合は、`ABKInAppMessage`で以下の方法を呼び出すことができます。

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[inAppMessage setInAppMessageClickAction:clickActionType withURI:uri];
```

{% endtab %}
{% tab swift %}

`````````swift
inAppMessage.setInAppMessageClickAction(clickActionType: clickActionType, withURI: uri)
```

{% endtab %}
{% endtabs %}

`inAppMessageClickActionType` は次のいずれかの値に設定できます。

| `ABKInAppMessageClickActionType` | クリック時動作 |
| -------------------------- | -------- |
| `ABKInAppMessageRedirectToURI` | メッセージがクリックされたときに指定されたURIが表示され、メッセージは閉じられます。`uri` パラメータをnilにすることはできないことに注意してください。 |
| `ABKInAppMessageNoneClickAction` | クリックするとメッセージが閉じられます。`uri` パラメータは無視され、`ABKInAppMessage`の`uri` プロパティはnilに設定されます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="アプリ内メッセージのクリック時の動作をカスタマイズする" }

{% alert important %}
ボタンを含むアプリ内メッセージの場合、ボタンテキストを追加する前にクリックアクションが追加されると、メッセージの`clickAction` も最終ペイロードに含まれます。
{% endalert %}

## アプリ内メッセージ本文クリックのカスタマイズ {#customizing-in-app-message-body-clicks}

アプリ内メッセージがクリックされると、次の[`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h) デリゲートメソッドが呼び出されます。

{% tabs %}
{% tab OBJECTIVE-C %}

`````````objc
- (BOOL) onInAppMessageClicked:(ABKInAppMessage *)inAppMessage;
```

{% endtab %}
{% tab swift %}

`````````swift
func onInAppMessageClicked(inAppMessage: ABKInAppMessage!) -> Bool
```

{% endtab %}
{% endtabs %}

## アプリ内メッセージボタンクリックのカスタマイズ {#customizing-in-app-message-button-clicks}

アプリ内メッセージボタンやHTMLアプリ内メッセージボタン（リンクなど）のクリックに対して、[`ABKInAppMessageUIDelegate`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ABKInAppMessageUIDelegate.h) には次のデリゲートメソッドが含まれています。

{% tabs %}
{% tab OBJECTIVE-C %}

`````````objc
- (BOOL)onInAppMessageButtonClicked:(ABKInAppMessageImmersive *)inAppMessage
                             button:(ABKInAppMessageButton *)button;

- (BOOL)onInAppMessageHTMLButtonClicked:(ABKInAppMessageHTML *)inAppMessage
                             clickedURL:(nullable NSURL *)clickedURL
                               buttonID:(NSString *)buttonID;
```

{% endtab %}
{% tab swift %}

`````````swift
func onInAppMessageButtonClicked(inAppMessage: ABKInAppMessageImmersive!,
                                 button: ABKInAppMessageButton) -> Bool

func onInAppMessageHTMLButtonClicked(inAppMessage: ABKInAppMessageHTML!,
                                     clickedURL: URL, buttonID: String) -> Bool
```

{% endtab %}
{% endtabs %}

各メソッドは、Brazeがクリックアクションの実行を続行すべきかどうかを示す `BOOL` 値を返します。

デリゲートメソッドでボタンのクリックアクションタイプにアクセスするには、次のコードを使用できます。

{% tabs %}
{% tab OBJECTIVE-C %}

`````````objc
if ([inAppMessage isKindOfClass:[ABKInAppMessageImmersive class]]) {
      ABKInAppMessageImmersive *immersiveIAM = (ABKInAppMessageImmersive *)inAppMessage;
      NSArray<ABKInAppMessageButton *> *buttons = immersiveIAM.buttons;
      for (ABKInAppMessageButton *button in buttons) {
         // Button action type is accessible via button.buttonClickActionType
      }
   }
```

{% endtab %}
{% tab swift %}

`````````swift
if inAppMessage is ABKInAppMessageImmersive {
      let immersiveIAM = inAppMessage as! ABKInAppMessageImmersive;
      for button in inAppMessage.buttons as! [ABKInAppMessageButton]{
        // Button action type is accessible via button.buttonClickActionType
      }
    }
```

{% endtab %}
{% endtabs %}

アプリ内メッセージにボタンがある場合、実行されるクリックアクションは `ABKInAppMessageButton` モデルのクリックアクションのみです。`ABKInAppMessage` モデルにデフォルトのクリックアクションが割り当てられている場合でも、アプリ内メッセージ本文はクリックできません。

## メソッドの宣言 {#method-declarations}

詳細については、次のヘッダーファイルを参照してください。

- [`ABKInAppMessage.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/ABKInAppMessage.h)