---
nav_title: Liquid 사용
article_title: Liquid 사용
page_order: 0
description: "이 참조 문서에서는 일반적인 Liquid 사용 사례에 대한 개요와 메시징에 Liquid 태그를 포함하는 방법을 설명합니다."
search_rank: 2
---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/path/dynamic-personalization-with-liquid){: style="float:right;width:120px;border:0;" class="noimgborder"}Liquid 사용 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecompathdynamic-personalization-with-liquid-stylefloatrightwidth120pxborder0-classnoimgborderuse-liquid}

> 이 문서에서는 다양한 사용자 속성을 활용하여 메시징에 개인 정보를 동적으로 삽입하는 방법을 설명합니다.

Liquid는 Shopify에서 개발하고 Ruby로 작성된 오픈소스 템플릿 언어입니다. Braze에서 Liquid를 사용하면 고객 프로필 데이터를 메시지에 가져와 해당 데이터를 커스터마이즈할 수 있습니다. 예를 들어, Liquid 태그를 사용하여 사용자의 가입 기념일에 따라 다른 혜택을 보내는 등의 조건부 메시지를 만들 수 있습니다. 또한 필터를 사용하면 사용자의 등록 날짜를 타임스탬프에서 "2022년 1월 15일"과 같이 더 읽기 쉬운 형식으로 변환하는 등 데이터를 조작할 수 있습니다. Liquid 구문과 기능에 대한 자세한 내용은 [지원되는 개인화 태그]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)를 참조하세요.

## 작동 방식 {#how-it-works}

Liquid 태그는 메시지에서 입력 안내 역할을 하며, 사용자 계정에서 동의된 정보를 가져와 개인화 및 관련 메시징 관행을 가능하게 합니다.

다음 블록에서는 사용자의 이름을 호출하는 Liquid 태그의 이중 사용과 사용자의 이름이 등록되어 있지 않은 경우를 위한 기본값 태그를 확인할 수 있습니다.

{% raw %}
```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```
{% endraw %}

Janet Doe라는 사용자에게 메시지는 다음과 같이 표시됩니다:

```
Hi Janet, thanks for using the App!
```

또는...

```
Hi Valued User, thanks for using the App!
```

{% alert important %}
HTML 주석(`<!-- -->`)은 Liquid가 읽히기 전에 제거되므로, HTML 주석 내의 Liquid 태그는 메시지에 렌더링되지 **않습니다**. 올바르게 렌더링하려면 사용하려는 모든 Liquid 태그가 HTML 주석 밖에 있는지 확인하세요.
{% endalert %}

## 대체할 수 있는 지원 값 {#supported-values-to-substitute}

가용성에 따라 다음 값을 메시지에 대체할 수 있습니다:

- [기본 사용자 정보]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags) (예: `first_name`, `last_name`, `email_address`)
- [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)
    - [중첩 커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support#liquid-templating)
- [커스텀 이벤트 속성정보]({{site.baseurl}}/user_guide/data/activation/events/custom_events)
- [가장 최근에 사용한 기기 정보]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#most-recently-used-device-information)
- [타겟 기기 정보]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#targeted-device-information)

Braze [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)를 통해 웹 서버에서 직접 콘텐츠를 가져올 수도 있습니다.

{% alert important %}
Braze는 현재 Shopify의 Liquid 5까지 지원합니다.
{% endalert %}

## Liquid 사용하기 {#using-liquid}

[Liquid 태그]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)를 사용하면 개인적인 터치를 더해 메시지의 품질을 높일 수 있습니다.

### Liquid 구문 {#liquid-syntax}

Liquid는 동적 개인화를 작성할 때 염두에 두어야 할 특정 구조, 즉 구문을 따릅니다. 다음은 기억해야 할 몇 가지 기본 규칙입니다:

