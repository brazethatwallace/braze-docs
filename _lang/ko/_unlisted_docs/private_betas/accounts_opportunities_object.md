---
nav_title: 계정 오브젝트
article_title: 계정 오브젝트
page_type: reference
permalink: /account_object/
hidden: true
description: "계정 오브젝트를 사용하여 사용자가 속한 계정을 기반으로 세그먼트를 구축한 다음, Liquid 태그를 사용하여 개인화된 메시지를 보내는 방법을 알아보세요."
---

# 계정 오브젝트 {#account-objects}

> 계정 오브젝트를 사용하여 사용자가 속한 계정을 기반으로 세그먼트를 구축한 다음, Liquid 태그를 사용하여 개인화된 메시지를 보내는 방법을 알아보세요.

계정 데이터를 가져오려면 [CSV 파일](#using-a-csv-file) 또는 Braze API를 사용하세요. Braze API를 사용하면 [여러 계정 생성](#create-multiple-accounts), [단일 계정 생성](#create-one-account), [여러 계정 삭제](#delete-multiple-accounts), [단일 계정 삭제](#delete-one-account)가 가능합니다.

| 오디언스 | 이 문서의 활용 방법 |
|----------|----------------------------|
| 마케터 | CSV를 사용하여 사용자 및 계정 데이터를 가져오고, 계정 속성을 기반으로 세그먼트를 구축하며, Braze에서 계정 정보로 메시지를 개인화합니다. |
| 개발자 | Braze REST API를 사용하여 계정 레코드를 프로그래밍 방식으로 생성, 업데이트, 삭제하고 Braze를 데이터와 동기화 상태로 유지합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
계정 오브젝트는 현재 베타 버전입니다. 이 베타에 참여하고 싶으시면 Braze 계정 매니저에게 문의하세요.
{% endalert %}

## 작동 방식 {#how-it-works}

계정 오브젝트는 사용자의 회사를 나타내는 커스텀 데이터 구조입니다. 고객 프로필에 연결되므로 B2B 스타일의 세그먼트를 구축하고 메시지를 개인화할 수 있습니다. 회사 이름, 산업, 역할, 거래 상태와 같은 계정 필드를 Braze 카탈로그, 세분화 필터, Liquid 태그와 함께 사용하세요.

예를 들어, 의료 분야에서 일하는 사용자를 타겟팅하고 의사와 병원 관리자에게 개인화된 메시지를 보내 메시지의 관련성을 더욱 높일 수 있습니다.

계정 오브젝트를 사용하려면 세 가지 유형의 데이터를 Braze로 가져와야 합니다:

- **사용자 데이터:** Braze에서 각 사람을 식별하는 데 사용되는 개별 고객 프로필(예: `external_id`, 이메일, 전화번호 또는 사용자 별칭을 통해). CSV를 통해 사용자 데이터를 가져옵니다.
- **사용자-계정 관계 데이터:** 사용자와 계정 간의 관계로, 사용자가 속한 회사와 해당 계정에서의 역할을 포함합니다. CSV를 통해 이 관계 데이터를 가져옵니다.
- **계정 데이터:** 회사 이름, 산업, 연간 매출 및 기타 기업 정보와 같은 회사 레코드 자체입니다. 세그먼트와 메시지에서 타겟팅하고 개인화하는 데 사용하는 레코드입니다. CSV 또는 Braze REST API를 통해 계정 데이터를 가져옵니다.

계정 오브젝트가 작동하려면 세 가지 데이터 유형을 모두 가져와야 합니다. 사용자 데이터는 Braze에서 사람을 식별하고, 사용자-계정 관계 데이터는 해당 사용자를 특정 계정 및 역할에 연결하며, 계정 데이터는 세분화 및 개인화에 사용되는 회사 수준의 속성을 제공합니다.

## 필수 조건 {#prerequisites}

이 기능을 사용하려면 Braze에 이미 사용자가 있어야 합니다.

## Braze로 데이터 가져오기 {#import-data-to-braze}

메시지 내에서 계정 오브젝트를 사용하려면 사용자 데이터가 이미 Braze에 존재해야 합니다. 그런 다음 두 가지 가져오기를 완료하세요: 먼저 사용자-계정 관계 데이터를 가져와 계정 연결 및 역할을 설정합니다(현재 CSV만 지원). 그런 다음 세분화 및 개인화에 사용되는 회사 수준의 세부 정보가 포함된 계정 데이터를 가져옵니다(CSV 또는 Braze REST API를 통해).

### 1단계: 사용자-계정 관계 데이터 가져오기 {#step-1-import-user-account-relationship-data}

먼저 다음 필드가 포함된 CSV 파일로 사용자-계정 관계 데이터를 Braze에 가져옵니다. 이를 통해 Braze가 기존 사용자를 올바른 계정 및 역할과 연결할 수 있습니다.

<style>
table td {
    word-break: break-word;
}
</style>

| 필드 이름 | 필드 유형 | 필수 | 설명 |
|------------------|------------|----------|-------------------------------------------------------------------------------------------------------|
| `account_id`       | 문자열     | 예      | 사용자가 속한 계정입니다. 계정 오브젝트의 `id` 필드(CRM ID)와 동일합니다. |
| `external_id`      | 문자열     | 예      | Braze에서의 사용자 [외부 ID](https://www.braze.com/user_guide/data/user_data_collection/user_profile_lifecycle/#identified-user-profiles)입니다. |
| `user_alias_name`  | 문자열     | 아니요*      | Braze에서의 사용자 [별칭 이름](https://www.braze.com/user_guide/data/user_data_collection/user_profile_lifecycle#user-aliases)입니다. |
| `user_alias_label` | 문자열     | 아니요*      | Braze에서의 사용자 [별칭 라벨](https://www.braze.com/user_guide/data/user_data_collection/user_profile_lifecycle/#what-happens-when-you-identify-anonymous-users)입니다. |
| `email`            | 문자열     | 아니요*     | 사용자의 이메일 주소입니다. |
| `phone`            | 문자열     | 아니요*      | 사용자의 전화번호입니다. |
| `user_role`             | 문자열     | 아니요       | 사용자가 계정에서 맡은 역할(예: "director" 또는 "employee")입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }
<sup>사용자를 식별하려면 `external_id`, `email`, `phone` 또는 `user_alias` 중 하나가 필요합니다.</sup>

#### CSV 파일 사용하기 {#using-a-csv-file}

사용자-계정 관계가 포함된 CSV를 Braze에 업로드합니다:

1. **데이터 설정** > **계정**으로 이동합니다.
2. **데이터 업데이트**를 선택합니다.
3. **CSV 업로드**에서 **사용자**를 선택한 다음 파일을 Braze에 업로드합니다.

![Braze의 '계정' 페이지에 있는 '데이터 업로드' 드롭다운]({% image_buster /assets/unlisted_docs/img/account_opportunity_object/update_account_data_csv.png %})

### 2단계: 계정 데이터 가져오기 {#step-2-import-account-data}

계정은 사용자가 속한 회사입니다. 다음 필드가 포함된 CSV 파일로 계정 데이터를 Braze에 가져옵니다. 각 계정에는 ID와 이름이 할당되어야 합니다.

<style>
table td {
    word-break: break-word;
}
</style>

| 필드 이름 | 필드 유형 | 필수 | 설명 |
|-----------------------------|------------|----------|------------------------------------------------------------------------------------|
| `id`                          | 문자열     | 예      | 고객 관계 관리(CRM) 플랫폼에서의 계정 ID입니다. |
| `name`                        | 문자열     | 예      | 계정의 이름입니다. |
| `type`                        | 문자열     | 아니요       | 계정 유형(예: 고객, 파트너 또는 리셀러)입니다. |
| `annual_revenue`              | 문자열     | 아니요       | 계정의 연간 매출입니다. |
| `industry`                    | 문자열     | 아니요       | 계정이 운영되는 산업입니다. |
| `number_of_employees`         | 문자열     | 아니요       | 직원 수이며, 범위를 지원합니다. |
| `address`                     | 문자열     | 아니요       | 계정의 도로 주소입니다. |
| `city`                        | 문자열     | 아니요       | 계정이 위치한 도시입니다. |
| `state`                       | 문자열     | 아니요       | 계정이 위치한 주입니다. |
| `postal_code`                 | 문자열     | 아니요       | 계정 주소의 우편번호입니다. |
| `country`                     | 문자열     | 아니요       | 계정이 위치한 국가입니다. |
| `notes`                       | 문자열     | 아니요       | 계정에 대한 추가 메모입니다. |
| `website`                     | 문자열     | 아니요       | 계정의 웹사이트 URL입니다. |
| `main_phone`                  | 문자열     | 아니요       | 계정의 대표 전화번호입니다. |
| `created_date`                | 시간       | 아니요       | 계정이 생성된 날짜입니다. |
| `account_owner_email_address` | 문자열     | 아니요       | 내부 계정 소유자(예: "회사 A 영업팀의 Tom이 회사 B를 담당")입니다. |
| `parent_account_id`           | 문자열     | 아니요       | 해당하는 경우 상위 계정의 ID(예: 모회사 ID에 연결)입니다. |
| `sic_code`                    | 문자열     | 아니요       | 표준 산업 분류 코드입니다. |
| 커스텀 필드                 | N/A        | 아니요       | 사용자가 정의하고 관리하는 커스텀 필드입니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }
{% alert note %}
일부 필드는 선택 사항이지만, 예약된 필드 이름이므로 데이터를 체계적으로 유지하는 데 도움이 되므로 가능하면 포함하세요.
{% endalert %}

다음으로, CSV 파일을 업로드하거나 Braze REST API를 사용하여 계정 데이터를 Braze에 가져옵니다. 이 데이터는 **데이터 설정**에서 확인할 수 있습니다. 브라우저 내 편집기에서는 이 데이터를 편집할 수 없습니다.

#### CSV 파일 사용하기

CSV를 통해 데이터를 가져오려면:

1. **데이터 설정** > **계정**으로 이동합니다.
2. **데이터 업데이트**를 선택합니다.
3. **CSV 업로드**에서 **계정 데이터**를 선택한 다음 파일을 Braze에 업로드합니다.

![Braze의 '계정' 페이지에 있는 '데이터 업로드' 드롭다운]({% image_buster /assets/unlisted_docs/img/account_opportunity_object/update_account_data_csv.png %})

## Braze API 사용하기 {#using-the-braze-api}

API(Application Programming Interface)를 사용하면 서로 다른 소프트웨어 시스템이 프로그래밍 방식으로 통신할 수 있습니다. Braze API와 상호작용할 때 특정 엔드포인트에 HTTP 요청을 보냅니다. 엔드포인트는 지시를 받아들이고 응답을 반환하는 구조화된 URL입니다. HTTP 메서드는 Braze에 수행할 동작을 알려주고, 요청 본문에는 데이터가 포함됩니다.

계정 관리를 위해 Braze API는 다음 HTTP 메서드를 사용합니다:

| 메서드 | 목적 | 동작 |
|--------|---------|----------|
| `PUT` | 리소스 생성 또는 업데이트 | 존재하지 않는 경우 새 계정 레코드를 추가합니다. 존재하는 경우 기존 레코드를 업데이트합니다. `PUT`은 멱등성을 갖도록 설계되어 동일한 데이터를 여러 번 동기화해도 중복이 생성되지 않습니다. |
| `DELETE` | 리소스 제거 | 지정된 계정 레코드와 해당 연결을 Braze에서 영구적으로 제거합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Braze API를 사용하면 대규모로 계정 데이터를 프로그래밍 방식으로 제어할 수 있습니다. 계정 관리 워크플로를 자동화하고, 데이터 소스에서 직접 계정 정보를 동기화하며, 수동 업로드나 편집 없이 Braze를 신뢰할 수 있는 소스와 일치시킬 수 있습니다. 이를 통해 운영 오버헤드를 줄이고 세분화 및 개인화를 위한 정확하고 시의적절한 계정 데이터를 유지할 수 있습니다.

HTTP 메서드와 REST API 작동 방식에 대한 자세한 내용은 다음 리소스를 참조하세요:
- MDN Web Docs의 [HTTP 요청 메서드](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods)
- [REST API 튜토리얼](https://restapitutorial.com/)
- [Braze API 개요](https://www.braze.com/docs/api/basics)

{% alert note %}
`/business/accounts` 엔드포인트에 대한 요청을 인증하려면 카탈로그 권한이 있는 API 키를 사용하세요.
{% endalert %}

이 섹션에서는 Braze API를 사용하여 다음을 수행하는 방법을 다룹니다:
- [여러 계정 생성](#create-multiple-accounts)
- [단일 계정 생성](#create-one-account)
- [여러 계정 삭제](#delete-multiple-accounts)
- [단일 계정 삭제](#delete-one-account)

### 여러 계정 생성 {#create-multiple-accounts}

`PUT`은 멱등성을 가지므로 동일한 요청을 여러 번 보내도 Braze는 중복을 생성하지 않고 기존 레코드를 업데이트합니다. 따라서 Braze의 계정 레코드를 최신 상태로 유지하는 데 안정적인 선택입니다.

다음 코드 스니펫은 `/business/accounts` 엔드포인트에 `PUT` 요청을 보냅니다. `accounts` 배열에는 여러 회사 오브젝트가 포함되어 있으며, 각각 [2단계: 계정 데이터 가져오기](#step-2-import-account-data)에서 정의된 계정 필드에 매핑됩니다. Braze는 각 오브젝트를 처리하고 **계정** 페이지에서 해당 레코드를 생성하거나 업데이트합니다. 이 작업은 비동기적입니다. Braze는 요청을 대기줄에 넣고 백그라운드에서 처리하므로, 즉각적인 확인이 필요하지 않은 대량 가져오기에 적합합니다.

여러 계정을 생성하려면 `/business/accounts`에 `PUT` 요청을 보냅니다. 계정이 존재하지 않으면 Braze가 **계정** 페이지에 새 항목을 추가합니다. 각 요청은 최대 50개의 계정을 지원할 수 있습니다. 이 작업은 비동기적입니다.

요청은 다음과 유사해야 합니다:

```plaintext
curl -X PUT https://YOUR_REST_API_URL/business/accounts \
  -H "Authorization: Bearer YOUR-REST-API-KEY" \
  -H "Content-Type: application/json" \
  -d '{
          "accounts": [
              {
                  "id": "ACC001",
                  "name": "Acme Corporation",
                  "type": "Customer",
                  "annual_revenue": "$5,000,000",
                  "industry": "Manufacturing",
                  "number_of_employees": "150",
                  "address": "123 Industrial Way",
                  "city": "Metropolis",
                  "state": "NY",
                  "postal_code": "10001",
                  "country": "USA",
                  "notes": "Key client in the manufacturing sector",
                  "website": "http://www.acme.com",
                  "main_phone": "+1-212-555-1234",
                  "created_date": "2023-01-15T09:30:00Z",
                  "account_owner_email_address": "owner@acme.com",
                  "parent_account_id": "",
                  "sic_code": "2011"
              },
              {
                  "id": "ACC002",
                  "name": "Global Solutions",
                  "type": "Partner",
                  "annual_revenue": "$10,000,000",
                  "industry": "Technology",
                  "number_of_employees": "500",
                  "address": "456 Tech Park",
                  "city": "Silicon Valley",
                  "state": "CA",
                  "postal_code": "94043",
                  "country": "USA",
                  "notes": "Important partner for software solutions",
                  "website": "http://www.globalsolutions.com",
                  "main_phone": "+1-650-555-5678",
                  "created_date": "2023-02-20T14:45:00Z",
                  "account_owner_email_address": "partner@globalsolutions.com",
                  "parent_account_id": "ACC001",
                  "sic_code": "7372"
              },
              {
                  "id": "ACC003",
                  "name": "Oceanic Ventures",
                  "type": "Customer",
                  "annual_revenue": "$3,200,000",
                  "industry": "Retail",
                  "number_of_employees": "75",
                  "address": "789 Ocean Blvd",
                  "city": "Miami",
                  "state": "FL",
                  "postal_code": "33101",
                  "country": "USA",
                  "notes": "Expanding presence in retail markets",
                  "website": "http://www.oceanicventures.com",
                  "main_phone": "+1-305-555-6789",
                  "created_date": "2023-03-05T08:15:00Z",
                  "account_owner_email_address": "contact@oceanicventures.com",
                  "parent_account_id": "",
                  "sic_code": "5941"
              }
          ]
      }'
```

### 단일 계정 생성 {#create-one-account}

여러 계정 생성과 마찬가지로 이 작업은 `PUT` 메서드를 사용합니다. 차이점은 계정 ID가 요청 본문이 아닌 엔드포인트 URL에 직접 포함된다는 것입니다. 이를 통해 단일 레코드를 정밀하게 제어할 수 있습니다.

다음 코드 스니펫은 `/business/accounts/ACC001`에 `PUT` 요청을 보내며, 여기서 `ACC001`은 계정의 고유 식별자입니다. 이 작업은 동기적입니다. Braze는 요청을 즉시 처리하고 완료되는 즉시 응답을 반환합니다. 이는 실시간 통합에 적합합니다. 예를 들어, 시스템에서 계정 정보가 변경되면 타겟팅이나 개인화를 위해 해당 업데이트를 Braze에 즉시 반영할 수 있습니다.

단일 계정을 생성하려면 `/business/accounts/:account_id`에 `PUT` 요청을 보냅니다. 계정이 존재하지 않으면 Braze가 새 계정 레코드를 생성합니다. 이 작업은 동기적입니다.

요청은 다음과 유사해야 합니다:

```plaintext
curl -X PUT https://YOUR_REST_API_URL/business/accounts/ACC001 \
  -H "Authorization: Bearer YOUR-REST-API-KEY" \
  -H "Content-Type: application/json" \
  -d '{
        "accounts": [
            {
                "name": "Braze",
                "type": "Customer",
                "annual_revenue": "$5,000,000",
                "industry": "Manufacturing",
                "number_of_employees": "150",
                "address": "123 Industrial Way",
                "city": "Metropolis",
                "state": "NY",
                "postal_code": "10001",
                "country": "USA",
                "notes": "Key client in the manufacturing sector",
                "website": "http://www.acme.com",
                "main_phone": "+1-212-555-1234",
                "created_date": "2023-01-15T09:30:00Z",
                "account_owner_email_address": "owner@acme.com",
                "parent_account_id": "",
                "sic_code": "2011"
            }
        ]
      }'
```

### 여러 계정 삭제 {#delete-multiple-accounts}

`DELETE` 메서드는 Braze에서 계정 레코드를 제거합니다. `PUT`과 달리 `DELETE` 요청은 되돌릴 수 없습니다. 계정이 삭제되면 사용자와 해당 계정 간의 연결이 제거됩니다.

다음 코드 스니펫은 요청 본문에 계정 ID 목록을 포함하여 `/business/accounts`에 `DELETE` 요청을 보냅니다. Braze는 각 ID를 처리하고 해당 계정 레코드를 제거합니다. 이 작업은 비동기적입니다. Braze는 제거를 대기줄에 넣고 백그라운드에서 처리합니다. 계정 그룹이 이탈했거나, 통합되었거나, Braze에서 세분화에 더 이상 관련이 없는 경우와 같은 대량 정리 작업에 사용하세요.

여러 계정을 삭제하려면 계정 ID 목록이 포함된 본문과 함께 `/business/accounts`에 `DELETE` 요청을 보냅니다. 이 작업은 비동기적입니다.

요청은 다음과 유사해야 합니다:

```plaintext
curl -X DELETE https://YOUR_REST_API_URL/business/accounts \
  -H "Authorization: Bearer YOUR-REST-API-KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "accounts": [
      { "id": "ACC001" },
      { "id": "ACC002" },
      { "id": "ACC003" }
    ]
  }'
```

### 단일 계정 삭제 {#delete-one-account}

단일 계정 생성과 마찬가지로 이 작업은 엔드포인트 URL에 ID를 직접 포함하여 특정 계정을 대상으로 합니다. 이를 통해 다른 레코드에 영향을 주지 않고 단일 레코드를 정밀하게 제어할 수 있습니다.

다음 코드 스니펫은 `/business/accounts/ACC001`에 `DELETE` 요청을 보냅니다. 이 작업은 동기적입니다. Braze는 요청을 즉시 처리하고 완료되는 즉시 응답을 반환합니다. 개별 계정이 폐쇄되었거나, 병합되었거나, 규정 준수 또는 데이터 위생 목적으로 Braze에서 제거해야 하는 경우에 사용하세요.

단일 계정을 삭제하려면 `/business/accounts/:account_id`에 `DELETE` 요청을 보냅니다. 이 작업은 동기적입니다.

요청은 다음과 유사해야 합니다:

```plaintext
curl -X DELETE https://YOUR_REST_API_URL/business/accounts/ACC001 \
  -H "Authorization: Bearer YOUR-REST-API-KEY"
```

## 메시지에서 오브젝트 사용하기 {#using-objects-in-messages}

[Braze로 데이터를 가져온](#importing-data-to-braze) 후, 계정 오브젝트를 사용하여 세그먼트를 구축하고 Liquid를 사용하여 사용자에게 개인화된 메시지를 보낼 수 있습니다.

### 1단계: 세그먼트 구축 {#step-1-build-a-segment}

다음으로, 사용자 데이터와 계정 데이터를 결합하는 세그먼트를 구축합니다. 이 예시에서는 건강 프로모션 회사에서 새 웨비나 등록을 늘리기 위해 의료 회사의 디렉터를 타겟팅합니다.

1. **오디언스** > **Segments**로 이동한 다음 **세그먼트 생성**을 선택합니다.
2. 세그먼트에 이름을 지정합니다.
3. **세그먼트 빌더**에서 **비즈니스** 필터를 선택하고 다음 세분화 필터를 설정합니다. 완료되면 **저장**을 선택합니다.

| 필터 | 설명 |
|---------------------------------|--------------------------------------------------|
| `Role is exactly director`      | 역할이 정확히 Director인 사용자를 타겟팅합니다 |
| `Accounts industry matches regex healthcare` | 의료 관련 산업의 계정에 속한 사용자를 매칭합니다 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
현재 여러 계정 필터를 사용하려면 **OR/AND** 드롭다운 대신 **기준 추가**를 선택하세요.
{% endalert %}

![의료 회사의 디렉터인 사용자를 위한 세그먼트를 생성하도록 설정된 세분화 필터]({% image_buster /assets/unlisted_docs/img/account_opportunity_object/build_segment.png %})

{% alert note %}
세분화는 기준에 일치하는 처음 1,000개의 계정 레코드에서만 작동합니다. 세그먼트당 최대 하나의 비즈니스 필터를 사용할 수 있으며, 모든 기준은 하나의 필터 안에 있어야 합니다.
{% endalert %}

### 2단계: Liquid를 사용하여 개인화하기 {#step-2-use-liquid-to-personalize}

이제 메시지를 개인화하여 사용자에게 기회에 대한 정보를 보낼 수 있습니다. 이 예시에서는 디렉터에게 메시지를 작성하고 웨비나에 연결합니다. Braze 카탈로그를 사용하여 개인화를 위한 산업별 이미지를 가져올 수도 있습니다.

#### 2.1단계: 계정 정보로 개인화하기 {#step-21-personalize-with-account-information}

개인화 유형으로 **비즈니스**를 선택한 다음 **이름**을 선택하여 사용자의 회사 이름으로 메시지를 개인화합니다.

다음이 클립보드에 복사됩니다.

{% raw %}
```javascript
{% business %}
{{ business_accounts[0].name }}
```
{% endraw %}

Braze는 {% raw %}`{% business %}`{% endraw %} 태그를 생성하며, 이 태그는 연결된 계정의 계정 정보를 포함하는 `business_accounts`라는 배열을 설정합니다.

자동 생성된 출력을 조정하여 메시지를 작성합니다.

아래 예시에서는 {% raw %}`{% business %}`{% endraw %} 태그 호출을 메시지 상단으로 이동하고 사용자의 이름으로 개인화합니다. 계정 이름을 사용하여 메시지를 개인화합니다. Liquid 출력은 동일하지만 메시지의 다른 부분에 배치합니다.

{% raw %}
```javascript
{% business %}

Hi {{${first_name}}},

We would love to invite you and your peers at {{ business_accounts[0].name }} to join our latest webinar named "Creating Optimal Health Outcomes for Patients".  Click the link below to register.
```
{% endraw %}

출력은 다음과 유사합니다:

{% raw %}
```javascript
Hi John,

We would love to invite you and your peers at Sunshine Health to join our latest webinar named "Creating Optimal Health Outcomes for Patients". Click the link below to register.
```
{% endraw %}

#### 2.2단계: 카탈로그와 연결하기 {#step-22-connect-with-catalogs}

다음으로, Braze 카탈로그를 사용하여 의료 회사에 해당하는 이미지를 추가하고 저장하여 메시지를 더욱 개인화합니다.

이 예시에서는 다음이 있다고 가정합니다:

- `industry_assets`라는 카탈로그가 설정되어 있음
- 각 카탈로그 항목의 ID는 계정의 산업에 해당하는 산업 이름임
- 기본 이미지와 보조 이미지에 대한 이미지 URL 링크

다음은 이 개인화에 사용되는 Liquid의 예시입니다.
{% raw %}
```javascript
//Make a call to the business tag.  This sets the accounts array and prepares us to pull account data out.
{% business %}

//Assign the user's accounts industry to a variable called industry.  This step isn't required but it makes everything easier to read.
{% assign industry = {{business_accounts[0].industry}} %}

//Make a catalog_items call to the industry_assets catalog and ask for the industry item (in this case, it will ask for "healthcare")
{% catalog_items industry_assets industry %}

// Get the hero image for the "healthcare" industry
{{items[0].hero_image}}
```
{% endraw %}

## 자주 묻는 질문(FAQ) {#faq}

### 커스텀 필드를 추가할 수 있나요? {#can-i-add-custom-fields}

네. 계정에 커스텀 필드를 추가할 수 있습니다. 자체 리드 스코어링 방법이 있는 경우, 계정 오브젝트의 커스텀 필드를 사용하여 이를 추적할 수도 있습니다.

### 사용자가 둘 이상의 계정에 연결될 수 있나요? {#can-a-user-be-associated-with-more-than-one-account}

아니요. 현재 각 사용자는 하나의 계정 연결만 가질 수 있습니다.

### 하나의 고객 프로필에 여러 이메일을 포함할 수 있나요? {#can-one-user-profile-contain-multiple-emails}

아니요. 고객 프로필에는 개인 이메일과 업무 이메일 등 둘 이상의 이메일을 포함할 수 없습니다.