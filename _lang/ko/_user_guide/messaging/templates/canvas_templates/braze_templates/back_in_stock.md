---
nav_title: 재입고
article_title: 재입고
page_order: 2
page_type: reference
description: "이 문서에서는 Braze Canvas 템플릿을 사용하여 재입고된 상품을 개인화된 메시징으로 사용자에게 알려 구매를 유도하는 방법을 설명합니다."
tool: Canvas
---

# 재입고 {#back-in-stock}

> 재입고 템플릿을 사용하면 이전에 품절된 상품을 조회했거나 관심을 표현한 사용자에게 해당 상품이 다시 구매 가능해졌음을 알리는 메시지를 생성할 수 있습니다. 이를 통해 제품이 다시 입고되는 중요한 순간에 사용자의 참여를 유도하여 원하는 제품을 구매할 수 있도록 도와줍니다.

이 문서에서는 사용자 라이프사이클의 전환 단계를 위해 설계된 **재입고** 템플릿의 사용 사례를 안내합니다. 이 과정을 마치면 상품이 재입고되었을 때 사용자에게 푸시(웹 또는 모바일), SMS 또는 이메일을 발송하고 최대 두 번의 리마인더를 보내는 Canvas를 만들 수 있습니다.

## 필수 조건 {#prerequisites}

이 템플릿을 성공적으로 사용하려면 다음이 필요합니다:

- 상품 정보가 포함된 [카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs/create)
- 메시지를 보내려는 상품에 대해 [재입고 알림]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications)이 설정되어 있어야 합니다

## 필요에 맞게 템플릿 맞춤 설정하기 {#tailoring-the-template-to-your-needs}

슬랙스, 청바지, 큐롯 등 다양한 종류의 바지를 전문으로 하는 소비자 직접 판매(D2C) 의류 소매업체인 PantsLabyrinth에서 일하고 있다고 가정해 보겠습니다. 재입고 템플릿을 사용하여 인기 청바지인 Classic Straight Leg이 재입고되었을 때 다양한 채널을 통해 고객에게 알릴 수 있습니다.

Canvas를 만들기 전에 스트레이트 레그 바지 재고 정보가 포함된 [카탈로그를 설정]({{site.baseurl}}/user_guide/data/activation/catalogs/create)하고 Classic Straight Leg 청바지에 대한 [재입고 알림을 설정]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications#setting-up-back-in-stock-notifications)합니다. 사용자가 앱에서 Classic Straight Leg 청바지를 즐겨찾기하는 커스텀 이벤트를 수행하면 알림을 구독하도록 설정했습니다.

재입고 템플릿에 접근하려면 새 Canvas를 만들 때 **Canvas 템플릿 사용** > **Braze 템플릿**을 선택합니다. 그런 다음 **Back in Stock** 옆에 있는 **템플릿 적용**을 선택합니다. 이제 필요에 맞게 템플릿을 살펴보겠습니다.

### 1단계: 세부 정보 설정하기 {#step-1-set-up-the-details}

목표에 맞게 Canvas 세부 정보를 조정해 보겠습니다.

1. 템플릿 이름 옆의 **편집**을 선택합니다.

![Canvas의 현재 제목과 설명.]({% image_buster /assets/img/canvas_templates/back_in_stock_old_name_description.png %}){: style="max-width:45%;"}

{:start="2"}
2. Canvas 이름을 업데이트하여 Classic Straight Leg 제품이 재입고되었을 때 사용자를 타겟팅하기 위한 Canvas임을 명시합니다.
3. 이 Canvas에 개인화된 메시징이 포함되어 있음을 설명하도록 설명을 업데이트합니다.
4. **Promotional** 태그 아래에 중첩된 **Back in Stock** 태그를 추가하여 Canvas 홈 페이지에서 필터링할 수 있도록 합니다.

![Canvas 이름이 "Back in Stock - Classic Straight Leg"이고 간단한 Canvas 설명이 있는 "Canvas 세부 정보 설정" 단계.]({% image_buster /assets/img/canvas_templates/back_in_stock_1.png %})

### 2단계: 전환 이벤트 할당하기 {#step-2-assign-conversion-events}

**주요 전환 이벤트 - A**를 **특정 구매 수행**으로 변경하고 제품 이름으로 **Classic Straight Leg**을 선택합니다.

![전환 기한이 7일인 Classic Straight Leg 제품 구매 전환 이벤트 유형에 대한 "전환 이벤트 할당" 섹션.]({% image_buster /assets/img/canvas_templates/back_in_stock_2.png %})

### 3단계: 진입 스케줄 맞춤 설정하기 {#step-3-tailor-the-entry-schedule}

진입 스케줄은 **액션 기반**으로 유지하여 사용자가 동작을 수행할 때 Canvas에 진입하도록 합니다. 템플릿에서 이미 **재입고 이벤트 수행**으로 설정되어 있습니다.

이 단계에서 두 가지를 조정합니다:

1. Classic Straight Leg 청바지 정보가 포함된 카탈로그를 선택합니다. 이 카탈로그의 이름은 "Straight Leg Pants"입니다.

![액션 기반 Canvas의 "진입 스케줄" 단계.]({% image_buster /assets/img/canvas_templates/back_in_stock_3.png %})

