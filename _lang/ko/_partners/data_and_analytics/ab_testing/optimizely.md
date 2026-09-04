---
nav_title: Optimizely
article_title: Optimizely
page_order: 2
description: "이 참조 문서에서는 Braze 고객 Segments, 이벤트 및 Currents 이벤트를 Optimizely Data Platform에 동기화할 수 있는 Braze와 Optimizely 간의 파트너십에 대해 설명합니다."
alias: /partners/optimizely/
page_type: partner
search_tag: Partner
---

# Optimizely

> [Optimizely](https://www.optimizely.com/)는 디지털 제품 및 마케팅 Campaign을 위한 실험 및 콘텐츠 관리 도구를 제공하는 선도적인 디지털 경험 플랫폼입니다.

Braze와 Optimizely 통합은 양방향 통합으로, 다음을 수행할 수 있습니다:

{% multi_lang_include partners/ab_testing/optimizely_integration_bullets.md %}

## 사전 요구 사항 {#prerequisites}

| 요구 사항                     | 설명 |
|----------------------------------|-------------|
| Optimizely Data Platform 계정 | 이 파트너십을 활용하려면 Optimizely Data Platform(ODP) 계정이 필요합니다. |
| Braze REST API 키               | 다음 권한이 있는 Braze REST API 키: `users.track`, `users.export.segments`, `segments.list`, `campaigns.trigger.send`, `canvas.trigger.send`. |
| Currents                         | 데이터를 Optimizely로 다시 내보내려면 계정에 Braze 커런츠가 설정되어 있어야 합니다. |
| Optimizely URL 및 토큰         | Optimizely 대시보드로 이동하여 수집 URL과 토큰을 복사하면 얻을 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사전 요구 사항" }

## 통합 {#integration}

### 1단계: 통합 구성 {#step-1-configure-the-integration}

1. Optimizely Data Platform(ODP)의 **App Directory**에서 **Braze** 앱을 선택한 다음 **Install App**을 선택합니다.
2. **Settings** 탭으로 이동합니다. **Authorization** 섹션에서 다음을 수행합니다:
    1. Braze **REST API 키**를 입력합니다.
    2. Braze **인스턴스 URL**을 선택합니다.
    2. **Verify API Key**를 선택합니다.
3. Braze에서 **[Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents)**로 이동합니다.
4. **Create New Current** > **Custom Currents Export**를 선택합니다.
5. ODP에서 제공하는 엔드포인트와 토큰을 사용하여 Current를 구성합니다. 이는 Braze 이벤트를 ODP에 동기화하는 데 필요합니다.

![Optimizely 인증 설정 화면.]({% image_buster /assets/img/optimizely/image1_authorization.png %})

{:start="6"}
6. ODP에서 **Segments** 섹션을 확장하고 **Segments to Sync** 목록에서 특정 Segments를 선택하거나, **Import All Customers**를 선택하여 모든 Segments를 동기화합니다.
7. Braze와 ODP 간에 원하는 [추가 필드 매핑](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/29918568615949-Integrate-Braze%23h_01J6Z1P53JVDBFZ758Q78CK1QB&sa=D&source=editors&ust=1733948158380300&usg=AOvVaw3WSAND5ie3LCVuSxUlLanR)을 추가합니다.
8. **Save**를 선택합니다.

![Optimizely Braze Segment 동기화 화면.]({% image_buster /assets/img/optimizely/image2_syncsegment.png %})

{% alert tip %}
고객 프로필을 가져오려면 Segments를 선택해야 합니다. Segments를 선택하지 않으면 통합에서 고객 프로필을 가져오지 않습니다.
{% endalert %}

### 2단계: 데이터 필드 매핑 {#step-2-map-data-fields}

통합에는 Braze와 ODP 간의 기본 데이터 필드 매핑이 포함되어 있습니다. 예를 들어, Braze의 **Email** 필드는 ODP의 **Last Seen Email** 필드에 매핑됩니다.

![Optimizely와 Braze Segment 필드 매핑 화면.]({% image_buster /assets/img/optimizely/image3_emailmapfield.png %})

#### 추가 필드 매핑(선택 사항) {#map-additional-fields-optional}

Braze에 ODP로 매핑하려는 추가 데이터 필드가 있는 경우, ODP에서 다음을 수행합니다:

1. 앱의 **Segments** 섹션에서 **Braze User Data Fields** 드롭다운 목록에서 Braze 필드를 선택합니다.
2. **ODP Customer Fields** 드롭다운 목록에서 ODP 필드를 선택합니다.
3. **Save Field Map**을 선택합니다.

![Optimizely Braze Segment 필드 매핑 저장 화면]({% image_buster /assets/img/optimizely/image4_mapfields.png %})

#### 불필요한 필드 매핑 삭제(선택 사항) {#delete-non-required-field-mappings-optional}

필요하지 않은 데이터 필드 매핑을 삭제할 수도 있습니다. ODP에서 다음을 수행합니다:

1. 앱의 **Segments** 섹션에서 **Field Map** 드롭다운 목록에서 삭제하려는 필드 매핑을 선택합니다.
2. **Delete Field Map**을 선택합니다.

![Optimizely Braze Segment 필드 매핑 삭제 화면]({% image_buster /assets/img/optimizely/image5_deletephonefield.png %})

### 3단계: Optimizely Data Platform(ODP)에서 Braze로 데이터 동기화 {#step-3-sync-data-from-optimizely-data-platform-odp-to-braze}

통합을 구성한 후, ODP에서 활성화를 설정하여 ODP 고객 데이터를 Braze로 동기화할 수 있습니다.

1. **Activation** > **Engage**로 이동하고 **Create New Campaign**을 선택합니다.
2. **Behavioral**을 선택하여 자동화된 반복 동기화를 설정합니다.
3. **Create From Scratch**를 선택한 다음, Braze로 동기화하는 데이터를 나타내는 활성화 이름을 입력합니다(예: **Braze Data Sync**).
4. **Enrollment** 섹션에서 Segment에 일치하는 고객의 데이터를 동기화하거나, 이벤트를 트리거하는 고객의 데이터를 동기화할 수 있습니다(예: ODP에서 고객이 이메일을 열람한 것을 감지한 경우):
   - **Segment에 일치하는 고객:** 원하는 Segment를 선택한 다음 **Next**를 선택합니다.<br><br>![Optimizely Segment 선택 화면]({% image_buster /assets/img/optimizely/image6_segment.png %})
   - **이벤트를 트리거하는 고객:** **Filter** 드롭다운 목록을 확장하고 이 데이터 동기화의 트리거로 사용할 ODP 이벤트를 선택합니다. 그런 다음 **Automation Rules**를 확장하고 필요에 따라 조정합니다. <br><br>![Optimizely 트리거 이벤트 화면]({% image_buster /assets/img/optimizely/image7_trigger.png %})
5. **Touchpoints**를 확장하고 **Touchpoint 1**을 편집하도록 선택한 다음 **Braze**를 선택합니다.
6. **Targeting** 섹션을 확장한 다음 **Target Identifier**를 선택합니다.
7. **Configure** 섹션에서 **Add Users To**에 대해 다음 옵션 중 하나를 선택합니다:
    - **Campaign:** Braze의 특정 Campaign에 고객을 추가합니다. 이 옵션을 선택한 후 Braze Campaign을 선택해야 합니다.
    - **Canvas:** Braze의 특정 Canvas에 고객을 추가합니다. 이 옵션을 선택한 후 BRAZE 캔버스를 선택해야 합니다.
    - **Profile Update Only:** Braze 고객 프로필만 업데이트합니다.
8. (선택 사항) Braze로 동기화할 **Number of Additional Fields**(최대 20개)를 선택합니다.
    그런 다음 각 추가 필드의 드롭다운 목록과 입력 필드에 대해 다음을 선택합니다:
    - 각 **Field #** 드롭다운 목록에서 채우려는 Braze 필드를 선택합니다.
    - 각 해당 **Field # Value**에 선택한 Braze 필드로 보내려는 ODP 필드를 입력합니다. 예를 들어, **Field #** 드롭다운 목록에서 **Company Name**을 선택한 경우, 해당 **Field # Value**에 `{{customer.company_name}}`을 입력합니다.
9. **Save**를 선택한 다음, 이동 경로에서 활성화 이름을 선택합니다.
10. 등록에서 **Segment에 일치하는 고객**을 선택한 경우, **Touchpoints** 섹션에서 **Select start time and schedule**을 선택합니다.
11. 다음 설정을 완료합니다:
    - **Recurring or Continuous:** **Recurring**을 선택합니다.
    - **Start Date:** Braze로 데이터를 보내려는 날짜를 입력합니다.
    - **End:** 기본값은 **Never**입니다. 특정 날짜에 Braze 데이터 동기화를 종료하려면 여기에서 설정합니다.
    - **Repeats:** **Daily**로 설정합니다.
    - **Repeat Every:** **1 day**로 설정합니다.
    - **Timing:** Braze로 데이터를 보내려는 시간을 입력합니다.
    - **Time Zone:** 이 데이터를 보내려는 시간대를 선택합니다.
12. **Apply**, **Save**, 그리고 **Go Live**를 선택합니다. 동기화는 지정한 시작 날짜 및 시간에 시작됩니다(또는 트리거 이벤트가 발생할 때 시작됩니다).

## 문제 해결 {#troubleshooting}

### 이벤트 검사 {#inspect-events}

ODP에서 Braze로 데이터가 올바르게 동기화되고 있는지 확인하려면 ODP에서 이벤트를 검사할 수 있습니다.

1. ODP에서 **Account Settings** > **Event Inspector**로 이동합니다.
2. **Start Inspector**를 선택합니다.
3. 인스펙터에서 데이터를 사용할 수 있으면 **Refresh** 옆에 숫자가 표시됩니다. 선택하여 데이터를 확인합니다.
4. ODP와 Braze가 주고받는 원시 데이터가 표시됩니다. **View Details**를 선택하면 해당 원시 데이터의 포맷된 버전을 확인할 수 있습니다.
5. Braze에서 ODP로 다시 전송된 데이터 필드는 `_braze`로 시작합니다.

### 활동 로그 확인 {#check-activity-logs}

각 데이터 동기화는 [ODP 활동 로그](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/4407268804365-Use-the-Activity-Log&sa=D&source=editors&ust=1733948158385124&usg=AOvVaw2tMOxzcTKfL0-oYLT4IMpP)에도 기록됩니다.

1. **Account Settings** > **Activity Log**로 이동합니다.
2. 카테고리를 **braze**로 필터링합니다.
3. **View Details**를 선택하면 일치 항목 수를 포함한 로그 세부 정보의 포맷된 보기를 확인할 수 있습니다.