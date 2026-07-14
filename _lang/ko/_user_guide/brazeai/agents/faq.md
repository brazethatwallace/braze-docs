---
nav_title: FAQ
article_title: 에이전트 FAQ
description: "이 문서에서는 Braze 에이전트에 대해 자주 묻는 질문에 대한 답변을 제공합니다."
page_order: 10
toc_headers: h2
---

# 에이전트 자주 묻는 질문 {#agents-frequently-asked-questions}

> 이 문서에서는 Braze 에이전트에 대해 자주 묻는 질문에 대한 답변을 제공합니다.

## 일반 {#general}

### Canvas 에이전트와 카탈로그 에이전트의 차이점은 무엇인가요? {#what-is-the-difference-between-canvas-agents-and-catalog-agents}

에이전트를 생성할 때 Canvas 에이전트를 만들지 카탈로그 에이전트를 만들지 지정합니다. 이에 따라 에이전트가 지원할 수 있는 지침과 옵션의 유형이 결정됩니다. Canvas 에이전트는 여정 내에서 사용자를 실시간으로 처리하고, 카탈로그 에이전트는 처리된 정보로 열을 추가하거나 업데이트하여 카탈로그 데이터를 보강합니다.

### Auto 모델과 BYO(Bring-Your-Own) 모델을 사용하는 것의 이점은 무엇인가요? {#what-are-the-benefits-of-using-auto-model-versus-bring-your-own-byo-model}

Braze Auto 모델을 사용하면 다음과 같은 이점이 있습니다:

- API 키를 검색하거나 입력하거나 통합을 설정할 필요가 없습니다
- 각 호출을 작업에 가장 효과적인 모델로 자동 라우팅합니다

### 현재 에이전트 사용량은 어디에서 확인할 수 있나요? {#where-can-i-find-my-current-agent-usage}

**설정** > **결제** > **크레딧 사용량** > **에이전트 콘솔**로 이동하여 크레딧 소비량, 호출 횟수, 에이전트별 크레딧 비율을 확인하세요. 자세한 내용은 [일일 호출 및 크레딧 한도]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits)를 참조하세요.

### 에이전트 지침에서 조건부 Liquid 문을 사용할 수 있나요? {#can-i-use-conditional-liquid-statements-in-agent-instructions}

아니요, {% raw %}`{% if %}`{% endraw %} 문과 같은 Liquid 블록을 작성하려고 하면 유효성 검사 오류가 발생할 수 있습니다. 에이전트는 대신 프롬프트에서 자연어 설명을 통해 다양한 시나리오를 처리할 수 있습니다.

### 에이전트가 제가 전달한 특정 Liquid 속성이나 Canvas 컨텍스트 이외의 사용자 데이터에 접근할 수 있나요? {#can-agents-access-user-data-beyond-the-specific-liquid-attributes-or-canvas-context-that-i-pass-to-them}

아니요. 에이전트는 지침에서 Liquid를 사용하여 전달된 특정 사용자 데이터 포인트, [+ 에이전트 컨텍스트]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#add-resources) 선택 항목, Canvas의 업스트림 [컨텍스트 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context), 또는 에이전트 단계의 추가 컨텍스트만 수신합니다. 에이전트는 수신하도록 구성하지 않은 속성에 대해 사용자 프로필을 검색할 수 없습니다.

