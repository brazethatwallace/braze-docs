---
nav_title: 연결된 소스
article_title: 연결된 소스
description: "이 페이지에서는 Braze 클라우드 데이터 수집을 사용하여 관련 데이터를 Snowflake, Redshift, BigQuery 및 Databricks 통합과 동기화하는 방법을 설명합니다."
page_order: 2
page_type: reference

---

# 연결된 소스 {#connected-sources}

> 연결된 소스는 Braze의 클라우드 데이터 수집(CDI) 기능으로 데이터를 직접 동기화하는 방식의 제로 복사 대안입니다. 연결된 소스는 데이터 웨어하우스에 직접 쿼리하여 기본 데이터를 Braze에 복사하지 않고도 새로운 세그먼트를 생성합니다.

Braze 워크스페이스에 연결된 소스를 추가한 후 세그먼트 확장 내에서 CDI 세그먼트를 생성할 수 있습니다. CDI 세그먼트 확장을 사용하면 데이터 웨어하우스를 직접 쿼리하는 SQL을 작성할 수 있으며(CDI 연결 소스를 통해 제공되는 데이터를 사용), Braze 내에서 타겟팅할 수 있는 사용자 그룹을 생성하고 유지할 수 있습니다.

이 소스를 사용하여 세그먼트를 생성하는 방법에 대한 자세한 내용은 [CDI 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments)을 참조하세요.

{% alert warning %}
연결된 소스는 데이터 웨어하우스에서 직접 실행되므로 데이터 웨어하우스에서 이러한 쿼리를 실행하는 데 관련된 모든 비용이 발생합니다. 연결된 소스는 데이터 포인트를 기록하지 않으며, CDI 세그먼트 확장은 SQL 세그먼트 크레딧을 소모하지 않습니다.
{% endalert %}

## 연결된 소스 통합하기 {#integrating-connected-sources}

### 1단계: 리소스 연결하기 {#step-1-connect-your-resources}

클라우드 데이터 수집 연결된 소스를 사용하려면 Braze와 인스턴스에서 일부 설정이 필요합니다. 다음 단계에 따라 통합을 설정하세요&#8722;일부 단계는 데이터 웨어하우스에서, 일부 단계는 Braze 대시보드에서 수행합니다.

{% tabs %}
{% tab Snowflake %}
**데이터 웨어하우스에서**
1. 역할을 생성하고 스키마에서 테이블을 쿼리하고 생성할 수 있는 권한을 부여합니다.
2. 웨어하우스를 설정하고 해당 역할에 액세스 권한을 부여합니다.
3. 해당 역할에 대한 사용자를 생성합니다.
4. 구성에 따라 Snowflake 네트워크 정책에서 Braze IP를 허용해야 할 수 있습니다.

**Braze 대시보드에서**

{: start="5"}
5. Braze 대시보드에서 새 연결된 소스를 생성합니다.
6. 연결된 소스의 동기화 세부 정보를 구성합니다.
7. Braze 대시보드에서 제공된 공개 키를 가져옵니다.

**데이터 웨어하우스에서**

{: start="8"}
8. Braze 대시보드의 공개 키를 [인증을 위한 Snowflake 사용자](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)에 추가합니다. 완료되면 연결된 소스를 사용하여 하나 이상의 CDI 세그먼트 확장을 생성할 수 있습니다.
{% endtab %}

{% tab Redshift %}
1. Redshift 환경에서 소스 데이터와 필요한 리소스를 설정합니다.
2. Braze 대시보드에서 새 연결된 소스를 생성합니다.
3. 통합을 테스트합니다.
4. 연결된 소스를 사용하여 하나 이상의 CDI 세그먼트 확장을 생성합니다.
{% endtab %}

{% tab BigQuery %}
1. BigQuery 환경에서 소스 데이터와 필요한 리소스를 설정합니다.
2. 서비스 계정을 생성하고 동기화하려는 데이터가 포함된 BigQuery 프로젝트 및 데이터셋에 대한 액세스를 허용합니다.
3. Braze 대시보드에서 새 연결된 소스를 생성합니다.
4. 통합을 테스트합니다.
5. 연결된 소스를 사용하여 하나 이상의 CDI 세그먼트 확장을 생성합니다.
{% endtab %}

