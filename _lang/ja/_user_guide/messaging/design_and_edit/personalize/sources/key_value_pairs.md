---
nav_title: キーと値のペア
article_title: キーと値のペア
page_order: 4
description: "このリファレンス記事では、キーと値のペアと、それを使用してユーザーデバイスに追加のデータペイロードを送信する方法について説明します。"
channel:
  - push
  - in-app messages
  - content cards

---

# キーと値のペア {#key-value-pairs}

> このページでは、キーと値のペアを使用してユーザーデバイスに追加のデータペイロードを送信する方法について説明します。この機能は、プッシュ通知、アプリ内メッセージ、メール、Content Cardのメッセージングチャネルで利用できます。

キーと値のペアを使用して、メッセージに構造化されたメタデータを追加します。これらの追加データペイロードにより、メッセージのレンダリングや処理方法に影響を与える文脈に応じた情報でメッセージを充実させることができます。

キーと値のペアはメタデータであるため、このデータは必ずしも受信者に表示されるわけではありませんが、接続されたシステムやプロセスがメッセージ処理をカスタマイズするために使用できます。

各ペアは以下で構成されます:

- **キー:** 識別子（例: `utm_source`）
- **値:** 関連データ（例: `newsletter`）

## ユースケース {#use-cases}

キーと値のペアでメタデータを追加するユースケースの例を以下に示します。

1. **トラッキングパラメーター:** 分析目的で UTM パラメーターを付加します
   - キー: `utm_campaign`
   - 値: `spring_sale`
2. **カスタムタグ:** 内部ルーティングやカテゴリ分けのためにタグを追加します
   - キー: `priority`
   - 値: `high`
3. **動作トリガー:** アプリ内の動作をトリガーまたはカスタマイズするために使用するメタデータです
   - キー: `deep_link`
   - 値: `app://promo-page`

## プッシュ通知 {#push-notifications}

キーと値のペアは、Android、iOS、Web プッシュ通知に追加できます。キーと値のペアを使用して、内部メトリクスやアプリコンテンツを更新したり、アラートの優先順位付け、ローカライゼーション、サウンドなどのプッシュ通知プロパティをカスタマイズしたりできます。

メッセージ作成画面で、**Settings** タブを選択し、**Add New Pair** を選択して、キーと値のペアを指定します。

メッセージ作成画面でキーと値のペアを追加すると、値は文字列として送信されます。iOS プッシュの場合、**Alert Options** を通じて追加する予約済みの Apple Push Notification service（APNs）アラートキー（ローカライゼーション引数の `loc-args` など）は、ペイロード内で正しい JSON 型にフォーマットされます。カスタムキーの場合、インテグレーションで解析しない限り、アプリは文字列値を受け取ります。

### iOS

Apple Push Notification service（APNs）は、キーと値のペアを使用したアラート設定とカスタムデータの送信をサポートしています。APNs は、アラートプロパティを制御する所定のキーと値を含む、Apple 予約済みの `aps` ライブラリを使用します。

#### APS ライブラリ {#aps-library}

| キー  | 値の型  | 値の説明 |
|-------------------|-----------------------------|----------------------------------|
| alert             | 文字列またはディクショナリオブジェクト | 文字列入力の場合、メッセージとして文字列を含むアラートを「閉じる」ボタンと「表示」ボタンとともに表示します。文字列以外の入力の場合、入力の子プロパティに応じてアラートまたはバナーを表示します |
| badge             | 数値                      | アプリアイコンのバッジとして表示される数値を制御します                                                                                                                              |
| sound             | 文字列                      | アラートとして再生するサウンドファイルの名前。アプリのバンドルまたは ```Library/Sounds``` フォルダーに含まれている必要があります                                                                                    |
| content-available | 数値                      | 値 1 を入力すると、起動時またはセッション再開時に新しい情報が利用可能であることをアプリに通知します |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="APS ライブラリ" }


##### アラートプロパティライブラリ {#alert-properties-library}

| キー            | 値の型               | 値の説明                                                                                                                             |
|----------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| title         | 文字列                   | Apple Watch が通知の一部として短時間表示する短い文字列                                                                    |
| body         | 文字列                   | プッシュ通知のコンテンツ                                                                                                                  |
| title-loc-key  | 文字列または null           | ```Localizable.strings``` ファイルから現在のローカライゼーションのタイトル文字列を設定するキー                                          |
| title-loc-args | 文字列の配列または null | title-loc-key のタイトルローカライゼーションフォーマット指定子の代わりに表示できる文字列値                                           |
| action-loc-key | 文字列の配列または null  | 指定された場合、指定された文字列が「閉じる」ボタンと「表示」ボタンのローカライゼーションを設定します                                                         |
| loc-key        | 文字列または null           | ```Localizable.strings``` ファイルから現在のローカライゼーションの通知メッセージを設定するキー                                  |
| loc-args       | 文字列の配列         | loc-key のローカライゼーションフォーマット指定子の代わりに表示できる文字列値                                                       |
| launch-image   | 文字列                  | ユーザーがアクションボタンをタップするかアクションスライドを動かしたときに起動画像として使用する、アプリバンドル内の画像ファイルの名前 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="アラートプロパティライブラリ" }

