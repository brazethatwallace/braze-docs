---
nav_title: メッセージを送信する
article_title: REST APIを使ってメッセージを送信する
page_order: 1
page_type: reference
description: "このリファレンス記事では、Braze REST APIを使用してプログラムでメッセージを送信する2つの方法について説明します。"
---

# REST APIを使ってメッセージを送信する {#sending-messages-using-the-rest-api}

> バックエンドからリアルタイムでメッセージを送信するには、2つの異なるBrazeエンドポイントを使用できます。それぞれリクエストの形式が異なります。1つはリクエストにメッセージの全内容を含める方式で、もう1つはキャンペーンIDを指定してダッシュボードで定義されたコンテンツを送信する方式です。

この方法は、APIがサポートするあらゆるメッセージングチャネル（WhatsApp、メール、SMS、プッシュ通知、Content Cards、webhookなど）で利用できます。

## 2つの送信方法 {#two-ways-to-send}

| | [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) |
| --- | --- | --- |
| **キャンペーンID** | オプション。ダッシュボードでのキャンペーントラッキングなしで送信する場合は省略します。または、各メッセージにAPIキャンペーンIDと`message_variation_id`を付加してダッシュボードでトラッキングします。 | 必須。 |
| **メッセージの内容** | リクエストに`messages`オブジェクトを含める必要があります（例：`messages.whats_app`、`messages.email`）。 | 受け付けられません。メッセージの内容は、Brazeダッシュボード内のキャンペーンで定義されます。 |
| **ユースケース** | APIリクエストで内容を完全に指定したメッセージを送信します。 | APIを介して、特定の受信者に対して事前作成されたキャンペーン（ダッシュボード内のコンテンツ）をトリガーします。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="2つの送信方法" }

リクエストとレスポンスの詳細については、[メッセージを即時送信（APIのみ）]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)および[APIトリガー配信を使用したキャンペーン送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)のエンドポイントリファレンスを参照してください。

---

## オプション1：リクエストにメッセージ内容を含めて送信する（`/messages/send`） {#option-1-send-with-message-content-in-the-request-messagessend}

APIリクエストでメッセージの全内容を指定したい場合に、このエンドポイントを使用します。`messages`オブジェクトを含める**必要があります**（例：`messages.whats_app`、`messages.email`、`messages.sms`）。キャンペーントラッキングなしで送信するには`campaign_id`を省略できます。または、各メッセージにAPIキャンペーンIDと`message_variation_id`を含めることで、ダッシュボードで送信をトラッキングできます（詳細は[エンドポイントリファレンス]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)を参照してください）。

**必須：** `messages.send`権限付きのAPIキー。

{% alert important %}
`external_user_ids`の各受信者は、Brazeに既に存在している必要があります。送信の一環としてユーザーを作成するには、まず[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を使用するか、代わりに[オプション2](#option-2-trigger-a-campaign-with-content-in-the-dashboard-campaignstriggersend)（APIトリガー型キャンペーン）を使用してください。
{% endalert %}

### 例：WhatsAppテンプレートメッセージ {#example-whatsapp-template-message}

```
POST YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "external_user_ids": ["user123"],
  "messages": {
    "whats_app": {
      "app_id": "YOUR_APP_ID",
      "subscription_group_id": "YOUR_WHATSAPP_SUBSCRIPTION_GROUP_ID",
      "message_type": "template_message",
      "message": {
        "template_name": "new_message_received",
        "template_language_code": "en_US"
      }
    }
  }
}
```

WhatsAppオブジェクトの完全な仕様については、[WhatsAppオブジェクト]({{site.baseurl}}/api/objects_filters/messaging/whats_app_object)を参照してください。

{% alert note %}
`/messages/send`エンドポイントは、TEXTまたはIMAGEヘッダーを持つWhatsAppテンプレートのみをサポートしています。DOCUMENT、VIDEO、その他のメディアヘッダータイプについては、代わりに[APIトリガー型キャンペーンエンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)またはBrazeダッシュボードを使用してください。
{% endalert %}

### 例：メール {#example-email}

```json
{
  "external_user_ids": ["user123"],
  "messages": {
    "email": {
      "app_id": "YOUR_APP_ID",
      "subject": "Your order has shipped",
      "from": "no-reply@example.com",
      "body": "<p>Your order #12345 is on its way.</p>"
    }
  }
}
```

他のチャネルについては、[メッセージングオブジェクト]({{site.baseurl}}/api/objects_filters#messaging-objects)を参照してください。

---

## オプション2：ダッシュボードのコンテンツでキャンペーンをトリガーする（`/campaigns/trigger/send`） {#option-2-trigger-a-campaign-with-content-in-the-dashboard-campaignstriggersend}

メッセージの内容がBrazeダッシュボードで作成されている場合（APIトリガー型キャンペーン）に、このエンドポイントを使用します。**必須**の`campaign_id`と受信者を送信します。`messages`オブジェクトは送信**しません**。

**必須：** `campaigns.trigger.send`権限付きのAPIキー。

### ステップ1：APIトリガー型キャンペーンを作成する {#step-1-create-an-api-triggered-campaign}

1. Brazeダッシュボードで、**メッセージング** > **キャンペーン**に移動します。
2. **キャンペーンを作成**を選択し、次に**APIトリガー型キャンペーン**（「APIキャンペーン」ではありません）を選択します。
3. メッセージチャネル（WhatsApp、メール、SMSなど）を追加し、ダッシュボードでメッセージ内容を作成します。
4. **キャンペーンID**（複数のメッセージバリアントを使用する場合は**Send ID**も）をメモしておきます。これらをAPIリクエストで使用します。

APIトリガー型キャンペーンの作成に関する詳細は、[APIトリガー配信]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)を参照してください。

### ステップ2：API経由でキャンペーンをトリガーする {#step-2-trigger-the-campaign-via-the-api}

`campaign_id`と`recipients`（または`broadcast`/`audience`）を指定して、`/campaigns/trigger/send`にPOSTリクエストを送信します。`messages`オブジェクトは含めないでください。コンテンツはキャンペーンから取得されます。

```
POST YOUR_REST_ENDPOINT/campaigns/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "recipients": [
    {
      "external_user_id": "user123"
    }
  ]
}
```

リクエスト本文の全体（`trigger_properties`、`send_to_existing_only`、`attributes`などを含む）については、[APIトリガー配信を使用したキャンペーン送信]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns#request-body)のエンドポイントリファレンスを参照してください。

---

## 統合を確認する {#verify-your-integration}

1. 上記のいずれかの方法でリクエストを送信します。その際、自分のユーザーIDを受信者として指定します。
2. メッセージが配信されたことを確認します。
3. オプション2を使用する場合、Brazeダッシュボードでキャンペーンを確認し、送信が記録されていることを確認します。

## 考慮事項 {#considerations}

- 対応している場合は、Brazeの[パーソナライゼーション機能]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize)を使ってコンテンツをカスタマイズしてください。
- メッセージングが関連規制に準拠していることを確認し、必要なオプトアウトオプションとプライバシー通知を含めてください。
- その他のエンドポイント（スケジューリング、キャンバストリガーなど）については、[メッセージングエンドポイント]({{site.baseurl}}/api/endpoints/messaging)を参照してください。