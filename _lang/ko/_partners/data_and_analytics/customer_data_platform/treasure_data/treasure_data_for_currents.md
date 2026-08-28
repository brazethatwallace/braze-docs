---
nav_title: Treasure Data for Currents
article_title: Treasure Data for Currents
description: "이 참조 문서에서는 Braze Currents와 Treasure Data 간의 파트너십을 설명합니다. Treasure Data는 Braze 이벤트 데이터를 Treasure Data로 스트리밍하여 분석 및 활성화에 활용할 수 있는 엔터프라이즈 고객 데이터 플랫폼입니다."
page_type: partner
tool: Currents
alias: /partners/treasure_data_for_currents/
search_tag: Partner
---


# Treasure Data for Currents

> [Treasure Data](https://www.treasuredata.com/)는 여러 소스에서 정보를 수집하고 마케팅 스택의 다양한 위치로 라우팅하는 고객 데이터 플랫폼(CDP)입니다.

Braze와 Treasure Data 통합을 사용하면 두 시스템 간의 정보 흐름을 제어할 수 있습니다. Currents를 사용하면 Braze 이벤트 데이터를 Treasure Data로 스트리밍하여 전체 성장 스택에서 활용할 수 있습니다.

권장 방법은 Treasure Data의 **Braze Currents Streaming** 커넥터와 Braze의 **Custom Currents Export**를 함께 사용하는 것입니다. 이 접근 방식은 다음을 제공합니다:

- Braze에서 Treasure Data로의 실시간 이벤트 스트리밍
- 이벤트 유형별 자동 테이블 라우팅 옵션
- JSON 파싱이 필요 없는 플랫한 SQL 쿼리 가능 스키마

{% alert note %}
Braze Currents Streaming 커넥터는 요청 시 사용할 수 있습니다. Treasure Data 지원팀에 문의하여 Treasure Data 계정에서 활성화하세요. 파트너 측 설정 세부 사항은 Treasure Data의 [Braze Currents Import Integration](https://docs.treasuredata.com/int/braze-currents-import-integration)을 참조하세요.
{% endalert %}

## 전제 조건 {#prerequisites}

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Treasure Data 계정 | 이 파트너십을 활용하려면 활성화된 [Treasure Data 계정](https://console.treasuredata.com)이 필요합니다. |
| Currents | Treasure Data로 데이터를 내보내려면 계정에 [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents#how-to-access-currents)가 설정되어 있어야 합니다. |
| Braze Currents 스트리밍 커넥터 | Treasure Data 지원팀에 문의하여 Treasure Data 계정에서 Braze Currents 스트리밍 커넥터를 활성화하세요. |
| Treasure Data Write API 키 | Treasure Data Write API 키는 Braze에서 들어오는 인바운드 스트림을 인증합니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="전제 조건" }

## 통합 {#integration}

### 1단계: Treasure Data에서 커넥터 구성하기 {#step-1-configure-the-connector-in-treasure-data}

1. Treasure Data 콘솔에서 **Connections** > **New Connection**으로 이동합니다.
2. **Braze Currents Streaming**을 선택합니다.
3. **Authentication**에서 Treasure Data Write API 키를 입력합니다.
4. **Source Settings**에서 다음 항목을 구성합니다.

| 필드 | 설명 |
| ----- | ----------- |
| Source Name | 이 연결에 대한 설명이 포함된 이름 |
| Datastore | **Plazma**를 선택합니다 |
| Database | 이벤트가 저장되는 Treasure Data 데이터베이스 |
| Table | 기본 대상 테이블 |
| Multiple Tables | 각 Braze 이벤트 유형을 자체 테이블로 라우팅하려면 선택합니다 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="소스 설정" }

5. 저장 후 **Unique ID**(`task_id`)를 복사합니다. 이 값은 다음 단계에서 필요합니다.

### 2단계: Braze에서 Custom Currents Export 만들기 {#step-2-create-a-custom-currents-export-in-braze}

Braze Currents UI의 **Treasure Data Export** 옵션은 레거시 Postback API 메서드를 사용하며 더 이상 권장되지 않습니다. 대신 **Custom Currents Export**를 사용하세요.

1. Braze에서 **파트너 통합** > **Data Export**로 이동합니다.
2. **Create New Current** > **Custom Currents Export**를 선택합니다.
3. 통합 이름과 오류 알림을 받을 연락처 이메일을 입력합니다.
4. **Credentials**에서 Treasure Data 리전의 엔드포인트 URL을 입력합니다. Treasure Data Write API 키를 **Bearer Token**으로 입력합니다.

| 리전 | 엔드포인트 URL |
| ------ | ------------ |
| US | `https://braze-in-streaming.treasuredata.com/v1/task/{TASK_ID}` |
| EU | `https://braze-in-streaming.eu01.treasuredata.com/v1/task/{TASK_ID}` |
| AP02 | `https://braze-in-streaming.ap02.treasuredata.com/v1/task/{TASK_ID}` |
| Tokyo | `https://braze-in-streaming.treasuredata.co.jp/task/v1/{TASK_ID}` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="리전별 엔드포인트 URL" }

`{TASK_ID}`를 [1단계](#step-1-configure-the-connector-in-treasure-data)에서 복사한 Unique ID로 교체합니다.

5. 내보낼 이벤트 유형을 선택합니다. Custom Currents 연결은 식별된 사용자와 `external_user_id`가 없는 사용자 모두의 이벤트를 전송할 수 있습니다. Treasure Data는 두 가지 모두 수집합니다.
6. **Launch Current**를 선택합니다.

{% alert warning %}
Treasure Data Write API 키와 엔드포인트 URL을 항상 최신 상태로 유지하세요. 엔드포인트에 **5일** 이상 연결할 수 없는 경우, Braze는 커넥터의 이벤트를 삭제하며 데이터는 영구적으로 손실됩니다.
{% endalert %}

## 데이터 쿼리하기 {#query-your-data}

이벤트가 유입되기 시작하면 SQL을 사용하여 쿼리할 수 있습니다. Treasure Data는 페이로드를 플랫하게 변환하므로 JSON을 직접 파싱할 필요가 없습니다.

```sql
SELECT
  id AS event_id,
  event_type,
  user_external_user_id,
  properties_campaign_name,
  properties_email_address,
  time
FROM your_database.your_table
WHERE TD_INTERVAL(time, '-1d', 'JST')
```

{% alert note %}
Treasure Data의 `time` 필드는 Braze에서 이벤트가 실제로 발생한 시각이 아니라, Treasure Data가 이벤트를 수신하고 처리한 시각의 타임스탬프입니다.
{% endalert %}

**Multiple Tables**를 선택한 경우, 각 이벤트 유형은 고유한 테이블에 저장됩니다(예: `users_message_email_open` 또는 `users_behaviors_purchase`).

데이터가 정상적으로 도착하고 있는지 확인하려면, Currents를 시작한 후 몇 분 뒤에 카운트 쿼리를 실행하세요:

```sql
SELECT COUNT(*)
FROM your_table
WHERE TD_INTERVAL(time, '-1h')
```

## 데이터 스키마 {#data-schema}

Treasure Data는 중첩된 JSON을 최대 2단계 깊이까지 평탄화합니다.

| JSON 유형 | Treasure Data 열 유형 |
| --------- | ------------------------- |
| string | string |
| number | long |
| boolean | string |
| array | JSON string |
| object (레벨 1) | `field_name` |
| object (레벨 2) | `parent_field_name_field_name` |
| null | 생략 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="데이터 유형 매핑" }

열 이름은 소문자와 밑줄만 사용합니다.

## 제한 사항 {#limits}

| 항목 | 제한 |
| ---- | ----- |
| 최대 페이로드 크기 | 요청당 1&nbsp;MB |
| 배치 크기 | 배치당 100개 이벤트 (기본값) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="제한 사항" }

