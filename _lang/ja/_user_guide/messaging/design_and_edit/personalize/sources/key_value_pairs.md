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

キーと値のペアでメタデータを追加するユースケースの例を以下に示します:

1. **トラッキングパラメーター:** 分析目的でUTMパラメーターを付加する
   - キー: `utm_campaign`
   - 値: `spring_sale`
2. **カスタムタグ:** 内部ルーティングやカテゴリ分けのためにタグを追加する
   - キー: `priority`
   - 値: `high`
3. **動作トリガー:** アプリ内の動作をトリガーまたはカスタマイズするために使用されるメタデータ
   - キー: `deep_link`
   - 値: `app://promo-page`

## プッシュ通知 {#push-notifications}

キーと値のペアは、Android、iOS、Webプッシュ通知に追加できます。キーと値のペアを使用して、内部指標やアプリコンテンツの更新、またはアラートの優先順位付け、ローカライゼーション、サウンドなどのプッシュ通知プロパティのカスタマイズを行うことができます。

メッセージ作成画面で、**Settings**タブを選択し、**Add New Pair**を選択して、キーと値のペアを指定します。

メッセージ作成画面でキーと値のペアを追加すると、値は文字列として送信されます。iOSプッシュの場合、**Alert Options**を通じて追加する予約済みのApple Push Notification service（APNs）アラートキー（ローカライゼーション引数の`loc-args`など）は、ペイロード内で正しいJSON型にフォーマットされます。カスタムキーの場合、インテグレーションで解析しない限り、アプリは文字列値を受け取ります。

### iOS

Apple Push Notification service（APNs）は、キーと値のペアを使用したアラート設定やカスタムデータの送信をサポートしています。APNsは、アラートプロパティを制御する事前定義されたキーと値を含む、Apple予約済みの`aps`ライブラリーを使用します。

#### APSライブラリー {#aps-library}

| キー  | 値の型  | 値の説明 |
|-------------------|-----------------------------|----------------------------------|
| alert             | 文字列またはディクショナリオブジェクト | 文字列入力の場合、文字列をメッセージとして「閉じる」ボタンと「表示」ボタン付きのアラートを表示します。文字列以外の入力の場合、入力の子プロパティに応じてアラートまたはバナーを表示します |
| badge             | 数値                      | アプリアイコンのバッジとして表示される数値を制御します                                                                                                                              |
| sound             | 文字列                      | アラートとして再生するサウンドファイルの名前。アプリのバンドルまたは```Library/Sounds```フォルダーに存在する必要があります                                                                                    |
| content-available | 数値                      | 値1を入力すると、起動時またはセッション再開時に新しい情報が利用可能であることをアプリに通知します |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="APSライブラリー" }


##### アラートプロパティライブラリー {#alert-properties-library}

| キー            | 値の型               | 値の説明                                                                                                                             |
|----------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| title         | 文字列                   | Apple Watchが通知の一部として短時間表示する短い文字列                                                                    |
| body         | 文字列                   | プッシュ通知のコンテンツ                                                                                                                  |
| title-loc-key  | 文字列またはnull           | ```Localizable.strings```ファイルから現在のローカライゼーションのタイトル文字列を設定するキー                                          |
| title-loc-args | 文字列の配列またはnull | title-loc-keyのタイトルローカライゼーションフォーマット指定子の代わりに表示できる文字列値                                           |
| action-loc-key | 文字列の配列またはnull  | 指定された場合、指定された文字列が「閉じる」ボタンと「表示」ボタンのローカライゼーションを設定します                                                         |
| loc-key        | 文字列またはnull           | ```Localizable.strings```ファイルから現在のローカライゼーションの通知メッセージを設定するキー                                  |
| loc-args       | 文字列の配列         | loc-keyのローカライゼーションフォーマット指定子の代わりに表示できる文字列値                                                       |
| launch-image   | 文字列                  | ユーザーがアクションボタンをタップするかアクションスライドを移動したときに起動画像として使用するアプリバンドル内の画像ファイルの名前 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="アラートプロパティライブラリー" }

Brazeのメッセージ作成画面は、**alert**と**そのプロパティ**、**content-available**、**sound**、**category**の各キーの作成を自動的に処理します。

