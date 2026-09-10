---
nav_title: 세그먼트 확장
article_title: 세그먼트 확장
page_order: 5
page_type: reference
description: "이 사용 방법 문서에서는 세그먼트 확장을 설정하고 사용하여 세분화 기능을 향상시키는 방법을 안내합니다."
tool: Segments
---

# 세그먼트 확장 {#segment-extensions}

> 세그먼트 확장을 사용하면 사용자 이력의 장기간에 걸쳐 매우 정밀한 Segment를 구축할 수 있습니다. 예를 들어, 세그먼트 확장을 사용하면 지난 16개월 동안 특정 제품을 구매한 사용자나 서비스에서 일정 금액 이상을 지출한 사용자를 타겟팅할 수 있습니다. 이벤트 속성정보를 사용하여 이 오디언스를 더욱 세분화하여 타겟팅을 더 정밀하게 만들 수 있습니다.

Braze 세분화를 사용하면 커스텀 이벤트 또는 구매 동작을 기반으로 사용자를 타겟팅할 수 있습니다. 세그먼트 확장은 이 기능을 강화하여 고객 프로필에 저장된 과거 데이터를 활용할 수 있게 합니다. 세그먼트 확장을 사용하면 지난 2년(730일) 동안 커스텀 이벤트 또는 구매 이벤트를 원하는 횟수만큼 완료한 사용자를 식별하고 도달할 수 있습니다.

## 세그먼트 확장을 사용하는 이유 {#why-use-segment-extensions}

Braze Segments는 동적 사용자 그룹을 생성할 수 있는 강력한 타겟팅 도구를 제공합니다. 대부분의 사용 사례에서는 이것만으로도 오디언스에 효과적으로 도달할 수 있습니다. 세그먼트 확장은 최대 2년 전의 행동을 분석하거나 복잡한 로직을 적용해야 하는 고급 사용 사례를 위해 설계되었으며, 데이터 보존이나 시스템 성능을 저하시키지 않습니다. [SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) 쿼리(SQL 세그먼트 확장) 또는 자체 [데이터 웨어하우스]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments)의 데이터를 사용하여 오디언스를 더욱 정교하게 세분화할 수 있습니다.

예를 들어, Braze 기본 세분화는 최근 제품 중 하나를 구매한 사용자를 식별하는 등 여러분이 정의한 특정 기준에 맞는 사용자를 찾아줍니다. 세그먼트 확장을 사용하면 더 깊이 분석할 수 있습니다. 예를 들어 18~24개월 전에 특정 제품의 특정 색상을 최소 두 번 이상 구매한 사용자를 식별하는 것이 가능합니다. 세그먼트 확장은 필수 기능이 아닌 향상 기능입니다. 더 고급 필터나 더 긴 룩백 윈도우가 필요한 경우, 데이터 사용량을 최적화하면서도 활용할 수 있는 훌륭한 도구입니다.

{% alert note %}
워크스페이스당 특정 시점에 활성화할 수 있는 세그먼트 확장은 기본적으로 50개로 제한됩니다. 이 한도를 늘려야 하는 경우, Braze 고객 성공 매니저에게 연락하여 사용 사례를 논의하세요.
{% endalert %}

## 세그먼트 확장 만들기 {#creating-a-segment-extension}

세그먼트 확장을 만들려면 커스텀 이벤트 속성정보를 기반으로 사용자 Segment를 세분화하는 필터를 생성합니다. 세그먼트 확장을 만들 때 Segment를 정적으로 할지, 아니면 설정된 간격으로 동적으로 새로 고칠지를 선택할 수 있습니다.

### 1단계: 세그먼트 확장으로 이동하기 {#step-1-navigate-to-segment-extensions}

**오디언스** > **세그먼트 확장**으로 이동합니다.

세그먼트 확장 테이블에서 **새 확장 만들기**를 선택한 다음, 세그먼트 확장 생성 환경을 선택합니다:

