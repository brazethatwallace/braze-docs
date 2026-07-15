---
nav_title: Stayfilm
article_title: Stayfilm
description: "Webhookキャンペーン、Connected Content、データ変換を使用して、StayfilmのパーソナライズされたビデオレンダリングをBrazeと統合する方法を説明します。"
alias: /partners/stayfilm/
page_type: partner
search_tag: Partner
---

# Stayfilm

> [Stayfilm](https://www.stayfilm.com/)は、大規模な自動パーソナライズビデオ制作のためのREST APIです。このプラットフォームは、データ、画像、テキスト、サウンドトラック、ナレーション、ビジュアルエフェクトを統合し、eコマース、マーケットプレイス、CRMワークフロー、マーケティングキャンペーン向けにカスタマイズされたビデオコンテンツを生成します。
>
> この統合では、BrazeからStayfilm APIにレンダリングジョブを送信し、ビデオの準備が完了するとコールバックを受信し、キャンペーンやキャンバスで使用するためにビデオURLとステータスをユーザープロファイルに保存します。

_この統合はStayfilmによって管理されています。_

## ユースケース {#use-cases}

Stayfilmは、以下を含むカスタマーライフサイクル全体にわたるパーソナライズされたビデオ配信をサポートしています。

- **オンボーディングとウェルカムジャーニー：** プロファイルやサインアップのコンテキストに合わせてパーソナライズされたビデオで新規ユーザーを歓迎します
- **商品およびマーケットプレイスコンテンツ：** カタログやユーザー提供のメディアから商品に焦点を当てたビデオを生成します
- **コンバージョンとアクティベーション：** 文脈に応じたビデオメッセージングで重要なアクションを強化します
- **ロイヤルティとアップセル：** パーソナライズされたオファーや利用マイルストーンをビデオ形式でハイライトします
- **奪還と離脱防止：** カスタマイズされたビデオコンテンツで非アクティブなユーザーを再エンゲージします

## 前提条件 {#prerequisites}

開始する前に、以下を確認してください。

| 要件 | 説明 |
| ----------- | ----------- |
| Stayfilm APIアクセス | Stayfilmに連絡して、`idproject`、`Subscription-Key`、OAuthクライアント認証情報、Stayfilm APIベースURLを含むプロジェクト認証情報を取得してください。認証とエンドポイントの詳細については、[Stayfilm APIドキュメント](https://apidoc.stayfilm.com)を参照してください。 |
| Brazeデータ変換 | [Brazeデータ変換]({{site.baseurl}}/user_guide/data/unification/data_transformation)を使用して、Stayfilmのコールバックを受信し、[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を通じてBrazeユーザープロファイルにマッピングします。 |
| Brazeユーザー識別子 | このウォークスルーでは、`external_id`を使用してStayfilmジョブをBrazeユーザープロファイルと関連付けます。`CallbackRelayData`で渡す値は、Brazeのユーザーの`external_id`と一致する必要があります。 |
| Brazeサンドボックス（推奨） | 本番環境にデプロイする前に、Brazeサンドボックスワークスペースで統合をテストしてください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合の仕組み {#how-the-integration-works}

この統合は双方向のWebhookフローを使用します。

1. **アウトバウンド：** Brazeの[Webhookキャンペーン]({{site.baseurl}}/user_guide/channels/webhooks)がStayfilmの`POST /Job`エンドポイントにレンダリングジョブを送信します。リクエストには、ユーザーメディア、テンプレート設定、およびBrazeユーザーの`external_id`に設定された`CallbackRelayData`が含まれます。
2. **インバウンド：** Stayfilmがレンダリングを完了すると、Brazeデータ変換のWebhook URLにコールバックを送信します。変換により、レスポンスが一致するユーザープロファイルの[カスタム属性]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)とカスタムイベントにマッピングされます。
3. **配信：** 保存された`stayfilm_video_url`属性を、カスタムHTMLを使用した[アプリ内メッセージ]({{site.baseurl}}/user_guide/channels/in_app_messages)などのメッセージングチャネルで使用します。

このウォークスルーのデータ変換は、以下のカスタム属性を書き込みます。

| 属性 | 説明 |
| --------- | ----------- |
| `stayfilm_video_status` | レンダリングが成功した場合は`ready`、Stayfilmがエラーを報告した場合は`failed` |
| `stayfilm_video_url` | レンダリングされたMP4ビデオのURL |
| `stayfilm_job_id` | Stayfilmジョブ識別子 |
| `stayfilm_render_error` | レンダリング失敗時のエラーメッセージ |
| `stayfilm_callback_received_at` | コールバックのISOタイムスタンプ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Custom attributes" }

変換では、`stayfilm_video_ready`または`stayfilm_video_failed`という名前のカスタムイベントも記録されます。

## 統合 {#integration}

以下のステップでは、概念実証について説明します。フローを検証した後、ジョブペイロード、属性、メッセージングをユースケースに合わせて調整してください。

### ステップ1：テストユーザーを作成する {#step-1-create-a-test-user}

統合の構築と検証に使用するテストユーザープロファイルを作成します。詳細については、[ユーザーのインポート]({{site.baseurl}}/user_guide/audience/manage_audience/import_users)を参照してください。

1. **オーディエンス** > **ユーザーのインポート**に移動します。
2. **クイックユーザー追加**を選択します。
3. `external_id`とその他の必須フィールドを入力し、**新規ユーザーを作成**を選択します。

{% alert important %}
メール、電話番号、氏名、政府発行ID、住所、注文の詳細などの個人データを`external_id`として使用しないでください。この統合全体を通じて、`external_id`は大文字と小文字を区別するものとして扱ってください。
{% endalert %}

このウォークスルーでは、`stayfilm-poc-001`をサンプルの`external_id`として使用します。後のステップで使用するため、選択した値をメモしておいてください。

### ステップ2：データ変換を作成する {#step-2-create-a-data-transformation}

Stayfilmのコールバックを受信し、ユーザープロファイルを更新するためのデータ変換を作成します。

1. **データ設定** > **データ変換**に移動します。
2. **変換を作成**を選択します。
3. `Stayfilm Callback Data Transformation`などの名前を入力します。
4. **編集エクスペリエンス**で、**ゼロから始める**を選択します。
5. **送信先を選択** > **送信先**で、**POST: Track users**を選択します。
6. **変換を作成**を選択します。
7. デフォルトの変換コードを以下に置き換えます。

```javascript
const brazeExternalId = payload.RelayedData;
if (!brazeExternalId) {
  throw new Error("Missing RelayedData. Expected Stayfilm callback to relay the Braze external_id from CallbackRelayData.");
}

const idJob = payload.IdJob || null;
const producedFiles = payload.ProducedFiles || {};
const videoUrl = producedFiles?.Videos?.VideoMP4?.Url || null;
const errorMessage = payload.ErrorMessage || null;
const hasError = payload.HasError === true || Boolean(errorMessage);
const isReady = !hasError && Boolean(videoUrl);
const now = new Date().toISOString();

let brazecall = {
  attributes: [
    {
      external_id: brazeExternalId,
      _update_existing_only: true,
      stayfilm_video_status: isReady ? "ready" : "failed",
      stayfilm_video_url: videoUrl || null,
      stayfilm_job_id: idJob,
      stayfilm_render_error: errorMessage,
      stayfilm_callback_received_at: now
    }
  ],
  events: [
    {
      external_id: brazeExternalId,
      _update_existing_only: true,
      name: isReady ? "stayfilm_video_ready" : "stayfilm_video_failed",
      time: now,
      properties: {
        stayfilm_job_id: idJob,
        stayfilm_video_url: videoUrl || null,
        stayfilm_render_error: errorMessage,
        stayfilm_status: payload.Status || payload.status || null
      }
    }
  ]
};

return brazecall;
```

{: start="8"}
8. **保存**を選択し、生成されたWebhook URLをコピーします。
9. 以下のサンプルStayfilmコールバックJSONを使用して、Webhook URLにテスト`POST`リクエストを送信します。`RelayedData`をステップ1で作成したテストユーザーの`external_id`に設定します。

```json
{
  "IdJob": "debug-job-001",
  "HasError": false,
  "Status": "DRAFT_DONE",
  "ProducedFiles": {
    "Videos": {
      "VideoMP4": {
        "Url": "https://example.com/stayfilm-poc-video.mp4"
      }
    }
  },
  "RelayedData": "stayfilm-poc-001"
}
```

cURL、Postman、または同様のツールでリクエストを送信します。成功したレスポンスは、HTTPステータス`201`と`{"message": "success"}`を返します。

{: start="10"}
10. **データ設定** > **データ変換**に移動し、変換がリストに表示されない場合はページをリロードします。
11. 変換を開き、**検証**を選択します。**出力**で検証が成功したことを確認します。
12. **有効化**を選択します。
13. コピーしたWebhook URLをコールバックURLとしてStayfilmに提供します。

{% alert note %}
Brazeの`external_id`以外のデータを`CallbackRelayData`に保存する場合は、`RelayedData`を適切に解析するように変換コードを更新してください。
{% endalert %}

### ステップ3：Stayfilmにジョブを送信するWebhookキャンペーンを作成する {#step-3-create-a-webhook-campaign-to-send-jobs-to-stayfilm}

Stayfilmにレンダリングジョブを送信する[Webhookキャンペーン]({{site.baseurl}}/user_guide/channels/webhooks)を作成します。

{% alert important %}
キャンペーンをテストする前に、Stayfilmがステップ2のデータ変換コールバックURLでプロジェクトを設定していることを確認してください。
{% endalert %}

1. **メッセージング** > **キャンペーン**に移動します。
2. **キャンペーンを作成** > **Webhook**を選択します。
3. `Stayfilm Webhook Integration`などのキャンペーン名を入力します。
4. **Webhookを作成** > **ゼロから始める**を選択します。
5. **Webhookを作成** > **Webhook URL**で、Stayfilmが提供する`POST /Job`エンドポイントURLを入力します。以下の例の*`{BASE_URL}`*を置き換えてください：`https://{BASE_URL}/stg/v3/job`
6. **HTTPメソッド**を**POST**に設定します。
7. **リクエストボディ**で**Raw Text**を選択し、Stayfilmが提供するジョブペイロードを貼り付けます。[Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call)を使用してボディをダイナミックにすることができます。

`CallbackRelayData`をBrazeユーザーの`external_id`に設定してください。Stayfilmはこの値をコールバックで`RelayedData`として返します。

{% raw %}
```json
{
  "SmartTags": ["Setup-Template"],
  "Medias": [
    {
      "Group": "userMedia",
      "URL": "https://{BASE_URL}/some_media.png"
    }
  ],
  "Videos": [{}],
  "CallbackRelayData": "stayfilm-poc-001"
}
```
{% endraw %}

以下のリクエストヘッダーを追加します。

| キー | 値 |
| --- | ----- |
| `idproject` | Stayfilmが提供する`idproject`の値 |
| `Subscription-Key` | Stayfilmが提供する`Subscription-Key` |
| `Content-Type` | `application/json` |
| `Authorization` | Connected Contentを通じて取得したOAuthベアラートークン（以下の例を参照） |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Request headers" }

以下のConnected Contentブロックで、*`{TENANT_ID}`*、*`{CLIENT_ID}`*、*`{CLIENT_SECRET_URL_ENCODED}`*、*`{SCOPE_URL_ENCODED}`*をStayfilmが提供する値に置き換えます。*`{CLIENT_SECRET_URL_ENCODED}`*と*`{SCOPE_URL_ENCODED}`*はブロックに貼り付ける前にURLエンコードしてください。OAuthの要件については、[Stayfilm APIドキュメント](https://apidoc.stayfilm.com)を参照してください。

{% raw %}
```
{% connected_content https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token
  :method post
  :body grant_type=client_credentials&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET_URL_ENCODED}&scope={SCOPE_URL_ENCODED}
  :content_type application/x-www-form-urlencoded
  :cache_max_age 3000
  :save stayfilm_auth
%}Bearer {{stayfilm_auth.access_token}}
```
{% endraw %}

{: start="8"}
8. **下書きを保存**を選択します。

{% alert note %}
キャンペーンページを離れて戻った場合、**ステータス**を**すべて**に設定すると、まだ**下書き**のキャンペーンを見つけることができます。
{% endalert %}

### ステップ4：Webhookキャンペーンをテストする {#step-4-test-the-webhook-campaign}

1. Webhookコンポーザーから、**テスト**タブを選択します。
2. **ユーザーとしてメッセージをプレビュー**で、**既存のユーザーを選択**を選択し、テストユーザー（例：`stayfilm-poc-001`）を検索します。
3. **テストを送信**を選択します。

成功したレスポンスは、HTTPステータス`201`と以下のようなJSONボディを返します。

```json
{
  "IdJob": "4557a77e-f56c-48be-81f7-2d8c5e558cb1",
  "Videos": [
    {
      "IdVideo": "87287b25-7814-4fa1-ad1a-f2ea89822d0f",
      "IdGenre": "f07a1334-5904-420a-9f31-92644f245c5a",
      "IdVideoTemplate": "7b77c3df-12a1-4636-a9b4-bc227f4c233f",
      "IdProject": "73ea3e73-b41e-4676-b674-51731d3bf49c",
      "Status": "DRAFT_RENDERING_PENDING",
      "DurationInSeconds": null,
      "URL": null,
      "ErrorMessage": null,
      "CreatedAt": "2026-06-16T00:35:28.7736263Z",
      "UpdatedAt": "2026-06-16T00:35:28.7736264Z",
      "IdVideoFather": null,
      "IdVideoSon": null,
      "ProducingStatus": "PENDING"
    }
  ],
  "Images": []
}
```

### ステップ5：Stayfilmのコールバックを確認する {#step-5-confirm-the-stayfilm-callback}

Stayfilmはビデオを非同期でレンダリングし、処理が完了するとデータ変換にコールバックを送信します。[Stayfilm APIドキュメント](https://apidoc.stayfilm.com)に記載されているStayfilm APIエンドポイントを通じてジョブステータスを監視してください。

1. **データ設定** > **データ変換**に移動します。
2. 変換の**ログ**タブを選択します。
3. **成功**ステータスのコールバックが表示されていることを確認します。

### ステップ6：アプリ内メッセージでビデオを表示する {#step-6-display-the-video-in-an-in-app-message}

ユーザープロファイルに`stayfilm_video_url`が設定された後、レンダリングされたビデオをキャンペーンまたはキャンバスで表示します。

1. **メッセージング** > **キャンペーン**に移動します。
2. **キャンペーンを作成** > **アプリ内メッセージ**を選択します。
3. `Stayfilm Video Show`などのキャンペーン名を入力します。
4. メッセージ作成画面で、**トラディショナルエディター**を選択します。
5. **送信先**で、**Webブラウザー**を選択します。
6. **メッセージタイプ**を**カスタムコード**に設定します。
7. 以下のHTMLを**HTML**フィールドに貼り付けます。

{% raw %}
```html
<!doctype html>
<html>
<head>
<meta charset="UTF-8">
</head>
<body>
<div id="stayfilm-video-url" style="display: none;">{{custom_attribute.${stayfilm_video_url}}}</div>
<video id="stayfilm-video" controls preload="metadata" playsinline style="width: 100%; max-width: 420px; border-radius: 12px; background: #000;">
Your browser does not support HTML5 video.
</video>
<script>
(function () {
  var urlElement = document.getElementById("stayfilm-video-url");
  var video = document.getElementById("stayfilm-video");
  var videoUrl = urlElement ? urlElement.textContent.trim() : "";
  if (!videoUrl || videoUrl.indexOf("http") !== 0) {
    return;
  }
  var source = document.createElement("source");
  source.src = videoUrl;
  source.type = "video/mp4";
  video.appendChild(source);
  video.load();
})();
</script>
</body>
</html>
```
{% endraw %}

{: start="8"}
8. **下書きを保存**を選択します。
9. **テスト**タブを選択します。
10. **ユーザーとしてメッセージをプレビュー**で、**既存のユーザーを選択**を選択し、テストユーザーの`external_id`を検索します。

プロファイルに`stayfilm_video_url`が設定されている場合、レンダリングされたビデオがプレビューに表示され、再生されます。

## 統合の拡張 {#extend-the-integration}

このウォークスルーでは、Stayfilm APIの一部をカバーしています。ジョブテンプレート、メディア入力、またはダウンストリームメッセージングを調整するには、[Stayfilm APIドキュメント](https://apidoc.stayfilm.com)を参照し、Webhookペイロード、データ変換マッピング、キャンペーンロジックを適宜更新してください。

## 考慮事項 {#considerations}

- **非同期レンダリング：** ビデオ生成は即時ではありません。Webhookと同じフローでアプリ内メッセージを送信するのではなく、`stayfilm_video_ready`カスタムイベントまたは`stayfilm_video_status`のセグメントからフォローアップメッセージングをトリガーしてください。
- **識別子の一貫性：** `CallbackRelayData`の値は、Brazeユーザーの`external_id`と正確に一致する必要があります。
- **OAuthトークンのキャッシュ：** Connected Contentの例では、OAuthトークンを3000秒間キャッシュします。Stayfilmがトークンの有効期間要件を変更した場合は、`cache_max_age`を調整してください。
- **サンドボックステスト：** 本番環境にリリースする前に、Brazeサンドボックスで完全なコールバックループを検証してください。
- **カスタム属性の容量：** この統合で作成されるStayfilmのカスタム属性とイベントに対して、ワークスペースに十分な容量があることを確認してください。

## トラブルシューティング {#troubleshooting}

Stayfilm統合で問題が発生した場合は、以下の表を参照してください。

| 問題 | 解決方法 |
| ----- | ---------- |
| データ変換の検証が失敗する | テストペイロードの`RelayedData`が有効なBrazeの`external_id`と一致していることを確認し、**検証**を選択する前に**データ変換**ページをリロードしてください。 |
| Webhookテストが201以外のレスポンスを返す | リクエストヘッダーのStayfilm認証情報を確認し、OAuth Connected ContentブロックがURLエンコードされた値を使用していることを確認し、`POST /Job` URLが正しいことを確認してください。 |
| 変換ログにコールバックが表示されない | Stayfilmがアクティブなデータ変換のWebhook URLを持っていることを確認し、ビデオレンダリングが完了するまで待ってください。 |
| アプリ内プレビューにビデオが表示されない | テストユーザープロファイルに`stayfilm_video_url`が設定されていること、およびアプリ内メッセージが**カスタムコード**で**Webブラウザー**をターゲットにしていることを確認してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Troubleshooting" }