Braze のメッセージ作成画面は、**alert** と**そのプロパティ**、**content-available**、**sound**、**category** の各キーの作成を自動的に処理します。

これらの値は、プッシュメッセージの作成時に **Settings** タブで入力できます。**Alert Options** を選択し、アラートディクショナリキーを選択すると、新しいキーと値のエントリにキーが自動的に入力されます。

![これらの値は、プッシュメッセージの作成時に Settings タブで入力できます。Alert Options を選択し、アラートディクショナリキーを選択すると、新しいキーと値のエントリにキーが自動的に入力されます。]({% image_buster /assets/img_archive/keyvalue_automatickeys.png %})
{% raw %}
Braze がプッシュ通知を APNs に送信すると、ペイロードは JSON としてフォーマットされます。

**シンプルなペイロード**

```
{
    "aps" : { "alert" : "Message received from Spencer" },
}
```

**複雑なペイロード**

```
{
    "aps" : {
        "alert" : {
            "body" : "Hi, welcome to our app!",
            "loc-key" : "France",
            "loc-args" : ["Bonjour", "bienvenue"],
            "action-loc-key" : "Button_Type_1",
            "launch-image" : "Paris"
      },
        "content-available" : 1
    },
}
```

{% endraw %}

##### カスタムキーと値のペア {#custom-key-value-pairs}

`aps` ライブラリのペイロード値に加えて、カスタムキーと値のペアをユーザーのデバイスに送信できます。これらのペアの値は、ディクショナリ（オブジェクト）、配列、文字列、数値、ブール値のプリミティブ型に制限されています。

![カスタムキーと値のペアに関連するスクリーンショット。]({% image_buster /assets/img_archive/keyvalue_enterpairs.png %})

カスタムキーと値のペアのユースケースには、内部メトリクスの管理やユーザーインターフェイスのコンテキスト設定などがありますが、これらに限定されません。Braze では、[extras キー]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/advanced_settings#extracting-data-from-push-key-value-pairs)を通じてアプリケーション内で使用するために、プッシュ通知とともに追加のキーと値のペアを送信できます。別のキーを使用する場合は、アプリがそのカスタムキーを処理できることを確認してください。

{% alert warning %}
アプリケーションで ab というトップレベルのキーまたはディクショナリを処理することは避けてください。
{% endalert %}

Apple は、カスタムペイロードデータとして顧客情報や機密データを含めないようクライアントに推奨しています。さらに、Apple は、アラートメッセージに関連するアクションがデバイス上のデータを削除しないことを推奨しています。

{% alert warning %}
HTTP/2 プロバイダー API を使用している場合、APNs に送信する個々のペイロードのサイズは 4096 バイトを超えることはできません。まもなく廃止予定のレガシーバイナリインターフェイスは、2048 バイトのペイロードサイズのみをサポートしています。
{% endalert %}

###### API トリガーキャンペーン {#api-triggered-campaigns}

Braze では、`extras` と呼ばれるカスタム定義の文字列キーと値のペアを送信できます。API トリガーおよびスケジュール済み API トリガーキャンペーンで extras にアクセスするには、ダッシュボードでキーを「example_key」に設定し、値を {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %} に設定します。これにより、開発者コンソールの出力は `"extras": { "test": { "foo": 1, "bar": 1 }` となります。

### Android

Braze では、キーと値のペアを使用してプッシュ通知に追加のデータペイロードを送信できます。

#### データペイロード {#data-payload}

iOS プッシュと同様に、カスタムキーと値のペアをユーザーのデバイスに送信できます。

カスタムキーと値のペアのユースケースには、内部メトリクスの管理やユーザーインターフェイスのコンテキスト設定などがありますが、任意の目的に使用できます。

{% alert important %}
データペイロードが正しく機能するためには、アプリのバックエンドがカスタムキーと値のペアを処理できる必要があります。
{% endalert %}

##### API トリガーキャンペーン

Braze では、`extras` と呼ばれるカスタム定義の文字列キーと値のペアを送信できます。API トリガーおよびスケジュール済み API トリガーキャンペーンで extras にアクセスするには、ダッシュボードでキーを「example_key」に設定し、値を {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %} に設定します。これにより、開発者コンソールの出力は `"extras": { "test": { "foo": 1, "bar": 1 }` となります。

