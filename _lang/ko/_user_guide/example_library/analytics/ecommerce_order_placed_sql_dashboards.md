---
nav_title: Order Placed SQL 대시보드
article_title: Dashboard Builder에서 이커머스 Order Placed 이벤트 보고하기
page_order: 1
page_type: reference
description: "쿼리 빌더 SQL을 ecommerce.order_placed 이벤트에 사용하여 이커머스 보고를 위한 매출 및 주문 타일을 Dashboard Builder에서 구축합니다."
tool: Reports
---

# Dashboard Builder에서 이커머스 Order Placed 이벤트 보고하기 {#report-on-ecommerce-order-placed-events-in-dashboard-builder}

> `ecommerce.order_placed` 권장 이벤트에서 커스텀 매출 및 주문 차트를 작성하려면 쿼리 빌더에서 SQL 쿼리를 저장하고 Dashboard Builder에서 결과를 시각화합니다.

## 이 예제 소개 {#about-this-example}

가상의 의류 소매 브랜드인 Flash & Thread는 [이커머스 권장 이벤트]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events)를 사용하여 주문을 기록합니다. 마케팅 팀은 사전 구축된 라스트 터치 기여도 뷰뿐만 아니라 일일 매출, 평균 주문 금액(AOV), 주문량을 하나의 대시보드에서 확인하고자 합니다.

이 패턴은 쿼리 빌더를 사용하여 Snowflake 공유 이벤트 테이블에서 `ecommerce.order_placed`를 쿼리한 다음, 저장된 쿼리를 Dashboard Builder의 **Custom Queries** 타일로 추가합니다. 추가 측정기준(신규 대 재구매 고객, 제품 카테고리 또는 Segment 수준 매출)에 대해서도 동일한 워크플로를 반복할 수 있습니다.

기본 제공 이커머스 대시보드가 필요한 측정기준 조합을 다루지 못할 때 이 방법을 사용하세요. 라스트 터치 기여도 매출의 경우 [Revenue - Last Touch Attribution]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder#revenue---last-touch-attribution) 대시보드를 참조하세요.

## 고려 사항 {#considerations}

- **이벤트 구현:** 쿼리가 데이터를 반환하려면 `ecommerce.order_placed`가 구현되어 있고 `total_value`(필요한 경우 제품 데이터 포함)를 전송하고 있어야 합니다. [Shopify 커넥터]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector)를 사용하는 경우 권장 이벤트가 이미 사용 가능할 수 있습니다.
- **쿼리 빌더 접근 권한:** 쿼리 빌더를 사용하려면 "View PII" [사용자 권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)이 필요합니다.
- **데이터 보존:** 쿼리 빌더는 기본적으로 최근 60일간의 데이터를 반환합니다. [Snowflake 데이터 공유]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)를 사용하면 최대 2년간 보존된 데이터를 쿼리할 수 있습니다. [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder)를 참조하세요.
- **타임아웃:** 6분 이상 실행되는 쿼리는 타임아웃됩니다. 보고서가 실패하면 날짜 범위를 좁히거나, `TIME`으로 필터링하거나, 오디언스 크기를 줄이세요. 이벤트 테이블은 `TIME`을 기준으로 클러스터링되어 있으므로 이벤트 발생 시점으로 필터링하는 것이 좋습니다.
- **매출 필드:** 샘플 쿼리는 이벤트 `properties`에서 `total_value`를 합산합니다. Braze의 표준화된 이커머스 매출은 제품 보고서에서 각 제품의 `price`와 `quantity`에서 파생되는 경우가 많습니다. `total_value`를 제품 라인 항목과 일치시키거나, 스키마에 맞게 SQL을 조정하세요.
- **열 레이블:** 표시 열 이름을 큰따옴표로 감싸세요(예: `"Date"`, `"Total Revenue"`). 그래야 Dashboard Builder에서 읽기 쉬운 축 및 테이블 헤더가 표시됩니다.
- **테스트:** 이 문서의 SQL은 예제로 제공됩니다. 대시보드를 널리 공유하기 전에 워크스페이스에서 쿼리를 검증하세요.

## 설정 {#setup}

### 1단계: 일일 매출 SQL 쿼리 만들기 {#step-1-create-a-sql-query-for-daily-revenue}

