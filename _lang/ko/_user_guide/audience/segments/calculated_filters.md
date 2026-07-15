---
nav_title: 계산된 필터
article_title: 계산된 필터
page_order: 5.5
page_type: reference
description: "이 참조 문서에서는 계산된 필터의 작동 방식, SQL 세그먼트 확장과의 비교, 계산된 필터를 생성하고 관리하는 방법을 다룹니다."
tool: Segments
---

# 계산된 필터 {#calculated-filters}

> 계산된 필터를 사용하면 사용자 이력의 장기간에 걸쳐 매우 정밀한 세그먼트를 구축할 수 있습니다. 예를 들어, 계산된 필터를 사용하여 지난 16개월 동안 특정 제품을 구매한 사용자나 서비스에 일정 금액 이상을 지출한 사용자를 타겟팅할 수 있습니다. 이벤트 속성정보를 사용하여 이 오디언스를 더욱 세분화하여 타겟팅을 더 정밀하게 만들 수 있습니다.

{% alert important %}
계산된 필터는 현재 얼리 액세스 중입니다. 얼리 액세스에 참여하고 싶으시면 고객 성공 매니저에게 문의하세요.
{% endalert %}

## 작동 방식 {#how-it-works}

Braze Segments는 동적 사용자 그룹을 생성할 수 있는 강력한 타겟팅 도구를 제공합니다. 대부분의 사용 사례에서는 이것만으로도 오디언스에 효과적으로 도달할 수 있습니다. 계산된 필터는 최대 2년 전의 동작을 분석하거나 복잡한 로직을 적용해야 하는 고급 사용 사례를 위해 설계되었으며, 데이터 보존이나 시스템 성능을 저하시키지 않습니다. 자체 [데이터 웨어하우스]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)의 데이터를 사용하여 오디언스를 더욱 세분화할 수 있습니다.

예를 들어, Braze 기본 세분화는 최근 제품 중 하나를 구매한 사용자를 식별하는 것과 같이 정의한 특정 기준에 맞는 사용자를 찾습니다. 계산된 필터를 사용하면 더 깊이 들어갈 수 있습니다. 예를 들어, 18~24개월 전에 특정 제품의 특정 색상을 최소 두 번 이상 구매한 사용자를 식별할 수 있습니다. 계산된 필터는 향상된 기능이지 필수 요건은 아닙니다. 더 고급 필터나 더 긴 이력 기간이 필요한 경우, 데이터 사용을 최적화하면서 도움이 되는 훌륭한 도구입니다.

## 계산된 필터와 SQL 세그먼트 확장 {#calculated-filters-and-sql-segment-extensions}

[SQL 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)과 계산된 필터는 모두 구매 및 커스텀 이벤트 동작에서 오디언스를 구축하는 데 도움이 되지만, 서로 다른 도구와 데이터 소스를 사용합니다. SQL 세그먼트 확장은 연결된 Snowflake 데이터에 대해 직접 작성하는 SQL을 사용합니다.

| 동작 | 계산된 필터 | SQL 세그먼트 확장 |
|---|---|---|
| 오디언스 정의 방법 | 구매, eCommerce 추천 이벤트, 메시지 상호작용 또는 커스텀 이벤트를 선택하고, 횟수, 기간, 선택적 속성정보 필터를 지정합니다 | 연결된 Snowflake에 대해 SQL을 작성합니다. 템플릿, 증분 새로고침 또는 전체 새로고침을 사용합니다 |
| 로직 실행 위치 | 기준과 새로고침은 Braze에서 계산된 필터로 관리됩니다 | 쿼리는 확장 구성에 따라 웨어하우스 컨텍스트에서 실행됩니다 |
| 필터 목록 페이지 | 하나의 계산된 필터 유형이며, **Segments** 열은 각 필터를 사용하는 세그먼트 수를 표시하고, **처리 중** 및 **처리 실패** 상태는 생성 상태를 반영합니다 | **유형** 열과 확장 유형에 따라 달라지는 필터가 포함됩니다 |
| 일반적인 사용 사례 | 구매 빈도, 총 지출, 커스텀 이벤트 횟수, 선택한 기간에 대한 속성정보 기반 규칙 | 웨어하우스 기반 로직, 테이블 간 조인, 계산된 필터 양식을 넘어서는 이력 기간 또는 집계 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="계산된 필터와 SQL 세그먼트 확장" }

