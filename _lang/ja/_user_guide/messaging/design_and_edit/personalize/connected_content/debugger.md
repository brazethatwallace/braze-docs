---
nav_title: Connected Contentデバッガー
article_title: Connected Contentデバッガー
page_order: 3.5
description: "このリファレンス記事では、メッセージの配信前に問題をトラブルシューティングするためのConnected Contentデバッガーの使用方法について説明します。"
---

# Connected Contentデバッガー {#connected-content-debugger}

> Connected Contentデバッガーを使用すると、各Connected Content呼び出しのライブリクエストとレスポンスを確認できるため、キャンペーンやキャンバスを開始する前にエンドポイント、ヘッダー、Liquidタグを検証できます。

## デバッガーについて {#about-the-debugger}

Connected Contentを使用すると、レンダリング時に外部APIへHTTPコールを行い、そのレスポンスをLiquidでメッセージに挿入することで、リアルタイムデータでメッセージを充実させることができます。このコールはBrazeの外部で行われるため、キャンペーンやキャンバスが本番稼働する前に、Brazeが送信したリクエストの内容、エンドポイントが返したレスポンス、またはコールが失敗した理由を正確に確認することが困難な場合があります。

Connected Contentデバッガーは、ローンチ前にこれらの問題をトラブルシューティングするのに役立ちます。メッセージ内のすべてのConnected Contentコールについて、ライブのリクエストとレスポンスを**プレビューとテスト**セクションで確認できます。これにより、エンドポイント、ヘッダー、Liquidタグが正しく設定されているかどうかを、Brazeダッシュボード内ですべて確認できます。

### サポート対象エリア {#supported-areas}

Connected Contentデバッガーは、以下のエリアで利用可能です。

- キャンバスのコンテキストステップ
- Content Cards
- メール
    - テンプレートを含む
    - フッターと購読ページは除外
- アプリ内メッセージ
- プッシュ通知
- SMS/MMS/RCS
- Webhook
    - テンプレートを含む
- WhatsApp

{% alert note %}
デバッガーはほとんどのチャネルで利用可能ですが、KakaoTalk、LINE、バナー、およびチャネル固有でない作成画面（コンテンツブロックやキャンバスのユーザー更新ステップなど）にはまだ対応していません。デバッガーが表示されない場合は、その機能ではConnected Contentのデバッグがまだサポートされていない可能性があります。
{% endalert %}

## デバッガーの使用 {#use-the-debugger}

プレビューを実行するたびに、BrazeはConnected Contentの呼び出し結果を**プレビュー**タブに自動的にレンダリングします。デバッガーを使用するには：

1. {% raw %}`{% connected_content %}`{% endraw %}タグを使用してメッセージを設定します。
2. **プレビューとテスト**セクションに移動します。メッセージにConnected Contentタグが含まれている場合、Connected Contentの呼び出し数と成功およびエラーのステータスを含むサマリービューを確認できます。

![テストセクション内のConnected Contentセクション。]({% image_buster /assets/img/connected_content/debugger1.png %})

{:start="3"}
3. **詳細を表示**を選択して、プレビューの横にデバッガーを開きます。ドロワーには、各Connected Content呼び出しのURLと結果のテーブルが表示されます。

![確認する3つのURLを含むConnected Contentの呼び出し。]({% image_buster /assets/img/connected_content/debugger3.png %})

{:start="4"}
4. 各URLと結果の横にある**表示**を選択すると、リクエストヘッダーとレスポンスヘッダー、ペイロード、メソッド、所要時間、キャッシュ情報を確認できます。

![リクエストとレスポンスの詳細を含むConnected Contentの呼び出し。]({% image_buster /assets/img/connected_content/debugger4.png %})

{:start="5"}
5. 結果を確認し、必要に応じてタグ、ヘッダー、またはエンドポイントを調整します。その後、新しいプレビューを生成して修正を確認します。

テンプレートに複数の{% raw %}`{% connected_content %}`{% endraw %}タグが含まれている場合、デバッガーは行われたすべての呼び出しを一覧表示します。1つのテンプレートから複数のメッセージ本文をレンダリングするチャネル（例えば、HTML、プレーンテキスト、AMP本文を個別にレンダリングするメールや、デバイス固有の本文を個別にレンダリングするクイックプッシュ）では、デバッガーは現在プレビュー中の本文だけでなく、すべての本文にわたって行われたすべてのConnected Content呼び出しを表示します。

## デバッグ出力を理解する {#understand-the-debug-output}

各Connected Contentの呼び出しには、それぞれ固有の**Response**タブと**Request**タブが表示されます。呼び出しが成功したかどうかを確認する最初の指標となるため、デフォルトでは**Response**タブが表示されます。

### URLの詳細 {#url-details}

