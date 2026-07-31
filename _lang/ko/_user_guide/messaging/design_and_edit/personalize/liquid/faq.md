---
nav_title: FAQ
article_title: 자주 묻는 질문
page_order: 12
description: "이 문서에서는 Liquid에 대해 자주 묻는 질문에 대한 답변을 제공합니다."
toc_headers: h2
---

# 자주 묻는 질문 {#frequently-asked-questions}

> 이 페이지에서는 Liquid에 대해 자주 묻는 질문에 대한 답변을 확인할 수 있습니다.

{% alert note %}
Braze는 현재 Shopify의 Liquid를 100% 지원하지 않으며, 설명서에서 설명하려고 시도한 특정 부분만 지원합니다. 오류 발생 위험이나 지원되지 않는 Liquid 사용을 줄이기 위해 Liquid를 사용하는 모든 메시지를 발송 전에 테스트하세요.
{% endalert %}

## Braze에서의 Liquid 사용 {#about-liquid-in-braze}

### Braze에서 Liquid 스니펫을 어떻게 사용하나요? {#how-do-i-use-liquid-snippets-in-braze}

대부분의 경우, Campaigns 또는 Canvases에서 이메일 메시지 본문이나 Segments와 같은 영역의 개인화 모달에 Liquid를 삽입하여 Liquid 스니펫을 활용할 수 있습니다.

#### 더 자세히 알아보려면 어디에서 확인할 수 있나요? {#where-can-i-learn-more}

Liquid에 대해 더 알아보려면 Braze 학습 경로 [Liquid를 활용한 동적 개인화](https://learning.braze.com/path/dynamic-personalization-with-liquid)를 확인하세요. 또한 [Liquid 사용 사례 라이브러리]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases)에서 영감을 얻고 Liquid를 사용한 다양한 개인화 예시를 참고할 수 있습니다.

### 개인화에 Liquid와 연결된 콘텐츠를 사용하는 것의 차이점은 무엇인가요? {#whats-the-difference-between-using-liquid-and-connected-content-for-personalization}

Braze 연결된 콘텐츠는 Liquid 태그의 한 예입니다. 마찬가지로 개인화에 사용되지만, Braze 내에 저장된 데이터가 아닌 외부 엔드포인트에서 데이터를 가져옵니다. 메시지 개인화를 확장하는 방법에 대해 자세히 알아보려면 전용 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) 섹션을 확인하세요.

### Liquid 템플릿이란 무엇인가요? {#what-is-liquid-templating}

Braze에서 Liquid를 사용하는 가장 일반적인 방법입니다. Liquid 템플릿은 사용자 프로필의 데이터를 메시지에 가져오는 것을 의미합니다. 이 데이터는 사용자의 이름부터 트리거된 메시지의 커스텀 이벤트까지 다양합니다.

지원되는 Liquid 태그의 전체 목록은 [지원되는 개인화 태그]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)를 참조하세요.

### Liquid를 사용하면 데이터 포인트가 기록되나요? {#does-using-liquid-log-data-points}

아니요.

## 개인화 태그 및 데이터 소스 {#personalization-tags-and-data-sources}

### Liquid를 사용하여 개인화된 인사말을 보내려면 어떻게 해야 하나요? {#how-can-i-use-liquid-to-send-a-personalized-greeting}

사용자의 이름을 사용한 개인화된 인사말을 위해 {% raw %}`{{${first_name}}}` 및 `{{${last_name}}}`{% endraw %}와 같은 표준 고객 프로필 속성을 가져올 수 있습니다.

또한 Liquid {% raw %}`{% if X %}`{% endraw %} 문을 사용하여 요일이나 커스텀 속성 등 다양한 조건에 따라 조건부 렌더링을 수행할 수 있습니다. 조건문에서 사용할 수 있는 지원되는 Liquid 연산자에 대한 자세한 내용은 [연산자]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/operators)를 확인하세요.

### 사용자의 위치를 기반으로 메시지를 개인화하려면 어떻게 해야 하나요? {#how-can-i-personalize-a-message-based-on-a-users-location}

