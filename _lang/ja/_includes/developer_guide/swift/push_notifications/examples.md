{% multi_lang_include developer_guide/prerequisites/swift.md %} また、[プッシュ通知の設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)も必要です。

{% alert note %}
この実装ガイドはSwiftの実装を中心としていますが、興味のある方のためにObjective-Cのスニペットも提供しています。
{% endalert %}

## 通知コンテンツアプリ拡張機能 {#notification-content-app-extensions}

![2つのプッシュメッセージが並んで表示されています。左のメッセージはデフォルトUIでのプッシュの表示例です。右のメッセージはカスタムプッシュUIを実装して作成されたコーヒーポイントカードのプッシュです。]({% image_buster /assets/img/push_implementation_guide/push1.png %}){: style="max-width:65%;border:0;margin-top:10px"}

通知コンテンツアプリ拡張機能は、プッシュ通知のカスタマイズに優れたオプションを提供します。通知コンテンツアプリ拡張機能は、プッシュ通知が展開されたときに、アプリの通知用のカスタムインターフェイスを表示します。

プッシュ通知は3つの方法で展開できます：
- プッシュバナーの長押し
- プッシュバナーを下にスワイプ
- バナーを横にスワイプして「表示」を選択

これらのカスタムビューは、インタラクティブな通知、ユーザーデータが入力された通知、さらには電話番号やメールなどの情報をキャプチャできるプッシュメッセージなど、さまざまな種類のコンテンツを表示することで、顧客をエンゲージするスマートな方法を提供します。Brazeのよく知られた機能の1つである[Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories)は、プッシュ通知コンテンツアプリ拡張機能の代表的な例です。

### 要件 {#requirements}

![Xcodeの「新しいターゲットのテンプレートを選択」画面で、Application Extensionの下にある「Notification Content Extension」が選択されています。]({% image_buster /assets/img/push_implementation_guide/push15.png %}){: style="float:right;max-width:50%;margin-left:10px; border:0;margin-top:10px"}
- [プッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)がアプリに正常に統合されていること
- コーディング言語に基づいてXcodeが生成する以下のファイル：

**Swift**<br>
- `NotificationViewController.swift`
- `MainInterface.storyboard`

**Objective-C**<br>
- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

## インタラクティブプッシュ通知 {#interactive-push-notification}

プッシュ通知は、コンテンツアプリエクステンション内でユーザーアクションに応答できます。iOS 12以降を使用しているユーザーの場合、プッシュ通知を完全にインタラクティブなメッセージに変えることができます。これは、プロモーションやアプリケーションにインタラクティビティを導入するための魅力的なオプションを提供します。例えば、プッシュ通知にユーザーがプレイできるゲーム、割引のためのスピントゥウィンホイール、リスティングや曲を保存するための「いいね」ボタンを含めることができます。

以下の例は、展開された通知内でユーザーがマッチゲームをプレイできるプッシュ通知を示しています。

![インタラクティブプッシュ通知のフェーズがどのように見えるかを示す図。ユーザーがプッシュ通知を押してインタラクティブなマッチングゲームを表示するシーケンス。]({% image_buster /assets/img/push_implementation_guide/push12.png %}){: style="border:0"}

### ダッシュボード設定 {#dashboard-configuration}

インタラクティブプッシュ通知を作成するには、ダッシュボードでカスタムビューを設定する必要があります。

1. **キャンペーン**ページから、**キャンペーンを作成**をクリックして新しいプッシュ通知キャンペーンを開始します。
2. **作成**タブで、**通知ボタン**をオンに切り替えます。
3. **iOS通知カテゴリ**フィールドにカスタムiOSカテゴリを入力します。
4. Notification Content Extension Targetの`.plist`で、`UNNotificationExtensionCategory`属性をカスタムiOSカテゴリに設定します。ここで指定する値は、Brazeダッシュボードの**iOS通知カテゴリ**で設定されている値と一致する必要があります。
5. `UNNotificationExtensionInteractionEnabled`キーを`true`に設定して、プッシュ通知でのユーザーインタラクションを有効にします。

