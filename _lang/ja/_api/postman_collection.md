---
nav_title: Postmanとサンプルリクエスト
article_title: Postmanとサンプルリクエスト
page_order: 3
description: "このリファレンス記事では、Braze Postmanコレクションについて、コレクションとは何か、コレクションのセットアップと使用方法、リクエストの編集と送信方法について説明します。"
page_type: reference

---

# Postmanとサンプルリクエスト {#postman-and-sample-requests}

> Brazeでは、Postmanコレクションを通じて、すべてのエンドポイントに対してサンプルAPIリクエストを生成できます。このリファレンス記事では、Braze Postmanコレクションについて、コレクションとは何か、コレクションのセットアップと使用方法、リクエストの編集と送信方法について説明します。

## Postmanとは {#what-is-postman}

Postmanは、APIリクエストの構築とテストのための無料のビジュアル編集ツールです。他の方法（たとえばcURLを使う方法）と比べて、PostmanではAPIリクエストを編集したり、ヘッダー情報を確認したりすることができます。コレクション（事前に作成されたAPIリクエストのサンプルライブラリ）を保存できます。REST APIのセットアップを高速化するために、すべてのエンドポイントについてあらかじめ作成されたサンプル集を提供しています。

[Postmanドキュメント](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro)の**Run in Postman**をクリックして、Postmanコレクションを表示またはダウンロードして始めましょう。

## Braze Postmanコレクションを使用する {#using-the-braze-postman-collection}

Postmanアカウント（MacOS版、Windows版、Linux版を[PostmanのWebサイト](https://www.getpostman.com)からダウンロードできます）をお持ちであれば、オレンジ色の**Run in Postman**ボタンをクリックすることで、ご自身のPostmanアプリでPostmanドキュメントを開くことができます。その後、[環境を作成](#setting-up-your-postman-environment)するか、Braze REST API環境をテンプレートとして使用し、利用可能な`POST`および`GET`リクエストをご自身のニーズに合わせて編集できます。

### Postman環境をセットアップする {#setting-up-your-postman-environment}

{% raw %}
Braze Postmanコレクションは、テンプレート変数`{{instance_url}}`を使用してBrazeインスタンスのREST API URLを事前に作成されたリクエストに置き換え、`{{api_key}}`変数をAPIキーに置き換えます。コレクション内のすべてのリクエストを手動で編集する代わりに、Postman環境でこの変数を設定できます。ドロップダウンからテンプレート環境（Braze REST API Environment Template）を選択して変数値をご自身のものに置き換えるか、独自の環境をセットアップすることもできます。
{% endraw %}

独自の環境をセットアップするには、以下の手順を実行します。

1. **Workspaces**タブで**Environments**を選択します。
2. **＋**プラスボタンをクリックして新しい環境を作成します。
3. この環境に名前を付け（たとえば「Braze API Requests」）、`instance_url`と`api_key`のキーを追加し、[Brazeインスタンス]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints)と[Braze REST APIキー]({{site.baseurl}}/api/api_key)に対応する値を指定します。
4. **Save**をクリックします。

{% alert note %}
`POST`リクエストの本文では、`api_key`は引用符で囲む必要があります: `"MY-API-KEY-EXAMPLE"`。`GET` URLでは引用符で囲まないでください。この書式は、このドキュメントの`POST`リクエストボディ、`GET` URL、および`YOUR-API-KEY-HERE`の環境テンプレートですでに提供されています。
{% endalert %}

![PostmanのBraze REST API環境にAPIキーとインスタンスURLの変数を追加する。]({% image_buster /assets/img_archive/postman_variable.png %})

### コレクションからビルド済みのリクエストを使用する {#using-the-pre-built-requests-from-the-collection}

環境を構成した後、コレクション内のビルド済みリクエストのいずれかを、新しいAPIリクエストを構築するためのテンプレートとして使用できます。ビルド済みリクエストの使用を開始するには、Postmanの**Collections**メニュー内でそのリクエストをクリックしてください。これにより、Postmanアプリのメインウィンドウで新しいタブとしてリクエストが開きます。

一般に、Braze APIエンドポイントが受け付けるリクエストには、`GET`と`POST`の2種類があります。エンドポイントが使用する`HTTP`メソッドに応じて、ビルド済みリクエストを異なる方法で編集する必要があります。

#### POSTリクエストを編集する {#edit-a-post-request}

`POST`リクエストを編集する場合、リクエストを開き、リクエストエディターの**Body**セクションに移動します。読みやすくするために、`JSON`リクエストボディをフォーマットする**raw**ラジオボタンを選択します。

![PostmanでPOST User Trackリクエストを編集する際のBodyタブ]({% image_buster /assets/img_archive/postman_post.png %})

#### GETリクエストを編集する {#edit-a-get-request}

`GET`リクエストを編集する場合は、リクエストURLで渡されるパラメーターを編集します。そのためには、**Params**タブを選択し、表示されるフィールドのキーと値のペアを編集します。

![PostmanでGET配信停止済みメールアドレスのクエリリスト取得リクエストを編集する際のParamsタブ。]({% image_buster /assets/img_archive/postman_get.png %})

### リクエストを送信する {#send-your-request}

APIリクエストの準備ができたら、**Send**をクリックします。リクエストが送信され、レスポンスデータがリクエストエディターの下のセクションに表示されます。ここから、Braze APIから返された生データの確認、HTTPレスポンスコードの確認、リクエストの処理にかかった時間の確認、ヘッダー情報の確認ができます。

![ステータスが201 Created、応答時間が269ミリ秒のPOSTリクエストからの本文レスポンスデータの例。]({% image_buster /assets/img_archive/postman_response.png %})