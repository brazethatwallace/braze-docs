---
nav_title: 데이터 웨어하우스 통합
article_title: 데이터 웨어하우스 통합
alias: /partners/databricks/
description: "이 페이지에서는 Braze 클라우드 데이터 수집을 사용하여 관련 데이터를 Snowflake, Redshift, BigQuery 및 Databricks 통합과 동기화하는 방법을 설명합니다."
page_order: 3
page_type: reference

---

# 데이터 웨어하우스 스토리지 통합 {#data-warehouse-storage-integrations}

> 이 페이지에서는 Braze 클라우드 데이터 수집(CDI)을 사용하여 Snowflake, Redshift, BigQuery 및 Databricks 통합과 관련 데이터를 동기화하는 방법을 설명합니다.

## 데이터 웨어하우스 통합 설정 {#setting-up-data-warehouse-integrations}

클라우드 데이터 수집 통합은 Braze 측과 데이터 웨어하우스 인스턴스 양쪽에서 일부 설정이 필요합니다. 다음 단계에 따라 통합을 설정하세요:

{% tabs %}
{% tab Snowflake %}
1. Snowflake 인스턴스에서 Braze에 동기화할 테이블 또는 뷰를 설정합니다.
2. Braze 대시보드에서 새 Snowflake 소스를 생성합니다.
3. Braze 대시보드에서 제공된 공개 키를 가져와 [인증을 위해 Snowflake 사용자에 추가합니다](https://docs.snowflake.com/en/user-guide/key-pair-auth.html).
4. Braze 대시보드에서 동기화를 생성하고, 통합을 테스트한 후 동기화를 시작합니다.

{% alert tip %}
[Snowflake 빠른 시작 가이드](https://quickstarts.snowflake.com/guide/braze_cdi/index.html)에서는 Snowflake Streams와 CDI를 사용하여 Braze에 데이터를 동기화하는 자동화된 파이프라인을 만드는 데 필요한 샘플 코드와 단계를 안내합니다.
{% endalert %}
{% endtab %}
{% tab Redshift %}
1. 동기화하려는 Redshift 테이블에 Braze 액세스가 허용되어 있는지 확인합니다. Braze는 인터넷을 통해 Redshift에 연결합니다.
2. Redshift 인스턴스에서 Braze에 동기화할 테이블 또는 뷰를 설정합니다.
3. Braze 대시보드에서 새 소스와 동기화를 생성합니다.
4. 통합을 테스트하고 동기화를 시작합니다.

{% alert note %}
동기화당 처리되는 행 수는 웨어하우스 성능, 네트워크 지연 시간, 동기화 쿼리와 일치하는 새 데이터의 양에 따라 달라집니다. 대시보드의 통합 **동기화 기록**을 사용하여 최근 실행의 소요 시간과 행 수를 확인하세요.
{% endalert %}
{% endtab %}
{% tab BigQuery %}
1. 서비스 계정을 생성하고 동기화하려는 데이터가 포함된 BigQuery 프로젝트 및 데이터셋에 대한 액세스를 허용합니다.
2. BigQuery 계정에서 Braze에 동기화할 테이블 또는 뷰를 설정합니다.
3. Braze 대시보드에서 새 소스와 동기화를 생성합니다.
4. 통합을 테스트하고 동기화를 시작합니다.
{% endtab %}
{% tab Databricks %}
1. 서비스 계정을 생성하고 동기화하려는 데이터가 포함된 Databricks 프로젝트 및 데이터셋에 대한 액세스를 허용합니다.
2. Databricks 계정에서 Braze에 동기화할 테이블 또는 뷰를 설정합니다.
3. Braze 대시보드에서 새 소스와 동기화를 생성합니다.
4. 통합을 테스트하고 동기화를 시작합니다.

{% alert important %}
Braze가 Classic 및 Pro SQL 인스턴스에 연결할 때 2~5분의 워밍업 시간이 소요될 수 있으며, 이로 인해 연결 설정 및 테스트 중, 그리고 예약된 동기화 시작 시 지연이 발생할 수 있습니다. 서버리스 SQL 인스턴스를 사용하면 워밍업 시간이 최소화되고 쿼리 처리량이 향상되지만, 통합 비용이 약간 높아질 수 있습니다.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}
1. 서비스 주체를 생성하고 Fabric API에 대한 액세스를 부여합니다.
2. 공유 작업 영역을 설정하고 서비스 주체에 액세스를 부여합니다.
3. 공유 Fabric 작업 영역에서 Braze에 동기화할 테이블 또는 뷰를 설정합니다.
4. Braze 대시보드에서 새 소스와 동기화를 생성합니다.
5. 통합을 테스트하고 동기화를 시작합니다.
{% endtab %}
{% endtabs %}

### 1단계: 테이블 또는 뷰 설정 {#step-1-set-up-tables-or-views}

시작하기 전에 [클라우드 데이터 수집을 위한 테이블 설정]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup)을 검토하여 소스 테이블 요구 사항과 `PAYLOAD` 형식 요구 사항을 비교해 보세요.

{% alert note %}
소스 테이블 또는 뷰에는 다음 섹션의 탭에서 해당 웨어하우스에 대해 나열되지 않은 열(예: 감사 또는 해싱용)이 포함될 수 있습니다. Braze는 해당 탭에 설명된 열만 읽으며, 다른 열은 클라우드 데이터 수집 동기화 중에 사용되지 않습니다.
{% endalert %}

{% tabs %}
{% tab Snowflake %}

#### 1.1단계: 테이블 설정 {#step-11-set-up-the-table}

```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     --braze_id can only be used to update existing users created through the Braze SDK
     BRAZE_ID VARCHAR(16777216),
     --If you include both email and phone, email is used as the primary identifier
     EMAIL VARCHAR(16777216),
     PHONE VARCHAR(16777216),
     PAYLOAD VARCHAR(16777216) NOT NULL
);
```

데이터베이스, 스키마, 테이블 이름은 원하는 대로 지정할 수 있지만, 열 이름은 위의 정의와 일치해야 합니다.

- `UPDATED_AT` - 이 행이 테이블에 업데이트되거나 추가된 시간입니다. Braze는 `UPDATED_AT`가 마지막으로 동기화된 값보다 이후인 행을 동기화합니다. 새 행이 동일한 타임스탬프를 공유하는 경우 정확한 경계 타임스탬프의 행이 다시 동기화될 수 있습니다.
- **사용자 식별자 열** - 테이블에는 하나 이상의 사용자 식별자 열이 포함될 수 있습니다. 각 행에는 하나의 식별자만 포함해야 합니다(`external_id`, `alias_name`과 `alias_label`의 조합, `braze_id`, `email` 또는 `phone` 중 하나). 소스 테이블에는 1개, 2개, 3개, 4개 또는 5개 식별자 유형 모두에 대한 열이 있을 수 있습니다.
    - `EXTERNAL_ID` - 업데이트하려는 사용자를 식별합니다. Braze에서 사용되는 `external_id` 값과 일치해야 합니다.
    - `ALIAS_NAME` 및 `ALIAS_LABEL` - 이 두 열은 사용자 별칭 객체를 생성합니다. `alias_name`은 고유 식별자여야 하며, `alias_label`은 별칭 유형을 지정합니다. 사용자는 서로 다른 레이블을 가진 여러 별칭을 가질 수 있지만, `alias_label`당 하나의 `alias_name`만 가질 수 있습니다.
    - `BRAZE_ID` - Braze 사용자 식별자입니다. Braze SDK에 의해 생성되며, 클라우드 데이터 수집을 통해 Braze ID로 새 사용자를 생성할 수 없습니다. 새 사용자를 생성하려면 외부 사용자 ID 또는 사용자 별칭을 지정하세요.
    - `EMAIL` - 사용자의 이메일 주소입니다. 동일한 이메일 주소를 가진 프로필이 여러 개 있는 경우, 가장 최근에 업데이트된 프로필이 업데이트 우선순위를 갖습니다. 이메일과 전화번호를 모두 포함하면 이메일이 기본 식별자로 사용됩니다.
    - `PHONE` - 사용자의 전화번호입니다. 동일한 전화번호를 가진 프로필이 여러 개 있는 경우, 가장 최근에 업데이트된 프로필이 업데이트 우선순위를 갖습니다.
