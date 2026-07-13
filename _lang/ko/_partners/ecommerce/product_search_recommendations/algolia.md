---
nav_title: Algolia
article_title: Algolia
description: "Algolia를 Braze 연결된 콘텐츠와 함께 사용하여 Braze 메시지에서 개인화된 검색 결과와 제품 추천을 동적으로 전달하는 방법을 알아보세요."
alias: /partners/algolia/
page_type: partner
search_tag: Partner
---

# Algolia

> [Algolia](https://www.algolia.com/)는 개발자가 빠르고 관련성 높으며 확장 가능한 검색 경험을 구축할 수 있도록 돕는 검색 및 디스커버리 플랫폼입니다. 강력한 API 우선 접근 방식을 통해 Algolia는 고급 랭킹 알고리즘과 AI 기반 인사이트를 결합하여 원활한 사이트 검색, 내비게이션 및 개인화된 콘텐츠 디스커버리를 제공합니다.

Algolia와 Braze 통합은 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)를 사용하여 Algolia 기반 검색 결과와 제품 추천을 Braze 메시지에 채웁니다. 발송 시점에 Algolia의 API를 쿼리하여 사용자를 높은 전환율의 제품 상세 페이지 또는 랜딩 페이지로 유도하는 개인화된 콘텐츠를 전달할 수 있습니다.

## 활용 사례 {#use-cases}

