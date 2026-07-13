---
nav_title: Zapier
article_title: Zapier
alias: /partners/zapier/
description: "この参考記事では、BrazeとZapier（Webアプリ間でデータを共有し、その情報を使ってアクションを自動化できるオートメーションWebツール）のパートナーシップについて概説しています。"
page_type: partner
search_tag: Partner

---
# Zapierとの統合 {#zapier-integration}

> [Zapier](https://zapier.com/) は、Webアプリ間でデータを共有し、その情報を使用してアクションを自動化できるオートメーションWebツールです。

BrazeとZapierのパートナーシップでは、Braze APIとBrazeの[Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook#creating-a-webhook)を活用してサードパーティアプリケーション（Google Workplace、Slack、Salesforce、WordPressなど）に接続し、さまざまなアクションを自動化できます。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|---|---|
| Zapierアカウント | このパートナーシップを活用するには、Zapierアカウントが必要です。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントはインスタンスの[Braze URL]({{site.baseurl}}/api/basics#api-definitions)に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

以下のZapierの例では、POST Webhookを使ってWordPressからBrazeに情報を送信します。この情報を使用してBrazeキャンバスを作成できます。

### ステップ1: Zapierトリガーを作成する {#step-1-create-a-zapier-trigger}

Zapierの用語では、「zap」とはアプリやサービスをつなぐ自動化されたワークフローのことです。どのzapでも、最初のパートはトリガーを指定することです。zapが有効になると、トリガーが検出されるたびにZapierによって対応するアクションが自動的に実行されます。

WordPressの例を使って、Zapierプラットフォームで、WordPressの新しい投稿が追加されたときにトリガーされるようにzapを設定し、**Post Status**と**Post Type**として**Published**と**Posts**を選択します。

![Zapierプラットフォームで、zap内でトリガーとして「new comment」、「any webhook」、「new post」のいずれかを選択します。この例では「new post」が選択されています。][5]

![Zapierプラットフォームで、zap内で目的のpost statusとpost typeを選択してトリガーを設定します。この例では「Published」と「Posts」が選択されています。][6]

### ステップ2: アクションWebhookを追加する {#step-2-add-an-action-webhook}

次にzapアクションを定義します。zapが有効になり、トリガーが検出されると、アクションが自動的に発生します。

この例の続きで、BrazeのエンドポイントにJSONとしてPOSTリクエストを送信します。これを行うには、**Apps**の下にある**Webhooks**オプションを選択します。

![Zapier Appsステップで、アクションとしてWebhooksが選択されています。]({% image_buster /assets/img_archive/zapier3.png %})

### ステップ3: Braze POSTをセットアップする {#step-3-set-up-braze-post}

Webhookを設定するときに、次の設定を使用してWebhook URLにBraze RESTエンドポイントを指定します。完了したら**Publish**を選択します。

- **Method**: POST
- **Webhook URL**: `https://rest.iad-01.braze.com/canvas/trigger/send`
- **Data Pass-Through**: False
- **Unflatten**: No
- **リクエストヘッダー**:
  - **Content-Type**: application/json
  - **Authorization**: Bearer YOUR-API-KEY
- **Data**:

```json
{
  "canvas_id": "your_canvas_identifier",
  "recipients": [
    {
      "external_user_id": "external_user_identifier",
      "context":{
        "string_property": "Your example string",
        "example_integer_property": 1
      }
    }
  ]
}
```

![Brazeエンドポイント、ヘッダー、ペイロードフィールドが設定されたZapier Webhookの構成画面。]({% image_buster /assets/img/zapier.png %}){: style="max-width:70%;"}

### ステップ4: Brazeキャンペーンを作成する {#step-4-create-a-braze-campaign}

zapの設定が完了したら、Liquidフォーマットを使用してメッセージに情報を表示することで、WordPressデータを使用してBrazeキャンペーンやキャンバスをカスタマイズできます。

## `/users/track`エンドポイントでZapierを使用する {#using-zapier-with-the-userstrack-endpoint}

Brazeの[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)エンドポイントにデータを送信するには（たとえば、Google Sheetsの**New or Updated Spreadsheet Row**のようなトリガーを使用する場合）、**Webhooks by Zapier**で**Custom Request**を使用してください。標準の**POST**アクションは使用しないでください。標準のPOSTアクションは、`/users/track`エンドポイントと互換性のない形式でリクエストをフォーマットします。

1. Zapierで、トリガーを選択します（たとえば、Google Sheetsの**New or Updated Spreadsheet Row**）。
2. アクションとして**Webhooks by Zapier**を選択し、**Custom Request**を選択します（POSTではありません）。
3. **Method**をPOSTに設定し、Braze RESTエンドポイントURL（たとえば`https://rest.iad-01.braze.com/users/track`）を入力し、PostmanやAPI呼び出しと同様に各要素をダブルクォートで囲んでリクエストボディをフォーマットします。トリガーのフィールド（たとえばスプレッドシートの列）を適切な場所でJSONボディにマッピングします。
4. 必要なヘッダーを追加します:
   - **Content-Type**: `application/json`
   - **Authorization**: `Bearer YOUR-REST-API-KEY`（Braze REST APIキーを括弧やクォートなしで使用します）
5. ステップをテストし、zapを有効にします。

[5]: {% image_buster /assets/img_archive/zapier1.png %}
[6]: {% image_buster /assets/img_archive/zapier2.png %}