{% raw %}
사용자의 위치에 대한 기본 속성이 있습니다: `{{${most_recent_location}}}`.
{% endraw %}

{% raw %}
### {{campaign.${name}}}과 {{campaign.${message_name}}}의 차이점은 무엇인가요? {#whats-the-difference-between-campaignname-and-campaignmessage_name}

`{{campaign.${name}}}` 및 `{{campaign.${message_name}}}` 모두 지원되는 Liquid 개인화 태그입니다. 두 태그 모두 Campaign 속성을 참조합니다. `{{campaign.${name}}}`은 Campaign의 이름을 나타내고, `{{campaign.${message_name}}}`은 메시지 배리언트의 이름입니다.
{% endraw %}

URL 및 쿼리 문자열 사용(예: 이름에 `%` 또는 공백이 포함된 경우)에 대해서는 [URL에서의 Campaign 이름]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#campaign-names-in-urls)을 참조하세요.

### 중첩된 객체에서 Liquid를 어떻게 사용하나요? {#how-do-i-use-liquid-with-nested-objects}

Braze에는 메시지에서 사용할 수 있는 Segments용 Liquid 코드를 생성하는 기본 제공 기능이 있습니다. 구체적으로, 객체 내에서 여러 기준과 일치하는 Segment를 생성할 수 있습니다.

자세한 내용은 [다중 기준 세분화]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support#segmentation-behavior-with-arrays-of-objects)를 확인하세요.

### 이벤트가 트리거하는 메시지를 개인화하기 위해 이벤트 속성을 어떻게 사용하나요? {#how-do-i-use-event-attributes-to-personalize-a-message-that-an-event-is-triggering}

{% raw %}
`api_triggered_property` 태그를 사용하여 API 트리거 이벤트의 속성정보에 접근할 수 있습니다: `{{api_trigger_properties.${attribute_key}}}`.
{% endraw %}

### Braze는 Liquid에서 배열의 배열을 지원하나요? {#does-braze-support-an-array-of-arrays-in-liquid}

Liquid는 기본적으로 배열의 배열을 지원하지 않습니다. 값을 쉼표로 구분된 문자열 배열로 저장하고, 필요할 때 `split` 필터를 사용하여 파싱하세요.

## 변수와 구문 {#variables-and-syntax}

### Liquid로 변수를 어떻게 할당하나요? {#how-do-i-assign-variables-with-liquid}

`assign` 태그를 사용하여 변수를 생성하고 할당할 수 있습니다. 이렇게 하면 메시지 작성기에서 변수가 생성되며, 메시지 전체에서 참조할 수도 있습니다.

### `assign`과 `capture`는 언제 사용해야 하나요? {#when-should-i-use-assign-versus-capture}

`assign`과 `capture` 모두 Liquid 변수를 생성하지만, 용도가 다릅니다:

- `assign`은 불리언, 숫자 또는 간단한 문자열과 같은 단일 값을 저장하는 간단한 변수에 사용합니다. 같은 줄에서 단일 필터를 적용할 수도 있습니다.
- `capture`는 여러 변수, 문자열 또는 복잡한 표현식을 포함할 수 있는 텍스트 블록을 저장하는 데 사용합니다.

값이 단일 `assign` 문으로 처리하기에 너무 복잡한 경우(예: 다른 Liquid 변수나 커스텀 속성을 매개변수로 사용하는 URL) `capture`를 사용하세요. `capture`는 연결된 콘텐츠 호출 본문에서 Liquid 변수를 구현할 때도 선호됩니다.

#### 예시 {#examples}

{% raw %}
```liquid
{% comment %}Use assign for custom attributes{% endcomment %}
{% assign name = {{custom_attribute.${first_name}}} %}
{% assign price = {{custom_attribute.${price}}} | plus: 0 %}

{% comment %}Use assign for a simple variable{% endcomment %}
{% assign discount_label = "20% off" %}
Hello {{ customer.first_name | default: "there" }}, enjoy {{ discount_label }} on your next order!

{% comment %}Use capture for complex strings{% endcomment %}
{% capture greeting %}Hello, {{custom_attribute.${first_name}}}! Your order #{{custom_attribute.${order_id}}} is ready.{% endcapture %}
{{ greeting }}

{% comment %}Use capture to create conditional content{% endcomment %}
{% capture promo_block %}
{% if customer.vip == true %}
As a VIP member, you get free shipping.
{% else %}
Join our VIP program to unlock free shipping.
{% endif %}
{% endcapture %}
```
{% endraw %}

