---
nav_title: Postmanとサンプルリクエスト
article_title: Postmanとサンプルリクエスト
page_order: 3
description: "このリファレンス記事では、Braze Postmanコレクションについて、コレクションとは何か、コレクションの設定と使用方法、リクエストの編集と送信方法について説明します。"
page_type: reference
---

# Postmanとサンプルリクエスト {#postman-and-sample-requests}

> Brazeでは、Postmanコレクションを通じて、すべてのエンドポイントに対してサンプルAPIリクエストを生成できます。このリファレンス記事では、Braze Postmanコレクションについて、コレクションとは何か、コレクションの設定と使用方法、リクエストの編集と送信方法について説明します。

## Postmanとは {#what-is-postman}

Postmanは、APIリクエストの作成とテストのための無料のビジュアル編集ツールです。他の方法（たとえばcURLの使用）と比較して、PostmanではAPIリクエストの編集、ヘッダー情報の表示などが可能です。コレクション（あらかじめ作成されたサンプルAPIリクエストのライブラリ）を保存できます。REST APIのセットアップを迅速に行うために、すべてのエンドポイント用にあらかじめ作成された例を含むコレクションを提供しています。

[Postmanドキュメント](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro)の**Run in Postman**をクリックして、Postmanコレクションの表示またはダウンロードを行い、使用を開始しましょう。

## Braze Postman コレクションの使用 {#using-the-braze-postman-collection}

Postman アカウントをお持ちの場合（macOS、Windows、Linux版は [Postman Web サイト](https://www.getpostman.com)からダウンロードできます）、オレンジ色の **Run in Postman** ボタンをクリックして、Braze の Postman ドキュメントをご自身の Postman アプリで開くことができます。その後、[環境を作成](#setting-up-your-postman-environment)するか、Braze REST API 環境をテンプレートとして使用し、利用可能な `POST` および `GET` リクエストをニーズに合わせて編集できます。

### Postman 環境の設定 {#setting-up-your-postman-environment}

{% raw %}
Braze Postman コレクションでは、テンプレート変数 `{{instance_url}}` を使用して、Braze インスタンスの REST API URL をビルド済みのリクエストに代入し、`{{api_key}}` 変数で APIキーを設定します。コレクション内のすべてのリクエストを手動で編集する代わりに、Postman 環境でこの変数を設定できます。ドロップダウンからテンプレート環境（Braze REST API Environment Template）を選択して変数値をご自身のものに置き換えるか、独自の環境を設定できます。
{% endraw %}

独自の環境を設定するには、以下のステップを実行してください。

1. **Workspaces** タブから **Environments** を選択します。
2. **+** プラスボタンをクリックして新しい環境を作成します。
3. この環境に名前を付け（例：「Braze API Requests」）、`instance_url` と `api_key` のキーを追加し、[Braze インスタンス]({{site.baseurl}}/api/basics)と [Braze REST APIキー]({{site.baseurl}}/api/basics)に対応する値を設定します。
4. **Save** をクリックします。

{% alert note %}
`POST` リクエストボディでは、`api_key` は引用符で囲む必要があります：`"MY-API-KEY-EXAMPLE"`。`GET` URL では引用符は不要です。このドキュメントの `POST` リクエストボディ、`GET` URL、および環境テンプレートでは、`YOUR-API-KEY-HERE` として既にこのフォーマットが提供されています。
{% endalert %}

![Postman の Braze REST API 環境にAPIキーとインスタンス URL の変数を追加する画面。]({% image_buster /assets/img_archive/postman_variable.png %})

### コレクションのビルド済みリクエストの使用 {#using-the-pre-built-requests-from-the-collection}

環境を設定した後、コレクション内の任意のビルド済みリクエストをテンプレートとして使用し、新しい API リクエストを作成できます。ビルド済みリクエストの使用を開始するには、Postman の **Collections** メニュー内でそのリクエストをクリックします。リクエストが Postman アプリのメインウィンドウに新しいタブとして開きます。

一般的に、Braze APIエンドポイントが受け付けるリクエストには `GET` と `POST` の2種類があります。エンドポイントが使用する `HTTP` メソッドに応じて、ビルド済みリクエストの編集方法が異なります。

#### POST リクエストの編集 {#edit-a-post-request}

`POST` リクエストを編集する場合、リクエストを開いてリクエストエディターの **Body** セクションに移動します。読みやすくするために、**raw** ラジオボタンを選択して `JSON` リクエストボディをフォーマットします。

![Postman で POST User Track リクエストを編集する際の Body タブ]({% image_buster /assets/img_archive/postman_post.png %})

#### GET リクエストの編集 {#edit-a-get-request}

`GET` リクエストを編集する場合、リクエスト URL で渡されるパラメーターを編集します。**Params** タブを選択し、表示されるフィールドでキーと値のペアを編集します。

![Postman で GET 購読解除メールアドレスリストのクエリリクエストを編集する際の Params タブ。]({% image_buster /assets/img_archive/postman_get.png %})

### リクエストの送信 {#send-your-request}

API リクエストの準備ができたら、**Send** をクリックします。リクエストが送信され、レスポンスデータがリクエストエディターの下のセクションに表示されます。ここから、Braze APIから返された生データの表示、HTTP レスポンスコードの確認、リクエストの処理にかかった時間の確認、ヘッダー情報の表示ができます。

![ステータス 201 Created、レスポンスタイム 269 ミリ秒の POST リクエストからのボディレスポンスデータの例。]({% image_buster /assets/img_archive/postman_response.png %})