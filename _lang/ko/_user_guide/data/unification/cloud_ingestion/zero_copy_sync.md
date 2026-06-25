---
nav_title: 제로 복사 개인화
article_title: CDI를 사용한 제로 복사 개인화
page_order: 7
page_type: reference
description: "이 페이지는 CDI를 사용하여 Braze Canvases를 트리거하는 방법에 대한 개요를 제공합니다."
---

# CDI를 사용한 제로 복사 개인화 {#zero-copy-personalization-using-cdi}

> CDI를 사용하여 제로 복사 개인화를 위한 Canvas 트리거를 동기화하는 방법을 알아보세요. 이 기능은 데이터 저장 솔루션에서 사용자별 정보에 액세스하여 대상 Canvas로 전달합니다. 캔버스 단계에는 Braze 고객 프로필에 유지되지 않는 개인화 필드를 선택적으로 포함할 수 있습니다.

## Canvas 트리거 동기화 {#syncing-canvas-triggers}

### 빠른 시작 단계 {#quick-start-steps}

이미 Braze CDI에 익숙하다면, Canvas 트리거 동기화 설정은 [사용자 데이터 CDI 통합]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/) 프로세스와 거의 동일하며, 다음과 같은 주의 사항이 있습니다:

- 외부 ID 또는 사용자 별칭 식별자만 지원됩니다. 이메일 및 전화번호는 지원되지 않는 식별자입니다.
- 기존 Braze 사용자만 동기화할 수 있습니다. 새 사용자는 생성할 수 없습니다.
- `properties`가 `payload` 열을 대체합니다. 이것은 개인화를 위한 Canvas 진입 등록정보로 사용하려는 필드의 JSON 문자열입니다.

시작하려면 새 동기화를 생성할 때 **Canvas Triggers** 데이터 유형을 선택하세요.

### Canvas 트리거 사용 {#using-canvas-triggers}

#### 1단계: Canvas 트리거를 위한 데이터 소스 설정 {#step-1-set-up-data-source-for-canvas-triggers}

{% tabs %}
{% tab Snowflake %}

##### 1.1단계: Snowflake에서 소스 테이블 설정 {#step-11-set-up-your-source-table-in-snowflake}

다음 예제의 이름을 사용하거나 고유한 데이터베이스, 스키마 및 테이블 이름을 선택할 수 있습니다. 테이블 대신 뷰 또는 구체화된 뷰를 사용할 수도 있습니다.

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id or alias_name and alias_label is required
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     PROPERTIES VARCHAR(16777216)
);
```

데이터베이스, 스키마 및 테이블 이름은 원하는 대로 지정할 수 있지만, 열 이름은 앞서 정의한 내용과 일치해야 합니다.

* `UPDATED_AT`: 이 행이 테이블에 업데이트되거나 추가된 시간입니다. Braze는 `UPDATED_AT`이 마지막 동기화 값보다 이후인 행을 동기화합니다. 동일한 타임스탬프를 공유하는 새 행이 있는 경우 정확한 경계 타임스탬프의 행이 다시 동기화될 수 있습니다.
* 사용자 식별자 열로 `external_id` 또는 `alias_name` 및 `alias_label` 중 하나가 필요합니다. 이들은 Canvas 메시징을 트리거할 사용자를 식별합니다.
  * `EXTERNAL_ID`: Canvas에 진입할 사용자를 식별합니다. 이 값은 Braze에서 사용하는 `external_id` 값과 일치해야 합니다.
  * `ALIAS_NAME` 및 `ALIAS_LABEL`: 이 열들은 사용자 별칭 오브젝트를 생성합니다. `alias_name`은 고유 식별자여야 하며, `alias_label`은 별칭 유형을 지정합니다. 사용자는 서로 다른 레이블을 가진 여러 별칭을 가질 수 있지만, `alias_label`당 하나의 alias_name만 가질 수 있습니다.
* `PROPERTIES`: Canvas에서 개인화 등록정보로 사용할 수 있는 필드의 JSON 문자열입니다. 사용자별 정보를 포함해야 합니다.

{% alert note %}
등록정보는 모든 행이나 사용자에 대해 필수는 아닙니다. 그러나 등록정보 값은 유효한 JSON 문자열이어야 합니다. 행에 등록정보가 없으면 빈 `{}` 문자열을 입력하세요.
{% endalert %}

##### 1.2단계: 자격 증명 설정 {#step-12-set-up-credentials}

역할, 웨어하우스 및 사용자를 설정하고 적절한 권한을 부여합니다. 기존 동기화에서 자격 증명이 이미 있는 경우 재사용할 수 있지만, Canvas 트리거 소스 테이블에 대한 액세스를 확장해야 합니다.

```sql

CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

CREATE USER BRAZE_INGESTION_USER;
GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;

```

##### 1.3단계: 네트워크 정책 구성 {#step-13-configure-network-policies}

계정에 네트워크 정책이 있는 경우, CDI 서비스 연결을 활성화하기 위해 Braze IP를 허용 목록에 추가하세요. IP 목록은 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=snowflake#step-15-allow-braze-ips-in-snowflake-network-policy-optional)을 참조하세요.

{% endtab %}
{% tab Redshift %}

##### 1.1단계: Redshift에서 소스 테이블 설정 {#step-11-set-up-your-source-table-in-redshift}

다음 예제의 이름을 사용하거나 고유한 데이터베이스, 스키마 및 테이블 이름을 선택할 수 있습니다. 테이블 대신 뷰 또는 구체화된 뷰를 사용할 수도 있습니다.

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC (
    updated_at timestamptz default sysdate not null,
    --at least one of external_id or alias_name and alias_label is required
    external_id varchar not null,.
    --if using user alias, both alias_name and alias_label are required
    alias_label varchar,
    alias_name varchar,
    properties varchar(max)
 );
```

데이터베이스, 스키마 및 테이블 이름은 원하는 대로 지정할 수 있지만, 열 이름은 앞서 정의한 내용과 일치해야 합니다.

* `UPDATED_AT`: 이 행이 테이블에 업데이트되거나 추가된 시간입니다. Braze는 `UPDATED_AT`이 마지막 동기화 값보다 이후인 행을 동기화합니다. 동일한 타임스탬프를 공유하는 새 행이 있는 경우 정확한 경계 타임스탬프의 행이 다시 동기화될 수 있습니다.
* 사용자 식별자 열로 `external_id` 또는 `alias_name` 및 `alias_label` 중 하나가 필요합니다. 이들은 Canvas 메시징을 트리거할 사용자를 식별합니다.
  * `EXTERNAL_ID`: Canvas에 진입할 사용자를 식별합니다. 이 값은 Braze에서 사용하는 `external_id` 값과 일치해야 합니다.
  * `ALIAS_NAME` 및 `ALIAS_LABEL`: 이 열들은 사용자 별칭 오브젝트를 생성합니다. `alias_name`은 고유 식별자여야 하며, `alias_label`은 별칭 유형을 지정합니다. 사용자는 서로 다른 레이블을 가진 여러 별칭을 가질 수 있지만, `alias_label`당 하나의 `alias_name`만 가질 수 있습니다.
* `PROPERTIES`: Canvas에서 개인화 등록정보로 사용할 수 있는 필드의 JSON 문자열입니다. 사용자별 정보를 포함해야 합니다.

{% alert note %}
등록정보는 모든 행이나 사용자에 대해 필수는 아닙니다. 그러나 등록정보 값은 유효한 JSON 문자열이어야 합니다. 행에 등록정보가 없으면 빈 `{}` 문자열을 입력하세요.
{% endalert %}

##### 1.2단계: 자격 증명 설정

역할, 웨어하우스 및 사용자를 설정하고 적절한 권한을 부여하세요. 기존 동기화에서 자격 증명이 이미 있는 경우 재사용할 수 있지만, Canvas 트리거 소스 테이블에 대한 액세스를 확장해야 합니다.

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE CANVAS_TRIGGERS_SYNC TO braze_user;
```

##### 1.3단계: 네트워크 정책 구성

계정에 네트워크 정책이 있는 경우, CDI 서비스 연결을 활성화하기 위해 Braze IP를 허용 목록에 추가하세요. IP 목록은 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=redshift#step-13-allow-access-to-braze-ips)을 참조하세요.

{% endtab %}
{% tab BigQuery %}

##### 1.1단계: 소스 테이블을 위한 새 프로젝트 또는 데이터세트 생성(선택 사항) {#step-11-create-a-new-project-or-dataset-for-your-source-table-optional}

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

##### 1.2단계: BigQuery에서 소스 테이블 설정 {#step-12-set-up-your-source-table-in-bigquery}
소스 테이블을 생성할 때 다음을 참조하세요:

| 필드 이름 | 유형 | 필수 여부 |
| :---- | :---- | :---- |
| **`UPDATED_AT`** | Timestamp | 예 |
| **`PROPERTIES`** | JSON | 예 |
| **`EXTERNAL_ID`** | STRING | NULLABLE |
| **`ALIAS_NAME`** | STRING | NULLABLE |
| **`ALIAS_LABEL`** | STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 aria-label="1.2단계: BigQuery에서 소스 테이블 설정" }

{% alert note %}
등록정보는 모든 행이나 사용자에 대해 필수는 아닙니다. 그러나 등록정보 값은 유효한 JSON 문자열이어야 합니다. 행에 등록정보가 없으면 빈 `{}` 문자열을 입력하세요.
{% endalert %}

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CANVAS_TRIGGERS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  --At least one of external_id or alias_name and alias_label is required
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  properties JSON
);
```

