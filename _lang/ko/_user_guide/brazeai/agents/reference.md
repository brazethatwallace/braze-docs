---
nav_title: 참조
article_title: 에이전트 참조
description: "Braze 에이전트에 대한 주요 세부 정보를 참조합니다."
page_order: 3
---

# 에이전트 참조 {#reference-for-agents}

> 커스텀 에이전트를 생성할 때 지침 및 출력 스키마와 같은 주요 설정에 대한 자세한 내용은 이 문서를 참조하세요. 단계별 설정은 [커스텀 에이전트 생성]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents)을 참조하세요. 소개는 [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents) 및 [자주 묻는 질문]({{site.baseurl}}/user_guide/brazeai/agents/faq)을 참조하세요.

## 모델 {#models}

에이전트를 설정할 때 응답을 생성하는 데 사용할 모델을 선택할 수 있습니다. 두 가지 옵션이 있습니다: Braze 기반 모델을 사용하거나 자체 API 키를 가져오는 것입니다.

{% alert important %}
Braze 기반 **Auto** 모델은 카탈로그 검색 및 Segment 멤버십과 같은 작업을 수행하기에 충분한 사고 능력을 갖춘 모델에 최적화되어 있습니다. 다른 모델을 사용할 때는 해당 모델이 사용 사례에 잘 작동하는지 테스트하는 것이 좋습니다. 다양한 속도와 기능을 가진 모델에 대해 다른 수준의 세부 정보 또는 단계별 사고를 제공하기 위해 [지침](#writing-instructions)을 조정해야 할 수도 있습니다.
{% endalert %}

### 옵션 1: Braze 기반 모델 사용 {#option-1-use-a-braze-powered-model}

이것은 추가 설정이 필요 없는 가장 간단한 옵션입니다. Braze는 대형 언어 모델(LLM)에 직접 액세스를 제공합니다. 이 옵션을 사용하려면 Gemini 모델을 사용하는 **Auto**를 선택하세요.

{% alert important %}
에이전트를 생성할 때 **모델** 드롭다운에서 **Braze Auto**가 옵션으로 표시되지 않으면, 고객 성공 매니저에게 문의하여 Braze Auto 모델을 사용할 수 있는 자격을 얻는 방법을 알아보세요.
{% endalert %}

### 옵션 2: 자체 API 키 가져오기 {#option-2-bring-your-own-api-key}

이 옵션을 사용하면 OpenAI, Anthropic 또는 Google Gemini와 같은 제공업체와 Braze 계정을 연결할 수 있습니다. LLM 제공업체로부터 자체 API 키를 가져오면 토큰 비용이 Braze가 아닌 제공업체를 통해 직접 청구됩니다.

레거시 모델은 몇 개월 후에 중단되거나 사용 중지될 수 있으므로 최신 모델을 정기적으로 테스트하는 것이 좋습니다. 에이전트를 대규모로 실행하기 위해 제공업체에 충분한 크레딧이 있는지 확인하세요. [알림 환경설정]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences)에서 에이전트 콘솔 알림에 가입하면 Braze가 모델이 더 이상 사용할 수 없거나 LLM 제공업체와의 청구 문제를 감지했을 때 알림을 받을 수 있습니다.

설정 방법:

1. **파트너 통합** > **기술 파트너**로 이동하여 제공업체를 찾으세요.
2. 제공업체에서 받은 API 키를 입력하세요.
3. **저장**을 선택하세요.

그런 다음 에이전트로 돌아가 모델을 선택할 수 있습니다.

Braze에서 제공하는 LLM을 사용할 때, 해당 모델의 제공업체는 Braze의 하위 프로세서로 작용하며, 이는 귀하와 Braze 간의 데이터 처리 부속서(DPA)의 조건에 따릅니다. 자체 API 키를 가져오기로 선택하면, LLM 구독의 제공업체는 귀하와 Braze 간의 계약에 따라 제3자 제공업체로 간주됩니다.

#### 사고 수준 {#thinking-levels}

