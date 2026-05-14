---
nav_title: 튜토리얼
article_title: "튜토리얼: Liquid 코드 작성하기"
page_order: 11
description: "이 참조 페이지에는 Liquid 코드를 시작하는 데 도움이 되는 초보자 친화적인 튜토리얼이 포함되어 있습니다."
page_type: tutorial
---

# 튜토리얼: Liquid 코드 작성하기 {#tutorials-writing-liquid-code}

> Liquid가 처음이신가요? 이 튜토리얼은 초보자 친화적인 사용 사례를 위한 Liquid 코드 작성을 시작하는 데 도움이 됩니다. 각 튜토리얼은 조건 로직과 Operator 등 다양한 학습 목표 조합을 다룹니다.

이 튜토리얼을 완료하면 다음을 할 수 있습니다:

- 일반적인 사용 사례를 위한 Liquid 코드 작성
- Liquid 조건 로직을 연결하여 사용자 데이터를 기반으로 메시지 개인화
- 변수와 필터를 사용하여 속성 값을 활용하는 수식 작성
- Liquid 코드의 기본 명령어를 인식하고 코드가 수행하는 작업에 대한 전반적인 이해 형성

| 튜토리얼 | 학습 목표 |
| --- | --- |
| [사용자 세그먼트별 메시지 개인화](#segments) | 기본값, 조건 로직 |
| [유기한 장바구니 리마인더](#reminders) | Operator, 조건 로직 |
| [이벤트 카운트다운](#countdown) | 변수, 날짜 필터 |
| [월별 생일 메시지](#birthday) | 변수, 날짜 필터, Operator |
| [좋아하는 제품 프로모션](#favorite-product) | 변수, 날짜 필터, 수식, Operator |
{: .reset-br-td-1 .reset-br-td-2 aria-label="Tutorials: Writing Liquid code" }

## 사용자 세그먼트별 개인화된 메시지 {#segments}

VIP 고객과 신규 가입자 등 다양한 사용자 세그먼트에 맞게 메시지를 커스터마이즈해 보겠습니다.

1. 사용자의 이름이 있는 경우와 없는 경우에 보낼 개인화된 인사말이 포함된 메시지를 작성합니다. 이를 위해 `first_name` 속성과 `first_name`이 비어 있을 때 사용할 기본값을 포함하는 Liquid 태그를 생성합니다. 이 시나리오에서는 기본값으로 "traveler"를 사용하겠습니다.

{% raw %}
```liquid
Happy summer, {{${first_name} | default: "traveler"}}!
```
{% endraw %}

{: start="2"}
2. 이제 사용자가 VIP 고객인 경우 보낼 메시지를 작성하겠습니다. 이를 위해 조건 로직 태그 `if`를 사용해야 합니다. 이 태그는 `vip_status` 커스텀 속성이 `VIP`와 같으면 다음 Liquid가 실행된다는 것을 의미합니다. 이 경우 특정 메시지가 전송됩니다.

{% raw %}
```liquid
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
```
{% endraw %}

{: start="3"}
3. 신규 가입자인 사용자에게 커스터마이즈된 메시지를 보내겠습니다. 조건 로직 태그 `elsif`를 사용하여 사용자의 `vip_status`가 `new`인 경우 다음 메시지가 전송되도록 지정합니다.

{% raw %}
```liquid
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
```
{% endraw %}

{: start="4"}
4. VIP도 아니고 신규도 아닌 사용자는 어떻게 할까요? `else` 태그를 사용하여 이전 조건이 충족되지 않은 경우 다음 메시지를 보내도록 지정할 수 있습니다. 그런 다음 더 이상 고려할 VIP 상태가 없으므로 `endif` 태그로 조건 로직을 닫습니다.

{% raw %}
```liquid
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}
```
{% endraw %}

{% details 전체 Liquid 코드 %}
{% raw %}
```liquid
Happy summer, {{${first_name} | default: "traveler"}}!
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}
```
{% endraw %}
{% enddetails %}

## 유기한 장바구니 리마인더 {#reminders}

장바구니에 남아 있는 항목을 사용자에게 알리는 개인화된 메시지를 보내겠습니다. 장바구니에 있는 항목 수에 따라 추가로 커스터마이즈하여, 항목이 3개 이하인 경우 모든 항목을 나열하고, 3개를 초과하는 경우 더 간결한 메시지를 보냅니다.

1. "같지 않음"을 의미하는 Operator `!=`를 사용하여 Liquid 조건 로직을 열어 사용자의 장바구니가 비어 있는지 확인합니다. 이 경우 커스텀 속성 `cart_items`가 빈 값이 아닌 조건을 설정합니다.

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
```
{% endraw %}

{: start="2"}
2. 그런 다음 "보다 큰"을 의미하는 Operator `>`를 사용하여 장바구니에 3개를 초과하는 항목이 있는지 확인해야 합니다.

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
```
{% endraw %}

{: start="3"}
3. 사용자의 이름으로 인사하는 메시지를 작성하되, 이름을 사용할 수 없는 경우 기본값으로 "there"를 사용합니다. 장바구니에 3개를 초과하는 항목이 있는 경우 표시할 내용을 포함합니다. 사용자에게 전체 목록을 보여주는 것은 부담스러울 수 있으므로 처음 3개의 `cart_items`만 나열합니다.

{% raw %}
```liquid
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
```
{% endraw %}

{: start="4"}
4. `else` 태그를 사용하여 이전 조건이 충족되지 않은 경우(즉, `cart_items`가 비어 있거나 3개 이하인 경우) 어떻게 할지 지정한 다음 보낼 메시지를 작성합니다. 3개의 항목은 많은 공간을 차지하지 않으므로 모두 나열할 수 있습니다. Liquid Operator `join`과 `,`를 사용하여 항목을 쉼표로 구분하여 나열하도록 지정합니다. `endif`로 로직을 닫습니다.

{% raw %}
```liquid
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you.
{% endif %}
```
{% endraw %}

{: start="5"}
5. `else`를 사용한 다음 `abort_message`를 사용하여 장바구니가 이전 조건을 충족하지 않는 경우(즉, 장바구니가 비어 있는 경우) Liquid 코드가 메시지를 보내지 않도록 합니다. `endif`로 로직을 닫습니다.

{% raw %}
```liquid
{% else %}
{% abort_message('No items in cart') %}
{% endif %}
```
{% endraw %}

{% details 전체 Liquid 코드 %}
{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you.
{% endif %}
{% else %}
{% abort_message('No items in cart') %}
{% endif %}
```
{% endraw %}
{% enddetails %}

## 이벤트 카운트다운 {#countdown}

기념일 세일까지 남은 일수를 알려주는 메시지를 사용자에게 보내겠습니다. 이를 위해 변수를 사용하여 속성 값을 조작하는 수식을 만들겠습니다.

1. 먼저 변수 `sale_date`를 커스텀 속성 `anniversary_date`에 할당하고 `date: "s"` 필터를 적용합니다. 이렇게 하면 `anniversary_date`가 초 단위로 표현되는 타임스탬프 형식으로 변환된 다음 해당 값이 `sale_date`에 할당됩니다.

{% raw %}
```liquid
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
```
{% endraw %}

{: start="2"}
2. 오늘의 타임스탬프를 캡처하는 변수도 할당해야 합니다. 변수 `today`를 `now`(현재 날짜 및 시간)에 할당한 다음 `date: "%s"` 필터를 적용합니다.

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
```
{% endraw %}

{: start="3"}
3. 이제 현재(`today`)와 기념일 세일(`sale_date`) 사이의 초 수를 계산합니다. 이를 위해 변수 `difference`를 `sale_date`에서 `today`를 뺀 값으로 할당합니다.

{% raw %}
```liquid
{% assign difference =  event_date | minus: today %}
```
{% endraw %}

{: start="4"}
4. 이제 `difference`를 메시지에서 참조할 수 있는 값으로 변환해야 합니다. 세일까지 몇 초가 남았는지 사용자에게 알려주는 것은 적절하지 않기 때문입니다. `difference_days`를 `event_date`에 할당하고 `86400`으로 나누어 일수를 구합니다.

{% raw %}
```liquid
{% assign difference_days = difference | divided_by: 86400 %}
```
{% endraw %}

{: start="5"}
5. 마지막으로 보낼 메시지를 작성합니다.

{% raw %}
```liquid
Get ready! Our Anniversary Sale is in {{ difference_days }} days!
```
{% endraw %}

{% details 전체 Liquid 코드 %}
{% raw %}
```liquid
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
{% assign today =  'now' | date: "%s"  %}
{% assign difference =  event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
Get ready! Our Anniversary Sale is in {{ difference_days }} days!
```
{% endraw %}
{% enddetails %}

## 월별 생일 메시지 {#birthday}

이번 달에 생일이 있는 모든 사용자에게 특별 프로모션을 보내겠습니다. 이번 달에 생일이 없는 사용자는 메시지를 받지 않습니다.

1. 먼저 이번 달을 가져옵니다. 변수 `this_month`를 `now`(현재 날짜 및 시간)에 할당한 다음 `date: "%B"` 필터를 사용하여 변수가 월과 같도록 지정합니다.

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
```
{% endraw %}

{: start="2"}
2. 이제 사용자의 `date_of_birth`에서 생일 월을 가져옵니다. 변수 `birth_month`를 `date_of_birth`에 할당한 다음 `date: "%B"` 필터를 사용합니다.

{% raw %}
```liquid
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
```
{% endraw %}

{: start="3"}
3. 이제 월 값을 가진 두 변수가 있으므로 조건 로직으로 비교할 수 있습니다. `this_month`가 사용자의 `birth_month`와 같은 조건을 설정합니다.

{% raw %}
```liquid
{% if {{this_month}} == {{birth_month}} %}
```
{% endraw %}

{: start="4"}
4. 이번 달이 사용자의 생일 월인 경우 보낼 메시지를 작성합니다.

{% raw %}
```liquid
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.
```
{% endraw %}

{: start="5"}
5. `else` 태그를 사용하여 조건이 충족되지 않은 경우(이번 달이 사용자의 생일 월이 아닌 경우) 어떻게 할지 지정합니다.

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="6"}
6. 사용자의 생일 월이 이번 달이 아닌 경우 메시지를 보내지 않으려면 `abort_message`를 사용하여 메시지를 취소한 다음 `endif`로 조건 로직을 닫습니다.

{% raw %}
```liquid
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}

{% details 전체 Liquid 코드 %}
{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
{% if {{this_month}} == {{birth_month}} %}
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.
{% else %}
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}
{% enddetails %}

## 좋아하는 제품 프로모션 {#favorite-product}

마지막 구매일이 6개월 이상 지난 사용자에게 좋아하는 제품을 프로모션해 보겠습니다.

1. 먼저 조건 로직을 사용하여 사용자의 좋아하는 제품과 마지막 구매일이 있는지 확인합니다.

{% raw %}
```liquid
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}
```
{% endraw %}

{: start="2"}
2. 그런 다음 사용자의 좋아하는 제품이나 마지막 구매일이 없는 경우 메시지를 보내지 않도록 지정합니다.

{% raw %}
```liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="3"}
3. `else`를 사용하여 위의 조건이 충족되지 않은 경우(사용자의 좋아하는 제품과 마지막 구매일이 _있는_ 경우) 어떻게 할지 지정합니다.

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="4"}
4. 구매일이 있는 경우 오늘 날짜와 비교할 수 있도록 변수에 할당해야 합니다. 먼저 변수 `today`를 `now`(현재 날짜 및 시간)에 할당하고 `date: "%s"` 필터를 사용하여 값을 초 단위로 표현되는 타임스탬프 형식으로 변환하여 오늘 날짜의 값을 만듭니다. `plus: 0` 필터를 추가하여 타임스탬프에 "0"을 더합니다. 이는 타임스탬프의 값을 변경하지 않지만 향후 수식에서 타임스탬프를 사용하는 데 유용합니다.


{% raw %}
```liquid
{% assign today = 'now' | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="5"}
5. 이제 변수 `last_purchase_date`를 커스텀 속성 `last_purchase_date`에 할당하고 `date: "s"` 필터를 사용하여 마지막 구매일을 초 단위로 캡처합니다. 다시 `plus: 0` 필터를 추가합니다.

{% raw %}
```liquid
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="6"}
6. 마지막 구매일과 오늘 날짜가 초 단위이므로 6개월이 몇 초인지 계산해야 합니다. 수식(약 6개월 * 30.44일 * 24시간 * 60분 * 60초)을 만들어 변수 `six_months`에 할당합니다. `times`를 사용하여 시간 단위의 곱셈을 지정합니다.

{% raw %}
```liquid
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}
```
{% endraw %}

{: start="7"}
7. 이제 모든 시간 값이 초 단위이므로 수식에서 해당 값을 사용할 수 있습니다. 오늘의 값에서 `last_purchase_date`를 빼는 `today_minus_last_purchase_date`라는 변수를 할당합니다. 이렇게 하면 마지막 구매 이후 경과한 초 수를 알 수 있습니다.

{% raw %}
```liquid
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}
```
{% endraw %}

{: start="8"}
8. 이제 조건 로직에서 시간 값을 직접 비교합니다. `today_minus_last_purchase_date`가 6개월 이상(`>=`)인 조건을 정의합니다. 즉, 마지막 구매일이 최소 6개월 전이라는 의미입니다.

{% raw %}
```liquid
{% if today_minus_last_purchase_date >= six_months %}
```
{% endraw %}

{: start="9"}
9. 마지막 구매가 최소 6개월 전인 경우 보낼 메시지를 작성합니다.

{% raw %}
```liquid
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?
```
{% endraw %}

{: start="10"}
10. `else` 태그를 사용하여 조건이 충족되지 않은 경우(구매가 최소 6개월 전이 아닌 경우) 어떻게 할지 지정합니다.

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="11"}
11. `abort_message`를 포함하여 메시지를 취소합니다.

{% raw %}
```liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="12"}
12. 마지막으로 두 개의 `endif` 태그로 Liquid를 종료합니다. 첫 번째 `endif`는 좋아하는 제품 또는 마지막 구매일에 대한 조건 확인을 닫고, 두 번째 `endif`는 마지막 구매일이 최소 6개월 전인지에 대한 조건 확인을 닫습니다.

{% raw %}
```liquid
{% endif %}
{% endif %}
```
{% endraw %}

{% details 전체 Liquid 코드 %}
{% raw %}
```liquid
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}
{% abort_message("No favorite product or last purchase date") %}
{% else %}
{% assign today = 'now' | date: "%s" | plus: 0 %}
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}
{% if today_minus_last_purchase_date >= six_months %}
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?
{% else %}
{% abort_message("Last purchase was less than six months ago") %}
{% endif %}
{% endif %}
```
{% endraw %}
{% enddetails %}