| フィールド | 説明 |
| --- | --- |
| URL | BrazeがLiquidタグをすべて解決した状態で呼び出した、完全にレンダリングされたURL。 |
| Method | 使用されたHTTPメソッド（GETまたはPOST）。 |
| Status code | エンドポイントが返したHTTPステータスコード（例：`200`、`404`、`500`）。Braze固有のコードについては、[レスポンスコードのトラブルシューティング](#troubleshooting-response-codes)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="URLの詳細" }

### Responseタブ {#response-tab}

| フィールド | 説明 |
| --- | --- |
| Duration | リクエストの完了にかかった時間（秒単位）。Durationはライブ（キャッシュされていない）呼び出しの場合にのみ表示されます。 |
| Served from cache | このレスポンスがエンドポイントへのライブ呼び出しではなく、BrazeのConnected Contentキャッシュから提供されたかどうかを示します（`Yes`または`No`）。キャッシュされた結果は以前のレスポンスを反映しており、必ずしもエンドポイントの現在の状態を示すものではありません。 |
| Response body | エンドポイントが返したレスポンスボディ。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Responseタブ" }

### Requestタブ {#request-tab}

| フィールド | 説明 |
| --- | --- |
| Headers | Connected Contentタグからのヘッダー（`:headers`、認証情報、`:content_type`などのオプション）。 |
| Body | 送信されたリクエストボディ（POSTリクエストの場合）。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requestタブ" }

## デバッガーに表示されるリクエストヘッダー {#which-request-headers-appear-in-the-debugger}

**Request**タブには、Connected Contentタグからのヘッダーが表示されます。カスタム`:headers`、保存された認証情報、`:content_type`や`:basic_auth`などのタグオプションで設定されたヘッダーが含まれます。Brazeは、エンドポイントへの送信リクエストに標準ヘッダー（例：`User-Agent`や`Host`）も追加します。これらのBrazeが追加したヘッダーは、`:headers`で設定した場合にデバッガーに表示されます。

{% alert note %}
一貫した`User-Agent`を送信するには、`:headers`で設定してください。Brazeはその値を使用し、デバッガーにそのヘッダーが表示されます。
{% endalert %}

{% multi_lang_include connected_content/outgoing_request_headers.md %}

## 認証情報のリダクション {#credential-redaction}

Connected Contentタグで`:basic_auth`、一般的なシークレットヘッダー、キー、またはその他の[認証情報オプション]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#authentication-types)を使用している場合、デバッガーは**Request**タブでそれらの値をリダクションし、一連のアスタリスク（*）に置き換えます。これにより、**プレビューとテスト**で値を公開することなく、認証情報がリクエストに含まれていることを確認できます。

認証情報がリダクションされている場合でも、認証の失敗は表示されます。エンドポイントが`401`または`403`を返した場合、そのステータスコードは**Response**タブに通常どおり表示されるため、認証情報自体は非表示であっても、認証の問題によりリクエストが拒否されたことを判断できます。

## レスポンスコードのトラブルシューティング {#troubleshooting-response-codes}

### エンドポイントエラーとBrazeが課す制限 {#endpoint-errors-versus-braze-imposed-limits}

**Response**タブに表示される非`2XX`ステータスコードのすべてがエンドポイントから返されるわけではありません。BrazeはConnected Contentの呼び出しに対して独自の制限を適用しており、これらはエンドポイントエラーと似たレスポンスを生成することがあります。

`408`、`429`、`502`、`503`、`504`、`599`などの[レスポンスコード]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#start-here-match-your-symptom)が表示される場合、問題は通常Braze側の呼び出しに関連しており、ホストの状態、タイムアウト、またはペイロードサイズが原因です。エンドポイントが一貫して大きなレスポンスを返す場合は、メッセージに必要なフィールドのみにレスポンスペイロードをトリミングすることを検討してください。

### エンドポイントが予期しないステータスコードを返した {#endpoint-returned-an-unexpected-status-code}

**Request**タブを使用して、URL、タグからのヘッダー、およびボディを確認してください。予期しない`4XX`レスポンスの一般的な原因は、URL、ヘッダー、またはボディ内のLiquidタグが期待どおりに解決されなかったことです。{% raw %}`{{ }}`{% endraw %}の参照が、プレビューに使用しているユーザーまたはコンテキストに存在するフィールドを指していることを確認してください。

### レスポンスが古く見える {#response-looks-stale}

**Response**タブの**Served from cache**を確認してください。`Yes`と表示されている場合、デバッガーは新しい呼び出しではなく、以前にキャッシュされたレスポンスを表示しています。現在のエンドポイントの動作を確認するには、一時的にタグに`:no_cache`を追加するか、キャッシュが期限切れになるのを待ってください（`:cache_max_age`に従います）。

## 関連記事 {#related-articles}

- [コネクテッドコンテンツリファレンス]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [Connected Content API呼び出しを行う]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)
- [送信リクエストヘッダー]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#outgoing-request-headers)
- [WebhookとConnected Contentリクエストのトラブルシューティング]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content)