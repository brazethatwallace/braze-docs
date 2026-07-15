---
nav_title: "유휴 Campaigns 및 Canvases"
permalink: "/idle_campaigns_canvases/"
hidden: true
---

# 유휴 Campaigns 및 Canvases {#idle-campaigns-and-canvases}

> 이 참조 문서에서는 Campaigns 및 Canvases의 유휴 상태에 대해 설명하고 자주 묻는 질문에 답변합니다.

{% alert note %}
2024년부터 Canvases도 Campaigns와 마찬가지로 **유휴** 상태로 표시되고 중지됩니다. Canvases가 유휴 상태이거나 중지되면 이 문서의 로직을 따릅니다.
{% endalert %}

Campaigns 및 Canvases는 일정 기간 동안 메시지를 발송하지 않았거나 사용자를 진입시키지 않은 경우 유휴 상태로 지정됩니다. 이러한 Campaigns 및 Canvases는 관련 중지 날짜에 자동으로 중지됩니다. 유휴 Campaigns 및 Canvases를 필터링하여 Campaigns 및 Canvases 목록을 정렬하고 관리할 수 있습니다.

종료 날짜가 있는 Campaigns 및 Canvases와 일회성 발송은 자동 중지 전 7일 동안 유휴 상태입니다. 11개월 동안 메시지를 발송하지 않은 Campaigns 및 Canvases는 자동 중지 전 1개월 동안 유휴 상태입니다.

## 유휴 Campaigns {#idle-campaigns}

다음 기준을 충족하는 유휴 Campaigns는 지속적으로 중지됩니다:

- 스케줄된 일회성 발송이 발송 날짜를 7일 초과한 경우
- 종료 날짜가 있는 스케줄 또는 동작 기반 Campaign이 종료 날짜를 7일 초과한 경우
- 종료 날짜가 없는 Campaign이 1년 동안 메시지를 발송하지 않은 경우

종료 날짜가 없는 Campaigns의 경우, 메시지가 발송되거나 Campaign이 업데이트되면 Campaign 중지를 위한 1년 카운트다운이 초기화됩니다. Campaigns가 중지되면 Braze는 대시보드와 이메일을 통해 고객에게 알립니다.

Campaigns는 기본 중지 날짜와 마지막 전환 기한 이후 1일 중 더 늦은 시점에 중지됩니다. 우승 배리언트 또는 개인화된 배리언트의 결과로 발생한 발송은 스케줄된 발송으로 처리되며, 우승 배리언트 또는 개인화된 배리언트가 발송된 후 7일 후에 중지됩니다. 모든 Campaigns는 매일 UTC 오전 4시에 모든 Braze 사용자에 대해 중지됩니다.

Content Cards는 만료 기한까지 중지되지 않으며, 앞서 언급한 기준과 전환 기한 규칙도 함께 적용됩니다.

유휴 Campaign을 활성 상태로 유지하는 방법은 다음 표를 참조하세요:

| 유휴 상태 사유 | Campaign을 활성화하는 단계 |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------|
| 스케줄된 일회성 발송이며 발송 날짜가 지난 Campaigns | 향후 발송을 스케줄합니다 |
| 스케줄 또는 동작 기반이며 종료 날짜가 있고 종료 날짜가 지난 Campaigns | 종료 날짜를 연장합니다 |
| 종료 날짜가 없고 1년 동안 메시지를 발송하지 않은 Campaigns | 메시지를 하나 발송하거나 Campaign을 편집합니다 |
| 종료 날짜와 일회성 발송이 있는 Campaigns | 향후 발송을 스케줄합니다 |
| 11개월 동안 메시지를 발송하지 않은 Campaigns | 메시지를 하나 발송하거나 Campaign을 편집합니다 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 인앱 메시지 Campaigns {#in-app-message-campaigns}

인앱 메시지 Campaign에 노출 횟수가 없고 30일 이상 편집되지 않은 경우 유휴 Campaign이 됩니다. 유휴 인앱 메시지 Campaign은 구성에 따라 계속 전달되지만, 인앱 메시지는 템플릿화된 인앱 메시지가 됩니다.

사용자가 노출 이벤트를 트리거하거나 마케터가 Campaign을 편집하면 Campaign이 활성 상태로 돌아가고 30일 카운터가 초기화됩니다.

## 유휴 Canvases {#idle-canvases}

다음 기준을 충족하는 유휴 Canvases는 지속적으로 중지됩니다:

- 스케줄된 일회성 발송이 발송 날짜와 최대 기간을 7일 이상 초과한 경우
- 종료 날짜가 있는 스케줄 또는 동작 기반 Canvas가 종료 날짜와 최대 기간을 7일 이상 초과한 경우
- 종료 날짜가 없는 Canvas가 12개월 이상 사용자를 진입시키지 않았거나 편집되지 않았으며 최대 기간이 지난 경우

종료 날짜가 없는 Canvases의 경우, 사용자가 진입하거나 Canvas가 업데이트되면 Canvas 중지를 위한 1년 카운트다운이 초기화됩니다. Canvases가 중지되면 Braze는 대시보드와 이메일을 통해 고객에게 알립니다.

Canvas의 [최대 기간]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)은 사용자가 주어진 Canvas를 완료하는 데 걸릴 수 있는 가장 긴 시간입니다. 이 기간에는 Content Cards 및 인앱 메시지의 만료가 포함됩니다.

유휴 Canvas를 활성 상태로 유지하는 방법은 다음 표를 참조하세요:

| 유휴 상태 사유 | Canvas를 활성화하는 단계 |
|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| 스케줄된 일회성 발송이며 최대 기간이 발송 날짜를 초과한 Canvases | 향후 발송을 스케줄합니다 |
| 스케줄 또는 동작 기반이며 종료 날짜가 있고 최대 기간이 종료 날짜를 초과한 Canvases | 종료 날짜를 연장합니다 |
| 종료 날짜가 없고 1년 동안 메시지를 발송하지 않은 Canvases | 메시지를 하나 발송하거나 Canvas를 편집합니다 |
| 종료 날짜와 일회성 발송이 있는 Canvases | 향후 발송을 스케줄합니다 |
| 11개월 동안 메시지를 발송하지 않은 Canvases | 메시지를 하나 발송하거나 Canvas를 편집합니다 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

상호작용 데이터를 복원하는 옵션이 없는 경우, 다음과 같은 이유일 수 있습니다:

- 복원 또는 기타 상호작용 데이터 관련 작업이 현재 진행 중입니다.
- 이 Canvas에 대한 상호작용 데이터가 존재하지 않았습니다.
- Canvas가 2021년 이전에 생성된 경우, 이전 정책에 따라 데이터가 영구적으로 삭제되었을 수 있습니다.

## 자주 묻는 질문 {#frequently-asked-questions}

### 어떤 Campaigns 또는 Canvases에 적용되나요? {#what-campaigns-or-canvases-does-this-apply-to}

이미 앞서 나열된 기준을 충족하는 Campaigns 및 Canvases와 앞으로 기준을 충족하게 될 Campaigns 및 Canvases에 적용됩니다.

### Campaign 또는 Canvas가 유휴 상태인지 어떻게 알 수 있나요? {#how-do-i-know-if-a-campaign-or-canvas-is-idle}

유휴 Campaigns 및 Canvases는 Campaign 및 Canvas 목록 페이지에서 **유휴** 카테고리 아래에 표시됩니다. Campaign 또는 Canvas가 중지될 날짜는 목록의 열로 표시됩니다.

!["Campaigns" 페이지의 "유휴" 필터.][1]{: style="max-width:60%;"}

### 유휴 Campaign 또는 Canvas가 업데이트되면 어떻게 되나요? {#what-happens-if-an-idle-campaign-or-canvas-is-updated}