- **인기 제품 홍보:** Algolia에서 인기 또는 최고 성과 제품을 자동으로 가져와 Braze 메시지에 포함시켜 관심도가 높은 아이템을 홍보하고 참여를 높입니다.
- **검색 인텔리전스로 Campaign 개인화:** Algolia 검색 및 브라우징 인텔리전스를 활용하여 Braze Campaign을 개인화하고, 각 사용자의 관심사에 맞는 제품이나 카테고리를 전달합니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|-------------|-------------|
| Algolia 계정 | 이 파트너십을 활용하려면 Algolia 계정이 필요합니다. |
| Algolia API 자격 증명 | Algolia API 키 및 애플리케이션 ID입니다. |
| Algolia 제품 인덱스 | 제품 데이터로 채워진 Algolia 인덱스입니다. Search 또는 Recommend API를 사용하려면 이 인덱스가 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 {#integration}

### 1단계: Algolia API 요청 설정 {#step-1-set-up-your-algolia-api-request}

요청 형식, 응답 구조 및 사용법에 대한 자세한 내용은 [Algolia Search API](https://www.algolia.com/doc/rest-api/search) 및 [Algolia Recommend API](https://www.algolia.com/doc/rest-api/recommend) 설명서를 참조하세요. 설정에 도움이 필요하면 Algolia 팀에 문의하세요.

{% tabs local %}
{% tab Search API %}

#### Search API 요청 예시 {#example-search-api-request}

```
POST https://{ALGOLIA_APP_ID}-dsn.algolia.net/1/indexes/{INDEX_NAME}/query
Content-Type: application/json
X-Algolia-API-Key: {ALGOLIA_API_KEY}
X-Algolia-Application-Id: {ALGOLIA_APP_ID}
```

#### 쿼리 페이로드 예시 {#example-query-payload}

```json
{
  "query": "",
  "hitsPerPage": 4,
  "filters": "category_page_id:'this week's offers'",
  "attributesToRetrieve": ["name", "price", "image", "url"]
}
```

이 예시에서 쿼리는 `category_page_id`라는 속성을 기반으로 카테고리 필터를 사용하는 페이지에서 상위 4개 결과를 가져옵니다. `attributesToRetrieve` 파라미터는 페이로드를 관리 가능한 크기로 유지하기 위해 응답을 제한합니다.

**사용 사례 예시:** 주간 특가 Braze Campaign에 `https://www.yoursite.com/weekly-offers`의 검색 결과를 포함하려면, 해당 Algolia 인덱스를 쿼리하고 필터를 적용하여 해당 페이지의 상위 결과를 가져옵니다.

{% alert tip %}
`attributesToRetrieve`를 사용하여 평점, 리뷰 또는 할인 등의 추가 필드를 가져와 개인화를 강화하세요.
{% endalert %}

{% endtab %}
{% tab Recommend API %}

#### Recommend API 요청 예시 {#example-recommend-api-request}

```
POST https://{ALGOLIA_APP_ID}.algolia.net/1/indexes/*/recommendations
Content-Type: application/json
X-Algolia-API-Key: {ALGOLIA_API_KEY}
X-Algolia-Application-Id: {ALGOLIA_APP_ID}
```

#### 쿼리 페이로드 예시

```json
{
  "requests": [
    {
      "indexName": "prod_ECOM",
      "model": "trending-items",
      "threshold": 40,
      "maxRecommendations": 4
    }
  ]
}
```

Recommend API는 **Frequently Bought Together**, **Related Products**, **Trending Items**, **Trending Facet Values**, **Looking Similar** 등 여러 모델을 지원합니다. 이 예시에서는 **Trending Items** 모델을 사용합니다.

{% alert important %}
추천이 사용자별 속성이나 objectID에 의존하는 경우, Algolia 계약에 정의된 사용량 제한에 유의하세요. 모범 사례는 [고려 사항](#considerations) 섹션을 참조하세요.
{% endalert %}

{% endtab %}
{% endtabs %}

### 2단계: Braze 연결된 콘텐츠 구현 {#step-2-implement-braze-connected-content}

Braze의 연결된 콘텐츠 기능을 사용하여 Algolia 엔드포인트에 API 호출을 수행하고 응답을 메시지에 동적으로 삽입합니다. 구성, 요청 형식 및 모범 사례에 대한 자세한 내용은 [연결된 콘텐츠]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/)를 참조하세요.

{% tabs local %}
{% tab Search API %}

#### 연결된 콘텐츠 Search 요청 예시 {#example-connected-content-search-request}

{% raw %}
```liquid
{% capture request_body %}
{
  "query": "",
  "hitsPerPage": 4,
  "filters": "category_page_id:'this week's offers'",
  "attributesToRetrieve": ["name", "price", "image", "url"]
}
{% endcapture %}

{% connected_content https://{{ALGOLIA_APP_ID}}-dsn.algolia.net/1/indexes/{{INDEX_NAME}}/query
  :method post
  :headers {"X-Algolia-API-Key":"{{ALGOLIA_API_KEY}}", "X-Algolia-Application-Id":"{{ALGOLIA_APP_ID}}", "Content-Type": "application/json"}
  :body {{request_body}}
  :save algolia_search
%}
```
{% endraw %}

{% endtab %}
{% tab Recommend API %}

#### 연결된 콘텐츠 Recommend 요청 예시 {#example-connected-content-recommend-request}

{% raw %}
```liquid
{% capture request_body %}
{
  "requests": [
    {
      "indexName": "prod_ECOM",
      "model": "trending-items",
      "threshold": 40,
      "maxRecommendations": 4
    }
  ]
}
{% endcapture %}

{% connected_content https://{{ALGOLIA_APP_ID}}.algolia.net/1/indexes/*/recommendations
  :method post
  :headers {"X-Algolia-Application-Id":"{{ALGOLIA_APP_ID}}", "X-Algolia-API-Key":"{{ALGOLIA_API_KEY}}", "Content-Type": "application/json"}
  :body {{request_body}}
  :save algolia_recommendations
%}
```
{% endraw %}

{% endtab %}
{% endtabs %}

### 3단계: Braze 메시지에서 검색 결과 포맷 지정 {#step-3-format-search-results-in-braze-messages}

Algolia에서 결과를 가져온 후 Liquid를 사용하여 API 응답을 구문 분석하고 메시지 내에서 결과를 동적으로 렌더링합니다.

{% tabs local %}
{% tab Search API %}

#### Search API용 Liquid 이메일 템플릿 예시 {#example-liquid-email-template-for-search-api}

{% raw %}
```liquid
{% for item in algolia_search.hits %}
  <div style="margin-bottom: 10px;">
    <img src="{{ item.image }}" alt="{{ item.name }}" width="100"/>
    <p><strong>{{ item.name }}</strong></p>
    <p>Price: ${{ item.price }}</p>
    <a href="{{ item.url }}">View Product</a>
  </div>
{% endfor %}
```
{% endraw %}

이 코드는 메시지 본문 내에서 Search API 결과로부터 제품 목록을 생성합니다. 각 제품 링크는 사용자를 제품 상세 페이지(PDP) 또는 Campaign 전용 랜딩 페이지로 안내합니다.

{% endtab %}
{% tab Recommend API %}

#### Recommend API용 Liquid 이메일 템플릿 예시 {#example-liquid-email-template-for-recommend-api}

{% raw %}
```liquid
{% for item in algolia_recommendations.hits %}
  <div style="margin-bottom: 10px;">
    <img src="{{ item.image }}" alt="{{ item.name }}" width="100"/>
    <p><strong>{{ item.name }}</strong></p>
    <p>Price: ${{ item.price }}</p>
    <a href="{{ item.url }}">View Product</a>
  </div>
{% endfor %}
```
{% endraw %}

이 코드는 메시지 본문 내에서 Recommend API 결과로부터 추천 제품 목록을 생성합니다. 각 제품 링크는 사용자를 제품 상세 페이지(PDP) 또는 Campaign 전용 랜딩 페이지로 안내합니다.

{% endtab %}
{% endtabs %}

## 고려 사항 {#considerations}

### 고유 쿼리 방지 {#avoiding-unique-queries}

Algolia 계약에 정의된 사용량 제한에 유의하세요. 사용자별 쿼리는 할당된 요청 수를 빠르게 초과할 수 있으므로 피하세요. 결과를 개인화하려면 개별 사용자 ID 대신 Segment를 타겟팅하거나, 특정 objectID 대신 카테고리 또는 브랜드로 필터링하세요. Braze 속성을 사용하여 추천을 추가로 개인화할 수 있습니다.

### 연결된 콘텐츠 결과 캐싱 {#caching-connected-content-results}

`cache_max_age`를 사용하여 연결된 콘텐츠 결과를 캐싱하면 Algolia에 대한 API 요청을 최소화하고 성능을 향상시킬 수 있습니다. 자세한 내용은 [응답 캐싱]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/caching_responses/)을 참조하세요.