---
nav_title: Open Loyalty
article_title: Open Loyalty
description: "BrazeとOpen Loyaltyの統合により、ポイント残高、ティアの変更、有効期限の警告などのロイヤルティデータをリアルタイムでBrazeに直接同期できます。"
alias: /partners/openloyalty/
page_type: partner
search_tag: Partner
---

# Open Loyalty

> [Open Loyalty](https://www.openloyalty.io/)は、クラウドベースのロイヤルティプログラムプラットフォームで、顧客ロイヤルティプログラムや報酬プログラムを構築・管理できます。BrazeとOpen Loyaltyの統合は、ポイント残高、ティアの変更、有効期限の警告などのロイヤルティデータをリアルタイムでBrazeに直接同期します。これにより、ユーザーのロイヤルティステータスが変化したときに、パーソナライズされたメッセージ（メール、プッシュ、SMS）をトリガーできます。

_この統合はOpen Loyaltyによって管理されています。_

## 統合について {#about-the-integration}

この統合は、Brazeデータ変換を使用してOpen LoyaltyからのWebhookをキャプチャし、Brazeユーザープロファイルにマッピングします。

* **リアルタイム更新**：ロイヤルティイベント（ポイント獲得、ティアアップグレード）をBrazeにプッシュします。
* **パーソナライゼーション**：Brazeテンプレートでロイヤルティ属性（現在の残高、次のティア名）を使用します。
* **双方向**：Brazeのエンゲージメントデータに基づいて、Open Loyaltyの顧客カスタム属性を更新します。

## ユースケース {#use-cases}

この統合は、以下のデータフローをカバーしています。

1. **Brazeへのイベント同期（インバウンド）**：Open LoyaltyからBrazeにデータを送信することで、ポイントの変更、ティアのアップグレード、報酬の交換を追跡します。データ変換により、このデータがユーザーイベントに変換されます。
2. **Open Loyalty会員の変更（アウトバウンド）**：「VIP」ラベルの追加やカスタム属性の更新など、Brazeでのユーザー行動に基づいてOpen Loyaltyの会員データを自動的に更新します。

## 前提条件 {#prerequisites}

始める前に、以下のものが必要です。

| 必要条件 | 説明 |
| :--- | :--- |
| Open Loyaltyアカウント | このパートナーシップを利用するには、Open LoyaltyテナントのAdminアカウントが必要です。 |
| Open Loyalty REST APIキー | Open Loyalty REST APIキー（BrazeからOpen Loyaltyにデータを送信する統合の場合）。<br><br> **Settings > Admins > API Keys**で作成します。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。<br><br> Brazeダッシュボードの**Settings** > **API Keys**からこのキーを作成します。 |
| Brazeデータ変換 | Webhookリスナーを設定するには、Brazeの「データ設定」タブへのアクセスが必要です。 |
| IDの一致 | Brazeでのユーザーの`external_id`が、Open Loyaltyの`loyaltyCardNumber`（または別のデフォルト識別子）と一致している必要があります。 |
| テナントID | Open LoyaltyのテナントID（アウトバウンド更新に必要）。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

主な統合は、データ変換を使用してOpen LoyaltyのWebhookイベントをBrazeに同期します。

### ステップ 1：BrazeでWebhook URLを生成する {#step-1-generate-the-webhook-url-in-braze}

まず、Brazeでデータ変換を作成し、データを受信するためのユニークなURLを生成します。

1.  Brazeで、**Data Settings > Data Transformation**を開きます。
2.  **Create Transformation**をクリックします。
3.  以下のフィールドに入力します。
     * **Transformation name**：説明的な名前を付けます（例：「Open Loyalty Point Update Events」）。
     * **Select destination**：**POST: Track users**を選択します。
4.  **Create Transformation**をクリックします。
5.  右側にある**Webhook URL**を見つけ、**Copy**をクリックします。

{% alert important %}
このURLは安全に保管してください。次のステップで必要になります。
{% endalert %}

### ステップ 2：Open LoyaltyでWebhookサブスクリプションを作成する {#step-2-create-the-webhook-subscription-in-open-loyalty}

Open Loyaltyに、先ほど生成したURLへ特定のイベントを送信するよう設定します。

1.  Open Loyalty管理パネルにログインします。
2.  **General > Webhooks**に移動します。
3.  **Add new webhook**をクリックし、サブスクリプションを設定します。
    * **eventName**：追跡したいイベントを選択します（例：`AvailablePointsAmountChanged`、`CustomerLevelChanged`、`キャンペーンEffectWasApplied`）。
    * **url**：ステップ1のBraze Webhook URLを貼り付けます。
    * 以下のヘッダーを追加します。
      * `Content-Type: application/json`
      * `User-エージェント: partner-OpenLoyalty`
4.  Webhookサブスクリプションを保存します。

### ステップ 3：データ変換を設定する {#step-3-configure-the-data-transformation}

受信したOpen LoyaltyのペイロードをBrazeのプロパティにマッピングするJavaScriptロジックをBrazeに記述します。

1.  Brazeで、ステップ1で作成したデータ変換を開きます。
2.  Open Loyaltyでイベントをトリガーし（例：メンバーのポイントを変更したり、ティアを割り当てたり）、**Webhook details**ペインにサンプルペイロードを生成します。
3.  **Transformation code**エディターで、受信データをマッピングするスクリプトを記述します。以下の例をガイドとして使用してください。

```javascript
// 1. Parse the incoming Open Loyalty payload
const data = payload.data;

// 2. Construct the Braze API body
let brazecall = {
  "events": [
    {
      // CRITICAL: Map the identifier (e.g., loyaltyCardNumber -> external_id)
      "external_id": data.customer.loyaltyCardNumber,

      // Define the Event Name (what you see in Braze)
      "name": "Loyalty Event Triggered",

      // timestamp
      "time": new Date().toISOString(),

      // Map specific properties you want to use in emails/segments
      "properties": {
        "event_type": payload.type, // for example, 'AvailablePointsAmountChanged'
        "new_balance": data.amount,
        "change_amount": data.amountChange,
        "tier_name": data.tier ? data.tier.name : null
      }
    }
  ]
};

return brazecall;
```

{: start="4"}
4. **Validate**をクリックして、コードがサンプルペイロードに対して正しく実行されることを確認し、**Activate**をクリックします。


## BrazeでOpen Loyaltyを使用する {#using-open-loyalty-with-braze}

インバウンドの統合が完了したら、**アウトバウンド更新**を設定し、Brazeでの行動に基づいてOpen Loyalty会員を変更します。

### ステップ 1：Braze Webhook キャンペーンを設定する {#step-1-configure-braze-webhook-campaign}

このプロセスでは、Braze Webhookを使用してOpen Loyalty Member APIに`PATCH`リクエストを送信します（例：「VIP」ラベルを追加する）。

1.  Brazeで、新しい**Webhook キャンペーン**を作成します（またはキャンバス内のWebhookを使用します）。
2.  **Compose Webhook**をクリックします。
3.  **Webhook URL**：Open Loyaltyインスタンス、テナントID、ユーザーID用のBraze Liquid変数を使ってURLを構築します。
    * フォーマット：
      {% raw %}
      `https://<YOUR_OL_INSTANCE>/api/<TENANT_ID>/member/loyaltyCardNumber={{${user_id}}}`
      {% endraw %}
4. 以下のフィールドに入力します。
    * **Request Method**：`PATCH`
    * **Request Headers**：
      * `Content-Type`: `application/json`
      * `X-AUTH-TOKEN`: `<YOUR_PERMANENT_TOKEN>`
      * `User-エージェント: Braze`
5.  **Request Body**：`Raw text`を選択し、ペイロードを貼り付けます。

```json
{
  "customer": {
    "labels": [
      {
        "key": "braze_vip_segment",
        "value": "optedIn"
      }
    ]
  }
}
```

### ステップ 2：トリガーを設定する {#step-2-configure-the-trigger}

1.  **Delivery**または**Entry Schedule**タブに移動します。
2.  以下のフィールドに入力します。
    * **Delivery Method**：アクションベース。
    * **Trigger**：関連するトリガーを定義します（例：ユーザーがBrazeで特定のセグメントに入る）。
    * **Launch**：キャンペーンを有効化します。

## トラブルシューティング {#troubleshooting}

### インバウンドイベントを検証する {#verify-inbound-events}
データ変換がアクティブになると、データがカスタムイベントとしてBrazeに表示されます。**Perform Custom Event**トリガーでキャンペーンを作成し、定義したイベント（例：`Loyalty Event Triggered`）が利用可能かどうかを確認することで検証できます。

### アウトバウンドWebhookを検証する {#verify-outbound-webhooks}
Brazeのメッセージアクティビティログを確認し、Webhookが`200 OK`ステータスを返したことを確認します。
* **401エラー**：Open Loyalty APIトークンを確認してください。
* **404エラー**：BrazeのユーザーIDがOpen Loyaltyに存在しません。