---
article_title: 메시지 우선순위 지정
permalink: /message_prioritization/
toc_headers: h2
description: "이 참조 문서에서는 최상위 메시지 우선순위 지정과 워크스페이스에서 이를 구성하는 방법에 대해 설명합니다."
---

# 메시지 우선순위 지정 {#message-prioritization}

> 메시지 우선순위 지정을 사용하여 사용자가 먼저 발송되는 메시지가 아닌, 비즈니스에 가장 중요한 메시지를 수신하도록 하세요.

{% alert important %}
메시지 우선순위 지정은 현재 베타 버전입니다. 이 베타에 참여하려면 Braze 계정 매니저에게 문의하세요.<br><br>이 문서는 2026년 7월 말 프로덕션 릴리스로 계획된 메시지 우선순위 지정 버전을 반영합니다. 여기에 설명된 일부 동작은 아직 모든 베타 워크스페이스에서 사용할 수 없을 수 있습니다.
{% endalert %}

## 메시지 우선순위 설정을 사용하는 이유 {#why-use-message-prioritization}

사용자가 수신할 수 있는 메시지 수에는 한계가 있으며, 일정 수준을 넘으면 메시지 볼륨 자체가 문제가 됩니다. 사용자에게 도달하는 메시지는 비즈니스에 가장 중요한 메시지여야 합니다. 메시지 우선순위 설정은 가장 가치 있는 메시지가 제한된 공간을 차지할 수 있도록 보장하며, 이를 우연에 맡기지 않습니다.

대부분의 팀은 최대 게재빈도 설정으로 메시지 볼륨을 관리합니다. 최대 게재빈도 설정만으로는 정밀한 제어가 어렵습니다. 사용자가 게재빈도 한도에 도달하면, 비즈니스 중요도가 아닌 발송 타이밍이 어떤 메시지가 전달될지를 결정하게 됩니다.

가치가 낮은 프로모션이 먼저 발송되면, 그날 나중에 발송될 예정이었던 로열티 보상이나 시간에 민감한 메시지가 사용했을 슬롯을 차지하게 됩니다. 팀에서는 보통 별도의 게재빈도 규칙, 수동 스케줄링, 임시 필터 등을 통해 이 문제를 해결하곤 합니다. 이러한 접근 방식은 지속적인 유지보수가 필요하며, Campaigns와 Canvases가 변경될수록 관리가 더 어려워집니다. 그리고 여전히 올바른 메시지가 전달될 것이라고 보장할 수 없습니다.

메시지 우선순위 설정은 최대 게재빈도 할당 방식을 **선착순**에서 **비즈니스 우선순위 기반**으로 변환합니다. 중요한 메시지의 순위를 지정하면, Braze가 발송 결정을 대신 처리합니다.

메시지 우선순위 설정은 다음과 같은 이점을 제공합니다:

- **한 번만 중요도를 정의하세요:** 카테고리와 순위 규칙을 사용하여 우선순위를 설정할 수 있습니다. 예를 들어, "로열티"를 "유료 파트너십"보다 우선시할 수 있습니다. 옵트인된 모든 발송이 해당 순위를 자동으로 준수합니다.
- **미래를 고려한 결정:** Braze는 사용자가 나중에 수신할 수 있는 메시지를 예측합니다. 우선순위가 더 높은 메시지를 위해 게재빈도 여유 공간을 확보하기 위해 우선순위가 낮은 메시지를 보류할 수 있습니다.
- **메시지 유형 및 채널 간 작동:** 예약 Campaigns, 행동 기반 Campaigns, 캔버스 단계가 공유 최대 게재빈도 설정 내에서 하나의 순위 풀에서 경쟁합니다.
- **재시도 기간:** 우선순위에서 밀린 메시지도 여유가 생기면 재시도할 수 있습니다. 이를 통해 우선순위가 낮은 메시지를 완전히 누락시키지 않으면서 메시지 조합을 개선합니다.

결과적으로 동일한 게재빈도 제한 발송량이 가장 중요한 메시지에 자동으로 할당됩니다.

메시지 우선순위 설정은 최대 게재빈도 한도에 자주 도달하는 대량 발송자에게 가장 유용합니다. 메시지 가치가 명확하게 차별화되는 경우에 가장 효과적입니다. 예를 들어, 로열티 또는 매출 기여 메시지와 일상적인 프로모션을 구분할 때 적합합니다.

## 작동 방식 {#how-it-works}

