---
nav_title: 클라우드 데이터 수집
article_title: Braze 클라우드 데이터 수집
alias: /cloud_ingestion/
description: "이 참조 문서에서는 Braze 클라우드 데이터 수집 소스 및 데이터 설정 권장 사항을 다룹니다."
page_order: 1
toc_headers: h2
---

# Braze 클라우드 데이터 수집 {#braze-cloud-data-ingestion}

> Braze 클라우드 데이터 수집(CDI)을 사용하면 데이터 저장 솔루션에서 Braze로 직접 연결을 설정하여 관련 사용자 데이터 및 기타 비사용자 데이터를 동기화할 수 있습니다. 이 데이터는 개인화 또는 세분화에 사용되어 마케팅 사용 사례를 지원할 수 있습니다. 클라우드 데이터 수집의 유연한 통합은 중첩된 JSON 및 오브젝트 배열을 포함한 복잡한 데이터 구조를 지원합니다.

## 작동 방식 {#how-it-works}

Braze 클라우드 데이터 수집(CDI)을 사용하면 데이터 웨어하우스 인스턴스와 Braze 워크스페이스 간의 통합을 설정하여 반복적으로 데이터를 동기화할 수 있습니다. 이 동기화는 설정한 스케줄에 따라 실행되며, 각 통합마다 다른 스케줄을 설정할 수 있습니다. 동기화는 15분마다 자주 실행하거나 한 달에 한 번만 실행하도록 설정할 수 있습니다. 15분보다 더 자주 동기화해야 하는 경우 고객 성공 매니저에게 문의하거나 실시간 데이터 수집을 위해 REST API 호출 사용을 고려하세요.

Amazon S3 파일 스토리지 통합은 이벤트 기반입니다. Braze는 S3/SQS 알림이 도착하면 새 파일을 수집합니다. 설정에 대한 자세한 내용은 [파일 스토리지 통합]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations)을 참조하세요.

{% alert note %}
대시보드의 동기화 빈도는 Braze가 동기화를 실행하는 주기를 제어합니다(예: 매시간 또는 한 시간 내에 더 자주 실행하는 옵션). 실행 간 1시간보다 긴 커스텀 간격을 설정하는 것은 아닙니다. 예약된 주기 외에 동기화를 실행하려면(예: 웨어하우스 로드가 완료된 후 온디맨드로 실행) 통합 ID와 함께 [동기화 트리거]({{site.baseurl}}/api/endpoints/cdi/post_job_sync) 엔드포인트를 사용하세요.
{% endalert %}

동기화가 실행되면 Braze는 데이터 웨어하우스 인스턴스에 직접 연결하여 지정된 테이블에서 모든 새 데이터를 검색하고 Braze 대시보드에서 해당 데이터를 업데이트합니다. 동기화가 실행될 때마다 업데이트된 데이터가 Braze에 반영됩니다.

### 통합 ID 찾기 {#finding-your-integration-id}

Braze 대시보드에서 통합을 조회할 때 URL에서 통합 ID를 찾을 수 있습니다. **Data Settings** > **Cloud Data Ingestion**으로 이동하여 통합을 선택하세요. 통합 ID는 URL에서 `https://[instance].braze.com/integrations/cloud_data_ingestion/[integration_id]` 형식으로 표시됩니다. 예를 들어 URL이 `https://dashboard-01.braze.com/integrations/cloud_data_ingestion/abc123xyz`인 경우 통합 ID는 `abc123xyz`입니다. 이 ID를 사용하여 동기화를 트리거하거나 동기화 상태를 확인하는 API 호출을 할 수 있습니다.

## 사용 사례 {#use-cases}

Braze 클라우드 데이터 수집 기능을 사용하면 다음을 수행할 수 있습니다:

- 데이터 웨어하우스 또는 파일 스토리지 솔루션에서 Braze로의 간단한 통합을 몇 분 만에 직접 생성할 수 있습니다.
- 속성, 이벤트, 구매를 포함한 사용자 데이터를 데이터 웨어하우스에서 Braze로 안전하게 동기화할 수 있습니다.
- 클라우드 데이터 수집을 Currents 또는 Snowflake 데이터 공유와 결합하여 데이터 루프를 완성할 수 있습니다.

또한, [연결된 소스]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources)는 제로 복사 대안입니다. Braze가 데이터 웨어하우스 또는 파일 스토리지 솔루션에 직접 쿼리하여 CDI 세그먼트를 구성할 수 있으며&#8212;기본 데이터를 Braze에 복사하지 않아도 됩니다.

## 지원되는 데이터 소스 {#supported-data-sources}

클라우드 데이터 수집은 다음 소스에서 데이터를 동기화할 수 있습니다:

   - Amazon Redshift
   - Databricks
   - Google BigQuery
   - Microsoft Fabric
   - Snowflake
   - Amazon S3

## 지원되는 데이터 유형 {#supported-data-types}

클라우드 데이터 수집은 다음 데이터 유형을 지원합니다:

### 사용자 데이터 {#user-data}
- 사용자 속성, 포함:
   - 중첩 커스텀 속성
   - 오브젝트 배열
   - 구독 상태
- 커스텀 이벤트
- 구매 이벤트
- 사용자 삭제 요청

