---
nav_title: 에이전트
article_title: 에이전트 단계
alias: /agent_step/
page_order: 2
page_type: reference
description: "이 참조 문서에서는 Canvas에서 에이전트 단계를 사용하여 콘텐츠를 생성하거나 실시간으로 지능적인 결정을 내리는 방법을 다룹니다."
tool: Canvas
toc_headers: h2
---

# 에이전트 단계 {#agent-step}

> 에이전트 단계를 사용하면 AI 기반 의사결정 및 콘텐츠 생성을 Canvas 워크플로에 직접 추가할 수 있습니다. 보다 일반적인 정보는 [Braze 에이전트]({{site.baseurl}}/user_guide/brazeai/agents)를 참조하세요.

![Canvas 사용자 여정의 에이전트 단계.]({% image_buster /assets/img/ai_agent/agent_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

## 전제 조건 {#prerequisites}

에이전트 단계는 [Canvas 컨텍스트 변수]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables)를 사용하여 관련 컨텍스트를 수집하고, Canvas에서 활용할 수 있는 변수를 출력합니다.

## 작동 방식 {#how-it-works}

사용자가 Canvas에서 에이전트 단계에 도달하면, Braze는 구성한 입력 데이터(전체 컨텍스트 또는 선택한 필드)를 선택한 에이전트에 전송합니다. 에이전트는 모델과 지시 사항을 사용하여 입력을 처리한 후 출력을 반환합니다. 해당 출력은 단계에서 정의한 출력 변수에 저장됩니다.

이 변수를 세 가지 주요 방식으로 활용할 수 있습니다:

- **의사 결정:** 에이전트의 응답을 기반으로 사용자를 서로 다른 Canvas 경로로 라우팅합니다. 예를 들어, 리드 스코어링 에이전트가 "영업 준비 완료", "마케팅 검증 완료", 또는 "부적격"과 같은 리드 카테고리를 반환할 수 있습니다. 이 할당을 사용하여 "영업 준비 완료" 리드에 대해 Slack 알림이나 자동 메시지를 트리거하고, "부적격" 리드는 여정에서 제외할 수 있습니다.
- **개인화:** 에이전트의 응답을 메시지에 직접 삽입합니다. 예를 들어, 에이전트가 고객 피드백을 분석하여 고객의 의견을 참조하고 해결 방안을 제안하는 공감적인 후속 이메일을 생성할 수 있습니다.
- **사용자 데이터 처리:** 사용자 데이터를 분석하고 표준화한 후 고객 프로필에 저장하거나 웹훅을 사용하여 전송합니다. 예를 들어, 에이전트가 감성 점수 또는 제품 친밀도 할당을 반환할 수 있습니다. 해당 데이터를 고객 프로필에 저장하여 향후 활용할 수 있습니다.

## Agent 단계 만들기 {#creating-an-agent-step}

### 1단계: 단계 추가 {#step-1-add-a-step}

사이드바에서 **Agent** 구성 요소를 끌어다 놓거나, 단계 하단에 있는 <i class="fas fa-plus-circle"></i> 더하기 버튼을 선택한 다음 **Agent**를 선택합니다.

### 2단계: 에이전트 선택 {#step-2-choose-your-agent}

이 단계에서 데이터를 처리할 에이전트를 선택합니다. 설정 방법은 [커스텀 에이전트 만들기]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)를 참조하세요.

에이전트 목록에서 각 에이전트에는 [일일 호출 한도]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#step-3-set-up-details)가 표시됩니다. 한도 위에 마우스를 올리면 사용된 비율과 한도 대비 오늘 사용된 호출 수를 포함하여 오늘의 진행 상황을 확인할 수 있습니다.

![에이전트 드롭다운에 두 개의 에이전트가 나열된 에이전트 단계 구성 패널. 각 에이전트에는 일일 호출 한도가 표시됩니다. 첫 번째 에이전트의 도구 설명에는 사용된 비율과 오늘 사용된 호출 수가 표시됩니다.]({% image_buster /assets/img/ai_agent/configure_agent_step.png %})

### 3단계: 에이전트 출력 설정 {#define-the-output-variable}

