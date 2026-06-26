---
nav_title: FAQ
article_title: 클라우드 데이터 수집 FAQ
page_order: 10
page_type: FAQ
description: "이 페이지에서는 클라우드 데이터 수집에 대해 자주 묻는 질문에 대한 답변을 제공합니다."
toc_headers: h2
---

# 자주 묻는 질문 {#frequently-asked-questions}

> 이 페이지에서는 클라우드 데이터 수집에 대해 자주 묻는 질문에 대한 답변을 제공합니다.

## "CDI 동기화 중 오류가 발생했습니다"라는 이메일을 받은 이유는 무엇인가요? {#why-was-i-emailed-error-in-cdi-sync}

이러한 유형의 이메일은 일반적으로 CDI 설정에 문제가 있음을 의미합니다. 다음은 몇 가지 일반적인 문제와 해결 방법입니다:

### CDI가 자격 증명을 사용하여 데이터 웨어하우스 또는 테이블에 액세스할 수 없습니다 {#cdi-cant-access-the-data-warehouse-or-table-using-your-credentials}

이는 CDI의 자격 증명이 잘못되었거나 데이터 웨어하우스에서 잘못 구성되었음을 의미할 수 있습니다. 자세한 내용은 [데이터 웨어하우스 통합]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/)을 참조하세요.

### 테이블을 찾을 수 없습니다 {#the-table-cannot-be-found}

올바른 데이터베이스 구성으로 통합을 업데이트하거나 데이터 웨어하우스에서 일치하는 리소스(예: `database/table`)를 생성해 보세요.

### 카탈로그를 찾을 수 없습니다 {#the-catalog-cannot-be-found}

통합에 설정된 카탈로그가 Braze 카탈로그에 존재하지 않습니다. 통합이 설정된 후에 카탈로그가 제거되었을 수 있습니다. 이 문제를 해결하려면 다른 카탈로그를 사용하도록 통합을 업데이트하거나 통합의 카탈로그 이름과 일치하는 새 카탈로그를 만드세요.

## "CDI 동기화에서 행 오류가 발생했습니다"라는 이메일을 받은 이유는 무엇인가요? {#why-was-i-emailed-row-errors-in-your-cdi-sync}

이러한 유형의 이메일은 동기화 중에 일부 데이터를 처리할 수 없었음을 의미합니다. 구체적인 오류를 확인하려면 **CDI** > **동기화 로그**로 이동하여 Braze에서 로그를 검토할 수 있습니다.

## 연결 테스트 및 고객지원 이메일의 오류를 수정하려면 어떻게 하나요? {#how-do-i-fix-errors-for-test-connection-and-support-emails}

{% tabs %}
{% tab Snowflake %}
### 테스트 연결이 느리게 실행됨 {#test-connection-runs-slow}

테스트 연결은 데이터 웨어하우스에서 실행되므로 웨어하우스 용량을 늘리면 속도가 향상될 수 있습니다. 서버리스 SQL 인스턴스를 사용하면 워밍업 시간이 최소화되고 쿼리 처리량이 향상되지만 통합 비용이 약간 높아질 수 있습니다.

### Snowflake 인스턴스에 연결하는 중 오류 발생: 해당 IP의 수신 요청은 Snowflake에 액세스할 수 없습니다 {#error-connecting-to-snowflake-instance-incoming-request-with-ip-is-not-allowed-to-access-snowflake}

공식 Braze IP를 IP 허용 목록에 추가해 보세요. 자세한 내용은 [데이터 웨어하우스 통합]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/)을 참조하거나 관련 IP를 허용하세요:

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

### 고객 구성으로 인해 SQL 실행 중 오류 발생: 002003 (42S02): SQL 컴파일 오류: 존재하지 않거나 권한이 없습니다 {#error-executing-sql-due-to-customer-config-002003-42s02-sql-compilation-error-does-not-exist-or-not-authorized}

테이블이 존재하지 않으면 테이블을 생성하세요. 테이블이 존재하는 경우 사용자 및 역할에 테이블에서 읽을 수 있는 권한이 있는지 확인하세요.

### 스키마를 사용할 수 없습니다 {#could-not-use-schema}

이 오류가 발생하면 지정된 사용자 또는 역할에 대해 해당 스키마에 대한 액세스 권한을 부여하세요.

### 역할을 사용할 수 없습니다 {#could-not-use-role}

이 오류가 발생하면 해당 사용자가 지정된 역할을 사용할 수 있도록 허용하세요.

### 사용자 액세스 비활성화 {#user-access-disabled}

이 오류가 발생하면 해당 사용자가 Snowflake 계정에 액세스할 수 있도록 허용하세요.

### 현재 및 이전 키로 Snowflake 인스턴스에 연결하는 중 오류 발생 {#error-connecting-to-snowflake-instance-with-current-and-old-key}

이 오류가 발생하면 사용자가 Braze 대시보드에 표시된 현재 공개 키를 사용하고 있는지 확인하세요.
{% endtab %}

{% tab Redshift %}
### 테스트 연결이 느리게 실행됨

테스트 연결은 데이터 웨어하우스에서 실행되므로 웨어하우스 용량을 늘리면 속도가 향상될 수 있습니다. 서버리스 SQL 인스턴스를 사용하면 워밍업 시간을 최소화하고 쿼리 처리량을 향상시킬 수 있지만, 통합 비용이 약간 증가할 수 있습니다.

### 관계 {table_name}에 대한 권한이 거부되었습니다 {#permission-denied-for-relation-tablename}

이 오류가 발생하는 경우:

  - 해당 사용자에 대한 스키마에 `usage` 권한을 부여하세요.
  - 해당 사용자에 대해 테이블에 `select` 권한을 부여하세요.

### 연결 생성 오류 {#create-connection-error}

이 오류가 발생하면 Redshift 엔드포인트와 포트가 올바른지 확인하세요.

### SSH 터널 생성 오류 {#create-ssh-tunnel-error}

이 오류가 발생하는 경우:

  - Braze 대시보드의 공개 키가 SSH 터널링에 사용되는 ec2 호스트에 있는지 확인하세요.
  - 사용자 이름이 올바른지 확인하세요.
  - SSH 터널이 올바른지 확인하세요.
{% endtab %}

{% tab BigQuery %}
### 테스트 연결이 느리게 실행됨

테스트 연결은 데이터 웨어하우스에서 실행되므로 웨어하우스 용량을 늘리면 속도가 향상될 수 있습니다. 서버리스 SQL 인스턴스를 사용하면 워밍업 시간이 최소화되고 쿼리 처리량이 향상되지만 통합 비용이 약간 높아질 수 있습니다.

### 사용자에게 테이블을 쿼리할 수 있는 권한이 없습니다 {#user-does-not-have-permission-to-query-table}

이 오류가 발생하면 테이블을 쿼리할 수 있는 사용자 권한을 추가하세요.

### 사용량이 커스텀 할당량을 초과했습니다 {#your-usage-exceeded-the-custom-quota}

이 오류가 발생하면 현재 속도로 동기화를 계속할 수 있도록 할당량을 업데이트해야 합니다.

### 위치 {region}에서 테이블을 찾을 수 없습니다 {#table-was-not-found-in-location-region-location}

이 오류가 발생하면 테이블이 올바른 프로젝트 및 데이터세트에 있는지 확인하세요.

### 잘못된 JWT 서명 {#invalid-jwt-signature}

이 오류가 발생하면 계정에 대해 BigQuery API 서비스가 활성화되어 있는지 확인하세요.
{% endtab %}

{% tab Databricks %}
### 테스트 연결이 느리게 실행됨

테스트 연결은 데이터 웨어하우스에서 실행되므로 웨어하우스 용량을 늘리면 속도가 향상될 수 있습니다. Databricks의 경우, Braze가 Classic 및 Pro SQL 인스턴스에 연결할 때 2~5분의 워밍업 시간이 있을 수 있으며, 이로 인해 연결 설정 및 테스트 중뿐만 아니라 스케줄된 동기화 시작 시에도 지연이 발생할 수 있습니다. 서버리스 SQL 인스턴스를 사용하면 워밍업 시간이 최소화되고 쿼리 처리량이 향상되지만 통합 비용이 약간 높아질 수 있습니다.

### 웨어하우스가 중지되어 명령이 실패했습니다 {#command-failed-because-warehouse-was-stopped}

이 오류가 발생하면 Databricks 웨어하우스가 실행 중인지 확인하세요.

### 서비스: Amazon S3; 상태 코드: 403; 오류 코드: 403 Forbidden {#service-amazon-s3-status-code-403-error-code-403-forbidden}

이 오류가 발생하면 [Databricks: S3 데이터에 액세스하는 동안 Forbidden 오류 발생](https://kb.databricks.com/security/forbidden-access-to-s3-data)을 참조하세요.
{% endtab %}
{% endtabs %}

## CDI 통합에 대한 이메일 알림 기본 설정을 업데이트하려면 어떻게 해야 하나요? {#how-do-i-update-my-email-alert-preferences-for-cdi-integrations}

각 통합에는 고유한 알림 기본 설정이 있습니다. CDI 페이지로 이동하여 업데이트할 통합 이름을 선택하세요. **알림 환경설정** 섹션에서 선택한 통합에 관한 알림 수신 방법을 업데이트할 수 있습니다.

## 미래의 UPDATED_AT이 통합과 동기화되면 어떻게 되나요? {#what-happens-if-a-future-updatedat-gets-synced-with-an-integration}

CDI는 `UPDATED_AT`을 사용하여 어떤 데이터가 새로운 데이터인지 결정합니다. 미래의 `UPDATED_AT`이 동기화되면 해당 미래 날짜 및 시간 이전의 모든 데이터는 처리되지 않습니다. 이 문제를 해결하려면:

1. `UPDATED_AT`을 수정하세요.
2. 이미 Braze와 동기화된 이전 데이터를 모두 제거하세요.
3. 새 통합을 생성하여 해당 테이블을 다시 처리하세요.

## "동기화된 행 수"가 웨어하우스의 숫자와 일치하지 않는 이유는 무엇인가요? {#why-doesnt-rows-synced-match-the-number-in-my-warehouse}

CDI는 `UPDATED_AT`을 사용하여 동기화 중에 어떤 레코드를 가져올지 결정합니다. [이 그림]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/#what-gets-synced)을 통해 작동 방식을 확인하세요. 동기화 실행 시작 시, CDI는 웨어하우스에 쿼리하여 이전에 처리된 `UPDATED_AT` 값보다 이후의 모든 레코드를 가져옵니다. 정확한 경계 타임스탬프에 있는 레코드도 새 행이 해당 타임스탬프를 공유하는 경우 다시 동기화될 수 있습니다. 쿼리가 실행되는 시점에 수집된 모든 레코드는 Braze에 동기화됩니다. 다음은 레코드가 동기화되지 않을 수 있는 일반적인 경우입니다:

- 이미 처리된 `UPDATED_AT` 값으로 테이블에 레코드를 추가하고 있습니다.
- 동기화를 통해 레코드 값이 처리된 후 업데이트하면서 `UPDATED_AT`은 변경하지 않고 그대로 두고 있습니다.
- 동기화가 진행되는 동안 레코드를 추가하거나 업데이트하고 있습니다. CDI 쿼리가 실행되는 시기에 따라 레코드가 선택되지 않는 경합 조건이 발생할 수 있습니다.

{% alert tip %}
앞으로 이러한 동작을 방지하려면 단조롭게 증가하는 `UPDATED_AT` 값을 사용하고 스케줄된 동기화 실행 중에 테이블을 업데이트하지 않는 것이 좋습니다.
{% endalert %}

## 대규모 CDI 가져오기에 대부분 고유한 `UPDATED_AT` 값이 필요한가요? {#do-i-need-mostly-distinct-updatedat-values-for-large-cdi-imports}

네. 대용량 실행(예: 약 1,000만 행 이상)의 경우 소스 데이터에 대부분 고유한 `UPDATED_AT` 값이 있는지 확인하세요. 너무 많은 행이 동일한 타임스탬프를 공유하면 CDI가 이후 실행에서 경계 타임스탬프의 행을 다시 선택할 가능성이 높아집니다. 이로 인해 중복 동기화 및 데이터 포인트 소비가 증가할 수 있습니다.

CDI 경계 동작에 대한 자세한 내용은 [중복 타임스탬프가 있는 행의 재동기화 방지]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices/#avoid-resyncing-rows-with-duplicate-timestamps)를 참조하세요.

### 이러한 SQL 검사는 어디에서 실행하나요? {#where-do-i-run-these-sql-checks}

CDI 통합에서 사용하는 동일한 테이블 또는 뷰를 대상으로 데이터 웨어하우스 SQL 편집기에서 직접 검사를 실행하세요:

- Snowflake: **Projects** > **Worksheets** (자세한 내용은 [Snowflake Worksheets](https://docs.snowflake.com/en/user-guide/ui-snowsight-worksheets-gs) 참조)
- Redshift: Query Editor v2 (자세한 내용은 [Using Amazon Redshift Query Editor v2](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-v2.html) 참조)
- BigQuery: BigQuery Studio SQL workspace (자세한 내용은 [BigQuery Studio introduction](https://cloud.google.com/bigquery/docs/bigquery-studio-introduction) 참조)
- Databricks: SQL editor (SQL warehouse) (자세한 내용은 [Databricks SQL editor](https://docs.databricks.com/en/sql/user/sql-editor/) 참조)
- Fabric: SQL query editor

대규모 동기화를 활성화하거나 확장하기 전에 다음 프로세스를 사용하세요:

1. 검증하려는 정확한 CDI 소스 테이블 또는 뷰와 동기화 기간을 식별합니다.
2. 웨어하우스 SQL 편집기를 열고 CDI에서 사용하는 동일한 데이터베이스 및 스키마를 선택한 다음, 소스 테이블 또는 뷰에 대한 읽기 액세스 권한이 있는 역할을 사용합니다.
3. 고유 타임스탬프 수 쿼리를 실행하여 해당 기간에 존재하는 고유한 `UPDATED_AT` 값의 수를 측정합니다.
4. `UPDATED_AT`별로 그룹화하고 행 수를 세는 쿼리를 실행하여 비정상적으로 높은 행 수를 가진 타임스탬프를 찾습니다.
5. 많은 행이 동일한 타임스탬프를 공유하는 경우, 연속 배치가 점진적으로 더 새로운 `UPDATED_AT` 값을 사용하도록 수집 프로세스를 조정하거나 타임스탬프 정밀도를 높여 행이 더 고르게 분포되도록 합니다.
6. 집중도가 줄어들 때까지 두 쿼리를 다시 실행한 다음 동기화를 시작하거나 확장합니다.
7. 시작 후 **CDI** > **동기화 로그**에서 경계 타임스탬프에서의 예상치 못한 재동기화 볼륨을 모니터링합니다.

웨어하우스에서 다음과 같은 검사를 사용하세요:

```sql
SELECT
  COUNT(*) AS total_rows,
  COUNT(DISTINCT UPDATED_AT) AS distinct_timestamps,
  ROUND(COUNT(*) * 1.0 / NULLIF(COUNT(DISTINCT UPDATED_AT), 0), 2) AS avg_rows_per_timestamp
FROM YOUR_CDI_SOURCE_TABLE
WHERE UPDATED_AT >= CAST('2026-04-01 00:00:00' AS TIMESTAMP)
  AND UPDATED_AT < CAST('2026-04-02 00:00:00' AS TIMESTAMP);
```

```sql
SELECT
  UPDATED_AT,
  COUNT(*) AS rows_at_timestamp
FROM YOUR_CDI_SOURCE_TABLE
WHERE UPDATED_AT >= CAST('2026-04-01 00:00:00' AS TIMESTAMP)
  AND UPDATED_AT < CAST('2026-04-02 00:00:00' AS TIMESTAMP)
GROUP BY UPDATED_AT
ORDER BY rows_at_timestamp DESC
LIMIT 20;
```

웨어하우스에서 `LIMIT`를 지원하지 않는 경우(예: Fabric), `TOP`과 같은 동등한 구문을 사용하세요.

## 적은 수의 행으로도 CDI 동기화에 여전히 몇 분이 걸리는 이유는 무엇인가요? {#why-can-a-cdi-sync-with-a-small-number-of-rows-still-take-several-minutes}

CDI 동기화에는 행 처리가 시작되기 전에 고정된 시작 시간이 포함됩니다. 이 시작 시간은 동기화 크기에 관계없이 유사하기 때문에, 적은 수의 동기화도 여전히 몇 분이 걸릴 수 있으며 분당 행 수 기준으로 더 느리게 보일 수 있습니다. 전체 동기화 시간은 소스 쿼리 복잡성, 데이터 형태 및 데이터 웨어하우스의 가용 용량에 따라 달라집니다. 자세한 내용은 [데이터 웨어하우스 통합]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/)을 참조하세요.

## 동기화 중에 여러 레코드가 동일한 ID를 공유하는 경우 순서가 유지되나요? {#during-a-sync-is-the-order-preserved-if-multiple-records-share-the-same-id}

처리 순서는 100% 예측할 수 없습니다. 예를 들어, 동기화 중에 테이블에 동일한 `EXTERNAL_ID`를 가진 행이 여러 개 있는 경우 최종 프로필에 어떤 값이 포함될지 보장할 수 없습니다. 페이로드 열에서 다른 속성으로 동일한 `EXTERNAL_ID`를 업데이트하는 경우 동기화가 완료되면 모든 변경 사항이 반영됩니다.

## CDI 동기화에서 새로운 사용자가 생성되지 않는 이유는 무엇인가요? {#why-are-new-users-not-being-created-from-my-cdi-sync}

CDI 통합에 **기존 사용자만 업데이트** 옵션이 활성화되어 있으면, Braze에 이미 존재하는 사용자만 업데이트되고 새로운 사용자는 생성되지 않습니다. 이는 동기화 테이블의 행이 기존 Braze 사용자와 일치하지 않는 `EXTERNAL_ID`를 참조하는 경우 해당 행이 건너뛰어진다는 것을 의미합니다.

CDI를 통해 새로운 사용자를 생성하려면 통합 설정에서 **기존 사용자만 업데이트** 토글을 끄세요. **데이터 설정** > **클라우드 데이터 수집**으로 이동하여 통합을 선택하세요.

## CDI의 보안 대책은 무엇인가요? {#what-are-the-security-measures-for-cdi}

### Braze의 조치 {#our-measures}

Braze는 CDI에 대해 다음과 같은 조치를 취하고 있습니다:

- 모든 자격 증명은 데이터베이스 내에서 암호화되며, 특정 직원만 인증된 액세스 권한을 갖습니다.
- 암호화된 연결을 사용하여 고객 웨어하우스로 데이터를 전송합니다.
- 고객에게 사용을 권장하는 것과 동일한 API 키와 TLS 연결을 사용하여 Braze API 엔드포인트에 요청을 보냅니다.
- 정기적으로 라이브러리를 업데이트하고 보안 패치를 적용합니다.

### 사용자 측 조치 {#your-measures}

사용자와 팀에서 다음과 같은 보안 조치를 설정하는 것이 좋습니다:

- 자격 증명 액세스를 CDI 작동에 필요한 최소한으로 제한하세요. 특정 테이블 및 뷰에서 select(및 count)를 실행할 수 있어야 하기 때문입니다.
- 테이블에 액세스할 수 있는 IP를 공식적으로 게시된 [Braze IP]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)로 제한하세요.