- **간단한 확장:** 안내 양식을 사용하여 단일 이벤트에 초점을 맞춘 세그먼트 확장을 생성합니다. SQL을 사용하고 싶지 않을 때 적합합니다.
- **템플릿으로 시작:** Snowflake 데이터를 활용하여 커스터마이징 가능한 템플릿으로 SQL Segment를 생성합니다.
- **증분 새로 고침:** 최근 2일간의 데이터를 자동으로 새로 고치거나 필요에 따라 수동으로 새로 고치는 Snowflake SQL Segment를 작성합니다. 정확성과 비용 효율성의 균형을 맞추기에 적합합니다.
- **전체 새로 고침:** 수동 새로 고침 시 전체 오디언스를 다시 계산하는 Snowflake 데이터 또는 [CDI 연결된 소스]({{site.baseurl}}/cdi_segment_extensions)를 사용한 SQL Segment를 작성합니다. 완전하고 최신의 오디언스 뷰가 필요할 때 적합합니다.

![선택할 수 있는 다양한 세그먼트 확장 생성 환경이 포함된 테이블.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%"}

SQL을 사용하는 환경을 선택한 경우 [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)에서 자세한 정보를 확인하세요. **간단한 확장**을 선택한 경우 2단계로 진행합니다.

#### SQL 크레딧 사용량 {#sql-credit-usage}

다음 세그먼트 확장 유형은 SQL 크레딧을 소비합니다:

- SQL 세그먼트 확장(증분 및 전체 새로 고침 모두)
- 카탈로그 Segments
- CDI Segments
    - 크레딧은 사용자의 자체 데이터 웨어하우스 내에서 소비됩니다

### 2단계: 세그먼트 확장 이름 지정하기 {#step-2-name-your-segment-extension}

필터링하려는 사용자 유형을 설명하여 세그먼트 확장의 이름을 지정합니다. 이렇게 하면 다른 사람들이 확장을 정확하게 찾아 적용하는 데 도움이 됩니다.

!["Online Shoppers Extension - 90 Days"라는 이름의 세그먼트 확장.]({% image_buster /assets/img/segment/segment_extension2.png %})

### 3단계: 기준 선택하기 {#step-3-choose-your-criteria}

타겟팅을 위해 구매, 메시지 인게이지먼트, 이커머스 추천 이벤트 또는 커스텀 이벤트 기준 중에서 선택합니다. 원하는 이벤트 유형 기준을 선택한 후, 사용자 목록에 대해 타겟팅할 구매 항목, 메시지 상호작용, 이커머스 추천 이벤트 또는 커스텀 이벤트를 선택합니다. 그런 다음 사용자가 해당 이벤트를 몇 번 수행해야 하는지(초과, 미만 또는 동일), 그리고 기간을 선택합니다—세그먼트 확장의 경우 최대 730일(2년) 전까지 조회할 수 있습니다.

730일 이상의 이벤트 데이터를 기반으로 한 세분화는 **Segments**에 있는 다른 필터를 사용하여 수행할 수 있습니다. 기간을 선택할 때 지난 X일간의 상대적 날짜 범위, 시작 날짜, 종료 날짜 또는 정확한 날짜 범위(날짜 A부터 날짜 B)를 지정할 수 있습니다.

![2025년 3월 1일부터 2025년 3월 31일까지의 날짜 범위에서 커스텀 이벤트를 2회 이상 수행한 사용자에 대한 세분화 기준.]({% image_buster /assets/img/segment/segment_extension1.png %})

이커머스 추천 이벤트를 사용하여 세그먼트 확장을 만드는 경우, 먼저 기준으로 **이커머스 추천 이벤트**를 선택한 다음, 드롭다운에서 이벤트를 선택합니다.

![사용 가능한 추천 이벤트 드롭다운이 있는 이커머스 추천 이벤트 기준.]({% image_buster /assets/img/segment/ecommerce_recommended_event_criterion.png %})

#### 이벤트 속성정보 세분화 {#event-property-segmentation}

타겟팅 정밀도를 높이려면 **속성정보 필터 추가** 체크박스를 선택합니다. 이를 통해 구매 또는 커스텀 이벤트의 특정 속성정보를 기반으로 세부적으로 필터링할 수 있습니다. 문자열, 숫자, 부울 및 시간 객체를 기반으로 한 이벤트 속성정보 세분화를 지원합니다.

##### 속성정보 데이터 유형 {#property-data-types}

문자열 속성정보의 경우 한 번에 여러 값을 입력할 수 있습니다. 다음 예시에서는 이 필터가 개 품종이 6개의 특정 품종 중 하나와 동일한 사용자를 조회합니다.

![문자열 속성정보를 기반으로 세분화하기.]({% image_buster /assets/img/segment/property5.png %})

##### 이커머스 추천 이벤트 속성정보 {#ecommerce-recommended-event-properties}

이커머스 추천 이벤트에 이벤트 속성정보를 추가하면 속성정보 드롭다운에 해당 이벤트에 사용 가능한 속성정보가 자동으로 채워집니다.

세그먼트 확장은 각 이커머스 추천 이벤트에 대해 문서화된 허용 목록에 있는 이벤트 속성정보만 지원합니다. API 또는 SDK를 통해 전송하는 커스텀 최상위 속성정보는 이벤트 데이터에 나타나더라도 확장 속성정보 필터에 유효하지 않습니다. 허용 목록에 없는 최상위 속성정보를 사용하면 확장이 저장되거나 보관 해제되지 않습니다.

비표준 속성정보를 기준으로 필터링해야 하는 경우, 이벤트를 기록할 때 해당 속성정보를 `metadata` 하위에 중첩시키세요(예: `color` 대신 `metadata.color`). 지원되는 속성정보는 [이벤트 스키마]({{site.baseurl}}/user_guide/data/activation/events/recommended_events#event-schemas) 및 [이커머스 추천 이벤트 유형]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events)을 참조하세요.

![사용 가능한 속성정보 드롭다운이 있는 세그먼트 확장 세부 정보.]({% image_buster /assets/img/segment/ecommerce_recommended_event_properties.png %})

##### 중첩된 이벤트 속성정보 {#nested-event-properties}

[중첩된 이벤트 속성정보]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects)를 기반으로 한 세분화도 지원합니다. 비교 드롭다운에서 중첩된 속성정보의 데이터 유형과 일치하는 비교를 선택합니다. 중첩된 속성정보를 포함하는 이커머스 추천 이벤트에도 동일한 중첩된 이벤트 속성정보 구문을 사용하여 중첩된 속성정보를 추가할 수 있습니다.

사용 가능한 다양한 중첩된 속성정보에 대한 정보는 [이커머스 추천 이벤트 유형]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events)을 참조하세요. 세그먼트 확장의 속성정보 이름에 필요한 스키마를 생성하려면 [커스텀 이벤트의 중첩 객체]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects)의 단계를 따르세요.