에이전트 출력은 "출력 변수"라고 하며, 쉽게 액세스할 수 있도록 [컨텍스트 변수]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context#context-variable-filters)에 저장됩니다. 출력 변수를 정의하려면 변수에 이름을 지정합니다.

출력 변수의 데이터 유형은 [에이전트 콘솔]({{site.baseurl}}/user_guide/brazeai/agents)에서 설정합니다. 에이전트 출력은 문자열, 숫자, 불리언 또는 객체로 저장할 수 있습니다. 따라서 Canvas에서 텍스트 개인화와 조건 로직 모두에 유연하게 활용할 수 있습니다. 다음은 각 유형의 일반적인 사용 사례입니다.

| 데이터 유형 | 일반적인 사용 사례 |
| --- | --- |
| 문자열 | 메시지 개인화(제목란, 카피, 응답) |
| 숫자 | 점수 산정, 임곗값, [오디언스 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths)에서의 라우팅 |
| 불리언 | [결정 분할]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split)에서의 예/아니오 분기 |
| 객체 | 이 섹션의 앞부분에서 다룬 데이터 유형 중 하나 이상을 단일 LLM 호출로 예측 가능한 데이터 구조에 활용 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="3단계: 에이전트 출력 설정 #define-the-output-variable" }

컨텍스트 변수와 동일한 템플릿 구문을 사용하여 Canvas 전체에서 출력 변수를 사용할 수 있습니다. **Context Variable** Segment 필터를 사용하거나, Liquid를 사용하여 에이전트 응답을 직접 템플릿에 적용합니다: {% raw %}`{{context.${response_variable_name}}}`{% endraw %}.

객체 출력 변수의 특정 속성정보를 사용하려면 Liquid에서 점 표기법을 사용하여 해당 속성정보에 액세스합니다: {% raw %}`{{context.${response_variable_name}.field_name}}`{% endraw %}

![변수 "agent_output"에 대한 객체 데이터 유형 출력이 포함된 Body HTML Writer의 에이전트 단계.]({% image_buster /assets/img/ai_agent/test_agent_step.png %}){: style="max-width:80%;"}

### 4단계: 선택적 단계 지침 추가 {#step-4-add-optional-step-instructions}

에이전트가 이 단계에 특화되어 알아야 하지만 에이전트의 기본 지침에서 아직 다루지 않은 내용에 대한 선택적 단계 지침을 포함할 수 있습니다. Canvas에서 일반적으로 사용하는 Liquid 템플릿 값을 입력할 수 있습니다.

### 5단계: 에이전트 테스트 {#step-5-test-the-agent}

Agent 단계는 두 가지 방법으로 테스트할 수 있습니다.

**단계 내 미리보기(Canvas 빌더):** 단계를 구성한 후 단계 미리보기를 사용하여 랜덤 사용자, 기존 사용자 또는 커스텀 사용자에 대한 에이전트 출력을 확인합니다. 이 방법은 전체 Canvas 경로를 실행하지 않고 단계를 단독으로 테스트합니다.

**Canvas 테스트(전체 여정):** Canvas 하단에서 **Canvas 테스트**를 선택하여 사용자 경로를 포괄적으로 미리봅니다. 테스트가 Agent 단계에 도달하면 Braze는 **에이전트 "{agentName}"을(를) 실행하시겠습니까?**라고 묻습니다.

- **예**를 선택하면 선택적으로 컨텍스트를 추가한 다음 **응답 시뮬레이션**을 선택하여 미리보기 사용자에 대해 에이전트를 호출합니다. 테스트 사용자의 프로필과 업스트림에서 이미 설정된 Canvas 컨텍스트를 보완하기 위해 일반 언어로 샘플 입력(예: 장바구니 내용 또는 메시지 텍스트)을 설명할 수 있습니다.
- **아니오**를 선택하면 실시간 호출을 건너뛰고 대신 에이전트 콘솔에서 구성한 에이전트의 **대체 출력**을 사용합니다.

**응답 시뮬레이션**의 호출은 에이전트의 일일 호출 한도에 포함되며 **에이전트 콘솔** > **로그**에 표시됩니다. Canvas 테스트의 전체 동작에 대해서는 [사용자 경로 미리보기]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths#agent-steps)를 참조하세요.

