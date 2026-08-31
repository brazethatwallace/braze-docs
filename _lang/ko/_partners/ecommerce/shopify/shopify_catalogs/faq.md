---
nav_title: FAQ
article_title: Shopify 제품 동기화 FAQ
page_order: 0
page_type: FAQ
description: "이 페이지에서는 Shopify 제품을 Braze 카탈로그에 동기화하는 것에 대해 자주 묻는 질문에 대한 답변을 제공합니다."
---

# 자주 묻는 질문 {#frequently-asked-questions}

> 이 페이지에서는 [Shopify 제품 동기화]({{site.baseurl}}/shopify_catalogs)에 대해 자주 묻는 질문에 대한 답변을 제공합니다.

## 카탈로그 및 동기화 동작 {#catalog-and-sync-behavior}

### Braze에서 Shopify 카탈로그를 직접 편집할 수 있나요? {#can-i-edit-my-shopify-catalog-directly-in-braze}

아니요. Shopify 카탈로그는 Braze에서 읽기 전용입니다. 수동으로 편집한 내용은 다음 동기화 시 덮어쓰일 수 있습니다. 모든 제품 업데이트는 Shopify에서 직접 수행하세요.

### Shopify 카탈로그를 어떻게 삭제하나요? {#how-do-i-delete-my-shopify-catalog}

Shopify 카탈로그를 삭제하려면 Shopify 파트너 페이지에서 동기화를 비활성화하세요. **카탈로그** 페이지에서 직접 카탈로그를 삭제하지 마세요. 비활성화하면 동기화된 모든 태그, 컬렉션, 메타필드 데이터를 포함한 전체 카탈로그가 제거됩니다. 비활성화하기 전에 이 카탈로그를 참조하는 Campaigns 또는 Canvases를 업데이트하거나 일시 중지하세요. 그렇지 않으면 제품 세부 정보가 누락된 메시지가 발송될 수 있습니다.

### 이전에 동기화된 제품 또는 제품 필드를 Shopify에서 삭제하면 어떻게 되나요? {#what-happens-if-i-delete-a-previously-synced-product-or-product-field-in-shopify}

Braze는 삭제를 감지하면 Shopify 카탈로그에서 해당 제품 또는 필드를 자동으로 제거합니다. 그러나 삭제된 제품 또는 필드를 참조하는 Campaigns, Canvases 또는 Segments는 정상적으로 작동하지 않게 됩니다. Shopify에서 제품이나 필드를 삭제하기 전에 Braze에서 해당 항목이 활발히 사용되고 있지 않은지 확인하세요.

### 카탈로그 ID(제품 식별자)를 어떻게 변경하나요? {#how-do-i-change-my-catalog-id-product-identifier}

카탈로그 ID를 변경하려면 먼저 동기화를 비활성화하고 활성 메시지가 이 카탈로그 데이터를 참조하지 않는지 확인하세요. 그런 다음 초기 동기화를 다시 실행하고 원하는 식별자를 선택하세요.

### 동기화된 태그, 컬렉션 또는 메타필드를 변경하면 활성 Campaigns에 영향을 미치나요? {#will-changing-my-synced-tags-collections-or-metafields-affect-active-campaigns}

네. 동기화 선택 항목을 변경하면 이를 참조하는 활성 Campaigns, Canvases 또는 [카탈로그 셀렉션]({{site.baseurl}}/catalog_selections)에 영향을 줄 수 있습니다. 변경하기 전에 활성 콘텐츠가 업데이트되었는지 확인하세요.

### 초기 동기화는 얼마나 걸리나요? {#how-long-does-the-initial-sync-take}

동기화 시간은 스토어의 제품 및 배리언트 수에 따라 달라집니다. 초기 동기화는 제품을 배치 단위로 가져오므로, 모든 제품 태그, 메타필드 및 컬렉션 연결이 표시되기까지 다소 시간이 걸릴 수 있습니다. Shopify 파트너 페이지에서 동기화 상태를 모니터링하세요.

## 구성 및 제한 사항 {#configuration-and-limits}

### 태그, 컬렉션, 메타필드는 몇 개까지 동기화할 수 있나요? {#how-many-tags-collections-or-metafields-can-i-sync}

구성당 각 항목을 최대 20개까지 동기화할 수 있습니다:

- 제품 태그 최대 20개
- 컬렉션 최대 20개
- 제품 메타필드 최대 20개

### 제품이 250개 이상의 컬렉션에 속하면 어떻게 되나요? {#what-if-a-product-belongs-to-more-than-250-collections}

