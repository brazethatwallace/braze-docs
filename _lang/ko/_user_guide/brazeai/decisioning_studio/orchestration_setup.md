---
nav_title: 오케스트레이션 설정
article_title: 오케스트레이션 설정
page_order: 4
page_type: reference
description: "이 문서에서는 CEP 선택, 필수 자격 증명 수집, 통합 구성 등 BrazeAI Decisioning Studio의 오케스트레이션 설정 방법을 설명합니다."
toc_headers: h2
---

# 오케스트레이션 설정 {#set-up-orchestration}

> 의사 결정 에이전트는 고객 데이터를 수집하고 1:1 수준에서 개인화한 후 커뮤니케이션을 오케스트레이션하기 위해 고객 참여 플랫폼(CEP)에 연결해야 합니다. 이 문서에서는 준비해야 할 사항과 지원되는 각 CEP에 대한 통합 구성 방법을 다룹니다.

## 오케스트레이션이란? {#what-is-orchestration}

오케스트레이션은 Decisioning Studio와 고객 참여 플랫폼(CEP) 간의 연결입니다. 의사 결정 에이전트가 각 고객에 대한 최적의 동작을 결정하면, 오케스트레이션은 CEP를 통해 개인화된 커뮤니케이션을 트리거하여 해당 결정을 실행합니다.

다음과 같이 생각하면 됩니다:

- **Decisioning Studio**는 *무엇을* 보낼지, *언제* 보낼지를 결정합니다
- **CEP**는 *어떻게* 보낼지를 처리합니다

## CEP 선택 {#choose-your-cep}

첫 번째 단계는 Decisioning Studio와 함께 사용할 CEP를 선택하는 것입니다. 선택에 따라 설정 복잡도와 사용 가능한 기능이 달라집니다.

### 지원되는 CEP {#supported-ceps}

| CEP | 통합 유형 | 설정 복잡도 |
|-----|----------|------------|
| **Braze** | 네이티브 API 통합 (권장) | 낮음 |
| **Salesforce Marketing Cloud** | API 이벤트 + Journey Builder | 중간 |
| **기타 CEP** | 커스텀 (추천 파일) | 높음 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="지원되는 CEP" }

{% alert tip %}
이미 Braze를 CEP로 사용하고 있다면, 가장 원활한 설정 경험을 위해 네이티브 Braze 통합을 사용하는 것을 권장합니다.
{% endalert %}

## 필수 조건 {#prerequisites}

오케스트레이션을 설정하기 전에, 선택한 CEP에 따라 다음 항목을 준비하세요.

{% tabs %}
{% tab Braze %}

| 요구 사항 | 설명 |
|---------|------|
| **REST API 키** | 사용자 데이터, 메시지, Campaign(캠페인), Canvas, Segment, 템플릿에 대한 권한이 있는 새 API 키. |
| **Braze 대시보드 URL** | Braze 인스턴스 URL (예: `https://dashboard-01.braze.com`). |
| **앱 ID** | 추적하려는 앱과 연결된 API 키 (**설정** > **앱 설정**에서 확인). |
| **이메일 표시 이름 및 주소** | Campaign에 사용할 발신자 정보 (**설정** > **이메일 환경설정**에서 확인). |
| **기본 템플릿** | 에이전트가 오케스트레이션에 사용할 메시지 템플릿. 각 템플릿에 대해 API 트리거 Campaign을 생성합니다. |
| **테스트 사용자 ID** | 시작 전 통합을 테스트하기 위한 사용자 ID. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

{% endtab %}
{% tab Salesforce Marketing Cloud %}

| 요구 사항 | 설명 |
|---------|------|
| **앱 패키지 자격 증명** | 서버 간 API 통합이 포함된 설치 패키지의 Client ID, Client Secret, Authentication Base URI, REST Base URI, SOAP Base URI. |
| **API 권한** | 채널, 자산, 자동화, 여정, 연락처, 데이터 확장, 추적 이벤트에 대한 범위. |
| **데이터 확장** | 가입자 데이터, 참여 데이터, 추천을 위한 데이터 확장이 필요합니다. |
| **이메일 템플릿** | Decisioning Studio에서 사용할 템플릿과 각 템플릿 ID. |
| **Journey Builder 접근 권한** | API 이벤트 진입 소스를 사용하는 다단계 여정을 생성하고 활성화할 수 있는 접근 권한. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

{% endtab %}
{% tab 기타 CEP %}

Braze 또는 Salesforce Marketing Cloud 이외의 CEP를 사용하는 경우, Decisioning Studio는 추천 파일 방식으로 통합할 수 있습니다:

