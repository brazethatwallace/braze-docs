---
nav_title: 객체 배열
article_title: 객체 배열
alias: "/array_of_objects/"
page_order: 2
page_type: reference
description: "이 참조 문서에서는 객체 배열을 커스텀 속성의 데이터 유형으로 사용하는 방법과 제한 사항 및 사용 예시를 설명합니다."
---

# 객체 배열 {#array-of-objects}

> 이 페이지에서는 객체 배열을 사용하여 관련 속성을 그룹화하는 방법을 설명합니다. 예를 들어, 한 사용자에게 속하는 애완동물 객체, 노래 객체, 계정 객체 그룹이 있을 수 있습니다. 이러한 객체 배열을 사용하여 Liquid로 메시지를 개인화하거나, 객체 내의 요소가 기준과 일치하는 경우 오디언스 Segment를 만들 수 있습니다.

{% multi_lang_include nested_attribute_objects/supported_data_types.md %}

## 고려 사항 {#considerations}

- 객체 배열은 API를 통해 전송되는 커스텀 속성을 위한 것입니다. CSV 업로드는 지원되지 않습니다. CSV 파일의 쉼표가 열 구분 기호로 해석되어 값에 포함된 쉼표가 구문 분석 오류를 유발하기 때문입니다.
- 객체 배열은 항목 수에 제한이 없지만 최대 크기는 100&nbsp;KB입니다. 업데이트(`$add` 또는 `$update` 등)로 인해 배열이 이 제한을 초과하면 Braze는 업데이트를 삭제하고 속성은 변경되지 않습니다. API 요청은 여전히 성공 응답을 반환합니다. 새 항목을 추가할 수 있도록 배열을 제한 이하로 유지하려면 먼저 `$remove`를 사용하여 배열에서 항목을 삭제하세요.
- 모든 Braze 파트너가 객체 배열을 지원하는 것은 아닙니다. 통합에서 이 기능을 지원하는지 확인하려면 [파트너 설명서]({{site.baseurl}}/partners/home)를 참조하세요.

배열의 항목을 업데이트하거나 제거하려면 키와 값으로 항목을 식별해야 하므로 배열의 각 항목에 고유 식별자를 포함하는 것이 좋습니다. 고유성은 해당 배열 범위로만 한정되며, 배열에서 특정 객체를 업데이트하거나 제거하려는 경우에 유용합니다. 이는 Braze에서 강제하지 않습니다.

{% alert important %}
요청 내 중첩 커스텀 속성에 유효하지 않은 값(예: 잘못된 시간 형식 또는 `null` 값)이 포함된 경우, Braze는 해당 요청의 모든 중첩 커스텀 속성 업데이트를 처리에서 제외합니다. 이는 해당 특정 속성 내의 모든 중첩 구조에 적용됩니다. 전송하기 전에 중첩 커스텀 속성 내의 모든 값이 유효한지 확인하세요. 자세한 내용은 [사용자 생성 및 업데이트]({{site.baseurl}}/api/endpoints/user_data/post_user_track#how-does-userstrack-handle-invalid-nested-custom-attributes)를 참조하세요.
{% endalert %}

{% alert tip %}
사용자 속성 객체에 대한 객체 배열 사용 방법에 대해 자세히 알아보려면 [사용자 속성 오브젝트]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrate-push-tokens)를 참조하세요.
{% endalert %}

## API 예제 {#api-example}

객체 배열로 저장되는 중첩 커스텀 속성을 생성하거나 업데이트하는 `/users/track` 요청을 보낼 때 이 예제를 사용하세요. 페이로드는 `$add`, `$remove`, `$update` 연산자를 사용하므로 매 요청마다 전체 배열을 다시 구축하지 않고도 특정 객체를 변경할 수 있습니다.

{% tabs local %}
{% tab 생성 %}

다음은 `pets` 배열을 사용한 `/users/track` 예제입니다. 펫의 속성정보를 캡처하려면 `pets`를 객체 배열로 나열하는 API 요청을 보내세요. 각 객체에는 나중에 업데이트할 때 참조할 수 있는 고유한 `id`가 할당되어 있습니다.

속성을 처음 생성하거나 전체 배열을 새로운 기본 객체 세트로 교체하려는 경우 이 형식을 사용하세요.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Mochi"
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Pixel"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab 추가 %}

`$add` 연산자를 사용하여 배열에 다른 항목을 추가합니다. 다음 예제는 사용자의 `pets` 배열에 세 개의 펫 객체를 추가하는 방법을 보여줍니다.

