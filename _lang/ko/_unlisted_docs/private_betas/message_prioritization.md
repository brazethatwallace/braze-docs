---
article_title: 메시지 우선순위 지정
permalink: /message_prioritization/
toc_headers: h2
description: "이 참조 문서에서는 최상위 메시지 우선순위 지정과 워크스페이스에서 이를 구성하는 방법에 대해 설명합니다."
---

# 메시지 우선순위 지정 {#message-prioritization}

> 메시지 우선순위 지정을 사용하여 사용자가 가장 중요한 Campaign을 수신하도록 하세요.

{% alert important %}
메시지 우선순위 지정은 현재 베타 버전입니다. 이 베타에 참여하려면 Braze 계정 매니저에게 문의하세요.
{% endalert %}

관리자만 최상위 메시지 우선순위 지정 설정을 구성할 수 있습니다. 제한된 사용자는 이 섹션의 각 페이지를 볼 수 있지만 변경할 수는 없습니다.

최상위 메시지 우선순위 지정 설정을 하려면 **설정** > **메시지 우선순위 지정**으로 이동하세요.

## 작동 방식 {#how-it-works}

메시지 우선순위 지정을 사용하면 [카테고리](#categories)와 [우선순위 지정 규칙](#prioritization-rules)을 생성하여 메시지 발송 순위를 매길 수 있습니다.

예를 들어, 뷰티 브랜드의 유료 파트너십 및 로열티 프로그램에 대한 이메일 프로모션을 관리하고 있다고 가정해 보겠습니다. 메시지 우선순위 지정을 사용하면 "유료 파트너십"과 "로열티"라는 두 개의 카테고리를 만들 수 있습니다. 그런 다음 브랜드에 더 중요한 비즈니스 기준에 따라 이 카테고리의 순위를 매길 수 있습니다. 예를 들어, 연말 시즌에는 1년 이상 멤버십 프로그램에 참여한 브랜드 고객을 우선시하기 위해 "로열티"를 "유료 파트너십"보다 높은 순위로 설정할 수 있습니다.

![유료 파트너십과 로열티 두 카테고리에 대한 우선순위 지정 규칙 예시.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization12.png %})

## 카테고리 {#categories}

우선순위 지정 규칙은 카테고리의 순위를 기반으로 하며, 카테고리는 주어진 Campaign에 할당할 수 있는 레이블입니다([태그]({{site.baseurl}}/user_guide/administrative/app_settings/tags)와 유사). 한 번에 최대 20개의 카테고리를 생성할 수 있습니다.

새 카테고리를 추가하려면:

1. **설정** > **메시지 우선순위 지정** > **카테고리**로 이동합니다.
2. **새 카테고리 생성**을 선택합니다.

![메시지 우선순위 지정 섹션의 '새 카테고리 생성' 버튼.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization1.png %})

{:start="3"}
3. 카테고리에 이름과 선택적 설명을 입력합니다.
4. **카테고리 생성**을 선택합니다.

!['P3'이라는 이름의 예시 카테고리와 '이것은 세 번째로 높은 우선순위 카테고리가 됩니다.'라는 설명.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization3.png %}){: style="max-width:60%;"}

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

규칙의 순서를 변경하려면 규칙 시작 부분의 <i class="fa-solid fa-grip-vertical"></i> 아이콘을 선택하고 드래그합니다. 규칙을 삭제하려면 <i class="fas fa-ellipsis-vertical"></i> 메뉴를 선택한 다음 **규칙 삭제**를 선택합니다.

업데이트를 적용하려면 반드시 **저장**을 선택하세요.

## Campaign 수준 설정 {#campaign-level-settings}

### 옵트인 {#opt-in}

{% alert important %}
현재 스케줄된 단일 채널 Campaign만 우선순위 지정에 옵트인할 수 있습니다. 액션 기반 및 API 트리거 Campaign과 Canvases는 지원되지 않습니다.
{% endalert %}

Campaign을 우선순위 지정에 옵트인하려면 Campaign의 **전달 스케줄** 페이지에서 **메시지 우선순위 지정에 옵트인** 체크박스를 선택합니다.

