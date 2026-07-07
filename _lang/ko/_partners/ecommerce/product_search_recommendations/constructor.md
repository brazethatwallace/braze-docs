---
nav_title: Constructor
article_title: Constructor
description: "이 참조 문서에서는 Braze와 Constructor 간의 파트너십에 대해 설명합니다. 이 파트너십을 통해 Constructor의 Offsite Product Discovery를 활용하여 Braze 메시지에서 개인화된 제품 추천을 동적으로 생성하고 전달할 수 있습니다."
alias: /partners/constructor/
page_type: partner
search_tag: Partner
---

# Constructor

> [Constructor](https://constructor.com/)는 AI와 머신 러닝을 활용하여 이커머스 및 리테일 웹사이트에 개인화된 검색, 추천, 브라우징 경험을 제공하는 검색 및 제품 디스커버리 플랫폼입니다.

Braze와 Constructor 통합을 사용하면 Constructor의 Offsite Product Discovery를 활용하여 Braze 메시지에서 개인화된 제품 추천을 동적으로 생성하고 전달할 수 있습니다.

## 활용 사례 {#use-cases}

- **유기한 장바구니 및 주문 후 후속 조치**: 사용자 행동과 장바구니 내용을 기반으로 동적 제품 추천을 생성하여 개인화된 유기한 장바구니 리마인더 또는 주문 후 제안을 전송합니다.
- **유기한 장바구니 아이템에 대한 유사 제품 추천**: 사용자의 장바구니에 남아 있는 아이템과 유사한 제품을 제안하여 참여를 유지하고 대안을 제공합니다.
- **최근 조회한 아이템 리마인더**: 사용자가 최근 조회했지만 아직 구매하지 않은 아이템에 대해 알림을 보내 구매를 완료하도록 유도합니다.
- **프로모션 캠페인**: 시즌 세일이나 특별 할인에 맞춰 사용자 선호도에 맞는 큐레이션된 제품 추천이 포함된 개인화된 프로모션 메시지를 전달합니다.
- **시각적으로 유사한 제품 제안**: 사용자가 최근 조회한 아이템과 시각적으로 유사한 아이템을 추천하여 선호할 수 있는 관련 옵션을 발견하도록 돕습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|-------------|-------------|
| Constructor 계정 | 이 파트너십을 활용하려면 Offsite Discovery 서비스가 활성화된 Constructor 계정이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integration}

Constructor 온보딩 팀과 협력하여 통합 프로세스를 완료하세요. 개인화된 제품 추천을 활성화하려면 웹사이트 또는 기타 관련 데이터 소스의 행동 데이터를 사용할 수 있어야 합니다. Constructor 온보딩 팀은 Braze 메시지에서 사용할 필요한 HTML 스니펫 구성도 도와줍니다.

## Constructor의 Offsite Discovery API URL {#constructors-offsite-discovery-api-url}

Constructor의 Offsite Discovery API URL을 사용하여 제품 이미지를 렌더링하고 사용자를 적절한 제품 상세 페이지로 안내할 수 있습니다. 아래는 엔드포인트 구조의 분석과 사용 방법 예시입니다.

### 예시 {#example}

```html
<a href="https://offsite-discovery.cnstrc.com/v1/product/url?position=[position]&ui=[ui]&pod_id=[pod_id]&key=[key]&style_id=[style_id]&campaign_id=[campaign_id]" target="_blank">
  <img
    src="https://offsite-discovery.cnstrc.com/v1/product/image?position=[position]&ui=[ui]&pod_id=[pod_id]&key=[key]&style_id=[style_id]&campaign_id=[campaign_id]"
    width="200"
    border="0"
    alt="Shop Now"
  />
</a>
```

### 파라미터 {#parameters}

| 파라미터 | 설명 |
|-------------|-------------|
| `position` | 추천 목록 내에서 특정 추천 아이템의 순위를 나타냅니다(예: `position = 2`). <br>![아이템의 위치 순위.]({% image_buster /assets/img/constructor/constructor_position.png %}) |
| `ui` | 사용자의 식별자를 나타내며, 추천 결과를 개인화하는 데 중요합니다. `ui` 파라미터를 Braze에서 고객의 `external_id`로 설정하세요. 생략하면 Constructor는 사용자별 추천 대신 일반 추천을 반환합니다. |
| `pod_id` | 추천을 위한 전략 및 서치앤다이징 규칙이 포함된 pod의 식별자입니다(예: 베스트셀러 전략이 있는 pod는 개인화된 베스트셀러를 생성합니다). |
| `key` | 이 고객에 대한 Constructor 인덱스 키입니다. |
| `style_id` | 제품 카드에 표시되는 이미지를 결정합니다. 예를 들어, 서로 다른 `style_ids`는 고유한 제품 카드 이미지를 표시합니다. |
| `campaign_id` | 이메일 캠페인의 고유 ID입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Parameters" }

### 선택 입력값 {#optional-inputs}

| 입력값 | 설명 |
|-------------|-------------|
| `item_id` | 시드 아이템을 나타냅니다. 대안, 보완, 번들과 같은 아이템-아이템 기반 전략에 필요합니다. 예를 들어, 이메일의 첫 번째 아이템이 시드 아이템이고 후속 아이템이 대안입니다. |
| `num_results` | 이메일에 추가할 제품 수입니다. 기본값은 10이며 최대 100까지 가능합니다. 예를 들어, `num_results = 3`은 세 개의 추천이 추가됨을 의미합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Optional inputs" }