---
nav_title: キャンペーンアラート
article_title: キャンペーンアラート
page_order: 6

page_type: reference
description: "このリファレンス記事では、キャンペーンアラートの概要、そのメリット、および安心感を得るための設定方法について説明します。"
tool: Campaigns
channel:
- email
- webhooks

---

# キャンペーンアラート

> 何か想定通りでないことが起きた場合にアラートでお知らせし、すべてが順調に進んでいるという安心感を提供します。キャンペーンしきい値アラートは安心感をもたらします。重要なキャンペーンが想定より多くまたは少ないメッセージを送信した場合に、いち早く把握できます。

キャンペーンアラートは、以下のキャンペーンで利用できます。

- 定期スケジュールキャンペーン
- アクションベースのキャンペーン
- APIトリガーキャンペーン

## キャンペーンアラートの設定

キャンペーンの分析ページに移動して、アラートの設定を開始します。**Set Up Alert** を選択すると、アラートのしきい値の上限と下限、およびアラートの受信者とチャネルを指定できます。

![「キャンセル」と「保存」の2つのボタンがあるキャンペーンモニタリングダイアログボックス。]({% image_buster /assets/img_archive/campaign_alerts.png %})

定期スケジュールキャンペーンの場合、キャンペーンが送信されるたびに送信されるメッセージ数の上限と下限のしきい値を設定できます。トリガーキャンペーンの場合、1時間あたりおよび1日あたりに送信されるメッセージ数の上限と下限のしきい値を設定できます。

メールアラート、Webhook アラート、またはその両方を設定できます。Webhook アラートは、Slack チャネルにアラートを送信できるため、非常に便利です。キャンペーンアラートと Slack の連携の詳細については、Slack のドキュメント「[Sending messages using incoming webhooks](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/)」を参照してください。

{% alert note %}
今後のキャンペーンにキャンペーンアラートを設定すると、キャンペーンの開始前や終了後にも更新を受け取る場合があります。これは、キャンペーンが手動で停止されるまでキャンペーンアラートが送信され続けるためです。
{% endalert %}

## キャンペーンアラートの Webhook ペイロード

以下は、キャンペーンアラート Webhook の本文のサンプルペイロードです。この例では、特定のキャンペーン送信で送信メッセージ数が500を下回った場合に送信されるよう設定されたアラートを使用しています。

```
{"text":"Your campaign 'Sample campaign' had fewer than 500 messages sent this run. It had 4 messages sent this run. See https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"data":{"url":"https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"app_group_name":"Sample workspace",
"campaign_name":"Sample campaign",
"campaign_api_id":"fe787bc5-d13f-4123-b22f-3bd48f9fc407","upper_threshold":0,"lower_threshold":500,"value":4}}
```

