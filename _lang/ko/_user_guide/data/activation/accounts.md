---
nav_title: 계정
article_title: 계정 오브젝트
page_order: 7
page_type: reference
description: "계정 오브젝트를 사용하여 사용자를 세분화하고, 계정 데이터로 메시지를 개인화하며, 계정 레코드를 관리하세요."
---

# 계정 오브젝트 {#account-objects}

> 계정 오브젝트를 사용하여 계정 데이터로 세분화하고 메시징을 개인화하세요.

{% alert important %}
계정은 얼리 액세스 단계입니다. 기능이 발전함에 따라 이 안내 사항이 변경될 수 있습니다.
{% endalert %}

계정 오브젝트를 사용하면 다음을 수행할 수 있습니다.

- 계정 기준으로 Segments 구축
- Liquid를 통해 계정 속성으로 메시지 개인화
- 한 곳에서 계정 레코드 관리

계정 오브젝트는 사용자 프로필에 연결된 워크스페이스 수준의 데이터 모델입니다. 계정 레코드는 하나의 특정 계정과 관련 필드 데이터입니다.
회사 속성과 같은 계정 컨텍스트가 메시징 타겟팅 및 개인화에 도움이 될 때 계정 오브젝트를 사용하세요.
계정 계층 구조(예: 상위 및 하위 계정)를 모델링하고 하나의 사용자 프로필을 여러 계정에 연결할 수도 있습니다.

## 계정 오브젝트를 사용하는 이유 {#why-use-account-objects}

일부 사용 사례에서는 Campaigns와 Canvases가 개별 사용자에게 전송되더라도 계정 수준의 컨텍스트가 필요합니다.

계정 오브젝트를 사용하면 계정 데이터를 한 번 저장하고 Braze 전체에서 세분화 및 개인화에 재사용할 수 있습니다.

이를 통해 다음을 수행할 수 있습니다.

- 계정 속성별로 세분화
- 공유 계정 컨텍스트(예: 회사명 또는 산업)로 메시지 개인화
- 계정 간 관계를 모델링하고 하나의 사용자 프로필을 여러 계정에 연결

이 접근 방식은 동일한 계정 속성을 여러 사용자 프로필에 중복 저장하는 것을 대체합니다.

## 전제 조건 {#prerequisites}

시작하기 전에:

- 워크스페이스에서 계정 얼리 액세스가 활성화되어 있어야 합니다. Braze 계정 팀에 문의하세요.
- Braze에 사용자가 이미 등록되어 있어야 합니다.
- 계정이 활성화되면 **데이터 설정** > **계정**에 표시됩니다. 계정을 처음 사용하는 경우 화면의 초기화 안내를 따르세요.

## 계정 데이터 모델 {#account-data-model}

각 계정에는 외부 ID(`id`)와 이름(`name`)이 필요합니다.

이 섹션의 계정 필드는 계정 오브젝트 스키마를 정의합니다. 이러한 필드는 Braze에 저장하는 모든 개별 계정 레코드에 적용됩니다.

Braze는 기본적으로 표준 필드가 포함된 계정 오브젝트를 제공합니다. 사용 사례에 따라 커스텀 필드를 추가하거나 제거할 수 있습니다.

| 필드 이름 | 필드 유형 | 필수 | 설명 |
| --- | --- | --- | --- |
| `id` | 문자열 | 예 | 계정의 시스템 ID(예: CRM ID). 워크스페이스 내에서 고유해야 합니다. |
| `name` | 문자열 | 예 | 계정 이름. |
| `type` | 문자열 | 아니요 | 계정 유형(예: 고객, 파트너, 리셀러). |
| `annual_revenue` | 숫자 | 아니요 | 계정 연간 매출. |
| `industry` | 문자열 | 아니요 | 계정 산업. |
| `number_of_employees` | 숫자 | 아니요 | 직원 수. |
| `address` | 문자열 | 아니요 | 도로명 주소. |
| `city` | 문자열 | 아니요 | 구/군/시. |
| `state` | 문자열 | 아니요 | 시/도. |
| `postal_code` | 문자열 | 아니요 | 우편번호. |
| `country` | 문자열 | 아니요 | 국가. |
| `notes` | 문자열 | 아니요 | 추가 메모. |
| `website` | 문자열 | 아니요 | 웹사이트 URL. |
| `main_phone` | 문자열 | 아니요 | 대표 전화번호. |
| `created_date` | 시간 | 아니요 | 계정 생성 타임스탬프. |
| `sic_code` | 문자열 | 아니요 | 표준 산업 분류 코드. |
| 커스텀 필드 | 커스텀 | 아니요 | 사용자가 정의하고 관리하는 필드. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="계정 데이터 모델 필드" }