これらの値は、プッシュメッセージの作成時に**Settings**タブで入力できます。**Alert Options**を選択し、アラートディクショナリキーを選択すると、新しいキーと値のエントリにキーが自動的に入力されます。

![プッシュメッセージの作成時にSettingsタブでこれらの値を入力できます。Alert Optionsを選択し、アラートディクショナリキーを選択すると、新しいキーと値のエントリにキーが自動的に入力されます。]({% image_buster /assets/img_archive/keyvalue_automatickeys.png %})
{% raw %}
BrazeがAPNsにプッシュ通知を送信する際、ペイロードはJSONとしてフォーマットされます。

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

`aps`ライブラリーのペイロード値に加えて、カスタムキーと値のペアをユーザーのデバイスに送信できます。これらのペアの値は、ディクショナリ（オブジェクト）、配列、文字列、数値、ブール値のプリミティブ型に制限されます。

![カスタムキーと値のペアに関連するスクリーンショット]({% image_buster /assets/img_archive/keyvalue_enterpairs.png %})

カスタムキーと値のペアのユースケースには、内部指標の管理やユーザーインターフェイスのコンテキスト設定などがありますが、これらに限定されません。Brazeでは、アプリケーション内で[extrasキー]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/advanced_settings#extracting-data-from-push-key-value-pairs)を通じて使用するために、プッシュ通知と一緒に追加のキーと値のペアを送信できます。別のキーを使用する場合は、アプリがそのカスタムキーを処理できることを確認してください。

{% alert warning %}
アプリケーションでabというトップレベルのキーまたはディクショナリを処理することは避けてください。
{% endalert %}

Appleは、カスタムペイロードデータとして顧客情報や機密データを含めないようクライアントに推奨しています。さらに、Appleはアラートメッセージに関連するアクションがデバイス上のデータを削除しないようにすることを推奨しています。

{% alert warning %}
HTTP/2プロバイダーAPIを使用している場合、APNsに送信する個々のペイロードのサイズは4096バイトを超えることはできません。まもなく廃止予定のレガシーバイナリインターフェイスは、2048バイトのペイロードサイズのみをサポートしています。
{% endalert %}

###### APIトリガーCampaign {#api-triggered-campaigns}

Brazeでは、`extras`と呼ばれるカスタム定義の文字列キーと値のペアを送信できます。APIトリガーおよびスケジュールされたAPIトリガーCampaignでextrasにアクセスするには、ダッシュボードでキーを「example_key」、値を{% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}と設定します。これにより、開発者コンソールの出力は`"extras": { "test": { "foo": 1, "bar": 1 }`となります。

### Android

Brazeでは、キーと値のペアを使用してプッシュ通知に追加のデータペイロードを送信できます。

#### データペイロード {#data-payload}

iOSプッシュと同様に、カスタムキーと値のペアをユーザーのデバイスに送信できます。

カスタムキーと値のペアのユースケースには、内部指標の管理やユーザーインターフェイスのコンテキスト設定などがありますが、任意の目的に使用できます。

{% alert important %}
データペイロードが正しく機能するためには、アプリのバックエンドがカスタムキーと値のペアを処理できる必要があります。
{% endalert %}

##### APIトリガーCampaign

Brazeでは、`extras`と呼ばれるカスタム定義の文字列キーと値のペアを送信できます。APIトリガーおよびスケジュールされたAPIトリガーCampaignでextrasにアクセスするには、ダッシュボードでキーを「example_key」、値を{% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}と設定します。これにより、開発者コンソールの出力は`"extras": { "test": { "foo": 1, "bar": 1 }`となります。

##### FCMメッセージングオプション {#fcm-messaging-options}

Androidプッシュ通知は、FCMメッセージオプションでさらにカスタマイズできます。これには、[通知の優先度]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings#notification-priority)、[サウンド]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings#sounds)、遅延、有効期間、折りたたみ可能性が含まれます。これらの値は、プッシュメッセージの作成時に**Settings**タブで指定できます。Brazeのメッセージ作成画面でこれらのオプションを設定する方法の詳細については、[プッシュ通知の詳細設定]({{site.baseurl}}/developer_guide/push_notifications/customization?sdktab=android#android_settings)を参照してください。

