---
nav_title: Webhookを作成する
article_title: Webhookを作成する
page_order: 1
channel:
  - webhooks
description: "このリファレンス記事では、Webhookキャンペーンの作成と設定方法について説明します。"
search_rank: 2
---

# Webhookキャンペーンを作成する {#create-a-webhook-campaign}

> Webhookキャンペーンを作成するか、マルチチャネルキャンペーンにWebhookを含めることで、他のシステムやアプリケーションにリアルタイム情報を提供し、アプリ外のアクションをトリガーできます。

Webhookを使用して、SalesforceやMarketoなどのシステムやバックエンドシステムに情報を送信できます。たとえば、顧客がカスタムイベントを一定回数実行した後に、プロモーションで顧客のアカウントにクレジットを付与したい場合があります。

{% alert tip %}
Webhookとは何か、またBrazeでどのように使用できるかについて詳しくは、先に進む前に[Webhook]({{site.baseurl}}/user_guide/channels/webhooks)をご確認ください。
{% endalert %}

## ステップ1: メッセージの作成場所を選択する {#step-1-choose-where-to-build-your-message}

メッセージをキャンペーンとキャンバスのどちらで送信すべきかわからない場合、キャンペーンは単一のターゲットメッセージングに適しており、キャンバスは複数ステップのユーザージャーニーに適しています。

{% tabs %}
{% tab キャンペーン %}

**手順:**

1. **メッセージング** > **キャンペーン**に移動し、**キャンペーンを作成**を選択します。
2. **Webhook**を選択するか、複数チャネルをターゲットとするキャンペーンの場合は**マルチチャネル**を選択します。
3. キャンペーンにわかりやすく意味のある名前を付けます。
4. （オプション）このキャンペーンの使用方法を説明する説明を追加します。
4. 必要に応じて[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams)と[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)を追加します。
   * タグを使用すると、キャンペーンを見つけやすくなり、レポートを作成しやすくなります。たとえば、[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reports/report_builder)を使用する場合、特定のタグでフィルタリングできます。
5. キャンペーンに必要な数のバリアントを追加して名前を付けます。追加した各バリアントに異なるWebhookテンプレートを選択できます。このトピックの詳細については、[多変量テストとABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を参照してください。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似している場合や同じコンテンツを持つ場合は、追加のバリアントを追加する前にメッセージを作成してください。その後、**バリアントを追加**ドロップダウンから**バリアントからコピー**を選択できます。
{% endalert %}

{% endtab %}
{% tab キャンバス %}

**手順:**

1. キャンバスコンポーザーを使用して[キャンバスを作成]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas)します。
2. キャンバスを設定したら、キャンバスビルダーでステップを追加します。ステップにわかりやすく意味のある名前を付けます。
3. [ステップスケジュール]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#step-2-edit-delivery-settings)を選択し、必要に応じて遅延を指定します。
4. 必要に応じて、このステップのオーディエンスをフィルタリングします。セグメントを指定し、追加のフィルターを追加することで、このステップの受信者をさらに絞り込むことができます。オーディエンスオプションは、遅延後のメッセージ送信時にチェックされます。
5. [進行動作]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas#advancement-behavior)を選択します。
6. メッセージと組み合わせたい他のメッセージングチャネルを選択します。

{% endtab %}
{% endtabs %}

## ステップ2: Webhookを構築する {#step-2-build-your-webhook}

Webhookをゼロから作成するか、既存のテンプレートを使用するか、既存のテンプレートの1つを使用するかを選択できます。次に、エディターの**作成**タブでWebhookを構築します。

**作成**タブは以下のフィールドで構成されています:

- 言語
- Webhook URL
- HTTPメソッド
- リクエストボディ

![Webhookテンプレートの例を含む「作成」タブ。]({% image_buster /assets/img_archive/webhook_compose.png %})

### 言語 {#internationalization}

[国際化]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization)はURLとリクエストボディでサポートされています。メッセージを国際化するには、**言語を追加**を選択し、必要なフィールドに入力します。

コンテンツを作成する前に言語を選択することをお勧めします。これにより、Liquid内の適切な場所にテキストを入力できます。使用可能な言語の完全なリストについては、[サポートされている言語]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization#languages-supported)を参照してください。

右から左に書く言語のコピーを追加する場合、右から左のメッセージの最終的な表示はサービスプロバイダーのレンダリング方法に大きく依存することに注意してください。右から左のメッセージをできるだけ正確に表示するためのベストプラクティスについては、[右から左のメッセージの作成]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)を参照してください。

### Webhook URL {#webhook-url}

