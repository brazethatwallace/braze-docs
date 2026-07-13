---
nav_title: SMSメッセージを送信する
article_title: REST APIを使用したSMSメッセージの送信
page_order: 2
page_type: reference
description: "このリファレンス記事では、Braze REST APIとAPI キャンペーンを使用してSMSメッセージを送信する方法を説明します。"
channel:
  - SMS
---

# REST APIを使用したSMSメッセージの送信 {#sending-sms-messages-using-the-rest-api}

> Braze REST APIを使用して、バックエンドからトランザクションSMSメッセージをリアルタイムで送信します。この方法を使えば、プログラムでSMSメッセージを送信するサービスを構築しながら、Brazeダッシュボード上で他のキャンペーンやキャンバスと並行して配信分析をトラッキングできます。

これは特に、バックエンドシステムでコンテンツが定義されている大量のトランザクションメッセージングにおいて有用です。たとえば、他のユーザーからメッセージが届いた際に消費者に通知し、Webサイトにアクセスして受信トレイを確認するよう促すことができます。

この方法を使えば、次のことができます：

- バックエンドからリアルタイムでSMSメッセージをトリガーする。
- マーケティング部門が所有するすべてのキャンペーンやキャンバスと並行して分析データをトラッキングする。
- メッセージ遅延、フォローアップリターゲティング、ABテストといった追加のBraze機能でユースケースを拡張する。
- 必要に応じて、[APIトリガー配信]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)に切り替えることで、メッセージテンプレートをBrazeダッシュボードで定義しつつ、送信はバックエンドからトリガーし続けることができます。

REST API経由でSMSメッセージを送信するには、BrazeダッシュボードでAPI キャンペーンを設定し、[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)エンドポイントを使用してメッセージを送信する必要があります。

## 前提条件 {#prerequisites}

このガイドを完了するには、以下が必要です：

| 必要条件 | 説明 |
| --- | --- |
| Braze REST APIキー | `messages.send` 権限を持つキー。作成するには、**設定** > **APIキー** > **APIキー**に移動します。 |
| SMSサブスクリプショングループ | Brazeワークスペースで設定されたSMSサブスクリプショングループ。 |
| バックエンドサービス | Braze REST APIに対してHTTP POSTリクエストを送信できるバックエンドサービスまたはスクリプト環境。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ステップ 1：API キャンペーンを作成する {#step-1-create-an-api-campaign}

1. Brazeダッシュボードで、**メッセージング** > **キャンペーン**に移動します。
2. **キャンペーンを作成**を選択し、次に**API キャンペーン**を選択します。
3. キャンペーンの名前と説明を入力します（例：「SMS通知」）。
4. 識別とトラッキングのために関連タグを追加します。
5. **メッセージングチャネルを追加**を選択し、次に**SMS**を選択します。
6. キャンペーンページに表示されている**キャンペーン ID**と**Message Variation ID**をメモしておきます。APIリクエストを構築する際に両方の値が必要です。

## ステップ 2：APIを使ってSMSメッセージを送信する {#step-2-send-an-sms-message-using-the-api}

[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages)エンドポイントへのPOSTリクエストを構築します。リクエストペイロードにキャンペーン ID、受信者の外部ユーザーID、およびSMSコンテンツを含めます。

{% alert important %}
`external_user_ids`で参照されている各受信者は、すでにBrazeに存在している必要があります。API経由のみの送信では、新しいユーザープロファイルは作成されません。送信の一部としてユーザーを作成する必要がある場合は、まず[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を使用するか、代わりに[APIトリガー型キャンペーン]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)を使用してください。
{% endalert %}

### リクエスト例 {#example-request}

```
POST YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

`YOUR_REST_ENDPOINT`を、ワークスペースの[RESTエンドポイントURL]({{site.baseurl}}/api/basics#endpoints)に置き換えます。

{% raw %}
```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "external_user_ids": ["user123"],
  "messages": {
    "sms": {
      "app_id": "YOUR_APP_ID",
      "subscription_group_id": "YOUR_SMS_SUBSCRIPTION_GROUP_ID",
      "message_variation_id": "YOUR_MESSAGE_VARIATION_ID",
      "body": "Hi {{${first_name}}}, you have a new message in your inbox. Check it out at https://yourwebsite.com/messages. Text STOP to opt out."
    }
  }
}
```
{% endraw %}

プレースホルダーの値を実際のIDに置き換えます。`body`フィールドは[Liquidパーソナライゼーション]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)をサポートしているため、メッセージの内容を各受信者に合わせて調整できます。SMSメッセージングオブジェクトがサポートするパラメーターの完全な一覧については、[SMSオブジェクト]({{site.baseurl}}/api/objects_filters/messaging/sms_object)を参照してください。

リクエストを構築した後、バックエンドサービスからBraze REST APIへPOSTリクエストを送信します。

## ステップ 3：統合を確認する {#step-3-verify-your-integration}

設定を完了したら、統合を確認します：

1. [ステップ 2](#step-2-send-an-sms-message-using-the-api)で説明した通りにAPIリクエストを送信します。その際、受信者として自身のユーザーIDを使用します。
2. SMSメッセージが自分の携帯電話に届いていることを確認します。
3. Brazeダッシュボードで、キャンペーンの結果ページに移動し、送信が記録されていることを確認します。
4. キャンペーンを拡大するにつれて、結果を注意深く監視します。

## 考慮事項 {#considerations}

- SMSキャンペーンが関連規制および通信事業者の要件に準拠していることを確認してください。すべてのメッセージにオプトアウトの手順（「STOPと送信してオプトアウト」など）を含めてください。詳細については、[SMSに関する法令]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations)および[オプトインとオプトアウトのキーワード]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout)を参照してください。
- Brazeの[パーソナライゼーション機能]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize)を使用して、ダイナミックなコンテンツやユーザー固有のデータを含め、SMSコンテンツをエンドユーザーに合わせてカスタマイズできます。
- Braze REST APIは、メッセージのスケジュール設定やキャンペーンのトリガーなどを行うための追加の[メッセージングエンドポイント]({{site.baseurl}}/api/endpoints/messaging)を提供しています。