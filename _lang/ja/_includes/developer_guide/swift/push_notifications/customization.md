{% multi_lang_include developer_guide/prerequisites/swift.md %} また、[プッシュ通知の設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)も必要です。

## アクションボタンのカスタマイズ {#push-action-buttons-integration}

Braze Swift SDKでは、プッシュアクションボタン用のURL処理がサポートされています。Brazeのデフォルトプッシュカテゴリには、`Accept/Decline`、`Yes/No`、`Confirm/Cancel`、`More`の4セットのデフォルトプッシュアクションボタンがあります。

![2つのカスタマイズ可能なアクションボタンを表示するためにプルダウンされているプッシュメッセージのGIF。]({% image_buster /assets/img_archive/iOS8Action.gif %}){: style="max-width:60%"}

### アクションボタンを手動で登録する {#manually-registering-action-buttons}

{% alert important %}
プッシュアクションボタンの手動登録は推奨されません。
{% endalert %}

`configuration.push.automation`設定オプションを使用して[プッシュ通知を設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)した場合、Brazeはデフォルトのプッシュカテゴリ用のアクションボタンを自動的に登録し、プッシュアクションボタンのクリック分析とURLルーティングを処理します。

ただし、代わりに手動でプッシュアクションボタンを登録することもできます。

#### ステップ1:Brazeデフォルトプッシュカテゴリの追加 {#registering}

[プッシュ登録]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-4-register-push-tokens-with-braze)時にデフォルトのプッシュカテゴリに登録するには、次のコードを使用します。

{% tabs %}
{% tab swift %}
a
```swift
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[[UNUserNotificationCenter currentNotificationCenter] setNotificationCategories:BRZNotifications.categories];
```

{% endtab %}
{% endtabs %}

{% alert note %}
バックグラウンドアクティベーションモードでプッシュアクションボタンをクリックすると、通知が閉じられるだけで、アプリは開きません。ユーザーが次回アプリを開くと、これらのアクションのボタンクリック分析がサーバーにフラッシュされます。
{% endalert %}

#### ステップ2:インタラクティブなプッシュ処理を有効にする {#enable-push-handling}

クリック分析やURLルーティングを含むプッシュアクションボタンの処理を有効にするには、アプリの`didReceive(_:completionHandler:)`デリゲートメソッドに次のコードを追加します。

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.notifications.handleUserNotification(response: response, withCompletionHandler: completionHandler)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
[AppDelegate.braze.notifications handleUserNotificationWithResponse:response
                                              withCompletionHandler:completionHandler];
```

{% endtab %}
{% endtabs %}

`UNNotification`フレームワークを使用し、Brazeの[通知メソッド]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-5-enable-push-handling)を実装している場合、このメソッドはすでに統合されているはずです。

## プッシュカテゴリのカスタマイズ {#customizing-push-categories}

Brazeはデフォルトのプッシュカテゴリのセットを提供するだけでなく、カスタムの通知カテゴリとアクションもサポートしています。アプリケーションにカテゴリを登録すると、Brazeダッシュボードを使用してこれらのカスタム通知カテゴリをユーザーに送信できます。

デバイスに表示される`LIKE_CATEGORY`を活用する例を次に示します。

![「unlike」と「like」の2つのプッシュアクションボタンを表示するプッシュメッセージ。]({% image_buster /assets/img_archive/push_example_category.png %})

### ステップ1:カテゴリを登録する {#step-1-register-a-category}

アプリにカテゴリを登録するには、以下のような方法を使用します。

{% tabs %}
{% tab swift %}

```swift
Braze.Notifications.categories.insert(
  .init(identifier: "LIKE_CATEGORY",
        actions: [
          .init(identifier: "LIKE_IDENTIFIER", title: "Like", options: [.foreground]),
          .init(identifier: "UNLIKE_IDENTIFIER", title: "Unlike", options: [.foreground])
        ],
        intentIdentifiers: []
       )
)
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
NSMutableSet<UNNotificationCategory *> *categories = [BRZNotifications.categories mutableCopy];

UNNotificationAction *likeAction = [UNNotificationAction actionWithIdentifier:@"LIKE_IDENTIFIER"
                                                                        title:@"Like"
                                                                      options:UNNotificationActionOptionForeground];

UNNotificationAction *unlikeAction = [UNNotificationAction actionWithIdentifier:@"UNLIKE_IDENTIFIER"
                                                                          title:@"Unlike"
                                                                        options:UNNotificationActionOptionForeground];

UNNotificationCategory *likeCategory = [UNNotificationCategory categoryWithIdentifier:@"LIKE_CATEGORY"
                                                                              actions:@[likeAction, unlikeAction]
                                                                    intentIdentifiers:@[]
                                                                              options:UNNotificationCategoryOptionNone];

