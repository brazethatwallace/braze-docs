---
nav_title: Oppizi
article_title: Oppizi
alias: /partners/oppizi/
description: "이 참고 문서에서는 Braze와 Oppizi의 파트너십에 대해 간략하게 설명합니다."
page_type: partner
search_tag: Partner
---

# Oppizi

> [Oppizi](https://www.oppizi.com/)는 오프라인 마케팅 분야의 글로벌 리더로, 기업이 측정 가능한 타겟팅 다이렉트 메일 및 전단지 캠페인을 운영할 수 있는 원스톱 솔루션을 제공합니다.

_이 통합은 Oppizi에서 유지 관리합니다._

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ------------------------------ | ----------------------------------------------------------------------------- |
| Oppizi 계정 | 이 통합을 사용하려면 활성 Oppizi 계정이 필요합니다. |
| Oppizi API 키 | Oppizi 계정의 **Integrations** > **Braze**에서 확인할 수 있습니다. |
| Oppizi 다이렉트 메일 워크플로 ID | **Direct Mail Workflow** 페이지에서 Oppizi 워크플로를 생성하여 ID를 받습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 활용 사례 {#use-cases}

Oppizi 통합을 사용하면 다음을 수행할 수 있습니다:

* Oppizi의 웹훅 및 다이렉트 메일 워크플로에 연결된 Braze 트리거를 사용하여 **자동화된 다이렉트 메일 엽서를 발송**할 수 있습니다.
* Oppizi 다이렉트 메일 워크플로에서 **임계값, 웨이브 및 제한을 구성**하여 캠페인 발송을 제어할 수 있습니다.
* 디자인 경험이 없어도 Oppizi에 내장된 디자인 도구로 **전문적인 엽서를 디자인**할 수 있습니다.
* Oppizi의 대시보드로 **캠페인 성과를 실시간으로 추적**할 수 있습니다.

## 통합 {#integration}

### 1단계: Oppizi API 키 생성하기 {#step-1-generate-your-oppizi-api-key}

Braze에서 웹훅 템플릿을 사용하려면 먼저 Oppizi API 키를 생성해야 합니다.

1. Oppizi에 로그인합니다.
2. **Integrations** > **Braze**로 이동합니다.
3. API 키를 생성합니다.

이 페이지에서 필요에 따라 키를 관리, 해지, 생성할 수 있습니다.

### 2단계: Braze 웹훅 템플릿 만들기 {#step-2-create-a-braze-webhook-template}

다음으로, 향후 Campaigns 또는 Canvases에서 사용할 Oppizi용 웹훅 템플릿을 Braze에서 만듭니다:

1. Braze에서 **Content** > **Webhook**으로 이동합니다.
2. **Create webhook template**을 선택합니다.
3. 템플릿 이름을 입력합니다.
4. 웹훅 템플릿에서 다음 필드를 입력합니다:

- **Webhook URL:** `https://webhooks.oppizi.com/events`
- **Request Body:** **Raw Text**

요청 메서드 및 헤더의 경우, Oppizi는 템플릿에 다음 HTTP 헤더와 함께 HTTP 메서드를 포함하도록 요구합니다. 다음 필드를 입력합니다:

- **HTTP Method:** POST
- **Request Headers:**
  - **Authorization:** `Bearer <oppiziAPIKey>`
  - **Content-Type:** `application/json`

![Braze의 Oppizi 웹훅 헤더 예시.]({% image_buster /assets/img/oppizi/oppizi_braze_webhook_headers.png %})

**Request Body**에는 **oppiziWorkflowID** 필드를 포함해야 합니다. 이 ID는 Oppizi에서 워크플로를 생성할 때 생성되며, 수신자를 추가할 다이렉트 메일 워크플로를 지정하는 데 필요합니다. Oppizi의 각 다이렉트 메일 워크플로에는 고유 ID가 있으므로, Braze에서 Oppizi 웹훅 템플릿을 만드는 경우 항상 워크플로 ID를 올바른 ID로 업데이트해야 합니다.

{% alert note %}
다이렉트 메일을 보내는 데 필요한 수신자의 우편 주소에 대한 필수 커스텀 속성이 Braze 계정에 설정되어 있는지 확인하세요.
{% endalert %}

![Braze의 Oppizi 웹훅 템플릿 예시.]({% image_buster /assets/img/oppizi/oppizi_braze_webhook_example.png %})

다음은 요청 본문 예시입니다:

{% raw %}
```json
{
    "event" : "workflow.addRecipient",
    "oppiziWorkflowID" : "<oppiziWorkflowID>",
    "requestType" : "live",
    "recipient" : {
        "recipientID" : "{{${braze_id}}}",
        "firstName" : "{{${first_name}}}",
        "lastName" : "{{${last_name}}}",
        "address1" : "{{custom_attribute.${address1}}}",
        "address2" : "{{custom_attribute.${address2}}}",
        "city" : "{{custom_attribute.${city}}}",
        "country" : "{{${country}}}",
        "zipCode" : "{{custom_attribute.${zipCode}}}",
        "state" : "{{custom_attribute.${state}}}"
    }
}
```
{% endraw %}

### 3단계: Oppizi에서 다이렉트 메일 워크플로 만들기 {#step-3-create-a-direct-mail-workflow-in-oppizi}

1. Oppizi에서 **Direct Mail Workflow** > **Create workflow**로 이동합니다.
2. 임계값, 웨이브, 엽서 형식 및 아트워크를 포함한 워크플로 세부 정보를 구성합니다.
3. 웹훅 세부 정보 섹션에서 워크플로 ID를 포함하여 바로 사용할 수 있는 요청 본문을 확인할 수 있으며, 이를 Braze에 바로 붙여넣을 수 있습니다.

### 4단계: Braze에서 요청 미리보기 및 테스트하기 {#step-4-preview-and-test-your-request-in-braze}

Oppizi의 워크플로 ID로 요청 본문을 추가한 후 테스트를 실행하여 설정이 예상대로 작동하는지 확인합니다.

테스트를 실행하려면 요청 본문에서 `requestType`을 `live`에서 `test`로 업데이트하세요. 이 단계는 다이렉트 메일 오디언스에 테스트 수신자가 추가되는 것을 방지하는 데 중요합니다.

테스트가 끝나면 `requestType`을 다시 `live`로 업데이트하고 Canvas를 저장합니다. 이제 자동화된 다이렉트 메일 캠페인을 시작할 준비가 되었습니다.