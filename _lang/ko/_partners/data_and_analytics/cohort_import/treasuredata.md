---
nav_title: Treasure Data
article_title: Treasure Data 코호트 가져오기
description: "이 참조 문서에서는 Treasure Data의 코호트 가져오기 기능에 대해 설명합니다."
alias: /partners/treasure_data_cohort_import/
page_type: partner
search_tag: Partner

---
# Treasure Data 코호트 가져오기 {#treasure-data-cohort-import}

> 이 문서에서는 Treasure Data에서 Braze로 사용자 코호트를 가져와 웨어하우스에만 존재할 수 있는 데이터를 기반으로 타겟 Campaign을 보내는 방법을 설명합니다.

{% alert important %}
이 기능은 현재 베타 버전입니다. 자세한 내용은 Treasure Data 및 Braze 담당자에게 문의하세요.
{% endalert %}

## 필수 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Treasure Data 계정 | 이 파트너십을 활용하려면 [Treasure Data](https://www.treasuredata.com/) 계정이 필요합니다. |
| Braze 데이터 가져오기 키 | Braze 대시보드에서 **파트너 통합** > **기술 파트너**로 이동한 다음 **Treasure Data**를 선택하여 확인할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
| Treasure Data 고정 IP 주소 | Treasure Data의 고정 IP 주소는 이 통합의 액세스 포인트이자 연결 소스입니다. 고정 IP 주소를 확인하려면 Treasure Data 고객 성공 담당자 또는 Treasure Data 기술 지원팀에 문의하세요. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 데이터 가져오기 통합 {#data-import-integration}

### 1단계: Braze 데이터 가져오기 키 가져오기 {#step-1-get-your-braze-data-import-key}

Braze에서 **파트너 통합** > **기술 파트너**로 이동하여 **Treasure Data**를 선택합니다. 여기에서 REST 엔드포인트를 확인하고 Braze 데이터 가져오기 키를 생성할 수 있습니다. 키가 생성되면 새 키를 만들거나 기존 키를 무효화할 수 있습니다.

### 2단계: 데이터 연결 생성 {#step-2-create-a-data-connection}

Treasure Data 내에서 데이터 연결을 생성하기 전에 인증이 필요합니다. 먼저 **Integrations Hub**를 선택한 다음 **Catalog**를 선택합니다.

![Treasure Data Integrations Hub Catalog]({% image_buster /assets/img/treasure_data/cohort/cohort1.png %})

**Catalog**에서 Braze 통합을 검색한 다음 아이콘 위에 마우스를 올리고 **Create Authentication**을 선택합니다. 자격 증명을 입력하고 인증 이름을 지정한 다음 **Done**을 선택합니다.

![Treasure Data Integrations Hub Catalog]({% image_buster /assets/img/treasure_data/cohort/cohort2.png %})

### 3단계: 코호트 오디언스 정의 {#step-3-define-your-cohort-audience}

**Audience Studio**에서 활성화를 통해 또는 **Data Workbench**에서 쿼리를 실행하여 코호트를 Braze에 동기화합니다.

{% alert important %}
이미 Braze 내에 존재하는 사용자만 코호트에 추가되거나 제거됩니다. 코호트 가져오기는 Braze에 새 사용자를 생성하지 않습니다.
{% endalert %}

{% tabs local %}
{% tab Data Workbench %}
#### 3.1단계: 쿼리 정의 {#step-31-define-your-query}

{% alert note %}
쿼리 열은 정확한 열 이름과 데이터 유형으로 지정해야 합니다. 쿼리 열에는 `user_ids`, `device_ids` 또는 UI 구성과 일치하는 Braze 별칭 열 중 하나 이상이 포함되어야 합니다. Braze 내에 존재하는 고객 프로필만 코호트에 추가됩니다. 코호트 가져오기는 새 고객 프로필을 생성하지 않습니다.
{% endalert %}

1. **Data Workbench** > **Queries**로 이동합니다.
2. **New Query**를 선택합니다.
3. 쿼리를 실행하여 결과 세트를 검증합니다.

![Treasure Data Integrations Hub Catalog]({% image_buster /assets/img/treasure_data/cohort/cohort3.png %})

##### 사용 사례: 식별자별 코호트 동기화 {#use-case-syncing-cohorts-by-identifier}

{% subtabs local %}
{% subtab Syncing External IDs %}
다음은 Treasure Data의 예시 테이블입니다:

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Use case: Syncing cohorts by identifier" }

{% alert warning %}
열 이름은 반드시 `user_ids`여야 하며, 그렇지 않으면 동기화가 실패합니다.
{% endalert %}

외부 ID를 사용하여 코호트를 동기화하려면 다음 쿼리를 실행합니다:

```sql
SELECT
  external_id as user_ids
FROM
  example_cohort_table
```

쿼리를 실행하면 다음 사용자 별칭이 Braze의 코호트에 추가됩니다:

 - `TDCohort1`
 - `TDCohort2`
 - `TDCohort3`
 - `TDCohort4`
{% endsubtab %}

{% subtab Syncing User Aliases %}
다음은 Treasure Data의 예시 테이블입니다:

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Use case: Syncing cohorts by identifier" }

사용자 별칭을 사용하여 코호트를 동기화하려면 다음 쿼리를 실행합니다:

```sql
SELECT
  email
FROM
  example_cohort_table
```

쿼리를 실행하면 다음 사용자 별칭이 Braze의 코호트에 추가됩니다:

 - `"alias_label":"email", "alias_name":"TDCohort1@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort2@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort3@gmail.com"`
 - `"alias_label":"email", "alias_name":"TDCohort4@gmail.com"`
{% endsubtab %}

{% subtab Syncing Device IDs %}
다음은 Treasure Data의 예시 테이블입니다:

| external_id |	email	| device_ids |
| ----------- | ----------- | ----------- |
| `TDCohort1`	| `TDCohort1@gmail.com`	| `1a2b3c` |
| `TDCohort2`	| `TDCohort2@gmail.com`	| `4d5f6g` |
| `TDCohort3`	| `TDCohort3@gmail.com`	| `7h8j9k` |
| `TDCohort4`	| `TDCohort4@gmail.com`	| `1ab2cd` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Use case: Syncing cohorts by identifier" }

{% alert warning %}
열 이름은 반드시 `device_ids`여야 하며, 그렇지 않으면 동기화가 실패합니다.
{% endalert %}

기기 ID를 사용하여 코호트를 동기화하려면 다음 쿼리를 실행합니다:

```sql
SELECT
  device_ids
FROM
  example_cohort_table
```

쿼리를 실행하면 다음 기기 ID가 Braze의 코호트에 추가됩니다:

- `1a2b3c`
- `4d5f6g`
- `7h8j9k`
- `1ab2cd`
{% endsubtab %}
{% endsubtabs %}

#### 3.2단계: 결과 내보내기 대상 지정 {#step-32-specify-the-result-export-target}

쿼리가 작성되면 **Export Results**를 선택합니다. 이전 단계에서 생성한 것과 같은 기존 인증을 선택하거나 출력에 사용할 새 인증을 생성할 수 있습니다.

![Treasure Data Integrations Hub Catalog]({% image_buster /assets/img/treasure_data/cohort/cohort5.png %})


| 내보내기 결과 매핑 | 설명 |
| ----------- | ----------- |
| Cohort ID | Braze로 전송될 백엔드 코호트 식별자입니다. |
| Cohort Name (선택 사항) | Braze 세분화 툴의 코호트 필터에 표시되는 이름입니다. 설정하지 않으면 `Cohort ID`가 `Cohort Name`으로 사용됩니다. |
| Operation | 쿼리가 Braze의 코호트에서 프로필을 추가할지 제거할지를 결정하는 데 사용됩니다. |
| Aliases (선택 사항) | 정의된 경우 쿼리 내 해당 열의 이름이 `alias_label`로 전송되고, 열의 각 행 값이 `alias_name`으로 전송됩니다. |
| Thread Count | 동시 API 호출 수입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3.2: Specify the result export target" }

사용 사례에 맞게 내보내기를 구성하려면 [Treasure Data의 단계](https://docs.treasuredata.com/articles/#!int/braze-cohort-export-integration/a/ExportIntegrationTemplate-SpecifytheResultExportTarget)를 따르세요.

#### 3.3단계: 쿼리 실행 {#step-33-execute-the-query}

쿼리에 이름을 지정하고 저장한 후 실행하거나, 바로 쿼리를 실행합니다. 쿼리가 성공적으로 완료되면 쿼리 결과가 자동으로 Braze로 내보내집니다.

{% endtab %}
{% tab Audience Studio %}
#### 3.1단계: 활성화 생성 {#step-31-create-an-activation}

새 Segment를 생성하거나 기존 Segment를 선택하여 코호트로 Braze에 동기화합니다. Segment 내에서 **Create activation**을 선택합니다.

#### 3.2단계: 활성화 세부 정보 입력 {#step-32-fill-out-your-activation-details}

![Treasure Data Integrations Activation Details]({% image_buster /assets/img/treasure_data/cohort/cohort7.png %})

| 활성화 세부 설정 | 설명 |
| ----------- | ----------- |
| Activation Name | 활성화의 이름입니다. |
| Activation Description | 활성화에 대한 간략한 설명입니다. |
| Authentication | 2단계에서 생성한 Braze 코호트 인증을 선택합니다. |
| Cohort ID | Braze로 전송될 백엔드 코호트 식별자입니다. |
| Cohort Name (선택 사항) | Braze 세분화 툴의 코호트 필터에 표시되는 이름입니다. 설정하지 않으면 `Cohort ID`가 `Cohort Name`으로 사용됩니다. |
| Operation | 쿼리가 Braze의 코호트에서 프로필을 추가할지 제거할지를 결정하는 데 사용됩니다. |
| Aliases (선택 사항) | 정의된 경우 쿼리 내 해당 열의 이름이 `alias_label`로 전송되고, 열의 각 행 값이 `alias_name`으로 전송됩니다. |
| Thread Count | 동시 API 호출 수입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3.2: Fill out your activation details" }

#### 3.3단계: 출력 매핑 설정 {#step-33-set-up-output-mapping}

![Treasure Data Integrations Activation Output Mapping]({% image_buster /assets/img/treasure_data/cohort/cohort6.png %})

| 활성화 출력 매핑 | 설명 |
| ----------- | ----------- |
| Attribute Columns | Segment 데이터베이스에서 Braze 코호트에 프로필을 동기화할 때 식별자로 매핑될 열을 결정합니다. |
| String Builder | 문자열 빌더는 Braze 통합에 필요하지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 3.3: Set up output mapping" }

{% alert important %}
 - `device_id`를 식별자로 사용하는 경우 **Output Column Name**은 반드시 `device_ids`로 지정해야 합니다.
 - 별칭을 식별자로 사용하는 경우 **Output Column Name**은 쿼리 내 해당 열의 이름이어야 하며, 이 이름이 `alias_label`로 전송되고 열의 각 행 값이 `alias_name`으로 전송됩니다.
 - `external_id`를 식별자로 사용하는 경우 **Output Column Name**은 반드시 `user_ids`로 지정해야 합니다.
{% endalert %}

관련 없거나 잘못된 열 이름은 모두 무시됩니다. 동기화에 둘 이상의 식별자를 사용할 수 있습니다.

#### 3.4단계: 활성화 스케줄 정의 {#step-34-define-your-activation-schedule}

원하는 동기화 스케줄을 정의하고 활성화를 저장합니다.

![Treasure Data Integrations Activation Schedule]({% image_buster /assets/img/treasure_data/cohort/cohort8.png %})
{% endtab %}
{% endtabs %}

### 4단계: Treasure Data 내보내기에서 Braze Segment 생성 {#step-4-create-a-braze-segment-from-the-treasure-data-export}

Braze에서 **Segments**로 이동하여 새 Segment를 생성하고 필터로 **Treasure Data Cohorts**를 선택합니다. 여기에서 포함할 Treasure Data 코호트를 선택할 수 있습니다. Treasure Data 코호트 Segment가 생성되면 Campaign 또는 Canvas를 생성할 때 오디언스 필터로 선택할 수 있습니다.

![Treasure Data Integrations Hub Catalog]({% image_buster /assets/img/treasure_data/cohort/cohort4.png %})

## 사용자 매칭 {#user-matching}

식별된 사용자는 `external_id` 또는 `alias`로 매칭할 수 있습니다. 익명 사용자는 `device_id`로 매칭할 수 있습니다. 원래 익명 사용자로 생성된 식별된 사용자는 `device_id`로 식별할 수 없으며, `external_id` 또는 `alias`로 식별해야 합니다.