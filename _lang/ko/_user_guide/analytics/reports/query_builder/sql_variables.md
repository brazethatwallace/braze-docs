---
nav_title: SQL 변수
article_title: 쿼리 빌더 SQL 변수
page_order: 2
page_type: reference
description: "쿼리 빌더에서 변수를 사용하여 쿼리를 재사용하고 코드에 데이터를 하드코딩하지 않는 방법을 알아보세요."
tool: Reports
---

# 쿼리 빌더 SQL 변수 {#query-builder-sql-variables}

> 쿼리 빌더에서 SQL 변수를 사용하여 쿼리를 재사용하고 코드에 데이터를 하드코딩하지 않는 방법을 알아보세요.

## SQL 변수를 사용하는 이유 {#why-use-sql-variables}

SQL 변수를 사용하면 다음과 같은 이점이 있습니다:

{% multi_lang_include analytics/sql_variables_benefits.md %}

## 변수 사용하기 {#using-variables}

### 1단계: 변수 추가 {#step-1-add-a-variable}

쿼리에 변수를 추가하려면 다음 구문을 사용합니다:

{% raw %}
```sql
{{variable_type.${custom_label}}}
```
{% endraw %}

다음을 교체합니다:

| 입력 안내 | 설명 |
|------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| `variable_type` | 사용하려는 사전 정의된 변수 유형(예: `campaign` 또는 `catalog_fields`). 전체 목록은 [지원되는 변수 유형](#variable-types)을 참조하세요. |
| `custom_label` | 쿼리 빌더의 **변수** 탭에서 변수를 식별하는 데 사용되는 레이블입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="1단계: 변수 추가" }

다음 예시에서는 한 달의 첫째 날과 마지막 날 사이의 총 사용자 수를 Campaign에 대해 쿼리합니다. 각 변수에는 다음 단계에서 값이 할당됩니다.

{% raw %}
```sql
SELECT COUNT(*) AS total_users
FROM USERS_CAMPAIGNS_REVENUE_SHARED
WHERE campaign_id = '{{campaign.${Campaign}}}'
  AND TIME > '{{start_date.${Month First Day}}}'
  AND TIME < '{{end_date.${Month Last Day}}}';
```
{% endraw %}

### 2단계: 값 할당 {#step-2-assign-a-value}

