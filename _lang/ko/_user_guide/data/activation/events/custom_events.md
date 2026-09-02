---
nav_title: 커스텀 이벤트
article_title: 커스텀 이벤트
page_order: 1
page_type: reference
description: "이 문서에서는 커스텀 이벤트 및 속성정보, 세분화, 사용 방법, Canvas 진입 속성정보, 관련 분석을 볼 수 있는 위치 등에 대해 설명합니다."
search_rank: 2
---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/custom-events-and-attributes){: style="float:right;width:120px;border:0;" class="noimgborder"}커스텀 이벤트 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomcustom-events-and-attributes-stylefloatrightwidth120pxborder0-classnoimgbordercustom-events}

> 이 문서에서는 커스텀 이벤트 및 속성정보, 고객 프로필 이벤트 기록, 관련 세분화 필터, Canvas 진입 속성정보, 관련 분석 등에 대해 설명합니다. Braze 이벤트에 대해 전반적으로 알아보려면 [이벤트]({{site.baseurl}}/user_guide/data/activation/events)를 참조하세요.

커스텀 이벤트는 사용자가 수행한 동작 또는 사용자에 대한 업데이트입니다. 커스텀 이벤트가 기록되면 원하는 수와 유형의 후속 Campaign을 트리거할 수 있습니다. 그런 다음 [세분화 필터](#segmentation-filters)를 사용하여 해당 커스텀 이벤트가 발생한 최근성 및 빈도에 따라 사용자를 세분화할 수 있습니다. 따라서 커스텀 이벤트는 애플리케이션 내에서 가치가 높은 사용자 상호작용을 추적하는 데 가장 적합합니다.

## 사용 사례 {#use-cases}

일반적인 커스텀 이벤트 사용 사례는 다음과 같습니다:

{% multi_lang_include data_activation/custom_event_use_cases.md %}

## 커스텀 이벤트 관리 {#managing-custom-events}

대시보드에서 **데이터 설정** > **커스텀 이벤트**로 이동하여 커스텀 이벤트를 관리, 생성 또는 차단 목록에 추가할 수 있습니다.

### 중복된 커스텀 속성 또는 이벤트 문제 해결 {#troubleshooting-duplicate-custom-attributes-or-events}

{% multi_lang_include data_activation/troubleshooting_duplicate_custom_data_entries.md %}

커스텀 이벤트 옆의 메뉴를 선택하여 다음 작업을 수행할 수 있습니다:

### 차단 목록에 추가 {#blocklisting}

작업 메뉴를 통해 개별 커스텀 이벤트를 차단 목록에 추가하거나, 최대 100개의 이벤트를 선택하여 일괄적으로 차단 목록에 추가할 수 있습니다.

커스텀 이벤트를 차단하면:

{% multi_lang_include data_activation/custom_event_block_effects.md %}

또한 차단된 커스텀 이벤트가 현재 Braze의 다른 영역에서 필터 또는 트리거에 의해 참조되고 있는 경우, 해당 이벤트를 참조하는 모든 필터 또는 트리거 인스턴스가 제거되고 보관될 것이라는 경고 모달이 표시됩니다.

커스텀 데이터의 차단 목록 추가 및 삭제에 대한 자세한 내용은 [커스텀 데이터 차단 목록]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data)을 참조하세요.

### 설명 추가 {#adding-descriptions}

`Manage Events, Attributes, Purchases` [사용자 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)이 있으면 커스텀 이벤트가 생성된 후에 설명을 추가할 수 있습니다. 커스텀 이벤트의 **설명 편집**을 선택하고 팀을 위한 메모 등 원하는 내용을 입력하세요.

### 태그 추가 {#adding-tags}

"Manage Events, Attributes, Purchases" [사용자 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)이 있으면 커스텀 이벤트가 생성된 후에 태그를 추가할 수 있습니다. 추가된 태그를 사용하여 이벤트 목록을 필터링할 수 있습니다.

### 데이터 내보내기 {#exporting-data}

커스텀 이벤트 목록을 CSV 파일로 내보내려면 페이지 상단의 **모두 내보내기**를 선택합니다. CSV 파일이 생성되고 다운로드 링크가 이메일로 전송됩니다.

