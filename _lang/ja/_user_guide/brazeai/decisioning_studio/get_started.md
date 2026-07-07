---
nav_title: はじめに
article_title: Decisioning Studioをはじめる
layout: dev_guide
guide_top_header: "Decisioning Studioをはじめる"
guide_top_text: ""
page_order: 0
search_rank: 2
page_type: landing
description: "このセクションでは、Decisioning Studioの概要と、あらゆるビジネス指標を最適化する意思決定エージェントの設計・デプロイ方法について紹介します。"

guide_featured_title: "セクション記事"
guide_featured_list:
  - name: エージェントを設計する
    link: /docs/user_guide/brazeai/decisioning_studio/design_agents
    image: /assets/img/braze_icons/settings-01.svg
  - name: データを準備する
    link: /docs/user_guide/brazeai/decisioning_studio/prepare_data
    image: /assets/img/braze_icons/database-01.svg
  - name: オーディエンスを定義する
    link: /docs/user_guide/brazeai/decisioning_studio/audience
    image: /assets/img/braze_icons/users-01.svg
  - name: オーケストレーションを設定する
    link: /docs/user_guide/brazeai/decisioning_studio/orchestration_setup
    image: /assets/img/braze_icons/dataflow-04.svg

guide_menu_title: "その他のリソース"
guide_menu_list:
  - name: Decisioning Studioについて
    link: /docs/user_guide/brazeai/decisioning_studio
    image: /assets/img/braze_icons/info-circle.svg
  - name: Decisioning Studio FAQ
    link: /docs/user_guide/brazeai/decisioning_studio/faq
    image: /assets/img/braze_icons/annotation-question.svg
---

BrazeAI Decisioning Studio™を使用すると、あらゆるビジネス指標を最適化する意思決定エージェントを設計・デプロイできます。

このリファレンスでは、エージェントの設計、データソースの構成と接続、オーケストレーションの設定、パフォーマンスの評価など、Decisioning Studioのセットアップに関わるステップの概要を説明します。

## 主要な設計上の意思決定 {#key-design-decisions}

AI意思決定サービスチームと協力して、以下の意思決定を行います。

| 意思決定 | 説明 | 例 |
|----------|------|-----|
| **成功指標** | カスタマーエンゲージメントをパーソナライズする際に、エージェントが最大化する指標は何ですか？ | 収益、生涯価値、ARPU、コンバージョン、リテンション |
| **オーディエンス** | Decisioning Studioエージェントは誰に対してカスタマーエンゲージメントの意思決定を行いますか？ | 全顧客、ロイヤルティメンバー、離脱リスクのあるサブスクライバー |
| **実験グループ** | Decisioning Studioのランダム化比較試験はどのように構成すべきですか？ | Decisioning Studio、ランダムコントロール、BAU、ホールドアウト |
| **ディメンション** | エージェントがパーソナライズすべき意思決定は何ですか？ | 時間帯、件名、頻度、オファー、チャネル |
| **オプション** | エージェントが使用できるオプションは何ですか？ | 特定のテンプレート、オファー、時間枠 |
| **制約** | エージェントが絶対に行うべきでない意思決定は何ですか？ | 地理的制限、予算上限、適格性ルール |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="主要な設計上の意思決定" }

これらの意思決定はそれぞれ、エージェントが生み出せるインクリメンタルなリフトの大きさとスピードに影響します。AI意思決定サービスチームがお客様と協力して、すべてのビジネスルールを遵守しながら最大の価値を生み出すエージェントを設計します。

![成功指標、オーディエンス、実験グループ、ディメンション、オプション、制約がDecisioning Studioエージェントの設計にどのように反映されるかを示す図]({% image_buster /assets/img/decisioning_studio/decisioning_studio_pro_agent_design.png %})

## Decisioning Studioの機能 {#decisioning-studio-capabilities}

| 機能 | 詳細 |
|------|------|
| **あらゆる成功指標** | 収益、コンバージョン、ARPU、生涯価値、またはあらゆるビジネスKPIに対して最適化 |
| **無制限のディメンション** | オファー、チャネル、タイミング、頻度、クリエイティブなど、あらゆる要素でパーソナライズ |
| **あらゆるCEP** | Braze、Salesforce Marketing Cloud、またはあらゆるプラットフォーム向けのカスタム統合とのネイティブ統合 |
| **AI意思決定サービス** | Brazeのデータサイエンスチームによる専任サポート |
| **高度な実験設計** | 完全にカスタマイズ可能なトリートメントグループとホールドアウト |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Decisioning Studioの機能" }

## ベストプラクティス {#best-practices}

Decisioning Studioエージェントを設計する際のベストプラクティスをいくつかご紹介します。

- **データの豊富さを最大化する：** エージェントが顧客に関する情報を多く持つほど、パフォーマンスが向上します。
- **アクションを多様化する：** エージェントが取れるアクションのセットが多様であるほど、各ユーザーに対する戦略をよりパーソナライズできます。
- **制約を最小限にする：** エージェントに対する制約は少ないほど効果的です。制約はビジネスルールを遵守しつつ、エージェント主導の実験をできる限り自由にするよう設計してください。