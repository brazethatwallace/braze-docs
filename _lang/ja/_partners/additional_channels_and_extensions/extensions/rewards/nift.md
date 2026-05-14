---
nav_title: Nift
article_title: Nift
description: "このリファレンス記事では、BrazeとNiftのパートナーシップについて説明します。Niftは、企業が顧客を獲得し、エンゲージし、維持するのを支援する双方向プラットフォームです。"
alias: /partners/nift/
page_type: partner
search_tag: Partner

---

# Nift

> [Nift](https://gonift.com/) は、企業が顧客を獲得し、エンゲージし、維持するのを支援します。この双方向プラットフォームでは、パートナーがNiftギフトカードで顧客への感謝を示すことができます。顧客に感謝を示すことで、顧客生涯価値が高まり、増分収益が生まれます。

_この統合はNiftによって管理されています。_

## 統合について {#about-the-integration}

BrazeとNiftの統合により、カスタマーライフサイクルの重要なタイミングでNiftギフトを含む「お礼」を自動的にトリガーし、どの顧客がギフトを使用したかを特定できます。Niftギフトカードは、Niftのマッチメイキング技術を利用して費用対効果の高い大規模な新規顧客獲得を行うブランドが提供する製品やサービスへのアクセスに使用できます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
|---|---|
| Niftアカウント | このパートナーシップを活用するには、Niftアカウントが必要です。 |
| Braze REST APIキー | すべてのユーザーデータ権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントは、[インスタンス]({{site.baseurl}}/api/basics/#endpoints)のBraze URLによって異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## 統合 {#integration}

### ステップ 1:NiftでBrazeに接続する {#step-1-connect-to-braze-in-nift}

[Niftダッシュボード](https://www.gonift.com/users/sign_in)にアクセスし、**Accounts** > **Integrations** > **Braze**に移動して、**Connect**をクリックします。

### ステップ 2:Braze認証情報を追加する {#step-2-add-braze-credentials}

**Link your Braze Account**ページで、Braze REST APIキーを入力し、[インスタンス]({{site.baseurl}}/api/basics/#endpoints)のBraze URLに応じてBrazeエンドポイントを選択します。

顧客に送信される紹介リンクの顧客IDパラメーター名を変更できます。Niftは、顧客が当社のブランドのギフトを選択した際に、その顧客をBrazeで処理済みとしてマークします。

**Link Account**をクリックします。

![ユーザーにBraze APIキーとBrazeダッシュボードURLの入力を求めるNiftサービス統合ページ。]({% image_buster /assets/img/nift/link_your_braze_account.png %})

## 統合の使用 {#using-the-integration}

統合を使用するには、メッセージングで紹介リンクを配布します。顧客が紹介リンクを使用し、当社のブランドのギフトを選択すると、NiftはBrazeでその顧客を処理済みとしてマークします。

Brazeとの統合後、Niftは以下のデータを含むイベントを既存の顧客のBrazeレコードに自動的にプッシュします。

- イベント名: `nift_processed`
- 時間: 顧客がギフトを選択/使用した時刻