---
nav_title: 모범 사례
article_title: 모범 사례
toc_headers: h2
page_order: 1
page_type: reference
description: "이 페이지에서는 클라우드 데이터 수집, 모범 사례 및 제품 제한 사항에 대한 개요를 제공합니다."
---

# 모범 사례 {#best-practices}

> Braze 클라우드 데이터 수집을 사용하면 데이터 웨어하우스 또는 파일 저장 시스템에서 Braze로 직접 연결을 설정하여 관련 사용자 또는 카탈로그 데이터를 동기화할 수 있습니다. 이 데이터를 Braze에 동기화하면 개인화, 트리거 또는 세분화와 같은 사용 사례에 활용할 수 있습니다.

## `UPDATED_AT` 열 이해하기 {#understanding-the-updated_at-column}

{% alert note %}
`UPDATED_AT`는 데이터 웨어하우스 통합에만 해당되며, S3 동기화에는 적용되지 않습니다.
{% endalert %}

동기화가 실행되면 Braze가 데이터 웨어하우스 인스턴스에 직접 연결하여 지정된 테이블에서 모든 새 데이터를 가져오고, Braze 대시보드의 해당 데이터를 업데이트합니다. 동기화가 실행될 때마다 Braze는 업데이트된 데이터를 반영합니다.

{% alert important %}
Braze CDI는 행 내용이 현재 Braze에 저장된 것과 동일한지 여부에 관계없이 `UPDATED_AT` 값을 기준으로 행을 엄격하게 동기화합니다. 따라서 불필요한 데이터 포인트 사용량을 방지하려면 `UPDATED_AT`를 적절히 사용하여 새로운 데이터 또는 업데이트된 데이터만 동기화하는 것이 좋습니다.
{% endalert %}

### 예시: 반복 동기화 {#example-recurring-sync}

CDI 동기화에서 `UPDATED_AT`가 어떻게 사용되는지 설명하기 위해 사용자 속성을 업데이트하는 반복 동기화 예시를 살펴보겠습니다.

- 파일 스토리지 소스
   - Amazon S3

## 지원되는 데이터 유형 {#supported-data-types}

클라우드 데이터 수집은 다음 데이터 유형을 지원합니다:
- 사용자 속성, 포함 항목:
   - 중첩 커스텀 속성
   - 오브젝트 배열
   - 가입 상태
- 커스텀 이벤트
- 구매 이벤트
- 카탈로그 항목
- 사용자 삭제 요청

### 데이터 유형 문제 방지 {#avoiding-data-type-issues}

CDI를 사용하여 외부 소스(예: Databricks 또는 Snowflake)에서 데이터를 동기화할 때, 동기화 전에 소스 열이 올바른 데이터 유형을 사용하는지 확인하세요. 일반적인 문제는 다음과 같습니다:

- **문자열로 저장된 타임스탬프:** 날짜 열이 소스 데이터베이스에서 varchar 또는 문자열이 아닌 timestamp 또는 datetime 유형을 사용하는지 확인하세요.
- **문자열로 저장된 숫자:** 동기화 전에 소스 쿼리에서 숫자 열을 integer 또는 플로트 유형으로 변환하세요.
- **동기화 간 일관성 없는 유형:** 동기화 간에 열 유형이 변경되면 Braze에서 새 데이터를 거부할 수 있습니다. 소스 스키마가 일관되게 유지되는지 확인하세요.

Braze 대시보드에서 커스텀 속성의 데이터 유형을 강제 적용하거나 변경하려면 [커스텀 데이터 관리]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data#forcing-data-type-comparisons)를 참조하세요.

외부 ID, 사용자 별칭, Braze ID, 이메일 또는 전화번호를 기준으로 사용자 데이터를 업데이트할 수 있습니다. 외부 ID, 사용자 별칭 또는 Braze ID를 기준으로 사용자를 삭제할 수 있습니다.

## 동기화되는 항목 {#what-gets-synced}

