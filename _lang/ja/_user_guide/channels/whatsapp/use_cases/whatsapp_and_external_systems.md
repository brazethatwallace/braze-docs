---
nav_title: "WhatsAppと外部システム"
article_title: "WhatsAppと外部システム"
page_order: 2
description: "このリファレンス記事では、BrazeとWhatsAppの統合を外部AIまたはコミュニケーションシステムと連携させるためのステップバイステップガイドを提供します。"
page_type: reference
alias: /whatsapp_external_system_integration/
channel:
  - WhatsApp
---

# BrazeとWhatsAppを外部AIまたはコミュニケーションシステムと統合する {#integrate-braze-and-whatsapp-with-an-external-ai-or-communication-system}

> WhatsAppチャネルでAIチャットボットやライブエージェントへの引き継ぎを活用して、カスタマーサポート業務を効率化しましょう。日常的な問い合わせを自動化し、必要に応じてシームレスに人間のエージェントに移行することで、応答時間を大幅に改善し、カスタマーエクスペリエンス全体を向上させることができます。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| - | - |
| 外部システム | APIを使用してチャットボットや自動クライアントサービスシステムを構築・管理できるサードパーティのAIまたはコミュニケーションシステム、あるいはその両方。 |
| BrazeとWhatsAppの統合 | Brazeが管理するWhatsApp番号 |
| Braze REST APIキー | `campaigns.trigger.send` 権限を持つREST APIキー。これはBrazeダッシュボードで**設定** > **APIキー**に移動して作成できます。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 仕組み {#how-it-works}

Brazeと外部AIまたはコミュニケーションシステム間の統合は双方向で機能し、Brazeがコミュニケーションチャネルとして、外部システムがメッセージを処理して応答を作成する「インテリジェンス」として動作します。

統合ワークフローは2つの主要なフローに分けられます。
**インバウンドフロー：** ユーザーのメッセージがBrazeに届き、処理のために外部システムに転送されます。
**アウトバウンドフロー：** メッセージを処理した後、外部システムがBrazeに応答を送信し、Brazeがエンドユーザーにメッセージを配信します。

このコミュニケーションを効率的に自動化するために、この統合では2つの主要なBraze機能を使用します：[webhookキャンペーン]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook)と[APIトリガーキャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)です。

![BrazeのWhatsAppチャネルと外部システム間の統合アーキテクチャ。]({% image_buster /assets/img/whatsapp/external_system_architecture.png %})
## 統合の設定 {#configuring-the-integration}

### ステップ 1: インバウンドメッセージ用のwebhookキャンペーンを作成する {#step-1-create-a-webhook-campaign-for-inbound-messages}

まず、Brazeが受信したWhatsAppメッセージを外部システムに送信する方法を確立するためのwebhookキャンペーンを作成します。

1. Brazeでwebhookキャンペーンを作成します。
2. webhook作成画面で、**Compose webhook**を選択します。
3. **Webhook URL**フィールドに、メッセージを受信する外部システムのAPIエンドポイント（URL）を入力します。
4. リクエストボディに**Raw text**を選択し、ユーザーの`external_id`と電話番号、メッセージ内容、その他の関連情報を含むパーソナライゼーション付きのペイロードを入力します。例：

{% raw %}
```liquid
{
  "user_id": "{{${user_id}}}",
  "phone_number": "{{${phone_number}}}",
  "message": "{{whats_app.${inbound_message_body}}}"
}
```
{% endraw %}

{: start="5"}
5. キャンペーン作成画面の**配信をスケジュール**ステップで、配信タイプに**アクションベース**を選択し、キャンペーントリガーに**WhatsApp インバウンドメッセージを送信**を選択します。

![WhatsAppインバウンドメッセージの送信をトリガーとするアクションベースの配信。]({% image_buster /assets/img/whatsapp/inbound_message_trigger.png %})

{: start="6"}
6. キャンペーンの作成を完了し、保存して起動します。キャンペーンを起動すると、メッセージを受信するたびにBrazeが外部システムにwebhookを送信します。

### ステップ 2: アウトバウンドメッセージ用のAPIトリガーキャンペーンを作成する {#step-2}

次に、外部システムがWhatsAppを通じてユーザーにメッセージを返信する方法を確立するためのAPIトリガーキャンペーンを作成します。

1. BrazeでWhatsAppキャンペーンを作成します。
2. メッセージ作成画面で、**WhatsApp Template Message**または**Response Message**を選択し、テンプレートまたは応答メッセージのレイアウトを選択します。インバウンドメッセージが24時間のWhatsApp時間枠を開いているため、任意の応答メッセージレイアウトを選択できます。

![メッセージタイプとメッセージレイアウトを選択するオプションがあるメッセージ作成画面。]({% image_buster /assets/img/whatsapp/response_message_layout.png %})

{: start="3"}
3. メッセージ本文にAPIトリガープロパティを追加します。例：{% raw %}`{{api_trigger_properties.${external_system_msg+body}}}`{% endraw %}。これにより、AIシステムが送信されるメッセージを入力できるようになります。

![トリガープロパティを含むメッセージ本文があるメッセージ作成画面。]({% image_buster /assets/img/whatsapp/api_trigger_properties.png %})

{: start="4"}
4. キャンペーン作成画面の**配信をスケジュール**ステップで、配信タイプに**アクションベース**を選択します。
5. キャンペーンを保存し、Brazeがこのキャンペーンに対して生成する一意の`campaign_id`をメモしておきます。次のステップでこのIDが必要になります。

### ステップ 3: 外部システムをAPIトリガーキャンペーンに接続する {#step-3-connect-the-external-system-to-the-api-triggered-campaign}

最後に、外部システムがBrazeを呼び出して応答を送信するように設定します。

1. 外部システムのコードで、受信したメッセージを処理して応答を生成した後、Brazeの`/messages/send`エンドポイントにPOSTリクエストを送信します。
2. `/messages/send`リクエストボディに、[ステップ 2](#step-2)の`campaign_id`、ユーザーの`external_id`、および外部システムの応答内容を含めます。
3. [ステップ 2](#step-2)のAPIトリガープロパティを使用して外部システムの応答を挿入し、認証のためにリクエストヘッダーにAPIキーを含めることを忘れないでください。以下のcURLの例を参照してください：

{% raw %}
```bash
curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer a valid rest API key' \
  -d '{
    "campaign_id": "campaign_id",
    "recipients": [
      {
        "external_user_id": "external_id",
        "trigger_properties": {
          "external_system_msg_body": "your external system message"
        }
      }
    ]
  }' \
  {{Braze endpoint}}/campaigns/trigger/send
```
{% endraw %}

これで、AIチャットボットワークフローを構築するための確かな基盤が整いました！

### ワークフローのカスタマイズ {#customizing-your-workflow}

統合ロジックを拡張して以下のことが可能です：
- 異なるキーワードを使用して、個別のwebhookキャンペーンをトリガーする。
- マルチステップのAPIトリガーキャンペーンを使用して、より複雑な会話フローを作成する。
- チャット情報をBrazeにカスタム属性として記録し、ユーザープロファイルを充実させ、将来のキャンペーンのセグメンテーションに活用する。