![プッシュメッセージ作成画面の設定にある通知ボタンのオプション。]({% image_buster /assets/img/push_implementation_guide/push16.png %}){: style="max-width:75%;border:0;margin-top:10px"}
![UNNotificationExtensionCategoryが「your_custom_category」に設定され、UNNotificationExtensionDefaultContentHiddenが1に設定され、UNNotificationExtensionInitialContentSizeRatioが1に設定されたNSExtensionを示すplist。]({% image_buster /assets/img/push_implementation_guide/push17.png %}){: style="max-width:75%;border:0;margin-top:10px"}

## パーソナライズされたプッシュ通知 {#personalized-push-notifications}

![2台のiPhoneが並べて表示されています。1台目のiPhoneにはプッシュメッセージの展開前のビューが表示されています。2台目のiPhoneにはプッシュメッセージの展開後のバージョンが表示され、コースの進捗状況、次のセッション名、次のセッションの完了期限が表示されています。]({% image_buster /assets/img/push_implementation_guide/push6.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

プッシュ通知は、コンテンツエクステンション内にユーザー固有の情報を表示できます。これにより、異なるプラットフォーム間で進捗を共有するオプションの追加、解除されたアチーブメントの表示、オンボーディングチェックリストの表示など、ユーザーに焦点を当てたプッシュコンテンツを作成できます。この例では、ユーザーがBraze Learningコースで特定のタスクを完了した後に表示されるプッシュ通知を示しています。通知を展開すると、ユーザーは学習パスの進捗状況を確認できます。ここで提供される情報はユーザー固有であり、セッションが完了したとき、または特定のユーザーアクションが実行されたときに、APIトリガーを活用して送信できます。

### ダッシュボードの設定

パーソナライズされたプッシュ通知を作成するには、ダッシュボードでカスタムビューを設定する必要があります。

1. **キャンペーン**ページから、**キャンペーンを作成**をクリックして新しいプッシュ通知キャンペーンを開始します。
2. **作成**タブで、**通知ボタン**をオンに切り替えます。
3. **iOS通知カテゴリ**フィールドにカスタムiOSカテゴリを入力します。
4. **設定**タブで、標準のLiquidを使用してキーと値のペアを作成します。メッセージに表示したい適切なユーザー属性を設定します。これらのビューは、特定のユーザープロファイルの特定のユーザー属性に基づいてパーソナライズできます。
5. Notification Content Extension Targetの`.plist`で、`UNNotificationExtensionCategory`属性をカスタムiOSカテゴリに設定します。ここで指定する値は、Brazeダッシュボードの**iOS通知カテゴリ**で設定したものと一致する必要があります。

![4組のキーと値のペア。「next_session_name」と「next_session_complete_date」はLiquidを使用してAPIトリガープロパティとして設定され、「completed_session count」と「total_session_count」はLiquidを使用してカスタムユーザー属性として設定されています。]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

### キーと値のペアの処理 {#handling-key-value-pairs}

`didReceive`メソッドは、通知コンテンツアプリエクステンションが通知を受信したときに呼び出されます。このメソッドは`NotificationViewController`内にあります。ダッシュボードで設定されたキーと値のペアは、`userInfo`ディクショナリを使用してコード内で表現されます。

#### プッシュ通知からのキーと値のペアの解析 {#parsing-key-value-pairs-from-push-notifications}

{% tabs %}
{% tab Swift %}
``` swift
func didReceive(_ notification: UNNotification) {
  let userInfo = notification.request.content.userInfo

  guard let value = userInfo["YOUR-KEY-VALUE-PAIR"] as? String,
        let otherValue = userInfo["YOUR-OTHER-KEY-VALUE-PAIR"] as? String,
  else { fatalError("Key-Value Pairs are incorrect.")}

  ...
}
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)didReceiveNotification:(nonnull UNNotification *)notification {
  NSDictionary *userInfo = notification.request.content.userInfo;

  if (userInfo[@"YOUR-KEY-VALUE-PAIR"] && userInfo[@"YOUR-OTHER-KEY-VALUE-PAIR"]) {

  ...

  } else {
    [NSException raise:NSGenericException format:@"Key-Value Pairs are incorrect"];
  }
}
```
{% endtab %}
{% endtabs %}

## 情報キャプチャプッシュ通知 {#information-capture-push-notification}

プッシュ通知は、コンテンツアプリ拡張機能内でユーザー情報をキャプチャでき、プッシュで可能なことの限界を広げます。プッシュ通知を通じてユーザー入力を求めることで、名前やメールなどの基本情報を要求するだけでなく、ユーザーにフィードバックの送信や未完了のユーザープロファイルの入力を促すこともできます。

{% alert tip %}
詳細については、[プッシュ通知データのロギング]({{site.baseurl}}/developer_guide/analytics/logging_channel_data/push_notifications)を参照してください。
{% endalert %}

次のフローでは、カスタムビューが状態変化に応答できます。それらの状態変化コンポーネントは各画像に示されています。

1. ユーザーがプッシュ通知を受信します。
2. プッシュが開かれます。展開後、プッシュはユーザーに情報を求めます。この例では、ユーザーのメールアドレスが要求されていますが、任意の種類の情報を要求できます。
3. 情報が提供され、期待される形式であれば登録ボタンが表示されます。
3. 確認ビューが表示され、プッシュが閉じられます。


### ダッシュボード設定

情報キャプチャプッシュ通知を作成するには、ダッシュボードでカスタムビューを設定する必要があります。

1. **キャンペーン**ページで、**キャンペーンを作成**をクリックして新しいプッシュ通知キャンペーンを開始します。
2. **作成**タブで、**通知ボタン**をオンに切り替えます。
3. **iOS通知カテゴリ**フィールドにカスタムiOSカテゴリを入力します。
4. **設定**タブで、標準のLiquidを使用してキーと値のペアを作成します。メッセージに表示させたい適切なユーザー属性を設定します。
5. Notification Content Extension Targetの`.plist`で、`UNNotificationExtensionCategory`属性をカスタムiOSカテゴリに設定します。ここで指定する値は、Brazeダッシュボードの**iOS通知カテゴリ**で設定されているものと一致する必要があります。

例に示されているように、プッシュ通知に画像を含めることもできます。これを行うには、[リッチプッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift)を統合し、キャンペーンの通知スタイルをリッチプッシュ通知に設定し、リッチプッシュ画像を含めます。

![3組のキーと値のペアを含むプッシュメッセージ。1.「Braze_id」がBraze IDを取得するLiquid呼び出しとして設定。2.「cert_title」が「Braze Marketer Certification」に設定。3.「Cert_description」が「Certified Braze marketers drive...」に設定。]({% image_buster /assets/img/push_implementation_guide/push9.png %})

### ボタンアクションの処理 {#handling-button-actions}

各アクションボタンは一意に識別されます。コードは、レスポンス識別子が`actionIdentifier`と等しいかどうかを確認し、等しい場合はユーザーがアクションボタンをクリックしたことを認識します。

**プッシュ通知アクションボタンレスポンスの処理**<br>

{% tabs %}
{% tab Swift %}
``` swift
func didReceive(_ response: UNNotificationResponse, completionHandler completion: @escaping (UNNotificationContentExtensionResponseOption) -> Void) {
  if response.actionIdentifier == "YOUR-REGISTER-IDENTIFIER" {
    // do something
  } else {
    // do something else
  }
}
```
{% endtab %}
{% tab Objective-C %}
```objc
- (void)didReceiveNotificationResponse:(UNNotificationResponse *)response completionHandler:(void (^)(UNNotificationContentExtensionResponseOption))completion {
  if ([response.actionIdentifier isEqualToString:@"YOUR-REGISTER-IDENTIFIER"]) {
    completion(UNNotificationContentExtensionResponseOptionDismiss);
  } else {
    completion(UNNotificationContentExtensionResponseOptionDoNotDismiss);
  }
}
```
{% endtab %}
{% endtabs %}

### プッシュの閉じ方 {#dismissing-pushes}

プッシュ通知は、アクションボタンの押下により自動的に閉じることができます。推奨される3つのプッシュ閉じオプションがあります。

1. `completion(.dismiss)` - 通知を閉じます
2. `completion(.doNotDismiss)` - 通知は開いたままになります
3. `completion(.dismissAndForward)` - プッシュが閉じられ、ユーザーがアプリケーションに転送されます