![중첩된 이벤트 속성정보를 기반으로 세분화하기.]({% image_buster /assets/img/segment/nested_segment_extensions.png %})

##### 조회 기간 및 데이터 포인트 {#lookback-window-and-data-points}

세그먼트 확장은 이벤트 속성정보의 장기 저장에 의존하며, 타임스탬프가 지정된 속성정보 저장 제한이 없습니다. 지난 2년 이내에 추적된 이벤트 속성정보를 조회할 수 있습니다. 세그먼트 확장 내에서 이벤트 속성정보를 사용해도 데이터 포인트 사용량에 영향을 미치지 않습니다.

{% alert note %}
Segment에서 이벤트 속성정보나 중첩 커스텀 속성을 사용하기 위해 세그먼트 확장이 반드시 필요한 것은 아닙니다. 세그먼트 확장은 기본 Segment를 만드는 데 사용되는 히스토리 기간을 확장할 뿐입니다. 지난 30일간의 이벤트 속성정보를 사용하거나 중첩 커스텀 속성을 사용하는 실시간 기본 [Segment]({{site.baseurl}}/user_guide/audience/segments)를 만들 수 있습니다. 마찬가지로 이벤트 속성정보를 기반으로 실시간 트리거되도록 [메시지를 스케줄]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)할 수 있으며, 세그먼트 확장은 필요하지 않습니다.
{% endalert %}