일부 LLM 제공업체에서는 선택한 모델의 사고 수준을 조정할 수 있습니다. 사고 수준은 모델이 답변하기 전에 사용하는 사고의 범위를 정의합니다—빠르고 직접적인 응답부터 더 긴 추론 체인까지 다양합니다. 이는 응답 품질, 지연 시간 및 토큰 사용량에 영향을 미칩니다.

| 수준 | 사용 시기 |
|-------|-------------|
| **최소** | 간단하고 명확하게 정의된 작업(예: 카탈로그 조회, 간단한 분류). 가장 빠른 응답과 가장 낮은 비용. |
| **낮음** | 약간 더 많은 추론이 도움이 되지만 깊은 분석이 필요하지 않은 작업. |
| **중간** | 다단계 또는 미묘한 작업(예: 여러 입력을 분석하여 동작을 추천). |
| **높음** | 복잡한 추론, 엣지 케이스, 또는 모델이 답변하기 전에 단계를 거쳐야 할 때. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사고 수준" }

**최소**로 시작하여 에이전트의 응답을 테스트하는 것을 권장합니다. 에이전트가 정확한 답변을 제공하는 데 어려움을 겪는 경우 사고 수준을 **낮음** 또는 **중간**으로 조정할 수 있습니다. 드문 경우에 **높음** 사고 수준이 필요할 수 있지만, 이 수준을 사용하면 높은 토큰 비용과 더 긴 응답 시간 또는 타임아웃 오류의 위험이 높아질 수 있습니다. 에이전트가 다단계 추론과 합리적인 응답 시간 사이에서 균형을 맞추는 데 어려움을 겪는 경우, 사용 사례를 Canvas 또는 카탈로그에서 함께 작동할 수 있는 둘 이상의 에이전트로 분리하는 것을 고려하세요.

Braze는 연결된 콘텐츠와 동일한 IP 범위를 아웃바운드 LLM 호출에 사용합니다. 해당 범위는 [연결된 콘텐츠 IP 허용 목록]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#connected-content-ip-allowlisting)에 나열되어 있습니다. 제공업체가 IP 허용 목록을 지원하는 경우, Braze만 사용할 수 있도록 키를 해당 범위로 제한할 수 있습니다.

{% alert important %}
Braze에서 제공하는 LLM을 사용할 때, 해당 모델의 제공업체는 Braze의 하위 프로세서로 작용하며, 이는 귀하와 Braze 간의 데이터 처리 부속서(DPA)의 조건에 따릅니다. 자체 API 키를 가져오기로 선택하면, LLM 구독의 제공업체는 귀하와 Braze 간의 계약에 따라 제3자 제공업체로 간주됩니다.
{% endalert %}

#### 사용할 모델 결정 {#determine-which-model-to-use}

각 LLM 제공업체는 모델 기능, 비용 및 사고 수준의 조합이 약간씩 다릅니다. 다음은 일반적인 가이드라인과 모범 사례입니다:

- 비용 효율성을 위해 높은 비용 모델보다 낮은 토큰 비용 모델을 우선적으로 테스트하세요. 낮은 비용 모델이 사용 사례에 어려움을 겪거나 일관성 없거나 부정확한 출력을 생성하는 경우에만 높은 비용 모델로 조정하세요.
- 속도 및 성능 효율성을 위해 높은 사고 수준보다 낮은 모델 사고 수준을 우선적으로 테스트하세요. 낮은 사고 수준이 사용 사례에 어려움을 겪거나 일관성 없거나 부정확한 출력을 생성하는 경우에만 높은 사고 수준 모델로 조정하세요.
- 낮은 비용 모델이나 모델 사고 수준이 사용 사례에 어려움을 겪거나 일관성 없거나 부정확한 출력을 생성하는 경우, 높은 비용 모델이나 사고 수준 모델로 조정하는 것을 고려하세요.
- 테스트 중에는 신뢰성과 정확성을 토큰 사용량 및 호출 시간과 균형 있게 맞추세요.
- 각 사용 사례마다 최적의 모델과 사고 수준이 다를 수 있습니다. 타임아웃 없이 일관된 품질을 확인하기 위해 철저히 테스트하는 것을 권장합니다.