메시지 우선순위를 사용하여 [카테고리](#categories)와 [우선순위 규칙](#prioritization-rules)을 만들어 메시지 전송 순위를 결정할 수 있습니다.

이 설정을 관리하려면 **설정** > **메시지 우선순위**로 이동합니다. 관리자만 최상위 메시지 우선순위 설정을 구성할 수 있습니다. 사용자가 이 섹션의 설정을 보려면 "View Message Prioritization" 권한이 필요하고, 편집하려면 "Edit Message Prioritization" 권한이 필요합니다.

예를 들어, 유료 파트너십과 로열티 프로그램의 이메일 프로모션을 관리하는 뷰티 브랜드가 메시지 우선순위를 사용하여 "Paid Partnerships"와 "Loyalty"라는 두 가지 카테고리를 만듭니다. 이 브랜드는 비즈니스 중요도에 따라 카테고리 순위를 매깁니다. 연말 시즌에는 장기 회원을 우선시하기 위해 "Loyalty"를 1순위로, "Paid Partnerships"를 2순위로 설정합니다.

![두 카테고리(Paid Partnerships 및 Loyalty)에 대한 우선순위 규칙의 예시입니다.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization12.png %})

전송 시점에 Braze는 전송할 메시지를 사용자가 수신할 수 있는 다른 메시지와 비교합니다. 비교 대상은 우선순위에 옵트인되어 있고, 우선순위 카테고리가 설정되어 있으며, 동일한 최대 게재빈도 설정 규칙과 동일한 최대 게재빈도 설정 기간 내에 해당하는 메시지입니다. 현재 메시지를 전송하면 더 높은 우선순위의 메시지가 나중에 전송되지 못할 경우, Braze는 낮은 우선순위의 메시지를 후순위로 처리합니다. 구성된 재시도 기간에 따라 해당 낮은 우선순위 메시지는 나중에 재시도되거나 전송되지 않습니다.

메시지 우선순위는 다음을 평가할 수 있습니다:

- 예약된 Campaigns
- 행동 기반 Campaigns
- Canvases

현재 API 트리거 Campaigns 또는 Canvases는 메시지 우선순위에서 지원되지 않으며 우선순위 결정에 참여하지 않습니다.

Braze는 현재 메시지를 전송하면 더 높은 우선순위의 메시지가 나중에 전송되지 못할 수 있는지를 평가할 때, 각 메시지의 예상 전송 시점에 대한 예측을 사용합니다. Braze가 Campaigns 및 Canvases의 향후 전송 시점을 예측하는 방법에 대한 자세한 내용은 [Braze는 향후 메시지 전송 시점을 어떻게 예측하나요?](#how-does-braze-predict-when-a-future-message-sends)를 참조하세요.

### 지원되는 메시지 채널 {#supported-message-channels}

메시지 우선순위는 최대 게재빈도 설정과 동일한 채널을 지원합니다:

- 푸시 알림
- 이메일
- SMS
- 웹훅
- WhatsApp
- LINE

우선순위 결정 및 최대 게재빈도 설정에서 iOS 푸시, Android 푸시, 웹 푸시 및 기타 푸시 알림 플랫폼은 별도의 채널이 아닌 하나의 공유 푸시 채널로 취급됩니다.

다음 채널은 최대 게재빈도 설정의 적용을 받지 않으므로 메시지 우선순위 대상이 아닙니다:

- Content Cards
- 인앱 메시지
- 배너

인앱 메시지와 배너는 여러 메시지가 동일한 트리거 또는 배치를 두고 경쟁할 때 어떤 메시지를 표시할지 결정하기 위해 자체 우선순위 설정을 사용합니다. 인앱 메시지의 경우 [우선순위 선택]({{site.baseurl}}/user_guide/channels/in_app_messages/traditional#choose-a-priority)을 참조하세요. 배너의 경우 [배너 우선순위]({{site.baseurl}}/user_guide/channels/banners#priority)를 참조하세요.

Campaign 또는 캔버스 단계가 대상이 아닌 채널만 사용하는 경우, 우선순위 결정에 참여하지 않습니다.

## 카테고리 {#categories}

우선순위 규칙은 카테고리 순위를 기반으로 하며, 카테고리는 특정 Campaign 또는 Canvas에 할당할 수 있는 레이블입니다([태그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)와 유사합니다). 한 번에 생성할 수 있는 카테고리 수에는 제한이 있습니다. 더 높은 한도를 원하시면 계정 매니저에게 문의하세요.

새 카테고리를 추가하려면:

1. **설정** > **메시지 우선순위** > **카테고리**로 이동합니다.
2. **새 카테고리 생성**을 선택합니다.

![메시지 우선순위 섹션의 '새 카테고리 생성' 버튼.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization1.png %})

{:start="3"}
3. 카테고리에 이름과 선택적 설명을 입력합니다.
4. **카테고리 생성**을 선택합니다.

![설명이 '세 번째로 높은 우선순위 카테고리입니다.'인 'P3'라는 이름의 카테고리 예시.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization3.png %}){: style="max-width:60%;"}

