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

Braze Segments는 동적 사용자 그룹을 생성할 수 있는 강력한 타겟팅 도구를 제공합니다. 대부분의 사용 사례에서는 이것만으로도 오디언스에 효과적으로 도달할 수 있습니다. 세그먼트 확장은 최대 2년 전의 동작을 분석하거나 복잡한 로직을 적용해야 하는 고급 사용 사례를 위해 설계되었으며, 데이터 보존이나 시스템 성능을 저하시키지 않습니다. [SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) 쿼리(SQL 세그먼트 확장) 또는 자체 [데이터 웨어하우스]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments)의 데이터를 사용하여 오디언스를 더욱 세분화할 수 있습니다.

예를 들어, Braze 기본 세분화는 최근 제품 중 하나를 구매한 사용자를 식별하는 것과 같이 정의한 특정 기준에 맞는 사용자를 찾습니다. 세그먼트 확장을 사용하면 더 깊이 들어갈 수 있습니다. 예를 들어 18~24개월 전에 특정 제품의 특정 색상을 최소 2회 이상 구매한 사용자를 식별할 수 있습니다. 세그먼트 확장은 향상 기능이지 필수 요건이 아닙니다. 더 고급 필터나 더 긴 조회 기간이 필요한 경우, 데이터 사용량을 최적화하면서 도움이 되는 훌륭한 도구입니다.

{% alert note %}
워크스페이스당 특정 시점에 기본 50개의 활성 세그먼트 확장이 할당됩니다. 이 한도를 늘려야 하는 경우, Braze 고객 성공 매니저에게 연락하여 사용 사례를 논의하세요.
{% endalert %}

## 세그먼트 확장 생성하기 {#creating-a-segment-extension}

세그먼트 확장을 생성하려면 커스텀 이벤트 속성정보를 기반으로 사용자 Segment를 세분화하는 필터를 만듭니다. 세그먼트 확장을 생성할 때 Segment가 정적인지 또는 설정된 간격으로 동적으로 새로고침되는지를 선택합니다.

### 1단계: 세그먼트 확장으로 이동하기 {#step-1-navigate-to-segment-extensions}

**오디언스** > **세그먼트 확장**으로 이동합니다.

세그먼트 확장 테이블에서 **새 확장 만들기**를 선택한 다음, 세그먼트 확장 생성 경험을 선택합니다:

- **간단한 확장:** 안내 양식을 사용하여 단일 이벤트에 초점을 맞춘 세그먼트 확장을 생성합니다. SQL을 사용하고 싶지 않을 때 가장 적합합니다.
- **템플릿으로 시작:** Snowflake 데이터를 사용하여 커스터마이즈 가능한 템플릿으로 SQL Segment를 생성합니다.
- **증분 새로고침:** 최근 2일간의 데이터를 자동으로 새로고침하거나 필요에 따라 수동으로 새로고침하는 Snowflake SQL Segment를 작성합니다. 정확성과 비용 효율성의 균형을 맞추는 데 가장 적합합니다.
- **전체 새로고침:** 수동 새로고침 시 전체 오디언스를 재계산하는 Snowflake 데이터 또는 [CDI 연결 소스]({{site.baseurl}}/cdi_segment_extensions)를 사용하여 SQL Segment를 작성합니다. 오디언스의 완전하고 최신 보기가 필요할 때 가장 적합합니다.

