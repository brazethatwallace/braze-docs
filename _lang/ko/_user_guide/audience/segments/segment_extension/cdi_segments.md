---
nav_title: CDI 세그먼트 확장
article_title: CDI 세그먼트 확장
page_order: 0
page_type: reference
alias: /cdi_segment_extensions/
tool:
- Segments
description: "이 문서에서는 클라우드 데이터 수집(CDI)을 사용하는 CDI 세그먼트 확장을 통해 데이터 웨어하우스를 쿼리하고 Braze에서 오디언스를 정의하는 방법을 설명합니다."

---

# CDI 세그먼트 확장 {#cdi-segment-extensions}

> Braze [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/)(CDI)을 사용하면 데이터 웨어하우스 또는 파일 스토리지 시스템에서 Braze로의 직접 연결을 설정하여 관련 사용자 또는 카탈로그 데이터를 정기적으로 동기화할 수 있습니다.

{% alert warning %}
CDI 세그먼트 확장은 데이터 웨어하우스를 직접 쿼리하므로, 데이터 웨어하우스에서 이러한 쿼리를 실행하는 데 관련된 모든 비용이 발생합니다. CDI 세그먼트 확장은 [SQL 세그먼트 크레딧]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/#monitoring-your-sql-segments-usage)을 소비하지 않으며, 세그먼트 확장 한도에 포함되지 않고, 데이터 포인트를 기록하지 않습니다.
{% endalert %}

## 필수 조건 {#prerequisites}

Braze 워크스페이스 내에서 세분화를 위해 데이터 웨어하우스 데이터를 사용하려면 [연결된 소스]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources/)를 생성한 다음, [세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/) 내에서 CDI 세그먼트를 생성해야 합니다. CDI 세그먼트 확장을 사용하면 CDI 연결을 통해 제공되는 데이터를 활용하여 자체 데이터 웨어하우스를 직접 쿼리하는 SQL을 작성하고, Braze 내에서 타겟팅할 수 있는 사용자 그룹을 생성할 수 있습니다.

## CDI 세그먼트 생성 {#creating-a-cdi-segment}

### 1단계: 소스 설정 {#step-1-set-up-your-source}

첫 번째 CDI 세그먼트 확장을 생성하기 전에, [연결된 소스]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources/)의 단계를 따라 데이터 웨어하우스와 새로운 연결된 소스를 설정합니다.

### 2단계: 세그먼트 생성 {#step-2-create-a-segment}

먼저 새로운 [세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/)을 생성한 다음, **Full refresh**를 선택합니다.

![]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:60%;"}

데이터 소스로 **CDI Data Tables**를 선택합니다.

![]({% image_buster /assets/img/segment/cdi_data_tables.png %}){: style="max-width:60%;"}

CDI 설정의 일부로, CDI 세그먼트 확장에서 사용할 다양한 연결을 선택할 수 있습니다. 각 연결에는 특정 데이터 테이블 세트가 있습니다. 개발팀이 CDI 설정 중에 연결 및 데이터 테이블을 구성할 수 있습니다.

스키마 및 사용 가능한 설명을 포함하여 사용 가능한 데이터 테이블을 보려면 **Reference**를 선택합니다. 준비가 되면 연결을 선택합니다.

![]({% image_buster /assets/img/segment/connection_schema_with_descriptions.png %}){: style="max-width:100%;"}

다음으로, [Braze SQL 구문]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/#writing-sql)을 사용하여 세그먼트에 대한 SQL을 작성합니다.

모든 CDI 세그먼트 확장은 선택된 열로 `external_user_id`를 사용해야 하며, `external_user_id`는 Braze에서 사용자에 대해 설정된 것과 일치해야 합니다.

{% alert important %}
`external_user_id`는 **문자열** 값이어야 합니다. 소스 ID가 숫자로 저장되어 있는 경우(예: `client_id`가 정수인 경우), Braze의 `external_id` 유형과 일치하도록 [SQL에서 문자열로 캐스팅](https://www.w3schools.com/sql/func_sqlserver_cast.asp)하세요.
{% endalert %}

쿼리 결과에 Braze에 존재하지 않는 사용자가 포함된 경우, 해당 사용자는 무시됩니다. Braze는 CDI 세그먼트 확장의 출력을 기반으로 새 사용자를 생성하지 않습니다.

{% alert tip %}
세그먼트 확장을 미리보기하고, 세그먼트 확장을 관리하며, 자동 멤버십 새로고침을 실행하는 방법을 알아보려면 [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/)을 참조하세요.
{% endalert %}

마지막으로, Braze Segment 내에서 [이 세그먼트 확장을 사용]({{site.baseurl}}/user_guide/audience/segments/segment_extension/#step-5-use-your-extension-in-a-segment)하여 이 오디언스에 Campaign 또는 Canvas를 보낼 수 있습니다.

## 고려 사항 {#considerations}

- 세그먼트 확장은 여러 연결이 아닌 하나의 연결에서만 데이터를 참조할 수 있습니다.
- 세그먼트 확장은 CDI 데이터 또는 Braze Snowflake(Currents) 데이터 중 하나를 데이터 소스로 사용할 수 있습니다. 세그먼트 확장 내에서 데이터 소스를 혼합할 수는 없지만, 여러 세그먼트 확장을 생성하여 Segment 내에서 함께 참조할 수 있습니다.

## 문제 해결 {#troubleshooting}

- **클라우드 데이터 수집** 페이지에서 각 연결 동기화에 대해 설정된 최대 런타임에 도달하면 쿼리가 시간 초과될 수 있습니다. 허용되는 최대 런타임은 60분입니다.
- SQL이 데이터 웨어하우스에 적합한 구문으로 작성되었는지 확인하세요.