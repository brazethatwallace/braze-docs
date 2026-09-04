---
nav_title: Shopify Segments 동기화
article_title: Shopify Segments 동기화
alias: /shopify_segments_sync/
page_order: 8
description: "이 참조 문서에서는 통합 오디언스 관리 및 타겟팅을 위해 Shopify Segments를 코호트로 Braze에 동기화하는 방법을 설명합니다."
---

# Shopify Segments 동기화 {#shopify-segments-sync}

> Shopify Segments 동기화는 Shopify 스토어를 Braze로 확장하여, 마케팅 팀이 표준 Braze Shopify 통합으로는 캡처되지 않는 신호를 포함해 Shopify에 있는 더 풍부한 사용자 데이터에 직접 접근할 수 있도록 합니다. Shopify Segments를 코호트로 동기화하면 두 플랫폼 간에 오디언스 정의를 일치시키고, 사용자가 Shopify에서 타겟팅되든 Braze Campaign을 통해 도달하든 일관되고 조율된 사용자 경험을 제공할 수 있습니다.

{% alert important %}
Shopify Segments 동기화는 현재 베타 버전입니다. 액세스를 요청하려면 고객 성공 매니저에게 문의하세요.
{% endalert %}

## 사전 요구 사항 {#prerequisites}

| 요구 사항 | 설명 |
| --- | --- |
| Braze Shopify 통합 | Braze Shopify 앱이 Shopify 스토어에 설치되어 있고 Braze 워크스페이스에 연결되어 있어야 합니다. 설정 방법은 [Shopify 표준 통합 설정]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) 또는 [Shopify 커스텀 통합 설정]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration)을 참조하세요. |
| Shopify 사용자 권한 | Segment 동기화를 시작하는 Shopify 사용자는 사용자 데이터를 내보내기 위한 **Export** 권한이 있어야 합니다. Shopify 권한에 대한 자세한 내용은 [Shopify 스토어 권한 설명서](https://help.shopify.com/en/manual/your-account/users/roles/permissions/store-permissions#customers-permissions)를 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사전 요구 사항" }

## 작동 방식 {#how-it-works}

Shopify Segments 동기화는 두 단계로 작동합니다.

1. **초기 백필:** Segment를 처음 동기화하면 Braze가 모든 현재 구성원을 백필하고 Braze에 해당 코호트를 생성합니다. 백필은 비동기적으로 실행되며 완료까지 몇 분 정도 걸릴 수 있습니다.
2. **지속적 동기화:** 초기 백필 후 Braze는 Shopify 웹훅도 구독하여 구성원 상태가 거의 실시간으로 동기화됩니다.

| 웹훅 토픽 | Braze에서의 효과 |
| --- | --- |
| `customer.joined_segment` | 해당 사용자가 대응하는 Braze 코호트에 추가됩니다. |
| `customer.left_segment` | 해당 사용자가 대응하는 Braze 코호트에서 제거됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="웹훅 토픽" }

동기화에 실패하면 액션 확장 Modal에 오류 배너가 표시되어 발생한 문제와 조치 방법을 안내합니다. 일부 오류는 **동기화 재시도** 액션을 제공합니다. 그 외의 오류는 관리자 또는 설정 변경이 필요합니다.

## 데이터 가져오기 통합 {#data-import-integration}

### 1단계: 동기화할 Shopify 세그먼트 선택 {#step-1-select-a-shopify-segment-to-sync}

Shopify에서 **Customers** > **Segments**로 이동하여 Braze에 동기화할 세그먼트를 선택합니다. 주문 내역, 제품 구매, 고객 태그, 생애 지출, 메타필드 기반 세그먼트를 포함하여 Shopify의 기본 세분화를 사용해 구축한 모든 세그먼트를 동기화할 수 있습니다.

![Shopify 세그먼트 목록이 표시된 세그먼트 패널.]({% image_buster /assets/img/shopify/shopify_segments.png %})

### 2단계: 동기화 시작 {#step-2-initiate-the-sync}

1. Shopify의 세그먼트 상세 페이지에서 **Use segment** 드롭다운을 열고 **Braze Segment Sync**를 선택합니다.

![Use segment 드롭다운에 Braze Segment Sync 옵션이 표시된 세그먼트 상세 페이지.]({% image_buster /assets/img/shopify/braze_segment_sync.png %})

{: start="2"}
2. Braze 액션 확장 모달이 열리며 세그먼트 이름과 오디언스 크기가 표시됩니다. **Sync with Braze**를 선택하여 가져오기를 시작합니다.

![Braze와 동기화하기 위한 버튼이 있는 모달.]({% image_buster /assets/img/shopify/sync_with_braze.png %}){:style="max-width:70%;"}

{: start="3"}
3. 모달이 동기화 중 상태로 전환되며 Braze가 멤버를 가져오는 동안 진행 배너가 표시됩니다.