##### 1.3단계: 자격 증명 설정 {#step-13-set-up-credentials}

사용자를 생성하고 권한을 부여하세요. 다른 동기화에서 자격 증명이 이미 있는 경우, Canvas 트리거 테이블에 대한 액세스 권한이 있는 한 재사용할 수 있습니다.

| 권한 | 목적 |
| :---- | :---- |
| BigQuery Connection User | Braze가 연결할 수 있도록 허용합니다. |
| BigQuery User | Braze가 쿼리를 실행하고, 메타데이터를 읽고, 테이블을 나열할 수 있도록 허용합니다. |
| BigQuery Data Viewer | Braze가 데이터세트 및 콘텐츠를 볼 수 있도록 허용합니다. |
| BigQuery Job User | Braze가 작업을 실행할 수 있도록 허용합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="1.3단계: 자격 증명 설정" }

권한을 부여한 후 JSON 키를 생성하세요. 자세한 방법은 [키 생성 및 삭제](https://cloud.google.com/iam/docs/keys-create-delete)를 참조하세요. 나중에 Braze 대시보드에 업로드하게 됩니다.

##### 1.4단계: 네트워크 정책 구성 {#step-14-configure-network-policies}
계정에 네트워크 정책이 있는 경우, CDI 서비스 연결을 활성화하기 위해 Braze IP를 허용 목록에 추가하세요. IP 목록은 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=bigquery#step-13-allow-access-to-braze-ips)을 참조하세요.

{% endtab %}
{% tab Databricks %}

##### 1.1단계: 소스 테이블을 위한 카탈로그 또는 스키마 생성 {#step-11-create-a-catalog-or-schema-for-your-source-table}

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

#### 1.2단계: Databricks에서 소스 테이블 설정 {#step-12-set-up-your-source-table-in-databricks}

소스 테이블을 생성할 때 다음을 참조하세요:

| 필드 이름 | 유형 | 필수 |
| :---- | :---- | :---- |
| `UPDATED_AT` | Timestamp | 예 |
| `PROPERTIES` | JSON | 예 |
| `EXTERNAL_ID` | STRING |  NULLABLE |
| `ALIAS_NAME` | STRING | NULLABLE |
| `ALIAS_LABEL` | STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="1.2단계: Databricks에서 소스 테이블 설정" }

스키마와 테이블 이름은 원하는 대로 지정할 수 있지만, 열 이름은 앞서 정의한 내용과 일치해야 합니다.

* `UPDATED_AT`: 이 행이 테이블에 업데이트되거나 추가된 시간입니다. Braze는 `UPDATED_AT`이 마지막 동기화 값보다 이후인 행을 동기화합니다. 동일한 타임스탬프를 공유하는 새 행이 있는 경우 정확한 경계 타임스탬프의 행이 다시 동기화될 수 있습니다.
* 사용자 식별자 열로 `external_id` 또는 `alias_name` 및 `alias_label` 중 하나가 필요합니다. 이들은 Canvas 메시징을 트리거할 사용자를 식별합니다.
  * `EXTERNAL_ID`: Canvas에 진입할 사용자를 식별합니다. 이 값은 Braze에서 사용하는 `external_id` 값과 일치해야 합니다.
  * `ALIAS_NAME` 및 `ALIAS_LABEL`: 이 열들은 사용자 별칭 오브젝트를 생성합니다. `alias_name`은 고유 식별자여야 하며, `alias_label`은 별칭 유형을 지정합니다. 사용자는 서로 다른 레이블을 가진 여러 별칭을 가질 수 있지만, `alias_label`당 하나의 alias_name만 가질 수 있습니다.
* `PROPERTIES`: Canvas에서 개인화 등록정보로 사용할 수 있는 필드의 문자열 또는 구조체입니다. 사용자별 정보를 포함해야 합니다.

