---
nav_title: "카탈로그 Segments"
article_title: "카탈로그 Segments"
page_order: 0
page_type: reference
alias: "/catalog_segments/"
description: "이 문서에서는 카탈로그 데이터를 SQL 세그먼트 확장에서 사용하여 사용자 오디언스를 구축하는 카탈로그 Segments를 생성하는 방법을 설명합니다."
tool: Segments
---

# 카탈로그 Segments {#catalog-segments}

> 카탈로그 Segments는 카탈로그 데이터를 커스텀 이벤트 또는 구매 데이터와 결합하여 생성하는 SQL 세그먼트 확장의 한 유형입니다. Segment에서 참조한 다음 Campaigns 및 Canvases에서 타겟팅할 수 있습니다.

카탈로그 Segments는 SQL을 사용하여 카탈로그의 데이터와 커스텀 이벤트 또는 구매 데이터를 결합합니다. 이를 위해 카탈로그와 커스텀 이벤트 또는 구매 간에 공통 식별자 필드가 있어야 합니다. 예를 들어, 카탈로그의 항목 ID 값은 커스텀 이벤트의 속성정보 값과 일치해야 합니다.

## 카탈로그 Segment 생성하기 {#creating-a-catalog-segment}

1. **세그먼트 확장** > **새 확장 만들기** > **템플릿으로 시작**으로 이동하여 템플릿을 선택합니다. <br>![이벤트, 구매 또는 RFM Segments에 대한 카탈로그 Segment를 생성하는 옵션이 있는 모달.]({% image_buster /assets/img/catalog-segments-template.png %}){: style="max-width:80%" }

{: start="2"}
2. SQL 편집기에 템플릿이 자동으로 채워집니다. <br>![미리 생성된 템플릿이 있는 SQL 편집기.]({% image_buster /assets/img/catalog-segments-editor.png %}){: style="max-width:80%" }<br>이 템플릿은 사용자 이벤트 데이터를 카탈로그 데이터와 결합하여 특정 카탈로그 항목에 참여한 사용자를 세그먼트합니다.

3. **변수** 탭을 사용하여 Segment를 생성하기 전에 템플릿에 필요한 필드를 제공합니다. <br>Braze가 카탈로그 항목에 대한 참여를 기반으로 사용자를 식별하려면 다음을 수행해야 합니다: <br> - 카탈로그 필드가 포함된 카탈로그를 선택합니다 <br> - 이벤트 속성정보가 포함된 커스텀 이벤트를 선택합니다 <br> - 카탈로그 필드와 이벤트 속성정보 값을 일치시킵니다

변수를 선택하기 위한 가이드라인은 다음과 같습니다:

| 변수 필드 | 설명 |
| --- | --- |
| `Catalog` | 사용자를 타겟팅하는 데 사용하는 카탈로그의 이름입니다. |
| `Catalog field` | `Custom event property`와 동일한 값을 포함하는 카탈로그의 필드입니다. 일반적으로 ID 유형입니다. 이커머스 사용 사례에서는 `shopify_id`가 됩니다. |
| `Custom event` | `Catalog field`와 일치하는 값을 가진 속성정보가 포함된 커스텀 이벤트의 이름입니다. 이커머스 사용 사례에서는 `Made Order`가 됩니다. |
| `Custom event property` | `Catalog field`와 값이 일치하는 커스텀 이벤트 속성정보의 이름입니다. 이커머스 예시 사용 사례에서는 `Shopify_ID`가 됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Creating a catalog segment" }

{: start="4"}
4. 필요한 경우, 카탈로그 내 특정 필드 값으로 세그먼트하기 위해 사용 사례에 맞는 추가 선택 필드를 입력합니다:
- `Catalog field`: 이 카탈로그 내의 특정 필드(열 이름)
- `Value`: 해당 필드 또는 열 내의 특정 값 <br><br> 건강 앱을 예로 들면, 예약할 수 있는 각 의사에 대한 카탈로그에 `specialty`라는 필드가 있고 `vision` 또는 `dental`과 같은 값이 포함되어 있다고 가정합니다. `dental` 값을 가진 의사를 방문한 사용자를 세그먼트하려면 `specialty`를 `Catalog field`로 선택하고 `dental`을 `Value`로 선택합니다.

5. SQL Segment를 생성한 후 **미리보기 실행**을 클릭하여 쿼리가 사용자를 반환하는지 또는 오류가 있는지 확인하는 것을 권장합니다. [쿼리 결과 미리보기]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/#previewing-results), [SQL 세그먼트 확장 관리]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/#managing-sql-segment-extensions) 등에 대한 자세한 내용은 [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/)을 확인하세요.

{% alert note %}
`CATALOGS_ITEMS_SHARED` 테이블을 사용하는 SQL Segment를 생성하는 경우 카탈로그 ID를 지정해야 합니다. 예를 들어:

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### SQL 반전이 필요한지 판단하기 {#determining-if-you-need-to-invert-sql}

이벤트가 0건인 사용자를 직접 쿼리하는 것은 불가능하지만, **SQL 반전**을 사용하여 이러한 사용자를 타겟팅할 수 있습니다.