## 통합 세부 사항 {#integration-details}

Braze는 [Currents 이벤트 용어집]({{site.baseurl}}/user_guide/data/distribution/braze_currents)에 나열된 모든 데이터를 Treasure Data로 내보내는 것을 지원합니다. 여기에는 [메시지 인게이지먼트]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) 및 [고객 행동]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) 이벤트의 모든 속성이 포함됩니다.

내보내기된 데이터의 페이로드 구조는 커스텀 HTTP 커넥터의 페이로드 구조와 동일합니다. [커스텀 HTTP 커넥터 예제 리포지토리](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors)에서 샘플 페이로드를 확인할 수 있습니다.

## 레거시 Postback 방식에서 마이그레이션 {#migrate-from-the-legacy-postback-method}

이전에 Braze에서 **Treasure Data Export**(Postback)를 사용한 경우:

1. 이 문서의 커스텀 Currents Export 설정을 완료합니다.
2. 새 테이블로 이벤트가 전달되고 있는지 확인합니다.
3. Braze에서 이전 Postback 기반 Current를 비활성화합니다.

원시 JSON 배열로 저장된 레거시 데이터는 `JSON_PARSE`와 `UNNEST`를 사용하여 계속 쿼리할 수 있습니다. 스트리밍 커넥터를 통해 수집된 새 데이터는 [데이터 스키마](#data-schema)에 설명된 플랫 스키마를 사용합니다.