카테고리를 편집하거나 삭제하려면 <i class="fas fa-ellipsis-vertical" aria-label="더보기 메뉴"></i> 메뉴를 선택합니다.

## 우선순위 규칙 {#prioritization-rules}

카테고리가 설정되면, 우선순위 규칙 세트에서 카테고리의 순위를 지정할 수 있습니다. 규칙은 우선순위가 높은 순서대로 정렬됩니다. 한 번에 생성할 수 있는 우선순위 규칙 수에는 제한이 있습니다. 더 높은 한도가 필요하시면 계정 매니저에게 문의하세요.

1. **설정** > **메시지 우선순위** > **우선순위 규칙**으로 이동하여 규칙을 설정합니다.

![아직 우선순위가 설정되지 않은 '우선순위 규칙' 섹션.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization4.png %})

{:start="2"}
2. **규칙 추가**를 선택합니다.
3. 드롭다운에서 카테고리를 선택합니다.

![P1이 카테고리로 선택된 '우선순위 1' 우선순위 규칙.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization5.png %})

{:start="4"}
4. 마지막 규칙 아래에서 **+ 규칙 추가**를 선택하여 규칙을 계속 추가합니다.

규칙의 순서를 변경하려면 규칙의 <i class="fa-solid fa-grip-vertical" aria-label="드래그하여 순서 변경"></i> 아이콘을 선택한 후 드래그합니다. 규칙을 삭제하려면 <i class="fas fa-ellipsis-vertical" aria-label="더 보기 메뉴"></i> 메뉴를 선택한 다음 **규칙 삭제**를 선택합니다.

업데이트를 적용하려면 반드시 **저장**을 선택하세요.

## 최대 게재빈도 설정 {#frequency-caps}

메시지 우선순위 지정은 기존 최대 게재빈도 설정 규칙 내에서 작동합니다. 우선순위 지정 대상이 되려면 Campaign 또는 캔버스 단계가 지원되는 채널을 사용하고 최대 게재빈도 설정 구성의 적용을 받아야 합니다. 최대 게재빈도 설정의 적용을 받지 않는 메시지는 메시지 우선순위 지정 대상이 아닙니다. 메시지를 항상 발송하려면 최대 게재빈도 설정에서 제외하세요. 이렇게 하면 메시지 우선순위 지정에서도 제외됩니다.

우선순위가 지정된 메시지는 다음 조건을 모두 충족해야만 발송할 수 있습니다.

1. 해당 사용자에 대해 관련 최대 게재빈도 설정 규칙에 아직 도달하지 않았을 것
2. 해당 메시지를 발송해도 이후 더 높은 우선순위의 메시지가 발송되기 전에 사용자가 게재빈도 한도에 도달하지 않을 것

![최대 게재빈도 설정 규칙의 예시.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization9.png %})

채널별 최대 게재빈도 설정 규칙, 카테고리별 규칙, 태그 필터, 또는 모든 채널에 적용되는 규칙을 사용할 수 있습니다. 메시지 우선순위 지정은 옵트인된 메시지에 적용되는 규칙과 함께 작동합니다.

카테고리별로 최대 게재빈도 설정 규칙을 생성하여 사용자가 특정 카테고리에서 수신하는 메시지 수를 관리할 수도 있습니다. 이를 통해 높은 우선순위 카테고리에서 너무 많은 메시지를 발송하는 것을 방지할 수 있습니다. **Additional filters** 아래에서 **Message prioritization category**를 선택한 다음, 드롭다운에서 카테고리를 선택하세요.

![P2 또는 P1을 선택할 수 있는 'Category' 필드 드롭다운이 포함된 최대 게재빈도 설정 규칙의 예시.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization8.png %}){: style="max-width:70%;"}

## 옵트인 {#opting-in}

### Campaign 옵트인 {#campaign-opt-in}

Campaign을 우선순위 지정에 옵트인하려면, Campaign의 전송 설정에서 **Opt-in to Message Prioritization** 체크박스를 선택합니다.

!["Opt-in to Message Prioritization" 체크박스.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization6.png %})

다음으로, **Category** 드롭다운에서 카테고리를 선택하여 Campaign을 카테고리에 할당합니다.

![Campaign 전송 설정의 메시지 우선순위 지정 카테고리 드롭다운.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization10.png %})

메시지 우선순위 지정은 예약된 Campaigns와 행동 기반 Campaigns를 지원합니다. API 트리거된 Campaigns는 지원되지 않습니다.

### Canvas 옵트인 {#canvas-opt-in}

Canvas 옵트인은 Campaigns와 유사하게 작동합니다. Canvas를 메시지 우선순위 지정에 옵트인하려면 Canvas 설정에서 메시지 우선순위 지정을 활성화하고 Canvas를 카테고리에 할당합니다. Canvas의 모든 단계는 해당 카테고리와 동일한 우선순위 수준을 공유하므로, 단계별로 개별적으로 우선순위를 설정할 수 없습니다.

