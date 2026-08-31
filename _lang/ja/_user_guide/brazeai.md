---
nav_title: BrazeAI
article_title: BrazeAI
description: "BrazeAI<sup>TM</sup>は、エンゲージメント戦略における創造性、パーソナライゼーション、最適化へのハードルを下げる、利用しやすく使いやすいツールのコレクションを提供します。"
page_order: 8
layout: dev_guide
search_rank: 12
tool:
  - Dashboard

guide_top_header: "BrazeAI<sup>TM</sup>"
guide_top_text: "BrazeAI<sup>TM</sup>は、エンゲージメント戦略における創造性、パーソナライゼーション、最適化へのハードルを下げる、利用しやすく使いやすいツールのコレクションを提供します。BrazeAI<sup>TM</sup>の機能を活用すれば、信頼できるアドバイザーとして創造性を導き、より良い意思決定を行い、顧客のユーザーエクスペリエンスを最適化できます。このハブでは、生成AI、インテリジェントスイート、アイテムのおすすめ、エージェント、その他キャンペーンやキャンバスで活用できるBrazeAI機能のガイドをご覧いただけます。"

guide_featured_title: "機能"
guide_featured_list:
  - name: エージェント
    link: /docs/user_guide/brazeai/agents
    image: /assets/img/braze_icons/star-06.svg
  - name: Braze MCPサーバー
    link: /docs/user_guide/brazeai/mcp_server
    image: /assets/img/braze_icons/dataflow-01.svg
  - name: コンテンツオプティマイザー
    link: /docs/user_guide/brazeai/content_optimizer
    image: /assets/img/braze_icons/image-user-check.svg
  - name: Decisioning Studio
    link: /docs/user_guide/brazeai/decisioning_studio
    image: /assets/img/braze_icons/stars-03.svg
  - name: 生成AI
    link: /docs/user_guide/brazeai/generative_ai
    image: /assets/img/braze_icons/lightbulb-02.svg
  - name: インテリジェントスイート
    link: /docs/user_guide/brazeai/intelligence_suite
    image: /assets/img/braze_icons/clock.svg
  - name: アイテムのおすすめ
    link: /docs/user_guide/brazeai/item_recommendations
    image: /assets/img/braze_icons/hearts.svg
  - name: オペレーター
    link: /docs/user_guide/brazeai/operator
    image: /assets/img/braze_icons/edit-05.svg
  - name: 予測スイート
    link: /docs/user_guide/brazeai/predictive_suite
    image: /assets/img/braze_icons/stars-01.svg
  - name: 勝者パス
    link: /docs/user_guide/messaging/canvas/canvas_components/experiment_step/winning_path
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: BrazeAI<sup>TM</sup>で最適化
    link: /docs/user_guide/brazeai/intelligence_suite/variant_selection
    image: /assets/img/braze_icons/trophy-01.svg
---

<br>

## 機能の概要 {#feature-overview}

| 目標 | 推奨される機能 |
| --- | --- |
| ユーザーのコンテキストを使用してユーザーごとにメッセージコピーをパーソナライズする | [Brazeエージェント]({{site.baseurl}}/user_guide/brazeai/agents)（[キャンバス]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step)または[カタログ]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents#use-catalog-agents)）、一度限りの下書きコピーには[生成AI]({{site.baseurl}}/user_guide/brazeai/generative_ai) |
| どのメッセージコンテンツ（件名やCTAなど）が時間の経過とともに最もパフォーマンスが高いかを最適化する | [コンテンツオプティマイザー]({{site.baseurl}}/user_guide/brazeai/content_optimizer)（メール、プッシュ通知、またはSMS/MMS/RCS）または[BrazeAI<sup>TM</sup>で最適化]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/variant_selection) |
| オファー、チャネル、タイミングにわたる1:1の意思決定でビジネス指標（収益、コンバージョン）を最大化する | [Decisioning Studio]({{site.baseurl}}/user_guide/brazeai/decisioning_studio) |
| 解約しそうなユーザーやイベントを実行しそうなユーザーを特定する | [解約予測]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_churn)または[予測イベント]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events) |
| メッセージ内のカタログから特定の商品をレコメンドする | [アイテムレコメンデーション]({{site.baseurl}}/user_guide/brazeai/item_recommendations) |
| ユーザーごとに最適なタイミングまたは最適なチャネルで送信する | [インテリジェントタイミング]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing)、[インテリジェントチャネル]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel) |
| ダッシュボードで直接コピーやクリエイティブを作成・改善する | [オペレーター]({{site.baseurl}}/user_guide/brazeai/operator) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="機能の概要" }

## よくある質問 {#frequently-asked-questions}

### BrazeAIとは？ {#what-is-brazeai}

BrazeAIは、生成コピー、パーソナライゼーション、予測、レコメンデーション、意思決定のためのBraze内のAI搭載ツールセットです。このページの機能リンクを使用して、各機能の設定ガイドを開いてください。

### 最初にどのBrazeAI機能を使うべきですか？ {#which-brazeai-feature-should-i-use-first}

このページの[機能の概要](#feature-overview)テーブルを参照して、コピー生成、送信時間の最適化、製品レコメンデーションなど、目標に合ったBrazeAI機能を見つけてください。