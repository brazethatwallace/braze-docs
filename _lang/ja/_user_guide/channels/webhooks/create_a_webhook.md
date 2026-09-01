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

メッセージをキャンペーンで送信するべきか、キャンバスで送信するべきかわからない場合は、キャンペーンは単発のターゲットメッセージングに適しており、キャンバスは複数ステップのユーザージャーニーに適しています。

{% tabs %}
{% tab キャンペーン %}

**ステップ:**

1. **メッセージング** > **キャンペーン**に移動し、**キャンペーンを作成**を選択します。
2. **Webhook**を選択するか、複数チャネルをターゲットとするキャンペーンの場合は**マルチチャネル**を選択します。
3. キャンペーンにわかりやすく意味のある名前を付けます。
4. (オプション) このキャンペーンの用途を説明する説明を追加します。
4. 必要に応じて[チーム]({{site.baseurl}}/user_guide/administer/global/user_management/teams)と[タグ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)を追加します。
   * タグを使用すると、キャンペーンを簡単に検索したり、レポートを作成したりできます。たとえば、[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reports/report_builder)を使用する際に、特定のタグでフィルターできます。
5. キャンペーンに必要な数だけバリアントを追加し、名前を付けます。追加したバリアントごとに異なるWebhookテンプレートを選択できます。このトピックの詳細については、[多変量テストとABテスト]({{site.baseurl}}/user_guide/messaging/ab_testing)を参照してください。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似している、または同じコンテンツの場合は、追加のバリアントを追加する前にメッセージを作成してください。その後、**バリアントを追加**ドロップダウンから**バリアントからコピー**を選択できます。
{% endalert %}

{% endtab %}
{% tab キャンバス %}

**ステップ:**

{% multi_lang_include messaging/canvas_message_step_setup.md %}

{% endtab %}
{% endtabs %}

## ステップ2: Webhookを作成する {#step-2-build-your-webhook}

Webhookをゼロから作成するか、既存のテンプレートを使用するか、Brazeが提供するテンプレートを使用するかを選択できます。次に、エディターの**作成**タブでWebhookを作成します。

**作成**タブは以下のフィールドで構成されています。

- 言語
- Webhook URL
- HTTP メソッド
- リクエストボディ

![Webhookテンプレートの例が表示された「作成」タブ。]({% image_buster /assets/img_archive/webhook_compose.png %})

### 言語 {#internationalization}

URLとリクエストボディで[国際化]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization)がサポートされています。メッセージを国際化するには、**言語を追加**を選択し、必須フィールドに入力します。

コンテンツを作成する前に言語を選択することをお勧めします。そうすることで、Liquid内の適切な箇所にテキストを入力できます。利用可能な言語の完全なリストについては、[サポートされている言語]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization#languages-supported)を参照してください。

右から左に書く言語でコピーを追加する場合、右から左へのメッセージの最終的な表示はサービスプロバイダーのレンダリング方法に大きく依存します。できるだけ正確に表示される右から左へのメッセージの作成に関するベストプラクティスについては、[右から左へのメッセージの作成]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages)を参照してください。

### Webhook URL {#webhook-url}

Webhook URL（HTTP URL）はエンドポイントを指定します。エンドポイントは、Webhookでキャプチャした情報を送信する場所です。

ベンダーに情報を送信する場合、ベンダーがAPI ドキュメントでこのURLを提供しているはずです。自社のシステムに情報を送信する場合は、開発チームに確認して正しいURLを使用していることを確認してください。

Brazeでは、標準ポート`80`（HTTP）および`443`（HTTPS）で通信するURLのみが許可されています。

#### Liquidの使用 {#using-liquid}

[Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)を使用してWebhook URLをパーソナライズできます。特定のエンドポイントでは、ユーザーの識別やユーザー固有の情報をURLの一部として提供する必要がある場合があります。Liquidを使用する場合は、URLで使用するユーザー固有の情報ごとに[デフォルト値]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web)を含めるようにしてください。

### HTTP メソッド {#http-method}

使用すべきHTTPメソッドは、情報を送信するエンドポイントによって異なります。ほとんどの場合、POSTを使用します。

| HTTP メソッド | 説明 |
| ----------- | ----------- |
| POST | 受信サーバーに新しい情報を書き込みます。データを送信する際に最も一般的に使用されるメソッドです。 |
| GET | 新しい情報を書き込むのではなく、既存の情報を取得します。定義上、GETリクエストはリクエストボディをサポートしません。 |
| PUT | エンドポイントの情報を更新し、既存の情報をリクエストボディの内容で置き換えます。 |
| DELETE | HTTP URLのリソースを削除します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="HTTPメソッド" }

### リクエストボディ {#request-body}