하나 이상의 새 객체를 추가하면서 기존 객체는 변경하지 않으려면 `$add`를 사용하세요.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$add": [
          {
            "id": 3,
            "type": "dog",
            "breed": "corgi",
            "name": "Biscuit"
          },
          {
            "id": 4,
            "type": "fish",
            "breed": "salmon",
            "name": "Pepper"
          },
           {
            "id": 5,
            "type": "bird",
            "breed": "parakeet",
            "name": "Noodle"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab 업데이트 %}

`_merge_objects` 매개변수와 `$update` 연산자를 사용하여 배열 내 특정 객체의 값을 업데이트합니다. 다른 [중첩 커스텀 속성]({{site.baseurl}}/nested_custom_attribute_support#api-request-body) 객체에 대한 업데이트와 유사하게, 이는 딥 머지를 수행합니다.

`$update`는 배열 내 객체에서 중첩 속성정보를 제거하는 데 사용할 수 없습니다. 이를 수행하려면 배열에서 전체 항목을 제거한 다음 해당 특정 키 없이 객체를 추가해야 합니다(`$remove`와 `$add`의 조합 사용).

객체가 이미 존재하고 `$identifier_key`와 `$identifier_value`로 매칭하여 하나 이상의 필드를 변경하려면 `$update`를 사용하세요.

다음 예제는 `id`가 `4`인 객체의 `breed` 속성정보를 `goldfish`로 업데이트하는 방법을 보여줍니다. 이 요청 예제는 또한 `id`가 `5`인 객체의 `name`을 `Annette`로 업데이트합니다. `_merge_objects` 매개변수가 `true`로 설정되어 있으므로, 이 두 객체의 다른 모든 필드는 동일하게 유지됩니다.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "pets": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "breed": "goldfish"
            }
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 5,
            "$new_object": {
              "name": "Annette"
            }
          }
        ]
      }
    }
  ]
}
```

{% alert warning %}
`_merge_objects`를 true로 설정해야 합니다. 그렇지 않으면 객체가 덮어쓰기됩니다. `_merge_objects`는 기본값으로 false입니다.
{% endalert %}

{% endtab %}
{% tab 제거 %}

`$remove` 연산자를 일치하는 키(`$identifier_key`)와 값(`$identifier_value`)과 함께 사용하여 배열에서 객체를 제거합니다.

`id = 2` 또는 `type = dog`와 같이 알려진 식별자 쌍에 대해 일치하는 모든 객체를 삭제하려면 `$remove`를 사용하세요.

다음 예제는 `pets` 배열에서 `id` 값이 `1`인 객체, `id` 값이 `2`인 객체, `type` 값이 `dog`인 객체를 제거하는 방법을 보여줍니다. `type` 값이 `dog`인 객체가 여러 개 있는 경우, 일치하는 모든 객체가 제거됩니다.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Remove by ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Remove any dog
          {
            "$identifier_key": "type",
            "$identifier_value": "dog"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

### 처리 순서 {#processing-order}

단일 `/users/track` 요청에 동일한 배열 속성에 대한 `$add`, `$remove`, `$update` 작업이 포함된 경우, Braze는 다음 순서로 처리합니다.

1. `$add`
2. `$remove`
3. `$update`

이 순서는 하나의 요청 내 단일 속성 업데이트 객체에 적용되며, 모든 작업이 평가된 후 배열의 최종 상태를 결정합니다.

`$add`가 `$remove`보다 먼저 실행되므로, 단일 요청 내에서 `$remove` 후 `$add`를 업서트 메커니즘으로 사용할 수 없습니다. `$add`가 먼저 처리된 다음 `$remove`가 항목을 삭제합니다. 업서트를 수행하려면 `$add` 전에 별도의 요청으로 `$remove`를 보내세요.

### 타임스탬프 {#timestamps}

객체 배열에 타임스탬프와 같은 필드를 포함할 때는 일반 문자열이나 Unix 에포크 정수 대신 `$time` 형식을 사용하세요.

```json
{
  "attributes": [
    {
      "external_id": "user123",
      "purchases": [
        {
          "item_name": "T-shirt",
          "price": 19.99,
          "purchase_time": {
            "$time": "2020-05-28"
          }
        }
      ]
    }
  ]
}
```

{% alert tip %}
자세한 내용은 [중첩 커스텀 속성]({{site.baseurl}}/user_guide/data/activation/attributes/nested_custom_attribute_support)을 참조하세요.
{% endalert %}

## SDK 예제 {#sdk-example}

{% tabs local %}
{% tab Android SDK %}
{% subtabs %}
{% subtab 생성 %}
```kotlin
val json = JSONArray()
    .put(JSONObject()
        .put("id", 1)
        .put("type", "dog")
        .put("breed", "beagle")
        .put("name", "Gus"))
    .put(JSONObject()
        .put("id", 2)
        .put("type", "cat")
        .put("breed", "calico")
        .put("name", "Pixel")
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json)
}
```
{% endsubtab %}

{% subtab 추가 %}
```kotlin
val json = JSONObject()
    .put("\$add", JSONArray()
        .put(JSONObject()
            .put("id", 3)
            .put("type", "dog")
            .put("breed", "corgi")
            .put("name", "Doug"))
        .put(JSONObject()
            .put("id", 4)
            .put("type", "fish")
            .put("breed", "salmon")
            .put("name", "Pepper"))
        .put(JSONObject()
            .put("id", 5)
            .put("type", "bird")
            .put("breed", "parakeet")
            .put("name", "Noodle")
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}

{% subtab 업데이트 %}
```kotlin
val json = JSONObject()
    .put("\$update", JSONArray()
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 4)
            .put("\$new_object", JSONObject()
                .put("breed", "goldfish")
            )
        )
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 5)
            .put("\$new_object", JSONObject()
                .put("name", "Annette")
            )
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}

{% subtab 삭제 %}
```kotlin
val json = JSONObject()
    .put("\$remove", JSONArray()
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 1)
        )
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 2)
        )
        .put(JSONObject()
            .put("\$identifier_key", "type")
            .put("\$identifier_value", "dog")
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Swift SDK %}
{% subtabs %}
{% subtab 생성 %}
```swift
let json: [[String: Any?]] = [
  [
    "id": 1,
    "type": "dog",
    "breed": "beagle",
    "name": "Mochi"
  ],
  [
    "id": 2,
    "type": "cat",
    "breed": "calico",
    "name": "Pixel"
  ]
]

braze.user.setCustomAttribute(key: "pets", array: json)
```
{% endsubtab %}

