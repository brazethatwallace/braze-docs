---
nav_title: "Delta Sharing"
article_title: Databricks Delta Sharing
page_order: 0
description: "이 참조 문서에서는 Braze와의 Databricks Delta Sharing(비공개 베타)에 대해 다루며, Databricks 계정에서 Braze 참여 및 Campaign 데이터에 액세스할 수 있는 방법을 설명합니다."
page_type: partner
search_tag: Partner
permalink: /delta_sharing/
hidden: true
---

# Databricks Delta Sharing

> Databricks [Delta Sharing](https://docs.databricks.com/en/delta-sharing/index.html)을 사용하면 Braze 참여 및 Campaign 데이터를 Databricks 환경으로 안전하게 공유할 수 있습니다. 이 문서에서는 데이터 제공자인 Braze에서 수신자인 Databricks 계정으로의 공유 작동 방식과 공유 테이블을 쿼리하는 방법을 설명합니다.

{% alert important %}
Braze와의 Databricks Delta Sharing은 **비공개 베타** 단계입니다. 가용성, 지원 리전 및 제품 동작은 변경될 수 있습니다. 참여하거나 워크스페이스에서 이 기능이 활성화되어 있는지 확인하려면 Braze 고객 성공 매니저에게 문의하세요.
{% endalert %}

Databricks Delta Sharing은 Braze 데이터 배포의 일부입니다. 데이터 배포 옵션에 대한 전체 개요는 [데이터 배포]({{site.baseurl}}/user_guide/data/distribution/)를 참조하세요.

## Delta Sharing 설정 {#set-up-delta-sharing}

Databricks에서 데이터 공유는 데이터 제공자와 데이터 수신자 간에 이루어집니다. Braze 계정은 공유를 생성하고 전송하는 **데이터 제공자**이며, Databricks 계정은 공유를 소비하여 쿼리할 수 있는 카탈로그를 생성하는 **데이터 수신자**입니다. 자세한 내용은 [Databricks 간 Delta Sharing을 사용하여 공유된 데이터 읽기(수신자용)](https://docs.databricks.com/en/delta-sharing/read-data-databricks.html)에 대한 Databricks 설명서를 참조하세요.

### 1단계: Braze에서 공유 구성 {#step-1-configure-sharing-from-braze}

1. Braze에서 **Partner Integrations** > **Data Sharing** > **Databricks Delta Sharing**으로 이동합니다.
2. Databricks 공유 식별자를 입력합니다.
3. 완료되면 **Create Datashare**를 선택합니다. Braze가 Databricks 계정으로 공유를 전송합니다.

### 2단계: Databricks에서 카탈로그 생성 {#step-2-create-a-catalog-in-databricks}

1. 몇 분 후 Databricks 계정에서 인바운드 공유를 수신해야 합니다.
2. 인바운드 공유를 사용하여 테이블을 보고 쿼리할 카탈로그를 생성합니다. 예시:
    {% raw %}
    ```sql
    CREATE CATALOG [IF NOT EXISTS] <catalog-name> USING SHARE braze.<share-name>;
    ```
    {% endraw %}
3. 적절한 사용자와 그룹이 새 카탈로그를 쿼리할 수 있도록 권한을 부여합니다.

{% alert warning %}
공유된 데이터는 Databricks 워크스페이스에서 읽기 전용입니다. 다른 데이터처럼 쿼리할 수 있지만, 공유를 통해 공유 테이블의 행을 수정하거나 삭제할 수는 없습니다.
{% endalert %}

## 사용 및 시각화 {#usage-and-visualization}

데이터 공유가 프로비저닝된 후, 수신 공유에서 카탈로그를 생성하면 공유 테이블이 Databricks 워크스페이스에 표시되며 저장된 다른 데이터처럼 쿼리할 수 있습니다. 공유된 데이터는 읽기 전용으로 유지됩니다.

Currents와 유사하게 Databricks Delta Sharing을 사용하여 다음을 수행할 수 있습니다:

- 복잡한 보고서 생성
- 기여도 모델링 수행
- 회사 내 안전한 공유
- 원시 이벤트 또는 사용자 데이터를 CRM(예: Salesforce)에 매핑
- 기타

Databricks에서 사용 가능한 테이블 및 열의 전체 목록은 [Databricks 원시 테이블 스키마 다운로드]({% image_buster /assets/download_file/databricks-data-sharing-raw-table-schemas.txt %})에서 텍스트 파일로 확인할 수 있습니다. 이 파일은 Databricks Delta Sharing 스키마(예: 수집 시간의 `DB_CREATED_AT`)를 반영합니다. [Snowflake 원시 테이블 스키마]({% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %}) 또는 Snowflake 이름 지정 및 필드를 설명하는 [SQL 테이블 참조]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments/sql_segments_tables/)와는 호환되지 않습니다.

{% alert note %}
비공개 베타 기간 동안 Databricks 스키마 파일에 나열된 모든 테이블이 공유에서 사용 가능하지 않을 수 있습니다. 열 이름과 유형도 Snowflake 데이터 공유와 다를 수 있습니다(예: `SF_CREATED_AT` 대신 `DB_CREATED_AT`). 워크스페이스의 현재 테이블 목록이 필요한 경우 Braze 고객 성공 매니저에게 문의하세요.
{% endalert %}

### 사용자 ID 스키마 {#user-id-schema}

사용자 ID에 대한 Braze와 Databricks 이름 지정 규칙의 차이점을 참고하세요.

| Braze 스키마 | Databricks 스키마 | 설명 |
| ----------- | ----------- | ----------- |
| `braze_id` | `USER_ID` | Braze가 자동으로 할당하는 고유 식별자입니다. |
| `external_id` | `EXTERNAL_USER_ID` | Braze에서 설정한 사용자 프로필의 고유 식별자입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="User ID schema" }

