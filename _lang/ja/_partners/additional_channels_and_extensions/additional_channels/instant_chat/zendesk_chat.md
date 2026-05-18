---
nav_title: Zendesk
article_title: Zendesk Chat
description: "Zendesk ChatとBrazeを統合し、双方向のSMS会話を設定する方法を学びます。"
alias: /partners/zendesk_chat/
page_type: partner
search_tag: Partner

---

# Zendesk Chat

> [Zendesk Chat](https://www.zendesk.com/service/messaging/)は、各プラットフォームのwebhookを使用して双方向のSMS会話を設定します。ユーザーがサポートをリクエストすると、Zendeskにチケットが作成されます。エージェントの応答はAPIトリガーのSMS キャンペーンを通じてBrazeに転送され、ユーザーの返信はZendeskに送り返されます。

## 前提条件 {#prerequisites}


| 要件 | 説明 |
|---|---|
| Zendeskアカウント | このパートナーシップを利用するには、Zendeskアカウントが必要です。|
| Zendesk Basic認証トークン | Zendesk Basic認証トークンは、BrazeからZendeskへのアウトバウンドWebhookリクエストに使用されます。|
| Braze REST APIキー | `campaigns.trigger.send` 権限を持つBraze REST APIキー。これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。|
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

Braze SMS機能とZendeskライブエージェントの応答を組み合わせることで、カスタマーサポートの効率を高め、ユーザーからの問い合わせに迅速に人的サポートで対応します。

## Zendesk Chatを統合する {#integrating-zendesk-chat}

### ステップ1：ZendeskでWebhookを作成する {#step-1-create-a-webhook-in-zendesk}

1. Zendesk開発者コンソールで、webhookにアクセスします：{% raw %}`https://{{url}}.zendesk.com/admin/apps-integrations/webhooks/webhooks`{% endraw %}
2. **Create Webhook**で、**Trigger or automation**を選択します。
3. **Endpoint URL**に、**/campaign/trigger/send**エンドポイントを追加します。
4. **Authentication**で**Bearer token**を選択し、`campaigns.trigger.send` 権限を持つBraze REST APIキーを追加します。

![Zendesk Webhookの例。]({% image_buster /assets/img/zendesk/instant_chat/chat1.png %}){: style="max-width:70%;"}

### ステップ2：アウトバウンドSMS キャンペーンを作成する {#step-2-create-an-outbound-sms-campaign}

次に、ZendeskからのWebhookをリッスンし、顧客にカスタムSMSレスポンスを送信するSMS キャンペーンを作成します。

#### ステップ2.1：メッセージを作成する {#step-21-compose-your-message}

ZendeskがAPIを介してメッセージのコンテンツを送信する場合、次の形式になります：

```
**----------------------------------------------\n\n{Replier Name}, {Replier Date}\n\n{Message}**
```

そのため、メッセージ内に表示させたい詳細をこの文字列から抽出する必要があります。そうしないと、ユーザーにすべての詳細が表示されてしまいます。

![フォーマットなしのSMSの例。]({% image_buster /assets/img/zendesk/instant_chat/chat2.png %}){: style="max-width:40%;"}

**Message**テキストボックスに、次のLiquidコードとオプトアウト言語またはその他の静的コンテンツを追加します：

{% raw %}
`````````liquid
{% assign body = {{api_trigger_properties.${msg_body}}} %}
{% assign msg = body | split: "
" %}
New message from Zendesk:
{{msg[2]}}

Feel free to respond directly to this number!
```
{% endraw %}

![フォーマット付きSMSの例。]({% image_buster /assets/img/zendesk/instant_chat/chat3.png %}){: style="max-width:70%;"}

#### ステップ2.2：配信をスケジュールする {#step-22-schedule-the-delivery}

配信タイプは**API-Triggered delivery**を選択し、次のステップで使用するキャンペーン IDをコピーします。

![API Triggered delivery]({% image_buster /assets/img/zendesk/instant_chat/chat4.png %}){: style="max-width:70%;"}

最後に、**Delivery Controls**で再適格性をオンにします。

![「Delivery Controls」で再適格性が有効になっている。]({% image_buster /assets/img/zendesk/instant_chat/chat5.png %})

### ステップ3：Zendeskでエージェントの返信をBrazeに転送するトリガーを作成する {#step-3-create-a-trigger-in-zendesk-to-forward-agent-replies-to-braze}

**Objects and rules** > **Business rules** > **Triggers**に移動します。

1. 新しい**カテゴリ**を作成します（例：**Trigger a message**）。
2. 新しい**トリガー**を作成します（例：**Respond via SMS Braze**）。
3. **Conditions**で以下を選択します：
- **Ticket>Comment**が**Present and requester can see comment**：新しいパブリックコメントがチケット更新に含まれるたびにメッセージがトリガーされます。
- **Ticket>Update**が**Web service (API)**に該当しない：ユーザーがBrazeからメッセージを送信しても携帯電話に転送されません。Zendeskからのメッセージのみが転送されます。

![Respond via SMS Braze。]({% image_buster /assets/img/zendesk/instant_chat/chat6.png %}){: style="max-width:70%;"}

**Actions**で**Notify by Webhook**を選択し、ステップ1で作成したエンドポイントを選択します。次に、API呼び出しのボディを指定します。[ステップ2.2](#step-22-schedule-the-delivery)の`campaign_id`をリクエスト本文に入力します。

![Respond via SMS Braze JSON本文。]({% image_buster /assets/img/zendesk/instant_chat/chat7.png %}){: style="max-width:70%;"}

{% raw %}
`````````liquid
{
    "campaign_id": "{{YOUR_CAMPAIGN_ID}}",
    "recipients": [
        {
            "external_user_id": "{{ticket.requester.custom_fields.braze_external_id}}",
			"trigger_properties": {
    "msg_body": "{{ticket.latest_public_comment_html}}"
		},
		"attributes": {
        "zendesk_ticket" : "{{ticket.id}}",
	"zendesk_ticket_open" : "true"
    }
        }
    ]
}
```
{% endraw %}


### ステップ4：チケットのクローズ時にユーザーを更新するトリガーをZendeskに作成する {#step-4-create-a-trigger-in-zendesk-to-update-a-user-when-a-ticket-is-closed}

チケットがクローズされたことをユーザーに通知したい場合は、テンプレート化されたレスポンスボディを使ってBrazeで新しいキャンペーンを作成します。

![チケットがクローズされたときにユーザーを更新する。]({% image_buster /assets/img/zendesk/instant_chat/chat8.png %}){: style="max-width:70%;"}

**API Triggered delivery**を選択し、キャンペーン IDをコピーします。

次に、チケットがクローズされたときにBrazeに通知するトリガーを設定します：
- カテゴリー：**Trigger a message**
- Conditionsで、**Ticket>Ticket Status**を選択し、**Solved**に変更します。

![Zendeskで設定された解決済みチケット。]({% image_buster /assets/img/zendesk/instant_chat/chat9.png %}){: style="max-width:70%;"}

**Actions**で**Notify by Webhook**を選択し、作成した2番目のエンドポイントを選択します。そこから、API呼び出しの本文を指定する必要があります：

![解決済みチケットのJSON本文。]({% image_buster /assets/img/zendesk/instant_chat/chat10.png %}){: style="max-width:70%;"}

{% raw %}
`````````liquid
{
    "campaign_id": "{{YOUR_API_KEY}}",
    "recipients": [
        {
            "external_user_id": "{{ticket.requester.custom_fields.braze_external_id}}",
"trigger_properties": {
    "msg_body": "Your ticket has been closed"
		},
,
			"attributes": {
	"zendesk_ticket_open" : "false"
    }
        }
    ]
}
```
{% endraw %}

### ステップ5：Zendeskでカスタムユーザーフィールドを追加する {#step-5-add-a-custom-user-field-in-zendesk}

管理センターで、サイドバーの**People**を選択し、**Configuration** > **User fields**を選択します。カスタムユーザーフィールド`braze_external_id`を追加します。

### ステップ6：インバウンドSMS転送を設定する {#step-6-set-up-inbound-sms-forwarding}

次に、Brazeで2つの新しいWebhook キャンペーンを作成します。これにより、顧客からのインバウンドSMSをZendeskの受信トレイに転送できます。

| キャンペーン | 目的 |
|--------------------|--------------------------------------------------------------------------------------|
| Webhook キャンペーン 1 | Zendeskに新しいチケットを作成します。 |
| Webhook キャンペーン 2 | 顧客からインバウンドで送信されたすべての会話型SMSレスポンスをZendeskに転送します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ6：インバウンドSMS転送を設定する" }

#### ステップ6.1：SMSキーワードカテゴリを作成する {#step-61-create-an-sms-keyword-category}

Brazeダッシュボードで、**Audience**に移動し、**SMSサブスクリプショングループ**を選択して、**Add Custom Keyword**を選択します。以下のフィールドに入力して、Zendesk専用のSMSキーワードカテゴリを作成します。

| フィールド | 説明 |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| Keyword Category | キーワードカテゴリの名前（例：`ZendeskSMS1`）。 |
| Keywords | カスタムキーワード（例：`SUPPORT`）。 |
| Reply Message | キーワードが検出されたときに送信されるメッセージ（例：「カスタマーサービス担当者がまもなくご連絡します。」）。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="ステップ6.1：SMSキーワードカテゴリを作成する" }

![BrazeのSMSキーワードカテゴリの例。]({% image_buster /assets/img/zendesk/instant_chat/chat11.png %}){: style="max-width:70%;"}

#### ステップ6.2：最初のWebhook キャンペーンを作成する {#step-62-create-your-first-webhook-campaign}

Brazeダッシュボードで、最初のWebhook キャンペーンを作成します。このメッセージはZendeskにサポートがリクエストされていることを通知します。

Webhookコンポーザーで、以下のフィールドに入力します：
- Webhook URL：{% raw %}https://{{url}}.zendesk.com/api/v2/tickets{% endraw %}
- HTTPメソッド：POST
- リクエストヘッダー：
- Content-Type: application/json
- Authorization: Basic {{Token}}
- リクエスト本文：

{% raw %}
`````````liquid
{
  "ticket": {
    "subject": "Action Needed",
    "comment": {
      "body": "{{sms.${inbound_message_body}}}"
    },
"requester":{
"name": "{{${first_name}}} {{${last_name}}}",
"user_fields": {
"braze_external_id": "{{${user_id}}}"
}
},
    "priority": "normal",
    "type": "problem"
  }
}
```
{% endraw %}

![2つの必須ヘッダーを含むリクエストの例。]({% image_buster /assets/img/zendesk/instant_chat/chat12.png %}){: style="max-width:70%;"}


#### ステップ6.3：最初の配信をスケジュールする {#step-63-schedule-the-first-delivery}

**Schedule Delivery**で**Action-Based Delivery**を選択し、トリガータイプとして**Send an SMS Inbound Message**を選択します。また、以前に設定したSMSサブスクリプショングループとキーワードカテゴリも追加します。

![最初のWebhook キャンペーンの「Schedule Delivery」ページ。]({% image_buster /assets/img/zendesk/instant_chat/chat13.png %})

**Delivery Controls**で再適格性をオンにします。

![最初のWebhook キャンペーンの「Delivery Controls」で再適格性が選択されている。]({% image_buster /assets/img/zendesk/instant_chat/chat14.png %})

#### ステップ6.4：2番目のWebhook キャンペーンを作成する {#step-64-create-your-second-webhook-campaign}

ユーザーからの残りのSMSメッセージをZendeskに転送するWebhook キャンペーンを設定します：

ZendeskはチケットIDを文字列として送信するため、コンテンツブロックを作成して文字列を整数に変換し、ZendeskのWebhookで使用できるようにします。

{% raw %}
`````````liquid
{% assign var = {{custom_attribute.${zendesk_ticket}}} | to_i %}{{var}}
```
{% endraw %}

Webhookコンポーザー内で：
- Webhook URL：{% raw %}https://{{url}}.zendesk.com/api/v2/tickets/{{content_blocks.${to_int}}}.json{% endraw %}
- リクエスト：PUT
- KVP：
    - Content-Type: application/JSON
    - Authorization: Basic {{Token}}

本文のサンプル：

{% raw %}
`````````liquid
{
  "ticket": {
    "comment": {
      "body": "Inbound message from {{${first_name}}} {{${last_name}}}: {{sms.${inbound_message_body}}}"
    }
}
}
```
{% endraw %}

#### ステップ6.5：2番目のWebhook キャンペーンのセットアップを完了する {#step-65-complete-second-webhook-campaign-setup}
- 「Other」カテゴリでインバウンドメッセージを送信したユーザーに対して、アクションベースのトリガーを設定します。
- 再適格性基準を設定します。
- 該当するオーディエンスを追加します（この場合、カスタム属性**zendesk_ticket_open**が**true**であること）。

[2]: {% image_buster /assets/img/zendesk/instant_chat/chat2.png %}