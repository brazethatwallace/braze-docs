---
nav_title: Amperity
article_title: Amperity
alias: /partners/amperity/
description: "이 참조 문서에서는 종합 엔터프라이즈 고객 데이터 플랫폼인 Amperity와 Braze 간의 파트너십에 대해 설명합니다. 이를 통해 Amperity 사용자를 동기화하고, 데이터를 통합하며, AWS S3 버킷을 사용하여 Braze로 데이터를 전송하는 등의 작업을 수행할 수 있습니다."
page_type: partner
search_tag: Partner

---

# Amperity

> [Amperity](https://amperity.com/)는 종합 엔터프라이즈 고객 데이터 플랫폼으로, 브랜드가 고객을 더 잘 이해하고, 전략적 의사결정을 내리며, 소비자에게 더 나은 서비스를 제공하기 위해 일관되게 올바른 조치를 취할 수 있도록 지원합니다. Amperity는 데이터 관리 통합, 분석, 인사이트 및 활성화 전반에 걸쳐 지능형 기능을 제공합니다.

_이 통합은 Amperity에서 유지 관리합니다._

{% multi_lang_include video.html id="06G0lxaSjgk" align="right" %}

Braze와 Amperity 통합은 두 플랫폼에 걸쳐 고객에 대한 통합 뷰를 제공합니다. 이 통합을 통해 다음을 수행할 수 있습니다:
- **고객 프로필 동기화**: Amperity에서 Braze로 사용자 데이터와 커스텀 속성을 매핑합니다.
- **오디언스 생성 및 전송**: 활성 고객 목록과 관련 커스텀 속성을 반환하는 세그먼트를 구축하여 Braze로 전송합니다.
- **데이터 업데이트 관리**: Braze로 커스텀 속성 업데이트를 전송하는 빈도를 제어합니다.
- **데이터 통합**: Amperity가 지원하는 다양한 플랫폼과 Braze 간의 데이터를 통합합니다.
- **Braze 데이터를 Amazon S3로 동기화**: Braze Currents를 사용하여 Braze Campaigns의 인게이지먼트 데이터를 통합하고, Apache Avro 형식으로 Amazon S3에 데이터를 동기화할 수 있습니다.

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Amperity 계정 | 이 파트너십을 활용하려면 [Amperity 계정](https://amperity.com/request-a-demo)이 필요합니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키. <br> Braze 대시보드에서 **개발자 콘솔** > **Rest API Key** > **새 API 키 생성**으로 이동하여 생성할 수 있습니다. |
| Braze 인스턴스 | Braze 인스턴스는 Braze 온보딩 매니저에게 문의하거나 [API 개요 페이지]({{site.baseurl}}/api/basics#endpoints)에서 확인할 수 있습니다. |
| Braze REST 엔드포인트 | Braze 엔드포인트 URL. 엔드포인트는 Braze 인스턴스에 따라 달라집니다. |
| Currents 커넥터(선택 사항) | S3 Currents 커넥터. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="필수 조건" }

## 데이터 매핑 {#data-mapping}

표준 속성과 커스텀 속성 모두 Amperity에서 Braze로 전송할 수 있으며, 이를 통해 Amperity를 통해 다양한 소스의 데이터로 Braze의 고객 프로필을 보강할 수 있습니다. 전송할 수 있는 구체적인 속성은 Amperity 시스템의 데이터와 Braze에서 설정한 속성에 따라 달라집니다.

이러한 속성에 대해 자세히 알아보려면 아래를 참조하세요.

### 표준 속성 {#standard-attributes}

[프로필 속성]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)은 고객이 누구인지를 설명합니다. 이러한 속성은 주로 다음과 같은 고객의 신원 정보와 관련됩니다:
- 이름
- 생년월일
- 이메일 주소
- 전화번호

### 커스텀 속성 {#custom-attributes}

Braze의 [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes)은 브랜드에서 결정하는 필드입니다. Amperity에서 Braze에 이미 존재하는 커스텀 속성을 관리하려면, Amperity에서 전송되는 출력을 Braze 워크스페이스에 이미 있는 이름과 일치시키세요. 여기에는 다음이 포함될 수 있습니다:
- 구매 이력
- 로열티 상태
- 가치 등급
- 최근 인게이지먼트 데이터

Amperity에서 Braze로 전송될 커스텀 속성의 이름을 확인하세요. Amperity는 일치하는 이름이 없을 때마다 커스텀 속성을 추가합니다.

커스텀 속성은 Braze 내에서 일치하는 `external_id` 또는 `braze_id`가 있는 사용자에 대해서만 업데이트됩니다.

### Amperity 오디언스 {#amperity-audiences}

Amperity에서 Braze로 동기화된 오디언스는 고객 프로필에 커스텀 속성으로 기록됩니다. 그런 다음 이를 사용하여 Braze에서 해당 사용자를 타겟팅할 수 있습니다.

![커스텀 데이터 카테고리에 커스텀 속성이 표시된 필터 드롭다운 목록.]({% image_buster /assets/img/amperity/custom_attributes_filters.png %}){: style="max-width:60%;"}

!["l12m_frequency" 및 "l12m_monetary"와 같은 커스텀 속성의 드롭다운 목록.]({% image_buster /assets/img/amperity/search_custom_attributes_filters.png %}){: style="max-width:40%;"}

### 데이터 유형 {#data-types}

지원되는 데이터 유형은 다음과 같습니다:
- Boolean
- Date
- Datetime
- Decimal
- Float
- Integer
- String
- Varchar

사용되는 데이터 유형은 속성의 특성에 따라 달라집니다. 예를 들어, 이메일 주소는 문자열이고, 고객의 나이는 정수일 수 있습니다.

### 속성 중복 {#duplication-of-attributes}

기본 고객 프로필 필드와 중복되는 커스텀 속성을 전송하지 마세요. 예를 들어, 생년월일은 Braze 표준 속성과 일치하도록 "dob"라는 이름의 고객 프로필 필드로 Braze에 전송해야 합니다. "birthday", "Birthdate" 또는 다른 문자열로 전송하면 커스텀 속성이 생성되고, "dob" 필드의 값은 업데이트되지 않습니다.

### 데이터 포인트 {#data-points}

Amperity는 Braze로의 동기화 간 변경 사항과 전체 전송 상태를 추적합니다. Amperity는 마지막 동기화 이후 변경된 목록 멤버십 및 기타 선택된 속성만 Braze로 전송합니다.

## 통합 {#integration}

### 1단계: Braze 구성 세부 정보 수집 {#step-1-capture-configuration-details-for-braze}

1. **사용자 데이터** 아래에서 `users.track` 권한이 있는 Braze 워크스페이스용 Braze REST API 키를 생성합니다. `users.track` 엔드포인트는 Amperity 오디언스를 커스텀 속성으로 Braze에 동기화합니다.
2. Braze 인스턴스의 [REST API 엔드포인트]({{site.baseurl}}/api/basics#endpoints)를 확인합니다. 예를 들어, Braze URL이 `https://dashboard-03.braze.com`인 경우, REST API 엔드포인트는 `https://rest.iad-03.braze.com`이고 인스턴스는 "US-03"입니다.
3. Amperity에서 Braze로 전송할 수 있는 [고객 프로필 필드]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields) 및 [커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes) 목록을 확인합니다.

### 2단계: Braze를 대상으로 설정—DataGrid Operator {#step-2-set-up-braze-as-a-destinationdatagrid-operator}

#### 2a단계: 고객 프로필 테이블 구축 {#step-2a-build-the-customer-profiles-table}

Amperity의 Customer 360 데이터베이스 내에 "Braze Customer Attributes"라는 새 테이블을 생성합니다. 이 테이블에는 브랜드가 Amperity에서 관리하려는 Braze의 모든 속성이 포함되어야 하며, Braze에서 요구하는 기본 고객 프로필 필드와 커스텀 속성이 모두 포함됩니다. [Amperity 설명서](https://docs.amperity.com/datagrid/destination_braze.html#customer-profiles-table)에 표시된 대로 SQL을 사용하여 이 테이블의 구조를 정의합니다.

#### 2b단계: 테이블 이름 지정, 유효성 검사 및 저장 {#step-2b-name-validate-and-save-the-table}

테이블 이름을 "Braze Customer Attributes"로 지정하고 저장합니다. 테이블이 **Segment Editor** 및 캠페인 내 **Edit Attributes** 편집기에서 접근 가능한지 확인합니다.

#### 2c단계: Braze를 대상으로 추가 {#step-2c-add-braze-as-a-destination}

Amperity 플랫폼에서 **Destinations** 탭으로 이동합니다. 새 대상을 추가하는 옵션을 찾습니다. 사용 가능한 옵션에서 **Braze**를 선택합니다.

![이름이 "Braze API"이고 설명이 "Braze로 오디언스 속성 전송"이며 플러그인이 "Braze"인 새 대상 섹션.]({% image_buster /assets/img/amperity/destination_name.png %}){: style="max-width:60%;"}

#### 2d단계: 대상 세부 정보 구성 {#step-2d-configure-destination-details}

**Braze settings** 아래에서 [Amperity 설명서](https://docs.amperity.com/datagrid/destination_braze.html#add-destination)에 표시된 대로 Braze 자격 증명과 대상 설정을 제공합니다. 이전 단계에서 수집한 구성 세부 정보를 입력하고 Braze 식별자를 정의합니다. 매칭에 사용할 수 있는 식별자는 다음과 같습니다:
- `braze_id`: Braze에서 자동으로 할당되는 식별자로, 변경할 수 없으며 사용자가 Braze에서 생성될 때 해당 사용자와 연결됩니다.
- `external_id`: 고객이 할당한 식별자로, 일반적으로 UUID입니다.

![인스턴스가 "US-03"이고, 사용자 식별자가 "external_id"이며, 빈 세그먼트 이름, S3 버킷이 "amperity-training-abc123"이고, S3 폴더가 "braze-attributes"인 Braze 설정 섹션.]({% image_buster /assets/img/amperity/braze_settings.png %}){: style="max-width:60%;"}

#### 2e단계: 데이터 템플릿 추가 {#step-2e-add-a-data-template}

**Destinations** 탭에서 Braze 대상의 메뉴를 열고 **Add data template**을 선택합니다. 템플릿의 이름과 설명을 입력하고(예: "Braze" 및 "Braze로 커스텀 속성 전송"), 비즈니스 사용자 접근 권한을 확인하고, 모든 구성 설정을 점검합니다.

대상의 일부로 구성되지 않은 필수 설정이 있는 경우, 데이터 템플릿의 일부로 구성합니다. 데이터 템플릿을 저장합니다.

![이름이 "Braze Audience Attributes"이고 설명이 "Braze로 오디언스 속성 전송"인 데이터 템플릿 이름 섹션.]({% image_buster /assets/img/amperity/data_template_name.png %}){: style="max-width:60%;"}

#### 2f단계: 구성 저장 {#step-2f-save-the-configuration}

필요한 세부 정보를 모두 입력한 후 구성을 저장합니다. 이제 Braze가 대상으로 구성되었으므로, Amp360 및 AmpIQ 사용자가 Braze로 데이터를 동기화할 수 있습니다.

### 3단계: Braze로 데이터 동기화 {#step-3-sync-data-to-braze}

Amperity 테넌트에서 Braze가 활성화되어 있는지 확인합니다. 활성화되어 있지 않은 경우, DataGrid Operator 또는 Amperity 담당자에게 문의하세요.

그런 다음 회사에 해당하는 Amp360 또는 AmpIQ의 동기화 지침을 따릅니다.

#### 동기화 옵션 1: Amp360을 통해 쿼리 결과를 Braze로 전송 {#syncing-option-1-send-query-results-to-braze-via-amp360}

Amp360 사용자는 SQL을 사용하여 자유 형식 쿼리를 작성한 다음, 결과를 Braze로 전송하는 스케줄을 구성할 수 있습니다.

##### 1단계: Amperity에서 쿼리 생성 {#step-1-create-a-query-in-amperity}

Amperity의 쿼리 기능으로 이동하여 원하는 고객 데이터 세트를 생성하는 SQL 쿼리를 작성합니다. 결과에는 Braze로 전송하려는 특정 속성이 포함되어야 합니다. 구매 이력이 포함된 사용자 목록을 반환하는 Amperity 쿼리 예시를 참조하세요.

##### 2단계: Amperity에서 새 오케스트레이션 추가 {#step-2-add-a-new-orchestration-in-amperity}

1. **Orchestration** 섹션으로 이동하여 새 오케스트레이션을 추가하는 옵션을 클릭합니다.
2. 오케스트레이션이 수행할 작업을 지정합니다. 일반적으로 실행할 SQL 쿼리와 결과를 전송할 위치를 지정합니다. 이 경우, 활성 고객 목록을 생성하기 위해 만든 SQL 쿼리를 선택하고 결과의 대상으로 Braze를 지정합니다.
3. 오케스트레이션이 실행될 시기와 빈도를 정의합니다. 예를 들어, 매일 특정 시간에 오케스트레이션을 실행할 수 있습니다.
4. 원하는 대로 구성한 후 오케스트레이션을 저장합니다. Amperity의 오케스트레이션 목록에 추가됩니다.
5. 오케스트레이션이 예상대로 작동하는지 테스트합니다. 오케스트레이션을 수동으로 트리거하고 Braze에서 결과를 확인하여 테스트할 수 있습니다.

##### 3단계: 오케스트레이션 실행 {#step-3-run-the-orchestration}

오케스트레이션을 실행하여 쿼리를 실행하고 결과를 Braze로 전송합니다. 수동으로 실행하거나 오케스트레이션 설정에서 구성한 스케줄에 따라 실행할 수 있습니다.

#### 동기화 옵션 2: AmpIQ를 통해 오디언스를 Braze로 전송 {#syncing-option-2-send-audiences-to-braze-via-ampiq}

AmpIQ 사용자는 비SQL 인터페이스를 통해 Amperity에서 세그먼트를 생성하고 Braze와 같은 다운스트림 대상으로 동기화할 수 있습니다. 사용자는 대상을 선택한 다음 각 대상으로 전송할 속성 목록을 구성할 수 있습니다.

##### 1단계: Amperity에서 세그먼트 생성 {#step-1-create-a-segment-in-amperity}

Amperity에서 고객 목록을 반환하는 세그먼트를 생성합니다. 이 세그먼트는 Braze에서 업데이트하려는 커스텀 속성과 연결되어야 합니다.

{% alert note %}
Braze로 전송할 수 있는 다양한 세그먼트 유형의 예시는 Amperity 설명서를 참조하세요.
{% endalert %}

##### 2단계: Amperity에서 캠페인 구축 {#step-2-build-a-campaign-in-amperity}

1. **Campaign** 섹션으로 이동하여 새 캠페인을 생성하는 옵션을 클릭합니다.
2. 나중에 식별하기 쉽도록 캠페인에 설명적이고 고유한 이름을 지정합니다. 특히 여러 캠페인이 있는 경우 유용합니다.
3. 이 캠페인으로 타겟팅할 고객 세그먼트를 선택합니다. 이전에 생성한 세그먼트여야 합니다. <br>![타겟팅에서 제외할 세그먼트의 드롭다운 필드.]({% image_buster /assets/img/amperity/select_segments.png %}){: style="max-width:50%;"}<br><br>
4. 캠페인의 일부로 전송할 데이터를 선택합니다. 여기에는 다양한 고객 속성이 포함될 수 있습니다. ![캠페인 속성 편집 모달에서는 대상 및 고객 속성을 선택할 수 있습니다.]({% image_buster /assets/img/amperity/edit_campaign_attributes.png %}){: style="max-width:90%;"}<br><br>
5. 캠페인 데이터를 전송할 대상으로 **Braze**를 선택합니다.
6. 캠페인을 실행할 시기와 빈도를 선택합니다. 일회성 이벤트 또는 반복 스케줄로 설정할 수 있습니다.
7. 캠페인을 저장하고 테스트를 실행하여 예상대로 작동하는지 확인합니다.

##### 3단계: 캠페인 실행 {#step-3-run-the-campaign}

캠페인을 실행하여 세그먼트를 Braze로 전송합니다. 수동으로 실행하거나 캠페인 설정에서 구성한 스케줄에 따라 실행할 수 있습니다.


### Braze Currents와 함께 Amperity 사용 {#using-amperity-with-braze-currents}
Braze Currents 데이터를 Amperity로 전송하려면:
1. Amazon S3 버킷으로 데이터를 전송하도록 [Braze Current를 설정]({{site.baseurl}}/user_guide/data/distribution/braze_currents/setting_up_currents)합니다.
2. 해당 Amazon S3 버킷에서 [Apache Avro 파일을 읽도록](https://docs.amperity.com/datagrid/source_amazon_s3.html) Amperity를 구성합니다.
3. 표준 워크플로를 사용하여 피드를 구성하고 데이터 로드를 자동화합니다.