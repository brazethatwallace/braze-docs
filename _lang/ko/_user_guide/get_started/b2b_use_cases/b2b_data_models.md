---
nav_title: 데이터 모델
article_title: B2B 데이터 모델 만들기
page_order: 0
page_type: reference
description: "Braze 데이터 도구를 사용하여 B2B 모델을 만드는 방법을 알아보세요."
---

# B2B 데이터 모델 만들기 {#create-a-b2b-data-model}

> 이 사용 사례는 Braze 데이터 도구를 사용하여 비즈니스 사용자를 타겟팅, 트리거, 개인화하고 메시지를 발송하는 데 도움이 되는 효과적이고 효율적인 B2B 데이터 모델을 만드는 방법을 보여줍니다.

{% alert note %}
이러한 권장 사항은 Braze가 B2B 기능을 구축함에 따라 시간이 지나면서 변경될 수 있습니다.
{% endalert %}

B2B 데이터 모델을 설정하는 방법을 살펴보기 전에 알아야 할 몇 가지 개념과 용어를 먼저 살펴보겠습니다.

B2B Campaign(캠페인)을 실행하는 데 필요한 네 가지 주요 B2B 오브젝트가 있습니다.

| 오브젝트 | 설명 |
| --- | --- |
| 리드 | 제품이나 서비스에 관심을 보였지만 아직 기회로 전환되지 않은 잠재고객에 대한 기록입니다. |
| 연락처 | 일반적으로 자격을 갖추고 리드에서 연락처로 전환되어 영업 기회를 추구하는 개인입니다. |
| 기회 | 진행 중인 잠재적 판매 또는 거래의 세부 정보를 추적하는 레코드입니다. |
| 계정 | 자격을 갖춘 잠재고객, 기존 고객, 파트너 또는 이와 유사한 중요한 관계를 맺고 있는 경쟁사 조직에 대한 기록입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="B2B 데이터 모델 만들기" }

Braze 내에서 이 네 가지 오브젝트는 고객 프로필과 비즈니스 오브젝트라는 두 가지 오브젝트로 결합 및 축소됩니다.

| Braze B2B 오브젝트 | 설명 | 원본 B2B 오브젝트 |
| --- | --- | --- |
| 고객 프로필 | 영업 CRM 시스템의 리드와 연락처에 직접 매핑됩니다. 리드는 Braze에서 캡처되므로 영업 CRM 시스템에서 자동으로 리드로 생성됩니다. 연락처로 전환되면 연락처 ID와 세부 정보가 다시 Braze에 동기화됩니다. | 리드<br> 연락처 |
| 비즈니스 오브젝트 | 영업 CRM 시스템의 모든 비사용자 오브젝트에 매핑됩니다. 여기에는 계정 오브젝트 및 기회 오브젝트와 같은 영업 관련 오브젝트가 포함됩니다. | 계정<br> 기회 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="B2B 데이터 모델 만들기" }

## 1단계: Braze에서 비즈니스 오브젝트 만들기 {#step-1-create-your-business-objects-in-braze}

비즈니스 오브젝트는 사용자 중심이 아닌 모든 데이터 세트입니다. B2B 맥락에서 이러한 데이터에는 계정 및 기회 데이터와 회사가 추적하는 기타 관련 비사용자 중심 데이터 세트가 포함됩니다.

Braze에서 비즈니스 오브젝트를 만들고 관리하는 방법에는 카탈로그와 연결된 소스 두 가지가 있습니다.

| 방법 | 설명 |
| --- | --- |
| [카탈로그]({{site.baseurl}}/user_guide/data/activation/catalogs) | Braze의 기본 고객 프로필에 있는 독립 데이터 오브젝트(보조 데이터 오브젝트)입니다. B2B 환경에서는 계정과 기회에 대한 카탈로그가 있을 것입니다. |
| [연결된 소스]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources) | Braze가 데이터 웨어하우스에 직접 쿼리할 수 있도록 합니다. 이미 리드, 연락처, 기회, 계정 오브젝트를 데이터 웨어하우스에 정기적으로 동기화하고 있을 가능성이 높으므로 Braze 세분화를 해당 웨어하우스에 직접 지정하고 제로 카피 환경에서 활성화할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="1단계: Braze에서 비즈니스 오브젝트 만들기" }

{% tabs %}
{% tab Catalogs %}

### 옵션 1: 계정 및 기회에 카탈로그 사용 {#option-1-use-catalogs-for-accounts-and-opportunities}

