---
nav_title: 유휴 Campaigns 및 Canvases
article_title: 유휴 Campaigns 및 Canvases
page_order: 1
page_type: reference
alias: /idle_campaigns/
description: "이 참조 문서에서는 Campaigns 및 Canvases의 유휴 상태에 대해 자동 중지 기준과 자주 묻는 질문을 포함하여 설명합니다."
toc_headers: h2
---

# 유휴 Campaigns 및 Canvases {#idle-campaigns-and-canvases}

> Campaigns 및 Canvases는 정해진 기간 동안 메시지를 전송하거나 사용자를 진입시키지 않으면 유휴 상태가 됩니다.

Braze는 유휴 Campaigns 및 Canvases를 관련 중지 날짜에 자동으로 중지합니다. Braze가 중지할 때까지 해당 메시징은 활성 상태를 유지합니다. 일회성 전송 및 종료 날짜가 있는 메시징은 해당 날짜가 지나면 유휴 상태가 되며, 7일 후 자동 중지됩니다. 종료 날짜가 없는 메시징은 11개월간 활동이 없으면 유휴 상태가 되고, 1년 후 자동 중지됩니다.

## 유휴 Campaigns {#idle-campaigns}

Braze는 다음 기준 중 하나라도 충족하는 유휴 Campaigns를 중지합니다.

- 예약된 일회성 전송이 전송 날짜를 7일 초과한 경우
- 종료 날짜가 있는 예약 또는 액션 기반 Campaign이 종료 날짜를 7일 초과한 경우
- 종료 날짜가 없는 Campaign이 1년 동안 메시지를 전송하거나, 사용자를 대조군에 등록하거나, 편집되지 않은 경우

종료 날짜가 없는 Campaigns의 경우 전송, 대조군 등록 또는 편집이 발생하면 1년 카운트다운이 초기화됩니다. Braze가 Campaigns를 중지하면 대시보드 및 이메일을 통해 회사 사용자에게 알립니다.

Braze는 기본 중지 날짜와 마지막 전환 기한 후 1일 중 더 늦은 시점에 Campaigns를 중지합니다. 우승 배리언트 또는 개인화된 배리언트의 전송은 예약 전송으로 처리되며, Braze는 해당 배리언트가 전송된 후 7일 뒤에 중지합니다. Campaigns는 매일 UTC 오전 4시에 중지됩니다.

Content Cards는 만료 기한까지 중지되지 않으며, 유휴 Campaign 중지 기준과 전환 기한 규칙도 함께 적용됩니다. 자세한 내용은 [Content Cards 중지는 어떻게 작동하나요?](#how-does-stopping-content-cards-work)를 참조하세요.

유휴 Campaign을 활성 상태로 유지하려면 아래 표를 참조하세요. 유휴 상태와 자동 중지는 서로 다른 기간을 사용합니다. 종료 날짜가 없는 Campaign은 11개월간 활동이 없으면 유휴 상태가 되며, Braze는 1년 후 자동으로 중지합니다.

| 유휴 상태 이유 | Campaign을 활성 상태로 만드는 방법 |
|---|---|
| 예약된 일회성 전송이 전송 날짜를 초과함 | 향후 전송을 예약합니다 |
| 종료 날짜가 있는 예약 또는 액션 기반 Campaign의 종료 날짜가 지남 | 종료 날짜를 연장합니다 |
| 종료 날짜가 없는 Campaign이 11개월간 메시지를 전송하거나, 사용자를 대조군에 등록하거나, 편집되지 않음 | 메시지를 전송하거나 Campaign을 편집합니다 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="유휴 Campaign을 활성 상태로 유지하는 방법" }

기능 플래그 Campaigns 및 기능 플래그 실험은 유휴 상태가 되지 않으며 자동 중지되지 않습니다.

### 인앱 메시지 Campaigns {#in-app-message-campaigns}

