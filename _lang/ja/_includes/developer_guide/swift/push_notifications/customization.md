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

`UNNotification`フレームワークを使用し、Brazeの[通知メソッド]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration#step-5-enable-push-handling)を実装した場合、このメソッドはすでに統合されているはずです。

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
アプリ内へのディープリンクやWeb URLへのリダイレクトなど、Swiftコードでローカルに作成できない動作についてのみ、Brazeダッシュボード上でアクションボタンを定義する必要があります。これらのアクションはダッシュボードで設定する必要があり、そうすることでどのURLやディープリンクを開くかを定義できます。アプリを開かずに通知を閉じるだけのアクションボタンについては、ダッシュボードで設定する必要はありません。通知の閉じ動作はiOSが自動的に処理します。アプリコードでカスタムカテゴリとそのアクションを登録し、ダッシュボードで対応するカテゴリ名を入力するだけです。
{% endalert %}

1. Brazeダッシュボードで、**メッセージング** > **プッシュ通知**を選択し、iOSの[プッシュキャンペーン]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message)を選択します。
2. **プッシュ通知を作成する**の下で、**アクションボタン**をオンにします。
3. **iOS通知カテゴリ**ドロップダウンで、**事前登録されたカスタムiOSカテゴリを入力**を選択します。
4. 最後に、前に作成したカテゴリのいずれかを入力します。次の例では、カスタムカテゴリ`LIKE_CATEGORY`を使用します。

![カスタムカテゴリの設定を含むプッシュ通知キャンペーンダッシュボード。]({% image_buster /assets/img_archive/ios-notification-category.png %})

### 例:カスタムプッシュカテゴリ {#example-custom-push-category}

2つのアクションボタンを持つプッシュ通知を作成したいとします。アプリにディープリンクする**Manage**と、単に通知を閉じるだけの**Keep**です。

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

## バッジのカスタマイズ {#customizing-badges}

