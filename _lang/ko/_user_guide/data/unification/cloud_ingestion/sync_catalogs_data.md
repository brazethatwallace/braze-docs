---
nav_title: 카탈로그 데이터 동기화 및 삭제
article_title: 카탈로그 데이터 동기화 및 삭제
page_order: 6
page_type: reference
description: "이 페이지에서는 카탈로그 데이터를 동기화하는 방법에 대한 개요를 제공합니다."

---

# 카탈로그 데이터 동기화 및 삭제 {#sync-and-delete-catalog-data}

> 이 페이지에서는 카탈로그 데이터를 동기화하는 방법에 대해 설명합니다.

## 1단계: 새 카탈로그 만들기 {#step-1-create-a-new-catalog}

[카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs)를 위한 새 클라우드 데이터 수집(CDI) 통합을 만들기 전에 새 카탈로그를 만들거나 통합에 사용할 기존 카탈로그를 식별해야 합니다. 새 카탈로그를 만드는 방법에는 여러 가지가 있으며, 이 중 어떤 방법이든 CDI 통합에 사용할 수 있습니다.
- [CSV]({{site.baseurl}}/user_guide/data/activation/catalogs/create) 업로드
- [Braze 대시보드]({{site.baseurl}}/user_guide/data/activation/catalogs/create)에서 또는 CDI 설정 중에 카탈로그 만들기
- [카탈로그 생성 엔드포인트]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog)를 사용하여 카탈로그 만들기

카탈로그 스키마에 대한 모든 변경 사항(예: 새 필드 추가 또는 필드 유형 변경)은 업데이트된 데이터가 CDI를 통해 동기화되기 전에 카탈로그 대시보드에서 수행해야 합니다. 데이터 웨어하우스 데이터와 Braze의 스키마 간 충돌을 방지하기 위해 동기화가 일시 중지되었거나 실행이 예정되지 않은 시점에 이러한 업데이트를 수행하는 것을 권장합니다.

## 2단계: 클라우드 데이터 수집과 카탈로그 데이터 통합 {#step-2-integrate-cloud-data-ingestion-with-catalog-data}
카탈로그 동기화 설정은 [사용자 데이터 CDI 통합]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations) 프로세스와 거의 동일합니다.

{% tabs %}
{% tab Snowflake %}

1. Snowflake에서 소스 테이블을 설정합니다. 다음 예시의 이름을 사용하거나 직접 데이터베이스, 스키마, 테이블 이름을 선택할 수 있습니다. 테이블 대신 뷰 또는 구체화된 뷰를 사용할 수도 있습니다.
  ```sql
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC (
         UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
         --ID of the catalog item to be created or updated
         ID VARCHAR(16777216) NOT NULL,
         --Catalog fields and values that should be added or updated
         PAYLOAD VARCHAR(16777216) NOT NULL,
         --The catalog item associated with this ID should be deleted
         DELETED BOOLEAN
    );
    ```
2. 역할, 웨어하우스, 사용자를 설정하고 적절한 권한을 부여합니다. 기존 동기화에서 사용하던 자격 증명이 있으면 재사용할 수 있지만, 카탈로그 소스 테이블에 대한 접근 권한을 확장해야 합니다.
    ```sql
    CREATE ROLE BRAZE_INGESTION_ROLE;

    GRANT USAGE ON DATABASE BRAZE_CLOUD_PRODUCTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION TO ROLE BRAZE_INGESTION_ROLE;
    GRANT SELECT ON TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC TO ROLE BRAZE_INGESTION_ROLE;

    CREATE WAREHOUSE BRAZE_INGESTION_WAREHOUSE;
    GRANT USAGE ON WAREHOUSE BRAZE_INGESTION_WAREHOUSE TO ROLE BRAZE_INGESTION_ROLE;

    CREATE USER BRAZE_INGESTION_USER;
    GRANT ROLE BRAZE_INGESTION_ROLE TO USER BRAZE_INGESTION_USER;
    ```
3. Snowflake 계정에 네트워크 정책이 있는 경우, CDI 서비스가 연결할 수 있도록 Braze IP를 허용 목록에 추가합니다. IP 목록은 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)을 참조하세요.
4. Braze 대시보드에서 **기술 파트너** > **Snowflake**로 이동하여 새 동기화를 만듭니다.
5. 연결 정보(또는 기존 자격 증명을 재사용)와 소스 테이블을 입력합니다.
6. 설정 흐름의 2단계로 진행하여 "Catalogs" 동기화 유형을 선택하고 통합 이름과 스케줄을 입력합니다. 통합 이름은 이전에 만든 카탈로그 이름과 **정확히 일치**해야 합니다.
7. 동기화 빈도를 선택하고 다음 단계로 진행합니다.
8. 대시보드에 표시된 공개 키를 Braze가 Snowflake에 연결하기 위해 만든 사용자에게 추가합니다. 이 단계를 완료하려면 Snowflake에서 `SECURITYADMIN` 이상의 접근 권한을 가진 사용자가 필요합니다.
9. **연결 테스트**를 선택하여 모든 것이 정상적으로 작동하는지 확인합니다.
10. 동기화를 저장하고, 동기화된 카탈로그 데이터를 모든 개인화 사용 사례에 활용합니다.
{% endtab %}
{% tab Redshift %}