##### FCM メッセージングオプション {#fcm-messaging-options}

Android プッシュ通知は、FCM メッセージオプションでさらにカスタマイズできます。これには、[通知の優先度]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings#notification-priority)、[サウンド]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings#sounds)、遅延、有効期間、折りたたみ可能性が含まれます。これらの値は、プッシュメッセージの作成時に **Settings** タブで指定できます。Braze のメッセージ作成画面でこれらのオプションを設定する方法の詳細については、[プッシュ通知の詳細設定]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_settings)を参照してください。

![FCM メッセージングオプションに関連するスクリーンショット。]({% image_buster /assets/img_archive/keyvalue_androidkeys.png %})

### サイレントプッシュ通知 {#silent-push-notifications}

サイレントプッシュ通知は、アラートメッセージやサウンドを含まないプッシュ通知で、バックグラウンドでアプリのインターフェイスやコンテンツを更新するために使用されます。これらの通知は、キーと値のペアを使用してバックグラウンドのアプリアクションをトリガーします。サイレントプッシュ通知は、[アンインストール追跡]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking)にも使用されます。

マーケターは、アプリのユーザーに送信する前に、サイレントプッシュ通知が期待どおりの動作をトリガーすることをテストする必要があります。[iOS]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=swift) または [Android]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=android) のサイレントプッシュ通知を作成した後、[外部ユーザー ID]({{site.baseurl}}/developer_guide/rest_api/messaging#external-user-id) または[メールアドレス]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)でフィルタリングして、テストユーザーのみをターゲットにしてください。

キャンペーンの開始時に、テストデバイスで目に見えるプッシュ通知を受信していないことを確認してください。

{% alert note %}
iOS のサイレント通知のゲーティングにより、以下の症状が発生する場合があります。

- iOS ユーザーのアンインストール追跡メトリクスが予想より低い
- サイレントプッシュ通知の配信が不安定または遅延する
- [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories)が表示されない
- Push Stories が期待される画像、動画、またはページなしで届く

これは Braze の問題ではなく、Apple プラットフォームの制限です。iOS は、アンインストール追跡や Push Stories を含む一部の Braze 機能のバックグラウンド通知を遅延またはドロップする場合があります。iOS がゲーティングする内容とタイミングの詳細については、[iOS の制限]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=swift#ios-limitations)を参照してください。
{% endalert %}

## アプリ内メッセージ {#in-app-messages}

アプリ内メッセージにキーと値のペアを追加するには、[従来のエディター]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional)で**設定**タブを選択し、**新しいペアを追加**を選択して、キーと値のペアを指定します。

{% alert note %}
アプリ内メッセージのドラッグ＆ドロップエディターでは、キーと値のペアを設定できません。
{% endalert %}
![アプリ内メッセージに関連するスクリーンショット。]({% image_buster /assets/img_archive/keyvalue_iam.png %})

### APIトリガーキャンペーン

Brazeでは、`extras` と呼ばれるカスタム定義の文字列キーと値のペアを送信できます。APIトリガーキャンペーンおよびスケジュールされたAPIトリガーキャンペーンでextrasにアクセスするには、ダッシュボードでキーを「example_key」、値を {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %} に設定します。これにより、開発者コンソールの出力は `"extras": { "test": { "foo": 1, "bar": 1 }` となります。

## メール {#emails}

SparkPost と SendGrid はどちらもメールのキーと値のペアをサポートしています。SendGrid を使用する場合、キーと値のペアは[ユニーク引数](https://docs.sendgrid.com/for-developers/sending-email/unique-arguments)として送信されます。SendGrid では、最大10,000バイトのデータまで、無制限の数のキーと値のペアを添付できます。これらのキーと値のペアは、SendGrid の [Event Webhook](https://sendgrid.com/docs/for-developers/tracking-events/event/) からの投稿で確認できます。

{% alert note %}
バウンスしたメールは、SparkPost や SendGrid にキーと値のペアを配信しません。
{% endalert %}

![Braze のメールメッセージ作成画面の「送信情報」タブ。]({% image_buster /assets/img_archive/keyvalue_email.png %})

## Content Cards

Content Cardsにキーと値のペアを追加するには、Brazeのメッセージ作成画面の**設定**タブに移動し、**新しいペアを追加**を選択します。

![Content Cardsにキーと値のペアを追加]({% image_buster /assets/img_archive/kvp_content_cards.png %}){: style="max-width:70%;"}

{% alert note %}
コントロールバリアントはキーと値のペアをサポートしていません。A/Bテストでコントロールグループの分析をキャプチャする必要がある場合は、`control=true` などのキーと値のペアを含むメッセージバリアントを作成し、インプレッションを記録しながらアプリコード内で非表示にしてください。
{% endalert %}