[categories addObject:likeCategory];
[UNUserNotificationCenter.currentNotificationCenter setNotificationCategories:categories];
```

{% endtab %}
{% endtabs %}

{% alert note %}
`UNNotificationAction`を作成するときに、アクションオプションのリストを指定できます。例えば、`.foreground`を使用すると、アクションボタンをタップした後にユーザーがアプリを開けるようになります。これは、「アプリを開く」や「アプリケーションにディープリンクする」などのナビゲーションクリック時の動作に必要です。アプリを開かずに通知を閉じるだけのアクションボタンが必要な場合は、アクションの`options`配列から`.foreground`を除外してください。詳細については、[`UNNotificationActionOptions`](https://developer.apple.com/documentation/usernotifications/unnotificationactionoptions)を参照してください。
{% endalert %}

### ステップ2:カテゴリを選択する {#step-2-select-your-categories}

カテゴリを登録したら、Brazeダッシュボードを使用して、そのタイプの通知をユーザーに送信します。

{% alert tip %}
アプリへのディープリンクやWeb URLへのリダイレクトなど、Swiftコードでローカルに作成できない動作についてのみ、Brazeダッシュボード上でアクションボタンを定義する必要があります。これらのアクションはダッシュボードで設定する必要があり、そうすることでどのURLやディープリンクを開くかを定義できます。アプリを開かずに通知を閉じるだけのアクションボタンについては、ダッシュボードで設定する必要はありません。通知の閉じ動作はiOSが自動的に処理します。アプリコードでカスタムカテゴリとそのアクションを登録し、ダッシュボードで対応するカテゴリ名を入力するだけです。
{% endalert %}

1. Brazeダッシュボードで、**メッセージング** > **プッシュ通知**を選択し、iOSの[プッシュキャンペーン]({{site.baseurl}}/user_guide/channels/push/create_a_push_message)を選択します。
2. **プッシュ通知を作成する**の下で、**アクションボタン**をオンにします。
3. **iOS通知カテゴリ**ドロップダウンで、**事前登録されたカスタムiOSカテゴリを入力**を選択します。
4. 最後に、前に作成したカテゴリのいずれかを入力します。次の例では、カスタムカテゴリ`LIKE_CATEGORY`を使用します。

![カスタムカテゴリの設定を含むプッシュ通知キャンペーンダッシュボード。]({% image_buster /assets/img_archive/ios-notification-category.png %})

### 例:カスタムプッシュカテゴリ {#example-custom-push-category}

2つのアクションボタンを持つプッシュ通知を作成したいとします。アプリにディープリンクする**Manage**と、通知を閉じるだけの**Keep**です。

次の例では、`MANAGE_IDENTIFIER`アクションに`.foreground`オプションが含まれており、タップするとアプリが開きます。これは、アプリの特定の部分にディープリンクするために必要です。`KEEP_IDENTIFIER`アクションは空のオプション配列を使用しており、アプリを開かずに通知を閉じます。

{% tabs %}
{% tab swift %}

```swift
Braze.Notifications.categories.insert(
  .init(identifier: "YOUR_CATEGORY",
        actions: [
          .init(identifier: "KEEP_IDENTIFIER", title: "Keep", options: []),
          .init(identifier: "MANAGE_IDENTIFIER", title: "Manage", options: [.foreground])
        ],
        intentIdentifiers: []
       )
)
UNUserNotificationCenter.current().setNotificationCategories(Braze.Notifications.categories)
```

{% endtab %}
{% endtabs %}

`MANAGE_IDENTIFIER`はアプリにディープリンクするため、Brazeダッシュボードでそのアクションボタンに関連するディープリンクURLを設定します。ただし、`KEEP_IDENTIFIER`は通知を閉じるだけなので、ダッシュボードにボタンを定義する必要はありません。ダッシュボードでは、アプリコードで登録した内容と一致するカテゴリ名（例:`YOUR_CATEGORY`）を入力するだけです。

## バッジをカスタマイズする {#customizing-badges}

バッジは、ユーザーの注意を引くのに最適な小さなアイコンです。Brazeダッシュボードでプッシュ通知を作成する際に、[**設定**]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_settings)タブでバッジカウントを指定できます。また、アプリケーションの[`applicationIconBadgeNumber`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber)プロパティや[リモート通知ペイロード](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1)を通じて、バッジカウントを手動で更新することもできます。

Brazeは、アプリがフォアグラウンドにある状態でBraze通知を受信した場合、バッジカウントを自動的にクリアします。バッジ番号を手動で0に設定すると、通知センターの通知もクリアされます。

通常のアプリ操作の一環としてバッジをクリアする計画がない場合、またはバッジをクリアするプッシュを送信しない場合は、アプリがアクティブになったときにバッジをクリアする必要があります。`SceneDelegate.swift`ファイルの`sceneDidBecomeActive(_:)`メソッド（または、アプリがまだ[`UIScene`ライフサイクル](https://developer.apple.com/documentation/technotes/tn3187-migrating-to-the-uikit-scene-based-life-cycle)を採用していない場合は、アプリの`applicationDidBecomeActive:`デリゲートメソッド）に以下のコードを追加してください。

{% tabs %}
{% tab swift %}

```swift
// For iOS 16.0+
let center = UNUserNotificationCenter.current()
do {
  try await center.setBadgeCount(0)
} catch {
  // Handle errors
}

