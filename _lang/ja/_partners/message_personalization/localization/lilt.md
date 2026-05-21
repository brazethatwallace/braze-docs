---
nav_title: LILT
article_title: LILT
description: "このリファレンス記事では、BrazeとLILTのパートナーシップについて説明します。"
alias: /partners/lilt/
page_type: partner
search_tag: Partner
---

# LILT

> [LILT](https://lilt.com/)は、企業の翻訳とコンテンツ作成のための完全なAIソリューションです。LILTは、AIエージェントと完全に自動化されたワークフローにより、グローバル企業のコンテンツ、製品、コミュニケーション、サポート業務の拡張と最適化を可能にします。

_この統合はLILTによって管理されています。_

## この統合について {#about-this-integration}

LILT Braze Connectorは、AIのスピードとエンタープライズグレードの品質でHTMLメールテンプレートの翻訳を可能にします。ブランドに沿ったインスタント翻訳や品質保証されたベリファイド翻訳をリクエストし、LILTから直接Brazeで多言語メールコンテンツを受け取ることができます。

## ユースケース {#use-cases}

LILTのBraze統合は、翻訳プロセスを自動化・高速化し、グローバルマーケティングチームがブランドの一貫性を保ちながら多言語キャンペーンを迅速に展開できるようにします。

### グローバルキャンペーンの効率的な展開 {#streamlined-global-campaign-launch}

手作業による翻訳の受け渡しによる遅延なく、複数の地域で同時にマーケティングキャンペーンを展開できます。

- **シナリオ：** 自社が10か国で新製品を発売します。
- **ソリューション：** マーケティングチームがBrazeで英語のメールテンプレートを完成させ、`LILT: Ready`のタグを付けると、LILT Connectorが自動的にコンテンツを取り込みます。ドメインに特化した言語スペシャリストが、品質保証のためにLILTプラットフォームでAI翻訳プロンプトをレビューし、Connectorが翻訳されたバージョンをBrazeにプッシュバックします。
- **メリット：** グローバルキャンペーンの市場投入までの時間を数日から数時間に短縮し、すべての顧客が最適なタイミングで新製品の発表を受け取ることができます。

### ブランドに沿ったインスタントローカライゼーション {#instant-brand-aligned-localization}

LILTのAIを使用して、一刻を争うコミュニケーションのために即座にブランドに沿った翻訳を行うことができます。

- **シナリオ：** フラッシュセール、期間限定オファー、緊急サービス停止などのメールを、5つの地域に即座に配信する必要があります。
- **ソリューション：** メールテンプレートに`LILT: Instant`のタグを付けます。LILTは、自社に特有のAIと言語資産（用語集やスタイルガイドなど）を使用して、数分以内に高品質でブランドの一貫性がある翻訳を生成します。
- **メリット：** 一刻を争うマーケティングに不可欠な、ブランドの声や品質を犠牲にすることなく、ハイパーレスポンシブでリアルタイムなコミュニケーションを可能にします。

## 前提条件 {#prerequisites}

| 要件 | 説明 |
|-----------------------|-----------------|
| LILTアカウント | このパートナーシップを利用するには、LILTアカウントが必要です。 |
| Braze REST APIキー | 以下の権限を持つBraze REST APIキー：<br>- `templates.email.create`<br>- `templates.email.update`<br>- `templates.email.info`<br>- `templates.email.list`<br>- `templates.translations.source.get`<br>- `templates.translations.update`<br>- `templates.translations.get`<br>- `templates.translations.all.get`<br><br> このキーはBrazeダッシュボードの**設定** > **APIキー**から作成します。 |
| Braze RESTエンドポイント | [RESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントはインスタンスのBraze URLに応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }


## 統合 {#integration}

### ステップ 1：LILT Braze Connectorを設定する {#step-1-configure-the-lilt-braze-connector}

1. LILTにログインし、**Connect** > **New Connector** > **Braze**と進みます。

![LILTのBrazeコネクター。]({% image_buster /assets/img/lilt/image_1_select_connector.png %})

{: start="2"}
2. Brazeコンテンツに必要なローカライゼーションワークフローを選択します。

![LILTのBrazeワークフロー。]({% image_buster /assets/img/lilt/image_2_select_workflow.png %})

{: start="3"}
3. 必要な設定の詳細を入力し、確認します：
- Braze APIキー
- Braze RESTエンドポイント

![API認証情報の入力。]({% image_buster /assets/img/lilt/image_3_api_creds.png %})

{: start="4"}
4. **Verify**を選択してセットアップをテストします。接続が確認されたら、設定を保存します。

### ステップ 2：Brazeワークスペースを準備する {#step-2-prepare-your-braze-workspace}

1. Brazeワークスペース設定で多言語機能を有効にします。

![Brazeでロケールを設定する。]({% image_buster /assets/img/lilt/image_4_lilt_locales.png %})

{: start="2"}
2. LILTワークフロー用にBrazeで以下のタグを作成します：
- `LILT: Ready`
- `LILT: In progress`
- `LILT: Sent to LILT`
- `LILT: Delivered`
- `LILT: Needs Attention`
- `LILT: Instant`

![BrazeでLILTタグを設定する。]({% image_buster /assets/img/lilt/image_5_lilt_tags.png %})

{: start="3"}
### ステップ 3：翻訳のためにコンテンツをLILTに送る {#step-3-send-content-to-lilt-for-translation}

1. LILT Braze Connectorを設定した後、Brazeメールテンプレート内でLiquid翻訳タグを使用して、翻訳対象のコンテンツを識別します。
- 例：{% raw %}`{% translation id_0 %}`Hello, `{{first_name}}!{% endtranslation %}`{% endraw %}
2. 希望するワークフローを示すテンプレートタグを更新して、翻訳を開始します：
- ベリファイド翻訳には`LILT: Ready`を選択します
- ブランドに沿ったインスタント翻訳には`LILT: Instant`を選択します
3. LILT Braze Connectorは、あらかじめ設定されたタイミングでタグ付けされたコンテンツをLILTに取り込みます。Brazeのコンテンツタグが自動的に更新されてプロジェクトの段階が反映されるため、翻訳の進捗状況を追跡できます。

![翻訳タグ付きBrazeメールテンプレート。]({% image_buster /assets/img/lilt/image_6_braze_template.png %})