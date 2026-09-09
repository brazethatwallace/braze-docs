---
nav_title: "데이터 공유"
article_title: Snowflake 데이터 공유
page_order: 0
description: "이 참조 문서에서는 Snowflake 보안 데이터 공유 통합에 대해 다루며, 이를 통해 Snowflake 인스턴스에서 직접 Braze 인게이지먼트 및 Campaign 데이터에 액세스할 수 있습니다."
page_type: partner
search_tag: Partner

---

# [![Braze 학습 과정]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/snowflake-secure-data-sharing-via-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Snowflake 데이터 공유 {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomsnowflake-secure-data-sharing-via-braze-stylefloatrightwidth120pxborder0-classnoimgbordersnowflake-data-sharing}

> Snowflake [보안 데이터 공유](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html)를 사용하면 일반적인 데이터 공급자 관계에서 발생하는 워크플로 마찰이나 지연, 장애 지점, 불필요한 비용에 대한 걱정 없이 Braze가 Snowflake 포털의 데이터에 대한 안전한 액세스를 제공할 수 있습니다. 데이터 공유는 다음 통합을 통해 또는 [Snowflake 리더 계정]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents#snowflake-reader-accounts)을 통해 설정할 수 있습니다.

Snowflake 데이터 공유는 Braze 데이터 배포의 일부입니다. 데이터 배포 옵션에 대한 전체 개요는 [데이터 배포]({{site.baseurl}}/user_guide/data/distribution)를 참조하세요.

{% alert tip %}
**Snowflake 계정 없이도 Snowflake 수준의 데이터에 액세스하고 싶으신가요?**<br>[Snowflake 리더 계정]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents#snowflake-reader-accounts)을 확인해 보세요. 리더 계정을 사용하면 Braze가 계정을 생성하고 데이터를 공유하며, 로그인하여 데이터에 액세스할 수 있는 자격 증명을 제공합니다. 이 경우 모든 데이터 공유 및 사용 요금은 전적으로 Braze에서 처리합니다.
{% endalert %}

## 데이터 배포 권한 {#data-distribution-entitlements}

데이터 배포 권한에 따라 데이터 공유에서 사용할 수 있는 이벤트 유형이 결정됩니다. Braze는 이벤트를 다음 카테고리로 구성합니다.

| 권한 | 이벤트 카테고리 | 설명 | 이벤트 용어집 참고 |
|------------|----------------|-------------|--------------------------|
| **인게이지먼트 이벤트** | 메시지 인게이지먼트 이벤트 | 메시지 발송, 전달, 열람, 클릭, 반송 및 기타 메시징 채널 상호작용과 관련된 이벤트 | [메시지 인게이지먼트 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) |
| **고객 행동 이벤트** | 메시지 인게이지먼트 이벤트 및 고객 행동 이벤트 | 모든 메시지 인게이지먼트 이벤트와 구매, 커스텀 이벤트, 세션, 기여도 및 인앱 사용자 액션과 관련된 이벤트를 포함합니다 | [메시지 인게이지먼트 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), [고객 행동 및 사용자 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) |
| **사용자 프로필 및 속성** | 메시지 인게이지먼트 이벤트, 고객 행동 이벤트 및 사용자 프로필 이벤트 | 메시지 인게이지먼트 이벤트와 고객 행동 이벤트, 그리고 사용자 프로필 및 속성 변경과 관련된 이벤트를 포함합니다 | [메시지 인게이지먼트 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events), [고객 행동 및 사용자 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events), [사용자 프로필 이벤트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/user_profiles_events) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="데이터 배포 권한" }

권한에 포함된 이벤트에 대한 질문이 있으면 Braze 계정 담당자 또는 고객 성공 매니저에게 문의하세요.

## 보안 데이터 공유 정보 {#about-secure-data-sharing}

데이터 공유에서는 계정 간에 실제 데이터가 복사되거나 전송되지 않습니다. 모든 공유는 Snowflake의 고유한 서비스 레이어와 메타데이터 스토어를 통해 이루어집니다. 공유 데이터는 계정에 스토리지를 차지하지 않으므로 월별 데이터 스토리지 요금에 영향을 주지 않는다는 점에서 중요한 개념입니다. **유일한** 비용은 공유 데이터를 쿼리하는 데 사용되는 컴퓨팅 리소스(예: 가상 웨어하우스)에 대한 비용뿐입니다.

또한 Snowflake의 내장 역할 및 권한 기능을 사용하면 Braze에서 공유된 데이터에 대한 접근을 Snowflake 계정 및 해당 데이터에 이미 적용된 접근 제어를 통해 관리하고 통제할 수 있습니다. 자체 데이터와 동일한 방식으로 접근을 제한하고 모니터링할 수 있습니다.

- **인사이트 도출 시간 단축**<br>구축하는 데 몇 주가 걸리는 ETL 프로세스에서 벗어나세요. Braze와 Snowflake의 고유한 아키텍처 덕분에 모든 고객 참여 및 Campaign 데이터가 데이터 레이크에 도착하는 즉시 접근하고 쿼리할 수 있습니다. 데이터가 복사되거나 이동되지 않으므로 가장 관련성 높고 최신의 정보만을 기반으로 고객 경험을 제공할 수 있습니다.
- **데이터 사일로 해소**<br>채널과 플랫폼 전반에 걸쳐 고객에 대한 종합적인 뷰를 구축하세요. 데이터 공유를 통해 Braze 고객 참여 데이터를 기존의 모든 Snowflake 데이터와 결합하는 것이 그 어느 때보다 쉬워지며, 단일하고 신뢰할 수 있는 정보 소스에서 더 풍부한 인사이트를 도출할 수 있습니다.
- **인게이지먼트 수준 비교**<br>Braze 벤치마크를 통해 고객 참여 전략을 최적화하세요. Braze와 Snowflake가 지원하는 이 인터랙티브 도구를 사용하면 브랜드의 인게이지먼트 데이터를 채널, 업종, 기기 플랫폼별 벤치마크와 비교할 수 있습니다.

Snowflake의 데이터 공유에 대해 더 자세히 알아보려면 [보안 데이터 공유 소개](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work)를 참조하세요.

## 전제 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Braze 액세스 | 데이터 공유를 설정하려면 Braze 계정 담당자 또는 고객 성공 매니저에게 문의하세요. |
| Snowflake 계정 | `admin` 권한이 있는 Snowflake 계정이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="전제 조건" }

## 보안 데이터 공유 설정 {#setting-up-secure-data-sharing}

Snowflake에서 데이터 공유는 [데이터 제공자](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers)와 [데이터 소비자](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers) 간에 이루어집니다. 이 맥락에서 Braze 계정은 데이터 공유를 생성하고 전송하므로 데이터 제공자 역할을 하며, Snowflake 계정은 데이터 공유를 사용하여 데이터베이스를 생성하므로 데이터 소비자 역할을 합니다. 자세한 내용은 [Snowflake: 공유 데이터 소비](https://docs.snowflake.com/en/user-guide/data-share-consumers)를 참조하세요.

### 1단계: Braze에서 데이터 공유 전송 {#step-1-send-the-datashare-from-braze}

{% multi_lang_include partners/snowflake/data_sharing_account_steps.md %}

### 2단계: Snowflake에서 데이터베이스 생성 {#step-2-create-the-database-in-snowflake}

1. 몇 분 후 Snowflake 계정에서 인바운드 데이터 공유를 수신할 수 있습니다.
2. 인바운드 데이터 공유를 사용하여 테이블을 조회하고 쿼리할 데이터베이스를 생성합니다. 예시:
    {% raw %}
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
    {% endraw %}
3. 새 데이터베이스에 쿼리할 수 있는 권한을 부여합니다.

{% alert warning %}
Braze 대시보드에서 공유를 삭제하고 다시 생성하는 경우, 이전에 생성한 데이터베이스를 삭제하고 `CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>`을 사용하여 다시 생성해야 인바운드 공유를 쿼리할 수 있습니다.
동일한 Snowflake 계정에 데이터를 공유하는 워크스페이스가 여러 개인 경우, 다중 워크스페이스 구성 관리에 대한 안내는 [Snowflake 데이터 공유 FAQ]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs)를 참조하세요.
{% endalert %}

## 사용법 및 시각화 {#usage-and-visualization}

데이터 공유가 프로비저닝된 후, 수신된 데이터 공유에서 데이터베이스를 생성하면 공유된 모든 테이블이 Snowflake 인스턴스에 표시되어 인스턴스에 저장하고 있는 다른 데이터와 마찬가지로 쿼리할 수 있습니다. 다만, 공유 데이터는 읽기 전용이며 쿼리만 가능하고 어떤 방식으로도 수정하거나 삭제할 수 없다는 점에 유의하세요.

Currents와 마찬가지로 Snowflake 보안 데이터 공유를 사용하여 다음을 수행할 수 있습니다:

{% multi_lang_include partners/data_sharing_use_cases.md %}

[원시 테이블 스키마를 다운로드하세요.](/docs/assets/download_file/data-sharing-raw-table-schemas.txt)

{% alert note %}
원시 스키마 다운로드에는 고객 프로필 속성 뷰가 포함되지 않습니다. `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`, `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` 및 관련 사용자 속성 뷰의 전체 스키마와 사용 가이드는 [고객 프로필 속성]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes)을 참조하세요.
{% endalert %}

### 사용자 ID 스키마 {#user-id-schema}

사용자 ID에 대한 Braze와 Snowflake 명명 규칙의 다음 차이점에 유의하세요.

| Braze 스키마 | Snowflake 스키마 | 설명 |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Braze에서 자동으로 할당하는 고유 식별자입니다. |
| `external_id` | `"EXTERNAL_USER_ID"` | 고객이 설정한 사용자 프로필의 고유 식별자입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사용자 ID 스키마" }

## 중요 정보 및 제한 사항 {#important-information-and-limitations}

### 파괴적 변경 vs 비파괴적 변경 {#breaking-versus-non-breaking-changes}

#### 비파괴적 변경 {#non-breaking-changes}

{% multi_lang_include partners/snowflake/non_breaking_changes.md %}

{% alert important %}
새 열은 비파괴적 변경으로 간주되므로, Braze에서는 `SELECT *` 쿼리를 사용하는 대신 각 쿼리에서 관심 있는 열을 명시적으로 나열할 것을 강력히 권장합니다. 또는 열을 명시적으로 지정하는 뷰를 생성한 후, 테이블을 직접 쿼리하는 대신 해당 뷰를 쿼리하는 방법도 있습니다.
{% endalert %}

#### 파괴적 변경 {#breaking-changes}

{% multi_lang_include partners/snowflake/breaking_changes.md %}

### Snowflake 리전 {#snowflake-regions}

Braze는 현재 모든 사용자 수준 데이터를 다음 Snowflake AWS 리전에서 호스팅하고 있습니다:

 - US East-1
 - EU-Central (Frankfurt)
 - AP-Northeast-1 (Tokyo)
 - AP-Southeast-2 (Sydney)
 - AP-Southeast-3 (Jakarta)

해당 리전 외부의 사용자에 대해서는, Braze가 AWS, Azure 또는 GCP 리전에서 Snowflake 인프라를 호스팅하는 공동 고객에게 데이터 공유를 제공할 수 있습니다.

### 데이터 보존 {#data-retention}

#### 보존 정책 {#retention-policy}

2년이 지난 데이터는 아카이브되어 장기 스토리지로 이동됩니다. 아카이브 프로세스의 일환으로 모든 이벤트는 익명화되며, 개인 식별 정보(PII)에 해당하는 민감한 필드는 제거됩니다(`properties`와 같은 선택적 PII 필드 포함). 아카이브된 데이터에는 여전히 `user_id` 필드가 포함되어 있어 모든 이벤트 데이터에 걸쳐 사용자별 분석이 가능합니다.

각 이벤트에 대해 해당 `USERS_*_SHARED` 뷰에서 최근 2년간의 데이터를 쿼리할 수 있습니다. 또한 각 이벤트에는 `USERS_*_SHARED_ALL` 뷰가 있으며, 이를 통해 익명화된 데이터와 비익명화된 데이터를 모두 반환하는 쿼리를 실행할 수 있습니다.

#### 과거 데이터 {#historical-data}

Snowflake의 과거 이벤트 데이터 아카이브는 2019년 4월까지 거슬러 올라갑니다. Braze가 Snowflake에 데이터를 저장하기 시작한 초기 몇 달 동안은 제품 변경이 이루어졌기 때문에, 일부 데이터가 약간 다르게 보이거나 일부 null 값이 있을 수 있습니다(당시 모든 사용 가능한 필드에 데이터를 전달하지 않았기 때문). 2019년 8월 이전의 데이터를 포함하는 결과는 예상과 약간 다를 수 있다고 가정하는 것이 좋습니다.

### 일반 데이터 보호 규정(GDPR) 준수 {#general-data-protection-regulation-gdpr-compliance}

{% include partners/snowflake_pii_gdpr.md %}

### 쿼리의 속도, 성능 및 비용 {#speed-performance-cost-of-queries}

데이터를 기반으로 실행하는 모든 쿼리의 속도, 성능 및 비용은 데이터를 쿼리하는 데 사용하는 웨어하우스 크기에 따라 결정됩니다. 경우에 따라 분석을 위해 액세스하는 데이터 양에 따라, 쿼리를 성공적으로 수행하려면 더 큰 웨어하우스 크기를 사용해야 할 수도 있습니다. Snowflake에는 적합한 크기를 결정하는 방법에 대한 우수한 리소스가 있으며, [웨어하우스 개요](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) 및 [웨어하우스 고려 사항](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html)을 참조하세요.

{% alert tip %}
Snowflake를 설정할 때 참고할 수 있는 예제 쿼리 세트에 대해서는 [샘플 쿼리]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/sample_queries) 및 [ETL 이벤트 파이프라인 설정]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/etl_pipline_setup) 예제를 확인하세요.
{% endalert %}