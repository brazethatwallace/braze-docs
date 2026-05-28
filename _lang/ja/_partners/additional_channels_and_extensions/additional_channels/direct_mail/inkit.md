---
nav_title: Inkit
article_title: Inkit
alias: /partners/inkit/
description: "このリファレンス記事では、BrazeとInkitのパートナーシップについて説明します。このパートナーシップにより、ダイレクトメールキャンペーンを自動化して時間と労力を節約し、オフラインの顧客をオンラインに呼び戻すことができます。"
page_type: partner
search_tag: Partner

---

# Inkit

> [Inkit](https://www.inkit.com)とBrazeにより、デジタルでもダイレクトメールでも、企業が安全にドキュメントを作成して配布することができます。

_この統合はInkitによって管理されています。_

## 統合について {#about-the-integration}

BrazeとInkitの統合により、ドキュメントを生成し、Braze webhookを使用してBrazeユーザーに直接メールで送信できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| --- | --- |
| Inkitアカウント | このパートナーシップを活用するには、[Inkitアカウント](https://www.inkit.com/)が必要です。 |
| Inkit APIキー<br><br>`<INKIT_API_TOKEN>` | このキーは[Inkitダッシュボード](https://app.inkit.io/#/account/integrations)の**Development**タブにあり、BrazeアカウントとInkitアカウントを接続できるようになります。|
| InkitテンプレートID<br><br>`<INKIT_TEMPLATE_ID>` | テンプレートを作成した後、**テンプレート**タブからテンプレートIDをコピーして、Brazeのテンプレートで使用できます。<br><br>たとえば、Inkit環境にテンプレートID: `tmpl_3bDScFl9cwr3OAVR1RSdEC` で `invoice_template` というテンプレートを作成できます。
| HTTPヘッダー | HTTPヘッダーは、BrazeからInkitに送信するAPIリクエストの一部です。この中には、Inkit APIの呼び出しを認証および許可するためのInkit APIキーが含まれます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

### ステップ 1: Inkitテンプレートを作成する {#step-1-create-an-inkit-template}

Inkitプラットフォーム上で、BrazeのCampaignで使用するテンプレートをHTML、Word、PowerPoint、Excel、またはPDFで作成します。詳細については、[Inkitのドキュメント](https://docs.inkit.com/docs/create-a-template)を参照してください。

### ステップ 2: Braze Webhookテンプレートを作成する {#step-2-create-your-braze-webhook-template}

今後のCampaignやCanvasで使用するInkit Webhookテンプレートを作成するには、Brazeプラットフォームで**コンテンツ** > **Webhook**に移動します。次に、**Webhookテンプレートを作成**を選択します。

単発のInkit WebhookのCampaignを作成したい場合、または既存のテンプレートを使用したい場合は、新しいCampaignを作成する際にBrazeで**Webhook**を選択します。

![テンプレートとメディアセクションのWebhookテンプレートタブで利用可能な事前デザイン済みWebhookテンプレートの選択画面。]({% image_buster /assets/img/inkit-webhook-template.png %})

Inkit Webhookテンプレートを選択すると、以下のように表示されます:
- **Webhook URL**: 空白
- **リクエスト本文**: Raw Text

Webhook URLフィールドで、Inkit Webhook URLを[作成](https://docs.inkit.com/docs/set-up-a-webhook-to-an-event)して入力します。

![Braze Webhookビルダーの作成タブに表示されているリクエスト本文のコードとWebhook URL。]({% image_buster /assets/img/inkit-integration.png %})

#### リクエストヘッダーとメソッド {#request-headers-and-method}

Inkitの認証には、Base64でエンコードされたInkit APIキーを含む`HTTP Header`が必要です。以下の内容はすでにキーと値のペアとしてテンプレートに含まれていますが、**設定**タブで`<INKIT_API_TOKEN>`をInkit APIキーに置き換える必要があります。

{% raw %}
- **HTTPメソッド**: POST
- **リクエストヘッダー**:
  - **Authorization**: Basic `{{ '<INKIT_API_TOKEN>' | base64_encode }}`
  - **Content-Type**: application/json
{% endraw %}

#### リクエスト本文 {#request-body}

Liquidが、以下の必須フィールドとオプションフィールドに関連付けられている適切なカスタム属性と一致していることを確認してください。また、どのリクエストにもカスタムデータフィールドを追加できます。

```json
{% raw %}{
  "api_token": "<INKIT_API_TOKEN>",
  "template_id": "<INKIT_TEMPLATE_ID>",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "company": "{{custom_attribute.${company_name}}}",
  "phone" : "{{${phone_number}}}",
  "address_line_1": "{{custom_attribute.${address}}}",
  "address_line_2": "{{custom_attribute.${address2}}}",
  "address_city": "{{${city}}}",
  "address_state": "{{custom_attribute.${state}}}",
  "address_zip": "{{custom_attribute.${zip}}}",
  "address_country": "{{${country}}}",
  "source" : "Braze"
}{% endraw %}
```

### ステップ 3: リクエストをプレビューする {#step-3-preview-your-request}

生のテキストが適切なBrazeタグである場合、自動的にハイライト表示されます。このWebhookを送信するには、`street`、`unit`、`state`、`zip`が[カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attributes)として設定されている必要があります。

**プレビュー**パネルでリクエストをプレビューするか、**テスト**タブに移動して、ランダムなユーザー、既存のユーザーを選択するか、独自にカスタマイズしてWebhookをテストします。

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないでください！<br>更新されたWebhookテンプレートは、新しい[WebhookのCampaign]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/)を作成するときに、**保存済み Webhook テンプレート**リストで見つけることができます。
{% endalert %}