### 비사용자 오브젝트 {#non-user-objects}
- 카탈로그 항목

### 제로 카피 메시징 {#zero-copy-messaging}
- 연결된 소스

## 클라우드 데이터 수집을 위한 사용자 식별자 {#user-identifiers-for-data-ingestion}

클라우드 데이터 수집을 통해 사용자 데이터를 동기화할 때, 다음 식별자 유형 중 하나 이상을 사용하여 사용자를 식별할 수 있습니다. 소스 테이블의 각 행에는 한 번에 하나의 식별자 유형에 대한 값만 포함되어야 하지만, 테이블에는 하나, 둘, 셋, 넷 또는 다섯 가지 식별자 유형 모두에 대한 열이 포함될 수 있습니다.

| 식별자 | 설명 |
|------------|-------------|
| `EXTERNAL_ID` | 생성하거나 업데이트할 고객 프로필을 식별하는 외부 ID입니다. Braze에서 사용하는 `external_id` 값과 일치해야 합니다. |
| `ALIAS_NAME` 및 `ALIAS_LABEL` | 이 두 열은 사용자 별칭 오브젝트를 생성합니다. `alias_name`은 고유 식별자여야 하며, `alias_label`은 별칭의 유형을 지정합니다. 사용자는 서로 다른 레이블로 여러 별칭을 가질 수 있지만, `alias_label`당 하나의 `alias_name`만 가질 수 있습니다. |
| `BRAZE_ID` | Braze SDK에서 생성된 Braze 사용자 식별자입니다. 클라우드 데이터 수집을 통해 Braze ID로 새 사용자를 생성할 수 없습니다. 새 사용자를 생성하려면 외부 ID 또는 사용자 별칭을 지정하세요. |
| `EMAIL` | 사용자의 이메일 주소입니다. 동일한 이메일 주소를 가진 프로필이 여러 개 존재하는 경우, 가장 최근에 업데이트된 프로필이 업데이트 대상으로 우선 적용됩니다. 이메일과 전화번호를 모두 포함하면 이메일이 기본 식별자로 사용됩니다. |
| `PHONE` | 사용자의 전화번호입니다. 동일한 전화번호를 가진 프로필이 여러 개 존재하는 경우, 가장 최근에 업데이트된 프로필이 업데이트 대상으로 우선 적용됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="클라우드 데이터 수집을 위한 사용자 식별자" }

테이블 열 구성 및 페이로드 형식 요구 사항에 대한 자세한 내용은 [클라우드 데이터 수집을 위한 테이블 설정]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/table_setup)을 참조하세요.

소스별 설정 지침 및 SQL 예시는 [데이터 웨어하우스 통합]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations)을 참조하세요.

## 데이터 포인트 사용량 {#data-point-usage}

데이터 포인트 기반 요금제를 사용하는 고객의 경우, 클라우드 데이터 수집에 대한 데이터 포인트 과금은 [`/users/track` 엔드포인트]({{site.baseurl}}/api/endpoints/user_data/post_user_track)를 통한 업데이트 과금과 동일합니다. 자세한 내용은 [데이터 포인트]({{site.baseurl}}/user_guide/data/infrastructure/data_points)를 참조하세요.

{% alert important %}
Braze 클라우드 데이터 수집은 사용 가능한 사용량 제한에 포함되므로, 다른 방법으로도 데이터를 전송하고 있다면 Braze API와 클라우드 데이터 수집 간에 사용량 제한이 합산됩니다.
{% endalert %}

## 제품 제한 사항 {#product-limitations}

| 제한 사항            | 설명                                                                                                                                                                        |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 통합 수 | 설정할 수 있는 통합 수에는 제한이 없습니다. 그러나 테이블 또는 뷰당 하나의 통합만 설정할 수 있습니다.                                             |
| 행 수         | 기본적으로 각 실행은 최대 5억 개의 행을 동기화할 수 있습니다. 5억 개 이상의 새 행이 포함된 동기화는 중단됩니다. 이보다 더 높은 제한이 필요한 경우 Braze 고객 성공 매니저 또는 Braze 지원팀에 문의하세요. |
| 행당 속성 수     | 각 행에는 하나의 사용자 ID와 최대 250개의 속성이 포함된 JSON 오브젝트가 있어야 합니다. JSON 오브젝트의 각 키는 하나의 속성으로 계산됩니다(즉, 배열은 하나의 속성으로 계산됩니다). |
| 페이로드 크기           | 각 행에는 최대 1MB의 페이로드가 포함될 수 있습니다. 1MB를 초과하는 페이로드는 거부되며, "Payload was greater than 1MB" 오류가 관련 외부 ID 및 잘린 페이로드와 함께 동기화 로그에 기록됩니다. |
| 데이터 유형              | 클라우드 데이터 수집을 통해 사용자 속성, 이벤트 및 구매를 동기화할 수 있습니다.                                                                                                  |
| Braze 리전           | 이 제품은 모든 Braze 리전에서 사용할 수 있습니다. 모든 Braze 리전은 모든 소스 데이터 리전에 연결할 수 있습니다.                                                                              |
| 소스 리전       | Braze는 모든 리전 또는 클라우드 공급자의 데이터 웨어하우스 또는 클라우드 환경에 연결됩니다.                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 aria-label="제품 제한 사항" }