リクエストボディは、指定したURLに送信される情報です。Webhookリクエストのボディは、JSONのキーと値のペアまたはローテキストで作成できます。

#### JSONのキーと値のペア {#json-key-value-pairs}

JSONのキーと値のペアを使用すると、JSON形式を期待するエンドポイントへのリクエストを簡単に作成できます。これはJSONリクエストを期待するエンドポイントでのみ使用できます。例えば、キーが`message_body`の場合、対応する値は`Your order just arrived!`のようになります。キーと値のペアを入力すると、コンポーザーがリクエストをJSON構文で設定し、JSONリクエストのプレビューが自動的に表示されます。

![JSONのキーと値のペアに設定されたリクエストボディ。]({% image_buster /assets/img/webhook_json_1.png %})

Liquidを使用してキーと値のペアをパーソナライズできます。例えば、任意のユーザー属性、[カスタム属性]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids#additional-notes-and-best-practices)、または[イベントプロパティ]({{site.baseurl}}/user_guide/data/activation/events/custom_events)をリクエストに含めることができます。例えば、顧客の名とメールアドレスをリクエストに含めることができます。各属性に[デフォルト値]({{site.baseurl}}/developer_guide/analytics/setting_user_ids?tab=web)を含めるようにしてください。

#### ローテキスト {#raw-text}

ローテキストオプションでは、任意の形式のボディを期待するエンドポイントへのリクエストを柔軟に作成できます。例えば、XML形式のリクエストを期待するエンドポイントへのリクエストを作成する場合に使用できます。

ローテキストでは、Liquidを使用した[パーソナライゼーション]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)と[国際化]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization)の両方がサポートされています。

![Liquidを使用したローテキストのリクエストボディの例。]({% image_buster /assets/img_archive/webhook_rawtext.png %})

