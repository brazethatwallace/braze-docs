---
nav_title: Zendesk
article_title: Zendesk Chat
description: "Zendesk Chat을 Braze와 통합하고 양방향 SMS 대화를 설정하는 방법을 알아보세요."
alias: /partners/zendesk_chat/
page_type: partner
search_tag: Partner

---

# Zendesk Chat

> [Zendesk Chat](https://www.zendesk.com/service/messaging/)은 각 플랫폼의 웹훅을 사용하여 양방향 SMS 대화를 설정합니다. 사용자가 고객지원을 요청하면 Zendesk에 티켓이 생성됩니다. 상담원 응답은 API 트리거 SMS Campaign을 통해 Braze로 전달되고, 사용자 답장은 다시 Zendesk로 전송됩니다.

## 필수 조건 {#prerequisites}


| 요구 사항 | 설명 |
|---|---|
| Zendesk 계정 | 이 파트너십을 활용하려면 Zendesk 계정이 필요합니다.|
| Zendesk 기본 승인 토큰 | Zendesk 기본 승인 토큰은 Braze에서 Zendesk로 아웃바운드 웹훅 요청을 보내는 데 사용됩니다.|
| Braze REST API 키 | `campaigns.trigger.send` 권한이 있는 Braze REST API 키. Braze 대시보드에서 **설정** > **API 키**로 이동하여 생성할 수 있습니다.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 활용 사례 {#use-cases}

Braze SMS 기능과 Zendesk 실시간 상담원 응답을 결합하여 사용자 문의에 대해 사람이 직접 신속하게 지원함으로써 고객지원 효율성을 높이세요.

## Zendesk Chat 통합하기 {#integrating-zendesk-chat}

### 1단계: Zendesk에서 웹훅 생성하기 {#step-1-create-a-webhook-in-zendesk}

1. Zendesk 개발자 콘솔에서 웹훅으로 이동합니다: {% raw %}`https://{{url}}.zendesk.com/admin/apps-integrations/webhooks/webhooks`{% endraw %}
2. **Create Webhook** 아래에서 **Trigger or automation**을 선택합니다.
3. **Endpoint URL**에 **/campaign/trigger/send** 엔드포인트를 추가합니다.
4. **Authentication** 아래에서 **Bearer token**을 선택하고 `campaigns.trigger.send` 권한이 있는 Braze REST API 키를 추가합니다.

![Zendesk 웹훅 예시.]({% image_buster /assets/img/zendesk/instant_chat/chat1.png %}){: style="max-width:70%;"}

### 2단계: 아웃바운드 SMS Campaign 생성하기 {#step-2-create-an-outbound-sms-campaign}

다음으로, Zendesk의 웹훅을 수신하고 고객에게 커스텀 SMS 응답을 보내는 SMS Campaign을 생성합니다.

#### 2.1단계: 메시지 작성하기 {#step-21-compose-your-message}

Zendesk가 API를 통해 메시지 콘텐츠를 전송하면 다음 형식으로 전달됩니다:

```
**----------------------------------------------\n\n{Replier Name}, {Replier Date}\n\n{Message}**
```

따라서 이 문자열에서 메시지에 표시할 세부 정보를 추출해야 합니다. 그렇지 않으면 사용자에게 모든 세부 정보가 표시됩니다.

![서식이 없는 SMS 예시.]({% image_buster /assets/img/zendesk/instant_chat/chat2.png %}){: style="max-width:40%;"}

**Message** 텍스트 상자에 다음 Liquid 코드와 옵트아웃 문구 또는 기타 정적 콘텐츠를 추가합니다:

{% raw %}
```liquid
{% assign body = {{api_trigger_properties.${msg_body}}} %}
{% assign msg = body | split: "
" %}
New message from Zendesk:
{{msg[2]}}

Feel free to respond directly to this number!
```
{% endraw %}

![서식이 포함된 SMS 예시.]({% image_buster /assets/img/zendesk/instant_chat/chat3.png %}){: style="max-width:70%;"}

#### 2.2단계: 전달 스케줄 설정하기 {#step-22-schedule-the-delivery}

전달 유형으로 **API-Triggered delivery**를 선택한 다음, 다음 단계에서 사용할 Campaign ID를 복사합니다.

![API 트리거 전달]({% image_buster /assets/img/zendesk/instant_chat/chat4.png %}){: style="max-width:70%;"}

마지막으로 **Delivery Controls** 아래에서 재자격을 활성화합니다.

!["Delivery Controls"에서 재자격이 활성화된 모습.]({% image_buster /assets/img/zendesk/instant_chat/chat5.png %})

### 3단계: Zendesk에서 상담원 답변을 Braze로 전달하는 트리거 생성하기 {#step-3-create-a-trigger-in-zendesk-to-forward-agent-replies-to-braze}

**Objects and rules** > **Business rules** > **Triggers**로 이동합니다.

1. 새 **카테고리**를 생성합니다(예: **Trigger a message**).
2. 새 **트리거**를 생성합니다(예: **Respond via SMS Braze**).
3. **Conditions** 아래에서 다음을 선택합니다:
- **Ticket>Comment**이 **Present and requester can see comment**인 경우 — 티켓 업데이트에 새 공개 댓글이 포함될 때마다 메시지가 트리거됩니다.
- **Ticket>Update**가 **Web service (API)**가 *다음이 아님* — 사용자가 Braze에서 메시지를 보낼 때 해당 메시지가 다시 사용자의 휴대폰으로 전달되지 않도록 합니다. Zendesk에서 오는 메시지만 전달됩니다.

![SMS Braze를 통해 응답.]({% image_buster /assets/img/zendesk/instant_chat/chat6.png %}){: style="max-width:70%;"}

**Actions** 아래에서 **Notify by Webhook**을 선택하고 1단계에서 생성한 엔드포인트를 선택합니다. 다음으로 API 호출의 본문을 지정합니다. [2.2단계](#step-22-schedule-the-delivery)의 `campaign_id`를 요청 본문에 입력합니다.

![SMS Braze JSON 본문을 통해 응답.]({% image_buster /assets/img/zendesk/instant_chat/chat7.png %}){: style="max-width:70%;"}

{% raw %}
```liquid
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


### 4단계: Zendesk에서 티켓 종료 시 사용자를 업데이트하는 트리거 생성하기 {#step-4-create-a-trigger-in-zendesk-to-update-a-user-when-a-ticket-is-closed}

사용자에게 티켓이 종료되었음을 알리려면 Braze에서 템플릿 응답 본문으로 새 Campaign을 생성합니다.

![티켓이 종료되면 사용자를 업데이트합니다.]({% image_buster /assets/img/zendesk/instant_chat/chat8.png %}){: style="max-width:70%;"}

**API Triggered delivery**를 선택하고 Campaign ID를 복사합니다.

다음으로, 티켓이 종료될 때 Braze에 알리는 트리거를 설정합니다:
- 카테고리: **Trigger a message**
- 조건에서 **Ticket>Ticket Status**를 선택하고 **Solved**로 변경합니다.

![Zendesk에서 해결된 티켓 설정.]({% image_buster /assets/img/zendesk/instant_chat/chat9.png %}){: style="max-width:70%;"}

**Actions** 아래에서 **Notify by Webhook**을 선택하고 방금 생성한 두 번째 엔드포인트를 선택합니다. 거기에서 API 호출의 본문을 지정해야 합니다:

![해결된 티켓 JSON 본문.]({% image_buster /assets/img/zendesk/instant_chat/chat10.png %}){: style="max-width:70%;"}

{% raw %}
```liquid
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

### 5단계: Zendesk에서 커스텀 사용자 필드 추가하기 {#step-5-add-a-custom-user-field-in-zendesk}

관리 센터에서 사이드바의 **People**을 선택한 다음 **Configuration** > **User fields**를 선택합니다. 커스텀 사용자 필드 `braze_external_id`를 추가합니다.

### 6단계: 인바운드 SMS 전달 설정하기 {#step-6-set-up-inbound-sms-forwarding}

다음으로, Braze에서 두 개의 새 웹훅 Campaign을 생성하여 고객의 인바운드 SMS를 Zendesk 받은편지함으로 전달할 수 있도록 합니다.

| Campaign | 목적 |
|--------------------|--------------------------------------------------------------------------------------|
| 웹훅 Campaign 1 | Zendesk에 새 티켓을 생성합니다. |
| 웹훅 Campaign 2 | 고객이 인바운드로 보낸 모든 대화형 SMS 응답을 Zendesk로 전달합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 6: Set up inbound-SMS forwarding" }

#### 6.1단계: SMS 키워드 카테고리 생성하기 {#step-61-create-an-sms-keyword-category}

Braze 대시보드에서 **Audience**로 이동하여 **SMS 구독 그룹**을 선택한 다음 **Add Custom Keyword**를 선택합니다. 다음 필드를 작성하여 Zendesk 전용 SMS 키워드 카테고리를 생성합니다.

| 필드 | 설명 |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| 키워드 카테고리 | 키워드 카테고리의 이름입니다(예: `ZendeskSMS1`). |
| 키워드 | 커스텀 키워드입니다(예: `SUPPORT`). |
| 답장 메시지 | 키워드가 감지될 때 전송되는 메시지입니다(예: "고객 서비스 담당자가 곧 연락드리겠습니다."). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 6.1: Create an SMS keyword category" }

![Braze의 SMS 키워드 카테고리 예시.]({% image_buster /assets/img/zendesk/instant_chat/chat11.png %}){: style="max-width:70%;"}

#### 6.2단계: 첫 번째 웹훅 Campaign 생성하기 {#step-62-create-your-first-webhook-campaign}

Braze 대시보드에서 첫 번째 웹훅 Campaign을 생성합니다. 이 메시지는 Zendesk에 고객지원이 요청되었음을 알립니다.

웹훅 작성기에서 다음 필드를 작성합니다:
- 웹훅 URL: {% raw %}https://{{url}}.zendesk.com/api/v2/tickets{% endraw %}
- HTTP 메서드: POST
- 요청 헤더:
- Content-Type: application/json
- Authorization: Basic {{Token}}
- 요청 본문:

{% raw %}
```liquid
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

![두 개의 필수 헤더가 포함된 요청 예시.]({% image_buster /assets/img/zendesk/instant_chat/chat12.png %}){: style="max-width:70%;"}


#### 6.3단계: 첫 번째 전달 스케줄 설정하기 {#step-63-schedule-the-first-delivery}

**Schedule Delivery**에서 **Action-Based Delivery**를 선택한 다음 트리거 유형으로 **Send an SMS Inbound Message**를 선택합니다. 또한 이전에 설정한 SMS 구독 그룹과 키워드 카테고리를 추가합니다.

![첫 번째 웹훅 Campaign의 "Schedule Delivery" 페이지.]({% image_buster /assets/img/zendesk/instant_chat/chat13.png %})

**Delivery Controls** 아래에서 재자격을 활성화합니다.

![첫 번째 웹훅 Campaign의 "Delivery Controls"에서 재자격이 선택된 모습.]({% image_buster /assets/img/zendesk/instant_chat/chat14.png %})

#### 6.4단계: 두 번째 웹훅 Campaign 생성하기 {#step-64-create-your-second-webhook-campaign}

사용자의 나머지 SMS 메시지를 Zendesk로 전달하는 웹훅 Campaign을 설정합니다:

Zendesk는 티켓 ID를 문자열로 전송하므로, 문자열을 정수로 변환하는 콘텐츠 블록을 생성하여 Zendesk의 웹훅에서 사용할 수 있도록 합니다.

{% raw %}
```liquid
{% assign var = {{custom_attribute.${zendesk_ticket}}} | to_i %}{{var}}
```
{% endraw %}

웹훅 작성기에서:
- 웹훅 URL: {% raw %}https://{{url}}.zendesk.com/api/v2/tickets/{{content_blocks.${to_int}}}.json{% endraw %}
- 요청: PUT
- KVP:
    - Content-Type:application/JSON
    - Authorization: Basic {{Token}}

샘플 본문:

{% raw %}
```liquid
{
  "ticket": {
    "comment": {
      "body": "Inbound message from {{${first_name}}} {{${last_name}}}: {{sms.${inbound_message_body}}}"
    }
}
}
```
{% endraw %}

#### 6.5단계: 두 번째 웹훅 Campaign 설정 완료하기 {#step-65-complete-second-webhook-campaign-setup}
- "Other" 카테고리에서 인바운드 메시지를 보내는 사용자에 대한 실행 기반 트리거를 설정합니다.
- 재자격 기준을 설정합니다.
- 적용 가능한 오디언스를 추가합니다(이 경우, 커스텀 속성 **zendesk_ticket_open**이 **true**인 경우).

[2]: {% image_buster /assets/img/zendesk/instant_chat/chat2.png %}