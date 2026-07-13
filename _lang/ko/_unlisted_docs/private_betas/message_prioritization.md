---
article_title: 메시지 우선순위 지정
permalink: /message_prioritization/
toc_headers: h2
description: "이 참조 문서에서는 최상위 메시지 우선순위 지정과 워크스페이스에서 이를 구성하는 방법에 대해 설명합니다."
---

# 메시지 우선순위 지정 {#message-prioritization}

> 메시지 우선순위 지정을 사용하여 사용자가 가장 중요한 Campaign을 수신하도록 하세요.

{% alert important %}
메시지 우선순위 지정은 현재 베타 버전입니다. 이 베타에 참여하려면 Braze 계정 매니저에게 문의하세요.<br><br>이 문서는 2026년 7월 말 프로덕션 릴리스로 계획된 메시지 우선순위 지정 버전을 반영합니다. 여기에 설명된 일부 동작은 아직 모든 베타 워크스페이스에서 사용할 수 없을 수 있습니다.
{% endalert %}

관리자만 최상위 메시지 우선순위 지정 설정을 구성할 수 있습니다. 제한된 사용자는 이 섹션의 각 페이지를 볼 수 있지만 변경할 수는 없습니다.

최상위 메시지 우선순위 지정 설정을 하려면 **설정** > **메시지 우선순위 지정**으로 이동하세요.

## 작동 방식 {#how-it-works}

메시지 우선순위 지정을 사용하면 [카테고리](#categories)와 [우선순위 지정 규칙](#prioritization-rules)을 생성하여 메시지 발송 순위를 매길 수 있습니다.

예를 들어, 뷰티 브랜드가 유료 파트너십 및 로열티 프로그램에 대한 이메일 프로모션을 관리하고 있다고 가정해 보겠습니다. 메시지 우선순위 지정을 사용하여 "유료 파트너십"과 "로열티"라는 두 개의 카테고리를 만들 수 있습니다. 그런 다음 브랜드에 더 중요한 비즈니스 기준에 따라 이 카테고리의 순위를 매길 수 있습니다. 연말 시즌에는 1년 이상 멤버십 프로그램에 참여한 고객을 우선시하기 위해 "로열티"를 "유료 파트너십"보다 높은 순위로 설정할 수 있습니다.

![유료 파트너십과 로열티 두 카테고리에 대한 우선순위 지정 규칙 예시.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization12.png %})

발송 시점에 Braze는 발송되는 메시지를 해당 사용자가 수신할 수 있는 다른 메시지와 비교합니다. 이 다른 메시지들은 우선순위 지정에 옵트인되어 있고, 우선순위 카테고리가 설정되어 있으며, 동일한 최대 게재빈도 설정 기간 내에서 동일한 최대 게재빈도 설정 규칙에 포함되어야 합니다. 현재 메시지를 발송하면 이후의 더 높은 우선순위 메시지 발송이 차단될 경우, Braze는 낮은 우선순위 메시지의 우선순위를 낮춥니다. 구성된 재시도 기간에 따라 해당 낮은 우선순위 메시지는 나중에 재시도되거나 발송되지 않습니다.

메시지 우선순위 지정은 다음을 평가할 수 있습니다:

- 스케줄된 Campaign
- 액션 기반 Campaign
- Canvases

Braze는 현재 메시지를 발송하면 이후의 더 높은 우선순위 메시지 발송이 차단될 수 있는지 평가할 때, 각 메시지의 예상 발송 시간을 예측합니다. Braze가 Campaign과 Canvases의 향후 발송 시간을 예측하는 방법에 대한 자세한 내용은 [Braze는 향후 메시지 발송 시간을 어떻게 예측하나요?](#how-does-braze-predict-when-a-future-message-sends)를 참조하세요.

### 지원되는 메시지 유형 {#supported-message-types}

메시지 우선순위 지정은 최대 게재빈도 설정과 동일한 채널을 지원합니다:

- 푸시 알림
- 이메일
- SMS
- 웹훅
- WhatsApp
- LINE

우선순위 지정 및 최대 게재빈도 설정에서 iOS 푸시, Android 푸시, 웹 푸시 및 기타 푸시 알림 플랫폼은 별도의 채널이 아닌 하나의 공유 푸시 채널로 취급됩니다.

## 카테고리 {#categories}

우선순위 지정 규칙은 카테고리의 순위를 기반으로 하며, 카테고리는 주어진 Campaign 또는 Canvas에 할당할 수 있는 레이블입니다([태그]({{site.baseurl}}/user_guide/administrative/app_settings/tags)와 유사). 한 번에 최대 20개의 카테고리를 생성할 수 있습니다.

새 카테고리를 추가하려면:

1. **설정** > **메시지 우선순위 지정** > **카테고리**로 이동합니다.
2. **새 카테고리 생성**을 선택합니다.

![메시지 우선순위 지정 섹션의 '새 카테고리 생성' 버튼.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization1.png %})

