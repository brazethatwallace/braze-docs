---
nav_title: 조건부 메시징 로직
article_title: 조건부 Liquid 메시징 로직
page_order: 6
description: "이 참조 문서에서는 캠페인에서 태그를 사용하는 방법과 사용해야 하는 경우에 대해 설명합니다."

---

# 조건부 메시징 로직 {#conditional-messaging-logic}

> [태그](https://docs.shopify.com/themes/liquid-documentation/tags)를 사용하면 메시징 캠페인에 프로그래밍 로직을 포함할 수 있습니다. 태그는 조건문을 실행하거나 변수 할당, 코드 블록 반복과 같은 고급 사용 사례에 활용할 수 있습니다. <br><br>이 페이지에서는 null, nil, blank 속성 값을 처리하는 방법과 커스텀 속성을 참조하는 방법 등 태그를 사용하는 방법과 사용해야 하는 경우에 대해 설명합니다.

## 태그 서식 지정 {#formatting-tags}

{% raw %}
태그는 `{% %}`로 감싸야 합니다.
{% endraw %}

작업을 좀 더 쉽게 하기 위해, Braze는 Liquid 구문을 올바르게 작성하면 녹색과 보라색으로 활성화되는 색상 서식을 포함하고 있습니다. 녹색 서식은 태그를 식별하는 데 도움이 되며, 보라색 서식은 개인화가 포함된 영역을 강조합니다.

조건부 메시징을 사용하는 데 어려움이 있다면, 커스텀 속성 및 기타 Liquid 요소를 삽입하기 전에 먼저 조건 구문을 작성해 보세요.

예를 들어, 먼저 메시지 필드에 다음을 추가합니다:
{% raw %}
```liquid
{% if X >0 %}
{% else %}
{% endif %}
```

녹색으로 강조 표시되는지 확인한 다음, 메시지 필드 모서리에 있는 파란색 `+`를 사용하여 `X`를 선택한 Liquid 또는 연결된 콘텐츠로 바꾸고, `0`을 원하는 값으로 바꿉니다.
<br><br>
그런 다음 `else` 조건문 사이에 필요한 메시지 변형을 추가합니다:
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Thanks for purchasing! Here's another 10% off!
{% else %}
Buy now! Would 5% off convince you?
{% endif %}
```
{% endraw %}

## 조건 로직 {#conditional-logic}

메시지에 조건문과 같은 다양한 유형의 [지능형 로직](http://docs.shopify.com/themes/liquid-documentation/basics)을 포함할 수 있습니다. 다음 예제에서는 [조건문](http://docs.shopify.com/themes/liquid-documentation/tags/control-flow-tags)을 사용하여 캠페인을 국제화합니다:
{% raw %}

```liquid
{% if ${language} == 'en' %}
This is a message in English from Braze!
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
这是一条来自Braze的中文消息。
{% else %}
This is a message from Braze! This is going to go to anyone who did not match the other specified languages!
{% endif %}
```

### 조건 태그 {#conditional-tags}

#### `if`와 `elsif` {#if-and-elsif}

조건 로직은 확인할 첫 번째 조건을 명시하는 `if` 태그로 시작합니다. 이후 조건은 `elsif` 태그를 사용하며, 이전 조건이 충족되지 않은 경우에 확인됩니다. 이 예제에서 사용자의 기기가 영어로 설정되어 있지 않으면, 이 코드는 사용자의 기기가 스페인어로 설정되어 있는지 확인하고, 그것도 실패하면 기기가 중국어로 설정되어 있는지 확인합니다. 사용자의 기기가 이러한 조건 중 하나를 충족하면, 사용자는 해당 언어로 메시지를 받게 됩니다.

#### `else`

조건 로직에 `{% else %}` 문을 포함할 수 있습니다. 설정한 조건 중 어느 것도 충족되지 않으면, `{% else %}` 문이 전송할 메시지를 지정합니다. 이 예제에서는 사용자의 언어가 영어, 스페인어 또는 중국어가 아닌 경우 기본적으로 영어를 사용합니다.

#### `case`와 `when` {#case-and-when}

`{% case %}`, `{% when %}`, `{% endcase %}`는 switch 문처럼 작동합니다. `case` 뒤에 하나의 표현식을 설정하면, 각 `when` 분기는 해당 표현식이 나열된 값과 같을 때 실행됩니다(Liquid는 내부적으로 동등 비교를 사용하며, `if`와 `elsif`를 `==`로 연결하는 것과 유사합니다). 하나의 `when` 태그에 쉼표 또는 `or`로 구분하여 여러 값을 나열할 수 있습니다. 일치하는 항목이 없을 때의 대체 처리에는 `{% else %}`를 사용하고, `{% endcase %}`로 닫습니다.

`when` 값의 형식을 데이터 유형에 맞게 일치시켜야 합니다. 텍스트(예: 언어 코드)의 경우 따옴표를 사용합니다: `{% when 'es' %}`. 숫자의 경우 따옴표를 생략합니다: `{% when 2 %}`.

```liquid
{% assign handle = 'cake' %}
{% case handle %}
{% when 'cake' %}
This is a cake
{% when 'cookie' %}
This is a cookie
{% else %}
This is not a cake nor a cookie
{% endcase %}
```

`handle` 대신 Braze 개인화 태그나 다른 Liquid 표현식을 사용할 수 있습니다. 더 많은 구문 옵션은 Shopify의 [`case` 태그 문서](https://shopify.dev/docs/api/liquid/tags/case)를 참조하세요.

#### `endif`

`{% endif %}` 태그는 `if` 블록이 끝났음을 나타냅니다. 해당 체인에서 `if`, `elsif`, `unless` 또는 `else`를 사용하는 모든 메시지에 `{% endif %}` 태그를 포함해야 합니다. `{% endif %}` 태그를 포함하지 않으면, Braze가 메시지를 구문 분석할 수 없어 오류가 발생합니다. `{% case %}`를 사용하는 경우에는 `{% endif %}`가 아닌 `{% endcase %}`로 블록을 닫습니다.

{% alert note %}
`if`, `elsif`, `unless` 태그에서는 연산자를 사용할 수 있지만 필터는 사용할 수 없습니다. `case`와 `when` 태그에서는 `case` 표현식이 `when` 값과 같을 때 각 분기가 일치하며, 해당 표현식에서도 필터는 지원되지 않습니다. 필터링된 값을 평가하려면 먼저 필터 결과를 변수에 할당한 다음 `case` 또는 `when` 절에서 해당 변수를 참조하세요. 자세한 내용은 [연산자와 필터를 사용하는 위치]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#where-to-use-operators-and-filters)를 참조하세요.
{% endalert %}

### 튜토리얼: 위치 기반 콘텐츠 전달 {#tutorial-deliver-location-based-content}

이 튜토리얼을 완료하면 "if", "elsif", "else" 문과 함께 태그를 사용하여 사용자의 위치에 따라 콘텐츠를 전달할 수 있습니다.

1. 사용자의 도시가 뉴욕인 경우 전송할 메시지를 설정하기 위해 `if` 태그로 시작합니다. 사용자의 도시가 뉴욕이면 이 첫 번째 조건이 충족되고, 사용자는 뉴요커 정체성을 명시하는 메시지를 받게 됩니다.

```liquid
{% if ${city} == "New York" %}
  🎉 Hey there, New Yorker! We're excited to offer you a special deal!
  Get 20% off your next sandwich at your local Sandwich Emperor.
  Just show this message at the counter to redeem your offer!
```

{: start="2"}
2. 다음으로, `elseif` 태그를 사용하여 사용자의 도시가 로스앤젤레스인 경우 전송할 메시지를 설정합니다.

```liquid
{% elsif ${city} == "Los Angeles" %}
  🌞 Hello, Los Angeles! Enjoy a sunny day with a delicious sandwich!
  Present this message at our LA restaurant for a 20% discount on your next order!
```

{: start="3"}
3. 또 다른 `elseif` 태그를 사용하여 사용자의 도시가 시카고인 경우 전송할 메시지를 설정합니다.

```liquid
{% elsif ${city} == "Chicago" %}
  🍕 Chicago, we have a treat for you!
  Swing by our restaurant and get 20% off your favorite sandwich.
  Just show this message to our staff!
```

{: start="4"}
4. 이제 `{% else %}` 태그를 사용하여 사용자의 도시가 샌프란시스코, 뉴욕 또는 시카고가 아닌 경우 전송할 메시지를 지정합니다.

```liquid
{% else %}
 🥪 Craving a sandwich? Visit us at any of our locations for a delicious meal!
  Check our website for the nearest restaurant to you!
```

{: start="5"}
5. 마지막으로, `{% endif %}` 태그를 사용하여 조건 로직이 완료되었음을 지정합니다.

```liquid
{% endif %}
```

{% endraw %}

{% details 전체 Liquid 코드 %}

{% raw %}
```liquid
{% if ${city} == "New York City" %}
  🎉 Hey there, New Yorker! We're excited to offer you a special deal!
  Get 20% off your next sandwich at our New York location.
  Just show this message at the counter to redeem your offer!
{% elsif ${city} == "Los Angeles" %}
  🌞 Hello, Los Angeles! Enjoy a sunny day with a delicious sandwich!
  Present this message at our LA restaurant for a 20% discount on your next order!
{% elsif ${city} == "Chicago" %}
  🍕 Chicago, we have a treat for you!
  Swing by our restaurant and get 20% off your favorite sandwich.
  Just show this message to our staff!
{% else %}
  🥪 Craving a sandwich? Visit us at any of our locations for a delicious meal!
  Check our website for the nearest restaurant to you!
{% endif %}
```
{% endraw %}

{% enddetails %}

## null, nil, blank 속성 값 처리 {#accounting-for-null-nil-and-blank-attribute-values}

조건 로직은 고객 프로필에 설정되지 않은 속성 값을 처리하는 데 유용한 방법입니다.

### null 및 nil 속성 값 {#null-and-nil-attribute-values}

null 또는 nil 값은 커스텀 속성의 값이 설정되지 않았을 때 발생합니다. 예를 들어, 아직 이름을 설정하지 않은 사용자는 Braze에 이름이 기록되어 있지 않습니다.

경우에 따라 이름이 설정된 사용자와 이름이 설정되지 않은 사용자에게 완전히 다른 메시지를 보내고 싶을 수 있습니다.

다음 태그를 사용하면 "first name" 속성이 null인 사용자에게 보낼 메시지를 지정할 수 있습니다:

{% raw %}
```liquid
{% if ${first_name} == null %}
  ....
{% endif %}
```
{% endraw %}

![Braze 대시보드에서 null 'first name' 속성을 사용하는 예제 메시지.]({% image_buster /assets/img/value_null.png %}){: style="max-width:60%;"}

{% raw %}
```liquid
{% if ${first_name} == null %}
We're having a sale! Hurry up and get 10% off all items today only!
{% else %}
Hey {{${first_name} | default: 'there'}}, we're having a sale! Hurry up and get 10% off all items today only!
{% endif %}
```

null 속성 값은 값 유형과 엄격하게 연결되지 않습니다(예: "null" 문자열은 "null" 배열과 동일). 따라서 위 예제에서 null 속성 값은 설정되지 않은 이름을 참조하며, 이는 문자열에 해당합니다.

{% endraw %}

### blank 속성 값 {#blank-attribute-values}

blank 값은 고객 프로필의 속성이 설정되지 않았거나, 공백 문자열(` `)로 설정되었거나, `false`로 설정된 경우에 발생합니다. Liquid 처리 오류를 방지하려면 다른 변수보다 먼저 blank 값을 확인해야 합니다.

다음 태그를 사용하면 "first name" 속성이 blank인 사용자에게 보낼 메시지를 지정할 수 있습니다.

{% raw %}
```liquid
{% if ${first_name} == blank %}
  ....
{% endif %}
```
{% endraw %}

## 커스텀 속성 참조 {#referencing-custom-attributes}

[커스텀 속성을 생성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#managing-custom-attributes)한 후, Liquid 메시징에서 이러한 커스텀 속성을 참조할 수 있습니다.

조건 로직을 사용할 때는 올바른 구문을 사용하기 위해 커스텀 속성의 데이터 유형을 알아야 합니다. 대시보드의 **커스텀 속성** 페이지에서 커스텀 속성과 연결된 데이터 유형을 확인한 다음, 각 데이터 유형에 대해 나열된 다음 예제를 참조하세요.

![커스텀 속성의 데이터 유형 선택. 제공된 예제는 데이터 유형이 문자열인 Favorite_Category 속성을 보여줍니다.]({% image_buster /assets/img_archive/custom_attribute_data_type.png %}){: style="max-width:80%;"}

{% alert tip %}
문자열과 배열은 주위에 작은따옴표가 필요하지만, 부울과 정수에는 작은따옴표를 사용하지 않습니다.
{% endalert %}

### 부울 {#boolean}

[부울]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#booleans)은 이진 값으로, `registration_complete: true`와 같이 `true` 또는 `false`로 설정할 수 있습니다. 부울 값에는 작은따옴표를 사용하지 않습니다.

{% raw %}

```liquid
{% if {{custom_attribute.${registration_complete}}} == true %}
```

{% endraw %}

### 숫자 {#number}

[숫자]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#numbers)는 정수 또는 플로트가 될 수 있는 숫자 값입니다. 예를 들어, 사용자는 `shoe_size: 10` 또는 `levels_completed: 287`을 가질 수 있습니다. 숫자 값에는 작은따옴표를 사용하지 않습니다.

{% raw %}

```liquid
{% if {{custom_attribute.${shoe_size}}} == 10 %}
```

{% endraw %}

정수에 대해 미만(<) 또는 초과(>)와 같은 다른 [기본 연산자](https://shopify.dev/docs/themes/liquid/reference/basics/operators)도 사용할 수 있습니다:

{% raw %}

```liquid
{% if {{custom_attribute.${flyer_miles}}} >= 500 %}
```

{% endraw %}

### 문자열 {#string}

[문자열]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#strings)은 영숫자 문자로 구성되며 사용자에 대한 데이터를 저장합니다. 예를 들어, `favorite_color: red` 또는 `phone_number: 3025981329`가 있을 수 있습니다. 문자열 값에는 작은따옴표를 사용해야 합니다.

{% raw %}

```liquid
{% if {{custom_attribute.${favorite_color}}} == 'blue' %}
```

{% endraw %}

문자열의 경우 Liquid에서 "=="와 "contains"를 모두 사용할 수 있습니다.

### 배열 {#array}

[배열]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#arrays)은 사용자에 대한 정보 목록입니다. 예를 들어, 사용자는 `last_viewed_shows: stranger things, planet earth, westworld`를 가질 수 있습니다. 배열 값에는 작은따옴표를 사용해야 합니다.

{% raw %}

```liquid
{% if {{custom_attribute.${last_viewed_shows}}} contains 'homeland' %}
```

{% endraw %}

배열의 경우 "contains"를 사용해야 하며 "=="는 사용할 수 없습니다.

### 시간 {#time}

이벤트가 발생한 시점의 타임스탬프입니다. [시간]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes#time) 값은 조건 로직에서 사용하려면 [수학 필터]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters#math-filters)를 적용해야 합니다.

{% raw %}

```liquid
{% assign expire = {{custom_attribute.${subscription_end_date}}} | plus: 0 %}
```

{% endraw %}