!['메시지 우선순위 지정에 옵트인' 체크박스.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization6.png %})

다음으로, **카테고리** 드롭다운에서 카테고리를 선택하여 Campaign에 카테고리를 할당합니다.

!['메시지 우선순위 지정에 옵트인' 체크박스.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization10.png %})

한 번에 최대 25개의 활성 Campaign을 옵트인할 수 있습니다. 초안, 중지 또는 아카이브된 Campaign은 이 제한에 포함되지 않습니다.

### 재시도 기간 {#retry-window}

재시도 기간을 사용하면 옵트인된 Campaign이 첫 번째 시도에서 발송할 만큼 충분히 높은 우선순위가 아닌 경우 최대 3일 동안 재시도할 수 있습니다. 이후 매일 메시지가 원래 스케줄된 시간과 동일한 시간에 다시 발송을 시도합니다. 재시도 기간의 마지막 날 이후에도 메시지가 여전히 발송되지 않으면 더 이상 재시도하지 않으며 영구적으로 우선순위가 낮아집니다.

재시도 기간은 해당 Campaign의 발송 간격보다 짧아야 합니다. 매주 월요일과 수요일에 발송하는 Campaign이 있는 경우 재시도 시도는 화요일에 발생합니다. 이는 재시도 기간을 1일로 설정해야 함을 의미합니다.

![1일로 설정된 '재시도 기간' 설정.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization13.png %})

## 최대 게재빈도 설정 {#frequency-caps}

### Campaign의 경우 {#for-campaigns}

메시지 우선순위 지정에 적격하려면 Campaign이 최대 게재빈도 설정에 옵트인되어 있어야 합니다. **전달 스케줄** 페이지의 **전달 제어** 섹션에서 Campaign이 옵트인되어 있는지 확인할 수 있습니다.

![적용 가능한 모든 채널에 대한 최대 게재빈도 설정 규칙 예시와 추가 필터 없음.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization9.png %})

### 최대 게재빈도 설정 규칙 {#frequency-capping-rules}

기존 최대 게재빈도 설정 규칙 내에서 우선순위를 최적화합니다. 필수는 아니지만, 채널, 태그 또는 카테고리에 관계없이 모든 메시지를 캡처하는 최대 게재빈도 설정 규칙을 하나 이상 설정하는 것을 강력히 권장합니다. 이 최대 게재빈도 설정 규칙은 메시지 우선순위 지정에 옵트인된 모든 메시지를 캡처하여 우선순위가 지정된 메시지가 동일한 특성을 공유하는 다른 메시지뿐만 아니라 서로 비교되도록 합니다.

이를 설정하려면 **설정** > **최대 게재빈도 설정 규칙**으로 이동합니다. 채널이 **적용 가능한 모든 채널**이고 추가 필터가 **없음**인 규칙을 생성합니다.

![적용 가능한 모든 채널에 대한 최대 게재빈도 설정 규칙 예시와 추가 필터 없음.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization11.png %})

카테고리별로 최대 게재빈도 설정 규칙을 생성할 수도 있습니다. 이를 통해 특정 카테고리가 높은 우선순위로 표시되었다는 이유만으로 해당 카테고리에서 너무 많은 메시지를 보내는 것을 방지하여 마케팅 메시지를 관리할 수 있습니다. **추가 필터**에서 **메시지 우선순위 지정 카테고리**를 선택하고 드롭다운에서 카테고리를 선택합니다.

![P2 또는 P1을 선택할 수 있는 '카테고리' 필드 드롭다운이 있는 최대 게재빈도 설정 규칙 예시.]({% image_buster /assets/unlisted_docs/img/message_prioritization/message_prioritization8.png %}){: style="max-width:70%;"}

메시지 우선순위 지정 외부의 메시지는 우선순위가 지정된 메시지와 최대 게재빈도 제한을 공유하므로, 메시지 우선순위 지정 외부의 메시지로 인해 높은 우선순위 메시지도 중단될 수 있습니다.

## 자주 묻는 질문 {#frequently-asked-questions}

