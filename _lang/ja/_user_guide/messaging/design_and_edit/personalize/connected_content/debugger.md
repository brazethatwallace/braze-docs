---
nav_title: Connected Contentデバッガー
article_title: Connected Contentデバッガー
page_order: 3.5
description: "このリファレンス記事では、メッセージの配信前に問題をトラブルシューティングするためのConnected Contentデバッガーの使用方法について説明します。"
---

# Connected Contentデバッガー {#connected-content-debugger}

> Connected Contentデバッガーを使用すると、各Connected Content呼び出しのライブリクエストとレスポンスを確認できるため、CampaignやCanvasを開始する前にエンドポイント、ヘッダー、Liquidタグを検証できます。

{% multi_lang_include alerts/early_access_beta_alert.md feature='Connected Content Debugger' %}

## デバッガーについて {#about-the-debugger}

Connected Contentを使用すると、レンダリング時に外部APIへHTTPコールを行い、そのレスポンスをLiquidでメッセージに挿入することで、リアルタイムデータでメッセージを充実させることができます。このコールはBrazeの外部で行われるため、CampaignやCanvasが公開される前に、Brazeがどのようなリクエストを送信したか、エンドポイントが何を返したか、またはコールが失敗した理由を正確に確認することが難しい場合があります。

Connected Contentデバッガーは、配信前にこれらの問題をトラブルシューティングするのに役立ちます。**プレビューとテスト**セクションで、メッセージ内のすべてのConnected Contentコールのライブリクエストとレスポンスを表示します。これにより、エンドポイント、ヘッダー、Liquidタグが正しく設定されていることを、Brazeダッシュボード内ですべて確認できます。

### サポートされているチャネル {#supported-channels}

Connected Contentデバッガーは、以下のチャネルで利用できます。

- Content Cards
- メール
    - テンプレートを含む
    - フッターと購読ページは除く
- アプリ内メッセージ
- プッシュ通知
- SMS/MMS/RCS
- Webhook
    - テンプレートを含む
- WhatsApp

{% alert note %}
早期アクセス期間中、デバッガーはほとんどのチャネルで利用できますが、KakaoTalk、LINE、バナー、またはチャネル固有でないコンポジションサーフェス（Content Blocks、Canvasのユーザー更新ステップ、コンテキストステップなど）ではまだ利用できません。デバッガーが表示されない場合、その機能ではConnected Contentのデバッグがまだサポートされていない可能性があります。
{% endalert %}

## デバッガーの使用 {#use-the-debugger}

プレビューを実行するたびに、Brazeは自動的にConnected Contentの呼び出し結果を**プレビュー**タブに表示します。デバッガーを使用するには:

1. {% raw %}`{% connected_content %}`{% endraw %}タグを使用してメッセージを設定します。
2. **プレビューとテスト**セクションに移動します。メッセージにConnected Contentタグが含まれている場合、Connected Contentの呼び出し数と成功・エラーのステータスを含むサマリービューが表示されます。

![テストセクション内のConnected Contentセクション。]({% image_buster /assets/img/connected_content/debugger1.png %})

{:start="3"}
3. **詳細を表示**を選択して、プレビューの横にデバッガーを開きます。ドロワーには、各Connected Content呼び出しのURLと結果のテーブルが表示されます。

![確認すべき3つのURLを含むConnected Content呼び出し。]({% image_buster /assets/img/connected_content/debugger3.png %})

{:start="4"}
4. 各URLと結果の横にある**表示**を選択すると、リクエストヘッダーとレスポンスヘッダー、ペイロード、メソッド、所要時間、キャッシュ情報を確認できます。

![リクエストとレスポンスの詳細を含むConnected Content呼び出し。]({% image_buster /assets/img/connected_content/debugger4.png %})

{:start="5"}
5. 結果を確認し、必要に応じてタグ、ヘッダー、またはエンドポイントを調整します。その後、新しいプレビューを生成して修正を確認します。

テンプレートに複数の{% raw %}`{% connected_content %}`{% endraw %}タグが含まれている場合、デバッガーは実行されたすべての呼び出しを一覧表示します。1つのテンプレートから複数のメッセージ本文をレンダリングするチャネル（例えば、HTML、プレーンテキスト、AMP本文を個別にレンダリングするメールや、デバイス固有の本文を個別にレンダリングするクイックプッシュなど）の場合、デバッガーは現在プレビュー中の本文だけでなく、すべての本文にわたるConnected Content呼び出しをすべて表示します。

## デバッグ出力を理解する {#understand-the-debug-output}