### 호출 흐름 제어 {#invocation-flow-controls}

다음 호출 흐름 제어는 워크스페이스당 적용됩니다:

- **Braze 기반 모델:** 분당 5,000회 호출
- **자체 API 키 가져오기:** 분당 5,000회 호출

많은 사용자가 동시에 에이전트 단계에 진입하면, Braze는 이러한 제한에 따라 호출을 대기줄에 넣으므로 대량 발송 시 처리 시간이 더 오래 걸릴 수 있습니다.

### 일일 호출 및 크레딧 한도 {#daily-invocation-and-credit-limits}

각 에이전트에는 일일 호출 한도가 있습니다(기본값 250,000, 계약에서 더 높은 값을 허용하지 않는 한 최대 1,000,000). 에이전트 콘솔 미리보기 및 **응답 시뮬레이션**을 사용하는 테스트 Canvas 실행을 포함한 모든 호출이 이 한도에 포함됩니다.

에이전트 콘솔에서 **일일 액션 크레딧 비용 한도**는 에이전트가 하루에 소비할 수 있는 최대 크레딧을 추정합니다. Braze는 선택한 모델에 대한 워크스페이스의 호출당 **크레딧 비율**에 일일 호출 한도를 곱합니다.

### 크레딧 사용량 모니터링 {#monitor-credit-usage}

**설정** > **청구** > **크레딧 사용량** > **에이전트 콘솔**로 이동하여 크레딧 소비량, 호출 횟수 및 에이전트별 크레딧 비율을 확인하세요.

크레딧 비율은 계약에서 제공되며 [크레딧 사용량]({{site.baseurl}}/user_guide/administer/global/billing/credits_usage) 대시보드(**크레딧 비율** 탭 및 **에이전트 콘솔** 탭)에 표시됩니다. 모델이나 호출 한도를 변경하면 추정치가 업데이트됩니다.

지출을 관리하려면 일일 호출 한도를 낮추세요. [자체 키 가져오기(BYO)](#option-2-bring-your-own-api-key) 모델의 경우, 더 낮은 비용의 모델을 선택하거나 [사고 수준](#thinking-levels)을 낮춰 제공업체 토큰 비용을 줄일 수도 있습니다. **Braze Auto**는 사고 수준 조정을 지원하지 않습니다.

### 사용량 제한 오류 {#rate-limit-errors}

LLM 제공업체가 Canvas 단계 에이전트 또는 카탈로그 에이전트 호출 중에 사용량 제한 오류를 반환하면, Braze는 호출이 성공하거나 완료할 수 없다고 판단할 때까지 지수 백오프를 사용하여 요청을 지속적으로 재시도합니다.

Canvas 또는 카탈로그 재시도가 모두 소진되면, **로그** 세부 정보 패널에 **Error**가 표시되고 **출력**에 제공업체 메시지(예: `Rate limit exceeded`)가 표시됩니다. 재시도는 최종 성공 또는 실패 여부에 관계없이 첫 번째 호출을 포함하여 로그에 표시됩니다. 특정 사용자의 경우, 성공하기까지 4번의 재시도가 필요했다면 사용자 ID를 검색하여 **로그**에서 5개(원본 + 4번의 재시도)를 모두 확인할 수 있으며, 원본과 처음 3번의 재시도는 `Rate limit exceeded`와 함께 **Error**로 표시됩니다.

![출력 필드에 사용량 제한 초과 오류가 표시된 에이전트 콘솔 로그 세부 정보.]({% image_buster /assets/img/ai_agent/rate_limit_error_log.png %}){: style="max-width:75%;"}

## 지침 작성 {#writing-instructions}

지침은 에이전트(시스템 프롬프트)에게 주는 규칙 또는 가이드라인입니다. 에이전트가 실행될 때마다 어떻게 행동해야 하는지를 정의합니다. 시스템 지침은 최대 25KB까지 가능합니다.

[BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator)를 사용하여 [시작 템플릿]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator)으로 에이전트를 구축한 경우, 미리 채워진 지침을 검토하고 필요에 따라 편집하세요.

프롬프트를 시작하는 데 도움이 되는 일반적인 모범 사례는 다음과 같습니다:

1. 결과를 염두에 두고 시작하세요. 목표를 먼저 명시하세요.
2. 모델에 역할이나 페르소나를 부여하세요("당신은 ...입니다").
3. 명확한 컨텍스트와 제약 조건을 설정하세요(오디언스, 길이, 톤, 형식).
4. 구조를 요청하세요("JSON/글머리 목록/표로 반환...").
5. 말하지 말고 보여주세요. 몇 가지 고품질 예제를 포함하세요.
6. 복잡한 작업을 순서가 있는 단계로 나누세요("1단계... 2단계...").
7. 추론을 장려하세요("단계를 내부적으로 생각한 다음 간결한 최종 답변을 제공하세요," 또는 "결정을 간략하게 설명하세요").
8. 파일럿, 검사 및 반복하세요. 작은 조정이 큰 품질 향상으로 이어질 수 있습니다.
9. 엣지 케이스를 처리하고, 가드레일을 추가하고, 거부 지침을 추가하세요.
10. 내부에서 효과가 있는 것을 측정하고 문서화하여 재사용 및 확장할 수 있도록 하세요.

### 예시 {#examples}

에이전트 콘솔의 시작 구성은 [Operator로 구축된 에이전트 템플릿]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator)을 참조하세요.

복사하거나 수정할 수 있는 전체 지침 예시는 [Braze 에이전트 사용 사례 라이브러리]({{site.baseurl}}/user_guide/brazeai/agents/examples)를 참조하세요.