{% tab Databricks %}
1. Databricks 환경에서 소스 데이터와 필요한 리소스를 설정합니다.
2. 서비스 계정을 생성하고 동기화하려는 데이터가 포함된 Databricks 프로젝트 및 데이터셋에 대한 액세스를 허용합니다.
3. Braze 대시보드에서 새 연결된 소스를 생성합니다.
4. 통합을 테스트합니다.
5. 연결된 소스를 사용하여 하나 이상의 CDI 세그먼트 확장을 생성합니다.

{% alert important %}
Braze가 Classic 및 Pro SQL 인스턴스에 연결할 때 2~5분의 워밍업 시간이 소요될 수 있으며, 이로 인해 연결 설정 및 테스트, CDI 세그먼트 확장 생성 및 새로고침 시 지연이 발생할 수 있습니다. 서버리스 SQL 인스턴스를 사용하면 워밍업 시간을 최소화하고 쿼리 처리량을 개선할 수 있지만, 통합 비용이 약간 높아질 수 있습니다.
{% endalert %}

{% endtab %}

{% tab Microsoft Fabric %}
1. 서비스 주체를 생성하고 통합에 사용할 Fabric 작업 영역에 대한 액세스를 허용합니다.
2. Fabric 작업 영역에서 소스 데이터를 설정하고 서비스 주체에 권한을 부여합니다.
3. Braze 대시보드에서 새 연결된 소스를 생성합니다.
4. 통합을 테스트합니다.
5. 연결된 소스를 사용하여 하나 이상의 CDI 세그먼트 확장을 생성합니다.
{% endtab %}

{% endtabs %}

### 2단계: 데이터 웨어하우스 설정하기 {#step-2-set-up-your-data-warehouse}

데이터 웨어하우스 환경에서 소스 데이터와 필요한 리소스를 설정합니다. 연결된 소스는 하나 이상의 테이블을 참조할 수 있으므로, Braze 사용자가 연결된 소스에서 원하는 모든 테이블에 액세스할 수 있는 권한이 있는지 확인하세요.

{% tabs %}
{% tab Snowflake %}
#### 2.1단계: 역할 생성 및 권한 부여 {#step-21-create-a-role-and-grant-permissions}

연결된 소스에서 사용할 역할을 생성합니다. 이 역할은 CDI 세그먼트 확장에서 사용 가능한 테이블 목록을 생성하고, 소스 테이블을 쿼리하여 새 Segments를 생성하는 데 사용됩니다. 연결된 소스가 생성되면 Braze는 소스 스키마에서 사용자가 사용할 수 있는 모든 테이블의 이름과 설명을 검색합니다.

스키마의 모든 테이블에 대한 액세스를 부여하거나 특정 테이블에만 권한을 부여할 수 있습니다. Braze 역할이 액세스할 수 있는 테이블은 CDI 세그먼트 확장에서 쿼리할 수 있습니다.

`create table` 권한은 Braze가 CDI 세그먼트 확장 쿼리 결과로 테이블을 생성한 후 Braze에서 Segment를 업데이트하는 데 필요합니다. Braze는 Segment당 임시 테이블을 생성하며, 해당 테이블은 Braze가 Segment를 업데이트하는 동안에만 유지됩니다.

```sql
CREATE ROLE BRAZE_INGESTION_ROLE;

GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT CREATE TABLE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to all current and future tables or views in the schema
GRANT SELECT ON ALL TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
GRANT SELECT ON FUTURE TABLES IN SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;

-- grant access to specific tables or views in the schema
GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC TO ROLE BRAZE_INGESTION_ROLE;

```

#### 2.2단계: 웨어하우스 설정 및 Braze 역할에 액세스 부여 {#step-22-set-up-the-warehouse-and-give-access-to-braze-role}

```sql
CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;

GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;
```

{% alert note %}
웨어하우스에 **자동 재개** 플래그가 켜져 있어야 합니다. 켜져 있지 않은 경우, 쿼리를 실행할 때 Braze가 이를 켤 수 있도록 웨어하우스에 대한 추가 `OPERATE` 권한을 Braze에 부여해야 합니다.
{% endalert %}

#### 2.3단계: 사용자 설정 {#step-23-set-up-the-user}
```sql
CREATE USER BRAZE_INGESTION_USER;

GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
```

이후 단계에서 Braze와 연결 정보를 공유하고 사용자에 추가할 공개 키를 받게 됩니다.

{% alert note %}
동일한 Snowflake 계정에 여러 워크스페이스를 연결할 때는 통합을 생성하는 각 Braze 워크스페이스에 대해 고유한 사용자를 생성해야 합니다. 워크스페이스 내에서는 통합 간에 동일한 사용자를 재사용할 수 있지만, 동일한 Snowflake 계정의 사용자가 워크스페이스 간에 중복되면 통합 생성이 실패합니다.
{% endalert %}