バッジは小さなアイコンで、ユーザーの注意を引くのに最適です。Brazeダッシュボードでプッシュ通知を作成する際、[**設定**]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_settings)タブでバッジカウントを指定できます。アプリケーションの[`applicationIconBadgeNumber`](https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIApplication_Class/index.html#//apple_ref/occ/instp/UIApplication/applicationIconBadgeNumber)プロパティまたは[リモート通知ペイロード](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CreatingtheNotificationPayload.html#//apple_ref/doc/uid/TP40008194-CH10-SW1)を使用して、バッジ数を手動で更新することもできます。

Brazeは、アプリがフォアグラウンドにあるときにBraze通知を受信すると、バッジカウントを自動的にクリアします。バッジ番号を手動で0に設定すると、通知センターの通知もクリアされます。

通常のアプリ操作の一部として、またはバッジをクリアするプッシュを送信してバッジをクリアする計画がない場合は、次のコードをアプリの`applicationDidBecomeActive:`デリゲートメソッドに追加して、アプリがアクティブになったときにバッジをクリアする必要があります。

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

## サウンドのカスタマイズ {#customizing-sounds}

### ステップ1:アプリ内でサウンドをホストする {#step-1-host-the-sound-in-your-app}

カスタムプッシュ通知サウンドは、アプリのメインバンドル内でローカルにホストする必要があります。次のオーディオデータ形式が使用できます。

- リニアPCM
- MA4
- µLaw
- aLaw

オーディオデータはAIFF、WAV、またはCAFファイルにパッケージできます。Xcodeで、サウンドファイルをアプリケーションバンドルの非ローカライズリソースとしてプロジェクトに追加します。

{% alert note %}
カスタムサウンドは再生時に30秒未満である必要があります。カスタムサウンドがこの制限を超えている場合、デフォルトのシステムサウンドが代わりに再生されます。
{% endalert %}

#### サウンドファイルを変換する {#converting-sound-files}

afconvertツールを使用してサウンドを変換できます。例えば、16ビットリニアPCMシステムサウンドSubmarine.aiffをCAFファイルのIMA4オーディオに変換するには、ターミナルで次のコマンドを使用します。

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

{% alert tip %}
QuickTime Playerでサウンドを開き、**ムービー**メニューから**ムービーインスペクターを表示**を選択すると、サウンドのデータ形式を確認できます。
{% endalert %}

### ステップ2:サウンドのプロトコルURLを提供する {#step-2-provide-a-protocol-url-for-the-sound}

アプリ内のサウンドファイルの場所を指すプロトコルURLを指定する必要があります。これには2つの方法があります。

* [Appleプッシュオブジェクト]({{site.baseurl}}/api/objects_filters/messaging/apple_object#apple-push-object)の`sound`パラメータを使用して、URLをBrazeに渡します。
* ダッシュボードでURLを指定します。[プッシュコンポーザー]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message#step-3-select-notification-type-ios-and-android)で**設定**を選択し、**サウンド**フィールドにプロトコルURLを入力します。

![Brazeダッシュボードのプッシュコンポーザー]({% image_buster /assets/img_archive/sound_push_ios.png %})

指定したサウンドファイルが存在しない場合、またはキーワード「default」を入力した場合は、Brazeではデバイスのデフォルトのアラートサウンドが使用されます。ダッシュボードとは別に、[messaging API][12]でサウンドを設定することもできます。

詳細については、[カスタムアラートサウンドの準備](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html)に関するApple Developerのドキュメントを参照してください。

## 設定 {#settings}

ダッシュボードからプッシュキャンペーンを作成する場合、**作成**ステップで**設定**タブをクリックし、利用可能な詳細設定を表示します。

![Braze iOSプッシュキャンペーンの作成設定タブと詳細オプション。]({% image_buster /assets/img_archive/ios_advanced_settings.png %})

### キーと値のペア {#key-value-pairs}

Brazeを使用すると、`extras`として知られるカスタム定義の文字列キーと値のペアを、アプリケーションへプッシュ通知と一緒に送ることができます。エクストラは、ダッシュボードまたはAPIを介して定義することができ、プッシュデリゲートの実装に渡される`notification`辞書内のキーと値のペアとして利用できます。

### アラートオプション {#alert-options}

**アラートオプション**チェックボックスを選択すると、デバイスにどのように通知が表示されるかを調整するために利用可能なキー値のドロップダウンが表示されます。

### コンテンツ利用可能フラグを追加する {#adding-content-available-flag}

新しいコンテンツをバックグラウンドでダウンロードするようにデバイスに指示するには、**コンテンツ利用可能フラグを追加**チェックボックスをオンにします。最も一般的には、[サイレント通知]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift)の送信に関心がある場合にチェックできます。

### mutable-contentフラグを追加する {#adding-mutable-content-flag}

**mutable-contentフラグを追加**チェックボックスをオンにして、受信側の高度なカスタマイズを有効にします。このフラグは、このチェックボックスの値に関係なく、[リッチプッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=swift)を作成するときに自動的に送信されます。

### 折りたたみID {#collapse-id}

同様の通知をまとめるには、折りたたみIDを指定します。同一の折りたたみIDを使用して複数の通知を送信すると、デバイスには最後に受信した通知のみが表示されます。[統合された通知](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/APNSOverview.html#//apple_ref/doc/uid/TP40008194-CH8-SW1)については、Appleのドキュメントを参照してください。

### 有効期限 {#expiry}

**有効期限**チェックボックスをオンにすると、メッセージの有効期限を設定できます。ユーザーのデバイスが接続性を失った場合、Brazeは指定された時間までメッセージの送信を試行し続けます。設定されていない場合、プラットフォームの有効期限はデフォルトで30日となります。配信前に有効期限切れとなったプッシュ通知は失敗とはみなされず、バウンスとして記録されないことに注意してください。