메시지 우선순위 지정은 예약된 Canvases와 행동 기반 Canvases를 지원합니다. API 트리거된 Canvases는 지원되지 않습니다.

## Intelligent Timing {#intelligent-timing}

Intelligent Timing을 사용하면 Braze가 각 사용자의 최적 발송 시간에 메시지를 보내므로, 동일한 Campaign이나 캔버스 메시지 단계에서 각 사용자에게 서로 다른 시간에 메시지가 전달될 수 있습니다. 메시지 우선순위 지정은 이를 고려합니다. 즉, 메시지가 예약된 시간에 모든 사용자에게 발송된다고 가정하는 대신, 해당 사용자의 최적 발송 시간을 기반으로 경쟁하는 메시지의 순위를 매깁니다.

Intelligent Timing을 사용하는 Campaigns 및 캔버스 메시지 단계의 경우, Braze는 각 사용자별 발송 시간을 계산할 때까지 최선의 노력으로 발송 타이밍을 예측합니다. Campaigns의 경우, 메시지 우선순위 지정은 해당 Campaign을 사용자의 다른 우선순위가 지정된 적격 메시지와 비교할 때 현재 발생에 대한 사용자의 최적 발송 시간을 사용합니다. 반복되는 Intelligent Timing Campaigns의 경우, Braze는 해당 발생에 대해 선택된 최적 발송 시간을 사용합니다.

캔버스 메시지 단계의 경우, Braze는 사용자가 해당 단계에 진입하고 Braze가 해당 단계에 대한 사용자의 최적 발송 시간을 계산한 후 이 예측을 업데이트합니다. 메시지 우선순위 지정은 현재 단계에 대해 계산된 발송 시간을 사용합니다. 결정적 경로(분기가 없고 단계 순서가 고정된 경로)에서는 Braze가 후속 메시지 단계의 예상 발송 시간을 결정할 때 업데이트된 타이밍도 반영합니다.

## 재시도 윈도우 {#retry-windows}

재시도 윈도우를 사용하면 옵트인된 메시지가 첫 번째 시도에서 전송할 만큼 충분히 높은 우선순위가 아닌 경우, 제한된 일수 동안 재시도할 수 있습니다. 최대 재시도 윈도우 기간은 Braze 플랫폼 에디션에 따라 다릅니다. 이후 각 날마다 메시지가 원래 예약되거나 트리거되어 전송되도록 설정된 동일한 시간에 다시 시도됩니다. 재시도 윈도우의 마지막 날이 지나도 메시지가 여전히 전송되지 않으면, 더 이상 재시도하지 않으며 영구적으로 우선순위가 낮아집니다.

반복 예약 Campaigns의 경우, 재시도 윈도우는 해당 Campaign의 최소 전송 간격보다 짧아야 합니다. 재시도는 Campaign이 해당 날에 정상적으로 전송 예약되어 있지 않더라도 항상 원래 전송 시간으로부터 하루 단위로 발생합니다. 예를 들어, 매주 월요일과 수요일에 전송하는 Campaign이 있는 경우 재시도 시도는 화요일에 발생하므로 재시도 윈도우는 1일로 설정해야 합니다. 매주 월요일, 수요일, 금요일에 전송하는 Campaign이 있고 금요일 전송이 1일 재시도 윈도우로 재시도되는 경우, 재시도 시도는 월요일이 아닌 토요일에 발생합니다.

![재시도 윈도우 설정이 1일로 지정된 모습.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization13.png %})

액션 기반 Campaigns의 경우, 재시도는 트리거된 메시지가 원래 전송될 것으로 예상된 시간을 기준으로 합니다.

예외 이벤트를 사용하는 액션 기반 Campaigns는 재시도 윈도우를 지원하지 않습니다.

Canvas 메시지의 재시도 윈도우는 단계 수준에서 구성됩니다. 지원되는 Canvas 메시징 단계에서 Canvas 메시지 단계의 우선순위가 낮아지고 재시도 윈도우가 구성되어 있는 경우, Braze는 재시도 윈도우 내에서 해당 단계를 나중에 다시 시도할 수 있습니다.

## Braze의 메시지 평가 방식 {#how-braze-evaluates-messages}

{% alert tip %}
메시지 우선순위 지정을 사용하기 위해 이 섹션의 모든 내용을 이해할 필요는 없습니다. 카테고리와 규칙을 설정하고 메시지를 옵트인하면, Braze가 자동으로 메시지를 평가하고 우선순위를 지정하여 가장 중요한 메시지를 발송하기 위해 최선을 다합니다. 여기의 세부 내용은 이러한 결정이 어떻게 이루어지는지 이해하고 싶을 때 참고하시면 됩니다.
{% endalert %}