## 중요 정보 및 제한 사항 {#important-information-and-limitations}

### 비공개 베타 가용성 {#closed-beta-availability}

비공개 베타 기간 동안 공유에 [Databricks 원시 테이블 스키마]({% image_buster /assets/download_file/databricks-data-sharing-raw-table-schemas.txt %}) 파일의 모든 테이블이 포함되지 않을 수 있습니다. 공유된 데이터는 열 이름과 유형에서 Snowflake 데이터 공유와 다를 수도 있습니다. 예를 들어, Databricks 공유는 수집 시간에 `DB_CREATED_AT`를 사용하고, Snowflake 공유는 `SF_CREATED_AT`를 사용합니다.

### 호환성을 깨는 변경과 깨지 않는 변경 {#breaking-versus-non-breaking-changes}

#### 호환성을 깨지 않는 변경 {#non-breaking-changes}

호환성을 깨지 않는 변경은 언제든지 발생할 수 있으며 일반적으로 추가 기능을 제공합니다. 호환성을 깨지 않는 변경의 예시:

- 새 테이블 또는 뷰 추가
- 기존 테이블 또는 뷰에 열 추가

{% alert important %}
새 열은 호환성을 깨지 않는 변경으로 간주되므로, Braze는 `SELECT *` 쿼리를 사용하는 대신 각 쿼리에서 관심 있는 열을 명시적으로 나열할 것을 강력히 권장합니다. 또는 열을 명시적으로 지정하는 뷰를 생성하고 공유 테이블을 직접 쿼리하는 대신 해당 뷰를 쿼리하세요.
{% endalert %}

#### 호환성을 깨는 변경 {#breaking-changes}

가능한 경우, 호환성을 깨는 변경은 사전 공지 및 마이그레이션 기간이 선행됩니다. 호환성을 깨는 변경의 예시:

- 테이블 또는 뷰 제거
- 기존 테이블 또는 뷰에서 열 제거
- 기존 열의 유형 또는 null 허용 여부 변경

### Databricks 리전 {#databricks-regions}

비공개 베타 기간 동안 지원되는 클라우드 제공자 및 리전은 워크스페이스와 롤아웃에 따라 다를 수 있습니다. 계정에 적용되는 옵션에 대해서는 Braze 고객 성공 매니저에게 문의하세요.

### 보존 정책 {#retention-policy}

비공개 베타 기간 동안 표준 보존 기간을 초과하는 과거 데이터 백필이 제한될 수 있습니다.

해당 `USERS_*_SHARED` 뷰에서 각 이벤트에 대해 최근 2년간의 데이터를 쿼리할 수 있습니다.

### 일반 데이터 보호 규정(GDPR) 준수 {#general-data-protection-regulation-gdpr-compliance}

{% multi_lang_include partners/snowflake_pii_gdpr.md %}

### 공유 데이터 쿼리: `TIME` 및 쿼리 성능 {#querying-shared-data-time-and-query-performance}

데이터 공유 뷰(예: `USERS_BEHAVIORS_CUSTOMEVENT_SHARED`)의 이벤트 데이터는 `TIME` 필드를 기준으로 클러스터링됩니다. 이벤트 발생 시점을 기준으로 필터링할 때는 `TIME`을 기본 필터로 사용하세요. `TIME`을 사용하여 행을 제한하는 쿼리는 클러스터링이 이벤트 시간에 맞춰져 있으므로 `DB_CREATED_AT`로 필터링하는 쿼리보다 일반적으로 더 높은 성능을 보입니다.

| 필드 | 의미 |
| ----- | ------- |
| `TIME` | 이벤트가 발생한 Unix 타임스탬프입니다. 발생 시간으로 필터링할 때 이 필드를 사용하세요. |
| `DB_CREATED_AT` | 행이 Databricks에 로드된 타임스탬프(수집 시간)입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Querying shared data: TIME and query performance" }

### 쿼리의 속도, 성능 및 비용 {#speed-performance-and-cost-of-queries}

데이터에 대해 실행하는 쿼리의 속도, 성능 및 비용은 사용하는 SQL 웨어하우스 크기에 따라 달라집니다. 액세스하는 데이터 양에 따라 쿼리가 성공적으로 완료되려면 더 큰 웨어하우스가 필요할 수 있습니다. 자세한 내용은 [SQL 웨어하우스 생성 및 구성](https://docs.databricks.com/en/compute/sql-warehouse/create.html)(클러스터 크기 및 스케일링 포함)에 대한 Databricks 설명서를 참조하세요.