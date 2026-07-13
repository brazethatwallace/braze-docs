{% multi_lang_include developer_guide/prerequisites/swift.md %} また、[プッシュ通知の設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)も必要です。

{% alert note %}
この実装ガイドはSwiftの実装を中心としていますが、興味のある方のためにObjective-Cのスニペットも提供しています。
{% endalert %}

## 通知コンテンツアプリ拡張機能 {#notification-content-app-extensions}

![並んで表示される2つのプッシュメッセージ。左側のメッセージはデフォルトのUIでのプッシュの見た目を示しています。右側のメッセージはカスタムプッシュUIを実装して作成したコーヒーパンチカードプッシュを表示しています。]({% image_buster /assets/img/push_implementation_guide/push1.png %}){: style="max-width:65%;border:0;margin-top:10px"}

通知コンテンツアプリ拡張機能は、プッシュ通知のカスタマイズに最適なオプションを提供します。プッシュ通知を展開すると、通知コンテンツアプリ拡張機能によって、アプリの通知のカスタムインターフェイスが表示されます。

プッシュ通知は、次の3つの方法で展開できます。
- プッシュバナーを長押しする
- プッシュバナーを下にスワイプする
- バナーを左にスワイプして「表示」を選択する

これらのカスタムビューでは、インタラクティブな通知、ユーザーデータを含む通知、電話番号やメールなどの情報を取得できるプッシュメッセージなど、さまざまな種類のコンテンツを表示して顧客をエンゲージするスマートな方法を提供します。Brazeでよく知られている機能の1つである[Push Stories]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories)は、プッシュ通知コンテンツアプリ拡張機能がどのようなものかを示す代表的な例です。

### 要件 {#requirements}

![Xcodeの「新しいターゲットのテンプレートを選択」画面で、Application Extensionの下にある「Notification Content Extension」が選択されています。]({% image_buster /assets/img/push_implementation_guide/push15.png %}){: style="float:right;max-width:50%;margin-left:10px; border:0;margin-top:10px"}
- [プッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)がアプリに正常に統合されていること
- コーディング言語に基づいてXcodeによって生成される以下のファイル:

**Swift**<br>
- `NotificationViewController.swift`
- `MainInterface.storyboard`

**Objective-C**<br>
- `NotificationViewController.h`
- `NotificationViewController.m`
- `MainInterface.storyboard`

## インタラクティブなプッシュ通知 {#interactive-push-notification}

プッシュ通知は、コンテンツアプリ拡張機能内でユーザーのアクションに応答できます。iOS 12以降を使用しているユーザーの場合、プッシュ通知を完全にインタラクティブなメッセージに変えることができます。これにより、プロモーションやアプリケーションにインタラクティビティを導入するエキサイティングなオプションが提供されます。例えば、プッシュ通知にユーザーがプレイできるゲーム、割引のためのスピン・トゥ・ウィンホイール、リストや曲を保存するための「いいね」ボタンなどを含めることができます。

次の例は、ユーザーが展開された通知内でマッチゲームをプレイできるプッシュ通知を示しています。

![インタラクティブなプッシュ通知のフェーズがどのように見えるかを示す図。シーケンスは、ユーザーがインタラクティブなマッチングゲームを表示するプッシュ通知を押す様子を示しています。]({% image_buster /assets/img/push_implementation_guide/push12.png %}){: style="border:0"}

### ダッシュボードの設定 {#dashboard-configuration}

インタラクティブなプッシュ通知を作成するには、ダッシュボードにカスタムビューを設定する必要があります。

1. **キャンペーン**ページから、**キャンペーンを作成**をクリックして新しいプッシュ通知キャンペーンを開始します。
2. **作成**タブで、**通知ボタン**をオンに切り替えます。
3. **iOS Notification Category**フィールドにカスタムiOSカテゴリを入力します。
4. 通知コンテンツ拡張ターゲットの`.plist`で、`UNNotificationExtensionCategory`属性をカスタムiOSカテゴリに設定します。ここに指定する値は、Brazeダッシュボードの**iOS Notification Category**で設定されているものと一致する必要があります。
5. `UNNotificationExtensionInteractionEnabled`キーを`true`に設定して、プッシュ通知でのユーザー操作を有効にします。

![プッシュメッセージ作成画面の設定にある通知ボタンオプション。]({% image_buster /assets/img/push_implementation_guide/push16.png %}){: style="max-width:75%;border:0;margin-top:10px"}
![UNNotificationExtensionCategoryが「your_custom_category」に設定され、UNNotificationExtensionDefaultContentHiddenが1に設定され、UNNotificationExtensionInitialContentSizeRatioが1に設定されたNSExtensionを含むplist。]({% image_buster /assets/img/push_implementation_guide/push17.png %}){: style="max-width:75%;border:0;margin-top:10px"}

## パーソナライズされたプッシュ通知 {#personalized-push-notifications}

![2台のiPhoneが並んで表示されています。1台目のiPhoneにはプッシュメッセージの展開前のビューが表示されています。2台目のiPhoneにはプッシュメッセージの展開バージョンが表示され、コースの進捗状況、次のセッション名、次のセッションの完了期限が表示されています。]({% image_buster /assets/img/push_implementation_guide/push6.png %}){: style="float:right;max-width:40%;margin-left:15px;border:0"}