### 동일한 카테고리의 메시지 간 동점은 어떻게 처리되나요? {#how-are-ties-broken-between-messages-in-the-same-category}

동일한 카테고리에서 두 메시지의 우선순위를 비교할 때, 가장 빠른 발송 시간을 가진 메시지에 더 높은 우선순위를 부여합니다. 반복 Campaign의 경우 발송 시간은 회사 시간 기준 오늘 자정 기준의 다음 발생 시간으로 계산됩니다. 현지 시간으로 스케줄된 Campaign의 경우 회사 시간 기준의 발송 시간을 가정합니다.

### 메시지 우선순위 지정과 최대 게재빈도 설정의 관계는 무엇인가요? {#what-is-the-relationship-between-message-prioritization-and-frequency-capping}

발송 시점에 발송되는 메시지를 사용자가 수신할 자격이 있는 다른 메시지와 비교합니다. 이 다른 메시지들은 동일한 최대 게재빈도 설정 규칙을 따르며 메시지 우선순위 지정에 옵트인되어 있어야 합니다. 메시지는 다음 조건을 충족할 때 발송됩니다:

1. 해당 사용자에 대해 관련 최대 게재빈도 설정 규칙이 아직 도달하지 않았으며,
2. 이 사용자에게 이 메시지를 발송해도 이후의 더 높은 우선순위 메시지가 발송되기 전에 제한에 도달하지 않는 경우.

### 메시지가 항상 발송되도록 하려면 어떻게 해야 하나요? {#how-can-i-make-sure-a-message-is-always-sent}

트랜잭션 또는 법무 알림과 같이 메시지가 항상 발송되어야 하는 시나리오가 있을 수 있습니다. 이 경우 메시지를 최대 게재빈도 설정에서 옵트아웃해야 합니다(이렇게 하면 메시지 우선순위 지정에도 부적격하게 됩니다). 이렇게 하면 다른 메시지 발송 여부에 관계없이 스케줄되거나 트리거될 때마다 메시지가 발송됩니다.

### 메시지는 실제로 언제 우선순위가 지정되나요? 스케줄이 있나요? {#when-are-messages-actually-prioritized-is-there-a-schedule}

각 메시지는 자체 스케줄된 발송 시간에 우선순위가 지정됩니다. 우선순위가 지정된 메시지에 대한 범용 평가 시간은 없습니다.

### 메시지가 이미 발송 예정이었지만 사용량 제한이나 기타 지연으로 인해 아직 발송되지 않았습니다. 이것이 다른 Campaign의 우선순위 지정에 어떤 의미가 있나요? {#my-message-was-scheduled-to-send-already-but-it-hasnt-yet-because-of-rate-limiting-or-other-delays-what-does-this-mean-for-prioritizing-other-campaigns}

메시지가 아직 처리 중인 경우 원래 스케줄된 시간에 발송된 것으로 가정합니다. 이 가정을 사용하여 다른 예정된 우선순위 메시지를 발송할지 여부를 결정합니다. 해당 메시지가 최종적으로 발송되면 실제 발송 시간을 사용합니다.

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

### Canvases를 메시지 우선순위 지정에 옵트인할 수 있나요? {#can-i-opt-canvases-into-message-prioritization}

아니요. 현재 Canvases를 메시지 우선순위 지정에 옵트인할 수 없습니다.

### 액션 기반 또는 API 트리거 Campaign은 어떻게 되나요? {#what-about-action-based-or-api-triggered-campaigns}

현재 메시지 우선순위 지정은 액션 기반 또는 API 트리거 Campaign에 대해 지원되지 않습니다.

### 메시지 우선순위 지정에 특화된 보고서 또는 분석 기능이 있나요? {#is-there-any-reporting-or-analytics-functionality-specific-to-message-prioritization}

현재 이 기능에 특화된 보고서 또는 분석 기능은 없습니다. 우선순위가 지정된 Campaign의 상태와 성능을 모니터링하려면 기존 [Braze 보고 기능]({{site.baseurl}}/user_guide/analytics/reporting)을 사용하는 것을 권장합니다.