---
nav_title: Amplitude와 연결된 콘텐츠
article_title: Amplitude와 연결된 콘텐츠
page_order: 0
alias: /partners/amplitude_api_endpoints/
page_type: partner
description: "Amplitude의 사용자 프로필 API는 Amplitude 사용자 프로필을 제공합니다. 여기에는 사용자 등록정보, 계산된 사용자 등록정보, 해당 사용자가 포함된 코호트의 코호트 ID 목록, 추천이 포함됩니다."
search_tag: Partner

---

# Amplitude와 연결된 콘텐츠 {#amplitude-and-connected-content}

> Amplitude의 사용자 프로필 API는 Amplitude 사용자 프로필을 제공합니다. 여기에는 사용자 등록정보, 계산된 사용자 등록정보, 해당 사용자가 포함된 코호트의 코호트 ID 목록, 추천이 포함됩니다. 다음은 연결된 콘텐츠와 함께 사용할 수 있는 일반적인 Amplitude API 엔드포인트 목록입니다.

## 엔드포인트 파라미터 {#endpoint-parameters}

다음 표는 사용자 프로필 API 호출에 사용할 수 있는 파라미터를 설명합니다.

| 파라미터 | 필수 | 설명 |
| --------- | -------- | ----------- |
| `user_id` | 선택 사항 | 쿼리할 사용자 ID(외부 데이터베이스 ID)이며, `device_id`가 설정되지 않은 경우 필수입니다. |
| `device_id` | 선택 사항 | 쿼리할 기기 ID(익명 ID)이며, `user_id`가 설정되지 않은 경우 필수입니다. |
| `get_recs` | 선택 사항<br>(기본값 false) | 이 사용자에 대한 추천 결과를 반환합니다. |
| `rec_id` | 선택 사항 | 검색할 추천이며, `get_recs`가 true인 경우 필수입니다. `rec_ids`를 쉼표로 구분하여 여러 추천을 가져올 수 있습니다. |
| `rec_type` | 선택 사항 | 기본 실험 대조군 설정을 재정의하며, `rec_type=model`은 모델 기반 추천을 반환하고 `rec_type=random`은 무작위 추천을 반환합니다. 향후 다른 옵션이 추가될 수 있습니다. |
| `get_amp_props` | 선택 사항<br>(기본값 false) | 계산을 제외한 이 사용자의 전체 사용자 등록정보 세트를 반환합니다. |
| `get_cohort_ids` | 선택 사항<br>(기본값 false) | 추적하도록 설정된 코호트 중 이 사용자가 속한 모든 코호트 ID 목록을 반환합니다. 기본적으로 어떤 코호트에서도 사용자의 코호트 멤버십은 추적되지 않습니다. |
| `get_computations` | 선택 사항<br>(기본값 false) | 이 사용자에 대해 활성화된 모든 계산 목록을 반환합니다. |
| `comp_id` | 선택 사항 | 이 사용자에 대해 활성화되었을 수 있는 단일 계산을 반환합니다. 존재하지 않으면 null 값을 반환합니다. `get_computations`가 true이면 이 값을 포함한 모든 값을 가져옵니다(아카이브되거나 삭제된 경우 제외). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Endpoint parameters" }

다음 표는 Amplitude의 응답에서 일반적으로 볼 수 있는 파라미터를 설명합니다.

| 응답 파라미터 | 설명 |
| ------------------ | ----------- |
| `rec_id` | 요청된 추천 ID입니다. |
| `child_rec_id` | 모델 성능 개선을 위한 내부 실험의 일환으로 Amplitude가 백엔드에서 사용할 수 있는 더 상세한 추천 ID입니다. 대부분의 경우 `rec_id`와 동일합니다. |
| `items` | 이 사용자에 대한 추천 목록입니다. |
| `is_control` | 이 사용자가 대조군에 속하면 true입니다. |
| `recommendation_source` | 이 추천을 생성하는 데 사용된 모델의 이름입니다. |
| `last_updated` | 이 추천이 마지막으로 생성되고 동기화된 타임스탬프입니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Endpoint parameters" }

## 일반적인 Amplitude 엔드포인트 {#common-amplitude-endpoints}

### 추천 가져오기 {#get-a-recommendation}

#### 엔드포인트 {#endpoint}
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_recs=true&rec_id=testRecId`
{% endraw %}
#### 응답 예시 {#example-response}
```json
{
  "userData": {
    "recommendations": [
      {
        "rec_id": "testRecId",
        "child_rec_id": "testRecId",
        "items": [
          "cookie",
          "cracker",
          "chocolate milk",
          "donut",
          "croissant"
        ],
        "is_control": false,
        "recommendation_source": "model",
        "last_updated": 1608670720
      }
    ],
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": null
  }
}
```

### 여러 추천 가져오기 {#get-multiple-recommendations}

#### 엔드포인트
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_recs=true&rec_id=testRecId,testRecId2`
{% endraw %}
#### 응답 예시
```json
{
  "userData": {
    "recommendations": [
      {
        "rec_id": "testRecId",
        "child_rec_id": "testRecId",
        "items": [
          "cookie",
          "cracker",
          "chocolate milk",
          "donut",
          "croissant"
        ],
        "is_control": false,
        "recommendation_source": "model",
        "last_updated": 1608670720
      },
            {
        "rec_id": "testRecId2",
        "child_rec_id": "testRecId2",
        "items": [
          "bulgogi",
          "bibimbap",
          "kimchi",
          "croffles",
          "samgyeopsal"
        ],
        "is_control": false,
        "recommendation_source": "model2",
        "last_updated": 1608670658
      }
    ],
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": null
  }
}
```

### 사용자 등록정보 가져오기 {#get-user-properties}

#### 엔드포인트
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_amp_props=true`
{% endraw %}
#### 응답 예시
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "library": "http/1.0",
      "first_used": "2020-01-13",
      "last_used": "2021-03-24",
      "number_property": 12,
      "boolean_property": true
    },
    "cohort_ids": null
  }
}
```

### 코호트 ID 가져오기 {#get-cohort-ids}

#### 엔드포인트
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_cohort_ids=true`
{% endraw %}
#### 응답 예시
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": null,
    "cohort_ids": ["cohort1", "cohort3", "cohort7"]
  }
}
```

### 단일 계산 가져오기 {#get-a-single-computation}

#### 엔드포인트
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&comp_id=testCompId`
{% endraw %}
#### 응답 예시
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "computed-prop-2": "3"
    },
    "cohort_ids": null
  }
}
```

### 모든 계산 가져오기 {#get-all-computations}

#### 엔드포인트
{% raw %}
`https://profile-api.amplitude.com/v1/userprofile?user_id=testUser&get_computations=true`
{% endraw %}
#### 응답 예시
```json
{
  "userData": {
    "recommendations": null,
    "user_id": "testUser",
    "device_id": "ffff-ffff-ffff-ffff",
    "amp_props": {
      "computed-prop-1": "5000000.0",
      "computed-prop-2": "3"
    },
    "cohort_ids": null
  }
}
```