- `PAYLOAD` - Braze에서 사용자에게 동기화하려는 필드의 JSON 문자열입니다.

#### 1.2단계: 역할 및 데이터베이스 권한 설정 {#step-12-set-up-the-role-and-database-permissions}

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;
```

필요에 따라 이름을 업데이트하되, 권한은 위의 예시와 일치해야 합니다.

#### 1.3단계: 웨어하우스 설정 및 Braze 역할에 액세스 부여 {#step-13-set-up-the-warehouse-and-give-access-to-braze-role}

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
웨어하우스에 **자동 재개** 플래그가 켜져 있어야 합니다. 그렇지 않은 경우, 쿼리 실행 시 Braze가 웨어하우스를 켤 수 있도록 추가 `OPERATE` 권한을 부여하세요.
{% endalert %}

#### 1.4단계: 사용자 설정 {#step-14-set-up-the-user}

```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

이 단계를 완료한 후 Braze와 연결 정보를 공유하면 사용자에 추가할 공개 키를 받게 됩니다.

{% alert note %}
서로 다른 워크스페이스를 동일한 Snowflake 계정에 연결할 때는 통합을 생성하는 각 Braze 워크스페이스에 대해 고유한 사용자를 만들어야 합니다. 워크스페이스 내에서는 통합 간에 동일한 사용자를 재사용할 수 있지만, 동일한 Snowflake 계정의 사용자가 워크스페이스 간에 중복되면 통합 생성이 실패합니다.
{% endalert %}

#### 1.5단계: Snowflake 네트워크 정책에서 Braze IP 허용(선택 사항) {#step-15-allow-braze-ips-in-snowflake-network-policy-optional}

Snowflake 계정의 구성에 따라 Snowflake 네트워크 정책에서 다음 IP 주소를 허용해야 할 수 있습니다. 이를 활성화하는 방법에 대한 자세한 내용은 [네트워크 정책 수정](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies)에 관한 Snowflake 설명서를 참조하세요.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Redshift %}

#### 1.1단계: 테이블 설정

선택적으로 소스 테이블을 보관할 새 데이터베이스와 스키마를 설정합니다.
```sql
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
CDI 통합에 사용할 테이블(또는 뷰)을 생성합니다.
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar,
   --If you include both email and phone, email is used as the primary identifier
   email varchar,
   phone varchar,
   payload varchar(max)
)
```

데이터베이스, 스키마, 테이블 이름은 원하는 대로 지정할 수 있지만, 열 이름은 위의 정의와 일치해야 합니다.

- `UPDATED_AT` - 이 행이 테이블에 업데이트되거나 추가된 시간입니다. Braze는 `UPDATED_AT`가 마지막으로 동기화된 값보다 이후인 행을 동기화합니다. 새 행이 동일한 타임스탬프를 공유하는 경우 정확한 경계 타임스탬프의 행이 다시 동기화될 수 있습니다.
- **사용자 식별자 열** - 테이블에는 하나 이상의 사용자 식별자 열이 포함될 수 있습니다. 각 행에는 하나의 식별자만 포함해야 합니다(`external_id`, `alias_name`과 `alias_label`의 조합, `braze_id`, `email` 또는 `phone` 중 하나). 소스 테이블에는 1개, 2개, 3개, 4개 또는 5개 식별자 유형 모두에 대한 열이 있을 수 있습니다.
    - `EXTERNAL_ID` - 업데이트하려는 사용자를 식별합니다. Braze에서 사용되는 `external_id` 값과 일치해야 합니다.
    - `ALIAS_NAME` 및 `ALIAS_LABEL` - 이 두 열은 사용자 별칭 객체를 생성합니다. `alias_name`은 고유 식별자여야 하며, `alias_label`은 별칭 유형을 지정합니다. 사용자는 서로 다른 레이블을 가진 여러 별칭을 가질 수 있지만, `alias_label`당 하나의 `alias_name`만 가질 수 있습니다.
    - `BRAZE_ID` - Braze 사용자 식별자입니다. Braze SDK에 의해 생성되며, 클라우드 데이터 수집을 통해 Braze ID로 새 사용자를 생성할 수 없습니다. 새 사용자를 생성하려면 외부 사용자 ID 또는 사용자 별칭을 지정하세요.
    - `EMAIL` - 사용자의 이메일 주소입니다. 동일한 이메일 주소를 가진 프로필이 여러 개 있는 경우, 가장 최근에 업데이트된 프로필이 업데이트 우선순위를 갖습니다. 이메일과 전화번호를 모두 포함하면 이메일이 기본 식별자로 사용됩니다.
    - `PHONE` - 사용자의 전화번호입니다. 동일한 전화번호를 가진 프로필이 여러 개 있는 경우, 가장 최근에 업데이트된 프로필이 업데이트 우선순위를 갖습니다.
- `PAYLOAD` - Braze에서 사용자에게 동기화하려는 필드의 JSON 문자열입니다.

#### 1.2단계: 사용자 생성 및 권한 부여 {#step-12-create-user-and-grant-permissions}

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

이것은 이 사용자에게 필요한 최소 권한입니다. 여러 CDI 통합을 생성하는 경우 스키마에 대한 권한을 부여하거나 그룹을 사용하여 권한을 관리할 수 있습니다.

#### 1.3단계: Braze IP에 대한 액세스 허용 {#step-13-allow-access-to-braze-ips}

방화벽이나 기타 네트워크 정책이 있는 경우 Redshift 인스턴스에 대한 Braze 네트워크 액세스를 허용해야 합니다. Redshift URL 엔드포인트의 예시는 "example-cluster.ap-northeast-2.redshift.amazonaws.com"입니다.