#### 2.4단계: Snowflake 네트워크 정책에서 Braze IP 허용(선택 사항) {#step-24-allow-braze-ips-in-your-snowflake-network-policy-optional}

Snowflake 계정의 구성에 따라 Snowflake 네트워크 정책에서 다음 IP 주소를 허용해야 할 수 있습니다. 이에 대한 자세한 내용은 [네트워크 정책 수정](https://docs.snowflake.com/en/user-guide/network-policies.html#modifying-network-policies)에 관한 Snowflake 설명서를 참조하세요.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}
{% endtab %}

{% tab Redshift %}
#### 2.1단계: 사용자 생성 및 권한 부여 {#step-21-create-user-and-grant-permissions}

```sql
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT CREATE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

연결된 소스에서 사용할 사용자를 생성합니다. 이 사용자는 CDI 세그먼트 확장에서 사용 가능한 테이블 목록을 생성하고, 소스 테이블을 쿼리하여 새 Segments를 생성하는 데 사용됩니다. 연결된 소스가 생성되면 Braze는 소스 스키마에서 사용자가 사용할 수 있는 모든 테이블의 이름과 설명을 검색합니다. 여러 CDI 통합을 생성하는 경우 스키마에 대한 권한을 부여하거나 그룹을 사용하여 권한을 관리할 수 있습니다.

스키마의 모든 테이블에 대한 액세스를 부여하거나 특정 테이블에만 권한을 부여할 수 있습니다. Braze 역할이 액세스할 수 있는 테이블은 CDI 세그먼트 확장에서 쿼리할 수 있습니다. 새 테이블이 생성될 때 사용자에게 액세스 권한을 부여하거나 사용자에 대한 기본 권한을 설정해야 합니다.

`create table` 권한은 Braze가 CDI 세그먼트 확장 쿼리 결과로 테이블을 생성한 후 Braze에서 Segment를 업데이트하는 데 필요합니다. Braze는 Segment당 임시 테이블을 생성하며, 해당 테이블은 Braze가 Segment를 업데이트하는 동안에만 유지됩니다.


#### 2.2단계: Braze IP에 대한 액세스 허용 {#step-22-allow-access-to-braze-ips}

방화벽이나 기타 네트워크 정책이 있는 경우 Braze에 Redshift 인스턴스에 대한 네트워크 액세스를 부여해야 합니다. Braze 대시보드 리전에 해당하는 다음 IP에서의 액세스를 허용하세요.

Braze가 Redshift의 데이터에 액세스할 수 있도록 보안 그룹을 변경해야 할 수도 있습니다. 다음 섹션의 IP와 Redshift 클러스터를 쿼리하는 데 사용되는 포트(기본값 5439)에서 인바운드 트래픽을 명시적으로 허용해야 합니다. 인바운드 규칙이 "모두 허용"으로 설정되어 있더라도 이 포트에서 Redshift TCP 연결을 명시적으로 허용해야 합니다. 또한 Braze가 클러스터에 연결할 수 있도록 Redshift 클러스터의 엔드포인트가 공개적으로 액세스 가능해야 합니다.

Redshift 클러스터를 공개적으로 액세스 가능하게 하고 싶지 않은 경우, VPC와 EC2 인스턴스를 설정하여 SSH 터널을 사용해 Redshift 데이터에 액세스할 수 있습니다. 자세한 내용은 [AWS: 로컬 머신에서 프라이빗 Amazon Redshift 클러스터에 어떻게 액세스하나요?](https://repost.aws/knowledge-center/private-redshift-cluster-local-machine)를 참조하세요.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% tab BigQuery %}
#### 2.1단계: 서비스 계정 생성 및 권한 부여 {#step-21-create-a-service-account-and-grant-permissions}

GCP에서 Braze가 테이블에 연결하고 데이터를 읽는 데 사용할 서비스 계정을 생성합니다. 서비스 계정에는 다음 섹션의 권한이 있어야 합니다:

- **BigQuery Connection User:** Braze가 연결할 수 있도록 허용합니다.
- **BigQuery User:** Braze에 쿼리 실행, 데이터셋 메타데이터 읽기, 테이블 목록 조회 액세스를 제공합니다.
- **BigQuery Data Viewer:** Braze에 데이터셋과 그 내용을 볼 수 있는 액세스를 제공합니다.
- **BigQuery Job User:** Braze에 작업을 실행할 수 있는 액세스를 제공합니다.
- **bigquery.tables.create** Braze에 Segment 새로고침 시 임시 테이블을 생성할 수 있는 액세스를 제공합니다.

연결된 소스에서 사용할 서비스 계정을 생성합니다. 이 사용자는 CDI 세그먼트 확장에서 사용 가능한 테이블 목록을 생성하고, 소스 테이블을 쿼리하여 새 Segments를 생성하는 데 사용됩니다. 연결된 소스가 생성되면 Braze는 소스 스키마에서 사용자가 사용할 수 있는 모든 테이블의 이름과 설명을 검색합니다.

데이터셋의 모든 테이블에 대한 액세스를 부여하거나 특정 테이블에만 권한을 부여할 수 있습니다. Braze 역할이 액세스할 수 있는 테이블은 CDI 세그먼트 확장에서 쿼리할 수 있습니다.

`create table` 권한은 Braze가 CDI 세그먼트 확장 쿼리 결과로 테이블을 생성한 후 Braze에서 Segment를 업데이트하는 데 필요합니다. Braze는 Segment당 임시 테이블을 생성하며, 해당 테이블은 Braze가 Segment를 업데이트하는 동안에만 유지됩니다.

서비스 계정을 생성하고 권한을 부여한 후 JSON 키를 생성합니다. 자세한 내용은 [Google Cloud: 서비스 계정 키 생성 및 삭제](https://cloud.google.com/iam/docs/keys-create-delete)를 참조하세요. 이 키는 나중에 Braze 대시보드에 업로드합니다.

#### 2.2단계: Braze IP에 대한 액세스 허용

네트워크 정책이 있는 경우 Braze에 BigQuery 인스턴스에 대한 네트워크 액세스를 부여해야 합니다. Braze 대시보드 리전에 해당하는 다음 IP에서의 액세스를 허용하세요.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Databricks %}
#### 2.1단계: 액세스 토큰 생성 {#step-21-create-an-access-token}

Braze가 Databricks에 액세스하려면 개인 액세스 토큰을 생성해야 합니다.

1. Databricks 작업 영역에서 상단 바의 Databricks 사용자 이름을 선택한 다음 드롭다운에서 **User Settings**를 선택합니다.
2. 서비스 계정에 연결된 소스에 사용되는 스키마에 대한 `CREATE TABLE` 권한이 있는지 확인합니다.
3. **Access tokens** 탭에서 **Generate new token**을 선택합니다.
4. 이 토큰을 식별하는 데 도움이 되는 코멘트(예: "Braze CDI")를 입력하고, Lifetime (days) 상자를 비워두어(공란) 토큰의 수명을 무제한으로 변경합니다.
5. **Generate**를 선택합니다.
6. 표시된 토큰을 복사한 다음 **Done**을 선택합니다.

이 토큰은 CDI 세그먼트 확장에서 사용 가능한 테이블 목록을 생성하고, 소스 테이블을 쿼리하여 새 Segments를 생성하는 데 사용됩니다. 연결된 소스가 생성되면 Braze는 소스 스키마에서 사용자가 사용할 수 있는 모든 테이블의 이름과 설명을 검색합니다.

스키마의 모든 테이블에 대한 액세스를 부여하거나 특정 테이블에만 권한을 부여할 수 있습니다. Braze 역할이 액세스할 수 있는 테이블은 CDI 세그먼트 확장에서 쿼리할 수 있습니다.

`create table` 권한은 Braze가 CDI 세그먼트 확장 쿼리 결과로 테이블을 생성한 후 Braze에서 Segment를 업데이트하는 데 필요합니다. Braze는 Segment당 임시 테이블을 생성하며, 해당 테이블은 Braze가 Segment를 업데이트하는 동안에만 유지됩니다.

자격 증명 생성 단계에서 Braze 대시보드에 입력해야 할 때까지 토큰을 안전한 곳에 보관하세요.

#### 2.2단계: Braze IP에 대한 액세스 허용

네트워크 정책이 있는 경우 Braze에 Databricks 인스턴스에 대한 네트워크 액세스를 부여해야 합니다. Braze 대시보드 리전에 해당하는 다음 IP에서의 액세스를 허용하세요.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% tab Microsoft Fabric %}
#### 2.1단계: Fabric 리소스에 대한 액세스 부여 {#step-21-grant-access-to-fabric-resources}
Braze는 Entra ID 인증을 사용하는 서비스 주체를 통해 Fabric 웨어하우스에 연결합니다. Braze가 사용할 새 서비스 주체를 생성하고 필요에 따라 Fabric 리소스에 대한 액세스를 부여합니다. Braze가 연결하려면 다음 세부 정보가 필요합니다:

{% multi_lang_include data_unification/azure_service_principal_credentials.md %}

{% multi_lang_include data_unification/azure_app_registration_steps.md %}

{% alert note %}
Azure는 서비스 주체 시크릿에 무제한 만료를 허용하지 않습니다. Braze로의 데이터 흐름을 유지하려면 자격 증명이 만료되기 전에 갱신해야 합니다.
{% endalert %}

#### 2.2단계: Fabric 리소스에 대한 액세스 부여 {#step-22-grant-access-to-fabric-resources}
Braze가 Fabric 인스턴스에 연결할 수 있도록 액세스를 제공합니다. Fabric 관리 포털에서 **Settings** > **Governance and insights** > **Admin portal** > **Tenant settings**로 이동합니다.

* **Developer settings**에서 "Service principals can use Fabric APIs"를 활성화하여 Braze가 Microsoft Entra ID를 사용하여 연결할 수 있도록 합니다.
* **OneLake settings**에서 "Users can access data stored in OneLake with apps external to Fabric"를 활성화하여 서비스 주체가 외부 앱에서 데이터에 액세스할 수 있도록 합니다.

#### 2.3단계: 웨어하우스 연결 문자열 가져오기 {#step-23-get-warehouse-connection-string}

Braze가 연결하려면 웨어하우스의 SQL 엔드포인트가 필요합니다. SQL 엔드포인트를 가져오려면 Fabric의 **작업 영역**으로 이동하고, 항목 목록에서 웨어하우스 이름 위에 마우스를 올린 다음 **Copy SQL connection string**을 선택합니다.
이 값을 3단계의 자격 증명 설정에 사용할 수 있도록 보관하세요.

#### 2.4단계: 방화벽에서 Braze IP 허용(선택 사항) {#step-24-allow-braze-ips-in-firewall-optional}

Microsoft Fabric 계정의 구성에 따라 Braze의 트래픽을 허용하기 위해 방화벽에서 다음 IP 주소를 허용해야 할 수 있습니다. 이를 활성화하는 방법에 대한 자세한 내용은 [Entra 조건부 액세스](https://learn.microsoft.com/en-us/fabric/security/protect-inbound-traffic#entra-conditional-access)에 관한 관련 설명서를 참조하세요.

{% multi_lang_include administer/data_centers.md datacenters='ips' %}

{% endtab %}

{% endtabs %}

### 3단계: Braze 대시보드에서 연결된 소스 생성하기 {#step-3-create-a-connected-source-in-the-braze-dashboard}

{% tabs %}
{% tab Snowflake %}
#### 3.1단계: Snowflake 연결 정보 및 소스 테이블 추가 {#step-31-add-snowflake-connection-information-and-source-table}

Braze 대시보드에서 연결된 소스를 생성합니다. **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**로 이동하여 **Add data source**를 선택한 다음 **Snowflake**를 선택합니다.

**Setup source**에서 다음을 입력합니다:
- **Credentials:** **Account Locator**, **Username**, **Role**
- **Configuration:** **Warehouse**, **Database**, **Schema**

새 Snowflake 자격 증명을 생성하는 경우 연결을 테스트하기 전에 **Save credentials and generate RSA key**를 선택합니다.

#### 3.2단계: 동기화 세부 정보 구성 {#step-32-configure-sync-details}

연결된 소스의 이름을 선택합니다. 이 이름은 새 CDI 세그먼트 확장을 생성할 때 사용 가능한 소스 목록에 표시됩니다.

이 소스의 최대 실행 시간을 구성합니다. Braze는 최대 실행 시간을 초과하는 쿼리를 자동으로 중단합니다. 허용되는 최대 실행 시간은 60분이며, 더 짧은 실행 시간을 설정하면 Snowflake 계정에서 발생하는 비용을 줄일 수 있습니다. 이 설정은 동기화 및 이를 사용하는 CDI 세그먼트 확장을 포함하여 이 소스를 통해 실행되는 쿼리에 적용됩니다.

{% alert note %}
쿼리가 지속적으로 시간 초과되고 최대 실행 시간을 60분으로 설정한 경우, 쿼리 실행 시간을 최적화하거나 Braze 사용자에게 더 큰 웨어하우스를 할당하는 것을 고려하세요.
{% endalert %}

#### 3.3단계: 공개 키 확인 {#step-33-note-the-public-key}

**Test connection** 단계에서 RSA 공개 키를 확인합니다. Snowflake에서 통합을 완료하는 데 이 키가 필요합니다.

{% endtab %}
{% tab Redshift %}
#### 3.1단계: Redshift 연결 정보 및 소스 테이블 추가 {#step-31-add-redshift-connection-information-and-source-table}

Braze 대시보드에서 연결된 소스를 생성합니다. **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**로 이동하여 **Add data source**를 선택한 다음 **Amazon Redshift**를 선택합니다.

**Setup source**에서 다음을 입력합니다:
- **Credentials:** **Redshift Host URL**, **Username**, **Password**, **Port**
- **Configuration:** **Database**, **Schema**

필요한 경우 **Connect with SSH Tunnel**을 활성화하고 **Tunnel Host**, **Tunnel Port**, **Tunnel Username**을 입력합니다.

#### 3.2단계: 동기화 세부 정보 구성

연결된 소스의 이름을 선택합니다. 이 이름은 새 CDI 세그먼트 확장을 생성할 때 사용 가능한 소스 목록에 표시됩니다.

이 소스의 최대 실행 시간을 구성합니다. Braze는 최대 실행 시간을 초과하는 쿼리를 자동으로 중단합니다. 허용되는 최대 실행 시간은 60분이며, 더 짧은 실행 시간을 설정하면 Redshift 계정에서 발생하는 비용을 줄일 수 있습니다.
이 설정은 동기화 및 이를 사용하는 CDI 세그먼트 확장을 포함하여 이 소스를 통해 실행되는 쿼리에 적용됩니다.

{% alert note %}
쿼리가 지속적으로 시간 초과되고 최대 실행 시간을 60분으로 설정한 경우, 쿼리 실행 시간을 최적화하거나 Braze 사용자에게 더 큰 웨어하우스를 할당하는 것을 고려하세요.
{% endalert %}

#### 3.3단계: 공개 키 확인(선택 사항) {#step-33-note-the-public-key-optional}

자격 증명에 **Connect with SSH Tunnel**이 선택되어 있는 경우, **Test connection** 단계에서 RSA 공개 키를 확인합니다. Redshift에서 통합을 완료하는 데 이 키가 필요합니다.

{% endtab %}
{% tab BigQuery %}
#### 3.1단계: BigQuery 연결 정보 및 소스 테이블 추가 {#step-31-add-bigquery-connection-information-and-source-table}

Braze 대시보드에서 연결된 소스를 생성합니다. **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**로 이동하여 **Add data source**를 선택한 다음 **Google BigQuery**를 선택합니다.

**Setup source**에서 다음을 입력합니다:
- **Credentials:** **Credential name** 및 **JSON key** 업로드
- **Configuration:** **Project**, **Dataset**

#### 3.2단계: 동기화 세부 정보 구성

연결된 소스의 이름을 선택합니다. 이 이름은 새 CDI 세그먼트 확장을 생성할 때 사용 가능한 소스 목록에 표시됩니다.

이 소스의 최대 실행 시간을 구성합니다. Braze는 최대 실행 시간을 초과하는 쿼리를 자동으로 중단합니다. 허용되는 최대 실행 시간은 60분이며, 더 짧은 실행 시간을 설정하면 BigQuery 계정에서 발생하는 비용을 줄일 수 있습니다. 이 설정은 동기화 및 이를 사용하는 CDI 세그먼트 확장을 포함하여 이 소스를 통해 실행되는 쿼리에 적용됩니다.

{% alert note %}
쿼리가 지속적으로 시간 초과되고 최대 실행 시간을 60분으로 설정한 경우, 쿼리 실행 시간을 최적화하거나 Braze 사용자에게 더 큰 웨어하우스를 할당하는 것을 고려하세요.
{% endalert %}

#### 3.3단계: 연결 테스트 {#step-33-test-the-connection}

**Test Connection**을 선택하여 사용자에게 표시되는 테이블 목록이 예상과 일치하는지 확인한 다음 **Done**을 선택합니다. 연결된 소스가 생성되었으며 CDI 세그먼트 확장에서 사용할 준비가 되었습니다.

{% endtab %}
{% tab Databricks %}
#### 3.1단계: Databricks 연결 정보 및 소스 테이블 추가 {#step-31-add-databricks-connection-information-and-source-table}

Braze 대시보드에서 연결된 소스를 생성합니다. **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**로 이동하여 **Add data source**를 선택한 다음 **Databricks**를 선택합니다.

**Setup source**에서 다음을 입력합니다:
- **Credentials:** **Credential Name**, **Hostname**, **HTTP Path**, **Access Token**
- **Configuration:** **Catalog**, **Schema**

#### 3.2단계: 동기화 세부 정보 구성

연결된 소스의 이름을 선택합니다. 이 이름은 새 CDI 세그먼트 확장을 생성할 때 사용 가능한 소스 목록에 표시됩니다.

이 소스의 최대 실행 시간을 구성합니다. Braze는 최대 실행 시간을 초과하는 쿼리를 자동으로 중단합니다. 허용되는 최대 실행 시간은 60분이며, 더 짧은 실행 시간을 설정하면 Databricks 계정에서 발생하는 비용을 줄일 수 있습니다. 이 설정은 동기화 및 이를 사용하는 CDI 세그먼트 확장을 포함하여 이 소스를 통해 실행되는 쿼리에 적용됩니다.

{% alert note %}
쿼리가 지속적으로 시간 초과되고 최대 실행 시간을 60분으로 설정한 경우, 쿼리 실행 시간을 최적화하거나 Braze 사용자에게 더 큰 웨어하우스를 할당하는 것을 고려하세요.
{% endalert %}

#### 3.3단계: 연결 테스트

**Test Connection**을 선택하여 사용자에게 표시되는 테이블 목록이 예상과 일치하는지 확인한 다음 **Done**을 선택합니다. 연결된 소스가 생성되었으며 CDI 세그먼트 확장에서 사용할 준비가 되었습니다.

{% endtab %}
{% tab Microsoft Fabric %}
#### 3.1단계: Microsoft Fabric 연결 정보 및 소스 테이블 추가 {#step-31-add-microsoft-fabric-connection-information-and-source-table}

Braze 대시보드에서 연결된 소스를 생성합니다. **Data Settings** > **Cloud Data Ingestion** > **Connected Sources**로 이동하여 **Add data source**를 선택한 다음 **Microsoft Fabric**을 선택합니다.

**Setup source**에서 다음을 입력합니다:
- **Credentials:** **Credentials Name**, **Tenant ID**, **Principal ID**, **Client Secret**, **Connection String**
- **Configuration:** **Database**, **Schema**

워크스페이스에서 **Connect with SSH Tunnel**을 사용할 수 있고 설정에 필요한 경우, **Tunnel Host**, **Tunnel Port**, **Tunnel Username**도 입력합니다.

#### 3.2단계: 동기화 세부 정보 구성

연결된 소스의 이름을 선택합니다. 이 이름은 새 CDI 세그먼트 확장을 생성할 때 사용 가능한 소스 목록에 표시됩니다.

이 소스의 최대 실행 시간을 구성합니다. Braze는 최대 실행 시간을 초과하는 쿼리를 자동으로 중단합니다. 허용되는 최대 실행 시간은 60분이며, 더 짧은 실행 시간을 설정하면 Microsoft Fabric 계정에서 발생하는 비용을 줄일 수 있습니다. 이 설정은 동기화 및 이를 사용하는 CDI 세그먼트 확장을 포함하여 이 소스를 통해 실행되는 쿼리에 적용됩니다.

{% alert note %}
쿼리가 지속적으로 시간 초과되고 최대 실행 시간을 60분으로 설정한 경우, 쿼리 실행 시간을 최적화하거나 Fabric 용량을 확장하는 것을 고려하세요.
{% endalert %}

#### 3.3단계: 연결 테스트

**Test Connection**을 선택하여 사용자에게 표시되는 테이블 목록이 예상과 일치하는지 확인한 다음 **Done**을 선택합니다. 연결된 소스가 생성되었으며 CDI 세그먼트 확장에서 사용할 준비가 되었습니다.

{% endtab %}
{% endtabs %}

### 4단계: 데이터 웨어하우스 구성 완료하기 {#step-4-finalize-the-data-warehouse-configuration}

{% tabs %}
{% tab Snowflake %}
마지막 단계에서 확인한 공개 키를 Snowflake의 사용자에 추가합니다. 이를 통해 Braze가 Snowflake에 연결할 수 있습니다. 이 방법에 대한 자세한 내용은 [Snowflake 설명서](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)를 참조하세요.

키를 언제든지 교체하려면 **Cloud Data Ingestion**의 **Data Access Management**로 이동하여 해당 계정에 대해 **Generate New Key**를 선택하면 새 공개 키를 생성할 수 있습니다.

```sql
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='{INSERT_YOUR_KEY}';
```

Snowflake의 사용자에 키를 추가한 후 Braze에서 **Test Connection**을 선택한 다음 **Done**을 선택합니다. 연결된 소스가 생성되었으며 CDI 세그먼트 확장에서 사용할 준비가 되었습니다.
{% endtab %}

{% tab Redshift %}
SSH 터널로 연결하는 경우, 마지막 단계에서 확인한 공개 키를 SSH 터널 사용자에 추가합니다.

사용자에 키를 추가한 후 Braze에서 **Test Connection**을 선택한 다음 **Done**을 선택합니다. 연결된 소스가 생성되었으며 CDI 세그먼트 확장에서 사용할 준비가 되었습니다.

{% endtab %}
{% tab BigQuery %}
BigQuery에는 해당되지 않습니다.

{% endtab %}
{% tab Databricks %}
Databricks에는 해당되지 않습니다.

{% endtab %}
{% tab Microsoft Fabric %}
Microsoft Fabric에는 해당되지 않습니다.

{% endtab %}
{% endtabs %}

{% alert note %}
소스가 "초안" 상태에서 "활성" 상태로 전환되려면 먼저 테스트에 성공해야 합니다. 생성 페이지를 닫아야 하는 경우 통합이 저장되며, 세부 정보 페이지를 다시 방문하여 변경하고 테스트할 수 있습니다.
{% endalert %}

## 추가 통합 또는 사용자 설정(선택 사항) {#setting-up-additional-integrations-or-users-optional}

{% tabs %}
{% tab Snowflake %}
Braze와 여러 통합을 설정할 수 있지만, 각 통합은 서로 다른 스키마에 연결되도록 구성해야 합니다. 추가 연결을 생성할 때 동일한 Snowflake 계정에 연결하는 경우 기존 자격 증명을 재사용할 수 있습니다.

통합 간에 동일한 사용자와 역할을 재사용하는 경우 공개 키를 다시 추가할 필요가 없습니다.
{% endtab %}

{% tab Redshift %}
Braze와 여러 소스를 설정할 수 있지만, 각 소스는 서로 다른 스키마에 연결되도록 구성해야 합니다. 추가 소스를 생성할 때 동일한 Redshift 계정에 연결하는 경우 기존 자격 증명을 재사용할 수 있습니다.
{% endtab %}

{% tab BigQuery %}
Braze와 여러 소스를 설정할 수 있지만, 각 소스는 서로 다른 데이터셋에 연결되도록 구성해야 합니다. 추가 소스를 생성할 때 동일한 BigQuery 계정에 연결하는 경우 기존 자격 증명을 재사용할 수 있습니다.
{% endtab %}

{% tab Databricks %}
Braze와 여러 소스를 설정할 수 있지만, 각 소스는 서로 다른 스키마에 연결되도록 구성해야 합니다. 추가 소스를 생성할 때 동일한 Databricks 계정에 연결하는 경우 기존 자격 증명을 재사용할 수 있습니다.
{% endtab %}

{% tab Microsoft Fabric %}
Braze와 여러 소스를 설정할 수 있지만, 각 소스는 서로 다른 스키마에 연결되도록 구성해야 합니다. 추가 소스를 생성할 때 동일한 Azure 계정에 연결하는 경우 기존 자격 증명을 재사용할 수 있습니다.
{% endtab %}
{% endtabs %}

## 연결된 소스 사용하기 {#using-the-connected-source}

소스가 생성되면 이를 사용하여 하나 이상의 CDI 세그먼트 확장을 만들 수 있습니다. 이 소스로 세그먼트를 만드는 방법에 대한 자세한 내용은 [CDI 세그먼트 확장 설명서]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments)를 참조하세요.

{% alert note %}
쿼리가 지속적으로 시간 초과되고 최대 런타임을 60분으로 설정한 경우, 쿼리 실행 시간을 최적화하거나 Braze 사용자에게 더 많은 컴퓨팅 리소스(예: 더 큰 데이터 웨어하우스)를 할당하는 것을 고려해 보세요.
{% endalert %}