---
nav_title: 메시지 보내기
article_title: REST API를 사용한 메시지 전송
page_order: 1
page_type: reference
description: "이 참조 문서에서는 Braze REST API를 사용하여 프로그래밍 방식으로 메시지를 전송하는 두 가지 방법을 다룹니다."
---

# REST API를 사용한 메시지 전송 {#sending-messages-using-the-rest-api}

> 두 가지 Braze 엔드포인트를 사용하여 백엔드에서 실시간으로 메시지를 보낼 수 있습니다. 각각 요청 형식이 다릅니다. 하나는 요청에 전체 메시지 내용을 포함해야 하며, 다른 하나는 Campaign ID를 요구하고 대시보드에서 정의된 콘텐츠를 전송합니다.

이 접근 방식은 API가 지원하는 모든 메시징 채널(WhatsApp, 이메일, SMS, 푸시, Content Cards, 웹훅 등)에서 작동합니다.

## 보내는 두 가지 방법 {#two-ways-to-send}

| | [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) |
| --- | --- | --- |
| **Campaign ID** | 선택 사항. 대시보드 Campaign 추적 없이 발송하려면 생략하거나, 대시보드에서 추적하려면 API Campaign ID와 각 메시지에 `message_variation_id`를 함께 제공합니다. | 필수. |
| **메시지 내용** | 요청에 `messages` 오브젝트를 포함해야 합니다(예: `messages.whats_app`, `messages.email`). | 허용되지 않음. 메시지 내용은 Braze 대시보드의 Campaign에서 정의됩니다. |
| **사용 사례** | API 요청에 완전히 명시된 내용으로 메시지를 전송합니다. | API를 통해 사전 구축된 Campaign(대시보드 내 콘텐츠)을 특정 수신자에게 트리거합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="보내는 두 가지 방법" }

전체 요청 및 응답 세부 정보는 [즉시 메시지 보내기(API 전용)]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) 및 [API 트리거 전달을 사용한 Campaign 보내기]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) 엔드포인트 참조 문서를 확인하세요.

---

## 옵션 1: 요청에 메시지 내용을 포함하여 전송(`/messages/send`) {#option-1-send-with-message-content-in-the-request-messagessend}

API 요청에서 전체 메시지 내용을 지정하려는 경우 이 엔드포인트를 사용합니다. `messages` 오브젝트(예: `messages.whats_app`, `messages.email` 또는 `messages.sms`)를 **반드시** 포함해야 합니다. Campaign 추적 없이 발송하려면 `campaign_id`를 생략하거나, 대시보드에서 발송 내역을 추적하려면 각 메시지에 API Campaign ID와 `message_variation_id`를 포함하세요(자세한 내용은 [엔드포인트 참조]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) 문서를 확인하세요).

**필수:** `messages.send` 권한이 있는 API 키.

{% alert important %}
`external_user_ids`에 포함된 각 수신자는 Braze에 이미 존재해야 합니다. 발송과 함께 사용자를 생성하려면 먼저 [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)를 사용하거나, [옵션 2](#option-2-trigger-a-campaign-with-content-in-the-dashboard-campaignstriggersend)(API 트리거 Campaign)를 대신 사용하세요.
{% endalert %}

### 예시: WhatsApp 템플릿 메시지 {#example-whatsapp-template-message}

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

전체 WhatsApp 오브젝트 사양은 [WhatsApp 오브젝트]({{site.baseurl}}/api/objects_filters/messaging/whats_app_object)를 참조하세요.

{% alert note %}
`/messages/send` 엔드포인트는 TEXT 또는 IMAGE 헤더가 포함된 WhatsApp 템플릿만 지원합니다. DOCUMENT, VIDEO 또는 기타 미디어 헤더 유형의 경우 [API 트리거 Campaign 엔드포인트]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) 또는 Braze 대시보드를 대신 사용하세요.
{% endalert %}

### 예시: 이메일 {#example-email}

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

다른 채널에 대해서는 [메시징 오브젝트]({{site.baseurl}}/api/objects_filters#messaging-objects)를 참조하세요.

---

## 옵션 2: 대시보드의 콘텐츠로 Campaign 트리거(`/campaigns/trigger/send`) {#option-2-trigger-a-campaign-with-content-in-the-dashboard-campaignstriggersend}

Braze 대시보드에서 메시지 콘텐츠가 구축된 경우(API 트리거 Campaign) 이 엔드포인트를 사용합니다. **필수** 항목인 `campaign_id`와 수신자를 전송하며, `messages` 오브젝트는 전송하지 **않습니다**.

**필수:** `campaigns.trigger.send` 권한이 있는 API 키.

### 1단계: API 트리거 Campaign 생성 {#step-1-create-an-api-triggered-campaign}

1. Braze 대시보드에서 **메시징** > **Campaigns**로 이동합니다.
2. **캠페인 생성**을 선택한 후, **API-Triggered Campaign**("API Campaign"이 아님)을 선택합니다.
3. 메시지 채널(WhatsApp, 이메일, SMS 등)을 추가하고 대시보드에서 메시지 내용을 구축합니다.
4. **Campaign ID**를 기록합니다(여러 메시지 배리언트를 사용하는 경우 **Send ID**도 함께 기록). API 요청에서 이 값들을 사용하게 됩니다.

API 트리거 Campaign 구축에 대한 자세한 내용은 [API 트리거 전달]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)을 참조하세요.

### 2단계: API를 통해 Campaign 트리거 {#step-2-trigger-the-campaign-via-the-api}

`campaign_id`와 `recipients`(또는 `broadcast`/`audience`)를 포함하여 `/campaigns/trigger/send`로 POST 요청을 전송합니다. `messages` 오브젝트는 포함하지 마세요—콘텐츠는 Campaign에서 제공됩니다.

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

전체 요청 본문(`trigger_properties`, `send_to_existing_only`, `attributes` 등 포함)은 [API 트리거 전달을 사용한 Campaign 보내기]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns#request-body) 엔드포인트 참조 문서를 확인하세요.

---

## 통합 확인 {#verify-your-integration}

1. 위의 옵션 중 하나를 사용하여 본인의 사용자 ID를 수신자로 지정하여 요청을 보냅니다.
2. 메시지가 전달되었는지 확인합니다.
3. 옵션 2를 사용하는 경우, Braze 대시보드에서 Campaign을 확인하여 발송이 기록되었는지 확인합니다.

## 고려 사항 {#considerations}

- 지원되는 환경에서 Braze [개인화 기능]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize)을 활용하여 콘텐츠를 맞춤 설정하세요.
- 관련 규정을 준수하고 필수적인 수신 거부 옵션 및 개인정보 처리방침을 포함하도록 메시징을 구성하세요.
- 추가 엔드포인트(스케줄링, Canvas 트리거 등)에 대해서는 [메시징 엔드포인트]({{site.baseurl}}/api/endpoints/messaging)를 참조하세요.