---
nav_title: テスト
article_title: iOS のプッシュ通知テスト
platform: iOS
page_order: 29
description: "この参照記事では、iOSプッシュ通知のコマンドラインプッシュテストについて説明します。"
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# テスト {#push-testing}

コマンドラインからアプリ内通知とプッシュ通知をテストする場合は、CURLと[メッセージングAPI]({{site.baseurl}}/api/endpoints/messaging)を介してターミナルから単一の通知を送信できます。次のフィールドをテストケースの正しい値に置き換える必要があります。

必須フィールド:

- `YOUR-API-KEY-HERE` - **設定** > **APIキー**で利用できます。このキーが`/messages/send` REST APIエンドポイントを介したメッセージ送信を許可されていることを確認してください。
- `EXTERNAL_USER_ID` - **ユーザーを検索**ページで確認できます。
- `REST_API_ENDPOINT_URL` - Brazeの[インスタンス]({{site.baseurl}}/api/basics#endpoints. Ensure using the endpoint corresponds to the Braze instance your workspace is on.

Optional fields:
- `YOUR_KEY1` (optional)に記載されています。使用するエンドポイントがワークスペースのBrazeインスタンスに対応していることを確認してください。

オプションフィールド:
- `YOUR_KEY1`（オプション）
- `YOUR_VALUE1`（オプション）

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer YOUR-API-KEY-HERE" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://{REST_API_ENDPOINT_URL}/messages/send
```