`Content-Type`[リクエストヘッダー](#request-headers-optional)を`application/x-www-form-url-encoded`に設定した場合、リクエストボディはURLエンコードされた文字列としてフォーマットする必要があります。例：

{% raw %}
```
to={{custom_attribute.${example}}}&text=Your+order+just+arrived
```
{% endraw %}

![URLエンコードされた文字列を含むリクエストボディ。]({% image_buster /assets/img_archive/webhook_rawtext_URL-encoded.png %})

## ステップ3: 追加設定を構成する {#step-3-configure-additional-settings}

### リクエストヘッダー（オプション） {#request-headers-optional}

特定のエンドポイントでは、リクエストにヘッダーを含める必要がある場合があります。コンポーザーの**作成**セクションで、必要な数だけヘッダーを追加できます。

![「Authorization」キーと「Content-Type」キーのリクエストヘッダーの例。]({% image_buster /assets/img_archive/webhook_request_headers_example.png %})

一般的なリクエストヘッダーには、[`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type) 指定（ボディに含まれるデータの種類を記述するもので、XML や JSON などがあります）と、ベンダーやシステムの認証情報を含む [`Authorization`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization) ヘッダーがあります。

{% alert note %}
HTTP ヘッダー名は、[RFC 7230 セクション 3.2（「各ヘッダーフィールドは大文字と小文字を区別しないフィールド名で構成されます」）](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2)に基づき、大文字と小文字を区別しません。受信エンドポイントや中間サービス（CDN など）がヘッダーの大文字小文字を変換しても、ヘッダーの処理には影響しません。`Content-Type`、`content-type`、`CONTENT-TYPE` はすべて同一として扱われます。
{% endalert %}

Content-Type 指定にはキー `Content-Type` を使用する必要があります。一般的な値は `application/json` または `application/x-www-form-urlencoded` です。

Authorization ヘッダーにはキー `Authorization` を使用する必要があります。一般的な値は {% raw %} `Bearer {{YOUR_TOKEN}}` または `Basic {{YOUR_TOKEN}}` {% endraw %} です。ここで `YOUR_TOKEN` はベンダーやシステムから提供された認証情報です。

## ステップ4：メッセージのテスト送信 {#step-4-test-send-your-message}

キャンペーンを公開する前に、Brazeではwebhookをテストしてリクエストが正しくフォーマットされていることを確認することをお勧めします。

テストするには、**テスト**タブに切り替えてテストwebhookを送信します。ランダムなユーザー、特定のユーザー（メールアドレスまたは外部ユーザーIDを入力）、または任意の属性を持つカスタマイズされたユーザーとしてwebhookをテストできます。

テストwebhookを送信すると、レスポンスメッセージを含むダイアログが表示されます。webhookリクエストが失敗した場合は、エラーメッセージを参照してwebhookのトラブルシューティングを行ってください。以下の例は、無効なwebhook URLを使用した場合のwebhookのレスポンスの詳細を示しています。

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

## ステップ5: キャンペーンまたはキャンバスの残りの部分を構築する {#step-5-build-the-remainder-of-your-campaign-or-canvas}

{% tabs %}
{% tab キャンペーン %}

次に、キャンペーンの残りの部分を構築します。webhookを構築するためのツールの最適な使い方については、以下のセクションを参照してください。

### 配信スケジュールまたはトリガーを選択する {#choose-delivery-schedule-or-trigger}

webhookは、スケジュールされた時間、アクション、またはAPIトリガーに基づいて配信できます。詳細については、[キャンペーンのスケジュール設定]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)を参照してください。

アクションベースの配信では、キャンペーンの期間と[サイレント時間]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/quiet_hours)も設定できます。

このステップでは、ユーザーがキャンペーンを[再度受け取れる]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/re_eligibility#turning-on-re-eligibility)ようにしたり、[フリークエンシーキャップ]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#about-frequency-capping)ルールを有効にしたりするなど、配信コントロールを指定することもできます。

### ターゲットユーザーを選択する {#choose-users-to-target}

次に、セグメントまたはフィルターを選択してオーディエンスを絞り込み、[ユーザーをターゲット]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)にする必要があります。このステップでは、セグメントからより大きなオーディエンスを選択し、必要に応じてフィルターでそのセグメントをさらに絞り込みます。概算のセグメント人数のプレビューが自動的に表示されます。正確なセグメントメンバーシップは常にメッセージ送信前に計算されることにご注意ください。

{% multi_lang_include audience/target_audiences.md %}

### コンバージョンイベントを選択する {#choose-conversion-events}

Brazeでは、キャンペーンを受信した後にユーザーが特定のアクション（[コンバージョンイベント]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)）を実行する頻度を追跡できます。ユーザーが指定したアクションを実行した場合にコンバージョンとしてカウントされる最大30日間のウィンドウを設定するオプションがあります。

{% endtab %}

{% tab キャンバス %}

まだ完了していない場合は、キャンバスステップの残りのセクションを完了してください。多変量テストや[BrazeAI<sup>TM</sup>による最適化]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#optimize-canvas-variants-with-brazeai)など、キャンバスの残りの構築に関する詳細については、[キャンバスの構築]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#step-2-build-your-canvas)を参照してください。

{% endtab %}
{% endtabs %}

## ステップ6: 確認とデプロイ {#step-6-review-and-deploy}

キャンペーンまたはキャンバスの構築が完了したら、詳細を確認し、テストを行ってから送信します。

## 知っておくべきこと {#things-to-know}

### エラー、リトライロジック、タイムアウト {#errors-retry-logic-and-timeouts}

Webhookは、Brazeサーバーが外部エンドポイントにリクエストを送信する仕組みに依存しているため、エラーが発生することがあります。最も一般的なエラーには、構文エラー、期限切れのAPIキー、レート制限、予期しないサーバー側の問題などがあります。webhookキャンペーンを送信する前に：

- webhookの構文エラーをテストしてください
- パーソナライズされた変数にデフォルト値が設定されていることを確認してください

webhookの送信に失敗すると、[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)にエラーメッセージが記録され、エラーのタイムスタンプ、アプリ名、エラーの詳細などの情報が含まれます。

![「An active access token must be used to query information about the current user」というメッセージのwebhookエラー。]({% image_buster /assets/img_archive/webhook-error.png %})

エラーメッセージだけではエラーの原因が十分に明確でない場合は、使用しているAPIエンドポイントのドキュメントを確認してください。通常、エンドポイントが使用するエラーコードの説明と、その一般的な原因が記載されています。

#### レスポンスコードとリトライロジック {#response-codes-and-retry-logic}

webhookリクエストが送信されると、受信サーバーはリクエストに対して何が起こったかを示すレスポンスコードを返します。以下の表は、サーバーが返す可能性のあるさまざまなレスポンス、キャンペーン分析への影響、およびエラーの場合にBrazeがキャンペーンの再配信を試みるかどうかをまとめたものです。

| レスポンスコード | 受信済みとしてマーク？ | リトライ？ |
|---------------|-----------|----------|
| `20x`（成功）  | はい |   該当なし  |
| `30x`（リダイレクト）  | いいえ | いいえ |
| `408`（リクエストタイムアウト）  | いいえ | はい |
| `429`（レート制限）  | いいえ | はい |
| `その他の4XX`（クライアントエラー）  | いいえ | いいえ |
| `5XX`（サーバーエラー）   | いいえ | はい |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="レスポンスコードとリトライロジック" }

{% alert note %}
Brazeは、このセクションで前述したステータスコードに対して、指数バックオフを使用して30分以内に最大5回リトライします。エンドポイントに到達できない場合、リトライは24時間にわたって分散される場合があります。<br><br>各webhookは、タイムアウトまでに90秒が許可されています。
{% endalert %}

`Retry-After` およびレート制限レスポンスヘッダーは、**リトライ可能な**試行（例：`408`、`429`、`5XX`の後）までBrazeが待機する時間に影響を与えることがあります。これらのヘッダーは、`401`などのリトライ不可のレスポンスをリトライ対象にするものではありません。

<!-- support-analyzer-phase2:webhook_delivery_failures -->
{% alert note %}
webhook送信が分析に表示されていないように見える場合は、キャンペーンまたはキャンバスステップの[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log)を開いてください。Brazeは特定のレスポンス（例：`408`、`429`、`5XX`）のみをリトライします。`401 Unauthorized`を含むほとんどの`4XX`クライアントエラーはリトライ**されません**。完全なレスポンス表については、[レスポンスコードとリトライロジック](#response-codes-and-retry-logic)を参照してください。
{% endalert %}


#### 403 Forbiddenとip許可リスト {#403-forbidden-and-ip-allowlisting} {#ip-allowlisting}

`403 Forbidden`レスポンスは、エンドポイントがリクエストを受信したが拒否したことを意味します。一般的な原因には、無効または欠落した認証、不十分なAPI権限、およびBrazeのアウトバウンドIPアドレスをブロックするネットワークルール（ファイアウォールやWebアプリケーションファイアウォールなど）があります。

webhookリクエストが一貫して`403`を返し、認証ヘッダーが正しい場合は、webhookを受信するサーバーでクラスターのBraze IPを許可リストに追加してください。[IP許可リスト](#ip-allowlisting)を参照してください。Connected Contentリクエストは同じアウトバウンドIPを使用します。[Connected Content IP許可リスト]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#connected-content-ip-allowlisting)を参照してください。

その他の`4XX`のトラブルシューティング手順については、[webhookとConnected Contentリクエストのトラブルシューティング]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#4xx-errors)を参照してください。

#### 認証とConnected Contentの認証情報 {#authentication-and-connected-content-credentials}

アウトバウンドwebhook HTTPリクエストは、エンドポイントに対して認証するための[Connected Content認証情報]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#authentication-types)（`:basic_auth`または`:auth_credentials`）の付与をサポートしていません。代わりに、webhookの**リクエストヘッダー**を使用して認証を設定してください。送信時にトークンやシークレットを取得するには、ヘッダーまたは本文フィールドに{% raw %}`{% connected_content %}`{% endraw %}タグを配置することで、webhookが送信される前にLiquidが解決します。

#### 保存済みwebhookテンプレートとキャンペーンの使用状況 {#saved-webhook-templates-and-campaign-usage}

Brazeは、特定の**保存済みwebhookテンプレート**を参照しているすべてのキャンペーンまたはキャンバスステップを一覧表示する組み込みレポートを提供していません。使用状況を監査するには、同じURLとHTTPメソッドを使用するwebhookステップを確認するか、[Brazeサポート]({{site.baseurl}}/support_contact)に連絡してください。

#### トラブルシューティングと追加のエラー詳細 {#troubleshooting-and-additional-error-details}

詳細な説明、トラブルシューティング手順、および特定のwebhookエラーの解決に関するガイダンスについては、[webhookとConnected Contentリクエストのトラブルシューティング]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content)を参照してください。異常ホスト検出システムの仕組みや、Brazeが自動メールおよびBraze Currentsの追加ログを通じてエラー通知を提供する方法についても説明されています。

### IP許可リスト {#ip-allowlisting}

webhookがBrazeから送信されると、Brazeサーバーは顧客またはサードパーティのサーバーにネットワークリクエストを行います。IP許可リストを使用すると、webhookリクエストがBrazeから送信されていることを確認でき、セキュリティのレイヤーを追加できます。

Brazeは以下のIPからwebhookを送信します。リストされたIPは、許可リストにオプトインされたAPIキーに自動的かつ動的に追加されます。

{% alert important %}
Braze間のwebhookを作成し、許可リストを使用している場合は、`127.0.0.1`を含む以下のすべてのIPを許可リストに追加する必要があります。
{% endalert %}

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### ユーザーの削除 {#delete-users}

個々のユーザーまたはセグメントのユーザーを削除するには、**オーディエンス** > **オーディエンスを管理** > **ユーザーの削除**に移動します。ダッシュボードはセグメントの一括削除（最大1,000万プロファイル）をサポートし、7日間のキャンセル期間が含まれ、共有REST APIレート制限を消費しません。手順、制限、権限については、[ユーザーの削除]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/delete_users)を参照してください。

より小さなバッチでのプログラムによる削除には、webhookキャンペーンの代わりに[`/users/delete`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)を使用してください。