---
nav_title: FAQ
article_title: Campaigns FAQ
page_order: 10
page_type: FAQ
description: "이 페이지에서는 Campaigns에 대해 자주 묻는 질문에 대한 답변을 제공합니다."
tool: Campaigns
---

# 자주 묻는 질문 {#frequently-asked-questions}

> 이 문서에서는 Campaigns에 대해 자주 묻는 질문에 대한 답변을 제공합니다.

## 멀티채널 Campaign은 어떻게 만드나요? {#how-do-i-create-a-multichannel-campaign}

**Campaign 만들기**의 [멀티채널 Campaigns]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#create-a-multichannel-campaign)에서 설정 단계 및 지원 채널을 확인하세요.

### 멀티채널 Campaign에 대조군을 추가할 수 있나요? {#can-i-add-a-control-group-to-my-multichannel-campaign}

**Campaign 만들기**의 [대조군]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#multichannel-control-groups)을 참조하세요. 크로스채널 테스트의 경우 [Canvas]({{site.baseurl}}/user_guide/messaging/canvas)를 사용하세요.

### Campaign 테스트 및 최적화를 시작하는 방법에는 어떤 것이 있나요? {#what-are-some-ways-i-can-start-testing-and-optimizing-campaigns}

다변량 Campaign과 여러 배리언트가 포함된 Canvases를 실행하는 것이 좋은 출발점입니다! 예를 들어, 서로 다른 문구나 제목란을 사용하는 하나의 메시지를 테스트하기 위해 [다변량 Campaign]({{site.baseurl}}/user_guide/messaging/ab_testing)을 실행할 수 있습니다. 여러 배리언트가 포함된 Canvases는 전체 워크플로를 테스트하는 데 도움이 됩니다.

### Campaign 열람율이 감소한 이유는 무엇인가요? {#why-did-the-open-rate-for-my-campaign-decrease}

낮은 열람율이 항상 기술적 문제와 관련이 있는 것은 아닙니다. 이메일 클리핑으로 인해 추적 픽셀이 누락되는 문제가 있을 수 있습니다. 그러나 콘텐츠나 오디언스 규모의 변화로 인해 이메일을 여는 사용자가 줄어든 것일 수도 있습니다.

### Campaign 오디언스는 어떻게 평가되나요? {#how-are-campaign-audiences-evaluated}

기본적으로 Campaign은 진입 시점에 오디언스 필터를 확인합니다. 지연이 포함된 실행 기반 Campaign의 경우 발송 시점에 Segment 기준을 재평가하여 메시지가 전송될 때 사용자가 여전히 타겟 오디언스에 포함되어 있는지 확인하는 옵션이 있습니다.

### 주어진 Campaign 또는 Canvas의 고유 수신자 수와 발송 수가 다른 이유는 무엇인가요? {#why-is-there-a-difference-between-the-number-of-unique-recipients-and-the-number-of-sends-for-a-given-campaign-or-canvas}

한 가지 가능한 설명은 Campaign 또는 Canvas에 재적격성이 켜져 있기 때문입니다. 이 경우 Segment 및 전달 설정에 적합한 사용자가 메시지를 두 번 이상 수신할 수 있습니다. 재적격성이 켜져 있지 않다면, 발송 수와 고유 수신자 간의 차이는 사용자가 여러 플랫폼에 걸쳐 여러 기기를 프로필에 연결해 두었기 때문일 수 있습니다.

예를 들어, iOS와 웹 푸시 알림이 모두 포함된 Canvas가 있는 경우, 모바일과 데스크톱 기기를 모두 사용하는 사용자는 두 개 이상의 메시지를 수신할 수 있습니다.

### *고유 수신자*가 타겟팅한 사용자 수보다 많은 이유는 무엇인가요? {#why-is-_unique-recipients_-higher-than-the-number-of-users-i-targeted}

*고유 수신자*가 예상 오디언스보다 높을 수 있는 이유는 Braze가 보고를 위해 일별 고유 수신자를 추적하기 때문입니다. 이를 통해 Braze는 사용자가 메시지를 수신할 때마다 전환 기간 내의 전환을 어트리뷰트할 수 있으며, 여러 수신을 하나의 총 생애 수치로 합치지 않습니다(합치면 전환 계산이 왜곡됩니다).

예를 들어, 사용자가 월요일과 금요일에 Campaign을 수신하고 각 발송 후 전환한 경우, Braze는 이를 두 번의 수신과 두 번의 전환으로 보고할 수 있습니다. Braze가 두 발송에 걸쳐 하나의 생애 "고유" 수치만 계산한다면, 유효한 전환이 누락되거나 하나의 수신자에 대해 이중 계산되어 Campaign 성과를 읽기 어렵게 됩니다.

반복 Campaign과 재적격성에도 같은 패턴이 적용됩니다. 두 명의 사용자가 오늘과 내일 각각 반복 발송을 수신하면, *고유 수신자*는 두 프로필이 아닌 네 개의 일별 수신자 행을 계산합니다.

