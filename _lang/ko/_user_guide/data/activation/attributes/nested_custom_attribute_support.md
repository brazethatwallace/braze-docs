---
nav_title: 중첩 커스텀 속성
article_title: 중첩 커스텀 속성
alias: "/nested_custom_attribute_support/"
page_order: 3
page_type: reference
description: "이 참조 문서에서는 중첩 커스텀 속성을 커스텀 속성의 데이터 유형으로 사용하는 방법과 제한 사항 및 사용 예시를 다룹니다."
---

# 중첩 커스텀 속성 {#nested-custom-attributes}

> 이 페이지에서는 중첩 커스텀 속성에 대해 설명하며, 이를 통해 속성 집합을 다른 속성의 등록정보로 정의할 수 있습니다. 즉, 커스텀 속성 오브젝트를 정의할 때 해당 오브젝트에 대한 추가 속성 집합을 정의할 수 있습니다.

{% multi_lang_include nested_attribute_objects/about_nested_attributes.md %}

{% multi_lang_include nested_attribute_objects/supported_data_types.md %}

## 고려 사항 {#considerations}

- 중첩 커스텀 속성은 Braze SDK 또는 API를 통해 전송되는 커스텀 속성을 위한 것입니다.
- 오브젝트의 최대 크기는 100&nbsp;KB입니다. 업데이트로 인해 오브젝트가 100&nbsp;KB를 초과하면 Braze는 해당 업데이트를 삭제하고 속성은 변경되지 않습니다.
- 키 이름과 문자열 값의 크기 제한은 255자입니다.
- 키 이름에는 공백을 포함할 수 없습니다.
- 마침표(`.`)와 달러 기호(`$`)는 중첩 커스텀 속성을 고객 프로필에 보내려는 경우 API 페이로드에서 지원되지 않는 문자입니다.
- 모든 Braze 파트너가 중첩 커스텀 속성을 지원하는 것은 아닙니다. 특정 파트너 통합에서 이 기능을 지원하는지 확인하려면 [파트너 설명서]({{site.baseurl}}/partners/home)를 참조하세요.
- 연결된 오디언스 API를 호출할 때 중첩 커스텀 속성을 필터로 사용할 수 없습니다.
- 기본적으로 **중첩 커스텀 속성** Segment 필터에는 오브젝트 유형 커스텀 속성, 오브젝트 배열 속성, 배열 유형 커스텀 속성이 포함됩니다. 속성을 선택하면 등록정보 스키마 선택기에 중첩 배열 필드에 대한 배열 경로(`[]` 표기법 사용)가 포함됩니다. 해당 필터에서 최상위 배열 커스텀 속성을 숨기려면 [Braze 고객지원]({{site.baseurl}}/braze_support)에 문의하세요.
- 대시보드에서 **커스텀 사용자로 미리보기**를 사용하여 메시지를 미리 볼 때, 모의 데이터는 문자열 또는 문자열 배열로만 입력할 수 있으며 중첩 오브젝트는 지원되지 않습니다. 중첩 커스텀 속성을 참조하는 메시지를 미리 보려면 프로필에 이미 중첩 속성이 있는 기존 사용자를 선택하세요. 중첩 커스텀 이벤트 등록정보의 경우, 렌더링을 확인하려면 테스트 사용자를 타겟으로 하는 라이브 Campaign을 시작해야 합니다.

## API 예제 {#api-example}

{% tabs local %}
{% tab 생성 %}
다음은 "가장 많이 재생한 노래" 오브젝트가 있는 `/users/track` 예제입니다. 노래의 등록정보를 캡처하기 위해 오브젝트 등록정보 집합과 함께 `most_played_song`을 오브젝트로 나열하는 API 요청을 보냅니다.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
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
  ]
}
```

{% endtab %}
{% tab 업데이트 %}
기존 오브젝트를 업데이트하려면 요청에 `_merge_objects` 매개변수를 포함하여 `users/track`으로 POST를 보내세요. 이렇게 하면 업데이트가 기존 오브젝트 데이터와 심층 병합됩니다. 심층 병합은 첫 번째 수준만이 아닌 오브젝트의 모든 수준이 다른 오브젝트에 병합되도록 합니다. 이 예시에서는 Braze에 이미 `most_played_song` 오브젝트가 있으며, 이제 `most_played_song` 오브젝트에 새 필드 `year_released`를 추가합니다.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "most_played_song": {
          "year_released": 1960
      }
    }
  ]
}
```

