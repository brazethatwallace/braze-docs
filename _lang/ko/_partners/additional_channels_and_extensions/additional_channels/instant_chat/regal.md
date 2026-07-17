---
nav_title: Regal
article_title: Regal
description: "이 참조 문서에서는 Braze와 Regal의 파트너십에 대해 설명합니다. Regal은 Voice AI 에이전트 플랫폼으로, Braze 데이터와 Regal 대화를 활용하여 개인화된 옴니채널 고객 여정을 오케스트레이션할 수 있습니다."
alias: /partners/regal/
page_type: partner
search_tag: Partner

---

# Regal

> [Regal.io](https://regal.io)는 기업이 채널 전반에서 지능적이고 실시간 대화를 통해 더 나은 고객 경험을 제공할 수 있도록 돕는 Voice AI 에이전트 플랫폼입니다.

_이 통합은 Regal에서 유지 관리합니다._

Regal과 Braze를 통합하면 행동 데이터와 대화형 인공지능을 통합하여 개인화된 옴니채널 고객 여정을 오케스트레이션할 수 있습니다. Braze는 고객 생애주기 전반에서 신호를 캡처하고, Regal은 이를 활용하여 AI 에이전트 대화, 라우팅 및 실시간 의사결정을 수행합니다.

Braze 데이터를 사용하여 AI 에이전트가 무엇을 말하고, 어떻게 응답하며, 언제 참여할지를 결정합니다. 대화 결과와 인사이트를 Braze로 다시 전송하여 타겟팅과 생애주기 마케팅을 개선합니다. 고객 여정의 핵심 순간에 AI 기반 전화와 SMS를 트리거하고, 각 대화에서 발생한 내용을 기반으로 Braze에서 후속 조치를 수행합니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Regal 계정 | 이 파트너십을 활용하려면 Regal 계정이 필요합니다. |
| Regal API 키 | Regal API 키를 사용하면 Braze에서 Regal로 이벤트를 전송할 수 있습니다.<br><br>이 키를 받으려면 [support@regal.io](mailto:support@regal.io)로 이메일을 보내세요. |
| Braze 데이터 변환 | Regal에서 데이터를 수신하려면 [데이터 변환]({{site.baseurl}}/data_transformation)이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 통합: Braze에서 Regal로 데이터 전송 {#integration-sending-data-from-braze-to-regal}

Braze Canvas 또는 Campaign 웹훅을 사용하여 고객 프로필 및 이벤트 데이터를 Braze에서 Regal로 전송합니다.

### 1단계: Regal에서 새 연락처 생성 {#step-1-create-new-contacts-in-regal}

Regal에서 전화 및 문자를 사용할 수 있도록, 새 Braze 프로필이 생성될 때마다 Regal로 웹훅을 전송하는 Canvas 또는 Campaign을 생성합니다.

1. "Create New Contact for Regal"이라는 제목의 Canvas 또는 Campaign을 생성하고 진입 유형으로 **액션 기반**을 선택합니다.

2. 트리거 로직을 **커스텀 이벤트**로 설정하고 전화번호가 있는 프로필이 생성될 때 발생하는 이벤트를 선택합니다. Regal에서는 전화번호 필드가 설정되어 있는지 확인하는 추가 필터를 추가하는 것도 권장합니다.

3. 새 웹훅 템플릿에서 다음 필드를 입력합니다:
   - **웹훅 URL**: <https://events.regalvoice.com/events>
   - **요청 본문**: Raw Text

#### 요청 헤더 및 메서드 {#request-headers-and-method}

Regal에는 인증을 위한 HTTP 헤더와 HTTP 메서드도 필요합니다. 다음 항목은 **설정** 탭에서 키-값 페어로 이미 템플릿에 포함되어 있습니다:
{% raw %}
- **HTTP 메서드**: POST
- **요청 헤더**:
    - **Authorization**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### 요청 본문 {#request-body}

유일한 필수 식별자는 `traits.phones` 내의 전화번호입니다. `traits.phones` 오브젝트를 사용하여 하나 이상의 전화번호를 연락처에 연결합니다. 각 전화번호에는 고유한 레이블, 기본 지정, 음성 및 SMS 옵트인 상태를 저장할 수 있습니다. 이 구조는 연락처에 여러 전화번호가 있을 때 특히 유용합니다.

```json
{
  "userId": "<uniqueIdentifier>",
  "traits": {
    "phones": {
      "<primaryPhoneNumber>": {
        "label": "Mobile",
        "isPrimary": true,
        "voiceOptIn": {
          "subscribed": true,
          "ip": "<ipAddress>",
          "source": "<leadSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": true,
          "ip": "<ipAddress>",
          "source": "<leadSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      },
      "<secondaryPhoneNumber>": {
        "label": "Home",
        "isPrimary": false,
        "voiceOptIn": {
          "subscribed": false,
          "ip": "<ipAddress>",
          "source": "<leadSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": false,
          "ip": "<ipAddress>",
          "source": "<leadSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      }
    },
    "email": "<email>",
    "firstName": "<firstName>",
    "lastName": "<lastName>",
    "custom1": "<custom1>",
    "custom2": "<custom2>"
  },
  "eventSource": "braze"
}
```

위의 페이로드 예시는 나열된 전화번호에 현재 음성 및 SMS 동의 상태가 포함되어 있다고 가정합니다. 그렇지 않은 경우 연락처를 생성할 때 `voiceOptIn`과 `smsOptIn`을 생략하고, 옵트인이 수집될 때 해당 전화번호의 동의를 업데이트하는 별도의 Canvas 또는 Campaign을 설정할 수 있습니다.

### 2단계: 옵트인 정보 업데이트 {#step-2-update-opt-in-information}

앱에서 다양한 시점에 옵트인 및 옵트아웃이 발생할 수 있으므로, 사용자가 구독 상태를 변경할 때 Regal을 업데이트합니다.

Regal에서는 연락처 수준이 아닌 전화번호별로 옵트인 및 옵트아웃을 관리할 수 있도록 `traits.phones` 스키마를 사용하는 것을 권장합니다.

다음 Canvas 설정을 사용하여 최신 옵트인 정보를 Regal로 전송합니다.

1. "Send Opt In or Out to Regal"이라는 제목의 새 Canvas 또는 Campaign을 생성합니다.

2. 다음 트리거 옵션 중 하나를 선택하고 사용자의 옵트인 상태를 나타내는 필드를 선택합니다:
    - **User Profile Field Updated**
    - **Update Subscription Group Status**
    - **Subscription Status**

3. 새 웹훅 템플릿에서 다음 필드를 입력합니다:
   - **웹훅 URL**: <https://events.regalvoice.com/events>
   - **요청 본문**: Raw Text

#### 요청 헤더 및 메서드

Regal에는 인증을 위한 HTTP 헤더와 HTTP 메서드도 필요합니다. 다음 항목은 **설정** 탭에서 키-값 페어로 이미 템플릿에 포함되어 있습니다:
{% raw %}
- **HTTP 메서드**: POST
- **요청 헤더**:
    - **Authorization**: `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### 요청 본문

```json
{
  "userId": "<uniqueIdentifier>",
  "traits": {
    "phones": {
      "<phoneNumber>": {
        "voiceOptIn": {
          "subscribed": "<voice_optin_subscribed>",
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": "<sms_optin_subscribed>",
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      }
    }
  },
  "eventSource": "braze"
}
```

이 페이로드에 추가 사용자 프로필 속성을 포함하여 다른 속성도 동시에 최신 상태로 유지할 수 있습니다.

### 3단계: 커스텀 이벤트 전송 {#step-3-send-custom-events}

Regal로 전송하려는 각 주요 이벤트에 대해 Canvas 또는 Campaign을 설정합니다.

이러한 이벤트는 단순히 아웃리치를 트리거하는 것 이상의 역할을 합니다(예: 리드가 가입을 완료했을 때 확인 문자 전송). 이벤트는 Regal AI 에이전트가 고객 여정 전반에서 대화하고, 의사결정을 내리고, 대화를 라우팅하는 방식을 결정하는 실시간 컨텍스트를 제공합니다. Braze에서 이벤트 데이터와 속성을 전송하면 AI 에이전트가 각 사용자의 행동, 선호도 및 생애주기 단계에 따라 대화를 조정할 수 있습니다.

예를 들어, Braze 이벤트와 속성은 Regal에서 다음과 같이 사용할 수 있습니다:

- **AI 에이전트 대화 개인화**: 최근 행동이나 제품 관심사를 대화에서 직접 참조합니다.
  - 예: 사용자가 생명보험 옵션을 탐색한 경우, 에이전트가 대화에서 `contact.firstName`과 `contact.brazeProductInterest`를 참조할 수 있습니다.
- **동적 대화 로직 구동**: 에이전트가 실시간으로 우선순위를 조정합니다.
  - 예: `contact.brazeAge`가 65세 이상이면 Medicare 보장을 우선시하고, 그렇지 않으면 ACA 플랜과 현재 보험 상태에 집중합니다.
- **지능형 라우팅 및 에스컬레이션 활성화**: 가치 또는 의도에 따라 대화를 라우팅합니다.
  - 예: `contact.brazeLeadTier`가 "High Value"이면 자격 확인 후 시니어 에이전트에게 전환하고, 그렇지 않으면 AI 에이전트가 계속 진행합니다.
- **메시징 및 오퍼 정렬**: Campaign 컨텍스트에 따라 에이전트가 제시하는 내용을 맞춤화합니다.
  - 예: `contact.brazeCampaignName`이 "Spring Mortgage Promo"이면 대화 중 프로모션 오퍼를 강조합니다.

"Send Product Interest Event to Regal"이라는 제목의 새 Canvas 또는 Campaign을 생성합니다.

```json
{
  "userId": "<uniqueIdentifier>",
  "traits": {
    "phones": {
      "<primaryPhoneNumber>": {
        "label": "Mobile",
        "isPrimary": true,
        "voiceOptIn": {
          "subscribed": true,
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": true,
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      },
      "<secondaryPhoneNumber>": {
        "label": "Home",
        "isPrimary": false,
        "voiceOptIn": {
          "subscribed": false,
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<voiceOptInText>",
          "timestamp": "<timestamp>"
        },
        "smsOptIn": {
          "subscribed": false,
          "ip": "<ipAddress>",
          "source": "<optInSource>",
          "text": "<smsOptInText>",
          "timestamp": "<timestamp>"
        }
      }
    },
    "email": "<email>",
    "firstName": "<firstName>",
    "lastName": "<lastName>",
    "brazeProductInterest": "Life Insurance",
    "brazeAge": 68,
    "brazeLeadTier": "High Value",
    "brazeCampaignName": "Spring Insurance Promo"
  },
  "name": "Product Interest Captured",
  "properties": {
    "action": "Viewed Product Comparison",
    "productCategory": "Life Insurance",
    "intentScore": "High",
    "lastPage": "Compare Life Insurance Plans",
    "readyToCommit": true
  },
  "eventSource": "braze"
}
```

#### 최신 연락처 속성 {#up-to-date-contact-attributes}

Regal에서는 주요 이벤트가 발생하는 시점에 최신 연락처 속성에 접근할 수 있도록 이벤트 페이로드에 주요 사용자 프로필 속성도 함께 전송하는 것을 권장합니다.

{% alert note %}
Regal로 전송해야 할 이벤트나 이러한 Canvases 및 Campaigns를 설정하는 방법에 대해 궁금한 점이 있으면 [support@regal.io](mailto:support@regal.io)로 이메일을 보내세요.
{% endalert %}

## 통합: Regal에서 Braze로 데이터 전송 {#integration-sending-data-from-regal-to-braze}

Regal 리포팅 웹훅과 Braze 데이터 변환을 사용하여 Regal 리포팅 이벤트(예: `SMS.sent` 및 `call.completed`)를 Braze로 전송합니다. 이러한 이벤트를 매핑하면 사용자 프로필에 표시되며 세분화, Canvas 및 Campaigns에서 사용할 수 있습니다.

### 1단계: Braze에서 데이터 변환 생성 {#step-1-create-a-data-transformation-in-braze}

Braze로 전송할 각 Regal 웹훅에 대해 하나의 데이터 변환을 생성합니다.

데이터 변환을 생성하려면:
1. Braze 대시보드에서 **Transformations** 페이지로 이동합니다.
2. 변환에 이름을 지정하고 **Create transformation**을 클릭합니다.
3. 변환 목록에서 <i class="fa-solid fa-ellipsis-vertical" title="작업 보기"></i> **View actions**를 선택하고 **Copy webhook URL**을 선택합니다.

### 2단계: Regal에서 리포팅 웹훅 활성화 {#step-2-enable-reporting-webhooks-in-regal}

리포팅 웹훅을 설정하려면:
1. Regal 앱으로 이동하여 **Settings** 페이지를 엽니다.

2. **Reporting Webhooks** 섹션에서 **Create Webhooks**를 클릭합니다.

3. 웹훅 엔드포인트 입력란에 해당 데이터 변환에 대한 Braze 데이터 변환 웹훅 URL을 추가합니다.

#### 엔드포인트 업데이트 {#updating-an-endpoint}

엔드포인트를 편집하면 캐시가 새로고침되어 새 엔드포인트로 이벤트를 전송하기까지 최대 5분이 소요될 수 있습니다.

#### 재시도 {#retries}

현재 Regal은 이러한 이벤트에 대해 재시도를 수행하지 않습니다. Braze가 5초 이내에 응답하지 않으면 Regal은 해당 이벤트를 삭제합니다. Regal은 향후 릴리스에서 재시도 기능을 추가할 예정입니다.

#### 이벤트 {#events}
리포팅 이벤트의 전체 목록, 속성 정의 및 샘플 페이로드는 Regal의 [리포팅 웹훅 가이드](https://developer.regal.io/docs/reporting-webhooks#events)를 참조하세요.

### 3단계: Regal 이벤트를 Braze 이벤트로 변환 {#step-3-transform-regal-events-into-braze-events}

Braze [데이터 변환]({{site.baseurl}}/data_transformation) 기능을 사용하면 수신되는 Regal 이벤트를 Braze에서 속성, 이벤트 또는 구매로 추가하는 데 필요한 형식으로 매핑할 수 있습니다.

1. 데이터 변환에 이름을 지정합니다. 이벤트 웹훅별로 데이터 변환을 설정하는 것이 권장됩니다.

2. 연결을 테스트하려면 Regal Agent Desktop에서 휴대폰으로 아웃바운드 전화를 걸고 대화 요약 양식을 제출하여 `call.completed` 이벤트를 생성합니다.

3. Regal 연락처를 Braze 프로필에 매핑하는 데 사용할 식별자를 결정합니다. Regal 이벤트에서 사용 가능한 식별자는 다음과 같습니다:
   - `userId` - 이전에 연락처에 대해 이 식별자를 전송한 경우에만 이벤트에 설정됩니다
   - `traits.phone`
   - `traits.email` - 이전에 연락처에 대해 이 식별자를 전송한 경우에만 이벤트에 설정됩니다

Braze에서 Regal로 전송하는 이벤트 페이로드에서 Regal은 여러 전화번호와 전화번호별 동의를 지원하기 위해 `traits.phones`를 사용하는 것을 권장합니다. Regal에서 Braze로 다시 전송되는 리포팅 이벤트에서는 `traits.phone`이 이벤트 페이로드의 식별자로 여전히 나타날 수 있습니다.

#### Braze 지원 식별자 {#braze-supported-identifiers}
- Braze는 전화번호를 식별자로 지원하지 않습니다. 이를 식별자로 사용하려면 전화번호를 Braze에서 [사용자 별칭]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases)으로 설정할 수 있습니다.
- Braze 데이터 변환을 사용할 때 이메일 주소를 식별자로 사용할 수 있습니다. 이메일 주소가 Braze 내에 프로필로 존재하는 경우 기존 프로필이 업데이트됩니다. 이메일 주소가 Braze 내에 아직 존재하지 않는 경우 이메일 전용 프로필이 생성됩니다.

## 사용 사례 {#use-cases}

{% tabs %}
{% tab 이메일 트리거 %}

**Regal의 통화 처리 결과를 기반으로 Braze에서 이메일 트리거**

아래는 Regal의 `call.completed` 이벤트에 대한 샘플 페이로드입니다.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+15555550123",
    "email": "xxx@example.com"
  },
  "name": "call.completed",
  "properties": {
    "agent_firstname": "Alex",
    "agent_fullname": "Alex Lee",
    "agent_id": "xxxx@example.com",
    "direction": "OUTBOUND",
    "regal_voice_phone": "+15555550200",
    "regal_voice_phone_internal_name": "Sales Line",
    "contact_phone": "+15555550123",
    "call_id": "WTxxxxx9",
    "type": "Outbound Call",
    "disposition": "Converted During Convo",
    "notes": null,
    "objections": null,
    "campaign_name": "Life Insurance Quote Follow Up",
    "campaign_friendly_id": "445",
    "started_at": 1657855046,
    "ended_at": 1657855053,
    "completed_at": 1657855059,
    "talk_time": 7,
    "wrapup_time": 6,
    "handle_time": 13,
    "journey_uuid": null,
    "journey_name": null,
    "journey_friendly_id": null
  },
  "originalTimestamp": "1657855059",
  "eventSource": "Regal Voice"
}
```

아래는 이를 Braze의 커스텀 이벤트로 매핑하는 샘플 데이터 변환입니다.

```
// The Braze /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is a default template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "name": "Call Completed",
     "time": isoString,
     "_update_existing_only": false,
     "properties": {
       "agent_firstname": payload.properties.agent_firstname,
       "agent_fullname": payload.properties.agent_fullname,
       "agent_id": payload.properties.agent_id,
       "direction": payload.properties.direction,
       "regal_voice_phone": payload.properties.regal_voice_phone,
       "regal_voice_phone_internal_name": payload.properties.regal_voice_phone_internal_name,
       "contact_phone": payload.properties.contact_phone,
       "call_id": payload.properties.call_id,
       "type": payload.properties.type,
       "disposition": payload.properties.disposition,
       "notes": payload.properties.notes,
       "objections": payload.properties.objections,
       "campaign_name": payload.properties.campaign_name,
       "campaign_friendly_id": payload.properties.campaign_friendly_id,
       "started_at": payload.properties.started_at,
       "ended_at": payload.properties.ended_at,
       "completed_at": payload.properties.completed_at,
       "talk_time": payload.properties.talk_time,
       "wrapup_time": payload.properties.wrapup_time,
       "handle_time": payload.properties.handle_time,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_name": payload.properties.journey_name,
       "journey_friendly_id": payload.properties.journey_friendly_id
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab 프로필 속성 업데이트 %}

**Regal의 `contact.attribute.edited` 이벤트를 기반으로 Braze에서 프로필 속성 업데이트**

아래는 Regal의 `contact.attribute.edited` 이벤트에 대한 샘플 페이로드입니다. Regal은 상담원이 대화 중 연락처 프로필의 속성을 업데이트할 때 이 이벤트를 전송합니다.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+15555550123",
    "email": "xxx@example.com"
  },
  "name": "contact.attribute.edited",
  "properties": {
    "agent_email": "xxxx@example.com",
    "contact_phone": "+15555550123",
    "changes": {
      "custom_properties": {
        "annual_income": {
          "old_value": "150,000",
          "new_value": "300,000"
        }
      }
    },
    "created_at": "1657855462"
  },
  "originalTimestamp": "1657855462",
  "eventSource": "Regal Voice"
}
```

아래는 새 커스텀 속성 값을 Braze 프로필의 관련 속성에 매핑하는 샘플 데이터 변환입니다:

```
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// Capture the key's updated property value within the 'changes' object and store this in an attributes variable that can be used in the /users/track request

const changes = payload.properties.changes.custom_properties;

const attributes = {};
for (const key in changes) {
 attributes[key] = changes[key].new_value;
}

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

const brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     ...attributes
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab 실험 동기화 유지 %}

**`contact.experiment.assigned` 이벤트를 사용하여 Braze와 Regal의 실험을 동기화 상태로 유지**

아래는 Regal의 `contact.experiment.assigned` 이벤트에 대한 샘플 페이로드입니다.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+15555550123",
    "email": "xxx@example.com"
  },
  "name": "contact.experiment.assigned",
  "properties": {
    "experiment_name": "Post Call Offer Test",
    "experiment_id": "xxxx-xxxx-xxxx-xxxx",
    "experiment_variant": "Aggressive Offer - 50%",
    "journey_uuid": "xxxx-xxxx-xxxx-xxxx",
    "journey_friendly_id": 220,
    "journey_name": "Post Call Follow Up"
  },
  "originalTimestamp": "1657855118",
  "eventSource": "Regal Voice"
}
```

아래는 이를 Braze의 커스텀 이벤트로 매핑하는 샘플 데이터 변환입니다.

```
// The Braze /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze, it must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z
let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     "name": "Contact Experiment Assigned",
     "time": isoString,
     "properties": {
       "experiment_name": payload.properties.experiment_name,
       "experiment_id": payload.properties.experiment_id,
       "experiment_variant": payload.properties.experiment_variant,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_friendly_id": payload.properties.journey_friendly_id,
       "journey_name": payload.properties.journey_name
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;

```
{% endtab %}
{% tab 연락처 구독 취소 %}

**Regal의 `contact.unsubscribed` 이벤트를 기반으로 Braze에서 연락처 구독 취소**

아래는 Regal의 `contact.unsubscribed` 이벤트에 대한 샘플 페이로드입니다.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+15555550123",
    "email": "xxx@example.com",
    "ip": "78.97.213.166"
  },
  "name": "contact.unsubscribed",
  "properties": {
    "new_subscription": true,
    "channel": "voice",
    "text": null,
    "ip": "207.38.149.143",
    "source": "regalvoice.agent_desktop",
    "timestamp": "1657855229"
  },
  "originalTimestamp": "1657855230",
  "eventSource": "Regal Voice"
}
```

아래는 Braze에서 연락처를 구독 취소하는 샘플 데이터 변환입니다.

```
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": true,
     "subscription_groups" : [{
       "subscription_group_id": "YOUR SUBSCRIPTION GROUP ID",
       "subscription_state": "unsubscribed"
     }]
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab 통화 분석 기반 후속 조치 트리거 %}

**Regal의 `call.analysis.available` 이벤트를 기반으로 Braze에서 맞춤형 후속 여정 트리거**

Regal의 `call.analysis.available` 이벤트를 사용하여 고객이 전환하지 않은 주요 이유를 파악하고 Braze에서 맞춤형 후속 여정을 트리거합니다.

예를 들어:

- 주요 반대 이유가 가격인 경우, 가치 중심의 후속 이메일을 전송합니다.
- 주요 반대 이유가 타이밍인 경우, 나중에 재고려할 수 있도록 사용자를 너처 시퀀스에 배치합니다.
- 주요 반대 이유가 신뢰인 경우, 후기, 평점 또는 규정 준수 관련 안내를 전송합니다.
- `needs_human_agent`가 true인 경우, 영업 또는 고객지원 팀에 알리고 추가 자동화 메시징을 중단합니다.

아래는 Regal의 `call.analysis.available` 이벤트에 대한 샘플 페이로드입니다.

```json
{
  "traits": {
    "phone": "+1XXXXXXXXXX",
    "email": "xxx@example.com"
  },
  "name": "call.analysis.available",
  "brand": "circle-bank",
  "contact_email": "xxx@example.com",
  "contact_phone": "+1XXXXXXXXXX",
  "created_at": "1754079836",
  "entity_type": "event",
  "event_id": "9f5d8dbb2973b0e2359c6fd34111111",
  "event_type": "regal_voice_event",
  "external_id": "41dd1aa2-1111-f011-a2d5-00505611111",
  "original_timestamp": "1754079835",
  "profile_id": "62653af1111111173af128291e92",
  "properties": {
    "agent_email": "xxx@example.com",
    "call_analysis": {
      "purchase_intent": "medium",
      "primary_objection": "price",
      "secondary_objection": "needs_to_compare",
      "product_interest": "Life Insurance",
      "follow_up_required": true,
      "follow_up_email_text": "Thanks for speaking with us today. I know cost is top of mind, so I wanted to send over a simple summary of the life insurance options we discussed and what may fit your budget.",
      "recommended_next_action": "send_value_oriented_follow_up",
      "needs_human_agent": false,
      "customer_sentiment_label": "interested_but_hesitant"
    },
    "contact_phone": "+1XXXXXXXXXX",
    "incoming_sip_headers": {
      "Via": "SIP/2.0/UDP srv1.example.com;branch=z9hG4bK776asdhds",
      "From": "<sip:customer@example.com>;tag=1928301774",
      "Call-ID": "a84b4c76e66710"
    },
    "is_ai_agent": true,
    "outgoing_sip_headers": {
      "Via": "SIP/2.0/TCP srv2.example.com;branch=z9hG4bKgsdh7723",
      "To": "<sip:agent@example.com>",
      "User-Agent": "RegalVoiceAI/1.0"
    },
    "task_id": "WT7f3ea47fa6e6055aa847f0a62111111"
  },
  "originalTimestamp": "1754079835",
  "source": "Regal Voice"
}
```

데이터 변환을 사용하여 `call_analysis` 필드(예: `primary_objection` 및 `needs_human_agent`)를 Braze 커스텀 이벤트 또는 프로필 속성에 매핑합니다. 그런 다음 Braze에서 해당 값을 기반으로 분기하는 Canvas 또는 Campaign 로직을 구축합니다.

{% endtab %}
{% tab 통화 트랜스크립트 링크 저장 %}

**`call.transcript.available` 이벤트의 트랜스크립트 링크로 프로필 속성 업데이트**

`call.transcript.available` 이벤트를 사용하여 전체 통화 트랜스크립트 링크를 Braze로 전송합니다. 데이터 변환을 통해 트랜스크립트 URL을 Braze 사용자 프로필 속성에 매핑하면 팀이 사용자 프로필에서 대화를 확인하고 검토할 수 있습니다.

아래는 Regal의 `call.transcript.available` 이벤트에 대한 샘플 페이로드입니다.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+15555550123",
    "email": "xxx@example.com"
  },
  "name": "call.transcript.available",
  "properties": {
    "agent_email": "xxx@example.com",
    "task_id": "WT953358e8822dd9333fc38dfbac25e1e1",
    "call_summary": "The agent Yuri explained insurance options to Alex and he said he'll need to think about it before moving forward Agent politely ended the call.",
    "contact_name": "Alex Smith",
    "contact_phone": "+15555550123",
    "is_voicemail": false,
    "moments_count": 18,
    "recording_id": "RE0118052841b7299d0630d1dff610c1fb",
    "recording_link": "https://api.twilio.com/2010-04-01/Accounts/ACxxx/Recordings/xxx.mp3",
    "recording_duration": 78.75987,
    "request_timestamp": 1657799128,
    "response_timestamp": 1657799136,
    "sentiments": {
      "contact_sentiment": 70,
      "agent_sentiment": 75,
      "agent_sentiment_reason": "Yuri was polite and attentive, effectively gathering information and providing a resource, which contributed to a positive interaction.",
      "contact_sentiment_reason": "Alex was satisfied with the information provided but may have wanted more assistance regarding insurance options."
    },
    "trackers": [
      {
        "tracker_id": "4be87957-9140-4451-894a-bdbaed1f2460",
        "tracker_name": "Refinance"
      },
      {
        "tracker_id": "eb2577c6-5e23-4c65-9e04-5cc5d49eee7e",
        "tracker_name": "High Intent"
      }
    ],
    "transcript": "[handling agent]: Hi Alex, this is Yuri with BrightCover Insurance. I'll be going over some insurance options with you today. [contact]: Sounds good. [handling agent]: Before we start, I'm going to transfer you to a specialist for a moment. One sec. [transfer agent]: Hi Alex, this is Lee. Just verifying a few details before sending you back to Yuri. [contact]: Okay. [handling agent]: Thanks, Alex. Based on what you shared, here are some plan options... [contact]: I'll need to think about it. [handling agent]: Totally understandable. Feel free to reach out anytime. Have a great day! END OF TRANSCRIPT",
    "transcript_is_truncated": false,
    "transcript_url": "https://app.regalvoice.com/transcripts/WT953358e8822dd9333fc38dfbac25e1e1"
  },
  "originalTimestamp": "1657843308",
  "eventSource": "Regal Voice",
  "eventId": "f49a3cf9cb1336683bd5f19dwe4c61147"
}
```

{% endtab %}
{% endtabs %}