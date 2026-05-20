---
nav_title: LiftIgniter
article_title: LiftIgniter
alias: /partners/liftigniter/
description: "このリファレンス記事では、BrazeとLiftIgniterのパートナーシップについて説明します。LiftIgniterは、業界をリードするパーソナライゼーションプラットフォームであり、企業によるカスタマーエクスペリエンスの変革を支援しています。"
page_type: partner
search_tag: Partner

---

# Liftigniter

> [LiftIgniter](https://www.liftigniter.com/)は、あらゆるタッチポイントにおけるリアルタイムのパーソナライゼーションを通じて、企業のカスタマーエクスペリエンスの変革を支援する、業界をリードするパーソナライゼーションプラットフォームです。

_この統合はLiftigniterによって管理されています。_

## 統合について {#about-the-integration}

LiftIgniterとBrazeの統合はコネクテッドコンテンツを使用し、ニュース記事、衣料品、その他の小売商品や動画などの興味深いトピックをおすすめできるようにします。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| --- | --- |
| LiftIgniterアカウント | このパートナーシップを活用するには、[LiftIgniterアカウント](https://console.liftigniter.com/login)が必要です。 |
| LiftIgniter APIの統合 | おすすめを取得できるようにするには、LiftIgniterをサイトまたはアプリに[統合](https://support.liftigniter.com/support/solutions/articles/30000024667-api-integration-overview)する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## 統合 {#integration}

[LiftIgniterのREST API](https://documenter.getpostman.com/view/2166502/liftigniter/7TFGvSV#9bdf75da-edd6-45ec-9c28-a0edefad1389)を使用して、パーソナライズされたコンテンツをメッセージに挿入します。LiftIgniterアカウントを取得し、LiftIgniterがアプリに統合されたら、次のテンプレートをメッセージ作成画面に追加して、必要に応じて情報を置き換えて（`x-api-key`、`theapikey`など）、メッセージにコンテンツを呼び出します。

{% raw %}
```
{% connected_content https://query.petametrics.com/v3/lkdk9usg5av95fvs/userId/model :method post :headers {"x-api-key": "theapikey"} :body "UseActivity"=false :content_type application/json :save json %}
```

次に、メッセージを記述し、JSONで呼び出すコンテンツを定義します。たとえば`{{json.items[0].title}}`です。

{% endraw %}

![LiftIgniter固有のコネクテッドコンテンツ呼び出しを含むプッシュキャンペーンの画像。画像フィールドにはコネクテッドコンテンツロジックも追加されています。]({% image_buster /assets/img/liftigniter.png %})

このメッセージを作成画面の本文に入力すると、メッセージをプレビューできます。以下の例に示すように、画像を取り込むこともできます。

![送信後のメッセージの表示イメージを示すプレビュー画像。]({% image_buster /assets/img/liftigniter2.png %})