이 요청이 수신된 후 커스텀 속성 오브젝트는 다음과 같이 표시됩니다:

```json
{"most_played_song": {
  "song_name": "Solea",
  "artist_name" : "Miles Davis",
  "album_name": "Sketches of Spain",
  "year_released": 1960,
  "genre": "Jazz",
  "play_analytics": {
     "count": 1000,
     "top_10_listeners": true
  }
}}
```

{% alert warning %}
`_merge_objects`를 `true`로 설정해야 합니다. 그렇지 않으면 오브젝트가 덮어쓰기됩니다. `_merge_objects`의 기본값은 `false`입니다.
{% endalert %}

{% endtab %}
{% tab 삭제 %}
커스텀 속성 오브젝트를 삭제하려면 커스텀 속성 오브젝트를 `null`로 설정하여 `users/track`으로 POST를 보내세요.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": null
    }
  ]
}
```

{% alert note %}
이 방법은 [오브젝트 배열]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects) 내부의 중첩 키를 삭제하는 데는 사용할 수 없습니다.
{% endalert %}

{% endtab %}
{% endtabs %}

## SDK 예제 {#sdk-example}

{% sdk_min_versions android:25.0.0 ios:6.1.0 web:4.7.0 %}

{% tabs local %}
{% tab Android SDK %}

**생성**
```kotlin
val json = JSONObject()
    .put("song_name", "Solea")
    .put("artist_name", "Miles Davis")
    .put("album_name", "Sketches of Spain")
    .put("genre", "Jazz")
    .put(
        "play_analytics",
        JSONObject()
            .put("count", 1000)
            .put("top_10_listeners", true)
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json)
}
```

**업데이트**
```kotlin
val json = JSONObject()
    .put("year_released", 1960)

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json, true)
}
```

**삭제**
```kotlin
braze.getCurrentUser { user ->
    user.unsetCustomUserAttribute("most_played_song")
}
```

{% endtab %}
{% tab Swift SDK %}

**생성**
```swift
let json: [String: Any?] = [
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": [
    "count": 1000,
    "top_10_listeners": true,
  ],
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json)
```

**업데이트**
```swift
let json: [String: Any?] = [
  "year_released": 1960
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json, merge: true)
```

**삭제**
```swift
braze.user.unsetCustomAttribute(key: "most_played_song")
```

{% endtab %}
{% tab Web SDK %}

**생성**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": {
    "count": 1000,
    "top_10_listeners": true
  }
};
braze.getUser().setCustomUserAttribute("most_played_song", json);
```

**업데이트**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "year_released": 1960
};
braze.getUser().setCustomUserAttribute("most_played_song", json, true);

