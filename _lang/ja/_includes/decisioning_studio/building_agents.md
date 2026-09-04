# AI意思決定エージェントの構築 {#building-ai-decisioning-agents}

> BrazeAI Decisioning Studio™ のエージェントを構築する方法を学習することで、パーソナライズされた実験を自動化し、手動で AB テストを行うことなく、コンバージョン、リテンション、収益などの成果を最適化することができます。

{% multi_lang_include decisioning_studio/alert_multi_platform_support.md %}

## エージェントについて {#about-agents}

AI意思決定エージェントとは、特定のビジネス目標を達成するためにカスタマイズされた、BrazeAI<sup>TM</sup>意思決定エンジンのカスタム構成です。

たとえば、初回購入後のフォローアップコンバージョンを増加させるためのリピート購入エージェントを構築できます。Brazeでオーディエンスとメッセージを定義すると、意思決定エージェントが毎日実験を実行し、各顧客に対して商品オファー、メッセージのタイミング、頻度のさまざまな組み合わせを自動的にテストします。時間の経過とともに、BrazeAI<sup>TM</sup>は最も効果的な方法を学習し、リピート購入率を最大化するためにBrazeを通じてパーソナライズされた送信をオーケストレーションします。

優れたエージェントを構築するには、以下を行います:

- BrazeAI<sup>TM</sup>が最適化する成功指標（収益、コンバージョン、ARPUなど）を選択します。
- テストするディメンション（オファー、件名、クリエイティブ、チャネル、送信時間など）を定義します。
- 各ディメンションのオプション（メールとSMSの比較、毎日と毎週の頻度の比較など）を選択します。

![紹介メール用のDecisioning Studioエージェントの例を示すダイアグラム。]({% image_buster /assets/img/offerfit/example_use_cases_referral_email.png %})

## サンプルエージェント {#sample-agents}

ここでは、BrazeAI Decisioning Studio™で構築できるエージェントの例をいくつか紹介します。AI意思決定エージェントは、顧客とのインタラクションから学習し、そのインサイトを翌日のアクションに反映します。

{% multi_lang_include decisioning_studio/sample_agents.md %}

## エージェントの構築 {#building-an-agent}

### 前提条件 {#prerequisites}

エージェントを構築する前に、[BrazeAI Decisioning Studio™を統合する]({{site.baseurl}}/developer_guide/decisioning_studio/integration)必要があります。

### ステップ1:AI Expert Services に問い合わせる {#step-1-contact-ai-expert-services}

AI Expert Services チームがお客様と緊密に連携し、意思決定エージェントのスコープ設定、設計、構築を行います。まだお問い合わせいただいていない場合は、[こちらからお問い合わせ](https://www.braze.com/get-started/)ください。

以下のステップをチームと一緒に進めることで、お客様に最適なカスタムエージェントを構築します。

### ステップ2:エージェントを設計する {#step-2-design-your-agent}

AI Expert Services チームと共に、以下を定義します。

- ターゲットオーディエンス
- 最適化するビジネス指標
- BrazeAI<sup>TM</sup>意思決定エージェントのアクション
- ビジネス成果を向上させるためにエージェントが活用すべきファーストパーティの顧客データ

設計が完了したら、チームがお客様と協力して、追加の統合要件を特定し、完了させます。

### ステップ3:配信プラットフォームを設定する {#step-3-set-up-your-delivery-platform}

次に、AI Expert Services チームがカスタマーエンゲージメントプラットフォームの設定をサポートします。Decisioning Studioは Braze との併用が最も効果的ですが、その他のさまざまなプラットフォームにも対応しています。追加リソースについては、AI Expert Services チームにお問い合わせください。

{% tabs local %}
{% tab Braze %}
Braze を設定するには、以下を行います。

1. [キャンペーン]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/api_triggered_delivery)または[キャンバス]({{site.baseurl}}/user_guide/messaging/canvas/create_a_canvas/?tab=api-triggered%20delivery#step-12-determine-your-canvas-entry-schedule)を作成します。BrazeAI Decisioning Studio™はこの配信方法を使用して、定義されたオーディエンス内のユーザーに1:1のパーソナライズされたアクティベーションイベントを送信します。
2. BrazeAI<sup>TM</sup>が専用のコントロールグループとして機能できるよう、Brazeの[コントロールグループ]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group)は含めないでください。
3. ディメンションに応じて、クリエイティブコンテンツにLiquidタグを設定し、BrazeAI<sup>TM</sup>のレコメンデーションに基づいてメッセージングをダイナミックに表示できます。BrazeAI<sup>TM</sup>は Braze APIを使用して、テンプレート内のLiquidタグに顧客固有のコンテンツを渡します。
{% endtab %}
{% endtabs %}

### ステップ4:ローンチとモニタリング {#step-4-launch-and-monitor}

エージェントをローンチした後も、AI Expert Services チームが引き続きモニタリングを行い、合意した設計に合わせてチューニングします。必要に応じて、エージェントの調整、拡張、変更もサポートします。