{% alert note %}
프로필에 정의하거나 저장할 수 있는 고유 **커스텀 이벤트** 또는 **커스텀 속성**의 수에 대한 고정된 대시보드 제한은 없습니다. 실질적인 한도는 데이터 형태, 수집량, 워크스페이스 성능에 따라 달라집니다. 매우 방대한 이벤트 또는 속성 카탈로그를 추적할 계획이라면 Braze 계정 팀과 함께 모델링 및 관리(예: 사용하지 않는 데이터 [차단 목록 추가]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data))에 대해 논의하세요.
{% endalert %}

## 사용 보고서 보기 {#viewing-usage-reports}

사용 보고서는 특정 커스텀 이벤트를 사용하는 모든 Canvases, Campaigns 및 Segments를 나열합니다. 이 목록에는 Liquid 사용은 포함되지 않습니다.

해당 커스텀 이벤트 옆의 체크박스를 선택한 다음 **사용 보고서 보기**를 선택하면 한 번에 최대 100개의 사용 보고서를 볼 수 있습니다.

## 커스텀 이벤트 기록하기 {#logging-custom-events}

커스텀 이벤트를 사용하려면 추가 설정이 필요합니다. 커스텀 이벤트를 기록하는 데 사용되는 메서드와 커스텀 이벤트에 속성정보 및 수량을 추가하는 방법에 대해서는 다음 플랫폼 설명서를 참조하세요.

{% details 플랫폼별 설명서를 확인하려면 펼치기 %}

- [Android 및 FireOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=swift)
- [웹]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=web)
- [React Native]({{site.baseurl}}/developer_guide/analytics#custom-events)
- [Unity]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=unity)
- [.NET MAUI (이전의 Xamarin)]({{site.baseurl}}/developer_guide/analytics?sdktab=xamarin#custom-events)
- [Roku]({{site.baseurl}}/developer_guide/analytics/logging_events?tab=roku)

{% enddetails %}

## 커스텀 이벤트 저장 {#custom-event-storage}

**고객 프로필**에 저장된 모든 데이터는 커스텀 이벤트 메타데이터(첫 번째 또는 마지막 발생, 총 횟수, 30일 동안의 Y 중 X)를 포함하여, 각 프로필이 <a href="/docs/user_archival#active-users">활성</a> 상태인 한 무기한 보존됩니다.

## 사용자의 이벤트 기록 보기 {#view-a-users-event-history}

사용자 프로필의 **이벤트 기록** 탭을 사용하여 해당 사용자의 최근 커스텀 이벤트 및 구매를 확인할 수 있습니다. 이를 통해 통합이 이벤트를 올바르게 기록하고 있는지 확인하고 대시보드에서 직접 사용자 수준의 문제를 해결할 수 있습니다.

사용자의 이벤트 기록을 보려면:

1. **오디언스** > **사용자 검색**으로 이동한 다음 사용자를 선택하여 프로필을 엽니다.
2. **이벤트 기록** 탭을 선택합니다.

이 탭에는 최근 30일 동안의 사용자 커스텀 이벤트 및 구매가 최대 100개까지 최신순으로 표시됩니다.

각 이벤트에는 다음이 포함됩니다:

- **이벤트 유형:** 이벤트가 커스텀 이벤트인지 구매인지 여부입니다.
- **이벤트 이름:** 기록된 이벤트 이름입니다.
- **시간:** 이벤트가 발생한 시점입니다.
- **속성정보:** 해당 발생에 대한 전체 이벤트 속성정보로, JSON으로 표시됩니다.

일반적인 사용 사례는 다음과 같습니다:

- 개발 중이거나 릴리스 후 SDK 또는 API 통합이 예상대로 이벤트를 전송하고 있는지 확인합니다.
- 사용자가 이벤트 트리거 Campaign 또는 Canvas에 진입했거나 진입하지 않은 이유를 문제 해결합니다.
- 데이터 내보내기를 설정하지 않고도 특정 사용자의 지원 문제를 조사합니다.

{% alert note %}
**이벤트 기록** 탭을 보려면 이벤트 속성정보에 개인 데이터가 포함될 수 있으므로 **사용자 검색**, **PII 보기**, **사용자 이벤트 속성정보 보기** 사용자 권한이 필요합니다. 자세한 내용은 [회사 사용자 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)을 참조하세요.
{% endalert %}

## 세분화 필터 {#segmentation-filters}

다음 표는 커스텀 이벤트별로 사용자를 세분화할 때 사용할 수 있는 필터를 보여줍니다.

| 세분화 옵션 | 드롭다운 필터 | 입력 옵션 |
| ---------------------| --------------- | ------------- |
| 커스텀 이벤트가 **X회 이상** 발생했는지 확인 | **MORE THAN** | **NUMBER** |
| 커스텀 이벤트가 **X회 미만** 발생했는지 확인 | **LESS THAN** | **NUMBER** |
| 커스텀 이벤트가 **정확히 X회** 발생했는지 확인 | **EXACTLY** | **NUMBER** |
| 커스텀 이벤트가 마지막으로 **X 날짜 이후**에 발생했는지 확인 | **AFTER** | **TIME** |
| 커스텀 이벤트가 마지막으로 **X 날짜 이전**에 발생했는지 확인 | **BEFORE** | **TIME** |
| 커스텀 이벤트가 마지막으로 **X일 이상 전**에 발생했는지 확인 | **MORE THAN** | **NUMBER OF DAYS AGO** (양수) |
| 커스텀 이벤트가 마지막으로 **X일 미만 전**에 발생했는지 확인 | **LESS THAN** | **NUMBER OF DAYS AGO** (양수) |
| 커스텀 이벤트가 **X회(최대 = 50) 이상** 발생했는지 확인 | **MORE THAN** | 지난 **Y일(Y = 1,3,7,14,21,30)** 동안 |
| 커스텀 이벤트가 **X회(최대 = 50) 미만** 발생했는지 확인 | **LESS THAN** | 지난 **Y일(Y = 1,3,7,14,21,30)** 동안 |
| 커스텀 이벤트가 **정확히 X회(최대 = 50)** 발생했는지 확인 | **EXACTLY** | 지난 **Y일(Y = 1,3,7,14,21,30)** 동안 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="세분화 필터" }

