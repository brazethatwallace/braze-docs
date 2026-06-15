---
nav_title: 기본값 설정
article_title: Liquid 기본값 설정
page_order: 5
description: "이 참조 문서에서는 메시지에서 사용하는 개인화 속성에 대해 기본 대체 값을 설정하는 방법을 다룹니다."

---

# 기본값 설정

{% raw %}

> 메시지에서 사용하는 모든 개인화 속성에 기본 대체 값을 설정할 수 있습니다. 이 문서에서는 기본값의 작동 방식, 설정 방법, 그리고 메시지에서 사용하는 방법을 다룹니다.

## 작동 방식

기본값은 "default"라는 이름의 [Liquid 필터](http://docs.shopify.com/themes/liquid-documentation/filters)를 지정하여 추가할 수 있습니다(아래와 같이 `|`를 사용하여 인라인으로 필터를 구분합니다).

```
| default: 'Insert Your Desired Default Here'
```

기본값이 제공되지 않고 해당 필드가 사용자에게 없거나 설정되지 않은 경우, 메시지에서 해당 필드는 비어 있게 됩니다.

다음 예시는 기본값을 추가하는 올바른 구문을 보여줍니다. 이 경우, 사용자의 `first_name` 필드가 비어 있거나 사용할 수 없으면 "Valued User"라는 단어가 `{{ ${first_name} }}` 속성을 대체합니다.

```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```

Janet Doe라는 사용자에게 메시지는 다음 중 하나로 표시됩니다:

```
Hi Janet, thanks for using the App!
```

또는...

```
Hi Valued User, thanks for using the App!
```
{% endraw %}

{% alert important %}
기본값은 빈 값(empty value)에 대해 표시되지만, 공백 값(blank value)에 대해서는 표시되지 않습니다. 빈 값은 아무것도 포함하지 않는 반면, 공백 값은 공백 문자(예: 스페이스)만 포함하고 다른 문자는 포함하지 않습니다. 예를 들어, 빈 문자열은 `""`처럼 보이고 공백 문자열은 `" "`처럼 보일 수 있습니다.
{% endalert %}

## 다양한 데이터 유형에 대한 기본값 설정

위의 예시는 문자열에 대한 기본값을 설정하는 방법을 보여줍니다. `empty`, `nil`(정의되지 않음), 또는 `false` 값을 가지는 모든 Liquid 데이터 유형에 대해 기본값을 설정할 수 있으며, 여기에는 문자열, 부울, 배열, 오브젝트, 숫자가 포함됩니다.

### 사용 사례: 부울

`premium_user`라는 부울 커스텀 속성이 있고 사용자의 프리미엄 상태에 따라 개인화된 메시지를 보내려 한다고 가정해 보겠습니다. 일부 사용자는 프리미엄 상태가 설정되어 있지 않으므로, 해당 사용자를 포함하기 위해 기본값을 설정해야 합니다.

1. `is_premium_user`라는 변수를 `premium_user` 속성에 할당하고 기본값을 `false`로 설정합니다. 이는 `premium_user`가 `nil`인 경우 `is_premium_user`의 값이 기본적으로 `false`가 된다는 의미입니다.

{% raw %}
```liquid
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
```

{: start="2"}
2. 그런 다음, 조건 로직을 사용하여 `is_premium_user`가 `true`인 경우 보낼 메시지를 지정합니다. 즉, `premium_user`가 `true`인 경우 무엇을 보낼지 지정합니다. 사용자의 이름이 없는 경우를 대비하여 사용자의 이름에도 기본값을 할당합니다.

```liquid
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
```

{: start="3"}
3. 마지막으로, `is_premium_user`가 `false`인 경우(즉, `premium_user`가 `false`이거나 `nil`인 경우) 보낼 메시지를 지정합니다. 그런 다음 조건 로직을 닫습니다.

```liquid
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}
```
{% endraw %}

{% details 전체 Liquid 코드 %}
{% raw %}
```liquid
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}
```
{% endraw %}
{% enddetails %}

### 사용 사례: 숫자

`reward_points`라는 숫자 커스텀 속성이 있고 사용자의 리워드 포인트가 포함된 메시지를 보내려 한다고 가정해 보겠습니다. 일부 사용자는 리워드 포인트가 설정되어 있지 않으므로, 해당 사용자를 처리하기 위해 기본값을 설정해야 합니다.

1. 사용자의 이름 또는 이름이 없는 경우 `Valued User`라는 기본값으로 메시지를 시작합니다.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2. `reward_points`라는 커스텀 속성을 사용하고 기본값을 `0`으로 설정하여 사용자가 보유한 리워드 포인트 수로 메시지를 마무리합니다. `reward_points`가 `nil` 값인 모든 사용자는 메시지에서 리워드 포인트가 `0`으로 표시됩니다.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}}, you have {{custom_attribute.${reward_points} | default: 0}} reward points.
```
{% endraw %}

### 사용 사례: 오브젝트

`city`와 `state` 등록정보를 포함하는 `location`이라는 중첩 고객 속성 오브젝트가 있다고 가정해 보겠습니다. 이러한 등록정보 중 하나라도 설정되지 않은 경우, 사용자에게 해당 정보를 제공하도록 안내하려 합니다.

1. 사용자의 이름으로 인사하고, 이름이 없는 경우를 대비하여 기본값을 포함합니다.

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2. 사용자의 위치를 확인하고 싶다는 메시지를 작성합니다.

{% raw %}
```liquid
We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.
```
{% endraw %}

{: start="3"}
3. 사용자의 위치를 메시지에 삽입하고, 주소 등록정보가 설정되지 않은 경우를 위한 기본값을 할당합니다.

{% raw %}
```liquid
Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}
```
{% endraw %}

{% details 전체 Liquid 코드 %}
{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}}

We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.

Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}
```
{% endraw %}
{% enddetails %}