1. **Analytics** > **쿼리 빌더**로 이동합니다.
2. **Create SQL Query**를 선택한 다음 **SQL Editor**를 선택합니다.
3. 쿼리 이름을 지정합니다(예: `Flash Thread — daily eCommerce revenue`).
4. 최근 60일간의 캘린더 일별 총 매출에 대해 다음 쿼리를 붙여넣고 조정합니다:

{% raw %}
```sql
SELECT
  DATE_TRUNC('day', TO_TIMESTAMP_NTZ(TIME))::DATE AS "Date",
  SUM(PARSE_JSON(PROPERTIES):total_value::NUMBER(18, 2)) AS "Total Revenue"
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED
WHERE NAME = 'ecommerce.order_placed'
  AND TO_TIMESTAMP_NTZ(TIME) >= DATEADD(day, -60, CURRENT_TIMESTAMP())
  AND TO_TIMESTAMP_NTZ(TIME) <= CURRENT_TIMESTAMP()
GROUP BY 1
ORDER BY 1;
```
{% endraw %}

{:start="5"}
5. **Run Query**를 선택한 다음 **Save**를 선택합니다.

쿼리 빌더 설정에 대한 자세한 내용은 [쿼리 빌더에서 보고서 실행하기]({{site.baseurl}}/user_guide/analytics/reports/query_builder#running-reports-in-the-query-builder)를 참조하세요.

### 2단계: Dashboard Builder 타일에 쿼리 추가하기 {#step-2-add-the-query-to-a-dashboard-builder-tile}

1. **Analytics** > **Dashboard Builder**로 이동합니다.
2. **Create Dashboard**를 선택합니다(또는 기존 대시보드를 엽니다).
3. 데이터 소스로 **Custom Queries**를 선택합니다.
4. **+ Add Tile**을 선택한 다음 1단계에서 저장한 쿼리를 선택합니다.
5. 연필 아이콘을 선택하여 타일을 편집합니다:
   - 차트 유형을 **Line graph**로 설정합니다.
   - **X-axis**를 `Date`로 설정합니다.
   - **Y-axis**를 `Total Revenue`로 설정합니다.
6. 필요에 따라 타일 크기를 조정한 다음 **Save**를 선택합니다.
7. **View Dashboard** > **Run Dashboard**를 선택합니다.

대시보드 생성에는 몇 분이 걸릴 수 있습니다. [커스텀 대시보드 만들기]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder#creating-a-custom-dashboard)를 참조하세요.

### 3단계: 추가 *Order Placed* 측정기준 추가하기(선택 사항) {#step-3-add-additional-_order-placed_-metrics-optional}

별도의 저장된 쿼리를 만든 다음 각각을 고유한 타일로 추가합니다(대시보드당 최대 10개 타일).

#### 일별 평균 주문 금액 및 주문 수 {#average-order-value-and-order-count-per-day}

{% raw %}
```sql
SELECT
  DATE_TRUNC('day', TO_TIMESTAMP_NTZ(TIME))::DATE AS "Date",
  AVG(PARSE_JSON(PROPERTIES):total_value::NUMBER(18, 2)) AS "Average Order Value",
  COUNT(*) AS "No. of Orders"
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED
WHERE NAME = 'ecommerce.order_placed'
  AND TO_TIMESTAMP_NTZ(TIME) >= DATEADD(day, -60, CURRENT_TIMESTAMP())
  AND TO_TIMESTAMP_NTZ(TIME) <= CURRENT_TIMESTAMP()
GROUP BY 1
ORDER BY 1;
```
{% endraw %}

X축에 `Date`, Y축에 두 측정기준을 사용하여 꺾은선형 또는 막대형 차트를 사용합니다(표시하지 않으려는 열은 선택 해제합니다).

#### 일별 신규 구매자 대 재구매자 {#new-versus-returning-purchasers-per-day}

이 패턴은 각 사용자의 첫 `ecommerce.order_placed` 날짜를 이후 구매 날짜와 비교합니다. 쿼리 빌더 기간이 전체 보고 기간을 포함할 때 가장 정확합니다(예: 기본 60일 기간).

{% raw %}
```sql
WITH order_days AS (
  SELECT DISTINCT
    USER_ID,
    DATE_TRUNC('day', TO_TIMESTAMP_NTZ(TIME))::DATE AS purchase_day
  FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED
  WHERE NAME = 'ecommerce.order_placed'
),
first_purchase AS (
  SELECT
    USER_ID,
    MIN(purchase_day) AS first_day
  FROM order_days
  GROUP BY USER_ID
),
per_day_purchasers AS (
  SELECT DISTINCT
    USER_ID,
    purchase_day
  FROM order_days
)
SELECT
  p.purchase_day AS "Date",
  COUNT(DISTINCT CASE
    WHEN f.first_day = p.purchase_day THEN p.USER_ID
  END) AS "New Purchasers",
  COUNT(DISTINCT CASE
    WHEN f.first_day < p.purchase_day THEN p.USER_ID
  END) AS "Returning Purchasers"
FROM per_day_purchasers AS p
INNER JOIN first_purchase AS f
  ON p.USER_ID = f.USER_ID
GROUP BY 1
ORDER BY 1;
```
{% endraw %}

#### 주문 라인 항목별 제품 카테고리 {#product-category-from-order-line-items}

`products` 배열을 플래튼하고 카테고리 필드로 필터링합니다. 다른 제품 메타데이터 키를 사용하는 경우 `metadata.category`를 교체하세요.

{% raw %}
```sql
SELECT
  f.value:metadata:category::STRING AS "Product Category",
  COUNT(*) AS "Line Items"
FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED,
  LATERAL FLATTEN(INPUT => PARSE_JSON(PROPERTIES):products) f
WHERE NAME = 'ecommerce.order_placed'
  AND f.value:metadata:category::STRING IS NOT NULL
  AND TRIM(f.value:metadata:category::STRING) != ''
  AND LOWER(TRIM(f.value:metadata:category::STRING)) != 'undefined'
GROUP BY 1
ORDER BY 2 DESC;
```
{% endraw %}

#### Segment별 구매 및 매출(Segment 분석) {#purchases-and-revenue-by-segment-segment-analytics}

이 쿼리를 사용하려면 보고 대상 Segments에 [Segment 분석 추적]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking)이 활성화되어 있어야 합니다. 날짜 선택기에는 [SQL 변수]({{site.baseurl}}/user_guide/analytics/reports/query_builder/sql_variables)를 사용하세요.

