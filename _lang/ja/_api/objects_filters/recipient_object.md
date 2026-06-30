---
nav_title: "受信者オブジェクト"
article_title: API 受信者オブジェクト
page_order: 9
page_type: reference
description: "この参照記事では、Braze 受信者オブジェクトのさまざまなコンポーネントについて説明します。"

---

# 受信者オブジェクト {#recipients-object}

> 受信者オブジェクトを使用すると、エンドポイントで情報をリクエストしたり書き込んだりできます。

このオブジェクトには、`external_user_id`、`user_alias`、`braze_id`、または `email` のいずれかを含める必要があります。**リクエストでは1つだけ指定してください。**

受信者オブジェクトを使用すると、[ユーザーエイリアスオブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object)、[トリガープロパティオブジェクト]({{site.baseurl}}/api/objects_filters/trigger_properties_object)、[Canvasエントリプロパティオブジェクト]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/context)、および[ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrating-push-tokens)を組み合わせることができます。

## オブジェクト本体 {#object-body}

```json
[{
  "user_alias": (optional, User Alias Object) User alias of user to receive message,
  "external_user_id": (optional, string) see External user ID,
  "braze_id": (optional, string) see Braze ID,
  "email": (optional, string) email address of user to receive message,
  "prioritization": (optional, array) see Prioritization; required when using email,
  "trigger_properties": (optional, object) personalization key-value pairs for this user when sending a campaign or message; see Trigger Properties,
  "context": (optional, object) personalization key-value pairs for this user when triggering a Canvas; see Canvas context object,
  "send_to_existing_only": (optional, boolean) defaults to true; cannot be used with user aliases; if set to `false`, an `attributes` object must also be included,
  "attributes": (optional, object) fields in the attributes object create or update an attribute of that name with the given value on the specified user profile before the message is sent and existing values are overwritten
}]
```

`send_to_existing_only` が `true` の場合、Brazeは既存のユーザーにのみメッセージを送信します。ただし、このフラグはユーザーエイリアスでは使用できません。

`send_to_existing_only` が `false` の場合、同じ受信者に `attributes` オブジェクトを含める必要があります。このフラグは `attributes` の代わりにはなりません。Brazeは `attributes` を使用して、送信前のプロファイル作成または更新を行います（例えば、メールやSMS配信のために `email` や電話番号フィールドを追加したり、サブスクリプショングループを更新したりします）。このオブジェクトがない場合、[`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns)や[`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases)で新規ユーザーに対する意図した組み合わせ動作は得られません。

そのプロファイルは、Brazeが送信する前に、メッセージのオーディエンスおよびチャネル適格性ルールを満たしている必要があります。

- [Braze ID]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle)
- [ユーザーエイリアス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle#user-aliases)
- [外部ユーザー ID]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields)
- [優先順位付け]({{site.baseurl}}/api/endpoints/user_data/post_user_identify#identifying-users-by-email)
- [ユーザー属性オブジェクト]({{site.baseurl}}/api/objects_filters/user_attributes_object#migrating-push-tokens)

## 受信者オブジェクトの重複排除 {#recipient-object-deduping}

受信者オブジェクトを使用してAPI呼び出しを行う際、**同一の宛先（つまりメールやプッシュ通知）をターゲットとする重複した受信者が存在する場合、Brazeはユーザーの重複を排除します**。つまり、Brazeは同一のユーザーを削除し、1つだけを残します。

例えば、同じ `external_user_id` を使用した場合、ユーザーはメッセージを1つだけ受信します。この動作を回避する必要がある場合は、複数のAPI呼び出しを行うことを検討してください。

同じ `external_user_id` が受信者配列内に複数回出現する場合、Brazeはメッセージを1つだけ送信し、配列内の最後のエントリのトリガープロパティを使用します。この動作は決定論的であり、配列の順序に基づいています。

次の例では、`userid1` は `"name": "Beth Test 2"` を使用したメッセージを1つ受信します。これは、そのエントリが配列内で最後に出現するためです。

```json
{"campaign_id":"#####","recipients":[
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 1"}},
{"external_user_id":"userid1","trigger_properties":{"name":"Beth Test 2"}}
]}
```