| 항목 | 설명 |
|------|------|
| **데이터 수집 기능** | CEP가 각 고객에 대한 개인화된 결정이 포함된 추천 파일(일반적으로 CSV 또는 JSON)을 수집할 수 있어야 합니다. |
| **동적 콘텐츠 지원** | Campaign이 추천 데이터를 기반으로 필드를 동적으로 채울 수 있어야 합니다. |
| **커스텀 엔지니어링 리소스** | 팀에서 추천 파일을 읽고 커뮤니케이션을 트리거하는 통합을 구축해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

{% endtab %}
{% endtabs %}

## Campaign 계획 {#plan-your-campaigns}

오케스트레이션을 설정하기 전에 다음 세부 사항을 고려하세요:

### 기본 템플릿 {#base-templates}

기본 템플릿은 의사 결정 에이전트가 사용할 수 있는 모든 메시지 템플릿입니다. 다음을 고려하세요:

- **템플릿 수는?** 에이전트는 하나의 템플릿 또는 여러 개의 템플릿으로 작동할 수 있습니다. 여러 개인 경우, 에이전트는 각 고객이 받을 템플릿을 개인화할 수 있습니다.
- **어떤 채널?** 이메일, 푸시, SMS 또는 조합. 각 채널에는 별도의 템플릿과 Campaign이 필요할 수 있습니다.
- **어떤 동적 요소?** 에이전트가 개인화할 메시지 부분(제목란, CTA, 오퍼, 타이밍 등)을 식별하세요. 이들은 API 트리거 등록정보 또는 동적 입력 안내가 됩니다.

### 재적격성 설정 {#re-eligibility-settings}

Campaign은 사용자가 메시지를 여러 번 받을 수 있도록 허용해야 합니다:

- 테스트 시, 동일한 Campaign을 동일한 사용자에게 반복적으로 보내야 합니다
- 프로덕션에서는, 에이전트가 연속된 날에 동일한 Campaign이 사용자에게 최적이라고 판단할 수 있습니다

{% alert note %}
테스트를 위한 재적격성을 설정하는 동안, Decisioning Studio 에이전트는 빈도 제한을 준수하도록 설계되어 있으며 프로덕션에서는 하루에 한 번 이상 동일한 Campaign을 사용자에게 보내지 않습니다.
{% endalert %}

### API 트리거 등록정보 {#api-trigger-properties}

Braze 통합의 경우, 에이전트가 최적화할 차원을 계획하세요. 이들은 Campaign에 동적 값을 전달하는 API 트리거 등록정보가 됩니다:

| 예시 차원 | API 트리거 등록정보 |
|----------|-------------------|
| 제목란 | {% raw %}`{{api_trigger_properties.${subject_line}}}`{% endraw %} |
| 행동 유도 문구 | {% raw %}`{{api_trigger_properties.${cta_message}}}`{% endraw %} |
| 오퍼 | {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %} |
| 할인 금액 | {% raw %}`{{api_trigger_properties.${discount}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="API 트리거 등록정보" }

## 통합 설정 {#integration-setup}

아래에서 CEP를 선택하여 통합 설정을 시작하세요.

{% tabs %}
{% tab Braze %}

## Braze 통합 설정 {#set-up-braze-integration}

다음 단계에 따라 Decisioning Studio 에이전트를 Braze의 오케스트레이션 기능과 통합하세요(Braze 서비스 팀이 도움을 드릴 수 있습니다):

### 1단계: API 키 생성 {#step-1-create-an-api-key}

**설정** > **API 키**로 이동한 다음, 다음 권한이 있는 새 키를 생성하세요:

{% multi_lang_include decisioning_studio/api_key_permissions.md %}

### 2단계: API 트리거 Campaign 설정 {#step-2-set-up-api-triggered-campaigns}

모든 최적화 차원에 대한 API 트리거 등록정보가 포함된 각 기본 템플릿에 대해 API 트리거 Campaign을 설정하세요.

기본 템플릿은 의사 결정 에이전트가 메시지 오케스트레이션에 사용할 수 있는 모든 템플릿입니다. 의사 결정 에이전트는 1개의 기본 템플릿 또는 여러 개를 가질 수 있으며, 여러 개인 경우 각 고객에게 적합한 기본 템플릿을 선택하는 것이 에이전트가 개인화하는 결정 중 하나가 됩니다.

### 3단계: 재적격성 구성 {#step-3-configure-re-eligibility}

모든 API 트리거 Campaign이 15분 이내에 사용자가 재적격 상태가 되도록 허용하세요.

![Decisioning Studio 빈도 제한 다이어그램]({% image_buster /assets/img/decisioning_studio/decisioning_studio_frequency_cap.png %})

{% alert note %}
Decisioning Studio 에이전트는 하루에 한 번 이상 동일한 Campaign을 보내지 않지만, 테스트 목적으로 하루에 여러 번 동일한 Campaign을 보낼 수 있어야 합니다.
{% endalert %}

### 4단계: 동적 입력 안내 추가 {#step-4-add-dynamic-placeholders}

이들은 Decisioning Studio 에이전트가 최적화하는 결정에 대한 동적 입력 안내 역할을 합니다.

#### 예시 1: 이메일 Campaign {#example-1-email-campaign}

Decisioning Studio 에이전트가 이메일 Campaign을 최적화한다고 가정합니다. 다음과 같이 구성될 수 있습니다:

![Decisioning Studio 이메일 예시 1]({% image_buster /assets/img/decisioning_studio/decisioning_email_example_1.png %})

에이전트가 템플릿 선택과 행동 유도 문구(CTA) 메시지를 최적화한다고 가정하면, 각 템플릿에 대해 API 트리거 Campaign을 생성해야 하며, 하나의 템플릿의 CTA 섹션은 다음과 같을 수 있습니다:

![Decisioning Studio 이메일 예시 2]({% image_buster /assets/img/decisioning_studio/decisioning_studio_braze_email_example_2.png %})

#### 예시 2: 푸시 Campaign {#example-2-push-campaign}

Decisioning Studio 에이전트가 푸시 Campaign의 메시지를 최적화한다고 가정합니다. 다음과 같이 구성될 수 있습니다:

![Decisioning Studio 푸시 예시 1]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_1.png %})

![Decisioning Studio 푸시 예시 2]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_2.png %})

결과 메시지는 다음과 같습니다:

![Decisioning Studio 푸시 예시 3]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_3.png %})

#### 예시 3: SMS Campaign {#example-3-sms-campaign}

Decisioning Studio 에이전트가 SMS Campaign의 필드를 최적화한다고 가정합니다. 다음과 같이 구성될 수 있습니다:

![Decisioning Studio SMS 예시 1]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_1.png %})

![Decisioning Studio SMS 예시 2]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_2.png %})

결과 메시지는 다음과 같습니다:

![Decisioning Studio SMS 예시 3]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_3.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## SFMC 통합 설정 {#set-up-sfmc-integration}

Decisioning Studio는 Salesforce Marketing Cloud와의 네이티브 통합을 지원합니다. Decisioning Studio는 동적 요소를 채우는 데 필요한 데이터와 함께 여정에 API 이벤트를 트리거합니다.

SFMC 통합을 구성하는 자세한 단계는 Decisioning Studio Go 설명서의 [SFMC 지침]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration)을 참조하세요.

{% endtab %}
{% tab 기타 CEP %}

## 기타 CEP 통합 설정 {#set-up-other-cep-integrations}

Decisioning Studio는 모든 고객 참여 플랫폼과 통합할 수 있습니다. 그러나 Decisioning Studio가 커뮤니케이션을 직접 트리거할 수 없으므로, 팀에서 일부 커스텀 엔지니어링 작업이 필요할 수 있습니다.

이 시나리오에서 에이전트는 "추천 파일"을 전달합니다. 이 파일에는 각 고객에 대한 행이 포함되어 있으며, 해당 고객에 대한 모든 개인화된 결정을 나타내는 열이 있습니다.

예를 들어, 다음 추천 파일은:

![Decisioning Studio 커스텀 예시 2]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_2.png %})

다음과 같은 이메일 Campaign을 최적화하는 데 사용될 수 있습니다:

![Decisioning Studio 커스텀 예시 1]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_1.png %})

{% endtab %}
{% endtabs %}

## 모범 사례 {#best-practices}

오케스트레이션을 준비할 때 다음 모범 사례를 염두에 두세요:

1. **좁은 범위로 시작하세요.** 처음에는 하나의 채널과 하나 또는 두 개의 템플릿을 사용하세요. 효과적인 방법을 파악한 후 나중에 확장할 수 있습니다.
2. **철저히 테스트하세요.** 시작하기 전에 소규모 사용자 세트로 통합을 테스트하여 동적 콘텐츠가 올바르게 채워지는지 확인하세요.
3. **설정을 문서화하세요.** Campaign ID, 템플릿 ID, API 키 및 기타 식별자를 기록해 두세요. Decisioning Studio 포털에서 이를 참조해야 합니다.
4. **팀과 협력하세요.** 오케스트레이션 설정에는 마케팅, 엔지니어링, 데이터 팀이 관여할 수 있습니다. 모든 사람이 프로세스에서 자신의 역할을 이해하도록 하세요.
5. **피드백 데이터를 계획하세요.** 오케스트레이션에는 메시지 발송과 에이전트가 학습하는 데 도움이 되는 참여 및 전환 데이터 수집이 포함됩니다. 자세한 내용은 [데이터 준비]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data)를 참조하세요.

## 다음 단계 {#next-steps}

오케스트레이션을 설정한 후, 에이전트 설계를 진행하세요:

- [의사 결정 에이전트 설계]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/design_agents)