### Liquid 변수가 제목란과 본문 사이에서 유지되나요? {#do-liquid-variables-carry-between-subject-line-and-body}

아니요. Braze는 각 메시지 구성 요소(예: 제목란, HTML 본문, 프리헤더, 푸시 제목)를 별도로 렌더링합니다. 한 필드에서 수행한 할당이나 캡처는 다른 필드에서 사용할 수 없습니다. 값이 필요한 각 필드에서 Liquid 또는 연결된 콘텐츠 호출을 반복하세요.

### for 루프 로직이란 무엇이며, 어떻게 사용할 수 있나요? {#what-is-for-loop-logic-and-how-can-i-use-it}

for 루프는 [반복 태그](https://shopify.github.io/liquid/tags/iteration/)라고도 합니다. Liquid 스니펫에서 for 루프 로직을 사용하면 조건이 충족될 때까지 Liquid 블록을 순환할 수 있습니다.

Braze에서는 배열 커스텀 속성의 항목을 확인하거나, [카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs), [셀렉션]({{site.baseurl}}/user_guide/data/activation/catalogs/selections) 또는 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content) 호출 응답에서 반환된 값 및 객체 목록을 확인하는 데 사용할 수 있습니다. 구체적으로, for 루프 로직을 메시징의 일부로 사용하여 제품이 재고가 있는지 또는 제품이 최소 평점을 충족하는지 확인할 수 있습니다.

예를 들어, "Games"라는 카탈로그에 "cheap_games"라는 셀렉션이 있다고 가정해 보겠습니다. "cheap_games"에 있는 게임의 제목을 가져오려면 다음 Liquid 스니펫을 사용할 수 있습니다:

{% raw %}
```liquid
{% catalog_selection_items Games cheap_games %}
{% for item in items %}
 Get this game: {{ item.title }}
{% endfor %}
```
{% endraw %}

설정된 조건이 충족되면 메시지가 진행될 수 있습니다. 이 로직을 사용하면 다양한 조건에 대해 Liquid 블록을 반복하는 대신 시간을 절약할 수 있는 유용한 방법입니다.

### 중단 로직이란 무엇이며, 어떻게 사용할 수 있나요? {#what-is-abort-logic-and-how-can-i-use-it}

중단 로직을 사용하면 조건이 충족될 때 메시지 발송을 중지할 수 있습니다. 이는 불완전한 메시지가 사용자에게 발송되는 것을 방지하는 데 특히 유용합니다. 마케팅 캠페인에서의 중단 로직 예시에 대해 자세히 알아보려면 [메시지 중단]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)을 참조하세요.

### `abort_message` 태그 안에서 Liquid를 사용할 수 있나요? {#can-i-use-liquid-inside-the-abort_message-tag}

아니요. {% raw %}`{% abort_message %}`{% endraw %} 태그는 Liquid 개인화가 아닌 따옴표로 묶인 정적 문자열을 허용합니다. 조건부 중단 동작이 필요한 경우 태그 앞에 다른 Liquid 로직을 사용하세요.

### Liquid로 전화번호를 마스킹하려면 어떻게 하나요? {#how-do-i-mask-phone-numbers-with-liquid}

`slice` 필터를 사용하여 특정 숫자를 추출하고 `append` 필터를 사용하여 마스킹 문자와 결합하면 전화번호를 마스킹할 수 있습니다.

#### 마지막 네 자리를 제외하고 모두 마스킹 {#mask-all-but-the-last-four-digits}

10자리 전화번호를 `******7890`으로 표시하려면:

{% raw %}
```liquid
{% assign phone = {{${phone_number}}} | split: '' %}
{% assign masked_phone = '' %}
{% for i in (0..5) %}
  {% assign masked_phone = masked_phone | append: '*' %}
{% endfor %}
{% for i in (6..9) %}
  {% assign masked_phone = masked_phone | append: phone[i] %}
{% endfor %}
{{ masked_phone }}
```
{% endraw %}

#### 처음 세 자리와 마지막 네 자리 표시 {#show-the-first-three-and-last-four-digits}

10자리 전화번호를 `123***7890`으로 표시하려면:

{% raw %}
```liquid
{% assign first_part = {{${phone_number}}} | slice: 0, 3 %}
{% assign last_part = {{${phone_number}}} | slice: -4, 4 %}
{% assign masked_phone_number = first_part | append: "***" | append: last_part %}
{{ masked_phone_number }}
```
{% endraw %}

## Canvas, 카탈로그 및 트리거 속성정보 {#canvas-catalogs-and-trigger-properties}

### API 트리거 Liquid가 Braze에서 실패하는 이유는 무엇인가요? {#why-is-my-api-triggered-liquid-failing-in-braze}

{% raw %}
중괄호가 추가로 포함된 것이 일반적인 원인입니다. 예를 들어, `{{{api_trigger_properties.${attribute_key}}}}` 는 유효한 Braze 개인화 구문이 아닙니다. 여는 중괄호 두 개와 닫는 중괄호 두 개를 정확히 사용하세요: `{{api_trigger_properties.${attribute_key}}}`.
{% endraw %}

### Canvas 컨텍스트 속성정보에 크기 제한이 있나요? {#are-there-size-limits-for-canvas-context-properties}

Braze는 [Canvas 컨텍스트 속성정보]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)에 대해 엄격한 제한을 적용하지 않지만, 페이로드를 약 1KB(~1,000자) 미만으로 유지하세요. 더 큰 객체는 메모리 사용량을 증가시키고 대량 발송 시 메시지 렌더링을 지연시킬 수 있습니다.

### 대시보드에서 특정 데이터 유형을 미리 볼 때 Liquid 오류가 발생하는 이유는 무엇인가요? {#why-do-i-get-a-liquid-error-when-previewing-certain-data-types-in-the-dashboard}

일부 [Canvas 컨텍스트 속성정보]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties) 유형은 비교 또는 수학 연산에 사용하기 전에 Liquid에서 형변환이 필요합니다. 예를 들어, 숫자 동작이 필요한 경우:

{% raw %}
```liquid
{{context.${property_name} | plus: 0}}
```
{% endraw %}

### 카탈로그 Liquid 스니펫이 중단 메시지를 반환하는 이유는 무엇인가요? {#why-does-my-catalog-liquid-snippet-return-an-abort-message}

카탈로그 Liquid 스니펫이 발송 중 중단되는 경우, 대량 또는 완전 동적 선택을 사용하는 대신 개인화 메뉴에서 개별 카탈로그 항목을 선택하여 스니펫을 다시 생성하세요. [카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs) 및 [셀렉션]({{site.baseurl}}/user_guide/data/activation/catalogs/selections)을 참조하세요.

## Content Blocks와 메시지 작성기 {#content-blocks-and-the-message-composer}

### Content Blocks를 사용하는 메시지에 여분의 간격이 생기는 이유는 무엇인가요? {#why-is-there-extra-spacing-in-messages-that-use-content-blocks}

Content Blocks와 Liquid를 사용하는 발송된 메시지에서 여분의 간격이 발견되면, 조건문 내에 불필요한 단락 또는 줄 바꿈이 있을 수 있습니다. 조건문을 여러 줄에 걸쳐 작성하지 말고 한 줄로 작성하세요.

#### 예시 {#example}

{% raw %}
```liquid
{% if {{custom_attribute.${has_discount}}} == true %}Discounted Item{% elsif {{custom_attribute.${is_new_arrival}}} == true %}New Arrival{% else %}Regular Item{% endif %}
```
{% endraw %}


### 여러 줄의 Liquid가 드래그 앤 드롭 편집기에서 예상치 못한 공백을 만드는 이유는 무엇인가요? {#why-does-multi-line-liquid-create-unexpected-whitespace-in-the-drag-and-drop-editors}