## 분석 {#analytics}

Braze는 커스텀 이벤트가 발생한 횟수와 각 사용자가 마지막으로 수행한 시점을 기록하여 세분화에 활용합니다. 보고서 설정, 필터 및 내보내기 옵션에 대해서는 [커스텀 이벤트 보고서]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report)를 참조하세요.

**커스텀 이벤트 보고서** 페이지에서 각 커스텀 이벤트가 발생하는 빈도를 집계하여 확인할 수 있습니다. 시계열에 겹쳐진 회색 선은 Campaign이 마지막으로 전송된 시점을 나타내며, Campaign이 커스텀 이벤트 활동에 미친 영향을 확인하는 데 유용합니다.

![대시보드의 커스텀 이벤트 페이지에서 커스텀 이벤트의 추세를 보여주는 커스텀 이벤트 횟수 그래프]({% image_buster /assets/img_archive/custom_event_analytics_example.png %} "custom_event_analytics_example.png")

**필터**를 사용하여 시간별, 월간 활성 사용자(MAU), Segments 또는 KPI or 핵심 성과 지표(KPI) or KPI or 핵심 성과 지표(KPI) or KPI or 핵심 성과 지표(KPI) or KPI or 핵심 성과 지표(KPI) or 핵심 성과 지표(KPI or 핵심 성과 지표(KPI)) 수식별로 커스텀 이벤트를 분류할 수도 있습니다.

![커스텀 이벤트 그래프 필터]({% image_buster /assets/img/custom_events_report_filters.png %}){: style="max-width:40%;"}

{% alert tip %}
[증분 커스텀 속성]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types#custom-attribute-data-types)을 사용하여 커스텀 이벤트와 유사한 사용자 행동에 대한 카운터를 유지할 수 있습니다. 하지만 커스텀 속성 데이터는 시계열로 확인할 수 없습니다. 시계열로 분석할 필요가 없는 사용자 행동은 이 방법을 사용하여 기록해야 합니다.
{% endalert %}

### 커스텀 이벤트 분석이 표시되지 않는 이유 {#why-custom-events-analytics-arent-showing}

커스텀 이벤트 데이터로 생성된 Segments는 생성되기 이전의 과거 이력 데이터를 표시할 수 없습니다.

## 커스텀 이벤트 속성정보 {#custom-event-properties}

커스텀 이벤트 속성정보는 이벤트의 특정 발생을 설명하는 커스텀 이벤트 메타데이터 또는 속성입니다. 이러한 속성정보는 트리거 조건을 더 세밀하게 설정하고, 메시징에서 개인화를 강화하며, 전환을 추적하고, 원시 데이터 내보내기를 통해 더 정교한 분석을 생성하는 데 사용할 수 있습니다.

자세한 내용은 [커스텀 이벤트 속성정보]({{site.baseurl}}/user_guide/data/activation/events/custom_events/custom_event_properties)를 참조하세요.