기본적으로 **변수** 탭은 쿼리 빌더에 표시되지 않습니다. 쿼리에 첫 번째 변수를 추가한 후에만 나타납니다. 거기에서 값을 할당할 수 있습니다. 선택할 수 있는 구체적인 값은 해당 변수의 [유형](#variable-types)에 따라 달라집니다.

다음 예시에서는 "Summer Feature Launch" Campaign이 값으로 할당되며, 2025년 6월의 첫째 날과 마지막 날도 함께 지정됩니다.

![주어진 예시를 보여주는 쿼리 빌더의 "변수" 탭.]({% image_buster /assets/img/query_builder_example.png %})

## 일반 변수 유형 {#variable-types}

### 숫자 {#number}

`number`는 문자열이 아닌 다른 변수와 조합하여 사용할 수 있습니다. `5.5`와 같은 소수를 포함하여 양수 또는 음수를 허용합니다.

{% tabs %}
{% tab 사용법 %}
{% raw %}
```sql
some_number_column < {{number.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### 문자열 {#string}

보고서 실행 간에 반복되는 문자열 값을 변경하는 데 사용합니다. SQL에서 값을 여러 번 하드코딩하지 않으려면 이 변수를 사용하세요.

{% tabs %}
{% tab 사용법 %}
{% raw %}
```sql
'{{string.${add a string here.}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### 목록 {#list}

옵션 목록에서 선택하는 데 사용합니다.

{% tabs local %}
{% tab 하나 선택 %}
{% subtabs %}
{% subtab 사용법 %}
{% raw %}
```sql
{{options.${metrics} | is_radio_button: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 여러 개 선택 %}
{% subtabs %}
{% subtab 사용법 %}
{% raw %}
```sql
{{options.${metrics} | is_multi_select: 'true' | options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### 라디오 버튼 {#radio-button}

**변수** 탭에서 선택 드롭다운 대신 라디오 버튼으로 옵션을 표시하는 데 사용합니다. 단독으로 사용할 수 없으며&#8212;[목록](#list)과 함께 사용해야 합니다.

{% tabs %}
{% tab 사용법 %}
```sql
is_radio_button: 'true'
```
{% endtab %}
{% endtabs %}

![Braze에서 렌더링된 라디오 버튼 예시.]({% image_buster /assets/img_archive/sql_variables_campaigns.png %}){: style="max-width:50%;"}

#### 다중 선택 {#multi-select}

선택 드롭다운에서 단일 선택 또는 다중 선택을 허용할지 여부를 설정합니다. 단독으로 사용할 수 없으며&#8212;[목록](#list)과 함께 사용해야 합니다.

{% tabs %}
{% tab 사용법 %}
```sql
is_multi_select: 'true'
```
{% endtab %}
{% endtabs %}

![Braze에서 렌더링된 다중 선택 목록 예시.]({% image_buster /assets/img_archive/sql_variables_productname.png %}){: style="max-width:50%;"}

#### 옵션 {#options}

레이블과 값 형태로 선택 가능한 옵션 목록을 제공하는 데 사용합니다. 레이블은 표시되는 내용이고, 값은 옵션이 선택될 때 변수가 대체되는 내용입니다. 단독으로 사용할 수 없으며&#8212;[목록](#list)과 함께 사용해야 합니다.

{% tabs %}
{% tab 사용법 %}
```sql
options: '[{"label": "test", "value": "test_value"}, {"label": "test2", "value": "test_value2"}]'
```
{% endtab %}
{% endtabs %}

## Braze 전용 변수 유형 {#braze-specific-variable-types}

### 날짜 범위 {#date-range}

날짜를 선택할 수 있는 캘린더를 표시하는 데 사용합니다. `start_date`와 `end_date`를 UTC 기준 지정된 날짜의 Unix 타임스탬프(초 단위)로 교체합니다(예: `1696517353`). 선택적으로 `start_date` 또는 `end_date`만 설정하여 캘린더에 단일 날짜만 표시할 수도 있습니다. `start_date`와 `end_date`의 레이블이 일치하지 않으면 날짜 범위가 아닌 두 개의 별도 날짜로 처리됩니다.

{% tabs %}
{% tab 사용법 %}
{% raw %}
```
time > {{start_date.${custom_label}}} AND time < {{end_date.${custom_label}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

날짜 범위를 다음 옵션 중 하나로 설정할 수 있습니다. `start_date`와 `end_date`가 모두 사용되고 동일한 레이블을 공유하면 모든 옵션이 표시됩니다. 그렇지 않고 하나만 사용되면 지정된 옵션만 표시됩니다.

| 옵션 | 설명 | 필수 값 |
| --- | --- | --- |
| 상대적 | 지난 X일을 지정합니다 | `start_date` 필요 |
| 시작 날짜 | 시작 날짜를 지정합니다 | `start_date` 필요 |
| 종료 날짜 | 종료 날짜를 지정합니다 | `end_date` 필요 |
| 날짜 범위 | 시작 날짜와 종료 날짜를 모두 지정합니다 | `start_date`와 `end_date` 모두 필요 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="날짜 범위" }

Liquid는 지정된 날짜 범위 내에서 캘린더를 표시하는 데 사용됩니다:

![Braze에서 렌더링된 캘린더 예시.]({% image_buster /assets/img_archive/query_builder_time_range.png %}){: style="max-width:50%;"}

### Campaigns {#campaigns}

{% tabs local %}
{% tab 단일 Campaign %}
하나의 Campaign을 선택하는 데 사용합니다. Canvas와 동일한 레이블을 공유하면 **변수** 탭에 Canvas 또는 Campaign 중 하나를 선택할 수 있는 라디오 버튼이 표시됩니다.

{% subtabs %}
{% subtab 사용법 %}
{% raw %}
```sql
campaign_id = '{{campaign.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 다중 Campaign %}
여러 Campaign을 다중 선택하는 데 사용합니다. Canvas와 동일한 레이블을 공유하면 **변수** 탭에 Canvas 또는 Campaign 중 하나를 선택할 수 있는 라디오 버튼이 표시됩니다.

- **대체 값:** Campaigns BSON ID

{% subtabs %}
{% subtab 사용법 %}
{% raw %}
```sql
campaign_id IN ({{campaigns.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 캠페인 배리언트 %}
선택한 Campaign에 속하는 캠페인 배리언트를 선택하는 데 사용합니다. Campaign 또는 Campaigns 변수와 함께 사용해야 합니다.

- **대체 값:** 캠페인 배리언트 API ID, 쉼표로 구분된 문자열(예: `api-id1, api-id2`).

{% subtabs %}
{% subtab 사용법 %}
{% raw %}
```sql
message_variation_api_id IN ({{campaign_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
모든 Campaign 및 Canvas 변수는 단일 그룹 내에서 상태를 동기화하기 위해 동일한 식별자를 사용해야 합니다.
{% endalert %}

### Canvases {#canvases}

{% tabs local %}
{% tab 단일 Canvas %}
하나의 Canvas를 선택하는 데 사용합니다. Campaign과 동일한 레이블을 공유하면 **변수** 탭에 Canvas 또는 Campaign 중 하나를 선택할 수 있는 라디오 버튼이 표시됩니다.

- **대체 값:** Canvas BSON ID

{% subtabs %}
{% subtab 사용법 %}
{% raw %}
```sql
canvas_id = '{{canvas.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 다중 Canvas %}
여러 Canvas를 선택하는 데 사용합니다. Campaign과 동일한 레이블을 공유하면 **변수** 탭에 Canvas 또는 Campaign 중 하나를 선택할 수 있는 라디오 버튼이 표시됩니다.

- **대체 값:** Canvases BSON ID

{% subtabs %}
{% subtab 사용법 %}
{% raw %}
```sql
canvas_id IN ({{canvases.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 캔버스 배리언트 %}
선택한 Canvas에 속하는 캔버스 배리언트를 선택하는 데 사용합니다. Canvas 또는 Canvases 변수와 함께 사용해야 합니다. 쉼표로 구분된 문자열로 하나 이상의 캔버스 배리언트 API ID를 설정합니다(예: `api-id1, api-id2`).

{% subtabs %}
{% subtab 사용법 %}
{% raw %}
```sql
canvas_variation_api_id IN ({{canvas_variants.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 단일 캔버스 단계 %}
선택한 Canvas에 속하는 캔버스 단계를 선택하는 데 사용합니다. Canvas 변수와 함께 사용해야 합니다.

{% subtabs %}
{% subtab 사용법 %}
{% raw %}
```sql
canvas_step_api_id = '{{canvas_step.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 다중 캔버스 단계 %}
선택한 Canvases에 속하는 캔버스 단계를 선택하는 데 사용합니다. Canvas 또는 Canvases 변수와 함께 사용해야 합니다.

{% subtabs %}
{% subtab 사용법 %}
{% raw %}
```sql
canvas_step_api_id IN ({{canvas_steps.${custom_label}}})
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert important %}
모든 Campaign 및 Canvas 변수는 단일 그룹 내에서 상태를 동기화하기 위해 동일한 식별자를 사용해야 합니다.
{% endalert %}

### 제품 {#products}

`products`는 Braze 대시보드에서 하나 이상의 제품을 선택하는 데 사용합니다.

{% tabs %}
{% tab 사용법 %}
{% raw %}
```sql
({{products.${custom_label}}})
```
{% endraw %}
{% endtab %}

{% tab 예시 %}
{% raw %}
```sql
SELECT product_name
FROM FULL_GAME_AND_DLC
WHERE product_id IN ({{products.${Games with DLC}}});
```
{% endraw %}
{% endtab %}
{% endtabs %}

### 커스텀 이벤트 {#custom-events}

목록에서 하나 이상의 커스텀 이벤트 또는 커스텀 이벤트 속성정보를 선택합니다.

{% tabs local %}
{% tab 이벤트 %}
`custom_events`는 Braze 대시보드에서 하나 이상의 커스텀 이벤트를 선택하는 데 사용합니다.

{% subtabs %}
{% subtab 사용법 %}
{% raw %}
```sql
'{{custom_events.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}

{% subtab 예시 %}
{% raw %}
```sql
SELECT event_name
FROM CUSTOM_EVENTS_TABLE
WHERE event_name IN ({{custom_events.${Purchased Game}}});
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 속성정보 %}
`custom_event_properties`는 현재 선택된 커스텀 이벤트에서 하나 이상의 속성정보를 선택하는 데 사용합니다. `custom_events` 변수가 설정되어 있어야 합니다.

{% subtabs %}
{% subtab 사용법 %}
{% raw %}
```sql
name = '{{custom_event_properties.${property names)}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### 워크스페이스 {#workspace}

`workspace`는 Braze 대시보드에서 단일 워크스페이스를 선택하는 데 사용합니다.

{% tabs %}
{% tab 사용법 %}
{% raw %}
```sql
workspace_id = '{{workspace.${app_group_id}}}'
```
{% endraw %}
{% endtab %}
{% endtabs %}

### 카탈로그 {#catalogs}

목록에서 하나 이상의 카탈로그 또는 카탈로그 필드를 선택합니다.

{% tabs local %}
{% tab 카탈로그 %}
`catalogs`는 Braze 대시보드에서 하나 이상의 카탈로그를 선택하는 데 사용합니다.

{% subtabs %}
{% subtab 사용법 %}
{% raw %}
```sql
catalog_id = '{{catalogs.${catalog}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 카탈로그 필드 %}
`catalog_fields`는 현재 선택된 카탈로그에서 하나 이상의 필드를 설정하는 데 사용합니다. `catalogs` 변수가 설정되어 있어야 합니다.

{% subtabs %}
{% subtab 사용법 %}
{% raw %}
```sql
field_name = '{{catalog_fields.${custom_label}}}'
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Segments {#segments}

[분석 추적]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking)이 활성화된 Segments를 선택하는 데 사용합니다. 이 열이 사용 가능한 테이블의 `user_segment_membership_ids` 열에 저장된 ID에 해당하는 Segment 분석 ID로 설정합니다.

{% tabs %}
{% tab 사용법 %}
{% raw %}
```sql
{{segments.${analytics_segments}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### 태그 {#tags}

Campaigns 및 Canvases의 태그를 선택하는 데 사용합니다. 선택한 태그와 연결된 작은따옴표로 구분된 쉼표 구분 BSON ID를 가진 Campaigns 및 Canvases로 설정됩니다.

{% tabs %}
{% tab 사용법 %}
{% raw %}
```sql
{{tags.${some tags}}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

## 변수 메타데이터 {#variable-metadata}

메타데이터는 변수 레이블 뒤에 파이프( &#124; ) 문자를 추가하여 변수에 첨부할 수 있으며, 이를 통해 변수의 동작을 변경할 수 있습니다. 메타데이터의 순서는 중요하지 않으며 원하는 수만큼 추가할 수 있습니다. 또한 특정 변수에만 해당하는 특수 메타데이터를 제외하고 모든 유형의 메타데이터를 모든 변수에 사용할 수 있습니다(해당하는 경우 표시됩니다). 모든 메타데이터의 사용은 선택 사항이며 변수의 기본 동작을 변경하는 데 사용됩니다.

{% tabs %}
{% tab 사용법 %}
{% raw %}
```sql
{{string.${my var}| is_required: 'false' | description: 'My optional string var'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### 부울 {#boolean}

변수의 값이 채워져 있는지 여부를 확인하는 데 사용합니다. 변수의 값이 채워지지 않은 경우 조건을 단축하려는 선택적 변수에 유용합니다. 다른 변수의 값에 따라 `true` 또는 `false`로 설정할 수 있습니다.

{% tabs %}
{% tab 사용법 %}
{% raw %}
```sql
{{string.${type_name_has_no_value} | visible: 'false'}} or {{string.${type_name_has_value} | visible: 'false'}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

`type`과 `name`은 참조되는 변수를 나타냅니다. 예를 들어, 다음 선택적 변수를 단축하려면: {% raw %}`{{campaigns.${messaging}}`{% endraw %}:

{% raw %}
```sql
{{string.${campaigns_messaging_has_no_value}  | visible: 'false'}} OR campaign_id IN ({{campaigns.${messaging} | is_required: 'false'}})
```
{% endraw %}

### 표시 여부 {#visible}

변수가 표시되는지 여부를 설정합니다. 모든 변수는 기본적으로 **변수** 탭에 표시되며, 여기에서 값을 입력할 수 있습니다.

다른 변수에 값이 있는지 여부 등 다른 변수에 의존하는 값을 가진 특수 변수가 여러 개 있습니다. 이러한 특수 변수는 **변수** 탭에 표시되지 않도록 비표시로 설정됩니다.

{% tabs %}
{% tab 사용법 %}
```sql
visible: 'false'
```
{% endtab %}
{% endtabs %}

### 필수 {#required}

변수가 기본적으로 필수인지 여부를 설정합니다. 변수의 빈 값은 일반적으로 잘못된 쿼리로 이어집니다.

{% tabs %}
{% tab 사용법 %}
```sql
required: 'false'
```
{% endtab %}
{% endtabs %}

### 순서 {#order}

**변수** 탭에서 변수의 위치를 선택하는 데 사용합니다.

{% tabs %}
{% tab 사용법 %}
```sql
order: '1'
```
{% endtab %}
{% endtabs %}

### 따옴표 포함 {#include-quotes}

{% tabs local %}
{% tab 작은따옴표 %}
변수의 값을 작은따옴표로 감싸는 데 사용합니다.

{% subtabs %}
{% subtab 사용법 %}
```sql
include_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 큰따옴표 %}
변수의 값을 큰따옴표로 감싸는 데 사용합니다.

{% subtabs %}
{% subtab 사용법 %}
```sql
include_double_quotes: 'true'
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### 입력 안내 텍스트 {#placeholder}

변수의 입력 필드에 표시되는 입력 안내 텍스트를 지정하는 데 사용합니다.

{% tabs %}
{% tab 사용법 %}
```sql
placeholder: 'enter some value'
```
{% endtab %}
{% endtabs %}

### 설명 {#description}

변수의 입력 필드 아래에 표시되는 설명 텍스트를 지정하는 데 사용합니다.

{% tabs %}
{% tab 사용법 %}
```sql
description: 'some description'
```
{% endtab %}
{% endtabs %}

### 기본값 {#default-value}

값이 지정되지 않은 경우 변수의 기본값을 지정하는 데 사용합니다.

{% tabs %}
{% tab 사용법 %}
```sql
default_value: '5'
```
{% endtab %}
{% endtabs %}

### 레이블 숨기기 {#hide-label}

변수의 레이블을 숨기는 데 사용합니다.

{% tabs %}
{% tab 사용법 %}
```sql
hide_label: 'true'
```
{% endtab %}
{% endtabs %}