---
nav_title: "POST: 사용자 별칭 업데이트"
article_title: "POST: 사용자 별칭 업데이트"
search_tag: Endpoint
page_order: 2
layout: api_page
page_type: reference
description: "이 문서에서는 사용자 별칭 업데이트 Braze 엔드포인트에 대한 자세한 내용을 설명합니다."
---
{% api %}
# 사용자 별칭 업데이트 {#update-user-alias}
{% apimethod post %}
/users/alias/update
{% endapimethod %}

> 이 엔드포인트를 사용하여 기존 사용자 별칭을 업데이트합니다.

요청당 최대 50개의 사용자 별칭을 지정할 수 있습니다.

사용자 별칭을 업데이트하려면 `alias_label`, `old_alias_name`, `new_alias_name`이 업데이트 사용자 별칭 오브젝트에 포함되어야 합니다. `alias_label` 및 `old_alias_name`에 연결된 사용자 별칭이 없는 경우 별칭이 업데이트되지 않습니다. 주어진 `alias_label` 및 `old_alias_name`이 발견되면 `old_alias_name`이 `new_alias_name`으로 업데이트됩니다.

{% alert note %}
이 엔드포인트는 업데이트되는 `alias_updates` 오브젝트의 순서를 보장하지 않습니다.
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#a084b843-b3cd-43f0-bfb1-ef7bada839c5 {% endapiref %}

## 필수 조건 {#prerequisites}

이 엔드포인트를 사용하려면 `users.alias.update` 권한이 있는 [API 키]({{site.baseurl}}/api/basics)가 필요합니다.

## 사용량 제한 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='users alias update' %}

## 요청 본문 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "alias_updates" : (required, array of update user alias object)
}
```

### 요청 매개변수 {#request-parameters}

| 매개변수 | 필수 | 데이터 유형 | 설명 |
| --------- | --------- | --------- | ----------- |
| `alias_updates` | 필수 | 업데이트 사용자 별칭 오브젝트 배열 | [사용자 별칭 오브젝트]({{site.baseurl}}/api/objects_filters/user_alias_object)를 참조하세요.<br><br> `old_alias_name`, `new_alias_name`, `alias_label`에 대한 자세한 내용은 [사용자 별칭]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases)을 참조하세요. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="요청 매개변수" }

### 업데이트 사용자 별칭 오브젝트 사양이 포함된 엔드포인트 요청 본문 {#endpoint-request-body-with-update-user-alias-object-specification}

```json
{
  "alias_label" : (required, string),
  "old_alias_name" : (required, string),
  "new_alias_name" : (required, string)
}
```

## 요청 예시 {#example-request}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "alias_updates" :[
    {
      "alias_label": "example_alias_label",
      "old_alias_name" : "example_old_alias_name",
      "new_alias_name" : "example_new_alias_name"
    }
  ]
}'
```

{% endapi %}