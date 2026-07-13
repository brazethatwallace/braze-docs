---
nav_title: 에이전트 생성
article_title: 커스텀 에이전트 생성
description: "에이전트를 생성하는 방법, 시작하기 전에 준비해야 할 사항, 그리고 메시징, 의사결정 및 데이터 관리 전반에 걸쳐 에이전트를 활용하는 방법을 알아봅니다."
page_order: 1
alias: /creating-agents/
---

# 커스텀 에이전트 생성 {#create-custom-agents}

> 커스텀 에이전트를 생성하는 방법, 시작하기 전에 준비해야 할 사항, 그리고 메시징, 의사결정 및 데이터 관리 전반에 걸쳐 에이전트를 활용하는 방법을 알아봅니다. 더 일반적인 정보는 [Braze 에이전트]({{site.baseurl}}/user_guide/brazeai/agents)를 참조하세요.

## 필수 조건 {#prerequisites}

시작하기 전에 다음이 필요합니다:

- 워크스페이스에서 **에이전트 콘솔**에 접근할 수 있는 [권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#list-of-permissions). 이 옵션이 보이지 않으면 Braze 관리자에게 확인하세요.
- 커스텀 AI 에이전트를 생성하고 편집할 수 있는 권한.
- 에이전트가 달성하기를 원하는 목표에 대한 아이디어. Braze 에이전트는 다음과 같은 동작을 지원할 수 있습니다:
   - **개인화된 메시징:** 제목란, 헤드라인, 제품 내 카피 또는 기타 콘텐츠를 생성합니다.
   - **사용자 라우팅:** 동작, 선호도 또는 커스텀 속성에 따라 Canvas에서 사용자를 라우팅합니다.
   - **데이터 관리:** 값을 계산하고, 카탈로그 항목을 보강하거나, 프로필 필드를 새로고침합니다.

## 작동 방식 {#how-it-works}

에이전트를 생성할 때 목적을 정의하고 동작 방식에 대한 가이드라인을 설정합니다. 실시간 상태가 되면 에이전트를 Braze에 배포하여 개인화된 카피를 생성하고, 실시간 결정을 내리거나, 카탈로그 필드를 업데이트할 수 있습니다. 에이전트를 구축하는 동안 초안으로 저장할 수 있으며, 대시보드에서 언제든지 에이전트를 일시 중지하거나 업데이트할 수 있습니다.

다음 사용 사례는 커스텀 에이전트를 활용하는 몇 가지 방법을 보여줍니다.

| 사용 사례 | 설명 |
| --- | --- |
| 고객 피드백 처리 | 사용자 피드백을 에이전트에 전달하여 감정을 분석하고 공감하는 후속 메시지를 생성합니다. 고가치 사용자의 경우 에이전트가 응답을 에스컬레이션하거나 특전을 포함할 수 있습니다. |
| 콘텐츠 현지화 | 글로벌 Campaign을 위해 카탈로그 텍스트를 다른 언어로 번역하거나 지역별 채널에 맞게 톤과 길이를 조정합니다. 예를 들어, "Classic Clubmaster Sunglasses"를 스페인어로 "Gafas de sol Classic Clubmaster"로 번역하거나 SMS Campaign을 위해 설명을 줄일 수 있습니다. |
| 리뷰 또는 피드백 요약 | 감정이나 피드백을 새로운 필드로 요약합니다. 예를 들어, 긍정적, 중립적 또는 부정적과 같은 감정 점수를 할당하거나 "대부분의 고객이 좋은 핏을 언급하지만 느린 배송을 지적합니다."와 같은 짧은 텍스트 요약을 생성합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="작동 방식" }

## 에이전트 생성 {#create-an-agent}

### 1단계: 에이전트 유형 선택 {#step-1-choose-an-agent-type}

에이전트를 생성하려면 먼저 에이전트 유형을 선택합니다:

1. **에이전트 콘솔**로 이동합니다.
2. **캔버스 단계 에이전트** 또는 **카탈로그 에이전트**를 선택합니다.

### 2단계: 에이전트 구축 방법 선택 {#step-2-choose-how-to-build-an-agent}

**에이전트 생성**을 선택한 다음 다음 옵션 중 하나를 선택합니다:

- **커스텀 에이전트**를 선택하여 처음부터 에이전트를 구축합니다
- **Operator로 에이전트 생성**의 옵션을 선택하여 [BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator)를 사용해 [시작 템플릿](#agent-templates-built-with-operator)을 적용합니다

Operator를 사용하는 경우, 다음 단계로 진행하기 전에 채팅에서 변경 사항을 검토하고 승인하세요.

### 3단계: 세부 정보 설정 {#step-3-set-up-details}

다음으로 에이전트의 세부 정보를 설정합니다:

1. 팀이 목적을 이해할 수 있도록 이름과 설명을 입력합니다.
2. (선택 사항) 에이전트를 필터링하기 위해 태그를 추가합니다.
3. 에이전트가 사용할 [모델]({{site.baseurl}}/user_guide/brazeai/agents/reference#models)을 선택합니다.
4. **Braze Auto** 모델을 사용하지 않는 경우, 모델의 [사고 수준]({{site.baseurl}}/user_guide/brazeai/agents/reference#thinking-levels)을 선택합니다. 최소, 낮음, 중간 또는 높음 중에서 선택할 수 있습니다. **최소**로 시작하여 에이전트의 응답을 테스트한 후 필요에 따라 조정하는 것을 권장합니다.
5. 일일 호출 한도를 설정합니다. 기본값은 250,000으로 설정되어 있지만 1,000,000까지 높일 수 있습니다. 1,000,000 이상으로 한도를 늘리려면 고객 성공 매니저에게 문의하여 자세히 알아보세요.

![Braze에서 커스텀 에이전트를 생성하기 위한 에이전트 콘솔 인터페이스. 화면에는 에이전트 이름과 설명을 입력하고, 모델을 선택하고, 일일 호출 한도를 설정하는 필드가 표시됩니다.]({% image_buster /assets/img/ai_agent/create_custom_agent.png %}){: style="max-width:75%;"}

### 4단계: 지침 작성 {#agent-instructions}

에이전트에게 지침을 제공합니다. Operator 템플릿을 사용한 경우, 미리 채워진 지침을 검토하고 필요에 따라 편집하세요.

예기치 않거나 모호한 시나리오에서 에이전트가 수행해야 할 작업에 대한 지침을 포함하세요. 이렇게 하면 에이전트의 혼란으로 인한 오류 위험을 최소화할 수 있습니다. 예를 들어, 에이전트에게 "긍정적" 또는 "부정적" 감정 값만 요청하는 대신, 결정할 수 없는 경우 "확신 없음"을 반환하도록 요청하세요.

모범 사례는 [지침 작성]({{site.baseurl}}/user_guide/brazeai/agents/reference#writing-instructions)을 참조하고, 에이전트 프롬프트에 대한 영감은 [예시]({{site.baseurl}}/user_guide/brazeai/agents/reference#examples)를 참조하세요.

{% alert tip %}
Canvas 에이전트의 경우, 사용자 속성(예: 이름, 성 또는 커스텀 속성)을 참조하기 위해 지침에서 Liquid를 사용할 수 있습니다. 에이전트 지침의 모든 Liquid 변수는 사용자가 해당 단계에 진입할 때 자동으로 에이전트 단계로 전달됩니다.
{% endalert %}

#### 컨텍스트 추가 {#add-resources}

에이전트가 참조할 수 있는 항목을 선택하려면 **+ 에이전트 컨텍스트**를 선택합니다. 여기에는 다음이 포함됩니다:

- [카탈로그 필드]({{site.baseurl}}/user_guide/brazeai/agents/reference#catalogs-and-fields): 보다 정확한 응답을 위해 에이전트에게 카탈로그 데이터에 대한 액세스를 제공합니다.
- [Segment 멤버십]({{site.baseurl}}/user_guide/brazeai/agents/reference#segment-membership-context): 에이전트가 사용자가 속한 Segments에 따라 응답을 개인화할 수 있도록 합니다. 최대 5개의 Segments를 선택할 수 있습니다.
- [브랜드 가이드라인]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines): 에이전트가 따를 브랜드 보이스와 스타일 가이드라인을 참조합니다. 예를 들어, 에이전트가 사용자에게 체육관 회원 가입을 유도하는 SMS 카피를 생성하도록 하려면, 이 필드를 사용하여 미리 정의된 대담하고 동기 부여가 되는 가이드라인을 참조할 수 있습니다.
- [모든 Canvas 컨텍스트]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables): 이 에이전트가 호출될 때 **지침** 섹션에서 참조되지 않은 변수를 포함하여 사용자의 모든 Canvas 컨텍스트 데이터를 분석합니다.
- [사용자 상호작용 데이터]({{site.baseurl}}/user_guide/brazeai/agents/reference#user-history): 각 사용자의 최근 Campaign 및 Canvas 열람, 클릭, 전환 데이터를 에이전트에 제공합니다.

### 5단계: 출력 선택 {#select-output}

**출력** 섹션에서 기본 스키마 또는 고급 스키마로 에이전트의 [출력]({{site.baseurl}}/user_guide/brazeai/agents/reference#outputs)을 구성하고 정의할 수 있습니다. Operator 템플릿을 사용한 경우, 미리 채워진 출력 스키마를 검토하고 필요에 따라 편집하세요.

최상의 결과를 얻으려면 **출력** 섹션에서 지정한 내용이 [4단계](#agent-instructions)에서 입력한 에이전트 지침과 일치하는지 확인하세요. 예를 들어, 에이전트 지침에서 두 개의 문자열이 있는 오브젝트를 원한다고 언급한 경우, **출력** 섹션에서도 두 개의 문자열이 있는 오브젝트를 지정해야 합니다. 에이전트 지침이 지정한 출력과 일치하지 않으면 에이전트가 혼란스러워하거나 시간 초과되거나 원하지 않는 출력을 생성할 수 있습니다.

{% alert tip %}
[고급 출력 스키마]({{site.baseurl}}/user_guide/brazeai/agents/reference#advanced-schemas)를 사용할 때, 에이전트가 다른 출력과 함께 근거를 반환하도록 하려면 `explanation`이라는 이름의 문자열 필드를 추가하세요. 응답을 검토하거나 디버깅하는 데 도움이 되도록 [지침](#agent-instructions)에서 에이전트에게 `explanation`을 채우도록 지시하세요.
{% endalert %}

#### 대체 값 구성 {#configure-fallback-values}

대체 값은 **캔버스 단계 에이전트**에서만 사용할 수 있습니다. Canvas 에이전트의 **출력** 섹션에서 에이전트 호출이 실패할 때(예: LLM이 시간 초과되거나 잘못된 API 키 오류를 반환하는 경우) Braze가 사용하는 값을 정의할 수 있습니다. 대체 값은 개인화 기본값처럼 작동합니다. 에이전트가 실행할 수 없을 때에도 사용자에게 유용한 출력을 제공하는 정적 제목란이나 짧은 메시지를 설정할 수 있습니다.

**카탈로그 에이전트**는 에이전트 콘솔에서 대체 값 구성을 지원하지 않습니다.

![숫자 스키마에 대한 대체 출력 필드를 보여주는 에이전트 콘솔 출력 구성.]({% image_buster /assets/img/ai_agent/fallback_output.png %}){: style="max-width:75%;"}

Canvas 에이전트의 경우, 대체 값은 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) 템플릿을 지원하므로 대체 텍스트에서 사용자 속성이나 컨텍스트 변수를 참조할 수 있습니다.

대체 필드는 Canvas 에이전트의 출력 형식에 맞게 조정됩니다:

| 출력 형식 | 대체 구성 |
| --- | --- |
| 문자열, 숫자 또는 부울 | 단일 대체 값을 입력합니다(Liquid 지원). |
| 필드(고급 스키마) | 에이전트 출력에 정의된 각 필드에 대해 대체 값을 입력합니다. |
| JSON 스키마(고급 스키마) | Braze가 JSON 스키마를 읽고 각 속성에 대한 입력 필드를 생성하여 키별로 대체 값을 정의할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="대체 값 구성" }

대체 값이 있는 Canvas 에이전트가 [에이전트 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step)에서 실행되면, Braze는 사용자별로 대체를 렌더링하고 `null` 대신 출력 변수에 저장합니다. 대체 값을 구성하지 않으면 실패한 호출은 Canvas 출력을 미설정(`null`) 상태로 남깁니다.

런타임 동작에 대해서는 [오류 처리 및 대체 동작]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior)을 참조하세요.

### 6단계: 에이전트 테스트 {#step-6-test-the-agent}

**미리보기** 창은 구성 화면 내에서 나란히 패널로 표시되는 에이전트의 인스턴스입니다. 에이전트를 생성하거나 업데이트하는 동안 이 섹션을 사용하여 테스트할 수 있으며, 최종사용자와 유사한 방식으로 경험해 볼 수 있습니다. 이 단계는 에이전트가 예상대로 동작하는지 확인하는 데 도움이 되며, 실시간으로 전환하기 전에 미세 조정할 기회를 제공합니다.

1. **에이전트 테스트** 필드에 예시 고객 데이터 또는 고객 응답을 입력합니다. 에이전트가 처리할 실제 시나리오를 반영하는 내용이면 됩니다.
2. 무작위 사용자, 기존 사용자 또는 커스텀 사용자에 대한 에이전트의 응답을 미리 봅니다.
3. **응답 시뮬레이션**을 선택합니다. 에이전트가 구성에 따라 실행되고 응답을 표시합니다.

{% alert note %}
테스트 실행은 일일 호출 한도에 포함됩니다.
{% endalert %}

![커스텀 에이전트를 테스트하기 위한 미리보기 창을 보여주는 에이전트 콘솔. 인터페이스에는 예시 고객 데이터가 포함된 샘플 입력 필드, 테스트 실행 버튼, 에이전트 출력이 나타나는 응답 영역이 표시됩니다.]({% image_buster /assets/img/ai_agent/custom_agent_test.png %})

출력을 비판적인 시각으로 검토하세요. 다음 질문을 고려해 보세요:

- 카피가 브랜드에 맞게 느껴지나요?
- 결정 로직이 고객을 의도한 대로 라우팅하나요?
- 계산된 값이 정확한가요?

무언가 이상하게 느껴지면 에이전트의 구성을 업데이트하고 다시 테스트하세요. 에이전트가 시나리오에 따라 어떻게 적응하는지 확인하기 위해 다양한 입력을 실행해 보세요. 특히 데이터가 없거나 잘못된 응답과 같은 엣지 케이스도 포함해야 합니다.

{% alert tip %}
에이전트에게 원하지 않는 것을 정확히 말하지 마세요. LLM은 지침에서 언급된 콘텐츠를 오히려 생성할 수 있습니다.
{% endalert %}

### 7단계: 에이전트 사용 {#step-7-use-your-agent}

에이전트를 사용할 준비가 완료되었습니다! 자세한 내용은 [에이전트 배포]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents)를 참조하세요.

## Operator로 구축된 에이전트 템플릿 {#agent-templates-built-with-operator}

Operator는 다음 에이전트 콘솔 시작 템플릿에 대해 지침, 출력 필드 및 컨텍스트를 미리 구성할 수 있습니다. Operator에서 템플릿을 선택하거나 Operator에게 이름으로 적용하도록 요청하세요.

### 캔버스 단계 에이전트 템플릿 {#canvas-step-agent-templates}

| 템플릿 | 설명 | 예시 출력 |
| --- | --- | --- |
| 개인화된 카피라이터 | 사용자 속성, Canvas 컨텍스트 및 브랜드 가이드라인을 기반으로 채널별 메시지 카피를 생성합니다 | 이메일 제목란과 프리헤더, 푸시 제목과 본문 |
| 피드백 분석가 | 개방형 설문조사 또는 고객지원 피드백을 Canvas 분기를 위한 구조화된 필드로 구문 분석합니다 | 감정, 주제, 권장 다음 동작 |
| 여정 라우터 | 프로필 및 여정 컨텍스트를 기반으로 각 사용자를 가장 관련성 높은 Canvas 경로로 라우팅합니다 | 경로 이름 또는 결정 분할 단계를 위한 부울 값 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="캔버스 단계 에이전트 템플릿" }

### 카탈로그 에이전트 템플릿 {#catalog-agent-templates}

| 템플릿 | 설명 | 예시 출력 |
| --- | --- | --- |
| 설명 작성기 | 기존 카탈로그 열에서 짧은 마케팅 설명을 작성합니다 | 제품 또는 목적지 설명 |
| 항목 분류기 | 행 데이터에서 카테고리 또는 태그를 할당합니다 | 필터링 및 추천을 위한 카테고리 레이블 |
| 현지화 번역기 | 문자 수 제한 내에서 카탈로그 문자열을 대상 로케일로 번역합니다 | 로케일별 현지화된 텍스트 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="카탈로그 에이전트 템플릿" }

## 관련 리소스 {#related-resources}

- [에이전트 참조]({{site.baseurl}}/user_guide/brazeai/agents/reference)
- [자주 묻는 질문]({{site.baseurl}}/user_guide/brazeai/agents/faq)
- [AI 실전 활용: 1:1 개인화를 위한 3가지 새로운 사용 사례에 대한 Braze 웨비나](https://www.braze.com/resources/webinars-and-events/ai-in-action-use-cases)