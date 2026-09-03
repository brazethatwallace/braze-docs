---
nav_title: "오브젝트 식별을 위한 별칭"
article_title: 오브젝트 식별을 위한 API 별칭
page_order: 11
page_type: reference
description: "이 문서에서는 오브젝트 식별을 위한 별칭 사양에 대해 설명합니다."

---

# 오브젝트 식별을 위한 별칭 {#aliases-to-identify-object}

속성 오브젝트에 필드가 있는 API 요청은 지정된 고객 프로필에 해당 이름의 속성을 지정된 값으로 생성하거나 업데이트합니다.

Braze 고객 프로필 필드 이름(아래에 나열되거나 [Braze 고객 프로필 필드]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields) 섹션에 나열된 항목)을 사용하여 대시보드의 고객 프로필에서 해당 특수 값을 업데이트하거나, 커스텀 속성 데이터를 추가할 수 있습니다.

## 오브젝트 본문 {#object-body}

```json
{
  "aliases_to_identify" : (required, array of aliases to identify object)
  [
    {
      "external_id" : (required, string) see External user ID,
      // external_ids for users that do not exist return a non-fatal error.
      // See server responses for details.
      "user_alias" : {
        "alias_name" : (required, string) see User aliases,
        "alias_label" : (required, string) see User aliases
      }
    }
  ]
}
```

- [외부 사용자 ID]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)
- [사용자 별칭]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases)