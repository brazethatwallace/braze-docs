# SQL 세그먼트 확장 {#sql-segment-extensions}

> [Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) 데이터의 Snowflake SQL 쿼리를 사용하여 세그먼트 확장을 생성할 수 있습니다. SQL은 다른 세분화 기능으로는 달성할 수 없는 방식으로 데이터 간의 관계를 설명할 수 있는 유연성을 제공하기 때문에 새로운 세그먼트 사용 사례를 발굴하는 데 도움이 됩니다.
>
> 표준 세그먼트 확장과 마찬가지로 SQL 세그먼트 확장에서 최대 2년(730일)까지의 이벤트를 쿼리할 수 있습니다. 표준 세그먼트 확장과 달리 SQL 세그먼트 확장은 [크레딧을 소모합니다](#credits).

## 필수 조건 {#prerequisites}

이 기능을 통해 PII 데이터에 접근할 수 있으므로, SQL 세그먼트 쿼리를 실행하려면 PII 권한이 반드시 필요합니다.

## 세그먼트 확장 생성하기 {#creating-a-segment-extension}

### 1단계: 편집기 선택 {#step-1-choose-an-editor}

SQL 세그먼트 확장을 만들 때 선택할 수 있는 SQL 편집기에는 SQL 편집기와 증분 SQL 편집기의 두 가지 유형이 있습니다.

- **전체 새로고침:** 세그먼트가 새로고침될 때마다 Braze는 사용 가능한 모든 데이터를 쿼리하여 세그먼트를 업데이트하며, 이때 증분 새로고침보다 더 많은 크레딧이 사용됩니다. 전체 새로고침 확장은 멤버십을 매일 자동으로 재생성할 수 있지만 증분 새로고침으로는 재생성할 수 없습니다.
- **증분 새로고침:** 증분 새로고침은 쿼리를 설정하는 데 더 비용 효율적인 방법이지만, 설정에 몇 가지 추가 [단계가](#step-2-write-your-sql) 필요합니다. 세그먼트를 구성할 때 이러한 추가 단계를 완료할 수 있다면, 쿼리가 더 적은 크레딧으로 실행되므로 이 옵션을 선택하는 것이 좋습니다.
- **AI SQL 생성기:** AI SQL 생성기는 일반 언어로 프롬프트를 작성하면 해당 세그먼트에 대한 SQL 쿼리로 변환해 줍니다. SQL을 직접 작성하지 않고도 빠르게 시작할 수 있는 방법입니다.

{% alert tip %}
두 SQL 편집기에서 생성된 모든 SQL Segments에 대해 수동으로 전체 새로고침을 수행할 수 있습니다.
{% endalert %}

{% tabs local %}
{% tab Full refresh %}

전체 새로고침 SQL 세그먼트 확장을 만들려면 다음과 같이 하세요:

1. **오디언스** > **세그먼트 확장**으로 이동합니다.
2. **Create New Extension**을 선택한 후 **Full refresh**를 선택합니다.<br><br>
   ![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. 세그먼트 확장의 이름을 추가하고 SQL을 입력합니다. 요구 사항 및 리소스에 대해서는 [2단계](#step-2-write-your-sql)를 참조하세요.<br><br>
   ![SQL 편집기에 표시된 SQL 세그먼트 확장 예시.]({% image_buster /assets/img_archive/sql_segments_editor.png %}){: style="max-width:60%" }<br><br>
4. 세그먼트 확장을 저장합니다.

{% endtab %}
{% tab Incremental refresh %}

증분 새로고침 SQL 세그먼트 확장을 만들려면 다음과 같이 하세요:

1. **오디언스** > **세그먼트 확장**으로 이동합니다.
2. **Create New Extension**을 선택하고 **Incremental refresh**를 선택합니다.<br><br>
   ![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. 세그먼트 확장의 이름을 추가하고 SQL을 입력합니다. 요구 사항 및 리소스는 [SQL 작성하기](#writing-sql) 섹션을 참조하세요.<br><br>
   ![증분 SQL 세그먼트 확장의 예시를 보여주는 SQL 편집기.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:60%" }<br><br>
4. 원하는 경우 **Regenerate Extension Daily**를 선택합니다.<br><br>
   ![확장을 매일 재생성하는 체크박스.]({% image_buster /assets/img_archive/sql_segments_regenerate.png %}){: style="max-width:60%" }<br><br>
   이 옵션을 선택하면 Braze가 매일 자동으로 세그먼트 멤버십을 업데이트합니다. 즉, 매일 자정(최대 1시간 지연 가능)에 회사 시간대 기준으로 Braze가 세그먼트에 새로운 사용자가 있는지 확인하고 자동으로 추가합니다. 7일 동안 세그먼트 확장을 사용하지 않은 경우, Braze는 자동으로 일일 재생성을 일시 중지합니다. 사용하지 않은 세그먼트 확장은 Campaign 또는 Canvas에 포함되지 않은 확장을 말합니다(Campaign 또는 Canvas가 활성 상태가 아니어도 확장은 "사용 중"으로 간주됩니다).<br><br>
5. 세그먼트 확장을 저장합니다.

{% endtab %}

{% tab AI SQL Generator %}

{% alert note %}
AI SQL 생성기는 현재 베타 기능으로 제공되고 있습니다. 이 베타 체험에 참여하려면 고객 성공 매니저에게 문의하세요.
{% endalert %}

AI SQL 생성기는 OpenAI가 제공하는 [GPT](https://openai.com/gpt-4)를 활용하여 SQL 세그먼트에 맞는 SQL을 추천합니다.

!["지난 달 알림을 받은 사용자" 프롬프트가 입력된 AI SQL 생성기]({% image_buster /assets/img/ai_sql_generator.png %}){: style="max-width:70%;"}

AI SQL 생성기를 사용하려면 다음과 같이 하세요:

1. 전체 또는 증분 새로고침을 사용하여 [SQL 세그먼트]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/)를 생성한 후 **Launch AI SQL Generator**를 선택합니다.
2. 프롬프트를 입력하고 **Generate**를 선택하여 프롬프트를 SQL로 변환합니다.
3. 생성된 SQL을 검토하여 올바른지 확인한 다음 세그먼트를 저장합니다.

#### 프롬프트 예시 {#example-prompts}

- 지난 달에 이메일을 받은 사용자
- 지난 1년간 구매 횟수가 5회 미만인 사용자

#### 팁 {#tips}

- 사용 가능한 [Snowflake 데이터 테이블]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/)을 숙지하세요. 이러한 테이블에 존재하지 않는 데이터를 요청하면 ChatGPT가 가짜 테이블을 만들어낼 수 있습니다.
- 이 기능에 대한 [SQL 작성 규칙]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments?tab=sql%20editor#writing-sql)을 숙지하세요. 이러한 규칙을 따르지 않으면 오류가 발생합니다. 예를 들어 SQL 코드에서 `user_id` 열을 선택해야 합니다. "users who"로 프롬프트를 시작하면 도움이 될 수 있습니다.
- AI SQL 생성기를 사용하면 분당 최대 20개의 프롬프트를 보낼 수 있습니다.

##{% multi_lang_include brazeai/generative_ai/policy.md %}

{% endtab %}
{% endtabs %}

{% alert note %}
실행하는 데 20분 이상 걸리는 SQL 쿼리는 시간 초과됩니다.
{% endalert %}

확장 처리가 완료되면 세그먼트 확장을 사용하여 [세그먼트를 생성]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#step-5-use-your-extension-in-a-segment)하고, Campaign 및 Canvases를 통해 이 새 세그먼트를 타겟팅할 수 있습니다.

### 2단계: SQL 작성하기 {#step-2-write-your-sql}

SQL 쿼리는 [Snowflake 구문](https://docs.snowflake.com/en/sql-reference.html)을 사용하여 작성해야 합니다. 쿼리할 수 있는 테이블과 열의 전체 목록은 [테이블 참조]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/)를 확인하세요.

{% alert important %}
쿼리할 수 있는 테이블에는 이벤트 데이터만 포함되어 있다는 점에 유의하세요. 사용자 속성을 쿼리하려면 SQL 세그먼트와 [기존 세그멘터]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)의 커스텀 속성 필터를 결합해야 합니다.
{% endalert %}

{% tabs %}
{% tab SQL Editor %}

SQL은 다음 규칙을 추가로 준수해야 합니다:

- 하나의 SQL 문을 작성합니다. 세미콜론을 포함하지 마세요.
- SQL은 하나의 열, 즉 `user_id` 열만 선택해야 합니다. 즉, SQL에 다음이 포함되어야 합니다:

```sql
SELECT DISTINCT user_id FROM "INSERT TABLE NAME"
```

- 이벤트가 0건인 사용자에 대해서는 쿼리할 수 없으므로, 이벤트를 X회 미만 수행한 사용자에 대한 쿼리는 다음 해결 방법을 따라야 합니다:
   1. 이벤트가 X회 이상인 사용자를 선택하는 쿼리를 작성합니다.
   2. 세그먼트에서 세그먼트 확장을 참조할 때 `doesn't include`를 선택하여 결과를 반전시킵니다.

#### 추가 규칙 {#additional-rules}

또한 표준 SQL 쿼리는 다음 규칙을 준수해야 합니다:

- `DECLARE` 문을 사용할 수 없습니다.
{% endtab %}
{% tab Incremental SQL Editor %}

모든 증분 새로고침 쿼리는 쿼리와 스키마 세부 정보의 두 부분으로 구성됩니다.

1. 편집기에서 원하는 테이블에서 `user_id`를 선택하는 쿼리를 작성합니다.
2. 편집기 위의 필드에서 **Operator**, **Number of times**, **Time period**를 선택하여 스키마 세부 정보를 추가합니다. 쿼리는 집계 열의 합계가 {% raw %}`{{operator}}` 및 `{{number of times}}`{% endraw %} 플레이스홀더로 지정된 특정 조건을 충족하는지 확인합니다. 이는 기존 세그먼트 확장을 만드는 워크플로와 유사하게 작동합니다.<br><br>
   - **Operator:** 이벤트가 발생 횟수보다 많거나, 적거나, 같은 횟수로 발생했는지 표시합니다.<br>
   !["More than"이 선택된 Operator 필드.]({% image_buster /assets/img_archive/sql_segments_operator.png %})<br><br>
   - **Number of times:** Operator와 관련하여 이벤트를 몇 번 평가할지 입력합니다.<br>
   !["5"가 입력된 Number of times 필드.]({% image_buster /assets/img_archive/sql_segments_times.png %})<br><br>
   - **Time period:** 이벤트 인스턴스를 확인하려는 1~730일 사이의 일 수입니다. 이 기간은 현재 날짜를 기준으로 과거 일수를 나타냅니다. 다음 예는 지난 365일 동안 이벤트를 5회 이상 수행한 사용자에 대한 쿼리를 보여줍니다.<br>
   !["365"가 입력된 Time period 필드.]({% image_buster /assets/img_archive/sql_segments_period.png %})

다음 예제에서 결과 세그먼트에는 지정된 날짜 이후 지난 30일 동안 `favorited` 이벤트를 3회 이상 수행한 사용자가 포함됩니다.

![증분 SQL 세그먼트 확장의 예시를 보여주는 SQL 편집기.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:65%" }

![증분 SQL 세그먼트 확장의 SQL 미리보기.]({% image_buster /assets/img_archive/sql_segments_incremental_preview.png %}){: style="max-width:85%" }

{% alert tip %}
증분 새로고침 세그먼트는 2일 이상 전에 발생한 이벤트인 지연 이벤트(예: 캡처 시점에 전송되지 않은 SDK 이벤트)를 고려합니다.
{% endalert %}

#### 추가 규칙

또한 증분 새로고침 쿼리는 다음 규칙을 준수해야 합니다:

- 하나의 SQL 문을 작성합니다. 세미콜론을 포함하지 마세요.
- 증분 SQL 세그먼트는 하나의 단일 이벤트만 참조할 수 있습니다. 날짜 및 개수에 대한 드롭다운은 선택한 이벤트를 기준으로 합니다.
- SQL에는 `user_id`, `$start_date` 열과 집계 함수(예: `COUNT`)가 있어야 합니다. 이 세 필드 없이 저장된 SQL은 오류가 발생합니다.
- `DECLARE` 문을 사용할 수 없습니다.
{% endtab %}
{% endtabs %}

{% alert note %}
`CATALOGS_ITEMS_SHARED` 테이블을 사용하는 SQL 세그먼트를 생성하는 경우 카탈로그 ID를 지정해야 합니다. 예를 들어:

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### 3단계: 쿼리 미리보기 {#step-3-preview-the-query}

저장하기 전에 쿼리 미리보기를 실행할 수 있습니다. 쿼리 미리보기는 자동으로 100개 행으로 제한되며 60초 후에 시간 초과됩니다. 미리보기를 실행할 때는 `user_id` 열 요구 사항이 적용되지 않습니다.

증분 SQL 세그먼트 확장의 경우 미리보기에는 Operator, Number of times 및 Time period 필드의 추가 기준이 포함되지 않습니다.

### 4단계: SQL 반전 필요 여부 판단 {#step-4-determine-if-you-need-to-invert-sql}

다음으로, SQL을 반전시켜야 하는지 판단합니다. 이벤트가 0건인 사용자를 직접 쿼리할 수는 없지만, **Invert SQL**을 사용하여 해당 사용자를 타겟팅할 수 있습니다.

{% alert note %}
기본적으로 **Invert SQL**은 토글되어 있지 않습니다. 그러나 부정이 필요한 SQL 문을 생성하기 위해 AI SQL 생성기를 사용할 경우, ChatGPT가 이 기능을 자동으로 토글하는 출력을 반환할 수 있습니다.
{% endalert %}

예를 들어, 구매 횟수가 3회 미만인 사용자를 타겟팅하려면, 먼저 구매 횟수가 3회 이상인 사용자를 선택하는 쿼리를 작성합니다. 그런 다음 **Invert SQL**을 선택하여 구매 횟수가 3회 미만인 사용자(구매 횟수가 0인 사용자 포함)를 타겟팅합니다.

{% alert important %}
이벤트가 전혀 없는 사용자를 특별히 타겟팅하려는 경우가 아니라면 SQL을 반전시킬 필요가 없습니다. **Invert SQL**이 선택된 경우, 해당 기능이 필요한지 확인하고 세그먼트가 원하는 오디언스와 일치하는지 확인하세요. 예를 들어, 쿼리가 최소 한 건의 이벤트가 있는 사용자를 타겟팅하는 경우, 이를 반전하면 이벤트가 전혀 없는 사용자만 타겟팅합니다.
{% endalert %}

!["지난 30일 동안 1~4개의 이메일을 클릭함"이라는 세그먼트 확장에 SQL 반전 옵션이 선택된 상태.]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:90%;"}

## 세그먼트 멤버십 새로고침 {#refreshing-segment-membership}

SQL을 사용하여 생성한 세그먼트 확장의 세그먼트 멤버십을 새로고침하려면 세그먼트 확장을 열고 **Refresh**를 선택합니다.

{% alert tip %}
사용자가 정기적으로 들어오고 나갈 것으로 예상되는 세그먼트를 만든 경우, Campaign이나 Canvas에서 해당 세그먼트를 타겟팅하기 전에 사용하는 세그먼트 확장을 수동으로 새로고침하세요.
{% endalert %}

## 세그먼트 확장 관리 {#managing-your-segment-extensions}

**세그먼트 확장** 페이지에서 SQL을 사용하여 생성된 세그먼트는 이름 옆에 <i class="fas fa-code" alt="SQL 세그먼트 확장"></i>로 표시됩니다.

SQL 세그먼트 확장을 선택하여 확장이 사용 중인 위치를 확인하거나, 확장을 아카이브하거나, [세그먼트 멤버십을 수동으로 새로고침](#refreshing-segment-membership)할 수 있습니다.

![SQL 편집기의 메시징 사용 섹션에서 SQL 세그먼트가 사용되는 위치를 표시합니다.]({% image_buster /assets/img_archive/sql_segments_usage.png %}){: style="max-width:70%;"}

### 새로고침 설정 지정 {#designating-refresh-settings}

{% multi_lang_include audience/segments.md section='Refresh settings' %}

## Snowflake 크레딧 {#credits}

각 Braze 워크스페이스에는 한 달에 5개의 Snowflake 크레딧이 제공됩니다. 크레딧이 더 필요한 경우 계정 매니저에게 문의하세요. 크레딧은 SQL Segment의 멤버십을 새로고침하거나 저장 후 새로고침할 때마다 사용됩니다. SQL Segment 내에서 미리보기를 실행하거나 기존 세그먼트 확장을 저장하거나 새로고침할 때는 크레딧이 사용되지 않습니다.

{% alert note %}
Snowflake 크레딧은 기능 간에 공유되지 않습니다. 예를 들어 SQL 세그먼트 확장과 쿼리 빌더의 크레딧은 서로 독립적입니다.
{% endalert %}

크레딧 사용량은 SQL 쿼리의 실행 시간과 상관관계가 있습니다. 실행 시간이 길수록 쿼리 비용이 더 많이 듭니다. 실행 시간은 시간이 지남에 따라 쿼리의 복잡성과 크기에 따라 달라질 수 있습니다. 쿼리를 더 복잡하고 자주 실행할수록 리소스 할당이 커지고 실행 시간이 빨라집니다.

크레딧을 절약하려면 SQL 세그먼트 확장을 저장하기 전에 쿼리를 미리보기하여 올바른지 확인하세요.

크레딧은 매월 1일 오전 12시(UTC)에 5로 초기화됩니다. 크레딧 사용량 패널에서 한 달 동안의 크레딧 사용량을 모니터링할 수 있습니다. **세그먼트 확장** 페이지에서 <i class="fa-solid fa-chart-column"></i> **View SQL Credit Usage**를 클릭합니다.

![SQL 세그먼트 확장 페이지의 SQL 크레딧 사용량 패널]({% image_buster /assets/img_archive/sql_segments_credits.png %}){: style="max-width:60%"}

크레딧이 0이 되면 다음과 같은 일이 발생합니다:

- 자동으로 새로고침되도록 설정된 모든 SQL 세그먼트 확장은 새로고침을 중지하여 이러한 세그먼트의 멤버십과 이러한 세그먼트를 타겟팅하는 모든 Campaign 또는 Canvases에 영향을 미칩니다.
- 새 SQL 세그먼트 확장은 남은 한 달 동안 초안으로만 저장할 수 있습니다.

SQL Segment를 생성한 모든 회사 사용자와 회사 관리자는 크레딧의 50%, 80%, 100%를 사용하면 알림 이메일을 받게 됩니다. 다음 달 초에 크레딧이 초기화되면 더 많은 SQL Segments를 만들 수 있으며 자동 새로고침이 다시 시작됩니다.

SQL Segment 크레딧을 더 구매하거나 세그먼트 확장을 추가로 구매하려면 계정 매니저에게 문의하세요.