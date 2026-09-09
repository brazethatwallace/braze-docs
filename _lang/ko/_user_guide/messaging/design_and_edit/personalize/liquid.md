---
nav_title: Liquid 참조
article_title: Liquid 참조
page_order: 3
layout: dev_guide
alias: /liquid/
search_rank: 3
guide_top_header: "Liquid 참조"
guide_top_text: "Liquid는 Shopify에서 만든 오픈소스 템플릿 언어로, Braze에서 동적 개인화를 구현하는 데 사용됩니다. 모든 사람에게 동일한 정적 메시지를 보내는 대신, Liquid를 사용하면 각 수신자의 프로필 데이터, 행동 또는 언어에 따라 콘텐츠가 변경되는 템플릿을 만들 수 있습니다. 이 섹션의 문서에서 지원되는 태그, 필터, 조건 로직, 기본값 및 일반적인 개인화 패턴을 확인하세요."
description: "이 랜딩 페이지에서는 지원되는 개인화 태그, 필터, 기본값 설정 등 Liquid에 관한 모든 내용을 다룹니다."

guide_featured_title: "섹션 문서"
guide_featured_list:
- name: Liquid 사용
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid
  image: /assets/img/braze_icons/beaker-02.svg
- name: 지원되는 개인화 태그
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags
  image: /assets/img/braze_icons/tag-01.svg
- name: 연산자
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/operators
  image: /assets/img/braze_icons/code-02.svg
- name: 필터
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/filters
  image: /assets/img/braze_icons/flag-02.svg
- name: 고급 필터
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters
  image: /assets/img/braze_icons/settings-01.svg
- name: 기본값 설정
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values
  image: /assets/img/braze_icons/table.svg
- name: 조건부 메시징 로직
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/conditional_logic
  image: /assets/img/braze_icons/columns-01.svg
- name: 메시지 중단
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: Liquid 사용 사례
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/liquid_use_cases
  image: /assets/img/braze_icons/list.svg
- name: 튜토리얼
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/tutorials
  image: /assets/img/braze_icons/book-open-01.svg
- name: 자주 묻는 질문
  link: /docs/user_guide/messaging/design_and_edit/personalize/liquid/faq
  image: /assets/img/braze_icons/annotation-question.svg

---

## Liquid에 대해 {#about-liquid}

Liquid는 메시지와 사용자 데이터 사이의 다리 역할을 합니다. 메시지를 보낼 때 Braze는 텍스트에서 Liquid 구문을 검색합니다. Liquid를 발견하면 해당 사용자에 맞는 관련 데이터를 가져와 메시지가 발송되기 전에 코드를 실제 값으로 대체합니다.

예를 들어, 정수 데이터 유형인 커스텀 속성을 고객 프로필에서 가져와 가장 가까운 정수로 반올림할 수 있습니다. Liquid 구문과 사용법에 대한 자세한 내용은 [**지원되는 개인화 태그**]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)를 참조하세요.

Liquid 템플릿 언어는 오브젝트, 태그, 필터의 사용을 지원합니다.

- [**오브젝트**]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid)를 사용하면 개인화된 속성을 메시지에 삽입할 수 있습니다.
- [**태그**]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)를 사용하면 메시징에 데이터를 삽입하고 조건 로직을 사용하여 특정 조건이 충족되었을 때 메시지를 보낼 수 있습니다. 예를 들어, 태그를 사용하여 "if" 문과 같은 지능적 로직을 Campaigns에 포함할 수 있습니다.
- [**필터**]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters)를 사용하면 개인화된 속성과 동적 콘텐츠의 형식을 변경할 수 있습니다. 예를 들어, [`date` 필터]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters#date-filter)를 사용하여 *2016-09-07 08:43:50 UTC*와 같은 타임스탬프를 *2016년 9월 7일*과 같은 날짜로 변환할 수 있습니다.

{% alert warning %}
Braze는 현재 Shopify의 Liquid를 100% 지원하지 않으며, 설명서에서 안내한 특정 부분만 지원합니다. 오류 또는 지원되지 않는 Liquid 사용 위험을 줄이기 위해 Liquid를 사용하는 모든 메시지를 발송 전에 테스트할 것을 강력히 권장합니다.
{% endalert %}

### Liquid 5 지원 {#liquid-5-support}

Braze는 **Shopify의 Liquid 5**까지 지원합니다. Liquid 구현은 구문 개인화 태그 유형과 공백 제어를 지원합니다. 특정 태그에 대한 자세한 내용은 [구문 태그]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags#syntax-tags)를 참조하세요.

메시징을 구성할 때 Liquid에서 사용할 수 있는 새로운 배열 및 수학 필터는 다음과 같습니다.
- `at_least`
- `at_most`
- `compact`
- `concat`
- `sort_natural`
- `where`

정의에 대한 자세한 내용은 [필터]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters)를 참조하세요.

## 알아야 할 용어 {#terms-to-know}

이 용어들은 [**Shopify 설명서**](https://shopify.github.io/liquid/basics/introduction/)에서 Braze의 지원 수준에 맞게 재해석되었습니다.

{% raw %}

| 용어 | 정의 | 예시 |
|---|---|---|
| Liquid | Shopify에서 개발하고 Ruby로 작성된 널리 사용되는 고객 대상 템플릿 언어로, 동적 콘텐츠를 로드하고 가져오는 데 사용됩니다. | `{{${first_name}}}`은 사용자의 이름을 메시지에 삽입합니다. |
| 오브젝트 | 변수와 의도한 변수 이름의 위치를 나타내며, 메시지에서 콘텐츠를 표시할 위치를 Liquid에 알려줍니다. | `{{${city}}}`는 사용자의 구/군/시를 메시지에 삽입합니다. |
| 조건 로직 태그 | 로직을 생성하고 메시지 콘텐츠의 흐름을 제어하는 데 사용됩니다. Braze에서 조건 로직 태그는 특정 사전 정의된 기준에 따라 메시지에 예외와 변형을 만드는 데 사용됩니다. | ```{% if ${language} == 'en' %}```은 사용자가 언어를 "English"로 설정한 경우 지정된 방식으로 메시지를 트리거합니다. |
| 필터 | Liquid 오브젝트의 출력을 변경, 축소 또는 재포맷하는 데 사용됩니다. 주로 수학적 연산을 만드는 데 사용됩니다. | ```{{"Big Sale" | upcase}}```는 "Big Sale"이라는 단어가 메시지에서 "BIG SALE"로 표시되도록 합니다. |
| 연산자 | 메시지에서 사용자가 어떤 메시지를 받을지에 영향을 줄 수 있는 종속성이나 조건을 만드는 데 사용됩니다. | 사용자가 `{% custom_attribute.${Total_Revenue} > 0%}`로 태그된 메시지에서 정의된 기준을 충족하면 해당 메시지를 받게 됩니다. 충족하지 못하면 설정에 따라 다른 지정된 메시지를 받거나 받지 않을 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="알아야 할 용어" }

{% endraw %}

<br>