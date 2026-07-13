---
nav_title: Lob
article_title: Lob
alias: /partners/lob/
description: "このリファレンス記事では、BrazeとLob.comのパートナーシップについて説明します。Lob.comを利用すれば、手紙やはがき、小切手などのダイレクトメールを郵送することができます。"
page_type: partner
search_tag: Partner

---

# Lob

> [Lob.com](https://lob.com) は、ユーザーにダイレクトメールを送ることができるオンラインサービスです。

_この統合はLobによって管理されています。_

## 統合について {#about-the-integration}

この統合により、次のことが可能になります。

- Braze webhookとLob APIを使用して、手紙やはがき、小切手などのダイレクトメールを郵送する。
- Brazeデータ変換とLob webhookを使用して、LobイベントをBrazeのカスタム属性およびイベントとして共有する。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| --- | --- |
| Lobアカウント | このパートナーシップを活用するには、Lobアカウントが必要です。 |
| Lob APIキー | Lob APIキーは、Lobダッシュボードのお客様の名前の下にある設定セクションで確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## Braze webhookを使用したメールの送信 {#sending-mail-using-braze-webhooks}

### ステップ1: Lobエンドポイントの選択 {#step-1-choose-a-lob-endpoint}

Lobで実行する内容に応じて、webhookのHTTPリクエストで対応するエンドポイントを使用する必要があります。各エンドポイントの詳細については、[LobのAPIリファレンスドキュメント](https://lob.com/docs#intro)を参照してください。

| 基本URL | 利用可能なエンドポイント |
| ------------ | ------------------- |
| `https://api.lob.com/` | `/v1/addresses<br>/v1/addresses/{id}`<br>`/v1/verify`<br>`/v1/postcards`<br>`/v1/postcards/{id}`<br>`/v1/letter`<br>`/v1/letter/{id}`<br>`/v1/checks<br>/v1/checks/{id}`<br>`/v1/bank_accounts`<br>`/v1/bank_accounts/{id}`<br>`/v1/bank_accounts/{id}/verify`<br>`/v1/areas<br>/v1/areas/{id}`<br>`/v1/routes/{zip_code}`<br>`/v1/routes`<br>`/v1/countries<br>/v1/states`|
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ1: Lobエンドポイントの選択" }

### ステップ2: BrazeのWebhookテンプレートを作成する {#step-2-create-your-braze-webhook-template}

今後のキャンペーンやキャンバスで使用するLob Webhookテンプレートを作成するには、Brazeダッシュボードの**コンテンツ** > **Webhook**に移動します。次に、**Webhookテンプレートを作成**を選択します。

単発のLob Webhook キャンペーンを作成したい場合、または既存のテンプレートを使用したい場合は、新しいキャンペーンを作成する際にBrazeで**Webhook**を選択します。

新しいWebhookテンプレートに、次のフィールドを入力してください:

- **Webhook URL**: `<LOB_API_ENDPOINT>`
- **リクエスト本文**: Raw Text

#### リクエストヘッダーとメソッド {#request-headers-and-method}

Lobには、認証用のHTTPヘッダーとHTTPメソッドが必要です。以下の内容はすでにキーと値のペアとしてテンプレートに含まれていますが、**設定**タブで`<LOB_API_KEY>`をご使用のLob APIキーに置き換える必要があります。このキーの直後に「:」を付加し、base 64でエンコードする必要があります。

- **HTTPメソッド**: POST
- **リクエストヘッダー**:
  - **Authorization**: Basic `{{'<LOB_API_KEY>:' | base64_encode}}`
  - **Content-Type**: application/json

![Braze Webhookビルダーの作成タブに表示されているリクエスト本文のコードとWebhook URL。]({% image_buster /assets/img_archive/lob_full_request.png %})

#### リクエスト本文 {#request-body}

Lobポストカードエンドポイントのリクエスト本文の例を次に示します。このリクエスト本文はBrazeの基本Lobテンプレートで提供されますが、他のエンドポイントを使用する場合は、それに応じてLiquidフィールドを調整する必要があります。

{% raw %}
```json
{
  "description": "Demo Postcard",
  "to": {
    "name": "{{${first_name}}} {{${last_name}}}",
    "address_line1": "{{custom_attribute.${address_line1}}}",
    "address_city": "{{custom_attribute.${address_city}}}",
    "address_zip": "{{custom_attribute.${address_zip}}}",
    "address_country": "{{custom_attribute.${address_country}}}"
  },
  "front": "https://lob.com/postcardfront.pdf",
  "back": "https://lob.com/postcardback.pdf",
  "use_type": "marketing",
  "size": "6x11"
}
```
{% endraw %}

### ステップ3: リクエストをプレビューする {#step-3-preview-your-request}

この時点で、キャンペーンはテストと送信の準備ができているはずです。エラーが発生した場合は、Lobダッシュボードと Braze開発者コンソールのエラーメッセージログを確認してください。例えば、以下のエラーは、認証ヘッダーのフォーマットが正しくないために発生したものです。

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないでください！<br>更新されたWebhookテンプレートは、新しい[webhook キャンペーン]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/)を作成するときに、**保存済み Webhook テンプレート**リストで見つけることができます。
{% endalert %}

![時間、アプリ名、チャネル、エラーメッセージを示すメッセージエラーログ。エラーメッセージには、メッセージアラートとステータスコードが含まれます。]({% image_buster /assets/img_archive/error_log.png %})

## Lob webhookを使用したイベントの共有 {#sharing-events-using-lob-webhooks}

[Brazeデータ変換]({{site.baseurl}}/user_guide/data/unification/data_transformation/)を使用すると、外部プラットフォームからBrazeへのデータフローを自動化するためのwebhookを構築および管理できます。各変換には一意のエンドポイントが割り当てられ、他のプラットフォームがwebhookの送信先として使用できます。

{% alert important %}
Lobのデータ変換テンプレートは、[`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を使用してイベントを送信し、データポイントを記録します。Lobのwebhook設定でレート制限を設定し、データの過剰な記録を避けることをお勧めします。
{% endalert %}

### ステップ1: Brazeで変換を作成する {#step-1-create-a-transformation-in-braze}

1. Brazeダッシュボードで、**データ設定** > **データ変換**に移動し、**変換の作成**を選択します。
2. 変換を表す短いわかりやすい名前を入力します。
3. **編集エクスペリエンス**で、**テンプレートを使用**を選択し、Lobを検索してチェックボックスをオンにします。
4. 完了したら、**変換の作成**を選択します。次のステップで使用する変換エディターにリダイレクトされます。

### ステップ2: Lobテンプレートの入力 {#step-2-fill-out-the-lob-template}

このテンプレートを使用すると、Lobイベントの1つを、Brazeで使用できるカスタムイベントまたは属性に変換できます。インラインコメントに従い、テンプレートの作成を完了してください。

{% alert tip %}
Lobのwebhookペイロード構造の詳細については、[Lob: webhookの使用](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks)を参照してください。
{% endalert %}

```json
// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JavaScript dot notation, such as payload.x.y.z

// In this example, this function removes the periods and underscores of the event_type.id sent in the Lob payload so that an event id that is formatted like: `letter.processed_for_delivery` will log an event to Braze with the name `letter processed for delivery`.

function formatString(input) {
    return input.replace(/[._]/g, ' ');
}

let braze_event = formatString(payload.event_type.id);

// In this example, a metadata value passed in the Lob Webhook called 'external_ID' is being used to match the Event to the corresponding Braze user.

let brazecall = {
  "attributes": [
    {
      "external_id": payload.body.metadata.external_id,
      "_update_existing_only": true,
      "Most Recent Mailer": payload.body.description
    }
  ],
  "events": [
    {
      "external_id": payload.body.metadata.external_id,
      "_update_existing_only": true,
      "name": braze_event,
      "time": new Date().toISOString(),
// Customize the properties to the Lob event you are syncing. Our example below pulls in the Tracking Events array of objects associated with certain Lob events.
      "properties": {
        "tracking_events": payload.body.tracking_events
      }
    }
  ]
};
// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

### ステップ3: Lobでwebhookを作成する {#step-3-create-a-webhook-in-lob}

1. テンプレートの作成が完了したら、**Activate**を選択し、**Webhook URL**をクリップボードにコピーします。
2. Lobで[新しいwebhookを作成し](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks#receiving-a-webhook-1)、BrazeのWebhook URLを使用してwebhookを受信します。