{:start="3"}
3. 카테고리에 이름과 선택적 설명을 입력합니다.
4. **카테고리 생성**을 선택합니다.

!["P3"이라는 이름의 예시 카테고리와 "이것은 세 번째로 높은 우선순위 카테고리입니다."라는 설명.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization3.png %}){: style="max-width:60%;"}

카테고리를 편집하거나 삭제하려면 <i class="fas fa-ellipsis-vertical"></i> 메뉴를 선택합니다.

## 우선순위 지정 규칙 {#prioritization-rules}

카테고리가 설정되면 우선순위 지정 규칙 세트에서 순위를 매길 수 있습니다. 규칙은 우선순위 내림차순으로 순위가 매겨집니다. 한 번에 최대 10개의 우선순위 지정 규칙을 생성할 수 있습니다.

1. **설정** > **메시지 우선순위 지정** > **우선순위 지정 규칙**으로 이동하여 규칙을 구성합니다.

![아직 우선순위가 설정되지 않은 '우선순위 지정 규칙' 섹션.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization4.png %})

{:start="2"}
2. **규칙 추가**를 선택합니다.
3. 드롭다운에서 카테고리를 선택합니다.

![P1이 카테고리로 선택된 '우선순위 1' 우선순위 지정 규칙.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization5.png %})

{:start="4"}
4. 마지막 규칙 아래에서 **+ 규칙 추가**를 선택하여 규칙을 계속 추가합니다.

규칙의 순서를 변경하려면 규칙의 <i class="fa-solid fa-grip-vertical"></i> 아이콘을 선택하고 드래그합니다. 규칙을 삭제하려면 <i class="fas fa-ellipsis-vertical"></i> 메뉴를 선택한 다음 **규칙 삭제**를 선택합니다.

업데이트를 적용하려면 반드시 **저장**을 선택하세요.

## Campaign 수준 설정 {#campaign-level-settings}

### 옵트인 {#opt-in}

Campaign을 우선순위 지정에 옵트인하려면 Campaign의 전달 설정에서 **메시지 우선순위 지정에 옵트인** 체크박스를 선택합니다.

!["메시지 우선순위 지정에 옵트인" 체크박스.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization6.png %})

다음으로, **카테고리** 드롭다운에서 카테고리를 선택하여 Campaign에 카테고리를 할당합니다.

![Campaign의 전달 설정에 있는 메시지 우선순위 지정 카테고리 드롭다운.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization10.png %})

메시지 우선순위 지정은 스케줄된 Campaign과 액션 기반 Campaign을 지원합니다.

### Intelligent Timing

Intelligent Timing을 사용하는 Campaign의 경우, 메시지 우선순위 지정은 원래 Campaign 스케줄만이 아니라 Braze가 각 사용자에 대해 선택한 발송 시간을 사용하여 메시지를 비교합니다. 이를 통해 Braze는 해당 사용자에게 가장 먼저 발송될 가능성이 높은 메시지를 고려할 수 있습니다.

반복 Intelligent Timing Campaign의 경우, Braze는 해당 Campaign을 다른 적격한 우선순위 지정 메시지와 비교할 때 현재 반복에 대해 선택된 알려진 발송 시간을 사용할 수 있습니다.

### 재시도 기간 {#retry-window}

재시도 기간을 사용하면 옵트인된 메시지가 첫 번째 시도에서 발송할 만큼 충분히 높은 우선순위가 아닌 경우 최대 3일 동안 재시도할 수 있습니다. 이후 매일 메시지가 원래 스케줄되거나 트리거된 시간과 동일한 시간에 다시 발송을 시도합니다. 재시도 기간의 마지막 날 이후에도 메시지가 여전히 발송되지 않으면 더 이상 재시도하지 않으며 영구적으로 우선순위가 낮아집니다.

반복 스케줄된 Campaign의 경우, 재시도 기간은 해당 Campaign의 최소 발송 간격보다 짧아야 합니다. 재시도는 Campaign이 해당 날짜에 정상적으로 발송되도록 스케줄되어 있지 않더라도 항상 원래 발송 시간으로부터 하루 단위로 발생합니다. 예를 들어, 매주 월요일과 수요일에 발송하는 Campaign이 있는 경우 재시도 시도는 화요일에 발생하므로 재시도 기간을 1일로 설정해야 합니다. 매주 월요일, 수요일, 금요일에 발송하는 Campaign이 있고 금요일 발송이 1일 재시도 기간으로 재시도되는 경우, 재시도 시도는 토요일에 발생하며 월요일이 아닙니다.

![1일로 설정된 '재시도 기간' 설정.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization13.png %})

액션 기반 Campaign의 경우, 재시도는 트리거된 메시지가 원래 발송될 것으로 예상된 시간을 기준으로 합니다.

예외 이벤트를 사용하는 액션 기반 Campaign은 재시도 기간을 지원하지 않습니다.

Canvas 메시지의 재시도 기간은 단계 수준에서 구성됩니다. 지원되는 Canvas 메시징 단계의 경우, Canvas 메시지 단계의 우선순위가 낮아지고 재시도 기간이 구성되어 있으면 Braze는 재시도 기간 내에서 해당 단계를 나중에 재시도할 수 있습니다.

## Canvas 수준 설정 {#canvas-level-settings}

Canvas를 메시지 우선순위 지정에 옵트인하려면 Canvas 설정에서 메시지 우선순위 지정을 활성화하고 Canvas에 카테고리를 할당합니다.

사용자가 여러 우선순위 지정 메시지에 적격한 경우, Braze는 지원되는 채널에서 옵트인된 Campaign과 적격한 Canvas 메시지 단계를 함께 평가합니다.

Campaign의 경우, 여기에는 적격한 스케줄된 발송과 액션 기반 발송이 포함됩니다.

Canvases의 경우, 여기에는 다음이 포함됩니다:

- 사용자가 진입할 자격이 있는 향후 스케줄된 Canvases
- 사용자가 현재 진행 중인 Canvases

Canvas 우선순위 지정은 전부 아니면 전무가 아닙니다. 더 높은 우선순위의 Campaign이 하나의 캔버스 단계의 우선순위를 낮출 수 있지만, 카테고리 순위, 발송 시간 및 최대 게재빈도 설정 규칙에 따라 동일한 Canvas의 이후 적격 단계는 여전히 발송될 수 있습니다.

### Braze가 향후 메시지를 평가하는 방법 {#how-braze-evaluates-future-messages}

Braze는 메시지 유형에 따라 Campaign과 Canvases를 다르게 평가합니다.

#### Campaigns

Braze는 각 적격 Campaign 메시지를 해당 메시지의 예상 발송 시간을 사용하여 비교합니다.

#### Canvases

Braze는 Canvas를 순회하여 사용자가 수신할 수 있는 향후 메시지를 결정합니다. 시작 지점은 다음과 같습니다:

- 향후 스케줄된 Canvases의 경우 Canvas 진입
- 사용자가 이미 Canvas에 있는 경우 사용자의 현재 단계

그런 다음 Braze는 다음과 같은 방식으로 캔버스 단계를 평가합니다.

##### 메시징 단계 {#messaging-steps}

이 단계들은 지원되는 채널에서 발송될 때 우선순위 지정에 포함되며 적격 메시지 세트에 추가됩니다.

- 메시지 단계
- Content Optimizer 단계

##### 연속 단계 {#continuation-steps}

