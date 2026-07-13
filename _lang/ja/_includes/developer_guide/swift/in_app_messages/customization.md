{% multi_lang_include developer_guide/prerequisites/swift.md %}

## UIデリゲートの設定（必須） {#setting-up-the-ui-delegate-required}

アプリ内メッセージの表示をカスタマイズし、さまざまなライフサイクルイベントに対応するには、[`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate)を設定する必要があります。これは、トリガーされたアプリ内メッセージのペイロードを受信・処理し、表示ライフサイクルイベントを受信し、表示タイミングをコントロールするために使用されるデリゲートプロトコルです。`BrazeInAppMessageUIDelegate`を使用するには、以下を行う必要があります。
- デフォルトの[`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui)実装を`inAppMessagePresenter`として使用します。
- `BrazeUI`ライブラリーをプロジェクトに含めます。

### ステップ1:`BrazeInAppMessageUIDelegate`プロトコルを実装する {#step-1-implement-the-brazeinappmessageuidelegate-protocol}

まず、`BrazeInAppMessageUIDelegate`プロトコルと、対応する必要なメソッドを実装します。以下の例では、このプロトコルをアプリケーションの`AppDelegate`クラスに実装しています。

{% tabs %}
{% tab swift %}
```swift
extension AppDelegate: BrazeInAppMessageUIDelegate {
  // Implement your protocol methods here.
}
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
@interface AppDelegate () <BrazeInAppMessageUIDelegate>

@end

@implementation AppDelegate
  // Implement your protocol methods here.
@end
```
{% endtab %}
{% endtabs %}

### ステップ2:`delegate`オブジェクトを割り当てる {#step-2-assign-the-delegate-object}

このアプリ内メッセージUIを`inAppMessagePresenter`として割り当てる前に、`BrazeInAppMessageUI`インスタンスの`delegate`オブジェクトを割り当てます。

{% tabs %}
{% tab swift %}
```swift
let inAppMessageUI = BrazeInAppMessageUI()
inAppMessageUI.delegate = self
AppDelegate.braze?.inAppMessagePresenter = inAppMessageUI
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
BrazeInAppMessageUI *inAppMessageUI = [[BrazeInAppMessageUI alloc] init];
inAppMessageUI.delegate = self;
AppDelegate.braze.inAppMessagePresenter = inAppMessageUI;
```

{% alert important %}
パラメーターが言語ランタイムと互換性がないため、すべてのデリゲートメソッドをObjective-Cで使用できるわけではありません。
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
アプリ内メッセージUIデリゲートの段階的な実装については、この[チュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui)を参照してください。
{% endalert %}

## クリック時の動作 {#on-click-behavior}

各`Braze.InAppMessage`オブジェクトには対応する[`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/clickaction)が含まれ、クリック時の動作が定義されます。

### クリックアクションのタイプ {#click-action-types}

`Braze.InAppMessage`の`clickAction`プロパティはデフォルトで`.none`に設定されていますが、次のいずれかの値に設定できます。

| `ClickAction` | クリック時の動作 |
| -------------------------- | -------- |
| `.url(URL, useWebView: Bool)` | 指定されたURLを外部ブラウザで開きます。`useWebView`が`true`に設定されている場合、Webビューで開きます。 |
| `.none` | クリックするとメッセージが閉じられます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="クリックアクションのタイプ" }

{% alert important %}
ボタンを含むアプリ内メッセージの場合、ボタンテキストを追加する前にクリックアクションが追加されると、メッセージの`clickAction`も最終ペイロードに含まれます。
{% endalert %}

### クリック時の動作をカスタマイズする {#customizing-on-click-behavior}

この動作をカスタマイズするには、以下のサンプルを参照して`clickAction`プロパティを変更できます。

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  if let newUrl = URL(string: "{your-url}") {
    context.message.clickAction = .url(newUrl, useWebView: true)
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

`inAppMessage(_:prepareWith:)`メソッドはObjective-Cでは利用できません。

{% endtab %}
{% endtabs %}

### カスタム動作の処理 {#handling-the-custom-behavior}

ユーザーがアプリ内メッセージをクリックした際に、以下の[`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate)デリゲートメソッドが呼び出されます。このコールバックは、アプリ内メッセージボタンやHTMLアプリ内メッセージボタン（リンク）に対するユーザーによるクリックでトリガーされ、これらの操作に対してはオプションのパラメーターとしてボタンIDが提供されます。このコールバックは、`brazeBridge.logClick()`によってトリガーされたプログラムによるクリックでは呼び出されません。

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  shouldProcess clickAction: Braze.InAppMessage.ClickAction,
  buttonId: String?,
  message: Braze.InAppMessage,
  view: InAppMessageView
) -> Bool
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view;
```

{% endtab %}
{% endtabs %}

このメソッドは、Brazeがクリックアクションの実行を続行するかどうかを示すブール値を返します。

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI, shouldProcess clickAction: Braze.InAppMessage.ClickAction,
  buttonId: String?, message: Braze.InAppMessage, view: InAppMessageView
) -> Bool {
    guard let buttonId,
      let idInt = Int(buttonId)
    else { return true }
    var button: BrazeKit.Braze.InAppMessage.Button? = nil

    switch message {
    case .modal(let modal):
      button = modal.buttons[idInt]

    case .modalImage(let modalImage):
      button = modalImage.buttons[idInt]

    case .full(let full):
      button = full.buttons[idInt]

    case .fullImage(let fullImage):
      button = fullImage.buttons[idInt]

    default:
      break
    }

    print(button?.id)
    print(button?.text)
    print(button?.clickAction)

    return true
  }
```