### 멀티채널 Campaign에서 전환 수가 고유 사용자 수를 초과할 수 있는 이유는 무엇인가요? {#why-can-the-number-of-conversions-exceed-the-number-of-unique-users-for-multichannel-campaigns}

**Campaign 만들기**의 [전환 및 보고]({{site.baseurl}}/user_guide/messaging/campaigns/creating_campaign#multichannel-conversions)와 **전환 이벤트**의 [전환 추적 규칙]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events#conversion-tracking-rules)을 참조하세요.

### Campaign이 사용 중인 Segment보다 도달 가능한 사용자 기반이 더 작은 이유는 무엇인가요? {#why-does-my-campaign-have-a-smaller-reachable-user-base-than-the-segment-that-im-using-for-the-campaign}

[글로벌 컨트롤 그룹]({{site.baseurl}}/user_guide/audience/global_control_group)이 설정되어 있으면 도달 가능한 오디언스의 일정 비율이 Campaign 수신에서 제외됩니다. 이는 Segment의 도달 가능 사용자 수가 Campaign의 도달 가능 사용자 수보다 클 수 있음을 의미하며, Campaign이 동일한 Segment를 사용하더라도 마찬가지입니다.

### 현지 시간대 전달이란 무엇인가요? {#what-does-local-time-zone-delivery-offer}

현지 시간대 전달을 사용하면 사용자의 개별 시간대에 맞춰 메시징 Campaign을 Segment에 전달할 수 있습니다. 현지 시간대 전달이 없으면 Campaign은 Braze의 회사 시간대 설정에 따라 예약됩니다.

예를 들어, 런던 소재 회사가 오후 12시에 Campaign을 발송하면 미국 서부 해안 사용자에게는 오전 4시에 도달합니다. 앱이 특정 국가에서만 사용 가능한 경우에는 문제가 되지 않을 수 있지만, 그렇지 않은 경우 사용자 기반에게 이른 아침 푸시 알림을 보내는 것은 피하는 것이 좋습니다.

### Braze는 사용자의 시간대를 어떻게 인식하나요? {#how-does-braze-recognize-a-users-time-zone}

Braze는 사용자의 기기에서 시간대를 자동으로 감지합니다. 이를 통해 시간대의 정확성과 사용자의 완전한 커버리지를 보장합니다. User API를 통해 생성되었거나 시간대가 없는 사용자는 SDK에 의해 앱에서 인식될 때까지 회사의 시간대가 기본 시간대로 설정됩니다.

대시보드의 [회사 설정]({{site.baseurl}}/user_guide/administer/global/admin_settings)에서 회사 시간대를 확인할 수 있습니다.

### Braze는 현지 시간대 전달을 위해 사용자를 언제 평가하나요? {#when-does-braze-evaluate-users-for-local-time-zone-delivery}

Braze는 다음 시점에 사용자의 진입 자격을 평가합니다.

- 예약된 날의 사모아 시간(UTC+13)
- 예약된 날의 현지 시간

사용자가 진입 자격을 갖추려면 두 확인을 모두 통과해야 합니다. 예를 들어, Canvas가 2021년 8월 7일 오후 2시 현지 시간대에 시작되도록 예약된 경우, 뉴욕에 위치한 사용자를 타겟팅하려면 다음 자격 확인이 필요합니다.

- 2021년 8월 6일 오후 9시 뉴욕 시간
- 2021년 8월 7일 오후 2시 뉴욕 시간

진입하려면 사용자가 두 평가 시점 모두에서 오디언스와 필터에 일치해야 합니다. 사용자가 첫 번째 확인에서 자격이 없으면 Braze는 두 번째 확인을 실행하지 않습니다. 시작 전에 사용자가 Segment에 있어야 하는 최소 시간은 없습니다. 각 확인 시점의 자격만이 중요합니다.

이 평가 동작은 [대시보드에서 Campaign을 얼마나 미리 예약하느냐](#how-do-i-schedule-a-local-time-zone-campaign)와 별개입니다. 최소 24시간 전에 예약하는 것은 전체 24시간 현지 시간대 기간에 걸쳐 메시지가 전달되도록 하기 위한 권장 사항이지, 각 사용자가 24시간 동안 오디언스에 있어야 한다는 요구 사항이 아닙니다.

#### 예시 {#examples}

예를 들어, Campaign이 오후 7시 UTC에 전달되도록 예약된 경우, 시간대가 식별되는 즉시(예: 사모아) Campaign 발송을 대기열에 넣기 시작합니다. 이는 메시지 발송을 준비하는 것이지 Campaign을 발송하는 것이 아닙니다. 자격을 확인할 때 사용자가 필터에 일치하지 않으면 타겟 오디언스에 포함되지 않습니다.

또 다른 예로, 같은 날에 발송되도록 예약된 두 개의 Campaign을 만들고 싶다고 가정합시다. 하나는 아침에, 하나는 저녁에 발송하며, 사용자가 이미 첫 번째 Campaign을 수신한 경우에만 두 번째 Campaign을 수신할 수 있도록 필터를 추가합니다. 현지 시간대 전달의 경우, 일부 사용자는 두 번째 Campaign을 수신하지 못할 수 있습니다. 이는 사용자의 시간대가 식별될 때 자격을 확인하는데, 예약된 시간이 사용자의 시간대에서 아직 도래하지 않았다면 첫 번째 Campaign을 수신하지 못했으므로 두 번째 Campaign에 대한 자격이 없기 때문입니다.

다음 타임라인은 시간 제한 멤버십 기간이 포함된 Segment 정의를 가정합니다. 이 예시에서 사용자는 가입 후 24시간이 지나면 Segment에서 나갑니다. 이 필터 동작은 사용자가 첫 번째 확인을 통과하고 두 번째 확인에서 실패하는 이유 중 하나입니다.

![첫 번째 확인 전에 Segment에 진입한 후 두 번째 확인 전에 나가는 사용자의 타임라인.]({% image_buster /assets/img/local_time_zone_diagram.png %})

{% details 타임라인 설명 %}

1. 사용자 A가 PST 오후 6시 59분(사모아 오후 4시 59분)에 Segment에 진입합니다.
2. Braze는 사모아 시간 오후 7시에 Segment 멤버십을 확인하여 다음 24시간 동안 Campaign을 수신할 자격이 있는 사용자를 결정합니다. 이 시점에서 사용자 A는 Segment에 있습니다.
3. Segment에는 24시간 기간이 있으므로, 사용자 A는 가입 후 24시간이 지난 PST 오후 6시 59분(사모아 오후 4시 59분)에 Segment에서 나갑니다.
4. 현지 시간 Campaign이 PST 오후 7시에 발송되지만, 사용자 A는 이미 Segment에서 나간 상태입니다.

{% enddetails %}

### 현지 시간대 Campaign은 어떻게 예약하나요? {#how-do-i-schedule-a-local-time-zone-campaign}

이전 섹션에서는 Braze가 현지 시간대 전달의 자격을 평가하는 시점(두 번의 확인)을 설명합니다. 이 섹션에서는 대시보드에서 Campaign 스케줄을 설정하는 시점(예약 리드 타임)과 24시간 미만의 사전 통보로 예약할 경우 어떤 사용자가 메시지를 수신하는지를 설명합니다.

Campaign을 예약할 때 지정된 시간에 발송하도록 선택한 다음 **사용자의 현지 시간대로 Campaign 발송**을 선택합니다.

Braze는 모든 현지 시간대 Campaign을 24시간 전에 예약할 것을 강력히 권장합니다. 이러한 Campaign은 하루 전체에 걸쳐 발송해야 하므로, 24시간 전에 예약하면 전체 Segment에 메시지가 도달할 수 있습니다. 그러나 필요한 경우 24시간 미만 전에도 이러한 Campaign을 예약할 수 있습니다. Braze는 발송 시간을 1시간 이상 지난 사용자에게는 메시지를 보내지 않습니다.

예를 들어, 현재 오후 1시이고 현지 시간대 Campaign을 오후 3시로 예약하면, 현지 시간이 오후 3시에서 오후 4시 사이인 모든 사용자에게 즉시 발송되지만, 현지 시간이 오후 5시인 사용자에게는 발송되지 않습니다. 또한, Campaign에 선택한 발송 시간은 회사의 시간대에서 아직 지나지 않은 시간이어야 합니다.

24시간 미만 전에 예약된 현지 시간대 Campaign을 편집해도 메시지의 스케줄은 변경되지 않습니다. 현지 시간대 Campaign을 나중 시간(예: 오후 6시 대신 오후 7시)으로 발송하도록 편집하기로 결정한 경우, 원래 발송 시간이 선택되었을 때 타겟 Segment에 있던 사용자는 여전히 원래 시간(오후 6시)에 메시지를 수신합니다. 현지 시간대를 더 이른 시간(예: 오후 5시 대신 오후 4시)으로 편집하면, Campaign은 여전히 원래 시간(오후 5시)에 모든 Segment 멤버에게 발송됩니다.

{% alert note %}
Canvas 구성 요소의 경우, 현지 시간대 전달을 위해 사용자가 24시간 동안 구성 요소에 있을 필요는 없습니다.
{% endalert %}

사용자에게 Campaign 재적격성을 허용한 경우, 원래 시간(오후 5시)에 다시 수신합니다. 그러나 이후 모든 Campaign 발생에 대해서는 업데이트된 시간에만 메시지가 발송됩니다.

### 현지 시간대 Campaign 변경 사항은 언제 적용되나요? {#when-do-changes-to-local-time-zone-campaigns-take-effect}

현지 시간대 Campaign의 타겟 Segment에는 전체 Segment에 대한 전달을 보장하기 위해 시간 기반 필터에 최소 48시간의 기간이 포함되어야 합니다. 예를 들어, 다음 필터를 사용하여 둘째 날의 사용자를 타겟팅하는 Segment를 고려해 보세요.

- 1일 이상 전에 처음 앱을 사용함
- 2일 미만 전에 처음 앱을 사용함

현지 시간대 전달은 전달 시간과 사용자의 현지 시간대에 따라 이 Segment의 사용자를 놓칠 수 있습니다. 이는 사용자의 시간대가 전달을 트리거할 시점에 사용자가 이미 Segment를 떠났을 수 있기 때문입니다.

### 출시 전에 예약된 Campaign에 어떤 변경을 할 수 있나요? {#what-changes-can-i-make-to-scheduled-campaigns-ahead-of-launch}

Campaign이 예약되면, 메시지를 발송 대기열에 넣기 전에 메시지 작성 이외의 항목을 편집해야 합니다. 모든 Campaign과 마찬가지로, 출시 후에는 전환 이벤트를 편집할 수 없습니다.

### 예약된 Campaign을 업데이트했는데 시작되지 않은 이유는 무엇인가요? {#i-updated-my-scheduled-campaign-why-didnt-it-launch}

이는 Campaign이 업데이트된 정확한 시간에 시작되도록 예약된 경우에 발생할 수 있습니다. 예를 들어, 현재 오후 3시 10분이고 Campaign을 오후 3시 10분에 시작하도록 변경한 후 **Campaign 업데이트**를 선택했다면, 이미 오후 3시 10분이 지났으므로 예약된 시작 시간이 경과한 것입니다. 같은 시간으로 Campaign을 예약하는 대신 **Campaign 시작 즉시 발송**을 선택하세요.

### 예약된 Campaign의 메시지가 대기열에 들어가기 전의 "안전 구간"은 얼마인가요? {#what-is-the-safe-zone-before-messages-on-a-scheduled-campaign-are-enqueued}

다음 시간 내에 메시지를 변경하는 것을 권장합니다.

- **일회성 예약 Campaign:** 예약된 발송 시간까지 편집 가능.
- **반복 예약 Campaign:** 예약된 발송 시간까지 편집 가능.
- **현지 발송 시간 Campaign:** 예약된 발송 시간 최소 24시간 전까지 편집 가능.
- **최적 발송 시간 Campaign:** Campaign이 발송되도록 예약된 날의 최소 24시간 전까지 편집 가능.

이러한 권장 사항 밖에서 메시지를 변경하면, 발송된 메시지에 업데이트가 반영되지 않을 수 있습니다. 예를 들어, 오후 12시 현지 시간에 발송되도록 예약된 Campaign의 발송 시간을 3시간 전에 편집하면, 다음과 같은 상황이 발생할 수 있습니다.

- Braze는 발송 시간을 1시간 이상 지난 사용자에게는 메시지를 보내지 않습니다.
- 이미 대기열에 들어간 메시지는 조정된 시간이 아닌 원래 대기열에 넣어진 시간에 발송될 수 있습니다.

변경이 필요한 경우 현재 Campaign을 중지하는 것을 권장합니다(대기열에 있는 메시지가 취소됩니다). 그런 다음 Campaign을 복제하고 필요한 변경을 수행한 후 새 Campaign을 시작할 수 있습니다. 이미 첫 번째 Campaign을 수신한 사용자를 이 Campaign에서 제외해야 할 수 있습니다. 시간대 발송을 허용하도록 Campaign 스케줄 시간을 다시 조정해야 합니다.

### 서머타임 전환일에 일별 예약 Campaign에 사용자가 진입하지 않은 이유는 무엇인가요? {#why-did-no-users-enter-my-daily-scheduled-campaign-on-daylight-saving-time-day}

서머타임(DST) 전환일에는, 시계가 앞으로 또는 뒤로 조정되는지에 따라 일별 예약 Campaign이 평소보다 최대 1시간 일찍 또는 늦게 실행될 수 있습니다. Segment가 예약된 발송 시간의 1시간 이내에 해당하는 타임스탬프가 있는 커스텀 속성이나 이벤트에 의존하는 경우, DST 전환일에 Campaign이 자격을 평가할 때 해당 사용자가 아직 자격을 갖추지 못할 수 있습니다.

예를 들어, 사용자가 일반적으로 오후 3시 UTC에 커스텀 속성 업데이트를 받고, Campaign이 매일 뉴욕(동부 시간) 오전 10시 30분에 실행된다고 가정합니다. 뉴욕이 표준 시간(UTC-5)인 동안, 동부 시간 오전 10시 30분은 UTC 오후 3시 30분에 해당하므로, Campaign은 속성이 기록된 후에 실행됩니다. 뉴욕이 서머타임(UTC-4)으로 전환되면, 동부 시간 오전 10시 30분은 UTC 오후 2시 30분에 해당하므로, 서머타임 전환일에 Campaign이 오후 3시 UTC 속성 업데이트 전에 실행될 수 있습니다. 자격 부여 속성이 아직 존재하지 않기 때문에 해당 사용자는 필터에서 제외됩니다. 재적격성이 꺼져 있으면, 이전 날에 진입한 사용자는 다시 진입할 수 없으므로 해당 날의 진입이 0건이 됩니다.

이를 방지하려면 커스텀 속성 또는 이벤트 업데이트가 Campaign의 예약된 발송 시간보다 1시간 이상 전에 발생하도록 하세요.

### Campaign에 진입하는 사용자 수가 예상 수와 일치하지 않는 이유는 무엇인가요? {#why-does-the-number-of-users-entering-a-campaign-not-match-the-expected-number}

Campaign에 진입하는 사용자 수는 오디언스와 트리거가 평가되는 방식 때문에 예상 수와 다를 수 있습니다. Braze에서 오디언스는 트리거 전에 평가됩니다([속성 변경]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/attribute_triggers#change-custom-attribute-value) 트리거를 사용하는 경우 제외). 이로 인해 트리거 동작이 평가되기 전에 선택한 오디언스에 포함되지 않는 사용자는 Campaign에서 제외됩니다.

{% alert tip %}
Campaign 문제 해결에 대한 추가 지원이 필요한 경우, 문제 발생 후 30일 이내에 Braze 지원팀에 문의하세요. 지난 30일간의 진단 로그만 보유하고 있습니다.
{% endalert %}

### 편집 후 사용자가 Campaign을 두 번 수신한 이유는 무엇인가요? {#why-did-users-receive-my-campaign-twice-after-i-edited-it}

라이브 Campaign을 먼저 중지하지 않고 편집하면, 사용자가 메시지를 두 번 수신할 수 있습니다. 이는 라이브 Campaign을 편집하면 원래 대기열이 아직 처리 중인 상태에서 업데이트된 버전을 위해 사용자가 다시 대기열에 들어가기 때문입니다. 원래 메시지를 아직 수신하지 않은 사용자가 두 대기열 모두에 포함될 수 있습니다. 이를 방지하려면 변경하기 전에 항상 [Campaign을 중지]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/change_your_campaign_after_launch#stopping-your-campaign)하세요.

### Campaign 분석 페이지에서 CSV 사용자 데이터 내보내기와 CSV 이메일 주소 내보내기 옵션의 차이점은 무엇인가요? {#what-is-the-difference-between-the-csv-export-user-data-and-csv-export-email-address-options-on-my-campaign-analytics-page}

**CSV 이메일 주소 내보내기** 옵션을 선택하면 이메일 주소가 있는 사용자의 데이터만 다운로드됩니다. 예를 들어, 100,000명의 사용자로 구성된 Segment가 있지만 그 중 50,000명만 이메일 주소가 있는 경우, **CSV 이메일 주소 내보내기**를 클릭하면 내보내기에는 50,000행의 데이터만 포함됩니다. 이에 비해 **CSV 사용자 데이터 내보내기**를 선택하면 모든 사용자 데이터가 내보내집니다.

### API 식별자로 Campaign을 검색할 수 있나요? {#can-i-search-for-a-campaign-by-its-api-identifier}

예, **Campaigns** 페이지에서 `api_id:YOUR_API_ID` 필터를 사용하여 API 식별자로 Campaign을 검색할 수 있습니다. 자세한 내용은 [Campaign 검색]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/search_campaigns)을 참조하세요.

### 입력 필드와 표시되는 텍스트에서 공백이 다르게 나타나는 이유는 무엇인가요? {#why-does-whitespace-appear-differently-in-input-fields-versus-displayed-text}

공백 처리는 CSS 스타일링으로 인해 입력 필드와 표시되는 텍스트 구성 요소 간에 다릅니다. 기본 `white-space: normal` CSS가 적용된 텍스트 구성 요소에서는 연속된 여러 공백이 표시될 때 하나의 공백으로 축소됩니다. 이는 렌더링된 텍스트의 표준 HTML 동작입니다.

입력 필드는 정확한 데이터 입력을 위해 정확한 간격을 보고 편집할 수 있어야 하므로, 입력한 그대로 여러 공백을 유지합니다. 이는 여러 공백이 있는 텍스트가 입력 필드(모든 공백이 유지됨)에서 볼 때와 대시보드의 다른 부분(CSS가 여러 공백을 축소할 수 있음)에서 표시될 때 다르게 보일 수 있음을 의미합니다.

예를 들어, Campaign 이름이나 UTM 매개변수에 여러 공백을 입력하면 모든 공백이 유지된 상태로 표시됩니다. 그러나 동일한 텍스트가 검색 결과, Campaign 목록 또는 기타 텍스트 구성 요소에 나타날 때는 CSS 공백 처리로 인해 여러 공백이 하나의 공백으로 표시될 수 있습니다.

### API Campaign과 API 트리거 Campaign의 차이점은 무엇인가요? {#what-is-the-difference-between-api-campaigns-and-api-triggered-campaigns}

API 트리거 Campaign을 사용하면 Braze 대시보드 내에서 Campaign 문구, 다변량 테스트 및 재적격성 규칙을 관리하면서 자체 서버 및 시스템에서 해당 콘텐츠의 전달을 트리거할 수 있습니다. 이러한 메시지에는 실시간으로 메시지에 템플릿화될 추가 데이터도 포함할 수 있습니다.

API Campaign은 API를 사용하여 발송된 메시지를 추적하는 데 사용됩니다. 대부분의 Campaign과 달리, 메시지, 수신자 또는 스케줄을 지정하지 않고 대신 API 호출에 식별자를 전달합니다.

### API 트리거 Campaign을 사용자가 수신했는지 확인하려면 어떻게 해야 하나요? {#how-can-i-confirm-if-my-users-received-an-api-triggered-campaign}

**Campaign 수신** 필터를 사용하여 [Segment를 생성]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)한 다음 확인하려는 특정 API 트리거 Campaign을 선택할 수 있습니다. Segment를 저장한 후 [`/users/export/segment` 엔드포인트]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)를 사용하여 해당 Segment의 사용자를 내보냅니다.

