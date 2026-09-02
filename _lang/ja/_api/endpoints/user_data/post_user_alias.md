---
nav_title: "POST:新しいユーザーエイリアスを作成する"
article_title: "POST:新しいユーザーエイリアスを作成する"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、「新しいユーザーエイリアスの作成」Brazeエンドポイントの詳細について説明します。"
---
{% api %}
# 新しいユーザーエイリアスを作成する {#create-new-user-alias}
{% apimethod post %}
/users/alias/new
{% endapimethod %}

> このエンドポイントを使用して、既存の識別済みユーザーに新しいユーザーエイリアスを追加するか、新しい未識別ユーザーを作成します。

リクエストごとに最大50個のユーザーエイリアスを指定できます。

**既存のユーザーにユーザーエイリアスを追加する**には、新しいユーザーエイリアスオブジェクトに`external_id`を含める必要があります。オブジェクトに`external_id`が存在しても、その`external_id`を持つユーザーがいない場合、エイリアスはどのユーザーにも追加されません。`external_id`が存在しない場合でもユーザーは作成されますが、後で識別する必要があります。これは「Identifying Users」と`users/identify`エンドポイントを使用して行うことができます。

**エイリアスのみの新規ユーザーを作成する**には、新しいユーザーエイリアスオブジェクトから`external_id`を省略する必要があります。ユーザーが作成されたら、`/users/track`エンドポイントを使用してエイリアスのみのユーザーに属性、イベント、購入を関連付け、`/users/identify`エンドポイントを使用して`external_id`でユーザーを識別します。

[`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)エンドポイントを使用して、`user_alias`でAPIトリガーキャンペーンをユーザーに送信できます。

## `alias_label`と`alias_name`が既に存在する場合 {#when-alias_label-and-alias_name-already-exist}

`alias_label`と`alias_name`の組み合わせは、ユーザー群全体で一意である必要があります。詳細については、[ユーザーエイリアス]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases)を参照してください。

`alias_label`と`alias_name`のペアが既にいずれかのユーザーに存在するリクエストを送信した場合（同じユーザーか別のユーザーかを問わず）、エンドポイントは成功レスポンスを返します（例：`"aliases_processed": 1`、`"message": "success"`）。この場合、リクエスト内のユーザーに新しいエイリアスは追加されません。`alias_label`と`alias_name`のペアが既に使用されているため、リクエストは変更を行わず、該当ユーザーにエイリアスが追加されなかったように見えることがあります。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5cf18e64-fd02-452f-8c90-9a0f7c4d0487 {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`users.alias.new`権限を持つ[APIキー]({{site.baseurl}}/api/basics)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='users alias new' %}

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "user_aliases" : (required, array of new user alias object)
}
```

### リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `user_aliases` | 必須 | 新しいユーザーエイリアスオブジェクトの配列 | [ユーザーエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object)を参照してください。<br><br>`alias_name`と`alias_label`の詳細については、[ユーザーエイリアス]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle#user-aliases)のドキュメントを参照してください。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

### 新しいユーザーエイリアスオブジェクトを指定したエンドポイントリクエスト本文 {#endpoint-request-body-with-new-user-alias-object-specification}

```json
{
  "external_id" : (optional, string),
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```

## リクエスト例 {#example-request}
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

## レスポンス {#response}

同じ`alias_label`と`alias_name`が既にユーザーに存在するためにエイリアスがスキップされた場合でも、レスポンス本文は成功を示すことがあります。詳細については、[エイリアスラベルと名前が既に存在する場合](#when-the-alias-label-and-name-already-exist)を参照してください。

```json
{
    "aliases_processed": 1,
    "message": "success"
}
```

## トラブルシューティング {#troubleshooting}

### このエンドポイントでユーザーエイリアスを作成した後、属性が更新されないのはなぜですか？ {#why-are-my-attributes-not-updating-after-i-create-a-user-alias-using-this-endpoint}

これは通常、`/users/alias/new`の後に別の`/users/track`リクエストを送信してエイリアスで属性を更新しようとした場合に発生します。Brazeが新しい`alias_label`と`alias_name`のペアをプロファイルに一貫して解決できるようになる前にトラックリクエストが処理されるため、属性が期待するユーザーに反映されません。

**推奨されるアプローチ：** エイリアスのみのプロファイルを作成する場合、または既に存在するエイリアスでプロファイルを更新する場合にのみ、単一の[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track)呼び出しを使用してください。`attributes`配列内で、`user_alias`とプロファイルフィールドを同じ[ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object)に配置することで、Brazeがユーザーの解決と更新の適用を1つのステップで行います。

そのオブジェクトからエイリアスのみのプロファイルを作成する必要がある場合は、`_update_existing_only`を`false`に設定してください。`user_alias`を使用しているときにこれを省略すると、Brazeはデフォルトで更新のみの動作となり、エイリアスのみのプロファイルは作成されません。エイリアスがワークスペース内のユーザーに既に存在する場合、同じリクエストでそのプロファイルが新しい属性で更新されます。

`/users/track`を使用して、`external_id`で識別された既存のユーザーに新しいエイリアスを追加することはできません。ユーザー属性オブジェクトでは、`external_id`と`user_alias`は相互に排他的です。識別済みユーザーにエイリアスを追加するには、まず`/users/alias/new`を呼び出してください。エイリアスが関連付けられた後、`/users/track`で`external_id`または既存のエイリアスを使用してそのプロファイルを更新できます。

たとえば、以下の`/users/track`本文は、エイリアスがまだ存在しない場合はエイリアスのみのプロファイルを作成し、そのエイリアスを既に持つ既存のプロファイルがある場合はそのプロファイルを更新します。
```json
{
  "attributes": [
    {
      "user_alias": {
        "alias_name": "example@example.com",
        "alias_label": "email"
      },
      "_update_existing_only": false,
      "string_attribute": "test_alias_only_update"
    }
  ]
}
```

{% endapi %}