![선택할 수 있는 다양한 세그먼트 확장 생성 경험이 있는 테이블.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%"}

SQL을 사용하는 경험을 선택한 경우, 자세한 내용은 [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)을 참조하세요. **간단한 확장**을 선택한 경우, 2단계로 계속 진행합니다.

#### SQL 크레딧 사용량 {#sql-credit-usage}

다음 세그먼트 확장 유형은 SQL 크레딧을 소비합니다:

- SQL 세그먼트 확장(증분 및 전체 새로고침 모두)
- 카탈로그 Segments
- CDI Segments
    - 크레딧은 자체 데이터 웨어하우스 내에서 소비됩니다

### 2단계: 세그먼트 확장 이름 지정하기 {#step-2-name-your-segment-extension}

필터링하려는 사용자 유형을 설명하여 세그먼트 확장의 이름을 지정합니다. 이렇게 하면 Segment에서 필터로 적용할 때 이 확장을 쉽고 정확하게 찾을 수 있습니다.

!["Online Shoppers Extension - 90 Days"라는 이름의 세그먼트 확장.]({% image_buster /assets/img/segment/segment_extension2.png %})

### 3단계: 기준 선택하기 {#step-3-choose-your-criteria}

타겟팅을 위해 구매, 메시지 인게이지먼트, 이커머스 추천 이벤트 또는 커스텀 이벤트 기준 중에서 선택합니다. 원하는 이벤트 유형 기준을 선택한 후, 사용자 목록에 대해 타겟팅할 구매 항목, 메시지 상호작용, 이커머스 추천 이벤트 또는 커스텀 이벤트를 선택합니다. 그런 다음 사용자가 해당 이벤트를 완료해야 하는 횟수(초과, 미만 또는 동일)와 기간을 선택합니다. 세그먼트 확장의 경우 최대 730일(2년) 전까지 조회할 수 있습니다.

730일 이상의 이벤트 데이터를 기반으로 한 세분화는 **Segments**에 있는 다른 필터를 사용하여 수행할 수 있습니다. 기간을 선택할 때 지난 X일의 상대적 날짜 범위, 시작 날짜, 종료 날짜 또는 정확한 날짜 범위(날짜 A부터 날짜 B까지)를 지정할 수 있습니다.

![2025년 3월 1일부터 2025년 3월 31일까지의 날짜 범위에서 커스텀 이벤트를 2회 이상 수행한 사용자에 대한 세분화 기준.]({% image_buster /assets/img/segment/segment_extension1.png %})

이커머스 추천 이벤트를 사용하여 세그먼트 확장을 생성하는 경우, 먼저 기준으로 **eCommerce Recommended Event**를 선택한 다음, 드롭다운에서 이벤트를 선택합니다.

![사용 가능한 추천 이벤트 드롭다운이 있는 이커머스 추천 이벤트 기준.]({% image_buster /assets/img/segment/ecommerce_recommended_event_criterion.png %})

#### 이벤트 속성정보 세분화 {#event-property-segmentation}

타겟팅 정밀도를 높이려면 **Add Property Filters** 체크박스를 선택합니다. 이렇게 하면 구매 또는 커스텀 이벤트의 특정 속성정보를 기반으로 세부적으로 분석할 수 있습니다. 문자열, 숫자, 부울 및 시간 오브젝트를 기반으로 한 이벤트 속성정보 세분화를 지원합니다.

문자열 속성정보의 경우 한 번에 여러 값을 입력할 수 있습니다. 아래 예시에서 이 필터는 상태가 gold, silver 또는 bronze 중 하나와 같은 사용자를 찾습니다.

![문자열 속성정보를 기반으로 한 세분화.]({% image_buster /assets/img/segment/property5.png %})

![숫자 속성정보를 기반으로 한 세분화.]({% image_buster /assets/img/segment/property2.png %})

![부울 속성정보를 기반으로 한 세분화.]({% image_buster /assets/img/segment/property3.png %})

![날짜/시간 오브젝트를 기반으로 한 세분화.]({% image_buster /assets/img/segment/property4.png %})

이커머스 추천 이벤트를 사용하고 이벤트 속성정보를 추가하면, 해당 특정 이커머스 추천 이벤트에 사용 가능한 속성정보로 속성정보 드롭다운이 자동으로 채워집니다.

![사용 가능한 속성정보 드롭다운이 있는 세그먼트 확장 세부 정보.]({% image_buster /assets/img/segment/ecommerce_recommended_event_properties.png %})

[중첩된 이벤트 속성정보]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects)를 기반으로 한 세분화도 지원합니다. 비교 드롭다운에서 중첩된 속성정보의 데이터 유형과 일치하는 비교를 선택합니다. 중첩된 속성정보를 포함하는 모든 이커머스 추천 이벤트에 대해 동일한 중첩된 이벤트 속성정보 구문을 사용하여 중첩된 속성정보를 추가할 수 있습니다. 사용 가능한 다양한 중첩된 속성정보에 대한 정보는 [이커머스 추천 이벤트 유형]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events)을 참조하세요. 세그먼트 확장의 속성정보 이름에 필요한 스키마를 생성하려면 [커스텀 이벤트의 중첩된 오브젝트]({{site.baseurl}}/user_guide/data/activation/events/custom_events/nested_objects)의 단계를 따르세요.