액션 기반 인앱 메시지 Campaigns는 30일 동안 전송, 대조군 등록 또는 편집이 없으면 유휴 상태가 됩니다. 유휴 인앱 메시지 Campaign은 설정에 따라 계속 전달됩니다. 워크스페이스에 따라 Braze는 이를 [템플릿 인앱 메시지]({{site.baseurl}}/user_guide/channels/in_app_messages/faq#what-are-templated-in-app-messages)로 전달할 수 있습니다.

전송, 대조군 등록 또는 편집이 발생하면 Campaign이 활성 상태로 돌아오고 30일 기간이 초기화됩니다. 자동 중지는 30일 유휴 기간이 아닌 [유휴 Campaigns](#idle-campaigns)의 7일 및 1년 규칙을 따릅니다.

## 유휴 Canvases {#idle-canvases}

Braze는 다음 기준 중 하나라도 충족하는 유휴 Canvases를 중지합니다.

- 예약된 일회성 전송이 전송 날짜와 [최대 기간]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas#maximum-duration)을 7일 이상 초과한 경우
- 종료 날짜가 있는 예약 또는 액션 기반 Canvas가 종료 날짜와 최대 기간을 7일 이상 초과한 경우
- 종료 날짜가 없는 Canvas가 12개월에 최대 기간을 더한 시간 동안 사용자를 진입시키거나 편집되지 않은 경우

종료 날짜가 없는 Canvases의 경우 사용자 진입 또는 편집이 발생하면 1년 카운트다운이 초기화됩니다. Braze가 Canvases를 중지하면 대시보드 및 이메일을 통해 회사 사용자에게 알립니다.

Canvas의 최대 기간은 사용자가 해당 Canvas를 완료하는 데 걸릴 수 있는 가장 긴 시간입니다. 이 기간에는 Content Cards 및 인앱 메시지의 만료가 포함됩니다.

유휴 Canvas를 활성 상태로 유지하려면 아래 표를 참조하세요. 유휴 상태와 자동 중지는 서로 다른 기간을 사용합니다. 종료 날짜가 없는 Canvas는 11개월에 최대 기간을 더한 시간 동안 활동이 없으면 유휴 상태가 되며, Braze는 12개월에 최대 기간을 더한 시간 후 자동으로 중지합니다.

| 유휴 상태 이유 | Canvas를 활성 상태로 만드는 방법 |
|---|---|
| 예약된 일회성 전송이 전송 날짜와 최대 기간을 초과함 | 향후 전송을 예약합니다 |
| 종료 날짜 및 최대 기간이 있는 예약 또는 액션 기반 Canvas의 종료 날짜가 지남 | 종료 날짜를 연장합니다 |
| 종료 날짜가 없는 Canvas가 11개월에 최대 기간을 더한 시간 동안 사용자를 진입시키거나 편집되지 않음 | 사용자를 진입시키거나 Canvas를 편집합니다 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="유휴 Canvas를 활성 상태로 유지하는 방법" }

기능 플래그 단계가 포함된 Canvases는 유휴 상태가 되지 않으며 자동 중지되지 않습니다.

중지된 Campaigns 및 Canvases의 메시징 상호작용 데이터에 대해서는 [메시징 상호작용 데이터 가용성에 대하여]({{site.baseurl}}/messaging_interaction_data)를 참조하세요.

## 자주 묻는 질문 {#frequently-asked-questions}

### 어떤 Campaigns 또는 Canvases에 적용되나요? {#what-campaigns-or-canvases-does-this-apply-to}

이 문서의 기준을 이미 충족한 Campaigns 및 Canvases와 나중에 기준을 충족하게 되는 Campaigns 및 Canvases 모두에 적용됩니다.

### Campaign 또는 Canvas가 유휴 상태인지 어떻게 알 수 있나요? {#how-do-i-know-if-a-campaign-or-canvas-is-idle}

유휴 Campaigns 및 Canvases를 찾으려면 **Campaigns** 또는 **Canvas** 페이지로 이동하여 **유휴**로 필터링하세요. Braze가 Campaign 또는 Canvas를 중지하는 날짜가 목록에 열로 표시됩니다.

![Campaigns 페이지의 "유휴" 필터.]({% image_buster /assets/img/idle_filter.png %}){: style="max-width:80%;"}

### 유휴 Campaign 또는 Canvas를 업데이트하면 어떻게 되나요? {#what-happens-if-an-idle-campaign-or-canvas-is-updated}

메시지를 전송하지 않은 Campaign 또는 사용자를 진입시키지 않은 Canvas를 업데이트하면 카운트다운이 초기화됩니다.

### 1년 동안 메시지를 전송하지 않은 Campaigns(또는 1년 동안 사용자를 진입시키지 않은 Canvases)에 종료 날짜가 미래에 설정되어 있으면 어떻게 되나요? {#what-happens-to-campaigns-that-havent-sent-a-message-in-one-year-or-canvases-that-havent-entered-users-in-one-year-but-have-an-end-date-in-the-future}

Braze는 종료 날짜 7일 후 UTC 오전 4시에 해당 Campaigns 및 Canvases를 중지합니다.

### Campaigns가 자동 중지되는 것을 방지할 수 있나요? {#can-i-prevent-campaigns-from-auto-stopping}

아니요. 자동 중지는 필요한 Campaigns만 활성 상태로 유지하여 대시보드를 깔끔하게 하고 성능을 향상시킵니다. 자동 중지된 모든 Campaigns의 목록이 필요하면 [지원 티켓을 제출]({{site.baseurl}}/user_guide/administer/personal/braze_support)하세요.

### 중지된 Campaigns 및 Canvases에 대한 이메일 알림은 누가 받나요? {#who-receives-email-notifications-about-stopped-campaigns-and-canvases}

기본적으로 관리자 권한이 있는 모든 사용자가 자동 중지된 Campaigns 및 Canvases에 대한 이메일 알림을 수신하도록 설정되어 있습니다. Campaign 또는 Canvas의 생성자는 중지 시 항상 알림을 받습니다. 수신자를 관리하려면 **설정** > **관리자 설정** > **알림 환경설정**으로 이동한 다음 **Campaign 자동 중지** 및 **Canvas 자동 중지**에서 수신자를 추가하거나 제거하세요.

### Content Cards 중지는 어떻게 작동하나요? {#how-does-stopping-content-cards-work}

Campaigns의 Content Cards는 만료 기한과 적절한 버퍼 기간이 지날 때까지 중지되지 않습니다. Braze는 버퍼 기간(일회성 전송, 종료 날짜 또는 종료 날짜 없음)과 만료 기한 중 더 늦은 시점에 중지합니다.

예를 들어, Content Card가 4월 1일에 만료되고, 일회성 전송이며, 전환 기한이 10일인 경우 Braze는 4월 12일에 중지합니다(전환 기한 후 10일에 1일을 더한 시점). Content Card가 4월 1일에 만료되고, API 트리거 방식이며, 3월 15일 이후 메시지를 전송하지 않은 경우 다음 해 3월 15일에 만료됩니다.

Canvases는 Content Cards가 중지된 후, 즉 최대 기간이 경과한 후에만 중지됩니다.

### Canvas에 기능 플래그 실험이 있습니다. 기능 플래그가 설정된 후에도 Canvas가 활성 상태로 유지되나요? {#i-have-a-feature-flag-experiment-in-my-canvas-after-my-feature-flag-is-set-does-the-canvas-remain-active}

네. 기능 플래그 단계가 포함된 Canvases는 자동 중지되지 않으며 유휴 상태가 되지 않습니다. 기능 플래그 Campaigns 및 기능 플래그 실험에도 동일한 예외가 적용됩니다.

### Campaign 목록을 활성으로만 필터링할 때 유휴 Campaigns가 표시되는 이유는 무엇인가요? {#why-do-idle-campaigns-appear-when-i-filter-the-campaign-list-to-active-only}

유휴 Campaigns는 중지될 때까지 활성으로 간주됩니다.

### 푸시 알림을 계속 전송 중인 Campaign도 유휴 상태인가요? {#is-a-campaign-idle-if-its-still-sending-push-notifications}

아니요. Campaign이 더 이상 적극적으로 메시지를 전송하지 않을 때 유휴로 표시됩니다.