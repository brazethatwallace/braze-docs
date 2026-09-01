---
nav_title: "オブジェクトを識別するためのエイリアス"
article_title: オブジェクトを識別するためのAPIエイリアス
page_order: 11
page_type: reference
description: "この記事では、オブジェクトを識別するためのエイリアスの仕様について説明します。"

---

# オブジェクトを識別するためのエイリアス {#aliases-to-identify-object}

属性オブジェクトにフィールドを含むAPIリクエストは、指定されたユーザープロファイルに対して、その名前の属性を指定された値で作成または更新します。

Brazeユーザープロファイルのフィールド名（以下にリストされているもの、または[Brazeユーザープロファイルフィールド]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)のセクションにリストされているもの）を使用して、ダッシュボードのユーザープロファイル上の特別な値を更新するか、独自のカスタム属性データをユーザーに追加します。

## オブジェクト本体 {#object-body}

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

- [外部ユーザー ID]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)
- [ユーザーエイリアス]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases)