---
article_title: 워크스페이스 사용량 제한
description: "워크스페이스 사용량 제한을 설정하여 회사의 전체 API 사용량 제한이 개별 워크스페이스에 어떻게 분배되는지 제어하고, 단일 통합 또는 팀이 특정 엔드포인트에 너무 많은 요청을 보내는 것을 방지하는 방법을 알아보세요."
permalink: /workspace_rate_limits/
---

# 워크스페이스 사용량 제한 {#workspace-rate-limits}

> 워크스페이스 사용량 제한을 설정하여 회사의 전체 API 사용량 제한이 개별 워크스페이스에 어떻게 분배되는지 제어하고, 단일 통합 또는 팀이 특정 엔드포인트에 너무 많은 요청을 보내는 것을 방지하는 방법을 알아보세요.

## 전제 조건 {#prerequisites}

워크스페이스 사용량 제한은 데이터 포인트가 없는 Braze 계약에서만 사용할 수 있습니다. 또한 사용량 제한을 관리하려면 [관리자 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)이 필요합니다.

## 워크스페이스 사용량 제한 정보 {#about-workspace-rate-limits}

기본적으로 회사 수준의 사용량 제한은 모든 워크스페이스에서 공유됩니다.

워크스페이스 사용량 제한을 사용하면 워크스페이스가 `/users/track` 또는 SDK 데이터와 같은 특정 수집 엔드포인트에 보낼 수 있는 최대 API 요청 수를 설정할 수 있습니다. 또한 워크스페이스 그룹에 사용량 제한을 적용할 수도 있으며, 이 경우 해당 그룹 내 모든 워크스페이스가 제한을 공유하게 됩니다.

예를 들어, `/users/track` 엔드포인트의 회사 수준 사용량 제한이 시간당 500,000건의 요청인 경우 다음과 같은 워크스페이스 사용량 제한을 설정할 수 있습니다.

- _Workspace 1_에 시간당 10,000건의 요청 사용량 제한 적용
- _Workspace 2_와 _Workspace 3_에 시간당 200,000건의 공유 사용량 제한 적용
- _Workspace 4_에는 사용량 제한을 적용하지 않음 — 이 경우 기본 회사 수준 사용량 제한이 사용됩니다

## 워크스페이스 사용량 제한 관리 {#managing-workspace-rate-limits}

### 제한 할당 {#assigning-a-limit}

하나 이상의 워크스페이스에 새로운 사용량 제한을 할당하려면 **설정** > **관리자 설정** > **워크스페이스 사용량 제한**으로 이동한 다음 **사용량 제한 할당**을 선택합니다.

![Braze 대시보드의 '워크스페이스 사용량 제한' 페이지.]({% image_buster /assets/unlisted_docs/img/workspace_rate_limits/settings.png %}){: style="max-width:85%;"}

다음으로, 엔드포인트와 하나 이상의 워크스페이스를 선택한 후 사용량 제한을 입력합니다. 제한은 1,000보다 큰 정수이어야 하며, 회사 수준의 사용량 제한을 초과할 수 없습니다.

완료되면 **사용량 제한 업데이트**를 선택합니다.

![엔드포인트, 워크스페이스 및 사용량 제한을 선택할 수 있는 '사용량 제한' 팝업 창.]({% image_buster /assets/unlisted_docs/img/workspace_rate_limits/update_rate_limit.png %}){: style="max-width:45%;"}

{% alert note %}
워크스페이스를 두 개 이상 선택하면 해당 워크스페이스 그룹 전체에서 사용량 제한이 공유됩니다.
{% endalert %}

### 제한 편집 {#editing-a-limit}

기존 워크스페이스 사용량 제한을 편집하려면 **설정** > **관리자 설정** > **워크스페이스 사용량 제한**으로 이동한 다음 <i class="fas fa-ellipsis-vertical" aria-label="더보기 메뉴 열기"></i> 세로 줄임표를 선택하고 **편집**을 선택합니다. 새로운 사용량 제한은 몇 분 내에 적용될 수 있습니다.

### 제한 초기화 {#resetting-a-limit}

기존 사용량 제한을 회사 수준의 사용량 제한으로 되돌리려면 **설정** > **관리자 설정** > **워크스페이스 사용량 제한**으로 이동한 다음 <i class="fas fa-ellipsis-vertical" aria-label="더보기 메뉴 열기"></i> 세로 줄임표를 선택하고 **초기화**를 선택합니다.

## 사용량 모니터링 {#monitoring-usage}

### 응답 헤더 {#response-headers}

기본적으로 모든 수집 응답에는 다음 헤더가 포함되며, 이는 회사 수준의 고정 사용량 제한을 반영합니다.

통합 로직에서 이러한 헤더를 사용하여 사용량 제한을 효과적으로 관리하는 것을 권장합니다. 예를 들어, 이러한 제한에 근접할 때 요청량을 줄이고, `Retry-After` 헤더를 사용하여 재시도 시점을 결정할 수 있습니다.

| 헤더 이름 | 설명 |
| ----- | ----- |
| `X-RateLimit-Limit` | 현재 사용량 제한 기간에 허용되는 최대 요청 수입니다. |
| `X-RateLimit-Remaining` | 현재 기간에 남아 있는 요청 수입니다. |
| `X-RateLimit-Reset` | 현재 사용량 제한 기간이 재설정되는 시점입니다(UTC 에포크 초). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### 오류 코드 {#error-codes}

워크스페이스 사용량 제한에 도달하면 요청은 `429` 응답 코드를 반환하며, 헤더에 `Retry-After` 값이 포함됩니다. 이 값은 사용량 제한이 재설정될 때까지 남은 초 수를 나타냅니다.

`Retry-After` 값은 워크스페이스 사용량 제한이 재설정되는 다음 정시까지 남은 초 수를 나타냅니다.

### API 사용량 대시보드 {#api-usage-dashboard}

워크스페이스 전반의 요청량, 응답 코드 및 수집 동작을 모니터링하려면 [API 사용량 대시보드]({{site.baseurl}}/user_guide/analytics/dashboards/api_usage)를 사용할 수도 있습니다.

대시보드에서 `429 Workspace Rate Limited` 또는 `429 Company Rate Limited`로 필터링하여 요청이 회사 수준 사용량 제한에 의해 제한되었는지 또는 워크스페이스 사용량 제한에 의해 제한되었는지 빠르게 식별할 수 있습니다.