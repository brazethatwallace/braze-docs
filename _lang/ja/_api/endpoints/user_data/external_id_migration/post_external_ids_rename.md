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

このエンドポイントは、ユーザーに新しい（プライマリ）`external_id`を設定し、既存の`external_id`を非推奨にします。つまり、非推奨のIDが削除されるまで、どちらの`external_id`でもユーザーを識別できるということです。複数のexternal IDを持つことで、以前のexternal ID命名スキーマを使用しているレガシーバージョンのアプリが壊れないように、移行期間を設けることができます。移行期間中、プロファイルはどちらの識別子でも完全に機能します。Braze SDK、REST API、メッセージングパイプラインは、非推奨のIDが明示的に削除されるまで、どちらのIDでもユーザーを参照し続けることができます。

古い命名スキーマが使用されなくなった後は、[`/users/external_ids/remove`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove)を使用して非推奨のexternal IDを削除することを強く推奨します。

{% alert warning %}
非推奨のexternal IDは、`/users/delete`ではなく`/users/external_ids/remove`エンドポイントを使用して削除してください。非推奨のexternal IDを使用して`/users/delete`にリクエストを送信すると、ユーザープロファイルは完全に削除され、元に戻すことはできません。
{% endalert %}

## 名前変更の仕組み {#how-renaming-works}

このエンドポイントを呼び出すと、ユーザープロファイルに新しいプライマリ`external_id`を割り当てると同時に、以前のプライマリ`external_id`を非推奨のexternal IDに変換します。名前変更が成功すると、ユーザープロファイルにはプライマリ`external_id`（新しい値）が1つと、非推奨のexternal ID（古い値）が1つ保持されます。

同じプロファイルに対する後続の名前変更呼び出しも許可されています。名前変更のたびに非推奨のexternal IDが追加されるため、プロファイルには1つのプライマリ`external_id`と複数の非推奨のexternal IDが蓄積される場合があります。ただし、`new_external_id`の値は、プライマリまたは非推奨のexternal IDとして、どのBrazeプロファイルにもすでに存在していてはなりません。

このエンドポイントはデータポイントを記録せず、MAUカウントにも影響しません。すべての履歴ユーザーデータ（イベント、購入、属性、キャンペーンエンゲージメント）は同じプロファイルに紐づいたままです。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#17682d2b-1546-4a3c-9703-aa5a12861d7c {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`users.external_ids.rename`権限を持つ[APIキー]({{site.baseurl}}/api/basics)が必要です。

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

- `current_external_id`はユーザーのプライマリIDである必要があり、非推奨IDにすることはできません。`current_external_id`として渡された値がプロファイル上の非推奨IDである場合、呼び出しは失敗します。失敗した名前変更を再試行する前に、[`/users/export/ids`エンドポイント]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)を使用して、現在どのIDがプライマリであるかを確認してください。
- `new_external_id`は、プライマリIDまたは非推奨IDとしてすでに使用されているものであってはなりません。すでに非推奨IDとして保存されているIDに名前を変更しようとすると、「new_external_id is already in use」エラーが返されます。
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

## レスポンス {#response}

レスポンスは、成功したすべての名前変更と、関連するエラーを伴う失敗した名前変更を確認します。`rename_errors`フィールドのエラーメッセージは、元のリクエストの配列内のオブジェクトのインデックスを参照します。

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

## 一括移行 {#bulk-migrations}

大規模なユーザー集団を含む移行の場合、ユーザーを最大50件のグループにバッチ処理し、各バッチを個別のAPI呼び出しとして送信します。このエンドポイントには1分あたり1,000リクエストのレート制限が適用されます。最大バッチサイズ（1リクエストあたり50オブジェクト）の場合、1分あたり最大50,000件のユーザー名前変更が可能です。

バッチ内の各名前変更オブジェクトは独立して処理されます。1つのオブジェクトの失敗が、同じリクエスト内の他のオブジェクトをブロックすることはありません。レスポンスボディでは、成功した名前変更（`external_ids`配列に記載）と失敗した名前変更（`rename_errors`配列にリクエスト配列内の失敗オブジェクトの位置を示すインデックス参照とともに記載）が区別されます。

一括移行を実行する場合：

1. ユーザー全体を最大50ペアのバッチで反復処理します。
2. 各レスポンスで、`external_ids`（成功）と`rename_errors`（失敗）の両方を確認し、再試行が必要なユーザーを特定します。
3. 失敗したオブジェクトを収集し、再試行バッチを別途スケジュールします。一般的な失敗原因には、`new_external_id`がすでに使用されている場合や、`current_external_id`がプライマリIDではなく非推奨IDである場合があります。
4. 成功と失敗を自分のレコードに記録し、移行状態をBrazeの外部で追跡できるようにします。

## 現在のexternal IDの確認 {#verifying-the-current-external-id}

移行中に、特定のプロファイルでどのexternal IDがアクティブなプライマリ識別子であるかを確認する必要がある場合があります。たとえば、特定のユーザーがすでに移行済みかどうかを判断する場合や、失敗した名前変更のトラブルシューティングを行う場合です。この目的には[`/users/export/ids`エンドポイント]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)を使用してください。

エクスポートエンドポイントは、プライマリと非推奨の両方のexternal IDを同じ基盤プロファイルに解決し、レスポンスには常に現在のプライマリ`external_id`を返します。つまり、ユーザーの既知の識別子（古いものでも新しいものでも）でクエリでき、レスポンスには正規のプライマリIDが含まれます。これは移行状態を判断する信頼性の高い方法です。

external IDのみを確認する場合（完全なプロファイルを取得するのではなく）、`fields_to_export`に`external_id`フィールドのみを渡してください。

## 推奨される移行ワークフロー {#recommended-migration-workflow}

ほとんどの移行ユースケースでは、以下の手順が推奨されます。

1. **ステージングでテストする** — 本番環境に触れる前に、開発またはステージングワークスペースで名前変更と確認のフロー全体を実行します。
2. **バッチで名前を変更する** — `/users/external_ids/rename`エンドポイントを最大50件のバッチで使用し、各レスポンスで`rename_errors`を処理して、失敗したペアを再試行キューに入れます。
3. **確認する** — 各バッチの後（または移行の最後に）、`/users/export/ids`を使用してプロファイルをスポットチェックし、期待されるプライマリ`external_id`が設定されていることを確認します。
4. **非推奨期間を維持する** — いずれかのシステム（フィールドのレガシーアプリバージョンを含む）が古いIDを参照する可能性がある限り、非推奨のexternal IDをアクティブに保ちます。このステップを急がないでください。
5. **非推奨IDを削除する** — すべてのシステムが新しいIDを使用していることが確認されたら、[`/users/external_ids/remove`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/post_external_ids_remove)を最大50件のバッチで使用してクリーンアップします。

SDKインテグレーションも移行する場合（たとえば、`changeUser`に渡す値を変更する場合）、非推奨IDが削除される前に、サーバーとクライアントの両方で新しいexternal IDが使用されるように、API側の名前変更とアプリのリリーススケジュールを調整してください。

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

### プロファイルが保持できる非推奨のexternal IDの数はいくつですか？ {#how-many-deprecated-external-ids-can-a-profile-have}
ユーザープロファイルは、1つのプライマリ`external_id`と、連続した名前変更操作によって蓄積された任意の数の非推奨のexternal IDを保持できます。1つのプロファイルが保持できる非推奨IDの数に文書化された上限はありませんが、Brazeでは不要になったら速やかに削除することを推奨しています。

{% endapi %}