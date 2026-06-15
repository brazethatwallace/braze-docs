---
nav_title: optilyz
article_title: optilyz
description: "このリファレンス記事では、Brazeとoptilyzのパートナーシップについて説明します。このパートナーシップにより、より顧客中心の、持続可能で収益性の高いダイレクトメールキャンペーンを実施できます。"
alias: /partners/optilyz/
page_type: partner
search_tag: Partner

---

# optilyz

> [optilyz](https://optilyz.com) はダイレクトメールオートメーションプラットフォームです。顧客中心型で持続可能かつ収益性の高いダイレクトメールキャンペーンを実施できます。

_この統合はoptilyzによって管理されています。_

## 統合について {#about-the-integration}

optilyzとBrazeのWebhook統合を使用して、手紙、はがき、セルフメーラーなどのダイレクトメールを顧客に送信できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| optilyzアカウント | このパートナーシップを活用するには、optilyzアカウントが必要です。 |
| optilyz APIキー<br><br>`<OPTILYZ_API_KEY>` | optilyz APIキーはoptilyzカスタマーサクセスマネージャーから提供されます。<br><br>このAPIキーでBrazeとoptilyzのアカウントを接続できます。 |
| optilyzオートメーションID<br><br>`<OPTILYZ_AUTOMATION_ID>` | オートメーションIDは、ページヘッダーのボックスに記載されています。<br><br>optilyzにログインしたら、データの送信先のオートメーションに移動できます。<br>最初にオートメーションをアクティブにする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## ユースケース {#use-cases}

ダイレクトメールをデジタルチャネルのように運用することは、大量の郵送から脱却し、チャネルを（デジタル）カスタマージャーニーの一部として活用することを意味します。最新のダイレクトメールアプローチの利点は、次のとおりです。
- 関連性の向上、ユースケースの追加、ABテストの容易化、クロスチャネル効果によるコンバージョン率の向上
- オートメーションとエンドツーエンドのソリューションによる労力の削減
- フレーム契約とコストの透明性によるコスト削減

## 統合 {#integration}

optilyzと統合するには、[optilyz API](https://www.optilyz.com/doc/api/) を使用して受信者データをBraze Webhookに送信します。

### ステップ 1: BrazeのWebhookテンプレートを作成する {#step-1-create-your-braze-webhook-template}

将来のCampaignsやCanvasesで使用するoptilyz Webhookテンプレートを作成するには、Brazeプラットフォームで**コンテンツ** > **Webhook**に移動します。次に、**Webhookテンプレートを作成**を選択します。

1回限りのoptilyz Webhookキャンペーンを作成するか、既存のテンプレートを使用する場合は、新しいキャンペーンを作成する際にBrazeで**Webhook**を選択します。

新しいWebhookテンプレートで、以下のフィールドに記入します。
- **Webhook URL**: Webhook URLはお客様ごとに異なり、optilyzのカスタマーサクセスマネージャーから提供されます。
- **リクエスト本文**: Raw Text

#### リクエストヘッダーとメソッド {#request-headers-and-method}

optilyzには、認証用のHTTPヘッダーとHTTPメソッドが必要です。以下の内容はすでにキーと値のペアとしてテンプレートに含まれていますが、**設定**タブで `<OPTILYZ_API_KEY>` をoptilyz APIキーに置き換える必要があります。このキーの直後に「:」を付加し、base 64でエンコードする必要があります。

- **HTTPメソッド**: POST
- **リクエストヘッダー**:
  - **Authorization**: {% raw %} `{{ '<OPTILYZ_API_KEY>:' | base64_encode }}` {% endraw %}
  - **Content-Type**: application/json

![Braze Webhookビルダーに表示されるリクエストヘッダーとHTTPメソッド。]({% image_buster /assets/img/optilyz/optilyz_settings.png %}){: style="max-width:50%"}

#### リクエスト本文 {#request-body}

次のリクエスト本文では、任意のLiquidパーソナライゼーションタグを使用して、optilyzの[APIドキュメント](https://www.optilyz.com/doc/api/)に従ってカスタムリクエストテンプレートを作成できます。

`variation` フィールドはオプションであり、オートメーション内部のどのデザインを使用するかを定義できます。バリエーションが省略された場合、optilyzは定義されたバリエーションの1つをランダムに割り当てます。

{% raw %}
```json
{
    "address": {
        "title": "{{custom_attribute.${salutation}}}",
        "firstName": "{{${first_name}}}",
        "lastName": "{{${last_name}}}",
        "street": "{{custom_attribute.${street}}}",
        "houseNumber": "{{custom_attribute.${houseNumber}}}",
        "address2": "{{custom_attribute.${address2}}}",
        "zipCode": "{{custom_attribute.${zipCode}}}",
        "city": "{{custom_attribute.${city}}}",
        "country": "{{custom_attribute.${country}}}"
    },
    "variation": {{custom_attribute.${designVariation}}}
}
```
{% endraw %}

![Braze Webhookビルダーの作成タブに表示されるリクエスト本文のコードとWebhook URLの画像。]({% image_buster /assets/img/optilyz/optilyz_compose.png %})

### ステップ 2: リクエストをプレビューする {#step-2-preview-your-request}

次に、**プレビュー**パネルでリクエストをプレビューするか、**テスト**タブに移動して、ランダムなユーザー、既存のユーザーを選択するか、独自にカスタマイズしてWebhookをテストします。ページを離れる前にテンプレートを保存することを忘れないでください。

![Braze Webhookビルダーのテストタブで利用可能なさまざまなテストフィールド。]({% image_buster /assets/img/optilyz/optilyz_testing.png %})

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないでください。<br>更新済みWebhookテンプレートは、新しい[Webhookキャンペーン]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/)を作成するときに、**保存済み Webhook テンプレート**リストで見つけることができます。
{% endalert %}