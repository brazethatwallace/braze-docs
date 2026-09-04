---
nav_title: Decisioning Studio 데이터 동기화
article_title: "BrazeAI Decisioning Studio 데이터 동기화"
description: "클라우드 데이터 수집을 사용하여 데이터 웨어하우스 테이블을 BrazeAI Decisioning Studio에 동기화하는 방법을 알아보세요."
page_order: 6.5
page_type: reference
toc_headers: h2
---

# BrazeAI Decisioning Studio 데이터 동기화 {#sync-brazeai-decisioning-studio-data}

> 이 페이지에서는 클라우드 데이터 수집(CDI)을 사용하여 데이터 웨어하우스의 데이터를 BrazeAI Decisioning Studio™에 직접 동기화하는 방법을 다룹니다.

CDI의 Decisioning Studio 대상을 사용하면, CDI가 웨어하우스 데이터를 BrazeAI Decisioning Studio에 직접 동기화할 수도 있습니다. 이러한 동기화의 데이터는 Decisioning Studio에서 활성화에 사용할 수 있지만, 고객 프로필과 Braze 워크스페이스는 변경되지 않습니다.

{% alert important %}
이 기능은 얼리 액세스 단계입니다. 액세스하려면 고객 성공 매니저 또는 계정 매니저에게 문의하세요.
{% endalert %}

## 작동 방식 {#how-it-works}

동기화를 생성할 때 Decisioning Studio를 대상으로 선택하고, 동기화하려는 데이터를 반환하는 SQL 쿼리를 작성합니다. CDI는 설정한 스케줄에 따라 해당 쿼리를 실행하고 결과를 Decisioning Studio 에셋으로 전달합니다. 각 동기화는 단일 에셋에 매핑되므로, 동일한 에셋에 둘 이상의 동기화를 연결할 수 없습니다.

Braze 데이터 플랫폼으로의 동기화와 달리, Decisioning Studio 동기화는 데이터를 고객 프로필, 이벤트 또는 카탈로그에 매핑하지 않습니다.

Decisioning Studio에 데이터를 제공하는 다른 방법은 [데이터 연결]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/connect_data_sources)을 참조하세요.

## 전제 조건 {#prerequisites}

- Braze 및 BrazeAI Decisioning Studio에 대한 액세스.
- 활성화된 클라우드 데이터 수집 데이터 웨어하우스 소스. 아직 설정하지 않은 경우 [데이터 웨어하우스 통합]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations)을 참조하세요.
- 동기화하려는 테이블 또는 뷰.
- 기본 키로 사용할 해당 테이블의 열(또는 열들)과 CDI가 증분 동기화에 사용할 수 있는 타임스탬프 열.

## Decisioning Studio 동기화 생성 {#create-a-decisioning-studio-sync}

### 1단계: 동기화 생성 및 대상 선택 {#step-1-create-the-sync-and-select-the-destination}

1. **Data Settings** > **Cloud Data Ingestion** > **Syncs**로 이동합니다.
2. **Create data sync**를 선택합니다.
3. **Integration Name**을 입력한 다음 **Data sources**에서 소스를 선택합니다.
4. **Destination**에서 **Data destination**을 **BrazeAI Decisioning Studio™**로 설정합니다.
5. **Data category**에서 테이블에 가장 적합한 **Decisioning Studio data** 유형을 선택합니다. **Customer profile**, **Message engagement events**, **Conversion events** 또는 **Other** 중에서 선택합니다. 이는 Decisioning Studio용으로 데이터에 태그를 지정하며, CDI가 행을 처리하는 방식은 변경하지 않습니다.

### 2단계: SQL 쿼리 작성 {#step-2-write-your-sql-query}

**Data definition** 단계에서 동기화하려는 테이블 또는 뷰의 데이터를 반환하는 SQL 쿼리를 작성합니다. 쿼리 결과가 동기화의 스키마가 됩니다.

Source Explorer를 사용하여 사용 가능한 테이블과 뷰를 탐색하거나, AI SQL 생성기를 사용하여 쿼리 작성에 도움을 받을 수 있습니다.

쿼리는 `UPDATED_AT` 열을 반환해야 합니다. CDI는 증분 동기화 및 변경 추적에 `UPDATED_AT`를 사용하기 때문입니다. 각 동기화 실행 시 CDI는 `UPDATED_AT`가 마지막으로 동기화된 값보다 이후인 행만 동기화합니다. 식별한 타임스탬프 열의 이름이 이미 `UPDATED_AT`가 아닌 경우, 쿼리에서 별칭을 지정할 수 있습니다:

