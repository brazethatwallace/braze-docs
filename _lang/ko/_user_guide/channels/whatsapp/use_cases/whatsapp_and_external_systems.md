---
nav_title: "WhatsApp 및 외부 시스템"
article_title: "WhatsApp 및 외부 시스템"
page_order: 2
description: "이 참조 문서에서는 Braze와 WhatsApp 통합을 외부 AI 또는 커뮤니케이션 시스템과 연동하는 방법을 단계별로 안내합니다."
page_type: reference
alias: /whatsapp_external_system_integration/
channel:
  - WhatsApp
---

# Braze와 WhatsApp을 외부 AI 또는 커뮤니케이션 시스템과 통합하기 {#integrate-braze-and-whatsapp-with-an-external-ai-or-communication-system}

> WhatsApp 채널에서 AI 챗봇과 실시간 상담원 전환 기능을 활용하여 고객 지원 운영을 간소화하세요. 일상적인 문의를 자동화하고 필요할 때 원활하게 상담원에게 전환함으로써 응답 시간을 크게 단축하고 전반적인 고객 경험을 향상시킬 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| - | - |
| 외부 시스템 | API를 사용하여 챗봇, 자동화된 클라이언트 서비스 시스템 또는 두 가지 모두를 구축하고 관리할 수 있는 서드파티 AI 또는 커뮤니케이션 시스템. |
| Braze와 WhatsApp 통합 | Braze에서 관리하는 WhatsApp 번호 |
| Braze REST API 키 | `campaigns.trigger.send` 권한이 있는 REST API 키. Braze 대시보드에서 **설정** > **API 키**로 이동하여 생성할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 작동 방식 {#how-it-works}

Braze와 외부 AI 또는 커뮤니케이션 시스템 간의 통합은 양방향으로 작동하며, Braze가 커뮤니케이션 채널 역할을 하고 외부 시스템이 메시지를 처리하고 응답을 생성하는 "인텔리전스" 역할을 합니다.

통합 워크플로는 두 가지 주요 흐름으로 나눌 수 있습니다.
**인바운드 흐름:** 사용자의 메시지가 Braze에 도착한 후 처리를 위해 외부 시스템으로 전달됩니다.
**아웃바운드 흐름:** 메시지를 처리한 후 외부 시스템이 Braze에 응답을 보내고, Braze가 최종 사용자에게 메시지를 전달합니다.

이 커뮤니케이션을 효율적으로 자동화하기 위해 이 통합에서는 두 가지 주요 Braze 기능을 사용합니다: [웹훅 Campaign]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) 및 [API 트리거 Campaign]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery).

![Braze WhatsApp 채널과 외부 시스템 간의 통합 아키텍처.]({% image_buster /assets/img/whatsapp/external_system_architecture.png %})
## 통합 구성하기 {#configuring-the-integration}

### 1단계: 인바운드 메시지용 웹훅 Campaign 생성하기 {#step-1-create-a-webhook-campaign-for-inbound-messages}

먼저 Braze에서 수신한 WhatsApp 메시지를 외부 시스템으로 전송하는 방법을 설정하기 위해 웹훅 Campaign을 생성합니다.

1. Braze에서 웹훅 Campaign을 생성합니다.
2. 웹훅 작성기에서 **Compose webhook**을 선택합니다.
3. **Webhook URL** 필드에 메시지를 수신할 외부 시스템의 API 엔드포인트(URL)를 입력합니다.
4. 요청 본문에서 **Raw text**를 선택하고 사용자의 `external_id`와 전화번호, 메시지 콘텐츠 및 기타 관련 정보를 포함하는 개인화된 페이로드를 입력합니다. 예시:

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
5. Campaign 작성기의 **Schedule Delivery** 단계에서 전달 유형으로 **Action-Based**를 선택하고 Campaign 트리거로 **Send a WhatsApp inbound message**를 선택합니다.

![WhatsApp 인바운드 메시지 전송을 트리거로 하는 실행 기반 전달.]({% image_buster /assets/img/whatsapp/inbound_message_trigger.png %})

{: start="6"}
6. Campaign 작성을 완료한 후 저장하고 시작합니다. Campaign을 시작하면 메시지가 수신될 때마다 Braze가 외부 시스템으로 웹훅을 전송합니다.

### 2단계: 아웃바운드 메시지용 API 트리거 Campaign 생성하기 {#step-2}

다음으로, 외부 시스템이 WhatsApp을 통해 사용자에게 메시지를 다시 보낼 수 있도록 API 트리거 Campaign을 생성합니다.

1. Braze에서 WhatsApp Campaign을 생성합니다.
2. 메시지 작성기에서 **WhatsApp Template Message** 또는 **Response Message**를 선택한 다음 템플릿 또는 응답 메시지 레이아웃을 선택합니다. 인바운드 메시지가 24시간 WhatsApp 기간을 열었으므로 모든 응답 메시지 레이아웃을 선택할 수 있습니다.

![메시지 유형과 메시지 레이아웃을 선택하는 옵션이 있는 메시지 작성기.]({% image_buster /assets/img/whatsapp/response_message_layout.png %})

{: start="3"}
3. 메시지 본문에 API 트리거 등록정보를 추가합니다. 예: {% raw %}`{{api_trigger_properties.${external_system_msg+body}}}`{% endraw %}. 이를 통해 AI 시스템이 전송할 메시지를 채울 수 있습니다.

![트리거 등록정보가 포함된 메시지 본문이 있는 메시지 작성기.]({% image_buster /assets/img/whatsapp/api_trigger_properties.png %})

{: start="4"}
4. Campaign 작성기의 **Schedule Delivery** 단계에서 전달 유형으로 **Action-Based**를 선택합니다.
5. Campaign을 저장한 후 Braze가 이 Campaign에 대해 생성한 고유 `campaign_id`를 기록해 둡니다. 다음 단계에서 이 ID가 필요합니다.

### 3단계: 외부 시스템을 API 트리거 Campaign에 연결하기 {#step-3-connect-the-external-system-to-the-api-triggered-campaign}

마지막으로, 외부 시스템이 Braze를 호출하여 응답을 전송하도록 구성합니다.

1. 외부 시스템의 코드에서 수신된 메시지를 처리하고 응답을 생성한 후 Braze `/messages/send` 엔드포인트에 POST 요청을 보냅니다.
2. `/messages/send` 요청 본문에 [2단계](#step-2)의 `campaign_id`, 사용자의 `external_id`, 외부 시스템 응답의 콘텐츠를 포함합니다.
3. [2단계](#step-2)의 API 트리거 등록정보를 사용하여 외부 시스템의 응답을 삽입하고, 인증을 위해 요청 헤더에 API 키를 포함하는 것을 잊지 마세요. 다음 cURL 예시를 참고하세요:

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

이제 AI 챗봇 워크플로를 구축하기 위한 탄탄한 기반이 마련되었습니다!

### 워크플로 커스터마이징 {#customizing-your-workflow}

통합 로직을 확장하여 다음을 수행할 수 있습니다:
- 다양한 키워드를 사용하여 서로 다른 웹훅 Campaign을 트리거합니다.
- 다단계 API 트리거 Campaign으로 더 복잡한 대화 흐름을 생성합니다.
- 채팅 정보를 Braze에 커스텀 속성으로 기록하여 고객 프로필을 강화하고 향후 Campaign을 세분화합니다.