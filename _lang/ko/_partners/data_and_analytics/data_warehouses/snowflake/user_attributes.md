---
nav_title: "고객 프로필 속성"
article_title: Snowflake의 사용자 속성 뷰
page_order: 10
page_type: partner
search_tag: Partner
toc_headers: h2
---

# 고객 프로필 속성 {#user-profile-attributes}

> 이 페이지는 Snowflake의 기본 속성 및 커스텀 속성 뷰에 대한 참조 문서입니다. 기본 속성에 대한 세 가지 뷰와 커스텀 속성에 대한 세 가지 뷰가 있으며, 각각 고유한 성능 고려 사항을 가진 특정 사용 사례를 위해 설계되었습니다.

## 대시보드와의 데이터 일치성 {#data-parity-with-the-dashboard}

드문 경우이지만, 이 페이지의 Snowflake 뷰에 있는 기본 및 커스텀 속성 값이 Braze 대시보드의 고객 프로필에 표시되는 내용과 일치하지 않을 수 있습니다.

예를 들어, Snowflake에서 속성이 `NULL`로 표시되지만 대시보드에서는 해당 사용자에 대한 값이 표시될 수 있습니다.

광범위한 불일치가 발견되면 고객 성공 매니저 또는 Braze 고객지원에 문의하세요.

## 사용 가능한 뷰 {#available-views}

<table aria-label="사용 가능한 뷰">
  <caption>사용 가능한 뷰</caption>
  <thead>
    <tr>
      <th>유형</th>
      <th>뷰</th>
      <th>설명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="3">기본 속성</td>
      <td><code>USER_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>고객 프로필 스냅샷</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>실시간 고객 프로필</td>
    </tr>
    <tr>
      <td><code>USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>이력 변경 로그</td>
    </tr>
    <tr>
      <td rowspan="3">커스텀 속성</td>
      <td><code>USER_CUSTOM_ATTRIBUTES_VIEW_SHARED</code></td>
      <td>고객 프로필 스냅샷</td>
    </tr>
    <tr>
      <td><code>USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED</code></td>
      <td>실시간 고객 프로필</td>
    </tr>
    <tr>
      <td><code>USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED</code></td>
      <td>이력 변경 로그</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="사용 가능한 뷰" }

## 고객 프로필 스냅샷 {#user-profile-snapshots}

이 뷰는 고객 프로필 속성의 주기적인 스냅샷을 제공합니다. 데이터는 최대 12시간까지 지연되므로, 실시간 업데이트가 필요하지 않은 쿼리에 유용합니다.

 - `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED`
 - `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`

### 사용법 {#usage}

* 최대 **12시간 지연**으로 사용자 속성의 스냅샷을 제공합니다.
* 실시간 정확성이 필요하지 않은 쿼리에 적합합니다.
* 특히 `USER_ID` 이외의 속성으로 필터링할 때 쿼리 실행 속도가 빠릅니다.
* **제한 사항:** 데이터가 실시간으로 최신 상태가 아닙니다.

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` 스키마 {#user_default_attributes_view_shared-schema}

| 컬럼 이름     | 데이터 유형     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_USER_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL_ADDRESS` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE_NUMBER` | VARCHAR |
| `DOB` | VARCHAR |
| `TIMEZONE` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
| `ARCHIVED` | BOOLEAN |
{: .reset-td-br-1 .reset-td-br-2 aria-label="USERDEFAULTATTRIBUTESVIEWSHARED schema" }


### `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED` 스키마 {#user_custom_attributes_view_shared-schema}

| 컬럼 이름     | 데이터 유형     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `EXTERNAL_USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `CUSTOM_ATTRIBUTES` | VARIANT |
| `ARCHIVED` | BOOLEAN |
{: .reset-td-br-1 .reset-td-br-2 aria-label="USERCUSTOMATTRIBUTESVIEWSHARED schema" }

## 실시간 고객 프로필 뷰 {#real-time-user-profile-views}

이 뷰는 고객 프로필 속성에 대한 거의 실시간 업데이트를 제공하며, Braze에서 업데이트가 발생한 후 최대 10분까지 데이터가 지연됩니다.

  - `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED`
  - `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`

### 사용법

* 최소 지연(~10분)으로 최신 사용자 속성을 제공합니다.
* 실시간 분석 및 최근 데이터가 필요한 시나리오에 유용합니다.
* **성능 고려 사항:**
    * 개별 사용자에 대한 쿼리는 더 빠릅니다(대형 웨어하우스 사용 시 1분 이내).
    * USER_ID 필터가 없는 쿼리는 모든 사용자에 대한 집계가 필요하므로 실행 시간이 크게 길어집니다.
    * 대규모 데이터셋(예: 1억 명 이상의 사용자)에 대한 쿼리는 수 분이 소요될 수 있습니다.

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` 스키마 {#user_latest_state_default_attributes_view_shared-schema}

| 컬럼 이름     | 데이터 유형     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `ARCHIVED` | BOOLEAN |
| `SF_UPDATED_AT` | TIMESTAMP_LTZ |
| `EXTERNAL_USER_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL_ADDRESS` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE_NUMBER` | VARCHAR |
| `DOB` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
| `TIMEZONE` | VARCHAR |
{: .reset-td-br-1 .reset-td-br-2 aria-label="USERLATESTSTATEDEFAULTATTRIBUTESVIEWSHARED schema" }

