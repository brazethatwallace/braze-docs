---
nav_title: FAQ
article_title: 자주 묻는 질문
page_order: 12
description: "이 문서에서는 Liquid에 대해 자주 묻는 질문에 대한 답변을 제공합니다."

---

# 자주 묻는 질문

> 이 페이지에서는 Liquid에 대해 자주 묻는 질문에 대한 답변을 확인할 수 있습니다.<br><br>Braze는 현재 Shopify의 Liquid를 100% 지원하지 않으며, 설명서에서 설명하려고 시도한 특정 부분만 지원합니다. 오류 발생 위험이나 지원되지 않는 Liquid 사용을 줄이기 위해 Liquid를 사용하는 모든 메시지를 발송 전에 테스트하는 것을 강력히 권장합니다.

### Braze에서 Liquid 스니펫을 어떻게 사용하나요?

대부분의 경우 캠페인이나 캔버스로 이동한 후, 이메일 메시지 본문이나 세그먼트 등의 영역에서 개인화 모달을 통해 Liquid를 삽입하여 Liquid 스니펫을 활용할 수 있습니다.

#### 더 자세히 알아보려면 어디를 참고하면 되나요?

Liquid에 대해 더 알아보려면 Braze Learning의 가이드 학습 경로 [Liquid를 활용한 동적 개인화](https://learning.braze.com/path/dynamic-personalization-with-liquid)를 확인하세요! 또한 [Liquid 사용 사례 라이브러리]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases/)에서 영감을 얻고 Liquid를 사용한 다양한 개인화 예시를 참고할 수 있습니다.

### 개인화에 Liquid와 연결된 콘텐츠를 사용하는 것의 차이점은 무엇인가요?

Braze 연결된 콘텐츠는 Liquid 태그의 한 예입니다. 마찬가지로 개인화에 사용되지만, 이 데이터는 Braze 내에 저장된 데이터가 아닌 외부 엔드포인트에서 가져옵니다. 메시지 개인화를 확장하는 방법에 대해 자세히 알아보려면 전용 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) 섹션을 확인하세요.

### Liquid 템플릿이란 무엇인가요?

Braze에서 Liquid를 사용하는 가장 일반적인 방법입니다. Liquid 템플릿은 고객 프로필의 데이터를 메시지에 가져오는 것을 의미합니다. 이 데이터는 사용자의 이름부터 트리거된 메시지의 커스텀 이벤트까지 다양할 수 있습니다.

지원되는 Liquid 태그의 전체 목록은 [지원되는 개인화 태그]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags/)를 참조하세요.

### Liquid로 변수를 어떻게 할당하나요?

`assign` 태그를 사용하여 변수를 생성하고 할당할 수 있습니다. 이렇게 하면 메시지 작성기에서 변수가 생성되며, 메시지 전체에서 참조할 수도 있습니다.

### Liquid를 사용하면 데이터 포인트가 기록되나요?

아니요.

### Liquid를 사용하여 개인화된 인사말을 보내려면 어떻게 하나요?

사용자의 이름을 사용한 개인화된 인사말의 경우, {% raw %} `{{${first_name}}}`, `{{${last_name}}}` 같은 표준 고객 프로필 속성을 가져올 수 있습니다.

또한 Liquid `{% if X %}` {% endraw %}문을 사용하여 요일이나 커스텀 속성 등 다양한 조건에 따라 조건부 렌더링을 수행할 수 있습니다. 조건문에서 사용할 수 있는 지원되는 Liquid Operator에 대한 자세한 내용은 [Operator]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/operators/)를 확인하세요.

### 고객의 위치를 기반으로 메시지를 개인화하려면 어떻게 하나요?

{% raw %}
사용자의 위치에 대한 기본 속성이 있습니다: `{{${most_recent_location}}}`.

### {{campaign.${name}}}과 {{campaign.${message_name}}}의 차이점은 무엇인가요?

`{{campaign.${name}}}`과 `{{campaign.${message_name}}}`은 모두 지원되는 Liquid 개인화 태그입니다. 두 태그 모두 캠페인 속성을 참조합니다. `{{campaign.${name}}}`은 캠페인의 이름을 나타내고, `{{campaign.${message_name}}}`은 메시지 배리언트의 이름입니다.
{% endraw %}

### 중첩된 오브젝트에서 Liquid를 어떻게 사용하나요?

