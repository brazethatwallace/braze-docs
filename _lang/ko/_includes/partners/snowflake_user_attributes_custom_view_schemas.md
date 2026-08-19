{% if include.schema == "history" %}

| 열 이름     | 데이터 타입     | 설명 |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Braze 워크스페이스 식별자 |
| `USER_ID` | VARCHAR | 고유 Braze 사용자 식별자 |
| `APP_ID` | VARCHAR | 워크스페이스 내 특정 앱 |
| `EXTERNAL_USER_ID` | VARCHAR | 자체 사용자 식별자(설정된 경우) |
| `TIME` | NUMBER | 프로필 업데이트의 unix 타임스탬프(초) |
| `TIME_MS` | NUMBER | 프로필 업데이트의 unix 타임스탬프(밀리초) |
| `UPDATE_SOURCE` | VARCHAR | 속성 업데이트의 소스(API, SDK, 대시보드 등) |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Snowflake에서 데이터가 마지막으로 업데이트된 시점 |
| `CUSTOM_ATTRIBUTES` | VARIANT | 모든 커스텀 속성(키-값 페어)을 포함하는 JSON 객체 |
| `ARCHIVED` | BOOLEAN | 고객 프로필이 보관되었는지 여부 |
| `EFF_DT` | TIMESTAMP_NTZ | 유효 날짜: 이 속성 상태가 시작된 시점 |
| `END_DT` | TIMESTAMP_NTZ | 종료 날짜: 이 속성 상태가 종료된 시점(현재 상태인 경우 NULL) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERCUSTOMATTRIBUTESHISTORYVIEWSHARED schema" }

{% elsif include.schema == "latest" %}

| 열 이름     | 데이터 타입     | 설명 |
|-----------------|---------------|-------------|
| `APP_GROUP_ID` | VARCHAR | Braze 워크스페이스 식별자 |
| `USER_ID` | VARCHAR | 고유 Braze 사용자 식별자 |
| `EXTERNAL_USER_ID` | VARCHAR | 자체 사용자 식별자(설정된 경우) |
| `TIME` | NUMBER | 프로필 업데이트의 unix 타임스탬프(초) |
| `TIME_MS` | NUMBER | 프로필 업데이트의 unix 타임스탬프(밀리초) |
| `UPDATE_SOURCE` | VARCHAR | 속성 업데이트의 소스(API, SDK, 대시보드 등) |
| `ARCHIVED` | BOOLEAN | 고객 프로필이 보관되었는지 여부 |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ | Snowflake에서 데이터가 마지막으로 업데이트된 시점 |
| `APP_ID` | VARCHAR | 워크스페이스 내 특정 앱 |
| `CUSTOM_ATTRIBUTES` | OBJECT | 모든 커스텀 속성(키-값 페어)을 포함하는 JSON 객체 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="USERLATESTSTATECUSTOMATTRIBUTEVIEWSHARED schema" }

{% alert note %}
이 뷰는 `CUSTOM_ATTRIBUTES`에 `VARIANT` 대신 `OBJECT` 타입을 사용합니다. 개별 속성을 쿼리하려면 동일한 JSON 접근자 구문(`:attribute_name::TYPE`)을 사용하세요.
{% endalert %}

{% endif %}