{% alert note %}
등록정보는 모든 행이나 사용자에 대해 필수는 아닙니다. 그러나 등록정보 값은 유효한 JSON 문자열이어야 합니다. 행에 등록정보가 없으면 빈 `{}` 문자열을 입력하세요.
{% endalert %}

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  --At least one of external_id or alias_name and alias_label is required
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  properties STRING, STRUCT, or MAP
);
```

##### 1.3단계: 자격 증명 설정

Databricks에서 개인 액세스 토큰을 생성합니다:

1. 사용자 이름을 선택한 다음 **User Settings**를 선택합니다.
2. **Access tokens** 탭에서 **Generate new token**을 선택합니다.
3. 토큰을 식별하기 위해 "Braze CDI"와 같은 주석을 추가합니다.
4. 만료가 없도록 **Lifetime (days)**을 비워두고, **Generate**를 선택합니다.
5. Braze 대시보드에서 사용할 수 있도록 토큰을 안전하게 복사하고 저장합니다.

##### 1.4단계: 네트워크 정책 구성

계정에 네트워크 정책이 있는 경우, CDI 서비스 연결을 활성화하기 위해 Braze IP를 허용 목록에 추가하세요. IP 목록은 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=databricks#step-13-allow-access-to-braze-ips)을 참조하세요.

{% endtab %}
{% tab Fabric %}

##### 1.1단계: Fabric에서 소스 테이블 설정 {#step-11-set-up-your-source-table-in-fabric}

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name]
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PROPERTIES VARCHAR NOT NULL,
  --at least one of external_id or alias_name and alias_label is required
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR
)
GO
```

##### 1.2단계: 자격 증명 설정

서비스 주체를 생성하고 권한을 부여합니다. 다른 동기화에서 자격 증명이 이미 있는 경우 재사용할 수 있습니다. 단, 계정 테이블에 대한 액세스 권한이 있는지 확인하세요.

##### 1.3단계: 네트워크 정책 구성

계정에 네트워크 정책이 있는 경우, CDI 서비스 연결을 활성화하기 위해 Braze IP를 허용 목록에 추가하세요. IP 목록은 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/?tab=microsoft%20fabric#step-15-allow-braze-ips-in-firewall-optional)을 참조하세요.

{% endtab %}
{% tab 파일 저장소 %}

파일 저장소에서 Canvas 트리거를 동기화하려면 다음 필드가 포함된 소스 파일을 생성하세요.

| 필드 | 필수 | 설명 |
| :---- | :---- | :---- |
| `EXTERNAL_ID` | 예, `external_id` 또는 `alias_name`과 `alias_label` 중 하나 | 업데이트하려는 사용자를 식별합니다. 이 값은 Braze에서 사용하는 `external_id` 값과 일치해야 합니다. |
| `ALIAS_NAME` 및 `ALIAS_LABEL` | 예, `external_id` 또는 `alias_name`과 `alias_label` 중 하나 | 이 두 열은 사용자 별칭 오브젝트를 생성합니다. `alias_name`은 고유 식별자여야 하며, `alias_label`은 별칭 유형을 지정합니다. 사용자는 서로 다른 레이블을 가진 여러 별칭을 가질 수 있지만, `alias_label`당 하나의 `alias_name`만 가질 수 있습니다. |
| `PROPERTIES` | 예 | Canvas에서 개인화 등록정보로 사용할 수 있는 필드의 JSON 문자열입니다. 사용자별 정보를 포함해야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="1.3단계: 네트워크 정책 구성" }

{% alert tip %}
파일 이름은 AWS 규칙을 따라야 하며 고유해야 합니다. 고유성을 보장하기 위해 타임스탬프를 추가하세요. Amazon S3 동기화에 대한 자세한 내용은 [파일 저장소 통합]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/)을 참조하세요.
{% endalert %}

{% endtab %}
{% endtabs %}

#### 2단계: 대상 Canvas 구성 {#step-2-configure-your-destination-canvas}

1. Canvas 트리거를 위한 대상 Canvas를 설정하세요. 새로운 API 트리거 Canvas를 생성하거나 기존 Canvas를 선택하세요. API 트리거 전달 스케줄 유형으로 Canvas를 만드는 방법에 대한 지침은 [진입 스케줄 유형]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/#entry-schedule-types)을 참조하세요.
2. API 트리거 전달 스케줄 유형을 선택한 후, Canvas 설정을 계속하고 Canvas를 구축하세요. Canvases는 단순한 단일 메시지 전송부터 여러 단계가 포함된 복잡한 고객 워크플로우까지 다양할 수 있습니다.
3. 캔버스 단계 내에서 [Canvas 진입 등록정보]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/context_and_event_properties/)를 사용하여 소스 테이블에서 동기화할 등록정보 필드로 메시지를 개인화하세요.
  * 예를 들어, 1단계에서 `account_balance`에 대한 등록정보 필드를 설정했다면, 메시지를 개인화하기 위해 다음의 Liquid 템플릿을 사용할 수 있습니다: `\{\{canvas_entry_properties.\$\{account_balance\}\}\}`.
