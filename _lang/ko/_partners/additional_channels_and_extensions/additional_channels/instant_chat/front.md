---
nav_title: Front
article_title: Front
description: "Front를 Braze와 통합하는 방법을 알아보세요"
alias: /partners/front/
page_type: partner
search_tag: Partner

---

# Front

> Front의 통합을 통해 Braze 데이터 변환과 각 플랫폼의 웹훅을 활용하여 양방향 대화형 SMS 파이프라인을 설정할 수 있습니다.

Front에서 수신되는 웹훅에는 라이브 상담원이 보낸 메시지가 포함된 페이로드가 담겨 있습니다. 이 요청은 Braze 엔드포인트에서 수락되기 전에 형식을 변환해야 합니다. Front 데이터 변환 템플릿은 페이로드를 재형식화하고 고객 프로필에 **Outbound SMS Sent**라는 커스텀 이벤트를 기록하며, 메시지 본문은 이벤트 속성정보로 전달됩니다.

Braze에서 새 변환을 설정하기 전에 [데이터 변환]({{site.baseurl}}/user_guide/data/unification/data_transformation/) 설명서에서 각 티어의 지원 매트릭스를 검토하는 것을 권장합니다. Free 및 Pro 티어는 월별 활성 변환 수와 수신 요청 수가 다릅니다. 현재 사용 중인 플랜이 사용 사례를 지원할 수 있는지 확인하세요.

## 필수 조건 {#prerequisites}

시작하기 전에 다음이 필요합니다:

| 요구 사항 | 설명 |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Front 계정 | 이 파트너십을 활용하려면 Front 계정이 필요합니다.|
| Braze 데이터 변환 웹훅 URL | [Braze 데이터 변환]({{site.baseurl}}/user_guide/data/unification/data_transformation/)은 Front에서 수신되는 웹훅을 Braze /users/track 엔드포인트에서 수락할 수 있도록 재형식화하는 데 사용됩니다.|
| Front REST API 키 | Front REST API 키는 Braze에서 Front로 아웃바운드 웹훅 요청을 보내는 데 사용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 활용 사례 {#use-cases}

- Braze 자동 SMS 메시징을 사용하여 사용자 선호도를 파악하고 라이브 영업 상담원이 후속 조치를 취하고 판매를 완료할 수 있도록 하여 리드 생성 프로세스를 간소화합니다.
- 자동 SMS 응답과 라이브 채팅 지원을 통해 판매 전환을 유도하여 장바구니를 포기한 고객을 다시 참여시킵니다.

## Front 통합하기 {#integrating-front}

### 1단계: 데이터 변환 생성 {#step-1-create-a-data-transformation}

먼저 Braze에서 새 데이터 변환을 생성합니다. 다음 단계는 간략화된 것입니다. 전체 안내는 [변환 생성하기]({{site.baseurl}}/user_guide/data/unification/data_transformation/creating_a_transformation/)를 참조하세요.

1. Braze에서 **데이터 설정** > **데이터 변환**으로 이동한 다음 **변환 생성**을 선택합니다.
2. **편집 환경**에서 **처음부터 시작**을 선택합니다.
3. **대상 선택**에서 **POST: Track Users**를 선택합니다.
4. 다음 변환 템플릿을 복사하여 붙여넣은 다음 엔드포인트를 저장하고 활성화합니다.
    {% raw %}
    ```liquid

    // This is a default template that you can use as a starting point. Feel free to delete this entirely to start from
    // scratch, or to delete specific components as you see fit

    // First, this code defines a variable, "brazecall", to build up a /users/track request
    // Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in
    // desired values in your /users/track request with JS dot notation, such as payload.x.y.z

    let brazecall = {
    "events": [
      {
      "phone": payload.recipients[1].handle,
      "_update_existing_only": true,
      "name": "Outbound SMS Sent",
      "time": new Date().toISOString(),
      "properties": {
        "message_id": payload.id,
        "message_body": payload.body,
        "front_author_username": payload.author.username
      }
      }
    ]
    };

    // After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
    return brazecall;
    ```
    {% endraw %}

    변환은 위의 JavaScript 예시를 따르되, 속성 이름과 경로를 Front 웹훅 페이로드에 맞게 조정하세요.

{% alert tip %}
이 템플릿을 특정 요구 사항에 맞게 수정할 수 있습니다. 예를 들어, 사전 설정된 커스텀 이벤트 이름을 커스터마이즈할 수 있습니다. 자세한 내용은 [데이터 변환 개요]({{site.baseurl}}/user_guide/data/unification/data_transformation/)를 참조하세요.
{% endalert %}

### 2단계: 아웃바운드 SMS Campaign 생성 {#step-2-create-an-outbound-sms-campaign}

다음으로, Front에서 웹훅을 수신하고 고객에게 커스텀 SMS 응답을 보내는 SMS Campaign을 생성합니다.

#### 2.1단계: 메시지 작성 {#step-21-compose-your-message}

**메시지** 텍스트 상자에 다음 Liquid 코드와 함께 수신 거부 문구 또는 기타 정적 콘텐츠를 추가합니다.

{% raw %}
```liquid
{{event_properties.${message_body}}}
```
{% endraw %}

메시지는 다음과 유사해야 합니다:

![Liquid 코드를 사용하는 메시지 예시.]({% image_buster /assets/img/front/sms_to_braze.png %}){: style="max-width:80%;"}

#### 2.2 전달 스케줄 설정 {#22-schedule-the-delivery}

전달 유형으로 **실행 기반 전달**을 선택한 다음, 커스텀 이벤트 트리거로 **Outbound SMS Sent**를 선택합니다.

!["전달 스케줄" 페이지.]({% image_buster /assets/img/front/custom_event_trigger.png %})

{% alert note %}
이 커스텀 이벤트는 사용자 프로필에 기록하는 데이터 변환입니다. 상담원 메시지는 이 이벤트의 이벤트 속성정보로 저장됩니다.
{% endalert %}

마지막으로, **전달 제어**에서 재자격을 활성화합니다.

!["전달 제어"에서 재자격이 활성화됨.]({% image_buster /assets/img/front/braze_reeligibility.png %})

### 3단계: 커스텀 채널 생성 {#step-3-create-a-custom-channel}

Front 대시보드에서 **Settings** > **Channels** > **Add Channels**로 이동한 다음 **Custom Channel**을 선택하고 새 Braze 채널의 이름을 입력합니다.

![Front 대시보드에서 Braze를 위한 커스텀 채널.]({% image_buster /assets/img/front/front_custom_channel.png %})

### 4단계: 설정 구성 {#step-4-configure-the-settings}

아웃바운드 API 엔드포인트 필드에 [이전에 생성한](#step-1-set-up-a-data-transformation-in-braze) 데이터 변환 웹훅 URL을 입력합니다. 새 Braze 채널의 라이브 상담원이 보내는 모든 아웃바운드 메시지가 여기로 전송됩니다. 이 채널은 또한 Braze가 SMS 메시지를 전달할 수 있는 엔드포인트 URL을 **Incoming URL** 필드에 제공합니다.

이 URL을 반드시 메모해 두세요&#8212;나중에 필요합니다.

![Front에서 새로 생성된 Braze 채널의 채널 설정.]({% image_buster /assets/img/front/front_custom_channel2.png %}){: style="max-width:65%;"}

### 5단계: 인바운드 SMS 전달 설정 {#step-5-set-up-inbound-sms-forwarding}

다음으로, Braze에서 두 개의 새 웹훅 Campaign을 생성하여 고객의 인바운드 SMS를 Front 받은편지함으로 전달할 수 있도록 합니다.

| 번호 | 목적 |
|---|---|
| 웹훅 Campaign 1 | Front에 라이브 채팅 대화가 요청되고 있음을 알립니다. |
| 웹훅 Campaign 2 | 고객이 인바운드로 보낸 모든 대화형 SMS 응답을 Front 받은편지함으로 전달합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="5단계: 인바운드 SMS 전달 설정" }

#### 5.1단계: SMS 키워드 카테고리 생성 {#step-51-create-an-sms-keyword-category}

Braze 대시보드에서 **오디언스**로 이동하여 **SMS 구독 그룹**을 선택한 다음 **커스텀 키워드 추가**를 선택합니다. Front 전용 SMS 키워드 카테고리를 생성하려면 다음 필드를 작성합니다.

| 필드 | 설명 |
|---|---|
| 키워드 카테고리 | 키워드 카테고리의 이름(예: `FrontSMS1`). |
| 키워드 | 커스텀 키워드(예: `TIMETOMOW`). 실수로 트리거되는 것을 방지하기 위해 일반적인 단어는 피하세요. 키워드는 대소문자를 구분하지 않으므로 `lawn`은 `LAWN`과 일치합니다. |
| 응답 메시지 | 키워드가 감지될 때 전송될 메시지(예: "조경사가 곧 연락드릴 것입니다."). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="5.1단계: SMS 키워드 카테고리 생성" }

![Braze의 SMS 키워드 카테고리 예시.]({% image_buster /assets/img/front/front_keyword.png %}){: style="max-width:65%;"}

#### 5.2단계: 첫 번째 웹훅 Campaign 생성 {#step-52-create-your-first-webhook-campaign}

