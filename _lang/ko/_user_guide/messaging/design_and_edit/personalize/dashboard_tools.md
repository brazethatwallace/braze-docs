---
nav_title: 대시보드 도구
article_title: 개인화를 위한 대시보드 도구
page_order: 0
description: "이 참조 문서에서는 Braze 메시지 및 랜딩 페이지 편집기의 개인화 추가 경험에 대해 설명합니다. 사전 포맷된 Liquid, 기본값, 색상 레이블 및 예측 제안과 같은 Liquid 편집기 향상 기능을 포함합니다."
---

# 개인화를 위한 대시보드 도구 {#dashboard-tools-for-personalization}

> Braze 대시보드 도구를 사용하면 모든 태그를 직접 작성하지 않고도 Liquid 개인화를 삽입할 수 있습니다. **개인화 추가** 플로우가 올바른 구문을 자동으로 생성하며, Liquid 편집기를 통해 템플릿을 빠르게 읽고 확장할 수 있습니다.

Liquid 구문 규칙, 지원되는 태그 및 고급 패턴에 대해서는 [Liquid 사용하기]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) 및 [지원되는 개인화 태그]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/supported_personalization_tags)를 참조하세요.

## 작성기 및 설정에서 개인화 추가 {#add-personalization-in-composers-and-settings}

**개인화 추가** 도구는 대시보드 전반의 템플릿 텍스트 필드 근처에 표시되며, 다음을 포함합니다:

- 본문 또는 헤더에서 Liquid를 지원하는 채널의 **Campaign 및 캔버스 단계**(예: 이메일, 푸시, SMS, 인앱 메시지, Content Cards, 웹훅).
- **드래그 앤 드롭 편집기** — 컨트롤은 보통 블록 또는 편집기 도구 모음에 있습니다. 예를 들어, 드래그 앤 드롭 인앱 메시지에서 **개인화 추가**를 선택하고, 개인화 유형을 선택한 다음, 생성된 스니펫을 콘텐츠에 배치한 후 **미리보기 및 테스트**에서 미리 볼 수 있습니다. 채널별 참고 사항은 해당 채널의 드래그 앤 드롭 또는 작성기 문서를 참조하세요([인앱 메시지 스타일 설정]({{site.baseurl}}/user_guide/channels/in_app_messages/customize/style_settings#adding-liquid) 또는 [드래그 앤 드롭으로 이메일 만들기]({{site.baseurl}}/user_guide/channels/email/drag_and_drop) 등).
- 개인화 선택기를 제공하는 **전문 작성기** — 예를 들어, [아이템 추천]({{site.baseurl}}/user_guide/brazeai/item_recommendations/using_recommendations)에서는 동일한 스타일의 창 내에서 **아이템 추천**과 같은 **개인화 유형** 옵션을 사용합니다.
- **랜딩 페이지** — 드래그 앤 드롭 편집기 또는 페이지 및 블록 설정에서 Liquid 개인화를 추가할 수 있습니다. 자세한 내용은 [랜딩 페이지 개인화]({{site.baseurl}}/user_guide/messaging/landing_pages/personalize_landing_pages)를 참조하세요.

## 사전 포맷된 변수 및 기본값 삽입 {#insert-pre-formatted-variables-and-defaults}

**개인화 추가** 도구를 사용하면 선택적 기본값과 함께 Liquid를 삽입하여 빈 프로필 데이터가 문구를 깨뜨리지 않도록 할 수 있습니다.

![개인화 삽입을 선택한 후 나타나는 개인화 추가 모달. 모달에는 개인화 유형, 속성, 선택적 기본값 필드가 있으며 Liquid 구문의 미리보기가 표시됩니다.]({% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}){: style="max-width:90%;"}

이 도구는 커서가 있던 위치에 지정한 기본값과 함께 Liquid를 삽입합니다. 삽입 지점은 전후 텍스트가 표시되는 미리보기 상자에서도 확인할 수 있습니다. 텍스트 블록이 강조 표시된 경우, 강조 표시된 텍스트가 대체됩니다.

![개인화 추가 모달의 GIF로, 사용자가 기본값으로 "fellow traveler"를 입력하면 모달이 작성기에서 강조 표시된 텍스트 "name"을 Liquid 스니펫으로 대체하는 모습을 보여줍니다.]({% image_buster /assets/img_archive/insert_var_shot.gif %})

많은 작성기에서 {% raw %}`{{`{% endraw %}를 입력하여 자동 완성을 사용하거나, 다른 곳에서 태그를 붙여넣을 수도 있습니다. 자세한 내용은 **Liquid 사용하기**의 [태그 삽입]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid#inserting-tags)을 참조하세요.

### 변수 할당 {#assign-variables}

{% raw %}
Liquid의 일부 작업에서는 조작하려는 값을 변수로 저장해야 합니다. Liquid 구문에 여러 속성, 이벤트 등록정보 또는 필터가 포함된 경우에 자주 발생합니다.

예를 들어, 두 개의 커스텀 데이터 정수를 더하고 싶다고 가정해 보겠습니다.

#### 잘못된 Liquid 예시 {#incorrect-liquid-example}

다음과 같이 사용할 수 없습니다:

```liquid
{{custom_attribute.${one}}} | plus: {{custom_attribute.${two}}}
```

이 Liquid는 한 줄에서 여러 속성을 참조할 수 없기 때문에 작동하지 않습니다. 수학 함수가 실행되기 전에 이 값 중 하나 이상에 변수를 할당해야 합니다. 두 개의 커스텀 속성을 더하려면 두 줄의 Liquid가 필요합니다: 하나는 커스텀 속성을 변수에 할당하는 줄이고, 다른 하나는 덧셈을 수행하는 줄입니다.

#### 올바른 Liquid 예시 {#correct-liquid-example}

다음과 같이 사용할 수 있습니다:

```liquid
{% assign value_one = {{custom_attribute.${one}}} %}
{% assign result = value_one | plus: {{custom_attribute.${two}}} %}
```

#### 튜토리얼: 변수를 사용하여 잔액 계산하기 {#tutorial-using-variables-to-calculate-a-balance}

기프트 카드 잔액과 리워드 잔액을 더하여 사용자의 현재 잔액을 계산해 보겠습니다:

먼저, `assign` 태그를 사용하여 `current_rewards_balance` 커스텀 속성을 "balance"라는 용어로 대체합니다. 이제 조작할 수 있는 `balance`라는 변수가 생겼습니다.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

다음으로, `plus` 필터를 사용하여 각 사용자의 기프트 카드 잔액과 `{{balance}}`로 표시되는 리워드 잔액을 합산합니다.

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}

{% alert tip %}
모든 메시지에서 동일한 변수를 할당하고 계신가요? `assign` 태그를 반복해서 작성하는 대신, 해당 태그를 콘텐츠 블록으로 저장하고 메시지 상단에 배치할 수 있습니다.<br><br>

1. [콘텐츠 블록을 생성합니다]({{site.baseurl}}/user_guide/messaging/design_and_edit/content_blocks#create-a-content-block).
2. 콘텐츠 블록에 이름을 지정합니다(공백이나 특수 문자 없이).
3. 페이지 하단에서 **편집**을 선택합니다.
4. `assign` 태그를 입력합니다.

콘텐츠 블록이 메시지 상단에 있으면, 변수가 메시지에 오브젝트로 삽입될 때마다 선택한 커스텀 속성을 참조하게 됩니다!
{% endalert %}

## Liquid 편집기 향상 기능 {#liquid-editor-enhancements}

이러한 대시보드 기능은 메시지를 작성하는 동안 Liquid를 더 쉽게 사용할 수 있도록 도와줍니다.

### 색상 레이블 {#color-labels}

각 Liquid 요소는 색상에 대응하여 Liquid 편집기에서 Liquid를 한눈에 구분할 수 있습니다.

![다양한 Liquid 요소에 대한 색상 레이블 다이어그램.]({% image_buster /assets/img/liquid_color_code.png %})

### 예측 Liquid {#predictive-liquid}

개인화된 메시지를 작성할 때 커스텀 속성, 속성 이름 등에 대해 예측 Liquid를 사용할 수도 있습니다.

![필드에 텍스트를 입력할수록 Braze가 다양한 Liquid 속성을 추천하는 모습.]({% image_buster /assets/img/liquid_auto_complete.gif %}){: style="max-width:70%;"}

## 다음 단계 {#next-steps}

- [Liquid 사용하기]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid) — Braze에서의 구문, `assign`, 조건문 및 필터
- [기본값 설정]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/setting_default_values) — 모달 외의 Liquid 기본값
- [필터]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/filters) — 날짜, 수학, 문자열 등의 포맷 지정