{% endtab %}
{% tab OBJECTIVE-C %}
```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view {
  NSInteger buttonInt = [buttonId integerValue];

  if (message.type == BRZInAppMessageRawTypeFull || message.type == BRZInAppMessageRawTypeModal) {
    BRZInAppMessageRawButton *button = message.buttons[buttonInt];
    NSLog(@"%ld", (long)button.identifier);
    NSLog(@"%@", button.text);
    NSLog(@"%ld", (long)button.clickAction);
  }
  return YES;
}
```

{% endtab %}
{% endtabs %}

## スワイプでスライドアップメッセージを閉じる {#swiping-to-dismiss-slideup-messages}

デフォルトでは、スライドアップのアプリ内メッセージはスワイプ操作で閉じることができます。スワイプの方向はスライドアップの位置によって決まります。

- **左または右にスワイプ：** 位置に関係なくスライドアップを閉じます。
- **下からのスライドアップ：** 上から下にスワイプするとメッセージが閉じられます。下から上にスワイプしても閉じられません。
- **上からのスライドアップ：** 下から上にスワイプするとメッセージが閉じられます。上から下にスワイプしても閉じられません。

このスワイプ動作はデフォルトの`BrazeInAppMessageUI` [`SlideupView`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/slideupview)に組み込まれており、スライドアップのアプリ内メッセージにのみ適用されます。モーダルおよびフルのアプリ内メッセージはスワイプによる閉じ操作をサポートしていません。スワイプ動作を含むスライドアップビューをさらにカスタマイズするには、[`SlideupView.Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/slideupview/attributes-swift.struct)を変更するか、サブクラス化によってカスタムビューを提供できます。

{% alert note %}
スライドアップメッセージの外側をタップしても、メッセージは閉じられません。モーダルまたはフルのアプリ内メッセージについては、以下のセクションで説明する`dismissOnBackgroundTap`属性を使用して、外側タップによる閉じ操作を有効にできます。
{% endalert %}

## モーダルの閉じ方をカスタマイズする {#customizing-modal-dismissals}

外側タップによる閉じ操作を有効にするには、カスタマイズするアプリ内メッセージタイプの`Attributes`構造体で`dismissOnBackgroundTap`プロパティを変更できます。

たとえば、モーダル画像のアプリ内メッセージに対してこの機能を有効にする場合は、以下を設定します。

{% tabs %}
{% tab swift %}

```swift
BrazeInAppMessageUI.ModalImageView.Attributes.defaults.dismissOnBackgroundTap = true
```

{% endtab %}
{% tab OBJECTIVE-C %}

`Attributes`によるカスタマイズはObjective-Cでは使用できません。

{% endtab %}
{% endtabs %}

デフォルト値は`false`です。これにより、ユーザーがアプリ内メッセージの外側をタップしたときにモーダルアプリ内メッセージが閉じられるかどうかが決まります。

| `DismissModalOnOutsideTap` | 説明 |
|----------|-------------|
| `true`         | モーダルアプリ内メッセージは外側タップで閉じられます。     |
| `false`        | デフォルト。モーダルアプリ内メッセージは外側タップでは閉じられません。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="モーダルの閉じ方のカスタマイズ" }

アプリ内メッセージのカスタマイズの詳細については、こちらの[記事](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization)を参照してください。

## メッセージの向きをカスタマイズする {#customizing-message-orientation}

アプリ内メッセージの向きをカスタマイズできます。すべてのメッセージに対して新しいデフォルトの向きを設定することも、単一のメッセージに対してカスタムの向きを設定することもできます。

{% tabs local %}
{% tab すべてのメッセージ %}
すべてのアプリ内メッセージのデフォルトの向きを選択するには、[`inAppMessage(_:prepareWith:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog)メソッドを使用して`PresentationContext`の`preferredOrientation`プロパティを設定します。

たとえば、縦向きをデフォルトの向きに設定するには：

{% subtabs %}
{% subtab swift %}
```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  context.preferredOrientation = .portrait
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  context.preferredOrientation = BRZInAppMessageRawOrientationPortrait;
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 単一のメッセージ %}
単一のメッセージの向きを設定するには、`Braze.InAppMessage`の`orientation`プロパティを変更します。

{% subtabs %}
{% subtab swift %}

```swift
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = .any

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = .portrait

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = .landscape
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = BRZInAppMessageRawOrientationAny;

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = BRZInAppMessageRawOrientationPortrait;

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = BRZInAppMessageRawOrientationLandscape;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

アプリ内メッセージが表示された後、メッセージが表示されている間にデバイスの向きが変わると、メッセージはデバイスの向きに合わせて回転します（メッセージの`orientation`設定でサポートされている場合に限ります）。

アプリ内メッセージが表示されるためには、デバイスの向きがメッセージの`orientation`プロパティによってサポートされている必要があります。また、`preferredOrientation`設定が適用されるのは、Xcodeのターゲット設定の**Deployment Info**セクションで、アプリケーションでサポートされているインターフェイスの向きにその向きが含まれている場合に限られます。

![Xcodeでサポートされている向き。]({% image_buster /assets/img/supported_interface_orientations_xcode.png %})

{% alert note %}
向きはメッセージの表示にのみ適用されます。デバイスの向きが変わると、メッセージビューはサポートされている向きのいずれかを採用します。小型のデバイス（iPhone、iPod Touch）では、モーダルまたはフルのアプリ内メッセージを横向きに設定すると、コンテンツが切り捨てられることがあります。
{% endalert %}

## 表示タイミングのカスタマイズ {#customizing-display-timing}

利用可能なアプリ内メッセージをユーザーエクスペリエンスの特定のポイントで表示するかどうかをコントロールできます。フルスクリーンゲーム中や読み込み画面など、アプリ内メッセージを表示させたくない状況がある場合は、保留中のアプリ内メッセージを遅延させるか破棄できます。アプリ内メッセージのタイミングをコントロールするには、`inAppMessage(_:displayChoiceForMessage:)` [デリゲートメソッド](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb)を使用して`BrazeInAppMessageUI.DisplayChoice`プロパティを設定します。

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  displayChoiceForMessage message: Braze.InAppMessage
) -> BrazeInAppMessageUI.DisplayChoice
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui displayChoiceForMessage:(BRZInAppMessageRaw *)message
```

{% endtab %}
{% endtabs %}

次のいずれかの値を返すよう`BrazeInAppMessageUI.DisplayChoice`を設定します。

| 表示の選択                      | 動作                                                                                                                    |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `.now`                              | メッセージはすぐに表示されます。これはデフォルト値です。                                                       |
| `.reenqueue`                        | メッセージは表示されず、スタックの一番上に戻されます。                                       |
| `.later`                            | メッセージは表示されず、スタックの一番上に戻されます。（非推奨。`.reenqueue`を使用してください） |
| `.discard`                          | メッセージは破棄され、表示されません。                                                                    |
{: .reset-td-br-1 .reset-td-br-2 aria-label="表示タイミングのカスタマイズ" }

{% alert tip %}
`InAppMessageUI`のサンプルについては、[Swift Braze SDKリポジトリ](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/InAppMessageUI)と[Objective-C](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/ObjC/Sources/InAppMessageUI)を確認してください。
{% endalert %}

## ステータスバーを非表示にする {#hiding-the-status-bar}

`Full`、`FullImage`、および`HTML`アプリ内メッセージについて、SDKではステータスバーがデフォルトで非表示になります。他の種類のアプリ内メッセージでは、ステータスバーは変更されません。この動作を設定するには、`inAppMessage(_:prepareWith:)` [デリゲートメソッド](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog)を使用して`PresentationContext`の`statusBarHideBehavior`プロパティを設定します。このフィールドの値は次のいずれかになります。

| ステータスバー非表示の動作            | 説明                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| `.auto`                             | メッセージビューがステータスバーの非表示状態を決定します。                                 |
| `.hidden`                           | ステータスバーを常に非表示にします。                                                           |
| `.visible`                          | ステータスバーを常に表示します。                                                        |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステータスバーの非表示" }

## ダークモードを無効にする {#disabling-dark-mode}

ユーザーデバイスでダークモードが有効になっているときにアプリ内メッセージでダークモードスタイルが採用されないようにするには、`inAppMessage(_:prepareWith:)` [デリゲートメソッド](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog)を実装します。メソッドに渡される`PresentationContext`には、表示される`InAppMessage`オブジェクトへの参照が含まれます。各`InAppMessage`には、`dark`と`light`のモードテーマを含む`themes`プロパティがあります。`themes.dark`プロパティを`nil`に設定すると、Brazeでは自動的にライトテーマを使用してアプリ内メッセージが表示されます。

ボタンがあるアプリ内メッセージタイプでは、`buttons`プロパティに追加の`themes`オブジェクトがあります。ボタンでダークモードスタイルが採用されないようにするには、[`map(_:)`](https://developer.apple.com/documentation/swift/array/map(_:)-87c4d)を使用して`dark`テーマがない`light`テーマのボタンの新しい配列を作成できます。

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  switch context.message {
    case .slideup:
      guard var slideup = context.message.slideup else { return }
      slideup.themes.dark = nil
      context.message.slideup = slideup

    case .modal:
      guard var modal = context.message.modal else { return }
      modal.themes.dark = nil
      modal.buttons = modal.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.modal = modal

    case .modalImage:
      guard var modalImage = context.message.modalImage else { return }
      modalImage.themes.dark = nil
      modalImage.buttons = modalImage.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.modalImage = modalImage

    case .full:
      guard var full = context.message.full else { return }
      full.themes.dark = nil
      full.buttons = full.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.full = full

    case .fullImage:
      guard var fullImage = context.message.fullImage else { return }
      fullImage.themes.dark = nil
      fullImage.buttons = fullImage.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.fullImage = fullImage

    default:
      break
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  switch (context.message.type) {
    case BRZInAppMessageRawTypeSlideup: {
      NSMutableDictionary *updatedThemes = [context.message.themes mutableCopy];
      [updatedThemes removeObjectForKey:@"dark"];
      context.message.themes = updatedThemes;
      break;
    }
    case BRZInAppMessageRawTypeModal:
    case BRZInAppMessageRawTypeFull:
    {
      NSMutableDictionary *updatedThemes = [context.message.themes mutableCopy];
      [updatedThemes removeObjectForKey:@"dark"];
      context.message.themes = updatedThemes;

      NSMutableArray *updatedButtons = [NSMutableArray arrayWithCapacity:context.message.buttons.count];
      for (BRZInAppMessageRawButton *button in context.message.buttons) {
        BRZInAppMessageRawButtonTheme *lightTheme = BRZInAppMessageRawButtonTheme.defaultLight;
        BRZInAppMessageRawButton *newButton = [button mutableCopy];
        newButton.textColor = lightTheme.textColor;
        newButton.backgroundColor = lightTheme.backgroundColor;
        newButton.borderColor = lightTheme.borderColor;
        [updatedButtons addObject:newButton];
      }
      context.message.buttons = updatedButtons;
      break;
    }
    default:
      break;
  }
}
```