5. Canvas를 구축한 후 시작하고 [3단계](#step-3-create-your-zero-copy-sync)로 진행하세요.

#### 3단계: 제로 복사 동기화 생성 {#step-3-create-your-zero-copy-sync}

소스 설정이 완료되고 대상 Canvas가 시작되면, 새로운 데이터 동기화를 생성하세요:

1. Braze에서 **데이터 설정** > **클라우드 데이터 수집**으로 이동하세요.
1. 연결 세부정보(또는 기존 자격 증명 재사용)를 입력하고 [1단계](#step-1-set-up-data-source-for-canvas-triggers)의 소스 테이블을 설정하세요.
2. 통합 이름을 지정하세요.
3. **Canvas Triggers** 데이터 유형을 선택하세요.
4. 대상 Canvas를 선택하세요([2단계](#step-2-configure-your-destination-canvas)에서 설정한 Canvas).
5. 동기화 빈도를 선택하세요.
6. 알림 환경설정을 구성하세요.
7. **Test Connection**을 선택하여 모든 것이 예상대로 작동하는지 확인하세요. Snowflake에 연결하는 경우, 먼저 대시보드에 표시된 공개 키를 Braze가 Snowflake에 연결하기 위해 생성한 사용자에게 추가하세요. 이 단계를 완료하려면 Snowflake에서 **SECURITYADMIN** 이상의 액세스 권한이 필요합니다.
8. 동기화를 저장하여 Canvas 트리거 동기화를 시작하세요.

동기화가 실행되면 소스 테이블의 사용자가 Canvas에 진입하기 시작합니다. Canvas 분석 및 클라우드 데이터 수집 동기화 로그 페이지를 사용하여 성과를 모니터링하세요.

{% alert tip %}
예기치 않은 전송을 방지하기 위해 전체 구성(동기화 동작부터 Canvas 설정까지)을 검토하세요. 사용량 제한, 최대 게재빈도 설정 및 세분화 필터와 같은 Canvas 설정으로 메시지 전달을 더욱 세밀하게 조정할 수 있습니다.<br><br>프로덕션 사용 사례를 구현하기 전에 소규모 또는 테스트 오디언스를 대상으로 시험 실행을 수행하는 것을 권장합니다.
{% endalert %}

### 고려 사항 {#considerations}

CDI Canvas 트리거는 `/canvas/trigger/send`에 대한 REST API 사용량 제한을 활용합니다. 이 엔드포인트를 CDI Canvas 트리거와 REST API 통합에서 동시에 사용하는 경우, 결합된 사용량이 사용량 제한에 포함될 것으로 예상하세요.

각 동기화 실행은 최대 약 375만 사용자/시간의 속도로 해당 대상 Canvas에 사용자를 진입시킵니다. 다음과 같은 경우 소스에서 Canvas 진입까지의 시간이 길어질 수 있습니다:

* 동기화 실행당 375만 명 이상의 사용자를 동기화하는 경우.
* REST API의 [`/canvas/trigger/send`에 대한 사용량 제한]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#rate-limit)을 이미 포화 상태로 사용하면서 CDI Canvas 트리거를 사용하는 경우.

메시지 아카이브가 활성화된 상태에서 제로 복사 CDI를 사용할 때 다음 사항을 고려하세요:

* 테이블의 결과는 처리 중에 Braze에 임시로 저장됩니다. 또한 정확히 무엇이 동기화되었는지 확인할 수 있도록 30일 동안 Snowflake로 내보내집니다.
* 아카이브된 메시지는 Braze 내 어디에도 저장되지 않습니다. 사본은 구성된 저장소에만 독점적으로 저장되도록 전송됩니다.
* Canvas 트리거와 함께 제로 복사 CDI를 사용하는 경우, Braze는 데이터 웨어하우스의 쿼리 결과 백업을 저장하지 않으며 고객 프로필에 데이터가 복사되지 않습니다.
* Canvas 컨텍스트 등록정보는 내부 시스템에 최대 30일 동안 기록될 수 있습니다.