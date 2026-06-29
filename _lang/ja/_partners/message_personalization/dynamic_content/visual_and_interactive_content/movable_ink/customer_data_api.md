---
nav_title: Customer Data APIへの接続
article_title: Movable Ink Customer Data APIへの接続
description: "このリファレンス記事では、Brazeに保存されている顧客イベントデータをアクティブ化して、Customer Data APIを使用してMovable Ink内でパーソナライズされたコンテンツを生成するための接続方法について説明します。"
page_type: partner
search_tag: Partner
---

# Movable Ink Customer Data APIへの接続 {#connect-to-the-movable-ink-customer-data-api}

> BrazeとMovable InkのCustomer Data API統合により、マーケターはBrazeに保存されている顧客イベントデータをアクティブ化して、Movable Ink内でパーソナライズされたコンテンツを生成できます。

Movable Inkは、Customer Data APIを介してBrazeから行動イベントを取り込むことができます。イベントは、Movable Inkに渡されるユニークユーザーID（UUID）に基づいてユーザープロファイルに保存されます。

ストーリー、Movable Ink Customer Data API、およびMovable Inkが行動データをどのように活用するかの詳細については、以下のサポートセンターの記事を参照してください。

- [行動データでコンテンツを強化する](https://support.movableink.com/hc/en-us/sections/360001239453-Power-content-with-behavioral-data)
- [Customer Data APIの概要およびガイド](https://support.movableink.com/hc/en-us/articles/13815957200663-Customer-Data-API-introduction-and-guide)
- [FAQ: Customer Data API](https://support.movableink.com/hc/en-us/articles/12423178752279-FAQ-Customer-Data-API)

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Movable Inkアカウント | このパートナーシップを活用するには、Movable Inkアカウントが必要です。 |
| Movable Ink API認証情報 | Movable Inkのソリューションチームが API認証情報を生成します。API認証情報は以下で構成されます。{::nomarkdown}<ul><li>エンドポイントURL（データの送信先）</li><li>ユーザー名とパスワード（APIの認証に使用）</li></ul>{:/} 必要に応じて、Movable Inkはユーザー名とパスワードを、基本認証ヘッダー値として使用するbase64エンコード値として提供できます。 |
| 行動イベントペイロード | イベントペイロードをMovable Inkクライアントエクスペリエンスチームと共有する必要があります。詳細については、「Movable Inkと[イベントペイロードを共有する](#event-payloads)」を参照してください。 |
| クリエイティブアセットとビジネスロジック | Movable Inkとクリエイティブアセットを共有する必要があります。これには、ブロックの構築方法をMovable Inkに指示するAdobe Photoshop（PSD）ファイルとフォールバック画像が含まれます。また、パートナーによってアクティブ化されたコンテンツブロックをいつどのように表示するかについてのビジネスロジックを提供する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

### ステップ1: BrazeでWebhook Campaignを作成する {#step-1-create-a-webhook-campaign-in-braze}

#### ステップ1a: 新しいCampaignを作成する {#step-1a-create-a-new-campaign}

1. Brazeで、[Webhook Campaignを作成します]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook)。
2. Campaignに名前と任意の説明を付けます。
3. テンプレートとして**Blank Template**を選択します。

#### ステップ1b: Customer Data API認証情報を追加する {#step-1b-add-your-customer-data-api-credentials}

1. **Webhook URL**フィールドに、Movable InkのエンドポイントURLを入力します。

![Movable InkエンドポイントURLとリクエストボディがJSON Key/Value Pairsに設定されているBrazeのWebhookコンポーザーの作成タブ]({% image_buster /assets/img/movable_ink/cd_api_webhook_url.png %}){: style="max-width:75%" }

{:start="2"}
2. **設定**タブを選択します。
3. 以下のリクエストヘッダーをキーと値のペアとして追加します。

| キー | 値 |
| --- | --- |
| Content-Type | application/json |
| Authorization | Movable Inkから受け取った基本認証を入力します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 1b: Add your Customer Data API credentials" }

![Content-TypeとAuthorizationのキーと値のペアが設定されたBrazeのWebhookコンポーザーの設定タブ]({% image_buster /assets/img/movable_ink/cd_api_webhook_settings.png %}){: style="max-width:75%" }

#### ステップ1c: ペイロードを設定する {#step-1c-configure-your-payload}

1. **Compose**タブに戻ります。
2. **Request Body**として、JSONキーと値のペアを使用して独自のリクエストボディを作成するか、イベントペイロードを生のテキストとして入力します。標準的なeコマースイベントの例については、[サンプルペイロード](#sample-payloads)を参照してください。

![ID、タイムスタンプ、ユーザーID、およびイベントタイプのJSONキーと値のペアが設定されたBrazeのWebhookコンポーザーの作成タブ]({% image_buster /assets/img/movable_ink/cd_api_webhook_kvp.png %}){: style="max-width:75%" }

#### ステップ1d: Webhookをテストする {#step-1d}

サンプルペイロードをMovable Inkクライアントエクスペリエンスチームと共有する必要があります。このペイロードは、作成したペイロードに基づいて**Test**タブで生成できます。

{% alert important %}
Movable Inkは、Movable Inkクライアントエクスペリエンスチームがマッピングを完了し、テストを受ける準備ができたことを確認するまで、BrazeでのWebhookテストを待つことを推奨しています。このマッピングが完了していない場合、テスト時にエラーが発生する可能性が高くなります。
{% endalert %}

Webhookをテストするには、以下の手順を実行します。

1. **Test**タブを選択します。
2. ユーザーとしてメッセージをプレビューし、そのユーザーのサンプルイベントペイロードを表示します。ランダムユーザー、特定のユーザー、またはカスタムユーザーとしてのプレビューを選択できます。
3. 問題がなければ、**Send test**をクリックしてテストリクエストを送信します。

![200 OKレスポンスを示すBrazeのWebhookレスポンスメッセージ]({% image_buster /assets/img/movable_ink/cd_api_webhook_response.png %}){: style="max-width:75%" }

### ステップ2: Campaign設定を確定する {#step-2-finalize-your-campaign-setup}

#### ステップ2a: Campaignをスケジュールする {#step-2a-schedule-your-campaign}

Webhookの作成とテストが完了したら、[Campaignをスケジュールします]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign)。

Brazeでは、スケジュール配信、アクションベースの配信、およびAPIトリガー配信がサポートされています。[アクションベースの配信]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)は、通常ほとんどの行動イベントのユースケースに最適です。ユースケースに最適な方法についてのご質問は、BrazeおよびMovable Inkのカスタマーサクセスマネージャーにお問い合わせください。

アクションベースの配信の場合:

1. トリガーアクションを指定します。これは、Movable InkへのWebhookをトリガーするイベントです。
2. **スケジュールの遅延**が**Immediately**に設定されていることを確認します。イベント発生直後にイベントデータが遅延なくMovable Inkに送信される必要があります。
3. 開始時間を指定してCampaign期間を設定します。終了時刻は適用されない可能性がありますが、ユースケースに必要な場合は設定できます。

{% alert note %}
データがMovable Inkにリアルタイムでストリーミングされるようにするには、**Send campaign to users in their local time zone**を選択しないでください。
{% endalert %}

#### ステップ2b: オーディエンスを指定する {#step-2b-specify-your-audience}

次に、このCampaignでターゲットにするユーザーを決定します。詳細については、「[ユーザーをターゲットにする]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/target_users)」を参照してください。

**コントロールグループ**のチェックボックスをオフにして、CampaignでABテストを使用しないようにしてください。コントロールグループが含まれている場合、一定の割合のユーザーのデータがMovable Inkに送信されません。オーディエンス全体を、コントロールグループではなくバリアントに移動する必要があります。

![バリアント分布の100%がバリアント1に割り当てられ、コントロールグループがないBraze CampaignのABテストパネル]({% image_buster /assets/img/movable_ink/cd_api_webhook_ab.png %})

#### ステップ2c: コンバージョンイベントを選択する（オプション） {#step-2c-choose-conversion-events-optional}

必要であれば、Braze内でこのCampaignにコンバージョンイベントを割り当てることができます。

ただし、Webhookがデータのストリーミングのみを目的としている場合、このレベルでのアトリビューションは、Brazeの行動データを使用してコンテンツをパーソナライズした後にCampaignレベルでアトリビューションを確認するよりも有用性が低い可能性があります。

### ステップ3: Campaignを起動する {#step-3-launch-the-campaign}

Webhookの設定を確認し、Campaignを起動します。

## 考慮事項 {#considerations}

### 一意のユーザー識別子の整合 {#aligning-on-a-unique-user-identifier}

`mi_u`として使用しているユニークユーザー識別子（UUID）値がBraze内で利用可能であり、Movable Inkに送信されるイベントペイロードに含めることができることを確認してください。

これにより、画像を生成する際にMovable Inkが参照する行動イベントが、その行動イベントを受信した同一の顧客に関連付けられます。UUID値がBrazeの`external_id`と同じでない場合、UUIDをキャプチャして属性としてBrazeに渡すか、この識別子を利用するためにBrazeイベントのイベントプロパティに含めて渡す必要があります。

Brazeは複数のプラットフォーム（Webやモバイルアプリなど）にわたってユーザーの行動を追跡するため、1人のユーザーが複数の異なる匿名IDを持つことがあります。`identify`イベントに匿名IDと既知の単一IDの両方が含まれている限り、`identify`イベントがMovable Inkに送信される時点で、これらのIDを単一の既知のストーリーズユーザープロファイルにマージできます。

Movable Inkが単一ユーザーの`user_id`を受信したら、そのユーザーの今後のすべてのイベントには同じ`user_id`が含まれている必要があります。

### Movable Inkとのイベントペイロードの共有 {#event-payloads}

Movable InkのCustomer Data APIへのコネクターを設定する前に、イベントペイロードをMovable Inkクライアントエクスペリエンスチームと共有してください。これにより、Movable InkがイベントをMovable Inkのイベントスキーマにマッピングでき、API呼び出しの拒否や失敗を防ぐことができます。

任意のイベントプロパティを使用して、Braze内でイベントペイロードを生成できます。ランダムなユーザー、または特定のユーザーIDを検索してサンプルペイロードを生成します。詳細については上記の「[ステップ1d](#step-1d)」を参照してください。

このサンプルペイロードをMovable Inkクライアントエクスペリエンスチームと共有してください。サンプルペイロードに、機密性の高い個人識別情報（メールアドレス、電話番号、誕生日全体など）が含まれていないことを確認してください。

カスタムイベントプロパティと、プロパティに含まれるデータの想定形式について詳しくは、「[カスタムイベントプロパティ]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties)」を参照してください。

### 既知のユーザーと匿名のユーザー {#known-versus-anonymous-users}

Brazeでは、匿名のユーザープロファイルでイベントを記録できます。イベントロギング中にどの識別子がユーザープロファイルにリンクされるかは、ユーザーがどのように作成されたか（Braze SDKまたはAPIを通じて）と、ユーザーライフサイクルの現在の段階に依存します。

#### 既知のユーザーのBrazeイベントのみを転送する {#only-forwarding-braze-events-for-known-users}

Webhook Campaignで`External User ID`フィルターを使用して、フィルター`External User ID` `is not blank`に一致する`external_id`を持つユーザーのみをターゲットにします。

#### 匿名ユーザーと既知ユーザーのBrazeイベントを転送する {#forwarding-braze-events-for-anonymous-and-known-users}

匿名ユーザー（プロファイルに`external_id`が割り当てられる前のユーザー）からのBrazeイベントを転送したい場合、`external_id`が利用可能になるまでMovable Inkの`anonymous_id`として使用する識別子を決定する必要があります。Brazeユーザープロファイルで一定に保たれる`anonymous_id`を選択してください。Webhook本文でLiquidロジックを使用して、`anonymous_id`または`user_id`を渡すかどうかを決定できます。

詳細については、[サンプルペイロード](#sample-payloads)にあるWebhookの例を参照してください。

## ペイロードの例 {#example-payloads}

### 商品閲覧イベント {#product-view-event}

{% tabs local %}
{% tab Brazeトリガーイベントの例 %}

{% raw %}

```json
{
  "events": [
    {
      "email": "test@example.com",
      "name": "Product Viewed",
      "time": "2023-12-06T19:20:45+01:00",
      "properties": {
        "categories": [
          {
            "id": "Bathroom",
            "url": "https://example.com/cat/bathroom"
          }
        ],
        "meta": {
          "color": "green"
        },
        "title": "All-Purpose Cleaning Wipes",
        "price": 1.99,
        "id": "56544",
        "url": "https://www.example.com/variants_id/5f08cb918dcc595aa74b0fbc"
      }
    }
  ]
}
```

{% endraw %}

{% endtab %}
{% tab 想定されるMovable Inkリクエストペイロード %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "123-abc-678",
  "event": "product_viewed",
  "properties": {
    "categories": [
      {
        "id": "Bathroom",
        "url": "https://example.com/cat/bathroom"
      }
    ],
    "meta": {
      "color": "green"
    },
    "title": "All-Purpose Cleaning Wipes",
    "price": 1.99,
    "id": "56544",
    "url": "https://www.example.com/variants_id/5f08cb918dcc595aa74b0fbc"
  },
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "track",
  "user_id": "5c3aa83113dd490100d3d8d7"
}'

```

{% endraw %}
{% endtab %}
{% tab Webhookの例 %}

この例では、`external_id`を持たないユーザーの`anonymous_id`としてハッシュ化されたメールアドレスが使用されています。

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

// Example of md5 hashing the email address to use as the anonymous_id
{% assign anon_id = {{${email_address}}} | md5 %}

// Condition logic to determine which identifier to use. If an external_id is available use that, otherwise use the anonymous_id
{% if {{${user_id}}} %}
{% capture user_identifier %}"user_id": "{{${user_id}}}"{% endcapture %}
{% else %}
{% capture user_identifier %}"anonymous_id": "{{anon_id}}"{% endcapture %}
{% endif %}

{
  {{user_identifier}}
  "event": "product_viewed",
  "properties": {
    "categories": [
      {
        "id": "{{event_properties.${categories}[0].id}}",
        "url": "{{event_properties.${categories}[0].url}}"
      }
    ],
    "meta": {
      "color": "{{event_properties.${meta}.color}}"
    },
    "title": "{{event_properties.${title}}}",
    "price": "{{event_properties.${price}}}",
    "id": "{{event_properties.${id}}}",
    "url": "{{event_properties.${url}}}"
  },
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "track",
}

```

{% endraw %}
{% endtab %}
{% endtabs %}

### カテゴリー閲覧イベント {#category-view-event}

{% tabs local %}
{% tab Brazeトリガーイベントの例 %}

{% raw %}

```json
{
  "events": [
    {
      "external_id": "123456789",
      "name": "Category Viewed",
      "time": "2023-12-06T19:20:45+01:00",
      "properties": {
        "id": "bathroom-1",
        "title": "Bathroom Stuff",
        "url": "https://www.example.com/categories/bathroom"
      }
    }
  ]
}
```

{% endraw %}

{% endtab %}
{% tab 想定されるMovable Inkリクエストペイロード %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "123-abc-678",
  "event": "category_viewed",
  "properties": {
    "id": "bathroom-1",
    "title": "Bathroom Stuff",
    "url": "https://www.example.com/categories/bathroom"
  },
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "track",
  "user_id": "5c3aa83113dd490100d3d8d7"
}'
```

{% endraw %}

{% endtab %}
{% tab Webhookの例 %}

この例では、既知のユーザー（`external_id`を持つユーザー）のみのイベントを追跡するWebhookを示しています。

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

{
  "event": "category_viewed",
  "properties": {
    "id": "{{event_properties.${id}}}",
    "title": "{{event_properties.${title}}}",
    "url": "{{event_properties.${url}}}"
  },
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "track",
  "user_id": "{{${user_id}}}"
}

```

{% endraw %}

{% endtab %}
{% endtabs %}

### 識別イベント {#identify-event}

{% tabs local %}
{% tab Brazeトリガーイベントの例 %}

{% raw %}

```json
{
  "events": [
    {
      "external_id": "123456789",
      "name": "Account Created",
      "time": "2023-12-06T19:20:45+01:00"
    }
  ]
}
```

{% endraw %}
{% endtab %}
{% tab 想定されるMovable Inkリクエストペイロード %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "jg0iq5gd30dqpwn8zmx05p06mzjmjir4r8",
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "identify",
  "user_id": "mycustomerid123"
}'
```

{% endraw %}
{% endtab %}
{% tab Webhookの例 %}

この例では、`external_id`を持たないユーザーの`anonymous_id`としてハッシュ化されたメールアドレスが使用されています。

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

// Example of md5 hashing the email address to use as the anonymous_id
{% assign anon_id = {{${email_address}}} | md5 %}

{
  "anonymous_id": "{{anon_id}}",
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "identify",
  "user_id": "{{${user_id}}}"
}

```

{% endraw %}

{% endtab %}
{% endtabs %}