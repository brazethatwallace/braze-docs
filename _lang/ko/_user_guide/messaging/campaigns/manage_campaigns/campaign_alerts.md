---
nav_title: 캠페인 알림
article_title: 캠페인 알림
page_order: 6

page_type: reference
description: "이 참조 문서에서는 캠페인 알림의 개요, 이점, 그리고 안심하고 운영할 수 있도록 알림을 설정하는 방법을 설명합니다."
tool: Campaigns
channel:
- email
- webhooks

---

# 캠페인 알림 {#campaign-alerts}

> 예상과 다른 상황이 발생했을 때 알림을 보내드리며, 모든 것이 순조롭게 진행되고 있다는 안심을 드리고자 합니다. 캠페인 임계값 알림은 안심을 제공합니다. 중요한 캠페인이 예상보다 많거나 적은 메시지를 발송할 때 가장 먼저 알 수 있습니다.

Canvas에서도 동일한 기능을 찾고 계신가요? [Canvas 임계값 알림]({{site.baseurl}}/user_guide/messaging/canvas/managing_canvases/canvas_threshold_alerts)을 참조하세요.

캠페인 알림은 다음 캠페인에서 사용할 수 있습니다:

- 반복 스케줄 캠페인
- 액션 기반 캠페인
- API 트리거 캠페인

## Campaign 알림 설정하기 {#setting-up-your-campaign-alert}

Campaign의 분석 페이지로 이동하여 알림 설정을 시작합니다. **Set Up Alert**를 선택하면 상한 및 하한 알림 임계값과 알림 수신자 및 채널을 지정할 수 있습니다.

![취소 및 저장 두 개의 버튼이 있는 Campaign 모니터링 대화 상자.]({% image_buster /assets/img_archive/campaign_alerts.png %})

예약된 반복 Campaign의 경우, Campaign이 발송될 때마다 전송되는 메시지의 상한 및 하한 임계값을 설정할 수 있습니다. 트리거 Campaign의 경우, 시간별 및 일별로 전송되는 메시지 수의 상한 및 하한 임계값을 설정할 수 있습니다.

이메일 알림, 웹훅 알림 또는 둘 다 설정할 수 있습니다. 웹훅 알림은 Slack 채널로 알림을 보낼 수 있어 매우 유용합니다. Campaign 알림을 Slack과 연동하는 방법에 대한 자세한 내용은 Slack의 [수신 웹훅을 사용하여 메시지 보내기](https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks/) 설명서를 참조하세요.

{% alert note %}
향후 Campaign에 대해 알림을 설정하면 Campaign이 시작되기 전과 종료된 후에도 업데이트를 받을 수 있습니다. 이는 Campaign 알림이 수동으로 중지될 때까지 계속 전송되기 때문입니다.
{% endalert %}

## Campaign 알림 웹훅 페이로드 {#campaign-alert-webhook-payload}

다음은 Campaign 알림 웹훅 본문의 샘플 페이로드입니다. 이 예시에서는 특정 Campaign 발송에서 메시지 발송 수가 500건 미만일 때 전송되도록 구성된 알림을 사용합니다.

```
{"text":"Your campaign 'Sample campaign' had fewer than 500 messages sent this run. It had 4 messages sent this run. See https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"data":{"url":"https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"app_group_name":"Sample workspace",
"campaign_name":"Sample campaign",
"campaign_api_id":"fe787bc5-d13f-4123-b22f-3bd48f9fc407","upper_threshold":0,"lower_threshold":500,"value":4}}
```

