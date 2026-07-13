---
nav_title: 쿼리 빌더
article_title: 쿼리 빌더
page_order: 4
description: "이 참조 문서에서는 쿼리 빌더에서 Snowflake의 Braze 데이터를 사용하여 보고서를 구축하는 방법을 설명합니다."
tool: Reports
alias: /query_builder/
---

# 쿼리 빌더 {#query-builder}

> 쿼리 빌더는 Snowflake의 Braze 데이터를 사용하여 보고서를 생성합니다. 쿼리 빌더에는 시작하는 데 도움이 되는 사전 구축된 SQL [쿼리 템플릿]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates)이 제공되며, 직접 커스텀 SQL 쿼리를 작성하여 더 많은 인사이트를 얻을 수도 있습니다.

쿼리 빌더는 일부 고객 데이터에 대한 직접 액세스를 허용하므로, "PII 보기" [권한]({{site.baseurl}}/user_guide/administer/global/user_management/permissions)이 있는 경우에만 쿼리 빌더에 액세스할 수 있습니다.

## 사용 가능한 데이터 테이블 {#available-data-tables}

쿼리 빌더는 [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) 및 [Snowflake 데이터 공유]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)와 동일한 Snowflake SQL 테이블을 사용합니다. 사용 가능한 테이블과 해당 열의 전체 목록은 [SQL 테이블 참조]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables)를 참조하세요.

## 쿼리 빌더에서 보고서 실행하기 {#running-reports-in-the-query-builder}

쿼리 빌더 보고서를 실행하려면:

1. **Analytics** > **쿼리 빌더**로 이동합니다.
2. **SQL 쿼리 생성**을 선택합니다. 쿼리 작성에 영감이나 도움이 필요하면 **쿼리 템플릿**을 선택하고 목록에서 템플릿을 선택합니다. 그렇지 않으면 **SQL 편집기**를 선택하여 편집기로 바로 이동합니다.
3. 보고서에는 현재 날짜와 시간이 자동으로 이름으로 지정됩니다. 이름 위에 마우스를 올리고 <i class="fas fa-pencil" alt="편집"></i>을 선택하여 SQL 쿼리에 의미 있는 이름을 지정합니다.
4. 편집기에서 SQL 쿼리를 작성하거나 **AI 쿼리 빌더** 탭에서 [AI의 도움을 받습니다](#ai-query-builder). 직접 SQL을 작성하는 경우 요구 사항과 리소스에 대해 [커스텀 SQL 쿼리 작성하기](#custom-sql)를 참조하세요.
5. **쿼리 실행**을 선택합니다.
6. 쿼리를 저장합니다.
7. 보고서의 CSV를 다운로드하려면 **내보내기**를 선택합니다.

![템플릿 쿼리 '최근 30일간 채널 참여 및 매출'의 결과를 보여주는 쿼리 빌더.]({% image_buster /assets/img_archive/query_builder.png %})

각 보고서의 결과는 하루에 한 번 생성할 수 있습니다. 같은 보고서를 하루에 두 번 이상 실행하면 두 보고서 모두에서 동일한 결과가 표시됩니다.

### 쿼리 템플릿 {#query-templates}

보고서를 처음 생성할 때 **SQL 쿼리 생성** > **쿼리 템플릿**을 선택하여 쿼리 템플릿에 액세스합니다.

사용 가능한 템플릿 목록은 [쿼리 템플릿]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates)을 참조하세요.

### 데이터 기간 {#data-timeframe}

쿼리는 최근 60일간의 데이터를 반환합니다. Currents 또는 [Snowflake 데이터 공유]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake)를 사용하는 경우 최대 2년간의 데이터를 쿼리할 수 있으며, 이는 Snowflake에서 데이터가 보존되는 기간입니다. 확장된 데이터 보존에 대한 자세한 내용은 고객 성공 매니저에게 문의하세요.

### 쿼리 빌더 시간대 {#query-builder-time-zone}

Snowflake 데이터베이스를 쿼리하는 기본 시간대는 UTC입니다. 따라서 **이메일 채널 참여** 페이지(회사의 시간대를 따름)와 쿼리 빌더 결과 사이에 일부 데이터 불일치가 있을 수 있습니다.

쿼리 결과에서 시간대를 변환하려면 다음 SQL을 쿼리에 추가하고 회사의 시간대에 맞게 커스터마이즈합니다:

{% raw %}
```sql
SELECT
DATE_TRUNC(
'day',
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME))
) AS send_date_sydney,
COUNT(ID) AS emails_sent
USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE
-- Apply the date range in Sydney time as well
CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) >= '2025-03-25 00:00:00'
AND CONVERT_TIMEZONE('UTC','Australia/Sydney', TO_TIMESTAMP(TIME)) < '2025-03-29 00:00:00'
AND APP_GROUP_ID = 'your app group ID'
GROUP BY
send_date_sydney
ORDER BY
send_date_sydney;
```
{% endraw %}