사용자가 우선순위가 지정된 여러 메시지에 적합한 경우, Braze는 옵트인된 Campaigns와 적합한 Canvas 메시지 단계를 지원되는 채널에서 함께 평가합니다.

Campaigns의 경우 적합한 예약 발송 및 행동 기반 발송이 포함됩니다.

Canvases의 경우 다음이 포함됩니다.

- 사용자가 진입할 수 있는 향후 예약된 Canvases
- 사용자가 현재 진행 중인 Canvases

Canvas 우선순위 지정은 전부 아니면 전무가 아닙니다. 우선순위가 높은 Campaign으로 인해 하나의 캔버스 단계가 우선순위에서 밀릴 수 있지만, 동일한 Canvas 내의 이후 적합한 단계들은 카테고리 순위, 발송 시점, 최대 게재빈도 설정 규칙에 따라 여전히 발송될 수 있습니다.

Braze는 동일한 최대 게재빈도 설정 규칙이 적용되는 경우에만 우선순위가 지정된 메시지를 비교합니다. 예를 들어, 동일한 이메일 최대 게재빈도 설정 규칙에 포함되는 두 개의 이메일 Campaign은 서로 우선순위를 비교할 수 있지만, 우선순위가 낮은 이메일 Campaign이 우선순위가 높은 SMS 메시지에 의해 우선순위에서 밀리지는 않습니다(두 메시지가 동일한 규칙에 포함되지 않는 한). 메시지 우선순위 지정 외부의 메시지도 이러한 최대 게재빈도 제한을 공유하므로, 우선순위가 높은 메시지라도 메시지 우선순위 지정 외부의 메시지 때문에 중단될 수 있습니다.

Braze는 Campaigns와 Canvases를 다르게 평가합니다. Canvas는 시간이 지남에 따라 분기하고 전개될 수 있기 때문입니다.

### Campaign 평가 {#evaluating-campaigns}

Braze는 각 적합한 Campaign 메시지를 해당 메시지의 예상 발송 시간을 기준으로 비교합니다.

### Canvas 평가 {#evaluating-canvases}

Canvas를 평가하기 위해 Braze는 **선행 탐색**을 수행합니다. 시작 지점에서 Canvas를 탐색하여 사용자가 향후 어떤 메시지를 언제 수신할 수 있는지 예측합니다. 선행 탐색은 다음에서 시작됩니다.

- 향후 예약된 Canvases의 경우 Canvas 진입 시점
- 사용자가 이미 Canvas에 있는 경우 사용자의 현재 단계

선행 탐색 시 Braze는 각 유형의 캔버스 단계를 다르게 처리합니다. 단계 유형에 따라 선행 탐색이 해당 단계를 집계하거나, 건너뛰거나, 중단하거나, 여러 경로로 분할됩니다.

| 단계 카테고리 | 선행 탐색에 미치는 영향 |
|---|---|
| 메시징 단계 | 우선순위 지정을 위한 적합한 메시지로 집계됨 |
| 연속 단계 | 건너뜀; 선행 탐색이 통과함 |
| 경계 단계 | 사용자가 해당 단계를 통과할 때까지 선행 탐색이 중단됨 |
| 분기 단계 | 선행 탐색이 가능한 모든 경로를 따라감 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Canvas 평가" }

#### 메시징 단계 {#messaging-steps}

이 단계들은 우선순위 지정에 집계되며, 지원되는 채널에서 발송할 때 적합한 메시지 세트에 추가됩니다.

- 메시지 단계
- Content Optimizer 단계

#### 연속 단계 {#continuation-steps}

이 단계들은 우선순위 지정에서 무시되며 선행 탐색에 영향을 미치지 않습니다.

- 컨텍스트 업데이트 단계
- 사용자 업데이트 단계
- 오디언스 동기화 단계
- 기능 플래그 단계
- 고정 지연이 있는 지연 단계

#### 경계 단계 {#boundary-steps}

Braze는 사용자가 Canvas에서 해당 단계를 실제로 통과할 때까지 선행 탐색을 중단합니다.

- 개인화된 지연이 있는 지연 단계
- 분기 단계 뒤에 오는 지연 단계
- 행동 경로 단계
- 실험 단계

#### 분기 단계 {#branching-steps}

이 단계들은 Canvas를 여러 가능한 경로로 분할합니다.

- 결정 분할 단계
- 오디언스 경로 단계

우선순위 지정 경로에 분기 단계가 포함된 경우, Braze는 모든 경로가 유효하다고 가정하고 지원되는 채널의 모든 병렬 메시지 단계를 우선순위 지정 대상으로 고려합니다. 최대 게재빈도 설정 규칙이 채널별로 적용될 수 있으므로, 필요 시 병렬 메시지 단계는 채널별로 중복 제거됩니다.

