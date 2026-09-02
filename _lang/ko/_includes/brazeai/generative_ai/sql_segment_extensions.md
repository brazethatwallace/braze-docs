# SQL 세그먼트 확장 {#sql-segment-extensions}

> [Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake) 데이터의 Snowflake SQL 쿼리를 사용하여 세그먼트 확장을 생성할 수 있습니다. SQL은 다른 세분화 기능으로는 달성할 수 없는 방식으로 데이터 간의 관계를 설명할 수 있는 유연성을 제공하기 때문에 새로운 세그먼트 사용 사례를 발굴하는 데 도움이 됩니다.
>
> 표준 세그먼트 확장과 마찬가지로 SQL 세그먼트 확장에서 최대 2년(730일)까지의 이벤트를 쿼리할 수 있습니다. 표준 세그먼트 확장과 달리 SQL 세그먼트 확장은 [크레딧을 소모합니다](#credits).

## 전제 조건 {#prerequisites}

이 기능을 통해 PII 데이터에 접근할 수 있으므로, SQL 세그먼트 쿼리를 실행하려면 PII 권한이 있어야 합니다.

## 세그먼트 확장 만들기 {#creating-a-segment-extension}

### 1단계: 에디터 선택 {#step-1-choose-an-editor}

SQL 세그먼트 확장을 만들 때 선택할 수 있는 SQL 에디터는 두 가지입니다: SQL 에디터와 증분 SQL 에디터입니다.

- **전체 새로고침:** Segment가 새로고침될 때마다 Braze가 사용 가능한 모든 데이터를 쿼리하여 Segment를 업데이트하므로, 증분 새로고침보다 더 많은 크레딧을 사용합니다. 전체 새로고침 확장은 매일 자동으로 멤버십을 재생성할 수 있지만, 증분 새로고침을 사용하여 새로고침할 수는 없습니다.
- **증분 새로고침:** 증분 새로고침은 쿼리를 설정하는 더 비용 효율적인 방법이지만, 설정 시 몇 가지 [추가 단계](#step-2-write-your-sql)가 필요합니다. Segment를 구성할 때 이러한 추가 단계를 완료할 수 있다면 이 옵션을 선택하는 것이 좋습니다. 쿼리가 더 적은 크레딧으로 실행되기 때문입니다.
- **AI SQL 생성기:** AI SQL 생성기를 사용하면 일반 언어로 프롬프트를 작성하여 Segment에 대한 SQL 쿼리로 변환할 수 있습니다. SQL을 직접 작성할 필요 없이 빠르게 시작할 수 있는 방법입니다.

{% alert tip %}
두 SQL 에디터 중 어느 것으로 만든 SQL Segments에서든 수동 전체 새로고침을 수행할 수 있습니다.
{% endalert %}

{% tabs local %}
{% tab 전체 새로고침 %}

전체 새로고침 SQL 세그먼트 확장을 만들려면 다음과 같이 합니다:

1. **오디언스** > **세그먼트 확장**으로 이동합니다.
2. **새 확장 만들기**를 선택한 다음 **전체 새로고침**을 선택합니다.<br><br>
   ![전체 새로고침과 증분 새로고침 옵션이 있는 새 확장 만들기 모달.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. 세그먼트 확장의 이름을 추가하고 SQL을 입력합니다. 요구 사항 및 리소스에 대해서는 [2단계](#step-2-write-your-sql)를 참조하세요.<br><br>
   ![예시 SQL 세그먼트 확장을 보여주는 SQL 에디터.]({% image_buster /assets/img_archive/sql_segments_editor.png %}){: style="max-width:60%" }<br><br>
4. 세그먼트 확장을 저장합니다.

{% endtab %}
{% tab 증분 새로고침 %}

증분 새로고침 SQL 세그먼트 확장을 만들려면 다음과 같이 합니다:

1. **오디언스** > **세그먼트 확장**으로 이동합니다.
2. **새 확장 만들기**를 선택한 다음 **증분 새로고침**을 선택합니다.<br><br>
   ![전체 새로고침과 증분 새로고침 옵션이 있는 새 확장 만들기 모달.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:50%" }<br><br>
3. 세그먼트 확장의 이름을 추가하고 SQL을 입력합니다. 요구 사항 및 리소스에 대해서는 [SQL 작성](#writing-sql) 섹션을 참조하세요.<br><br>
   ![예시 증분 SQL 세그먼트 확장을 보여주는 SQL 에디터.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:60%" }<br><br>
4. 원하는 경우 **매일 확장 재생성**을 선택합니다.<br><br>
   ![매일 확장을 재생성하는 체크박스.]({% image_buster /assets/img_archive/sql_segments_regenerate.png %}){: style="max-width:60%" }<br><br>
   이 옵션을 선택하면 Braze가 매일 자동으로 Segment 멤버십을 업데이트합니다. 즉, 매일 자정(회사 시간대 기준, 최대 1시간 지연 가능)에 Braze가 Segment에 새 사용자가 있는지 확인하고 자동으로 Segment에 추가합니다. 세그먼트 확장이 7일 동안 사용되지 않으면 Braze가 자동으로 매일 재생성을 일시 중지합니다. 사용되지 않은 세그먼트 확장이란 Campaign 또는 Canvas에 포함되지 않은 확장을 의미합니다(확장이 "사용됨"으로 간주되려면 Campaign 또는 Canvas가 활성 상태일 필요는 없습니다).<br><br>
5. 세그먼트 확장을 저장합니다.

{% endtab %}

{% tab AI SQL 생성기 %}

{% alert note %}
AI SQL 생성기는 현재 베타 기능으로 제공됩니다. 이 베타 체험에 참여하려면 고객 성공 매니저에게 문의하세요.
{% endalert %}

AI SQL 생성기는 OpenAI가 지원하는 [GPT](https://openai.com/gpt-4)를 레버리지하여 SQL Segment에 대한 SQL을 추천합니다.

![프롬프트 "지난 달 알림을 받은 사용자"가 입력된 AI SQL 생성기]({% image_buster /assets/img/ai_sql_generator.png %}){: style="max-width:70%;"}

AI SQL 생성기를 사용하려면 다음과 같이 합니다:

1. 전체 새로고침 또는 증분 새로고침을 사용하여 [SQL Segment]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)를 만든 후 **AI SQL 생성기 실행**을 선택합니다.
2. 프롬프트를 입력하고 **생성**을 선택하여 프롬프트를 SQL로 변환합니다.
3. 생성된 SQL이 올바른지 검토한 후 Segment를 저장합니다.

#### 예시 프롬프트 {#example-prompts}

- 지난 달에 이메일을 받은 사용자
- 지난 1년간 구매 횟수가 5회 미만인 사용자

#### 팁 {#tips}

- 사용 가능한 [Snowflake 데이터 테이블]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables)을 숙지하세요. 이 테이블에 존재하지 않는 데이터를 요청하면 ChatGPT가 가짜 테이블을 만들어낼 수 있습니다.
- 이 기능의 [SQL 작성 규칙]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments?tab=sql%20editor#writing-sql)을 숙지하세요. 이러한 규칙을 따르지 않으면 오류가 발생합니다. 예를 들어, SQL 코드는 `user_id` 열을 선택해야 합니다. 프롬프트를 "~한 사용자"로 시작하면 도움이 될 수 있습니다.
- AI SQL 생성기를 사용하여 분당 최대 20개의 프롬프트를 전송할 수 있습니다.

##{% multi_lang_include brazeai/generative_ai/policy.md %}

{% endtab %}
{% endtabs %}

{% alert note %}
실행 시간이 20분을 초과하는 SQL 쿼리는 시간 초과됩니다.
{% endalert %}

확장 처리가 완료되면 세그먼트 확장을 사용하여 [Segment를 만들고]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension#step-5-use-your-extension-in-a-segment) 이 새 Segment를 Campaign 및 Canvases에 타겟팅할 수 있습니다.

### 2단계: SQL 작성 {#step-2-write-your-sql}

SQL 쿼리는 [Snowflake 구문](https://docs.snowflake.com/en/sql-reference.html)을 사용하여 작성해야 합니다. 쿼리할 수 있는 테이블 및 열의 전체 목록은 [테이블 레퍼런스]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables)를 참조하세요.

{% alert important %}
쿼리할 수 있는 테이블에는 이벤트 데이터만 포함되어 있습니다. 사용자 속성을 쿼리하려면 SQL Segment를 [클래식 세그먼터]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)의 커스텀 속성 필터와 결합해야 합니다.
{% endalert %}

{% tabs %}
{% tab SQL 에디터 %}

SQL은 다음 규칙을 추가로 준수해야 합니다:

- 단일 SQL 문을 작성합니다. 세미콜론은 포함하지 마세요.
- SQL은 `user_id` 열 하나만 선택해야 합니다. 즉, SQL에는 다음이 포함되어야 합니다:

```sql
SELECT DISTINCT user_id FROM "INSERT TABLE NAME"
```

- 이벤트가 0회인 사용자를 쿼리하는 것은 불가능하므로, 이벤트를 X회 미만 수행한 사용자에 대한 쿼리는 다음 해결 방법을 따라야 합니다:
   1. 이벤트를 X회 이상 수행한 사용자를 선택하는 쿼리를 작성합니다.
   2. Segment에서 세그먼트 확장을 참조할 때 `doesn't include`를 선택하여 결과를 반전합니다.

#### 추가 규칙 {#additional-rules}

또한, 표준 SQL 쿼리는 다음 규칙을 준수해야 합니다:

- `DECLARE` 문을 사용할 수 없습니다.
{% endtab %}
{% tab 증분 SQL 에디터 %}

모든 증분 새로고침 쿼리는 두 부분으로 구성됩니다: 쿼리와 스키마 세부 정보입니다.

1. 에디터에서 원하는 테이블로부터 `user_id`를 선택하는 쿼리를 작성합니다.
2. 에디터 상단의 필드에서 **연산자**, **횟수**, **기간**을 선택하여 스키마 세부 정보를 추가합니다. 쿼리는 집계 열의 합이 {% raw %}`{{operator}}`와 `{{number of times}}`{% endraw %} 입력 안내로 지정된 특정 조건을 충족하는지 확인합니다. 이 기능은 클래식 세그먼트 확장을 만드는 워크플로와 유사하게 작동합니다.<br><br>
   - **연산자:** 이벤트가 발생 횟수보다 많은지, 적은지, 또는 같은지를 나타냅니다.<br>
   ![연산자 필드에서 "초과"가 선택된 화면.]({% image_buster /assets/img_archive/sql_segments_operator.png %})<br><br>
   - **횟수:** 연산자와 관련하여 이벤트를 평가할 횟수입니다.<br>
   ![횟수에 "5"가 입력된 화면.]({% image_buster /assets/img_archive/sql_segments_times.png %})<br><br>
   - **기간:** 이벤트의 인스턴스를 확인할 1~730일 범위의 일수입니다. 이 기간은 현재 날짜를 기준으로 과거 일수를 나타냅니다. 다음 예시는 지난 365일 동안 이벤트를 5회 이상 수행한 사용자를 쿼리하는 것을 보여줍니다.<br>
   ![기간 필드에 "365"가 입력된 화면.]({% image_buster /assets/img_archive/sql_segments_period.png %})

다음 예시에서, 결과 Segment에는 지정된 날짜 이후 지난 30일 동안 `favorited` 이벤트를 3회 이상 수행한 사용자가 포함됩니다.

![예시 증분 SQL 세그먼트 확장을 보여주는 SQL 에디터.]({% image_buster /assets/img_archive/sql_segments_editor_incremental.png %}){: style="max-width:65%" }

![증분 SQL 세그먼트 확장의 SQL 미리보기.]({% image_buster /assets/img_archive/sql_segments_incremental_preview.png %}){: style="max-width:85%" }

{% alert tip %}
증분 새로고침 Segments는 지연 이벤트를 고려합니다. 지연 이벤트란 2일 이상 전에 발생한 이벤트(예: 캡처 시점에 전송되지 않은 SDK 이벤트)를 말합니다.
{% endalert %}

#### 추가 규칙

또한, 증분 새로고침 쿼리는 다음 규칙을 준수해야 합니다:

- 단일 SQL 문을 작성합니다. 세미콜론은 포함하지 마세요.
- 증분 SQL Segment는 하나의 단일 이벤트만 참조할 수 있습니다. 날짜 및 횟수 드롭다운은 선택한 이벤트를 기준으로 합니다.
- SQL에는 `user_id`, `$start_date`, 그리고 집계 함수(예: `COUNT`)가 포함되어야 합니다. 이 세 가지 필드 없이 저장된 SQL은 오류가 발생합니다.
- `DECLARE` 문을 사용할 수 없습니다.
{% endtab %}
{% endtabs %}

{% alert note %}
`CATALOGS_ITEMS_SHARED` 테이블을 사용하는 SQL Segment를 만드는 경우 카탈로그 ID를 지정해야 합니다. 예를 들면 다음과 같습니다:

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### 3단계: 쿼리 미리보기 {#step-3-preview-the-query}

저장하기 전에 쿼리 미리보기를 실행할 수 있습니다. 쿼리 미리보기는 자동으로 100행으로 제한되며 60초 후 시간 초과됩니다. `user_id` 열 요구 사항은 미리보기를 실행할 때는 적용되지 않습니다.

증분 SQL 세그먼트 확장의 경우 미리보기에는 연산자, 횟수, 기간 필드의 추가 기준이 포함되지 않습니다.

### 4단계: SQL 반전이 필요한지 결정 {#step-4-determine-if-you-need-to-invert-sql}

다음으로, SQL 반전이 필요한지 결정합니다. 이벤트가 0회인 사용자를 직접 쿼리하는 것은 불가능하지만, **SQL 반전**을 사용하면 이러한 사용자를 타겟팅할 수 있습니다.

{% alert note %}
기본적으로 **SQL 반전**은 토글되어 있지 않습니다. 그러나 AI SQL 생성기를 사용하여 부정이 필요한 SQL 문을 생성하면 ChatGPT가 이 기능을 자동으로 토글하는 결과를 반환할 수 있습니다.
{% endalert %}

예를 들어, 구매 횟수가 3회 미만인 사용자를 타겟팅하려면 먼저 3회 이상 구매한 사용자를 선택하는 쿼리를 작성합니다. 그런 다음 **SQL 반전**을 선택하여 구매 횟수가 3회 미만인 사용자(구매 0회 포함)를 타겟팅합니다.

{% alert important %}
이벤트가 0회인 사용자를 구체적으로 타겟팅하려는 경우가 아니라면 SQL을 반전할 필요가 없습니다. **SQL 반전**이 선택된 경우 해당 기능이 필요한지, Segment가 원하는 오디언스와 일치하는지 확인하세요. 예를 들어, 쿼리가 이벤트가 1회 이상인 사용자를 타겟팅하는 경우, 반전하면 이벤트가 0회인 사용자만 타겟팅됩니다.
{% endalert %}

![SQL 반전 옵션이 선택된 "지난 30일 동안 이메일 1~4회 클릭" 세그먼트 확장.]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:90%;"}

## 세그먼트 멤버십 갱신 {#refreshing-segment-membership}

SQL을 사용하여 생성한 세그먼트 확장의 세그먼트 멤버십을 갱신하려면, 해당 세그먼트 확장을 열고 **갱신**을 선택합니다.

{% alert tip %}
사용자가 정기적으로 진입하고 이탈할 것으로 예상되는 Segment를 생성한 경우, Campaign 또는 Canvas에서 해당 Segment를 타겟팅하기 전에 사용하는 세그먼트 확장을 수동으로 갱신하세요.
{% endalert %}

## SQL 세그먼트 확장 관리하기 {#managing-your-segment-extensions}

**세그먼트 확장** 페이지에서 SQL을 사용하여 생성된 Segments는 이름 옆에 <i class="fas fa-code" alt="SQL 세그먼트 확장"></i>로 표시됩니다.

SQL 세그먼트 확장을 선택하면 해당 확장이 사용되고 있는 위치를 확인하고, 확장을 보관하거나, 수동으로 [Segment 멤버십을 새로고침](#refreshing-segment-membership)할 수 있습니다.

![SQL 에디터의 메시징 사용 섹션으로, SQL Segment가 사용되고 있는 위치를 보여줍니다.]({% image_buster /assets/img_archive/sql_segments_usage.png %}){: style="max-width:70%;"}

### 새로고침 설정 지정하기 {#designating-refresh-settings}

{% multi_lang_include audience/segments.md section='Refresh settings' %}

## Snowflake 크레딧 {#credits}

각 Braze 워크스페이스에는 한 달에 5개의 Snowflake 크레딧이 제공됩니다. 크레딧이 더 필요한 경우 계정 매니저에게 문의하세요. 크레딧은 SQL Segment의 멤버십을 새로고침하거나 저장 후 새로고침할 때마다 사용됩니다. SQL Segment 내에서 미리보기를 실행하거나 기존 세그먼트 확장을 저장하거나 새로고침할 때는 크레딧이 사용되지 않습니다.

{% alert note %}
Snowflake 크레딧은 기능 간에 공유되지 않습니다. 예를 들어 SQL 세그먼트 확장과 쿼리 빌더의 크레딧은 서로 독립적입니다.
{% endalert %}

크레딧 사용량은 SQL 쿼리의 실행 시간과 상관관계가 있습니다. 실행 시간이 길수록 쿼리 비용이 더 많이 듭니다. 실행 시간은 시간이 지남에 따라 쿼리의 복잡성과 크기에 따라 달라질 수 있습니다. 쿼리를 더 복잡하고 자주 실행할수록 리소스 할당이 커지고 실행 시간이 빨라집니다.

크레딧을 절약하려면 SQL 세그먼트 확장을 저장하기 전에 쿼리를 미리보기하여 올바른지 확인하세요.

크레딧은 매월 1일 오전 12시(UTC)에 5로 초기화됩니다. 크레딧 사용량 패널에서 한 달 동안의 크레딧 사용량을 모니터링할 수 있습니다. **세그먼트 확장** 페이지에서 <i class="fa-solid fa-chart-column"></i> **SQL 크레딧 사용량 보기**를 클릭합니다.

![SQL 세그먼트 확장 페이지의 SQL 크레딧 사용량 패널]({% image_buster /assets/img_archive/sql_segments_credits.png %}){: style="max-width:60%"}

크레딧이 0이 되면 다음과 같은 일이 발생합니다:

- 자동으로 새로고침되도록 설정된 모든 SQL 세그먼트 확장은 새로고침을 중지하여 이러한 세그먼트의 멤버십과 이러한 세그먼트를 타겟팅하는 모든 Campaign 또는 Canvases에 영향을 미칩니다.
- 새 SQL 세그먼트 확장은 남은 한 달 동안 초안으로만 저장할 수 있습니다.

SQL Segment를 생성한 모든 회사 사용자와 회사 관리자는 크레딧의 50%, 80%, 100%를 사용하면 알림 이메일을 받게 됩니다. 다음 달 초에 크레딧이 초기화되면 더 많은 SQL Segments를 만들 수 있으며 자동 새로고침이 다시 시작됩니다.

SQL Segment 크레딧을 더 구매하거나 세그먼트 확장을 추가로 구매하려면 계정 매니저에게 문의하세요.