### Campaign을 삭제할 수 있나요? {#can-i-delete-a-campaign}

아니요, 하지만 [Campaign을 아카이브]({{site.baseurl}}/user_guide/messaging/governance/archiving)할 수 있습니다.

### 실행 기반 Campaign과 API 트리거 Campaign의 차이점은 무엇인가요? {#what-is-the-difference-between-action-based-and-api-triggered-campaigns}

<style>
table th:nth-child(1) {
    width: 50%;
}
table th:nth-child(3) {
    width: 50%;
}
</style>

#### 실행 기반 {#action-based}

실행 기반 전달 Campaign 또는 이벤트 트리거 Campaign은 트랜잭션 또는 성과 기반 메시지에 매우 효과적이며, 사용자가 특정 이벤트를 완료한 후 메시지를 트리거하여 발송할 수 있습니다.

| 장점 | 단점 |
| ---- | ---- |
| • **메시지 활동 로그**를 통해 플랫폼으로 들어오는 JSON 페이로드 확인 가능(테스트 사용자가 이벤트를 트리거한 경우)<br><br>• 개인화 요소가 커스텀 이벤트 속성정보에 포함됨<br><br>• 커스텀 이벤트를 사용하여 메시지 수신 자격이 있는 사용자의 Segment를 만들 수 있음 | • 데이터 포인트를 소비함 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="실행 기반" }

#### API 트리거 {#api-triggered}

API 트리거 및 서버 트리거 Campaign은 더 고급 트랜잭션을 처리하는 데 이상적이며, 자체 서버 및 시스템에서 Campaign 콘텐츠의 전달을 트리거할 수 있습니다. 메시지를 트리거하는 API 요청에는 실시간으로 메시지에 템플릿화될 추가 데이터도 포함할 수 있습니다.

| 장점 | 고려 사항 |
| ---- | ---- |
| • 데이터 포인트를 소비하지 않음<br><br>• 개인화 요소가 JSON 페이로드 속성정보에 포함됨 | • JSON 페이로드 속성정보에서 메시지 수신 자격이 있는 사용자의 Segment를 만들 수 없음<br><br>• **메시지 활동 로그**로 들어오는 JSON 페이로드를 확인할 수 없음 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="API 트리거" }

### "요청 시간 초과" 오류에 대한 지원 티켓을 제출할 때 어떤 정보를 포함해야 하나요? {#what-should-i-include-when-submitting-a-support-ticket-for-a-request-timed-out-error}

Campaign 또는 Canvas를 생성하거나 편집하는 중 "요청 시간 초과" 오류가 발생하여 [Braze 지원팀]({{site.baseurl}}/user_guide/administer/personal/braze_support)에 문의해야 하는 경우, 해결 속도를 높이기 위해 다음 정보를 포함하세요.

{% multi_lang_include messaging/support_ticket_request_timed_out_details.md context='campaign' %}

### 발송 분석이 설정한 최대 수신자 제한과 일치하지 않는 이유는 무엇인가요? {#why-dont-my-send-analytics-match-the-maximum-recipient-limit-i-set}

활성 Campaign에 최대 수신자 제한을 추가하거나 변경하면, 다음과 같은 이유로 발송 분석에 제한이 반영되지 않을 수 있습니다.

- **출시 후 제한 추가:** 최대 수신자 제한이 Campaign 시작 시 설정되지 않은 경우, 제한을 적용하기 전에 이미 대기열에 들어간 메시지는 계속 발송됩니다. 제한은 변경을 저장한 후 대기열에 넣는 발송에만 적용됩니다.
- **사용량 제한조치와의 상호작용:** Campaign에 사용량 제한도 적용된 경우, 메시지가 더 긴 시간 범위에 걸쳐 분배될 수 있습니다. 최대 수신자 제한은 메시지가 대기열에 들어갈 때 평가되며, 전달될 때가 아닙니다. 메시지가 이미 대기열에 있는 상태에서 제한이 변경되면, 해당 메시지에는 원래 제한이 적용됩니다.
- **반복 Campaign:** 반복 Campaign의 경우, 각 예약 발송이 최대 수신자 제한을 독립적으로 평가합니다. 발송 간에 제한을 변경해도 이전 발송 수는 소급 조정되지 않습니다.

