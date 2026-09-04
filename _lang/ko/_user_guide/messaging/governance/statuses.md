---
nav_title: 상태
article_title: 상태
page_order: 6
description: "Campaigns 및 Canvases의 상태와 대시보드에서 이를 사용하는 방법에 대해 알아보세요."
tool:
    - Campaigns
    - Canvas
---

# Campaign 및 Canvas 상태 {#campaign-and-canvas-statuses}

> Campaigns 및 Canvases의 상태와 대시보드에서 이를 사용하는 방법에 대해 알아보세요.

## 상태별 필터링 {#filtering-by-status}

Campaign 또는 Canvas를 상태별로 필터링하려면 **All Statuses**를 선택한 다음 원하는 상태를 선택하세요.

![Braze 대시보드의 'All Statuses' 드롭다운.]({% image_buster /assets/img/messaging_fundamentals/filter-by-status.png %}){: style="max-width:70%;"}

## 상태 변경하기 {#changing-the-status}

Campaign 또는 Canvas의 상태를 변경하려면 <i class="fas fa-ellipsis-vertical"></i> 메뉴를 선택한 다음 상태를 선택합니다.

![Braze 대시보드의 Canvases 목록에서 하나의 Canvas에 대해 메뉴가 열려 있는 모습.]({% image_buster /assets/img/messaging_fundamentals/change-status.png %})

## 사용 가능한 상태 {#available-statuses}

Campaign과 Canvases에 사용할 수 있는 상태는 다음과 같습니다.

| 상태 | 설명 |
| --- | --- |
| 활성 | 활성 Campaign과 Canvases는 현재 발송 중인 상태입니다. 기본적으로 각 페이지에서 활성 Campaign과 Canvases를 확인할 수 있습니다. |
| 초안 | Campaign과 Canvases의 초안은 저장되었지만 아직 실행되지 않은 상태입니다. 편집을 계속하고 발송을 시작하려면 Braze 대시보드에서 **메시징**으로 이동한 후 **Canvas** 또는 **Campaigns**를 선택하여 초안을 선택할 수 있습니다. |
| 보관됨 | 보관된 Campaign과 Canvases는 더 이상 발송되지 않는 메시지입니다. 이러한 Campaign과 Canvases는 [**홈**]({{site.baseurl}}/user_guide/analytics/dashboards/home) 및 [**매출**]({{site.baseurl}}/user_guide/analytics/reports/revenue_report) 페이지의 통계 그래프에서도 제거됩니다. |
| 중지됨 | 중지된 Campaign과 Canvases는 일시 중지된 상태이지만 여전히 편집할 수 있습니다. Canvas를 재개하려면 Canvas 빌더의 **요약** 단계로 이동하여 **Canvas 재개**를 선택합니다. Campaign의 경우 <i class="fas fa-ellipsis-vertical" aria-label="더 보기 메뉴"></i> 메뉴를 선택한 다음 **재개**를 선택합니다. 자세한 내용은 [중지된 Canvas 동작](#stopped-canvas-behavior)을 참조하세요. |
| 유휴 | Campaign 또는 Canvas가 더 이상 메시지를 발송하지 않으면 Braze는 Campaign과 Canvases 목록을 정렬하고 관리하는 데 도움이 되도록 유휴 상태를 할당합니다. 어떤 Campaign 또는 Canvases가 자동으로 중지되는지와 관련 중지 날짜를 확인할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용 가능한 상태" }

### 중지된 Canvas 동작 {#stopped-canvas-behavior}

Canvas가 중지되면 다음과 같은 상황이 발생합니다.

- **예약된 메시지:** Canvas에서 사용자의 위치에 관계없이 예약된 메시지는 발송되지 않습니다. 여기에는 사용량 제한조치로 인해 대기줄에 추가된 사용자도 포함됩니다.
- **이메일 발송:** 이메일 서비스 공급자(ESP)가 기존 요청을 계속 처리할 수 있으므로 이메일 발송이 즉시 중단되지 않을 수 있습니다.
- **지연 단계:** [지연 단계]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/delay_step)에 있는 사용자는 정상적으로 해당 단계에 머물지만, 설정된 기간이 종료되면 Canvas에서 퇴장합니다.
- **초안 변경 사항:** Canvas가 중지되면 Canvas에 대한 모든 초안 변경 사항이 삭제됩니다.

#### Canvas를 재개하는 경우 {#when-you-resume-a-canvas}

Canvas를 재개하려면 Canvas 빌더의 **요약** 단계로 이동하여 **Canvas 재개**를 선택합니다. Canvas를 재개하면 사용자는 중단된 지점부터 여정을 계속합니다.

- 지연 단계의 사용자: Canvas가 중지되었을 때 지연 단계에서 대기 중이던 사용자는 남은 지연 기간 동안 계속 대기합니다. 예를 들어, Canvas가 3일 동안 중지되었을 때 사용자가 24시간 지연의 2시간 경과 시점에 있었다면, Canvas가 재개된 후 22시간을 더 대기한 후 다음 단계로 진행합니다.
- 메시지 대기 중인 사용자: Canvas가 중지되었을 때 보류 중이던 예약 메시지는 Canvas를 재개할 때 예약된 대로 발송됩니다. 단, 예약된 시간이 이미 지나지 않은 경우에 한합니다.
- 퇴장한 사용자: 중지 기간 동안 Canvas에서 퇴장한 사용자(예: 지연 단계에 있다가 지연이 종료된 사용자)는 Canvas를 재개해도 다시 진입하지 않습니다.

#### 현지 시간대 동작 {#local-time-zone-behavior}

Canvas가 **사용자를 현지 시간대에 맞춰 이 Canvas에 진입시키기**로 설정된 경우, 중지 및 재개 시 다음 사항을 고려하세요.

- 진입 기간: Canvas를 재개하면 사용자는 원래 설정된 대로 현지 시간대에 따라 진입합니다. Braze는 각 사용자의 시간대에 따라 진입 자격을 계속 평가합니다.
- 놓친 진입 기간: 특정 시간대의 사용자에 대해 예약된 진입 기간 동안 Canvas가 중지된 경우, Canvas가 재개되어도 해당 사용자는 소급하여 진입하지 않습니다. 진입 평가는 앞으로의 시점부터 재개됩니다.

#### 일반적인 시나리오 {#common-scenarios}

**시나리오 1: 메시지 내용 오류**
Canvas를 실행했지만 메시지 중 하나에서 오타를 발견한 경우입니다. Canvas를 중지하고 초안 모드에서 메시지를 수정한 다음 재개합니다. 아직 메시지를 받지 않은 사용자는 수정된 버전을 받게 됩니다. 이미 메시지를 받은 사용자는 다시 받지 않습니다.

**시나리오 2: 타겟팅 문제**
Canvas가 잘못된 Segment를 타겟팅하고 있다는 것을 알게 된 경우입니다. 더 많은 사용자가 진입하는 것을 방지하기 위해 즉시 Canvas를 중지합니다. 현재 지연 단계에 있는 사용자는 지연 기간이 종료되면 퇴장합니다. 그런 다음 올바른 타겟팅으로 새 Canvas를 만들 수 있습니다.

**시나리오 3: 장기 지연 시나리오**
7일 지연 단계가 있는 Canvas가 있습니다. 3일째에 Canvas를 중지합니다. 지연 단계에 있던 사용자는 계속 대기하지만, Canvas가 여전히 중지된 상태에서 지연 기간이 종료되면 Canvas에서 퇴장합니다. 지연이 종료되기 전에 Canvas를 재개하면 사용자는 여정을 계속 진행합니다.

## 모범 사례 {#best-practices}

### 상태별로 메시지 모니터링하기 {#monitor-your-messages-by-status}

상태별로 메시지를 모니터링하여 성능 세부 정보를 검토할 수 있습니다. 예를 들어, 활성 상태인 Campaigns가 여러 개 있는 경우 각 Campaign의 인게이지먼트 측정기준을 평가하고 필요에 따라 조정할 수 있습니다. 반대로 중지된 Canvases가 몇 개 있다면, 메시징을 재개할지 아니면 완전히 보관할지 검토할 수 있습니다.

{% alert tip %}
정리하는 더 많은 방법을 찾고 계신가요? [팀]({{site.baseurl}}/user_guide/administer/global/user_management/teams)과 [태그]({{site.baseurl}}/user_guide/messaging/governance/tags)를 추가하여 한눈에 더 많은 맥락을 파악해 보세요.
{% endalert %}

### 활성 메시지 감사하기 {#audit-your-active-messages}

활성 상태인 Campaigns와 Canvases를 정기적으로 감사하면 관련성과 성능을 평가하고, 오래된 Campaigns와 Canvases를 제거하거나 업데이트하여 메시징을 최신 상태로 유지할 수 있습니다.