예를 들어, 한 분기에서 이메일을 보낼 수 있고 다른 분기에서도 이메일을 보낼 수 있는 경우, Braze는 선행 탐색 중 이를 하나의 가능한 이메일 발송으로 처리합니다. 다른 분기에서 푸시를 보낼 수 있는 경우, Braze는 해당 가능한 푸시 발송을 별도로 고려합니다.

Intelligent Timing을 사용하는 Canvas 메시지 단계의 경우, Braze는 사용자가 해당 단계에 도달하면 각 사용자에 대해 계산된 발송 시간을 사용합니다. 자세한 내용은 [Intelligent Timing](#intelligent-timing)을 참조하세요.

Content Optimizer 단계는 항상 지정된 채널에서 발송하므로 메시징 단계처럼 처리됩니다. 그러나 재시도 창은 Content Optimizer 단계에 적용되지 않습니다. 재시도가 실험을 방해할 수 있기 때문입니다. 지원되는 다른 Canvas 메시징 단계에서는 재시도 창을 사용할 수 있습니다. 지원되지 않는 채널의 캔버스 단계는 메시지 우선순위 지정에 참여하지 않습니다.

## 예시 {#examples}

### 높은 우선순위 Campaign 대 낮은 우선순위 Campaign {#higher-priority-campaign-versus-lower-priority-campaign}

한 사용자가 같은 날 두 개의 이메일 Campaign에 적격하며, 두 Campaign 모두 동일한 최대 게재빈도 설정 규칙에 포함된다고 가정합니다. 높은 우선순위 Campaign이 그날 나중에 발송될 예정이라면, Braze는 낮은 우선순위 Campaign의 우선순위를 낮추어 높은 우선순위 Campaign이 대신 발송될 수 있도록 합니다. 낮은 우선순위 Campaign에 재시도 기간이 있는 경우, Braze는 나중에 다시 시도할 수 있습니다.

### 높은 우선순위 행동 기반 Campaign 대 낮은 우선순위 메시지 {#higher-priority-action-based-campaign-versus-lower-priority-message}

한 사용자가 2시간 후에 발송되도록 설정된 높은 우선순위 행동 기반 Campaign을 트리거한다고 가정합니다. 해당 지연 시간 동안 Braze는 다른 우선순위 메시지를 먼저 발송할지 결정할 때 예정된 행동 기반 Campaign을 고려할 수 있습니다. 이를 통해 높은 우선순위 행동 기반 Campaign이 곧 발송될 예정인 경우 낮은 우선순위 메시지가 먼저 발송되는 것을 방지할 수 있습니다.

### 높은 우선순위 Canvas 대 낮은 우선순위 Campaign {#higher-priority-canvas-versus-lower-priority-campaign}

한 사용자가 낮은 우선순위 Campaign에 적격하지만, 그날 나중에 높은 우선순위 Canvas 메시지를 받을 것으로 예상된다고 가정합니다. Braze가 해당 미래 Canvas 메시지를 미리 평가할 수 있다면, 낮은 우선순위 Campaign의 우선순위를 낮추어 높은 우선순위 Canvas 메시지가 대신 발송될 수 있도록 합니다.

### 경계 단계가 있는 높은 우선순위 Canvas 대 낮은 우선순위 Campaign {#higher-priority-canvas-with-a-boundary-step-versus-lower-priority-campaign}

높은 우선순위 Canvas에 행동 경로 단계, 실험 또는 개인화된 지연이 다음 메시지 단계 전에 포함되어 있다고 가정합니다. 사용자가 해당 단계에 도달하여 통과하기 전까지, Braze는 하위 높은 우선순위 Canvas 메시지를 미리 확인하지 않습니다. 이 경우 낮은 우선순위 Campaign이 먼저 발송될 수 있습니다.

### 높은 우선순위 분기 Canvas 대 낮은 우선순위 메시지 {#higher-priority-branching-canvas-versus-lower-priority-message}

높은 우선순위 Canvas가 사용자가 따르는 분기에 따라 다른 메시지를 발송할 수 있다고 가정합니다. Braze는 메시지를 비교할 때 이러한 가능한 미래 경로를 보수적으로 평가합니다. 이를 통해 높은 우선순위 Canvas 분기가 나중에 동일한 최대 게재빈도 설정을 사용할 수 있는 경우, 낮은 우선순위 메시지가 지금 발송되는 것을 방지할 수 있습니다.

### Intelligent Timing이 적용된 캔버스 단계와 하위 단계 {#canvas-step-with-intelligent-timing-and-downstream-steps}

한 사용자가 Intelligent Timing을 사용하는 높은 우선순위 Canvas 메시지 단계에 진입한다고 가정합니다. Braze가 Intelligent Timing이 적용된 단계에 대한 해당 사용자의 발송 시간을 계산하면, 메시지 우선순위 설정은 현재 단계와 동일한 확정 경로상의 이후 메시지 단계에 대해 해당 사용자별 발송 시간을 사용합니다. 이를 통해 Braze는 초기 경로 추정치만 사용하는 대신 업데이트된 타이밍을 활용하여 하위 Canvas 메시지를 다른 우선순위 발송과 비교할 수 있습니다.

## 제한 사항 {#limitations}

메시지 우선순위 지정에는 다음과 같은 기능 제한이 있습니다. 구체적인 제한은 Braze 플랫폼 에디션에 따라 다르며, 자세한 내용은 Braze 계정 매니저에게 문의하세요.

- 활성 상태의 옵트인된 예약 Campaigns 및 Canvases 수 제한(합산)
- 활성 상태의 옵트인된 행동 기반 Campaigns 및 Canvases 수 제한(합산)
- 월별 우선순위 결정 횟수 제한
- 워크스페이스당 카테고리 수 제한
- 워크스페이스당 우선순위 규칙 수 제한
- 최대 재시도 기간 길이

## 자주 묻는 질문 {#frequently-asked-questions}

### 같은 카테고리 내 메시지 간 우선순위가 동일할 경우 어떻게 결정되나요? {#how-are-ties-in-priority-broken-between-messages-in-the-same-category}

같은 카테고리에서 두 Campaign의 우선순위를 비교할 때, Braze는 발송 시간이 더 이른 Campaign에 더 높은 우선순위를 부여합니다. 재시도 창이 설정되어 있는 경우, Braze는 같은 우선순위 규칙 내에서 Campaign을 비교할 때 해당 재시도 창의 종료 시간을 사용합니다. 반복 Campaign의 경우, 발송 시간은 회사 시간 기준 자정을 기준으로 다음 발생 시각으로 계산됩니다. 현지 시간 기준으로 예약된 Campaign의 경우, Braze는 회사 시간 기준의 발송 시간을 가정합니다.

같은 카테고리의 Canvases에 대해서는 Braze가 Canvas 진입 시점을 동점 처리 기준으로 사용하여, 같은 Canvas 내 모든 단계가 다른 Campaign 및 Canvases와 비교할 때 동일한 상대적 우선순위를 유지하도록 합니다.

### 메시지가 항상 발송되도록 하려면 어떻게 해야 하나요? {#how-can-i-make-sure-a-message-is-always-sent}

트랜잭션 또는 법적 알림과 같이 메시지가 항상 발송되어야 하는 시나리오가 있을 수 있습니다. 이 경우, 해당 메시지를 최대 게재빈도 설정에서 제외해야 하며, 이렇게 하면 메시지 우선순위 지정 대상에서도 제외됩니다. 이렇게 하면 다른 메시지의 발송 여부와 관계없이 예약되거나 트리거될 때마다 해당 메시지가 발송됩니다.

### 메시지는 실제로 언제 우선순위가 결정되나요? 별도의 스케줄이 있나요? {#when-are-messages-actually-prioritized-is-there-a-schedule}

각 메시지는 발송이 예상되는 시점을 기준으로 우선순위가 결정됩니다. 우선순위가 지정된 메시지에 대한 범용 평가 시간은 없습니다.

### Braze는 향후 메시지 발송 시점을 어떻게 예측하나요? {#how-does-braze-predict-when-a-future-message-sends}

Braze는 메시지 유형에 따라 향후 발송 시점을 다르게 예측합니다:

- **예약된 Campaign:** Braze는 각 Campaign이 발송될 것으로 예상되는 시간을 사용합니다. Intelligent Timing을 사용하는 예약된 Campaign의 경우, Braze는 해당 Campaign 발생에 대한 각 사용자의 최적 발송 시간을 사용합니다.
- **행동 기반 Campaign:** Braze는 각 트리거된 메시지가 발송될 것으로 예상되는 시간을 사용하며, 트리거와 발송 사이에 설정된 지연 시간도 포함됩니다.
- **캔버스 단계:** Braze는 사용자의 Canvas 진입 또는 현재 Canvas 위치에 다운스트림 단계의 타이밍을 더하여 계산합니다. Intelligent Timing을 사용하는 Canvas 메시지 단계의 경우, 사용자가 해당 단계에 진입하면 Braze는 해당 사용자에 대해 계산한 개별 발송 시간을 사용합니다. 같은 결정적 경로에 있는 후속 메시지 단계의 경우, Braze는 이후 예상 발송 시점을 결정할 때 해당 Intelligent Timing 발송 시간을 사용합니다. 사용자가 Intelligent Timing이 적용된 단계에 도달하기 전에는 예측이 최선의 추정에 기반합니다.

### 내 메시지가 이미 발송 예정이었지만 사용량 제한이나 기타 지연으로 아직 발송되지 않았습니다. 다른 Campaign의 우선순위에는 어떤 영향이 있나요? {#my-message-was-scheduled-to-send-already-but-it-hasnt-yet-because-of-rate-limiting-or-other-delays-what-does-this-mean-for-prioritizing-other-campaigns}

메시지가 아직 처리 중인 경우, Braze는 해당 메시지가 원래 예정된 시간에 발송된 것으로 가정하며, 이를 기반으로 다른 향후 우선순위 메시지의 발송 여부를 결정합니다. 해당 메시지가 최종적으로 발송되면, Braze는 실제 발송 시간을 사용합니다.

### 내 메시지가 우선순위가 지정되었지만 마지막 순간에 중단되었습니다. 우선순위에는 어떤 영향이 있나요? {#my-message-was-prioritized-but-aborted-last-minute-what-does-that-mean-for-prioritization}

메시지에 우선순위가 지정되면, Braze는 해당 메시지가 원래 예정된 시간에 발송된 것으로 가정합니다. 일반적으로 메시지 우선순위 지정 기능에서는 Liquid 중단 사용을 권장하지 않습니다. [`abort_message` Liquid 로직]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages)으로 인해 메시지가 중단된 경우, 해당 사용자에게 메시지가 발송된 것으로 가정하고 이에 따라 향후 Campaign의 우선순위를 결정합니다.