### 계산된 필터를 사용해야 하는 경우 {#when-to-use-calculated-filters}

대시보드에서 안내하는 구매, eCommerce, 메시지 상호작용, 커스텀 이벤트 규칙만으로 충분하고 웨어하우스 테이블에 대한 임의의 SQL이 필요하지 않은 경우 계산된 필터를 사용하세요.

### 다른 세그먼트 확장 유형을 사용해야 하는 경우 {#when-to-use-other-segment-extension-types}

전체 SQL, Snowflake 기반 데이터, 템플릿 또는 대규모 또는 복잡한 웨어하우스 쿼리를 위해 설계된 새로고침 모드가 필요한 경우 [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)을 사용하세요. [클라우드 데이터 수집]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments) 연결의 데이터를 사용하여 데이터 웨어하우스를 직접 쿼리하는 SQL이 필요한 경우 [CDI 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments)을 사용하세요.

### 계산된 필터와 세그먼트 확장을 함께 사용하기 {#use-calculated-filters-and-segment-extensions-together}

하나의 Segment에서 계산된 필터를 SQL 또는 CDI 세그먼트 확장과 함께 참조할 수 있습니다. 예를 들어, 확장에서 정의한 웨어하우스 기반 코호트와 계산된 필터 빌더에서 관리하는 구매 또는 커스텀 이벤트 규칙을 결합할 수 있습니다.

## 계산된 필터 생성하기 {#create-a-calculated-filter}

계산된 필터를 생성하려면 사용자 동작을 기반으로 기준을 정의한 다음, 필터를 저장하고 활성화한 후 Segment에서 사용합니다.

### 1단계: 세부 정보 설정 {#step-1-set-up-details}

1. **오디언스** > **계산된 필터**로 이동합니다.
2. **계산된 필터 생성**을 선택합니다.
3. 타겟팅하려는 사용자를 설명하여 계산된 필터의 이름을 지정합니다. 설명적인 이름을 사용하면 Segment에 추가할 때 필터를 더 쉽게 찾을 수 있습니다.
4. (선택 사항) [태그]({{site.baseurl}}/user_guide/administer/global/workspace_settings/tags)를 추가하여 워크스페이스에서 계산된 필터를 정리합니다.

**반복 오디언스 업데이트 활성화**를 선택하여 반복 스케줄에 따라 필터를 새로고침할 수도 있습니다. 이 설정을 켜지 않으면, 필터를 업데이트하거나 **오디언스 업데이트**를 선택하지 않는 한 계산된 필터가 새로고침되지 않습니다.

### 2단계: 기준 선택 {#step-2-choose-your-criteria}

타겟팅을 위한 구매, eCommerce, 커스텀 또는 메시지 상호작용 이벤트 기준을 선택합니다. 이벤트 유형을 선택한 후, 특정 이벤트, 사용자가 완료해야 하는 횟수(초과, 미만 또는 동일), 기간을 선택합니다.

기간을 선택할 때 상대적 날짜 범위(지난 X일), 시작 날짜, 종료 날짜 또는 정확한 날짜 범위를 지정할 수 있습니다.

![2026년 6월 21일부터 2026년 6월 27일까지의 날짜 범위에서 커스텀 이벤트를 0회 초과 수행한 사용자에 대한 계산된 필터 기준.]({% image_buster /assets/img/segment/calculated_filter_example.png %})