### 4단계: 새로 고침 설정 지정하기(선택 사항) {#step-4-designate-refresh-settings-optional}

{% multi_lang_include audience/segments.md section='Refresh settings' %}

### 5단계: 세그먼트 확장 저장하기 {#step-5-save-your-segment-extension}

**저장**을 선택하면 세그먼트 확장이 처리되기 시작합니다. 세그먼트 확장이 생성되는 데 걸리는 시간은 사용자 수, 캡처하는 커스텀 이벤트 또는 구매 이벤트의 수, 조회하는 히스토리 기간에 따라 달라집니다.

세그먼트 확장이 처리 중일 때 세그먼트 확장 이름 옆에 작은 애니메이션이 표시되고, 세그먼트 확장 목록의 **상태** 열에 **처리 중**이 표시됩니다. 처리 중에는 세그먼트 확장을 편집할 수 없습니다.

![두 개의 활성 확장이 있는 "세그먼트 확장" 페이지.]({% image_buster /assets/img/segment/segment_extension5.png %})

세그먼트 확장이 처리 중일 때 Braze는 오디언스 세분화 목적으로 처리가 시작되기 전의 기본 Segment 버전 히스토리를 계속 사용합니다. 처리는 저장 또는 새로 고침이 발생할 때마다 이루어지며, 사용자 프로필을 쿼리하고 업데이트하는 작업을 포함합니다. 즉, 기본 Segment의 멤버십이 즉시 업데이트되지는 않습니다. 이는 새로 고침이 처리를 시작하기 전에 사용자의 작업이 수행되지 않으면, 해당 특정 새로 고침이 완료된 후 사용자가 세그먼트 확장에 포함된다는 보장이 없음을 의미합니다. 반대로, 새로 고침 전에 세그먼트 확장에 포함되어 있었지만 더 이상 기준을 충족하지 않는 사용자는 새로 고침 프로세스가 완료되고 업데이트가 적용될 때까지 계속 기본 Segment와 매칭됩니다.

#### 세그먼트 확장 상태 {#segment-extension-statuses}

**세그먼트 확장** 페이지에서 각 확장은 **상태**와 **마지막 처리** 타임스탬프를 표시합니다. 확장을 저장하거나 새로 고친 후 이 열을 확인하여 처리가 성공적으로 완료되었는지 확인하세요.

| 상태 | 설명 |
|---|---|
| 활성 | 확장이 성공적으로 처리를 완료하여 세분화에 사용할 수 있습니다. **마지막 처리**에 가장 최근 새로 고침이 완료된 시점이 표시됩니다. |
| 초안 | 확장이 저장되었지만 아직 활성화되지 않았습니다. |
| 보관됨 | 확장이 보관되어 세분화에 사용할 수 없습니다. |
| 새로 고침 비활성화됨 | 반복 오디언스 업데이트가 비활성화되었습니다. |
| 처리 중 | Braze가 저장 또는 새로 고침을 처리하고 있습니다. **상태** 열에 **처리 중**이 표시되고, 확장 이름 옆에 작은 애니메이션이 나타나며, 처리가 완료될 때까지 확장을 편집할 수 없습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="세그먼트 확장 상태" }

처리가 성공적으로 완료되지 않으면 **상태** 열에 여전히 **활성**이 표시될 수 있지만 확장 이름 옆에 오류 아이콘이 나타납니다. 아이콘 위로 마우스를 가져가면 실패 사유를 확인할 수 있습니다. 실패가 발생했지만 확장 처리가 완료되었어야 한다고 판단되면, 먼저 확장을 새로 고쳐보세요—상태가 오래된 것일 수 있습니다.