1. Redshift에서 소스 테이블을 설정합니다. 다음 예시의 이름을 사용하거나 직접 데이터베이스, 스키마, 테이블 이름을 선택할 수 있습니다. 테이블 대신 뷰 또는 구체화된 뷰를 사용할 수도 있습니다.
    ```sql
    CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
    CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
    CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC (
       updated_at timestamptz default sysdate not null,
       --ID of the catalog item to be created or updated
       id varchar not null,
       --Catalog fields and values that should be added or updated
       payload varchar(max),
       --The catalog item associated with this ID should be deleted
       deleted boolean
    )
    ```
2. 사용자를 설정하고 적절한 권한을 부여합니다. 기존 동기화에서 사용하던 자격 증명이 있으면 재사용할 수 있지만, 카탈로그 소스 테이블에 대한 접근 권한을 확장해야 합니다.
    {% raw %}
    ```sql
    CREATE USER braze_user PASSWORD '{password}';
    GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
    GRANT SELECT ON TABLE CATALOGS_SYNC TO braze_user;
    ```
    {% endraw %}
3. 방화벽이나 기타 네트워크 정책이 있는 경우, Braze가 Redshift 인스턴스에 네트워크로 접근할 수 있도록 허용해야 합니다. Braze 대시보드 지역에 해당하는 다음 IP의 접근을 허용합니다. IP 목록은 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)을 참조하세요.

{% endtab %}
{% tab BigQuery %}

1. 선택적으로, 소스 테이블을 저장할 새 프로젝트 또는 데이터셋을 설정합니다.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