인앱 메시지 드래그 앤 드롭 편집기 또는 이메일 드래그 앤 드롭 편집기에서 Liquid 코드가 여러 줄에 걸쳐 있으면, 각 {% raw %}`{% %}`{% endraw %} 블록이 보이지 않는 텍스트로 렌더링됩니다. 줄 바꿈이 표시되는 출력 앞에 빈 줄로 유지되어 예상치 못한 공백이 발생합니다.

#### 해결 방법 1: 공백 제어 태그 사용(권장) {#solution-1-use-whitespace-control-tags-recommended}

태그 구분자 안에 하이픈을 추가하여 코드 가독성을 유지하면서 주변 공백을 제거하세요:

{% raw %}
```liquid
{%- assign event_date = {{custom_attribute.${PreferredPickupDate}}} | date: "%s" -%}
{%- assign today = 'now' | date: "%s" -%}
{%- assign difference = event_date | minus: today -%}
{%- assign difference_days = difference | divided_by: 86400 -%}
Only {{ difference_days }} days until your move!
```
{% endraw %}

#### 해결 방법 2: Liquid를 한 줄로 통합 {#solution-2-consolidate-liquid-onto-a-single-line}

모든 줄 바꿈을 제거하여 Liquid를 하나의 연속된 줄로 만드세요:

{% raw %}
```liquid
{% assign event_date = {{custom_attribute.${PreferredPickupDate}}} | date: "%s" %}{% assign today = 'now' | date: "%s" %}{% assign difference = event_date | minus: today %}{% assign difference_days = difference | divided_by: 86400 %}Only {{ difference_days }} days until your move!
```
{% endraw %}