### 쿼리 기록 {#query-history}

쿼리 빌더의 **쿼리 기록** 섹션에는 이전에 실행한 쿼리가 표시되어 작업을 추적하고 재사용하는 데 도움이 됩니다. 쿼리 기록은 7일간 보존되며, 7일이 지난 쿼리는 자동으로 제거됩니다.

더 긴 기간 동안 쿼리 사용을 감사하거나 7일 이후의 기록을 유지해야 하는 경우, 만료되기 전에 중요한 쿼리 결과를 내보내거나 저장하는 것을 권장합니다.

## AI 쿼리 빌더로 SQL 생성하기 {#generating-sql-with-the-ai-query-builder}

AI 쿼리 빌더는 OpenAI가 제공하는 [GPT](https://openai.com/gpt-4)를 활용하여 쿼리에 대한 SQL을 추천합니다.

![SQL AI 쿼리 빌더.]({% image_buster /assets/img_archive/query_builder_ai_tab.png %}){: style="max-width:60%;" }

AI 쿼리 빌더로 SQL을 생성하려면:

1. 쿼리 빌더에서 보고서를 생성한 후 **AI 쿼리 빌더** 탭을 선택합니다.
2. 프롬프트를 입력하거나 샘플 프롬프트를 선택하고 **생성**을 선택하여 프롬프트를 SQL로 변환합니다.
3. 생성된 SQL이 올바른지 검토한 다음 **편집기에 삽입**을 선택합니다.

### 팁 {#tips}

- [SQL 테이블 참조]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables)에서 사용 가능한 테이블과 열을 숙지하세요. 이러한 테이블에 존재하지 않는 데이터를 요청하면 ChatGPT가 가짜 테이블을 만들어낼 수 있습니다.
- 이 기능의 [SQL 작성 규칙]({{site.baseurl}}/user_guide/analytics/reports/query_builder#custom-sql)을 숙지하세요. 이러한 규칙을 따르지 않으면 오류가 발생합니다.
- AI 쿼리 빌더로 분당 최대 20개의 프롬프트를 보낼 수 있습니다.

#{% multi_lang_include brazeai/generative_ai/policy.md %}

## 커스텀 SQL 쿼리 작성하기 {#custom-sql}

[Snowflake 구문](https://docs.snowflake.com/en/sql-reference)을 사용하여 SQL 쿼리를 작성합니다. 쿼리할 수 있는 테이블과 열의 전체 목록은 [테이블 참조]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables)를 참조하세요.

쿼리 빌더 내에서 테이블 세부 정보를 보려면:

1. **쿼리 빌더** 페이지에서 **참조** 패널을 열고 **사용 가능한 데이터 테이블**을 선택하여 사용 가능한 데이터 테이블과 이름을 확인합니다.
3. <i class="fas fa-chevron-down" alt=""></i> **세부 정보 보기**를 선택하여 테이블 설명과 데이터 유형 등 테이블 열에 대한 정보를 확인합니다.
4. SQL에 테이블 이름을 삽입하려면 <i class="fas fa-copy" title="SQL 편집기에 테이블 이름 복사"></i> **SQL 편집기에 테이블 이름 복사**를 선택합니다.

Braze에서 제공하는 사전 작성된 쿼리를 사용하려면 쿼리 빌더에서 보고서를 처음 생성할 때 **쿼리 템플릿**을 선택합니다.

쿼리를 특정 기간으로 제한하면 결과를 더 빠르게 생성하는 데 도움이 됩니다. 다음은 최근 1시간 동안의 구매 수와 생성된 매출을 가져오는 예시 쿼리입니다.

```sql
SELECT COUNT(*) as Purchases, SUM(price) as Revenue
FROM USERS_BEHAVIORS_PURCHASE_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('hour', -1, date_trunc('day',CURRENT_DATE()));
```

이 쿼리는 지난 한 달간의 이메일 발송 수를 조회합니다:

```sql
SELECT COUNT(*) as Sends
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
WHERE to_date(to_timestamp_ntz(time)) >= DATEADD('month', -1, date_trunc('day',CURRENT_DATE()));
```

`CANVAS_ID`, `CANVAS_VARIATION_API_ID` 또는 `CAMPAIGN_ID`를 쿼리하면 관련 이름 열이 결과 테이블에 자동으로 포함됩니다. `SELECT` 쿼리 자체에 포함할 필요가 없습니다.

| ID 이름 | 관련 이름 열 |
| --- | --- |
| `CANVAS_ID` | Canvas Name |
| `CANVAS_VARIATION_API_ID` | Canvas Variant Name |
| `CAMPAIGN_ID` | Campaign Name |
{: .reset-td-br-1 .reset-td-br-2 aria-label="커스텀 SQL 쿼리 작성하기" }

이 쿼리는 세 가지 ID와 관련 이름 열을 최대 100행으로 조회합니다:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
LIMIT 100
```

### 캠페인 배리언트 이름 자동 채우기 {#automatically-populate-the-campaign-variant-name}

캠페인 배리언트 이름이 자동으로 채워지도록 하려면 다음 예시와 같이 쿼리에 `MESSAGE_VARIATION_API_ID` 열 이름을 포함합니다:

```sql
SELECT CANVAS_ID, CANVAS_VARIATION_API_ID, CAMPAIGN_ID, MESSAGE_VARIATION_API_ID
FROM USERS_MESSAGES_EMAIL_SEND_SHARED
LIMIT 100
```

### 문제 해결 {#troubleshooting}

쿼리는 다음과 같은 이유로 실패할 수 있습니다:

- SQL 쿼리의 구문 오류
- 처리 시간 초과(6분 후)
    - 실행하는 데 6분 이상 걸리는 보고서는 시간 초과됩니다.
    - 보고서가 시간 초과되면 데이터를 쿼리하는 시간 범위를 제한하거나 더 구체적인 데이터 세트를 쿼리해 보세요.

## 변수 사용하기 {#using-variables}

변수를 사용하면 SQL에서 사전 정의된 변수 유형을 사용하여 값을 수동으로 복사할 필요 없이 값을 참조할 수 있습니다. 예를 들어, Campaign의 ID를 SQL 편집기에 수동으로 복사하는 대신 {% raw %}`{{campaign.${My campaign}}}`{% endraw %}을 사용하여 **변수** 탭의 드롭다운에서 직접 Campaign을 선택할 수 있습니다.

변수가 생성되면 쿼리 빌더 보고서의 **변수** 탭에 표시됩니다. SQL 변수를 사용하면 다음과 같은 이점이 있습니다:

- Campaign ID를 붙여넣는 대신 보고서를 생성할 때 목록에서 선택할 수 있는 Campaign 변수를 만들어 시간을 절약합니다.
- 향후 약간 다른 사용 사례(예: 다른 커스텀 이벤트)에 대해 보고서를 재사용할 수 있도록 변수를 추가하여 값을 교체합니다.
- 각 보고서에 필요한 편집량을 줄여 SQL 편집 시 사용자 오류를 줄입니다. SQL에 더 익숙한 팀원이 보고서를 만들면 기술적 지식이 적은 팀원이 사용할 수 있습니다.

### 가이드라인 {#guidelines}

변수는 다음 Liquid 구문을 따라야 합니다: {% raw %}`{{ type.${name}}}`{% endraw %}, 여기서 `type`은 허용되는 유형 중 하나여야 하며 `name`은 원하는 이름을 지정할 수 있습니다. 이러한 변수의 레이블은 기본적으로 변수 이름으로 설정됩니다.

기본적으로 모든 변수는 필수입니다(변수 값이 선택되지 않으면 보고서가 실행되지 않음). 단, 날짜 범위는 값이 제공되지 않으면 기본적으로 최근 30일로 설정됩니다.

### 변수 유형 {#variable-types}

다음 변수 유형이 허용됩니다:

- [숫자](#number)
- [날짜 범위](#date-range)
- [메시징](#messaging)
- [제품](#products)
- [커스텀 이벤트](#custom-events)
- [커스텀 이벤트 속성](#custom-event-properties)
- [워크스페이스](#workspace)
- [카탈로그](#catalogs)
- [카탈로그 필드](#catalog-fields)
- [옵션](#options)
- [Segments](#segments)
- [문자열](#string)
- [태그](#tags)

#### 숫자 {#number}

- **대체 값:** 제공된 값(예: `5.5`)
- **사용 예시:** {% raw %}`some_number_column < {{number.${some name}}}`{% endraw %}

#### 날짜 범위 {#date-range}

`start_date`와 `end_date`를 모두 사용하는 경우 날짜 범위로 사용할 수 있도록 동일한 이름을 가져야 합니다.

##### 예시 값 {#example-values}

날짜 범위 유형은 상대적, 시작 날짜, 종료 날짜 또는 날짜 범위일 수 있습니다.

`start_date`와 `end_date`가 동일한 이름으로 모두 사용되면 네 가지 유형이 모두 표시됩니다. 하나만 사용되면 관련 유형만 표시됩니다.

| 날짜 범위 유형 | 설명 | 필수 값 |
| --- | --- | --- |
| 상대적 | 최근 X일을 지정합니다 | `start_date` 필요 |
| 시작 날짜 | 시작 날짜를 지정합니다 | `start_date` 필요 |
| 종료 날짜 | 종료 날짜를 지정합니다 | `end_date` 필요 |
| 날짜 범위 | 시작 날짜와 종료 날짜를 모두 지정합니다 | `start_date`와 `end_date` 모두 필요 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="예시 값" }

- **대체 값:** `start_date`와 `end_date`를 UTC 기준 지정된 날짜의 Unix 타임스탬프(초 단위)로 대체합니다(예: `1696517353`).
- **사용 예시:** 상대적, 시작 날짜, 종료 날짜 및 날짜 범위 변수 모두에 대해:
    - {% raw %}`time > {{start_date.${some name}}} AND time < {{end_date.${some name}}}` {% endraw %}
        - 날짜 범위가 필요하지 않은 경우 `start_date` 또는 `end_date`만 사용할 수 있습니다.

#### 메시징 {#messaging}

모든 메시징 변수는 하나의 그룹에서 상태를 연결하려면 동일한 식별자를 공유해야 합니다.

##### Canvas

하나의 Canvas를 선택하기 위한 변수입니다. Campaign과 동일한 이름을 공유하면 **변수** 탭에 Canvas 또는 Campaign 중 하나를 선택하는 라디오 버튼이 표시됩니다.

- **대체 값:** Canvas BSON ID
- **사용 예시:** {% raw %}`canvas_id = '{{canvas.${some name}}}'`{% endraw %}

##### Canvases

여러 Canvases를 선택하기 위한 변수입니다. Campaign과 동일한 이름을 공유하면 **변수** 탭에 Canvas 또는 Campaign 중 하나를 선택하는 라디오 버튼이 표시됩니다.

- **대체 값:** Canvases BSON ID
- **사용 예시:** {% raw %}`canvas_id IN ({{canvases.${some name}}})`{% endraw %}

##### Campaign

하나의 Campaign을 선택하기 위한 변수입니다. Canvas와 동일한 이름을 공유하면 **변수** 탭에 Canvas 또는 Campaign 중 하나를 선택하는 라디오 버튼이 표시됩니다.

- **대체 값:** Campaign BSON ID
- **사용 예시:** {% raw %}`campaign_id = '{{campaign.${some name}}}'`{% endraw %}

##### Campaigns

여러 Campaigns를 다중 선택하기 위한 변수입니다. Canvas와 동일한 이름을 공유하면 **변수** 탭에 Canvas 또는 Campaign 중 하나를 선택하는 라디오 버튼이 표시됩니다.

- **대체 값:** Campaigns BSON ID
- **사용 예시:** {% raw %}`campaign_id IN ({{campaigns.${some name}}})`{% endraw %}

##### 캠페인 배리언트 {#campaign-variants}

선택한 Campaign에 속하는 캠페인 배리언트를 선택하기 위한 변수입니다. Campaign 또는 Campaigns 변수와 함께 사용해야 합니다.

- **대체 값:** 캠페인 배리언트 API ID, 쉼표로 구분된 문자열(예: `api-id1, api-id2`)
- **사용 예시:** {% raw %}`message_variation_api_id IN ({{campaign_variants.${some name}}})`{% endraw %}

##### 캔버스 배리언트 {#canvas-variants}

선택한 Canvas에 속하는 캔버스 배리언트를 선택하기 위한 변수입니다. Canvas 또는 Canvases 변수와 함께 사용해야 합니다.

- **대체 값:** 캔버스 배리언트 API ID, 쉼표로 구분된 문자열(예: `api-id1, api-id2`)
- **사용 예시:** {% raw %}`canvas_variation_api_id IN ({{canvas_variants.${some name}}})`{% endraw %}

##### 캔버스 단계 {#canvas-step}

선택한 Canvas에 속하는 캔버스 단계를 선택하기 위한 변수입니다. Canvas 변수와 함께 사용해야 합니다.

- **대체 값:** 캔버스 단계 API ID
- **사용 예시:** {% raw %}`canvas_step_api_id = '{{canvas_step.${some name}}}'`{% endraw %}

##### 캔버스 단계(복수) {#canvas-steps}

선택한 Canvases에 속하는 캔버스 단계를 선택하기 위한 변수입니다. Canvas 또는 Canvases 변수와 함께 사용해야 합니다.

- **대체 값:** 캔버스 단계 API ID
- **사용 예시:** {% raw %}`canvas_step_api_id IN ({{canvas_steps.${some name}}})`{% endraw %}