불일치를 방지하려면 Campaign을 시작하기 전에 최대 수신자 제한을 설정하고, 발송이 진행 중인 동안에는 수정하지 마세요.

### 발송 수가 예상 오디언스 규모보다 낮은 이유는 무엇인가요? {#why-are-sends-lower-than-the-estimated-audience-size}

여러 요인으로 인해 발송 수가 예상 오디언스 규모보다 낮을 수 있습니다.

- **실행 기반 전달:** 사용자가 트리거를 수행한 후에만 발송이 생성되므로, 발송은 시간이 지남에 따라 누적되며 Campaign을 처음 구축할 때 표시되는 사전 추정치에 미치지 못할 수 있습니다.
- **출시 후 오디언스 편집:** 출시 후 진입 또는 타겟 필터를 변경하면 **예상 오디언스** 스냅샷이 이후 발송에서 실제 자격을 가진 사용자와 동기화되지 않을 수 있습니다(예: 사용자가 재진입 자격이 없는 경우).
- **오디언스 경로 단계:** Canvas의 경우, [오디언스 경로]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/audience_paths) 단계는 사용자가 자격을 갖춘 가장 높은 우선순위 브랜치에 해당하는 사용자에게만 메시지를 보내므로, 평면 Segment 수에 비해 발송이 줄어들 수 있습니다.
- **대조군:** [글로벌 컨트롤 그룹]({{site.baseurl}}/user_guide/audience/global_control_group) 또는 Campaign 수준 대조군이 사용 중인 경우, 오디언스의 일부가 전달에서 제외됩니다.
- **전달 타이밍 및 기간:** 현지 시간대 또는 예약 Campaign의 경우, 사용자가 진입 시점과 발송 시점 모두에서 자격을 갖추어야 합니다. 특정 시간대의 사용자는 전달 기간 밖에 있을 수 있습니다.
- **이메일 중복 제거:** Campaign 또는 Canvas가 동일한 이메일을 가진 여러 사용자를 타겟팅하는 경우, 발송 시점에 해당 이메일 주소를 가진 무작위 사용자가 선택됩니다. 메시지는 한 번만 발송되고 중복이 제거되어 동일한 이메일 주소로 여러 번 전달되지 않지만, 예상 오디언스 규모에는 모든 사용자가 포함됩니다.
- **이메일 전달 가능성 필터:** 이메일 Campaign의 경우, Braze는 하드 바운스된 사용자, 이메일 수신을 거부한 사용자, 스팸으로 표시된 사용자, 프로필에 이메일 주소가 없는 사용자, 또는 필수 구독 그룹에 구독하지 않은 사용자를 제외합니다. 이러한 확인은 발송 시점에 실행되므로, Segment에 있는 사용자도 실제 발송 수에서 제외될 수 있습니다.
- **CSV 가져오기 타이밍:** [CSV 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)로 Segment 멤버십이 유지되는 경우, 예약된 Campaign이 발송된 후에 추가된 이메일 주소는 해당 발송으로 도달하지 않습니다. Braze는 발송 시점의 Segment 멤버십 스냅샷을 유지하지 않으므로, 현재 Segment 규모가 실제 메시지를 받은 사용자 수를 초과할 수 있습니다.
- **글로벌 최대 게재빈도 설정:** 워크스페이스 수준의 제한으로 인해 자격이 있는 사용자가 동일한 기간에 다른 메시지를 수신하지 못하여 실제 발송이 줄어들 수 있습니다.
- **새로 가져온 사용자:** 방금 자격을 갖춘 프로필은 다음 평가 또는 발송 패스까지 수신하지 못할 수 있으므로, 이후 실행에서 수치가 따라잡습니다.
- **푸시 도달 가능성:** 푸시 Campaign의 경우, 오디언스가 올바른 앱에 대해 푸시가 활성화되어 있는지 확인하세요. 푸시 활성 사용자를 필터링하지 않으면, 예상 오디언스에 푸시를 수신할 수 없는 프로필이 포함될 수 있습니다. **타겟 사용자** 단계에서 **도달 가능한 사용자**를 확인하여 더 가까운 운영 추정치를 얻으세요.
- **사용량 제한조치:** [전달 속도 사용량 제한]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting)은 단일 발송 발생 시 Braze가 분당 보내는 메시지 수를 제한합니다. Braze는 더 긴 기간에 걸쳐 전달을 분산하므로, 일부 발송이 지연되거나 아직 수치에 반영되지 않았거나, 제한이 자격 있는 오디언스에 비해 낮은 경우 완료되지 않을 수 있습니다.
- **재적격성 기간:** 아직 재적격성이 없는 사용자는 쿨다운 기간 동안 다시 수신하지 않으므로, 해당 기간 동안 발송이 예상 오디언스 규모에 미치지 않습니다.
- **보고 기간:** 분석 시간 범위에 모든 발송이 포함되지 않을 수 있습니다.
- **Segment 재평가:** 발송 시점에 재평가하는 실행 기반 또는 예약 Campaign의 경우, Campaign이 대기열에 들어갔을 때 Segment에 있던 사용자가 실제 메시지 발송 시점에는 더 이상 자격이 없을 수 있습니다.
- **발송 제한:** **타겟 오디언스**의 최대 사용자 수(또는 유사한 제한)가 제한에 도달하면 전달을 중지합니다.
- **엄격한 기기 또는 브라우저 필터:** 최신 앱 버전이나 브라우저만 일치하는 필터는 광범위한 Segment 미리보기에 비해 발송 시점에 도달 가능한 대상을 축소합니다.

