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

# キャンペーンアラート {#campaign-alerts}

> 何か想定通りでないことが起きた場合にアラートでお知らせし、すべてが順調に進んでいるという安心感を提供します。キャンペーンしきい値アラートは安心感をもたらします。重要なキャンペーンが想定より多くまたは少ないメッセージを送信した場合に、いち早く把握できます。

キャンバスでも同じ機能をお探しですか？[キャンバスしきい値アラート]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/canvas_threshold_alerts)を参照してください。

キャンペーンアラートは、以下のキャンペーンで利用できます。

- 定期スケジュールキャンペーン
- アクションベースキャンペーン
- APIトリガーキャンペーン

## キャンペーンアラートの設定 {#setting-up-your-campaign-alert}

キャンペーンの分析ページに移動して、アラートの設定を開始します。**アラートを設定** を選択すると、アラートのしきい値の上限と下限、およびアラートの受信者とチャネルを指定できます。

![キャンペーン監視ダイアログボックス。「キャンセル」と「保存」の2つのボタンがあります。]({% image_buster /assets/img_archive/campaign_alerts.png %})

スケジュールされた定期キャンペーンの場合、キャンペーンが送信されるたびに送信されるメッセージの上限と下限のしきい値を設定できます。トリガーキャンペーンの場合、1時間あたりおよび1日あたりに送信されるメッセージ数の上限と下限のしきい値を設定できます。

メールアラート、webhookアラート、またはその両方を設定できます。webhookアラートは、Slackチャネルにアラートを送信できるため、非常に便利です。キャンペーンアラートとSlackの連携の詳細については、Slackのドキュメント「[Sending messages using incoming webhooks](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/)」を参照してください。

{% alert note %}
今後のキャンペーンにキャンペーンアラートを設定すると、キャンペーンの開始前や終了後に更新を受け取る場合があります。これは、キャンペーンが手動で停止されるまで、キャンペーンアラートが送信され続けるためです。
{% endalert %}

## キャンペーンアラートWebhookペイロード {#campaign-alert-webhook-payload}

以下は、キャンペーンアラートWebhookの本文のサンプルペイロードです。この例では、特定のキャンペーン送信で送信メッセージ数が500件を下回った場合に送信されるよう設定されたアラートを使用しています。

```
{"text":"Your campaign 'Sample campaign' had fewer than 500 messages sent this run. It had 4 messages sent this run. See https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"data":{"url":"https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"app_group_name":"Sample workspace",
"campaign_name":"Sample campaign",
"campaign_api_id":"fe787bc5-d13f-4123-b22f-3bd48f9fc407","upper_threshold":0,"lower_threshold":500,"value":4}}
```