{: start="2"}
2. **시작 시간(필수)**을 원하는 시작 날짜와 시간으로 설정합니다.

![시작 시간이 2025년 1월 2일 오전 12시인 "진입 기간" 섹션.]({% image_buster /assets/img/canvas_templates/back_in_stock_4.png %})

### 4단계: 타겟 오디언스 선택하기 {#step-4-select-the-target-audience}

Classic Straight Leg 청바지를 구매할 가능성이 높은 사용자로 타겟 오디언스를 정의합니다.

1. 타겟 Segment인 "Favorited - Classic Straight Leg Jeans"를 선택합니다. 이 Segment는 앱이나 웹사이트에서 Classic Straight Leg 청바지를 즐겨찾기한 사용자로 구성됩니다.
2. "Jeans"를 "0"회 이상 구매한 사용자를 포함하는 필터를 선택합니다.

!["Favorited - Classic Straight Leg Jeans" Segment가 있는 "타겟 오디언스" 단계.]({% image_buster /assets/img/canvas_templates/back_in_stock_5.png %})

{: start="3"}
3. 진입 제어를 조정하여 Canvas의 최대 기간이 지난 후 사용자가 Canvas에 다시 진입할 수 있도록 합니다. 이렇게 하면 사용자가 동일한 단계를 동시에 트리거할 가능성을 줄일 수 있습니다.

![Canvas의 최대 기간 동안 사용자가 이 Canvas에 다시 진입할 수 있도록 허용하는 체크박스가 있는 "진입 제어" 섹션.]({% image_buster /assets/img/canvas_templates/back_in_stock_6.png %})

{: start="4"}
4. Classic Straight Leg 청바지를 즐겨찾기 해제하는 커스텀 이벤트를 수행한 사용자를 제거하도록 종료 기준을 조정합니다.

!["Unfavorited" 커스텀 이벤트를 수행한 사용자에 대한 예외가 있는 "종료 기준" 섹션.]({% image_buster /assets/img/canvas_templates/back_in_stock_7.png %})

### 5단계: 발송 설정 선택하기 {#step-5-select-your-send-settings}

기본 구독 설정을 유지하여 메시지나 알림 수신에 가입했거나 옵트인한 사용자에게만 발송하고, 나머지 설정(최대 게재빈도 설정, 방해금지 시간, 시드 그룹)은 건너뜁니다.

![가입했거나 옵트인한 사용자를 타겟팅하는 "발송 설정" 단계.]({% image_buster /assets/img/canvas_templates/back_in_stock_8.png %})

### 6단계: Canvas 커스터마이즈하기 {#step-6-customize-your-canvas}

이제 사용자에게 발송할 채널과 콘텐츠를 커스터마이즈하여 Canvas를 구축합니다. 네 가지 템플릿 채널(모바일 및 웹 푸시, SMS, 이메일)을 모두 사용하고 [인텔리전트 채널]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel) 필터를 사용하므로 추가하거나 제거할 항목이 없습니다.

{% alert tip %}
[Canvas 진입 속성]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties)을 사용하여 참조하는 제품에 따라 Canvas의 메시지를 커스터마이즈할 수 있습니다.
{% endalert %}

각 메시지 단계를 살펴보며 콘텐츠를 업데이트하는 것으로 커스터마이즈를 시작합니다.

1. `!!YOURCATALOGHERE!!`를 카탈로그 이름("Straight_Leg_Pants")으로 교체합니다.
2. `[0]`을 Classic Straight Leg 청바지의 인덱스 번호인 "9"로 교체합니다. 이 청바지는 카탈로그의 `items` 배열에서 열 번째 항목이기 때문입니다. (배열은 Liquid에서 0부터 인덱싱되므로 첫 번째 항목은 `1`이 아닌 `0`입니다.)
3. 나머지 모든 메시지 단계에 대해 1번과 2번을 반복합니다. 여기에는 다음이 포함됩니다:
    - 1일 지연 후 발송되는 "In-Product Msg & Email" 메시지
    - 구매하지 않은 사용자에게 발송되는 "Push+Email Alert" 메시지
4. 행동 경로 단계를 업데이트하여 **Purchase** 동작 그룹을 선택합니다. 그런 다음 **Make a specific purchase**를 선택하고 제품으로 Classic Straight Leg 청바지를 선택합니다.

![제품이 재입고되었음을 사용자에게 알리는 메시지가 있는 모바일 푸시 Canvas 단계.]({% image_buster /assets/img/canvas_templates/back_in_stock_9.png %})

### 7단계: Canvas 테스트 및 시작하기 {#step-7-test-and-launch-your-canvas}

Canvas를 테스트하고 검토하여 예상대로 작동하는지 확인한 후 **Canvas 시작**을 선택하여 시작합니다. 이제 Classic Straight Leg 청바지를 즐겨찾기하고 메시징 채널을 구독한 사용자는 재입고 시 알림을 받게 됩니다!

{% alert tip %}
Canvas를 시작하기 전과 후에 고려해야 할 사항은 [시작 전후 체크리스트]({{site.baseurl}}/user_guide/messaging/canvas/ideas_and_strategies/pre_post_launch_checklist#things-to-consider-before-launch)를 확인하세요.
{% endalert %}