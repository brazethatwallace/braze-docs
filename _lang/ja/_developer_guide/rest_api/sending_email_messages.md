---
nav_title: メールメッセージの送信
article_title: REST APIを使用したメールメッセージの送信
page_order: 3
page_type: reference
description: "この参照記事では、Braze REST APIとAPI キャンペーンを使用してメールメッセージを送信する方法について説明します。"
channel:
  - email
---

# REST APIを使用したメールメッセージの送信 {#sending-email-messages-using-the-rest-api}

> Braze REST APIを使用して、バックエンドからリアルタイムでトランザクションメールを送信できます。このアプローチにより、プログラムでメールを送信するサービスを構築しながら、Brazeダッシュボードで他のキャンペーンやキャンバスと一緒に配信分析を追跡できます。

これは、コンテンツがバックエンドシステムで定義されるトランザクションメッセージングに特に便利です。たとえば、消費者が別のユーザーからメッセージを受信したときに通知し、Webサイトにアクセスして受信トレイを確認するよう促すことができます。

このアプローチでは、以下のことが可能です。

- バックエンドからリアルタイムでメールをトリガーする。
- 開封、クリック数、バウンスなど、マーケティング所有のすべてのキャンペーンやキャンバスと一緒に分析を追跡する。
- メッセージインタラクションデータを使用して、フォローアップのリターゲティングなどの後続メッセージをトリガーする。
- メッセージ遅延やABテストなど、追加のBraze機能でユースケースを拡張する。
- オプションで、[APIトリガー配信]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)に切り替えて、Brazeダッシュボードでメールテンプレートを定義しながら、バックエンドから送信をトリガーする。

REST APIを通じてメールを送信するには、BrazeダッシュボードでAPI キャンペーンを設定し、[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)エンドポイントを使用してメッセージを送信する必要があります。

## 前提条件 {#prerequisites}

このガイドを完了するには、以下が必要です。

| 要件 | 説明 |
| --- | --- |
| Braze REST APIキー | `messages.send` 権限を持つキー。作成するには、**設定** > **APIキー** > **APIキー**に移動します。 |
| BrazeアプリID | ワークスペース内のアプリの識別子。確認するには、**設定** > **APIキー**に移動し、**アプリ識別子**セクションを確認します。この値はメールメッセージングオブジェクトの `app_id` フィールドに必須です。詳細については、[アプリ識別子]({{site.baseurl}}/api/identifier_types)を参照してください。 |
| HTMLメールコンテンツ | 事前に準備したメールメッセージのHTML本文。 |
| バックエンドサービス | Braze REST APIにHTTP POSTリクエストを送信できるバックエンドサービスまたはスクリプティング環境。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ステップ 1: API キャンペーンを作成する {#step-1-create-an-api-campaign}

1. Brazeダッシュボードで、**Messaging** > **キャンペーン**に移動します。
2. **キャンペーンを作成**を選択し、**API キャンペーン**を選択します。
3. キャンペーンの名前と説明を入力します（例:「メールメッセージ通知」）。
4. 識別と追跡のために関連するタグを追加します。
5. **メッセージングチャネルを追加**を選択し、**Email**を選択します。
6. キャンペーンページに表示される**キャンペーン ID**をメモします。APIリクエストを構築する際にこの値が必要です。オプションで、**Message Variation ID**もメモしてください。送信統計を特定のメッセージバリエーションに帰属させたい場合は、リクエストに含めます。

## ステップ 2: APIを使用してメールを送信する {#step-2-send-an-email-using-the-api}

[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)エンドポイントへのPOSTリクエストを構築します。リクエストペイロードにキャンペーン ID、受信者の外部ユーザーID、およびメールコンテンツを含めます。

{% alert important %}
`external_user_ids` で参照される各受信者は、Brazeにすでに存在している必要があります。APIのみの送信では、新しいユーザープロファイルは作成されません。送信の一部としてユーザーを作成する必要がある場合は、まず[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を使用するか、代わりに[APIトリガーキャンペーン]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)を使用してください。
{% endalert %}

### リクエスト例 {#example-request}

```
POST https://YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

`YOUR_REST_ENDPOINT` をワークスペースの[RESTエンドポイントURL]({{site.baseurl}}/api/basics#endpoints)に置き換えてください。

{% raw %}
```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "external_user_ids": ["user123"],
  "messages": {
    "email": {
      "app_id": "YOUR_APP_ID",
      "message_variation_id": "YOUR_MESSAGE_VARIATION_ID",
      "subject": "You have a new message!",
      "from": "Notifications <notifications@example.com>",
      "body": "<html><body><h1>You have a new message!</h1><p>Hi {{${first_name}}},</p><p>You received a new message in your inbox. Click the link below to read it:</p><a href='https://yourwebsite.com/messages'>View message</a><p>Thank you for using our service!</p></body></html>"
    }
  }
}
```
{% endraw %}

プレースホルダーの値を実際のIDに置き換えてください。`from` フィールドは `"Display Name <user@example.com>"` の形式を使用する必要があります。`body` フィールドは有効なHTMLを受け付け、[Liquidパーソナライゼーション]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)をサポートしているため、各受信者に合わせてメールコンテンツをカスタマイズできます。メールメッセージングオブジェクトでサポートされるパラメーターの完全なリストについては、[メールオブジェクト]({{site.baseurl}}/api/objects_filters/messaging/email_object)を参照してください。

リクエストを構築したら、バックエンドサービスからBraze REST APIにPOSTリクエストを送信します。

## ステップ 3: インテグレーションを検証する {#step-3-verify-your-integration}

設定が完了したら、インテグレーションを検証します。

1. [ステップ 2](#step-2-send-an-email-using-the-api)の説明に従って、自分のユーザーIDを受信者としてAPIリクエストを送信します。
2. メールが受信トレイに配信されたことを確認します。
3. Brazeダッシュボードでキャンペーン結果ページに移動し、送信が記録されていることを確認します。
4. キャンペーンをスケールする際に、結果を注意深く監視します。

## 考慮事項 {#considerations}

- GDPRやCAN-SPAMなどの関連規制に準拠するために、必要なオプトアウトオプションとプライバシー通知を含めて、メールキャンペーンが準拠していることを確認してください。詳細については、[ユーザーサブスクリプションの管理]({{site.baseurl}}/user_guide/channels/email/subscriptions)および[メールのベストプラクティス]({{site.baseurl}}/user_guide/channels/email/best_practices)を参照してください。
- Brazeの[パーソナライゼーション機能]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize)を使用して、ダイナミックなコンテンツやユーザー固有のデータを含め、エンドユーザーごとにメールコンテンツをカスタマイズできます。
- Braze REST APIは、メッセージのスケジュール設定、キャンペーンのトリガーなどのための追加の[メッセージングエンドポイント]({{site.baseurl}}/api/endpoints/messaging)を提供しています。