{% endtab %}
{% endtabs %}

## App Storeレビュープロンプトをカスタマイズする {#customizing-the-app-store-review-prompt}

キャンペーンでアプリ内メッセージを使用して、ユーザーにApp Storeのレビューを依頼できます。

{% alert note %}
このプロンプトの例はBrazeのデフォルト動作をオーバーライドするため、実装するとインプレッションを自動的に追跡できません。[自身で分析データを記録する]({{site.baseurl}}/developer_guide/analytics)必要があります。
{% endalert %}

### ステップ1:アプリ内メッセージデリゲートを設定する {#step-1-set-the-in-app-message-delegate}

まず、アプリで[`BrazeInAppMessageUIDelegate`]({{site.baseurl}}/developer_guide/in_app_messages/customization#swift_setting-up-the-ui-delegate-required)を設定します。

### ステップ2:デフォルトのApp Storeレビューメッセージを無効にする {#step-2-disable-the-default-app-store-review-message}

次に、`inAppMessage(_:displayChoiceForMessage:)` [デリゲートメソッド](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb)を実装して、デフォルトのApp Storeレビューメッセージを無効にします。

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(_ ui: BrazeInAppMessageUI, displayChoiceForMessage message: Braze.InAppMessage) -> BrazeInAppMessageUI.DisplayChoice {
  if message.extras["AppStore Review"] != nil,
    let messageUrl = message.clickAction.url {
      UIApplication.shared.open(messageUrl, options: [:], completionHandler: nil)
      return .discard
  } else {
    return .now
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui
                            displayChoiceForMessage:(BRZInAppMessageRaw *)message {
  if (message.extras != nil && message.extras[@"AppStore Review"] != nil) {
    [[UIApplication sharedApplication] openURL:message.url options:@{} completionHandler:nil];
    return BRZInAppMessageUIDisplayChoiceDiscard;
  } else {
    return BRZInAppMessageUIDisplayChoiceNow;
  }
}
```

{% endtab %}
{% endtabs %}

### ステップ3:ディープリンクを作成する {#step-3-create-a-deep-link}

ディープリンク処理コードで、次のコードを追加して`{YOUR-APP-SCHEME}:app-store-review`ディープリンクを処理します。`SKStoreReviewController`を使用するには`StoreKit`をインポートする必要があることに注意してください。

{% tabs %}
{% tab swift %}

```swift
func application(_ app: UIApplication, open url: URL, options: [UIApplicationOpenURLOptionsKey : Any] = [:]) -> Bool {
  let urlString = url.absoluteString.removingPercentEncoding
  if (urlString == "{YOUR-APP-SCHEME}:app-store-review") {
    SKStoreReviewController.requestReview()
    return true;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)application:(UIApplication *)app openURL:(NSURL *)url options:(NSDictionary<UIApplicationOpenURLOptionsKey, id> *)options {
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  if ([urlString isEqualToString:@"{YOUR-APP-SCHEME}:app-store-review"]) {
    [SKStoreReviewController requestReview];
    return YES;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% endtabs %}

{% raw %}

### ステップ4:クリック時のカスタム動作を設定する {#step-4-set-custom-on-click-behavior}

次に、以下の内容でアプリ内メッセージングキャンペーンを作成します。

- キーと値のペア `"AppStore Review" : "true"`
- ディープリンク`{YOUR-APP-SCHEME}:app-store-review`を使用して、クリック時の動作を「アプリにディープリンクする」に設定します。

{% endraw %}

{% alert tip %}
AppleはApp Storeのレビュープロンプトをユーザーごとに年間最大3回に制限しているため、キャンペーンの[レート制限]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting)はユーザーごとに年間3回に設定する必要があります。<br><br>ユーザーはApp Storeのレビュープロンプトをオフにできます。そのため、カスタムレビュープロンプトでは、App Storeのネイティブレビュープロンプトが表示されることを約束したり、直接レビューを求めたりしないでください。
{% endalert %}