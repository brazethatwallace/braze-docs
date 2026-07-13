---
nav_title: FAQ
article_title: Decisioning Studio よくある質問
page_order: 8
page_type: FAQ
description: "このページでは、Decisioning Studioに関するよくある質問への回答を提供します。"
---

# よくある質問 {#frequently-asked-questions}

> この記事では、Decisioning Studioに関するよくある質問への回答を提供します。

## 意思決定エージェントとは何ですか？ {#what-is-a-decisioning-agent}

意思決定エージェントとは、特定のビジネス目標を達成するためにカスタマイズされた、BrazeAI Decisioning Studio™のカスタム設定です。これは、選択した成功指標、ディメンション、およびオプションによって定義されます。意思決定エージェントは、選択したビジネス指標を最大化するために、顧客ごとに最適なアクションを自動的に発見します。

### どの指標を最適化できますか？ {#what-metrics-can-i-optimize-for}

目標に沿ったあらゆるビジネス指標に対して最適化できます。例えば、収益、コンバージョン、ユーザーあたりの平均収益（ARPU）、顧客生涯価値（CLV）、利益、契約更新、その他のビジネスKPIなどがあります。

### Decisioning Studioにおけるディメンションとは何ですか？ {#what-are-dimensions-in-decisioning-studio}

ディメンションとは、意思決定エージェントが成功指標を最大化するために操作できる*手段の種類*と考えることができます。典型的なディメンションには、オファー、件名、クリエイティブ、チャネル、送信時間などがあります。

### アクションバンクとは何ですか？ {#what-is-an-action-bank}

アクションバンクは、意思決定エージェントが各ディメンションの「レバー」に対してアクセス可能な*具体的な選択肢*を定義します。例えば、チャネルディメンションについては、意思決定エージェントがアクセスできる特定のチャネルを定義します。オファーディメンションでは、意思決定エージェントがテストできる特定のオファーを定義します。

### 意思決定エージェントは、設定していないアクションを取ることができますか？ {#can-the-decisioning-agent-take-actions-i-havent-configured}

いいえ。意思決定エージェントは、設定してアクションバンクに追加したアクションのみを実行できます。つまり、可能なすべてのアクションは、アクションバンクに入れたものの組み合わせによって定義されます。

### 制約とは何ですか？ {#what-are-constraints}

制約は、意思決定エージェントが重要なビジネスルールを遵守するよう、そのアクションを制限します。例えば、特定のオファーが対象外の地域にいる顧客に選択されないようにしたり、意思決定エージェントが支出できる最大予算を設定したりすることが挙げられます。

### Decisioning Studio GoとDecisioning Studio Proの違いは何ですか？ {#what-is-the-difference-between-decisioning-studio-go-and-decisioning-studio-pro}

Decisioning Studio Proには、BrazeのフォワードデプロイドデータサイエンスチームによるAI意思決定サービスのサポートが含まれています。これにより、ビジネス成果を最大化するためのエージェントの設計と設定を支援します。詳細については、[Decisioning Studio GoとDecisioning Studio Proの比較]({{site.baseurl}}/user_guide/brazeai/decisioning_studio#decisioning-studio-go-vs-decisioning-studio-pro)を参照してください。