Shopify에서는 제품이 250개 이상의 컬렉션에 속할 수 있지만, Braze는 제품당 처음 250개의 컬렉션 연결만 가져올 수 있습니다. 제품이 처음 가져온 250개 범위 밖의 선택된 컬렉션에 속하는 경우, 해당 연결은 Shopify 카탈로그에 반영되지 않습니다. 누락된 컬렉션 연결이 확인되면 고객 성공 매니저에게 문의하세요.

### 구성 모달에 모든 컬렉션이 표시되지 않는 이유는 무엇인가요? {#why-dont-i-see-all-my-collections-in-the-configuration-modal}

구성 모달에는 가장 최근에 업데이트된 컬렉션 최대 5,000개가 표시됩니다. 스토어가 이 제한을 초과하면 오래된 컬렉션이 표시되지 않을 수 있습니다. 상위 5,000개 범위 밖에 있는 이전에 선택한 컬렉션은 여전히 선택 항목에 표시됩니다.

### 단일 카탈로그 셀렉션에서 태그와 컬렉션을 동시에 필터링할 수 있나요? {#can-i-filter-by-both-tags-and-collections-in-a-single-catalog-selection}

아니요. 카탈로그 셀렉션은 셀렉션 필터당 하나의 배열 필드만 지원합니다. 동일한 셀렉션에서 태그와 컬렉션을 결합할 수 없습니다. 태그와 컬렉션 기준을 모두 기반으로 사용자를 타겟팅해야 하는 경우, SQL 쿼리와 함께 [세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension)을 사용하세요.

### 카탈로그 셀렉션 제한은 어떻게 되나요? {#what-are-the-catalog-selection-limits}

카탈로그 셀렉션은 표준 카탈로그 셀렉션과 동일한 제한이 적용됩니다. 항목 제한, 필터 제약 조건 및 티어 기반 스토리지 한도에 대한 자세한 내용은 [카탈로그 셀렉션]({{site.baseurl}}/catalog_selections)을 참조하세요.

## 메타필드 및 문제 해결 {#metafields-and-troubleshooting}

### 일부 메타필드 유형이 표시되지 않는 이유는 무엇인가요? {#why-are-some-of-my-metafield-types-not-showing-up}

지원되는 메타필드 유형만 구성 모달에 표시됩니다. 현재 지원되지 않는 유형은 `dimension`, `json`, `link`, `money`, `rating`, `rich_text_field`, `volume`, `weight`입니다. 지원되는 유형과 전체 목록은 Shopify 제품 동기화 페이지의 [Shopify 제품 메타필드]({{site.baseurl}}/shopify_catalogs#shopify-product-metafields)를 참조하세요.

### "Duplicate Metafield Column Name" 오류가 발생했습니다. 어떻게 해야 하나요? {#i-got-a-duplicate-metafield-column-name-error-what-do-i-do}

선택한 메타필드 중 두 개 이상이 카탈로그에서 동일한 열 이름을 생성하려고 합니다. 충돌하는 메타필드 중 하나를 선택 해제하거나, Shopify에서 메타필드 키의 이름을 변경하여 각각 고유한 열 이름에 매핑되도록 하세요. 그런 다음 구성을 다시 저장하세요.

### 태그를 로드하는 데 예상보다 오래 걸리는 이유는 무엇인가요? {#why-are-my-tags-taking-longer-than-expected-to-load}

태그는 구성 모달을 열 때 Shopify에서 직접 가져옵니다. 스토어에 제품이나 태그가 많은 경우 로드하는 데 시간이 더 걸릴 수 있습니다. 이는 예상되는 동작이며 동기화 성능에는 영향을 미치지 않습니다. 로드가 지속적으로 시간 초과되는 경우, Shopify 스토어의 전체 태그 수를 줄이거나 지원팀에 문의하세요.

## 스토리지 {#storage}

### 추가 제품 데이터를 동기화하면 카탈로그 스토리지에 영향을 미치나요? {#will-syncing-additional-product-data-affect-my-catalog-storage}

네. 태그, 메타필드, 컬렉션을 동기화하면 카탈로그 스토리지 사용량이 증가합니다. 무료 카탈로그 티어에는 100 MB 스토리지 제한이 있습니다. 동기화가 제한을 초과하면 Braze는 동기화를 중단하고 제품 업데이트가 더 이상 반영되지 않습니다. 필요한 경우 계정 매니저에게 연락하여 티어를 업그레이드하세요.