// Prior to iOS 16. Deprecated in iOS 17+.
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
// For iOS 16.0+
UNUserNotificationCenter *center = [UNUserNotificationCenter currentNotificationCenter];
[center setBadgeCount:0 withCompletionHandler:^(NSError * _Nullable error) {
    if (error != nil) {
        // Handle errors
    }
}];

// Prior to iOS 16. Deprecated in iOS 17+.
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% endtabs %}

## サウンドをカスタマイズする {#customizing-sounds}

### ステップ1:アプリでサウンドをホストする {#step-1-host-the-sound-in-your-app}

カスタムプッシュ通知サウンドは、アプリのメインバンドル内にローカルでホストする必要があります。以下のオーディオデータ形式がサポートされています。

- Linear PCM
- MA4
- µLaw
- aLaw

オーディオデータは、AIFF、WAV、またはCAFファイルにパッケージできます。Xcodeで、サウンドファイルをアプリケーションバンドルの非ローカライズリソースとしてプロジェクトに追加してください。

{% alert note %}
カスタムサウンドは再生時に30秒以内である必要があります。カスタムサウンドがこの制限を超える場合、代わりにデフォルトのシステムサウンドが再生されます。
{% endalert %}

#### サウンドファイルを変換する {#converting-sound-files}

afconvertツールを使用してサウンドを変換できます。たとえば、16ビットリニアPCMシステムサウンドSubmarine.aiffをCAFファイルのIMA4オーディオに変換するには、ターミナルで以下のコマンドを使用します。

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

{% alert tip %}
サウンドのデータ形式を確認するには、QuickTime Playerで開き、**ムービー**メニューから**ムービーインスペクタを表示**を選択します。
{% endalert %}

### ステップ2:サウンドのプロトコルURLを指定する {#step-2-provide-a-protocol-url-for-the-sound}

アプリ内のサウンドファイルの場所を示すプロトコルURLを指定する必要があります。これには2つの方法があります。

* [Appleプッシュオブジェクト]({{site.baseurl}}/api/objects_filters/messaging/apple_object)の`sound`パラメーターを使用して、URLをBrazeに渡します。
* ダッシュボードでURLを指定します。[プッシュコンポーザー]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message#step-3-select-notification-type-ios-and-android)で**設定**を選択し、**サウンド**フィールドにプロトコルURLを入力します。

![Brazeダッシュボードのプッシュコンポーザー]({% image_buster /assets/img_archive/sound_push_ios.png %})

指定されたサウンドファイルが存在しない場合、またはキーワード「default」が入力された場合、Brazeはデフォルトのデバイスアラートサウンドを使用します。ダッシュボード以外にも、[メッセージングAPI][12]を通じてサウンドを設定することもできます。

詳細については、Appleデベロッパードキュメントの[カスタムアラートサウンドの準備](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html)を参照してください。

## 設定 {#settings}

ダッシュボードからプッシュキャンペーンを作成する際、**作成**ステップの**設定**タブをクリックすると、利用可能な詳細設定を確認できます。

![詳細オプションを含むBraze iOSプッシュキャンペーンの作成設定タブ。]({% image_buster /assets/img_archive/ios_advanced_settings.png %})

### キーと値のペア {#key-value-pairs}

Brazeでは、`extras` と呼ばれるカスタム定義の文字列キーと値のペアをプッシュ通知と一緒にアプリケーションに送信できます。extrasはダッシュボードまたはAPIを通じて定義でき、プッシュデリゲート実装に渡される `notification` ディクショナリ内でキーと値のペアとして利用できます。

### アラートオプション {#alert-options}

**アラートオプション**チェックボックスを選択すると、デバイスでの通知の表示方法を調整するためのキーと値のドロップダウンが表示されます。

### content-availableフラグの追加 {#adding-content-available-flag}

**Add Content-Available Flag**チェックボックスをオンにすると、バックグラウンドで新しいコンテンツをダウンロードするようデバイスに指示できます。最も一般的には、[サイレント通知]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift)の送信に関心がある場合にチェックを入れます。

### mutable-contentフラグの追加 {#adding-mutable-content-flag}

**Add Mutable-Content Flag**チェックボックスをオンにすると、高度なレシーバーカスタマイズを有効にできます。このフラグは、このチェックボックスの値に関係なく、[リッチプッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift)を作成する際に自動的に送信されます。

### 折りたたみID {#collapse-id}

折りたたみIDを指定すると、類似の通知をまとめることができます。同じ折りたたみIDで複数の通知を送信した場合、デバイスには最後に受信した通知のみが表示されます。Appleの[統合通知](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1)に関するドキュメントを参照してください。

### 有効期限 {#expiry}

**有効期限**チェックボックスをオンにすると、メッセージの有効期限を設定できます。ユーザーのデバイスが接続を失った場合、Brazeは指定された時間までメッセージの送信を試み続けます。これが設定されていない場合、プラットフォームのデフォルトの有効期限は30日です。配信前に期限切れになったプッシュ通知は失敗とは見なされず、バウンスとして記録されません。