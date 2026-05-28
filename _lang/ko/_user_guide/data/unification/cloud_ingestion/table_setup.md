---
nav_title: 테이블 설정
article_title: 클라우드 데이터 수집 테이블 설정
toc_headers: h2
page_order: 2
page_type: reference
description: "CDI 소스 테이블을 설정하는 방법과 페이로드 형식 요구 사항과의 차이점에 대해 알아봅니다."
---

# 클라우드 데이터 수집 테이블 설정 {#cloud-data-ingestion-table-setup}

> 이 페이지에서는 클라우드 데이터 수집(CDI)의 관련되지만 서로 다른 두 가지 요구 사항인 소스 테이블 설정과 페이로드 형식 지정을 구분하여 설명합니다.

## 테이블 설정과 페이로드 형식 지정 비교 {#understand-table-setup-compared-to-payload-formatting}

CDI 사용자 데이터 동기화의 경우 다음 두 가지를 모두 구성합니다:

| 레이어 | 제어 대상 |
| --- | --- |
| 소스 테이블 설정 | 필수 열, 사용자 식별자 및 `UPDATED_AT` 동기화 동작 |
| 페이로드 형식 지정 | `PAYLOAD`의 JSON 필드(속성, 이벤트, 구매에 대한 오브젝트 형태 포함) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="테이블 설정과 페이로드 형식 지정 비교" }

Braze는 먼저 소스 테이블에서 행을 읽은 다음, 선택한 데이터 유형에 따라 `PAYLOAD` 필드를 검증합니다.

## 소스 테이블 설정 {#set-up-your-source-table}

데이터 웨어하우스 사용자 데이터 동기화의 경우 소스 테이블 또는 뷰에 다음이 포함되어야 합니다:

- `UPDATED_AT`
- `PAYLOAD`
- 하나 이상의 지원되는 사용자 식별자 열:
  - `EXTERNAL_ID`
  - `ALIAS_NAME` 및 `ALIAS_LABEL`
  - `BRAZE_ID`
  - `EMAIL`
  - `PHONE`

테이블에 여러 식별자 열이 포함되어 있더라도 각 행에는 한 번에 하나의 식별자 유형만 포함해야 합니다.

### `UPDATED_AT` 요구 사항 {#updated_at-requirements}

- 일광 절약 시간 문제를 방지하려면 `UPDATED_AT` 값을 UTC로 저장합니다.
- Braze는 `UPDATED_AT`가 마지막으로 동기화된 값보다 이후인 행을 동기화합니다.
- 새 행이 동일한 타임스탬프를 공유하는 경우 정확한 경계 타임스탬프의 행이 다시 동기화될 수 있습니다.

중복 타임스탬프 및 증분 업데이트에 대한 지침은 [클라우드 데이터 수집 모범 사례]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices/#avoid-resyncing-rows-with-duplicate-timestamps)를 참조하세요.

{% alert note %}
파일 스토리지 소스는 다른 설정 요구 사항을 사용하며 `UPDATED_AT`를 지원하지 않습니다. 자세한 내용은 [파일 스토리지 통합]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/#required-file-formats)을 참조하세요.
{% endalert %}

## `PAYLOAD` 열 설정 {#set-up-the-payload-column}

`PAYLOAD` 값은 선택한 데이터 유형에 대해 Braze `/users/track` 엔드포인트에서 사용하는 것과 동일한 오브젝트 형식을 따릅니다.

| 데이터 유형 | 형식 참조 |
| --- | --- |
| `attributes` | [사용자 속성 오브젝트]({{site.baseurl}}/api/objects_filters/user_attributes_object/#migrating-push-tokens) |
| `events` | [이벤트 오브젝트]({{site.baseurl}}/api/objects_filters/event_object/) |
| `purchases` | [구매 오브젝트]({{site.baseurl}}/api/objects_filters/purchase_object/) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="PAYLOAD 열 설정" }

중첩 속성의 경우 [오브젝트 등록정보로 날짜 캡처]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support/#capturing-dates-as-object-properties)의 형식을 사용하여 날짜를 포함합니다.

### 페이로드 예시 {#payload-examples}

{% tabs local %}
{% tab 중첩 커스텀 속성 %}
커스텀 속성 동기화를 위한 페이로드 열에 중첩 커스텀 속성을 포함할 수 있습니다.

```json
{
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "genre": "Jazz",
        "play_analytics": {
            "count": 1000,
            "top_10_listeners": true
        }
      }
}
```

{% endtab %}
{% tab 이벤트 %}
이벤트를 동기화하려면 이벤트 이름이 필수입니다. `time` 필드는 ISO 8601 문자열 또는 `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 형식으로 지정합니다. `time` 필드가 없는 경우 Braze는 `UPDATED_AT` 열 값을 이벤트 시간으로 사용합니다. `app_id` 및 `properties`를 포함한 기타 필드는 선택 사항입니다.

행당 하나의 이벤트를 동기화할 수 있습니다.

```json
{
    "app_id" : "your-app-id",
    "name" : "rented_movie",
    "time" : "2013-07-16T19:20:45+01:00",
    "properties": {
        "movie": "The Sad Egg",
        "director": "Dan Alexander"
    }
}
```

{% endtab %}
{% tab 구매 %}
구매 이벤트를 동기화하려면 `product_id`, `currency`, `price`가 필수입니다. 선택 사항인 `time` 필드는 ISO 8601 문자열 또는 `yyyy-MM-dd'T'HH:mm:ss:SSSZ` 형식으로 지정합니다. `time` 필드가 없는 경우 Braze는 `UPDATED_AT` 열 값을 이벤트 시간으로 사용합니다. `app_id`, `quantity`, `properties`를 포함한 기타 필드는 선택 사항입니다.

행당 하나의 구매 이벤트를 동기화할 수 있습니다.

```json
{
    "app_id" : "11ae5b4b-2445-4440-a04f-bf537764c9ad",
    "product_id" : "Completed Order",
    "currency" : "USD",
    "price" : 219.98,
    "time" : "2013-07-16T19:20:30+01:00",
    "properties" : {
        "products" : [ { "name": "Monitor", "category": "Gaming", "product_amount": 19.99 },
        { "name": "Gaming Keyboard", "category": "Gaming ", "product_amount": 199.99 }
        ]
    }
}
```

{% endtab %}
{% tab 구독 그룹 %}
구독 그룹 상태를 동기화하려면 각 행에 하나 이상의 `subscription_group_id` 및 `subscription_state` 쌍을 포함합니다.
```json
{
    "subscription_groups" : [
        {
            "subscription_group_id": "subscription_group_identifier_1",
            "subscription_state": "unsubscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_2",
            "subscription_state": "subscribed"
        },
        {
            "subscription_group_id": "subscription_group_identifier_3",
            "subscription_state": "subscribed"
        }
      ]
}
```
{% endtab %}
{% endtabs %}

## 관련 CDI 설정 문서 {#related-cdi-setup-docs}

- 소스별 DDL 예시는 [데이터 웨어하우스 통합]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)을 참조하세요.
- 파일 기반 설정은 [파일 스토리지 통합]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/)을 참조하세요.
- 동기화 동작 및 최적화 지침은 [클라우드 데이터 수집 모범 사례]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/best_practices/)를 참조하세요.