예를 들어, 메시지 1과 메시지 2가 있다고 가정해 보겠습니다. 메시지 1이 향후 더 높은 우선순위의 메시지 2를 위해 중단된 경우, 메시지 2가 실제로 발송된다는 보장은 없습니다. 메시지 2도 다음과 같은 이유로 중단될 수 있습니다:

- Liquid 중단 메시지
- 사용자가 더 이상 Segment에 포함되지 않는 경우
- 우선순위 규칙 외부의 메시지로 인한 최대 게재빈도 설정 제한

메시지 2가 중단되면 메시지 1을 다시 발송하려는 시도는 없습니다.

사용자가 낮은 우선순위의 메시지는 수신하지만 같은 최대 게재빈도 설정 규칙에 대해 높은 우선순위의 메시지를 수신하지 못하는 경우가 다음과 같은 이유로 발생할 수 있습니다:

- 높은 우선순위 메시지가 다른 규칙에 의해 최대 게재빈도가 제한되었습니다.
- 높은 우선순위 메시지가 다른 규칙에 대해 더 높은 우선순위를 가진 또 다른 향후 Campaign과 충돌했습니다.
- 낮은 우선순위 메시지 발송 시점에 사용자가 높은 우선순위 메시지의 오디언스에 포함되지 않았습니다.
- 두 메시지 모두 발송 가능했어야 하지만, 우선순위 설정 외부의 메시지가 높은 우선순위 메시지보다 먼저 발송되었습니다.