다음 필드를 사용하여 CDI 통합에 사용할 테이블을 하나 이상 만듭니다:

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CATALOGS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp,
  id STRING,
  payload JSON,
  deleted BOOLEAN
);
```

| 필드 이름 | 유형 | 모드 |
| --- | --- | --- |
| UPDATED_AT | TIMESTAMP | REQUIRED |
| PAYLOAD | JSON | REQUIRED |
| ID | STRING | REQUIRED |
| DELETED | BOOLEAN | OPTIONAL |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="2단계: 클라우드 데이터 수집과 카탈로그 데이터 통합" }

{:start="2"}

2. 사용자를 설정하고 적절한 권한을 부여합니다. 기존 동기화에서 사용하던 자격 증명이 있으면 재사용할 수 있지만, 카탈로그 소스 테이블에 대한 접근 권한을 확장해야 합니다.
서비스 계정에는 다음 섹션의 권한이 있어야 합니다:
- BigQuery Connection User: Braze가 연결을 설정할 수 있습니다.
- BigQuery User: Braze가 쿼리를 실행하고, 데이터셋 메타데이터를 읽고, 테이블을 나열할 수 있습니다.
- BigQuery Data Viewer: Braze가 데이터셋과 그 내용을 볼 수 있습니다.
- BigQuery Job User: Braze가 작업을 실행할 수 있습니다.<br><br>서비스 계정을 만들고 권한을 부여한 후 JSON 키를 생성합니다. 자세한 내용은 [키 생성 및 삭제](https://cloud.google.com/iam/docs/keys-create-delete)를 참조하세요. 이 키는 나중에 Braze 대시보드에 업데이트합니다.

{:start="3"}
3. 네트워크 정책이 있는 경우, Braze가 BigQuery 인스턴스에 네트워크로 접근할 수 있도록 허용해야 합니다. IP 목록은 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)을 참조하세요.

{% endtab %}
{% tab Databricks %}

1. Databricks에서 소스 테이블을 설정합니다. 다음 예시의 이름을 사용하거나 직접 카탈로그, 스키마, 테이블 이름을 선택할 수 있습니다. 테이블 대신 뷰 또는 구체화된 뷰를 사용할 수도 있습니다.

```sql
CREATE SCHEMA BRAZE-CLOUD-PRODUCTION.INGESTION;
```

```sql
CREATE TABLE `BRAZE-CLOUD-PRODUCTION.INGESTION.CATALOGS_SYNC`
(
  updated_at TIMESTAMP DEFAULT current_timestamp(),
  id STRING,
  deleted BOOLEAN,
  payload STRING, STRUCT, or MAP
);
```

| 필드 이름 | 유형 | 모드 |
| --- | --- | --- |
| UPDATED_AT | TIMESTAMP | REQUIRED |
| PAYLOAD | STRING, STRUCT, or MAP | REQUIRED |
| ID | STRING | REQUIRED |
| DELETED | BOOLEAN | NULLABLE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="2단계: 클라우드 데이터 수집과 카탈로그 데이터 통합" }

{:start="2"}

2. Databricks 워크스페이스에서 개인 액세스 토큰을 만듭니다.

- a. Databricks 사용자 이름을 선택한 다음 드롭다운 메뉴에서 **User Settings**를 선택합니다.
- b. **Access tokens** 탭에서 **Generate new token**을 선택합니다.
- c. 이 토큰을 식별하는 데 도움이 되는 코멘트를 입력합니다(예: "Braze CDI").
- d. **Lifetime (days)** 상자를 비워 두어 토큰 수명을 무제한으로 변경합니다. **Generate**를 선택합니다.
- e. 표시된 토큰을 복사한 다음 **Done**을 선택합니다.
- f. Braze 대시보드에서 자격 증명 생성 단계에 입력해야 할 때까지 토큰을 안전한 곳에 보관합니다.

{:start="3"}
3. 네트워크 정책이 있는 경우, Braze가 Databricks 인스턴스에 네트워크로 접근할 수 있도록 허용해야 합니다. IP 목록은 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views) 페이지를 참조하세요.

{% endtab %}
{% tab Microsoft Fabric %}

다음 필드를 사용하여 CDI 통합에 사용할 테이블을 하나 이상 만듭니다:

```sql
CREATE OR ALTER TABLE [warehouse].[schema].[CDI_table_name]
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  ID VARCHAR NOT NULL,
  DELETED BIT
)
GO
```

{:start="2"}

2. 서비스 주체를 설정하고 적절한 권한을 부여합니다. 기존 동기화에서 사용하던 자격 증명이 있으면 재사용할 수 있지만, 카탈로그 소스 테이블에 대한 접근 권한을 확장해야 합니다. 새 서비스 주체 및 자격 증명 생성 방법에 대한 자세한 내용은 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views) 페이지를 참조하세요.

{:start="3"}
3. 네트워크 정책이 있는 경우, Braze가 Microsoft Fabric 인스턴스에 네트워크로 접근할 수 있도록 허용해야 합니다. IP 목록은 [클라우드 데이터 수집]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations#step-1-set-up-tables-or-views)을 참조하세요.

{% endtab %}
{% tab S3 %}
JSON 또는 CSV 형식을 사용하여 S3에 소스 파일을 만듭니다. 각 파일에는 다음 필드가 포함되어야 합니다:

| 필드 | 필수 여부 | 설명 |
| --- | --- | --- |
| `ID` | 예 | 생성하거나 업데이트할 카탈로그 항목의 ID입니다. |
| `PAYLOAD` | 예 | Braze의 카탈로그 항목에 동기화할 필드의 JSON 문자열입니다. |
| `DELETED` | 선택 사항 | `true`로 설정하면 해당 카탈로그 항목이 카탈로그에서 제거됩니다. |
| `UPDATED_AT` | *지원되지 않음* | 파일 스토리지는 `UPDATED_AT` 열을 지원하지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="2단계: 클라우드 데이터 수집과 카탈로그 데이터 통합" }

{% alert note %}
파일 이름은 AWS 규칙을 따라야 하며 고유해야 합니다. 고유성을 보장하려면 타임스탬프를 추가하세요.
{% endalert %}

전체 S3 설정에는 S3 버킷, Amazon SQS 대기줄, AWS IAM 역할 및 정책이 필요합니다. Braze는 동기화가 생성된 후 업로드된 파일만 처리하므로, 수집하려는 기존 파일은 다시 업로드하세요.

전체 S3 설정 흐름은 [파일 스토리지 통합]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations)을 참조하세요. 특히 다음 항목을 확인하세요:

- [AWS에서 클라우드 데이터 수집 설정]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#setting-up-cloud-data-ingestion-in-aws)
- [Braze에서 클라우드 데이터 수집 설정]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#setting-up-cloud-data-ingestion-in-braze)
- [문제 해결]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations#troubleshooting)

일반적인 AWS 측 알림 및 권한 문제에 대해서는 [대상에 이벤트 알림 메시지 게시 권한 부여](https://docs.aws.amazon.com/AmazonS3/latest/userguide/grant-destinations-permissions-to-s3.html)를 참조하세요.

다음 예시는 파일 스토리지에서 카탈로그 데이터를 동기화하기 위한 유효한 JSON 및 CSV 형식을 보여줍니다.

{% subtabs %}
{% subtab JSON 카탈로그 %}
```jsonl
{"id":"85","payload":"{\"product_name\":\"Product 85\",\"price\":85.85}"}
{"id":"86","payload":"{\"product_name\":\"Product 86\",\"price\":86.86}"}
{"id":"1","payload":"{\"product_name\":\"Product 1\",\"price\":1.01}","deleted":true}
```

{% alert important %}
소스 파일의 각 줄에는 유효한 JSON이 포함되어야 하며, 그렇지 않으면 파일이 건너뛰어집니다.
{% endalert %}
{% endsubtab %}
{% subtab 삭제 포함 CSV 카탈로그 %}
```plaintext
ID,PAYLOAD,DELETED
85,"{""product_name"": ""Product 85"", ""price"": 85.85}",false
86,"{""product_name"": ""Product 86"", ""price"": 86.86}",false
1,"{""product_name"": ""Product 1"", ""price"": 1.01}",true
```
{% endsubtab %}
{% subtab 삭제 미포함 CSV 카탈로그 %}
```plaintext
ID,PAYLOAD
85,"{""product_name"": ""Product 85"", ""price"": 85.85}"
86,"{""product_name"": ""Product 86"", ""price"": 86.86}"
```
{% endsubtab %}
{% endsubtabs %}

추가 파일 예시는 [파일 스토리지 통합]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations)을 참조하세요.

{% endtab %}
{% endtabs %}

## 통합 작동 방식 {#how-the-integration-works}

{% alert note %}
이 섹션의 동기화 뷰는 데이터 웨어하우스 통합에만 적용됩니다. S3 파일 스토리지의 경우, Braze는 버킷에 새 파일이 업로드되면 해당 파일을 처리합니다. 자세한 내용은 [파일 스토리지 통합]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations)을 참조하세요.
{% endalert %}

동기화가 실행될 때마다 Braze는 `UPDATED_AT`이 마지막으로 동기화된 값보다 이후인 모든 행을 가져옵니다. 정확히 경계 타임스탬프에 있는 행은 동일한 타임스탬프를 공유하는 새로운 행이 있는 경우 다시 동기화될 수 있습니다. 동기화가 실행될 때마다 완전히 새로고침되는 소스 테이블을 설정하려면 카탈로그 데이터로부터 데이터 웨어하우스에 뷰를 생성하는 것을 권장합니다. 뷰를 사용하면 매번 쿼리를 다시 작성할 필요가 없습니다.

예를 들어, `product_id`와 세 개의 추가 속성이 있는 제품 데이터 테이블(`product_catalog_1`)이 있는 경우, 다음 뷰를 동기화할 수 있습니다:

{% tabs %}
{% tab Snowflake %}
```sql
CREATE VIEW BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    product_id as id,
    TO_JSON(
        OBJECT_CONSTRUCT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    )as PAYLOAD FROM "product_catalog_1";