![중첩된 이벤트 속성정보를 기반으로 한 세분화.]({% image_buster /assets/img/segment/nested_segment_extensions.png %})

세그먼트 확장은 이벤트 속성정보의 장기 저장에 의존하며 타임스탬프 속성정보 저장 제한이 없습니다. 지난 2년 이내에 추적된 이벤트 속성정보를 조회할 수 있습니다. 세그먼트 확장 내에서 이벤트 속성정보를 사용해도 데이터 포인트 사용량에 영향을 미치지 않습니다.

{% alert note %}
Segment에서 이벤트 속성정보나 중첩 커스텀 속성을 사용하기 위해 세그먼트 확장이 필요한 것은 아닙니다. 세그먼트 확장은 기본 Segment를 생성하는 데 사용되는 과거 기간을 확장할 뿐입니다. 지난 30일간의 이벤트 속성정보를 사용하거나 중첩 커스텀 속성을 사용하는 실시간 기본 [Segment]({{site.baseurl}}/user_guide/audience/segments)를 생성할 수 있습니다. 마찬가지로, 이벤트 속성정보를 기반으로 실시간으로 트리거되도록 [메시지를 스케줄]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery)할 수 있으며, 세그먼트 확장이 필요하지 않습니다.
{% endalert %}

### 4단계: 새로고침 설정 지정하기(선택 사항) {#step-4-designate-refresh-settings-optional}

{% multi_lang_include audience/segments.md section='Refresh settings' %}

### 5단계: 세그먼트 확장 저장하기 {#step-5-save-your-segment-extension}

**저장**을 선택하면 세그먼트 확장이 처리되기 시작합니다. 세그먼트 확장을 생성하는 데 걸리는 시간은 사용자 수, 캡처하는 커스텀 이벤트 또는 구매 이벤트 수, 그리고 과거 이력을 조회하는 일수에 따라 달라집니다.

세그먼트 확장이 처리되는 동안 세그먼트 확장 이름 옆에 작은 애니메이션이 표시되고, 세그먼트 확장 목록의 **마지막 처리** 열에 "Processing"이라는 단어가 표시됩니다. 처리 중인 세그먼트 확장은 편집할 수 없습니다.

![2개의 활성 확장이 있는 "세그먼트 확장" 페이지.]({% image_buster /assets/img/segment/segment_extension5.png %})

세그먼트 확장이 처리되는 동안 Braze는 오디언스 세분화 목적으로 처리가 시작되기 전의 기본 Segment 버전 이력을 계속 사용합니다. 처리는 저장 또는 새로고침이 발생할 때마다 이루어지며, 고객 프로필을 쿼리하고 업데이트하는 작업을 포함합니다. 즉, 기본 Segment의 멤버십이 즉시 업데이트되지는 않습니다. 이는 사용자의 동작이 새로고침 처리가 시작되기 전에 수행되지 않으면, 해당 특정 새로고침이 완료된 후 사용자가 세그먼트 확장에 포함된다고 보장할 수 없음을 의미합니다. 반대로, 새로고침 전에 세그먼트 확장에 있었지만 더 이상 기준을 충족하지 않는 사용자는 새로고침 프로세스가 완료되고 업데이트가 적용될 때까지 기본 Segment와 계속 일치합니다.

