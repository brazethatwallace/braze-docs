---
nav_title: Contentsquare
article_title: Contentsquare
description: "このリファレンス記事では、BrazeとContentsquareのパートナーシップについて説明します。Contentsquareは、デジタルエクスペリエンス分析プラットフォームであり、顧客のデジタルエクスペリエンスに基づいてメッセージをターゲティングすることで、キャンペーンの関連性とコンバージョン率を向上させることができます。"
alias: /partners/contentsquare/
page_type: partner
search_tag: Partner

---

# Contentsquare

> [Contentsquare](https://contentsquare.com/) は、カスタマーエクスペリエンスをかつてない方法で理解できるようにするデジタルエクスペリエンス分析プラットフォームです。

*この統合はContentsquareによって管理されています。*

## 統合について {#about-the-integration}

BrazeとContentsquareの統合により、ライブシグナル（不正行為、フラストレーションシグナルなど）をBrazeのカスタムイベントとして送信できます。Contentsquareのエクスペリエンスインサイトを活用し、顧客のデジタルエクスペリエンスとボディランゲージに基づいてメッセージをターゲティングすることで、キャンペーンの関連性とコンバージョン率を向上させます。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Contentsquareアカウント | このパートナーシップを活用するには、Contentsquareアカウントが必要です。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。Brazeダッシュボードで新しいキーを作成するには、**設定** > **APIキー**に移動します。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({% image_buster /assets/img/contentsquare_custom_events.png %})。エンドポイントは、インスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

BrazeとContentsquareの一般的なユースケースには、以下のようなものがあります。
- Braze内でカスタマーエクスペリエンスデータを表面化することで、顧客の意図に基づいてメッセージをハイパーパーソナライズします。
- 顧客のデジタル行動、躊躇、フラストレーション、意図に基づいて顧客をリターゲティングします。
- Contentsquare内で不十分なエクスペリエンスを特定し、ターゲットを絞ったメッセージとリテンションオファーで顧客を取り戻します。
- 適切なタイミングと場所で、より関連性が高く共感的なメッセージを送ることで、リスクのある顧客を回復させます。

## 統合 {#integration}

ContentsquareをBrazeに統合するには、Contentsquare統合カタログから「Live Signals」統合のインストールをリクエストする必要があります。

1. Contentsquareで、**Settings**メニューの**Console**をクリックします。現在作業中のプロジェクトにリダイレクトされます。
2. **Projects**ページで、**Integrations**タブに移動し、**+ Add integration**ボタンをクリックします。
3. 統合カタログで**Live Signals**統合を見つけ、**Add**をクリックします。その後、ContentsquareチームからライブシグナルをBrazeに送信するためのコードスニペットの設定について連絡があります。
4. Contentsquareにより統合が処理されます。統合が完了すると、インジケーターのテキストが更新されます。

詳細については、[Contentsquare統合をリクエストする](https://uxanalyser.zendesk.com/hc/en-gb/articles/4405613239186)を参照してください。

## この統合を使う {#using-this-integration}

統合が完了すると、Contentsquareのカスタムイベントをキャンペーンやキャンバスで使用できるようになります。**データ設定** > **カスタムイベント**から、どのイベントがBrazeに送信されているかを確認できます。

![BrazeのカスタムイベントタブにおけるContentsquareライブシグナルデータ]({% image_buster /assets/img/contentsquare_custom_events.png %})