카탈로그는 Braze에서 호스팅 및 관리되는 데이터 테이블입니다. 계정 및 기회 데이터는 선택한 영업 CRM 시스템에서 생성되지만, 계정 기반 세분화, 계정 기반 마케팅, 리드 관리 등 마케팅 목적으로 사용하기 위해 Braze에서 이를 복제하게 됩니다.

이 옵션의 경우, 계정용 카탈로그와 기회용 카탈로그를 각각 하나씩 생성하고 [카탈로그 API]({{site.baseurl}}/api/endpoints/catalogs) 또는 [카탈로그 클라우드 데이터 수집(CDI)]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_catalogs_data)을 통해 Braze 업데이트를 전송하여 자주 업데이트하는 것을 권장합니다. 이러한 카탈로그를 생성할 때 카탈로그의 `id`(첫 번째 열)이 영업 CRM 시스템의 `id`와 일치하는지 확인하세요.

#### CRM 필드 매핑 {#map-over-your-crm-fields}

아래 표에는 CRM의 계정 및 기회 오브젝트에서 매핑할 수 있는 필드의 몇 가지 예가 나와 있습니다.

{% subtabs %}
{% subtab Account catalog %}

이 사용 사례에서는 Salesforce가 예시 CRM 시스템입니다. CRM의 오브젝트에 포함된 모든 필드에 매핑할 수 있습니다.

<table aria-label="CRM 필드 매핑" border="1">
  <caption>CRM 필드 매핑</caption>
  <thead>
  <tr>
    <th><b>Braze 오브젝트</b></th>
    <th><b>Braze 필드</b></th>
    <th><b>CRM 오브젝트(Salesforce)</b></th>
    <th><b>CRM 필드(Salesforce)</b></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td rowspan="4">카탈로그 &gt; 계정 카탈로그</td>
    <td><code>id</code></td>
    <td><code>account</code></td>
    <td><code>id</code></td>
  </tr>
  <tr>
    <td><code>AccountName</code></td>
    <td><code>account</code></td>
    <td><code>Account Name</code></td>
  </tr>
  <tr>
    <td><code>Type</code></td>
    <td><code>account</code></td>
    <td><code>Type</code></td>
  </tr>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>account</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
  </tbody>
</table>

{% endsubtab %}
{% subtab Opportunity catalog %}

이 사용 사례에서는 Salesforce가 예시 CRM 시스템입니다. CRM의 오브젝트에 포함된 모든 필드에 매핑할 수 있습니다.

<table aria-label="매핑된 계정 필드 예시 테이블" border="1">
  <caption>매핑된 계정 필드 예시 테이블</caption>
  <thead>
  <tr>
    <th><b>Braze 오브젝트</b></th>
    <th><b>Braze 필드</b></th>
    <th><b>CRM 오브젝트(Salesforce)</b></th>
    <th><b>CRM 필드(Salesforce)</b></th>
  </tr>
  </thead>
  <tbody>
  <tr>
    <td rowspan="4">카탈로그 &gt; 기회 카탈로그</td>
    <td><code>id</code></td>
    <td><code>opportunity</code></td>
    <td><code>id</code></td>
  </tr>
  <tr>
    <td><code>OpportunityName</code></td>
    <td><code>opportunity</code></td>
    <td><code>Opportunity Name</code></td>
  </tr>
  <tr>
    <td><code>Territory</code></td>
    <td><code>opportunity</code></td>
    <td><code>Territory</code></td>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>opportunity</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
  </tr>
  </tbody>
</table>

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Connected sources %}

### 옵션 2: 계정 및 기회에 연결된 소스 사용 {#option-2-use-connected-sources-for-accounts-and-opportunities}

연결된 소스는 사용자의 데이터 웨어하우스에 호스팅되고 Braze [CDI 세그먼트 확장]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments)에 의해 쿼리되는 데이터 테이블입니다. 카탈로그와 달리, 비즈니스 오브젝트(계정 및 기회)를 Braze에 복제하는 대신 데이터 웨어하우스에 보관하고 웨어하우스를 신뢰할 수 있는 소스로 사용하게 됩니다.

연결된 소스를 설정하려면 [연결된 소스 통합하기]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/connected_sources#integrating-connected-sources)를 참조하세요.

{% endtab %}
{% endtabs %}

## 2단계: 비즈니스 오브젝트를 고객 프로필과 연결 {#step-2-relate-your-business-objects-to-user-profiles}

