---
nav_title: SQL 편집기
article_title: "클라우드 데이터 수집: SQL 편집기"
description: "SQL 쿼리를 사용하여 클라우드 데이터 수집 동기화를 생성하고 검증하는 방법을 알아보세요."
page_order: 11
page_type: reference
toc_headers: h2
---

# 클라우드 데이터 수집: SQL 편집기 {#cloud-data-ingestion-sql-editor}

> 이 페이지에서는 Braze 클라우드 데이터 수집(CDI) SQL 편집기를 사용하여 SQL 쿼리로 동기화를 생성하고 검증하는 방법을 다룹니다.

클라우드 데이터 수집의 SQL 편집기를 사용하면 데이터 웨어하우스에 대해 SQL 쿼리를 직접 작성하여 동기화를 생성할 수 있습니다. 이를 통해 전용 CDI 테이블을 생성하거나 유지 관리할 필요가 없어지며, 이전에는 [데이터 웨어하우스 통합의 1.1단계]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)에서 이 작업이 필요했습니다.

SQL 편집기는 다음과 같은 경우에 사용합니다:

- 업스트림 테이블을 수정하지 않고 데이터를 동기화하려는 경우
- 데이터 웨어하우스의 원시 데이터로 작업하려는 경우
- `PAYLOAD` 열을 구성하지 않으려는 경우
- SQL을 사용하여 더 복잡한 데이터 사용 사례를 처리하려는 경우

{% alert important %}
클라우드 데이터 수집 SQL 편집기는 베타 버전입니다. 액세스하려면 고객 성공 매니저 또는 계정 매니저에게 문의하세요.
{% endalert %}

## 필수 조건 및 제한 사항 {#prerequisites-and-limitations}

SQL 편집기에는 다음과 같은 제한 사항이 있습니다:

- 데이터 웨어하우스 소스에만 사용 가능: Snowflake, Redshift, BigQuery, Databricks, Fabric.
- 단일 문, 읽기 전용 쿼리만 지원됩니다.

{% alert note %}
Braze는 데이터에 대해 읽기 전용 쿼리만 실행하며 기본 테이블을 수정하지 않습니다. 쿼리 실행 중에 임시 오브젝트가 생성될 수 있지만 유지되지는 않습니다.
{% endalert %}

## 새 SQL 편집기 동기화 생성 {#create-a-new-sql-editor-sync}

먼저 소스를 생성한 다음 SQL 편집기로 동기화를 생성하려면 다음 단계를 따르세요. CDI용 소스를 이미 설정한 경우 3단계로 건너뛸 수 있습니다.

{% alert note %}
이 단계에서는 Snowflake 소스를 예시로 사용합니다. 다른 데이터 웨어하우스 소스의 설정 프로세스도 유사하며, [데이터 웨어하우스 통합 설정]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#setting-up-data-warehouse-integrations) 설명서의 [2단계: Braze 대시보드에서 새 소스 생성]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-2-create-a-new-source-in-the-braze-dashboard)에서 확인할 수 있습니다.
{% endalert %}

### 1단계: Snowflake 역할, 권한, 데이터 웨어하우스 및 사용자 설정 {#step-1-set-up-your-snowflake-role-permissions-warehouse-and-user}

CDI에서 Snowflake 소스를 생성하기 전에, Braze가 사용하는 Snowflake 사용자가 쿼리하려는 데이터에 대한 액세스 권한과 쿼리를 실행할 데이터 웨어하우스를 갖고 있는지 확인하세요.

#### 1.1단계: (선택 사항) 데이터베이스 및 스키마 생성 {#step-11-optional-create-a-database-and-schema}

필요한 경우 CDI 데이터를 위한 전용 데이터베이스와 스키마를 생성합니다:

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```

#### 1.2단계: 역할 및 데이터베이스 권한 설정 {#step-12-set-up-role-and-database-permissions}

동기화하려는 테이블에 대한 액세스 권한을 부여합니다:

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.MY_USER_TABLE TO ROLE BRAZE_INGESTION_ROLE;
```

사용 사례에 따라 여러 테이블이나 향후 테이블에 대한 액세스 권한을 부여할 수도 있습니다. 예를 들어, 스키마의 모든 향후 테이블에 대한 액세스 권한을 부여하려면:

```sql
GRANT SELECT ON FUTURE TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
```