Webhook URL（HTTP URL）はエンドポイントを指定します。エンドポイントは、Webhookでキャプチャしている情報を送信する場所です。

ベンダーに情報を送信する場合、ベンダーはこのURLをAPIドキュメントで提供する必要があります。自社システムに情報を送信する場合は、開発チームまたはエンジニアリングチームに確認して、正しいURLを使用していることを確認してください。

Brazeは、標準ポート`80`（HTTP）および`443`（HTTPS）で通信するURLのみを許可します。

#### Liquidの使用 {#using-liquid}

[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)を使用してWebhook URLをパーソナライズできます。特定のエンドポイントでは、URLの一部としてユーザーを識別したり、ユーザー固有の情報を提供したりする必要がある場合があります。Liquidを使用する場合は、URLで使用するユーザー固有の情報ごとに[デフォルト値]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web)を含めるようにしてください。

### HTTPメソッド {#http-method}

使用すべきHTTPメソッドは、情報を送信するエンドポイントによって異なります。ほとんどの場合、POSTを使用します。

| HTTPメソッド | 説明 |
| ----------- | ----------- |
| POST | 受信サーバーに新しい情報を書き込みます。データ送信時に最も一般的に使用されるメソッドです。 |
| GET | 新しい情報を書き込むのではなく、既存の情報を取得します。定義上、GETリクエストはリクエストボディをサポートしません。 |
| PUT | エンドポイントの情報を更新し、既存の情報をリクエストボディの内容で置き換えます。 |
| DELETE | HTTP URL内のリソースを削除します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="HTTPメソッド" }

### リクエストボディ {#request-body}

リクエストボディは、指定したURLに送信される情報です。Webhookリクエストのボディは、JSONキーと値のペアまたはRawテキストで作成できます。

#### JSONキーと値のペア {#json-key-value-pairs}

JSONキーと値のペアを使用すると、JSON形式を期待するエンドポイント向けのリクエストを簡単に作成できます。JSONリクエストを期待するエンドポイントでのみ使用できます。たとえば、キーが`message_body`の場合、対応する値は`Your order just arrived!`のようになります。キーと値のペアを入力すると、コンポーザーがJSON構文でリクエストを設定し、JSONリクエストのプレビューが自動的に表示されます。

![リクエストボディをJSONキーと値のペアに設定した例。]({% image_buster /assets/img/webhook_json_1.png %})

Liquidを使用してキーと値のペアをパーソナライズできます。ユーザー属性、[カスタム属性]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids#additional-notes-and-best-practices)、または[イベントプロパティ]({{site.baseurl}}/user_guide/data/activation/events/custom_events)をリクエストに含めることができます。たとえば、顧客の名とメールアドレスをリクエストに含めることができます。各属性に[デフォルト値]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web)を含めるようにしてください。

#### Rawテキスト {#raw-text}

Rawテキストオプションを使用すると、任意の形式のボディを期待するエンドポイント向けのリクエストを柔軟に作成できます。たとえば、XML形式のリクエストを期待するエンドポイント向けのリクエストを作成する場合に使用できます。

Rawテキストでは、Liquidを使用した[パーソナライゼーション]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)と[国際化]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization)の両方がサポートされています。

![Liquidを使用したRawテキストのリクエストボディの例。]({% image_buster /assets/img_archive/webhook_rawtext.png %})