### 6단계: Segment에서 확장 사용하기 {#step-6-use-your-extension-in-a-segment}

세그먼트 확장을 만든 후 Segment를 생성하거나 Campaign 또는 Canvas의 오디언스를 정의할 때 필터로 사용할 수 있습니다. **사용자 속성** 섹션 아래의 필터 목록에서 **Braze 세그먼트 확장**을 선택하여 시작하세요.

!["Braze 세그먼트 확장"이 표시된 필터 드롭다운이 있는 "필터" 섹션.]({% image_buster /assets/img/segment/segment_extension7.png %})

Braze 세그먼트 확장 필터 목록에서 이 Segment에 포함하거나 제외할 세그먼트 확장을 선택합니다.

!["지난 56일간 이메일 클릭 1회" Segment를 포함하는 "Braze 세그먼트 확장" 필터.]({% image_buster /assets/img/segment/segment_extension6.png %})

세그먼트 확장 기준을 보려면 **확장 세부 정보 보기**를 선택하여 새 창에서 세부 정보를 확인하세요.

!["지난 56일간 이메일 클릭 1회"에 대한 확장.]({% image_buster /assets/img/segment/segment_extension8.png %}){: style="max-width:70%;"}

이제 평소처럼 [Segment 만들기]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)를 진행할 수 있습니다.

## 자주 묻는 질문 {#frequently-asked-questions}

### 여러 커스텀 이벤트를 사용하는 세그먼트 확장을 만들 수 있나요? {#can-i-create-a-segment-extension-that-uses-multiple-custom-events}

네. [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)을 사용할 때 여러 이벤트를 추가하거나 여러 Snowflake 테이블을 참조할 수 있습니다.

**간단한 확장** 세그먼트 확장을 사용할 때는 하나의 커스텀 이벤트, 하나의 구매 이벤트 또는 하나의 채널 상호작용을 선택할 수 있습니다. 그러나 기본 Segment를 생성할 때 AND 또는 OR로 여러 세그먼트 확장을 결합할 수 있습니다.

### 활성 Campaign에 포함된 세그먼트 확장을 아카이브할 수 있나요? {#can-i-archive-segment-extensions-if-they-exist-in-an-active-campaign}

아니요. 세그먼트 확장을 아카이브하려면 먼저 모든 활성 메시징에서 해당 확장을 제거해야 합니다.

### 세그먼트 확장에서 배열을 사용할 수 있나요? {#can-i-use-arrays-in-segment-extensions}

네. 배열을 사용하려면 속성정보 이름에 대괄호(`[]`)를 추가하세요. 속성정보가 `location_code`인 경우 `location_code[]`로 입력합니다.

Braze는 `[]`를 사용하여 배열을 순회하고, 순회된 배열의 항목 중 이벤트 속성정보와 일치하는 항목이 있는지 확인합니다. 예를 들어, 배열 속성정보의 값 중 하나 이상과 일치하는 사용자의 세그먼트 확장을 만들 수 있습니다.

### Braze는 "최근 __일" 상대적 기간을 어떻게 계산하나요? {#how-does-braze-calculate-the-time-period-for-a-relative-time-period-of-last-__-days}

세그먼트 확장에서 상대적 기간("최근 X일")을 계산할 때, 시작 시간은 자정 UTC로 설정됩니다. 예를 들어, 2024-09-16 21:00 UTC에 새로고침되고 10일을 지정하는 세그먼트 확장의 경우, 시작 시간은 2024-09-06 21:00 UTC가 아닌 2024-09-06 00:00 UTC로 설정됩니다.

그러나 SQL 세그먼트를 사용하면 시간대를 지정할 수 있습니다. 회사 시간 기준 자정을 기준으로 10일 전에 커스텀 이벤트를 수행한 사용자 또는 현재 시간 기준으로 10일 전에 이벤트를 수행한 사용자를 식별할 수 있습니다.