또한 에이전트는 필수 데이터가 누락되었을 때 경고할 수 없으며, 프롬프트에 있는 내용으로 그대로 진행합니다. 에이전트 설정을 의도적인 입력-출력 설계로 취급하세요. 에이전트에 필요한 모든 필드를 전달하고 **에이전트 콘솔** > **로그**에서 입력을 확인하세요. 자세한 안내는 [에이전트가 수신하는 데이터]({{site.baseurl}}/user_guide/brazeai/agents/reference#what-data-agents-receive)를 참조하세요.

## 문제 해결 {#troubleshooting}

### 에이전트가 지침이나 규칙을 따르지 않는 이유는 무엇인가요? {#why-did-my-agent-not-follow-my-instructions-or-rules}

[Operator]({{site.baseurl}}/user_guide/brazeai/operator)를 사용하여 에이전트가 지침을 따르지 않는 이유를 문제 해결해 보세요. Operator는 단계별 지침과 자세한 설명을 제공할 수 있습니다.

### 카탈로그 에이전트가 일부 행을 건너뛰는 이유는 무엇인가요? {#why-did-my-catalog-agent-skip-some-rows}

카탈로그 에이전트는 **실행에 필수**로 표시한 열이 비어 있거나 누락된 경우 해당 행을 건너뜁니다. 예를 들어, 아직 채워지지 않은 `gender` 필드가 이에 해당합니다. 입력 열을 선택한 후 카탈로그 필드에 대해 필수 입력 제어를 활성화하고 에이전트가 실행되기 전에 값이 포함되어야 하는 열을 선택하세요. 선택된 열은 기본적으로 필수로 시작되지만, 호출을 차단하지 않고 비어 있어도 되는 열은 제거할 수 있습니다. 이렇게 하면 불완전한 데이터에 토큰을 낭비하는 것을 방지할 수 있습니다.

에이전트는 열 종속성도 준수합니다. 출력 열이 다른 열에 종속되는 경우(예: 열 D가 열 B와 C의 값을 필요로 하는 경우), 해당 행에 대해 업스트림 열이 채워질 때까지 에이전트가 실행되지 않습니다.

자세한 내용은 [카탈로그 에이전트 모범 사례]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#catalog-agent-best-practices)를 참조하세요.

### 에이전트가 복잡한 작업을 처리하는 데 어려움을 겪고 있습니다. 성능을 어떻게 개선할 수 있나요? {#subagent-approach}

에이전트가 요청한 작업을 처리하는 데 어려움을 겪고 있다면 하위 에이전트 접근 방식을 고려해 보세요. 예를 들어, 세 개의 에이전트를 사용하여 다음을 수행할 수 있습니다:

- 에이전트 1은 인바운드 비정형 Canvas 컨텍스트 데이터를 표준화하고 변환합니다.
- 에이전트 2는 항목 세부 정보 카탈로그를 참조하고 관련될 수 있는 항목을 식별합니다.
- 에이전트 3은 각 항목에 대한 다양한 설명이 포함된 다른 카탈로그를 참조하고 이메일에 넣을 사용자에게 가장 관련성 높은 항목 설명을 식별합니다.

### 커스텀 에이전트가 자주 시간 초과되는 원인은 무엇인가요? {#what-might-cause-a-custom-agent-to-frequently-time-out}

커스텀 에이전트가 시간 초과될 수 있는 경우:

- 에이전트 지침에 불완전하거나 모순되는 내용이 있는 경우
- 에이전트 지침이 모든 시나리오를 다루지 않거나 대체 조건을 포함하지 않는 경우(예: "모든 입력이 비어 있으면 '개인화할 수 없습니다'를 출력")
- 에이전트 지침이 **출력** 탭에 지정된 것과 다른 출력 형식을 요청하는 경우(예: 에이전트 지침에서는 문자열을 요청하지만 **출력** 탭에서는 출력이 숫자로 정의된 경우)
- 에이전트의 작업이 너무 복잡하여 [하위 에이전트 접근 방식](#subagent-approach)이 더 적합한 경우

Canvas 에이전트의 경우, 호출이 실패했을 때 사용자가 여전히 출력을 받을 수 있도록 에이전트 콘솔에서 [대체 값]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values)을 구성하세요.

### 에이전트가 테스트에서는 잘 작동했는데 Canvas에서 실행하면 사용자별 데이터를 받지 못하는 이유는 무엇인가요? {#why-did-my-agent-do-fine-in-testing-but-isnt-getting-any-user-specific-data-when-i-launch-it-in-a-canvas}

에이전트가 테스트 중에는 올바르게 작동하지만 실시간 Canvas에서 사용자별 데이터를 수신하지 못하는 경우, 다음 문제 해결 단계를 시도해 보세요:

- 에이전트가 수신할 사용자별 데이터가 에이전트 지침에 Liquid 변수로 입력되어 있는지 확인하세요.
- 중요한 데이터가 Canvas 컨텍스트에 있는 경우, 에이전트 구성에서 **모든 Canvas 컨텍스트 추가** 옵션을 사용하여 에이전트가 전체 Canvas 컨텍스트를 수신하도록 하세요.
- 에이전트가 접근할 Canvas 컨텍스트가 Canvas 컨텍스트로 저장되어 있는지 확인하세요. 에이전트 단계 전에 컨텍스트 단계를 사용하여 이 데이터를 저장하세요.

## 규정 준수 {#compliance}

### 에이전트 콘솔은 GDPR/CCPA를 준수하나요? {#is-agent-console-gdprccpa-compliant}

네. 고객이 Braze Auto 모델(Gemini 기반)을 사용하는 경우, Google은 고객과 Braze 간의 데이터 처리 부록(DPA) 조건에 따라 Braze 하위 처리자로서 역할을 합니다.

### 에이전트 콘솔은 HIPAA를 준수하나요? {#is-agent-console-hipaa-compliant}

네. Braze Auto 모델을 사용하는 경우, Auto 모델을 구동하는 Gemini를 대상으로 Google과 특정 HIPAA(미국의료정보보호법) 계약인 비즈니스 제휴 부록(BAA)을 체결하고 있습니다.

BAA는 Braze Auto 모델을 사용하는 고객에게만 적용됩니다. 고객이 자체 LLM 키를 사용하는 경우, Braze는 HIPAA 적용 대상인 보호 대상 건강 정보(PHI)를 고객을 대신하여 LLM에 전송하지 않으며, 고객이 직접 전송합니다. 이 경우 Braze와 Google 간의 BAA는 적용되지 않습니다. 자체 LLM 키를 통한 데이터 처리는 고객의 계약 및 LLM 제공업체와 직접 체결한 BAA에 의해 관리됩니다.