동기화가 실행될 때마다 Braze는 이전에 동기화되지 않은 행을 찾습니다. 이를 위해 테이블 또는 뷰의 `UPDATED_AT` 열을 확인합니다. Braze는 `UPDATED_AT` 값이 마지막으로 동기화된 `UPDATED_AT` 값보다 이후인 행을 선택하여 가져옵니다. 정확한 경계 타임스탬프에 있는 행도 해당 타임스탬프에 새로운 행이 실행 간 추가된 경우 다시 동기화될 수 있습니다.

{% alert important %}
CDI는 마지막으로 동기화된 `UPDATED_AT` 값의 행 수를 추적합니다. 동일한 타임스탬프로 새 행이 실행 간 추가되면, CDI는 포괄적 경계(`>=`)로 전환하여 이미 처리된 행을 포함하여 해당 타임스탬프의 모든 행을 다시 동기화합니다. 중복 동기화와 불필요한 데이터 포인트 소비를 방지하려면 동기화 실행 간에 고유한 `UPDATED_AT` 값을 사용하세요. 자세한 내용은 [중복 타임스탬프로 행이 다시 동기화되는 것 방지하기](#avoid-resyncing-rows-with-duplicate-timestamps)를 참조하세요.
{% endalert %}

데이터 웨어하우스에서 다음 사용자 및 속성을 테이블에 추가하고, `UPDATED_AT` 시간을 데이터 추가 시점으로 설정하세요:

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_1",
        "attribute_b":"example_value_1"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

다음 예약된 동기화에서 Braze는 가장 최근 동기화된 타임스탬프보다 이후인 `UPDATED_AT` 타임스탬프를 가진 모든 행을 동기화합니다. Braze는 필드를 업데이트하거나 추가하므로 매번 전체 고객 프로필을 동기화할 필요가 없습니다. 동기화 후 고객 프로필에 새로운 업데이트가 반영됩니다:

**반복 동기화, 2022년 7월 20일 오후 12시 두 번째 실행**

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_2",
        "attribute_b":"example_value_2"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-16 00:25:30</code></td>
      <td><code>customer_9012</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":false,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

`customer_9012`에 대한 새 행이 추가되었지만, 해당 `UPDATED_AT` 값(`2022-07-16 00:25:30`)이 저장된 타임스탬프(`2022-07-19 09:07:23`)보다 이전이므로 동기화되지 않습니다. 그러나 `customer_5678`의 기존 행은 `UPDATED_AT` 값이 저장된 타임스탬프와 동일하므로 포괄적 경계로 인해 다시 동기화됩니다. 이 동작에 대한 자세한 내용은 [UPDATED_AT 시간이 동기화 시간과 동일하지 않도록 하기](#make-sure-the-updated_at-time-isnt-the-same-time-as-your-sync)를 참조하세요. 저장된 `UPDATED_AT`은 `2022-07-19 09:07:23`으로 유지됩니다.

**반복 동기화, 2022년 7월 21일 오후 12시 세 번째 실행**

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>2022-07-17 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_1",
        "attribute_b":"example_value_1"
    },
    "attribute_3":"2019-07-16T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-18 11:59:23</code></td>
      <td><code>customer_3456</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2":42,
    "attribute_3":"2019-07-16T19:20:30+1:00",
    "attribute_5":"testing"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-19 09:07:23</code></td>
      <td><code>customer_5678</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_4":true,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-16 00:25:30</code></td>
      <td><code>customer_9012</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"xyz",
    "attribute_4":false,
    "attribute_5":"testing_123"
}
{% endhighlight %}
      </td>
    </tr>
    <tr>
      <td><code>2022-07-21 08:30:00</code></td>
      <td><code>customer_1234</code></td>
      <td>
{% highlight json linenos %}
{
    "attribute_1":"abcdefg",
    "attribute_2": {
        "attribute_a":"example_value_2",
        "attribute_b":"example_value_2"
    },
    "attribute_3":"2019-07-20T19:20:30+1:00"
}
{% endhighlight %}
      </td>
    </tr>
  </tbody>
