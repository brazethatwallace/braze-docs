---
nav_title: Certona
article_title: Certona
alias: /partners/certona/
description: "この参考記事では、カスタマーライフサイクル全体にわたってパーソナライゼーションを提供するリアルタイムのオムニチャネルパーソナライゼーションソリューションである Braze と Certona のパートナーシップについて説明しています。Certona と Braze のコネクテッドコンテンツパートナーを組み合わせて使用することで、マルチチャネルキャンペーンにおすすめのコンテンツを簡単に挿入できます。"
page_type: partner
search_tag: Partner

---

# Certona

> [Certona](https://www.certona.com/)のプラットフォームは、カスタマーライフサイクル全体にわたるパーソナライゼーションを推進します。高度にパーソナライズされたメールキャンペーンから、機械学習による製品おすすめまで、Certonaはパーソナライゼーションの力を確実に活用できるようにします。

_この統合は Certona によって管理されています。_

## 統合について {#about-the-integration}

Braze と Certona の統合では、コネクテッドコンテンツを通じて Braze のキャンペーンやキャンバスで Certona の機械学習による製品おすすめを利用できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| --- | --- |
| [Certona アカウント](https://manage.certona.com/) | このパートナーシップを活用するには、Certona アカウントが必要です。 |
| [Certona REST API エンドポイント](https://manage.certona.com/) | このエンドポイントは、Braze のキャンペーンメッセージで直接使用され、ユーザー IDに基づいておすすめコンテンツを取得します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

Certona の REST APIを使用して、パーソナライズされたコンテンツをメッセージに挿入します。これを行うには、Certona REST API エンドポイントとともに、次のコネクテッドコンテンツテンプレートを Braze のメッセージ作成画面に追加します。

{% raw %}
```liquid
{% connected_content {CERTONA_REST_API_KEY} :save recommendations %}
```

次に、関連するテキストや画像など、呼び出したいコンテンツを定義します。たとえば `{{recommendations.CertonaObject.RecommendedItems[0].Items[0].name}}` です。

{% endraw %}

![メッセージ本文に Certona 関連のコネクテッドコンテンツが含まれたプッシュキャンペーンの画像。]({% image_buster /assets/img/certona.png %})

このメッセージをメッセージ作成画面に追加したら、コネクテッドコンテンツの呼び出しをプレビューして、正しい情報が表示されていることを確認します。

![送信前にメッセージを十分にテストするようユーザーに促す「Test」タブの画像。]({% image_buster /assets/img/certona2.png %})