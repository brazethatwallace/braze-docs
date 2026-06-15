---
nav_title: LiveRamp
article_title: LiveRamp
description: "LiveRamp, Snowflake, Braze를 연결하여 고도로 개인화되고 관련성 높은 마케팅 캠페인을 만드는 방법을 알아보세요."
alias: /partners/liveramp/
page_type: partner
search_tag: Partner
---

# LiveRamp, Snowflake, Braze 연결하기 {#connect-liveramp-snowflake-and-braze}

> LiveRamp, Snowflake, Braze를 연결하여 인사이트 도출 시간을 단축하고, 데이터 사일로를 해소하며, 고객 참여를 최적화함으로써 고도로 개인화되고 관련성 높은 마케팅 캠페인을 만드는 방법을 알아보세요. 이 통합은 실행 가능한 개인 기반 인사이트를 제공하고 소비자 터치포인트를 통합하여 더 나은 오디언스 세분화와 적시 캠페인을 가능하게 함으로써 데이터 중심 마케팅을 강화합니다. 또한 Snowflake 기반 벤치마크를 활용하여 업계 표준에 맞춰 마케팅 전략을 개선할 수 있습니다.

{% alert important %}
Snowflake의 [Secure Data Shares](https://docs.snowflake.com/en/user-guide/data-sharing-intro)는 LiveRamp, Snowflake, Braze 간에 데이터를 전송하지 않습니다. 데이터는 Snowflake의 서비스와 메타데이터 저장소를 통해서만 공유되므로 데이터가 복사되지 않으며 추가 스토리지 비용이 발생하지 않습니다. 공유 데이터에 대한 접근은 Snowflake 계정의 접근 제어를 사용하여 관리 및 통제됩니다.
{% endalert %}

## 활용 사례 {#use-cases}

- **데이터 최소화:** LiveRamp의 Activation 앱은 Snowflake의 Secure Data Share 기능을 사용하여 인스턴스에서 직접 테이블을 효과적으로 읽습니다. 다운스트림 파트너에게 전달하는 시점까지 Snowflake에서 데이터가 이동하지 않습니다.
- **안전한 1st Party 활성화:** 위의 Identity Resolution 애플리케이션을 사용하면 LiveRamp의 Activation 애플리케이션은 Snowflake 인스턴스의 RampID 기반 테이블만 활용하므로 PII가 외부로 유출될 필요가 없습니다.
- **라이브 시간 단축:** 환경 내에서 직접 데이터를 RampID로 확인하면 최종 대상으로의 전달이 몇 시간 내에 이루어질 수 있으며, 이는 LiveRamp의 기존 파일 기반 방식을 사용할 때 며칠이 걸리는 것과 비교됩니다. 이를 통해 적시에 캠페인 성과를 최적화하는 능력이 크게 향상됩니다.
- **운영 비용 절감:** 위와 마찬가지로 Snowflake의 Secure Data Share 기능을 사용하면 LiveRamp 또는 최종 대상으로 파일을 전송하는 것과 비교하여 시간과 비용을 절약할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
|---|---|
| Snowflake 계정 | 관리자 수준의 권한이 있는 Snowflake 계정이 필요합니다. |
| LiveRamp 계정 | Snowflake 내에서 필요한 LiveRamp 애플리케이션에 대해 논의하려면 LiveRamp 계정 팀 또는 [snowflake@liveramp.com](mailto:snowflake@liveramp.com)으로 문의하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 통합 설정 {#setting-up-the-integration}

### 1단계: Braze에 데이터 공유 요청 {#step-1-request-a-data-share-from-braze}

먼저 Braze 계정 매니저 또는 고객 성공 매니저에게 연락하여 Braze 계정에 대한 Snowflake 데이터 공유 커넥터를 구매하세요. 데이터 공유를 요청하면 Braze가 공유를 구매한 워크스페이스에서 공유를 프로비저닝합니다. 공유가 프로비저닝되면 Snowflake 인스턴스 내에서 수신 데이터 공유 형태로 모든 데이터에 즉시 접근할 수 있습니다. 인스턴스에서 공유가 표시되면 공유에서 데이터베이스를 생성하여 테이블을 확인하고 쿼리할 수 있습니다.

전체 안내는 [Braze와 Snowflake 통합 가이드]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)를 참조하세요.

### 2단계: Snowflake에서 LiveRamp 앱 설정 {#step-2-set-up-the-liveramp-app-in-snowflake}

번역 및 ID 확인 기능은 LiveRamp Identity Resolution and Translation 네이티브 앱을 통해 Snowflake 내에서 사용할 수 있으며, 이 앱은 계정에 공유를 생성하여 자체 Snowflake 환경 내에서 참조 데이터셋을 쿼리할 수 있는 뷰를 제공합니다.

네이티브 앱을 설정하려면 LiveRamp 문서의 다음 단계를 따르세요: [Snowflake에서 LiveRamp 네이티브 앱 설정](https://docs.liveramp.com/identity/en/set-up-the-liveramp-native-app-in-snowflake.html). 완료되면 다음 단계로 진행하세요.

### 3단계: 데이터 테이블 생성 {#step-3-create-a-data-table}

{% alert warning %}
PII 기반 테이블을 준비하기 전에 작업 중 실행되는 [LiveRamp의 개인정보 보호 필터](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html)를 이해해야 합니다. 이 필터는 입력 테이블의 속성 열(비식별자)에 너무 고유한 값이 포함되지 않도록 합니다. 이는 소비자 개인정보를 보호하고 재식별을 방지하는 데 매우 중요합니다.
{% endalert %}

다음으로, LiveRamp 네이티브 앱에 대해 호출될 [필수 형식](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html)의 데이터 테이블을 생성합니다. 다음 카테고리를 참조하여 어떤 식별자가 확인에 적합한지 결정하세요:

| 식별자 유형 | 설명 |
|---|---|
| 전체 PII | 개인 식별 정보(PII)에는 사용자의 이름, 우편 주소, 이메일, 전화번호가 포함됩니다. **참고:** 모든 레코드에 모든 식별자가 필요한 것은 아닙니다. |
| 이메일만 | `alex-lee@email.com`과 같은 사용자의 이메일 주소입니다. |
| 기기 | 여기에는 서드파티 쿠키, 모바일 광고 ID(MAID), 커넥티드 TV ID(CTV ID), RampID(가구 RampID로 확인됨)가 포함됩니다. |
| CID | 플랫폼 파트너 또는 LiveRamp와의 ID 동기화에서 가져온 식별자로, 내부 고객 ID 등이 해당됩니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3: Create a data table" }

#### Braze 식별자 {#braze-identifiers}

Braze의 이벤트 로그에는 LiveRamp 네이티브 앱 내에서 사용할 수 있는 식별자가 포함되어 있습니다. 각 이벤트 유형에 사용 가능한 식별자의 전체 목록은 [Braze 이벤트 스키마 및 식별자]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt)를 다운로드하세요.

| 식별자 유형 | 설명 |
|---|---|
| `AD_ID` | `ios_idfa`, `google_ad_id`, `roku_ad_id`와 같은 광고 ID로, 특정 이벤트 유형 내에서 캡처되며 LiveRamp의 Device Resolution 서비스와 함께 사용할 수 있습니다. 기본적으로 광고 ID는 수집되지 않지만 [Braze 설명서]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#data-not-collected-by-default)를 따라 추적을 활성화할 수 있습니다. |
| `EMAIL_ADDRESS` | LiveRamp의 Email Only Resolution 서비스와 함께 사용할 수 있는 이메일 주소입니다. |
| `TO_PHONE_NUMBER` | LiveRamp의 PII Resolution 서비스와 함께 사용할 수 있는 전화번호입니다. |
| `EXTERNAL_USER_ID` | 사용자와 연결된 외부 ID로, LiveRamp의 Device Resolution 서비스(CID)와 함께 사용할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Braze identifiers" }

{% alert important %}
LiveRamp의 애플리케이션 내에서 클라이언트 또는 브랜드별 커스텀 식별자를 사용하려면 [LiveRamp와의 ID 동기화](https://docs.liveramp.com/identity/en/getting-started-with-liveramp-identity.html)가 필요합니다.
{% endalert %}

### 4단계: 변수 설정 {#step-4-set-your-variables}

다음으로, 앱에서 제공하는 실행 단계 워크시트에서 작업에 대한 변수를 설정합니다. 여기에는 대상 데이터베이스, 관련 테이블(입력 데이터, 측정기준, 로깅), 출력 테이블 이름 정의 등의 세부 정보가 포함됩니다. 전체 안내는 [LiveRamp: 변수 지정](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#specify-the-variables-43-150727)을 참조하세요.

### 5단계: PII 확인을 위한 메타데이터 테이블 생성 {#step-5-create-the-metadata-table-for-pii-resolution}

변수가 설정되었으므로 PII 확인을 위한 메타데이터 테이블을 생성합니다. 이 테이블은 관련된 식별자 카테고리에 따라 실행할 특정 작업 유형에 대한 세부 정보를 제공합니다. 전체 안내는 [LiveRamp: 메타데이터 테이블 생성](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#create-the-metadata-table-43)을 참조하세요.

### 6단계: ID 확인 작업 수행 {#step-6-perform-the-identity-resolution-operation}

마지막으로 ID 확인 작업을 수행합니다. 전체 안내는 [LiveRamp: ID 확인 작업 수행](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#perform-the-identity-resolution-operation)을 참조하세요.

{% tabs local %}
{% tab 입력 예시 %}
```sql
call lr_resolution_and_transcoding(
$customer_input_table_name,
$customer_meta_table_name,
$output_table_name,
$customer_logging_table_name,
$customer_metrics_table_name
);
```
{% endtab %}

{% tab 출력 예시 %}
```sql
call check_for_output(
$output_table_name
);
```
{% endtab %}
{% endtabs %}

### 다음 단계 {#next-steps}

이제 데이터가 전용 RampID 인코딩으로 가명 처리되었으므로, RampID 기반 테이블을 LiveRamp의 Managed Activation Application에 공유하여 주요 광고 플랫폼 파트너에게 간소화된 이행을 수행할 수 있습니다. Activation Application에는 추가 세분화 및 다운스트림 대상 파트너의 선택/구성을 위한 비즈니스 사용자 친화적인 인터페이스가 포함되어 있습니다. 애플리케이션에 대한 자세한 내용은 LiveRamp 계정 팀 또는 [snowflake@liveramp.com](mailto:snowflake@liveramp.com)으로 문의하세요.

## 문제 해결 {#troubleshooting}

{% alert note %}
보다 구체적인 문제나 질문이 있는 경우 [martech@liveramp.com](mailto:martech@liveramp.com)으로 문의하세요.
{% endalert %}

### Snowflake 리전 {#snowflake-regions}

현재 이 애플리케이션은 다음 미국 기반 리전에서만 사용할 수 있습니다:

  - aws-us-east-1: POA18931
  - aws-us-west-2: FAA28932
  - azure-east-us-2: BL60425

### 개인정보 보호 및 열 값 {#privacy-column-values}

이 프로세스는 행별로 모든 열 값의 조합을 고유 값 기준으로 평가합니다. 특정 열 값 조합이 3회 이하로 발생하면 해당 열 값을 포함하는 행은 매칭할 수 없으며 출력 테이블에 반환되지 않습니다. 마찬가지로 개인정보를 보호하기 위해 LiveRamp 서비스는 열 값 조합의 고유성을 평가하며, 드문 조합으로 인해 파일 행의 5% 이상이 매칭 불가능해지면 작업이 실패합니다.

### 과거 데이터 {#historical-data}

Snowflake의 과거 데이터는 2019년 4월까지 거슬러 올라가지만, 제품 변경으로 인해 2019년 8월 이전 데이터에는 약간의 차이가 있을 수 있습니다.

### 속도, 성능, 비용 {#speed-performance-cost}

쿼리의 속도와 비용은 사용하는 웨어하우스 크기에 따라 달라집니다. 웨어하우스 크기를 선택할 때 데이터 접근 요구 사항을 고려하세요.

### Braze 벤치마크 {#braze-benchmarks}

벤치마크를 사용하면 Snowflake Data Exchange에서 직접 사용할 수 있는 업계 표준과 측정기준을 비교할 수 있습니다.

### 호환성에 영향을 주는 변경 사항과 주지 않는 변경 사항 {#breaking-vs-non-breaking-changes}

통합에 영향을 줄 수 있는 변경 사항에 유의하세요. 호환성에 영향을 주는 변경 사항은 사전 공지와 마이그레이션 기간이 제공됩니다.