Braze 대시보드에서 [이전에 생성한](#step-3-configure-the-settings-for-your-new-custom-braze-channel) URL을 사용하여 첫 번째 웹훅 Campaign을 생성합니다.

![Braze에서 생성해야 할 첫 번째 웹훅 Campaign 예시.]({% image_buster /assets/img/front/sms_to_front.png %}){: style="max-width:65%;"}

요청 본문에 다음을 추가합니다:

{% raw %}
```liquid
{
 "sender": {
  "handle": "{{${phone_number}}}",
  "name": "{{${user_id}}}"
 },
 "body_format": "markdown",
 "metadata": {
  "headers": {
   "first_name": "{{${first_name}}}",
   "last_name": "{{${last_name}}}"
  }
 },
 "body": "{{sms.${inbound_message_body} | default : "no body available" }}"
}
```
{% endraw %}

설정 탭에서 `Authorization`, `content-type`, `accept` 요청 헤더를 구성합니다.

![세 개의 필수 헤더가 포함된 요청 예시.]({% image_buster /assets/img/front/webhook_settings.png %}){: style="max-width:65%;"}

#### 5.3단계: 첫 번째 전달 스케줄 설정 {#step-53-schedule-the-first-delivery}

**전달 스케줄**에서 **실행 기반 전달**을 선택한 다음 트리거 유형으로 **SMS 인바운드 메시지 전송**을 선택합니다. 또한 [이전에 설정한](#step-51-create-an-sms-keyword-category) SMS 구독 그룹과 키워드 카테고리를 추가합니다.

![첫 번째 웹훅 Campaign의 "전달 스케줄" 페이지.]({% image_buster /assets/img/front/front_actionbased_keyword.png %})

**전달 제어**에서 재자격을 활성화합니다.

![첫 번째 웹훅 Campaign의 "전달 제어"에서 재자격이 선택됨.]({% image_buster /assets/img/front/braze_reeligibility.png %})

#### 5.4단계: 두 번째 웹훅 Campaign 생성 {#step-54-create-your-second-webhook-campaign}

두 번째 웹훅 Campaign은 첫 번째와 동일하므로 [첫 번째 Campaign을 복제하고 이름을 변경할 수 있습니다]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns/#duplicating-segments-or-campaigns).

#### 5.5단계: 두 번째 전달 스케줄 설정 {#step-55-schedule-the-second-delivery}

**전달 스케줄**에서 **실행 기반 트리거**와 **SMS 구독 그룹**을 [첫 번째 전달](#step-53-schedule-the-first-delivery)과 동일하게 설정합니다. 단, **키워드 카테고리**는 **Other**를 선택합니다.

![두 번째 웹훅 Campaign의 "전달 스케줄" 페이지, 키워드 카테고리로 "Other"가 선택됨.]({% image_buster /assets/img/front/front_actionbased_other_keyword.png %})

#### 5.6단계: 오디언스 필터 추가 {#step-56-add-an-audience-filter}

이제 웹훅 Campaign이 고객의 인바운드 SMS 응답을 전달할 수 있습니다. 라이브 채팅용 메시지만 전달되도록 SMS 응답을 필터링하려면 **타겟 오디언스 단계**에 **Last Received Message From Specific Campaign** 세분화 필터를 추가합니다.

!["Last Received Message From Specific Campaign"이 선택된 오디언스 필터.]({% image_buster /assets/img/front/front_segment_last_received_message.png %}){: style="max-width:65%;"}

그런 다음 필터를 구성합니다:

1. **Campaign**에서 [이전에 생성한](#step-2-create-an-outbound-sms-campaign) SMS Campaign을 선택합니다.
2. **Operator**에서 **Less Than**을 선택합니다.
3. **기간**에서 고객의 응답 없이 채팅이 열려 있어야 하는 시간을 선택합니다.

![선택된 오디언스 필터의 구성 설정.]({% image_buster /assets/img/front/front_target_audience.png %})

## 고려 사항 {#considerations}

### 청구 가능한 메시지 세그먼트 {#billable-segments}

- Braze의 SMS 메시지는 메시지 세그먼트 단위로 요금이 부과됩니다. 세그먼트를 정의하는 기준과 메시지가 어떻게 분할되는지 이해하는 것이 메시지 요금 청구 방식을 이해하는 핵심입니다. 자세한 내용은 [설명서]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator/)를 참조하세요.
- 긴 상담원 응답은 더 많은 청구 가능한 세그먼트를 소비합니다.

### 데이터 포인트 기록 {#logging-data-points}

현재 이 통합은 라이브 상담원이 Front에서 SMS를 보낼 때마다 고객 프로필에 커스텀 이벤트를 기록해야 합니다. 이는 몇 개의 메시지만 주고받는 빠른 교환에는 적합할 수 있지만, 대화가 길어질수록 데이터 포인트에 미치는 영향도 커집니다. Braze 데이터 포인트의 세부 사항에 대한 질문이 있으시면 Braze 계정 매니저에게 문의하세요.

### SMS 메시지에 링크 포함 {#including-links-in-sms-messages}

Front 라이브 채팅에서 링크를 보내면 추가 HTML 태그와 함께 렌더링됩니다.

### Front에서 이미지 파일 첨부 {#attaching-image-file-from-front}

Front의 이미지 파일은 Braze에서 보낸 SMS 메시지에서 렌더링되지 않습니다.

### 수신 거부 {#opt-outs}

대화형 메시지는 "stop"이라는 단어 또는 퍼지 수신 거부로 인식될 수 있는 유사한 표현이 포함될 위험이 더 높습니다.