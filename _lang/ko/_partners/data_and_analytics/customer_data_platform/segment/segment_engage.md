---
nav_title: Segment Engage
article_title: Segment Engage
page_order: 3
alias: /partners/segment_personas/
alias: /partners/segment_engage/
alias: /partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_personas/

description: "이 참조 문서에서는 마케팅 스택의 소스 간에 정보를 수집하고 라우팅하는 고객 데이터 플랫폼인 Segment와 Braze 간의 파트너십에 대해 설명합니다."
page_type: partner
search_tag: Partner

---

# Segment Engage

> [Segment](https://segment.com)는 고객 데이터를 수집, 정리 및 활성화하는 데 도움이 되는 고객 데이터 플랫폼입니다. 이 참조 문서에서는 [Braze와 Segment Engage](https://segment.com/docs/destinations/braze/#Engage) 간의 연결에 대한 개요와 올바른 구현 및 사용을 위한 요구 사항 및 프로세스를 설명합니다.

Braze와 Segment 통합을 사용하면 Segment의 내장 오디언스 빌더인 [Engage](https://segment.com/docs/engage/)를 사용하여 다양한 소스에서 이미 수집한 데이터를 기반으로 사용자 세그먼트를 생성할 수 있습니다. 이러한 오디언스는 코호트로 Braze에 동기화되거나, [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/) 또는 [커스텀 이벤트]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events)를 통해 고객 프로필에 표시되며, 이를 사용하여 Campaign 및 Canvas 리타겟팅에 사용할 Braze 세그먼트를 생성할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Segment 계정 | 이 파트너십을 활용하려면 [Segment 계정](https://app.segment.com/login)이 필요합니다. |
| Braze 클라우드 대상 | Segment 통합에서 이미 [Braze를 대상으로 설정]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/)해야 합니다.<br><br>여기에는 [연결 설정]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings)에서 올바른 Braze 데이터 센터와 REST API 키를 제공하는 것이 포함됩니다. |
| Braze 데이터 가져오기 키 | Engage 오디언스를 코호트로 Braze에 동기화하려면 데이터 가져오기 키를 생성해야 합니다.<br><br>코호트 가져오기는 얼리 액세스 중이며, 이 기능에 액세스하려면 Braze 고객 성공 매니저에게 문의하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 코호트 대상 통합 {#cohorts-destination-integration}

### 1단계: Engage 오디언스 생성 {#step-1-create-an-engage-audience}
1. Segment에서 Engage의 **Audiences** 탭으로 이동하고 **New**를 클릭합니다.
2. 오디언스를 생성합니다. 페이지 상단 모서리의 번개 아이콘은 오디언스가 실시간으로 업데이트되는지 여부를 나타냅니다.
3. 다음으로, Braze를 대상으로 선택합니다.
4. **Review & Create**를 클릭하여 오디언스를 미리 봅니다. 기본적으로 Segment는 모든 과거 데이터를 쿼리하여 계산된 특성 및 오디언스의 현재 값을 설정합니다. 이 데이터를 생략하려면 **Historical Backfill**을 선택 해제합니다.

### 2단계: 코호트 데이터 가져오기 키 캡처 {#step-2-capture-your-cohort-data-import-key}

Braze에서 **파트너 통합** > **기술 파트너**로 이동하고 **Segment**를 선택합니다.

여기에서 REST 엔드포인트를 확인하고 Braze 데이터 가져오기 키를 생성할 수 있습니다. 키가 생성되면 새 키를 만들거나 기존 키를 무효화할 수 있습니다.

### 3단계: Braze 코호트 대상 연결 {#step-3-connect-the-braze-cohorts-destination}
[Segment의 지침](https://segment.com/docs/connections/destinations/catalog/actions-braze-cohorts/#getting-started)에 따라 코호트 대상을 설정하여 Engage 오디언스를 코호트로 Braze에 동기화합니다.

### 4단계: Engage 오디언스에서 Braze 세그먼트 생성 {#step-4-create-a-braze-segment-from-the-engage-audience}
Braze에서 **Segments**로 이동하여 새 세그먼트를 생성하고 필터로 **Segment Cohorts**를 선택합니다. 여기에서 포함할 Segment 코호트를 선택할 수 있습니다. Segment 코호트 세그먼트가 생성되면 Campaign 또는 Canvas를 생성할 때 오디언스 필터로 선택할 수 있습니다.

![]({% image_buster /assets/img/segment/segment3.png %})

## 클라우드 모드 통합 {#cloud-mode-integration}

### 1단계: Segment 계산된 특성 또는 오디언스 생성 {#step-1-create-a-segment-computed-trait-or-audience}

1. Segment에서 **Engage**의 **Computed Traits** 또는 **Audiences** 탭으로 이동하고 **New**를 클릭합니다.
2. 계산된 특성 또는 오디언스를 생성합니다. 페이지 상단 모서리의 번개 아이콘은 계산이 실시간으로 업데이트되는지 여부를 나타냅니다.
3. 다음으로, **Braze**를 대상으로 선택합니다.
4. **Review & Create**를 클릭하여 오디언스를 미리 봅니다. 기본적으로 Segment는 모든 과거 데이터를 쿼리하여 계산된 특성 및 오디언스의 현재 값을 설정합니다. 이 데이터를 생략하려면 **Historical Backfill**을 선택 해제합니다.
5. 계산된 특성 또는 오디언스 설정에서 데이터를 Braze로 전송하는 방식에 따라 연결 설정을 조정합니다.

#### 계산된 특성 및 오디언스 {#computed-traits-and-audiences}

[계산된 특성](https://segment.com/docs/engage/audiences/computed-traits/) 및 [오디언스](https://segment.com/docs/Engage/audiences/)는 커스텀 속성 또는 커스텀 이벤트로 Braze에 전송할 수 있습니다.
- `identify` 호출을 사용하여 전송된 특성 및 오디언스는 Braze에서 커스텀 속성으로 표시됩니다.
- `track` 호출을 사용하여 전송된 특성 및 오디언스는 Braze에서 커스텀 이벤트로 표시됩니다.

계산된 특성을 Braze 대상에 연결할 때 사용할 메서드를 선택할 수 있습니다(또는 두 가지 모두 사용하도록 선택할 수 있습니다).

{% tabs %}
{% tab Identify %}

계산된 특성 및 오디언스를 `identify` 호출로 Braze에 전송하여 Braze에서 커스텀 속성을 생성할 수 있습니다.

예를 들어, "Last Product Viewed Item"에 대한 Engage 계산된 특성이 있는 경우 사용자의 Braze 프로필에서 **커스텀 속성** 아래에 `last_product_viewed_item`이 표시됩니다. 이것이 Engage 오디언스인 경우에는 **커스텀 속성** 아래에 `true`로 설정된 오디언스가 표시됩니다.

| 계산된 특성 | 오디언스 |
| -------------- | --------- |
| ![고객 프로필 내의 커스텀 속성 섹션에 "last_product_viewed_item"이 "Sweater"로 표시됩니다.]({% image_buster /assets/img/segment/last_viewed-id-braze.png %}) | ![고객 프로필 내의 커스텀 속성 섹션에 "dormant_shopper"가 "true"로 표시됩니다.]({% image_buster /assets/img/segment/dormant-identify-braze.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Computed traits and audiences" }

{% endtab %}
{% tab Track %}

계산된 특성 및 오디언스를 `track` 호출로 Braze에 전송하여 Braze에서 커스텀 이벤트를 생성할 수 있습니다.

이전 예시를 계속하면, 사용자에게 "Last Product Viewed Item"에 대한 계산된 특성이 있는 경우 사용자의 Braze 프로필에서 **커스텀 이벤트** 아래에 해당 횟수 및 가장 최근 타임스탬프와 함께 `Trait Computed`로 표시됩니다. 이것이 Engage 오디언스인 경우에는 **커스텀 속성** 아래에 `true`로 설정된 오디언스, 횟수 및 가장 최근 타임스탬프가 표시됩니다.

| 계산된 특성 | 오디언스 |
| -------------- | --------- |
| ![고객 프로필 내 커스텀 이벤트 섹션에 "Trait Computed"가 "1"회로 표시되며, 마지막 시간은 "20시간 전"입니다.]({% image_buster /assets/img/segment/last_viewed-track-braze.png %}) | ![고객 프로필 내의 커스텀 속성 섹션에 "Audience Entered"가 "1"회로 표시되며, 마지막 시간은 "3월 9일 오전 1시 45분"입니다.]({% image_buster /assets/img/segment/dormant-track-braze.png %}) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Computed traits and audiences" }

{% endtab %}
{% endtabs %}

### 2단계: Braze에서 사용자 세그먼트 생성 {#step-2-segment-users-in-braze}

Braze에서 이러한 사용자의 세그먼트를 생성하려면 **참여** 아래의 **Segments**로 이동하여 새 세그먼트를 생성하고 이름을 지정합니다. 다음으로, 사용한 호출에 따라:
- **Identify**: 필터로 **커스텀 속성**을 선택하고 커스텀 속성을 찾습니다. 그런 다음 "정규식 일치" 옵션(특성) 또는 "같음" 옵션(오디언스)을 사용하고 적절한 변수를 입력합니다.
- **Track**: 필터로 **커스텀 이벤트**를 선택하고 커스텀 이벤트를 찾습니다. 그런 다음 "초과", "미만" 또는 "정확히" 옵션을 사용하고 원하는 값을 입력합니다. 이는 세그먼트를 정의하는 방식에 따라 달라집니다.

저장하면 타겟 사용자 단계에서 Canvas 또는 Campaign 생성 시 이 세그먼트를 참조할 수 있습니다.

## 동기화 시간 {#sync-time}

Braze와 Segment Engage 연결의 기본 설정은 `Realtime`이지만, 메시지 전송 시점에 오디언스 크기를 제한하는 일부 시간 기반 필터를 포함하여 실시간 동기화에서 페르소나를 제외하는 일부 필터가 있습니다.

## Segment 디버거 테스트 {#segment-debugger-testing}

Segment의 대시보드는 고객이 "소스"의 데이터가 예상대로 "대상"으로 전송되는지 테스트할 수 있는 "디버거" 기능을 제공합니다.

이 기능은 Braze [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)에 연결되므로, 식별된 사용자(Braze 고객 프로필에 대한 사용자 ID가 이미 있는 사용자)에게만 사용할 수 있습니다.

이 기능은 사이드 바이 사이드 Braze 통합에서는 작동하지 않습니다. 올바른 Braze REST API 정보를 입력하지 않으면 서버 데이터가 전달되지 않습니다.