プッシュ通知では、コンテンツ拡張機能内にユーザー固有の情報を表示できます。これにより、さまざまなプラットフォームで進捗を共有するオプションの追加、アンロックされた実績の表示、オンボーディングチェックリストの表示など、ユーザー中心のプッシュコンテンツを作成できます。この例は、ユーザーがBraze Learningコースで特定のタスクを完了した後に表示されるプッシュ通知を示しています。通知を展開することで、ユーザーは学習パスの進捗を確認できます。ここで提供される情報はユーザー固有であり、セッションが完了するか、APIトリガーを利用して特定のユーザーアクションが実行されたときに発火させることができます。

### ダッシュボードの設定

パーソナライズされたプッシュ通知を作成するには、ダッシュボードにカスタムビューを設定する必要があります。

1. **キャンペーン**ページから、**キャンペーンを作成**をクリックして新しいプッシュ通知キャンペーンを開始します。
2. **作成**タブで、**通知ボタン**をオンに切り替えます。
3. **iOS Notification Category**フィールドにカスタムiOSカテゴリを入力します。
4. **設定**タブで、標準のLiquidを使用してキーと値のペアを作成します。メッセージに表示したい適切なユーザー属性を設定します。これらのビューは、特定のユーザープロファイルの特定のユーザー属性に基づいてパーソナライズできます。
5. 通知コンテンツ拡張ターゲットの`.plist`で、`UNNotificationExtensionCategory`属性をカスタムiOSカテゴリに設定します。ここに指定する値は、Brazeダッシュボードの**iOS Notification Category**で設定されているものと一致する必要があります。

![Liquidを使用してAPIトリガープロパティとして「next_session_name」と「next_session_complete_date」が設定され、Liquidを使用してカスタムユーザー属性として「completed_session count」と「total_session_count」が設定された4組のキーと値のペア。]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

### キーと値のペアの処理 {#handling-key-value-pairs}

メソッド`didReceive`は、通知コンテンツアプリ拡張機能が通知を受信したときに呼び出されます。このメソッドは`NotificationViewController`内にあります。ダッシュボードで提供されるキーと値のペアは、`userInfo`辞書を使用してコード内で表現されます。

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

## 情報取得プッシュ通知 {#information-capture-push-notification}

プッシュ通知は、コンテンツアプリ拡張機能内でユーザー情報をキャプチャし、プッシュで可能なことの限界を押し広げます。プッシュ通知を通じてユーザー入力をリクエストすることで、名前やメールなどの基本的な情報をリクエストできるだけでなく、フィードバックの送信や未完成のユーザープロファイルの完成をユーザーに促すこともできます。

{% alert tip %}
詳細については、[プッシュ通知データのログ記録]({{site.baseurl}}/developer_guide/analytics/logging_channel_data/push_notifications)を参照してください。
{% endalert %}

次のフローでは、カスタムビューは状態の変化に応答できます。これらの状態変更コンポーネントは、各画像に表示されています。

1. ユーザーがプッシュ通知を受信します。
2. プッシュが開封されます。展開後、プッシュはユーザーに情報を求めます。この例では、ユーザーのメールアドレスがリクエストされますが、任意の種類の情報をリクエストすることもできます。
3. 情報が提供され、期待される形式であれば、登録ボタンが表示されます。
3. 確認ビューが表示され、プッシュが閉じられます。


### ダッシュボードの設定

情報取得プッシュ通知を作成するには、ダッシュボードにカスタムビューを設定する必要があります。

1. **キャンペーン**ページから、**キャンペーンを作成**をクリックして新しいプッシュ通知キャンペーンを開始します。
2. **作成**タブで、**通知ボタン**をオンに切り替えます。
3. **iOS Notification Category**フィールドにカスタムiOSカテゴリを入力します。
4. **設定**タブで、標準のLiquidを使用してキーと値のペアを作成します。メッセージに表示したい適切なユーザー属性を設定します。
5. 通知コンテンツ拡張ターゲットの`.plist`で、`UNNotificationExtensionCategory`属性をカスタムiOSカテゴリに設定します。ここに指定する値は、Brazeダッシュボードの**iOS Notification Category**で設定されているものと一致する必要があります。

例に見られるように、プッシュ通知に画像を含めることもできます。これを行うには、[リッチプッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift)を統合し、キャンペーンの通知スタイルをリッチプッシュ通知に設定し、リッチプッシュ画像を含める必要があります。

![キーと値のペアが3セットあるプッシュメッセージ。1.「Braze_id」はBraze IDを取得するためのLiquidコールとして設定。2.「cert_title」は「Braze Marketer Certification」として設定。3.「Cert_description」は「Certified Braze marketers drive...」として設定。]({% image_buster /assets/img/push_implementation_guide/push9.png %})

### ボタンアクションの処理 {#handling-button-actions}

各アクションボタンは一意に識別されます。コードは、応答識別子が`actionIdentifier`と等しいかどうかをチェックし、等しい場合はユーザーがアクションボタンをクリックしたことを認識します。

**プッシュ通知アクションボタンの応答の処理**<br>

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

プッシュ通知は、アクションボタンを押すと自動的に閉じることができます。推奨される組み込みのプッシュ閉じオプションは3つあります。

1. `completion(.dismiss)` - 通知を閉じます
2. `completion(.doNotDismiss)` - 通知は開いたままになります
3. `completion(.dismissAndForward)` - プッシュが閉じられ、ユーザーがアプリケーションに転送されます