### 글로벌 최대 게재빈도 설정에 대해 자주 묻는 질문은 어디에 있나요? {#where-are-frequently-asked-questions-about-global-frequency-capping}

캘린더 일, 사일런트 푸시, 웹훅, Canvas 동작 및 관련 주제에 대한 질문은 [사용량 제한 및 최대 게재빈도 설정]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping)의 [자주 묻는 질문]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/faq)을 참조하세요.

### Campaign의 발송률이 낮아지는 이유는 무엇인가요? {#why-is-my-campaign-experiencing-lower-send-rates}

일별 예약 Campaign이 시간이 지남에 따라 더 적은 사용자에게 발송되는 경우, 다음 사항을 확인하세요.

- **재적격성이 켜져 있는지 확인:** 재적격성이 없으면 Braze는 각 사용자에게 한 번만 메시지를 보냅니다. 일별 예약 Campaign에서는 오디언스에 일치하고 아직 메시지를 수신하지 않은 사용자만 각 발송에 자격이 있습니다. 더 많은 사용자가 메시지를 수신할수록 이후 각 발송에는 자격이 있는 사용자가 더 적어지므로 발송량이 감소합니다.
- **오디언스가 고정 멤버십인지 확인:** [CSV 가져오기]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/csv_import)를 Segment 필터로 사용하는 것과 같이 고정 사용자 목록으로 구축된 오디언스는 자동으로 새 멤버를 얻지 않습니다. 새 진입자가 없으면 사용자가 메시지를 수신함에 따라 발송량이 회복될 수 없습니다.