#### 이벤트 속성정보 세분화 {#event-property-segmentation}

타겟팅 정밀도를 높이려면 **속성정보 필터 추가**를 선택합니다. 이를 통해 구매, eCommerce 이벤트 또는 커스텀 이벤트의 속성정보를 기준으로 필터링할 수 있습니다. Braze는 문자열, 숫자, 부울 및 시간 오브젝트를 기반으로 한 이벤트 속성정보 세분화를 지원합니다.

문자열 속성정보의 경우 여러 값을 한 번에 입력할 수 있습니다. 예를 들어, 상태가 골드, 실버 또는 브론즈인 사용자를 타겟팅할 수 있습니다. eCommerce 추천 이벤트의 경우, 속성정보 드롭다운에 해당 이벤트에 사용 가능한 속성정보가 표시됩니다.

{% alert note %}
이벤트 속성정보를 Segment에서 사용하기 위해 계산된 필터가 반드시 필요한 것은 아닙니다. 계산된 필터는 기본 Segment를 생성하는 데 사용되는 이력 기간을 확장할 뿐입니다. 지난 30일간의 이벤트 속성정보를 사용하는 실시간 기본 [Segment]({{site.baseurl}}/user_guide/audience/segments)를 생성할 수 있습니다. 마찬가지로, 이벤트 속성정보를 기반으로 실시간으로 트리거되도록 [메시지를 스케줄]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)할 수 있으며, 계산된 필터가 필요하지 않습니다.
{% endalert %}

### 3단계: 필터 저장 및 활성화 {#step-3-save-and-activate-your-filter}

**저장**을 선택하여 계산된 필터를 저장합니다. 활성화하지 않고 필터를 저장할 수 있지만, Segment를 구축할 때 옵션으로 표시되려면 필터를 활성화해야 합니다.

계산된 필터를 활성화하면, 이를 참조하는 Segment, Campaign 또는 Canvas가 평가될 때 Braze가 실시간으로 평가합니다.

## Segment에서 계산된 필터 사용하기 {#use-a-calculated-filter-in-a-segment}

계산된 필터를 생성하고 활성화한 후, Segment를 구축하거나 Campaign 또는 Canvas의 오디언스를 정의할 때 추가합니다.

1. Segment 빌더에서 필터 목록을 엽니다.
2. **기타 필터**에서 **기존 계산된 필터**를 선택합니다.
3. Segment 정의에 포함할 계산된 필터를 선택합니다.

필터를 추가한 후, 필터 드롭다운 옆의 아이콘을 선택하여 필터의 세부 정보를 확인하고 오디언스에 적용된 기준을 확인합니다.

![세부 정보를 보기 위한 아이콘이 있는 Segment 빌더의 계산된 필터.]({% image_buster /assets/img/segment/view_cf_details.png %}){: style="max-width:70%;"}

Segments 구축에 대한 자세한 내용은 [Segment 생성하기]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)를 참조하세요.

## 계산된 필터 관리하기 {#manage-calculated-filters}

**오디언스** > **계산된 필터**로 이동하여 워크스페이스에서 계산된 필터를 확인, 편집 및 관리합니다.

**계산된 필터** 페이지에는 워크스페이스의 모든 계산된 필터가 나열됩니다. 사용 가능한 제어 기능으로 목록을 좁힐 수 있습니다. 계산된 필터 유형은 하나뿐이므로 유형별 필터링 옵션이 없으며, 테이블에 **유형** 열이 포함되지 않습니다. **Segments** 열을 사용하여 각 계산된 필터를 사용하는 세그먼트 수를 확인합니다.

### 상태 레이블 {#status-labels}

각 계산된 필터는 다음 상태 중 하나를 표시합니다. **처리 중** 및 **처리 실패**는 멤버십 생성이 진행 중이거나 성공적으로 완료되지 않았을 때 표시됩니다.