알아두어야 할 중요한 사항:
- Braze가 Redshift의 데이터에 액세스할 수 있도록 보안 그룹을 변경해야 할 수도 있습니다.
- 테이블의 IP와 Redshift 클러스터를 쿼리하는 데 사용되는 포트(기본값은 5439)에서 인바운드 트래픽을 명시적으로 허용해야 합니다. 인바운드 규칙이 "모두 허용"으로 설정되어 있더라도 이 포트에서 Redshift TCP 연결을 명시적으로 허용해야 합니다.
- Braze가 클러스터에 연결하려면 Redshift 클러스터의 엔드포인트가 공개적으로 액세스 가능해야 합니다.
     - Redshift 클러스터를 공개적으로 액세스 가능하게 하고 싶지 않은 경우, VPC와 EC2 인스턴스를 설정하여 SSH 터널을 사용해 Redshift 데이터에 액세스할 수 있습니다. 자세한 내용은 [AWS 지식 센터 게시물](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)을 참조하세요.

Braze 대시보드 리전에 해당하는 다음 IP에서의 액세스를 허용하세요.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab BigQuery %}

#### 1.1단계: 테이블 설정

선택적으로 소스 테이블을 보관할 새 프로젝트 또는 데이터셋을 설정합니다.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

다음 필드를 사용하여 CDI 통합에 사용할 테이블을 하나 이상 생성합니다:

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  --At least one of external_id, alias_name and alias_label, or braze_id is required
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload JSON
);
```

| 필드 이름 | 유형 | 모드 |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `PAYLOAD`| JSON | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="1.1단계: 테이블 설정" }

프로젝트, 데이터셋, 테이블 이름은 원하는 대로 지정할 수 있지만, 열 이름은 위의 정의와 일치해야 합니다.

- `UPDATED_AT` - 이 행이 테이블에 업데이트되거나 추가된 시간입니다. Braze는 `UPDATED_AT`가 마지막으로 동기화된 값보다 이후인 행을 동기화합니다. 새 행이 동일한 타임스탬프를 공유하는 경우 정확한 경계 타임스탬프의 행이 다시 동기화될 수 있습니다.
- **사용자 식별자 열** - 테이블에는 하나 이상의 사용자 식별자 열이 포함될 수 있습니다. 각 행에는 하나의 식별자만 포함해야 합니다(`external_id`, `alias_name`과 `alias_label`의 조합, `braze_id`, `email` 또는 `phone` 중 하나). 소스 테이블에는 1개, 2개, 3개, 4개 또는 5개 식별자 유형 모두에 대한 열이 있을 수 있습니다.
    - `EXTERNAL_ID` - 업데이트하려는 사용자를 식별합니다. Braze에서 사용되는 `external_id` 값과 일치해야 합니다.
    - `ALIAS_NAME` 및 `ALIAS_LABEL` - 이 두 열은 사용자 별칭 객체를 생성합니다. `alias_name`은 고유 식별자여야 하며, `alias_label`은 별칭 유형을 지정합니다. 사용자는 서로 다른 레이블을 가진 여러 별칭을 가질 수 있지만, `alias_label`당 하나의 `alias_name`만 가질 수 있습니다.
    - `BRAZE_ID` - Braze 사용자 식별자입니다. Braze SDK에 의해 생성되며, 클라우드 데이터 수집을 통해 Braze ID로 새 사용자를 생성할 수 없습니다. 새 사용자를 생성하려면 외부 사용자 ID 또는 사용자 별칭을 지정하세요.
    - `EMAIL` - 사용자의 이메일 주소입니다. 동일한 이메일 주소를 가진 프로필이 여러 개 있는 경우, 가장 최근에 업데이트된 프로필이 업데이트 우선순위를 갖습니다. 이메일과 전화번호를 모두 포함하면 이메일이 기본 식별자로 사용됩니다.
    - `PHONE` - 사용자의 전화번호입니다. 동일한 전화번호를 가진 프로필이 여러 개 있는 경우, 가장 최근에 업데이트된 프로필이 업데이트 우선순위를 갖습니다.
- `PAYLOAD` - Braze에서 사용자에게 동기화하려는 필드의 JSON 문자열입니다.

{% alert important %}
**BigQuery 파티셔닝**

CDI는 BigQuery의 파티션을 지원합니다. `UPDATED_AT`의 함수로 파티셔닝하면(예: 데이터셋 크기에 따라 일, 주 또는 시간 단위로) BigQuery가 스캔해야 하는 데이터를 줄일 수 있습니다. 이를 통해 매우 큰 테이블의 성능과 효율성이 향상됩니다.

다른 필드로 파티셔닝하지 마세요. 다양한 구성을 테스트하여 특정 데이터에 가장 적합한 설정을 찾으세요.

모든 CDI 쿼리는 `UPDATED_AT`로 필터링하지만, 이 동작은 변경될 수 있습니다. 쿼리에 이 절이 포함되어야 한다는 것을 _전제하지 않도록_ 테이블 스키마를 설계하세요.

자세한 내용은 [BigQuery 파티셔닝 설명서](https://docs.cloud.google.com/bigquery/docs/partitioned-tables)를 참조하세요.
{% endalert %}

#### 1.2단계: 서비스 계정 생성 및 권한 부여 {#step-12-create-a-service-account-and-grant-permissions}

Braze가 테이블에서 연결하고 데이터를 읽는 데 사용할 GCP 서비스 계정을 생성합니다. 서비스 계정에는 다음 권한이 있어야 합니다:

- **BigQuery Connection User:** Braze가 연결할 수 있도록 허용합니다.
- **BigQuery User:** Braze가 쿼리를 실행하고, 데이터셋 메타데이터를 읽고, 테이블을 나열할 수 있는 액세스를 제공합니다.
- **BigQuery Data Viewer:** Braze가 데이터셋과 그 내용을 볼 수 있는 액세스를 제공합니다.
- **BigQuery Job User:** Braze가 작업을 실행할 수 있는 액세스를 제공합니다.

서비스 계정을 생성하고 권한을 부여한 후 JSON 키를 생성합니다. 자세한 내용은 [서비스 계정 키 생성 및 삭제](https://cloud.google.com/iam/docs/keys-create-delete)를 참조하세요. 이 키는 이후 단계에서 Braze 대시보드에 업로드합니다.

#### 1.3단계: Braze IP에 대한 액세스 허용

네트워크 정책이 있는 경우 BigQuery 인스턴스에 대한 Braze 네트워크 액세스를 허용해야 합니다. Braze 대시보드 리전에 해당하는 다음 IP에서의 액세스를 허용하세요.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Databricks %}

#### 1.1단계: 테이블 설정

선택적으로 소스 테이블을 보관할 새 카탈로그 또는 스키마를 설정합니다.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

다음 필드를 사용하여 CDI 통합에 사용할 테이블을 하나 이상 생성합니다:


```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  --At least one of external_id, alias_name and alias_label, or braze_id is required
  external_id STRING,
  --If using user alias, both alias_name and alias_label are required
  alias_name STRING,
  alias_label STRING,
  --braze_id can only be used to update existing users created through the Braze SDK
  braze_id STRING,
  --If you include both email and phone, email is used as the primary identifier
  email STRING,
  phone STRING,
  payload STRING, STRUCT, or MAP
);
```


| 필드 이름 | 유형 | 모드 |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `PAYLOAD`| STRING, STRUCT, or MAP | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
| `EMAIL`| STRING | NULLABLE |
| `PHONE`| STRING | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="1.1단계: 테이블 설정" }

스키마와 테이블 이름은 원하는 대로 지정할 수 있지만, 열 이름은 위의 정의와 일치해야 합니다.

- `UPDATED_AT` - 이 행이 테이블에 업데이트되거나 추가된 시간입니다. Braze는 `UPDATED_AT`가 마지막으로 동기화된 값보다 이후인 행을 동기화합니다. 새 행이 동일한 타임스탬프를 공유하는 경우 정확한 경계 타임스탬프의 행이 다시 동기화될 수 있습니다.
- **사용자 식별자 열** - 테이블에는 하나 이상의 사용자 식별자 열이 포함될 수 있습니다. 각 행에는 하나의 식별자만 포함해야 합니다(`external_id`, `alias_name`과 `alias_label`의 조합, `braze_id`, `email` 또는 `phone` 중 하나). 소스 테이블에는 1개, 2개, 3개, 4개 또는 5개 식별자 유형 모두에 대한 열이 있을 수 있습니다.
    - `EXTERNAL_ID` - 업데이트하려는 사용자를 식별합니다. Braze에서 사용되는 `external_id` 값과 일치해야 합니다.
    - `ALIAS_NAME` 및 `ALIAS_LABEL` - 이 두 열은 사용자 별칭 객체를 생성합니다. `alias_name`은 고유 식별자여야 하며, `alias_label`은 별칭 유형을 지정합니다. 사용자는 서로 다른 레이블을 가진 여러 별칭을 가질 수 있지만, `alias_label`당 하나의 `alias_name`만 가질 수 있습니다.
    - `BRAZE_ID` - Braze 사용자 식별자입니다. Braze SDK에 의해 생성되며, 클라우드 데이터 수집을 통해 Braze ID로 새 사용자를 생성할 수 없습니다. 새 사용자를 생성하려면 외부 사용자 ID 또는 사용자 별칭을 지정하세요.
    - `EMAIL` - 사용자의 이메일 주소입니다. 동일한 이메일 주소를 가진 프로필이 여러 개 있는 경우, 가장 최근에 업데이트된 프로필이 업데이트 우선순위를 갖습니다. 이메일과 전화번호를 모두 포함하면 이메일이 기본 식별자로 사용됩니다.
    - `PHONE` - 사용자의 전화번호입니다. 동일한 전화번호를 가진 프로필이 여러 개 있는 경우, 가장 최근에 업데이트된 프로필이 업데이트 우선순위를 갖습니다.
- `PAYLOAD` - Braze에서 사용자에게 동기화하려는 필드의 문자열 또는 구조체입니다.

#### 1.2단계: 액세스 토큰 생성 {#step-12-create-an-access-token}

Braze가 Databricks에 액세스하려면 개인 액세스 토큰을 생성해야 합니다.

1. Databricks 워크스페이스에서 상단 바의 Databricks 사용자 이름을 선택한 다음 드롭다운에서 **User Settings**를 선택합니다.
2. 액세스 토큰 탭에서 **Generate new token**을 선택합니다.
3. 이 토큰을 식별하는 데 도움이 되는 코멘트(예: "Braze CDI")를 입력하고, Lifetime (days) 상자를 비워두어(공란) 토큰의 수명을 무제한으로 변경합니다.
4. **Generate**를 선택합니다.
5. 표시된 토큰을 복사한 다음 **Done**을 선택합니다.

자격 증명 생성 단계에서 Braze 대시보드에 입력해야 할 때까지 토큰을 안전한 장소에 보관하세요.

#### 1.3단계: Braze IP에 대한 액세스 허용

네트워크 정책이 있는 경우 Databricks 인스턴스에 대한 Braze 네트워크 액세스를 허용해야 합니다. Braze 대시보드 리전에 해당하는 다음 IP에서의 액세스를 허용하세요.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}
{% tab Microsoft Fabric %}

#### 1.1단계: 서비스 주체 설정 및 액세스 부여 {#step-11-set-up-the-service-principal-and-grant-access}
Braze는 Entra ID 인증을 사용하는 서비스 주체를 통해 Fabric 웨어하우스에 연결합니다. Braze가 사용할 새 서비스 주체를 생성하고 필요에 따라 Fabric 리소스에 대한 액세스를 부여합니다. Braze가 연결하려면 다음 세부 정보가 필요합니다:

{% multi_lang_include data_unification/azure_service_principal_credentials.md %}

{% multi_lang_include data_unification/azure_app_registration_steps.md %}

{% alert note %}
Azure는 서비스 주체 시크릿에 무제한 만료를 허용하지 않습니다. Braze로의 데이터 흐름을 유지하려면 자격 증명이 만료되기 전에 갱신하세요.
{% endalert %}

#### 1.2단계: Fabric 리소스에 대한 액세스 부여 {#step-12-grant-access-to-fabric-resources}
Braze가 Fabric 인스턴스에 연결할 수 있도록 액세스를 제공합니다. Fabric 관리 포털에서 **Settings** > **Governance and insights** > **Admin portal** > **Tenant settings**로 이동합니다.

* **Developer settings**에서 **Service principals can use Fabric APIs**를 활성화하여 Braze가 Microsoft Entra ID를 사용하여 연결할 수 있도록 합니다.
* **OneLake settings**에서 **Users can access data stored in OneLake with apps external to Fabric**를 활성화하여 서비스 주체가 외부 앱에서 데이터에 액세스할 수 있도록 합니다.

#### 1.3단계: 공유 작업 영역 설정 및 액세스 부여 {#step-13-set-up-a-shared-workspace-and-grant-access}

Braze에 연결하려는 모든 Fabric 리소스는 공유 작업 영역에 배치해야 합니다. 기본 **My Workspace**만 사용해 왔다면 새 공유 작업 영역을 생성하세요:

1. 탐색 메뉴에서 **Workspaces**를 선택한 다음 **+ New workspace**를 선택합니다.
2. 작업 영역의 **Name**을 입력한 다음 **Apply**를 선택합니다.

공유 작업 영역이 준비되면 서비스 주체에 액세스를 부여합니다:

1. 작업 영역을 선택한 다음 **Manage Access**를 선택합니다.
2. **+ Add people or groups**를 선택합니다.
3. 1.1단계에서 생성한 서비스 주체의 이름을 검색하여 선택합니다. 표시되지 않으면 1.2단계에서 **Service principals can use Fabric APIs** 설정을 활성화했는지 확인하세요.
4. 역할 드롭다운에서 **Contributor**를 선택합니다.

이제 서비스 주체는 SQL 엔드포인트를 통해 이 작업 영역의 Fabric 웨어하우스 리소스(Braze에 사용할 웨어하우스 포함)에 액세스할 수 있습니다.

#### 1.4단계: 테이블 설정 {#step-14-set-up-the-table}
Braze는 Fabric Warehouses의 테이블과 뷰를 모두 지원합니다. 새 웨어하우스를 생성해야 하는 경우 1.3단계의 공유 작업 영역 내에서 생성하세요. Fabric 콘솔에서 **Create > Data Warehouse > Warehouse**로 이동합니다.

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name]
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  --at least one of external_id, alias_name and alias_label, email, phone, or braze_id is required
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR,
  --braze_id can only be used to update existing users created through the Braze SDK
  BRAZE_ID VARCHAR,
  --If you include both email and phone, email is used as the primary identifier
  EMAIL VARCHAR,
  PHONE VARCHAR
)
GO
```