`Content-Type`[リクエストヘッダー](#request-headers-optional)を`application/x-www-form-url-encoded`に設定した場合、リクエストボディはURLエンコードされた文字列としてフォーマットする必要があります。例:

{% raw %}
```
to={{custom_attribute.${example}}}&text=Your+order+just+arrived
```
{% endraw %}

![URLエンコードされた文字列のリクエストボディ。]({% image_buster /assets/img_archive/webhook_rawtext_URL-encoded.png %})

## ステップ3: 追加設定を構成する {#step-3-configure-additional-settings}

### リクエストヘッダー（オプション） {#request-headers-optional}

特定のエンドポイントでは、リクエストにヘッダーを含める必要がある場合があります。コンポーザーの**作成**セクションで、必要な数のヘッダーを追加できます。

![「Authorization」キーと「Content-Type」キーのリクエストヘッダーの例。]({% image_buster /assets/img_archive/webhook_request_headers_example.png %})

一般的なリクエストヘッダーは、`Content-Type`仕様（ボディで期待されるデータの種類（XMLやJSONなど）を記述するもの）と、ベンダーやシステムの認証情報を含む認証ヘッダーです。

Content-Type仕様にはキー`Content-Type`を使用する必要があります。一般的な値は`application/json`または`application/x-www-form-urlencoded`です。

認証ヘッダーにはキー`Authorization`を使用する必要があります。一般的な値は{% raw %}`Bearer {{YOUR_TOKEN}}`または`Basic {{YOUR_TOKEN}}`{% endraw %}で、`YOUR_TOKEN`はベンダーやシステムから提供された認証情報です。

## ステップ4: テスト送信する {#step-4-test-send-your-message}

キャンペーンを公開する前に、Brazeではリクエストが適切にフォーマットされていることを確認するためにWebhookをテストすることをお勧めします。

テストするには、**テスト**タブに切り替えてテストWebhookを送信します。ランダムユーザー、特定のユーザー（メールアドレスまたは外部ユーザーIDを入力）、または選択した属性を持つカスタマイズされたユーザーとしてWebhookをテストできます。

テストWebhookを送信すると、レスポンスメッセージを含むダイアログが表示されます。Webhookリクエストが失敗した場合は、エラーメッセージを参照してWebhookのトラブルシューティングを行ってください。以下の例は、無効なWebhook URLを持つWebhookのレスポンスの詳細です。

```http
404 Not Found

{
  "error": {
    "message": "Unrecognized request URL. Please see https://lob.com/docs or email us at support@lob.com.",
    "status_code": 404
  }
}

```

詳細については、[テストメッセージの送信]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=webhook)を参照してください。

## ステップ5: キャンペーンまたはキャンバスの残りを構築する {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab キャンペーン %}

次に、キャンペーンの残りの部分を構築します。Webhookを構築するためのツールの最適な使用方法の詳細については、以下のセクションを参照してください。

### 配信スケジュールまたはトリガーを選択する {#choose-delivery-schedule-or-trigger}

Webhookは、スケジュールされた時間、アクション、またはAPIトリガーに基づいて配信できます。詳細については、[キャンペーンのスケジュール設定]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)を参照してください。

アクションベースの配信では、キャンペーンの期間と[サイレント時間]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)を設定することもできます。

このステップでは、ユーザーがキャンペーンを[再受信可能]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility)にすることや、[フリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping)ルールを有効にするなどの配信コントロールを指定することもできます。

### ターゲットユーザーを選択する {#choose-users-to-target}

次に、セグメントまたはフィルターを選択してオーディエンスを絞り込み、[ユーザーをターゲット]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)する必要があります。このステップでは、セグメントからより大きなオーディエンスを選択し、必要に応じてフィルターを使用してそのセグメントをさらに絞り込みます。おおよそのセグメント人口のプレビューが自動的に表示されます。正確なセグメントメンバーシップは、メッセージが送信される前に常に計算されることに注意してください。

{% multi_lang_include audience/target_audiences.md %}

### コンバージョンイベントを選択する {#choose-conversion-events}

Brazeでは、キャンペーンを受信した後にユーザーが特定のアクション（[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)）を実行する頻度を追跡できます。ユーザーが指定されたアクションを実行した場合にコンバージョンがカウントされる最大30日間の期間を設定するオプションがあります。

{% endtab %}

{% tab キャンバス %}

まだ完了していない場合は、キャンバスステップの残りのセクションを完了してください。キャンバスの残りの構築方法、多変量テストとインテリジェントセレクションの実装方法などの詳細については、キャンバスドキュメントの[キャンバスを構築する]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas)ステップを参照してください。

{% endtab %}
{% endtabs %}

## ステップ6: 確認してデプロイする {#step-6-review-and-deploy}

キャンペーンまたはキャンバスの最後の構築が完了したら、詳細を確認し、テストしてから送信してください。

## 知っておくべきこと {#things-to-know}

### エラー、リトライロジック、タイムアウト {#errors-retry-logic-and-timeouts}

Webhookは、Brazeサーバーが外部エンドポイントにリクエストを行うことに依存しており、エラーが発生する場合があります。最も一般的なエラーには、構文エラー、期限切れのAPIキー、レート制限、予期しないサーバー側の問題があります。Webhookキャンペーンを送信する前に:

- Webhookの構文エラーをテストする
- パーソナライズされた変数にデフォルト値があることを確認する

Webhookの送信に失敗した場合、エラーメッセージが[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)に記録され、エラーのタイムスタンプ、アプリ名、エラーの詳細などの情報が含まれます。

![「現在のユーザーに関する情報を照会するには、アクティブなアクセストークンを使用する必要があります」というメッセージのWebhookエラー。]({% image_buster /assets/img_archive/webhook-error.png %})