## 데이터 통합 옵션 {#data-integration-options}

다음을 통해 계정 레코드를 관리할 수 있습니다.

- 계정 레코드용 REST API 엔드포인트
- **데이터 설정** > **계정**에서 개별 레코드의 브라우저 내 편집

## 시작하기 {#get-started}

### 1단계: 계정 활성화 {#step-1-enable-accounts}

계정은 회사 수준에서 활성화됩니다. 얼리 액세스 기간 동안 Braze 계정 팀이 일회성 활성화를 처리합니다.

계정이 활성화되면 **데이터 설정** > **계정**으로 이동하여 메시지가 표시되면 일회성 초기화 플로우를 완료하세요.

### 2단계: 계정 레코드 추가 {#step-2-add-account-records}

REST API 또는 브라우저 내 편집을 통해 계정 레코드를 추가하거나 업데이트하세요.

### 3단계: 계정 기준에 대한 계산된 필터 생성 {#step-3-create-a-calculated-filter-for-account-criteria}

계정 데이터로 세분화하기 전에 계정 기준을 정의하는 계산된 필터를 생성하세요. 자세한 내용은 [계산된 필터 작동 방식]({{site.baseurl}}/user_guide/audience/segments/calculated_filters#how-it-works)을 참조하세요.

### 4단계: Segment 빌더에서 계산된 필터 사용 {#step-4-use-the-calculated-filter-in-segment-builder}

Segment 빌더에서 생성한 계산된 필터를 선택한 다음, Campaign 또는 Canvas 타겟팅을 지원하는 추가 사용자 속성 필터를 추가하세요.

## 계정 기반 Segments 구축 {#build-account-based-segments}

계정 레코드와 계산된 필터가 준비되면:

1. [Segment 빌더]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment)로 이동합니다.
2. 계정 기준에 대해 미리 구성된 계산된 필터를 추가합니다.
3. 추가 사용자 속성 필터를 추가합니다.
4. Segment를 저장합니다.

예시:

- **계산된 필터:** 계정 `industry`가 정확히 `healthcare`
- **사용자 속성 필터:** `days_since_last_login`이 `30` 미만

## Liquid로 개인화 {#personalize-with-liquid}

`{% raw %}{% data_object account %}{% endraw %}` Liquid 태그를 사용하여 사용자의 계정 데이터를 `data_objects` 배열에 로드하세요.

{% alert note %}
**미리보기 및 테스트**를 사용할 때는 개인화가 올바르게 해석될 수 있도록 계정 데이터가 포함된 Segment를 사용하세요.
{% endalert %}

{% raw %}
```liquid
{% data_object account %}
Hi {{${first_name}}},
We'd love to invite you and your peers at {{ data_objects[0].name }}.
```
{% endraw %}

일치하는 모든 계정을 반복하려면:

{% raw %}
```liquid
{% data_object account %}
{% for acct in data_objects %}
- {{ acct.name }}
{% endfor %}
```
{% endraw %}

## API 기본 사항 {#api-basics}

얼리 액세스 기간 동안 REST API를 사용하여 계정 레코드를 관리할 수 있습니다.

{% alert note %}
계정 엔드포인트에 대한 세부 정보는 얼리 액세스 온보딩 시 제공됩니다. 액세스 또는 온보딩 세부 정보가 필요하면 Braze 계정 팀에 문의하세요.
{% endalert %}

인증 및 REST 엔드포인트 기본 사항은 [Braze API 개요]({{site.baseurl}}/api/basics)를 참조하세요.

## 자주 묻는 질문 {#frequently-asked-questions}

### 계정에 커스텀 필드를 추가할 수 있나요? {#can-i-add-custom-fields-to-accounts}

네. 워크스페이스에서 커스텀 계정 필드를 정의하고 관리할 수 있습니다. 필드 요구 사항은 [계정 데이터 모델](#account-data-model)을 참조하세요.

### 계정은 유료 애드온인가요? {#is-accounts-a-paid-add-on}

아니요. 계정은 유료 애드온이 아니며 모든 플랜에서 사용할 수 있습니다. 얼리 액세스 기간 동안 Braze 계정 팀이 워크스페이스에서 활성화해야 합니다.