```
{% endtab %}
{% tab Redshift %}
```sql
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS
SELECT
    CURRENT_TIMESTAMP as UPDATED_AT,
    Product_id as id,
    JSON_SERIALIZE(
        OBJECT (
            'attribute_1',
            attribute_1,
            'attribute_2',
            attribute_2,
            'attribute_3',
            attribute_3)
    ) as PAYLOAD FROM "product_catalog_1";
```
{% endtab %}
{% tab BigQuery %}
```sql
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    product_id as ID,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.product_catalog_1`);
```
{% endtab %}
{% tab Databricks %}
```sql
CREATE view IF NOT EXISTS BRAZE_CLOUD_PRODUCTION.INGESTION.CATALOGS_SYNC AS (SELECT
    last_updated as UPDATED_AT,
    product_id as ID,
    TO_JSON(
      STRUCT(
      attribute_1,
      attribute_2,
      attribute_3,
      )
    ) as PAYLOAD
  FROM `BRAZE_CLOUD_PRODUCTION.INGESTION.product_catalog_1`);
```
{% endtab %}
{% tab Microsoft Fabric %}
```sql
CREATE VIEW [braze].[user_update_example]
AS SELECT
    id as ID,
    CURRENT_TIMESTAMP as UPDATED_AT,
    JSON_OBJECT('attribute_1':attribute_1, 'attribute_2':attribute_2, 'attribute_3':attribute_3, 'attribute_4':attribute_4) as PAYLOAD

FROM [braze].[product_catalog] ;
```
{% endtab %}
{% endtabs %}

- 통합에서 가져온 데이터는 제공된 `id`를 기반으로 대상 카탈로그에서 아이템을 생성하거나 업데이트하는 데 사용됩니다.
- DELETED가 `true`로 설정된 경우, 해당 카탈로그 아이템이 삭제됩니다.
- 동기화는 데이터 포인트를 기록하지 않지만, 동기화된 모든 데이터는 총 카탈로그 사용량에 포함됩니다. 이 사용량은 저장된 총 데이터를 기준으로 측정되므로, 변경된 데이터만 동기화하는 것에 대해 걱정할 필요가 없습니다.