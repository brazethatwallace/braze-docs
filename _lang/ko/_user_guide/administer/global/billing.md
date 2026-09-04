---
nav_title: 청구
article_title: 청구
alias: /subscription_and_usage/
page_order: 5
page_type: reference
description: "이 참조 문서에서는 데이터 소비를 모니터링하고 확인할 수 있는 청구 페이지를 다룹니다."
tool: Dashboard
search_rank: 5
---

# 청구 {#billing}

> **청구** 페이지를 사용하여 워크스페이스, 앱 및 이벤트 소스 전반의 데이터 소비를 모니터링하고 확인하는 방법을 알아보세요. 이 문서에서는 페이지의 다양한 섹션과 각 섹션에서 제공하는 정보를 다룹니다.

**청구** 페이지로 이동하려면 **설정** > **청구**로 이동하세요.

**청구** 페이지에는 다음 탭이 포함되어 있습니다:

- [구독 및 사용량](#subscriptions-and-usage)
- [앱별 최다 사용 이벤트 및 속성](#most-used-events-and-attributes-by-app)
- [총 데이터 포인트 사용량](#total-data-points-dashboard)

## 구독 및 사용량 {#subscriptions-and-usage}

**구독 및 사용량** 탭에는 사용량 그래프와 계약 세부 정보가 포함되어 있습니다. 이 페이지의 데이터는 매일 미국 동부 시간(ET) 오후 10:00에 업데이트됩니다. 실시간 활동을 반영하지는 않습니다.

### 사용량 그래프 {#usage-graphs}

여기에서 워크스페이스에 적용되는 사용량 그래프를 확인할 수 있습니다. 구매한 제품에 따라 대시보드에 표시되는 사용량 측정기준이 다를 수 있습니다.

![월간 고유 방문자를 보여주는 사용량 그래프]({% image_buster /assets/img/subscription_and_billing4.png %}){: style="max-width:90%;"}

이 그래프에서는 월간 활성 사용자, 월간 고유 방문자, 이메일 발송 수를 확인할 수 있습니다. 이러한 사용량 그래프는 사용량 예산을 계획하고 어떤 워크스페이스가 전체 사용량에 기여하는지 더 깊이 이해하는 데 특히 유용합니다.

### 계약 세부 정보 {#contract-details}

계약 세부 정보에는 Braze와의 현재 계약 시작일과 종료일이 나열됩니다.

#### 고려 사항 {#considerations}

계약에서 월간 고유 방문자(MUV)를 사용하다가 월간 활성 사용자(MAU)만 사용하는 계약으로 변경하는 경우, 기존 데이터는 여전히 MUV 그래프에 표시되고 새로운 데이터는 MAU 그래프에만 표시됩니다. 예를 들어, 계약이 10월에 종료되는 경우 MUV 그래프에는 9월 말까지의 데이터가 표시됩니다.

## 앱별 최다 사용 이벤트 및 속성 {#most-used-events-and-attributes-by-app}

**앱별 최다 사용 이벤트 및 속성** 아래에서 속성 및 커스텀 이벤트 데이터 포인트 사용량의 주요 요인을 확인할 수 있습니다.

![앱별 최다 사용 이벤트 및 속성]({% image_buster /assets/img/most_used_events_attributes_time.png %})

각 앱에서 **세부 내역 보기**를 선택하면 선택한 기간 동안의 각 커스텀 속성, 프로필 속성, 커스텀 이벤트의 예상 횟수와 해당 앱의 속성 및 이벤트 업데이트에서 해당 속성 또는 이벤트가 차지하는 비율을 확인할 수 있습니다.

![앱별 최다 사용 이벤트 및 속성 세부 내역 탭]({% image_buster /assets/img/most_used_events_attributes_2.png %}){: style="max-width:60%"}

이와 같은 데이터 세부 내역은 어떤 특정 데이터 포인트가 할당량의 큰 비율을 차지하고 있는지 파악하는 데 도움이 됩니다. 의도하지 않거나 불필요한 방식으로 데이터 포인트를 사용하고 있지 않은지 수시로 모니터링하는 것을 권장합니다. 고객 성공 매니저가 현재 플랜을 최대한 활용할 수 있도록 안내하거나 더 유연한 옵션을 제공해 드릴 수 있습니다.

## 총 데이터 포인트 대시보드 {#total-data-points-dashboard}

**총 데이터 포인트 사용량** 탭에서는 데이터 포인트 사용량을 상세하게 확인할 수 있습니다. 이 섹션의 모든 데이터를 주 단위 또는 월 단위로 집계하여 볼 수 있습니다.

{% alert note %}
데이터 포인트 정보는 24시간마다 캐시됩니다.
{% endalert %}

관리자인데 **총 데이터 포인트 사용량** 탭을 볼 수 없는 경우, 브라우저가 Braze 대시보드 도메인에 대해 서드파티 쿠키를 허용하고 있는지, 그리고 시크릿 모드가 아닌지 확인하세요.

![주 단위로 데이터 포인트 사용량 필터링]({% image_buster /assets/img/subscription_and_billing2.png %})

### 계약 세부 정보

여기에서 현재 Braze 계약의 시작 및 종료 시기, 할당된 데이터 포인트, 현재 계약 기간 동안 사용된 전체 데이터 포인트의 합계를 확인할 수 있습니다.

이 섹션의 필드는 다음과 같이 정의됩니다:

- **계약 유형:** 청구 기간 구조로, 연간 또는 다년 계약입니다.
- **계약 시작 및 종료일:** 전체 계약의 시작일과 종료일입니다.
- **할당된 데이터 포인트:** 청구 기간당 계약에서 할당된 데이터 포인트 수량입니다.
- **계약 데이터 포인트 사용량:** 계약 기간 동안 기록된 전체 데이터 포인트의 누적 합계이며, 다음 청구 기간에 초기화되지 않습니다.

### 회사 청구 데이터 {#company-billing-data}

#### 앱 수준 총 데이터 포인트 사용량 {#app-level-total-data-point-usage}

이 그래프는 앱별 데이터 포인트 사용량을 보여줍니다.

![앱 수준 총 데이터 포인트 사용량은 각 앱의 데이터 포인트 사용량을 표시합니다.]({% image_buster /assets/img/app_level_total.png %})

합계 중 하나를 선택하면 각 워크스페이스의 주간 데이터 포인트 합계를 보여주는 **시간별 데이터 포인트 사용량** 테이블을 확인할 수 있습니다. **앱 이름** 열이 비어 있는 행은 앱과 연결되지 않은 데이터 포인트를 나타냅니다(예: `app_id`를 지정하지 않은 요청에서 사용된 데이터 포인트).

![시간별 데이터 포인트 사용량은 두 개의 워크스페이스에 대한 총 주간 데이터 포인트를 표시합니다.]({% image_buster /assets/img/data_point_usage_time.png %})

#### 워크스페이스 데이터 포인트 사용량 {#workspace-data-point-usage}

이 그래프를 통해 워크스페이스별 회사의 총 데이터 포인트 사용량을 평가할 수 있습니다. 각 워크스페이스가 회사의 데이터 포인트 사용량에 어떻게 기여하고 있는지 파악할 수 있습니다.

![두 개의 워크스페이스에 대한 워크스페이스 데이터 포인트 사용량 그래프]({% image_buster /assets/img/appgroup_datapoint_usage.png %}){: style="max-width:90%;"}

#### 이벤트 소스별 청구 주기 데이터 포인트 사용량 {#billing-cycle-data-point-usage-by-event-source}

이 그래프를 통해 다양한 API 속성, 커스텀 이벤트, 세션 등 여러 이벤트 소스에 걸쳐 데이터 포인트 사용량이 어떻게 분포되어 있는지 확인할 수 있습니다.

![이벤트 소스별 청구 주기 데이터 포인트 사용량은 여러 이벤트 소스 간의 데이터 포인트 할당을 표시합니다.]({% image_buster /assets/img/event_source_stats.png %})

#### 시간별 데이터 포인트 사용량 {#data-point-usage-over-time}

이 그래프를 통해 할당된 데이터 포인트 대비 총 데이터 포인트 사용량을 빠르게 확인할 수 있습니다.

![시간별 데이터 포인트 사용량은 현재 청구 주기 할당 데이터 포인트와 누적 합계를 비교합니다.]({% image_buster /assets/img/company_data_point_usage_time.png %}){: style="max-width:90%;"}

## 다음 단계 {#next-steps}

{% article_tiles %}
- name: 알림 환경설정
  link: /docs/user_guide/administer/global/admin_settings/notification_preferences
- name: 크레딧 사용량 대시보드
  link: /docs/credits_usage_dashboard
{% endarticle_tiles %}