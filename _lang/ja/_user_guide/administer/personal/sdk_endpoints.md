---
nav_title: APIおよびSDKエンドポイント
article_title: APIおよびSDKエンドポイント
page_order: 5
page_type: reference
description: "Brazeインスタンスに対応する正しいダッシュボードURL、REST APIエンドポイント、SDK エンドポイントを確認できます。"

---

# APIおよびSDKエンドポイント {#api-and-sdk-endpoints}

> Brazeインスタンスに対応する正しいダッシュボードURL、REST APIエンドポイント、SDK エンドポイントを確認できます。ログイン、API呼び出し、SDKの統合にこれらのURLが必要です。

Brazeでは、ダッシュボード、SDK、RESTエンドポイント用に複数のインスタンスを管理しており、これらを「クラスター」と呼んでいます。Brazeのオンボーディングマネージャーが、お客様がどのクラスターに属しているかをお知らせします。Braze SDKの詳細については、[Braze 101](https://learning.braze.com/braze-101) Brazeラーニングコースをご覧ください。

[dashboard.braze.com](https://dashboard.braze.com)にログインすると、自動的に正しいクラスターアドレスに移動します。

{% multi_lang_include administer/data_centers.md datacenters='instances' %}

{% alert important %}
SDKを統合する際は、SDK エンドポイントを使用してください。REST APIを呼び出す際は、RESTエンドポイントを使用してください。
{% endalert %}

APIへのアクセスの詳細については、[APIの概要に関する記事]({{site.baseurl}}/api/basics/)をご覧ください。