Braze에는 메시지에서 사용할 수 있는 세그먼트용 Liquid 코드를 생성하는 내장 기능이 있습니다. 구체적으로, 오브젝트 내에서 여러 기준과 일치하는 세그먼트를 생성할 수 있습니다.

자세한 내용은 [다중 기준 세분화]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support/#multi-criteria-segmentation)를 확인하세요.

### 이벤트가 트리거하는 메시지를 개인화하기 위해 이벤트 속성을 어떻게 사용하나요?

{% raw %}
`api_triggered_property` 태그를 사용하여 API 트리거 이벤트의 등록정보에 접근할 수 있습니다: `{{api_trigger_properties.${attribute_key}}}`.
{% endraw %}

### 중단 로직이란 무엇이며, 어떻게 사용하나요?

중단 로직을 사용하면 조건이 충족될 때 메시지 발송을 중지할 수 있습니다. 이는 불완전한 메시지가 사용자에게 발송되는 것을 방지하는 데 특히 유용합니다. 마케팅 캠페인에서의 중단 로직 예시에 대해 자세히 알아보려면 [메시지 중단]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/)을 참조하세요.

### for 루프 로직이란 무엇이며, 어떻게 사용하나요?

for 루프는 [반복 태그](https://shopify.github.io/liquid/tags/iteration/)라고도 합니다. Liquid 스니펫에서 for 루프 로직을 사용하면 조건이 충족될 때까지 Liquid 블록을 순환할 수 있습니다.

Braze에서는 배열 커스텀 속성의 항목을 확인하거나, [카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs/), [선택]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/), 또는 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/) 호출 응답에서 반환된 값 및 오브젝트 목록을 확인하는 데 사용할 수 있습니다. 구체적으로, for 루프 로직을 메시징의 일부로 사용하여 제품의 재고 여부나 제품의 최소 평점 충족 여부를 확인할 수 있습니다.

예를 들어, "Games"라는 카탈로그에 "cheap_games"라는 선택이 있다고 가정해 보겠습니다. "cheap_games"에 있는 게임의 제목을 가져오려면 다음 Liquid 스니펫을 사용할 수 있습니다:

{% raw %}
```liquid
{% catalog_selection_items Games cheap_games %}
{% for item in items %}
 Get this game: {{ item.title }}
{% endfor %}
```
{% endraw %}

설정된 조건이 충족되면 메시지가 진행될 수 있습니다. 이 로직을 사용하면 다양한 조건에 대해 Liquid 블록을 반복하는 대신 시간을 절약할 수 있는 유용한 방법입니다.

### 콘텐츠 블록을 사용하는 메시지에 여분의 공백이 생기는 이유는 무엇인가요?

Liquid가 포함된 콘텐츠 블록을 사용하는 발송된 메시지에서 여분의 공백이 발견되면, 조건문 내에 불필요한 단락이나 줄 바꿈이 있을 수 있습니다. 조건문을 여러 줄에 걸쳐 작성하지 말고 한 줄에 작성하세요.

#### 예시

{% raw %}
```liquid
{% if {{custom_attribute.${has_discount}}} == true %}Discounted Item{% elsif {{custom_attribute.${is_new_arrival}}} == true %}New Arrival{% else %}Regular Item{% endif %}
{% endraw %}

### When should I use `assign` versus `capture`?

Both `assign` and `capture` create Liquid variables, but they serve different purposes:

- `assign` is for simple variables that store a single value, such as a boolean, number, or simple string. You can also apply a single filter in the same line.
- `capture` is for storing a block of text that may include multiple variables, strings, or complex expressions. Use `capture` when the value is too complex for a single `assign` statement, such as URLs that utilize other Liquid variables or custom attributes as parameters. `capture` is also preferred when implementing Liquid variables in the body of Connected Content calls.

#### Examples

{% raw %}
```liquid
{% comment %} Valid assign usage {% endcomment %}
{% assign name = {{custom_attribute.${first_name}}} %}
{% assign price = {{custom_attribute.${price}}} | plus: 0 %}

{% comment %} Use capture for complex strings {% endcomment %}
{% capture greeting %}Hello, {{custom_attribute.${first_name}}}! Your order #{{custom_attribute.${order_id}}} is ready.{% endcapture %}
{{ greeting }}
```
{% endraw %}