웨어하우스, 스키마, 테이블 또는 뷰 이름은 원하는 대로 지정할 수 있지만, 열 이름은 위의 정의와 일치해야 합니다.

- `UPDATED_AT` - 이 행이 테이블에 업데이트되거나 추가된 시간입니다. Braze는 `UPDATED_AT`가 마지막으로 동기화된 값보다 이후인 행을 동기화합니다. 새 행이 동일한 타임스탬프를 공유하는 경우 정확한 경계 타임스탬프의 행이 다시 동기화될 수 있습니다.
- **사용자 식별자 열** - 테이블에는 하나 이상의 사용자 식별자 열이 포함될 수 있습니다. 각 행에는 하나의 식별자만 포함해야 합니다(`external_id`, `alias_name`과 `alias_label`의 조합, `braze_id`, `email` 또는 `phone` 중 하나). 소스 테이블에는 1개, 2개, 3개, 4개 또는 5개 식별자 유형 모두에 대한 열이 있을 수 있습니다.
    - `EXTERNAL_ID` - 업데이트하려는 사용자를 식별합니다. Braze에서 사용되는 `external_id` 값과 일치해야 합니다.
    - `ALIAS_NAME` 및 `ALIAS_LABEL` - 이 두 열은 사용자 별칭 객체를 생성합니다. `alias_name`은 고유 식별자여야 하며, `alias_label`은 별칭 유형을 지정합니다. 사용자는 서로 다른 레이블을 가진 여러 별칭을 가질 수 있지만, `alias_label`당 하나의 `alias_name`만 가질 수 있습니다.
    - `BRAZE_ID` - Braze 사용자 식별자입니다. Braze SDK에 의해 생성되며, 클라우드 데이터 수집을 통해 Braze ID로 새 사용자를 생성할 수 없습니다. 새 사용자를 생성하려면 외부 사용자 ID 또는 사용자 별칭을 지정하세요.
    - `EMAIL` - 사용자의 이메일 주소입니다. 동일한 이메일 주소를 가진 프로필이 여러 개 있는 경우, 가장 최근에 업데이트된 프로필이 업데이트 우선순위를 갖습니다. 이메일과 전화번호를 모두 포함하면 이메일이 기본 식별자로 사용됩니다.
    - `PHONE` - 사용자의 전화번호입니다. 동일한 전화번호를 가진 프로필이 여러 개 있는 경우, 가장 최근에 업데이트된 프로필이 업데이트 우선순위를 갖습니다.
