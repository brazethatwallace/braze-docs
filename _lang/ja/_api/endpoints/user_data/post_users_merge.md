---
nav_title: "POST:ユーザーをマージする"
article_title: "POST:ユーザーをマージする"
search_tag: Endpoint
page_order: 6
layout: api_page
page_type: reference
description: "この記事では、「ユーザーのマージ」Brazeエンドポイントの詳細について説明します。"

---
{% api %}
# ユーザーをマージする {#merge-users}
{% apimethod post %}
/users/merge
{% endapimethod %}

> このエンドポイントを使用して、あるユーザーを別のユーザーにマージします。

リクエストごとに最大50件のマージを指定できます。このエンドポイントは非同期です。

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#d262b86d-cf84-46e2-b9d0-f882bb7078de {% endapiref %}

## 前提条件 {#prerequisites}

このエンドポイントを使用するには、`users.merge` 権限を持つ[APIキー]({{site.baseurl}}/api/api_key/)が必要です。

## レート制限 {#rate-limit}

{% multi_lang_include rate_limits.md endpoint='users merge' %}

## リクエスト本文 {#request-body}

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "merge_updates" : (required, array of objects)
}
```

## リクエストパラメーター {#request-parameters}

| パラメーター | 必須 | データタイプ | 説明 |
|---|---|---|---|
| `merge_updates` | 必須 | 配列 | オブジェクトの配列。各オブジェクトには `identifier_to_merge` オブジェクトと `identifier_to_keep` オブジェクトが含まれている必要があり、それぞれが `external_id`、`user_alias`、`phone`、または `email` のいずれかでユーザーを参照する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="リクエストパラメーター" }

### マージ動作 {#merge-behavior}

以下に説明する動作は、Snowflakeを利用して**いない**すべてのBraze機能に当てはまります。ユーザーのマージは、**メッセージング履歴**タブ、セグメントエクステンション、クエリビルダー、およびCurrentsには反映されません。

{% alert important %}
エンドポイントは、`merge_updates` オブジェクトが更新される順序を保証しません。
{% endalert %}

このエンドポイントは、ターゲットユーザーに以下のフィールドが存在しない場合、それらをマージします。

- 名
- 姓
- メールアドレス（[暗号化]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption/)されていない場合）
- 性別
- 生年月日
- 電話番号
- タイムゾーン
- 市区町村
- 国
- 言語
- デバイス情報
- セッション数（両方のプロファイルのセッションの合計）
- 初回セッションの日付（Brazeは2つの日付のうち早い方を選択します）
- 最終セッションの日付（Brazeは2つの日付のうち遅い方を選択します）
- カスタム属性（Brazeはターゲットプロファイル上の既存のカスタム属性を保持し、ターゲットプロファイルに存在しなかったカスタム属性も追加します）
- カスタムイベントと購入イベントのデータ
- 「Y日間でX回」セグメンテーション用のカスタムイベントおよび購入イベントのプロパティ（X<=50 かつ Y<=30）
- セグメント可能なカスタムイベントのサマリー
  - イベント数（両プロファイルの合計）
  - イベントが最初に発生した日時（Brazeは2つの日付のうち早い方を選択します）
  - イベントが最後に発生した日時（Brazeは2つの日付のうち遅い方を選択します）
- アプリ内購入の合計（セント単位）（両方のプロファイルの合計）
- 購入総数（両方のプロファイルの合計）
- 初回購入日（Brazeは2つの日付のうち早い方を選択します）
- 最終購入日（Brazeは2つの日付のうち遅い方を選択します）
- アプリの概要
- Last_X_atフィールド（孤立したプロファイルのフィールドがより新しい場合、Brazeはフィールドを更新します）
- Campaignのインタラクションデータ（Brazeは最も新しい日付フィールドを選択します）
- ワークフローの概要（Brazeは最も新しい日付フィールドを選択します）
- メッセージとメッセージのエンゲージメント履歴
- Brazeは、アプリが両方のユーザープロファイルに存在する場合にのみセッションデータをマージします。

{% alert note %}
ユーザーをマージする場合、`/users/merge` エンドポイントの使用は、[`changeUser()` メソッド](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)の使用と同じように機能します。
{% endalert %}

Brazeは、マージ時に3つのユーザータイプを異なる方法で処理します。削除対象としてマークされたユーザー、テストユーザー、およびグローバルコントロールグループのユーザーです。詳細については、[ユーザーマージの動作]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users/merge_behavior/)を参照してください。

#### カスタムイベント日と購入イベント日の動作 {#custom-event-date-and-purchase-event-date-behavior}

これらのマージされたフィールドは「Y日間でX件のイベント」フィルターを更新します。購入イベントの場合、これらのフィルターには「Y日間の購入回数」と「過去Y日間の使用金額」が含まれます。

### メールまたは電話番号でユーザーをマージする {#merging-users-by-email-or-phone-number}

識別子として `email` または `phone` が指定された場合、識別子に追加の `prioritization` 値を含める必要があります。`prioritization` は、複数のユーザーが見つかった場合にどのユーザーをマージするかを指定する順序付き配列である必要があります。つまり、優先順位付けから複数のユーザーが一致した場合、マージは行われません。

配列に指定できる値は次のとおりです。

- `identified`
- `unidentified`
- `most_recently_updated`（最も最近更新されたユーザーを優先することを意味します）
- `least_recently_updated`（最も更新が古いユーザーを優先することを意味します）

優先順位配列には、一度に以下のオプションのうち1つしか存在できません。

- `identified` は `external_id` を持つユーザーを優先することを意味します
- `unidentified` は `external_id` を持たないユーザーを優先することを意味します

{% alert important %}
両方のプロファイルに無効な電話番号がある場合、Brazeはそれらをマージしません。無効な番号はE.164形式で保存されておらず、マージジョブはそれらのプロファイルを結合しません。エンドポイントは成功メッセージとともに `202 Accepted` を返すため、HTTP応答ではマージがスキップされたことは示されません。マージする前に、一方または両方のプロファイルの電話番号を修正してください。
{% endalert %}

## リクエスト例 {#example-requests}

### 基本リクエスト {#basic-request}

これはリクエストのパターンを示す基本的なリクエスト本文です。

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "external_id": "old-user1"
      },
      "identifier_to_keep": {
        "external_id": "current-user1"
      }
    },
    {
      "identifier_to_merge": {
        "email": "user1@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep":  {
        "email": "user2@braze.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    },
    {
      "identifier_to_merge": {
        "user_alias": {
          "alias_name": "old-user2@example.com",
          "alias_label": "email"
        }
      },
      "identifier_to_keep": {
        "user_alias": {
          "alias_name": "current-user2@example.com",
          "alias_label": "email"
        }
      }
    }
  ]
}'
```

