---
nav_title: Scuba
article_title: Scuba Analytics
description: "이 Scuba와 Braze 기술 참조 문서에서는 Braze Segments를 사용하여 Scuba의 실시간 데이터 인사이트를 활성화하는 방법을 설명합니다."
page_type: partner
search_tag: Partner
noindex: true
hidden: true
---

# Scuba Analytics

>[Scuba Analytics](https://scuba.io)는 고속 시계열 데이터를 위해 설계된 풀스택 머신 러닝 기반 데이터 협업 플랫폼입니다. Scuba를 사용하면 사용자(액터라고도 함)를 선택적으로 내보내고 Braze 플랫폼에 로드할 수 있습니다. Scuba에서는 커스텀 액터 속성을 사용하여 행동 트렌드를 분석하고, 다양한 플랫폼에서 데이터를 활성화하며, 머신 러닝을 활용한 예측 모델링을 수행할 수 있습니다.

_이 통합은 Scuba Analytics에서 유지 관리합니다._

## 사전 요구 사항 {#prerequisites}

Braze에서 Scuba Analytics를 사용하려면 다음이 필요합니다.

| 요구 사항 | 설명 |
|---|---|
| Scuba API 토큰 | `https://{scuba_hostname}/api/create_token` 엔드포인트에서 가져올 수 있는 Scuba API 토큰입니다. |
| Braze REST API 키 | `users.track` 권한이 있는 Braze REST API 키입니다. <br><br> Braze 대시보드에서 **설정** > **API 키**로 이동하여 생성할 수 있습니다. |
| Braze REST 엔드포인트 | REST 엔드포인트 URL입니다. 엔드포인트는 [인스턴스에 대한 Braze URL](https://scuba.io)에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="사전 요구 사항" }

## Scuba 데이터를 Braze에 업로드하기 {#uploading-your-scuba-data-to-braze}

{% alert important %}
다음 요청은 curl을 사용합니다. API 요청을 더 효과적으로 관리하려면 Postman과 같은 API 클라이언트를 사용하는 것을 권장합니다.
{% endalert %}

Scuba 데이터를 Braze에 업로드하려면 `application/json` 콘텐츠-유형을 사용하여 `https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation`으로 POST 요청을 보냅니다:

```bash
curl -X POST "https://scuba.pliant.io/a/scuba-connectors/prod/braze-activation" \
-H "content-type: application/json" \
-d '{"braze_host":"BRAZE_API_ENDPOINT", \
"braze_api_key":"BRAZE_API_KEY", \
"scuba_host":"HOSTNAME", \
"scuba_token":"SCUBA_API_TOKEN", \
"scuba_table_name":"TABLE_NAME", \
"scuba_actor_property_name":"ACTOR_PROPERTY_NAME", \
"scuba_actor_property_value_filter":"ACTOR_PROPERTY_FILTER" \
"scuba_actor_id":"ACTOR_ID", \
"scuba_period_start":"PERIOD_START", \
"scuba_period_end":"PERIOD_END", \
"scuba_record_limit":"RECORD_LIMIT"}'
```

다음을 교체합니다:

| 입력 안내 | 설명 |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_ENDPOINT` | 현재 Braze 인스턴스의 Braze REST 엔드포인트 URL입니다. 자세한 내용은 [REST API 키]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers)를 참조하세요. |
| `BRAZE_API_KEY` | `users.track` 권한이 있는 Braze REST API 키입니다. |
| `HOSTNAME` | 현재 Scuba 인스턴스의 호스트 이름입니다. |
| `SCUBA_API_TOKEN` | Scuba API 토큰입니다. |
| `TABLE_NAME` | 데이터셋이 속한 테이블입니다. 자세한 내용은 [용어집: 데이터셋 테이블](https://docs.scuba.io/glossary/dataset-table)을 참조하세요. |
| `ACTOR_PROPERTY_NAME` | 데이터셋이 속한 액터 속성입니다. 이 이름과 일치하는 데이터만 반환됩니다. 자세한 내용은 [용어집: 액터 속성](https://docs.scuba.io/glossary/actor-property)을 참조하세요. |
| `ACTOR_PROPERTY_FILTER` | 액터 속성에 대한 오디언스 검색 필터입니다. |
| `ACTOR_ID` | 데이터셋이 속한 액터 속성의 ID입니다. 이 ID는 Braze의 `external_id`와 일치합니다. 자세한 내용은 [용어집: 액터](https://docs.scuba.io/glossary/actor)를 참조하세요. |
| `PERIOD_START` | BQL 호환 날짜 형식의 시작 기간입니다. 자세한 내용은 [BQL 구문 및 사용법](https://docs.scuba.io/guides/bql-syntax-and-usage)을 참조하세요. |
| `PERIOD_END` | BQL 호환 날짜 형식의 종료 기간입니다. 자세한 내용은 [BQL 구문 및 사용법](https://docs.scuba.io/guides/bql-syntax-and-usage)을 참조하세요. |
| `RECORD_LIMIT` | **선택 사항**: 반환할 최대 레코드 수입니다. `scuba_record_limit`를 생략하면 Scuba는 최대 100개의 레코드를 반환합니다. 이를 변경하려면 `scuba_record_limit`에 음이 아닌 숫자를 할당합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Scuba 데이터를 Braze에 업로드하기" }

### 기본 동작 {#default-behavior}

기본적으로 `update_existing_only`는 `false`로 설정되어 있으며, 이 경우 Braze의 기존 레코드를 업데이트하는 동시에 존재하지 않는 레코드에 대해 새 레코드를 생성합니다. Scuba가 새 레코드를 생성하지 않도록 하려면 `update_existing_only`를 `true`로 설정합니다.

### 사용량 제한 {#rate-limit}

Scuba는 이 엔드포인트에 분당 50,000건의 요청으로 사용량 제한을 적용합니다.

## Scuba의 행동 데이터를 사용하여 Segments 생성하기 {#creating-segments-using-scubas-behavioral-data}

[데이터를 업로드](#uploading-your-scuba-data-to-braze)한 후, Scuba의 행동 데이터를 사용하여 Braze에서 사용자 Segments를 생성할 수 있습니다.

### 1단계: 새 Segment 생성 {#step-1-create-a-new-segment}

Braze에서 **오디언스** > **Segments**로 이동한 다음 **Create Segment**를 선택하고 Segment 이름을 입력합니다.

![Braze에서 새 Segment를 생성하는 화면.]({% image_buster /assets/img/scuba/analytics/segment_name.png %})

### 2단계: Scuba 속성 찾기 및 선택 {#step-2-find-and-select-the-scuba-attribute}

**Segment Details** > **Filters**에서 **커스텀 속성**을 선택합니다.

!['Segment Details'에서 '커스텀 속성' 필터를 선택하는 화면.]({% image_buster /assets/img/scuba/analytics/filter_attribute.png %})

**Search custom attributes**를 선택한 다음 이전 POST 요청에서 사용한 액터 속성정보 이름을 선택합니다.

![액터 속성정보를 커스텀 속성으로 선택하는 화면.]({% image_buster /assets/img/scuba/analytics/select_property.png %})

### 3단계: 속성 구성 {#step-3-configure-the-attribute}

액터 속성정보 이름 옆에서 연산자와 값을 선택합니다(해당되는 경우). 이 값들은 Scuba에서 정의한 액터 속성정보에 의해 결정됩니다. 완료되면 **Save**를 선택합니다.

![선택한 속성에 대한 연산자와 값을 선택하는 화면.]({% image_buster /assets/img/scuba/analytics/operator_end.png %})