- `PAYLOAD` - Braze에서 사용자에게 동기화하려는 필드의 JSON 문자열입니다.


#### 1.5단계: 웨어하우스 연결 문자열 가져오기 {#step-15-get-warehouse-connection-string}
웨어하우스의 SQL 엔드포인트를 가져오려면 Fabric에서 **작업 영역**으로 이동하여 항목 목록에서 웨어하우스 이름 위에 마우스를 올린 다음 **Copy SQL connection string**을 선택합니다.

![사용자가 SQL 연결 문자열을 가져와야 하는 Microsoft Azure의 Fabric 콘솔 페이지]({% image_buster /assets/img/cloud_ingestion/fabric_1.png %})


#### 1.6단계: 방화벽에서 Braze IP 허용(선택 사항) {#step-16-allow-braze-ips-in-firewall-optional}

Microsoft Fabric 계정의 구성에 따라 Braze의 트래픽을 허용하기 위해 방화벽에서 다음 IP 주소를 허용해야 할 수 있습니다. 이를 활성화하는 방법에 대한 자세한 내용은 [Entra 조건부 액세스](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access)에 관한 관련 설명서를 참조하세요.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### 2단계: Braze 대시보드에서 새 소스 생성 {#step-2-create-a-new-source-in-the-braze-dashboard}


{% tabs %}
{% tab Snowflake %}

Braze 대시보드에서 **Data Settings** > **Cloud Data Ingestion** > **Sources**로 이동하여 **Add data source**를 선택한 다음 **Snowflake**를 선택합니다.

#### 2.1단계: Snowflake 연결 정보 추가 {#step-21-add-snowflake-connection-information}

소스 이름을 선택하고 Snowflake 자격 증명 및 구성을 입력한 다음 다음 단계로 진행합니다.

계속하기 전에 **Snowflake Account Locator**에 입력하는 값을 확인하세요.

