---
nav_title: "POST: 새 사용자 별칭 만들기"
article_title: "POST: 새 사용자 별칭 만들기"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "이 문서에서는 새 사용자 별칭 만들기 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."

---
{% api %}
# 새 사용자 별칭 만들기 {#create-new-user-alias}
{% apimethod post %}
/users/alias/new
{% endapimethod %}

> 이 엔드포인트를 사용하여 기존 식별된 사용자에 대한 새 사용자 별칭을 추가하거나 식별되지 않은 새 사용자를 만들 수 있습니다.

요청당 최대 50개의 사용자 별칭을 지정할 수 있습니다.

**기존 사용자의 사용자 별칭을 추가하려면** 새 사용자 별칭 오브젝트에 `external_id`를 포함해야 합니다. 오브젝트에 `external_id`가 있지만 해당 `external_id`를 가진 사용자가 없는 경우 별칭은 어떤 사용자에게도 추가되지 않습니다. `external_id`가 없으면 사용자는 계속 생성되지만 나중에 식별해야 합니다. "사용자 식별" 및 `users/identify` 엔드포인트를 사용하여 이 작업을 수행할 수 있습니다.

**별칭 전용 사용자를 새로 만들려면** 새 사용자 별칭 오브젝트에서 `external_id`를 생략해야 합니다. 사용자가 생성된 후 `/users/track` 엔드포인트를 사용하여 별칭 전용 사용자를 속성, 이벤트 및 구매와 연결하고, `/users/identify` 엔드포인트를 사용하여 `external_id`로 사용자를 식별합니다.

## `alias_label`과 `alias_name`이 이미 존재하는 경우 {#when-alias_label-and-alias_name-already-exist}

`alias_label`과 `alias_name`의 조합은 사용자 기반 전체에서 고유해야 합니다. 자세한 내용은 [사용자 별칭]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)을 참조하세요.

`alias_label`과 `alias_name` 쌍이 이미 어떤 사용자에게 존재하는 경우(동일한 사용자이든 다른 사용자이든) 요청을 보내면 엔드포인트는 여전히 성공 응답을 반환합니다(예: `"aliases_processed": 1`, `"message": "success"`). 이 경우 요청의 사용자에게 새 별칭이 추가되지 않습니다. `alias_label`과 `alias_name` 쌍이 이미 사용 중이므로 요청은 어떤 변경도 수행하지 않으며, 해당 사용자에게 별칭이 추가되지 않은 것처럼 보일 수 있습니다.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5cf18e64-fd02-452f-8c90-9a0f7c4d0487 {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `users.alias.new` 권한이 있는 [API 키]({{site.baseurl}}/api/api_key/)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='users alias new' %}

## 요청 본문 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "user_aliases" : (required, array of new user alias object)
}
```

### 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | ---------| --------- | ----------- |
| `user_aliases` | 필수 | 새 사용자 별칭 오브젝트 배열 | [사용자 별칭 오브젝트]({{site.baseurl}}/api/objects_filters/user_alias_object/)를 참조하세요.<br><br> `alias_name` 및 `alias_label`에 대한 자세한 내용은 [사용자 별칭]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) 설명서를 참조하세요.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### 새 사용자 별칭 오브젝트 사양이 포함된 엔드포인트 요청 본문 {#endpoint-request-body-with-new-user-alias-object-specification}

```json
{
  "external_id" : (optional, string),
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```

## 요청 예시 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/new' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "user_aliases" :[
    {
      "external_id": "external_identifier",
      "alias_name" : "example_name",
      "alias_label" : "example_label"
    }
  ]
}'
```

## 응답 {#response}

동일한 `alias_label`과 `alias_name`이 이미 사용자에게 존재하여 별칭이 건너뛰어진 경우에도 응답 본문은 여전히 성공을 나타낼 수 있습니다. 자세한 내용은 [별칭 라벨과 이름이 이미 존재하는 경우](#when-the-alias-label-and-name-already-exist)를 참조하세요.

```json
{
    "aliases_processed": 1,
    "message": "success"
}
```


{% endapi %}