### 사용 사례: 배열

`destination`과 `departure_date` 등록정보를 가진 여행 정보가 포함된 `upcoming_trips`라는 배열 커스텀 속성이 있다고 가정해 보겠습니다. 사용자에게 예정된 여행이 있는지 여부에 따라 개인화된 메시지를 보내려 합니다.

1. `upcoming_trips`가 `empty`인 경우 메시지를 보내지 않도록 조건 로직을 작성합니다.

{% raw %}
```liquid
{% if {{custom_attribute.${upcoming_trips}}} == empty %}
{% abort_message('No upcoming trips scheduled') %}
```
{% endraw %}

{: start="2"}
2. `upcoming_trips`에 콘텐츠가 있는 경우 보낼 메시지를 지정합니다:<br><br>**2a.** 사용자에게 인사하고, 이름이 없는 경우를 대비하여 기본값을 포함합니다. <br>**2b.** `for` 태그를 사용하여 `upcoming_trips`에 포함된 각 여행의 등록정보(또는 정보)를 가져오도록 지정합니다. <br>**2c.** 메시지에 등록정보를 나열하고, `departure_date`가 설정되지 않은 경우를 위한 기본값을 포함합니다. (여행이 생성되려면 `destination`이 필수이므로, 해당 항목에는 기본값을 설정할 필요가 없다고 가정합니다.)<br>**2d.** `for` 태그를 닫은 다음 조건 로직을 닫습니다.

{% raw %}
```liquid
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
  Here are your upcoming trips:
  <ul>
  {% for trip in {{custom_attribute.${upcoming_trips}}} %}
    <li>
      Destination: {{trip.destination}}
      Departure Date: {{trip.departure_date | default: 'Date not set'}}
    </li>
  {% endfor %}
  </ul>
{% endif %}
```
{% endraw %}

{% details 전체 Liquid 코드 %}
{% raw %}
```liquid
{% if {{custom_attribute.${upcoming_trips}}} == blank %}
{% abort_message('No upcoming trips scheduled') %}
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
  Here are your upcoming trips:
  <ul>
  {% for trip in {{custom_attribute.${upcoming_trips}}} %}
    <li>
      Destination: {{trip.destination}}
      Departure Date: {{trip.departure_date | default: 'Date not set'}}
    </li>
  {% endfor %}
  </ul>
{% endif %}
```
{% endraw %}
{% enddetails %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[37]:#accounting-for-null-attribute-values