**Snowflake Account Locator** 필드에 Snowflake [계정 식별자](https://docs.snowflake.com/en/user-guide/admin-account-identifier)를 입력합니다. `myorganization-myaccount`와 같은 계정 식별자 값만 입력하세요. `https://`, `.snowflakecomputing.com` 또는 경로를 포함하지 마세요.

Snowflake 계정 식별자를 찾으려면:

1. Snowsight에서 계정 메뉴를 선택합니다.
2. **View account details**를 선택합니다.
3. **Account identifier** 값을 복사합니다.
4. Snowflake URL에서 복사하는 경우 `.snowflakecomputing.com` 앞의 값만 사용하세요.

#### 2.2단계: Braze 사용자에 공개 키 추가 {#step-22-add-a-public-key-to-the-braze-user}

자격 증명과 구성을 입력한 후 **Save credentials**를 클릭하고 RSA 키를 생성한 다음 Snowflake로 돌아가 설정을 완료합니다. 대시보드에 표시된 공개 키를 Braze가 Snowflake에 연결하기 위해 생성한 사용자에 추가합니다.

이 작업을 수행하는 방법에 대한 자세한 내용은 [Snowflake 설명서](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)를 참조하세요. 키를 교체하려는 경우 Braze가 새 키 쌍을 생성하고 새 공개 키를 제공할 수 있습니다.

```sql
ALTER USER BRAZE_INGESTION_USER SET RSA_PUBLIC_KEY='MIIBIjANBgkqhkiG9w0BA...';
```
{% endtab %}
{% tab Redshift %}

Braze 대시보드에서 **Data Settings** > **Cloud Data Ingestion** > **Sources**로 이동하여 **Add data source**를 선택한 다음 **Amazon Redshift**를 선택합니다.

#### 2.1단계: Redshift 연결 정보 및 소스 테이블 추가 {#step-21-add-redshift-connection-information-and-source-table}

소스 이름을 선택하고 Redshift 자격 증명 및 구성을 입력합니다. 프라이빗 네트워크 터널을 사용하는 경우 슬라이더를 토글하고 터널 정보를 입력합니다. 그런 다음 다음 단계로 진행합니다.

{% alert note %}
Braze 대시보드에서 **Database name** 필드는 Amazon Redshift가 데이터베이스 식별자에 추가 문자를 지원하더라도 문자(A–Z, a–z), 숫자(0–9), 밑줄(_)만 허용합니다.
{% endalert %}

#### 2.2단계: 연결 테스트 및 소스 연결 {#step-22-test-connection-and-connect-to-source}

다음으로 **Test connection**을 선택합니다. 성공하면 나머지 설정을 완료하고 **Connect to Source**를 클릭합니다. 연결에 실패하면 문제 해결에 도움이 되는 오류 메시지가 표시됩니다.

#### 문제 해결: 잘못된 스냅샷 식별자 {#troubleshooting-invalid-snapshot-identifier}

**Test connection** 또는 동기화 설정 중에 Braze가 `Invalid snapshot identifier` 오류를 반환하면, 소스 객체가 쿼리될 때 사용되는 스냅샷 참조를 Redshift가 확인할 수 없는 것입니다.

Redshift에서 스냅샷은 클러스터의 특정 시점 백업입니다. 각 스냅샷에는 Redshift가 해당 백업 상태를 참조하는 데 사용하는 고유 식별자가 있습니다. 자세한 내용은 [Amazon Redshift 스냅샷 및 백업](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshots.html)을 참조하세요.

이 오류는 Braze가 소스 객체를 검증하는 동안 메타데이터가 변경될 때 발생할 수 있습니다(예: 스냅샷 복사, 복원 또는 복제 관련 작업 중). 자세한 내용은 [다른 AWS 리전으로 스냅샷 복사](https://docs.aws.amazon.com/redshift/latest/mgmt/cross-region-snapshot-copy.html) 및 [스냅샷에서 클러스터 복원](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-snapshot-restore-cluster-from-snapshot.html)을 참조하세요.

문제를 해결하려면:

1. Braze에서 클러스터 엔드포인트, 데이터베이스, 스키마, 객체 이름을 포함한 소스 설정을 확인합니다.
2. Redshift에서 직접 동일한 쿼리를 실행하여 테이블 또는 뷰가 읽기 가능하고 안정적인지 확인합니다.
3. 활성 스냅샷, 복원, 크기 조정 또는 복제 작업이 완료된 후 다시 시도합니다.
4. 문제가 지속되면 자주 변경되는 기본 테이블 대신 구체화된 뷰를 쿼리합니다.

구체화된 뷰는 스케줄에 따라 새로 고칠 수 있는 사전 계산된 쿼리 결과를 저장하므로 CDI 동기화에 대한 읽기가 더 안정적일 수 있습니다. 자세한 내용은 [Amazon Redshift의 구체화된 뷰](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-overview.html)를 참조하세요.

예시:

```sql
CREATE MATERIALIZED VIEW ingestion.users_attributes_mv AS
SELECT updated_at, external_id, alias_label, alias_name, braze_id, email, phone, payload
FROM ingestion.users_attributes_sync;

REFRESH MATERIALIZED VIEW ingestion.users_attributes_mv;
```

구체화된 뷰를 생성한 후 Braze CDI 동기화에서 기본 테이블 대신 구체화된 뷰 이름을 소스 객체로 사용하세요.
{% endtab %}
{% tab BigQuery %}

Braze 대시보드에서 **Data Settings** > **Cloud Data Ingestion** > **Sources**로 이동하여 **Add data source**를 선택한 다음 **Google BigQuery**를 선택합니다.

#### 2.1단계: BigQuery 연결 정보 및 소스 테이블 추가 {#step-21-add-bigquery-connection-information-and-source-table}

소스 이름을 선택합니다. 그런 다음 JSON 키를 업로드하고 서비스 계정 이름을 입력합니다. 그런 다음 나머지 구성 필드를 입력합니다.

#### 2.2단계: 연결 테스트 및 소스 연결

다음으로 **Test connection**을 선택합니다. 성공하면 나머지 설정을 완료하고 **Connect to Source**를 클릭합니다. 연결에 실패하면 문제 해결에 도움이 되는 오류 메시지가 표시됩니다.

{% endtab %}
{% tab Databricks %}

Braze 대시보드에서 **Data Settings** > **Cloud Data Ingestion** > **Sources**로 이동하여 **Add data source**를 선택한 다음 **Databricks**를 선택합니다.

#### 2.1단계: Databricks 연결 정보 및 소스 테이블 추가 {#step-21-add-databricks-connection-information-and-source-table}

소스 이름을 선택하고 Databricks 자격 증명 및 구성을 입력합니다. 그런 다음 다음 단계로 진행합니다.

#### 2.2단계: 연결 테스트 및 소스 연결

다음으로 **Test connection**을 선택합니다. 성공하면 나머지 설정을 완료하고 **Connect to Source**를 클릭합니다. 연결에 실패하면 문제 해결에 도움이 되는 오류 메시지가 표시됩니다.

{% alert note %}
소스를 생성하기 전에 반드시 테스트에 성공해야 합니다. 생성 페이지를 닫으면 소스가 저장되지 않습니다.
{% endalert %}

{% endtab %}
{% tab Microsoft Fabric %}

Braze 대시보드에서 Data Settings > Cloud Data Ingestion > Sources로 이동하여 **Add data source**를 선택한 다음 **Microsoft Fabric**을 선택합니다.

#### 2.1단계: 클라우드 데이터 수집 동기화 설정 {#step-21-set-up-a-cloud-data-ingestion-sync}

소스 이름을 선택하고 Microsoft Fabric 자격 증명 및 구성을 입력합니다.
- **Credentials Name**은 Braze에서 이 자격 증명에 대한 레이블이며, 유용한 값을 설정할 수 있습니다.
- Tenant ID, Principal ID, Client Secret, Connection String을 가져오는 방법에 대한 자세한 내용은 섹션 1의 단계를 참조하세요.

#### 2.2단계: 연결 테스트 및 소스 연결

다음으로 **Test connection**을 선택합니다. 성공하면 나머지 설정을 완료하고 **Connect to Source**를 클릭합니다. 연결에 실패하면 문제 해결에 도움이 되는 오류 메시지가 표시됩니다.

{% alert note %}
소스를 생성하기 전에 반드시 테스트에 성공해야 합니다. 생성 페이지를 닫으면 소스가 저장되지 않습니다.
{% endalert %}

{% endtab %}

{% endtabs %}

### 3단계: Braze 대시보드에서 새 동기화 생성 {#step-3-create-a-new-sync-in-the-braze-dashboard}
**Data Settings** > **Cloud Data Ingestion** > **Syncs**로 이동하여 **Create data sync**를 선택합니다.

{% tabs %}
{% tab Snowflake %}

#### 3.1단계: 동기화 세부 정보 구성 및 연결 테스트 {#step-31-configure-sync-details-and-test-connection}
동기화 이름을 선택합니다. 그런 다음 활성 소스 중에서 선택하고 동기화할 소스 테이블을 입력합니다. 데이터 유형을 선택하고 **Test Connection**을 클릭합니다.

성공하면 데이터 미리보기가 표시됩니다. **Next: Notifications**를 선택하여 계속합니다. 연결에 실패하면 문제 해결에 도움이 되는 오류 메시지가 표시됩니다.

{% alert note %}
다음 단계로 진행하기 전에 반드시 동기화 테스트에 성공해야 합니다. 동기화 생성 페이지를 닫아야 하는 경우 **Save as draft**를 클릭하여 진행 중인 작업을 저장하세요.
{% endalert %}

#### 3.2단계: 알림 기본 설정 추가 {#step-32-add-notification-preferences}
동기화 오류 알림을 받을 연락처 이메일을 입력합니다. Braze는 이 연락처 정보를 사용하여 예기치 않은 테이블 액세스 손실과 같은 통합 오류에 대한 알림을 보냅니다.

연락처 이메일은 누락된 테이블, 권한 등과 같은 글로벌 또는 동기화 수준 오류에 대한 알림만 받습니다. 행 수준 문제에 대한 알림은 받지 않습니다. 글로벌 오류는 동기화 실행을 방해하는 연결의 심각한 문제를 나타냅니다.

이러한 문제에는 다음이 포함될 수 있습니다:

- 연결 문제
- 리소스 부족
- 권한 문제
- (카탈로그 동기화에만 해당) 카탈로그 티어의 공간 부족

#### 3.3단계: 스케줄링 {#step-33-scheduling}
마지막으로 동기화를 비반복 또는 반복으로 구성합니다.

비반복 동기화는 수동으로 또는 API를 통해 트리거할 수 있습니다.

반복 동기화는 15분마다에서 월 1회까지 빈도를 설정할 수 있습니다. Braze는 반복 동기화를 UTC 시간대로 스케줄링합니다.

{% endtab %}

{% tab Redshift %}

#### 3.1단계: 동기화 세부 정보 구성 및 연결 테스트
동기화 이름을 선택합니다. 그런 다음 활성 소스 중에서 선택하고 동기화할 소스 테이블을 입력합니다. 데이터 유형을 선택하고 **Test Connection**을 클릭합니다.

성공하면 데이터 미리보기가 표시됩니다. **Next: Notifications**를 선택하여 계속합니다. 연결에 실패하면 문제 해결에 도움이 되는 오류 메시지가 표시됩니다.

{% alert note %}
다음 단계로 진행하기 전에 반드시 동기화 테스트에 성공해야 합니다. 동기화 생성 페이지를 닫아야 하는 경우 **Save as draft**를 클릭하여 진행 중인 작업을 저장하세요.
{% endalert %}

#### 3.2단계: 알림 기본 설정 추가
동기화 오류 알림을 받을 연락처 이메일을 입력합니다. Braze는 이 연락처 정보를 사용하여 예기치 않은 테이블 액세스 손실과 같은 통합 오류에 대한 알림을 보냅니다.

연락처 이메일은 누락된 테이블, 권한 등과 같은 글로벌 또는 동기화 수준 오류에 대한 알림만 받습니다. 행 수준 문제에 대한 알림은 받지 않습니다. 글로벌 오류는 동기화 실행을 방해하는 연결의 심각한 문제를 나타냅니다.

이러한 문제에는 다음이 포함될 수 있습니다:

- 연결 문제
- 리소스 부족
- 권한 문제

(카탈로그 동기화에만 해당) 카탈로그 티어의 공간 부족

#### 3.3단계: 스케줄링
마지막으로 동기화를 비반복 또는 반복으로 구성합니다.

비반복 동기화는 수동으로 또는 API를 통해 트리거할 수 있습니다.

반복 동기화는 15분마다에서 월 1회까지 빈도를 설정할 수 있습니다. Braze는 반복 동기화를 UTC 시간대로 스케줄링합니다.

{% endtab %}

{% tab BigQuery %}

#### 3.1단계: 동기화 세부 정보 구성 및 연결 테스트
동기화 이름을 선택합니다. 그런 다음 활성 소스 중에서 선택하고 동기화할 소스 테이블을 입력합니다. 데이터 유형을 선택하고 **Test Connection**을 클릭합니다.

성공하면 데이터 미리보기가 표시됩니다. **Next: Notifications**를 선택하여 계속합니다. 연결에 실패하면 문제 해결에 도움이 되는 오류 메시지가 표시됩니다.

{% alert note %}
다음 단계로 진행하기 전에 반드시 동기화 테스트에 성공해야 합니다. 동기화 생성 페이지를 닫아야 하는 경우 **Save as draft**를 클릭하여 진행 중인 작업을 저장하세요.
{% endalert %}

#### 3.2단계: 알림 기본 설정 추가
동기화 오류 알림을 받을 연락처 이메일을 입력합니다. Braze는 이 연락처 정보를 사용하여 예기치 않은 테이블 액세스 손실과 같은 통합 오류에 대한 알림을 보냅니다.

연락처 이메일은 누락된 테이블, 권한 등과 같은 글로벌 또는 동기화 수준 오류에 대한 알림만 받습니다. 행 수준 문제에 대한 알림은 받지 않습니다. 글로벌 오류는 동기화 실행을 방해하는 연결의 심각한 문제를 나타냅니다. 이러한 문제에는 다음이 포함될 수 있습니다:

- 연결 문제
- 리소스 부족
- 권한 문제

(카탈로그 동기화에만 해당) 카탈로그 티어의 공간 부족

#### 3.3단계: 스케줄링
마지막으로 동기화를 비반복 또는 반복으로 구성합니다.

비반복 동기화는 수동으로 또는 API를 통해 트리거할 수 있습니다.

반복 동기화는 15분마다에서 월 1회까지 빈도를 설정할 수 있습니다. Braze는 반복 동기화를 UTC 시간대로 스케줄링합니다.

{% endtab %}

{% tab Databricks %}

#### 3.1단계: 동기화 세부 정보 구성 및 연결 테스트
동기화 이름을 선택합니다. 그런 다음 활성 소스 중에서 선택하고 동기화할 소스 테이블을 입력합니다. 데이터 유형을 선택하고 **Test Connection**을 클릭합니다.

성공하면 데이터 미리보기가 표시됩니다. **Next: Notifications**를 선택하여 계속합니다. 연결에 실패하면 문제 해결에 도움이 되는 오류 메시지가 표시됩니다.

{% alert note %}
다음 단계로 진행하기 전에 반드시 동기화 테스트에 성공해야 합니다. 동기화 생성 페이지를 닫아야 하는 경우 **Save as draft**를 클릭하여 진행 중인 작업을 저장하세요.
{% endalert %}

#### 3.2단계: 알림 기본 설정 추가
동기화 오류 알림을 받을 연락처 이메일을 입력합니다. Braze는 이 연락처 정보를 사용하여 예기치 않은 테이블 액세스 손실과 같은 통합 오류에 대한 알림을 보냅니다.

연락처 이메일은 누락된 테이블, 권한 등과 같은 글로벌 또는 동기화 수준 오류에 대한 알림만 받습니다. 행 수준 문제에 대한 알림은 받지 않습니다. 글로벌 오류는 동기화 실행을 방해하는 연결의 심각한 문제를 나타냅니다.

이러한 문제에는 다음이 포함될 수 있습니다:
- 연결 문제
- 리소스 부족
- 권한 문제

(카탈로그 동기화에만 해당) 카탈로그 티어의 공간 부족

#### 3.3단계: 스케줄링
마지막으로 동기화를 비반복 또는 반복으로 구성합니다.

비반복 동기화는 수동으로 또는 API를 통해 트리거할 수 있습니다.

반복 동기화는 15분마다에서 월 1회까지 빈도를 설정할 수 있습니다. Braze는 반복 동기화를 UTC 시간대로 스케줄링합니다.

{% endtab %}
{% tab Microsoft Fabric %}

#### 3.1단계: 동기화 세부 정보 구성 및 연결 테스트

동기화 이름을 선택합니다. 그런 다음 활성 소스 중에서 선택하고 동기화할 소스 테이블을 입력합니다. 데이터 유형을 선택하고 **Test Connection**을 클릭합니다.

성공하면 데이터 미리보기가 표시됩니다. **Next: Notifications**를 선택하여 계속합니다. 연결에 실패하면 문제 해결에 도움이 되는 오류 메시지가 표시됩니다.

{% alert note %}
다음 단계로 진행하기 전에 반드시 동기화 테스트에 성공해야 합니다. 동기화 생성 페이지를 닫아야 하는 경우 **Save as draft**를 클릭하여 진행 중인 작업을 저장하세요.
{% endalert %}

#### 3.2단계: 알림 기본 설정 추가
동기화 오류 알림을 받을 연락처 이메일을 입력합니다. Braze는 이 연락처 정보를 사용하여 예기치 않은 테이블 액세스 손실과 같은 통합 오류에 대한 알림을 보냅니다.

연락처 이메일은 누락된 테이블, 권한 등과 같은 글로벌 또는 동기화 수준 오류에 대한 알림만 받습니다. 행 수준 문제에 대한 알림은 받지 않습니다. 글로벌 오류는 동기화 실행을 방해하는 연결의 심각한 문제를 나타냅니다.

이러한 문제에는 다음이 포함될 수 있습니다:

- 연결 문제
- 리소스 부족
- 권한 문제

(카탈로그 동기화에만 해당) 카탈로그 티어의 공간 부족

#### 3.3단계: 스케줄링
마지막으로 동기화를 비반복 또는 반복으로 구성합니다.

비반복 동기화는 수동으로 또는 API를 통해 트리거할 수 있습니다.

반복 동기화는 15분마다에서 월 1회까지 빈도를 설정할 수 있습니다. Braze는 반복 동기화를 UTC 시간대로 스케줄링합니다.

{% endtab %}
{% endtabs %}

{% alert note %}
통합이 초안에서 활성 상태로 전환되려면 반드시 테스트에 성공해야 합니다. 생성 페이지를 닫으면 통합이 저장되며, 세부 정보 페이지를 다시 방문하여 변경하고 테스트할 수 있습니다.
{% endalert %}

## 추가 통합 또는 사용자 설정(선택 사항) {#set-up-additional-integrations-or-users-optional}

{% tabs %}
{% tab Snowflake %}
Braze와 여러 통합을 설정할 수 있지만, 각 통합은 서로 다른 테이블을 동기화하도록 구성해야 합니다. 추가 동기화를 생성할 때 동일한 Snowflake 계정에 연결하는 경우 기존 자격 증명을 재사용할 수 있습니다.

통합 간에 동일한 사용자와 역할을 재사용하는 경우 공개 키를 다시 추가할 필요가 없습니다.
{% endtab %}
{% tab Redshift %}
Braze와 여러 통합을 설정할 수 있지만, 각 통합은 서로 다른 테이블을 동기화하도록 구성해야 합니다. 추가 동기화를 생성할 때 동일한 Snowflake 또는 Redshift 계정에 연결하는 경우 기존 자격 증명을 재사용할 수 있습니다.

통합 간에 동일한 사용자를 재사용하는 경우, 해당 사용자가 모든 활성 동기화에서 제거되기 전까지는 Braze 대시보드에서 사용자를 삭제할 수 없습니다.
{% endtab %}
{% tab BigQuery %}

Braze와 여러 통합을 설정할 수 있지만, 각 통합은 서로 다른 테이블을 동기화하도록 구성해야 합니다. 추가 동기화를 생성할 때 동일한 BigQuery 계정에 연결하는 경우 기존 자격 증명을 재사용할 수 있습니다.

통합 간에 동일한 사용자를 재사용하는 경우, 해당 사용자가 모든 활성 동기화에서 제거되기 전까지는 Braze 대시보드에서 사용자를 삭제할 수 없습니다.

{% endtab %}
{% tab Databricks %}

Braze와 여러 통합을 설정할 수 있지만, 각 통합은 서로 다른 테이블을 동기화하도록 구성해야 합니다. 추가 동기화를 생성할 때 동일한 Databricks 계정에 연결하는 경우 기존 자격 증명을 재사용할 수 있습니다.

통합 간에 동일한 사용자를 재사용하는 경우, 해당 사용자가 모든 활성 동기화에서 제거되기 전까지는 Braze 대시보드에서 사용자를 삭제할 수 없습니다.

{% endtab %}
{% tab Microsoft Fabric %}

Braze와 여러 통합을 설정할 수 있지만, 각 통합은 서로 다른 테이블을 동기화하도록 구성해야 합니다. 추가 동기화를 생성할 때 동일한 Fabric 계정에 연결하는 경우 기존 자격 증명을 재사용할 수 있습니다.

통합 간에 동일한 사용자를 재사용하는 경우, 해당 사용자가 모든 활성 동기화에서 제거되기 전까지는 Braze 대시보드에서 사용자를 삭제할 수 없습니다.

{% endtab %}
{% endtabs %}

## 동기화 실행 {#running-the-sync}

{% tabs %}
{% tab Snowflake %}
활성화되면 설정 시 구성한 스케줄에 따라 동기화가 실행됩니다. 정상 테스트 스케줄 외에 동기화를 실행하거나 최신 데이터를 가져오려면 **Sync Now**를 선택하세요. 이 실행은 정기적으로 예약된 향후 동기화에 영향을 미치지 않습니다.

{% endtab %}
{% tab Redshift %}
활성화되면 설정 시 구성한 스케줄에 따라 동기화가 실행됩니다. 정상 테스트 스케줄 외에 동기화를 실행하거나 최신 데이터를 가져오려면 **Sync Now**를 선택하세요. 이 실행은 정기적으로 예약된 향후 동기화에 영향을 미치지 않습니다.

{% endtab %}
{% tab BigQuery %}

활성화되면 설정 시 구성한 스케줄에 따라 동기화가 실행됩니다. 정상 테스트 스케줄 외에 동기화를 실행하거나 최신 데이터를 가져오려면 **Sync Now**를 선택하세요. 이 실행은 정기적으로 예약된 향후 동기화에 영향을 미치지 않습니다.

{% endtab %}
{% tab Databricks %}

활성화되면 설정 시 구성한 스케줄에 따라 동기화가 실행됩니다. 정상 테스트 스케줄 외에 동기화를 실행하거나 최신 데이터를 가져오려면 **Sync Now**를 선택하세요. 이 실행은 정기적으로 예약된 향후 동기화에 영향을 미치지 않습니다.

{% endtab %}
{% tab Microsoft Fabric %}

활성화되면 설정 시 구성한 스케줄에 따라 동기화가 실행됩니다. 정상 테스트 스케줄 외에 동기화를 실행하거나 최신 데이터를 가져오려면 **Sync Now**를 선택하세요. 이 실행은 정기적으로 예약된 향후 동기화에 영향을 미치지 않습니다.

{% endtab %}

{% endtabs %}