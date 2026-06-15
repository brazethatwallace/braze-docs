---
nav_title: Mention Me
article_title: Mention MeとBrazeを統合する
description: Mention Me 統合設定ガイド
alias: /partners/mention_me/
page_type: partner
search_tag: Partner
---

# Mention Me

> [Mention Me](https://www.mention-me.com/)とBrazeを組み合わせることで、プレミアム顧客を獲得し、揺るぎないブランドロイヤルティを育むための入り口とすることができます。ファーストパーティの紹介データをBrazeにシームレスに統合することで、ブランドのファンをターゲットにした、高度にパーソナライズされたオムニチャネル体験を提供できます。

_この統合はMention Meによって管理されます。_

## 前提条件 {#prerequisites}

開始する前に、以下が必要です。

| 前提条件 | 説明 |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Mention Meアカウント | このパートナーシップを活用するには、[Mention Me](https://mention-me.com/login)アカウントが必要です。 |
| Braze REST APIキー | `users.track`および`templates.email.create`権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、お使いのインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

* Mention Meが紹介した顧客の連絡先データとオプトインをリアルタイムでBrazeに送信します
* 紹介データを使ってクーポンのリマインダーメールを作成します
* 紹介データを使用して高価値の顧客をセグメント化しターゲットを絞ることで、他のマーケティングチャネルのパフォーマンスを強化します

## Mention MeからBrazeに送信されるデータ {#what-data-is-sent-from-mention-me-to-braze}

この統合を設定すると、Mention Meで顧客属性とイベントが自動的に作成されるため、事前にこれらの作業を行う必要はありません。

関連するイベントやカスタム属性のリンクには、Brazeに登録された顧客のメールアドレスが使用されます。Mention Meは、オプトインのステータスに関係なく、Mention Meを介してイベントをトリガーした見込み客や既存顧客のイベントと連絡先プロファイル属性を送信します。

詳細については、[連絡先プロファイルの属性とイベント](https://help.mention-me.com/hc/en-gb/articles/26677937177501-What-Mention-Me-data-is-sent-to-Braze)を参照してください。

## Mention Meの統合 {#integrating-mention-me}

{% alert tip %}
詳細なステップバイステップのチュートリアルについては、[Mention MeのBraze設定ドキュメント](https://help.mention-me.com/hc/en-gb/articles/26151773368221-How-to-setup-Braze-with-Mention-Me)を参照してください。
{% endalert %}

Mention MeとBrazeを統合するには:

1. Mention Meで[Braze統合](https://mention-me.com/merchant/~/integrations/braze)ページに移動し、**Connect**を選択します。
2. **Create New Authorization**を選択し、[事前に作成したAPIキー](#prerequisites)を追加して、Brazeインスタンスを選択します。
3. 同期する国を1つ以上選択します。
4. 完了したら、**Connect**を選択します。