1. **Braze에서는 직선 따옴표를 사용하세요:** 곡선 따옴표(**' '**)와 직선 따옴표(**&#39; &#39;**)에는 차이가 있습니다. Braze의 Liquid에서는 직선 따옴표(**&#39; &#39;**)를 사용하세요. 특정 텍스트 편집기에서 복사하여 붙여넣을 때 곡선 따옴표가 나타날 수 있으며, 이로 인해 Liquid에 문제가 발생할 수 있습니다. Braze 대시보드에 직접 따옴표를 입력하면 문제가 없습니다!
2. **괄호는 쌍으로 사용합니다:** 모든 괄호는 열고 닫아야 합니다 **{ }**. 반드시 중괄호를 사용하세요!
3. **if 문은 쌍으로 사용합니다:** 모든 `if`에는 `if` 문이 끝났음을 나타내는 `endif`가 필요합니다.
4. **case 문은 쌍으로 사용합니다:** 모든 `case`에는 블록을 닫는 `endcase`가 필요합니다.
5. **변수 이름에는 ASCII 문자를 사용해야 합니다:** Liquid 변수 이름(`assign` 또는 `capture`로 생성)은 ASCII 문자, 숫자, 밑줄만 지원합니다. Braze 개인화 속성 이름(`custom_attribute.${...}` 또는 `event_properties.${...}` 내부)에는 비ASCII 문자를 포함할 수 있습니다.

#### 연산자와 필터를 사용할 수 있는 위치 {#where-to-use-operators-and-filters}

연산자(`==`, `!=`, `>`, `and`, `or` 등)와 필터(`| size`, `| plus` 등)는 각각 특정 Liquid 컨텍스트에서만 사용할 수 있습니다.

| 컨텍스트 | 연산자 | 필터 |
|-----------|-----------|---------|
| `assign` | 지원되지 않음 | 지원됨 |
| `if`, `elsif`, `unless` | 지원됨 | 지원되지 않음 |
| `case`, `when` | 동등 비교만 가능[^case_when_ops] | 지원되지 않음 |
| `for` | 지원되지 않음 | 지원되지 않음 |
| 배열 접근 (`[ ]`) | 지원되지 않음 | 지원되지 않음 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="연산자와 필터를 사용할 수 있는 위치" }

[^case_when_ops]: `case`와 `when` 태그에서 Liquid는 `case` 표현식을 각 `when` 값과 동등 비교(equality)를 사용하여 비교합니다(`if`와 `elsif`를 `==`로 연결하는 것과 유사). `when` 절 내에서는 `if`와 `elsif`에서처럼 임의의 비교 또는 논리 연산자를 사용할 수 없습니다. 예시는 [조건부 메시징 로직]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic#case-and-when)을 참조하세요.

필터를 지원하지 않는 컨텍스트에서 필터링된 값이 필요한 경우, 먼저 결과를 변수에 할당하세요.

{% raw %}

##### 조건문에서 필터 결과 사용하기 {#use-a-filter-result-in-a-conditional}

조건문에서 필터를 직접 사용할 수 없습니다. 다음은 잘못된 예입니다:

```liquid
{% if my_array | size > 3 %}
You have more than 3 items!
{% endif %}
```

대신 필터 결과를 변수에 할당하세요:

```liquid
{% assign array_size = my_array | size %}
{% if array_size > 3 %}
You have more than 3 items!
{% endif %}
```

##### for 루프에서 필터 결과 사용하기 {#use-a-filter-result-in-a-for-loop}

`for` 루프의 반복 가능 항목에 필터를 적용할 수 없습니다. 다음은 잘못된 예입니다:

```liquid
{% for item in my_array | reverse %}
{{ item }}
{% endfor %}
```

대신 필터링된 값을 변수에 할당하세요:

```liquid
{% assign reversed = my_array | reverse %}
{% for item in reversed %}
{{ item }}
{% endfor %}
```

##### 배열 접근에 필터 결과 사용하기 {#use-a-filter-result-for-array-access}

대괄호 안에서 필터를 사용할 수 없습니다. 다음은 잘못된 예입니다:

```liquid
{{ my_array[my_var | minus: 1] }}
```

대신 먼저 필터링된 값을 할당하세요:

```liquid
{% assign adjusted_index = my_var | minus: 1 %}
{{ my_array[adjusted_index] }}
```

##### 비교 결과를 변수에 저장하기 {#store-a-comparison-result-in-a-variable}

`assign` 문에서 연산자를 사용할 수 없습니다. 다음은 잘못된 예입니다:

```liquid
{% assign is_vip = total_spend > 100 %}
{% if is_vip %}
Welcome to the VIP lounge!
{% endif %}
```

대신 조건문을 사용하여 변수를 설정하세요:

```liquid
{% assign is_vip = false %}
{% if total_spend > 100 %}
{% assign is_vip = true %}
{% endif %}

{% if is_vip %}
Welcome to the VIP lounge!
{% endif %}
```

{% endraw %}

#### 기본 속성과 커스텀 속성 {#default-attributes-and-custom-attributes}

{% raw %}

메시지에 `{{${first_name}}}`라는 텍스트를 포함하면, 메시지가 전송될 때 사용자의 이름(고객 프로필에서 가져옴)이 대체됩니다. 다른 기본 사용자 속성에도 동일한 형식을 사용할 수 있습니다.

커스텀 속성의 값을 사용하려면 변수에 "custom_attribute" 네임스페이스를 추가해야 합니다. 예를 들어, "zip code"라는 커스텀 속성을 사용하려면 메시지에 `{{custom_attribute.${zip code}}}`를 포함하면 됩니다.

### 태그 삽입하기 {#inserting-tags}

메시지에서 두 개의 여는 중괄호 `{{`를 입력하면 태그를 삽입할 수 있으며, 입력하는 동안 계속 업데이트되는 자동 완성 기능이 트리거됩니다. 입력하면서 나타나는 옵션에서 변수를 선택할 수도 있습니다.

커스텀 태그를 사용하는 경우 원하는 메시지에 태그를 복사하여 붙여넣을 수 있습니다.

#### 이중 괄호 예외 사항 {#exceptions-for-double-brackets}

`{% assign %}` 또는 `{% if %}`와 같은 다른 Liquid 태그 내에서 태그를 사용하는 경우 이중 괄호를 사용하거나 괄호 없이 사용할 수 있습니다. 태그가 단독으로 사용될 때만 이중 괄호로 감싸야 합니다. 간단하게 하려면 항상 이중 괄호를 사용하면 됩니다.

다음 태그는 모두 올바릅니다:

```liquid
{% if custom_attribute.${Number_Game_Attended} == 1 %}
{% if {{custom_attribute.${Number_Game_Attended}}} == 1 %}

{% assign value_one = {{custom_attribute.${one}}} %}
{% assign value_one = custom_attribute.${one} %}
```

{% endraw %}

{% alert note %}

이메일 메시지에서 Liquid를 사용하는 경우 다음 사항을 확인하세요:

1. 클래식 편집기가 아닌 HTML 편집기를 사용하여 삽입하세요. 클래식 편집기는 Liquid를 일반 텍스트로 구문 분석할 수 있습니다. 예를 들어, Liquid가 사용자의 이름을 템플릿에 적용하는 대신 {% raw %}`Hi {{ ${first_name} }}, thanks for using our service!`{% endraw %}로 구문 분석될 수 있습니다.
2. Liquid 코드는 `<body>` 태그 내에만 배치하세요. 이 태그 밖에 배치하면 전달 시 일관되지 않은 렌더링이 발생할 수 있습니다.

{% endalert %}

### HTML 편집기와 클래식 편집기 간 전환 {#switching-between-html-and-classic-editors}

HTML 편집기와 클래식 편집기 간에 전환하면 Liquid 스니펫과 Content Blocks의 위치가 메시지 내에서 변경될 수 있습니다. 편집기를 전환한 후 템플릿을 검토하세요. 보다 예측 가능한 레이아웃 제어가 필요한 경우 드래그 앤 드롭 편집기를 사용하세요.

### 사전 서식이 지정된 변수 삽입하기 {#inserting-pre-formatted-variables}

템플릿 텍스트 필드 근처에 있는 **개인화 추가** Modal을 통해 기본값이 포함된 사전 서식 변수를 삽입할 수 있습니다.

![개인화 삽입을 선택한 후 나타나는 개인화 추가 Modal. 이 Modal에는 개인화 유형, 속성, 선택적 기본값 필드가 있으며 Liquid 구문의 미리보기가 표시됩니다.]({% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}){: style="max-width:90%;"}

Modal은 커서가 있던 위치에 지정된 기본값과 함께 Liquid를 삽입합니다. 삽입 지점은 미리보기 상자에서도 지정되며, 이전 텍스트와 이후 텍스트가 표시됩니다. 텍스트 블록이 강조 표시된 경우 강조 표시된 텍스트가 대체됩니다.

![사용자가 기본값으로 "fellow traveler"를 입력하고, Modal이 작성기에서 강조 표시된 텍스트 "name"을 Liquid 스니펫으로 대체하는 개인화 추가 Modal의 GIF.]({% image_buster /assets/img_archive/insert_var_shot.gif %})