이 단계들은 우선순위 지정에서 무시되며 전방 탐색에 영향을 미치지 않습니다.

- 컨텍스트 업데이트 단계
- 사용자 업데이트 단계
- 오디언스 동기화 단계
- 기능 플래그 단계
- 고정 지연이 있는 지연 단계

##### 경계 단계 {#boundary-steps}

Braze는 사용자가 Canvas에서 실제로 해당 지점을 통과할 때까지 이 단계에서 전방 탐색을 중지합니다.

- 개인화된 지연이 있는 지연 단계
- 분기 단계 뒤에 오는 지연 단계
- 행동 경로 단계
- 실험 단계

##### 분기 단계 {#branching-steps}

이 단계들은 Canvas를 여러 가능한 경로로 분할합니다.

- 결정 분할 단계
- 오디언스 경로 단계

우선순위 지정 경로에 분기 단계가 포함된 경우, Braze는 모든 경로가 유효하다고 가정하고 지원되는 채널의 모든 병렬 메시지 단계를 우선순위 지정에 고려합니다. 최대 게재빈도 설정 규칙은 채널별로 적용될 수 있으므로, 필요한 경우 병렬 메시지 단계는 채널별로 중복 제거됩니다.

예를 들어, 한 분기에서 이메일을 발송할 수 있고 다른 분기에서도 이메일을 발송할 수 있는 경우, Braze는 이를 전방 탐색 우선순위 지정을 위한 단일 가능한 이메일 발송으로 취급합니다. 다른 분기에서 푸시를 발송할 수 있는 경우, Braze는 해당 가능한 푸시 발송도 별도로 고려합니다.

Intelligent Timing을 사용하는 Canvas 메시지 단계의 경우, Braze는 사용자가 실제로 해당 단계에 도달할 때까지 최선의 노력으로 시간을 예측합니다. 사용자가 Intelligent Timing 단계에 진입하고 Braze가 사용자별 발송 시간을 계산하면, 메시지 우선순위 지정은 현재 단계에 대해 해당 계산된 발송 시간을 사용합니다. 결정적 경로에서 Braze는 후속 메시지 단계의 예상 발송 시간을 결정할 때 해당 업데이트된 시간도 반영합니다.

Content Optimizer 단계는 항상 지정된 채널에서 발송되므로 메시징 단계처럼 취급됩니다. 그러나 재시도가 실험을 방해할 수 있으므로 재시도 기간은 Content Optimizer 단계에 적용되지 않습니다. 다른 지원되는 Canvas 메시징 단계는 재시도 기간을 사용할 수 있습니다. 지원되지 않는 채널의 캔버스 단계는 메시지 우선순위 지정에 참여하지 않습니다.

## 최대 게재빈도 설정 {#frequency-caps}

메시지 우선순위 지정은 기존 최대 게재빈도 설정 규칙 내에서 작동합니다. 우선순위 지정된 메시지는 다음 조건을 충족할 때만 발송될 수 있습니다:

1. 해당 사용자에 대해 관련 최대 게재빈도 설정 규칙이 아직 도달하지 않았으며,
2. 이 메시지를 발송해도 이후의 더 높은 우선순위 메시지가 발송되기 전에 사용자가 제한에 도달하지 않는 경우.

최대 게재빈도 설정의 적용을 받지 않는 메시지는 메시지 우선순위 지정에 적격하지 않습니다. 메시지가 항상 발송되도록 하려면 최대 게재빈도 설정에서 옵트아웃하세요. 이렇게 하면 메시지 우선순위 지정에서도 제외됩니다.

### 지원되는 Campaign 및 캔버스 단계의 경우 {#for-supported-campaigns-and-canvas-steps}

메시지 우선순위 지정에 적격하려면 Campaign 또는 캔버스 단계가 지원되는 채널을 사용하고 최대 게재빈도 설정 구성 내에서 평가되어야 합니다.

![최대 게재빈도 설정 규칙 예시.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization9.png %})

### 최대 게재빈도 설정 규칙 {#frequency-capping-rules}