![FCMメッセージングオプションに関連するスクリーンショット]({% image_buster /assets/img_archive/keyvalue_androidkeys.png %})

### サイレントプッシュ通知 {#silent-push-notifications}

サイレントプッシュ通知は、アラートメッセージやサウンドを含まないプッシュ通知で、バックグラウンドでアプリのインターフェイスやコンテンツを更新するために使用されます。これらの通知は、キーと値のペアを使用してバックグラウンドのアプリアクションをトリガーします。サイレントプッシュ通知は、[アンインストール追跡]({{site.baseurl}}/user_guide/analytics/tracking/uninstall_tracking)にも使用されます。

マーケターは、アプリのユーザーに送信する前に、サイレントプッシュ通知が期待どおりの動作をトリガーすることをテストする必要があります。[iOS]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=swift)または[Android]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=android)のサイレントプッシュ通知を作成した後、[外部ユーザーID]({{site.baseurl}}/developer_guide/rest_api/messaging#external-user-id)または[メールアドレス]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)でフィルタリングして、テストユーザーのみをターゲットにしてください。

Campaignの起動時に、テストデバイスで目に見えるプッシュ通知を受信していないことを確認してください。

{% alert note %}
iOSのサイレント通知ゲートにより、以下の症状が発生する場合があります:

- iOSユーザーのアンインストール追跡指標が予想より低くなる
- サイレントプッシュ通知の配信が不安定または遅延する
- [Push Stories]({{site.baseurl}}/user_guide/channels/push/create_a_push_message/push_stories)が表示されない
- Push Storiesが期待される画像、動画、またはページなしで届く

これはBrazeの問題ではなく、Appleプラットフォームの制限です。iOSは、アンインストール追跡やPush Storiesを含む一部のBraze機能のバックグラウンド通知を遅延またはドロップする場合があります。iOSがゲートする内容とタイミングの詳細については、[iOSの制限]({{site.baseurl}}/developer_guide/push_notifications/silent?sdktab=swift#ios-limitations)を参照してください。
{% endalert %}

## アプリ内メッセージ {#in-app-messages}

[従来のエディター]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional)で、**Settings**タブを選択し、**Add New Pair**を選択してから、キーと値のペアを指定することで、アプリ内メッセージにキーと値のペアを追加できます。

{% alert note %}
アプリ内メッセージのドラッグ＆ドロップエディターでは、キーと値のペアを設定できません。
{% endalert %}
![アプリ内メッセージに関連するスクリーンショット]({% image_buster /assets/img_archive/keyvalue_iam.png %})

### APIトリガーCampaign

Brazeでは、`extras`と呼ばれるカスタム定義の文字列キーと値のペアを送信できます。APIトリガーおよびスケジュールされたAPIトリガーCampaignでextrasにアクセスするには、ダッシュボードでキーを「example_key」、値を{% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}と設定します。これにより、開発者コンソールの出力は`"extras": { "test": { "foo": 1, "bar": 1 }`となります。

## メール {#emails}

SparkPostとSendGridの両方がメールでのキーと値のペアをサポートしています。SendGridを使用している場合、キーと値のペアは[unique arguments](https://docs.sendgrid.com/for-developers/sending-email/unique-arguments)として送信されます。SendGridでは、最大10,000バイトのデータまで無制限の数のキーと値のペアを添付できます。これらのキーと値のペアは、SendGridの[Event Webhook](https://sendgrid.com/docs/for-developers/tracking-events/event/)からの投稿で確認できます。

{% alert note %}
バウンスしたメールは、SparkPostまたはSendGridにキーと値のペアを配信しません。
{% endalert %}

![Brazeのメールメッセージ作成画面の送信情報タブ]({% image_buster /assets/img_archive/keyvalue_email.png %})

## Content Cards

Content Cardsにキーと値のペアを追加するには、Brazeのメッセージ作成画面の**Settings**タブに移動し、**Add New Pair**を選択します。

![Content Cardsにキーと値のペアを追加]({% image_buster /assets/img_archive/kvp_content_cards.png %}){: style="max-width:70%;"}