### `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` 스키마 {#user_latest_state_custom_attribute_view_shared-schema}

| 컬럼 이름     | 데이터 유형     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `EXTERNAL_USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `ARCHIVED` | BOOLEAN |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `APP_ID` | VARCHAR |
| `CUSTOM_ATTRIBUTES` | OBJECT |
{: .reset-td-br-1 .reset-td-br-2 aria-label="USERLATESTSTATECUSTOMATTRIBUTEVIEWSHARED schema" }

## 이력 변경 로그 {#historical-change-logs}

이 뷰는 사용자 속성의 이력 변경 로그를 저장하며, 12시간 단위로 변경 사항을 캡처합니다.

- `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED`
- `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`

### 사용법

* 롤링 6개월 기간 동안 사용자 속성의 이력 변경 기록을 제공합니다.
* 데이터는 12시간마다 스냅샷이 생성되므로, 이 기간 내의 여러 업데이트는 단일 레코드로 결합됩니다. 이 기간 내의 개별 변경 사항은 별도로 보존되지 않습니다.
* `EFF_DT`와 `END_DT`는 사용자 속성 상태의 시작과 끝을 나타냅니다.

{% include partners/snowflake_user_attributes_date_fields_note.md %}

### `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` 스키마 {#user_default_attributes_history_view_shared-schema}

| 컬럼 이름     | 데이터 유형     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `EXTERNAL_USER_ID` | VARCHAR |
| `FIRST_NAME` | VARCHAR |
| `LAST_NAME` | VARCHAR |
| `EMAIL_ADDRESS` | VARCHAR |
| `GENDER` | VARCHAR |
| `PHONE_NUMBER` | VARCHAR |
| `DOB` | VARCHAR |
| `TIMEZONE` | VARCHAR |
| `HOME_CITY` | VARCHAR |
| `COUNTRY` | VARCHAR |
| `LANGUAGE` | VARCHAR |
| `EFF_DT` | TIMESTAMP_NTZ |
| `END_DT` | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="USERDEFAULTATTRIBUTESHISTORYVIEWSHARED schema" }

### `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED` 스키마 {#user_custom_attributes_history_view_shared-schema}

| 컬럼 이름     | 데이터 유형     |
|-----------------|---------------|
| `APP_GROUP_ID` | VARCHAR |
| `USER_ID` | VARCHAR |
| `APP_ID` | VARCHAR |
| `EXTERNAL_USER_ID` | VARCHAR |
| `TIME` | NUMBER |
| `TIME_MS` | NUMBER |
| `UPDATE_SOURCE` | VARCHAR |
| `SF_UPDATED_AT` | TIMESTAMP_NTZ |
| `CUSTOM_ATTRIBUTES` | VARIANT |
| `ARCHIVED` | BOOLEAN |
| `EFF_DT` | TIMESTAMP_NTZ |
| `END_DT` | TIMESTAMP_NTZ |
{: .reset-td-br-1 .reset-td-br-2 aria-label="USERCUSTOMATTRIBUTESHISTORYVIEWSHARED schema" }

## 모범 사례 {#best-practices}

### 권장 쿼리 사용법 {#recommended-query-usage}

| 사용 사례                                               | 권장 뷰                                   | 참고                                                                 |
|--------------------------------------------------------|----------------------------------------------------|-----------------------------------------------------------------------|
| 최근 업데이트가 필요하지 않은 **일반 쿼리** | `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` 및 `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`               | 빠른 실행, 최대 12시간 전 데이터.                          |
| **최신 사용자 속성**이 필요한 쿼리       | `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` 및 `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED` | 거의 실시간 업데이트를 제공하지만 대규모 데이터셋에서는 느릴 수 있습니다. |
| 속성 변경의 **이력 추적**           | `USER_DEFAULT_ATTRIBUTES_HISTORY_VIEW_SHARED` 및 `USER_CUSTOM_ATTRIBUTES_HISTORY_VIEW_SHARED`      | 12시간 단위로 속성 변경 사항을 저장합니다.                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="권장 쿼리 사용법" }

### 성능 고려 사항 {#performance-considerations}

* `USER_DEFAULT_ATTRIBUTES_VIEW_SHARED` 또는 `USER_CUSTOM_ATTRIBUTES_VIEW_SHARED`에 대한 쿼리는 대형 웨어하우스에서 대규모 데이터셋(~10억 명의 사용자)에 대해 10초 이내에 반환되어야 합니다.
* `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` 또는 `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED `에 대한 단일 사용자 쿼리는 1분 이내에 반환되지만, `USER_ID` 필터링 없이는 성능이 크게 저하됩니다.
* `USER_LATEST_STATE_DEFAULT_ATTRIBUTES_VIEW_SHARED` 또는 `USER_LATEST_STATE_CUSTOM_ATTRIBUTE_VIEW_SHARED`에서 1억 명 이상의 사용자에 대한 쿼리는 사용자별 집계로 인해 수 분이 소요될 수 있습니다.