Braze는 기존 최대 게재빈도 설정 규칙 내에서 우선순위를 최적화합니다. 우선순위 지정된 메시지는 동일한 적용 가능한 최대 게재빈도 설정 규칙을 공유하는 경우에만 비교됩니다.

예를 들어, 동일한 이메일 최대 게재빈도 설정 규칙에 포함되는 두 개의 이메일 Campaign은 서로 우선순위를 비교할 수 있습니다. 두 메시지가 동일한 최대 게재빈도 설정 규칙에 포함되지 않는 한, 낮은 우선순위의 이메일 Campaign이 더 높은 우선순위의 SMS 메시지를 위해 우선순위가 낮아지지는 않습니다.

채널별 최대 게재빈도 설정 규칙, 카테고리별 규칙, 태그 필터 또는 모든 채널에 적용되는 규칙을 사용할 수 있습니다. 메시지 우선순위 지정은 옵트인된 메시지에 적용되는 규칙과 함께 작동합니다.

카테고리별로 최대 게재빈도 설정 규칙을 생성하여 특정 카테고리에서 사용자가 수신하는 메시지 수를 관리할 수 있습니다. 이를 통해 높은 우선순위 카테고리가 너무 많은 메시지를 발송하는 것을 방지할 수 있습니다. **추가 필터**에서 **메시지 우선순위 지정 카테고리**를 선택하고 드롭다운에서 카테고리를 선택합니다.

![P2 또는 P1을 선택할 수 있는 '카테고리' 필드 드롭다운이 있는 최대 게재빈도 설정 규칙 예시.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization8.png %}){: style="max-width:70%;"}

메시지 우선순위 지정 외부의 메시지는 우선순위 지정된 메시지와 최대 게재빈도 제한을 공유하므로, 메시지 우선순위 지정 외부의 메시지로 인해 높은 우선순위 메시지도 중단될 수 있습니다.

## 예시 {#examples}

### 높은 우선순위 Campaign 대 낮은 우선순위 Campaign {#higher-priority-campaign-versus-lower-priority-campaign}

사용자가 같은 날 두 개의 이메일 Campaign에 적격하고 두 Campaign 모두 동일한 최대 게재빈도 설정 규칙에 포함된다고 가정합니다. 높은 우선순위 Campaign이 그날 나중에 발송될 것으로 예상되는 경우, Braze는 높은 우선순위 Campaign이 대신 발송될 수 있도록 낮은 우선순위 Campaign의 우선순위를 낮출 수 있습니다. 낮은 우선순위 Campaign에 재시도 기간이 있는 경우, Braze는 나중에 다시 시도할 수 있습니다.

### 높은 우선순위 액션 기반 Campaign 대 낮은 우선순위 메시지 {#higher-priority-action-based-campaign-versus-lower-priority-message}

사용자가 2시간 후에 발송되도록 설정된 높은 우선순위 액션 기반 Campaign을 트리거했다고 가정합니다. 해당 지연 동안 Braze는 다른 우선순위 지정 메시지를 먼저 발송할지 결정할 때 해당 예정된 액션 기반 Campaign을 고려할 수 있습니다. 이를 통해 높은 우선순위 액션 기반 Campaign이 곧 발송될 것으로 예상되는 경우 낮은 우선순위 메시지가 먼저 발송되는 것을 방지할 수 있습니다.

### 높은 우선순위 Canvas 대 낮은 우선순위 Campaign {#higher-priority-canvas-versus-lower-priority-campaign}

사용자가 낮은 우선순위 Campaign에 적격하지만, 그날 나중에 높은 우선순위 Canvas 메시지를 수신할 것으로 예상된다고 가정합니다. Braze가 해당 향후 Canvas 메시지를 이미 평가할 수 있는 경우, 높은 우선순위 Canvas 메시지가 대신 발송될 수 있도록 낮은 우선순위 Campaign의 우선순위를 낮출 수 있습니다.

### 경계 단계가 있는 높은 우선순위 Canvas 대 낮은 우선순위 Campaign {#higher-priority-canvas-with-a-boundary-step-versus-lower-priority-campaign}

