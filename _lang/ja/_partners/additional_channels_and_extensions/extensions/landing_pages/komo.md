---
nav_title: Komo
article_title: Komo
description: "この参考記事では、BrazeとKomoの提携について説明しています。Komoは、ゲーミフィケーション、インタラクティブコンテンツ、コンペティション、賞品、ロイヤルティを専門とするカスタマーエンゲージメントプラットフォームです。この統合を通じて、Komoで収集されたファーストパーティおよびゼロパーティデータをBrazeに公開できます。"
alias: /partners/komo/
page_type: partner
search_tag: Partner

---

# Komo

> [Komo](https://komo.tech/) は、ゲーミフィケーション、インタラクティブコンテンツ、コンペティション、賞品、ロイヤルティに特化したカスタマーエンゲージメントプラットフォームです。

*この統合はKomoによって管理されています。*

## 統合について {#about-the-integration}

BrazeとKomoの統合により、Komo Engagement Hubを通じてファーストパーティデータとゼロパーティデータを収集できます。これらのハブは、インタラクティブなコンテンツとゲーミフィケーション機能を提供するダイナミックなマイクロサイトです。これらのハブから収集されたユーザーデータは、Braze APIに送信されます。

- KomoからBrazeにファーストパーティおよびゼロパーティのユーザーデータをリアルタイムで取り込みます
- アンケート、投票、クイズの質問に回答する際に、市場調査およびユーザーの好みのデータを取り込みます
- ユーザーが引き続きエンゲージし、自身に関するデータをさらに共有するにつれて、Brazeでユーザープロファイルを徐々に構築します
- Brazeを通じて送信されるトランザクションメールの外観と操作感を標準化します

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Komoアカウント | このパートナーシップを利用するには、アクティブなKomoアカウントが必要です。[Komo](https://komo.tech/) にアクセスして、今すぐトライアルを開始してください。 |
| Braze REST APIキー | `users.track` 権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、インスタンスのBraze URLに依存します。<br><br>たとえば、https://rest.iad-03.braze.com のようになります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

{% tabs local %}
{% tab Data Capture - Form Submission %}

ユーザーがKomoでカスタマイズ可能なデータキャプチャフォームを送信すると、Braze統合でマッピングされているKomoのフィールドが、`/users/track/` API呼び出しを介してBrazeに渡されます。

データキャプチャフォームは、カードの開始時または終了時のいずれかに存在します。

{% endtab %}
{% tab Market Research - Coming soon %}

Komoでは、ユーザーがクイズの質問、投票、パーソナリティテスト、スワイパーなどに回答したときに取得したマーケットリサーチデータを渡すこともできます。このデータにより、フォーム送信でキャプチャしたデータを超えて、ユーザーのプロファイルを強化できます。

{% endtab %}
{% endtabs %}

## 統合 {#integration}

### ステップ 1: Komo Engagement Hubとカードを公開する {#step-1-publish-a-komo-engagement-hub-and-card}

データキャプチャフォームを含む少なくとも1枚のカードを持つKomo Hubを公開する必要があります。公開後、ユーザーエクスペリエンスをエンドツーエンドでテストし、統合が正しく機能していることを確認できます。

![Komo Hub。]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step1.png %})

### ステップ 2: Braze Connectedアプリを追加する {#step-2-add-the-braze-connected-app}

Komoで**Company Settings**タブに移動し、**Connected Apps**セクションを選択します。

次に、リストからBraze統合を見つけて、**Connect**ボタンを選択して統合を有効にします。

![Braze統合を接続する。]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2a.png %}){: style="max-width:50%;"}

![Braze統合の接続ステップ2b。]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2b.png %})

#### ワークフローで統合を構成する {#configure-the-integration-via-a-workflow}

次に、ワークスペース、サイト、またはカード内で、Brazeにデータを同期するワークフローを設定する必要があります。

ワークスペース全体、サイト（多くのカードを含む）、または単一のカードのいずれをワークフローのスコープとするかは、ワークフローを多くのカードやキャンペーンにわたってトリガーさせたいかどうかによります。

ワークフローを作成後、トリガーを定義し、ステップメニューでBrazeを検索し、「Track User」ステップを追加します。

![Track Userの設定。]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3a.png %})

ここから、KomoからBrazeに同期させたいイベント、アトリビューション、サブスクリプションを設定します。

![コンテンツブロックリスト。]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3b.png %})

## 統合の使用 {#using-the-integration}

これで統合が稼働しています。ワークフロー実行タブで各実行をモニターできます。