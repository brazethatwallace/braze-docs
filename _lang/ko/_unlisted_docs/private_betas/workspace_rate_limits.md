---
article_title: 워크스페이스 사용량 제한
description: "워크스페이스 사용량 제한을 설정하여 회사의 전체 API 사용량 제한이 개별 워크스페이스에 어떻게 분배되는지 제어하고, 단일 통합 또는 팀이 특정 엔드포인트에 너무 많은 요청을 보내는 것을 방지하는 방법을 알아보세요."
permalink: /workspace_rate_limits/
---

# 워크스페이스 사용량 제한 {#workspace-rate-limits}

> 워크스페이스 사용량 제한을 설정하여 회사의 전체 API 사용량 제한이 개별 워크스페이스에 어떻게 분배되는지 제어하고, 단일 통합 또는 팀이 특정 엔드포인트에 너무 많은 요청을 보내는 것을 방지하는 방법을 알아보세요.

## 필수 조건 {#prerequisites}

워크스페이스 사용량 제한은 데이터 포인트가 포함되지 않은 Braze 계약에서만 사용할 수 있습니다. 또한 사용량 제한을 관리하려면 [관리자 권한]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin)이 필요합니다.

## 워크스페이스 사용량 제한 소개 {#about-workspace-rate-limits}

기본적으로 회사 수준의 사용량 제한은 모든 워크스페이스에서 공유됩니다.

워크스페이스 사용량 제한을 사용하면 워크스페이스가 `/users/track` 또는 SDK 데이터와 같은 특정 수집 엔드포인트에 보낼 수 있는 최대 API 요청 수를 설정할 수 있습니다. 또한 워크스페이스 그룹에 사용량 제한을 적용할 수 있으며, 이 경우 해당 그룹의 모든 워크스페이스에서 제한이 공유됩니다.

예를 들어, `/users/track` 엔드포인트의 회사 수준 사용량 제한이 시간당 500,000건의 요청인 경우, 다음과 같이 워크스페이스 사용량 제한을 설정할 수 있습니다:

- _워크스페이스 1_에 시간당 10,000건의 요청 제한 적용
- _워크스페이스 2_와 _워크스페이스 3_에 시간당 200,000건의 공유 요청 제한 적용
- _워크스페이스 4_에는 사용량 제한을 적용하지 않으며, 기본 회사 수준 사용량 제한이 사용됨

## 워크스페이스 사용량 제한 관리 {#managing-workspace-rate-limits}

### 제한 할당 {#assigning-a-limit}

하나 이상의 워크스페이스에 새 사용량 제한을 할당하려면 **설정** > **관리자 설정** > **워크스페이스 사용량 제한**으로 이동한 다음 **사용량 제한 할당**을 선택합니다.

![Braze 대시보드의 워크스페이스 사용량 제한 페이지.]({% image_buster /assets/unlisted_docs/img/workspace_rate_limits/settings.png %}){: style="max-width:85%;"}

다음으로 엔드포인트와 하나 이상의 워크스페이스를 선택한 후 사용량 제한을 입력합니다. 제한은 1,000보다 크고 회사 수준 사용량 제한을 초과하지 않는 정수여야 합니다.

완료되면 **사용량 제한 업데이트**를 선택합니다.

![엔드포인트, 워크스페이스, 사용량 제한을 선택할 수 있는 옵션이 있는 사용량 제한 팝업 창.]({% image_buster /assets/unlisted_docs/img/workspace_rate_limits/update_rate_limit.png %}){: style="max-width:45%;"}

{% alert note %}
둘 이상의 워크스페이스를 선택하면 해당 워크스페이스 그룹에서 사용량 제한이 공유됩니다.
{% endalert %}

### 제한 편집 {#editing-a-limit}

기존 워크스페이스 사용량 제한을 편집하려면 **설정** > **관리자 설정** > **워크스페이스 사용량 제한**으로 이동한 다음 <i class="fas fa-ellipsis-vertical"></i> 세로 줄임표를 선택하고 **편집**을 선택합니다. 새 사용량 제한은 몇 분 내에 적용될 수 있습니다.

### 제한 초기화 {#resetting-a-limit}

기존 사용량 제한을 회사 수준 사용량 제한으로 되돌리려면 **설정** > **관리자 설정** > **워크스페이스 사용량 제한**으로 이동한 다음 <i class="fas fa-ellipsis-vertical"></i> 세로 줄임표를 선택하고 **초기화**를 선택합니다.

## 사용량 모니터링 {#monitoring-usage}

### 응답 헤더 {#response-headers}

기본적으로 모든 수집 응답에는 안정적인 회사 수준 사용량 제한을 반영하는 다음 헤더가 포함됩니다.

사용량 제한을 효과적으로 관리하기 위해 통합 로직에서 이러한 헤더를 사용하는 것을 권장합니다. 예를 들어, 제한에 가까워지면 요청량을 줄이고 `Retry-After` 헤더를 사용하여 재시도 시점을 결정할 수 있습니다.

| 헤더 이름 | 설명 |
| ----- | ----- |
| `X-RateLimit-Limit` | 현재 사용량 제한 기간에 허용되는 최대 요청 수입니다. |
| `X-RateLimit-Remaining` | 현재 기간에 남은 요청 수입니다. |
| `X-RateLimit-Reset` | 현재 사용량 제한 기간이 초기화되는 시점입니다(UTC 에포크 초). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### 오류 코드 {#error-codes}

워크스페이스 사용량 제한에 도달하면 요청은 `429` 응답 코드를 반환하며, 헤더에 `Retry-After` 값이 포함됩니다. 이 값은 사용량 제한이 초기화될 때까지의 초 수를 나타냅니다.

`Retry-After` 값은 워크스페이스 사용량 제한이 초기화되는 다음 정시까지의 초 수를 반영합니다.

### API 사용량 대시보드 {#api-usage-dashboard}

워크스페이스 전반의 요청량, 응답 코드, 수집 동작을 모니터링하려면 [API 사용량 대시보드]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_dashboard/)를 사용할 수도 있습니다.

대시보드에서 `429 Workspace Rate Limited` 또는 `429 Company Rate Limited`로 필터링하여 요청이 회사 수준 사용량 제한에 의해 제한되었는지 워크스페이스 사용량 제한에 의해 제한되었는지 빠르게 확인할 수 있습니다.