두 가지 방법 모두 렌더링된 메시지에서 원치 않는 빈 줄을 방지합니다. 이는 인앱 메시지 드래그 앤 드롭 편집기, 이메일 드래그 앤 드롭 편집기, 그리고 Liquid를 사용하는 Content Blocks에 적용됩니다. 자세한 내용은 [공백 제어](https://shopify.github.io/liquid/basics/whitespace/)를 참조하세요.

### 드래그 앤 드롭 검색 도구의 **Row**에서 Content Block이 보이지 않는 이유는 무엇인가요? {#why-is-my-content-block-missing-from-row-in-the-drag-and-drop-search-tool}

일부 Content Blocks는 드래그 앤 드롭 편집기 검색의 **Row** 아래에 표시되지 않습니다. **Content** 탭(**Advanced**)에서 HTML 블록을 추가한 다음, 해당 HTML 블록에 Content Block Liquid 태그를 삽입하여 블록 콘텐츠를 렌더링하세요.

### 드래그 앤 드롭 Content Block 미리보기가 작성 보기와 다른 이유는 무엇인가요? {#why-does-my-drag-and-drop-content-block-preview-differ-from-the-compose-view}

Content Block을 Liquid로 템플릿화하면, 블록 내의 모바일 미디어 쿼리가 블록을 메시지에 직접 드래그할 때와 동일한 방식으로 미리보기에 적용되지 않을 수 있습니다. 블록을 드래그하면 레이아웃은 유지되지만 소스 블록과 분리되므로, 이후 블록을 편집해도 메시지가 자동으로 업데이트되지 않습니다.

### 메시지 작성기에서 이벤트 속성정보 값을 미리보기하려면 어떻게 해야 하나요? {#how-do-i-preview-event-property-values-in-message-composer}

**커스텀 사용자로 미리보기**를 사용하고 미리보기할 사용자의 샘플 커스텀 이벤트 속성정보 값을 입력하세요. 이는 중단 로직이 있는 메시지에서 중단을 트리거하지 않는 미리보기 값이 필요할 때도 유용합니다.

## 이메일 메시지의 Liquid {#liquid-in-email-messages}

### 메시지가 "Invalid from email address for recipient:"로 중단되는 이유는 무엇인가요? {#why-does-my-message-abort-with-invalid-from-email-address-for-recipient}

이 중단은 **From** 주소의 Liquid가 누락된 변수, 추가 공백 또는 허용되지 않는 문자 등 잘못된 구문을 생성할 때 발생합니다. 테스트 사용자로 미리보기하고 렌더링된 **From** 주소가 구성된 발송 도메인과 일치하는지 확인하세요.

### 동적 회신 주소는 어떻게 만드나요? {#how-do-i-create-a-dynamic-reply-to-address}

워크스페이스에서 동적 회신 주소 구성을 지원하는 경우 **Reply-To** 필드에서 Liquid를 사용하세요. 필요에 따라 **From** 표시 이름 설정과 함께 사용하세요. 워크스페이스별 옵션에 대해서는 [이메일 설정]({{site.baseurl}}/user_guide/administer/global/workspace_settings/email_preferences)을 참조하세요.

## Liquid 오류 문제 해결 {#troubleshooting-liquid-errors}

### Liquid 코드가 올바르게 보이는데 왜 작동하지 않나요? {#why-is-my-liquid-code-not-working-when-it-looks-correct}

Liquid 코드가 구문적으로 올바르게 보이지만 작동하지 않는 경우, 곧은 따옴표(`' '` 또는 `" "`)와 하이픈(`-`) 대신 스마트 따옴표(둥근 따옴표 `' '` 또는 `" "`)와 스마트 대시(엠 대시 `—`)가 사용되었는지 확인하세요. Liquid는 곧은 ASCII 문자만 인식하므로, 스마트 따옴표와 대시는 구문 분석 오류를 일으킵니다.

이 문제는 macOS 키보드 설정에서 **Use smart quotes and dashes**가 활성화되어 있을 때 흔히 발생하며, Braze 대시보드에서 입력할 때 문자가 자동으로 변환됩니다.

macOS에서 이 설정을 비활성화하려면:

1. **System Settings** > **Keyboard** > **Text Input** > **Edit**으로 이동합니다.
2. **Use smart quotes and dashes**를 선택 해제합니다.

| 예시 | 둥근 따옴표 (작동하지 않음) | 곧은 따옴표 (작동함) |
| --- | --- | --- |
| 기본값 | {% raw %}`{{${first_name} | default: 'Torchie'}}`{% endraw %} | {% raw %}`{{${first_name} | default: 'Torchie'}}`{% endraw %} |
| 조건문 | {% raw %}`{% if ${country} contains 'US' %}`{% endraw %} | {% raw %}`{% if ${country} contains 'US' %}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="스마트 따옴표 예시" }

이는 기본값, 조건문 및 따옴표를 사용하는 모든 Liquid에 적용됩니다. 둥근 따옴표와 곧은 따옴표는 화면에서 동일하게 보일 수 있으므로, 코드를 주의 깊게 비교하거나 일반 텍스트 편집기에 붙여넣어 확인하세요.

Liquid에서의 따옴표 사용에 대한 자세한 내용은 [Liquid 구문]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#liquid-syntax)을 참조하세요.

### "Unexpected end token" Liquid 오류가 표시되는 이유는 무엇인가요? {#why-am-i-seeing-an-unexpected-end-token-liquid-error}

이 오류는 일반적으로 중괄호가 추가되었거나 누락되었음을 나타냅니다. {% raw %}`{{ }}`{% endraw %}를 다른 Liquid 태그 표현식 안에 중첩하지 마세요. 예를 들어, 속성 참조를 추가 중괄호 쌍으로 감싸는 대신 {% raw %}`{{custom_attribute.${date_of_birth} | date: '%s'}}`{% endraw %}를 사용하세요.

### 인앱 메시지에서 연결된 콘텐츠 재시도를 사용할 수 없는 이유는 무엇인가요? {#why-is-connected-content-retry-unavailable-for-my-in-app-message}

{% raw %}
재시도가 포함된 `{% connected_content %}` 태그는 일부 인앱 메시지 형식을 포함하여 모든 메시지 유형에서 지원되지 않습니다. 재시도 매개변수를 제거하거나 재시도된 연결된 콘텐츠 호출에 지원되는 채널을 사용하세요.
{% endraw %}