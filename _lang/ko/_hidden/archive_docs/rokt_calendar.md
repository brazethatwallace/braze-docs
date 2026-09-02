---
nav_title: Rokt Calendar
article_title: Rokt Calendar
description: "이 참조 문서에서는 브랜드가 캘린더 이벤트 및 알림 형태로 1:1 이벤트와 프로모션 커뮤니케이션을 푸시할 수 있게 해주는 동적 캘린더 마케팅 기술인 Rokt Calendar와 Braze 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner
noindex: true
hidden: true
---

# Rokt Calendar

> [Rokt Calendar](https://www.rokt.com/rokt-calendar/)는 브랜드가 캘린더 이벤트 및 알림 형태로 1:1 이벤트와 프로모션 커뮤니케이션을 푸시할 수 있게 해주는 동적 캘린더 마케팅 기술입니다.

_이 통합은 Rokt Calendar에서 유지 관리합니다._

## 통합 정보 {#about-the-integration}

Braze와 Rokt Calendar 통합을 사용하면 Rokt Calendar 가입자와 해당 데이터를 Braze 웹훅을 통해 Braze로 푸시할 수 있습니다. 그런 다음 이 데이터를 Braze Canvases에서 여정 타겟팅 및 오디언스 세분화에 사용할 수 있으며, 다음 커스텀 [Rokt Calendar 속성](#audience-segmentation) 중 하나를 활용할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항  | 설명 |
| ------------ | ----------- |
| Rokt Calendar 계정 | 이 파트너십을 활용하려면 클라이언트별 Rokt Calendar 계정이 필요합니다. 계정 매니저와 상담하려면 [sales-calendar@rokt.com](mailto:sales-calendar@rokt.com)으로 문의하세요.  |
| Rokt Calendar 설정 | Rokt Calendar 계정 매니저가 다음과 같은 설정을 포함하여 귀하의 요구에 가장 적합하도록 캘린더를 설정하는 데 도움을 드립니다:<br>- 병합 플래그<br>- SubscriberID 대체 플래그<br>- 필요한 경우 이메일 캡처 |
| Rokt Calendar OAuth 자격 증명 | Rokt Calendar 계정 매니저가 제공하는 이 키를 사용하면 Braze와 Rokt Calendar 계정을 연결할 수 있습니다.<br><br>Braze 대시보드에서 **설정** > **연결된 콘텐츠**에서 생성할 수 있습니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. 이 키를 Rokt Calendar 계정 매니저에게 제공해야 합니다.<br><br>Braze 대시보드의 **설정** > **API 키**에서 생성할 수 있습니다. |
| [Braze REST 엔드포인트]({{site.baseurl}}/api/basics/#endpoints) | REST 엔드포인트 URL. 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
| 외부 가입자 ID | Rokt Calendar 구독 프로세스에서 캘린더 가입자를 Braze 사용자와 매칭하는 데 사용되는 식별자입니다. 이것은 Rokt Calendar에 전달하는 값입니다.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 오디언스 세분화 {#audience-segmentation}

Rokt Calendar가 새 사용자를 생성하거나 기존 가입자를 Braze 사용자와 매칭하면, Rokt Calendar는 Braze 내에서 필터링할 수 있는 다음 커스텀 구독 속성을 전송합니다:

| 커스텀 속성  | 정의       | 예시          |
| ----------------  | ---------------- | ---------------- |
| `rokt:account_code` | Rokt Calendar 계정의 코드 | `brazetest/f5733866ade2` 및 `brazetest/ff10919f1078` |
| `rokt:account_id` | Rokt Calendar 계정의 ID | `d0ce4299-7d6c-4888-bfd8-c7e867a0fa6c/f5733866ade2` |
| `rokt:account_name` | Rokt Calendar 계정의 이름 | `Braze Test/f5733866ade2` |
| `rokt:calendar_code` | Rokt Calendar 캘린더의 코드 | `test-calendar-1/f5733866ade2` |
| `rokt:calendar_id` | Rokt Calendar 캘린더의 ID | `9a9007c7-f5a4-e811-b13c-06424c4f2724/f5733866ade2` |
| `rokt:calendar_title` | Rokt Calendar 캘린더의 제목 | `Test Calendar 1/f5733866ade2` |
| `rokt:country_code` | 생성된 구독과 관련된 국가 코드 | `AU/f5733866ade2` |
| `rokt:device_name` | 생성된 구독과 관련된 기기 유형 | `Desktop/f5733866ade2` |
| `rokt:geo_country` | 생성된 구독과 관련된 출신 국가 | `Australia/f5733866ade2` |
| `rokt:optIn1` | 사용자가 생성된 구독과 관련된 2개의 옵트인 중 첫 번째에 옵트인했는지 여부 | `True/f5733866ade2` |
| `rokt:optIn2` | 사용자가 생성된 구독과 관련된 2개의 옵트인 중 두 번째에 옵트인했는지 여부 | `True/f5733866ade2` |
| `rokt:source` | 생성된 구독의 소스 | `brazetest.Rokt Calendarapp.com/f5733866ade2` |
| `rokt:subscriber_email` | 구독 프로세스 중 사용자가 입력한 이메일 주소 | `test@email.com/f5733866ade2` |
| `rokt:subscription_id` | 생성된 구독과 관련된 고유 식별자 역할을 하는 구독 ID | `06423672-b6ba-4536-aa36-70788a7a0a36` |
| `rokt:subscription_method` | 생성된 구독과 관련된 구독 방법(webcal/Google) | `WebCal/f5733866ade2` |
| `rokt:tags` | 생성된 구독과 관련하여 사용된 캘린더 태그 | `Test Calendar 1/All Teams/f5733866ade2 and Test Calendar 1/TeamI//f5733866ade2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Audience segmentation #audience-segmentation" }

Rokt Calendar는 사용자가 Rokt 캘린더를 구독하는 즉시 `subscribe` 커스텀 이벤트를 트리거하며, 이는 Braze 세분화에서 사용하거나 Campaign 또는 Canvas 구성요소의 트리거로 사용할 수 있습니다.

## 통합 {#integration}

### 1단계: 캘린더 가입자 오디언스 구축 {#step-1-building-an-audience-of-calendar-subscribers}

Canvas에서 캘린더 이벤트를 보내려면 먼저 사용자가 이미 구독한 Rokt 캘린더 설정이 있어야 합니다. 이를 위해 사용자에게 캘린더를 구독하는 위치와 방법을 알려야 합니다. Rokt Calendar는 다음을 권장합니다:

#### 구독 통합 포인트 제공 {#provide-subscription-integration-points}
캘린더 가입자 오디언스를 구축하려면 사용자가 이동하여 구독할 수 있는 대상을 제공해야 합니다. 구독 통합 포인트의 예시는 다음과 같습니다:
  - 웹사이트에 캘린더 버튼 추가
  - 이메일 또는 단문 메시지 서비스에 캘린더 링크 추가
  - 앱에 캘린더 버튼 추가
  - 소셜 미디어에 캘린더 링크 추가

#### 캘린더 홍보 {#promote-the-calendar}
가입자 오디언스를 구축하려면 오디언스에게 캘린더를 홍보하여 구독 방법을 알려야 합니다. 캘린더 홍보 예시는 다음과 같습니다:
  - 소셜 미디어 게시물
  - 이메일 뉴스레터 및 업데이트
  - 블로그 게시물
  - 인앱 알림

### 2단계: Braze에서 Rokt Calendar 웹훅 생성 {#step-2-create-a-rokt-calendar-webhook-in-braze}

Braze 내에서 웹훅 Campaign 또는 Canvas 내 웹훅을 설정하여 다음 중 하나를 수행할 수 있습니다:

- 새 개인화된 이벤트 전송: 가입자 캘린더의 세그먼트에 새 이벤트를 추가할 수 있습니다.
- 개인화된 이벤트 업데이트: 가입자 캘린더의 기존 이벤트를 업데이트할 수 있습니다.

향후 Campaigns 또는 Canvases에서 사용할 Rokt Calendar 웹훅 템플릿을 생성하려면 Braze 플랫폼에서 **템플릿** > **웹훅 템플릿**으로 이동합니다.

일회성 Rokt Calendar 웹훅 Campaign을 생성하거나 기존 템플릿을 사용하려면 새 Campaign을 생성할 때 Braze에서 **웹훅**을 선택합니다.

{% tabs %}
{% tab 새 이벤트 전송 %}
Rokt Calendar 웹훅 템플릿을 선택하면 다음이 표시됩니다:
- **웹훅 URL**: {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}`{% endraw %}
- **요청 본문**: Raw Text
{% endtab %}
{% tab 기존 이벤트 업데이트 %}
Rokt Calendar 웹훅 템플릿을 선택하면 다음이 표시됩니다:
- **웹훅 URL**: {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}/update`{% endraw %}
- **요청 본문**: Raw Text
{% endtab %}
{% endtabs %}

#### 요청 헤더 및 메서드 {#request-headers-and-method}

Rokt Calendar는 Rokt Calendar 연결된 콘텐츠 자격 증명 이름을 포함하는 승인용 `HTTP Header`가 필요합니다. 다음은 이미 템플릿 내에 키-값 페어로 포함되어 있지만, **설정** 탭에서 `<Rokt-Calendar-API>`를 `설정 관리 > 연결된 콘텐츠 > 자격 증명`에 있는 자격 증명 이름으로 교체해야 합니다.

{% raw %}
- **HTTP 메서드**: POST
- **요청 헤더**:
  - **Authorization**: Bearer `{% connected_content https://api.roktcalendar.com/oauth2/token :method post :basic_auth <Rokt-Calendar-API> :body grant_type=client_credentials :save token :retry %}{{token.access_token}}`
  - **Content-Type**: application/json
{% endraw %}

#### 요청 본문 {#request-body}

{% tabs local %}
{% tab 새 이벤트 전송 %}
{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  },
  "subscriptionIds": ["{{custom_attribute.${rokt:subscription_id}| join: '","'  }}"]
}
```
{% endraw %}
{% endtab %}
{% tab 기존 이벤트 업데이트 %}
{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  }
}
```
{% endraw %}
{% endtab %}
{% tab 이벤트 세부 정보 %}
다음 필드에는 이벤트 수준에서 커스터마이즈할 수 있는 정보가 포함되어 있습니다.

| 필드             | 정의       | 예시          |
| ----------------  | ---------------- | ---------------- |
| `eventId` <br>***필수** | 추가하거나 업데이트할 이벤트의 고유 식별자 | `Event_00001`
| `eventTitle` <br>***필수** | 캘린더에 표시되는 이벤트 제목 | Summer Sale 2019
| `eventDescr` | 캘린더에 표시되는 이벤트 설명 | The sale is on for three days; click this link `www.mybusiness.com/sale` to see the offers. |
| `eventLocation` | 캘린더에 표시되는 이벤트 위치. 이것은 eventTitle을 보완하는 두 번째 행동 유도 문구로 자주 사용됩니다. | Open the event to get 50% off |
| `eventStart` <br>***필수**  | 캘린더에 표시되는 이벤트의 시작 날짜 및 시간 | `2019-02-21T15:00:00` |
| `eventEnd` <br>***필수**  | 캘린더에 표시되는 이벤트의 종료 날짜 및 시간 | `2019-02-21T16:00:00` |
| `eventTz` <br>***필수**  | 캘린더에 표시되는 이벤트의 시간대. 적용 가능한 시간대 목록은 [여기](https://roktcalendar-api.readme.io/docs/timezones)에서 확인할 수 있습니다. | `Eastern Standard Time` |
| `notifyBefore` <br>***필수**  | 캘린더에 표시되는 이벤트의 알림 시간. 분 단위로 표시됩니다. | `15` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Request body" }
{% endtab %}
{% endtabs %}

{% alert tip %}
유효한 시간대 목록은 [https://roktcalendar-api.readme.io/reference/timezones](https://roktcalendar-api.readme.io/reference/timezones)를 참조하세요.
{% endalert %}

### 3단계: 요청 미리보기 {#step-3-preview-your-request}

**미리보기** 패널에서 요청을 미리 보거나 **테스트** 탭으로 이동하여 랜덤 사용자, 기존 사용자를 선택하거나 직접 커스터마이즈하여 웹훅을 테스트할 수 있습니다.

{% alert important %}
페이지를 떠나기 전에 템플릿을 저장하는 것을 잊지 마세요! <br>업데이트된 웹훅 템플릿은 새 [웹훅 Campaign]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook/)을 생성할 때 **저장된 웹훅 템플릿** 목록에서 찾을 수 있습니다.
{% endalert %}