### Intelligent Timing은 메시지 우선순위 지정과 어떻게 연동되나요? {#how-does-intelligent-timing-work-with-message-prioritization}

Campaign의 경우, 메시지 우선순위 지정은 현재 발생에 대한 각 사용자의 최적 발송 시간을 사용합니다. Canvas 메시지 단계의 경우, Braze는 사용자가 해당 단계에 도달하면 각 사용자에 대해 계산된 발송 시간을 사용하고, 같은 결정적 경로에 있는 후속 메시지 단계에 해당 타이밍을 반영합니다. 자세한 내용은 [Intelligent Timing](#intelligent-timing)을 참조하세요.

### 메시지 우선순위 지정에 특화된 리포팅 또는 분석 기능이 있나요? {#is-there-any-reporting-or-analytics-functionality-specific-to-message-prioritization}

Braze는 이메일, LINE, 푸시 알림, SMS, 웹훅, WhatsApp 등 지원되는 채널에 대해 Currents 및 데이터 공유에서 메시지 우선순위 지정 관련 이벤트를 제공합니다. 여기에는 `users.messages.<channel>.Abort` 이벤트로 기록되는 우선순위 해제 및 최대 게재빈도 제한 이벤트와 설정된 재시도 창 내에서 메시지가 나중에 재시도된 시점을 보여주는 재시도 이벤트(`users.messages.<channel>.Retry` 이벤트로 기록)가 포함됩니다.

또한 메시징 진단 대시보드, 기존 우선순위 해제 및 재시도 일일 통계, 그리고 기존 [Braze 리포팅 기능]({{site.baseurl}}/user_guide/analytics/reports)을 활용하여 우선순위가 지정된 Campaign 및 Canvases의 상태와 성능을 모니터링할 수 있습니다.