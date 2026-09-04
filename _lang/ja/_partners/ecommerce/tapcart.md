---
nav_title: Tapcart
article_title: TapcartとBrazeを統合する
description: "TapcartとBrazeの統合について説明します。"
alias: /partners/tapcart/
page_type: partner
search_tag: Partner
---

# Tapcart

> [Tapcart](https://www.tapcart.com/) はShopifyを採用したブランド向けの業界をリードするモバイルコマースプラットフォームで、顧客が好むパーソナライズされた魅力的なショッピング体験を提供するカスタムモバイルアプリの作成を可能にします。

_この統合はTapcartによって管理されます。_

## 前提条件 {#prerequisites}

| 要件              | 説明                                                                                                                                         |
|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Tapcart エンタープライズアカウント | この連携は **Tapcart エンタープライズの顧客** のみご利用いただけます。                                                                              |
| Braze アプリ API キー         | [Braze アプリ識別子 API キー]({{site.baseurl}}/api/identifier_types)が必要です。各プラットフォーム（iOSやAndroidなど）にはそれぞれ独自のアプリ識別子があります。Brazeダッシュボードで、**設定** > **APIと識別子** > **アプリ識別子** に移動してください。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 連携について {#about-the-integration}

TapcartとBrazeの連携方法については、Tapcartの Web サイトにある[Tapcartの連携ガイド](https://help.tapcart.com/en/articles/13893755-braze-tapcart)を直接ご確認ください。連携後、Brazeで以下のTapcart機能を使用できます。

- ベースSDK連携
- iOSおよびAndroidプッシュ通知
- リッチプッシュメッセージ
- ユーザージャーニーのトラッキングとセグメンテーション

以下の機能は現在サポートされていません：Push Stories、Webプッシュ、アプリ内メッセージのカスタマイズ。

{% alert note %}
その他のご質問がある場合は、Tapcartの実装スペシャリストにお問い合わせいただくか、[help@tapcart.co](mailto:help@tapcart.co) までメールでご連絡ください。
{% endalert %}