단일 발생의 발송을 줄이는 [전달 속도 사용량 제한]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping#delivery-speed-rate-limiting) 및 기타 요인에 대해서는 [발송 수가 예상 오디언스 규모보다 낮은 이유는 무엇인가요?](#why-are-sends-lower-than-the-estimated-audience-size)를 참조하세요.

### 이메일과 단문 메시지 서비스에서 고유 수신자가 발송 수를 초과할 수 있는 이유는 무엇인가요? {#why-can-unique-recipients-exceed-sends-for-email-and-sms}

이메일과 단문 메시지 서비스의 경우, Braze는 ESP 발송 시도 전에 **고유 수신자**를 증가시키고, 성공적인 ESP 응답 후에 **발송**을 증가시킵니다. 영구적인 오류(예: 잘못된 이메일 주소) 또는 중복 주소로 인해 고유 수신자가 발송을 초과할 수 있습니다.

### **마지막 발송**이 예약한 발송 시간과 일치하지 않는 이유는 무엇인가요? {#why-doesnt-last-sent-match-my-scheduled-send-time}

단일 예약 발송이 있는 Campaign의 경우, **마지막 발송**은 시작 시간과 일치합니다. **현지 시간대로 발송**이 활성화된 반복 Campaign의 경우, 더 이른 시간대의 사용자(예: GMT vs. PST)에 대한 발송이 워크스페이스 스케줄 시간 전에 완료되므로 **마지막 발송**이 예약된 시간보다 더 일찍 표시될 수 있습니다.

### 중지된 과거 Campaign이 **Analytics** 페이지에서 더 이상 측정기준을 표시하지 않는 이유는 무엇인가요? {#why-does-a-stopped-historical-campaign-no-longer-show-metrics-on-the-analytics-page}

**Analytics** 탭은 기본적으로 지난 90일을 표시합니다. Campaign이 해당 기간 밖에서 마지막으로 발송된 경우, **Analytics** 페이지에서 Campaign이 발송된 시기를 포함하도록 날짜 범위를 조정할 때까지 측정기준이 0으로 표시될 수 있습니다. 자세한 내용은 [Campaign 분석]({{site.baseurl}}/user_guide/analytics/reports/campaign_analytics)을 참조하세요.

**인터랙션 데이터 복원**은 Campaign 분석을 복원하지 않습니다. 이는 리타겟팅 필터 및 사용자 인터랙션 기록에만 적용됩니다. 자세한 내용은 [메시징 인터랙션 데이터]({{site.baseurl}}/messaging_interaction_data)를 참조하세요.