{% raw %}
```sql
WITH event_conversions AS (
  SELECT
    user_id,
    time,
    TRY_CAST(GET_PATH(PARSE_JSON(PROPERTIES), 'total_value')::string AS FLOAT) AS price,
    id AS purchase_event_id,
    f.value::string AS user_segment_membership_id
  FROM USERS_BEHAVIORS_CUSTOMEVENT_SHARED,
    LATERAL FLATTEN(input => user_segment_membership_ids) AS f
  WHERE NAME = 'ecommerce.order_placed'
    AND time > {{start_date.${Start Date}}}
    AND time < {{end_date.${End Date}}}
)
SELECT
  user_segment_membership_id AS "Segment Analytics Id",
  COUNT(DISTINCT purchase_event_id) AS "Total Purchases",
  ROUND(SUM(price), 2) AS "Total Revenue"
FROM event_conversions
GROUP BY 1
ORDER BY 3 DESC;
```
{% endraw %}

### 기타 기본 제공 이커머스 보고 {#other-built-in-ecommerce-reporting}

| 보고서 | 사용 시기 |
| --- | --- |
| [Revenue - Last Touch Attribution]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder#revenue---last-touch-attribution) | Campaign 또는 Canvas별 라스트 터치 기여도 매출 |
| [커스텀 이벤트 보고서]({{site.baseurl}}/user_guide/analytics/reports/custom_events_report) | 권장 이벤트의 이벤트 볼륨 및 빈도 |
| Campaign 또는 Canvas 전환 | `ecommerce.order_placed`가 주요 전환 이벤트인 경우 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="기타 기본 제공 이커머스 보고" }

## 관련 문서 {#related-articles}

- [이커머스 권장 이벤트]({{site.baseurl}}/user_guide/data/activation/events/recommended_events/ecommerce_events)
- [쿼리 빌더]({{site.baseurl}}/user_guide/analytics/reports/query_builder)
- [쿼리 빌더의 SQL 변수]({{site.baseurl}}/user_guide/analytics/reports/query_builder/sql_variables)
- [Dashboard Builder]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder)
- [Revenue - Last Touch Attribution]({{site.baseurl}}/user_guide/analytics/dashboards/dashboard_builder#revenue---last-touch-attribution)
- [SQL 테이블 참조]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables#USERS_BEHAVIORS_CUSTOMEVENT_SHARED)
- [Segment 분석 추적]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking)