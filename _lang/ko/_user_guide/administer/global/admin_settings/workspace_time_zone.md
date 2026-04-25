---
nav_title: 작업 공간 시간대
article_title: 메시지 전송을 위한 작업 공간 시간대
alias: /workspace_time_zones/
page_order: 3
description: "이 참조 문서에서는 다양한 지리적 위치에서 운영되는 팀을 위한 Campaign 및 Canvas 스케줄 조정을 제공하는 Braze 작업 공간의 다양한 시간대를 구성하는 방법을 다룹니다."
---

# 메시지 전송을 위한 작업 공간 시간대

> 작업 공간 시간대를 통해 관리자는 개별 작업 공간에 대한 특정 시간대를 정의할 수 있습니다. 이로 인해 예약된 Campaigns 및 Canvases(로컬 시간 또는 Intelligent Timing을 사용하지 않는 경우)는 회사의 전체 시간대가 아닌 작업 공간에 지정된 시간대에 따라 전송됩니다.

{% multi_lang_include early_access_beta_alert.md feature='Workspace time zones' %}

기본적으로 새 작업 공간은 회사에 설정된 시간대를 상속받습니다. 관리자는 작업 공간 시간대를 사용하여 하나 이상의 작업 공간에 대해 이 기본값을 재정의할 수 있습니다. 작업 공간 시간대가 설정되면 해당 작업 공간 내의 예약된 Campaigns 및 Canvases는 전송 시간을 위해 해당 새로운 시간대를 참조합니다.

예를 들어, 작업 공간 시간대가 PST로 설정되고 해당 작업 공간 내의 Campaign이 오후 3시 PST에 전송되도록 예약된 경우, 오후 3시 PST에 전달됩니다. 회사의 전체 시간대가 다르더라도(예: EST, 오후 3시 PST는 오후 6시 EST) 이 사실은 변하지 않습니다.

## 작업 공간 시간대 관리

관리자라면 **설정** > **관리자 설정** > **워크스페이스 시간대**로 이동하여 작업 공간 시간대에 접근하고 관리할 수 있습니다.

여기에서 모든 작업 공간의 목록, 설정된 시간대 및 마지막으로 시간대가 편집된 시간을 볼 수 있습니다. 검색창을 사용하여 이름으로 특정 작업 공간을 찾습니다.

!["워크스페이스 시간대" 페이지에는 작업 공간 목록, 해당 시간대 및 마지막으로 시간대가 편집된 시간이 포함되어 있습니다.]({% image_buster /assets/img/workspaces/time_zones/workspace_time_zones_page.png %})

### 시간대 설정

{% alert note %}
시간대 업데이트가 적용되는 데 몇 분 정도 걸릴 수 있습니다.
{% endalert %}

{% tabs %}
{% tab 단일 작업 공간 %}
1. 목록에서 원하는 작업 공간을 찾습니다.
2. 작업 공간 이름 옆에 있는 **편집** 아이콘을 선택합니다.

!["편집" 버튼이 작업 공간 이름 옆에 있습니다.]({% image_buster /assets/img/workspaces/time_zones/single_edit_icon.png %})

{: start="3"}
3. 드롭다운 메뉴에서 해당 작업 공간에 대한 원하는 시간대를 선택합니다.
4. **저장**을 선택합니다.

![GMT 시간대가 선택된 드롭다운 메뉴입니다.]({% image_buster /assets/img/workspaces/time_zones/edit_single_workspace.png %})
{% endtab %}
{% tab 다중 작업 공간 %}

다음 단계를 수행하여 여러 작업 공간에 특정 시간대를 한 번에 적용할 수 있습니다:

1. 업데이트하려는 모든 작업 공간 옆의 체크박스를 선택합니다.
2. **시간대 편집**을 선택합니다.
3. 드롭다운 메뉴에서 선택한 모든 작업 공간에 적용할 시간대를 선택합니다.

![여러 작업 공간이 선택되고 "시간대 편집" 버튼이 있는 "워크스페이스 시간대" 페이지입니다.]({% image_buster /assets/img/workspaces/time_zones/bulk_edit_workspace_time_zone.png %})

{: start="4"}
4. **저장**을 선택합니다.

{% endtab %}
{% endtabs %}

## Campaigns 및 Canvases에 미치는 영향

{% alert important %}
Campaign 스케줄에 대한 혼란을 방지하기 위해 각 작업 공간 내의 관련 팀과 이해관계자에게 시간대 변경 사항을 알려주세요.
{% endalert %}

- **로컬 시간 및 Intelligent Timing Campaign:** 사용자의 로컬 시간 또는 [Intelligent Timing]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/scheduled_delivery/#option-3-intelligent-timing)을 전달에 사용하는 Campaigns 및 Canvases는 이전과 동일하게 작동하며 작업 공간 시간대의 영향을 받지 않습니다.
- **예약된 Campaigns 및 Canvases:** 사용자의 로컬 시간 또는 Intelligent Timing을 전달에 사용하지 않는 예약된 Campaign 또는 Canvas는 이제 작업 공간에서 선택한 시간대를 기준으로 전송됩니다.
- **시간대 변경 전에 예약된 Campaigns:** 작업 공간 시간대를 변경하기 전에 Campaign 또는 Canvas를 예약한 경우, Braze는 원래 전송 시간을 유지하며 다시 예약하지 않습니다. 예를 들어, Campaign이 오후 7시 PST에 전송되도록 설정되어 있고 작업 공간 시간대가 EST로 변경된 경우, Campaign은 여전히 오후 7시 PST(현재 오후 10시 EST에 해당)에 전송됩니다. 시스템은 원래 시간을 계속 참조하지만 새로운 작업 공간 시간대를 통해 해석합니다.

## 날짜 기반 오디언스 필터에 미치는 영향

작업 공간 시간대가 업데이트되면 날짜만 사용하는 오디언스 필터(특정 시간이 제공되지 않는 경우)는 새 시간대의 경계를 기준으로 다시 평가됩니다.

"마지막으로 커스텀 이벤트 X를 수행한 날짜 이후"와 같은 필터의 경우, Braze는 작업 공간 시간대를 사용하여 해당 날짜의 시작과 끝을 결정합니다. 이 설정을 변경하면 해당 특정 날짜의 오후 11시 59분 기준 시점이 이동합니다.

### 예시

작업 공간이 시간대를 동부 표준시(EST)에서 태평양 표준시(PST)로 업데이트합니다.

- **이전 기준 시점:** 오후 11시 59분 EST
- **새 기준 시점:** 오후 11시 59분 PST(다음 날 오전 2시 59분 EST에 해당)

이 변경 후, 2026년 3월 6일 오후 10시 PST(2026년 3월 7일 오전 1시 EST에 해당)에 커스텀 이벤트를 수행한 사용자는 해당 날짜의 PST 캘린더 경계 내에 포함되므로 이제 오디언스에 포함됩니다.

## 보고서 불일치

작업 공간 시간대는 Campaign 전송에 대한 정밀한 제어를 제공하지만, 이 기능이 얼리 액세스 단계에 있는 동안 잠재적인 보고서 불일치에 유의해야 합니다. 특정 시간대가 재정의된 작업 공간의 보고서를 분석할 때 데이터 포인트를 교차 참조하고 시간대를 고려하세요.