![동기화가 진행 중임을 보여주는 모달.]({% image_buster /assets/img/shopify/sync_in_progress.png %}){:style="max-width:70%;"}

{: start="4"}
4. **Close**를 선택합니다. 동기화는 백그라운드에서 계속 진행됩니다. 모달을 닫아도 동기화가 중단되지 않습니다.

동기화가 완료되었는지 확인하려면 모달을 닫았다가 다시 여세요. 동기화가 완료되면 성공 배너와 함께 모달이 열립니다.

![동기화가 활성 상태임을 확인하는 모달.]({% image_buster /assets/img/shopify/braze_sync_active.png %}){:style="max-width:70%;"}

### 3단계: 코호트 멤버십 필터로 Braze Segment 생성 {#step-3-create-a-braze-segment-with-the-cohort-membership-filter}

Braze에서 **오디언스** > **Segments**로 이동하여 새 Segment를 생성합니다. **필터 추가**에서 **코호트 멤버십** 필터를 선택한 다음 드롭다운에서 동기화된 Shopify 세그먼트를 선택합니다. 저장 후, Campaign 또는 Canvas에서 사용자를 타겟팅할 때 이 Braze Segment를 참조할 수 있습니다.

![Shopify 코호트 필터가 적용된 Segment 빌더.]({% image_buster /assets/img/shopify/segment_builder_cohort_import.png %})

## Segment 재동기화 {#re-syncing-a-segment}

Segment가 동기화된 후에는 동일한 작업 확장에서 언제든지 코호트 멤버십을 새로고침할 수 있습니다.

1. Shopify에서 동기화된 Segment를 열고 **Use segment** > **Braze Segment Sync**를 선택합니다.
2. Modal에서 **Sync now**를 선택합니다.
3. 확인 대화 상자에서 **Sync now**를 선택하여 재동기화를 시작합니다.

재동기화는 누적 방식입니다. 현재 Shopify Segment와 일치하는 사용자는 코호트에 추가되지만, 더 이상 일치하지 않는 사용자는 코호트에 그대로 남아 있습니다.

## Braze에서 동기화된 Segments 관리 {#managing-synced-segments-in-braze}

Braze 대시보드에서 동기화된 모든 Segment를 관리할 수 있습니다. **파트너 통합** > **기술 파트너**로 이동하여 Shopify 통합을 선택한 다음 **사용자 관리** 탭을 엽니다.

### 동기화 상태 {#sync-status}

동기화된 모든 Segment에는 동기화 상태가 있습니다.

| 상태 | 설명 |
| --- | --- |
| **동기화 중** | Braze가 Segment 멤버를 가져오고 있습니다. |
| **대기 중** | Segment가 동기화 슬롯이 열릴 때까지 대기 중입니다. |
| **활성** | Segment가 동기화되었으며 멤버십이 거의 실시간으로 업데이트됩니다. |
| **일시중지** | 이 Segment의 멤버십 업데이트가 일시중지되었습니다. |
| **Error** | 마지막 동기화 시도가 실패했습니다. **Retry sync**를 선택하여 다시 시도하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="동기화 상태" }

### 대량 Segments 동기화 {#syncing-segments-in-bulk}

추가 Segments를 동기화하려면 통합을 편집하고, **사용자 관리** 단계로 이동한 다음 **Sync segments** 섹션에서 **Edit segments**를 선택합니다. 선택 Modal에서:

- 원하는 수의 Segments를 선택할 수 있습니다. 한 번에 25개의 Segments가 동기화되며, 나머지는 자동으로 대기줄에 추가됩니다.
- 이미 동기화 중인 Segments는 잠겨 있습니다. Segment를 제거하려면 Shopify에서 삭제하세요.

변경 사항을 저장하면 동기화가 시작됩니다.

### 단일 Segment 일시중지 {#pausing-a-single-segment}

하나의 Segment에 대한 동기화를 일시중지하려면 Segments 테이블의 해당 행에서 **Pause sync**를 선택하고 확인합니다. Segment 동기화가 일시중지되면:

- 코호트와 해당 멤버는 Braze에 유지되며 타겟팅이 가능합니다. 코호트를 사용하는 Campaigns 및 Canvases는 코호트의 현재 멤버에게 계속 전송됩니다.
- 멤버십 업데이트가 중단됩니다.
- Shopify에서 Segment 이름을 변경하면 코호트의 표시 이름도 업데이트됩니다.
- Shopify에서 Segment를 삭제하면 추적이 종료됩니다.
- Shopify 액션 확장 프로그램의 **Sync now** 요청은 거부됩니다.

다시 시작하려면 해당 행에서 **Resume sync**를 선택합니다. Braze가 멤버십 업데이트를 재개하고 보충 동기화를 실행합니다. 동기화가 일시중지된 동안 Shopify Segment를 떠난 사용자는 Braze 코호트에 그대로 남아 있습니다.

