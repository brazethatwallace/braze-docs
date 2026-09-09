---
nav_title: 5月
page_order: 8
noindex: true
page_type: update
description: "この記事には2020年5月のリリースノートが含まれています。"
---
# 2020年5月 {#may-2020}

## Google Tag マネージャー

[Google Tag マネージャー]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)を使用したBrazeのAndroid SDKのデプロイと管理方法に関するドキュメントと例を追加しました。

## 新しいブラックリストメールAPIエンドポイント {#new-blacklist-email-api-endpoint}

Braze API経由でメールアドレスを[ブラックリスト化]({{site.baseurl}}/api/endpoints/email/post_blacklist)できるようになりました。メールアドレスをブラックリストに登録すると、そのユーザーはメールの購読解除となり、ハードバウンスとしてマークされます。

## Braze APIエンドポイントのAPIキー変更 {#api-key-change-for-braze-api-endpoints}

2020年5月より、BrazeはAPIキーの読み取り方法をより安全なものに変更しました。APIキーはリクエストヘッダーとして渡す必要があります。例は、各エンドポイントページの**リクエスト例**セクション、および**APIキーの説明**で確認できます。

Brazeは、リクエストボディおよびURLパラメータで渡される`api_key`を引き続きサポートしますが、最終的には廃止される予定です（時期未定）。**APIコールを適宜更新してください。**これらの変更は[Postman](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro)内で更新されています。
{% details APIキーの説明 %}
{% tabs %}
{% tab GET Request %}
この例では、`/email/hard_bounces`エンドポイントを使用しています。

**変更前：リクエストボディのAPIキー**
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?api_key={YOUR_REST_API_KEY}&start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@example.com' \
```
**変更後：ヘッダーのAPIキー**
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@example.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endtab %}
{% tab POST Request %}
この例では、`/user/track`エンドポイントを使用しています。

**変更前：リクエストボディのAPIキー**
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--data-raw '{
	"api_key": YOUR-API-KEY-HERE ,
	"attributes": [
 	{
 	  "external_id":"user_id",
      "string_attribute": "sherman",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": ["banana", "apple"]
    }
    ]
}'
```
**変更後：ヘッダーのAPIキー**
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
	"attributes": [
 	{
	  "external_id":"user_id",
      "string_attribute": "sherman",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": ["banana", "apple"]
    }
    ]
}'
```
{% endtab %}
{% endtabs %}
{% enddetails %}