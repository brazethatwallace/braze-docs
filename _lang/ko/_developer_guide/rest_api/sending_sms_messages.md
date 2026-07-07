---
nav_title: SMS 메시지 전송
article_title: REST API를 사용하여 SMS 메시지 전송
page_order: 2
page_type: reference
description: "이 참조 문서에서는 Braze REST API와 API 캠페인을 사용하여 SMS 메시지를 전송하는 방법을 안내합니다."
channel:
  - SMS
---

# REST API를 사용하여 SMS 메시지 전송 {#sending-sms-messages-using-the-rest-api}

> Braze REST API를 사용하여 백엔드에서 실시간으로 트랜잭션 SMS 메시지를 전송할 수 있습니다. 이 접근 방식을 사용하면 SMS 메시지를 프로그래밍 방식으로 전송하면서 Braze 대시보드의 다른 Campaigns 및 Canvases와 함께 전달 분석을 추적할 수 있는 서비스를 구축할 수 있습니다.

특히 백엔드 시스템에서 콘텐츠가 정의되는 대량의 트랜잭션 메시징에 유용합니다. 예를 들어, 다른 사용자로부터 메시지를 받았을 때 소비자에게 알림을 보내 웹사이트를 방문하여 받은편지함을 확인하도록 안내할 수 있습니다.

이 접근 방식을 사용하면 다음을 수행할 수 있습니다:

- 백엔드에서 실시간으로 SMS 메시지를 트리거합니다.
- 모든 마케팅 소유 Campaigns 및 Canvases와 함께 분석을 추적합니다.
- 메시지 지연, 후속 리타겟팅, A/B 테스트와 같은 추가 Braze 기능으로 사용 사례를 확장합니다.
- 선택적으로, [API 트리거 전달]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)로 전환하여 Braze 대시보드에서 메시지 템플릿을 정의하면서도 백엔드에서 전송을 트리거할 수 있습니다.

REST API를 통해 SMS 메시지를 전송하려면 Braze 대시보드에서 API 캠페인을 설정한 다음 [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) 엔드포인트를 사용하여 메시지를 전송해야 합니다.

## 필수 조건 {#prerequisites}

이 가이드를 완료하려면 다음이 필요합니다:

| 요구 사항 | 설명 |
| --- | --- |
| Braze REST API 키 | `messages.send` 권한이 있는 키. 키를 생성하려면 **설정** > **API 키** > **API 키**로 이동합니다. |
| SMS 구독 그룹 | Braze 워크스페이스에 구성된 SMS 구독 그룹. |
| 백엔드 서비스 | Braze REST API에 HTTP POST 요청을 보낼 수 있는 백엔드 서비스 또는 스크립팅 환경. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 1단계: API 캠페인 생성 {#step-1-create-an-api-campaign}

1. Braze 대시보드에서 **메시징** > **Campaigns**로 이동합니다.
2. **캠페인 생성**을 선택한 다음 **API Campaigns**를 선택합니다.
3. "SMS 메시지 알림"과 같은 캠페인 이름과 설명을 입력합니다.
4. 식별 및 추적을 위한 관련 태그를 추가합니다.
5. **메시징 채널 추가**를 선택한 다음 **SMS**를 선택합니다.
6. 캠페인 페이지에 표시된 **Campaign ID**와 **Message Variation ID**를 기록해 두세요. API 요청을 구성할 때 두 값이 모두 필요합니다.

## 2단계: API를 사용하여 SMS 메시지 전송 {#step-2-send-an-sms-message-using-the-api}

[`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages) 엔드포인트에 POST 요청을 구성합니다. 요청 페이로드에 캠페인 ID, 수신자의 외부 사용자 ID 및 SMS 콘텐츠를 포함합니다.

{% alert important %}
`external_user_ids`에 참조된 각 수신자는 Braze에 이미 존재해야 합니다. API 전용 전송은 새로운 고객 프로필을 생성하지 않습니다. 전송의 일환으로 사용자를 생성해야 하는 경우, 먼저 [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)을 사용하거나 대신 [API 트리거 Campaign]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)을 사용하세요.
{% endalert %}

### 예시 요청 {#example-request}

```
POST YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

`YOUR_REST_ENDPOINT`를 워크스페이스의 [REST 엔드포인트 URL]({{site.baseurl}}/api/basics#endpoints)로 교체하세요.

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

플레이스홀더 값을 실제 ID로 교체하세요. `body` 필드는 [Liquid 개인화]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)를 지원하므로 각 수신자에게 맞춤화된 메시지 콘텐츠를 작성할 수 있습니다. SMS 메시징 오브젝트에서 지원하는 매개변수의 전체 목록은 [SMS 오브젝트]({{site.baseurl}}/api/objects_filters/messaging/sms_object)를 참조하세요.

요청을 구성한 후, 백엔드 서비스에서 Braze REST API로 POST 요청을 전송합니다.

## 3단계: 통합 확인 {#step-3-verify-your-integration}

설정을 완료한 후, 통합을 확인합니다:

1. [2단계](#step-2-send-an-sms-message-using-the-api)에 설명된 대로 API 요청을 보내고, 수신자로 자신의 사용자 ID를 사용하세요.
2. SMS 메시지가 휴대폰으로 전달되었는지 확인하세요.
3. Braze 대시보드에서 캠페인 결과 페이지로 이동하여 전송이 기록되었는지 확인하세요.
4. 캠페인을 확장할 때 결과를 면밀히 모니터링하세요.

## 고려 사항 {#considerations}

- SMS 캠페인이 관련 규정 및 통신사 요구 사항을 준수하는지 확인하세요. 모든 메시지에 옵트아웃 안내(예: "옵트아웃하려면 STOP을 문자로 보내세요")를 포함하세요. 자세한 내용은 [SMS 법률 및 규정]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations) 및 [옵트인 및 옵트아웃 키워드]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout)를 참조하세요.
- Braze [개인화 기능]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize)을 사용하여 동적 콘텐츠 및 사용자별 데이터를 포함하여 SMS 콘텐츠를 개별 소비자에 맞게 조정하세요.
- Braze REST API는 메시지 스케줄링, 캠페인 트리거 등을 위한 추가 [메시징 엔드포인트]({{site.baseurl}}/api/endpoints/messaging)를 제공합니다.