---
nav_title: Zendesk
article_title: Zendesk
description: "이 참조 문서에서는 두 플랫폼 간의 고객지원 데이터를 동기화할 수 있는 Braze 웹훅을 활용할 수 있게 해주는 인기 고객지원 스위트인 Zendesk와 Braze 간의 파트너십에 대해 설명합니다."
alias: /partners/zendesk/
page_type: partner
search_tag: Partner

---

# Zendesk

> [Zendesk Support Suite](https://www.zendesk.com/support-suite/)(ZSS)는 이메일, 웹챗, 음성 또는 소셜 메시징 앱을 통한 옴니채널 고객지원으로 고객과 자연스러운 대화를 나눌 수 있는 기능을 비즈니스에 제공합니다. Zendesk는 상호작용의 추적과 우선순위 지정을 중시하는 간소화된 티켓팅 시스템을 제공하여, 비즈니스가 고객에 대한 통합된 이력 뷰를 가질 수 있도록 합니다.

Braze와 Zendesk 서버 간 통합을 통해 다음을 활용할 수 있습니다:
- Braze 웹훅을 사용하여 Braze의 사용자 여정에서 메시지 인게이지먼트로 인해 Zendesk에서 고객지원 티켓 생성을 자동화합니다. 예를 들어, 통합을 성공적으로 구현하고 테스트한 후, Braze는 "앱이 마음에 드시나요?"라는 인앱 메시지에 부정적으로 응답한 사용자로부터 고객지원 티켓을 생성하여 고객지원 팀이 해당 고객에게 후속 조치를 취할 수 있도록 합니다.
- Zendesk 웹훅을 사용하여 Zendesk의 활동으로 인해 Braze에서 고객 프로필을 업데이트하는 것과 같은 양방향 사용 사례를 지원합니다. 예를 들어, 티켓이 해결된 후 Braze의 고객 프로필에 이벤트를 기록합니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Zendesk 계정 | 이 파트너십을 활용하려면 [Zendesk 관리자 계정](https://`<your-zendesk-instance>`.zendesk.com/agent/admin)이 필요합니다. |
| Zendesk API 토큰 | Braze에서 Zendesk 티켓 엔드포인트로 요청을 보내려면 Zendesk [API 토큰](https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token-\)이 필요합니다. |
| 공통 식별자(권장) | Braze와 Zendesk 간의 [공통 식별자](#common-identifier)를 사용하는 것이 권장됩니다. |
| Braze API 키 | Zendesk에서 Braze 엔드포인트로 요청을 보내려면 Braze API 키가 필요합니다. 사용하는 API 키가 Zendesk 웹훅이 사용하는 Braze 엔드포인트에 대한 올바른 권한을 가지고 있는지 확인하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## Braze에서 Zendesk로의 통합 {#braze-to-zendesk-integration}

### 1단계: Braze 웹훅 생성 {#step-1-create-your-braze-webhook}

웹훅을 생성하려면:

- **Campaigns:** Braze 대시보드에서 **Campaigns** 페이지로 이동합니다. **캠페인 만들기**를 클릭하고 **웹훅**을 선택합니다.
- **Canvas:** 새 Canvas 또는 기존 Canvas에서 Canvas 빌더에서 전체 또는 메시지 단계를 생성합니다. 그런 다음 **메시지**를 클릭하고 메시지 옵션에서 **웹훅**을 선택합니다.

웹훅에서 다음 필드를 입력합니다:
- **웹훅 URL**: `<your-zendesk-instance>.zendesk.com/api/v2/tickets.json`
- **요청 본문**: Raw Text

추가 사용 사례는 [Zendesk 고객지원 API](https://developer.zendesk.com/rest_api/docs/support/introduction)를 통해 처리할 수 있으며, 이 경우 웹훅 URL 끝의 `/api/v2/` 엔드포인트가 그에 맞게 변경됩니다.

#### 요청 헤더 및 메서드 {#request-header-and-method}

Zendesk는 인증을 위한 HTTP 헤더와 HTTP 메서드가 필요합니다. **설정** 탭에서 <email_address>를 Zendesk 관리자 이메일로, <api_token>을 Zendesk API 토큰으로 교체하세요.

- **HTTP Method**: POST
- **요청 헤더**:
  - **Authorization**: Basic {% raw %} `{{ '<email_address>/token:<api_token>' | base64_encode }}` {% endraw %}
  - **Content-Type**: application/json

![Zendesk 인증 헤더와 POST 메서드가 구성된 Braze 웹훅 설정.]({% image_buster /assets/img_archive/zendesk_step1.gif %}){: style="max-width:70%;"}

#### 요청 본문 {#request-body}

웹훅 페이로드에서 유형, 제목, 상태 등의 티켓 세부 정보를 정의합니다. 티켓 세부 정보는 [Zendesk 티켓 API](https://developer.zendesk.com/rest_api/docs/support/tickets#create-ticket)를 기반으로 확장 및 커스텀할 수 있습니다. 다음 예제를 사용하여 페이로드를 구성하고 원하는 필드를 입력하세요.

{% raw %}
```json
{% assign ticket_type = 'question/incident/task/problem' %} << Choose one >>
{% assign ticket_subject = '' %}
{% capture ticket_body %}
<< Your message here >>
{% endcapture %}
{% assign ticket_subject_tag = '' %}
{% assign ticket_status = 'New' %}

{
"ticket": {
"requester_id": "{{${user_id}}}",
"requester": { "name": "{{${first_name}}} {{${last_name}}}", "email": "{{${email_address}}}", "phone": "{{${phone_number}}}"},
"type": "{{ ticket_type }}",
"subject":  "{{ticket_subject}}",
"comment":  { "body": "{{ticket_body}}" },
"priority": "urgent",
"status": "{{ ticket_status }}"
  }
}
```
{% endraw %}

### 2단계: 요청 미리보기 {#step-2-preview-your-request}

원시 텍스트가 적용 가능한 Braze 태그인 경우 자동으로 강조 표시됩니다.

**미리보기** 패널에서 요청을 미리 보거나 **테스트** 탭으로 이동하여 임의의 사용자 또는 기존 사용자를 선택하거나 직접 커스텀하여 웹훅을 테스트할 수 있습니다.

마지막으로, Zendesk 측에서 티켓이 생성되었는지 확인합니다.

## 공통 식별자 {#common-identifier}

Braze와 Zendesk 간에 공통 식별자가 있는 경우, 이를 `requester_id`로 활용하는 것이 권장됩니다. 이렇게 하면 두 세트의 사용자를 통합하는 데 도움이 됩니다. 또는 그렇지 않은 경우, 이름, 이메일 주소, 전화번호 등의 식별 속성 세트를 전달하는 것이 좋습니다.

## Zendesk에서 Braze로의 통합 {#zendesk-to-braze-integration}

### 1단계: 웹훅 생성 {#step-1-create-a-webhook}

1. [관리 센터](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb)에서 사이드바의 **Apps and integrations**를 클릭한 다음 **Webhooks > Webhooks**를 선택합니다.<br><br>
2. **Create webhook**을 클릭합니다.<br><br>
3. **Trigger** 또는 **Automation**을 선택하고 **Next**를 클릭합니다.<br>![Trigger 및 Automation 옵션이 표시된 Zendesk 웹훅 생성 화면.]({% image_buster /assets/img_archive/zendesk2.png %}){: style="max-width:70%;"}<br><br>
4. 웹훅에 다음 정보를 입력합니다:
- 웹훅의 이름과 설명을 입력합니다.
- 웹훅이 사용할 Braze 엔드포인트 URL을 입력합니다. {% raw %}이 예제에서는 `https://{{instance_url}}/users/track`을 사용합니다.{% endraw %}
- 웹훅의 요청 메서드로 POST를 선택하고 요청 형식을 JSON으로 설정합니다.
- 웹훅의 인증 메서드로 bearer 토큰 인증을 선택하고 [Braze API 키]({{site.baseurl}}/api/basics#creating-rest-api-keys)를 제공합니다.
  - 사용하는 API 키가 웹훅이 사용하는 Braze 엔드포인트에 대한 [올바른 권한]({{site.baseurl}}/api/basics#rest-api-key-permissions)을 가지고 있는지 확인하세요.<br><br>
5. (권장) 웹훅이 올바르게 작동하는지 테스트합니다.<br><br>
6. 트리거 및 자동화 웹훅의 경우, 설정을 완료하기 전에 웹훅을 트리거 또는 자동화에 연결해야 합니다. 웹훅에 대한 트리거 생성 예제는 다음 단계를 참조하세요. 트리거가 생성된 후 이 페이지로 돌아와 **Finish setup**을 선택할 수 있습니다.

### 2단계: 트리거 또는 자동화 생성 {#step-2-create-a-trigger-or-automation}

웹훅을 트리거 또는 자동화에 연결하는 방법은 [Zendesk의 안내](https://support.zendesk.com/hc/en-us/articles/4408839108378#topic_bwm_1tv_dpb)를 따르세요.

아래 예제에서는 고객지원 케이스 상태가 "Solved" 또는 "Closed"로 변경되었을 때 웹훅을 호출하는 트리거를 사용합니다.

1. **관리 센터**에서 사이드바의 **Objects and rules**를 클릭한 다음 **Business rules > Triggers**를 선택합니다.<br><br>
2. **Add trigger**를 선택합니다.<br><br>
3. 트리거의 이름을 지정하고 카테고리를 선택합니다.<br><br>
4. **Add condition**을 선택하여 웹훅을 트리거할 조건을 설정합니다. 예를 들어, "Status category changed to closed" 또는 "Status category changed to solved".![상태 카테고리 조건이 표시된 Zendesk 트리거 조건 빌더.]({% image_buster /assets/img_archive/zendesk1.png %}){: style="max-width:70%;"}<br><br>
5. **Add action**을 선택하고 **Notify active webhook**을 선택한 다음 드롭다운에서 이전 단계에서 생성한 웹훅을 선택합니다.<br><br>
6. Zendesk 변수 플레이스홀더를 사용하여 관련 필드를 동적으로 채우면서 Braze 엔드포인트에 맞게 JSON 본문을 정의합니다.<br>![JSON 본문 변수가 포함된 Zendesk 웹훅 액션 페이로드 편집기.]({% image_buster /assets/img_archive/zendesk3.png %}){: style="max-width:70%;"}<br><br>
7. **Create**를 선택합니다.<br><br>
8. 웹훅으로 돌아가서 **Finish setup**을 클릭합니다.