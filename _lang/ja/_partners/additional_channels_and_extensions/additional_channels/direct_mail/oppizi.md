---
nav_title: Oppizi
article_title: Oppizi
alias: /partners/oppizi/
description: "このリファレンス記事では、BrazeとOppiziのパートナーシップについて説明します。"
page_type: partner
search_tag: Partner
---

# Oppizi

> [Oppizi](https://www.oppizi.com/)はオフラインマーケティングのグローバルリーダーであり、測定可能でターゲットを絞ったダイレクトメールやチラシ配布キャンペーンを実施するためのワンストップソリューションを企業に提供しています。

_この統合はOppiziによって管理されています。_

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ------------------------------ | ----------------------------------------------------------------------------- |
| Oppiziアカウント | この統合を使用するには、アクティブなOppiziアカウントが必要です。 |
| Oppizi APIキー | Oppiziアカウントの**Integrations** > **Braze**で確認できます。 |
| Oppiziダイレクトメールワークフローid | Oppiziの**Direct Mail Workflow**ページでワークフローを作成し、IDを取得します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## ユースケース {#use-cases}

Oppiziとの統合により、以下のことが可能です。

* OppiziのWebhookとダイレクトメールワークフローに接続されたBrazeトリガーを使用して、**自動ダイレクトメールはがきを送信**できます。
* Oppiziのダイレクトメールワークフローで**しきい値、ウェーブ、リミットを設定**し、Campaignsの送信をコントロールできます。
* Oppiziの内蔵デザインツールで**プロフェッショナルなはがきをデザイン**できます。デザイン経験は不要です。
* Oppiziのダッシュボードで**キャンペーンパフォーマンスをリアルタイムに追跡**できます。

## 統合 {#integration}

### ステップ 1: Oppizi APIキーを生成する {#step-1-generate-your-oppizi-api-key}

BrazeでWebhookテンプレートを使用するには、まずOppizi APIキーを生成する必要があります。

1. Oppiziにログインします。
2. **Integrations** > **Braze**に移動します。
3. APIキーを生成します。

必要に応じて、このページからキーの管理、失効、作成ができます。

### ステップ 2: BrazeでWebhookテンプレートを作成する {#step-2-create-a-braze-webhook-template}

次に、今後のCampaignsやCanvasesで使用するために、BrazeでOppizi用のWebhookテンプレートを作成します。

1. Brazeで**Content** > **Webhook**に移動します。
2. **Create webhook template**を選択します。
3. テンプレートの名前を入力します。
4. Webhookテンプレートに、以下のフィールドを入力します。

- **Webhook URL:** `https://webhooks.oppizi.com/events`
- **リクエスト本文:** **Raw Text**

リクエストメソッドとヘッダーについて、OppiziはHTTPメソッドと以下のHTTPヘッダーをテンプレートに含めることを要求しています。以下のフィールドに入力してください。

- **HTTPメソッド:** POST
- **リクエストヘッダー:**
  - **Authorization:** `Bearer <oppiziAPIKey>`
  - **Content-Type:** `application/json`

![BrazeでのOppizi Webhookヘッダーの例。]({% image_buster /assets/img/oppizi/oppizi_braze_webhook_headers.png %})

**リクエストボディ**には、フィールド**oppiziWorkflowID**を含める必要があります。このIDはOppiziでワークフローを作成する際に生成され、受信者をどのダイレクトメールワークフローに追加するかを指定するために必要です。Oppiziの各ダイレクトメールワークフローには固有のIDがあるため、BrazeでOppizi Webhookテンプレートを作成する場合は、ワークフローIDを常に正しいものに更新してください。

{% alert note %}
ダイレクトメールの送信に必要な受信者の郵便住所のカスタム属性が、Brazeアカウントに設定されていることを確認してください。
{% endalert %}

![BrazeでのOppizi Webhookテンプレートの例。]({% image_buster /assets/img/oppizi/oppizi_braze_webhook_example.png %})

以下はリクエストボディの例です。

{% raw %}
```json
{
    "event" : "workflow.addRecipient",
    "oppiziWorkflowID" : "<oppiziWorkflowID>",
    "requestType" : "live",
    "recipient" : {
        "recipientID" : "{{${braze_id}}}",
        "firstName" : "{{${first_name}}}",
        "lastName" : "{{${last_name}}}",
        "address1" : "{{custom_attribute.${address1}}}",
        "address2" : "{{custom_attribute.${address2}}}",
        "city" : "{{custom_attribute.${city}}}",
        "country" : "{{${country}}}",
        "zipCode" : "{{custom_attribute.${zipCode}}}",
        "state" : "{{custom_attribute.${state}}}"
    }
}
```
{% endraw %}

### ステップ 3: Oppiziでダイレクトメールワークフローを作成する {#step-3-create-a-direct-mail-workflow-in-oppizi}

1. Oppiziで、**Direct Mail Workflow** > **Create workflow**に移動します。
2. しきい値、ウェーブ、はがきフォーマット、アートワークなど、ワークフローの詳細を設定します。
3. Webhookの詳細セクションに、ワークフローIDを含むすぐに使えるリクエストボディがあり、Brazeに直接貼り付けることができます。

### ステップ 4: Brazeでリクエストをプレビューしてテストする {#step-4-preview-and-test-your-request-in-braze}

OppiziのワークフローIDを含むリクエストボディを追加した後、テストを実行してセットアップが期待どおりに機能していることを確認します。

テストを実行するには、リクエストボディの`requestType`を`live`から`test`に更新します。このステップは、ダイレクトメールのオーディエンスにテスト受信者が追加されるのを防ぐために重要です。

テストが完了したら、`requestType`を`live`に戻してCanvasを保存します。これで、自動ダイレクトメールキャンペーンを開始する準備が整いました。