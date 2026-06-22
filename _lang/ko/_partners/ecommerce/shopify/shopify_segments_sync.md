---
nav_title: Shopify Segments 동기화
article_title: Shopify Segments 동기화
alias: /shopify_segments_sync/
page_order: 8
description: "이 참조 문서에서는 통합 오디언스 관리 및 타겟팅을 위해 Shopify Segments를 코호트로 Braze에 동기화하는 방법을 설명합니다."
---

# Shopify Segments 동기화 {#shopify-segments-sync}

> Shopify Segments 동기화는 Shopify 스토어를 Braze로 확장하여, 마케팅 팀이 표준 Braze Shopify 통합으로는 캡처되지 않는 신호를 포함해 Shopify에 있는 더 풍부한 사용자 데이터에 직접 접근할 수 있도록 합니다. Shopify Segments를 코호트로 동기화하면 두 플랫폼 간에 오디언스 정의를 일치시키고, 사용자가 Shopify에서 타겟팅되든 Braze Campaign을 통해 참여하든 일관되고 조율된 사용자 경험을 제공할 수 있습니다.

{% alert important %}
Shopify Segments 동기화는 현재 베타 버전입니다. 액세스를 요청하려면 고객 성공 매니저에게 문의하세요.
{% endalert %}

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| Braze Shopify 통합 | Braze Shopify 앱이 Shopify 스토어에 설치되어 있고 Braze 워크스페이스에 연결되어 있어야 합니다. 설정 안내는 [Shopify 표준 통합 설정]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/) 또는 [Shopify 커스텀 통합 설정]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/)을 참조하세요. |
| Shopify 사용자 권한 | Segment 동기화를 시작하는 Shopify 사용자는 고객 데이터를 내보내기 위한 **내보내기** 권한이 있어야 합니다. Shopify 권한에 대한 자세한 내용은 [Shopify 스토어 권한 설명서](https://help.shopify.com/en/manual/your-account/users/roles/permissions/store-permissions#customers-permissions)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 작동 방식 {#how-it-works}

Shopify Segments 동기화는 두 단계로 작동합니다.

1. Segment를 처음 동기화하면 Braze가 현재 모든 멤버를 백필하고 Braze에 해당 코호트를 생성합니다. 백필은 비동기적으로 실행되며 완료까지 잠시 시간이 걸릴 수 있습니다.
2. 초기 동기화 중에 Braze는 현재 멤버를 백필하고 Shopify 웹훅을 구독하여 멤버십이 거의 실시간으로 동기화된 상태를 유지합니다.

| 웹훅 토픽 | Braze에서의 효과 |
| --- | --- |
| `customer.joined_segment` | 사용자가 해당 Braze 코호트에 추가됩니다. |
| `customer.left_segment` | 사용자가 해당 Braze 코호트에서 제거됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="웹훅 토픽" }

동기화가 실패하면 액션 확장 모달에 권장 조치와 함께 오류 배너가 표시됩니다. **Sync with Braze**를 선택하여 재시도하세요.

## 데이터 가져오기 통합 {#data-import-integration}

### 1단계: 동기화할 Shopify Segment 선택 {#step-1-select-a-shopify-segment-to-sync}

Shopify에서 **Customers** > **Segments**로 이동하여 Braze에 동기화할 Segment를 선택합니다. 주문 내역, 제품 구매, 고객 태그, 생애 지출, 메타필드를 기반으로 한 Segment를 포함하여 Shopify의 네이티브 세분화를 사용해 구축한 모든 Segment를 동기화할 수 있습니다.

![Shopify Segments 목록이 있는 Segments 패널.]({% image_buster /assets/img/shopify/shopify_segments.png %})

### 2단계: 동기화 시작 {#step-2-initiate-the-sync}

1. Shopify의 Segment 상세 페이지에서 **Use segment** 드롭다운을 열고 **Braze Segment Sync**를 선택합니다.

!["Braze Segment Sync" 옵션이 있는 "Use segment" 드롭다운이 표시된 Segment 상세 페이지.]({% image_buster /assets/img/shopify/braze_segment_sync.png %})

{: start="2"}
2. Braze 액션 확장 모달이 열리면 Segment 이름과 오디언스 크기가 표시됩니다. **Sync with Braze**를 선택하여 가져오기를 시작합니다.

![Braze와 동기화 버튼이 있는 모달.]({% image_buster /assets/img/shopify/sync_with_braze.png %}){:style="max-width:70%;"}

{: start="3"}
3. **Done**을 선택합니다.

![동기화가 활성 상태임을 확인하는 모달.]({% image_buster /assets/img/shopify/braze_sync_active.png %}){:style="max-width:70%;"}

### 3단계: 코호트 멤버십 필터로 Braze Segment 생성 {#step-3-create-a-braze-segment-with-the-cohort-membership-filter}

Braze에서 **Audience** > **Segments**로 이동하여 새 Segment를 생성합니다. **Add Filter**에서 **Cohort Membership** 필터를 선택하고 드롭다운에서 동기화된 Shopify Segment를 선택합니다. 저장한 후 Campaign 또는 Canvas에서 사용자를 타겟팅할 때 이 Braze Segment를 참조할 수 있습니다.

!["Shopify Cohorts" 필터가 있는 Segment 빌더.]({% image_buster /assets/img/shopify/segment_builder_cohort_import.png %})

## 사용자 매칭 {#user-matching}

Shopify Segments에서 동기화된 사용자는 Braze Shopify 통합의 일부로 설정된 `shopify_customer_id` 별칭을 사용하여 Braze 고객 프로필과 매칭됩니다. 매칭되는 Braze 고객 프로필이 없는 사용자는 동기화 중에 건너뜁니다.

Shopify 통합이 사용자를 식별하고 별칭을 지정하는 방법에 대한 자세한 내용은 [Shopify 데이터 기능]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/)을 참조하세요.

## 제한 사항 {#limitations}

- **단방향 동기화.** Segment 멤버십은 Shopify에서 Braze로만 전달됩니다. Braze에서 직접 변경한 코호트 멤버십은 Shopify로 다시 푸시되지 않습니다.
- **프로필 생성 불가.** 이미 Braze 고객 프로필이 있는 Shopify 고객만 코호트에 추가됩니다.
- **동기화 취소 불가.** Shopify Segment가 동기화되면 취소할 수 없습니다.