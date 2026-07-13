---
nav_title: REST API
article_title: REST API
page_order: 1
description: "コネクテッドコンテンツを使用してREST APIからメッセージにデータを取得し、リアルタイムのパーソナライゼーションを行う方法を説明します。"
---

# REST API {#rest-api}

> [コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)を使用して、送信時に外部REST APIからメッセージに直接データを取得できます。これにより、自社サーバー、サードパーティサービス、または公開されている任意のAPIエンドポイントからのリアルタイム情報でメッセージをパーソナライズできます。

## 仕組み {#how-it-works}

{% raw %}
コネクテッドコンテンツは、指定したURLにHTTPリクエストを送信し、レスポンスを保存してLiquidで参照できるようにします。メッセージに `{% connected_content %}` タグを追加すると、メッセージ送信時にBrazeがエンドポイントを呼び出します。

```liquid
{% connected_content https://api.example.com/user/{{${user_id}}}/recommendations :save recs %}
We think you'll love {{recs.top_pick}}!
```
{% endraw %}

コネクテッドコンテンツはGETリクエストとPOSTリクエストをサポートしています。Brazeはサーバーが2秒以内に応答することを要求するため、エンドポイントは低レイテンシーになるよう設計してください。

## 一般的なユースケース {#common-use-cases}

| ユースケース | 説明 |
| --- | --- |
| 製品のおすすめ | レコメンデーションエンジンからパーソナライズ済みの製品おすすめを取得する |
| リアルタイムの価格・在庫情報 | 送信時の最新の価格や在庫レベルを表示する |
| 天気に基づくコンテンツ | 地域の天気データを取得してメッセージングをカスタマイズする |
| ロイヤルティポイント残高 | 最新の報酬やアカウント残高を表示する |
| コンテンツフィード | 最新のブログ記事、記事、またはニュースを挿入する |
{: .reset-td-br-1 .reset-td-br-2 aria-label="一般的なユースケース" }

## 認証 {#authentication}

Brazeはコネクテッドコンテンツリクエストに対して、ベーシック認証、トークン認証、OAuthをサポートしています。認証情報はBrazeダッシュボードの**設定** > **コネクテッドコンテンツ**に安全に保存し、API呼び出しで参照できます。

詳細については、[コネクテッドコンテンツAPI呼び出しの作成]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#authentication-types)を参照してください。

## エラー処理 {#error-handling}

エンドポイントがエラーを返すかタイムアウトした場合、Brazeはコネクテッドコンテンツのレスポンスの代わりに空の文字列をレンダリングします。保存された変数がnullかどうかを確認することで失敗を検出し、条件に応じてメッセージを中止したりフォールバックコンテンツを表示したりできます。

詳細については、[コネクテッドコンテンツの中止]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content)を参照してください。

## パフォーマンスに関する考慮事項 {#performance-considerations}

Brazeは大量のメッセージを配信するため、サーバーは数千の同時接続を処理できる必要があります。適切な場所でキャッシュを使用し、外部エンドポイントの過負荷を避けるためにメッセージにレート制限を設定してください。

コネクテッドコンテンツの完全なリファレンスについては、[コネクテッドコンテンツ]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)を参照してください。