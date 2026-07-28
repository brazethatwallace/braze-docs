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

BrazeとKomoの統合により、Komoエンゲージメントハブを通じてファーストパーティデータおよびゼロパーティデータを収集できます。これらのハブは、インタラクティブなコンテンツやゲーミフィケーション機能を提供するダイナミックなマイクロサイトです。これらのハブから収集されたユーザーデータは、Braze APIに送信されます。

{% multi_lang_include partners/extensions/landing_pages/komo_integration_bullets.md %}

## 前提条件 {#prerequisites}

| 要件 | 説明 |
| ----------- | ----------- |
| Komo アカウント | このパートナーシップを活用するには、アクティブな Komo アカウントが必要です。今すぐトライアルを開始するには、[Komo](https://komo.tech/) にアクセスしてください。 |
| Braze REST APIキー | `users.track` 権限を持つ Braze REST APIキー。<br><br>これは、Brazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze REST エンドポイント | [REST エンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics#endpoints)。エンドポイントは、お使いのインスタンスの Braze URL に応じて異なります。<br><br>たとえば、次のようになります: https://rest.iad-03.braze.com |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

{% tabs local %}
{% tab データキャプチャ - フォーム送信 %}

ユーザーがKomoでカスタマイズ可能なデータキャプチャフォームを送信すると、Braze連携でマッピングされたKomoフィールドが`/users/track/` API呼び出しを通じてBrazeに渡されます。

データキャプチャフォームは、カードの最初または最後に存在します。

{% endtab %}
{% tab マーケットリサーチ - 近日公開 %}

Komoでは、ユーザーがクイズの質問、投票、パーソナリティテスト、スワイパーなどに回答した際にキャプチャされたマーケットリサーチデータを渡す機能も提供しています。このデータにより、フォーム送信でキャプチャされたデータ以上にユーザーのプロファイルを充実させることができます。

{% endtab %}
{% endtabs %}

## 連携 {#integration}

### ステップ1：Komo エンゲージメントハブとカードを公開する {#step-1-publish-a-komo-engagement-hub-and-card}

データキャプチャフォームを含むカードが少なくとも1つあるKomo ハブを公開する必要があります。公開後、ユーザーエクスペリエンスをエンドツーエンドでテストし、連携が正しく機能していることを確認できます。

![Komo ハブ。]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step1.png %})

### ステップ2：Braze Connected Appを追加する {#step-2-add-the-braze-connected-app}

Komoで**Company Settings**タブに移動し、**Connected Apps**セクションを選択します。

次に、リストからBraze連携を見つけ、**Connect**ボタンを選択して連携を有効にします。

![Braze連携の接続。]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2a.png %}){: style="max-width:50%;"}

![Braze連携の接続ステップ2b。]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step2b.png %})

#### ワークフローによる連携の設定 {#configure-the-integration-via-a-workflow}

次に、Brazeにデータを同期するためのワークフローを、ワークスペース、サイト、またはカード内に設定する必要があります。

ワークフローのスコープをワークスペース全体、サイト（複数のカードを含む）、または単一のカードのいずれに設定するかは、ワークフローを複数のカードやキャンペーンにわたってトリガーしたいかどうかによって異なります。

ワークフローを作成したら、トリガーを定義し、ステップメニューでBrazeを検索して「Track User」ステップを追加します。

![Track Userの設定。]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3a.png %})

ここから、KomoからBrazeに同期するイベント、アトリビューション、および購読を設定します。

![コンテンツブロックリスト。]({% image_buster /assets/img/Braze Komo Images v2/Braze-Komo-Step3b.png %})

## インテグレーションの使用 {#using-the-integration}

インテグレーションが稼働しました。**Workflow Runs** タブで各実行を監視できます。