```sql
SELECT *, LAST_MODIFIED AS UPDATED_AT FROM my_table
```

`UPDATED_AT`가 증분 동기화를 제어하는 방식(뒤로 이동할 때 발생하는 상황 포함)에 대한 자세한 내용은 [UPDATED_AT 열 이해]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices#understanding-the-updated_at-column)를 참조하세요.

{% alert note %}
`JOIN` 절을 포함한 단일 문, 읽기 전용 쿼리만 지원됩니다. CDI는 읽기 전용 쿼리를 실행하며 기본 테이블을 수정하지 않습니다.
{% endalert %}

### 3단계: 쿼리 미리보기 및 유효성 검사 {#step-3-preview-and-validate-your-query}

**Preview and validate**를 선택하여 쿼리를 실행합니다. **Query preview (first 10 rows)** 섹션에 소스에서 반환된 처음 10개 행과 각 열의 감지된 데이터 유형이 표시되므로, 계속하기 전에 데이터가 올바른지 확인할 수 있습니다.

### 4단계: 기본 키 선택 {#step-4-select-a-primary-key}

모든 Decisioning Studio 동기화에는 기본 키 또는 복합 키(각 행을 고유하게 식별하는 하나 이상의 열)가 필요합니다. 유효성 검사가 성공하면 **Primary key** 드롭다운을 열고 기본 키로 사용할 열을 선택합니다. 여러 열을 선택하면 복합 키가 형성됩니다.

{% alert tip %}
좋은 기본 키는 모든 행에 대해 고유하고, 비어 있지 않으며, 동기화 실행 간에 안정적입니다. `UUID()` 또는 `CURRENT_TIMESTAMP`와 같이 쿼리 시점에 생성되는 값은 중복 또는 누락된 행을 유발할 수 있으므로 피하세요.
{% endalert %}

### 5단계: 알림, 스케줄 설정 및 동기화 생성 {#step-5-set-notifications-schedule-and-create-the-sync}

1. **Notifications** 단계에서 동기화 오류 알림을 받을 **Contact Email(s)**을 하나 이상 입력합니다. **Row Error** 및 **Sync success** 알림도 켤 수 있습니다.
2. **Schedule** 단계에서 **Recurring sync**를 켜면 스케줄에 따라 동기화가 자동으로 실행됩니다. **Recurring sync**를 끄면 대시보드에서 수동으로 트리거하거나 [동기화 트리거]({{site.baseurl}}/api/endpoints/cdi/post_job_sync) 엔드포인트를 통해 트리거할 때만 동기화가 실행됩니다.
3. **Summary**를 검토한 다음 동기화를 생성합니다.

## 동기화 편집 {#editing-a-sync}

기존 동기화를 편집할 때 SQL 쿼리를 변경하면 저장하기 전에 재검증이 필요합니다. 기본 키와 복합 키는 변경할 수 없으며 계속 반환되어야 합니다.

유효한 변경 사항은 다음 동기화 실행 시 적용됩니다.

## 스키마 변경 처리 {#handling-schema-changes}

CDI는 소스 스키마 변경을 추가 방식으로 처리합니다. 매 동기화 실행 시 CDI는 소스 스키마를 기존 Decisioning Studio 에셋과 비교하고, 이미 있는 열은 유지하면서 새 열을 추가합니다.

| 소스 테이블의 변경 사항 | 동기화 동작 |
|---|---|
| 새 열이 추가됨 | CDI가 Decisioning Studio 에셋에 열을 추가합니다. 해당 열이 존재하기 전에 전달된 행은 해당 열에 `null`이 표시됩니다. |
| 열이 제거됨 | CDI가 해당 열 업데이트를 중지하지만, 열과 기존 데이터는 에셋에 남아 있습니다. 다른 열은 계속 동기화됩니다. |
| 열 이름이 변경됨 | 제거된 열과 새 열로 처리됩니다. 원래 열은 에셋에 남아 있고, 새 열이 추가됩니다. |
| 열의 데이터 유형이 변경됨 | CDI가 가능한 경우 값을 변환합니다. 변환할 수 없는 행은 동기화 실행 세부 정보에서 행 오류로 보고됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="스키마 변경 처리" }

CDI가 스키마 변경을 감지하면 동기화 실행 세부 정보와 동기화 편집 페이지에 표시되며, 알림 연락처에 이메일 알림이 전송됩니다. 전달되는 열을 변경하려면 SQL 쿼리를 업데이트하고 재검증하세요.