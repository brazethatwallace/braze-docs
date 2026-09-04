---
nav_title: CDI 세그먼트 확장
article_title: CDI 세그먼트 확장
page_order: 0
page_type: reference
alias: /cdi_segment_extensions/
tool:
- Segments
description: "이 문서에서는 클라우드 데이터 수집을 사용하는 CDI 세그먼트 확장을 통해 데이터 웨어하우스를 쿼리하고 Braze에서 오디언스를 정의하는 방법을 설명합니다."

---

# CDI 세그먼트 확장 {#cdi-segment-extensions}

> Braze [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion)(CDI)을 사용하면 데이터 웨어하우스 또는 파일 스토리지 시스템에서 Braze로의 직접 연결을 설정하여 관련 사용자 또는 카탈로그 데이터를 정기적으로 동기화할 수 있습니다.

{% alert warning %}
CDI 세그먼트 확장은 데이터 웨어하우스를 직접 쿼리하므로, 데이터 웨어하우스에서 이러한 쿼리를 실행하는 데 관련된 모든 비용이 발생합니다. CDI 세그먼트 확장은 [SQL 세그먼트 크레딧]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#credits)을 소비하지 않으며, 세그먼트 확장 한도에 포함되지 않고, 데이터 포인트를 기록하지 않습니다.
{% endalert %}

## 전제 조건 {#prerequisites}

Braze 워크스페이스 내에서 세분화를 위해 데이터 웨어하우스 데이터를 사용하려면, 먼저 [연결된 소스]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources)를 생성한 다음, [세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension) 내에서 CDI 세그먼트를 생성해야 합니다. CDI 세그먼트 확장을 사용하면 CDI 연결을 통해 제공되는 데이터를 활용하여 자체 데이터 웨어하우스를 직접 쿼리하는 SQL을 작성하고, Braze 내에서 타겟팅할 수 있는 사용자 그룹을 생성할 수 있습니다.

## CDI Segment 만들기 {#creating-a-cdi-segment}

### 1단계: 소스 설정하기 {#step-1-set-up-your-source}

첫 번째 CDI 세그먼트 확장을 만들기 전에, [연결된 소스]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources)의 단계를 따라 데이터 웨어하우스에 새로운 연결된 소스를 설정하세요.

### 2단계: Segment 만들기 {#step-2-create-a-segment}

1. **오디언스** > **세그먼트 확장**으로 이동한 다음 **새 확장 만들기**를 선택합니다.
2. **세그먼트 확장 생성 환경 선택** 메뉴에서 **전체 새로 고침(CDI Segments 포함)**을 선택합니다.

![생성 옵션이 포함된 "세그먼트 확장 생성 환경 선택" 메뉴.]({% image_buster /assets/img/segment/segment_extension_modal.png %}){: style="max-width:60%;"}

{: start="3"}
3. **이 세그먼트 확장의 데이터 소스 선택** 메뉴에서 **CDI 데이터 테이블**을 선택합니다. 이 메뉴는 하나 이상의 [연결된 소스]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources)를 설정한 후에만 표시됩니다.

![CDI 데이터 테이블 옵션이 포함된 "이 세그먼트 확장의 데이터 소스 선택" 메뉴.]({% image_buster /assets/img/segment/cdi_data_tables.png %}){: style="max-width:60%;"}

{: start="4"}
4. 사용할 연결을 선택한 다음 쿼리를 작성합니다. 각 연결에는 특정 데이터 테이블 세트가 있습니다. 개발팀이 CDI 설정 중에 연결과 데이터 테이블을 구성할 수 있습니다.
5. **소스 탐색기**를 선택하여 스키마 및 사용 가능한 설명을 포함한 사용 가능한 데이터 테이블을 확인합니다.

![스키마 및 사용 가능한 설명을 포함한 사용 가능한 데이터 테이블을 보여주는 소스 탐색기.]({% image_buster /assets/img/segment/connection_schema_with_descriptions.png %}){: style="max-width:100%;"}

{: start="6"}
6. [Braze SQL 구문]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments#step-2-write-your-sql)을 사용하여 Segment에 대한 SQL을 작성합니다. 모든 CDI 세그먼트 확장은 선택된 열로 `external_user_id`를 사용해야 하며, `external_user_id`는 Braze에서 사용자에 대해 설정된 것과 일치해야 합니다.<br><br>
쿼리 결과에 Braze에 존재하지 않는 사용자가 포함되어 있으면, 해당 사용자는 무시됩니다. Braze는 CDI 세그먼트 확장의 출력 결과를 기반으로 새로운 사용자를 생성하지 않습니다.

{% alert important %}
`external_user_id`는 문자열 값이어야 합니다. 소스 ID가 숫자로 저장되어 있는 경우(예: `client_id`가 정수인 경우), Braze의 `external_id` 타입과 일치하도록 [SQL에서 문자열로 캐스팅](https://www.w3schools.com/sql/func_sqlserver_cast.asp)하세요.
{% endalert %}

{: start="7"}
7. Braze Segment 내에서 [이 세그먼트 확장을 사용]({{site.baseurl}}/user_guide/audience/segments/segment_extension#step-6-use-your-extension-in-a-segment)하여 이 오디언스에 Campaign 또는 Canvas를 보냅니다.

{% alert tip %}
세그먼트 확장을 미리 보고, 세그먼트 확장을 관리하고, 자동 멤버십 새로 고침을 실행하는 방법에 대해 알아보려면 [SQL 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments)을 참조하세요.
{% endalert %}

## 고려 사항 {#considerations}

- 세그먼트 확장은 여러 연결이 아닌 하나의 연결에서만 데이터를 참조할 수 있습니다.
- 세그먼트 확장은 다음 중 하나를 데이터 소스로 사용할 수 있습니다: CDI 데이터 또는 Braze Snowflake(Currents) 데이터. 세그먼트 확장 내에서 데이터 소스를 혼합할 수는 없지만, 여러 세그먼트 확장을 만들어 하나의 Segment 내에서 함께 참조할 수 있습니다.

## 문제 해결 {#troubleshooting}

- 쿼리가 최대 런타임에 도달하면 타임아웃될 수 있습니다. 최대 런타임은 **Cloud Data Ingestion** 페이지에서 각 연결 동기화에 대해 설정됩니다. 허용되는 최대 런타임은 60분입니다.
- SQL이 데이터 웨어하우스에 적합한 구문으로 작성되었는지 확인하세요.