```

**삭제**
```javascript
import * as braze from "@braze/web-sdk";
braze.getUser().setCustomUserAttribute("most_played_song", null);
```

{% endtab %}
{% endtabs %}

## 날짜를 오브젝트 등록정보로 캡처하기 {#capturing-dates-as-object-properties}

날짜를 오브젝트 등록정보로 캡처하려면 `$time` 키를 사용해야 합니다. 다음 예시에서는 "Important Dates" 오브젝트를 사용하여 `birthday`와 `wedding_anniversary`라는 오브젝트 등록정보 집합을 캡처합니다. 이러한 날짜의 값은 `$time` 키가 포함된 오브젝트이며, null 값이 될 수 없습니다.

{% alert note %}
처음에 날짜를 오브젝트 등록정보로 캡처하지 않은 경우, 모든 사용자에 대해 `$time` 키를 사용하여 이 데이터를 다시 전송하는 것이 좋습니다. 그렇지 않으면 `$time` 속성을 사용할 때 불완전한 Segment가 생성될 수 있습니다. 그러나 중첩 커스텀 속성의 `$time` 값이 올바른 형식이 아닌 경우 전체 중첩 커스텀 속성이 업데이트되지 않습니다.
{% endalert %}

```json
{
  "attributes": [
    {
      "external_id": "time_with_nca_test",
      "important_dates": {
        "birthday": {"$time" : "1980-01-01"},
        "wedding_anniversary": {"$time" : "2020-05-28"}
      }
    }
  ]
}
```

{% alert note %}
중첩 커스텀 속성의 경우 연도가 0 미만이거나 3000보다 크면 Braze는 해당 값을 사용자에게 저장하지 않습니다.
{% endalert %}

## Liquid 템플릿 {#liquid-templating}

다음 Liquid 템플릿 예시는 앞선 API 요청에서 저장된 커스텀 속성 오브젝트 등록정보를 참조하여 메시징에 사용하는 방법을 보여줍니다.

`custom_attribute` 개인화 태그와 점 표기법을 사용하여 오브젝트의 등록정보에 접근합니다. 오브젝트 이름(오브젝트 배열을 참조하는 경우 배열 내 위치)을 지정한 다음 점(마침표)과 등록정보 이름을 입력합니다.

{% raw %}
`{{custom_attribute.${most_played_song}[0].artist_name}}` — "Miles Davis"
<br> `{{custom_attribute.${most_played_song}[0].song_name}}` — "Solea"
<br> `{{custom_attribute.${most_played_song}[0].play_analytics.count}}` — "1000"
{% endraw %}

중첩 커스텀 속성 Liquid를 메시지에 사용하려면:

1. Campaign 또는 Canvas로 이동한 다음 개인화를 추가할 메시지 단계를 엽니다.
2. 메시지 작성기에서 값을 표시할 위치에 Liquid 스니펫을 삽입합니다.
3. 프로필에 이미 중첩 커스텀 속성이 있는 기존 사용자로 **미리보기 및 테스트**를 사용하여 값이 예상대로 렌더링되는지 확인합니다.

### 개인화 {#personalization}

**개인화 추가**를 사용하여 중첩 커스텀 속성을 메시지에 삽입할 수 있습니다.

**개인화 추가**를 열려면:

1. Campaign 또는 Canvas로 이동한 다음 개인화를 추가할 메시지 단계를 엽니다.
2. 메시지 작성기에서 **개인화**를 선택하여 **개인화 추가** 사이드바를 열고 개인화 옵션을 선택합니다.

중첩 커스텀 속성 개인화를 구성하려면:

1. **개인화 유형**에서 **중첩 커스텀 속성**을 선택합니다.
2. **최상위 속성**에서 삽입할 중첩 커스텀 속성 경로를 선택합니다.
   예를 들어, `preferences.neighborhood_office`를 선택합니다.
3. 선택 사항: **기본값**에 해당 속성에 대한 자체 값이 없는 사용자를 위한 대체 값을 입력합니다.
4. 생성된 **Liquid 스니펫**을 검토하여 예상 경로와 일치하는지 확인합니다.
5. **삽입**을 선택합니다.

이 예시에서 Braze는 `preferences.neighborhood_office`의 중첩 값을 메시지에 삽입합니다. 기본값은 해당 속성에 대한 자체 값이 없는 사용자를 위해 메시지에 포함되는 대체 값입니다.

{% alert tip %}
중첩 커스텀 속성을 삽입하는 옵션이 표시되지 않으면 스키마가 생성되었는지 확인하세요.
{% endalert %}

## 스키마 재생성 {#regenerate-schema}

스키마가 생성된 후에는 **캘린더 일 기준 하루에 한 번**(회사의 시간대 기준) 재생성할 수 있습니다. 이 섹션에서는 스키마를 재생성하는 방법을 설명합니다. 스키마에 대한 자세한 내용은 [중첩 오브젝트 탐색기를 사용하여 스키마 생성]({{site.baseurl}}/user_guide/audience/segments/segment_with_nested_custom_attributes#generate-schema)을 참조하세요.

중첩 커스텀 속성의 스키마를 재생성하려면:

1. **데이터 설정** > **커스텀 속성**으로 이동합니다.
2. 중첩 커스텀 속성을 검색합니다.
3. 속성의 **속성 이름** 열에서 <i class="fas fa-plus" aria-label="스키마 관리"></i> **스키마 관리**를 선택하여 스키마를 관리합니다.
4. 모달이 나타납니다. **스키마 재생성**을 선택합니다.

**스키마 재생성** 동작은 회사의 시간대 기준으로 **캘린더 일 기준 하루에 한 번**으로 제한됩니다. 스키마 작업이 이미 **진행 중**인 경우(상태가 **생성 중**인 동안에는 옵션을 사용할 수 없음) 다른 재생성을 시작할 수 없습니다. 스키마 재생성은 새 오브젝트만 감지하며 현재 스키마에 존재하는 오브젝트를 삭제하지 않습니다.

{% alert important %}
기존 오브젝트가 있는 오브젝트 배열의 스키마를 초기화하려면 새 커스텀 속성을 생성해야 합니다. 스키마 재생성은 기존 오브젝트를 삭제하지 않습니다.
{% endalert %}

스키마를 재생성한 후 데이터가 예상대로 표시되지 않으면 해당 속성이 충분히 자주 수집되지 않을 수 있습니다. 사용자 데이터는 해당 중첩 속성에 대해 Braze에 이전에 전송된 데이터를 기반으로 샘플링됩니다. 속성이 충분히 수집되지 않으면 스키마에 반영되지 않습니다.

## 중첩 커스텀 속성 변경 트리거 {#trigger-nested-custom-attribute-changes}

중첩 커스텀 속성 오브젝트가 변경될 때 트리거할 수 있습니다. 이 옵션은 오브젝트 배열의 변경에는 사용할 수 없습니다. 경로 탐색기를 볼 수 있는 옵션이 표시되지 않으면 스키마가 생성되었는지 확인하세요.

예를 들어, 실행 기반 Campaign에서 **커스텀 속성 값 변경**에 대한 새 트리거 동작을 추가하여 지역 사무소 선호도를 변경한 사용자를 타겟팅할 수 있습니다.

실행 기반 Campaign에서 이 트리거를 구성하려면:

1. Campaign을 생성하거나 편집한 다음 전달 유형을 **실행 기반 전달**로 설정합니다.
2. 트리거 설정에서 **커스텀 속성 값 변경**을 선택합니다.
3. 모니터링할 중첩 커스텀 속성 경로를 선택합니다.
   예를 들어, `preferences.neighborhood_office`를 선택합니다.
4. 원하는 트리거 조건(예: **새 값**)을 선택합니다.
5. Campaign 메시지와 오디언스 구성을 완료한 다음 Campaign을 시작합니다.

## 오브젝트 배열에서의 세분화 동작 {#segmentation-behavior-with-arrays-of-objects}

오브젝트 배열에 대해 여러 `Nested Custom Attribute` 필터를 AND 로직으로 사용하여 세분화할 때, 각 필터는 배열의 모든 항목에 대해 독립적으로 평가됩니다. 배열의 _어떤_ 항목이든 각 개별 필터를 충족하면 사용자가 Segment에 해당됩니다. 필터가 _동일한_ 항목과 일치할 필요는 없습니다.

예를 들어, 사용자에게 다음과 같은 배열이 있다고 가정합니다:

```json
{
  "orders": [
    {"product": "Shoes", "price": 80},
    {"product": "Hat", "price": 25}
  ]
}
```

다음 AND 필터가 있는 Segment:

- `orders[].price`가 50보다 큼
- `orders[].price`가 30보다 작음

이 사용자는 첫 번째 필터가 "Shoes" 항목(80 > 50)과 일치하고 두 번째 필터가 "Hat" 항목(25 < 30)과 일치하므로 해당됩니다. 단일 항목이 두 조건을 모두 충족하지 않더라도 사용자는 여전히 Segment에 포함됩니다.

배열 내 동일한 항목에서 모든 조건이 일치해야 하는 경우, 동일한 경로에서 [다중 기준 세분화]({{site.baseurl}}/user_guide/audience/segments/segment_with_nested_custom_attributes#use-multi-criteria-segmentation)를 사용하거나 교차 항목 매칭을 방지하도록 데이터를 재구성하세요.

## 데이터 포인트 {#data-points}

전송되는 모든 키는 데이터 포인트를 소비합니다. 예를 들어, 고객 프로필에서 초기화된 이 오브젝트는 7개의 데이터 포인트를 소비합니다:

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "year_released": 1960,
        "genre": "Jazz",
        "play_analytics": {
          "count": 1000,
          "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% alert note %}
커스텀 속성 오브젝트를 `null`로 업데이트하는 것도 데이터 포인트를 소비합니다.
{% endalert %}