| 예시 | 카테고리 | 에이전트 유형 | 기능 |
| --- | --- | --- | --- |
| [사용자 컨텍스트를 기반으로 개인화된 메시지 작성]({{site.baseurl}}/user_guide/brazeai/agents/examples#write-personalized-messaging-based-on-a-users-context) | 콘텐츠 생성 | Canvas 단계 에이전트 | 검색했지만 예약하지 않은 사용자를 위해 조율된 이메일 제목/프리헤더 및 푸시 제목/본문을 생성합니다. |
| [사용자 피드백을 분석하여 다음 단계 결정]({{site.baseurl}}/user_guide/brazeai/agents/examples#analyze-user-feedback-to-determine-next-steps) | 데이터 표준화 | Canvas 단계 에이전트 | 여행 후 설문조사의 감정과 주제를 분류한 다음 CRM 다음 단계를 추천합니다. |
| [기존 속성에서 사용자를 관심사 버킷으로 분류]({{site.baseurl}}/user_guide/brazeai/agents/examples#categorize-users-into-interest-buckets-from-existing-attributes) | 친밀도 에이전트 | Canvas 단계 에이전트 | 속성 및 높은 의도 신호에서 사용자를 관심사 버킷으로 분류한 다음 최적의 다음 경험 또는 항목을 추천합니다. |
| [최근 행동에서 가장 관련성 높은 Canvas 경로로 사용자 라우팅]({{site.baseurl}}/user_guide/brazeai/agents/examples#route-users-to-the-most-relevant-canvas-path-from-recent-behavior) | 친밀도 에이전트 | Canvas 단계 에이전트 | 최근 행동에서 동기를 추론하고 사용자의 다음 캔버스 단계에 가장 적합한 경로 키를 반환합니다. |
| [실시간 높은 의도 행동에서 사용자를 관심사 카테고리에 할당]({{site.baseurl}}/user_guide/brazeai/agents/examples#assign-users-to-interest-categories-from-real-time-high-intent-actions) | 친밀도 에이전트 | Canvas 단계 에이전트 | 높은 의도 행동에서 관심사 카테고리를 할당하고 최적의 다음 경험 또는 항목을 추천합니다. |
| [수신 거부 의도에 대한 인바운드 메시지 분류]({{site.baseurl}}/user_guide/brazeai/agents/examples#classify-inbound-messages-for-opt-out-intent) | 분류 및 라우팅 | Canvas 단계 에이전트 | 메시지가 수신 거부 요청인지 여부를 나타내는 엄격한 부울 값을 반환합니다. |
| [자동화를 위해 인바운드 메시지를 구조화된 데이터로 표준화]({{site.baseurl}}/user_guide/brazeai/agents/examples#standardize-inbound-messages-into-structured-data-for-automation) | 데이터 표준화 | Canvas 단계 에이전트 | 인바운드 SMS 또는 채팅을 다운스트림 자동화를 위한 구조화된 의도, 엔티티 및 규정 준수 플래그로 정규화합니다. |
| [브랜드 가이드라인에 맞는 높은 전환율의 설명 작성]({{site.baseurl}}/user_guide/brazeai/agents/examples#write-high-converting-descriptions-that-align-with-brand-guidelines) | 콘텐츠 생성 | 카탈로그 에이전트 | 각 카탈로그 행에 대해 짧고 브랜드에 맞는 설명을 생성합니다. |
| [지역별 사용 언어에 따른 번역 제공]({{site.baseurl}}/user_guide/brazeai/agents/examples#provide-translations-based-on-language-used-by-region) | 카탈로그 보강 | 카탈로그 에이전트 | 로케일 및 문자 제한에 따라 UI 및 마케팅 문자열을 현지화합니다. |
| [설명, 카테고리 및 태그로 카탈로그 항목 보강]({{site.baseurl}}/user_guide/brazeai/agents/examples#enrich-catalog-items-with-descriptions-categories-and-tags) | 카탈로그 보강 | 카탈로그 에이전트 | 기존 카탈로그 항목 데이터에서 향상된 설명, 카테고리 및 태그를 생성합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="예시 요약" }

### Liquid 사용 {#using-liquid}

에이전트의 지침에 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)를 포함하면 응답에 추가적인 개인화 레이어를 더할 수 있습니다. 에이전트가 받는 정확한 Liquid 변수를 지정할 수 있으며, 이를 프롬프트의 컨텍스트에 포함할 수 있습니다. 예를 들어, "이름"을 명시적으로 작성하는 대신 Liquid 스니펫 {% raw %}`{{${first_name}}}`{% endraw %}을 사용할 수 있습니다:

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

**에이전트 콘솔**의 **로그** 섹션에서 에이전트의 입력 및 출력 세부 정보를 검토하여 Liquid에서 렌더링된 값을 확인할 수 있습니다.

### 에이전트가 수신하는 데이터 {#what-data-agents-receive}

에이전트 컨텍스트는 개방형 대화 메모리가 아닙니다. 채팅 어시스턴트와 달리, 에이전트는 호출 시 명시적으로 전달한 데이터만 볼 수 있습니다—사용자 프로필을 탐색하거나, 누락된 필드를 추론하거나, 필요한 정보가 없을 때 알려주지 않습니다.

각 에이전트를 의도적인 입력-출력 파이프라인으로 설계하세요. 에이전트가 필요로 하는 모든 데이터 포인트를 다음 중 하나 이상을 사용하여 연결하세요:

1. **지침의 Liquid:** 사용자 속성({% raw %}`{{${first_name}}}`{% endraw %}) 및 [Canvas 컨텍스트 변수]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables)({% raw %}`{{context.${variable_name}}}`{% endraw %})를 에이전트 프롬프트에 직접 템플릿으로 포함합니다.
2. **+ 에이전트 컨텍스트:** 에이전트 콘솔에서 카탈로그, Segment 멤버십, 브랜드 가이드라인, **모든 Canvas 컨텍스트** 또는 사용자 상호작용 데이터를 선택합니다.
3. [컨텍스트 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context): 에이전트 단계가 실행되기 전에 Canvas 업스트림에서 `context.*` 변수를 설정하거나 업데이트합니다.
4. **에이전트 단계의 추가 컨텍스트:** 다른 방법으로 이미 지정되지 않은 추가 Liquid 템플릿 값을 단계 구성에서 발송 시 에이전트에 전달합니다.

이러한 컨텍스트 변수를 에이전트 지침에 Liquid 템플릿으로 포함하거나 **모든 Canvas 컨텍스트 추가**를 선택해야 합니다. 이러한 채널 중 하나를 통해 값이 전달되지 않으면 에이전트는 해당 값을 수신하지 않습니다. 필수 입력을 지침 또는 [사용 사례 전제 조건]({{site.baseurl}}/user_guide/brazeai/agents/use_cases)에 나열하고, 테스트 후 **에이전트 콘솔** > **로그**에서 입력을 확인하세요.

![지침에 Liquid가 포함된 에이전트의 세부 정보.]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:50%;"}

카탈로그 에이전트의 경우, JSON 스키마 대신 **출력** 섹션의 **필드**를 사용하세요. 해당 필드 이름과 일치하는 키-값 출력을 모델에 요청하는 지침을 작성할 수 있습니다.

프롬프트 모범 사례에 대한 자세한 내용은 다음 모델 제공업체의 가이드를 참조하세요:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gemini](https://support.google.com/a/users/answer/14200040?hl=en)

## 출력 {#outputs}

[BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator)를 사용하여 [시작 템플릿]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator)으로 에이전트를 구축한 경우, 미리 채워진 출력 스키마를 검토하고 필요에 따라 편집하세요.

### 기본 스키마 {#basic-schemas}

기본 스키마는 에이전트가 반환하는 간단한 출력입니다. 문자열, 숫자, 부울, 문자열 배열 또는 숫자 배열이 될 수 있습니다.

예를 들어, 제품을 받은 후 고객이 얼마나 만족하는지 확인하기 위해 간단한 피드백 설문조사에서 사용자 감정 점수를 수집하려면, 출력 형식을 구조화하기 위해 기본 스키마로 **숫자**를 선택할 수 있습니다.

{% alert important %}
배열은 Canvas 단계 에이전트에서만 사용할 수 있으며, 카탈로그 에이전트에서는 사용할 수 없습니다.
{% endalert %}

![기본 스키마로 숫자가 선택된 에이전트 콘솔.]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

### 고급 스키마 {#advanced-schemas}

고급 스키마 옵션에는 필드를 수동으로 구조화하거나 JSON을 사용하는 방법이 있습니다.

- **필드:** 일관되게 사용할 수 있는 에이전트 출력을 적용하는 노코드 방식입니다.
- **JSON:** 정밀한 출력 형식을 만드는 코드 접근 방식으로, JSON 스키마 내에 변수와 오브젝트를 중첩할 수 있습니다. Canvas 단계 에이전트에서만 사용할 수 있으며, 카탈로그 에이전트에서는 사용할 수 없습니다.

단일 값 출력이 아닌 구조화된 방식으로 여러 값이 정의된 데이터 구조를 에이전트가 반환하도록 하려면 고급 스키마를 사용하는 것이 좋습니다. 이렇게 하면 출력이 일관된 컨텍스트 변수로 더 잘 포맷됩니다.

### 대체 출력 {#fallback-output}

대체 값은 Canvas 단계 에이전트에서만 사용할 수 있습니다. Canvas 단계 에이전트의 에이전트 콘솔 **출력** 섹션에서 호출이 실패했을 때 Braze가 사용하는 값을 정의할 수 있습니다.

**JSON** 스키마의 경우, Braze는 스키마를 읽고 각 속성에 대한 입력 필드를 생성하여 키별로 대체 값을 설정할 수 있습니다. **필드** 스키마의 경우, 각 필드에 대한 대체 값을 입력합니다. 기본 스키마의 경우, 단일 대체 값을 입력합니다. Canvas 단계 에이전트는 대체 값에서 Liquid를 지원합니다.

설정 단계는 [대체 값 구성]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#configure-fallback-values)을 참조하세요. Canvas에서의 런타임 동작은 [오류 처리 및 대체 동작]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#fallback-behavior)을 참조하세요.

예를 들어, 사용자가 제출한 양식을 기반으로 샘플 여행 일정을 생성하는 에이전트 내에서 출력 형식을 사용할 수 있습니다. 출력 형식을 사용하면 모든 에이전트 응답이 `tripStartDate`, `tripEndDate`, `destination` 값과 함께 반환되도록 정의할 수 있습니다. 이러한 각 값은 컨텍스트 변수에서 추출하여 Liquid를 사용한 개인화를 위해 메시지 단계에 배치할 수 있습니다.

{% tabs %}
{% tab 필드 %}

레스토랑의 최신 아이스크림 맛을 추천할 가능성을 확인하기 위해 간단한 피드백 설문조사의 응답을 포맷하려면, 다음 필드를 설정하여 출력 형식을 구조화할 수 있습니다:

| 필드 이름 | 값 |
| --- | --- |
| **likelihood_score** | 숫자 |
| **explanation** | 문자열 |
| **confidence_score** | 숫자 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="고급 스키마" }

![likelihood score, explanation, confidence score에 대한 세 가지 출력 필드를 보여주는 에이전트 콘솔.]({% image_buster /assets/img/ai_agent/output_format_fields.png %}){: style="max-width:85%;"}

{% endtab %}
{% tab JSON 스키마 %}

레스토랑 체인에서의 가장 최근 식사 경험에 대한 사용자 피드백을 수집하려면, 출력 형식으로 **JSON 스키마**를 선택하고 다음 JSON을 삽입하여 감정 변수와 추론 변수를 포함하는 데이터 오브젝트를 반환할 수 있습니다.

```json
{
  "type": "object",
  "properties": {
    "sentiment": {
      "type": "string"
    },
    "reasoning": {
      "type": "string"
    }
  },
  "required": [
    "sentiment",
    "reasoning"
  ]
}
```

{% endtab %}
{% endtabs %}

## 카탈로그 및 필드 {#catalogs-and-fields}

에이전트가 참조할 특정 카탈로그를 선택하고, 관련이 있을 때 제품 및 기타 비사용자 데이터를 이해하는 데 필요한 컨텍스트를 에이전트에 제공하세요. 에이전트는 도구를 사용하여 관련 항목만 찾고, 이를 LLM에 보내 토큰 사용을 최소화합니다. 더 나은 카탈로그 검색을 위해 [지식 소스]({{site.baseurl}}/user_guide/brazeai/agents/knowledge_sources)를 생성하고 카탈로그를 직접 첨부하는 대신 에이전트 컨텍스트로 추가하세요.

![에이전트가 검색할 "restaurants" 카탈로그 및 "Loyalty_Program" 열이 선택된 화면.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:75%;"}

카탈로그 에이전트를 카탈로그 필드에 배포할 때, 필수 입력 제어를 활성화하고 에이전트가 호출되기 전에 실행에 필요한 선택된 열을 지정하세요. 에이전트는 필수 열 중 하나가 비어 있거나 누락된 경우에만 해당 행을 건너뜁니다—예를 들어, 아직 채워지지 않은 `gender` 필드가 있는 경우입니다. 선택된 열은 기본적으로 필수로 설정되지만, 실행을 차단하지 않고 비어 있을 수 있는 열은 제거할 수 있습니다. 이렇게 하면 불완전한 데이터에 대한 토큰 낭비를 방지할 수 있습니다.

카탈로그 에이전트는 입력 필드가 서로 의존하는 경우 열 순서도 준수합니다. 열 D가 열 B와 C에서 생성되어야 하는 경우, 에이전트는 해당 행에 B와 C에 값이 포함될 때까지 열 D에서 실행하지 않습니다.

배포 시나리오 및 예시는 [카탈로그 에이전트 사용]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#use-catalog-agents) 및 [카탈로그 에이전트 모범 사례]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#catalog-agent-best-practices)를 참조하세요.

## Segment 멤버십 컨텍스트 {#segment-membership-context}

에이전트가 Canvas에서 사용될 때 각 사용자의 Segment 멤버십을 교차 참조하기 위해 최대 5개의 Segment를 선택할 수 있습니다. 에이전트에 "로열티 사용자" Segment에 대한 Segment 멤버십이 선택되어 있고, 에이전트가 Canvas에서 사용된다고 가정해 보겠습니다. 사용자가 에이전트 단계에 들어가면, 에이전트는 에이전트 콘솔에서 지정한 각 Segment에 각 사용자가 멤버인지 교차 참조할 수 있으며, 각 사용자의 멤버십(또는 비멤버십)을 LLM의 컨텍스트로 사용할 수 있습니다.

![에이전트 멤버십 접근을 위해 선택된 "로열티 사용자" Segment.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:75%;"}

## 브랜드 가이드라인 {#brand-guidelines}

에이전트가 응답에서 준수해야 할 [브랜드 가이드라인]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines)을 선택할 수 있습니다. 예를 들어, 에이전트가 사용자에게 체육관 멤버십 가입을 유도하는 SMS 카피를 생성하도록 하려면, 이 필드를 사용하여 미리 정의된 대담하고 동기 부여가 되는 가이드라인을 참조할 수 있습니다.

## 사용자별 상호작용 기록 {#user-history}

사용자의 상호작용 데이터에는 최근 Campaign 및 Canvas 열람, 클릭, 전환 데이터가 포함됩니다. 예를 들어, Canvas에서 평가될 때 에이전트가 참조할 수 있도록 이 컨텍스트를 포함할 수 있습니다. 사용자별 상호작용 기록은 에이전트가 개인화된 메시지 카피를 작성하는 역할을 할 때도 영향을 줄 수 있습니다.

## 버전 기록 {#version-history}

에이전트 콘솔은 에이전트 변경 사항을 저장할 때마다 새 버전을 기록합니다. **버전 기록** 탭에는 저장된 모든 버전과 저장 간의 편집 내용이 나열됩니다.

1. 에이전트 콘솔에서 에이전트를 엽니다.
2. **버전 기록** 탭을 선택합니다.
3. 구성을 검토할 버전을 선택합니다.

버전에서 변경된 내용을 확인하려면 **보기**를 선택하세요. Braze는 추가 및 삭제를 강조 표시하는 코드 스타일 인라인 diff를 표시합니다. 삭제된 콘텐츠는 빨간색 취소선 스타일로 표시됩니다.

이전 버전의 지침을 복원해야 하는 경우, 해당 버전의 **보기**를 열고 지침 텍스트를 복사한 다음 현재 **지침** 필드에 붙여넣으세요.

{% alert tip %}
인라인 diff 보기에서 <kbd>⌘</kbd> + <kbd>A</kbd>(macOS) 또는 <kbd>Ctrl</kbd> + <kbd>A</kbd>(Windows)를 눌러 빨간색 삭제 마크업 없이 모든 지침을 선택하면 깨끗한 텍스트를 복사하여 복원할 수 있습니다.
{% endalert %}

## 에이전트 복제 {#duplicate-agents}

에이전트를 복제하여 원본과 나란히 개선 사항이나 반복을 테스트할 수 있습니다. [버전 기록](#version-history)을 사용하여 이전 구성을 검토하거나 복원하세요. 에이전트를 복제하려면:

1. 에이전트의 행 위에 마우스를 올리고 <i class="fas fa-ellipsis-vertical"></i> 메뉴를 선택합니다.
2. **복제**를 선택합니다.

## 에이전트 아카이브 {#archive-agents}

더 많은 커스텀 에이전트를 생성함에 따라, 활발히 사용되지 않는 에이전트를 아카이브하여 **에이전트 관리** 페이지를 정리할 수 있습니다. 에이전트를 아카이브하려면:

1. 에이전트의 행 위에 마우스를 올리고 <i class="fas fa-ellipsis-vertical"></i> 메뉴를 선택합니다.
2. **아카이브**를 선택합니다.