{% subtab 추가 %}
```swift
let json: [String: Any?] = [
  "$add": [
    [
      "id": 3,
      "type": "dog",
      "breed": "corgi",
      "name": "Biscuit"
    ],
    [
      "id": 4,
      "type": "fish",
      "breed": "salmon",
      "name": "Pepper"
    ],
    [
      "id": 5,
      "type": "bird",
      "breed": "parakeet",
      "name": "Noodle"
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}

{% subtab 업데이트 %}
```swift
let json: [String: Any?] = [
  "$update": [
    [
      "$identifier_key": "id",
      "$identifier_value": 4,
      "$new_object": [
        "breed": "goldfish"
      ]
    ],
    [
      "$identifier_key": "id",
      "$identifier_value": 5,
      "$new_object": [
        "name": "Annette"
      ]
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}

{% subtab 삭제 %}
```swift
let json: [String: Any?] = [
  "$remove": [
    [
      "$identifier_key": "id",
      "$identifier_value": 1,
    ],
    [
      "$identifier_key": "id",
      "$identifier_value": 2,
    ],
    [
      "$identifier_key": "type",
      "$identifier_value": "dog",
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
중첩 커스텀 속성은 AppboyKit에서 지원되지 않습니다.
{% endalert %}
{% endtab %}

{% tab Web SDK %}
{% subtabs local %}
{% subtab 생성 %}
```javascript
import * as braze from "@braze/web-sdk";
const json = [{
  "id": 1,
  "type": "dog",
  "breed": "beagle",
  "name": "Mochi"
}, {
  "id": 2,
  "type": "cat",
  "breed": "calico",
  "name": "Pixel"
}];
braze.getUser().setCustomUserAttribute("pets", json);
```
{% endsubtab %}

{% subtab 추가 %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$add": [{
    "id":  3,
    "type":  "dog",
    "breed":  "corgi",
    "name":  "Doug",
  }, {
    "id":  4,
    "type":  "fish",
    "breed":  "salmon",
    "name":  "Pepper",
  }, {
    "id":  5,
    "type":  "bird",
    "breed":  "parakeet",
    "name":  "Noodle",
  }]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}

{% subtab 업데이트 %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$update": [
    {
      "$identifier_key": "id",
      "$identifier_value": 4,
      "$new_object": {
        "breed": "goldfish"
      }
    },
    {
      "$identifier_key": "id",
      "$identifier_value": 5,
      "$new_object": {
        "name": "Annette"
      }
    }
  ]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}

{% subtab 삭제 %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$remove": [
    {
      "$identifier_key": "id",
      "$identifier_value": 1,
    },
    {
      "$identifier_key": "id",
      "$identifier_value": 2,
    },
    {
      "$identifier_key": "type",
      "$identifier_value": "dog",
    }
  ]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Liquid 템플릿 {#liquid-templating}

이 `pets` 배열을 사용하여 메시지를 개인화할 수 있습니다. 다음 Liquid 템플릿 예제는 앞선 API 요청에서 저장된 커스텀 속성 객체 속성정보를 참조하고 메시징에 사용하는 방법을 보여줍니다.

{% raw %}
```liquid
{% assign pets = {{custom_attribute.${pets}}} %}

{% for pet in pets %}
I have a {{pet.type}} named {{pet.name}}! They are a {{pet.breed}}.
{% endfor %}
```
{% endraw %}

이 시나리오에서는 Liquid를 사용하여 `pets` 배열을 반복하고 각 펫에 대한 문장을 출력할 수 있습니다. `pets` 커스텀 속성에 [변수를 할당]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/dashboard_tools#assign-variables)하고 점 표기법을 사용하여 객체의 속성정보에 접근합니다. 객체 이름 뒤에 마침표 `.`를 입력하고, 그 뒤에 속성정보 이름을 지정합니다.

## 세분화 {#segmentation}

객체 배열을 기반으로 사용자를 세분화할 때, 배열의 객체 중 하나라도 기준과 일치하면 해당 사용자는 Segment에 포함됩니다.

새 Segment를 생성하고 필터로 **중첩 커스텀 속성**을 선택합니다. 그런 다음 객체 배열의 이름을 검색하고 선택합니다.

![객체 배열로 필터링합니다.]({% image_buster /assets/img_archive/array_of_objects_segmenting_1.gif %})

점 표기법을 사용하여 객체 배열에서 사용할 필드를 지정합니다. 텍스트 필드를 빈 대괄호 `[]`로 시작하여 Braze에 객체 배열 내부를 조회하고 있음을 알립니다. 그 뒤에 마침표 `.`를 추가하고, 사용할 필드 이름을 입력합니다.

예를 들어, `type` 필드를 기반으로 `top_3_movies` 객체 배열을 필터링하려면 `[].type`을 입력하고 `Fantasy Movie`와 같이 필터링할 영화를 선택합니다.


### 중첩 수준 {#levels-of-nesting}

최대 한 수준의 배열 중첩(배열 내의 배열)으로 Segment를 생성할 수 있습니다. 예를 들어, 다음 속성이 주어진 경우 `pets[].name`에 `Mochi`가 포함된 Segment는 만들 수 있지만, `pets[].nicknames[]`에 `Gugu`가 포함된 Segment는 만들 수 없습니다.

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Mochi",
          "nicknames": [
            "MoMo",
            "Mochi"
          ]
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Pixel",
          "nicknames": [
            "PiPi",
            "Pixel"
          ]
        }
      ]
    }
  ]
}
```
{% endraw %}

## 데이터 포인트 {#data-points}

데이터 포인트는 속성정보를 생성, 업데이트 또는 제거하는지에 따라 다르게 기록됩니다.

{% tabs local %}
{% tab 생성 %}

새 배열을 생성하면 객체의 각 속성에 대해 하나의 데이터 포인트가 기록됩니다. 이 예제는 8개의 데이터 포인트가 소비됩니다. 각 펫 객체에는 4개의 속성이 있고 객체가 2개 있기 때문입니다.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Mochi"
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Pixel"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab 업데이트 %}

기존 배열을 업데이트하면 추가된 각 속성정보에 대해 하나의 데이터 포인트가 기록됩니다. 이 예제는 두 개의 객체 각각에서 하나의 속성정보만 업데이트하므로 2개의 데이터 포인트가 소비됩니다.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "pets": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "breed": "goldfish"
            }
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 5,
            "$new_object": {
              "name": "Annette"
            }
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab 제거 %}

배열에서 객체를 제거하면 전송하는 각 제거 기준에 대해 하나의 데이터 포인트가 기록됩니다. 이 예제는 이 구문으로 여러 마리의 개를 제거할 수 있더라도 3개의 데이터 포인트가 소비됩니다.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Remove by ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Remove any dog
          {
            "$identifier_key": "type",
            "$identifier_value": "dog"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}