높은 우선순위 Canvas에 다음 메시지 단계 전에 행동 경로 단계, 실험 또는 개인화된 지연이 포함되어 있다고 가정합니다. 사용자가 해당 단계에 도달하여 통과할 때까지 Braze는 하위의 높은 우선순위 Canvas 메시지를 전방 탐색하지 않습니다. 이 경우 낮은 우선순위 Campaign이 먼저 발송될 수 있습니다.

### 높은 우선순위 분기 Canvas 대 낮은 우선순위 메시지 {#higher-priority-branching-canvas-versus-lower-priority-message}

높은 우선순위 Canvas가 사용자가 따르는 분기에 따라 다른 메시지를 발송할 수 있다고 가정합니다. Braze는 메시지를 비교할 때 이러한 가능한 향후 경로를 보수적으로 평가합니다. 이를 통해 높은 우선순위 Canvas 분기가 나중에 동일한 최대 게재빈도 제한을 사용할 수 있는 경우 낮은 우선순위 메시지가 먼저 발송되는 것을 방지할 수 있습니다.

### Canvas Intelligent Timing 단계 및 하위 단계 {#canvas-intelligent-timing-step-and-downstream-steps}

사용자가 Intelligent Timing을 사용하는 높은 우선순위 Canvas 메시지 단계에 진입했다고 가정합니다. Braze가 Intelligent Timing 단계에 대한 해당 사용자의 발송 시간을 계산하면, 메시지 우선순위 지정은 현재 단계와 동일한 결정적 경로의 이후 메시지 단계에 대해 해당 사용자별 발송 시간을 사용합니다. 이를 통해 Braze는 이전 경로 추정치만이 아닌 업데이트된 시간을 사용하여 하위 Canvas 메시지를 다른 우선순위 지정 발송과 비교할 수 있습니다.

## 제한 사항 {#limitations}

메시지 우선순위 지정에는 다음과 같은 제한 사항이 있습니다:

- 워크스페이스당 최대 20개의 카테고리
- 워크스페이스당 최대 10개의 우선순위 지정 규칙
- 한 번에 최대 25개의 활성 옵트인된 우선순위 지정 스케줄 항목
- 한 번에 최대 25개의 활성 옵트인된 우선순위 지정 액션 기반 항목
- 최대 3일의 재시도 기간

스케줄 항목 제한은 스케줄된 Campaign과 스케줄된 옵트인 Canvases를 합산한 총계입니다. 액션 기반 항목 제한은 액션 기반 Campaign과 액션 기반 옵트인 Canvases를 합산한 총계입니다.

## 자주 묻는 질문 {#frequently-asked-questions}

### 동일한 카테고리의 메시지 간 동점은 어떻게 처리되나요? {#how-are-ties-broken-between-messages-in-the-same-category}

동일한 카테고리에서 두 Campaign의 우선순위를 비교할 때, Braze는 더 빠른 발송 시간을 가진 Campaign에 더 높은 우선순위를 부여합니다. 재시도 기간이 구성된 경우, Braze는 동일한 우선순위 규칙 내에서 Campaign을 비교할 때 해당 재시도 기간의 종료 시점을 사용합니다. 반복 Campaign의 경우 발송 시간은 회사 시간 기준 자정 기준의 다음 발생 시간으로 계산됩니다. 현지 시간으로 스케줄된 Campaign의 경우 Braze는 회사 시간 기준의 발송 시간을 가정합니다.

동일한 카테고리의 Canvases의 경우, Braze는 동일한 Canvas의 모든 단계가 다른 Campaign 및 Canvases에 대해 동일한 상대적 우선순위를 유지하도록 Canvas 진입 시간을 동점 처리 기준으로 사용합니다.

### 메시지가 항상 발송되도록 하려면 어떻게 해야 하나요? {#how-can-i-make-sure-a-message-is-always-sent}

트랜잭션 또는 법무 알림과 같이 메시지가 항상 발송되어야 하는 시나리오가 있을 수 있습니다. 이 경우 메시지를 최대 게재빈도 설정에서 옵트아웃해야 하며, 이렇게 하면 메시지 우선순위 지정에도 부적격하게 됩니다. 이렇게 하면 다른 메시지 발송 여부에 관계없이 스케줄되거나 트리거될 때마다 메시지가 발송됩니다.

