---
nav_title: 認証とセキュリティ
article_title: メッセージングAPI認証とセキュリティ
page_order: 1
page_type: reference
description: "メッセージングAPIリクエストを安全に認証する方法について説明します。"
hidden: true
---

# メッセージングAPI認証とセキュリティ {#messaging-api-authentication-and-security}

{% alert important %}
このページはベータ版です。メッセージングAPIの機能とドキュメントは変更される可能性があります。
{% endalert %}

メッセージングAPIはクライアントサイドのREST APIキーを使用します。これらのキーは、サーバーサイドのBraze REST APIリクエストに使用されるプライベートREST APIキーとは異なります。

## クライアントサイドREST APIキー {#client-side-rest-api-keys}

クライアントサイドREST APIキーは1つのワークスペースにスコープされ、メッセージングAPIの権限に制限されています。これらのキーはクライアントアプリケーションに埋め込むことができます。

{% alert important %}
クライアントアプリケーションでは、クライアントサイドREST APIキーのみを使用してください。プライベートなサーバーサイドREST APIキーをクライアントサイドのコードに公開してはなりません。
{% endalert %}

クライアントサイドREST APIキーを作成するには：

1. Brazeダッシュボードで**設定** > **APIと識別子** > **APIキー**に移動します。
2. **APIキーを作成**を選択します。
3. **キータイプ**で**クライアント**を選択します。
4. バナーを取得するための`banners.sync`権限、バナーイベントをレポートするための`banners.track`権限、またはその両方を割り当てます。

## リクエストの認証 {#authenticating-requests}

クライアントサイドREST APIキーを`Authorization`ヘッダーにBearerトークンとして送信します：

```bash
Authorization: Bearer {YOUR_CLIENT_SIDE_REST_API_KEY}
```

HTTPSと、お使いのBrazeインスタンスの[RESTエンドポイント]({{site.baseurl}}/api/basics#endpoints)を使用してください。

## ユーザーの識別 {#user-identity}

クライアントサイドREST APIキーは、呼び出し元のアプリケーションとワークスペースを認証しますが、ユーザーは認証しません。リクエスト内の`external_user_id`は、バナーのコンテンツとイベントに関連付けられたユーザーを識別します。

メッセージングAPIリクエストを行う前に、アプリケーションの認可制御を適用してください。

## 認証エラー {#authentication-errors}

認証と権限の失敗はエンドポイントによって異なる場合があります。各エンドポイントのステータスコード表と[メッセージングAPIエラーハンドリング]({{site.baseurl}}/api/messaging_api/error_handling)を参照してください。