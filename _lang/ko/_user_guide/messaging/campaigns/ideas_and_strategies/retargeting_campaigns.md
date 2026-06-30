---
nav_title: 캠페인 리타겟팅
article_title: 캠페인 리타겟팅
page_order: 2
page_type: reference
description: "이 참조 문서에서는 사용자가 수신한 메시지를 기반으로 캠페인을 리타겟팅하는 방법과 이유를 설명합니다."
tool:
  - Campaigns

---

# 캠페인 리타겟팅 {#retarget-campaigns}

> 사용자가 이메일을 열었는지 여부와 같은 이전 행동을 기반으로 캠페인을 리타겟팅하면 사용자를 재분류하여 효과적인 데이터 중심 마케팅 접근 방식을 구현할 수 있습니다.

Braze는 사용자가 수신한 메시지를 기반으로 리타겟팅하는 기능을 지원합니다. Campaigns 및 Canvases와의 상호작용을 기반으로 사용자를 리타겟할 수 있습니다.

각 리타겟팅 필터는 추가한 후 여러 옵션을 제공합니다. 사용자 타겟팅에 대한 자세한 내용은 캠페인 설정에 관한 [Braze 학습 과정](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)을 확인하세요!

![사용 가능한 필터의 드롭다운 메뉴가 있는 Segment 세부 정보 섹션.]({% image_buster /assets/img_archive/retarget.png %}){: style="max-width:80%;"}

## 리타겟팅 필터 {#retargeting-filters}

이 섹션의 리타겟팅 필터를 Campaigns 및 Canvases에서 사용자에게 사용할 수 있습니다.

### Campaign 클릭/열기 {#clickedopened-campaign}

이 필터를 사용하여 다음 행동을 한 사용자 또는 하지 않은 사용자를 찾을 수 있습니다:

- 이메일 클릭
- 인앱 메시지 클릭
- 푸시 알림 직접 열기
- 이메일 열기
- 인앱 메시지 조회

![채널 상호작용 옵션이 있는 Campaign 클릭/열기 필터.]({% image_buster /assets/img_archive/clickedopened.png %})

리타겟할 Campaign을 선택하여 더 구체적으로 지정할 수 있습니다.

### 태그가 있는 Campaign 또는 Canvas 클릭 또는 열기 {#clicked-or-opened-campaign-or-canvas-with-tag}

이 필터를 사용하여 특정 태그가 있는 Campaigns 또는 Canvases와 상호작용한 사용자 또는 하지 않은 사용자를 찾을 수 있습니다:

- 이메일 클릭
- 인앱 메시지 클릭
- 푸시 알림 직접 열기
- 이메일 열기
- 인앱 메시지 조회

![태그가 있는 Campaign 또는 Canvas 클릭 또는 열기 필터.]({% image_buster /assets/img_archive/retarget_tag_filter.png %})

### Campaign에서 전환 {#converted-from-campaign}

이 필터를 사용하여 타겟 Campaign에서 전환한(기본 전환 기준) 사용자 또는 전환하지 않은 사용자를 찾을 수 있습니다.

반복 Campaigns의 경우, 이 필터는 사용자가 Campaign의 가장 최근 메시지에서 전환했는지 여부를 나타냅니다.

![Campaign 선택이 있는 Campaign에서 전환 필터.]({% image_buster /assets/img_archive/converted_from_campaign.png %})

### Canvas에서 전환 {#converted-from-canvas}

이 필터를 사용하여 타겟 Canvas에서 전환한(기본 전환 기준) 사용자 또는 전환하지 않은 사용자를 찾을 수 있습니다.

반복 Canvases의 경우, 이 필터는 사용자가 Canvas를 거치는 동안 한 번이라도 전환한 적이 있는지 여부를 나타냅니다.

![Canvas 선택이 있는 Canvas에서 전환 필터.]({% image_buster /assets/img_archive/converted_from_canvas.png %})

### Campaign 대조군에 포함 {#in-campaign-control-group}

이 필터를 사용하여 타겟 Campaign의 대조군에 포함된 사용자 또는 포함되지 않은 사용자를 찾을 수 있습니다.

![Campaign 선택이 있는 Campaign 대조군에 포함 필터.]({% image_buster /assets/img_archive/campaign_control_group.png %})

### Canvas 대조군에 포함 {#in-canvas-control-group}

이 필터를 사용하여 타겟 Canvas의 대조군에 포함된 사용자 또는 포함되지 않은 사용자를 찾을 수 있으며, 드롭다운에서 선택할 수 있습니다.

![Canvas 선택이 있는 Canvas 대조군에 포함 필터.]({% image_buster /assets/img_archive/canvas_control_group.png %})

### 특정 Campaign에서 마지막으로 메시지 수신 {#last-received-message-from-specific-campaign}

이 필터를 사용하여 특정 Campaign에서 지정된 날짜 또는 일수 이전 또는 이후에 마지막으로 메시지를 수신한 사용자를 찾을 수 있습니다. 이 필터는 사용자가 다른 Campaigns에서 메시지를 수신한 시점은 고려하지 않습니다.

{% multi_lang_include audience/segments.md section='same channel identifier' %}

![날짜 옵션이 있는 특정 Campaign에서 마지막으로 메시지 수신 필터.]({% image_buster /assets/img_archive/last_received_specific_campaign.png %})

### 태그가 있는 Campaign 또는 Canvas에서 마지막으로 메시지 수신 {#last-received-message-from-campaign-or-canvas-with-tag}

이 필터를 사용하여 특정 태그가 있는 Campaign 또는 Canvas에서 지정된 날짜 또는 일수 이전 또는 이후에 마지막으로 메시지를 수신한 사용자를 찾을 수 있습니다. 이 필터는 사용자가 다른 Campaigns 또는 Canvases에서 메시지를 수신한 시점은 고려하지 않습니다.

![태그가 있는 Campaign 또는 Canvas에서 마지막으로 메시지 수신 필터.]({% image_buster /assets/img_archive/last_received_campaign_with_tag.png %})

### Campaign에서 메시지 수신 {#received-message-from-campaign}

이 필터를 사용하여 타겟 Campaign에서 메시지를 수신한 사용자 또는 수신하지 않은 사용자를 찾을 수 있습니다.

{% multi_lang_include audience/segments.md section='same channel identifier' %}

![Campaign 선택이 있는 Campaign에서 메시지 수신 필터.]({% image_buster /assets/img_archive/receivedcamp.png %})

### 태그가 있는 Campaign 또는 Canvas에서 메시지 수신 {#received-message-from-campaign-or-canvas-with-tag}

이 필터를 사용하여 타겟 태그가 있는 Campaign 또는 Canvas에서 메시지를 수신한 사용자 또는 수신하지 않은 사용자를 찾을 수 있습니다.

![태그가 있는 Campaign 또는 Canvas에서 메시지 수신 필터.]({% image_buster /assets/img_archive/received_campaign_with_tag.png %})

## 캠페인 리타겟팅의 장점 {#advantages-with-retargeting-campaigns}

리타겟팅은 원래 Segment에 사용자가 취하기를 원하는 특정 행동이 포함되어 있을 때 특히 효과적입니다. 예를 들어, 구매를 한 적이 없는 사용자를 대상으로 하는 카드가 있다고 가정해 보겠습니다. 이 카드는 할인된 인앱 구매 프로모션을 광고합니다. 초기 Segment는 다음과 같습니다:

- 앱 내 지출 금액이 정확히 0
- 마지막 앱 사용이 14일 이내

Segment의 총 사용자 수는 100,000명이며, 콘텐츠 카드 통계에서 60,000명의 고유 사용자가 카드를 조회하고 20,000명의 고유 사용자가 카드를 클릭한 것을 알 수 있습니다. 세그먼터를 통해 카드를 클릭한 사용자 중 실제로 구매한 사용자 수를 확인할 수 있습니다:

- 앱 내 지출 금액이 0보다 큼
- 클릭한 카드가 해당 카드 이름

이러한 통계를 분석한 후, 카드를 클릭했지만 구매하지 않은 사용자의 Segment를 만들 수 있습니다:

- 앱 내 지출 금액이 정확히 0
- 클릭한 카드가 해당 카드 이름

이 Segment를 프로모션 또는 다른 인앱 구매에 대한 추가 메시지로 리타겟할 수 있습니다. 리타겟팅은 메시징 캠페인으로 수행할 수 있습니다. 멀티채널 접근 방식을 사용하면 사용자가 응답할 가능성이 가장 높은 곳에서 도달할 수 있어 캠페인의 효과를 높일 수 있습니다.