![랜덤 사용자로 에이전트 출력을 미리보기합니다.]({% image_buster /assets/img/ai_agent/agent_step_preview.png %}){: style="max-width:80%;"}

## 오류 처리 {#error-handling}

Braze가 에이전트 실패, 사용량 제한 오류 및 호출 흐름 제어를 처리하는 방법에 대해서는 에이전트 배포의 [오류 처리 및 대체 동작]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior)과 Braze 에이전트의 [오류 처리]({{site.baseurl}}/user_guide/brazeai/agents#error-handling)를 참조하세요.

- 연결된 모델이 LLM 공급자로부터 [사용량 제한 오류]({{site.baseurl}}/user_guide/brazeai/agents/reference#rate-limit-errors)를 반환하면, Braze는 호출이 성공하거나 완료할 수 없다고 판단할 때까지 지수 백오프를 사용하여 요청을 지속적으로 재시도합니다. 이후 사용자는 다음 캔버스 단계로 진행합니다.
- 기타 실패(예: 타임아웃 오류 또는 잘못된 API 키)가 발생하거나 에이전트가 일일 호출 한도에 도달하면, 에이전트 콘솔에서 [대체 값이 설정]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values)되어 있지 않은 한 출력 변수는 `null`로 설정됩니다. 대체 값이 설정된 경우, Braze는 사용자별로 Liquid를 사용하여 대체 값을 렌더링하고 그 결과를 출력 변수에 저장합니다. 일일 한도로 인해 호출이 차단된 경우에도 마찬가지입니다.
- 대체 값을 설정하지 않은 경우, 다운스트림 메시지 단계에서 [기본 Liquid 값]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values)을 사용하여 null 출력을 처리하세요. 예를 들어, **개인화 추가** Modal에서 {% raw %}`{{context.${response_variable_name}.push_title | default: 'Hello friend!'}}`{% endraw %} 또는 {% raw %}`{{context.${response_variable_name}.push_body | default: 'Open our app to get your prize!'}}`{% endraw %}와 같은 기본 Liquid 값을 입력할 수 있습니다.
- 동일한 입력에 대한 응답은 캐시되며, 몇 분 이내에 반복되는 동일한 호출에 재사용될 수 있습니다.
    - 캐시된 값을 사용하는 응답도 총 호출 수 및 일일 호출 수에 포함됩니다.
- 에이전트 단계는 대량의 사용자를 처리하는 데 시간이 걸릴 수 있습니다. Braze는 [호출 흐름 제어]({{site.baseurl}}/user_guide/brazeai/agents/reference#invocation-flow-controls)에 따라 호출을 대기줄에 넣으므로, 대량 발송 시 사용자가 대기 상태로 남아 있을 수 있습니다. 로그를 확인하여 호출이 진행되고 있는지 확인하세요.

## 분석 {#analytics}

에이전트 단계의 성능을 추적하려면 다음 측정기준을 참조하세요:

| 측정기준 | 설명 |
| --- | --- |
| *진입* | 사용자가 에이전트 단계에 진입한 횟수입니다. |
| *다음 단계로 진행* | 에이전트 단계를 통과한 후 플로우의 다음 단계로 진행한 사용자 수입니다. |
| *Canvas 종료* | 에이전트 단계를 통과한 후 Canvas를 종료한 사용자 수입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="분석" }

## 모범 사례 {#best-practices}

### 복잡한 사용 사례에서는 에이전트 간에 작업을 분할하세요 {#split-tasks-between-agents-for-complicated-use-cases}

에이전트가 요청한 작업의 복잡성을 감당하기 어려운 경우, 작업을 둘 이상의 에이전트 단계로 분할하세요. 하나의 프롬프트에 데이터 정리, 라우팅 로직, 전체 메시지 작성을 함께 포함하면 목표가 서로 충돌하여 출력 품질이 일정하지 않을 수 있습니다.

다음 패턴은 여행 예시에 세 개의 에이전트를 사용합니다. 최근 앱에서 검색했지만 예약하지 않은 사용자에게 결제를 유도하는 리타겟팅 카피를 보내려는 경우입니다.