#### 1.3단계: 데이터 웨어하우스 설정 및 Braze 역할에 액세스 권한 부여 {#step-13-set-up-the-warehouse-and-grant-access-to-the-braze-role}

Braze가 쿼리를 실행할 데이터 웨어하우스를 생성합니다:

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
데이터 웨어하우스에 자동 재개 플래그가 활성화되어 있어야 합니다. 활성화되어 있지 않은 경우, 쿼리 실행 시 Braze가 데이터 웨어하우스를 켤 수 있도록 추가 `OPERATE` 권한을 부여하세요.
{% endalert %}

#### 1.4단계: Snowflake 사용자 생성 {#step-14-create-a-snowflake-user}

Braze용 사용자를 생성하고 역할을 할당합니다:

```sql
CREATE USER BRAZE_INGESTION_USER;
GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

Braze에서 Snowflake 소스를 구성할 때 이 사용자를 사용합니다.

### 2단계: Braze 대시보드에서 새 소스 생성 {#step-2-create-a-new-source-in-the-braze-dashboard}

이 단계에서는 Braze에서 Snowflake 소스를 생성하고 연결을 검증합니다.

#### 2.1단계: Snowflake 소스 추가 {#step-21-add-a-snowflake-source}

1. Braze 대시보드에서 **데이터 설정** > **클라우드 데이터 수집** > **소스**로 이동합니다.
2. **데이터 소스 추가**를 선택합니다.
3. **Snowflake**를 선택합니다.

#### 2.2단계: 연결 세부 정보 입력 {#step-22-enter-connection-details}

소스의 이름을 선택하고 Snowflake 자격 증명 및 구성을 입력합니다.

{% alert note %}
**Snowflake Account Locator** 필드에는 Snowflake [계정 식별자](https://docs.snowflake.com/en/user-guide/admin-account-identifier)를 입력합니다. 일반적으로 `xy12345.us-east-1.aws`와 같은 형식입니다. 이는 데이터베이스 이름이나 데이터 웨어하우스 이름과 다릅니다.
{% endalert %}

#### 2.3단계: RSA 키 설정 완료 {#step-23-complete-rsa-key-setup}

자격 증명과 구성을 입력한 후 **Save credentials**를 선택하고 RSA 키를 생성합니다. 그런 다음 Snowflake로 돌아가서 설정을 완료합니다. 대시보드에 표시된 공개 키를 Braze가 Snowflake에 연결하기 위해 생성한 사용자에게 추가합니다.

자세한 내용은 [Snowflake 키 쌍 인증](https://docs.snowflake.com/en/user-guide/key-pair-auth)을 참조하세요. 키를 교체하려면 Braze에서 새 키 쌍을 생성하고 새 공개 키를 제공할 수 있습니다.

```sql
ALTER USER BRAZE_INGESTION_USER SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BA...';
```

Braze로 돌아가서 **Test connection**을 선택하여 소스 액세스를 확인한 다음 소스를 생성합니다.

### 3단계: 새 동기화 생성 및 SQL 쿼리 작성 {#step-3-create-a-new-sync-and-write-your-sql-query}

1. **데이터 설정** > **클라우드 데이터 수집** > **동기화**로 이동합니다.
2. **Create data sync**를 선택합니다.
3. **데이터 유형**에서 동기화를 선택합니다.
4. 2단계에서 생성한 소스를 참조합니다.
5. **SQL**을 선택하고 데이터 웨어하우스에서 사용자 데이터를 반환하는 SQL 쿼리를 작성합니다. SQL 쿼리는 Braze에 동기화할 데이터를 정의합니다. 쿼리 결과가 동기화의 스키마가 됩니다.

소스 탐색기를 사용하여 동기화할 수 있는 테이블과 뷰를 찾아보거나, AI SQL 생성기를 사용하여 SQL 쿼리에 대한 Braze Operator의 도움을 받을 수 있습니다.

{% alert note %}
`JOIN` 절을 포함한 읽기 전용 쿼리만 지원됩니다. 자세한 내용은 [SQL 제약 조건](#sql-constraints)을 참조하세요.
{% endalert %}

### 4단계: 쿼리 미리보기 및 검증 {#step-4-preview-and-validate-your-query}

**Preview and validate**를 선택하여 쿼리를 실행합니다.

미리보기:

- 결과를 테이블 형식으로 표시합니다
- 최대 100개 행을 표시합니다
- 최대 250개 열을 표시합니다

검증을 성공적으로 통과하려면 SQL 쿼리가 다양한 필수 열을 반환해야 합니다:

| 동기화 데이터 유형 | 필수 열 |
|---|---|
| 속성 | - 사용자 식별자, `external_id`, `braze_id`, `alias_name` 및 `alias_label`, 이메일 또는 전화번호 중 하나.<br>- `UPDATED_AT`.<br>- 동기화할 최소 하나의 추가 열(속성). |
| 사용자 삭제 | - 사용자 식별자, `external_id`, `braze_id`, `alias_name` 및 `alias_label`, 이메일 또는 전화번호 중 하나.<br>- `UPDATED_AT`. |
| Canvas 트리거 | - 사용자 식별자, `external_id`, `braze_id`, `alias_name` 및 `alias_label`, 이메일 또는 전화번호 중 하나.<br>- `UPDATED_AT`. |
| 커스텀 이벤트 | - 사용자 식별자, `external_id`, `braze_id`, `alias_name` 및 `alias_label`, 이메일 또는 전화번호 중 하나.<br>- `UPDATED_AT`.<br>- 이벤트 이름을 나타내는 `NAME`.<br>- 이벤트 시간을 나타내는 `TIME`. 사용할 수 없는 경우 CDI가 `UPDATED_AT`을 대체로 사용합니다. |
| 구매 이벤트 | - 사용자 식별자, `external_id`, `braze_id`, `alias_name` 및 `alias_label`, 이메일 또는 전화번호 중 하나.<br>- `UPDATED_AT`.<br>- `PRODUCT_ID`.<br>- `CURRENCY`.<br>- `PRICE`.<br>- 구매 이벤트 시간을 나타내는 `TIME`. 사용할 수 없는 경우 CDI가 `UPDATED_AT`을 대체로 사용합니다. |
| 카탈로그 | - 카탈로그 항목 식별자를 나타내는 `ID`.<br>- `UPDATED_AT`.<br>- 동기화할 최소 하나의 추가 열(카탈로그 필드). |
| 계정 | - 계정 식별자를 나타내는 `ID`.<br>- 계정 이름을 나타내는 `NAME`.<br>- `UPDATED_AT`.<br>- 동기화할 최소 하나의 추가 열(계정 필드). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="4단계: 쿼리 미리보기 및 검증" }

필수 열 외의 추가 열은 각각 속성, Canvas 컨텍스트 등록정보, 이벤트 등록정보, 카탈로그 필드, 계정 필드로 동기화됩니다. 미리보기 및 검증 오류에 대한 유용한 팁과 수정 방법은 [검증 동작](#validation-behavior) 및 [문제 해결](#troubleshooting)을 참조하세요.

### 5단계: 속성 매핑 검토 및 동기화 생성 {#step-5-review-attribute-mapping-and-create-sync}

검증이 성공하면 **Next: Notifications**로 계속 진행하여 동기화를 생성합니다.

{% alert important %}
부정확한 SQL 구성은 데이터 포인트의 과다 소비 및 광범위한 운영 리스크를 포함한 의도하지 않은 결과를 초래할 수 있습니다. 쿼리 로직이 올바른지 확인하는 것은 사용자의 책임이며, 동기화를 활성화하기 전에 모든 결과를 신중하게 미리보기해야 합니다.
{% endalert %}

## SQL 제약 조건 {#sql-constraints}

### `SELECT` 쿼리만 사용 {#use-select-queries-only}

읽기 전용 쿼리만 지원됩니다.

사용할 수 있는 항목:

- `SELECT`
- `WITH` (CTE)
- `JOIN`

사용할 수 없는 항목:

- `INSERT`, `UPDATE` 또는 `DELETE`
- `CREATE` 또는 `DROP`
- `;`로 구분된 여러 문

### 단일 문 사용 {#use-a-single-statement}

쿼리는 단일 실행 가능한 문이어야 합니다.

## 검증 동작 {#validation-behavior}

SQL 편집기는 진행하기 전에 쿼리를 검증합니다.

### SQL 오류 {#sql-errors}

쿼리에 구문 오류가 포함된 경우:

- 검증이 실패합니다
- 미리보기가 표시되지 않습니다
- 데이터 웨어하우스에서 오류 메시지를 반환합니다

### 컴파일 오류 {#compilation-errors}

쿼리가 유효하지 않은 테이블, 열 또는 권한이 없는 오브젝트를 참조하는 경우:

- 검증이 실패합니다
- 미리보기가 표시되지 않습니다
- 데이터 웨어하우스에서 오류 메시지를 반환합니다

### 연결 오류 {#connection-errors}

Braze가 데이터 웨어하우스에 연결할 수 없는 경우:

- 검증이 실패합니다
- 미리보기가 표시되지 않습니다
- 연결 오류 메시지가 표시됩니다

### 쿼리 시간 초과 {#query-timeout}

쿼리가 너무 오래 실행되는 경우:

- Braze가 쿼리를 종료합니다
- 검증이 실패합니다
- 시간 초과 오류가 표시됩니다

### 테이블 스키마 오류 {#table-schema-errors}

쿼리가 컴파일되더라도 다음과 같은 경우 검증이 실패할 수 있습니다:

- 식별자 열이 발견되지 않은 경우
- `UPDATED_AT`이 누락된 경우
- 기타 필수 열이 누락된 경우

이 경우 성공적인 검증을 위해 미리보기가 계속 표시됩니다. 각 동기화 데이터 유형에 필요한 열에 대한 자세한 내용은 [이전 섹션의 4단계](#step-4-preview-and-validate-your-query)를 참조하세요.

### 결과가 0행인 경우 {#zero-row-results}

쿼리가 0행을 반환하는 경우:

- 검증이 **통과**합니다
- 동기화를 계속 생성할 수 있습니다
- 행이 반환될 때까지 사용자가 업데이트되지 않습니다

## `PAYLOAD` 지원 (레거시) {#payload-support-legacy}

SQL 편집기는 `PAYLOAD` 열이 있는 [레거시 CDI 테이블]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations?tab=snowflake#step-1-set-up-tables-or-views)을 지원합니다.

쿼리에 다음이 포함된 경우:

- 유효한 식별자
- `UPDATED_AT`
- `PAYLOAD` 열
- 추가 열

그러면:

- Braze는 `PAYLOAD` 열만 동기화합니다
- Braze는 추가 열을 무시합니다

## SQL 동기화 편집 {#edit-a-sql-sync}

기존 동기화를 편집할 때:

- SQL 변경 사항은 재검증이 필요합니다
- 유효하지 않은 변경 사항은 저장할 수 없습니다
- 유효한 변경 사항은 저장 후 적용됩니다

동기화 실행이 이미 진행 중인 경우 변경 사항은 다음 실행에 적용됩니다.

## 문제 해결 {#troubleshooting}

이 섹션에는 일반적인 오류와 문제 해결 방법이 포함되어 있습니다.

### 미리보기를 사용할 수 없음 {#no-preview-available}

"미리보기를 사용할 수 없음"이 표시되면 다음 기본 오류 유형 중 하나가 원인일 수 있습니다.

| 오류 유형 | 해결 단계 |
|---|---|
| "미리보기를 사용할 수 없음" | 오류 배너에서 힌트를 확인하세요. |
| "소스에 연결할 수 없음" | 구성된 사용자 이름, 계정 로케이터 및 RSA 키 쌍 인증 설정을 확인하세요.<br>데이터 웨어하우스가 실행 중인지 확인하세요.<br>네트워크 액세스를 확인하세요. |
| "SQL 구문 오류" | SQL 구문을 확인하세요. |
| "오브젝트가 존재하지 않거나 권한이 없음" | 역할에 테이블에 대한 `SELECT` 액세스 권한이 있는지 확인하세요.<br>데이터베이스 및 스키마 권한을 확인하세요.<br>테이블 이름 오타를 확인하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="미리보기를 사용할 수 없음" }

### 식별자 열 필수 {#identity-column-required}

쿼리에 `external_id`와 같은 유효한 식별자가 포함되어 있는지 확인하세요.

### `UPDATED_AT` 열 누락 {#updated_at-column-is-missing}

증분 동기화를 위한 타임스탬프 열을 추가하세요.

### 동기화할 속성/카탈로그 필드/계정 필드가 없음 {#add-more-columns-there-are-no-attributescatalog-fieldsaccount-fields-to-sync}

식별자와 `UPDATED_AT` 외에 최소 하나의 추가 열을 추가하세요.

### 쿼리 실행 시간 초과 {#query-execution-timed-out}

쿼리를 최적화하거나 더 큰 데이터 웨어하우스를 사용하세요.