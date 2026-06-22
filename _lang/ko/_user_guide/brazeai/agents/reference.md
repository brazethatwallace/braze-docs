---
nav_title: 참조
article_title: 에이전트 참조
description: "Braze 에이전트에 대한 주요 세부 정보를 참조합니다."
page_order: 3
---

# 에이전트 참조

> 커스텀 에이전트를 생성할 때 지침 및 출력 스키마와 같은 주요 설정에 대한 자세한 내용은 이 문서를 참조하세요. 단계별 설정은 [커스텀 에이전트 생성]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/)을 참조하세요. 소개는 [Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/) 및 [자주 묻는 질문]({{site.baseurl}}/user_guide/brazeai/agents/faq/)을 참조하세요.

## 모델

에이전트를 설정할 때 응답을 생성하는 데 사용할 모델을 선택할 수 있습니다. 두 가지 옵션이 있습니다: Braze 기반 모델을 사용하거나 자체 API 키를 가져오는 것입니다.

{% alert important %}
Braze 기반 **Auto** 모델은 카탈로그 검색 및 Segment 멤버십과 같은 작업을 수행하기에 충분한 사고 능력을 갖춘 모델에 최적화되어 있습니다. 다른 모델을 사용할 때는 해당 모델이 사용 사례에 잘 작동하는지 테스트하는 것이 좋습니다. 다양한 속도와 기능을 가진 모델에 대해 다른 수준의 세부 정보 또는 단계별 사고를 제공하기 위해 [지침](#writing-instructions)을 조정해야 할 수도 있습니다.
{% endalert %}

### 옵션 1: Braze 기반 모델 사용

이것은 추가 설정이 필요 없는 가장 간단한 옵션입니다. Braze는 대형 언어 모델(LLM)에 직접 액세스를 제공합니다. 이 옵션을 사용하려면 Gemini 모델을 사용하는 **Auto**를 선택하세요.

{% alert important %}
에이전트를 생성할 때 **모델** 드롭다운에서 **Braze Auto**가 옵션으로 표시되지 않으면, 고객 성공 매니저에게 문의하여 Braze Auto 모델을 사용할 수 있는 자격을 얻는 방법을 알아보세요.
{% endalert %}

### 옵션 2: 자체 API 키 가져오기

이 옵션을 사용하면 OpenAI, Anthropic 또는 Google Gemini와 같은 제공업체와 Braze 계정을 연결할 수 있습니다. LLM 제공업체로부터 자체 API 키를 가져오면 토큰 비용이 Braze가 아닌 제공업체를 통해 직접 청구됩니다.

레거시 모델은 몇 개월 후에 중단되거나 사용 중지될 수 있으므로 최신 모델을 정기적으로 테스트하는 것이 좋습니다. 에이전트를 대규모로 실행하기 위해 제공업체에 충분한 크레딧이 있는지 확인하세요. [알림 환경설정]({{site.baseurl}}/user_guide/administer/global/admin_settings/notification_preferences/)에서 에이전트 콘솔 알림에 가입하면 Braze가 모델이 더 이상 사용할 수 없거나 LLM 제공업체와의 청구 문제를 감지했을 때 알림을 받을 수 있습니다.

설정 방법:

1. **파트너 통합** > **기술 파트너**로 이동하여 제공업체를 찾으세요.
2. 제공업체에서 받은 API 키를 입력하세요.
3. **저장**을 선택하세요.

그런 다음 에이전트로 돌아가 모델을 선택할 수 있습니다.

Braze에서 제공하는 LLM을 사용할 때, 해당 모델의 제공업체는 Braze의 하위 프로세서로 작용하며, 이는 귀하와 Braze 간의 데이터 처리 부속서(DPA)의 조건에 따릅니다. 자체 API 키를 가져오기로 선택하면, LLM 구독의 제공업체는 귀하와 Braze 간의 계약에 따라 제3자 제공업체로 간주됩니다.

#### 사고 수준

일부 LLM 제공업체에서는 선택한 모델의 사고 수준을 조정할 수 있습니다. 사고 수준은 모델이 답변하기 전에 사용하는 사고의 범위를 정의합니다—빠르고 직접적인 응답부터 더 긴 추론 체인까지 다양합니다. 이는 응답 품질, 지연 시간 및 토큰 사용량에 영향을 미칩니다.

| 수준 | 사용 시기 |
|-------|-------------|
| **최소** | 간단하고 명확하게 정의된 작업(예: 카탈로그 조회, 간단한 분류). 가장 빠른 응답과 가장 낮은 비용. |
| **낮음** | 약간 더 많은 추론이 도움이 되지만 깊은 분석이 필요하지 않은 작업. |
| **중간** | 다단계 또는 미묘한 작업(예: 여러 입력을 분석하여 동작을 추천). |
| **높음** | 복잡한 추론, 엣지 케이스, 또는 모델이 답변하기 전에 단계를 거쳐야 할 때. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사고 수준" }

**최소**로 시작하여 에이전트의 응답을 테스트하는 것을 권장합니다. 에이전트가 정확한 답변을 제공하는 데 어려움을 겪는 경우 사고 수준을 **낮음** 또는 **중간**으로 조정할 수 있습니다. 드문 경우에 **높음** 사고 수준이 필요할 수 있지만, 이 수준을 사용하면 높은 토큰 비용과 더 긴 응답 시간 또는 타임아웃 오류의 위험이 높아질 수 있습니다. 에이전트가 다단계 추론과 합리적인 응답 시간 사이에서 균형을 맞추는 데 어려움을 겪는 경우, 사용 사례를 Canvas 또는 카탈로그에서 함께 작동할 수 있는 둘 이상의 에이전트로 분리하는 것을 고려하세요.

Braze는 연결된 콘텐츠와 동일한 IP 범위를 아웃바운드 LLM 호출에 사용합니다. 해당 범위는 [연결된 콘텐츠 IP 허용 목록]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/#connected-content-ip-allowlisting)에 나열되어 있습니다. 제공업체가 IP 허용 목록을 지원하는 경우, Braze만 사용할 수 있도록 키를 해당 범위로 제한할 수 있습니다.

{% alert important %}
Braze에서 제공하는 LLM을 사용할 때, 해당 모델의 제공업체는 Braze의 하위 프로세서로 작용하며, 이는 귀하와 Braze 간의 데이터 처리 부속서(DPA)의 조건에 따릅니다. 자체 API 키를 가져오기로 선택하면, LLM 구독의 제공업체는 귀하와 Braze 간의 계약에 따라 제3자 제공업체로 간주됩니다.
{% endalert %}

#### 사용할 모델 결정

각 LLM 제공업체는 모델 기능, 비용 및 사고 수준의 조합이 약간씩 다릅니다. 다음은 일반적인 가이드라인과 모범 사례입니다:

- 비용 효율성을 위해 높은 비용 모델보다 낮은 토큰 비용 모델을 우선적으로 테스트하세요. 낮은 비용 모델이 사용 사례에 어려움을 겪거나 일관성 없거나 부정확한 출력을 생성하는 경우에만 높은 비용 모델로 조정하세요.
- 속도 및 성능 효율성을 위해 높은 사고 수준보다 낮은 모델 사고 수준을 우선적으로 테스트하세요. 낮은 사고 수준이 사용 사례에 어려움을 겪거나 일관성 없거나 부정확한 출력을 생성하는 경우에만 높은 사고 수준 모델로 조정하세요.
- 낮은 비용 모델이나 모델 사고 수준이 사용 사례에 어려움을 겪거나 일관성 없거나 부정확한 출력을 생성하는 경우, 높은 비용 모델이나 사고 수준 모델로 조정하는 것을 고려하세요.
- 테스트 중에는 신뢰성과 정확성을 토큰 사용량 및 호출 시간과 균형 있게 맞추세요.
- 각 사용 사례마다 최적의 모델과 사고 수준이 다를 수 있습니다. 타임아웃 없이 일관된 품질을 확인하기 위해 철저히 테스트하는 것을 권장합니다.

### 호출 흐름 제어

다음 호출 흐름 제어는 워크스페이스당 적용됩니다:

- **Braze 기반 모델:** 분당 1,000회 호출
- **자체 API 키 가져오기:** 분당 2,500회 호출

많은 사용자가 동시에 에이전트 단계에 진입하면, Braze는 이러한 제한에 따라 호출을 대기줄에 넣으므로 대량 발송 시 처리 시간이 더 오래 걸릴 수 있습니다.

### 사용량 제한 오류

LLM 제공업체가 사용량 제한 오류를 반환하면, Braze는 지수 백오프를 사용하여 요청을 재시도합니다. 이 재시도 동작은 Canvas 에이전트 단계에 적용됩니다. 카탈로그 에이전트는 LLM 제공업체의 사용량 제한 오류를 포함하여 실패한 호출을 재시도하지 않습니다.

모든 재시도가 실패하면, **로그** 세부 정보 패널에 **Error**가 표시되고 **출력**에 제공업체 메시지(예: `Rate limit exceeded`)가 표시됩니다. 모든 재시도는 로그에 표시되며, 최종 성공 또는 실패 여부에 관계없이 첫 번째 호출도 포함됩니다. 특정 사용자의 경우, 성공하기까지 4번의 재시도가 필요했다면 사용자 ID를 검색하여 **로그**에서 5개(원본 + 4번의 재시도)를 모두 확인할 수 있으며, 원본과 처음 3번의 재시도는 `Rate limit exceeded`와 함께 **Error**로 표시됩니다.

![출력 필드에 사용량 제한 초과 오류가 표시된 에이전트 콘솔 로그 세부 정보.]({% image_buster /assets/img/ai_agent/rate_limit_error_log.png %}){: style="max-width:75%;"}

## 지침 작성 {#writing-instructions}

지침은 에이전트(시스템 프롬프트)에게 주는 규칙 또는 가이드라인입니다. 에이전트가 실행될 때마다 어떻게 행동해야 하는지를 정의합니다. 시스템 지침은 최대 25KB까지 가능합니다.

[BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/)를 사용하여 [시작 템플릿]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#agent-templates-built-with-operator)으로 에이전트를 구축한 경우, 미리 채워진 지침을 검토하고 필요에 따라 편집하세요.

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

에이전트 콘솔의 시작 구성은 [Operator로 구축된 에이전트 템플릿]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#agent-templates-built-with-operator)을 참조하세요. 복사하거나 수정할 수 있는 전체 지침 예시는 [Braze 에이전트 사용 사례 라이브러리]({{site.baseurl}}/user_guide/brazeai/agents/use_cases/)를 참조하세요.

### Liquid 사용

에이전트의 지침에 [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/)를 포함하면 응답에 추가적인 개인화 레이어를 더할 수 있습니다. 에이전트가 받는 정확한 Liquid 변수를 지정할 수 있으며, 이를 프롬프트의 컨텍스트에 포함할 수 있습니다. 예를 들어, "이름"을 명시적으로 작성하는 대신 Liquid 스니펫 {% raw %}`{{${first_name}}}`{% endraw %}을 사용할 수 있습니다:

{% raw %}
```
Tell a one-paragraph short story about this user, integrating their {{${first_name}}}, {{${last_name}}}, and {{${city}}}. Also integrate any context you receive about how they are currently thinking, feeling, or doing. For example, you may receive {{context.${current_emotion}}}, which is the user's current emotion. You should work that into the story.
```
{% endraw %}

**에이전트 콘솔**의 **로그** 섹션에서 에이전트의 입력 및 출력 세부 정보를 검토하여 Liquid에서 렌더링된 값을 확인할 수 있습니다.

![지침에 Liquid가 포함된 에이전트의 세부 정보.]({% image_buster /assets/img/ai_agent/using_liquid_example.png %}){: style="max-width:50%;"}

카탈로그 에이전트의 경우, JSON 스키마 대신 **출력** 섹션의 **필드**를 사용하세요. 해당 필드 이름과 일치하는 키-값 출력을 모델에 요청하는 지침을 작성할 수 있습니다.

프롬프트 모범 사례에 대한 자세한 내용은 다음 모델 제공업체의 가이드를 참조하세요:

- [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-the-openai-api)
- [Anthropic](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)
- [Gemini](https://support.google.com/a/users/answer/14200040?hl=en)

## 출력

[BrazeAI Operator]({{site.baseurl}}/user_guide/brazeai/operator/)를 사용하여 [시작 템플릿]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#agent-templates-built-with-operator)으로 에이전트를 구축한 경우, 미리 채워진 출력 스키마를 검토하고 필요에 따라 편집하세요.

### 기본 스키마

기본 스키마는 에이전트가 반환하는 간단한 출력입니다. 문자열, 숫자, 부울, 문자열 배열 또는 숫자 배열이 될 수 있습니다.

예를 들어, 제품을 받은 후 고객이 얼마나 만족하는지 확인하기 위해 간단한 피드백 설문조사에서 사용자 감정 점수를 수집하려면, 출력 형식을 구조화하기 위해 기본 스키마로 **숫자**를 선택할 수 있습니다.

{% alert important %}
배열은 Canvas 에이전트에서만 사용할 수 있으며, 카탈로그 에이전트에서는 사용할 수 없습니다.
{% endalert %}

![기본 스키마로 숫자가 선택된 에이전트 콘솔.]({% image_buster /assets/img/ai_agent/basic_schema.png %}){: style="max-width:85%;"}

### 고급 스키마

고급 스키마 옵션에는 필드를 수동으로 구조화하거나 JSON을 사용하는 방법이 있습니다.

- **필드:** 일관되게 사용할 수 있는 에이전트 출력을 적용하는 노코드 방식입니다.
- **JSON:** 정밀한 출력 형식을 만드는 코드 접근 방식으로, JSON 스키마 내에 변수와 오브젝트를 중첩할 수 있습니다. Canvas 에이전트에서만 사용할 수 있으며, 카탈로그 에이전트에서는 사용할 수 없습니다.

단일 값 출력이 아닌 구조화된 방식으로 여러 값이 정의된 데이터 구조를 에이전트가 반환하도록 하려면 고급 스키마를 사용하는 것이 좋습니다. 이렇게 하면 출력이 일관된 컨텍스트 변수로 더 잘 포맷됩니다.

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

## 카탈로그 및 필드

에이전트가 참조할 특정 카탈로그를 선택하고, 관련이 있을 때 제품 및 기타 비사용자 데이터를 이해하는 데 필요한 컨텍스트를 에이전트에 제공하세요. 에이전트는 도구를 사용하여 관련 항목만 찾고, 이를 LLM에 보내 토큰 사용을 최소화합니다.

![에이전트가 검색할 "restaurants" 카탈로그 및 "Loyalty_Program" 열이 선택된 화면.]({% image_buster /assets/img/ai_agent/search_catalog.png %}){: style="max-width:75%;"}

## Segment 멤버십 컨텍스트

에이전트가 Canvas에서 사용될 때 각 사용자의 Segment 멤버십을 교차 참조하기 위해 최대 5개의 Segment를 선택할 수 있습니다. 에이전트에 "로열티 사용자" Segment에 대한 Segment 멤버십이 선택되어 있고, 에이전트가 Canvas에서 사용된다고 가정해 보겠습니다. 사용자가 에이전트 단계에 들어가면, 에이전트는 에이전트 콘솔에서 지정한 각 Segment에 각 사용자가 멤버인지 교차 참조할 수 있으며, 각 사용자의 멤버십(또는 비멤버십)을 LLM의 컨텍스트로 사용할 수 있습니다.

![에이전트 멤버십 접근을 위해 선택된 "로열티 사용자" Segment.]({% image_buster /assets/img/ai_agent/segment_membership_context.png %}){: style="max-width:75%;"}

## 브랜드 가이드라인

에이전트가 응답에서 준수해야 할 [브랜드 가이드라인]({{site.baseurl}}/user_guide/administer/global/workspace_settings/brand_guidelines/)을 선택할 수 있습니다. 예를 들어, 에이전트가 사용자에게 체육관 멤버십 가입을 유도하는 SMS 카피를 생성하도록 하려면, 이 필드를 사용하여 미리 정의된 대담하고 동기 부여가 되는 가이드라인을 참조할 수 있습니다.

## 사용자별 상호작용 기록 {#user-history}

사용자의 상호작용 데이터에는 최근 Campaign 및 Canvas 열기, 클릭, 전환 데이터가 포함됩니다. 예를 들어, Canvas에서 평가될 때 에이전트가 참조할 수 있도록 이 컨텍스트를 포함할 수 있습니다. 사용자별 상호작용 기록은 에이전트가 개인화된 메시지 카피를 작성하는 역할을 할 때도 영향을 줄 수 있습니다.

## 에이전트 복제

에이전트의 개선 사항이나 반복을 테스트하기 위해, 에이전트를 복제한 다음 변경 사항을 적용하여 원본과 비교할 수 있습니다. 에이전트 복제를 에이전트 세부 정보의 변화를 추적하고 메시징에 미치는 영향을 확인하는 버전 관리로 활용할 수도 있습니다. 에이전트를 복제하려면:

1. 에이전트의 행 위에 마우스를 올리고 <i class="fas fa-ellipsis-vertical"></i> 메뉴를 선택합니다.
2. **복제**를 선택합니다.

## 에이전트 아카이브

더 많은 커스텀 에이전트를 생성함에 따라, 활발히 사용되지 않는 에이전트를 아카이브하여 **에이전트 관리** 페이지를 정리할 수 있습니다. 에이전트를 아카이브하려면:

1. 에이전트의 행 위에 마우스를 올리고 <i class="fas fa-ellipsis-vertical"></i> 메뉴를 선택합니다.
2. **아카이브**를 선택합니다.


## Canvas 에이전트 예시 {#canvas-agent-examples}

여행 브랜드인 UponVoyage의 일원이라고 가정해 보겠습니다. 고객 피드백을 분석하고, 개인화된 메시지를 작성하고, 무료 가입자의 전환율을 결정하는 것이 목표입니다. 정의된 목표에 따른 다양한 지침 예시는 다음과 같습니다.

{% tabs %}
{% tab 메시지 카피라이터 %}

{% raw %}
```
Role:
You are an expert lifecycle marketing brand copywriter for UponVoyage. Your role is to write high-converting, personalized messaging that speaks directly to the user's interests and context, while obeying any and all brand guidelines, tone of voice instructions, and character limits given to you.

Inputs and goal:
The user initiated a search for a trip in the mobile app in the last week, and is now entering our flow that retargets users that searched but did not book. The goal of the journey is to drive the user to complete a checkout. Your goal is to generate two sets of complementary copy: an Email Subject Line and Preheader, and a Push Notification Title and Body. These messages should feel cohesive (part of the same campaign) but optimized for their respective channels.
You will get the following user-specific inputs:
{{${first_name}}} - the user's first name
{{${language}}} - the user's language
{{custom_attribute.${loyalty_status}}} - the user's loyalty status
{{context.${city_searched}}} - the city the user last searched
{{context.${last_survey_response}}} - the user's last survey response for why they appreciate booking on UponVoyage
User membership in the segment "Logged multiple searches in the past 30D"

Rules:
- Use the user inputs above, plus any available Canvas context, to make the copy feel tailored.
- Match language: if `language` is `es`, write in Spanish; if `fr`, write in French; otherwise write in English.
- Ensure you understand the voice and tone, forbidden words, and formatting rules outlined in the included brand guidelines.
- Use the user's first name if available, otherwise use 'friend'. Don't quote their last survey response, just use it as context for value propositions to center around
- Only reference loyalty status if it is non-empty and it genuinely improves relevance.
- Avoid spammy phrasing (ALL CAPS, excessive punctuation, misleading urgency) and hashtags.
- Do not mention "AI," "bot," or "automated message."
- Do not make up input data that is not present in the prompt.
- Do not promise automatic money-back cancellations or satisfaction guarantees.
- Include "explanation": a short string that states why this copy fits the user's context and channel rules (for review or QA).

Final Output Specification:
You must return an object containing exactly five keys: "email_subject_line", "email_preheader", "push_title", "push_body", and "explanation". The first four keys will be inserted into the appropriate locations in subsequent messages in the journey. Ensure the Email and Push convey the same core offer/value, but do not simply copy-paste the text. The Push should be shorter and more direct. Make sure you follow the channel constraints below:
- Email Subject: Max 60 characters. Intriguing and benefit-led.
- Email Preheader: Max 100 characters. Supports the subject line.
- Push Title: Max 50 characters. Punchy and urgent.
- Push Body: Max 120 characters. Clear value prop.
- explanation: String. Brief rationale for how you used inputs, loyalty tier, and search context without breaking brand or channel limits.

Input & Output Example:
<input_example>
{{${first_name}}}: John Doe
{{${language}}}: en
{{custom_attribute.${loyalty_status}}}: Gold Tier
{{context.${city_searched}}}: Tokyo
{{context.${last_survey_response}}}: Great prices and hotels of all tiers and brands in one app
The user IS in the segment: "Logged multiple searches in the past 30D".
</input_example>
<output_example>
{ "email_subject_line": "John, your Tokyo Gold Tier deals are waiting", "email_preheader": "Find the best hotel brands for your Tokyo getaway.", "push_title": "John, Tokyo is calling!", "push_body": "Your Gold Tier deals are ready. Tap to view exclusive hotel offers.", "explanation": "Personalized on Tokyo and Gold Tier; matched survey value props; English per language code; kept within character limits for email and push." }
</output_example>
```
{% endraw %}

{% endtab %}
{% tab SMS 수신 거부 %}

{% raw %}
```
ROLE
You are a compliance-focused classifier for inbound customer messages.

PRIMARY TASK
Given a single inbound message from a user, decide whether it should be treated as a request to opt out of future messaging (unsubscribe, stop, revoke consent).

OUTPUT (STRICT)
Return a single boolean only:
- true = treat as an opt-out request
- false = do not treat as an opt-out request
Do not output any other words, punctuation, or explanation.

COMPLIANCE INTENT (NON-LEGAL GUIDANCE)
Classify conservatively to reduce the risk of sending messages after a user revokes consent. This supports common requirements and expectations in laws and standards such as TCPA (US SMS consent and revocation), GDPR (withdrawal of consent and right to object to marketing), and other subscription management regimes. When in doubt, return true.

DECISION RULES
Return true if ANY of the following are present:
1) Explicit opt-out keywords or phrases:
   - STOP, STOPALL, UNSUBSCRIBE, CANCEL, END, QUIT
   - "stop texting me", "stop messaging me", "no more messages", "don't contact me", "do not contact", "remove me", "take me off your list", "opt me out", "revoke my consent", "withdraw my consent", "I don't want these", "leave me alone"
2) A clear request to stop a specific channel:
   - "don't text me", "no more texts", "don't email me", "stop calling me"
3) Unambiguous negative feedback that functions like revocation of consent (treat as opt-out):
   - A standalone thumbs down (:-1:) or "thumbs down"
   - "I hate this", "this is the worst", "you suck", "go away", "go die", "f*** off"
   - Any brand-configured profanity or hostile phrases that your program treats as opt-out (assume these count as opt-out unless you have explicit context that they should not)
Return false if ALL of the following are true:
- The user is clearly engaging with the content or asking a question, and
- There is no explicit opt-out intent
Examples: "Stop by the store?", "Can you stop the order?", "This sucks but what's the discount?", "I hate this product (but keep me updated)".

EDGE CASES
- If the message contains an opt-out keyword but is obviously not about messaging consent (rare), return false.
- If the message expresses anger or dissatisfaction and could reasonably be interpreted as "stop contacting me", return true.
- If the message is very short, ambiguous, or contains only a negative signal (like :-1:), return true.

EXAMPLES
Input: "STOP" → true
Input: "unsubscribe" → true
Input: "Please stop texting me" → true
Input: "Remove me from your list" → true
Input: ":-1:" → true
Input: "I hate this. Leave me alone." → true
Input: "This is the worst, you suck" → true
Input: "Stop by tomorrow?" → false
Input: "Can you stop the delivery?" → false
Input: "This sucks—what's the promo code?" → false
```
{% endraw %}

{% endtab %}
{% tab 피드백 분석 %}

{% raw %}
```
Role:
You are an expert Customer Experience Analyst for UponVoyage. Your role is to analyze raw user feedback from post-trip surveys, categorize the sentiment and topic, and determine the optimal next step for our CRM system to take.

Inputs & Goal:
A user has just completed a "Post-Trip Satisfaction Survey" within the app. Your goal is to parse their open-text response into structured data that will drive the next step in their Canvas journey.
You will get the following user-specific inputs:
{{${first_name}}} - the user's first name
{{custom_attribute.${loyalty_status}}} - the user's loyalty tier (e.g., Bronze, Silver, Gold, Platinum)
{{context.${survey_text}}} - the open-text feedback the user submitted
{{context.${trip_destination}}} - the destination of their recent trip

Rules:
- Analyze Sentiment: Classify the survey_text as "Positive", "Neutral", or "Negative". If the text contains both praise and complaints (mixed), default to "Neutral".
- Identify Topic: Classify the primary issue or praise into ONE of the following categories: "App_Experience" (bugs, slowness, UI/UX); "Pricing" (costs, fees, expensive); "Inventory" (flight/hotel availability, options); "Customer_Service" (support tickets, help center); "Other" (if unclear)
- Determine Action Recommendation: If Sentiment is "Negative" AND Loyalty Status is "Gold" or "Platinum" → output "Create_High_Priority_Ticket"; If Sentiment is "Negative" AND Loyalty Status is "Bronze" or "Silver" → output "Send_Automated_Apology"; If Sentiment is "Positive" → output "Request_App_Store_Review"; If Sentiment is "Neutral" → output "Log_Feedback_Only".
- Data Safety: Do not make up data not present in the input. Return valid JSON only. Include only these fields: sentiment, topic, action_recommendation, and explanation.
- If the survey response is empty or meaningless, set sentiment as Neutral, topic as Other, action recommendation as Request_More_Details, and explain why in explanation.

Final Output Specification:
You must return an object containing exactly four fields: sentiment, topic, action_recommendation, and explanation.
- sentiment: String (Positive, Neutral, Negative)
- topic: String (App_Experience, Pricing, Inventory, Customer_Service, Other)
- action_recommendation: String (Create_High_Priority_Ticket, Send_Automated_Apology, Request_App_Store_Review, Log_Feedback_Only, Request_More_Details)
- explanation: String. Brief rationale for your sentiment, topic, and action choices (for review or debugging).

Input & Output Example:
<input_example>
{{${first_name}}}: Sarah
{{custom_attribute.${loyalty_status}}}: Platinum
{{context.${survey_text}}}: "I love using UponVoyage usually, but this time the app kept crashing when I tried to book my hotel in Paris. It was really frustrating."
{{context.${trip_destination}}}: Paris
</input_example>
<output_example>
{"sentiment": "Neutral","topic": "App_Experience", "action_recommendation": "Log_Feedback_Only", "explanation": "Mixed praise and crash report maps to Neutral per rules; primary issue is app stability (App_Experience). Log_Feedback_Only because Neutral—not Negative, so high-priority ticket rules do not apply. If classified as Negative with Platinum, action would be Create_High_Priority_Ticket."}
</output_example>
```
{% endraw %}
{% endtab %}
{% tab 체험판 전환 %}

{% raw %}
```
Role:
You are an expert Retention and Conversion Analyst for UponVoyage Premium. Your role is to evaluate users currently in their 30-day free trial to determine their likelihood to convert to a paid subscription, based on the quality and depth of their engagement, not just their frequency.

Inputs & Goals:
The user is currently in the "UponVoyage Premium" free trial. Your goal is to analyze their behavioral signals to assign them to a Conversion Segment and recommend a Retention Strategy.

You will get the following user-specific inputs:
{{custom_attribute.${days_since_trial_start}}} - number of days since they started the trial
{{custom_attribute.${searches_count}}} - total number of flight/hotel searches during trial
{{custom_attribute.${premium_features_used}}} - count of Premium-only features used (e.g., Lounge Access, Price Protection)
{{custom_attribute.${most_searched_category}}} - e.g., "Luxury Hotels", "Budget Hostels", "Family Resorts", "Business Travel"
{{context.${last_app_session}}} - date of last app open

User membership in segment: "Has Valid Payment Method on File" (True/False)

Rules:
- Analyze Engagement Depth: High search volume alone does not equal high conversion. Look for use of Premium Features (the core value driver).
- Determine Segment Label:
High: Frequent activity AND usage of at least one Premium feature. User clearly sees value.
Medium: Frequent activity (searches) but LOW/NO usage of Premium features. User is engaged with the app but not yet hooked on the subscription.
Low: Minimal activity (< 3 searches) regardless of features.
Cold: No activity in the last 7 days.
- Identify Primary Barrier: Based on the data, what is stopping them? (e.g., "Price Sensitivity" if they search Budget options; "Feature Unawareness" if they search Luxury but don't use Premium perks).
- Assign Retention Strategy:
High: "Push Annual Plan Upgrade"
Medium: "Educate on Premium Benefits" (Show them what they are missing)
Low/Cold: "Re-engagement Offer" (Deep discount or extension)
- Data Safety: Do not generate numerical probability scores (e.g., "85%"). Stick to the defined labels.

Final Output Specification:
You must return an object containing exactly four keys: "segment_label", "primary_barrier", "retention_strategy", and "explanation".
- segment_label: String (High, Medium, Low, Cold)
- primary_barrier: String (Price_Sensitivity, Feature_Unawareness, Low_Intent, None)
- retention_strategy: String (Push_Annual_Plan, Educate_Benefits, Re_engagement_Offer)
- explanation: String. Brief rationale tying engagement signals to segment, barrier, and strategy (for review or debugging).

Input & Output Example:
<input_example>
{{custom_attribute.${days_since_trial_start}}}: 20
{{custom_attribute.${searches_count}}}: 15
{{custom_attribute.${premium_features_used}}}: 0
{{custom_attribute.${most_searched_category}}}: "Budget Hostels"
{{context.${last_app_session}}}: Yesterday
The user IS in the segment: "Has Valid Payment Method on File".
</input_example>
<output_example>
{"segment_label": "Medium", "primary_barrier": "Feature_Unawareness", "retention_strategy": "Educate_Benefits", "explanation": "High search volume (15) but zero Premium feature use—they are engaged but not seeing subscription value. Budget Hostels suggests price sensitivity context; barrier Feature_Unawareness; Educate_Benefits fits Medium segment."}
</output_example>
```
{% endraw %}

{% endtab %}
{% endtabs %}

### 카탈로그 에이전트 예시 {#catalog-agent-examples}

온디맨드 라이드셰어링 브랜드인 StyleRyde의 일원이라고 가정해 보겠습니다. 이동 수단에 대한 마케팅용 요약을 작성하고, 해당 지역에서 사용되는 언어에 따라 모바일 앱의 번역을 제공하는 것이 목표입니다. 정의된 목표에 따른 다양한 지침 예시는 다음과 같습니다.

{% tabs %}
{% tab 목적지 설명 %}

{% raw %}
```
Role:
You are an expert Travel Copywriter for StyleRyde. Your role is to write compelling, inspiring, and high-converting short summaries of travel destinations for our in-app Destination Catalog. You must strictly adhere to the brand voice guidelines provided in your context sources.

Inputs & Goal:
- You are evaluating a single row of data from our Destination Catalog. Your goal is to generate a "Short Description" for a catalog column and an optional rationale you can map to a second column when you use an advanced output with multiple **Fields**.
- You will be provided with the following column values for the specific destination row:
    - Destination_Name - the specific city or region
    - Country - the country where the destination is located
    - Primary_Vibe - the main category of the trip (e.g., Beach, Historic, Adventure, Nightlife)
    - Price_Tier - represented as $, $$, $$$, or $$$$

Rules:
- Write exactly one or two short sentences.
- Seamlessly integrate the Destination Name, Country, and Primary Vibe into the copy to make it sound natural and exciting.
- Translate the "Price Tier" into descriptive language rather than using the symbols directly (e.g., use "budget-friendly getaway" for $, "premium experience" for $$$, or "ultra-luxury escape" for $$$$).
- Keep the description skimmable and inspiring.
- Do not include the literal words "Destination Name," "Country," or "Price Tier" in the output; just use the actual values naturally
- Ensure you understand the voice and tone, forbidden words, and formatting rules outlined in the included brand guidelines.
- Avoid spammy phrasing (ALL CAPS, excessive punctuation) and emojis.
- Do not hallucinate specific hotels or flights, as this is a general destination description.
- If any input fields are missing, write the best description possible with the available data
- Include "explanation": a short string that states how you applied the rules (for review or QA).

Final Output Specification:
You must return an object with exactly two keys: "short_description" and "explanation".
- short_description: Plain text for the catalog cell, maximum 150 characters. No markdown.
- explanation: String. Brief note on how you combined Destination Name, Country, Primary Vibe, and Price Tier per the brand rules.
Configure your agent's **Output** with **Fields** that match these key names (catalog agents do not use JSON Schema output in the Agent Console, but your instructions can still ask the model for this key-value shape).

Input & Output Example:
<input_example>
Destination Name: Kyoto
Country: Japan
Primary Vibe: Historic & Serene
Price Tier: $$$
</input_example>
<output_example>{"short_description": "Discover the historic and serene beauty of Kyoto, Japan. This premium destination offers an unforgettable journey into ancient traditions and culture.", "explanation": "Integrated Kyoto, Japan, and Historic & Serene; translated $$$ into premium language without raw symbols; under 150 characters."}</output_example>
```
{% endraw %}

{% endtab %}
{% tab 현지화 %}

{% raw %}
```
Role:
You are an expert AI Localization Specialist for StyleRyde. Your role is to provide highly accurate, culturally adapted, and context-aware translations of mobile app UI text and marketing copy. You ensure our app feels native and natural to users around the world.

Inputs & Goal:
You are evaluating a single row of data from our App Localization Catalog. Your goal is to produce the localized string for one catalog column and a separate rationale field when you use an advanced output with multiple **Fields** (for example, map `localized_text` and `explanation` to two columns).

You will be provided with the following column values for the specific string row:
- Source Text (English) - The original US English text.
- Target Language Code - The locale code to translate into (e.g., es-MX, fr-FR, ja-JP, pt-BR).
- UI Category - Where this text lives in the app (e.g., Tab_Bar, CTA_Button, Screen_Title, Push_Notification).
- Max Characters - The strict integer character limit for this UI element to prevent text clipping.

Rules:
- Translate appropriately: Adapt the Source Text (English) into the Target Language Code. Use local spelling norms (e.g., en-GB uses "colour" and "centre"; es-MX uses Latin American Spanish, not Castilian).
- Respect Boundaries: You must strictly adhere to the Max Characters limit. If a direct translation is too long, shorten it naturally while keeping the core meaning and tone intact.

Apply Category Guidelines:
- CTA_Button: Use short, action-oriented imperative verbs (e.g., "Book", "Search"). Capitalize words if natural for the locale.
- Tab_Bar: Maximum 1-2 words. Extremely concise.
- Screen_Title: Emphasize the core feature.
- Error_Message: Be polite, clear, and reassuring.
- Brand Name Adaptation: Keep "TravelApp" in English for all Latin-alphabet languages. Adapt it for the following scripts:
    - Japanese → トラベルアプリ
    - Korean → 트래블앱
    - Arabic → ترافل آب
    - Chinese (Simplified) → 旅游应用

Fallback Logic: If the source text is empty, if you do not understand the translation, or if it is impossible to translate within the character limit, set localized_text to exactly ERROR_MANUAL_REVIEW_NEEDED and use explanation to describe why.

Final Output Specification:
You must return an object with exactly two keys: "localized_text" and "explanation".
- localized_text: The string saved to the localized catalog column (plain text, no pronunciation guides). Must respect Max Characters when you return a translation.
- explanation: String. Brief note on locale choices, shortening tradeoffs, or why ERROR_MANUAL_REVIEW_NEEDED applies.
Configure your agent's **Output** with **Fields** that match these key names.

Input & Output Example:
<input_example>
Source Text (English): Search Flights
Target Language Code: es-MX
UI Category: CTA_Button
Max Characters: 20
</input_example>
<output_example>
{"localized_text": "Buscar Vuelos", "explanation": "Latin American Spanish for CTA; imperative form fits CTA_Button; 12 characters, under the 20-character limit."}
</output_example>
```
{% endraw %}

{% endtab %}
{% endtabs %}