各Connected Contentの呼び出しには、それぞれ**Response**タブと**Request**タブが表示されます。**Response**タブは、呼び出しが成功したかどうかを確認する最初の指標となるため、デフォルトで表示されます。

### URLの詳細 {#url-details}

| フィールド | 説明 |
| --- | --- |
| URL | Brazeが呼び出した完全にレンダリングされたURLで、すべてのLiquidタグが解決された状態です。 |
| Method | 使用されたHTTPメソッド（GETまたはPOST）。 |
| Status code | エンドポイントが返したHTTPステータスコード（例：`200`、`404`、`500`）。Braze固有のコードについては、[レスポンスコードのトラブルシューティング](#troubleshooting-response-codes)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="URLの詳細" }

### Responseタブ {#response-tab}

| フィールド | 説明 |
| --- | --- |
| Duration | リクエストの完了にかかった時間（秒単位）。Durationはライブ（キャッシュされていない）呼び出しの場合にのみ表示されます。 |
| Served from cache | このレスポンスがエンドポイントへのライブ呼び出しではなく、BrazeのConnected Contentキャッシュから提供されたかどうかを示します（`Yes`または`No`）。キャッシュされた結果は以前のレスポンスを反映しており、エンドポイントの現在の状態とは限りません。 |
| Response body | エンドポイントが返したボディです。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Responseタブ" }

### Requestタブ {#request-tab}

| フィールド | 説明 |
| --- | --- |
| Headers | `:headers`で設定されたものを含む、Brazeが送信したリクエストヘッダーです。 |
| Body | 送信されたリクエストボディ（POSTリクエストの場合）。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requestタブ" }

## 認証情報のリダクション {#credential-redaction}

Connected Contentタグで`:basic_auth`、一般的なシークレットヘッダー、キー、またはその他の[認証情報オプション]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#authentication-types)を使用している場合、デバッガーは**リクエスト**タブでそれらの値をリダクションし、一連のアスタリスク（*）に置き換えます。これにより、**プレビュー＆テスト**で値を公開することなく、認証情報がリクエストに含まれていたことを確認できます。

認証情報がリダクションされている場合でも、認証の失敗は引き続き表示されます。エンドポイントが`401`または`403`を返した場合、そのステータスコードは**レスポンス**タブに通常どおり表示されるため、認証情報自体は非表示であっても、認証の問題によりリクエストが拒否されたことを判断できます。

## レスポンスコードのトラブルシューティング {#troubleshooting-response-codes}

### エンドポイントエラーとBrazeが課す制限 {#endpoint-errors-versus-braze-imposed-limits}

**レスポンス**タブに表示されるすべての非`2XX`ステータスコードがエンドポイントから返されたものとは限りません。BrazeはConnected Contentの呼び出しに独自の制限を課しており、これらがエンドポイントエラーに似たレスポンスを生成することがあります。

`408`、`429`、`502`、`503`、`504`、`599`などの[レスポンスコード]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content#start-here-match-your-symptom)が表示される場合、問題は通常Braze側の呼び出しに関連しており、ホストの状態、タイムアウト、またはペイロードサイズに起因します。エンドポイントが常に大きなレスポンスを返す場合は、メッセージに必要なフィールドのみにレスポンスペイロードを絞り込むことを検討してください。

### エンドポイントが予期しないステータスコードを返した場合 {#endpoint-returned-an-unexpected-status-code}

**リクエスト**タブを使用して、Brazeが送信した正確なURL、ヘッダー、本文を確認してください。予期しない`4XX`レスポンスの一般的な原因は、URL、ヘッダー、または本文内のLiquidタグが期待どおりに解決されなかったことです。{% raw %}`{{ }}`{% endraw %}の参照が、プレビューに使用しているユーザーまたはコンテキストに存在するフィールドを指しているか確認してください。

### レスポンスが古い場合 {#response-looks-stale}

**レスポンス**タブの**キャッシュから提供**を確認してください。`Yes`と表示されている場合、デバッガーは新しい呼び出しではなく、以前にキャッシュされたレスポンスを表示しています。現在のエンドポイントの動作を確認するには、タグに一時的に`:no_cache`を追加するか、キャッシュの有効期限（`:cache_max_age`に基づく）が切れるのを待ってください。

## 関連記事 {#related-articles}

- [Connected Contentリファレンス]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [Connected Content API呼び出しを行う]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call)
- [WebhookとConnected Contentリクエストのトラブルシューティング]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/troubleshooting_webhooks_and_connected_content)