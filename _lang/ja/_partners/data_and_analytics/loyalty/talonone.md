---
nav_title: Talon.One
article_title: Talon.One
alias: /partners/talonone/
description: "この参考記事では、BrazeとTalon.Oneのパートナーシップについて説明しています。Talon.Oneは、文脈に応じた1対1のクーポン、紹介、割引、およびロイヤルティキャンペーンを迅速かつ効率的に開始できるプロモーションエンジンです。"
page_type: partner
search_tag: Partner

---

# Talon.One

> [Talon.One](https://talon.one/)は、モバイルマーケティングCRMにパーソナライズされたインセンティブを提供し、文脈に応じた1対1のクーポン、紹介、割引、およびロイヤルティキャンペーンを迅速かつ効率的に開始することを可能にします。

_この統合はTalon.Oneによって管理されています。_

## 統合について {#about-the-integration}

BrazeとTalon.Oneの統合により、Talon.Oneによって生成されたコードをBrazeのコネクテッドコンテンツを通じてオーディエンスに送信することで、ロイヤルティプログラムやクーポンプログラムを次のレベルに引き上げることができます。


## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Talon.Oneアカウント | このパートナーシップを活用するには、Talon.Oneアカウントが必要です。 |
| Talon.One APIキー | Talon.Oneの**Settings** > **Developer Settings**で、統合用のBrazeサードパーティAPIキーを作成します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert warning %}
Talon.Oneでは、1分あたり2,500メッセージの最大レート制限が**_必要です_**。このレート制限はBrazeダッシュボードで[変更できます]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#delivery-speed-rate-limiting)。
{% endalert %}

## 統合 {#integration}

1. [Talon.Oneドキュメント](https://docs.talon.one/docs/dev/technology-partners/braze)にアクセスして、統合の設定方法、Talon.One APIクーポンエンドポイントの使用方法、およびBrazeメッセージに必要なコネクテッドコンテンツテンプレートの場所についてのガイダンスを確認してください。
2. Talon.Oneが提供するその他の機能（ロイヤルティポイントや紹介など）を利用するには、次の記事を参照してください。
  - [ロイヤルティポイントをBrazeに追加する](https://docs.talon.one/docs/dev/technology-partners/braze/adding-loyalty-points-braze)
  - [Brazeでロイヤルティ元帳を取得する](https://docs.talon.one/docs/dev/technology-partners/braze/receiving-loyalty-ledger-braze)
  - [Brazeを介してクーポンを作成する](https://docs.talon.one/docs/dev/technology-partners/braze/creating-coupons-braze)
  - [Brazeを介して紹介を作成する](https://docs.talon.one/docs/dev/technology-partners/braze/creating-referrals-braze)
  - [Brazeを介して誕生日プロモーションを作成する](https://docs.talon.one/docs/dev/technology-partners/braze/bday-promotion-braze)