예를 들어, 구매가 3건 미만인 사용자를 타겟팅하려면 먼저 구매가 3건 이상인 사용자를 선택하는 쿼리를 작성합니다. 그런 다음 **SQL 반전**을 선택하여 구매가 3건 미만인 사용자(구매가 0건인 사용자 포함)를 타겟팅합니다.

![SQL 반전 옵션이 선택된 "지난 30일 동안 이메일을 1~4회 클릭한 사용자"라는 이름의 세그먼트 확장.]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:70%;"}

{% alert important %}
이벤트가 0건인 사용자를 특별히 타겟팅하려는 경우가 아니라면 SQL을 반전할 필요가 없습니다. **SQL 반전**이 선택된 경우, 해당 기능이 필요한지 그리고 Segment가 원하는 오디언스와 일치하는지 확인하세요. 예를 들어, 쿼리가 이벤트가 1건 이상인 사용자를 타겟팅하는 경우, 반전하면 이벤트가 0건인 사용자만 타겟팅하게 됩니다.
{% endalert %}

## Segment 멤버십 새로고침 {#refreshing-segment-membership}

카탈로그 Segment의 Segment 멤버십을 새로고침하려면 카탈로그 Segment를 열고 **동작** > **새로고침** > **예, 새로고침**을 선택합니다.

{% alert tip %}
사용자가 정기적으로 진입하고 이탈할 것으로 예상되는 Segment를 생성한 경우, Campaign 또는 Canvas에서 해당 Segment를 타겟팅하기 전에 사용하는 카탈로그 Segment를 수동으로 새로고침하세요.
{% endalert %}

### 새로고침 설정 지정하기 {#designating-refresh-settings}

{% multi_lang_include segments.md section='Refresh settings' %}

## 활용 사례 {#use-cases}

{% tabs local %}
{% tab Health %}

### 건강 앱 {#health-app}

건강 앱이 있고 치과 방문을 예약한 사용자를 세그먼트하려고 한다고 가정합니다. 또한 다음이 있습니다:

- 환자가 예약할 수 있는 다양한 의사가 포함된 카탈로그 `Doctors`(각각 `doctor ID`가 할당됨)
- 카탈로그의 `doctor ID` 필드와 동일한 값을 공유하는 `doctor ID` 속성정보가 있는 커스텀 이벤트 `Booked Visit`
- `dental` 값이 포함된 카탈로그 내의 `speciality` 필드

다음 변수를 사용하여 카탈로그 Segment를 설정합니다:

| 변수 | 속성정보 |
| --- | --- |
| `Catalog` | Doctors |
| `Catalog field` | doctor ID |
| `Custom event` | Booked Visit |
| `Custom event property` | doctor ID |
| `(Under Filter SQL Results) Catalog field` | Specialty |
| `(Under Filter SQL Results) Value` | Dental |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Health app" }

{% endtab %}
{% tab SaaS %}

### SaaS 플랫폼 {#saas-platform}

B2B SaaS 플랫폼이 있고 기존 고객의 직원인 사용자를 세그먼트하려고 한다고 가정합니다. 또한 다음이 있습니다:

- 현재 SaaS 플랫폼을 사용 중인 다양한 계정이 포함된 카탈로그 `Accounts`(각각 `account ID`가 할당됨)
- 카탈로그의 "account ID" 필드와 동일한 값을 공유하는 "account ID" 속성정보가 있는 커스텀 이벤트 `Event Attendance`
- `enterprise` 값이 포함된 카탈로그 내의 `Classification` 필드

다음 변수를 사용하여 카탈로그 Segment를 설정합니다:

| 변수 | 속성정보 |
| --- | --- |
| `Catalog` | Accounts |
| `Catalog field ` | account ID |
| `Custom event` | Event Attendance |
| `Custom event property` | account ID |
| `(Under Filter SQL Results) Catalog field` | Classification |
| `(Under Filter SQL Results) Value` | Enterprise |
{: .reset-td-br-1 .reset-td-br-2 aria-label="SaaS platform" }

{% endtab %}
{% endtabs %}

## 자주 묻는 질문 {#frequently-asked-questions}

### 카탈로그 Segment를 실행하면 SQL 세그먼트 확장 크레딧이 소비되나요? {#does-running-a-catalog-segment-consume-sql-segment-extension-credits}

예, 카탈로그 Segments는 SQL로 구동되며 SQL 세그먼트 확장 크레딧을 소비합니다. 자세한 내용은 [SQL Segments 사용량]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/#monitoring-your-sql-segments-usage)을 확인하세요.

### 카탈로그 Segment를 생성하면 SQL 세그먼트 확장 할당량이 소비되나요? {#does-creating-a-catalog-segment-consume-sql-segment-extension-allotments}

예. SQL 세그먼트 확장이 세그먼트 확장 할당량에 포함되는 것과 동일하게, 카탈로그 Segments도 해당 할당량에 포함됩니다.

### 현재 템플릿이 지원하지 않는 카탈로그 Segment 사용 사례가 있습니다. 어떻게 설정해야 하나요? {#i-have-a-catalog-segment-use-case-that-the-current-template-doesnt-serve-how-should-i-set-that-up}

고객지원 매니저에게 문의하거나 [Braze 고객지원]({{site.baseurl}}/user_guide/administer/personal/braze_support/)에 연락하여 추가 안내를 받으세요.