| 상태 | 설명 |
|---|---|
| 활성 | 필터가 활성화되어 Segments에서 사용할 수 있습니다. |
| 초안 | 필터가 저장되었지만 활성화되지 않았습니다. |
| 아카이브됨 | 필터가 아카이브되었습니다. |
| 처리 중 | Braze가 필터 업데이트를 처리하고 있습니다. |
| 처리 실패 | 가장 최근 처리 시도가 성공적으로 완료되지 않았습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="상태 레이블" }

### 개별 필터 편집 및 관리 {#edit-and-manage-individual-filters}

계산된 필터의 행 메뉴를 열어 편집, 아카이브, 오디언스 새로고침 또는 메시징에서 어떻게 사용되고 있는지 확인합니다. 처리 중인 계산된 필터는 편집할 수 없습니다.

{% alert note %}
워크스페이스에는 한 번에 최대 500개의 활성화된 계산된 필터를 보유할 수 있습니다. 이 한도를 늘려야 하는 경우 Braze 계정 매니저에게 문의하세요.
{% endalert %}

#### 저장과 활성화 {#save-versus-activate}

계산된 필터를 활성화하지 않고 저장할 수 있습니다. 비활성 필터는 워크스페이스에 남아 있지만 활성화할 때까지 Segments에 추가할 수 없습니다. **필터 활성화**를 선택하여 세분화에서 필터를 사용합니다.

## 자주 묻는 질문 {#frequently-asked-questions}

### 여러 커스텀 이벤트를 사용하는 계산된 필터를 생성할 수 있나요? {#can-i-create-a-calculated-filter-that-uses-multiple-custom-events}

계산된 필터를 사용할 때 하나의 커스텀 이벤트, 하나의 구매 이벤트, 하나의 eCommerce 이벤트 또는 하나의 채널 상호작용을 선택할 수 있습니다. 그러나 Segment를 생성할 때 여러 계산된 필터를 AND 또는 OR로 결합할 수 있습니다.

[SQL 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)을 사용하면 여러 이벤트를 추가하거나 여러 Snowflake 테이블을 참조할 수 있습니다.

### 활성 Campaign에 존재하는 계산된 필터를 아카이브할 수 있나요? {#can-i-archive-calculated-filters-if-they-exist-in-an-active-campaign}

아니요. 계산된 필터를 아카이브하려면 먼저 모든 활성 메시징에서 해당 필터를 제거해야 합니다.

### 계산된 필터에서 배열을 사용할 수 있나요? {#can-i-use-arrays-in-calculated-filters}

네. 배열을 사용하려면 속성정보 이름에 대괄호(`[]`)를 추가합니다. 속성정보가 `location_code`인 경우 `location_code[]`로 입력합니다.

Braze는 `[]`를 사용하여 배열을 순회하고 순회된 배열의 항목이 이벤트 속성정보와 일치하는지 확인합니다. 예를 들어, 배열 속성정보의 값 중 하나 이상과 일치하는 사용자의 계산된 필터를 생성할 수 있습니다.

### Braze는 "지난 X일"의 상대적 기간을 어떻게 계산하나요? {#how-does-braze-calculate-the-time-period-for-a-relative-time-period-of-last-x-days}

계산된 필터가 상대적 기간("지난 X일")을 계산할 때, 시작 시간은 UTC 자정으로 설정됩니다. 예를 들어, 2024-09-16 21:00 UTC에 새로고침되고 10일을 지정하는 계산된 필터의 경우, 시작 시간은 2024-09-06 21:00 UTC가 아닌 2024-09-06 00:00 UTC로 설정됩니다.

그러나 SQL Segments를 사용하여 시간대를 지정할 수 있습니다. 예를 들어, 회사 시간 기준 자정을 기준으로 10일 전에 커스텀 이벤트를 수행한 사용자나, 현재 시간을 기준으로 10일 전에 이벤트를 수행한 사용자를 식별할 수 있습니다.