### 모든 Segment 동기화 일시중지 {#pausing-all-segment-syncing}

모든 Segments의 동기화를 한꺼번에 일시중지하려면 통합을 편집하고, **사용자 관리** 단계의 **Sync segments** 섹션에서 **Pause sync**를 선택한 다음 설정을 저장합니다. 모든 Segment 동기화가 일시중지된 동안:

- Segments 테이블에는 Segment 이름만 표시되며, 제목 옆에 **Paused** 상태가 나타납니다.
- 다시 시작할 때까지 행 수준 작업을 사용할 수 없습니다.
- Braze는 Shopify에서 이름을 변경해도 코호트 이름을 업데이트하지 않습니다. 다시 시작하면 코호트 이름이 새로고침됩니다.
- 액션 확장 프로그램의 **Sync now** 요청은 거부됩니다. 확장 프로그램은 각 Segment의 마지막으로 알려진 상태를 계속 표시하며, **Sync now**를 선택해도 동기화가 시작되지 않습니다.

다시 시작하려면 같은 섹션에서 **Resume sync**를 선택하고 저장합니다. Braze가 이전에 선택된 모든 Segments를 보충 동기화로 자동 재동기화합니다. 다시 선택할 필요가 없습니다. 개별적으로 일시중지한 Segments는 Segments 테이블의 해당 행에서 다시 시작할 때까지 일시중지 상태를 유지합니다.

## Shopify의 Segment 업데이트 {#segment-updates-in-shopify}

### Segment 이름 변경 {#renaming-a-segment}

Shopify segment의 이름을 변경하면, Braze가 대응하는 코호트의 표시 이름을 자동으로 업데이트합니다. 재동기화는 필요하지 않습니다. Braze는 segment의 동기화가 개별적으로 일시 중지된 동안에도 코호트 이름을 업데이트합니다. 모든 segment 동기화가 일시 중지된 경우, Braze는 동기화를 재개할 때 코호트 이름을 업데이트합니다.

### Segment 기준 변경 {#changing-segment-criteria}

Shopify segment의 기준을 변경해도 Braze는 코호트 멤버십을 자동으로 업데이트하지 않습니다. 새롭게 기준에 부합하는 사용자를 반영하려면, 작업 확장에서 segment를 재동기화하세요. 더 이상 기준에 부합하지 않는 사용자는 코호트에 그대로 남아 있습니다. 재동기화는 멤버를 제거하지 않기 때문입니다. 자세한 내용은 [Segment 재동기화](#re-syncing-a-segment)를 참조하세요.

## 사용자 매칭 {#user-matching}

Shopify Segments에서 동기화된 사용자는 Braze Shopify 통합의 일부로 설정된 `shopify_customer_id` 별칭을 사용하여 Braze 사용자 프로필과 매칭됩니다. 매칭되는 Braze 사용자 프로필이 없는 사용자는 동기화 중 건너뛰게 됩니다.

Shopify 통합이 사용자를 식별하고 별칭을 지정하는 방법에 대한 자세한 내용은 [Shopify 데이터 기능]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features)을 참조하세요.

Braze는 동기화된 사용자를 기존 Braze 사용자 프로필과 매칭합니다. 이때 해당 프로필이 어떻게 생성되었는지에 관계없이 매칭이 이루어지며, Shopify 과거 데이터 백필, 자체 데이터 플랫폼(예: Snowflake 또는 기타 데이터 웨어하우스), 직접 API 가져오기를 통해 생성된 프로필도 포함됩니다. 코호트가 Shopify Segment보다 작은 경우, 일부 Segment 구성원에게 아직 매칭되는 Braze 프로필이 없다는 의미입니다. 매칭 범위를 늘리려면 동기화 전에 선호하는 방법으로 Braze 사용자 프로필을 채워 넣으세요.

## 제한 사항 {#limitations}

- **단방향 동기화.** Segment 멤버십은 Shopify에서 Braze로만 전달됩니다. Braze에서 직접 변경한 코호트 멤버십은 Shopify로 다시 푸시되지 않습니다.
- **프로필 생성 불가.** Braze 사용자 프로필이 이미 있는 Shopify 고객만 코호트에 추가됩니다.
- **Braze에서 동기화를 중지할 수 없음.** Segment 동기화를 중지하려면 Shopify에서 해당 Segment를 삭제하세요. 코호트와 해당 멤버는 Braze에 그대로 유지되며 업데이트가 중지됩니다.
- **재동기화 시 멤버만 추가됨.** Segment를 재동기화하면 새로 일치하는 사용자가 코호트에 추가되지만, Shopify Segment에 더 이상 포함되지 않는 사용자는 제거되지 않습니다.