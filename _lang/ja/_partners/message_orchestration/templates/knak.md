---
nav_title: Knak
article_title: Knak
alias: /partners/knak/
description: "この参考記事では、BrazeとKnakのパートナーシップについて説明しています。Knakはキャンペーン作成プラットフォームで、数日や数週間ではなく数分から数時間で完全なレスポンシブメールを作成し、すぐに使えるBrazeテンプレートとしてエクスポートできます。"
page_type: partner
search_tag: Knak

---

# Knak

> [Knak](https://knak.com/) は、企業のマーケティングチームが社内で使用するために構築された、初のキャンペーン作成プラットフォームです。ドラッグ＆ドロップのプラットフォームにより、コーディングや外部の支援なしに、誰でも数分で美しくブランドに沿ったメールやランディングページを作成できます。

_この統合はKnakによって管理されています。_

## 統合について {#about-the-integration}

BrazeとKnakの統合により、数日や数週間ではなく数分から数時間で完全なレスポンシブメールを作成し、すぐに使えるBrazeテンプレートとしてエクスポートできます。Knakは、外部エージェンシーやハンドコーディングを必要とせずに、Brazeで管理するキャンペーンのメール作成をレベルアップしたいマーケター向けに構築されています。

## 前提条件 {#prerequisites}

| 必要条件 | 説明 |
| ----------- | ----------- |
| Knakアカウント | このパートナーシップを活用するには、Knakアカウントが必要です。 |
| Braze REST APIキー | 完全な**テンプレート**権限を持つBraze REST APIキー。<br><br>これはBrazeダッシュボードの**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、お使いのインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="前提条件" }

## ユースケース {#use-cases}

Knakは、コーディングや外部の支援を必要とせずにメール作成をレベルアップしたいマーケター向けに構築されています。以下のような方に最適です：
- 現在メールにシンプルなテンプレートを使用していて、さらにレベルアップしたい方
- Braze用のメール作成を外部の組織や開発者に依頼している方
- アセット制作のクリエイティブコントロールを取り戻し、市場投入までの時間を大幅に短縮したい方

## 統合 {#integration}

### ステップ 1: 統合を設定する {#step-1-configure-your-integration}

Knakで **Integrations** > **Platforms** > **+ Add New Integration** に移動します。

![統合追加ボタン]({% image_buster /assets/img/knak/integration-setup-step-2-add-new-integration.png %})

次に、**Braze**プラットフォームを選択し、Braze APIキーとRESTエンドポイントを入力します。**Create New Integration**をクリックして統合を完了します。

![新しい統合の作成]({% image_buster /assets/img/knak/integration-setup-step-4-add-api-key.png %})

### ステップ 2: Knakテンプレートを同期する {#step-2-sync-your-knak-templates}

Knakで、Brazeに同期したいメールを見つけて**Publish**を選択し、次に**Sync**を選択します。

![Knak統合1]({% image_buster /assets/img/knak/integration-post-step-1-sync.png %})

次にメール名を確認し、**Sync**をクリックします。

![Knak統合2]({% image_buster /assets/img/knak/integration-post-step-2-asset-name.png %})

## 統合を利用する {#using-the-integration}

アップロードしたKnakメールは、Brazeの**エンゲージメント** > **テンプレートとメディア**で確認できます。美しくブランドに沿った、完全にレスポンシブなメールが揃っています。あとはあなたのクリエイティビティ次第です！