エラーメッセージがエラーの原因について十分に明確でない場合は、使用しているAPIエンドポイントのドキュメントを確認してください。通常、エンドポイントが使用するエラーコードの説明と、その一般的な原因が記載されています。

#### レスポンスコードとリトライロジック {#response-codes-and-retry-logic}

Webhookリクエストが送信されると、受信サーバーはリクエストで何が起こったかを示すレスポンスコードを返します。以下の表は、サーバーが送信する可能性のあるさまざまなレスポンス、キャンペーン分析への影響、およびエラーの場合にBrazeがキャンペーンの再配信を試みるかどうかをまとめたものです:

| レスポンスコード | 受信済みとしてマーク？ | リトライ？ |
|---------------|-----------|----------|
| `20x`（成功）  | はい |   N/A  |
| `30x`（リダイレクト）  | いいえ | いいえ |
| `408`（リクエストタイムアウト）  | いいえ | はい |
| `429`（レート制限）  | いいえ | はい |
| `その他の4XX`（クライアントエラー）  | いいえ | いいえ |
| `5XX`（サーバーエラー）   | いいえ | はい |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="レスポンスコードとリトライロジック" }

{% alert note %}
Brazeは、このセクションで前述したステータスコードに対して、エクスポネンシャルバックオフを使用して30分以内に最大5回リトライします。エンドポイントに到達できない場合、リトライは24時間にわたって分散される場合があります。<br><br>各Webhookはタイムアウトまでに90秒が許可されています。
{% endalert %}

`Retry-After`およびレート制限レスポンスヘッダーは、**リトライ可能な**試行（たとえば、`408`、`429`、または`5XX`の後）までBrazeが待機する時間に影響を与える場合があります。これらは、`401`などのリトライ不可能なレスポンスをリトライ対象にするものではありません。

#### 認証とConnected Contentの認証情報 {#authentication-and-connected-content-credentials}

送信Webhook HTTPリクエストは、エンドポイントに対する認証に[Connected Contentの認証情報]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#authentication-types)（`:basic_auth`または`:auth_credentials`）のアタッチをサポートしていません。代わりに、Webhookの**リクエストヘッダー**を使用して認証を設定してください。送信時にトークンやシークレットを取得するには、ヘッダーまたはボディフィールドに{% raw %}`{% connected_content %}`{% endraw %}タグを配置して、Webhookが送信される前にLiquidが解決するようにできます。

#### 保存済みWebhookテンプレートとキャンペーンの使用状況 {#saved-webhook-templates-and-campaign-usage}

Brazeは、特定の**保存済みWebhookテンプレート**を参照するすべてのキャンペーンまたはキャンバスステップをリストする組み込みレポートを提供していません。使用状況を監査するには、同じURLとHTTPメソッドを使用するWebhookステップを確認するか、[Brazeサポート]({{site.baseurl}}/support_contact)にお問い合わせください。

#### トラブルシューティングと追加のエラー詳細 {#troubleshooting-and-additional-error-details}

特定のWebhookエラーの詳細な説明、トラブルシューティング手順、および解決ガイダンスについては、[WebhookとConnected Contentリクエストのトラブルシューティング]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content)を参照してください。また、異常ホスト検出システムの仕組みや、Brazeが自動メールおよびBraze Currentsの追加ログを通じてエラー通知を提供する方法についても説明しています。

### IP許可リスト {#ip-allowlisting}

WebhookがBrazeから送信されると、Brazeサーバーは顧客またはサードパーティのサーバーにネットワークリクエストを行います。IP許可リストを使用すると、WebhookリクエストがBrazeから送信されていることを確認でき、セキュリティの層を追加できます。

Brazeは以下のIPからWebhookを送信します。リストされたIPは、許可リストにオプトインされたすべてのAPIキーに自動的かつ動的に追加されます。

{% alert important %}
Braze間のWebhookを作成し、許可リストを使用している場合は、`127.0.0.1`を含む以下のすべてのIPを許可リストに追加する必要があります。
{% endalert %}

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### ユーザーの削除 {#delete-users}

個々のユーザーまたはセグメントのユーザーを削除するには、**オーディエンス** > **オーディエンスを管理** > **ユーザーを削除**に移動します。ダッシュボードは一括セグメント削除（最大1,000万プロファイル）をサポートしており、7日間のキャンセル期間が含まれ、共有REST APIレート制限を消費しません。手順、制限、権限については、[ユーザーの削除]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users)を参照してください。

プログラムによる小規模バッチの削除には、Webhookキャンペーンの代わりに[`/users/delete`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)を使用してください。