### 未識別ユーザーをマージする {#merging-unidentified-user}

以下のリクエストは、メールアドレス `john.smith@braze.com` を持つ最も最近更新された未識別ユーザーを、external ID `john` を持つユーザーにマージします。この例では、`most_recently_updated` を使用することでクエリを未識別ユーザー1件に絞り込みます。つまり、このメールアドレスを持つ未識別ユーザーが2人いた場合、external ID `john` を持つユーザーにマージされるのは1人だけです。

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'
```

### 未識別ユーザーを識別済みユーザーにマージする {#merging-unidentified-user-into-identified-user}

次の例では、メールアドレス `john.smith@braze.com` を持つ最も最近更新された未識別ユーザーを、メールアドレス `john.smith@braze.com` を持つ最も最近更新された識別済みユーザーにマージします。

`most_recently_updated` を使用して、クエリを1人のユーザーに絞り込みます（`identifier_to_merge` では未識別ユーザー1人、`identifier_to_keep` では識別済みユーザー1人）。

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified", "most_recently_updated"]
      },
      "identifier_to_keep": {
        "email": "john.smith@braze.com",
        "prioritization": ["identified", "most_recently_updated"]
      }
    }
  ]
}'
```

### most_recently_updatedの優先順位付けを含めずに未識別ユーザーをマージする {#merging-an-unidentified-user-without-including-the-most_recently_updated-prioritization}

メールアドレス `john.smith@braze.com` を持つ未識別ユーザーが2人いる場合、このリクエスト例ではユーザーはマージされません。そのメールアドレスを持つ未識別ユーザーが2人存在するためです。このリクエストは、メールアドレス `john.smith@braze.com` を持つ未識別ユーザーが1人だけの場合にのみ機能します。

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/merge' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "merge_updates": [
    {
      "identifier_to_merge": {
        "email": "john.smith@braze.com",
        "prioritization": ["unidentified"]
      },
      "identifier_to_keep": {
        "external_id": "john"
      }
    }
  ]
}'
```

## 応答 {#response}

このエンドポイントには `202` と `400` の2つのステータスコード応答があります。

### 成功応答の例 {#example-success-response}

ステータスコード `202` は、次の応答本文を返す可能性があります。

```json
{
  "message": "success"
}
```

### エラー応答の例 {#example-error-response}

ステータスコード `400` は、次の応答本文を返す可能性があります。発生する可能性のあるエラーの詳細については、「[トラブルシューティング](#troubleshooting)」を参照してください。

```json
{
  "message": "'merge_updates' must be an array of objects"
}
```

## トラブルシューティング {#troubleshooting}

### 成功応答が返されたがマージされたユーザーがまだ検索可能である {#a-success-response-was-returned-but-the-merged-user-is-still-searchable}

成功応答はリクエストが受け付けられたことを確認するものですが、マージ操作にはプロファイルのマージとソースプロファイルの削除という2つのステップが含まれます。このため、成功応答の後しばらくの間、`identifier_to_merge` プロファイルがダッシュボードで検索可能な状態のままになることがあります。これは想定される動作です。数分待ってからマージが完了したことを確認してください。

マージされたユーザーが数分経っても存在する場合は、リクエスト内の識別子が正しく、リクエストに使用したAPIキーと同じワークスペースのユーザーに属していることを確認してください。

### エラーリファレンス {#error-reference}

以下の表は、発生する可能性のあるエラーメッセージの一覧です。

| エラー | トラブルシューティング |
| --- | --- |
| `'merge_updates' must be an array of objects` | `merge_updates` がオブジェクトの配列であることを確認してください。 |
| `a single request may not contain more than 50 merge updates` | 1回のリクエストで指定できるマージ更新は50件までです。 |
| `identifiers must be objects with an 'external_id' property that is a string, 'user_alias' property that is an object, 'email' property that is a string, or 'phone' property that is a string` | リクエストの識別子を確認してください。 |
| `'merge_updates' must only have 'identifier_to_merge' and 'identifier_to_keep'` | `merge_updates` に `identifier_to_merge` と `identifier_to_keep` の2つのオブジェクトのみが含まれていることを確認してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="トラブルシューティング" }

{% endapi %}