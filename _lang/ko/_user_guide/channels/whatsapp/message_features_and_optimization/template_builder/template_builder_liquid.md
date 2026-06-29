---
nav_title: Liquid
article_title: WhatsApp 템플릿 빌더의 Liquid
description: "이 참조 문서에서는 WhatsApp 템플릿 빌더의 메시지 추가 정보와 조건부 Liquid 로직에 대해 다룹니다."
alias: /whatsapp_template_builder_liquid/
page_type: reference
channel:
  - WhatsApp
page_order: 1
---

# WhatsApp 템플릿 빌더의 Liquid {#liquid-in-the-whatsapp-template-builder}

> Liquid를 사용하여 WhatsApp 템플릿 빌더에서 템플릿을 개인화할 수 있지만, Meta의 템플릿 구조로 인해 다른 Braze 채널에는 없는 제약이 존재합니다. 특히 메시지 추가 정보와 조건부 메시징 로직이라는 두 가지 Liquid 패턴에 특별한 처리가 필요합니다.

메시지 추가 정보와 조건부 메시징 로직의 경우, Meta는 템플릿의 각 변수가 발송 시점에 실제로 렌더링된 콘텐츠를 포함하도록 요구합니다. 빈 문자열을 가져오거나 표시되는 텍스트가 아닌 보이지 않는 메타데이터로 동작하는 변수는 발송 실패를 유발합니다. 변수의 콘텐츠만 변경하는 것이 아니라 정적 메시지 구조를 변경하는 조건문도 예기치 않은 동작을 유발합니다.

{% alert note %}
이 문서에서 설명하는 제약은 템플릿 메시지(Meta 승인 템플릿을 사용하는 아웃바운드 메시지)에만 적용됩니다. 이 제약은 응답 메시지(사용자가 연 24시간 메시징 기간 내에 발송되는 메시지)나 다른 Braze 채널의 메시지 추가 정보, 조건 로직 및 기타 Liquid 패턴에는 적용되지 않습니다.
{% endalert %}

## 개요 {#overview}

| 패턴 | 지원 여부 | 참고 |
| ----- | ----- | ----- |
| 다른 표시 콘텐츠와 함께 변수 내부의 `message_extras` | ✅ 예 | 태그가 캡처되며, 표시되는 텍스트가 Meta의 변수 콘텐츠 요구 사항을 충족합니다 |
| 변수의 유일한 콘텐츠로서의 `message_extras` | ❌ 아니요 | 빈 문자열로 확인되어 발송 실패를 유발합니다 |
| 변수 슬롯 내부의 조건부 Liquid | ✅ 예 | Braze가 발송 전에 평가하며, Meta는 최종 렌더링된 값만 확인합니다 |
| 변수 슬롯 외부의 조건부 Liquid | ❌ 아니요 | Liquid 태그가 리터럴 텍스트로 렌더링되어 수신자가 원시 구문을 보게 됩니다 |
| 변수 슬롯으로 시작하거나 끝나는 템플릿 | ❌ 아니요 | Meta는 모든 템플릿의 시작과 끝에 정적 텍스트를 요구합니다 |
| 빈 문자열로 확인되는 변수 슬롯 | ❌ 아니요 | Meta는 발송 시점에 모든 변수에 비어 있지 않은 콘텐츠를 요구합니다 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="빠른 참조" }

## 메시지 추가 정보 {#message-extras}

[`message_extras` Liquid 태그]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters/message_extras/)를 사용하면 발송 시점에 키-값 메타데이터로 메시지에 주석을 달 수 있습니다. 이 데이터는 메시지 본문에 렌더링되지 않습니다. 대신 기여도, 영향 측정, 이벤트 보강 등의 목적으로 연결된 콘텐츠, Currents 또는 기타 데이터 캡처 메커니즘으로 전달됩니다.

{% raw %}
```liquid
{% message_extras :key campaign_id :value "spring_promo_2025" %}
```
{% endraw %}

### 독립형 메시지 추가 정보 변수가 실패하는 이유 {#why-standalone-message-extras-variables-fail}

WhatsApp 템플릿 빌더에서 템플릿 변수(예: {% raw %}`{{1}}`, `{{2}}`{% endraw %})는 Liquid 표현식에 직접 매핑됩니다. Meta의 유효성 검사는 승인된 템플릿의 모든 변수 슬롯이 발송 시점에 비어 있지 않은 콘텐츠를 포함하도록 요구합니다. 이 콘텐츠는 수신자에게 표시되는 텍스트로 렌더링되어야 합니다.

`message_extras`는 출력을 렌더링하지 않으므로, 템플릿 변수 내부에 단독으로 배치하면 해당 변수 슬롯에 빈 문자열이 제출됩니다. Meta가 이를 거부하므로 메시지 발송이 실패합니다.

{% details WhatsApp 템플릿 빌더에서의 잘못된 사용법 %}

{% raw %}
```
Template variable {{1}}: {% message_extras :key attribution_source :value "canvas_a" %}
```
{% endraw %}

발송 시점에 {% raw %}`{{1}}`{% endraw %}이 빈 문자열로 확인되어 발송 실패를 유발합니다.

{% enddetails %}

### 올바른 사용법 {#correct-usage}

`message_extras` 태그를 올바르게 포함하려면 기존 변수에 태그를 삽입합니다. 즉, 표시되는 출력을 생성하는 Liquid 블록 내부, 구체적으로 실제 템플릿 변수를 채우는 동일한 표현식 내부에 태그를 배치합니다. Meta는 변수에 콘텐츠가 포함되어 있으므로 이를 수락하고, Braze는 메타데이터를 캡처하며, 수신자는 렌더링된 텍스트만 보게 됩니다.

#### 예시 {#example}

템플릿 본문이 다음과 같다고 가정합니다:

{% raw %}
```
Hi {{1}}, your order has shipped.
```
{% endraw %}

그리고 변수 {% raw %}`{{1}}`{% endraw %}이 다음에 매핑되어 있습니다:

{% raw %}
```
{{ ${first_name} | default: "there" }}
```
{% endraw %}

메시지 추가 정보를 첨부하려면 변수 표현식을 다음과 같이 다시 작성합니다:

{% raw %}
```
{{ ${first_name} | default: "there" }}{% message_extras :key order_source :value "canvas_spring" %}
```
{% endraw %}

발송 시점에 {% raw %}`{{1}}`{% endraw %}은 `"Alex"`와 같은 값으로 확인되며, 이는 Meta의 요구 사항을 충족하는 표시 콘텐츠입니다. `message_extras` 태그는 평가되고 데이터가 캡처되지만, 수신자가 보는 렌더링된 문자열에는 아무것도 기여하지 않습니다.

### 핵심 규칙 {#key-rules}

- `message_extras`를 템플릿 변수의 유일한 콘텐츠로 할당하지 마세요.
- 항상 표시되는 텍스트로 확인되는 변수에 태그를 첨부하세요.
- 렌더링된 출력에 영향을 주지 않고 동일한 변수 표현식에 여러 `message_extras` 태그를 추가할 수 있습니다.
- 본문, 헤더 및 기타 모든 변수 슬롯에서 이 패턴을 사용하세요.

## 조건부 메시징 로직 {#conditional-messaging-logic}

메시징 채널에서 Liquid `if/elsif/else` 블록은 텍스트의 전체 섹션을 조건부로 포함하거나 제외할 수 있습니다. Braze는 발송 전에 전체 Liquid 출력을 렌더링하며, 결과는 로직이 생성하는 내용이 됩니다.

그러나 Meta 승인 WhatsApp 템플릿은 고정된 구조를 가집니다. Meta는 템플릿 콘텐츠를 두 가지 범주로 분류합니다:

- **정적 텍스트:** 템플릿 생성 시 확정되며 모든 수신자에게 동일하게 유지되는 하드코딩된 문자열입니다.
- **변수 슬롯:** 발송 시점에 콘텐츠가 채워지는 자리 표시자 위치(예: {% raw %}`{{1}}`{% endraw %})입니다.

### 변수 슬롯 외부의 조건부 메시징 로직이 실패하는 이유 {#why-conditional-messaging-logic-outside-a-variable-slot-fails}

승인된 템플릿에서 정적 텍스트 대 변수 슬롯의 비율은 고정되어 있으며 발송별로 변경할 수 없고 엄격한 제한이 있습니다. Meta는 템플릿의 모든 변수 슬롯에 대해 최소한의 정적 텍스트를 요구합니다. 대부분 또는 전체가 변수인 템플릿은 만들 수 없습니다. 이는 Meta가 확정된 정적 콘텐츠로 간주하는 텍스트를 추가하거나 제거하는 조건부 Liquid를 포함할 수 없음을 의미합니다.

`if/else` 블록을 사용하여 정적 텍스트 청크를 조건부로 포함하거나 제외하려고 하면, Meta는 로직을 평가하지 않습니다. 변수 슬롯 외부의 Liquid 태그는 리터럴 출력 텍스트로 처리됩니다. 수신자는 메시지에서 원시 Liquid 구문 태그({% raw %}`{% if %}`, `{% else %}`, `{% endif %}`{% endraw %})와 모든 분기 콘텐츠를 그대로 보게 됩니다.

{% details WhatsApp 템플릿 빌더에서의 잘못된 사용법 %}

{% raw %}
```
{% if ${loyalty_tier} == "gold" %}Hi {{1}}, we have an exclusive Gold member offer.{% else %}Hi {{1}}, we have a special offer for you.{% endif %}
```
{% endraw %}

이는 하나의 템플릿에 두 개의 서로 다른 승인된 템플릿을 포함하려는 시도입니다. 정적 텍스트를 감싸는 조건문은 예상대로 동작하지 않습니다.

{% enddetails %}

### 올바른 사용법

조건문은 변수 슬롯 내부에서 유효하며 지원됩니다. 조건문은 해당 변수를 채우는 값을 제어합니다. Meta는 {% raw %}`{{1}}`{% endraw %}에 콘텐츠가 채워졌다는 것만 확인하며, 내부의 Liquid가 어떻게 해당 값에 도달했는지는 검사하지 않습니다.

#### 예시

{% raw %}
```
{% if ${loyalty_tier} == "gold" %}exclusive Gold member{% else %}valued customer{% endif %}
```
{% endraw %}

템플릿 변수의 값으로 사용하면 `"exclusive Gold member"` 또는 `"valued customer"`가 생성됩니다. 둘 다 Meta의 변수 콘텐츠 요구 사항을 충족하는 비어 있지 않은 문자열입니다.

템플릿 본문 자체는 구조적으로 변경되지 않습니다:

{% raw %}
```
Hi {{1}}, we have a special offer for you.
```
{% endraw %}

### 변수 슬롯 내부에 조건 로직 배치하기 {#place-conditional-logic-inside-a-variable-slot}

템플릿 빌더에서 변수 슬롯에 조건부 Liquid를 배치하는 두 가지 방법이 있습니다:

1. **Content Blocks 사용(미리 채우기 지원):** Content Blocks 내부에 조건 로직을 구축한 다음 변수에서 해당 블록을 참조합니다. 이 방법은 미리 채우기를 지원하므로, 발송 전에 템플릿 빌더에서 변수가 미리보기 값을 표시할 수 있습니다.
2. **자리 표시자를 사용하고 Liquid 붙여넣기(미리 채우기 미지원):** 템플릿 생성 시 {% raw %}`{{1}}`{% endraw %}과 같은 자리 표시자를 추가한 다음, 전체 Liquid 표현식을 해당 변수 슬롯에 직접 붙여넣습니다. 이 방법은 미리 채우기를 지원하지 않지만, 모든 Liquid 로직에 사용할 수 있습니다.

### 동일한 제약의 영향을 받는 기타 Liquid 구성요소 {#other-liquid-components-affected-by-the-same-constraint}

표시되는 출력을 생성하지 않는 모든 Liquid 태그는 변수 외부에 배치하면 원시 텍스트로 렌더링됩니다. 여기에는 다음이 포함됩니다:

- **`catalog_items`:** 카탈로그 데이터를 조회하고 참조하는 Liquid는 변수 슬롯 내부에 있어야 합니다. 그렇지 않으면 태그가 메시지에 그대로 표시됩니다.
- **`assign`:** 변수 할당 태그(예: {% raw %}{% assign discount = "20%" %}{% endraw %})는 자체적으로 출력을 생성하지 않습니다. 메시지에서 나중에 사용할 값을 설정하기 위해 변수 슬롯 외부에서 사용하면 `assign` 태그가 리터럴로 렌더링됩니다. 출력이 필요한 변수 슬롯 내부의 Liquid 표현식 시작 부분에 `assign` 로직을 포함하세요.
- **Liquid 태그만 포함하는 Content Blocks:** Content Blocks에 Liquid 로직이 포함되어 있지만 표시되는 텍스트를 생성하지 않는 경우(예: `assign` 또는 `message_extras` 태그만 사용하는 경우), 변수 슬롯 외부에서 참조하면 원시 블록 콘텐츠가 메시지에 표시됩니다. 표시되는 출력을 생성하지 않는 Content Blocks는 렌더링되는 콘텐츠와 함께 변수 슬롯 내부에 삽입해야 합니다.

### 추가 구조적 제약 {#additional-structural-constraints}

Meta는 템플릿에 다음을 요구합니다:

- **정적 텍스트로 시작해야 합니다.** 템플릿은 변수 슬롯으로 시작할 수 없습니다(예: {% raw %}`{{1}} is ready for you`{% endraw %}).
- **정적 텍스트로 끝나야 합니다.** 템플릿은 변수 슬롯으로 끝날 수 없습니다.

이러한 제약은 Liquid 사용 여부와 관계없이 존재합니다. 승인된 템플릿 구조 자체에 적용됩니다.

### 핵심 규칙

- 변수 슬롯 표현식 내부에서 조건문을 자유롭게 사용하여 렌더링되는 값을 제어하세요.
- 정적 텍스트(메시지에서 변수 슬롯이 아닌 부분)를 추가, 제거 또는 교체하기 위해 조건문을 사용하지 마세요.
- 변수 내부의 모든 조건 분기가 비어 있지 않은 문자열을 생성하는지 확인하세요(빈 문자열이 실패를 유발하는 이유는 [메시지 추가 정보](#message-extras)를 참조하세요).
- 템플릿은 Meta에 제출된 대로 정적 텍스트로 시작하고 끝나야 합니다.