</table>

이 세 번째 실행에서 `customer_1234`에 대한 새 행이 추가되었으며, `UPDATED_AT` 값(`2022-07-21 08:30:00`)이 저장된 타임스탬프보다 이후입니다. 이 새 행과 `customer_5678`의 기존 행(저장된 타임스탬프와 동일한 `UPDATED_AT`을 가진)이 모두 동기화됩니다. 저장된 `UPDATED_AT`은 이제 `2022-07-21 08:30:00`으로 설정됩니다.

{% alert note %}
`UPDATED_AT` 값은 특정 동기화의 실행 시작 시간보다 이후일 수도 있습니다. 그러나 이는 권장되지 않습니다. 마지막 `UPDATED_AT` 타임스탬프를 "미래"로 밀어내어 이후 동기화에서 이전 값을 동기화하지 못하게 되기 때문입니다.
{% endalert %}

## `UPDATED_AT` 열에 UTC 타임스탬프 사용하기 {#use-a-utc-timestamp-for-the-updated_at-column}

`UPDATED_AT` 열은 일광 절약 시간 관련 문제를 방지하기 위해 UTC로 설정해야 합니다. 가능하면 `CURRENT_DATE()` 대신 `SYSDATE()`와 같은 UTC 전용 함수를 사용하세요.

## 중복 타임스탬프가 있는 행의 재동기화 방지 {#avoid-resyncing-rows-with-duplicate-timestamps}

CDI는 마지막으로 동기화된 `UPDATED_AT` 타임스탬프의 행 수를 추적합니다. CDI가 마지막 실행 이후 동일한 타임스탬프로 새 행이 추가된 것을 감지하면 포함 경계(`>=`)를 사용하여 이미 처리된 행을 포함하여 해당 타임스탬프의 모든 행을 다시 선택합니다. 그렇지 않으면 CDI는 배타 경계(`>`)를 사용하여 마지막으로 동기화된 값보다 엄격하게 늦은 행만 선택합니다.

예를 들어, 동기화가 `UPDATED_AT = 2025-04-01 00:00:00`인 5개의 행을 처리한 후 동일한 타임스탬프로 6번째 행이 추가되면, 다음 동기화에서 행 수 변경을 감지하고 6개의 행을 모두 다시 동기화합니다. 이로 인해 중복 데이터와 불필요한 데이터 포인트 소비가 발생할 수 있습니다.

이를 방지하려면:

- `VIEW`에 대한 동기화를 설정하는 경우 `CURRENT_TIMESTAMP`를 기본값으로 사용하지 마세요. `UPDATED_AT` 필드가 쿼리 실행 시간으로 평가되기 때문에 동기화가 실행될 때마다 모든 데이터가 동기화됩니다.
- 오래 실행되는 파이프라인이나 쿼리가 소스 테이블에 데이터를 쓰는 경우, 동기화와 동시에 실행하지 않거나 삽입된 모든 행에 동일한 타임스탬프를 사용하지 않도록 하세요.
- 동일한 타임스탬프를 공유하는 모든 행을 쓰려면 트랜잭션을 사용하세요.
- 행이 처리된 후 다시 선택되지 않도록 고유하고 단조 증가하는 `UPDATED_AT` 값을 사용하세요.

### 예시: 후속 업데이트 관리 {#example-managing-subsequent-updates}

이 예시는 데이터를 처음으로 동기화하는 일반적인 프로세스를 보여주며, 이후 업데이트에서는 변경된 데이터(델타)만 업데이트합니다. 일부 사용자 데이터가 포함된 테이블 `EXAMPLE_DATA`가 있다고 가정해 봅시다. 첫째 날에는 다음과 같은 값이 있습니다:

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;font-size: 14px; font-weight: bold; background-color: #f4f4f7; text-transform: lowercase; color: #212123; font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top;word-break:normal}
</style>