고객 프로필은 대부분의 인구통계학적 세분화, 트리거링 및 개인화를 지원하는 Braze의 주요 오브젝트입니다. 고객 프로필에는 SDK 및 기타 소스에서 수집한 [기본 사용자 데이터]({{site.baseurl}}/user_guide/data/unification/user_data)와 속성(인구통계 데이터), 이벤트(행동 데이터) 또는 구매(트랜잭션 데이터)의 형태를 취하는 [커스텀 데이터]({{site.baseurl}}/user_guide/data/activation)가 포함됩니다.

### 2.1단계: 영업 CRM ID를 Braze에 매핑 {#step-21-map-sales-crm-ids-to-braze}

먼저, Braze와 선택한 CRM에 데이터를 공유할 수 있는 공통 식별자가 있는지 확인합니다. 다음 표를 사용하여 영업 CRM ID 필드를 Braze 사용자 오브젝트에 다시 매핑하는 것을 권장합니다. 아래 표에는 Salesforce가 CRM 시스템으로 표시되어 있지만 이 작업은 모든 CRM에서 수행할 수 있습니다.

#### Braze 오브젝트: User {#braze-object-user}

| Braze 필드 | CRM 오브젝트(Salesforce) | CRM 필드(Salesforce) | 추가 정보 |
| --- | --- | --- | --- |
| `Aliases.salesforce_lead_id` | Lead | `id` | - 사용자 별칭 라벨: `salesforce_lead_id` <br>- 사용자 별칭 이름: `lead_id` |
| `Aliases.salesforce_contact_id` | Contact | `id` | - 사용자 별칭 라벨: `salesforce_contact_id` <br>- 사용자 별칭 이름: `contact_id` |
| `AccountId` | Contact | `AccountId` |
| `OpportunityId` (선택 사항, 스칼라) <br>또는<br> `Opportunities` (선택 사항, 배열) | Opportunity | `id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Braze 오브젝트: User" }

{% alert note %}
`external_id` 대신 [별칭]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases)을 사용하여 Salesforce 리드 및 연락처 식별자를 Braze에 다시 매핑하는 것을 권장합니다. 제품 주도 성장 스타일 이니셔티브를 식별하고 실행할 때 필요한 조회 횟수를 줄일 수 있기 때문입니다.
{% endalert %}

ID를 동기화한 후에는 Braze 고객 프로필을 비즈니스 오브젝트와 연결해야 합니다.

### 2.2단계: 고객 프로필과 비즈니스 오브젝트 간의 관계 만들기 {#step-22-create-a-relationship-between-user-profiles-and-your-business-objects}

{% tabs %}
{% tab Catalogs %}

#### 옵션 1: 카탈로그를 사용할 때 {#option-1-when-using-catalogs}

이제 기회 및 계정 세부 정보가 Braze 카탈로그로 반영되었으므로 이러한 카탈로그와 메시지를 보내려는 고객 프로필 간에 관계를 만들어야 합니다. 현재 이 작업을 수행하려면 두 단계가 필요합니다:

1. 고객 프로필에 계정(예: `account_id (string)`), 기회 ID(예: `opportunity_ids (array)`) 또는 둘 다를 속성으로 포함시킵니다.
2. 이벤트 속성정보로 계정 ID가 포함된 이벤트(예: `account_linked`)를 기록합니다.

```json
{
  "attributes" : [
    {
      "external_id" : "user1",
      "accountId" : "001J7000004K7AF",
      "opportunityIds" : [
"0064J000004EU59",
"0064J000004EU5G"
]
    }
  ],
  "events" : [
    {
      "external_id" : "user1",
      "name" : "account_linked",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "account_id": "001J7000004K7AF"
      }
    }
  ]
}
```

{% endtab %}
{% tab Connected sources %}

#### 옵션 2: 연결된 소스를 사용하는 경우 {#option-2-when-using-connected-sources}

연결된 소스의 테이블 중 하나에 사용자를 위해 Braze에서 설정한 `external_user_id`와 일치하는 `user_id`가 포함되어야 합니다. 위의 고객 프로필 설정에서는 리드와 `contact_ids`를 `external_id`로 사용하므로 리드/연락처 테이블에 이러한 ID가 포함되어 있는지 확인해야 합니다.

ID가 일치하는지 확인하는 것 외에도 효율적인 세분화 및 개인화를 위해 `account_id`, `opportunity_id`와 같은 기본 계정 수준 데이터와 `industry`와 같은 일반적인 기업 속성까지 고객 프로필에 기록하는 것을 권장합니다.

{% endtab %}
{% endtabs %}