### 메시지는 실제로 언제 우선순위가 지정되나요? 스케줄이 있나요? {#when-are-messages-actually-prioritized-is-there-a-schedule}

각 메시지는 예상 발송 시간에 따라 우선순위가 지정됩니다. 우선순위 지정된 메시지에 대한 범용 평가 시간은 없습니다.

### Braze는 향후 메시지 발송 시간을 어떻게 예측하나요? {#how-does-braze-predict-when-a-future-message-sends}

Braze는 각 메시지 유형에 따라 향후 발송 시간을 다르게 예측합니다:

- **스케줄된 Campaign:** Braze는 각 Campaign의 예상 발송 시간을 사용합니다. Intelligent Timing을 사용하는 스케줄된 Campaign의 경우, Braze는 해당 Campaign 발생에 대한 각 사용자의 최적 발송 시간을 사용합니다.
- **액션 기반 Campaign:** Braze는 각 트리거된 메시지의 예상 발송 시간을 사용하며, 트리거와 발송 사이에 구성된 지연도 포함합니다.
- **캔버스 단계:** Braze는 사용자의 Canvas 진입 또는 현재 Canvas 위치와 하위 단계의 시간을 사용합니다. Intelligent Timing을 사용하는 Canvas 메시지 단계의 경우, 사용자가 해당 단계에 진입하면 Braze는 해당 사용자에 대해 계산한 사용자별 발송 시간을 사용합니다. 동일한 결정적 우선순위 지정 경로의 후속 메시지 단계에 대해 Braze는 이후 예상 발송 시간을 결정할 때 해당 Intelligent Timing 발송 시간을 사용합니다. 사용자가 Intelligent Timing 단계에 도달하기 전에는 예측이 최선의 노력으로 유지됩니다.

### 메시지가 이미 발송 예정이었지만 사용량 제한이나 기타 지연으로 인해 아직 발송되지 않았습니다. 이것이 다른 Campaign의 우선순위 지정에 어떤 의미가 있나요? {#my-message-was-scheduled-to-send-already-but-it-hasnt-yet-because-of-rate-limiting-or-other-delays-what-does-this-mean-for-prioritizing-other-campaigns}

메시지가 아직 처리 중인 경우 Braze는 원래 스케줄된 시간에 발송된 것으로 가정하며, 이를 기반으로 다른 예정된 우선순위 메시지를 발송할지 여부를 결정합니다. 해당 메시지가 최종적으로 발송되면 Braze는 실제 발송 시간을 사용합니다.

### 메시지가 우선순위가 지정되었지만 마지막 순간에 중단되었습니다. 이것이 우선순위 지정에 어떤 의미가 있나요? {#my-message-was-prioritized-but-aborted-last-minute-what-does-that-mean-for-prioritization}

메시지가 우선순위가 지정되면 Braze는 원래 스케줄된 시간에 발송된 것으로 가정합니다. 일반적으로 메시지 우선순위 지정에서는 Liquid 중단을 사용하지 않는 것을 권장합니다. [`abort_message` Liquid 로직]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages)으로 인해 메시지가 중단된 경우, 해당 사용자에게 발송된 것으로 가정하고 이후 Campaign의 우선순위를 그에 따라 지정합니다.

두 개의 메시지가 있다고 가정해 보겠습니다: 메시지 1과 메시지 2. 메시지 1이 이후의 더 높은 우선순위 메시지 2를 위해 중단된 경우, 이것이 메시지 2가 실제로 발송된다는 것을 보장하지는 않습니다. 메시지 2도 다음과 같은 이유로 중단될 수 있습니다:

- Liquid 중단 메시지
- 사용자가 더 이상 Segment에 속하지 않음
- 우선순위 지정 규칙 외부의 메시지로 인한 최대 게재빈도 제한

메시지 2가 중단되면 메시지 1을 다시 발송하려는 시도는 없습니다.

사용자가 동일한 최대 게재빈도 설정 규칙에 대해 낮은 우선순위 메시지는 수신하지만 높은 우선순위 메시지는 수신하지 못할 수 있는 이유는 다음과 같습니다:

- 높은 우선순위 메시지가 다른 규칙에 의해 최대 게재빈도 제한에 걸렸습니다.
- 높은 우선순위 메시지가 다른 규칙에 대해 더 높은 우선순위를 가진 다른 이후 Campaign과 충돌했습니다.
- 낮은 우선순위 메시지 발송 시점에 사용자가 높은 우선순위 메시지의 오디언스에 속하지 않았습니다.
- 두 메시지 모두 발송 가능했어야 하지만, 우선순위 지정 설정 외부의 메시지가 높은 우선순위 메시지보다 먼저 발송되었습니다.

### 경계 단계는 Canvas 우선순위 지정에 어떤 영향을 미치나요? {#how-do-boundary-steps-affect-canvas-prioritization}

경계 단계는 사용자가 Canvas에서 실제로 해당 지점에 도달하거나 완료할 때까지 Canvas를 통한 전방 탐색을 중지합니다. 예를 들어, 높은 우선순위 메시지가 행동 경로 단계, 개인화된 지연 또는 실험 단계 뒤에 있는 경우, Braze는 사용자가 해당 경계를 통과할 때까지 해당 하위 메시지를 사용하여 낮은 우선순위 Campaign을 차단하지 않습니다.

### Canvas 우선순위 지정에서 분기는 어떻게 작동하나요? {#how-does-branching-work-in-canvas-prioritization}

Canvas에 분기 경로가 포함된 경우, Braze는 각 경로가 유효하다고 가정하고 채널별로 가능한 최대 향후 발송량을 비교합니다. 이를 통해 높은 우선순위 Canvas 경로가 나중에 동일한 최대 게재빈도 제한을 소비할 수 있는 경우 낮은 우선순위 메시지가 먼저 발송되는 것을 방지할 수 있습니다.

### 사용자가 동시에 우선순위 지정된 Canvas를 통해 여러 경로를 가지고 있는 경우 어떻게 되나요? {#what-happens-if-a-user-has-multiple-paths-through-a-prioritized-canvas-at-the-same-time}

Braze는 각 유효한 경로를 가능한 향후 경로로 취급하고 해당 경로의 적격 메시지 단계를 독립적으로 평가합니다. 여러 경로가 동일한 채널에서 발송할 수 있는 경우, Braze는 필요한 경우 해당 가능한 발송을 채널별로 중복 제거합니다.

### Canvas 우선순위 지정에서 Intelligent Timing은 어떻게 작동하나요? {#how-does-intelligent-timing-work-in-canvas-prioritization}

사용자가 Intelligent Timing Canvas 메시지 단계에 도달하기 전에 Braze는 해당 단계의 시간을 최선의 노력으로 예측합니다. 사용자가 해당 단계에 진입하고 Braze가 사용자별 발송 시간을 계산하면, 메시지 우선순위 지정은 현재 단계와 동일한 결정적 우선순위 지정 경로의 후속 메시지 단계에 대해 해당 계산된 발송 시간을 사용합니다.

### 메시지 우선순위 지정에 특화된 보고서 또는 분석 기능이 있나요? {#is-there-any-reporting-or-analytics-functionality-specific-to-message-prioritization}

Braze는 이메일, LINE, 푸시 알림, SMS, 웹훅, WhatsApp을 포함한 지원되는 채널에 대해 Currents 및 데이터 공유에서 메시지 우선순위 지정 관련 이벤트를 제공합니다. 여기에는 `users.messages.<channel>.abort` 테이블에 기록되는 우선순위 낮춤 및 최대 게재빈도 제한 이벤트와 구성된 재시도 기간 내에서 메시지가 나중에 재시도된 시점을 보여주는 재시도 이벤트(`user_messages_<channel>_retry` 테이블에 기록)가 포함됩니다.

Campaign의 경우, 메시징 진단 대시보드, 기존 우선순위 낮춤 및 재시도 일일 통계, 그리고 기존 [Braze 보고 기능]({{site.baseurl}}/user_guide/analytics/reporting)을 사용하여 우선순위 지정된 Campaign과 Canvases의 상태와 성능을 모니터링할 수도 있습니다.