<table aria-label="예시: 후속 업데이트 관리">
  <caption>예시: 후속 업데이트 관리</caption>
    <thead>
        <tr>
            <th>external_id</th>
            <th>attribute_1</th>
            <th>attribute_2</th>
            <th>attribute_3</th>
            <th>attribute_4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12345</td>
            <td>823</td>
            <td>blue</td>
            <td>380</td>
            <td>FALSE</td>
        </tr>
        <tr>
            <td>23456</td>
            <td>28</td>
            <td>blue</td>
            <td>823</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>blue</td>
            <td>384</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td>red</td>
            <td>349</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>red</td>
            <td>813</td>
            <td>FALSE</td>
        </tr>
    </tbody>
</table>

이 데이터를 CDI가 기대하는 형식으로 변환하려면 다음 쿼리를 실행할 수 있습니다:

```sql
SELECT
    CURRENT_TIMESTAMP AS UPDATED_AT,
    EXTERNAL_ID AS EXTERNAL_ID,
    TO_JSON(
        OBJECT_CONSTRUCT(
            'attribute_1', attribute_1,
            'attribute_2', attribute_2,
            'attribute_3', attribute_3,
            'attribute_4', attribute_4
        )
    ) AS PAYLOAD
FROM EXAMPLE_DATA;
```

이 중 어느 것도 이전에 Braze에 동기화되지 않았으므로 모든 데이터를 CDI의 소스 테이블에 추가하세요:

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
  </tbody>
</table>

동기화가 실행되고 Braze는 사용 가능한 모든 데이터를 "2023-03-16 15:00:00"까지 동기화했다고 기록합니다. 그런 다음, 2일째 아침에 ETL이 실행되고 사용자 테이블의 일부 필드가 업데이트됩니다(*로 표시):

<table aria-label="예시: 후속 업데이트 관리">
  <caption>예시: 후속 업데이트 관리. *는 마지막 동기화 이후 업데이트된 필드를 나타냅니다.</caption>
    <thead>
        <tr>
            <th>external_id</th>
            <th>attribute_1</th>
            <th>attribute_2</th>
            <th>attribute_3</th>
            <th>attribute_4</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>12345</td>
            <td style="background-color: #FFFF00;">145*</td>
            <td style="background-color: #FFFF00;">red*</td>
            <td>380</td>
            <td style="background-color: #FFFF00;">TRUE*</td>
        </tr>
        <tr>
            <td>23456</td>
            <td style="background-color: #FFFF00;">15*</td>
            <td>blue</td>
            <td>823</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>34567</td>
            <td>234</td>
            <td>blue</td>
            <td style="background-color: #FFFF00;">495*</td>
            <td style="background-color: #FFFF00;">FALSE*</td>
        </tr>
        <tr>
            <td>45678</td>
            <td>245</td>
            <td style="background-color: #FFFF00;">green*</td>
            <td>349</td>
            <td>TRUE</td>
        </tr>
        <tr>
            <td>56789</td>
            <td>1938</td>
            <td>red</td>
            <td style="background-color: #FFFF00;">693*</td>
            <td>FALSE</td>
        </tr>
    </tbody>
</table>

이제 변경된 값만 CDI 소스 테이블에 추가하면 됩니다. 이 행들은 이전 행을 업데이트하는 대신 추가할 수 있습니다. 그러면 테이블은 다음과 같이 됩니다:

<table role="presentation">
  <thead>
    <tr>
      <th>UPDATED_AT</th>
      <th>EXTERNAL_ID</th>
      <th>PAYLOAD</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "823", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"380", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "28", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"823", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_1": "234", "ATTRIBUTE_2":"blue", "ATTRIBUTE_3":"384", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_1": "245", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"349", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-16 15:00:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_1": "1938", "ATTRIBUTE_2":"red", "ATTRIBUTE_3":"813", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>12345</td>
      <td><code>{ "ATTRIBUTE_1": "145", "ATTRIBUTE_2":"red", "ATTRIBUTE_4":"TRUE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>23456</td>
      <td><code>{ "ATTRIBUTE_1": "15"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>34567</td>
      <td><code>{ "ATTRIBUTE_3":"495", "ATTRIBUTE_4":"FALSE"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>45678</td>
      <td><code>{ "ATTRIBUTE_2":"green"}</code></td>
    </tr>
    <tr>
      <td>2023-03-17 09:30:00</td>
      <td>56789</td>
      <td><code>{ "ATTRIBUTE_3":"693"}</code></td>
    </tr>
  </tbody>
</table>

CDI는 새 행만 동기화하므로 다음 동기화가 실행되면 마지막 다섯 행만 동기화됩니다.

## 추가 팁 {#additional-tips}

### 소비를 최소화하기 위해 새로운 또는 업데이트된 속성만 작성하기 {#only-write-new-or-updated-attributes-to-minimize-consumption}

동기화가 실행될 때마다 Braze는 이전에 동기화되지 않은 행을 찾습니다. 테이블 또는 뷰의 `UPDATED_AT` 열을 사용하여 이를 확인합니다. Braze는 `UPDATED_AT`가 마지막으로 동기화된 `UPDATED_AT` 값보다 나중인 모든 행을 선택하고 가져오며, 해당 행이 현재 고객 프로필에 있는 것과 동일한지 여부는 고려하지 않습니다. 새 행이 동일한 타임스탬프를 공유하는 경우 경계 타임스탬프에 있는 행도 다시 동기화될 수 있습니다. 이러한 이유로 추가하거나 업데이트하려는 속성만 동기화하는 것을 권장합니다.

데이터 포인트 사용량은 CDI를 사용하든 REST API나 SDK와 같은 다른 수집 방법을 사용하든 동일하므로, 소스 테이블에 새로운 또는 업데이트된 속성만 추가하고 있는지 확인하는 것은 사용자의 몫입니다.

### `EXTERNAL_ID`와 `PAYLOAD` 열 분리하기 {#separate-external_id-from-payload-column}

`PAYLOAD` 오브젝트에는 외부 ID 또는 다른 ID 유형이 포함되어서는 안 됩니다.

### 속성 제거하기 {#remove-an-attribute}

사용자 프로필에서 속성을 생략하려면 `null`로 설정할 수 있습니다. 속성을 변경하지 않고 유지하려면 업데이트될 때까지 Braze로 보내지 마세요. 속성을 완전히 제거하려면 `TO_JSON(OBJECT_CONSTRUCT_KEEP_NULL(...))`을 사용하세요.

### 증분 업데이트하기 {#make-incremental-updates}

동시 업데이트 시 의도하지 않은 덮어쓰기를 방지하기 위해 데이터를 증분 업데이트하세요.

{% alert important %}
* **서로 다른 속성에 대한 업데이트:** 대부분의 경우, 두 업데이트가 사용자의 동일한 속성에 영향을 미치지 않으면 완전히 독립적인 결과를 가집니다. 예를 들어, 사용자의 `Color` 속성을 업데이트하고 별도로 `Size` 속성을 업데이트하는 경우, 두 업데이트가 서로 몇 초 내에 발생하더라도 둘 다 올바르게 적용됩니다.
* **동일한 속성에 대한 업데이트:** 단일 동기화 실행 내에서 여러 업데이트가 동일한 속성을 대상으로 하면 경합 조건이 발생할 수 있습니다. 이러한 드문 경우에 한 업데이트가 다른 업데이트를 덮어쓸 수 있습니다. 이 동작을 방지하는 가장 좋은 방법은 CDI 동기화의 소스 데이터가 각 사용자의 최신 상태만 반영하도록 하거나, 주어진 사용자 또는 사용자+속성 쌍에 대한 모든 업데이트가 단일 행에 포함되도록 하는 것입니다.
* **오브젝트 배열 연산자:** 독립적 업데이트의 유일한 예외는 오브젝트 배열에 대한 `$add`, `$remove`, `$update` 연산자이며, 동일한 배열에 대한 업데이트가 서로 상호 작용할 수 있습니다.
* **이벤트:** 각 이벤트는 고유하고 타임스탬프가 연결되어 있으므로 경합 조건은 이벤트에 영향을 미치지 않습니다.
{% endalert %}

이 동작을 방지하는 가장 좋은 방법은 CDI 동기화의 소스 데이터가 각 사용자의 최신 상태만 반영하도록 하거나, 주어진 사용자 또는 사용자+속성 쌍에 대한 모든 업데이트가 단일 행에 포함되도록 하는 것입니다.

### 다른 테이블에서 JSON 문자열 생성하기 {#create-a-json-string-from-another-table}

각 속성을 별도의 열에 내부적으로 저장하는 것을 선호하는 경우, Braze와의 동기화를 위해 해당 열을 JSON 문자열로 변환해야 합니다. 이를 위해 다음과 같은 쿼리를 사용할 수 있습니다:

{% tabs local %}
{% tab Snowflake %}
Snowflake에서 소스 열을 CDI 필드로 포맷하려면 이 쿼리를 사용하세요.
```sql
CREATE TABLE "EXAMPLE_USER_DATA"
    (attribute_1 string,
     attribute_2 string,
     attribute_3 number,
     my_user_id string);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'yet_another_attribute',
            attribute_3)
    )as PAYLOAD FROM "EXAMPLE_USER_DATA";
```
{% endtab %}
{% tab Redshift %}
Redshift에서 소스 열을 CDI 필드로 포맷하려면 이 쿼리를 사용하세요.
```sql
CREATE TABLE "EXAMPLE_USER_DATA"
    (attribute_1 string,
     attribute_2 string,
     attribute_3 number,
     my_user_id string);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'yet_another_attribute',
            attribute_3)
    ) as PAYLOAD FROM "EXAMPLE_USER_DATA";
```
{% endtab %}
{% tab BigQuery %}
BigQuery에서 소스 열을 CDI 필드로 포맷하려면 이 쿼리를 사용하세요.
```sql
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (attribute_1 string,
     attribute_2 STRING,
     attribute_3 NUMERIC,
     my_user_id STRING);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
      STRUCT(
        'attribute_1' AS attribute_1,
        'attribute_2'AS attribute_2,
        'yet_another_attribute'AS attribute_3
      )
    ) as PAYLOAD
  FROM BRAZE.EXAMPLE_USER_DATA;
```
{% endtab %}
{% tab Databricks %}
Databricks에서 소스 열을 CDI 필드로 포맷하려면 이 쿼리를 사용하세요.
```sql
CREATE OR REPLACE TABLE BRAZE.EXAMPLE_USER_DATA (
    attribute_1 string,
    attribute_2 STRING,
    attribute_3 NUMERIC,
    my_user_id STRING
);

SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    my_user_id as EXTERNAL_ID,
    TO_JSON(
      STRUCT(
        attribute_1,
        attribute_2,
        attribute_3
      )
    ) as PAYLOAD
  FROM BRAZE.EXAMPLE_USER_DATA;
```
{% endtab %}
{% tab Microsoft Fabric %}
Microsoft Fabric에서 소스 열을 CDI 필드로 포맷하려면 이 쿼리를 사용하세요.
```sql
CREATE TABLE [braze].[users] (
    attribute_1 VARCHAR,
    attribute_2 VARCHAR,
    attribute_3 VARCHAR,
    attribute_4 VARCHAR,
    user_id VARCHAR
)
GO

CREATE VIEW [braze].[user_update_example]
AS SELECT
    user_id as EXTERNAL_ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[users] ;
```
{% endtab %}

{% endtabs %}

### `UPDATED_AT` 타임스탬프 사용하기 {#use-the-updated_at-timestamp}

Braze는 `UPDATED_AT` 타임스탬프를 사용하여 성공적으로 동기화된 데이터를 추적합니다. CDI는 또한 마지막으로 동기화된 타임스탬프의 행 수를 추적합니다. 실행 사이에 동일한 타임스탬프로 새 행이 추가되면, CDI는 해당 타임스탬프의 모든 행을 다시 동기화하여 중복 데이터가 발생할 수 있습니다. 자세한 내용과 팁은 [중복 타임스탬프가 있는 행의 재동기화 방지하기](#avoid-resyncing-rows-with-duplicate-timestamps)를 참조하세요.

### 테이블 구성 {#table-configuration}

고객이 모범 사례나 코드 스니펫을 공유할 수 있는 공개 [GitHub 리포지토리](https://github.com/braze-inc/braze-examples/tree/main/cloud-data-ingestion)가 있습니다. 자체 스니펫을 기여하려면 풀 리퀘스트를 생성하세요!

### 데이터 포맷 {#data-formatting}

Cloud Data Ingestion 테이블 설정 요구 사항 및 페이로드 포맷 요구 사항은 [Cloud Data Ingestion을 위한 테이블 설정]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup)에 문서화되어 있습니다.

해당 페이지를 사용하여 다음을 구분하세요:

- 소스 테이블 요구 사항(필수 열, 식별자 열, `UPDATED_AT` 동작)
- 페이로드 요구 사항(각 데이터 유형에 대해 `/users/track` 오브젝트 형식과 일치해야 하는 필드)

### 데이터 웨어하우스 쿼리의 타임아웃 방지하기 {#avoid-timeouts-for-data-warehouse-queries}

최적의 성능과 잠재적 오류를 방지하기 위해 쿼리가 1시간 이내에 완료되도록 하는 것을 권장합니다. 쿼리가 이 시간을 초과하는 경우, 데이터 웨어하우스 구성을 검토하는 것을 고려하세요. 웨어하우스에 할당된 리소스를 최적화하면 쿼리 실행 속도를 개선하는 데 도움이 될 수 있습니다.

## 제품 제한 사항 {#product-limitations}

| 제한 사항            | 설명                                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 통합 수 | 설정할 수 있는 통합 수에는 제한이 없습니다. 그러나 테이블 또는 뷰당 하나의 통합만 설정할 수 있습니다.                                             |
| 행 수         | 기본적으로 각 실행은 최대 5억 개의 행을 동기화할 수 있습니다. Braze는 5억 개 이상의 새 행이 포함된 동기화를 중단합니다. 이보다 더 높은 한도가 필요한 경우 Braze 고객 성공 매니저 또는 Braze 지원팀에 문의하세요. |
| 행당 속성     | 각 행에는 하나의 사용자 ID와 최대 250개의 속성이 포함된 JSON 오브젝트가 있어야 합니다. JSON 오브젝트의 각 키는 하나의 속성으로 계산됩니다(즉, 배열도 하나의 속성으로 계산됩니다). |
| 페이로드 크기           | 각 행에는 최대 1MB의 페이로드를 포함할 수 있습니다. Braze는 1&nbsp;MB를 초과하는 페이로드를 거부하고, 관련 외부 ID 및 잘린 페이로드와 함께 "Payload was greater than 1MB"라는 오류를 동기화 로그에 기록합니다. |
| 데이터 유형              | 클라우드 데이터 수집을 통해 사용자 속성, 이벤트, 구매를 동기화할 수 있습니다.                                                                                                  |
| Braze 리전           | 이 제품은 모든 Braze 리전에서 사용할 수 있습니다. 모든 Braze 리전은 모든 소스 데이터 리전에 연결할 수 있습니다.                                                                              |
| 소스 리전       | Braze는 모든 리전 또는 클라우드 공급자의 데이터 웨어하우스 또는 클라우드 환경에 연결합니다.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 aria-label="제품 제한 사항" }

<br><br>