- 에이전트 1은 Canvas 컨텍스트를 요약합니다. 로열티 등급, 마지막으로 검색한 구/군/시, 높은 의도의 검색 행동 등의 필드를 읽고, 이후 단계에서 재사용할 수 있는 짧은 구조화된 요약을 출력 변수로 반환합니다.
- 에이전트 2는 Canvas에서 분기할 수 있는 라우팅 값을 반환합니다. 숫자, 불리언 또는 구조화된 객체를 사용하여 출력이 분기 방식과 일치하도록 하세요. 해당 값을 [오디언스 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) 또는 [결정 분할]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/decision_split) 단계에 매핑하세요. 예를 들어, 로열티 중심 메시징과 할인 중심 메시징을 위한 별도의 경로를 고려해 보세요.
- 에이전트 3은 생성된 메시지 텍스트를 원하는 분기에서만 작성합니다. 에이전트 1의 요약(및 분기별 컨텍스트)을 전달하여 이 에이전트가 동일한 프롬프트에서 입력 정규화와 전략 선택을 수행하는 대신 톤과 채널 제한에 집중할 수 있도록 하세요.

### 실험 경로 단계를 사용하여 소규모로 에이전트 여정을 테스트하세요 {#use-the-experiment-paths-step-to-test-agentic-journeys-at-small-scale}

기존 여정 대비 에이전트의 성능과 크레딧 소비를 테스트하려면 [실험 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) 단계를 추가하여 오디언스의 일부만 에이전트 단계가 포함된 분기에 진입하도록 하세요.

예를 들어, 하루에 수천 명의 사용자만 에이전트가 있는 경로로 보내고 나머지는 대조군 경로 또는 에이전트가 없는 경로로 보내는 것부터 시작할 수 있습니다. 1~2주간 데이터를 수집하고 경로 간 KPI, 카운터 측정기준, 에이전트 크레딧 소비를 비교하세요. 이렇게 하면 에이전트 활성화 분기로 트래픽을 늘리기 전에 확신을 쌓고 투자수익률을 증명할 수 있으며, 호출 소비를 제한하면서 진행할 수 있습니다.

## 자주 묻는 질문 {#frequently-asked-questions}

### Agent 단계는 언제 사용해야 하나요? {#when-should-i-use-an-agent-step}

일반적으로, 특정 상황별 데이터를 LLM에 제공하고 사람이 처리하기 어려운 규모로 Canvas 컨텍스트 변수를 지능적으로 할당하고자 할 때 Agent 단계를 사용하는 것을 권장합니다.

이전에 초콜릿과 딸기를 주문한 사용자에게 새로운 아이스크림 맛을 추천하는 개인화된 메시지를 보내는 경우를 예로 들어 보겠습니다. Agent 단계와 AI 아이템 추천의 차이점은 다음과 같습니다.

- **Agent 단계:** LLM을 사용하여 에이전트에 제공된 지침과 상황별 데이터 포인트를 기반으로 사용자가 원할 수 있는 것에 대해 정성적 결정을 내립니다. 이 예시에서 Agent 단계는 사용자가 다양한 맛을 시도해 보고 싶어할 가능성에 기반하여 새로운 맛을 추천할 수 있습니다.
- **AI 아이템 추천:** 머신 러닝 모델을 사용하여 구매와 같은 과거 사용자 이벤트를 기반으로 사용자가 가장 원할 가능성이 높은 제품을 예측합니다. 이 예시에서 AI 아이템 추천은 사용자의 이전 두 번의 주문(초콜릿과 딸기)과 워크스페이스 내 다른 사용자의 행동과의 비교를 기반으로 맛(바닐라)을 제안합니다.

### Agent 단계는 입력 데이터를 어떻게 사용하나요? {#how-do-agent-steps-use-input-data}

Agent 단계는 에이전트가 사용하도록 구성된 상황별 데이터와 단계에 추가한 [선택적 단계 지침](#step-4-add-optional-step-instructions)을 분석합니다.

## 관련 문서 {#related-articles}

- [Braze Agents 개요]({{site.baseurl}}/user_guide/brazeai/agents)
- [커스텀 에이전트 만들기]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)
- [에이전트 배포]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents)
- [에이전트 참고 자료]({{site.baseurl}}/user_guide/brazeai/agents/reference)