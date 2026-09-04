---
nav_title: 오케스트레이션 설정
article_title: 오케스트레이션 설정
page_order: 4
page_type: reference
description: "이 문서에서는 CEP 선택, 필수 자격 증명 수집, 통합 구성 등 BrazeAI Decisioning Studio의 오케스트레이션 설정 방법을 설명합니다."
toc_headers: h2
---

# 오케스트레이션 설정 {#set-up-orchestration}

> 의사 결정 에이전트는 고객 데이터를 수집하고 1:1 수준에서 개인화한 후 커뮤니케이션을 오케스트레이션하기 위해 고객 인게이지먼트 플랫폼(CEP)에 연결해야 합니다. 이 문서에서는 준비해야 할 사항과 지원되는 각 CEP에 대한 통합 구성 방법을 다룹니다.

## 오케스트레이션이란 무엇인가요? {#what-is-orchestration}

오케스트레이션은 Decisioning Studio와 고객 인게이지먼트 플랫폼(CEP) 간의 연결입니다. 의사결정 에이전트가 각 고객에게 최적의 액션을 결정하면, 오케스트레이션은 CEP를 통해 개인화된 커뮤니케이션을 트리거하여 해당 결정을 실행합니다.

다음과 같이 생각해 보세요:

- **Decisioning Studio**는 무엇을 보낼지, 언제 보낼지를 결정합니다
- **CEP**는 어떻게 보낼지를 처리합니다

## 고객 인게이지먼트 플랫폼 선택 {#choose-your-cep}

첫 번째 단계는 Decisioning Studio와 함께 사용할 고객 인게이지먼트 플랫폼을 선택하는 것입니다. 선택에 따라 설정 복잡도와 사용 가능한 기능이 달라집니다.

### 지원되는 고객 인게이지먼트 플랫폼 {#supported-ceps}

| 고객 인게이지먼트 플랫폼 | 통합 유형 | 설정 복잡도 |
|-----|-----------------|------------------|
| **Braze** | 네이티브 API 통합 (권장) | 낮음 |
| **Salesforce Marketing Cloud** | API 이벤트 + Journey Builder | 중간 |
| **기타 고객 인게이지먼트 플랫폼** | 커스텀 (추천 파일) | 높음 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="지원되는 고객 인게이지먼트 플랫폼" }

{% alert tip %}
이미 Braze를 고객 인게이지먼트 플랫폼으로 사용하고 있다면, 가장 원활한 설정 경험을 위해 네이티브 Braze 통합을 사용하는 것을 권장합니다.
{% endalert %}

## 사전 요구 사항 {#prerequisites}

오케스트레이션을 설정하기 전에, 선택한 고객 인게이지먼트 플랫폼(CEP)에 따라 다음 항목을 준비하세요.

{% tabs %}
{% tab Braze %}

| 요구 사항 | 설명 |
|------|-------------|
| **REST API 키** | 사용자 데이터, 메시지, Campaigns, Canvas, Segments, 템플릿에 대한 권한이 있는 새 API 키입니다. |
| **Braze 대시보드 URL** | Braze 인스턴스 URL입니다(예: `https://dashboard-01.braze.com`). |
| **앱 ID** | 추적하려는 앱과 연결된 API 키입니다(**설정** > **앱 설정**에서 확인할 수 있습니다). |
| **이메일 표시 이름 및 주소** | Campaigns에 사용할 발신자 정보입니다(**설정** > **이메일 환경설정**에서 확인할 수 있습니다). |
| **기본 템플릿** | 에이전트가 오케스트레이션에 사용하는 메시지 템플릿입니다. 각 템플릿에 대해 API 트리거 Campaigns를 생성합니다. |
| **테스트 사용자 ID** | 출시 전에 통합을 테스트하기 위한 사용자 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사전 요구 사항" }

{% endtab %}
{% tab Salesforce Marketing Cloud %}

| 요구 사항 | 설명 |
|------|-------------|
| **앱 패키지 자격 증명** | 서버 간 API 통합이 포함된 설치 패키지의 클라이언트 ID, 클라이언트 시크릿, 인증 기본 URI, REST 기본 URI, SOAP 기본 URI입니다. |
| **API 권한** | 채널, 에셋, 자동화, 여정, 연락처, 데이터 확장, 추적 이벤트에 대한 범위입니다. |
| **데이터 확장** | 가입자 데이터, 인게이지먼트 데이터, 추천을 위한 데이터 확장이 필요합니다. |
| **이메일 템플릿** | Decisioning Studio에서 사용할 템플릿과 각 템플릿의 템플릿 ID입니다. |
| **Journey Builder 액세스** | API 이벤트 진입 소스를 사용하여 다단계 여정을 생성하고 활성화할 수 있는 액세스 권한입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사전 요구 사항" }

{% endtab %}
{% tab 기타 CEP %}

Braze 또는 Salesforce Marketing Cloud 이외의 CEP를 사용하는 경우, Decisioning Studio는 추천 파일 방식을 통해 통합할 수 있습니다.

| 항목 | 설명 |
|------|-------------|
| **데이터 수집 기능** | CEP가 각 고객에 대한 개인화된 의사결정이 포함된 추천 파일(일반적으로 CSV 또는 JSON)을 수집할 수 있어야 합니다. |
| **동적 콘텐츠 지원** | Campaigns가 추천 데이터를 기반으로 필드를 동적으로 채울 수 있어야 합니다. |
| **커스텀 엔지니어링 리소스** | 추천 파일을 읽고 커뮤니케이션을 트리거하는 통합을 구축할 팀이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사전 요구 사항" }

{% endtab %}
{% endtabs %}

## Campaign 계획하기 {#plan-your-campaigns}

오케스트레이션을 설정하기 전에 다음 세부 사항을 고려하세요:

### 기본 템플릿 {#base-templates}

기본 템플릿은 의사결정 에이전트가 사용할 수 있는 모든 메시지 템플릿입니다. 다음을 고려하세요:

- **템플릿 수는 몇 개인가요?** 에이전트는 하나의 템플릿 또는 여러 개의 템플릿으로 작업할 수 있습니다. 여러 개인 경우, 에이전트는 각 고객이 받는 템플릿을 개인화할 수 있습니다.
- **어떤 채널인가요?** 이메일, 푸시, SMS 또는 이들의 조합입니다. 각 채널에는 별도의 템플릿과 Campaign이 필요할 수 있습니다.
- **어떤 동적 요소가 있나요?** 에이전트가 개인화하는 메시지 부분(예: 제목란, CTA, 오퍼, 타이밍)을 식별하세요. 이러한 요소는 API 트리거 속성정보 또는 동적 입력 안내가 됩니다.

### 재자격 설정 {#re-eligibility-settings}

Campaign은 사용자가 메시지를 여러 번 받을 수 있도록 허용해야 합니다:

- 테스트 시, 동일한 Campaign을 동일한 사용자에게 반복적으로 전송합니다
- 프로덕션 환경에서는 에이전트가 연속된 날에 동일한 Campaign이 사용자에게 최적이라고 판단할 수 있습니다

{% alert note %}
테스트를 위한 재자격을 설정하는 동안, Decisioning Studio 에이전트는 빈도 제한을 준수하도록 설계되어 있으며 프로덕션 환경에서는 하루에 한 번 이상 동일한 Campaign을 사용자에게 전송하지 않습니다.
{% endalert %}

### API 트리거 속성정보 {#api-trigger-properties}

Braze 통합의 경우, 에이전트가 최적화하는 차원을 계획하세요. 이러한 차원은 Campaign에 동적 값을 전달하는 API 트리거 속성정보가 됩니다:

| 차원 예시 | API 트리거 속성정보 |
|-------------------|---------------------|
| 제목란 | {% raw %}`{{api_trigger_properties.${subject_line}}}`{% endraw %} |
| 행동 유도 문구 | {% raw %}`{{api_trigger_properties.${cta_message}}}`{% endraw %} |
| 오퍼 | {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %} |
| 할인 금액 | {% raw %}`{{api_trigger_properties.${discount}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="API 트리거 속성정보" }

## 통합 설정 {#integration-setup}

이 목록에서 고객 인게이지먼트 플랫폼(CEP)을 선택하여 통합 설정을 시작하세요.

{% tabs %}
{% tab Braze %}

## Braze 통합 설정 {#set-up-braze-integration}

Decisioning Studio 에이전트를 Braze의 오케스트레이션 기능과 통합하려면 다음 단계를 따르세요(Braze 서비스 팀이 도움을 드릴 수 있습니다):

### 1단계: API 키 생성 {#step-1-create-an-api-key}

**설정** > **API 키**로 이동한 다음, 다음 권한을 가진 새 키를 생성합니다:

{% multi_lang_include decisioning_studio/api_key_permissions.md %}

### 2단계: API 트리거 Campaigns 설정 {#step-2-set-up-api-triggered-campaigns}

최적화된 모든 차원에 대한 API 트리거 속성정보를 포함하여 각 기본 템플릿에 대해 API 트리거 Campaign을 설정합니다.

기본 템플릿은 Decisioning 에이전트가 메시지 오케스트레이션에 사용할 수 있는 모든 템플릿입니다. Decisioning 에이전트는 1개의 기본 템플릿 또는 여러 개의 기본 템플릿을 가질 수 있으며, 여러 개인 경우 각 고객에게 적합한 기본 템플릿을 선택하는 것이 에이전트가 개인화하는 의사결정 중 하나입니다.

### 3단계: 재적격성 구성 {#step-3-configure-re-eligibility}

모든 API 트리거 Campaigns에서 사용자가 15분 이내에 재적격 상태가 될 수 있도록 설정합니다.

![Decisioning Pro 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_studio_frequency_cap.png %})

{% alert note %}
Decisioning Studio 에이전트는 동일한 Campaign을 하루에 두 번 이상 발송하지 않지만, 테스트 목적으로 동일한 Campaigns를 하루에 여러 번 발송할 수 있는 기능이 필요합니다.
{% endalert %}

### 4단계: 동적 입력 안내 추가 {#step-4-add-dynamic-placeholders}

이는 Decisioning Studio 에이전트가 최적화하는 의사결정을 위한 동적 입력 안내 역할을 합니다.

#### 예시 1: 이메일 Campaign {#example-1-email-campaign}

Decisioning Studio 에이전트가 이메일 Campaign을 최적화한다고 가정합니다. 다음과 같이 구성할 수 있습니다:

![Decisioning Studio 이메일 예시 구성]({% image_buster /assets/img/decisioning_studio/decisioning_email_example_1.png %})

에이전트가 템플릿 선택과 행동 유도 문구(CTA) 메시지를 최적화한다고 가정하면, 각 템플릿에 대해 API 트리거 Campaign을 생성해야 하며, 하나의 템플릿의 CTA 섹션은 다음과 같을 수 있습니다:

![Decisioning Studio 이메일 CTA 예시]({% image_buster /assets/img/decisioning_studio/decisioning_studio_braze_email_example_2.png %})

#### 예시 2: 푸시 Campaign {#example-2-push-campaign}

Decisioning Studio 에이전트가 푸시 Campaign의 메시지를 최적화한다고 가정합니다. 다음과 같이 구성할 수 있습니다:

![Decisioning Studio 푸시 구성 예시]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_1.png %})

![Decisioning Studio 푸시 트리거 속성정보 예시]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_2.png %})

결과 메시지는 다음과 같습니다:

![Decisioning Studio 푸시 결과 메시지 예시]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_3.png %})

#### 예시 3: SMS Campaign {#example-3-sms-campaign}

Decisioning Studio 에이전트가 SMS Campaign의 필드를 최적화한다고 가정합니다. 다음과 같이 구성할 수 있습니다:

![Decisioning Studio SMS 구성 예시]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_1.png %})

![Decisioning Studio SMS 트리거 속성정보 예시]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_2.png %})

결과 메시지는 다음과 같습니다:

![Decisioning Studio SMS 결과 메시지 예시]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_3.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## SFMC 통합 설정 {#set-up-sfmc-integration}

Decisioning Studio는 Salesforce Marketing Cloud와의 네이티브 통합을 지원합니다. Decisioning Studio는 동적 요소를 채우는 데 필요한 데이터와 함께 여정에 API 이벤트를 트리거합니다.

{% alert important %}
구성 시 API ID는 대문자로 입력해야 합니다. 여기에는 여정 ID, Campaign ID 및 기타 모든 식별자가 포함됩니다. API ID를 소문자로 입력했지만 SFMC 데이터에 대문자 UUID가 포함되어 있으면 이벤트 필터가 일치하지 않고 보고 측정기준이 올바르게 채워지지 않습니다.
{% endalert %}

{% endtab %}
{% tab 기타 CEP %}

## 기타 CEP 통합 설정 {#set-up-other-cep-integrations}

Decisioning Studio는 모든 고객 인게이지먼트 플랫폼과 통합할 수 있습니다. 그러나 Decisioning Studio가 커뮤니케이션을 직접 트리거할 수 없으므로 팀에서 일부 커스텀 엔지니어링 작업이 필요할 수 있습니다.

이 시나리오에서 에이전트는 "추천 파일"을 전달합니다. 이 파일에는 각 고객에 대한 행이 포함되어 있으며, 해당 고객에 대한 모든 개인화된 의사결정을 나타내는 열이 있습니다.

예를 들어, 다음 추천 파일은:

![Decisioning Studio 추천 파일 예시]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_2.png %})

다음과 같은 이메일 Campaign을 최적화하는 데 사용될 수 있습니다:

![Decisioning Studio 커스텀 이메일 Campaign 예시]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_1.png %})

{% endtab %}
{% endtabs %}

## 모범 사례 {#best-practices}

오케스트레이션을 준비할 때 다음 모범 사례를 참고하세요:

1. **좁은 범위에서 시작하세요:** 처음에는 하나의 채널과 한두 개의 템플릿만 사용하세요. 효과적인 방법을 파악한 후 나중에 확장할 수 있습니다.
2. **철저하게 테스트하세요:** 출시 전에 소규모 사용자 그룹을 대상으로 통합을 테스트하여 동적 콘텐츠가 올바르게 채워지는지 확인하세요.
3. **설정을 문서화하세요:** Campaign ID, 템플릿 ID, API 키 및 기타 식별자를 기록해 두세요. Decisioning Studio 포털에서 참조할 때 이러한 정보가 필요합니다.
4. **팀과 협력하세요:** 오케스트레이션 설정에는 마케팅, 엔지니어링, 데이터 팀이 관여할 수 있습니다. 모든 구성원이 프로세스에서 자신의 역할을 이해하고 있는지 확인하세요.
5. **피드백 데이터를 계획하세요:** 오케스트레이션은 메시지를 전송하고 에이전트의 학습에 도움이 되는 인게이지먼트 및 전환 데이터를 수집합니다. 자세한 내용은 [데이터 준비]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data)를 참조하세요.

## 다음 단계 {#next-steps}

오케스트레이션을 설정한 후, 에이전트 설계를 진행하세요:

- [의사결정 에이전트 설계]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/design_agents)