메시지를 발송하지 않은 Campaign이나 사용자를 진입시키지 않은 Canvas가 업데이트되면 카운트다운이 초기화됩니다.

### 1년 동안 메시지를 발송하지 않은 Campaigns(또는 1년 동안 사용자를 진입시키지 않은 Canvases)가 미래에 종료 날짜가 있는 경우 어떻게 되나요? {#what-happens-to-campaigns-that-havent-sent-a-message-in-one-year-or-canvases-that-havent-entered-users-in-one-year-but-have-an-end-date-in-the-future}

이러한 Campaigns 및 Canvases는 종료 날짜 이후 7일째 UTC 오전 4시에 중지됩니다.

#### Campaigns가 자동으로 중지되는 것을 막을 수 있나요? {#can-i-stop-campaigns-from-automatically-stopping}

아니요. 이 기능은 필요한 Campaigns만 활성 상태로 유지하여 대시보드를 깔끔하게 하고 성능을 개선하는 데 도움이 됩니다. 자동 중지된 모든 Campaigns 목록을 원하시면 [고객지원 티켓을 제출]({{site.baseurl}}/help/support/)하여 제공받으세요.

### 중지된 Campaigns 및 Canvases에 대한 이메일 알림은 누가 받나요? {#who-will-receive-email-notifications-about-stopped-campaigns-and-canvases}

기본적으로 관리자 권한이 있는 모든 사용자는 Campaigns 및 Canvases 자동 중지에 대한 이메일 알림을 수신하도록 설정되어 있습니다. Campaign 또는 Canvas의 생성자는 중지 시 항상 알림을 받습니다. 사용자는 **회사 설정** > **알림 환경설정**으로 이동하여 **Campaign Automatically Stopped** 알림 및 **Canvas Automatically Stopped** 알림에서 수신자를 추가하거나 제거하여 이메일 알림 환경설정을 관리할 수 있습니다.

### Content Cards 중지는 어떻게 작동하나요? {#how-does-stopping-content-cards-work}

Campaigns의 Content Cards는 만료 기한과 적절한 버퍼 기간까지 중지되지 않습니다. 버퍼 기간(Campaign이 일회성 발송인지, 종료 날짜가 있는지, 종료 날짜가 없는지에 따라 다름)과 만료 기한 중 더 늦은 시점에 중지됩니다.

예를 들어, Content Card가 4월 1일에 만료되고 일회성 발송이며 전환 기한이 10일인 경우, 4월 12일(전환 기한 이후 10일 + 1일)에 중지됩니다. Content Card가 4월 1일에 만료되고 API 트리거 방식이며 3월 15일 이후 메시지를 발송하지 않은 경우, 다음 해 3월 15일에 만료됩니다.

Canvases는 Content Cards가 중지된 후에만 중지되며, 이는 최대 기간이 경과했음을 의미합니다.

### Canvas에 피처 플래그 실험이 있습니다. 피처 플래그가 설정된 후에도 Canvas가 활성 상태로 유지되나요? {#i-have-a-feature-flag-experiment-in-my-canvas-after-my-feature-flag-is-set-will-the-canvas-remain-active}

피처 플래그 단계가 있는 Canvases는 자동으로 중지되지 않으며 유휴 상태가 되지 않습니다.

### 활성 Campaigns만 표시하도록 필터를 적용했는데 왜 유휴 Campaigns가 Campaigns 목록에 표시되나요? {#why-am-i-seeing-idle-campaigns-displayed-in-my-campaigns-list-when-i-applied-a-filter-to-show-active-campaigns-only}

유휴 Campaigns는 중지될 때까지 활성으로 간주됩니다.

### Campaign이 아직 푸시 알림을 발송하고 있는데 유휴로 표시되나요? {#would-a-campaign-be-listed-as-idle-when-its-still-sending-push-notifications}

아니요. Campaign은 더 이상 메시지를 활발히 발송하지 않을 때 유휴로 표시됩니다.

[1]: {% image_buster /assets/unlisted_docs/img/idle_filter.png %}