### 6단계: Segment에서 확장 사용하기 {#step-6-use-your-extension-in-a-segment}

세그먼트 확장을 생성한 후, Segment를 생성하거나 Campaign 또는 Canvas의 오디언스를 정의할 때 필터로 사용할 수 있습니다. **사용자 속성** 섹션 아래의 필터 목록에서 **Braze Segment Extension**을 선택하여 시작합니다.

!["Braze Segment Extensions"를 표시하는 필터 드롭다운이 있는 "필터" 섹션.]({% image_buster /assets/img/segment/segment_extension7.png %})

Braze 세그먼트 확장 필터 목록에서 이 Segment에 포함하거나 제외할 세그먼트 확장을 선택합니다.

!["지난 56일간 이메일 클릭 1회" Segment를 포함하는 "Braze Segment Extensions" 필터.]({% image_buster /assets/img/segment/segment_extension6.png %})

세그먼트 확장 기준을 보려면 **확장 세부 정보 보기**를 선택하여 새 창에서 세부 정보를 표시합니다.

!["지난 56일간 이메일 클릭 1회"에 대한 확장.]({% image_buster /assets/img/segment/segment_extension8.png %}){: style="max-width:70%;"}

이제 평소처럼 [Segment 생성]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)을 진행할 수 있습니다.

## 자주 묻는 질문 {#frequently-asked-questions}

### 여러 커스텀 이벤트를 사용하는 세그먼트 확장을 생성할 수 있나요? {#can-i-create-a-segment-extension-that-uses-multiple-custom-events}

네. [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)을 사용할 때 여러 이벤트를 추가하거나 여러 Snowflake 테이블을 참조할 수 있습니다.

**간단한 확장** 세그먼트 확장을 사용할 때는 하나의 커스텀 이벤트, 하나의 구매 이벤트 또는 하나의 채널 상호작용을 선택할 수 있습니다. 그러나 기본 Segment를 생성할 때 여러 세그먼트 확장을 AND 또는 OR로 결합할 수 있습니다.

### 활성 Campaign에 존재하는 세그먼트 확장을 아카이브할 수 있나요? {#can-i-archive-segment-extensions-if-they-exist-in-an-active-campaign}

아니요. 세그먼트 확장을 아카이브하려면 먼저 모든 활성 메시징에서 제거해야 합니다.

### 세그먼트 확장에서 배열을 사용할 수 있나요? {#can-i-use-arrays-in-segment-extensions}

네. 배열을 사용하려면 속성정보 이름에 대괄호(`[]`)를 추가합니다. 속성정보가 `location_code`인 경우 `location_code[]`로 입력합니다.

Braze는 `[]`를 사용하여 배열을 순회하고 순회된 배열의 항목이 이벤트 속성정보와 일치하는지 확인합니다. 예를 들어, 배열 속성정보의 값 중 하나 이상과 일치하는 사용자의 세그먼트 확장을 생성할 수 있습니다.

### Braze는 "지난 __ 일"의 상대적 기간을 어떻게 계산하나요? {#how-does-braze-calculate-the-time-period-for-a-relative-time-period-of-last-__-days}

세그먼트 확장이 상대적 기간("지난 X일")을 계산할 때, 시작 시간은 자정 UTC로 설정됩니다. 예를 들어, 2024-09-16 21:00 UTC에 새로고침되고 10일을 지정하는 세그먼트 확장의 경우, 시작 시간은 2024-09-06 21:00 UTC가 아닌 2024-09-06 00:00 UTC로 설정됩니다.

그러나 SQL Segments를 사용하여 시간대를 지정할 수 있습니다. 회사 시간 기준 자정을 기준으로 10일 전에 커스텀 이벤트를 수행한 사용자 또는 현재 시간을 기준으로 10일 전에 이벤트를 수행한 사용자를 식별할 수 있습니다.