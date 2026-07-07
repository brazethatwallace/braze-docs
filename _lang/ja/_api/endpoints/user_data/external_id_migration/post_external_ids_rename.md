---
nav_title: "POST:外部IDの名前を変更する"
article_title: "POST:外部IDの名前を変更する"
search_tag: Endpoint
page_order: 1
layout: api_page
page_type: reference
description: "この記事では、「外部IDの名前を変更」エンドポイントの詳細について説明します。"

---
{% api %}
# 外部IDの名前を変更する {#rename-external-id}
{% apimethod post %}
/users/external_ids/rename
{% endapimethod %}

> このエンドポイントを使用して、ユーザーのexternal IDの名前を変更します。

1回のリクエストで最大50個の名前変更オブジェクトを送信できます。

このエンドポイントは、ユーザーに新しい（プライマリ）`external_id`を設定し、既存の`external_id`を非推奨にします。つまり、非推奨のIDが削除されるまで、どちらの`external_id`でもユーザーを識別できるということです。複数のexternal IDを持つことで、以前のexternal ID命名スキーマを使用しているレガシーバージョンのアプリが壊れないように、移行期間を設けることができます。

古い命名スキーマが使用されなくなった後は、[`/users/external_ids/remove`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove)を使用して非推奨のexternal IDを削除することを強く推奨します。

{% alert warning %}
非推奨のexternal IDは、`/users/delete`ではなく`/users/external_ids/remove`エンドポイントを使用して削除してください。非推奨のexternal IDを使用して`/users/delete`にリクエストを送信すると、ユーザープロファイルは完全に削除され、元に戻すことはできません。
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#17682d2b-1546-4a3c-9703-aa5a12861d7c {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`users.external_ids.rename`権限を持つ[APIキー]({{site.baseurl}}/api/api_key)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='external id migration' %}

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "external_id_renames" : (required, array of external ID rename objects)
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
| --------- | ---------| --------- | ----------- |
| `external_id_renames` | 必須 | 外部識別子リネームオブジェクトの配列 | 外部識別子の名前変更オブジェクトの構造については、リクエスト例と以下の制限事項を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 aria-label="リクエストパラメーター" }

以下の点に注意してください。

- `current_external_id`はユーザーのプライマリIDである必要があり、非推奨IDにすることはできません。
- `new_external_id`は、プライマリIDまたは非推奨IDとしてすでに使用されているものであってはなりません。
- `current_external_id`と`new_external_id`を同じにすることはできません。

## リクエスト例 {#request-example}
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/external_ids/rename' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "external_id_renames" :[
    {
      "current_external_id": "existing_external_id",
      "new_external_id" : "new_external_id"
    }
  ]
}'
```

## 応答 {#response}

この応答は、成功したすべての名前変更と、関連するエラーを伴う失敗した名前変更を確認します。`rename_errors`フィールドのエラーメッセージは、元のリクエストの配列内のオブジェクトのインデックスを参照します。

```
{
  "message" : (string) status message,
  "external_ids" : (array of strings) successful rename operations,
  "rename_errors": (array of arrays) <minor error message>
}
```

`message`フィールドは、有効なリクエストに対しては`success`を返します。より具体的なエラーは`rename_errors`配列に格納されます。`message`フィールドは、以下の場合にエラーを返します。

- 無効なAPIキー
- 空の`external_id_renames`配列
- 50を超えるオブジェクトを持つ`external_id_renames`配列
- レート制限に到達（1分あたり1,000件以上のリクエスト）

## よくある質問 {#frequently-asked-questions}

### MAUに影響しますか？ {#does-this-impact-mau}
いいえ。ユーザー数は変わらず、新しい`external_id`が設定されるだけです。

### ユーザーの行動履歴は変わりますか？ {#does-user-behavior-change-historically}
いいえ。ユーザー自体は同じであり、すべての行動履歴は引き続きそのユーザーに紐づいています。

### 開発ワークスペースまたはステージングワークスペースで実行できますか？ {#can-it-be-run-on-development-or-staging-workspaces}
はい。実際、ステージングまたは開発ワークスペースでテスト移行を実行し、本番データで実行する前にすべてがスムーズに進んでいることを確認することを強く推奨します。

### データポイントは記録されますか？ {#does-this-log-data-points}
この機能はデータポイントを記録しません。

### 推奨される非推奨期間はどのくらいですか？ {#what-is-the-recommended-deprecation-period}
非推奨のexternal IDをいつまで保持できるかについて厳密な制限はありませんが、非推奨のIDでユーザーを参照する必要がなくなったら、削除することを強く推奨します。

{% endapi %}